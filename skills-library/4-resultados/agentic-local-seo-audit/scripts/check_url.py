#!/usr/bin/env python3
"""
check_url.py — URL Validation & Accessibility Checker
Local Business SEO Audit System

Validates a URL's accessibility, checks HTTP status, extracts key SEO signals,
and detects common technical issues before starting the audit.

Usage:
    python3 scripts/check_url.py --url https://example.com
    python3 scripts/check_url.py --url https://example.com --json
    python3 scripts/check_url.py --url https://example.com --full
"""

import argparse
import json
import re
import socket
import ssl
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; SEO-Audit-Bot/1.0; "
        "+https://github.com/mshahiddigital/local-seo-audit)"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "identity",
    "Connection": "close",
}

TIMEOUT = 15


def normalize_url(url: str) -> str:
    """Ensure URL has a scheme."""
    if not url.startswith(("http://", "https://")):
        return f"https://{url}"
    return url


def check_ssl(hostname: str, port: int = 443) -> dict:
    """Check SSL certificate validity and expiry."""
    result = {"valid": False, "expires": None, "days_remaining": None, "error": None}
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(
            socket.create_connection((hostname, port), timeout=TIMEOUT),
            server_hostname=hostname
        ) as sock:
            cert = sock.getpeercert()
            not_after = cert.get("notAfter")
            if not_after:
                exp = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
                now = datetime.now(timezone.utc)
                days = (exp - now).days
                result.update({
                    "valid":          True,
                    "expires":        exp.strftime("%Y-%m-%d"),
                    "days_remaining": days,
                })
            else:
                result["valid"] = True
    except ssl.SSLCertVerificationError as e:
        result["error"] = f"SSL verification failed: {e}"
    except ssl.SSLError as e:
        result["error"] = f"SSL error: {e}"
    except (ConnectionRefusedError, socket.timeout, OSError) as e:
        result["error"] = f"Connection error: {e}"
    return result


def _get_ssl_context() -> ssl.SSLContext:
    """Return a best-effort SSL context, falling back to unverified on macOS cert issues."""
    try:
        ctx = ssl.create_default_context()
        # Try to load certifi certs if available
        try:
            import certifi
            ctx = ssl.create_default_context(cafile=certifi.where())
        except ImportError:
            pass
        return ctx
    except Exception:
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx


def fetch_url(url: str) -> dict:
    """Fetch URL and return status, headers, response time, and content."""
    req = urllib.request.Request(url, headers=HEADERS, method="GET")
    start = time.time()
    result = {
        "url":            url,
        "final_url":      url,
        "status_code":    None,
        "response_time":  None,
        "headers":        {},
        "content":        "",
        "redirect_chain": [],
        "error":          None,
    }

    # Try verified SSL first, then fall back to unverified (handles macOS cert issues)
    ssl_contexts = [_get_ssl_context(), ssl._create_unverified_context()]
    for i, ctx in enumerate(ssl_contexts):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
                result["response_time"] = round((time.time() - start) * 1000)
                result["status_code"]   = resp.status
                result["final_url"]     = resp.url
                result["headers"]       = dict(resp.headers)
                result["content"]       = resp.read(200_000).decode("utf-8", errors="replace")
                result["error"]         = None
            return result  # Success — stop trying

        except urllib.error.HTTPError as e:
            result["response_time"] = round((time.time() - start) * 1000)
            result["status_code"]   = e.code
            result["error"]         = f"HTTP {e.code}: {e.reason}"
            try:
                result["headers"] = dict(e.headers)
            except Exception:
                pass
            return result  # HTTP error is a valid response

        except ssl.SSLCertVerificationError:
            if i < len(ssl_contexts) - 1:
                continue  # Try next (unverified) context
            result["error"] = "SSL certificate verification failed"

        except urllib.error.URLError as e:
            result["error"] = f"URL error: {e.reason}"
            if "SSL" in str(e.reason) and i < len(ssl_contexts) - 1:
                continue  # Try unverified context
            break

        except socket.timeout:
            result["error"] = f"Timeout after {TIMEOUT}s"
            break

        except Exception as e:
            result["error"] = f"Unexpected error: {e}"
            break

    return result


