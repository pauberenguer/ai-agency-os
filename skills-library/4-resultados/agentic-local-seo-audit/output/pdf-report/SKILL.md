---
name: pdf-report
description: >
  Generates professionally designed PDF audit reports. Activates when the user
  requests a PDF report, wants to export audit findings, asks for a printable
  report, or uses the generate-pdf or export-html commands. Produces a visually
  stunning HTML report with SVG gauge charts, color-coded severity cards, and
  professional tables, then converts to PDF. Uses Python script for reliable
  multi-engine PDF generation. All files saved to {REPORTS_DIR}/.
---

# PDF Report Generation System

## Executive Summary

The PDF report is the client-facing deliverable — the tangible output of the entire 21-phase audit. Report quality directly impacts perceived value. A well-designed PDF report converts audit findings into client trust: 87% of clients who receive a visually professional audit report retain the agency vs. 34% who receive a plain text output (AgencyAnalytics survey, 2024). Every phase must produce its own PDF; the final master report compiles all phases into a single document.

**2025–2026 reporting context:**
- Include SEO Health Index = (LOCAL-IMPACT × 0.55) + (SERP-TRUST × 0.45) as the master metric
- AI Overviews impact must be called out per relevant finding (20–35% of local queries)
- All CWV thresholds use 2025 values: INP < 200ms (not FID), LCP < 2.5s, CLS < 0.1
- Score grades: A (90–100) / B (75–89) / C (60–74) / D (45–59) / F (< 45)
- Source data for reports comes from: Ahrefs (backlinks, keywords), SEMrush (traffic, gaps), Screaming Frog (technical crawl), Google Search Console (GSC) (coverage, performance), PageSpeed Insights + Lighthouse (CWV), BrightLocal (citations, GBP rank), Majestic (TF:CF), Google Business Profile (GBP), ChatGPT/Perplexity (AI visibility tests)
- GBP 2025 features to include in reports: Q&A section completeness, service menu with prices, review velocity (last 90 days), Google Reserve/Booking integration, AI Overview local pack eligibility (≥4.3 stars, 50+ reviews), GBP Posts frequency
- AI crawler access status must be reported in technical findings (14 crawlers, 3 tiers)
- llms.txt presence/absence should be flagged in AI SEO section
- Brand mention authority score (YouTube/Reddit/Wikipedia correlation with AI citations) in reputation section
- Platform-specific AI optimization status (AIO, ChatGPT, Perplexity, Gemini, Copilot) in AI SEO section

**Numbered Action Steps:**
1. Confirm `{AUDIT_DIR}/` has all required phase `.md` files — run `python3 scripts/audit_status.py --project projects/[slug]` — Effort: 1 min
2. Run `python3 scripts/report_compiler.py --project projects/[slug]` → generates `{AUDIT_DIR}/master-report.md` — Effort: 2 min
3. Build HTML report for each phase — use full design system (SVG gauges, color cards, tables) — Effort: 30–60 min per phase
4. Save HTML to `{REPORTS_DIR}/phase-[N]-[slug].html` — Effort: 1 min per phase
5. Run `python3 scripts/generate_pdf.py --html {REPORTS_DIR}/phase-[N]-[slug].html` — generates PDF — Effort: 30 sec per phase
6. Confirm PDF size and page count — alert if <2 pages (likely rendering error) or >30 pages (likely runaway content) — Effort: 1 min
7. Repeat steps 3–6 for all 21 phases + LOCAL-IMPACT + SERP-TRUST + master report — Effort: varies
8. Deliver master-report.pdf + all phase PDFs in `{REPORTS_DIR}/` folder to client — Effort: 5 min

---

## Tools for This Phase

| Tool | Purpose | Cost |
|---|---|---|
| `python3 scripts/generate_pdf.py` | Chrome headless + WeasyPrint fallback PDF generation | Free (local) |
| **Google Chrome headless** | Primary PDF engine — highest fidelity HTML→PDF | Free |
| **WeasyPrint** | Fallback PDF engine — no Chrome needed | Free |
| **Google Chrome browser** | Preview HTML before PDF conversion | Free |
| `python3 scripts/report_compiler.py` | Compile all phase .md files into master-report.md | Free (local) |

---

## Report Quality Standards (2025)

| Report Element | Minimum Standard | Excellent Standard |
|---|---|---|
| Cover page | Business name, score, date, URL | + SVG gauge chart, grade badge, key verdict |
| Dashboard page | Score cards per dimension | + Competitor comparison bars, trend arrows |
| Issue cards | Status + issue + fix | + Priority score, effort estimate, competitor context |
| Priority matrix | Impact × Feasibility table | + Visual heat map, 30/90-day roadmap |
| File size | < 5MB | < 2MB (optimized images) |
| Page count | 15–30 pages | 20–40 pages (comprehensive) |
| Completeness | All completed phases | All 21 phases + both scoring frameworks |

---

## Required Report Sections by Report Type

| Report Type | Cover Page | Score Gauge | Issue Cards | Priority Matrix | Competitor Table | Quick Wins | Roadmap | AI Visibility Callout |
|---|---|---|---|---|---|---|---|---|
| Per-phase PDF | Yes | Yes (phase score) | Yes | Yes | Yes (phase-specific) | Yes (top 3) | No | Yes (if content/on-page/AI phase) |
| LOCAL-IMPACT PDF | Yes | Yes (composite) | No | No | Yes (benchmarks) | Yes (top 5) | No | Yes (AI readiness dimension) |
| SERP-TRUST PDF | Yes | Yes (composite) | No | No | Yes (benchmarks) | Yes (top 5) | No | Yes (T2 dimension) |
| Master Report PDF | Yes | Yes (SEO Health Index) | Yes (all phases) | Yes (master) | Yes (full competitor summary) | Yes (top 10) | Yes (30/90/180-day) | Yes (dedicated section) |

## 2025–2026 Report Content Requirements

| Section | What to Include | Why It Matters |
|---|---|---|
| AI Visibility Dashboard | AIO citation status, ChatGPT/Perplexity mentions, AI crawler access score | AI search drives 20–35% of local queries; clients need to see their AI presence |
| GBP Health Summary | Q&A completeness, review velocity (last 90 days), service menu, Google Reserve status, AI Overview eligibility | GBP is the #1 local ranking factor; 2025 features (Q&A, service menu) directly affect AIO inclusion |
| Brand Mention Authority | YouTube/Reddit/Wikipedia presence, brand mention score vs. backlink profile | Brand mentions correlate 3× more with AI visibility than backlinks (Ahrefs Dec 2025) |
| AI Crawler Access | Tier 1/2/3 crawler status, llms.txt presence, IndexNow status | Blocked AI crawlers = invisible to that platform regardless of content quality |
| Platform Readiness | Per-platform scores (AIO, ChatGPT, Perplexity, Gemini, Copilot) | Only 11% of domains cited by both ChatGPT and AIO — platform-specific optimization required |
| Citability Score | Answer block quality, self-containment, statistical density | AI models cite passages meeting specific structural criteria (134–167 word blocks, answer-first) |

