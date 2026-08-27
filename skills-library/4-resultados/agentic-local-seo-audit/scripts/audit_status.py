#!/usr/bin/env python3
"""
audit_status.py — Audit Progress Tracker
Local Business SEO Audit System

Scans the project directory to determine which audit phases are complete,
shows progress statistics, and indicates what to run next.

Usage:
    python3 scripts/audit_status.py
    python3 scripts/audit_status.py --project projects/acme-plumbing
    python3 scripts/audit_status.py --project projects/acme-plumbing --json
"""

import argparse
import json
import os
import sys
from pathlib import Path
from datetime import datetime


# Canonical audit phase definitions
PHASES = [
    {"num":  0,  "id": "intake",             "name": "Information Gathering",            "file": "intake-data.md",            "required": True},
    {"num":  1,  "id": "competitors",        "name": "Competitor Deep Analysis",         "file": "competitor-profiles.md",    "required": True},
    {"num":  2,  "id": "technical",          "name": "Technical SEO",                    "file": "technical-findings.md",     "required": True},
    {"num":  3,  "id": "onpage",             "name": "On-Page SEO",                      "file": "onpage-findings.md",        "required": True},
    {"num":  4,  "id": "content",            "name": "Content Audit",                    "file": "content-inventory.md",      "required": True},
    {"num":  5,  "id": "content-gaps",       "name": "Content Gap Analysis",             "file": "content-gaps.md",           "required": True},
    {"num":  6,  "id": "keywords",           "name": "Keyword Gap Analysis",             "file": "keyword-gaps.md",           "required": True},
    {"num":  7,  "id": "topical-gaps",       "name": "Topical Gap Analysis",             "file": "topical-gaps.md",           "required": True},
    {"num":  8,  "id": "authority",          "name": "Topical Authority",                "file": "topical-authority.md",      "required": False},
    {"num":  9,  "id": "entities",           "name": "Entity Audit",                     "file": "entity-findings.md",        "required": False},
    {"num": 10,  "id": "speed",              "name": "Core Web Vitals & Speed",          "file": "speed-findings.md",         "required": True},
    {"num": 11,  "id": "local",              "name": "Local SEO",                        "file": "local-findings.md",         "required": True},
    {"num": 12,  "id": "backlinks",          "name": "Backlink & Link Profile",          "file": "backlink-findings.md",      "required": True},
    {"num": 13,  "id": "social",             "name": "Social Media",                     "file": "social-findings.md",        "required": False},
    {"num": 14,  "id": "ai-seo",             "name": "AI Visibility & AI SEO",           "file": "ai-seo-findings.md",        "required": True},
    {"num": 15,  "id": "reputation",         "name": "Reputation & Reviews",             "file": "reputation-findings.md",    "required": True},
    {"num": 16,  "id": "brand-serp",         "name": "Brand SERP & Knowledge Panel",     "file": "brand-serp-findings.md",    "required": False},
    {"num": 17,  "id": "cro",               "name": "UX & CRO",                         "file": "cro-findings.md",           "required": False},
    {"num": 18,  "id": "voice",              "name": "Voice Search",                     "file": "voice-findings.md",         "required": False},
    {"num": 19,  "id": "accessibility",      "name": "Accessibility",                    "file": "accessibility-findings.md", "required": False},
    {"num": 20,  "id": "penalty",            "name": "Penalty Check",                    "file": "penalty-findings.md",       "required": True},
    {"num": 21,  "id": "multi-location",     "name": "Multi-Location SEO",               "file": "multi-location-findings.md","required": False},
]

SCORING_PHASES = [
    {"id": "local-impact",  "name": "LOCAL-IMPACT Score",  "file": "local-impact-scores.md"},
    {"id": "serp-trust",    "name": "SERP-TRUST Score",    "file": "serp-trust-scores.md"},
    {"id": "master-report", "name": "Master Report",       "file": "master-report.md"},
]


def find_project_dir(base: str = ".") -> Path | None:
    """Find the most recently modified project directory."""
    projects = Path(base) / "projects"
    if not projects.exists():
        return None

    dirs = [d for d in projects.iterdir() if d.is_dir() and not d.name.startswith(".")]
    if not dirs:
        return None

    # Return most recently modified
    return max(dirs, key=lambda d: d.stat().st_mtime)


def check_phase(audit_dir: Path, reports_dir: Path, phase: dict) -> dict:
    """Check if a phase is complete (finding file exists + has content)."""
    finding_file = audit_dir / phase["file"]
    report_pdf   = reports_dir / f"phase-{phase['num']}-{phase['id']}.pdf"
    report_html  = reports_dir / f"phase-{phase['num']}-{phase['id']}.html"

    finding_exists = finding_file.exists() and finding_file.stat().st_size > 100
    pdf_exists     = report_pdf.exists()
    html_exists    = report_html.exists()

    status = "complete" if finding_exists else "pending"

    modified = None
    if finding_exists:
        modified = datetime.fromtimestamp(finding_file.stat().st_mtime).strftime("%Y-%m-%d %H:%M")

    return {
        "phase_num":       phase["num"],
        "phase_id":        phase["id"],
        "phase_name":      phase["name"],
        "required":        phase["required"],
        "status":          status,
        "finding_file":    str(finding_file),
        "finding_exists":  finding_exists,
        "pdf_exists":      pdf_exists,
        "html_exists":     html_exists,
        "last_modified":   modified,
    }


