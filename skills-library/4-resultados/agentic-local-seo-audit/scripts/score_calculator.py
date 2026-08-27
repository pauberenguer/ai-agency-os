#!/usr/bin/env python3
"""
score_calculator.py — LOCAL-IMPACT & SERP-TRUST Score Calculator
Local Business SEO Audit System

Reads raw scoring data (YAML blocks from audit/*.md files) and computes:
  - LOCAL-IMPACT final score (60 items, 0-3 scale, 8 dimensions)
  - SERP-TRUST final score (50 items, 0-4 scale, 5 dimensions)
  - SEO Health Index: (LOCAL-IMPACT × 0.55) + (SERP-TRUST × 0.45)
  - Grade assignments (A+ to F)
  - Veto checks and score caps
  - Competitor position rankings

Usage:
    python3 scripts/score_calculator.py --framework local-impact --data audit/local-impact-scores.md
    python3 scripts/score_calculator.py --framework serp-trust --data audit/serp-trust-scores.md
    python3 scripts/score_calculator.py --both \
        --local-impact audit/local-impact-scores.md \
        --serp-trust audit/serp-trust-scores.md
    python3 scripts/score_calculator.py --both --local-impact data/li.md --serp-trust data/st.md --json
"""

import argparse
import json
import re
import sys
from pathlib import Path


# Grade thresholds
GRADE_THRESHOLDS = [
    (97, "A+"), (93, "A"), (90, "A-"),
    (87, "B+"), (83, "B"), (80, "B-"),
    (77, "C+"), (73, "C"), (70, "C-"),
    (67, "D+"), (63, "D"), (60, "D-"),
    (0,  "F"),
]

# LOCAL-IMPACT dimensions
LOCAL_IMPACT_DIMENSIONS = {
    "L":  {"name": "Listing Quality",       "items": 10, "max": 30},
    "O":  {"name": "Online Reviews",         "items": 10, "max": 30},
    "C":  {"name": "Citation Consistency",   "items": 10, "max": 30},
    "A":  {"name": "Authority Signals",      "items": 10, "max": 30},
    "L2": {"name": "Local Content",          "items":  5, "max": 15},
    "I":  {"name": "Integrated Visibility",  "items":  5, "max": 15},
    "P":  {"name": "Performance",            "items":  5, "max": 15},
    "T":  {"name": "Tracking",               "items":  5, "max": 15},
}
LOCAL_IMPACT_MAX_RAW = 180  # 60 items × 3 max per item

# LOCAL-IMPACT veto conditions
LOCAL_IMPACT_VETOES = [
    {"id": "V01", "label": "GBP not claimed or verified",                          "cap": 15},
    {"id": "V02", "label": "Website not indexed by Google",                        "cap": 10},
    {"id": "V03", "label": "Active Google penalty",                                "cap": 10},
    {"id": "V04", "label": "NAP wrong on website + GBP + majority of citations",  "cap": 20},
    {"id": "V05", "label": "Zero Google reviews",                                  "cap": 25},
    {"id": "V06", "label": "No SSL certificate",                                   "cap": 20},
]

# SERP-TRUST dimensions
SERP_TRUST_DIMENSIONS = {
    "T":  {"name": "Technical Foundation",        "items": 10, "max": 40},
    "R":  {"name": "Ranking Signals",             "items": 10, "max": 40},
    "U":  {"name": "User Experience & Performance","items": 10, "max": 40},
    "S":  {"name": "Search Authority",            "items": 10, "max": 40},
    "T2": {"name": "Trust & AI Readiness",        "items": 10, "max": 40},
}
SERP_TRUST_MAX_RAW = 200  # 50 items × 4 max per item

# SERP-TRUST weights for optional weighted scoring
SERP_TRUST_WEIGHTS = {"T": 0.20, "R": 0.25, "U": 0.20, "S": 0.20, "T2": 0.15}

# SERP-TRUST veto conditions
SERP_TRUST_VETOES = [
    {"id": "V01", "label": "Site not indexed by Google",       "cap": 10},
    {"id": "V02", "label": "Active manual penalty in GSC",     "cap": 15},
    {"id": "V03", "label": "No HTTPS / expired SSL",           "cap": 25},
    {"id": "V04", "label": "LCP > 6s on mobile",              "cap": 30},
    {"id": "V05", "label": "Cloaked / hidden content served",  "cap": 10},
    {"id": "V06", "label": ">50% toxic backlinks",             "cap": 20},
    {"id": "V07", "label": "Zero structured data",             "cap": 40},
]

