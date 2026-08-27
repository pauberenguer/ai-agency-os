#!/usr/bin/env python3
"""
site_crawler.py — Technical SEO Site Crawler
Local Business SEO Audit System

Crawls a website to collect technical SEO data: status codes, redirects,
title tags, meta descriptions, H1 tags, canonical URLs, noindex flags,
structured data types, and internal link graph.

Results are saved as CSV and JSON for use by the Technical SEO audit phase.

Usage:
    python3 scripts/site_crawler.py --url https://example.com
    python3 scripts/site_crawler.py --url https://example.com --max-pages 100
    python3 scripts/site_crawler.py --url https://example.com --output projects/acme/data/crawl/
    python3 scripts/site_crawler.py --url https://example.com --max-pages 200 --output projects/acme/data/crawl/ --csv
"""

import argparse
import csv
import json
import re
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from collections import deque
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse, urlunparse


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; LocalSEOCrawler/1.0; "
        "+https://github.com/mshahiddigital/local-seo-audit)"
    ),
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "identity",
    "Connection": "close",
}

CRAWL_DELAY   = 0.5   # seconds between requests
MAX_PAGE_SIZE = 500_000  # bytes (500KB) max to read per page
TIMEOUT       = 15


def normalize_url(url: str) -> str:
    """Normalize a URL: lowercase scheme+host, remove fragment, sort params."""
    parsed = urlparse(url)
    # Remove fragment, keep path/query
    normalized = parsed._replace(
        scheme   = parsed.scheme.lower(),
        netloc   = parsed.netloc.lower(),
        fragment = "",
    )
    return urlunparse(normalized)


def is_same_domain(url: str, base_domain: str) -> bool:
    """Check if a URL belongs to the same domain."""
    parsed = urlparse(url)
    netloc = parsed.netloc.lower().lstrip("www.")
    base   = base_domain.lower().lstrip("www.")
    return netloc == base or netloc.endswith(f".{base}")


def is_crawlable(url: str) -> bool:
    """Filter out non-HTML resources."""
    lower = url.lower().split("?")[0]
    excluded_exts = (
        ".pdf", ".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg",
        ".mp4", ".mp3", ".zip", ".doc", ".docx", ".xls", ".xlsx",
        ".css", ".js", ".woff", ".woff2", ".ttf", ".ico",
        ".xml", ".json", ".txt", ".csv",
    )
    return not any(lower.endswith(ext) for ext in excluded_exts)


def extract_links(html: str, base_url: str) -> list[str]:
    """Extract all internal href links from HTML."""
    hrefs = re.findall(r'<a[^>]+href=["\']([^"\'#][^"\']*)["\']', html, re.IGNORECASE)
    links = []
    for href in hrefs:
        href = href.strip()
        if href.startswith(("javascript:", "mailto:", "tel:", "#")):
            continue
        absolute = urljoin(base_url, href)
        if absolute.startswith("http"):
            links.append(normalize_url(absolute))
    return links


def fetch_page(url: str) -> dict:
    """Fetch a page and return structured data."""
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    start = time.time()
    result = {
        "url":          url,
        "final_url":    url,
        "status":       None,
        "content_type": None,
        "response_ms":  None,
        "html":         None,
        "is_redirect":  False,
        "error":        None,
    }

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            result["response_ms"]  = round((time.time() - start) * 1000)
            result["status"]       = resp.status
            result["final_url"]    = resp.url
            result["is_redirect"]  = resp.url != url
            result["content_type"] = resp.headers.get("Content-Type", "")

            if "text/html" in result["content_type"]:
                result["html"] = resp.read(MAX_PAGE_SIZE).decode("utf-8", errors="replace")

    except urllib.error.HTTPError as e:
        result["response_ms"] = round((time.time() - start) * 1000)
        result["status"]      = e.code
        result["error"]       = f"HTTP {e.code}"
    except urllib.error.URLError as e:
        result["error"] = str(e.reason)
    except Exception as e:
        result["error"] = str(e)

    return result


