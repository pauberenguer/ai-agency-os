# Proprietary Scoring Methodology

## Overview

The Local SEO Audit System uses two proprietary scoring frameworks that work together to provide a complete assessment of a local business's search visibility:

| Framework | Focus | Items | Scale | Max Raw | Normalized |
|-----------|-------|-------|-------|---------|------------|
| **LOCAL-IMPACT** | Local presence & visibility | 60 | 0-3 | 180 | 0-100 |
| **SERP-TRUST** | Search engine trust & authority | 50 | 0-4 | 200 | 0-100 |

---

## How the Frameworks Complement Each Other

```
LOCAL-IMPACT                          SERP-TRUST
━━━━━━━━━━━━━━━━                     ━━━━━━━━━━━━━━━━
Listing Quality (L)                   Technical Foundation (T)
Online Reviews (O)                    Ranking Signals (R)
Citation Consistency (C)              User Experience (U)
Authority Signals (A)                 Search Authority (S)
Local Content (L2)                    Trust & AI Readiness (T2)
Integrated Visibility (I)
Performance (P)
Tracking (T)
━━━━━━━━━━━━━━━━                     ━━━━━━━━━━━━━━━━
"Can customers FIND you locally?"     "Does Google TRUST your site?"
```

### When to Use Each

- **LOCAL-IMPACT alone**: Quick GBP/local presence health check
- **SERP-TRUST alone**: Technical and authority audit focus
- **Both together**: Full local SEO audit (recommended for all comprehensive audits)

---

## Combined Score: SEO Health Index

When both frameworks are scored, compute the **SEO Health Index**:

```
SEO Health Index = (LOCAL-IMPACT Score × 0.55) + (SERP-TRUST Score × 0.45)
```

### Why 55/45 Weighting?

For **local businesses**, local presence signals (GBP, reviews, citations) have a slightly higher direct impact on local pack rankings than general organic signals. The 55/45 split reflects this local-first priority. Adjust to 50/50 for businesses where organic rankings matter equally.

### Combined Grade Table

| SEO Health Index | Grade | Assessment |
|-----------------|-------|------------|
| 90-100 | A+ | Market leader — maintain and innovate |
| 80-89 | A | Strong position — optimize edges |
| 70-79 | B+ | Good foundation — clear growth path |
| 60-69 | B | Competitive — address gaps systematically |
| 50-59 | C+ | Below potential — prioritized action needed |
| 40-49 | C | Underperforming — significant work required |
| 30-39 | D | At risk — urgent intervention |
| 0-29 | F | Critical — fundamental rebuild needed |

---

## Scoring Process

### Step 1: Gather Data

Before scoring, collect:
- Website URL and access (fetch homepage + key pages)
- Google Business Profile URL
- Competitor URLs (minimum 3)
- Google Search Console data (if available)
- Current rankings for target keywords

### Step 2: Score Each Item

For each item in both frameworks:

1. **Research**: Use web fetch, search, and page inspection to verify current state
2. **Score**: Assign the score that best matches observed reality
3. **Evidence**: Record what was observed to justify the score
4. **Competitor Context**: Note how competitors compare on this item

### Step 3: Apply Veto Checks

Both frameworks have veto checks — critical conditions that cap the maximum score:

**LOCAL-IMPACT Veto Checks (6):**
- GBP not claimed → Cap at 15
- Site not indexed → Cap at 10
- Active penalty → Cap at 10
- Wrong NAP everywhere → Cap at 20
- Zero reviews → Cap at 25
- No SSL → Cap at 20

**SERP-TRUST Veto Checks (7):**
- Site not indexed → Cap at 10
- Active manual penalty → Cap at 15
- No HTTPS / expired SSL → Cap at 25
- LCP > 6s on mobile → Cap at 30
- Cloaked/hidden content → Cap at 10
- >50% toxic backlinks → Cap at 20
- Zero structured data → Cap at 40

