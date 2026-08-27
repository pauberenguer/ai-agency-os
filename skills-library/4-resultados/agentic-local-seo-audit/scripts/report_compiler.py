#!/usr/bin/env python3
"""
report_compiler.py — Master Audit Report Compiler
Local Business SEO Audit System

Reads all phase audit markdown files from the project's audit/ directory,
extracts scores, issues, and findings, and compiles a structured master report
data structure that can be used by the PDF generator.

Usage:
    python3 scripts/report_compiler.py --project projects/acme-plumbing
    python3 scripts/report_compiler.py --project projects/acme-plumbing --json
    python3 scripts/report_compiler.py --project projects/acme-plumbing --output audit/master-report.md
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path


PHASE_FILES = {
    0:  "intake-data.md",
    1:  "competitor-profiles.md",
    2:  "technical-findings.md",
    3:  "onpage-findings.md",
    4:  "content-inventory.md",
    5:  "content-gaps.md",
    6:  "keyword-gaps.md",
    7:  "topical-gaps.md",
    8:  "topical-authority.md",
    9:  "entity-findings.md",
    10: "speed-findings.md",
    11: "local-findings.md",
    12: "backlink-findings.md",
    13: "social-findings.md",
    14: "ai-seo-findings.md",
    15: "reputation-findings.md",
    16: "brand-serp-findings.md",
    17: "cro-findings.md",
    18: "voice-findings.md",
    19: "accessibility-findings.md",
    20: "penalty-findings.md",
    21: "multi-location-findings.md",
}

PHASE_NAMES = {
    0: "Information Gathering",
    1: "Competitor Deep Analysis",
    2: "Technical SEO",
    3: "On-Page SEO",
    4: "Content Audit",
    5: "Content Gap Analysis",
    6: "Keyword Gap Analysis",
    7: "Topical Gap Analysis",
    8: "Topical Authority",
    9: "Entity Audit",
    10: "Core Web Vitals & Speed",
    11: "Local SEO",
    12: "Backlink & Link Profile",
    13: "Social Media",
    14: "AI Visibility & AI SEO",
    15: "Reputation & Reviews",
    16: "Brand SERP & Knowledge Panel",
    17: "UX & CRO",
    18: "Voice Search",
    19: "Accessibility",
    20: "Penalty Check",
    21: "Multi-Location SEO",
}


def extract_score(content: str) -> int | None:
    """Extract SCORE from a phase finding file."""
    patterns = [
        r'SCORE[:\s]+(\d+)/100',
        r'score[:\s]+(\d+)',
        r'Score[:\s]+(\d+)/100',
        r'Phase Score[:\s]+(\d+)',
    ]
    for pat in patterns:
        m = re.search(pat, content)
        if m:
            return int(m.group(1))
    return None


def extract_status(content: str) -> str:
    """Extract status from a phase finding file."""
    if "❌ Critical Issues" in content or "CRITICAL ISSUES" in content:
        return "critical"
    elif "⚠️ Needs Attention" in content or "HIGH PRIORITY" in content:
        return "warning"
    elif "✅ Healthy" in content:
        return "healthy"
    return "unknown"


def extract_issues(content: str, severity: str) -> list[str]:
    """Extract issues of a given severity from phase content."""
    patterns = {
        "critical": [
            r'(?i)(?:CRITICAL[:\s-]+|❌\s*)(.{10,200})',
            r'(?i)##\s*Critical Issues?\s*\n(.*?)(?=\n##|\Z)',
        ],
        "high": [
            r'(?i)(?:HIGH PRIORITY[:\s-]+|⚠️\s*)(.{10,200})',
        ],
    }

    issues = []
    for pat in patterns.get(severity, []):
        matches = re.findall(pat, content, re.DOTALL)
        for m in matches:
            # Clean up and truncate
            clean = re.sub(r'\s+', ' ', m.strip())
            if 15 < len(clean) < 300:
                issues.append(clean[:280])
    return issues[:10]  # Cap at 10 per severity per phase


def extract_quick_wins(content: str) -> list[str]:
    """Extract quick wins from phase content."""
    wins = []
    m = re.search(r'(?i)(?:QUICK WINS?|quick wins?)[\s:]*\n(.*?)(?=\n##|\n---|\Z)', content, re.DOTALL)
    if m:
        section = m.group(1)
        for line in section.split("\n"):
            line = line.strip().lstrip("-•*").strip()
            if len(line) > 20:
                wins.append(line[:200])
    return wins[:5]


def parse_phase_file(audit_dir: Path, phase_num: int) -> dict:
    """Parse a phase finding file and extract structured data."""
    filename = PHASE_FILES.get(phase_num)
    if not filename:
        return None

    filepath = audit_dir / filename
    if not filepath.exists():
        return None

    content = filepath.read_text(encoding="utf-8", errors="replace")

    return {
        "phase_num":    phase_num,
        "phase_name":   PHASE_NAMES.get(phase_num, f"Phase {phase_num}"),
        "file":         str(filepath),
        "score":        extract_score(content),
        "status":       extract_status(content),
        "critical":     extract_issues(content, "critical"),
        "high":         extract_issues(content, "high"),
        "quick_wins":   extract_quick_wins(content),
        "word_count":   len(content.split()),
        "char_count":   len(content),
        "present":      True,
    }


def load_meta(project_dir: Path) -> dict:
    """Load project metadata."""
    meta_path = project_dir / "project.json"
    if meta_path.exists():
        try:
            return json.loads(meta_path.read_text())
        except Exception:
            pass
    return {}


def load_scores(audit_dir: Path) -> dict:
    """Load LOCAL-IMPACT and SERP-TRUST score files."""
    scores = {"local_impact": None, "serp_trust": None, "seo_health_index": None}

    li_file = audit_dir / "local-impact-scores.md"
    st_file = audit_dir / "serp-trust-scores.md"

    if li_file.exists():
        content = li_file.read_text()
        m = re.search(r'overall[:\s]+(\d+(?:\.\d+)?)', content, re.IGNORECASE)
        if m:
            scores["local_impact"] = float(m.group(1))

    if st_file.exists():
        content = st_file.read_text()
        m = re.search(r'overall[:\s]+(\d+(?:\.\d+)?)', content, re.IGNORECASE)
        if m:
            scores["serp_trust"] = float(m.group(1))

    if scores["local_impact"] and scores["serp_trust"]:
        scores["seo_health_index"] = round(
            scores["local_impact"] * 0.55 + scores["serp_trust"] * 0.45, 1
        )

    return scores


def compute_overall_score(phase_scores: list[int | None]) -> int:
    """Compute the overall site health score as the average of available phase scores."""
    valid = [s for s in phase_scores if s is not None]
    return round(sum(valid) / len(valid)) if valid else 0


def compile_report(project_dir: Path) -> dict:
    """Compile the full master report data structure."""
    audit_dir   = project_dir / "audit"
    reports_dir = project_dir / "reports"
    meta        = load_meta(project_dir)
    scores      = load_scores(audit_dir)

    phases = []
    all_critical = []
    all_high     = []
    all_quick_wins = []
    phase_scores = []

    for num in sorted(PHASE_FILES.keys()):
        phase = parse_phase_file(audit_dir, num)
        if phase:
            phases.append(phase)
            if phase["score"]:
                phase_scores.append(phase["score"])
            all_critical.extend([{"phase": phase["phase_name"], "issue": i} for i in phase["critical"]])
            all_high.extend([{"phase": phase["phase_name"], "issue": i} for i in phase["high"]])
            all_quick_wins.extend(phase["quick_wins"])

    overall_score = compute_overall_score(phase_scores)

    report = {
        "compiled_at":        datetime.now().isoformat(),
        "business_name":      meta.get("business_name", "Unknown Business"),
        "website_url":        meta.get("website_url", ""),
        "location":           meta.get("location", ""),
        "audit_started":      meta.get("audit_started", ""),
        "project_dir":        str(project_dir),
        "overall_score":      overall_score,
        "local_impact_score": scores["local_impact"],
        "serp_trust_score":   scores["serp_trust"],
        "seo_health_index":   scores["seo_health_index"],
        "phases_completed":   len(phases),
        "phases_total":       len(PHASE_FILES),
        "phases":             phases,
        "all_critical_issues": all_critical,
        "all_high_issues":    all_high,
        "all_quick_wins":     list(dict.fromkeys(all_quick_wins))[:15],  # dedupe, cap 15
        "pdf_count":          len(list(reports_dir.glob("*.pdf"))) if reports_dir.exists() else 0,
    }

    return report


def write_master_report_md(report: dict, output_path: Path):
    """Write a structured master-report.md from compiled data."""
    lines = [
        f"---",
        f"skill: report-generation",
        f"phase: master",
        f"date: {datetime.now().strftime('%Y-%m-%d')}",
        f"business: {report['business_name']}",
        f"url: {report['website_url']}",
        f"score: {report['overall_score']}",
        f"status: compiled",
        f"---",
        f"",
        f"# Master SEO Audit Report",
        f"**Business:** {report['business_name']}",
        f"**URL:** {report['website_url']}",
        f"**Location:** {report['location']}",
        f"**Compiled:** {report['compiled_at'][:10]}",
        f"",
        f"## Overall Scores",
        f"- **Site Health Score:** {report['overall_score']}/100",
        f"- **LOCAL-IMPACT Score:** {report['local_impact_score'] or 'Not run'}/100",
        f"- **SERP-TRUST Score:** {report['serp_trust_score'] or 'Not run'}/100",
        f"- **SEO Health Index:** {report['seo_health_index'] or 'Not computed'}/100",
        f"",
        f"## Critical Issues ({len(report['all_critical_issues'])} found)",
    ]

    for item in report["all_critical_issues"][:20]:
        lines.append(f"- **[{item['phase']}]** {item['issue']}")

    lines.extend([
        f"",
        f"## High Priority Issues ({len(report['all_high_issues'])} found)",
    ])

    for item in report["all_high_issues"][:20]:
        lines.append(f"- **[{item['phase']}]** {item['issue']}")

    lines.extend([
        f"",
        f"## Quick Wins ({len(report['all_quick_wins'])} identified)",
    ])

    for win in report["all_quick_wins"]:
        lines.append(f"- {win}")

    lines.extend([
        f"",
        f"## Phase Scores",
        f"| Phase | Name | Score | Status |",
        f"|-------|------|-------|--------|",
    ])

    for p in report["phases"]:
        score = f"{p['score']}/100" if p["score"] else "N/A"
        lines.append(f"| {p['phase_num']} | {p['phase_name']} | {score} | {p['status']} |")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Master report written: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Compile master audit report from phase findings.")
    parser.add_argument("--project", required=True, help="Project directory path")
    parser.add_argument("--output",  default=None,  help="Output markdown file (default: {project}/audit/master-report.md)")
    parser.add_argument("--json",    action="store_true", help="Print compiled data as JSON")

    args = parser.parse_args()

    project_dir = Path(args.project)
    if not project_dir.exists():
        print(f"ERROR: Project directory not found: {args.project}", file=sys.stderr)
        sys.exit(1)

    report = compile_report(project_dir)

    if args.json:
        print(json.dumps(report, indent=2, default=str))
        return

    # Default output
    output_path = Path(args.output) if args.output else project_dir / "audit" / "master-report.md"
    write_master_report_md(report, output_path)

    # Print summary
    print(f"\nReport Summary:")
    print(f"  Business:    {report['business_name']}")
    print(f"  Overall:     {report['overall_score']}/100")
    print(f"  Phases done: {report['phases_completed']}/{report['phases_total']}")
    print(f"  Critical:    {len(report['all_critical_issues'])} issues")
    print(f"  Quick wins:  {len(report['all_quick_wins'])}")
    print(f"  PDFs:        {report['pdf_count']}")


if __name__ == "__main__":
    main()