def extract_seo_data(html: str | None, url: str) -> dict:
    """Extract all SEO signals from a page's HTML."""
    if not html:
        return {}

    data = {}

    # Title
    m = re.search(r'<title[^>]*>([^<]{1,200})</title>', html, re.IGNORECASE)
    data["title"]      = m.group(1).strip() if m else ""
    data["title_len"]  = len(data["title"])

    # Meta description
    m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']{1,400})',
                  html, re.IGNORECASE)
    if not m:
        m = re.search(r'<meta[^>]+content=["\']([^"\']{1,400})[^>]+name=["\']description["\']',
                      html, re.IGNORECASE)
    data["meta_desc"]     = m.group(1).strip() if m else ""
    data["meta_desc_len"] = len(data["meta_desc"])

    # H1
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
    h1_texts = [re.sub(r'<[^>]+>', '', h).strip() for h in h1s]
    data["h1_count"] = len(h1s)
    data["h1_text"]  = " | ".join(h1_texts[:2])

    # H2 count
    data["h2_count"] = len(re.findall(r'<h2', html, re.IGNORECASE))

    # Canonical
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
                  html, re.IGNORECASE)
    data["canonical"] = m.group(1).strip() if m else ""

    # Robots meta
    m = re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)["\']',
                  html, re.IGNORECASE)
    data["robots_meta"] = m.group(1).strip() if m else ""
    data["noindex"]     = "noindex" in data["robots_meta"].lower()

    # Open Graph
    og_title = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)["\']',
                         html, re.IGNORECASE)
    data["og_title"] = og_title.group(1)[:100] if og_title else ""

    # Schema types
    schemas = re.findall(r'"@type"\s*:\s*"([^"]+)"', html)
    data["schema_types"] = ", ".join(list(set(schemas))[:5])

    # Image count + missing alt
    images = re.findall(r'<img[^>]+>', html, re.IGNORECASE)
    data["image_count"]     = len(images)
    data["images_no_alt"]   = sum(1 for img in images if not re.search(r'alt=["\'][^"\']+["\']', img, re.IGNORECASE))

    # Word count (rough)
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text).strip()
    data["word_count"] = len(text.split())

    # Viewport
    data["has_viewport"] = bool(re.search(r'<meta[^>]+name=["\']viewport["\']', html, re.IGNORECASE))

    return data


def crawl(start_url: str, max_pages: int = 50, delay: float = CRAWL_DELAY) -> list[dict]:
    """
    Crawl the website starting from start_url.
    Returns a list of page records with full SEO data.
    """
    parsed_start = urlparse(normalize_url(start_url))
    base_domain  = parsed_start.netloc.lstrip("www.")

    visited  = set()
    queue    = deque([normalize_url(start_url)])
    results  = []
    crawled  = 0

    print(f"Starting crawl: {start_url}")
    print(f"Max pages: {max_pages} | Delay: {delay}s")

    while queue and crawled < max_pages:
        url = queue.popleft()

        if url in visited:
            continue
        visited.add(url)

        if not is_crawlable(url):
            continue

        print(f"  [{crawled + 1}/{max_pages}] {url[:80]}", end="\r")

        fetch = fetch_page(url)
        seo   = extract_seo_data(fetch.get("html"), url)
        links = extract_links(fetch.get("html") or "", fetch.get("final_url") or url)

        record = {
            "url":          url,
            "final_url":    fetch["final_url"],
            "status":       fetch["status"],
            "is_redirect":  fetch["is_redirect"],
            "response_ms":  fetch["response_ms"],
            "error":        fetch["error"],
            **seo,
            "outbound_links": len(links),
        }

        results.append(record)
        crawled += 1

        # Queue new internal links
        for link in links:
            if link not in visited and is_same_domain(link, base_domain):
                queue.append(link)

        time.sleep(delay)

    print(f"\nCrawl complete: {crawled} pages")
    return results


def analyze_crawl(records: list[dict]) -> dict:
    """Run analysis on crawl results to identify issues."""
    issues = {
        "broken_pages":       [],
        "redirects":          [],
        "noindex_pages":      [],
        "missing_title":      [],
        "long_title":         [],
        "short_title":        [],
        "missing_meta_desc":  [],
        "missing_h1":         [],
        "multiple_h1":        [],
        "missing_canonical":  [],
        "missing_schema":     [],
        "slow_pages":         [],
        "thin_content":       [],
        "images_missing_alt": [],
    }

    for r in records:
        url = r.get("url", "")

        if r.get("status") and r["status"] >= 400:
            issues["broken_pages"].append({"url": url, "status": r["status"]})

        if r.get("is_redirect"):
            issues["redirects"].append({"url": url, "final": r.get("final_url")})

        if r.get("noindex"):
            issues["noindex_pages"].append(url)

        title_len = r.get("title_len", 0)
        if not r.get("title"):
            issues["missing_title"].append(url)
        elif title_len > 60:
            issues["long_title"].append({"url": url, "len": title_len, "title": r.get("title","")[:60]})
        elif title_len < 30:
            issues["short_title"].append({"url": url, "len": title_len, "title": r.get("title","")})

        if not r.get("meta_desc"):
            issues["missing_meta_desc"].append(url)

        h1 = r.get("h1_count", 0)
        if h1 == 0:
            issues["missing_h1"].append(url)
        elif h1 > 1:
            issues["multiple_h1"].append({"url": url, "count": h1})

        if not r.get("canonical"):
            issues["missing_canonical"].append(url)

        if not r.get("schema_types"):
            issues["missing_schema"].append(url)

        if r.get("response_ms") and r["response_ms"] > 3000:
            issues["slow_pages"].append({"url": url, "ms": r["response_ms"]})

        if r.get("word_count", 0) < 300 and r.get("status") == 200:
            issues["thin_content"].append({"url": url, "words": r.get("word_count")})

        if r.get("images_no_alt", 0) > 0:
            issues["images_missing_alt"].append({"url": url, "count": r["images_no_alt"]})

    return issues