def extract_seo_signals(content: str, base_url: str) -> dict:
    """Extract key SEO signals from the page HTML."""
    signals = {}

    # Title tag
    m = re.search(r'<title[^>]*>([^<]{1,200})</title>', content, re.IGNORECASE)
    signals["title"]       = m.group(1).strip() if m else None
    signals["title_len"]   = len(signals["title"]) if signals["title"] else 0

    # Meta description
    m = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']{1,300})',
                  content, re.IGNORECASE)
    if not m:
        m = re.search(r'<meta[^>]+content=["\']([^"\']{1,300})[^>]+name=["\']description["\']',
                      content, re.IGNORECASE)
    signals["meta_desc"]     = m.group(1).strip() if m else None
    signals["meta_desc_len"] = len(signals["meta_desc"]) if signals["meta_desc"] else 0

    # H1 tags
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
    signals["h1_count"]  = len(h1s)
    signals["h1_text"]   = [re.sub(r'<[^>]+>', '', h).strip() for h in h1s[:3]]

    # Canonical
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']',
                  content, re.IGNORECASE)
    signals["canonical"] = m.group(1).strip() if m else None

    # Robots meta
    m = re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)["\']',
                  content, re.IGNORECASE)
    signals["robots_meta"] = m.group(1).strip() if m else None

    # Viewport (mobile)
    signals["has_viewport"] = bool(
        re.search(r'<meta[^>]+name=["\']viewport["\']', content, re.IGNORECASE)
    )

    # Schema.org
    schemas = re.findall(r'"@type"\s*:\s*"([^"]+)"', content)
    signals["schema_types"] = list(set(schemas))

    # Open Graph
    og_tags = re.findall(r'<meta[^>]+property=["\']og:([^"\']+)["\'][^>]+content=["\']([^"\']+)["\']',
                         content, re.IGNORECASE)
    signals["og_tags"] = {k: v for k, v in og_tags}

    # Word count (rough)
    text = re.sub(r'<[^>]+>', ' ', content)
    text = re.sub(r'\s+', ' ', text)
    signals["word_count"] = len(text.split())

    return signals


def check_robots_txt(base_url: str) -> dict:
    """Fetch and analyze robots.txt."""
    robots_url = urljoin(base_url, "/robots.txt")
    result = {"url": robots_url, "exists": False, "sitemap_refs": [], "content": None, "error": None}

    try:
        data = fetch_url(robots_url)
        if data["status_code"] == 200 and data["content"]:
            result["exists"]       = True
            result["content"]      = data["content"][:2000]
            result["sitemap_refs"] = re.findall(r'(?i)^sitemap:\s*(.+)$',
                                                data["content"], re.MULTILINE)
    except Exception as e:
        result["error"] = str(e)

    return result


def check_sitemap(base_url: str) -> dict:
    """Check for XML sitemap."""
    candidates = ["/sitemap.xml", "/sitemap_index.xml", "/sitemap-index.xml"]
    for path in candidates:
        url = urljoin(base_url, path)
        data = fetch_url(url)
        if data["status_code"] == 200:
            url_count = len(re.findall(r'<url>', data["content"], re.IGNORECASE))
            return {
                "found":     True,
                "url":       url,
                "url_count": url_count,
                "is_index":  "<sitemapindex" in data["content"].lower(),
            }
    return {"found": False, "url": None, "url_count": 0}


def run_checks(url: str, full: bool = False) -> dict:
    """Run all URL checks and return a structured report."""
    url = normalize_url(url)
    parsed = urlparse(url)
    hostname = parsed.netloc

    report = {
        "url":         url,
        "hostname":    hostname,
        "checked_at":  datetime.now().isoformat(),
        "accessible":  False,
        "status_code": None,
        "https":       url.startswith("https://"),
        "ssl":         None,
        "redirect":    None,
        "response_ms": None,
        "seo_signals": {},
        "robots_txt":  None,
        "sitemap":     None,
        "issues":      [],
        "passes":      [],
    }

    # SSL check
    if report["https"]:
        report["ssl"] = check_ssl(hostname)

    # Fetch main URL
    fetch = fetch_url(url)
    report["status_code"] = fetch["status_code"]
    report["response_ms"] = fetch["response_time"]

    if fetch["error"] and not fetch["status_code"]:
        report["issues"].append(f"CRITICAL: Site unreachable — {fetch['error']}")
        return report

    if fetch["status_code"] in (200, 301, 302, 307, 308):
        report["accessible"] = True
        if fetch["final_url"] != url:
            report["redirect"] = fetch["final_url"]

    # SEO signals
    if fetch["content"]:
        report["seo_signals"] = extract_seo_signals(fetch["content"], url)

    # Full checks
    if full:
        report["robots_txt"] = check_robots_txt(url)
        report["sitemap"]    = check_sitemap(url)

    # Generate issues and passes
    ssl = report["ssl"] or {}
    seo = report["seo_signals"]

    if not report["https"]:
        report["issues"].append("CRITICAL: Site uses HTTP not HTTPS")
    elif ssl.get("error"):
        report["issues"].append(f"CRITICAL: SSL error — {ssl['error']}")
    elif ssl.get("days_remaining", 999) < 30:
        report["issues"].append(f"HIGH: SSL certificate expires in {ssl['days_remaining']} days")
    else:
        report["passes"].append(f"HTTPS active, SSL valid until {ssl.get('expires', 'unknown')}")

    if report["status_code"] == 200:
        report["passes"].append(f"Site accessible (HTTP 200) in {report['response_ms']}ms")
    elif report["status_code"] in (301, 302):
        report["issues"].append(f"MEDIUM: Redirect detected ({report['status_code']}) → {fetch['final_url']}")

    if seo.get("title"):
        if 50 <= seo["title_len"] <= 60:
            report["passes"].append(f"Title tag optimal length ({seo['title_len']} chars): {seo['title'][:60]}")
        elif seo["title_len"] > 60:
            report["issues"].append(f"MEDIUM: Title too long ({seo['title_len']} chars) — trim to 50-60")
        else:
            report["issues"].append(f"MEDIUM: Title too short ({seo['title_len']} chars) — expand to 50-60")
    else:
        report["issues"].append("HIGH: Missing title tag")

    if not seo.get("meta_desc"):
        report["issues"].append("HIGH: Missing meta description")
    elif seo["meta_desc_len"] > 160:
        report["issues"].append(f"LOW: Meta description too long ({seo['meta_desc_len']} chars)")

    if seo.get("h1_count") == 0:
        report["issues"].append("HIGH: No H1 tag found")
    elif seo.get("h1_count") > 1:
        report["issues"].append(f"MEDIUM: Multiple H1 tags ({seo['h1_count']}) — should be exactly 1")
    else:
        report["passes"].append(f"H1 present: {seo['h1_text'][0][:80] if seo.get('h1_text') else ''}")

    if not seo.get("has_viewport"):
        report["issues"].append("HIGH: Missing viewport meta tag — mobile SEO risk")
    else:
        report["passes"].append("Viewport meta tag present")

    if seo.get("schema_types"):
        report["passes"].append(f"Structured data found: {', '.join(seo['schema_types'][:5])}")
    else:
        report["issues"].append("HIGH: No structured data (schema.org) detected")

    robots_meta = seo.get("robots_meta", "")
    if robots_meta and ("noindex" in robots_meta.lower() or "none" in robots_meta.lower()):
        report["issues"].append(f"CRITICAL: Page has noindex robots meta: {robots_meta}")

    if report["response_ms"] and report["response_ms"] > 3000:
        report["issues"].append(f"HIGH: Slow TTFB ({report['response_ms']}ms) — target <800ms")
    elif report["response_ms"] and report["response_ms"] < 800:
        report["passes"].append(f"Fast response time ({report['response_ms']}ms)")

    return report


