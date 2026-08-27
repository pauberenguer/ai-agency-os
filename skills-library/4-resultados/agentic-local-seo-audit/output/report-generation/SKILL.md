---
name: report-generation
description: >
  Master audit report compilation. Activates when compiling the final audit
  report, creating deliverables, producing action plans, building roadmaps, or
  summarizing all audit findings into a single master document.
  Output: {AUDIT_DIR}/master-report.md
---

# Master Audit Report — Compilation Skill

## Executive Summary

The master report is the culmination of all 21 audit phases — the client's definitive reference document for the next 6–12 months of SEO work. A well-structured master report delivers: clear business impact framing (not just technical findings), a prioritized action plan with effort estimates, measurable KPIs, and a roadmap stakeholders can act on. In 2025, the master report must explicitly address AI visibility (AI Overviews, ChatGPT, Perplexity) as a separate strategic dimension — clients increasingly ask "why aren't we showing up in AI answers?"

**2025 master report requirements:**
- Include SEO Health Index = (LOCAL-IMPACT × 0.55) + (SERP-TRUST × 0.45) as the headline metric
- AI Overviews section mandatory: AIO appears for 20–35% of local service queries
- All CWV data must use 2025 thresholds: INP < 200ms (replaced FID March 2024)
- Include GBP performance data: review velocity, Q&A status, photo count vs. 100+ benchmark
- ChatGPT/Perplexity visibility test results must appear in AI visibility section

---

## Tools for This Phase

| Tool | Purpose | Cost |
|------|---------|------|
| `python3 scripts/report_compiler.py` | Compile all phase .md files → master-report.md | Free (local) |
| `python3 scripts/score_calculator.py --both` | Compute LOCAL-IMPACT + SERP-TRUST + SEO Health Index | Free (local) |
| `python3 scripts/generate_pdf.py` | Convert master HTML → PDF (Chrome or WeasyPrint) | Free (local) |
| `python3 scripts/audit_status.py` | Verify all 21 phases complete before compiling | Free (local) |
| **Google Search Console** | Page-level data for KPI baseline (current traffic) | Free |
| **Ahrefs / SEMrush** | DR, traffic estimate, keyword count for executive summary | Paid |

---

## Step 1: Read Project Context + Compile All Findings

```bash
# Compile all phase findings into structured master report data
python3 scripts/report_compiler.py --project {PROJECT_DIR} --output {AUDIT_DIR}/master-report.md
```

Then read all individual phase files to enrich the compiled report:
- `{AUDIT_DIR}/intake-data.md`
- `{AUDIT_DIR}/competitor-profiles.md`
- `{AUDIT_DIR}/local-impact-scores.md`
- `{AUDIT_DIR}/serp-trust-scores.md`
- All other `{AUDIT_DIR}/*.md` files

---

## Master Report Structure

### Section 1: Executive Summary (3-5 paragraphs)
- Business overview and market position
- Overall site health narrative (not just score — what it means for the business)
- Top 3 critical issues that are costing rankings/leads RIGHT NOW
- Top 3 opportunities with highest revenue potential
- Overall trajectory: what 6-12 months of action can achieve

### Section 2: Overall Site Health Score

```
Overall Site Health: [X]/100   Grade: [A-F]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Technical:    [X]/100    Local SEO:    [X]/100
On-Page:      [X]/100    AI Visibility: [X]/100
Content:      [X]/100    Authority:     [X]/100
Speed/CWV:    [X]/100    Reputation:    [X]/100
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Section 3: Proprietary Framework Scores

#### LOCAL-IMPACT Score: [X]/100 — Grade: [X]
(Load from `{AUDIT_DIR}/local-impact-scores.md`)

```
Dimension Breakdown:
L  Listing Quality       [XX/30]  ████████░░  [X%]
O  Online Reviews         [XX/30]  ███████░░░  [X%]
C  Citation Consistency   [XX/30]  █████░░░░░  [X%]
A  Authority Signals      [XX/30]  ████████░░  [X%]
L2 Local Content          [XX/15]  ██████░░░░  [X%]
I  Integrated Visibility  [XX/15]  ███████░░░  [X%]
P  Performance            [XX/15]  ████████░░  [X%]
T  Tracking               [XX/15]  █████░░░░░  [X%]

Veto Checks: [status of all 6 vetoes]
```

Or compute with: `python3 scripts/score_calculator.py --local-impact {AUDIT_DIR}/local-impact-scores.md`

#### SERP-TRUST Score: [X]/100 — Grade: [X]
(Load from `{AUDIT_DIR}/serp-trust-scores.md`)

```
Dimension Breakdown:
T  Technical Foundation   [XX/40]  ████████░░  [X%]
R  Ranking Signals        [XX/40]  ███████░░░  [X%]
U  User Experience        [XX/40]  █████░░░░░  [X%]
S  Search Authority       [XX/40]  ████████░░  [X%]
T2 Trust & AI Readiness   [XX/40]  ██████░░░░  [X%]