### Step 4: Calculate Scores

```
LOCAL-IMPACT:
  Raw = sum of 60 items (each 0-3)
  Normalized = (Raw / 180) × 100
  Final = min(Normalized, lowest triggered veto cap)

SERP-TRUST:
  Raw = sum of 50 items (each 0-4)
  Normalized = (Raw / 200) × 100
  Final = min(Normalized, lowest triggered veto cap)

SEO Health Index:
  = (LOCAL-IMPACT Final × 0.55) + (SERP-TRUST Final × 0.45)
```

### Step 5: Dimension Breakdown

Report per-dimension scores for diagnostic granularity:

```
LOCAL-IMPACT Dimensions:        SERP-TRUST Dimensions:
  L: Listing Quality [X/30]      T:  Technical Foundation [X/40]
  O: Online Reviews [X/30]       R:  Ranking Signals [X/40]
  C: Citations [X/30]            U:  User Experience [X/40]
  A: Authority [X/30]            S:  Search Authority [X/40]
  L2: Local Content [X/15]       T2: Trust & AI Readiness [X/40]
  I: Integrated Vis. [X/15]
  P: Performance [X/15]
  T: Tracking [X/15]
```

---

## Reporting Format

### Score Dashboard (for reports)

```
┌─────────────────────────────────────────────┐
│           SEO HEALTH INDEX: 72 / 100        │
│                  Grade: B+                   │
├──────────────────────┬──────────────────────┤
│   LOCAL-IMPACT: 75   │   SERP-TRUST: 68     │
│   Grade: B+          │   Grade: B            │
├──────────────────────┴──────────────────────┤
│  Dimension Breakdown:                        │
│  ████████░░ Listing Quality      80%         │
│  ███████░░░ Online Reviews       70%         │
│  █████░░░░░ Citations            50%         │
│  ████████░░ Authority            80%         │
│  ██████░░░░ Technical Foundation 60%         │
│  ████████░░ Ranking Signals      80%         │
│  ███████░░░ User Experience      70%         │
│  █████░░░░░ Search Authority     50%         │
│  ██████░░░░ Trust & AI Ready     60%         │
├─────────────────────────────────────────────┤
│  Veto Checks: ✅ All clear                   │
│  Competitors Avg: 65 | Your Position: 2/4   │
└─────────────────────────────────────────────┘
```

### Competitor Comparison Format

```
| Metric | Client | Comp 1 | Comp 2 | Comp 3 | Gap |
|--------|--------|--------|--------|--------|-----|
| LOCAL-IMPACT | 75 | 82 | 68 | 71 | -7 vs leader |
| SERP-TRUST | 68 | 75 | 62 | 70 | -7 vs leader |
| SEO Health Index | 72 | 79 | 65 | 71 | -7 vs leader |
```

---

## Score Tracking Over Time

Recommend quarterly re-scoring to track progress:

```
| Quarter | LOCAL-IMPACT | SERP-TRUST | SEO Health | Key Changes |
|---------|-------------|------------|------------|-------------|
| Q1 2026 | 45 | 38 | 42 | Baseline audit |
| Q2 2026 | 62 | 55 | 59 | GBP optimized, tech fixes |
| Q3 2026 | 75 | 68 | 72 | Content + citations built |
| Q4 2026 | 82 | 78 | 80 | Authority + AI visibility |
```

---

## Framework Intellectual Property

These scoring frameworks are proprietary to the Local SEO Audit System plugin:

- **LOCAL-IMPACT** — Local Optimization, Consistency, Authority & Listing — Impact Performance Assessment & Competitive Tracking
- **SERP-TRUST** — Search Engine Results Page — Technical Reliability, User Signals & Search Trust

Both frameworks are designed to be reproducible, evidence-based, and comparable across businesses and time periods. They provide structured, quantitative assessment where the SEO industry typically relies on subjective judgment.
