---
description: Generate a professional PDF report from completed audit findings
argument-hint: [output-filename]
---

Generate a professionally designed PDF audit report from all completed audit findings.

Follow the pdf-report skill instructions exactly:

1. **Aggregate Data**: Collect all audit findings, scores, issues, and recommendations
   from the conversation context. Organize by phase.

2. **Generate HTML**: Using the complete HTML template from the pdf-report skill,
   generate a fully populated HTML file. Replace ALL placeholders with real data.
   Compute all SVG gauge values (stroke-dashoffset = 339.29 * (1 - score/100)).

3. **Write HTML File**: Save to `{REPORTS_DIR}/{business-name-slug}-seo-audit-{date}.html`
   Create the reports/ directory if it doesn't exist.

4. **Convert to PDF**: Always use the cross-platform Python script:
   ```
   python3 scripts/generate_pdf.py --html {REPORTS_DIR}/{filename}.html
   ```
   The script auto-detects Chrome/Chromium on macOS, Linux, and Windows.

5. **Report Output**: Tell the user the PDF path and file size.
   Also mention the HTML file is available for customization.

If $ARGUMENTS is provided, use it as the output filename (without extension).
Otherwise, use the format: {business-name-slug}-seo-audit-{YYYY-MM-DD}

IMPORTANT: The report must be visually stunning. Use the full design system
from the pdf-report skill: SVG gauge charts, color-coded issue cards,
CSS bar charts, timeline roadmaps, and professional tables.