Veto Checks: [status of all 7 vetoes]
```

Or compute with: `python3 scripts/score_calculator.py --serp-trust {AUDIT_DIR}/serp-trust-scores.md`

#### SEO Health Index: [X]/100 — Grade: [X]
```
SEO Health Index = (LOCAL-IMPACT [X] × 0.55) + (SERP-TRUST [X] × 0.45) = [X]/100
Status: Excellent | Good | Fair | Poor | Critical
```

Or compute with: `python3 scripts/score_calculator.py --both --li-file {AUDIT_DIR}/local-impact-scores.md --st-file {AUDIT_DIR}/serp-trust-scores.md`

---

### Section 4: Critical Issues — Fix Immediately

All CRITICAL priority issues from all phases, consolidated:

| # | Issue | Phase | Impact | Est. Fix Time |
|---|-------|-------|--------|--------------|
| 1 | [issue] | [Phase X] | Revenue loss / Rankings loss | [X hours] |
| 2 | [issue] | [Phase X] | [impact] | [X hours] |
...

Expand each critical issue with:
- Root cause
- Specific fix steps
- Expected improvement when fixed
- Effort required

---

### Section 5: Priority Matrix (Impact × Effort Quadrant)

```
HIGH IMPACT, LOW EFFORT (Do First — Quick Wins):
  • [issue/opportunity]
  • [issue/opportunity]
  • [issue/opportunity]

HIGH IMPACT, HIGH EFFORT (Strategic Priorities):
  • [issue/opportunity]
  • [issue/opportunity]

LOW IMPACT, LOW EFFORT (Fill When Available):
  • [issue/opportunity]

LOW IMPACT, HIGH EFFORT (Deprioritize):
  • [issue/opportunity]
```

---

### Section 6: Quick Wins — Implement Today/This Week

Maximum 15 quick wins, ordered by impact:

| # | Quick Win | Page/Section | Expected Impact | Time to Implement |
|---|-----------|-------------|----------------|-----------------|
| 1 | [specific action] | [URL or section] | [specific outcome] | < 1 hour |
| 2 | [specific action] | [URL or section] | [specific outcome] | 1-2 hours |
...

---

### Section 7: 30-Day Action Plan (Weekly Breakdown)

**Week 1 — Critical Fixes:**
- [ ] [Critical issue 1] — Owner: [team/contractor] — Expected: [X improvement]
- [ ] [Critical issue 2]
- [ ] [Quick wins batch]

**Week 2 — Technical & On-Page:**
- [ ] [Technical fix]
- [ ] [On-page optimization batch]
- [ ] [Content update]

**Week 3 — Local & Content:**
- [ ] [GBP optimization]
- [ ] [Citation submissions]
- [ ] [New content piece]

**Week 4 — Authority & Measurement:**
- [ ] [Link building outreach]
- [ ] [Analytics/tracking setup]
- [ ] [Review generation system launch]

---

### Section 8: 90-Day Strategic Plan

**Month 1:** Foundation — Fix critical issues, establish tracking, launch content engine
**Month 2:** Acceleration — Content at scale, link acquisition, local authority building
**Month 3:** Optimization — Refine based on data, scale what's working, close keyword gaps

---

### Section 9: 6-Month Roadmap

Quarterly milestone targets with specific KPIs:
- [KPI 1]: [current] → [target at month 3] → [target at month 6]
- [KPI 2]: [current] → [target] → [target]
- Rankings, traffic, leads, review count/rating, LOCAL-IMPACT score

---

### Section 10: 12-Month Vision

Where can this business be in 12 months with consistent execution?
- Market position vs. current top competitors
- Estimated traffic increase (%)
- Estimated lead volume increase
- LOCAL-IMPACT score projection
- Topical authority level

---

### Section 11: KPI Tracking Framework

| KPI | Current | Month 1 Target | Month 3 Target | Month 6 Target | Tracking Tool |
|-----|---------|---------------|---------------|---------------|--------------|
| Organic traffic | [X/mo] | | | | GA4 |
| Local pack positions | [rank] | | | | GBP Insights |
| Google review count | [X] | | | | GBP |
| Google avg. rating | [X.X] | | | | GBP |
| Phone call conversions | [X/mo] | | | | CallTracking |
| Form submissions | [X/mo] | | | | GA4 |
| LOCAL-IMPACT score | [X] | | | | Quarterly audit |
| SERP-TRUST score | [X] | | | | Quarterly audit |
| SEO Health Index | [X] | | | | Quarterly audit |

---

### Section 12: Resource & Budget Recommendations

By priority:
1. **Immediate fixes** (can be done in-house): [list] — [est. hours]
2. **Technical implementation** (developer needed): [list] — [est. cost]
3. **Content creation**: [X pieces/month] — [in-house vs. content agency cost]
4. **Link building / PR**: [budget recommendation]
5. **Tools needed**: [specific tools + costs]
6. **Total estimated investment**: [$X-Y/month]

---

### Section 13: Competitor Summary

| Competitor | Overall Score | Key Advantage | Biggest Gap vs. Client |
|-----------|--------------|--------------|----------------------|
| [Comp 1] | [X/100] | [what they do best] | [where they beat client] |
| [Comp 2] | [X/100] | | |
| [Comp 3] | [X/100] | | |

LOCAL-IMPACT + SERP-TRUST competitor scores included if scored.

---

### Section 14: Phase-by-Phase Detail Summary

One paragraph + key findings per phase, with score and status.

---

## PDF Export

After compiling master report, generate the final PDF:

```bash
# Convert HTML master report to PDF
python3 scripts/generate_pdf.py --html {REPORTS_DIR}/master-report.html