# SEO Health Index weights
SEO_HEALTH_WEIGHTS = {"local_impact": 0.55, "serp_trust": 0.45}


def assign_grade(score: float) -> str:
    for threshold, grade in GRADE_THRESHOLDS:
        if score >= threshold:
            return grade
    return "F"


def progress_bar(pct: float, width: int = 10) -> str:
    """ASCII progress bar."""
    filled = round(pct / 100 * width)
    return "█" * filled + "░" * (width - filled)


def extract_yaml_block(content: str) -> dict:
    """Extract and parse the YAML data block from a markdown file."""
    # Look for ```yaml ... ``` block
    m = re.search(r'```ya?ml\s*\n(.*?)```', content, re.DOTALL | re.IGNORECASE)
    if not m:
        # Try raw YAML at the start (frontmatter style)
        m = re.search(r'^---\s*\n(.*?)---', content, re.DOTALL)
    if not m:
        return {}

    yaml_text = m.group(1)

    try:
        import yaml
        return yaml.safe_load(yaml_text) or {}
    except ImportError:
        # Minimal manual YAML parser for simple key: value structures
        result = {}
        for line in yaml_text.split("\n"):
            m2 = re.match(r'^(\s*)(\w[\w_-]*):\s*(.*)$', line)
            if m2:
                indent = len(m2.group(1))
                key    = m2.group(2)
                val    = m2.group(3).strip()
                if val and indent == 0:
                    # Attempt numeric conversion
                    try:
                        result[key] = int(val)
                    except ValueError:
                        try:
                            result[key] = float(val)
                        except ValueError:
                            result[key] = val.strip('"\'')
        return result
    except Exception:
        return {}


def compute_local_impact(scores: dict) -> dict:
    """
    Compute LOCAL-IMPACT final score from raw dimension scores.

    Input: dict with dimension raw scores under 'dimensions' key.
    Output: complete score report with normalization and veto application.
    """
    dims = scores.get("dimensions", {})
    vetoes_triggered = scores.get("vetoes_triggered", [])

    # Sum raw scores
    raw_total = sum(d.get("raw", 0) for d in dims.values() if isinstance(d, dict))
    if raw_total == 0:
        # Try alternate format: dimensions.L = number
        raw_total = sum(v for k, v in dims.items() if isinstance(v, (int, float)))

    normalized = round((raw_total / LOCAL_IMPACT_MAX_RAW) * 100, 1)

    # Apply veto caps
    effective_cap = 100
    triggered_details = []
    for veto in LOCAL_IMPACT_VETOES:
        if veto["id"] in vetoes_triggered or veto["label"].lower() in [v.lower() for v in vetoes_triggered]:
            effective_cap = min(effective_cap, veto["cap"])
            triggered_details.append(veto)

    final_score = min(normalized, effective_cap)
    grade = assign_grade(final_score)

    # Dimension breakdown
    breakdown = {}
    for code, meta in LOCAL_IMPACT_DIMENSIONS.items():
        dim_data = dims.get(code, {})
        if isinstance(dim_data, dict):
            raw = dim_data.get("raw", 0)
        else:
            raw = float(dim_data) if dim_data else 0
        pct = round((raw / meta["max"]) * 100, 1) if meta["max"] > 0 else 0
        breakdown[code] = {
            "name":   meta["name"],
            "raw":    raw,
            "max":    meta["max"],
            "pct":    pct,
            "bar":    progress_bar(pct),
        }

    return {
        "framework":          "LOCAL-IMPACT",
        "raw_total":          raw_total,
        "max_raw":            LOCAL_IMPACT_MAX_RAW,
        "normalized":         normalized,
        "effective_cap":      effective_cap,
        "final_score":        final_score,
        "grade":              grade,
        "vetoes_triggered":   triggered_details,
        "dimensions":         breakdown,
        "competitors":        scores.get("competitors", []),
    }