def print_report(report: dict):
    """Print a human-readable accessibility report."""
    print("=" * 60)
    print(f"URL CHECK REPORT")
    print(f"URL:     {report['url']}")
    print(f"Checked: {report['checked_at']}")
    print("=" * 60)

    status_icon = "✅" if report["accessible"] else "❌"
    print(f"\n{status_icon} Status: HTTP {report['status_code']} | {report['response_ms']}ms")

    if report.get("redirect"):
        print(f"↳ Redirects to: {report['redirect']}")

    ssl = report.get("ssl") or {}
    if ssl.get("valid"):
        print(f"🔒 SSL: Valid, expires {ssl.get('expires')} ({ssl.get('days_remaining')} days)")
    elif ssl.get("error"):
        print(f"⚠️  SSL: {ssl['error']}")

    seo = report.get("seo_signals", {})
    if seo:
        print(f"\n--- SEO SIGNALS ---")
        print(f"Title ({seo.get('title_len',0)} chars): {seo.get('title','N/A')}")
        print(f"Meta desc ({seo.get('meta_desc_len',0)} chars): {(seo.get('meta_desc') or 'MISSING')[:80]}")
        print(f"H1 tags: {seo.get('h1_count',0)} — {seo.get('h1_text',['N/A'])[0][:60] if seo.get('h1_text') else 'N/A'}")
        print(f"Schema types: {', '.join(seo.get('schema_types',[])) or 'None'}")
        print(f"Word count: ~{seo.get('word_count',0)}")

    if report.get("issues"):
        print(f"\n--- ISSUES ({len(report['issues'])}) ---")
        for issue in report["issues"]:
            print(f"  ⚠️  {issue}")

    if report.get("passes"):
        print(f"\n--- PASSES ({len(report['passes'])}) ---")
        for p in report["passes"]:
            print(f"  ✅ {p}")

    robots = report.get("robots_txt")
    if robots:
        status = "✅ Found" if robots.get("exists") else "❌ Missing"
        print(f"\nRobots.txt: {status}")
        if robots.get("sitemap_refs"):
            print(f"  Sitemap refs: {', '.join(robots['sitemap_refs'])}")

    sitemap = report.get("sitemap")
    if sitemap:
        if sitemap.get("found"):
            print(f"Sitemap: ✅ {sitemap['url']} ({sitemap['url_count']} URLs)")
        else:
            print(f"Sitemap: ❌ Not found at standard paths")

    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="Check URL accessibility and SEO signals.")
    parser.add_argument("--url",  required=True, help="URL to check")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--full", action="store_true", help="Run extended checks (robots.txt, sitemap)")

    args = parser.parse_args()
    report = run_checks(args.url, full=args.full)

    if args.json:
        print(json.dumps(report, indent=2, default=str))
    else:
        print_report(report)

    # Exit code: 0 = accessible, 1 = not accessible
    sys.exit(0 if report["accessible"] else 1)


if __name__ == "__main__":
    main()