# Or use Chrome directly
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-sandbox --print-to-pdf-no-header \
  --print-to-pdf="{REPORTS_DIR}/master-report.pdf" \
  "file:///absolute/path/{REPORTS_DIR}/master-report.html"
```

**PDF Design for Master Report:**
- Professional cover page with all scores and business info
- Executive dashboard with gauge charts for all key scores
- Phase-by-phase summary with color-coded status badges
- Roadmap timeline visualization
- Priority matrix quadrant chart

Write final report HTML to `{REPORTS_DIR}/master-report.html`.
Write final PDF to `{REPORTS_DIR}/master-report.pdf`.
Write markdown to `{AUDIT_DIR}/master-report.md`.

---

## Report Quality Checklist (Before Delivering)

| Check | Standard | Status |
|-------|---------|--------|
| All 21 phases included (or N/A noted) | Required | ✅/❌ |
| SEO Health Index computed and displayed | Required | ✅/❌ |
| LOCAL-IMPACT + SERP-TRUST both scored | Required | ✅/❌ |
| AI Overviews section present | Required | ✅/❌ |
| INP used (not FID) in all CWV references | Required | ✅/❌ |
| All recommendations have effort estimates | Required | ✅/❌ |
| All issues have Impact × Feasibility scores | Required | ✅/❌ |
| Competitor benchmarks present in every section | Required | ✅/❌ |
| 30-day plan broken into weekly tasks | Required | ✅/❌ |
| KPI tracking table with current baselines | Required | ✅/❌ |
| Quick wins list (≤ 1 hour each) | Required | ✅/❌ |
| No placeholder text remaining | Required | ✅/❌ |

---

## Priority Matrix

| Task | Impact (1–5) | Feasibility (1–5) | Priority | Effort |
|------|-------------|-------------------|---------|--------|
| Executive summary (3–5 paragraphs, business framing) | 5 | 4 | 20 | 30–60 min |
| SEO Health Index + framework scores display | 5 | 5 | 25 | 15–30 min |
| Critical issues section (all phases consolidated) | 5 | 4 | 20 | 30–60 min |
| Priority matrix (Impact × Effort quadrant) | 5 | 5 | 25 | 15–30 min |
| 30-day action plan (weekly breakdown) | 5 | 4 | 20 | 30–45 min |
| Quick wins list (top 15, impact-ordered) | 4 | 5 | 20 | 20–30 min |
| KPI tracking framework with baselines | 4 | 4 | 16 | 20–30 min |
| AI visibility section (AIO + ChatGPT + Perplexity) | 4 | 5 | 20 | 20–30 min |
| Competitor summary table | 4 | 4 | 16 | 15–20 min |
| 90-day + 6-month roadmap | 3 | 4 | 12 | 20–30 min |

---

## Output

Write to `{AUDIT_DIR}/master-report.md` with YAML frontmatter:

```yaml
---
skill: output/report-generation
phase: final
date: [YYYY-MM-DD]
business: [Business Name]
url: [URL]
seo_health_index: [X/100]
local_impact_score: [X/100]
serp_trust_score: [X/100]
phases_completed: [X/21]
critical_issues: [X]
high_issues: [X]
quick_wins: [X]
---
```

**Key consumers:**
- `output/pdf-report` — master-report.md → HTML → PDF conversion
- Client/stakeholder — primary deliverable for strategy alignment
- Future audit sessions — baseline for progress measurement