def compute_serp_trust(scores: dict) -> dict:
    """
    Compute SERP-TRUST final score from raw dimension scores.

    Input: dict with dimension raw scores under 'dimensions' key.
    Output: complete score report with normalization, veto application, and weighted score.
    """
    dims = scores.get("dimensions", {})
    vetoes_triggered = scores.get("vetoes_triggered", [])

    raw_total = sum(d.get("raw", 0) for d in dims.values() if isinstance(d, dict))
    if raw_total == 0:
        raw_total = sum(v for k, v in dims.items() if isinstance(v, (int, float)))

    normalized = round((raw_total / SERP_TRUST_MAX_RAW) * 100, 1)

    # Weighted score
    weighted = 0.0
    for code, weight in SERP_TRUST_WEIGHTS.items():
        dim_data = dims.get(code, {})
        raw  = dim_data.get("raw", 0) if isinstance(dim_data, dict) else float(dim_data or 0)
        max_ = SERP_TRUST_DIMENSIONS.get(code, {}).get("max", 40)
        pct  = (raw / max_) * 100 if max_ > 0 else 0
        weighted += pct * weight
    weighted = round(weighted, 1)

    # Veto caps
    effective_cap = 100
    triggered_details = []
    for veto in SERP_TRUST_VETOES:
        if veto["id"] in vetoes_triggered or veto["label"].lower() in [v.lower() for v in vetoes_triggered]:
            effective_cap = min(effective_cap, veto["cap"])
            triggered_details.append(veto)

    final_score = min(normalized, effective_cap)
    grade = assign_grade(final_score)

    # Dimension breakdown
    breakdown = {}
    for code, meta in SERP_TRUST_DIMENSIONS.items():
        dim_data = dims.get(code, {})
        raw  = dim_data.get("raw", 0) if isinstance(dim_data, dict) else float(dim_data or 0)
        pct  = round((raw / meta["max"]) * 100, 1) if meta["max"] > 0 else 0
        breakdown[code] = {
            "name":   meta["name"],
            "raw":    raw,
            "max":    meta["max"],
            "pct":    pct,
            "weight": SERP_TRUST_WEIGHTS.get(code, 0),
            "bar":    progress_bar(pct),
        }

    return {
        "framework":          "SERP-TRUST",
        "raw_total":          raw_total,
        "max_raw":            SERP_TRUST_MAX_RAW,
        "normalized":         normalized,
        "weighted":           weighted,
        "effective_cap":      effective_cap,
        "final_score":        final_score,
        "grade":              grade,
        "vetoes_triggered":   triggered_details,
        "dimensions":         breakdown,
        "competitors":        scores.get("competitors", []),
    }


def compute_seo_health_index(local_impact_score: float, serp_trust_score: float) -> dict:
    """Compute the combined SEO Health Index."""
    score = round(
        (local_impact_score * SEO_HEALTH_WEIGHTS["local_impact"]) +
        (serp_trust_score   * SEO_HEALTH_WEIGHTS["serp_trust"]),
        1
    )
    grade = assign_grade(score)

    status = "Excellent" if score >= 80 else \
             "Good"      if score >= 65 else \
             "Fair"      if score >= 50 else \
             "Poor"      if score >= 35 else "Critical"

    return {
        "seo_health_index":      score,
        "grade":                 grade,
        "status":                status,
        "local_impact_score":    local_impact_score,
        "local_impact_weight":   SEO_HEALTH_WEIGHTS["local_impact"],
        "serp_trust_score":      serp_trust_score,
        "serp_trust_weight":     SEO_HEALTH_WEIGHTS["serp_trust"],
    }


def print_local_impact(result: dict):
    """Print LOCAL-IMPACT scorecard to stdout."""
    print("━" * 45)
    print(" LOCAL-IMPACT SCORECARD")
    print(f" Score: {result['final_score']}/100  Grade: {result['grade']}")
    print("━" * 45)
    print(f" Raw: {result['raw_total']}/{result['max_raw']}  Normalized: {result['normalized']}")
    if result["vetoes_triggered"]:
        print(f" ⚠️  Veto cap applied: {result['effective_cap']}")
    print()
    print(" Dimension Breakdown:")
    for code, dim in result["dimensions"].items():
        print(f"  {code:<3} {dim['name']:<22} [{dim['raw']:>2}/{dim['max']}] {dim['bar']} {dim['pct']}%")
    print()
    if result["vetoes_triggered"]:
        print(" Vetoes Triggered:")
        for v in result["vetoes_triggered"]:
            print(f"  ❌ {v['id']}: {v['label']} (cap: {v['cap']})")
    if result["competitors"]:
        print(" Competitor Scores:")
        for comp in result["competitors"]:
            print(f"  {comp.get('name','?')}: {comp.get('score','?')}/100")
    print("━" * 45)