def save_results(records: list[dict], output_dir: Path, as_csv: bool = True):
    """Save crawl results to JSON and optionally CSV."""
    output_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")

    # JSON
    json_path = output_dir / f"crawl-{ts}.json"
    json_path.write_text(json.dumps(records, indent=2, default=str), encoding="utf-8")
    print(f"JSON saved: {json_path}")

    # Issues analysis
    issues   = analyze_crawl(records)
    issues_path = output_dir / f"crawl-issues-{ts}.json"
    issues_path.write_text(json.dumps(issues, indent=2, default=str), encoding="utf-8")
    print(f"Issues saved: {issues_path}")

    # CSV
    if as_csv and records:
        csv_path = output_dir / f"crawl-{ts}.csv"
        fieldnames = [
            "url", "status", "is_redirect", "final_url", "response_ms",
            "title", "title_len", "meta_desc_len", "h1_count", "h1_text",
            "word_count", "canonical", "noindex", "schema_types",
            "image_count", "images_no_alt", "has_viewport", "error",
        ]
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(records)
        print(f"CSV saved: {csv_path}")

    return json_path, issues_path


def print_summary(records: list[dict], issues: dict):
    """Print crawl summary."""
    print("\n" + "=" * 55)
    print(f"CRAWL SUMMARY — {len(records)} pages")
    print("=" * 55)

    status_counts = {}
    for r in records:
        s = r.get("status") or "error"
        status_counts[s] = status_counts.get(s, 0) + 1
    for status, count in sorted(status_counts.items()):
        print(f"  HTTP {status}: {count} pages")

    print(f"\nTECHNICAL ISSUES FOUND:")
    print(f"  Broken pages (4xx/5xx): {len(issues['broken_pages'])}")
    print(f"  Redirects:              {len(issues['redirects'])}")
    print(f"  Noindex pages:          {len(issues['noindex_pages'])}")
    print(f"  Missing title:          {len(issues['missing_title'])}")
    print(f"  Title too long (>60):   {len(issues['long_title'])}")
    print(f"  Missing meta desc:      {len(issues['missing_meta_desc'])}")
    print(f"  Missing/multiple H1:    {len(issues['missing_h1']) + len(issues['multiple_h1'])}")
    print(f"  Missing canonical:      {len(issues['missing_canonical'])}")
    print(f"  No structured data:     {len(issues['missing_schema'])}")
    print(f"  Slow pages (>3s):       {len(issues['slow_pages'])}")
    print(f"  Thin content (<300w):   {len(issues['thin_content'])}")
    print(f"  Images missing alt:     {len(issues['images_missing_alt'])}")
    print("=" * 55)


def main():
    parser = argparse.ArgumentParser(description="Crawl a website for technical SEO data.")
    parser.add_argument("--url",       required=True,              help="Starting URL to crawl")
    parser.add_argument("--max-pages", type=int, default=50,       help="Maximum pages to crawl (default: 50)")
    parser.add_argument("--output",    default="data/crawl",       help="Output directory")
    parser.add_argument("--delay",     type=float, default=0.5,    help="Delay between requests in seconds")
    parser.add_argument("--csv",       action="store_true",        help="Also save as CSV")
    parser.add_argument("--json",      action="store_true",        help="Print results as JSON to stdout")

    args = parser.parse_args()
    output_dir = Path(args.output)

    records = crawl(args.url, max_pages=args.max_pages, delay=args.delay)
    issues  = analyze_crawl(records)

    if args.json:
        print(json.dumps({"records": records, "issues": issues}, indent=2, default=str))
    else:
        save_results(records, output_dir, as_csv=args.csv)
        print_summary(records, issues)


if __name__ == "__main__":
    main()
