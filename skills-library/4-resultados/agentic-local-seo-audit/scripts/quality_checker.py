#!/usr/bin/env python3
"""
quality_checker.py — SEO Skill Quality Scorer
The val_bpb equivalent for the SEO-AutoImprove loop.

Scores any SKILL.md file on 5 dimensions (0-20 each = 100 total):
  1. Completeness   — required sections present?
  2. Specificity    — concrete tools/thresholds vs generic advice?
  3. Recency        — 2025/2026 SEO signals referenced?
  4. Actionability  — numbered steps, effort estimates, priority scores?
  5. Output Protocol — {AUDIT_DIR} paths, output filename declared?

Usage:
  python3 scripts/quality_checker.py --skill audit/technical-seo/SKILL.md
  python3 scripts/quality_checker.py --all
  python3 scripts/quality_checker.py --skill [path] --json
  python3 scripts/quality_checker.py --all --json
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ─── Constants ────────────────────────────────────────────────────────────────

SKILL_DIRS = [
    "cross-cutting/seo-audit-identity",
    "cross-cutting/local-impact-auditor",
    "cross-cutting/serp-trust-auditor",
    "research/audit-intake",
    "research/competitor-analysis",
    "research/keyword-gaps",
    "research/content-gaps",
    "research/topical-gaps",
    "audit/technical-seo",
    "audit/onpage-seo",
    "audit/content-audit",
    "audit/ai-content-audit",
    "audit/speed-optimization",
    "audit/penalty-check",
    "audit/accessibility-audit",
    "local/local-seo",
    "local/entity-audit",
    "local/multi-location-seo",
    "local/reputation-audit",
    "local/brand-serp",
    "ai-visibility/ai-seo",
    "ai-visibility/voice-search",
    "strategy/topical-authority",
    "strategy/backlink-audit",
    "strategy/social-media-audit",
    "strategy/ux-cro-audit",
    "output/report-generation",
    "output/pdf-report",
]

# ─── Scoring Dimensions ────────────────────────────────────────────────────────

def score_completeness(content: str) -> tuple[int, list[str]]:
    """
    Dimension 1: Completeness (0-20)
    Checks for required structural sections in a SKILL.md file.
    """
    score = 0
    notes = []
    checks = [
        (r"##\s+Step\s+\d+|##\s+Section\s+\d+|##\s+Phase|##\s+STEP",
         4, "Has numbered steps/sections"),
        (r"##.*output|##.*findings|##.*deliverable|write.*to.*AUDIT_DIR|{AUDIT_DIR}",
         4, "Declares output/findings section"),
        (r"##.*competitor|competitor\s+context|vs\.?\s+competitor|competitor\s+comparison",
         3, "Has competitor context section"),
        (r"##.*scoring|##.*score|##.*priority|impact.*feasibility|priority\s+score",
         3, "Has scoring/priority section"),
        (r"##.*recommendation|##.*action|##.*fix|##.*quick.win",
         3, "Has recommendations/actions section"),
        (r"##.*summary|##.*executive|##.*overview|phase.*complete",
         3, "Has summary/executive section"),
    ]
    for pattern, pts, label in checks:
        if re.search(pattern, content, re.IGNORECASE):
            score += pts
        else:
            notes.append(f"Missing: {label}")
    return min(score, 20), notes


def score_specificity(content: str) -> tuple[int, list[str]]:
    """
    Dimension 2: Specificity (0-20)
    Checks for concrete tools, thresholds, URLs vs generic advice.
    """
    score = 0
    notes = []

    # Concrete threshold values (numbers with units)
    threshold_patterns = [
        r"\d+\s*ms",           # milliseconds
        r"\d+\s*KB|MB",        # file sizes
        r"\d+\s*chars?",       # character counts
        r"\d+\/100",           # scores
        r"<\s*\d+\s*ms",       # "< 600ms"
        r"\d+\s*%",            # percentages
        r"\d+\s*seconds?",     # seconds
        r"\d+\s*words?",       # word counts
        r"0\.\d+",             # decimal metrics (e.g. 0.1)
    ]
    threshold_matches = sum(
        1 for p in threshold_patterns if re.search(p, content, re.IGNORECASE)
    )
    if threshold_matches >= 4:
        score += 6
    elif threshold_matches >= 2:
        score += 3
        notes.append("Few specific thresholds/numbers — add more concrete metrics")
    else:
        notes.append("Missing specific thresholds/metrics (e.g. '<600ms', '50-60 chars', '2,000+ words')")

    # Named tools and platforms
    tools = [
        "rank math", "ahrefs", "semrush", "screaming frog", "google search console",
        "gsc", "ga4", "google analytics", "pagespeed", "gtmetrix", "lighthouse",
        "chrome", "litespeed", "cloudflare", "json-ld", "schema.org",
        "google business profile", "gbp", "tripadvisor", "trustpilot",
        "majestic", "moz", "brightlocal", "whitespark", "dataforseo",
        "perplexity", "chatgpt", "gemini", "copilot",
    ]
    tool_count = sum(1 for t in tools if t.lower() in content.lower())
    if tool_count >= 5:
        score += 6
    elif tool_count >= 2:
        score += 3
        notes.append("Reference more specific tools (Rank Math, Ahrefs, GSC, etc.)")
    else:
        notes.append("No specific tools named — very generic")

    # Concrete examples (e.g., sample text, code snippets, URLs)
    if re.search(r"```|`[^`]+`|\[example\]|e\.g\.|for example|such as", content, re.IGNORECASE):
        score += 4
    else:
        notes.append("No concrete examples, code snippets, or sample text")

    # Competitor-specific language
    if re.search(r"competitor\s+\d|top\s+\d|rank\s+#\d|position\s+\d", content, re.IGNORECASE):
        score += 4
    else:
        notes.append("Add rank-specific competitor benchmarks (e.g. 'vs. top-3 competitors')")

    return min(score, 20), notes


def score_recency(content: str) -> tuple[int, list[str]]:
    """
    Dimension 3: Recency (0-20)
    Checks for 2025/2026 SEO signals and current best practices.
    """
    score = 0
    notes = []

    # Year references
    year_refs = len(re.findall(r"202[5-6]", content))
    if year_refs >= 3:
        score += 5
    elif year_refs >= 1:
        score += 2
        notes.append("Add more 2025/2026 year references to signal recency")
    else:
        notes.append("No 2025/2026 references — skill may appear outdated")

    # Modern AI signals
    ai_signals = [
        "ai overview", "aio", "ai mode", "ai search", "geo ", "generative engine",
        "llm seo", "llm visibility", "ai visibility", "ai citation", "chatgpt",
        "perplexity", "gemini", "copilot", "aeo", "answer engine",
        "ai overview", "featured snippet", "people also ask",
    ]
    ai_count = sum(1 for s in ai_signals if s.lower() in content.lower())
    if ai_count >= 4:
        score += 6
    elif ai_count >= 2:
        score += 3
        notes.append("Add more AI search signals (AI Overviews, GEO, AEO, LLM SEO)")
    else:
        notes.append("Missing AI visibility signals — critical for 2025 SEO")

    # Modern technical signals
    modern_tech = [
        "inp", "interaction to next paint", "core web vitals", "cwv",
        "passkeys", "http/3", "http3", "bfcache", "speculation rules",
        "webp", "avif", "lazy load", "lcp", "cls",
        "helpful content", "e-e-a-t", "eeat",
    ]
    tech_count = sum(1 for t in modern_tech if t.lower() in content.lower())
    if tech_count >= 4:
        score += 5
    elif tech_count >= 2:
        score += 2
        notes.append("Add more modern technical signals (INP, EEAT, Helpful Content)")
    else:
        notes.append("Missing modern tech signals (INP replaced FID in 2024, etc.)")

    # Local SEO 2025 signals
    local_signals = [
        "gbp", "google business profile", "review velocity", "q&a",
        "service areas", "data axle", "neustar", "acxiom",
        "apple maps", "bing places", "waze",
    ]
    local_count = sum(1 for l in local_signals if l.lower() in content.lower())
    if local_count >= 3:
        score += 4
    elif local_count >= 1:
        score += 2
        notes.append("Add GBP 2025 features (Q&A, service areas, review velocity)")

    return min(score, 20), notes


def score_actionability(content: str) -> tuple[int, list[str]]:
    """
    Dimension 4: Actionability (0-20)
    Checks for numbered steps, effort estimates, priority scores, timelines.
    """
    score = 0
    notes = []

    # Numbered step lists
    numbered_steps = len(re.findall(r"^\s*\d+\.\s+\S", content, re.MULTILINE))
    if numbered_steps >= 10:
        score += 6
    elif numbered_steps >= 5:
        score += 3
        notes.append("Add more numbered action steps (target 10+)")
    else:
        notes.append("Very few numbered steps — not actionable enough")

    # Effort estimates
    effort_patterns = [
        r"\d+\s*min", r"\d+\s*hour", r"\d+\s*hr",
        r"low\s+effort", r"medium\s+effort", r"high\s+effort",
        r"quick\s+fix", r"week\s+\d", r"month\s+\d",
    ]
    effort_count = sum(1 for p in effort_patterns if re.search(p, content, re.IGNORECASE))
    if effort_count >= 3:
        score += 5
    elif effort_count >= 1:
        score += 2
        notes.append("Add effort estimates (e.g. '30 min', 'Week 1', 'Low effort')")
    else:
        notes.append("Missing effort estimates — users can't prioritize without them")

    # Priority scoring
    priority_patterns = [
        r"impact\s*[×x\*]\s*feasibility", r"priority\s+score",
        r"p-score", r"[🔴🟠🟡🟢]\s+p\d", r"critical.*high.*medium.*low",
        r"high\s+priority", r"🔴.*critical", r"priority\s+matrix",
    ]
    if any(re.search(p, content, re.IGNORECASE) for p in priority_patterns):
        score += 5
    else:
        notes.append("Add priority scoring (Impact × Feasibility matrix or 🔴/🟠/🟡/🟢)")

    # Tables (structured output)
    table_count = content.count("|---|") + content.count("|:---|")
    if table_count >= 3:
        score += 4
    elif table_count >= 1:
        score += 2
        notes.append("Add more structured tables for findings and recommendations")
    else:
        notes.append("No tables — add structured tables for better actionability")

    return min(score, 20), notes


def score_output_protocol(content: str) -> tuple[int, list[str]]:
    """
    Dimension 5: Output Protocol (0-20)
    Checks for correct project path conventions and output file declaration.
    """
    score = 0
    notes = []

    # Uses {AUDIT_DIR} or {REPORTS_DIR} path variables
    if "{AUDIT_DIR}" in content:
        score += 6
    else:
        notes.append("Missing {AUDIT_DIR} path variable — add to output section")

    # Declares specific output filename
    output_file_patterns = [
        r"\{AUDIT_DIR\}/[\w-]+\.md",
        r"projects/\[slug\]/",
        r"intake-data\.md|competitor-profiles\.md|technical-findings\.md|"
        r"onpage-findings\.md|content-inventory\.md|content-gaps\.md|"
        r"keyword-gaps\.md|topical-gaps\.md|topical-authority\.md|"
        r"entity-findings\.md|speed-findings\.md|local-findings\.md|"
        r"backlink-findings\.md|social-findings\.md|ai-seo-findings\.md|"
        r"reputation-findings\.md|brand-serp-findings\.md|cro-findings\.md|"
        r"voice-findings\.md|accessibility-findings\.md|penalty-findings\.md|"
        r"master-report\.md",
    ]
    if any(re.search(p, content, re.IGNORECASE) for p in output_file_patterns):
        score += 5
    else:
        notes.append("Declare exact output filename (e.g. {AUDIT_DIR}/technical-findings.md)")

    # Reads intake-data.md for context
    if "intake-data.md" in content:
        score += 4
    else:
        notes.append("Should read {AUDIT_DIR}/intake-data.md at start for business context")

    # Has YAML frontmatter requirements for output
    if re.search(r"skill:|phase:|score:|status:", content):
        score += 3
    else:
        notes.append("Declare YAML frontmatter for output file (skill, phase, score, status)")

    # References DATA_DIR or REPORTS_DIR
    if "{REPORTS_DIR}" in content or "{DATA_DIR}" in content:
        score += 2
    else:
        notes.append("Consider referencing {REPORTS_DIR} or {DATA_DIR} for PDF/data output")

    return min(score, 20), notes


# ─── Main Scoring Function ─────────────────────────────────────────────────────

def score_skill(skill_path: Path) -> dict:
    """Score a single SKILL.md file and return full result dict."""
    if not skill_path.exists():
        return {"error": f"File not found: {skill_path}"}

    content = skill_path.read_text(encoding="utf-8")
    name = str(skill_path.parent.relative_to(skill_path.parent.parent.parent)) \
           if skill_path.parent.parent.parent.name in ["local-seo-audit", "."] \
           else str(skill_path.parent)

    # Try to get relative path from project root
    try:
        cwd = Path.cwd()
        rel = skill_path.parent.relative_to(cwd)
        name = str(rel)
    except ValueError:
        name = str(skill_path.parent)

    d1_score, d1_notes = score_completeness(content)
    d2_score, d2_notes = score_specificity(content)
    d3_score, d3_notes = score_recency(content)
    d4_score, d4_notes = score_actionability(content)
    d5_score, d5_notes = score_output_protocol(content)

    total = d1_score + d2_score + d3_score + d4_score + d5_score

    grade = (
        "A+" if total >= 97 else "A"  if total >= 93 else "A-" if total >= 90 else
        "B+" if total >= 87 else "B"  if total >= 83 else "B-" if total >= 80 else
        "C+" if total >= 77 else "C"  if total >= 73 else "C-" if total >= 70 else
        "D+" if total >= 67 else "D"  if total >= 63 else "D-" if total >= 60 else "F"
    )

    all_notes = []
    if d1_notes: all_notes.extend([f"[Completeness] {n}" for n in d1_notes])
    if d2_notes: all_notes.extend([f"[Specificity]  {n}" for n in d2_notes])
    if d3_notes: all_notes.extend([f"[Recency]      {n}" for n in d3_notes])
    if d4_notes: all_notes.extend([f"[Actionability]{n}" for n in d4_notes])
    if d5_notes: all_notes.extend([f"[Output]       {n}" for n in d5_notes])

    return {
        "skill": name,
        "path": str(skill_path),
        "total": total,
        "grade": grade,
        "dimensions": {
            "completeness":    {"score": d1_score, "max": 20, "notes": d1_notes},
            "specificity":     {"score": d2_score, "max": 20, "notes": d2_notes},
            "recency":         {"score": d3_score, "max": 20, "notes": d3_notes},
            "actionability":   {"score": d4_score, "max": 20, "notes": d4_notes},
            "output_protocol": {"score": d5_score, "max": 20, "notes": d5_notes},
        },
        "improvement_notes": all_notes,
        "word_count": len(content.split()),
        "line_count": len(content.splitlines()),
    }


def bar(score: int, max_score: int = 20, width: int = 10) -> str:
    """ASCII progress bar."""
    filled = round((score / max_score) * width)
    return "█" * filled + "░" * (width - filled)


def print_skill_report(result: dict) -> None:
    """Pretty-print a single skill score report."""
    if "error" in result:
        print(f"ERROR: {result['error']}")
        return

    total = result["total"]
    grade = result["grade"]
    dims  = result["dimensions"]

    color_total = (
        "\033[92m" if total >= 80 else
        "\033[93m" if total >= 65 else
        "\033[91m"
    )
    reset = "\033[0m"

    print(f"\n{'━'*60}")
    print(f" SKILL QUALITY REPORT")
    print(f" Skill: {result['skill']}")
    print(f"{'━'*60}")
    print(f" Overall Score: {color_total}{total}/100  Grade: {grade}{reset}")
    print(f"{'━'*60}")
    print(f" Dimension Breakdown:")
    for dim_name, dim_data in dims.items():
        s, m = dim_data["score"], dim_data["max"]
        label = dim_name.replace("_", " ").title().ljust(18)
        b = bar(s, m)
        print(f"   {label} {b}  {s:2}/{m}")
    print(f"{'━'*60}")

    notes = result["improvement_notes"]
    if notes:
        print(f" Improvement Opportunities ({len(notes)} found):")
        for note in notes:
            print(f"   ⚠  {note}")
    else:
        print(" No improvement opportunities found — skill is comprehensive.")

    print(f"{'━'*60}")
    print(f" File: {result['path']}")
    print(f" Words: {result['word_count']} | Lines: {result['line_count']}")
    print(f"{'━'*60}\n")


def print_all_report(results: list[dict]) -> None:
    """Print ranking table of all skills."""
    valid = [r for r in results if "error" not in r]
    valid.sort(key=lambda r: r["total"], reverse=True)

    print(f"\n{'━'*70}")
    print(f" SKILL QUALITY RANKING — All {len(valid)} Skills")
    print(f"{'━'*70}")
    print(f" {'#':>2}  {'Score':>5}  {'Grade':>4}  {'Skill':<40}")
    print(f"{'─'*70}")

    for i, r in enumerate(valid, 1):
        score = r["total"]
        grade = r["grade"]
        name  = r["skill"][:40]
        if score >= 80:
            indicator = "✅"
        elif score >= 65:
            indicator = "⚠️ "
        else:
            indicator = "❌"
        print(f" {i:>2}  {score:>5}  {grade:>4}  {indicator}  {name}")

    avg = sum(r["total"] for r in valid) / len(valid) if valid else 0
    print(f"{'─'*70}")
    print(f" Average score: {avg:.1f}/100")
    below_65 = [r for r in valid if r["total"] < 65]
    if below_65:
        print(f" Skills needing improvement: {len(below_65)}")
        for r in below_65:
            print(f"   → {r['skill']} ({r['total']}/100)")
    print(f"{'━'*70}\n")


# ─── CLI Entry Point ───────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Score SKILL.md files for the SEO-AutoImprove loop.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 scripts/quality_checker.py --skill audit/technical-seo/SKILL.md
  python3 scripts/quality_checker.py --all
  python3 scripts/quality_checker.py --skill audit/onpage-seo/SKILL.md --json
  python3 scripts/quality_checker.py --all --json
        """
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--skill", metavar="FILE", help="Path to a single SKILL.md file")
    group.add_argument("--all",   action="store_true", help="Score all 27 skills")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of formatted text")
    args = parser.parse_args()

    # Resolve project root (parent of scripts/)
    scripts_dir = Path(__file__).parent
    project_root = scripts_dir.parent

    if args.skill:
        # Single skill
        skill_path = Path(args.skill)
        if not skill_path.is_absolute():
            # Try relative to cwd first, then project root
            if (Path.cwd() / skill_path).exists():
                skill_path = Path.cwd() / skill_path
            else:
                skill_path = project_root / skill_path

        result = score_skill(skill_path)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_skill_report(result)
        sys.exit(0 if "error" not in result else 1)

    else:
        # All skills
        results = []
        missing = []
        for skill_dir in SKILL_DIRS:
            skill_path = project_root / skill_dir / "SKILL.md"
            if skill_path.exists():
                results.append(score_skill(skill_path))
            else:
                missing.append(skill_dir)

        if missing and not args.json:
            print(f"Warning: {len(missing)} skill files not found:")
            for m in missing:
                print(f"  Missing: {m}/SKILL.md")

        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print_all_report(results)
        sys.exit(0)


if __name__ == "__main__":
    main()
