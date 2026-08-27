#!/usr/bin/env python3
"""
generate_pdf.py — Professional PDF Report Generator
Local Business SEO Audit System

Converts an HTML report file to PDF using headless Chrome.
Includes automatic Chrome binary detection, retry logic, and file size reporting.
Also supports WeasyPrint as a fallback if Chrome is not available.

Usage:
    python3 scripts/generate_pdf.py --html reports/phase-1-competitor-profiles.html
    python3 scripts/generate_pdf.py --html path/to/report.html --output path/to/output.pdf
    python3 scripts/generate_pdf.py --html report.html --engine weasyprint
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/snap/bin/chromium",
]


def find_chrome() -> str | None:
    """Locate the Chrome/Chromium binary."""
    for path in CHROME_PATHS:
        if os.path.isfile(path):
            return path

    # Try PATH
    for cmd in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        found = shutil.which(cmd)
        if found:
            return found

    return None


def chrome_to_pdf(chrome: str, html_path: str, pdf_path: str,
                  page_size: str = "A4", margin: str = "10mm") -> bool:
    """Convert HTML to PDF using headless Chrome."""
    html_abs = Path(html_path).resolve()
    pdf_abs  = Path(pdf_path).resolve()

    # Ensure output directory exists
    pdf_abs.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--disable-software-rasterizer",
        "--disable-background-networking",
        "--disable-default-apps",
        "--no-first-run",
        "--disable-sync",
        "--run-all-compositor-stages-before-draw",
        "--disable-checker-imaging",
        f"--print-to-pdf={pdf_abs}",
        f"--print-to-pdf-no-header",
        f"file://{html_abs}",
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode == 0 and pdf_abs.exists():
            return True
        else:
            print(f"Chrome error (code {result.returncode}): {result.stderr[:500]}", file=sys.stderr)
            return False
    except subprocess.TimeoutExpired:
        print("Chrome timed out after 60 seconds", file=sys.stderr)
        return False
    except FileNotFoundError:
        print(f"Chrome binary not found at: {chrome}", file=sys.stderr)
        return False


def weasyprint_to_pdf(html_path: str, pdf_path: str) -> bool:
    """Convert HTML to PDF using WeasyPrint (pip install weasyprint)."""
    try:
        from weasyprint import HTML
        html_abs = Path(html_path).resolve()
        pdf_abs  = Path(pdf_path).resolve()
        pdf_abs.parent.mkdir(parents=True, exist_ok=True)

        HTML(filename=str(html_abs)).write_pdf(str(pdf_abs))
        return pdf_abs.exists()
    except ImportError:
        print("WeasyPrint not installed. Run: pip install weasyprint", file=sys.stderr)
        return False
    except Exception as e:
        print(f"WeasyPrint error: {e}", file=sys.stderr)
        return False


def format_size(size_bytes: int) -> str:
    """Format file size in human-readable form."""
    if size_bytes >= 1_000_000:
        return f"{size_bytes / 1_000_000:.1f} MB"
    elif size_bytes >= 1_000:
        return f"{size_bytes / 1_000:.0f} KB"
    else:
        return f"{size_bytes} bytes"


def main():
    parser = argparse.ArgumentParser(description="Convert HTML audit report to PDF.")
    parser.add_argument("--html",   required=True, help="Input HTML file path")
    parser.add_argument("--output", default=None,  help="Output PDF path (default: same dir as HTML, .pdf ext)")
    parser.add_argument("--engine", default="auto",
                        choices=["auto", "chrome", "weasyprint"],
                        help="PDF engine (default: auto — Chrome first, WeasyPrint fallback)")

    args = parser.parse_args()

    html_path = args.html
    if not Path(html_path).exists():
        print(f"ERROR: HTML file not found: {html_path}", file=sys.stderr)
        sys.exit(1)

    # Determine output path
    if args.output:
        pdf_path = args.output
    else:
        pdf_path = str(Path(html_path).with_suffix(".pdf"))

    print(f"Input:  {html_path}")
    print(f"Output: {pdf_path}")

    success = False

    if args.engine in ("auto", "chrome"):
        chrome = find_chrome()
        if chrome:
            print(f"Engine: Chrome ({chrome})")
            success = chrome_to_pdf(chrome, html_path, pdf_path)
            if not success and args.engine == "auto":
                print("Chrome failed, trying WeasyPrint...", file=sys.stderr)
        elif args.engine == "chrome":
            print("ERROR: Chrome not found. Install Google Chrome or use --engine weasyprint", file=sys.stderr)
            sys.exit(1)

    if not success and args.engine in ("auto", "weasyprint"):
        print("Engine: WeasyPrint")
        success = weasyprint_to_pdf(html_path, pdf_path)

    if success:
        size = Path(pdf_path).stat().st_size
        print(f"SUCCESS: PDF generated — {format_size(size)}")
        print(f"Path: {Path(pdf_path).resolve()}")
        sys.exit(0)
    else:
        print("ERROR: PDF generation failed with all available engines.", file=sys.stderr)
        print("Install Chrome: brew install --cask google-chrome", file=sys.stderr)
        print("Or WeasyPrint:  pip install weasyprint", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