## Architecture

1. **Read** `{AUDIT_DIR}/intake-data.md` to get PROJECT_DIR, business name, URL
2. **Aggregate** all audit findings from `{AUDIT_DIR}/*.md` files
3. **Generate** a complete HTML file using the design system below with real audit data
4. **Write** the HTML file to `{REPORTS_DIR}/phase-[N]-[slug].html`
5. **Convert** to PDF using the Python script (auto-detects Chrome or WeasyPrint):
   ```bash
   python3 scripts/generate_pdf.py --html {REPORTS_DIR}/phase-[N]-[slug].html
   ```
   Or directly via Chrome:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
     --headless=new --disable-gpu --no-sandbox --print-to-pdf-no-header \
     --print-to-pdf="{REPORTS_DIR}/phase-[N]-[slug].pdf" \
     "file:///[absolute-path-to-html]"
   ```
6. **Report** PDF path + file size to user

## Step 1: Detect Chrome Path (Manual Fallback)

If not using the Python script, detect the Chrome binary:

```bash
if [ -f "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]; then
  CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
elif command -v google-chrome &> /dev/null; then
  CHROME="google-chrome"
elif command -v chromium-browser &> /dev/null; then
  CHROME="chromium-browser"
elif command -v chromium &> /dev/null; then
  CHROME="chromium"
else
  echo "ERROR: Chrome not found. Install with: brew install --cask google-chrome"
  exit 1
fi
echo "Chrome found at: $CHROME"
```

## Step 2: Generate HTML Report

Write a complete HTML file using the template structure and design system below.
Replace ALL placeholder values with real audit data from the conversation.

### File Naming Convention
```
reports/{business-name-slug}-seo-audit-{YYYY-MM-DD}.html
reports/{business-name-slug}-seo-audit-{YYYY-MM-DD}.pdf
```

## Step 3: Convert to PDF

```bash
mkdir -p reports
"$CHROME" --headless --disable-gpu --no-sandbox \
  --print-to-pdf="reports/{filename}.pdf" \
  "file://{absolute-path-to-html}"
```

---

## HTML TEMPLATE STRUCTURE

Generate the COMPLETE HTML below, populated with real audit data.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SEO Audit Report — {BUSINESS_NAME}</title>
  <style>
    /* ============================================
       DESIGN SYSTEM — SEO AUDIT REPORT
       ============================================ */

    :root {
      /* Brand Colors */
      --primary: #1E3A5F;
      --primary-light: #2563EB;
      --primary-bg: #EFF6FF;
      --accent: #0EA5E9;

      /* Score Colors */
      --score-excellent: #059669;
      --score-excellent-bg: #ECFDF5;
      --score-good: #10B981;
      --score-good-bg: #D1FAE5;
      --score-warning: #D97706;
      --score-warning-bg: #FEF3C7;
      --score-critical: #DC2626;
      --score-critical-bg: #FEE2E2;

      /* Neutrals */
      --text-primary: #111827;
      --text-secondary: #6B7280;
      --text-muted: #9CA3AF;
      --border: #E5E7EB;
      --surface: #F9FAFB;
      --white: #FFFFFF;

      /* Typography */
      --font-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace;
    }

    /* Print Settings */
    @page {
      size: A4;
      margin: 18mm 15mm 22mm 15mm;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: var(--font-sans);
      font-size: 10.5pt;
      line-height: 1.6;
      color: var(--text-primary);
      background: var(--white);
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }

    /* Page Break Utilities */
    .page-break { page-break-after: always; }
    .no-break { page-break-inside: avoid; }
    .break-before { page-break-before: always; }

    /* ============================================
       COVER PAGE
       ============================================ */
    .cover {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      text-align: center;
      background: linear-gradient(135deg, var(--primary) 0%, #0F172A 100%);
      color: var(--white);
      padding: 60px 40px;
      margin: -18mm -15mm 0 -15mm;
      page-break-after: always;
    }

    .cover-badge {
      display: inline-block;
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.25);
      border-radius: 20px;
      padding: 6px 20px;
      font-size: 11pt;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 40px;
    }

    .cover h1 {
      font-size: 32pt;
      font-weight: 800;
      line-height: 1.2;
      margin-bottom: 16px;
    }

    .cover .subtitle {
      font-size: 14pt;
      color: rgba(255,255,255,0.8);
      margin-bottom: 50px;
    }

    .cover-score {
      margin: 30px 0;
    }

    .cover-meta {
      margin-top: 50px;
      font-size: 10pt;
      color: rgba(255,255,255,0.6);
    }

    .cover-meta strong {
      color: rgba(255,255,255,0.9);
    }

    .cover-meta div {
      margin: 6px 0;
    }

    /* ============================================
       TABLE OF CONTENTS
       ============================================ */
    .toc {
      padding: 40px 0;
    }

    .toc h2 {
      font-size: 20pt;
      color: var(--primary);
      margin-bottom: 30px;
      padding-bottom: 10px;
      border-bottom: 3px solid var(--primary);
    }

    .toc-list {
      list-style: none;
    }

    .toc-list li {
      padding: 10px 0;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11pt;
    }

    .toc-list li .toc-num {
      font-weight: 700;
      color: var(--primary);
      min-width: 30px;
    }

    .toc-list li .toc-dots {
      flex: 1;
      border-bottom: 1px dotted var(--text-muted);
      margin: 0 10px;
      height: 1px;
    }

    /* ============================================
       SECTION HEADERS
       ============================================ */
    .section {
      padding: 10px 0 30px 0;
    }

    .section-header {
      margin-bottom: 24px;
      padding-bottom: 12px;
      border-bottom: 3px solid var(--primary);
    }

    .section-header h2 {
      font-size: 18pt;
      color: var(--primary);
      margin-bottom: 4px;
    }

    .section-header .section-sub {
      font-size: 10pt;
      color: var(--text-secondary);
    }

    h3 {
      font-size: 13pt;
      color: var(--primary);
      margin: 20px 0 10px 0;
      padding-bottom: 6px;
      border-bottom: 1px solid var(--border);
    }

    h4 {
      font-size: 11pt;
      color: var(--text-primary);
      margin: 14px 0 8px 0;
    }

    p {
      margin-bottom: 10px;
    }

    /* ============================================
       SCORE GAUGES (SVG)
       ============================================ */
    .score-dashboard {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin: 20px 0;
    }

    .score-dashboard .overall {
      grid-column: 1 / -1;
      display: flex;
      justify-content: center;
      margin-bottom: 10px;
    }

    .gauge-card {
      text-align: center;
      padding: 15px;
      background: var(--surface);
      border-radius: 10px;
      border: 1px solid var(--border);
    }

    .gauge-card .gauge-label {
      font-size: 9pt;
      font-weight: 600;
      color: var(--text-secondary);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 8px;
    }

    .gauge-overall {
      text-align: center;
      padding: 20px;
      background: var(--primary-bg);
      border-radius: 12px;
      border: 2px solid var(--primary);
    }

    /* ============================================
       ISSUE CARDS
       ============================================ */
    .issue-card {
      border-left: 4px solid;
      padding: 12px 16px;
      margin-bottom: 12px;
      border-radius: 0 8px 8px 0;
      page-break-inside: avoid;
    }

    .issue-card.critical {
      border-color: var(--score-critical);
      background: var(--score-critical-bg);
    }

    .issue-card.high {
      border-color: var(--score-warning);
      background: var(--score-warning-bg);
    }

    .issue-card.medium {
      border-color: #FBBF24;
      background: #FFFBEB;
    }

    .issue-card.low {
      border-color: var(--score-good);
      background: var(--score-good-bg);
    }

    .issue-card .issue-title {
      font-weight: 700;
      font-size: 10.5pt;
      margin-bottom: 4px;
    }

    .issue-card .issue-desc {
      font-size: 9.5pt;
      color: var(--text-secondary);
      margin-bottom: 6px;
    }

    .issue-card .issue-meta {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    /* Badges */
    .badge {
      display: inline-block;
      padding: 2px 8px;
      border-radius: 10px;
      font-size: 8pt;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    .badge-critical { background: var(--score-critical); color: white; }
    .badge-high { background: var(--score-warning); color: white; }
    .badge-medium { background: #FBBF24; color: #78350F; }
    .badge-low { background: var(--score-good); color: white; }
    .badge-pass { background: var(--score-excellent); color: white; }
    .badge-effort { background: var(--primary-light); color: white; }
    .badge-info { background: #6366F1; color: white; }

    /* ============================================
       TABLES
       ============================================ */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0 20px 0;
      font-size: 9.5pt;
      page-break-inside: auto;
    }

    thead {
      display: table-header-group;
    }

    thead th {
      background: var(--primary);
      color: var(--white);
      padding: 10px 12px;
      text-align: left;
      font-weight: 600;
      font-size: 9pt;
      text-transform: uppercase;
      letter-spacing: 0.3px;
    }

    tbody tr {
      border-bottom: 1px solid var(--border);
    }

    tbody tr:nth-child(even) {
      background: var(--surface);
    }

    tbody td {
      padding: 8px 12px;
      vertical-align: top;
    }

    /* ============================================
       BAR CHARTS (CSS-only)
       ============================================ */
    .bar-chart {
      margin: 15px 0;
    }

    .bar-row {
      display: flex;
      align-items: center;
      margin-bottom: 8px;
    }

    .bar-label {
      width: 140px;
      font-size: 9pt;
      font-weight: 500;
      color: var(--text-primary);
      flex-shrink: 0;
    }

    .bar-track {
      flex: 1;
      height: 22px;
      background: var(--surface);
      border-radius: 4px;
      overflow: hidden;
      position: relative;
    }

    .bar-fill {
      height: 100%;
      border-radius: 4px;
      display: flex;
      align-items: center;
      padding-left: 8px;
      font-size: 8pt;
      font-weight: 700;
      color: white;
      min-width: 30px;
    }

    .bar-fill.client { background: var(--primary-light); }
    .bar-fill.comp1 { background: #94A3B8; }
    .bar-fill.comp2 { background: #CBD5E1; }
    .bar-fill.comp3 { background: #E2E8F0; color: var(--text-secondary); }

    /* ============================================
       TIMELINE / ROADMAP
       ============================================ */
    .timeline {
      position: relative;
      padding-left: 30px;
      margin: 20px 0;
    }

    .timeline::before {
      content: '';
      position: absolute;
      left: 8px;
      top: 0;
      bottom: 0;
      width: 3px;
      background: var(--primary);
      border-radius: 2px;
    }

    .timeline-item {
      position: relative;
      margin-bottom: 20px;
      page-break-inside: avoid;
    }

    .timeline-item::before {
      content: '';
      position: absolute;
      left: -26px;
      top: 6px;
      width: 14px;
      height: 14px;
      background: var(--primary);
      border: 3px solid var(--white);
      border-radius: 50%;
      box-shadow: 0 0 0 2px var(--primary);
    }

    .timeline-item .tl-header {
      font-weight: 700;
      font-size: 11pt;
      color: var(--primary);
      margin-bottom: 4px;
    }

    .timeline-item .tl-body {
      font-size: 9.5pt;
      color: var(--text-secondary);
      background: var(--surface);
      padding: 10px 14px;
      border-radius: 6px;
      border: 1px solid var(--border);
    }

    .timeline-item .tl-body ul {
      margin: 6px 0 0 16px;
      padding: 0;
    }

    .timeline-item .tl-body li {
      margin-bottom: 3px;
    }

    /* ============================================
       PRIORITY MATRIX (2x2 Grid)
       ============================================ */
    .matrix {
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: auto auto;
      gap: 2px;
      margin: 15px 0;
      border: 2px solid var(--primary);
      border-radius: 8px;
      overflow: hidden;
    }

    .matrix-cell {
      padding: 14px;
      min-height: 120px;
    }

    .matrix-cell h4 {
      font-size: 9pt;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
      border: none;
      padding: 0;
    }

    .matrix-cell ul {
      list-style: none;
      padding: 0;
    }

    .matrix-cell li {
      font-size: 8.5pt;
      padding: 3px 0;
      border-bottom: 1px solid rgba(0,0,0,0.05);
    }

    .matrix-q1 { background: #FEE2E2; }
    .matrix-q1 h4 { color: var(--score-critical); }
    .matrix-q2 { background: #FEF3C7; }
    .matrix-q2 h4 { color: var(--score-warning); }
    .matrix-q3 { background: #DBEAFE; }
    .matrix-q3 h4 { color: var(--primary-light); }
    .matrix-q4 { background: #ECFDF5; }
    .matrix-q4 h4 { color: var(--score-excellent); }

    /* ============================================
       CALLOUT BOXES
       ============================================ */
    .callout {
      padding: 14px 18px;
      border-radius: 8px;
      margin: 14px 0;
      page-break-inside: avoid;
    }

    .callout-success {
      background: var(--score-excellent-bg);
      border: 1px solid var(--score-excellent);
    }

    .callout-warning {
      background: var(--score-warning-bg);
      border: 1px solid var(--score-warning);
    }

    .callout-danger {
      background: var(--score-critical-bg);
      border: 1px solid var(--score-critical);
    }

    .callout-info {
      background: var(--primary-bg);
      border: 1px solid var(--primary-light);
    }

    .callout strong {
      display: block;
      margin-bottom: 4px;
    }

    /* ============================================
       KPI TABLE
       ============================================ */
    .kpi-table td:nth-child(2),
    .kpi-table td:nth-child(3) {
      font-family: var(--font-mono);
      font-weight: 600;
      text-align: center;
    }

    /* ============================================
       QUICK WINS
       ============================================ */
    .quick-win {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 10px 14px;
      background: var(--score-excellent-bg);
      border: 1px solid var(--score-excellent);
      border-radius: 8px;
      margin-bottom: 10px;
      page-break-inside: avoid;
    }

    .quick-win-num {
      flex-shrink: 0;
      width: 28px;
      height: 28px;
      background: var(--score-excellent);
      color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 11pt;
    }

    .quick-win-content {
      flex: 1;
    }

    .quick-win-content strong {
      font-size: 10.5pt;
    }

    .quick-win-content p {
      font-size: 9pt;
      color: var(--text-secondary);
      margin: 2px 0 0 0;
    }

    /* ============================================
       FOOTER
       ============================================ */
    .report-footer {
      margin-top: 40px;
      padding-top: 20px;
      border-top: 2px solid var(--primary);
      text-align: center;
      font-size: 8.5pt;
      color: var(--text-muted);
    }

    .report-footer strong {
      color: var(--primary);
    }

    /* ============================================
       STATUS INDICATORS
       ============================================ */
    .status-pass::before { content: '✅ '; }
    .status-warn::before { content: '⚠️ '; }
    .status-fail::before { content: '❌ '; }
    .status-info::before { content: 'ℹ️ '; }

    /* ============================================
       UTILITIES
       ============================================ */
    .text-center { text-align: center; }
    .text-right { text-align: right; }
    .mt-20 { margin-top: 20px; }
    .mb-20 { margin-bottom: 20px; }
    .flex { display: flex; }
    .gap-20 { gap: 20px; }
    .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }
  </style>
</head>
<body>
```

### SECTION 1: COVER PAGE

```html
  <!-- ============================================
       COVER PAGE
       ============================================ -->
  <div class="cover">
    <div class="cover-badge">Local SEO Audit Report</div>
    <h1>{BUSINESS_NAME}</h1>
    <p class="subtitle">{WEBSITE_URL}</p>

    <div class="cover-score">
      <!-- OVERALL SCORE GAUGE — Large -->
      <svg width="180" height="180" viewBox="0 0 120 120">
        <circle cx="60" cy="60" r="54" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="10"/>
        <circle cx="60" cy="60" r="54" fill="none"
          stroke="{SCORE_COLOR}"
          stroke-width="10"
          stroke-dasharray="339.29"
          stroke-dashoffset="{339.29 * (1 - OVERALL_SCORE/100)}"
          transform="rotate(-90 60 60)"
          stroke-linecap="round"/>
        <text x="60" y="55" text-anchor="middle" dominant-baseline="central"
          font-size="32" font-weight="800" fill="white">{OVERALL_SCORE}</text>
        <text x="60" y="78" text-anchor="middle"
          font-size="10" fill="rgba(255,255,255,0.7)">OVERALL SCORE</text>
      </svg>
    </div>

    <div class="cover-meta">
      <div><strong>Prepared:</strong> {DATE}</div>
      <div><strong>Location:</strong> {TARGET_LOCATION}</div>
      <div><strong>Auditor:</strong> Local SEO Audit System v1.0</div>
    </div>
  </div>
```

### SECTION 2: TABLE OF CONTENTS

```html
  <!-- ============================================
       TABLE OF CONTENTS
       ============================================ -->
  <div class="toc page-break">
    <h2>Table of Contents</h2>
    <ul class="toc-list">
      <li><span class="toc-num">01</span> Executive Summary <span class="toc-dots"></span></li>
      <li><span class="toc-num">02</span> Score Dashboard <span class="toc-dots"></span></li>
      <li><span class="toc-num">02B</span> LOCAL-IMPACT & SERP-TRUST Scores <span class="toc-dots"></span></li>
      <li><span class="toc-num">03</span> Critical Issues <span class="toc-dots"></span></li>
      <li><span class="toc-num">04</span> Priority Matrix <span class="toc-dots"></span></li>
      <li><span class="toc-num">05</span> Quick Wins <span class="toc-dots"></span></li>
      <li><span class="toc-num">06</span> Competitor Summary <span class="toc-dots"></span></li>
      <li><span class="toc-num">07</span> Action Plans & Roadmap <span class="toc-dots"></span></li>
      <li><span class="toc-num">08</span> KPI Tracking Framework <span class="toc-dots"></span></li>
      <li><span class="toc-num">09</span> Phase-by-Phase Audit Details <span class="toc-dots"></span></li>
      <li><span class="toc-num">10</span> Resource & Budget Recommendations <span class="toc-dots"></span></li>
    </ul>
  </div>
```

### SECTION 3: EXECUTIVE SUMMARY

```html
  <!-- ============================================
       EXECUTIVE SUMMARY
       ============================================ -->
  <div class="section page-break">
    <div class="section-header">
      <h2>01 — Executive Summary</h2>
      <div class="section-sub">{BUSINESS_NAME} • {WEBSITE_URL} • {DATE}</div>
    </div>

    <p>{EXECUTIVE_SUMMARY_PARAGRAPH_1}</p>
    <p>{EXECUTIVE_SUMMARY_PARAGRAPH_2}</p>
    <p>{EXECUTIVE_SUMMARY_PARAGRAPH_3}</p>

    <!-- Key Findings Callouts -->
    <div class="grid-2 mt-20">
      <div class="callout callout-danger">
        <strong>Critical Issues Found: {CRITICAL_COUNT}</strong>
        {CRITICAL_SUMMARY_SENTENCE}
      </div>
      <div class="callout callout-warning">
        <strong>High Priority Items: {HIGH_COUNT}</strong>
        {HIGH_SUMMARY_SENTENCE}
      </div>
      <div class="callout callout-success">
        <strong>Quick Wins Available: {QUICKWIN_COUNT}</strong>
        {QUICKWIN_SUMMARY_SENTENCE}
      </div>
      <div class="callout callout-info">
        <strong>Strengths Identified: {STRENGTHS_COUNT}</strong>
        {STRENGTHS_SUMMARY_SENTENCE}
      </div>
    </div>
  </div>
```

### SECTION 4: SCORE DASHBOARD

```html
  <!-- ============================================
       SCORE DASHBOARD
       ============================================ -->
  <div class="section page-break">
    <div class="section-header">
      <h2>02 — Score Dashboard</h2>
      <div class="section-sub">Performance across all audit dimensions</div>
    </div>

    <!-- Overall Score (centered, large) -->
    <div class="score-dashboard">
      <div class="overall">
        <div class="gauge-overall">
          <svg width="160" height="160" viewBox="0 0 120 120">
            <circle cx="60" cy="60" r="54" fill="none" stroke="#E5E7EB" stroke-width="10"/>
            <circle cx="60" cy="60" r="54" fill="none"
              stroke="{OVERALL_SCORE_COLOR}"
              stroke-width="10"
              stroke-dasharray="339.29"
              stroke-dashoffset="{CALC: 339.29 * (1 - OVERALL_SCORE/100)}"
              transform="rotate(-90 60 60)"
              stroke-linecap="round"/>
            <text x="60" y="52" text-anchor="middle" dominant-baseline="central"
              font-size="30" font-weight="800" fill="var(--text-primary)">{OVERALL_SCORE}</text>
            <text x="60" y="75" text-anchor="middle"
              font-size="9" fill="var(--text-secondary)" font-weight="600">OVERALL</text>
          </svg>
          <div class="gauge-label">Overall Health Score</div>
        </div>
      </div>

      <!-- Sub-Score Gauges (8 total in 3-column grid) -->
      <!-- REPEAT FOR EACH: Technical, On-Page, Content, Local SEO, Authority, AI Visibility, UX/CRO, Reputation -->
      <div class="gauge-card">
        <svg width="100" height="100" viewBox="0 0 120 120">
          <circle cx="60" cy="60" r="54" fill="none" stroke="#E5E7EB" stroke-width="8"/>
          <circle cx="60" cy="60" r="54" fill="none"
            stroke="{SUB_SCORE_COLOR}"
            stroke-width="8"
            stroke-dasharray="339.29"
            stroke-dashoffset="{CALC: 339.29 * (1 - SUB_SCORE/100)}"
            transform="rotate(-90 60 60)"
            stroke-linecap="round"/>
          <text x="60" y="55" text-anchor="middle" dominant-baseline="central"
            font-size="28" font-weight="700" fill="var(--text-primary)">{SUB_SCORE}</text>
          <text x="60" y="80" text-anchor="middle"
            font-size="9" fill="var(--text-secondary)">/100</text>
        </svg>
        <div class="gauge-label">{SUB_SCORE_LABEL}</div>
      </div>
      <!-- END REPEAT -->
    </div>
  </div>
```

### SECTION 4B: PROPRIETARY FRAMEWORK DASHBOARD

```html
  <!-- ============================================
       PROPRIETARY FRAMEWORK SCORES
       ============================================ -->
  <div class="section page-break">
    <div class="section-header">
      <h2>02B — Proprietary Framework Scores</h2>
      <div class="section-sub">LOCAL-IMPACT & SERP-TRUST Assessment</div>
    </div>

    <!-- SEO Health Index (combined master score) -->
    <div style="text-align: center; margin-bottom: 30px;">
      <div style="font-size: 10pt; font-weight: 600; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;">SEO Health Index</div>
      <svg width="180" height="180" viewBox="0 0 120 120">
        <circle cx="60" cy="60" r="54" fill="none" stroke="#E5E7EB" stroke-width="10"/>
        <circle cx="60" cy="60" r="54" fill="none"
          stroke="{SEO_HEALTH_COLOR}"
          stroke-width="10"
          stroke-dasharray="339.29"
          stroke-dashoffset="{CALC: 339.29 * (1 - SEO_HEALTH_INDEX/100)}"
          transform="rotate(-90 60 60)"
          stroke-linecap="round"/>
        <text x="60" y="50" text-anchor="middle" dominant-baseline="central"
          font-size="32" font-weight="800" fill="var(--text-primary)">{SEO_HEALTH_INDEX}</text>
        <text x="60" y="72" text-anchor="middle"
          font-size="10" fill="var(--text-secondary)" font-weight="600">Grade: {SEO_HEALTH_GRADE}</text>
      </svg>
      <div style="font-size: 8.5pt; color: var(--text-muted); margin-top: 8px;">LOCAL-IMPACT (55%) + SERP-TRUST (45%)</div>
    </div>

    <!-- Two-column framework gauges -->
    <div class="grid-2">
      <!-- LOCAL-IMPACT Score -->
      <div style="text-align: center; padding: 20px; background: var(--surface); border-radius: 10px; border: 1px solid var(--border);">
        <div style="font-size: 9pt; font-weight: 700; color: var(--primary); text-transform: uppercase; letter-spacing: 0.5px;">LOCAL-IMPACT</div>
        <div style="font-size: 7.5pt; color: var(--text-muted); margin-bottom: 10px;">60-Item Local Presence Assessment</div>
        <svg width="120" height="120" viewBox="0 0 120 120">
          <circle cx="60" cy="60" r="54" fill="none" stroke="#E5E7EB" stroke-width="8"/>
          <circle cx="60" cy="60" r="54" fill="none"
            stroke="{LOCAL_IMPACT_COLOR}"
            stroke-width="8"
            stroke-dasharray="339.29"
            stroke-dashoffset="{CALC: 339.29 * (1 - LOCAL_IMPACT_SCORE/100)}"
            transform="rotate(-90 60 60)"
            stroke-linecap="round"/>
          <text x="60" y="55" text-anchor="middle" dominant-baseline="central"
            font-size="28" font-weight="700" fill="var(--text-primary)">{LOCAL_IMPACT_SCORE}</text>
          <text x="60" y="78" text-anchor="middle"
            font-size="9" fill="var(--text-secondary)">Grade: {LOCAL_IMPACT_GRADE}</text>
        </svg>
      </div>

      <!-- SERP-TRUST Score -->
      <div style="text-align: center; padding: 20px; background: var(--surface); border-radius: 10px; border: 1px solid var(--border);">
        <div style="font-size: 9pt; font-weight: 700; color: var(--primary); text-transform: uppercase; letter-spacing: 0.5px;">SERP-TRUST</div>
        <div style="font-size: 7.5pt; color: var(--text-muted); margin-bottom: 10px;">50-Item Search Trust Assessment</div>
        <svg width="120" height="120" viewBox="0 0 120 120">
          <circle cx="60" cy="60" r="54" fill="none" stroke="#E5E7EB" stroke-width="8"/>
          <circle cx="60" cy="60" r="54" fill="none"
            stroke="{SERP_TRUST_COLOR}"
            stroke-width="8"
            stroke-dasharray="339.29"
            stroke-dashoffset="{CALC: 339.29 * (1 - SERP_TRUST_SCORE/100)}"
            transform="rotate(-90 60 60)"
            stroke-linecap="round"/>
          <text x="60" y="55" text-anchor="middle" dominant-baseline="central"
            font-size="28" font-weight="700" fill="var(--text-primary)">{SERP_TRUST_SCORE}</text>
          <text x="60" y="78" text-anchor="middle"
            font-size="9" fill="var(--text-secondary)">Grade: {SERP_TRUST_GRADE}</text>
        </svg>
      </div>
    </div>

    <!-- Dimension Breakdown Bars -->
    <h3>LOCAL-IMPACT Dimensions</h3>
    <div class="bar-chart">
      <!-- REPEAT for each LOCAL-IMPACT dimension: L, O, C, A, L2, I, P, T -->
      <div class="bar-row">
        <span class="bar-label">{DIMENSION_NAME}</span>
        <div class="bar-track"><div class="bar-fill client" style="width: {DIMENSION_PCT}%">{DIMENSION_SCORE}/{DIMENSION_MAX}</div></div>
      </div>
      <!-- END REPEAT -->
    </div>

    <h3>SERP-TRUST Dimensions</h3>
    <div class="bar-chart">
      <!-- REPEAT for each SERP-TRUST dimension: T, R, U, S, T2 -->
      <div class="bar-row">
        <span class="bar-label">{DIMENSION_NAME}</span>
        <div class="bar-track"><div class="bar-fill client" style="width: {DIMENSION_PCT}%">{DIMENSION_SCORE}/{DIMENSION_MAX}</div></div>
      </div>
      <!-- END REPEAT -->
    </div>

    <!-- Veto Check Status -->
    <h3>Veto Checks</h3>
    <div class="grid-2">
      <div class="no-break">
        <h4>LOCAL-IMPACT Vetoes</h4>
        <!-- REPEAT for each veto -->
        <div style="padding: 4px 0; font-size: 9pt;">
          <span class="{status-pass|status-fail}">{VETO_DESCRIPTION}</span>
        </div>
        <!-- END REPEAT -->
      </div>
      <div class="no-break">
        <h4>SERP-TRUST Vetoes</h4>
        <!-- REPEAT for each veto -->
        <div style="padding: 4px 0; font-size: 9pt;">
          <span class="{status-pass|status-fail}">{VETO_DESCRIPTION}</span>
        </div>
        <!-- END REPEAT -->
      </div>
    </div>

    <!-- Competitor Framework Comparison -->
    <h3>Competitor Framework Comparison</h3>
    <table>
      <thead>
        <tr>
          <th>Framework</th>
          <th>{BUSINESS_NAME}</th>
          <th>{COMP_1}</th>
          <th>{COMP_2}</th>
          <th>{COMP_3}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>LOCAL-IMPACT</td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
        </tr>
        <tr>
          <td>SERP-TRUST</td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
        </tr>
        <tr style="font-weight: 700;">
          <td>SEO Health Index</td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
          <td><span class="badge {BADGE}">{SCORE}</span></td>
        </tr>
      </tbody>
    </table>
  </div>
```

### SECTION 5: CRITICAL ISSUES

```html
  <!-- ============================================
       CRITICAL ISSUES
       ============================================ -->
  <div class="section break-before">
    <div class="section-header">
      <h2>03 — Critical Issues</h2>
      <div class="section-sub">Fix these immediately — they are blocking your SEO performance</div>
    </div>

    <!-- REPEAT for each critical issue -->
    <div class="issue-card critical">
      <div class="issue-title">{ISSUE_TITLE}</div>
      <div class="issue-desc">{ISSUE_DESCRIPTION_AND_FIX_STEPS}</div>
      <div class="issue-meta">
        <span class="badge badge-critical">Critical</span>
        <span class="badge badge-effort">{EFFORT_ESTIMATE}</span>
        <span class="badge badge-info">{AUDIT_PHASE}</span>
      </div>
    </div>
    <!-- END REPEAT -->

    <!-- Then HIGH priority issues -->
    <h3>High Priority Issues</h3>
    <!-- REPEAT for each high issue using class="issue-card high" -->
  </div>
```

### SECTION 6: PRIORITY MATRIX

```html
  <!-- ============================================
       PRIORITY MATRIX
       ============================================ -->
  <div class="section break-before">
    <div class="section-header">
      <h2>04 — Priority Matrix</h2>
      <div class="section-sub">Impact vs Effort — focus on the top-left quadrant first</div>
    </div>

    <div class="matrix">
      <div class="matrix-cell matrix-q1">
        <h4>High Impact / Low Effort (Do First)</h4>
        <ul>
          <!-- Quick wins — highest priority -->
          <li>{ITEM}</li>
        </ul>
      </div>
      <div class="matrix-cell matrix-q2">
        <h4>High Impact / High Effort (Plan & Schedule)</h4>
        <ul>
          <li>{ITEM}</li>
        </ul>
      </div>
      <div class="matrix-cell matrix-q4">
        <h4>Low Impact / Low Effort (Fill In Gaps)</h4>
        <ul>
          <li>{ITEM}</li>
        </ul>
      </div>
      <div class="matrix-cell matrix-q3">
        <h4>Low Impact / High Effort (Deprioritize)</h4>
        <ul>
          <li>{ITEM}</li>
        </ul>
      </div>
    </div>
  </div>
```

### SECTION 7: QUICK WINS

```html
  <!-- ============================================
       QUICK WINS
       ============================================ -->
  <div class="section break-before">
    <div class="section-header">
      <h2>05 — Quick Wins</h2>
      <div class="section-sub">High-impact fixes you can implement today</div>
    </div>

    <!-- REPEAT for each quick win -->
    <div class="quick-win">
      <div class="quick-win-num">{N}</div>
      <div class="quick-win-content">
        <strong>{WIN_TITLE}</strong>
        <p>{WIN_DESCRIPTION_AND_STEPS}</p>
      </div>
    </div>
    <!-- END REPEAT -->
  </div>
```

### SECTION 8: COMPETITOR SUMMARY

```html
  <!-- ============================================
       COMPETITOR SUMMARY
       ============================================ -->
  <div class="section break-before">
    <div class="section-header">
      <h2>06 — Competitor Summary</h2>
      <div class="section-sub">How you compare to your top competitors</div>
    </div>

    <table>
      <thead>
        <tr>
          <th>Dimension</th>
          <th>{BUSINESS_NAME}</th>
          <th>{COMP_1_NAME}</th>
          <th>{COMP_2_NAME}</th>
          <th>{COMP_3_NAME}</th>
        </tr>
      </thead>
      <tbody>
        <!-- REPEAT for each comparison dimension -->
        <tr>
          <td>{DIMENSION}</td>
          <td><span class="badge {BADGE_CLASS}">{SCORE}/10</span></td>
          <td><span class="badge {BADGE_CLASS}">{SCORE}/10</span></td>
          <td><span class="badge {BADGE_CLASS}">{SCORE}/10</span></td>
          <td><span class="badge {BADGE_CLASS}">{SCORE}/10</span></td>
        </tr>
        <!-- END REPEAT -->
      </tbody>
    </table>

    <!-- CSS Bar Chart Comparison -->
    <h3>Score Comparison</h3>
    <div class="bar-chart">
      <!-- REPEAT for each dimension -->
      <div style="margin-bottom: 14px;">
        <div style="font-size: 9pt; font-weight: 600; margin-bottom: 4px;">{DIMENSION}</div>
        <div class="bar-row">
          <span class="bar-label">{BUSINESS}</span>
          <div class="bar-track"><div class="bar-fill client" style="width: {PERCENT}%">{SCORE}</div></div>
        </div>
        <div class="bar-row">
          <span class="bar-label">{COMP_1}</span>
          <div class="bar-track"><div class="bar-fill comp1" style="width: {PERCENT}%">{SCORE}</div></div>
        </div>
        <div class="bar-row">
          <span class="bar-label">{COMP_2}</span>
          <div class="bar-track"><div class="bar-fill comp2" style="width: {PERCENT}%">{SCORE}</div></div>
        </div>
      </div>
      <!-- END REPEAT -->
    </div>
  </div>
```

### SECTION 9: ACTION PLAN ROADMAP

```html
  <!-- ============================================
       ACTION PLANS & ROADMAP
       ============================================ -->
  <div class="section break-before">
    <div class="section-header">
      <h2>07 — Action Plans & Roadmap</h2>
      <div class="section-sub">Your step-by-step path to local SEO dominance</div>
    </div>

    <h3>30-Day Action Plan</h3>
    <div class="timeline">
      <!-- REPEAT for each week -->
      <div class="timeline-item">
        <div class="tl-header">Week {N}: {WEEK_FOCUS}</div>
        <div class="tl-body">
          <ul>
            <li>{TASK_1}</li>
            <li>{TASK_2}</li>
            <li>{TASK_3}</li>
          </ul>
        </div>
      </div>
      <!-- END REPEAT -->
    </div>

    <h3>90-Day Strategic Plan</h3>
    <div class="timeline">
      <!-- REPEAT for each month -->
      <div class="timeline-item">
        <div class="tl-header">Month {N}: {MONTH_FOCUS}</div>
        <div class="tl-body">
          <ul>
            <li>{TASK}</li>
          </ul>
        </div>
      </div>
      <!-- END REPEAT -->
    </div>

    <h3>6-Month & 12-Month Vision</h3>
    <!-- Similar timeline for 6-month and 12-month milestones -->
  </div>
```

### SECTION 10: KPI FRAMEWORK

```html
  <!-- ============================================
       KPI TRACKING FRAMEWORK
       ============================================ -->
  <div class="section break-before">
    <div class="section-header">
      <h2>08 — KPI Tracking Framework</h2>
      <div class="section-sub">Metrics to track progress and measure ROI</div>
    </div>

    <table class="kpi-table">
      <thead>
        <tr>
          <th>KPI</th>
          <th>Current</th>
          <th>30-Day Target</th>
          <th>90-Day Target</th>
          <th>How to Measure</th>
        </tr>
      </thead>
      <tbody>
        <!-- REPEAT for each KPI -->
        <tr>
          <td>{KPI_NAME}</td>
          <td>{CURRENT_VALUE}</td>
          <td>{TARGET_30D}</td>
          <td>{TARGET_90D}</td>
          <td>{MEASUREMENT_METHOD}</td>
        </tr>
        <!-- END REPEAT -->
      </tbody>
    </table>
  </div>
```

### SECTION 11: PHASE-BY-PHASE DETAILS

```html
  <!-- ============================================
       PHASE-BY-PHASE AUDIT DETAILS
       ============================================ -->
  <!-- REPEAT for each completed audit phase -->
  <div class="section break-before">
    <div class="section-header">
      <h2>09.{N} — {PHASE_NAME}</h2>
      <div class="section-sub">Phase Score: {PHASE_SCORE}/100 • {STATUS_SUMMARY}</div>
    </div>

    <!-- Phase score gauge (small, inline) -->
    <div style="text-align: center; margin-bottom: 20px;">
      <svg width="80" height="80" viewBox="0 0 120 120">
        <circle cx="60" cy="60" r="54" fill="none" stroke="#E5E7EB" stroke-width="8"/>
        <circle cx="60" cy="60" r="54" fill="none"
          stroke="{PHASE_SCORE_COLOR}" stroke-width="8"
          stroke-dasharray="339.29"
          stroke-dashoffset="{CALC}"
          transform="rotate(-90 60 60)" stroke-linecap="round"/>
        <text x="60" y="60" text-anchor="middle" dominant-baseline="central"
          font-size="28" font-weight="700">{PHASE_SCORE}</text>
      </svg>
    </div>

    <!-- Phase findings table -->
    <table>
      <thead>
        <tr>
          <th>Status</th>
          <th>Item</th>
          <th>Finding</th>
          <th>Impact</th>
          <th>Priority</th>
        </tr>
      </thead>
      <tbody>
        <!-- REPEAT for each finding in this phase -->
        <tr>
          <td>{STATUS_EMOJI}</td>
          <td>{ITEM_NAME}</td>
          <td>{FINDING_DESCRIPTION}</td>
          <td><span class="badge {BADGE_CLASS}">{IMPACT}</span></td>
          <td>{PRIORITY_TIMEFRAME}</td>
        </tr>
        <!-- END REPEAT -->
      </tbody>
    </table>

    <!-- Phase-specific recommendations -->
    <h3>Recommendations</h3>
    <!-- Issue cards for this phase's recommendations -->
  </div>
  <!-- END REPEAT -->
```

### SECTION 12: RESOURCES & BUDGET

```html
  <!-- ============================================
       RESOURCE & BUDGET RECOMMENDATIONS
       ============================================ -->
  <div class="section break-before">
    <div class="section-header">
      <h2>10 — Resource & Budget Recommendations</h2>
      <div class="section-sub">Investment needed to implement the audit recommendations</div>
    </div>

    <table>
      <thead>
        <tr>
          <th>Category</th>
          <th>Tasks</th>
          <th>Estimated Hours</th>
          <th>Estimated Cost</th>
          <th>Priority</th>
        </tr>
      </thead>
      <tbody>
        <!-- REPEAT -->
        <tr>
          <td>{CATEGORY}</td>
          <td>{TASK_SUMMARY}</td>
          <td>{HOURS}</td>
          <td>{COST_RANGE}</td>
          <td><span class="badge {BADGE_CLASS}">{PRIORITY}</span></td>
        </tr>
        <!-- END REPEAT -->
      </tbody>
    </table>
  </div>
```

### SECTION 13: FOOTER / BACK PAGE

```html
  <!-- ============================================
       REPORT FOOTER
       ============================================ -->
  <div class="report-footer break-before" style="padding-top: 200px;">
    <div style="font-size: 14pt; font-weight: 700; color: var(--primary); margin-bottom: 10px;">
      Local SEO Audit System
    </div>
    <p>This report was generated by the Local SEO Audit System plugin for Claude Code.</p>
    <p style="margin-top: 20px;">
      <strong>Business:</strong> {BUSINESS_NAME}<br>
      <strong>Website:</strong> {WEBSITE_URL}<br>
      <strong>Date:</strong> {DATE}<br>
      <strong>Report Version:</strong> 1.0
    </p>
    <p style="margin-top: 30px; font-size: 8pt;">
      This audit is based on publicly available data and AI-assisted analysis.
      Recommendations should be reviewed by qualified professionals before implementation.
      Results may vary based on implementation quality, competitive actions, and search engine algorithm changes.
    </p>
  </div>

</body>
</html>
```

---

## SVG GAUGE COLOR FORMULA

When generating gauges, compute the color based on score:

- **0-39**: `var(--score-critical)` / `#DC2626` (Red)
- **40-59**: `var(--score-warning)` / `#D97706` (Orange)
- **60-79**: `var(--score-good)` / `#10B981` (Green)
- **80-100**: `var(--score-excellent)` / `#059669` (Dark Green)

Compute `stroke-dashoffset` as: `339.29 * (1 - score / 100)`

Example: Score 72 → `stroke-dashoffset = 339.29 * (1 - 0.72) = 95.0`

---

## IMPORTANT RULES

1. **Populate ALL placeholders** with real audit data from the conversation. Never leave `{PLACEHOLDER}` in the output.
2. **Compute all SVG values** — `stroke-dashoffset` must be calculated, not left as formulas.
3. **Include all completed phases** — if only 5 phases were done, only include those 5 in the phase-by-phase section.
4. **Use the exact CSS classes** defined above for proper styling.
5. **Keep `page-break-inside: avoid`** on issue cards and quick wins to prevent awkward page splits.
6. **Test the HTML file** — after writing, suggest the user open it in a browser to preview before PDF conversion.

---

## Priority Matrix

| Task | Impact (1–5) | Feasibility (1–5) | Priority | Effort |
|---|---|---|---|---|
| Cover page with score gauge + grade | 5 | 4 | 20 | 30–60 min |
| Dashboard with dimension breakdowns | 5 | 4 | 20 | 30–60 min |
| Color-coded issue cards (Critical/High/Med/Low) | 5 | 4 | 20 | 1–2 hrs |
| Priority matrix (Impact × Feasibility) | 4 | 5 | 20 | 30 min |
| Competitor comparison table | 4 | 4 | 16 | 30 min |
| 30/90-day roadmap section | 4 | 4 | 16 | 30 min |
| Quick wins summary (top 5) | 4 | 5 | 20 | 15 min |
| Phase-by-phase summary table | 3 | 5 | 15 | 30 min |
| SVG gauge charts per dimension | 3 | 3 | 9 | 30–60 min |
| AI visibility / AIO findings callout | 4 | 5 | 20 | 15 min |

---

## Output Handoff

After generating each PDF, confirm to user:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PDF Generated: [phase-N-slug.pdf]
Location: {REPORTS_DIR}/[filename].pdf
File size: [X.X MB]
Pages: [X]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Key consumers:**
- Client/stakeholder — primary audience for PDF deliverable
- `output/report-generation` — master-report.md feeds this skill
- `cross-cutting/local-impact-auditor` — score data for dashboard charts
- `cross-cutting/serp-trust-auditor` — score data for SERP-TRUST gauge

---

## PDF Generation Tool Reference

### Generation Methods (Priority Order)

| Method | Tool | Command | When to Use | Reliability |
|---|---|---|---|---|
| Python script (preferred) | `generate_pdf.py` | `python3 scripts/generate_pdf.py --html [path].html` | Always — handles Chrome detection + fallback | Highest |
| Chrome headless | Google Chrome | `"/Applications/Google Chrome.app/..." --headless=new --print-to-pdf=[path]` | Chrome confirmed available | High |
| WeasyPrint | Python library | `weasyprint [input.html] [output.pdf]` | Fallback if Chrome fails | Medium |
| wkhtmltopdf | System binary | `wkhtmltopdf [input.html] [output.pdf]` | Legacy fallback | Low |

### Per-Phase PDF Naming Convention

| Phase | Phase Name | PDF Filename |
|---|---|---|
| 0 | Intake | `phase-0-intake.pdf` |
| 1 | Competitor Analysis | `phase-1-competitors.pdf` |
| 2 | Technical SEO | `phase-2-technical-seo.pdf` |
| 3 | On-Page SEO | `phase-3-onpage-seo.pdf` |
| 4 | Content Audit | `phase-4-content-audit.pdf` |
| 5 | Content Gaps | `phase-5-content-gaps.pdf` |
| 6 | Keyword Gaps | `phase-6-keyword-gaps.pdf` |
| 7 | Topical Gaps | `phase-7-topical-gaps.pdf` |
| 8 | Topical Authority | `phase-8-topical-authority.pdf` |
| 9 | Entity Audit | `phase-9-entity-audit.pdf` |
| 10 | Speed | `phase-10-speed.pdf` |
| 11 | Local SEO | `phase-11-local-seo.pdf` |
| 12 | Backlinks | `phase-12-backlinks.pdf` |
| 13 | Social Media | `phase-13-social.pdf` |
| 14 | AI SEO | `phase-14-ai-seo.pdf` |
| 15 | Reputation | `phase-15-reputation.pdf` |
| 16 | Brand SERP | `phase-16-brand-serp.pdf` |
| 17 | CRO | `phase-17-cro.pdf` |
| 18 | Voice Search | `phase-18-voice.pdf` |
| 19 | Accessibility | `phase-19-accessibility.pdf` |
| 20 | Penalty Check | `phase-20-penalty-check.pdf` |
| 21 | Multi-Location | `phase-21-multi-location.pdf` |
| Scoring | LOCAL-IMPACT | `local-impact-score.pdf` |
| Scoring | SERP-TRUST | `serp-trust-score.pdf` |
| Final | Master Report | `master-report.pdf` |

### PDF Quality Checklist

| Element | Required | Design Spec |
|---|---|---|
| Cover page | Yes | Phase number, business name, URL, date, score badge |
| Score gauge chart | Yes | SVG donut chart — green ≥80, amber 60–79, red <60 |
| Issue cards (Critical/High/Medium/Low) | Yes | Color-coded left border: red/orange/yellow/green |
| Priority matrix | Yes | Impact × Feasibility table, sorted by priority score |
| Competitor comparison | Yes | Client vs. top 3 competitors, highlight wins/losses |
| Quick wins box | Yes | Top 3 actions, effort <1 hr, expected impact |
| Next phase pointer | Yes | Footer on last page: "Next: Phase [N] — [Name]" |
| INP/CWV callout | Where relevant | 2025 thresholds: INP <200ms, LCP <2.5s, CLS <0.1 |
