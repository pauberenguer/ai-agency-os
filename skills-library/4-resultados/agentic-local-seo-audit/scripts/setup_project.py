#!/usr/bin/env python3
"""
setup_project.py — Project Directory Setup
Local Business SEO Audit System

Creates a structured project directory under projects/[business-slug]/
based on the business name or domain. Called at the start of every audit.

Usage:
    python3 scripts/setup_project.py --name "Acme Plumbing" --url "https://acmeplumbing.com"
    python3 scripts/setup_project.py --name "Smith Law Firm" --url "https://smith-law.com" --location "Chicago, IL"

Output:
    Prints the project slug and absolute paths for all subdirectories.
    Creates the directory structure if it doesn't exist.
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


def slugify(text: str) -> str:
    """Convert a string to a URL-safe slug."""
    text = text.lower().strip()
    # Remove protocol and www from URLs
    text = re.sub(r'^https?://(www\.)?', '', text)
    # Remove trailing slashes and paths
    text = text.split('/')[0]
    # Replace dots with hyphens for domain names
    text = text.replace('.', '-')
    # Replace non-alphanumeric chars with hyphens
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Collapse multiple hyphens
    text = re.sub(r'-+', '-', text)
    # Strip leading/trailing hyphens
    text = text.strip('-')
    return text


def get_domain_slug(url: str) -> str:
    """Extract and slugify the domain from a URL."""
    try:
        parsed = urlparse(url if url.startswith('http') else f'https://{url}')
        domain = parsed.netloc or parsed.path
        domain = re.sub(r'^www\.', '', domain)
        return slugify(domain)
    except Exception:
        return None


def resolve_slug(name: str, url: str) -> str:
    """
    Determine the best project slug.
    Priority: business name slug (primary), domain slug (fallback).
    """
    name_slug = slugify(name) if name else None
    domain_slug = get_domain_slug(url) if url else None

    if name_slug and len(name_slug) >= 3:
        return name_slug
    elif domain_slug:
        return domain_slug
    else:
        return f"audit-{datetime.now().strftime('%Y%m%d-%H%M%S')}"


def create_project_structure(base_dir: Path, slug: str) -> dict:
    """
    Create the full project directory structure and return paths.

    Structure:
        projects/
          {slug}/
            audit/        — Markdown findings files (one per phase)
            reports/      — HTML + PDF reports (one per phase)
            data/         — Raw data, screenshots, CSVs, logs
            data/crawl/   — Site crawl output
            data/serp/    — SERP snapshot data
            data/scores/  — Scoring framework YAML data
    """
    project_root = base_dir / "projects" / slug

    subdirs = {
        "project_root": project_root,
        "audit":        project_root / "audit",
        "reports":      project_root / "reports",
        "data":         project_root / "data",
        "data_crawl":   project_root / "data" / "crawl",
        "data_serp":    project_root / "data" / "serp",
        "data_scores":  project_root / "data" / "scores",
    }

    for key, path in subdirs.items():
        path.mkdir(parents=True, exist_ok=True)

    return {k: str(v) for k, v in subdirs.items()}


def write_project_meta(paths: dict, name: str, url: str, slug: str,
                        location: str = None) -> str:
    """Write project metadata file to the project root."""
    meta = {
        "business_name": name,
        "website_url":   url,
        "slug":          slug,
        "location":      location or "",
        "created_at":    datetime.now().isoformat(),
        "audit_started": datetime.now().strftime("%Y-%m-%d"),
        "phases_completed": [],
        "paths": paths,
    }

    meta_path = Path(paths["project_root"]) / "project.json"

    # Merge with existing meta if it exists (don't overwrite completed phases)
    if meta_path.exists():
        try:
            existing = json.loads(meta_path.read_text())
            meta["phases_completed"] = existing.get("phases_completed", [])
            meta["created_at"] = existing.get("created_at", meta["created_at"])
        except Exception:
            pass

    meta_path.write_text(json.dumps(meta, indent=2))
    return str(meta_path)


def main():
    parser = argparse.ArgumentParser(
        description="Set up a new SEO audit project directory."
    )
    parser.add_argument("--name",     required=True, help="Business name")
    parser.add_argument("--url",      required=True, help="Website URL (https://...)")
    parser.add_argument("--location", default="",    help="Target location (City, State)")
    parser.add_argument("--base",     default=".",   help="Base directory (default: current dir)")
    parser.add_argument("--json",     action="store_true", help="Output as JSON")

    args = parser.parse_args()

    base_dir = Path(args.base).resolve()
    slug = resolve_slug(args.name, args.url)
    paths = create_project_structure(base_dir, slug)
    meta_path = write_project_meta(paths, args.name, args.url, slug, args.location)

    if args.json:
        print(json.dumps({
            "slug":        slug,
            "paths":       paths,
            "meta_file":   meta_path,
        }, indent=2))
    else:
        print(f"Project slug:     {slug}")
        print(f"Project root:     {paths['project_root']}")
        print(f"Audit directory:  {paths['audit']}")
        print(f"Reports directory:{paths['reports']}")
        print(f"Data directory:   {paths['data']}")
        print(f"Meta file:        {meta_path}")
        print(f"\nSET PROJECT PATHS:")
        print(f"  PROJECT_SLUG={slug}")
        print(f"  PROJECT_DIR={paths['project_root']}")
        print(f"  AUDIT_DIR={paths['audit']}")
        print(f"  REPORTS_DIR={paths['reports']}")
        print(f"  DATA_DIR={paths['data']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