def print_serp_trust(result: dict):
    """Print SERP-TRUST scorecard to stdout."""
    print("━" * 45)
    print(" SERP-TRUST SCORECARD")
    print(f" Score: {result['final_score']}/100  Grade: {result['grade']}")
    print(f" Weighted: {result['weighted']}/100")
    print("━" * 45)
    print(f" Raw: {result['raw_total']}/{result['max_raw']}  Normalized: {result['normalized']}")
    if result["vetoes_triggered"]:
        print(f" ⚠️  Veto cap applied: {result['effective_cap']}")
    print()
    print(" Dimension Breakdown:")
    for code, dim in result["dimensions"].items():
        print(f"  {code:<3} {dim['name']:<26} [{dim['raw']:>2}/{dim['max']}] {dim['bar']} {dim['pct']}%")
    print()
    if result["vetoes_triggered"]:
        print(" Vetoes Triggered:")
        for v in result["vetoes_triggered"]:
            print(f"  ❌ {v['id']}: {v['label']} (cap: {v['cap']})")
    if result["competitors"]:
        print(" Competitor Scores:")
        for comp in result["competitors"]:
            print(f"  {comp.get('name','?')}: {comp.get('score','?')}/100")
    print("━" * 45)


def print_seo_health(result: dict):
    """Print SEO Health Index."""
    print("━" * 45)
    print(" SEO HEALTH INDEX")
    print(f" Score: {result['seo_health_index']}/100  Grade: {result['grade']}")
    print(f" Status: {result['status']}")
    print(f" = LOCAL-IMPACT ({result['local_impact_score']} × {result['local_impact_weight']})")
    print(f" + SERP-TRUST   ({result['serp_trust_score']} × {result['serp_trust_weight']})")
    print("━" * 45)


def load_scores_from_file(filepath: str) -> dict:
    """Load and parse scores from a markdown file."""
    path = Path(filepath)
    if not path.exists():
        print(f"ERROR: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)
    content = path.read_text(encoding="utf-8")
    return extract_yaml_block(content)


def main():
    parser = argparse.ArgumentParser(description="Compute LOCAL-IMPACT and SERP-TRUST scores.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--local-impact", metavar="FILE",
                       help="Path to LOCAL-IMPACT scores markdown file")
    group.add_argument("--serp-trust",   metavar="FILE",
                       help="Path to SERP-TRUST scores markdown file")
    group.add_argument("--both",         action="store_true",
                       help="Compute both frameworks and SEO Health Index")

    parser.add_argument("--li-file",     metavar="FILE", required=False,
                        help="LOCAL-IMPACT file path (required with --both), e.g. projects/slug/audit/local-impact-scores.md")
    parser.add_argument("--st-file",     metavar="FILE", required=False,
                        help="SERP-TRUST file path (required with --both), e.g. projects/slug/audit/serp-trust-scores.md")
    parser.add_argument("--json",        action="store_true", help="Output as JSON")

    args = parser.parse_args()

    output = {}

    if args.local_impact:
        raw = load_scores_from_file(args.local_impact)
        result = compute_local_impact(raw)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_local_impact(result)

    elif args.serp_trust:
        raw = load_scores_from_file(args.serp_trust)
        result = compute_serp_trust(raw)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_serp_trust(result)

    elif args.both:
        if not args.li_file or not args.st_file:
            parser.error("--both requires --li-file and --st-file (e.g. projects/slug/audit/local-impact-scores.md)")
        li_raw = load_scores_from_file(args.li_file)
        st_raw = load_scores_from_file(args.st_file)

        li_result = compute_local_impact(li_raw)
        st_result = compute_serp_trust(st_raw)
        hi_result = compute_seo_health_index(li_result["final_score"], st_result["final_score"])

        if args.json:
            print(json.dumps({
                "local_impact":     li_result,
                "serp_trust":       st_result,
                "seo_health_index": hi_result,
            }, indent=2))
        else:
            print_local_impact(li_result)
            print()
            print_serp_trust(st_result)
            print()
            print_seo_health(hi_result)


if __name__ == "__main__":
    main()