def generate_status_report(project_dir: Path) -> dict:
    """Generate a full status report for the given project directory."""
    audit_dir   = project_dir / "audit"
    reports_dir = project_dir / "reports"

    # Load project metadata
    meta = {}
    meta_path = project_dir / "project.json"
    if meta_path.exists():
        try:
            meta = json.loads(meta_path.read_text())
        except Exception:
            pass

    phase_results = [check_phase(audit_dir, reports_dir, p) for p in PHASES]

    completed      = [p for p in phase_results if p["status"] == "complete"]
    pending        = [p for p in phase_results if p["status"] == "pending"]
    req_completed  = [p for p in completed if p["required"]]
    req_total      = [p for p in phase_results if p["required"]]

    # Check scoring phases
    scoring_results = []
    for sp in SCORING_PHASES:
        f = audit_dir / sp["file"]
        scoring_results.append({
            "id":      sp["id"],
            "name":    sp["name"],
            "status":  "complete" if f.exists() and f.stat().st_size > 50 else "pending",
            "file":    str(f),
        })

    # Report PDFs
    pdf_count = len(list(reports_dir.glob("*.pdf"))) if reports_dir.exists() else 0

    # Next recommended phase
    next_phase = None
    for p in pending:
        if p["required"]:
            next_phase = p
            break
    if not next_phase and pending:
        next_phase = pending[0]

    return {
        "project_dir":      str(project_dir),
        "business_name":    meta.get("business_name", "Unknown"),
        "website_url":      meta.get("website_url", "Unknown"),
        "audit_started":    meta.get("audit_started", "Unknown"),
        "phases":           phase_results,
        "scoring":          scoring_results,
        "pdf_count":        pdf_count,
        "total_phases":     len(PHASES),
        "completed_count":  len(completed),
        "pending_count":    len(pending),
        "required_done":    len(req_completed),
        "required_total":   len(req_total),
        "pct_complete":     round(len(completed) / len(PHASES) * 100),
        "next_phase":       next_phase,
    }


def print_status(report: dict):
    """Print a human-readable status report."""
    print("━" * 55)
    print(f" AUDIT STATUS — {report['business_name']}")
    print(f" URL: {report['website_url']}")
    print(f" Started: {report['audit_started']}")
    print("━" * 55)
    print(f" Progress: {report['completed_count']}/{report['total_phases']} phases ({report['pct_complete']}%)")
    print(f" Required: {report['required_done']}/{report['required_total']} critical phases")
    print(f" PDFs generated: {report['pdf_count']}")
    print("━" * 55)
    print()

    # Phase grid
    print(" PHASE STATUS:")
    for p in report["phases"]:
        icon     = "✅" if p["status"] == "complete" else "⬜"
        req_flag = " [required]" if p["required"] else ""
        pdf_flag = " 📄" if p["pdf_exists"] else ""
        modified = f"  ({p['last_modified']})" if p["last_modified"] else ""
        print(f"  {icon} Phase {p['phase_num']:>2}: {p['phase_name']}{pdf_flag}{req_flag}{modified}")

    print()
    print(" SCORING & OUTPUT:")
    for s in report["scoring"]:
        icon = "✅" if s["status"] == "complete" else "⬜"
        print(f"  {icon} {s['name']}")

    if report["next_phase"]:
        np = report["next_phase"]
        print()
        print(f" NEXT RECOMMENDED: Phase {np['phase_num']} — {np['phase_name']}")
        print(f"  Run: /audit-{np['phase_id']}")

    print("━" * 55)


def main():
    parser = argparse.ArgumentParser(description="Show audit progress status.")
    parser.add_argument("--project", default=None, help="Project directory path")
    parser.add_argument("--base",    default=".",  help="Base directory (default: current)")
    parser.add_argument("--json",    action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.project:
        project_dir = Path(args.project)
        if not project_dir.exists():
            print(f"ERROR: Project directory not found: {args.project}", file=sys.stderr)
            print(f"Create it first with: python3 scripts/setup_project.py --name \"Business Name\" --url \"https://...\" --location \"City, ST\"", file=sys.stderr)
            sys.exit(1)
        audit_dir = project_dir / "audit"
        if not audit_dir.exists():
            print(f"ERROR: Project exists but has no audit/ directory: {args.project}", file=sys.stderr)
            print(f"Re-run: python3 scripts/setup_project.py --name \"Business Name\" --url \"https://...\" --location \"City, ST\"", file=sys.stderr)
            sys.exit(1)
    else:
        project_dir = find_project_dir(args.base)
        if not project_dir:
            print("No project directory found under projects/.", file=sys.stderr)
            print("Create one first: python3 scripts/setup_project.py --name \"Business Name\" --url \"https://...\" --location \"City, ST\"", file=sys.stderr)
            sys.exit(1)

    report = generate_status_report(project_dir)

    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print_status(report)


if __name__ == "__main__":
    main()
