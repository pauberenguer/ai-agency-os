---
name: local-impact-auditor
description: >
  Score a local business using the proprietary 60-item LOCAL-IMPACT framework
  across 8 dimensions (Listing, Reviews, Citations, Authority, Local Content,
  Integrated Visibility, Performance, Tracking). 0-3 scale per item, veto
  checks, normalized 0-100 score. Use /score-local-impact or after audit phases.
  Output: {AUDIT_DIR}/local-impact-scores.md
---

# LOCAL-IMPACT Auditor — Proprietary Scoring Framework

You are executing the LOCAL-IMPACT scoring framework — a 60-item assessment of local business presence, visibility, and competitiveness. This is the primary scoring framework for local SEO health.

**Framework:** LOCAL-IMPACT (Local Optimization, Consistency, Authority & Listing — Impact Performance Assessment & Competitive Tracking)
**Items:** 60 | **Scale:** 0–3 per item | **Max Raw:** 180 | **Normalized:** 0–100 | **Version:** 2025.1

---

## Prerequisites

Before scoring, confirm you have:
- [ ] Business name, website URL, target location
- [ ] Google Business Profile URL (or search `business name + location` on Google Maps)
- [ ] At least 3 competitor GBP URLs for comparison
- [ ] Access to or output from prior audit phases in `{AUDIT_DIR}/`

If missing, collect before proceeding. Read `{AUDIT_DIR}/intake-data.md` for all context.

---

## Framework Reference

Load the complete rubric from `references/local-impact-benchmark.md`.

### Scoring Dimensions
| Code | Dimension | Items | Max | Key Tools |
|------|-----------|-------|-----|-----------|
| L | Listing Quality | 10 | 30 | Google Maps, GBP dashboard, BrightLocal |
| O | Online Reviews | 10 | 30 | BrightLocal, Podium, ReviewTrackers |
| C | Citation Consistency | 10 | 30 | BrightLocal, Whitespark, Yext |
| A | Authority Signals | 10 | 30 | Ahrefs, Majestic, Moz Link Explorer |
| L2 | Local Content | 5 | 15 | Screaming Frog, GSC, site_crawler.py |
| I | Integrated Visibility | 5 | 15 | Apple Maps, Bing Places, Otterly.ai |
| P | Performance | 5 | 15 | PageSpeed Insights, GTmetrix, Lighthouse |
| T | Tracking | 5 | 15 | GA4, GSC, CallRail, Hotjar |

---

## Step 1: Research Phase — Dimension-by-Dimension Evidence Gathering

### Dimension L — Listing Quality (GBP Completeness)

**Primary tool:** Google Business Profile dashboard or Google Maps listing
**2025 GBP Completeness Checklist:**
1. Business name (exact legal name, no keyword stuffing) — GSC brand signal
2. Primary category + all relevant secondary categories (2025: up to 10)
3. Description — 750 character max, keyword-rich first 250 chars
4. Service areas (if service-area business) vs. storefront address
5. Hours of operation including special/holiday hours
6. Phone number (local area code preferred over 1-800)
7. Website URL (tracking parameter: `?utm_source=google&utm_medium=organic&utm_campaign=gbp`)
8. Products/Services with prices, descriptions (every service listed)
9. Photos: minimum 10 exterior + 10 interior + 5 team + 5 work examples (2025 benchmark: 50+ total)
10. GBP Posts: minimum 1 active post per week (offers, updates, events)
11. Q&A section: minimum 5 seeded Q&As with keyword-rich answers
12. Attributes: all applicable attributes checked (women-owned, veteran-owned, accessibility, etc.)
13. Messaging enabled (if applicable to business type)
14. Menu/Service menu (for restaurants/salons/etc.)

**Benchmark thresholds:**
- 100% complete: all 13 elements present → Score 3
- 8–12 elements: → Score 2
- 4–7 elements: → Score 1
- <4 elements: → Score 0

### Dimension O — Online Reviews

**Primary tools:** BrightLocal Review Dashboard, Google Maps, Podium, ReviewTrackers
**2025 Review Benchmarks (Local Pack Competitiveness):**
| Metric | Score 3 (Excellent) | Score 2 (Good) | Score 1 (Weak) | Score 0 (Absent) |
|--------|--------------------|--------------|--------------|--------------------|
| Google rating | ≥4.5 stars | 4.0–4.4 stars | 3.5–3.9 stars | <3.5 stars |
| Google review count | ≥50 reviews | 25–49 reviews | 10–24 reviews | <10 reviews |
| Review velocity | ≥4 new/month | 2–3 new/month | 1 new/month | <1 per month |
| Response rate | ≥90% responded | 70–89% | 50–69% | <50% |
| Response time | <24 hours | 24–72 hours | 3–7 days | >7 days |
| Review platforms | 4+ platforms | 3 platforms | 2 platforms | 1 platform only |

**Multi-platform check:** Google, Yelp, Facebook, TripAdvisor, BBB, Houzz, Healthgrades, Avvo (per industry)
**AI visibility angle:** Google AI Overviews pulls review ratings — businesses with <4.0 stars are rarely featured

### Dimension C — Citation Consistency

**Primary tools:** BrightLocal Citation Audit, Whitespark Citation Finder, Yext Knowledge Network
**NAP Consistency Check:**
- Name: Exact match across all directories (no abbreviations, no "LLC" variations)
- Address: Street number, street name, suite formatting consistent (Ste vs Suite vs #)
- Phone: Same format (+1-XXX-XXX-XXXX vs (XXX) XXX-XXXX — pick one)

**Tier 1 Citations (must be present):**
Data Axle (formerly Infogroup), Neustar/Localeze, Acxiom, Foursquare — these feed hundreds of downstream directories

**Tier 2 Citations (local pack important):**
Google Business Profile, Yelp, Facebook, BBB, Apple Maps, Bing Places, Foursquare, Yellow Pages, MapQuest

**Inconsistency threshold:** >3 NAP inconsistencies across top 50 citations → Score 0–1

### Dimension A — Authority Signals

**Primary tools:** Ahrefs Site Explorer, Majestic (Trust Flow / Citation Flow), Moz Domain Authority
**Local Authority Benchmarks:**
| Signal | Score 3 | Score 2 | Score 1 | Score 0 |
|--------|---------|---------|---------|---------|
| Domain Rating (Ahrefs DR) | >30 | 15–30 | 5–14 | <5 |
| Local referring domains | >25 local RDs | 10–25 | 3–9 | <3 |
| Chamber of Commerce link | Present | — | — | Absent |
| BBB accreditation | Accredited | Listed | — | Not listed |
| .edu / .gov links | Any present | — | — | None |
| Industry association links | 3+ | 1–2 | — | None |

**Local link types to check:** Chamber of Commerce, local newspaper mentions, city/county business directories, industry associations, local sponsorships

### Dimension L2 — Local Content Quality

**Primary tools:** Screaming Frog, {DATA_DIR}/crawl/ (site_crawler.py output), GSC
**Content Thresholds:**
- Service pages: ≥800 words, unique content per service, service-area keywords integrated
- Location pages (multi-location): ≥600 words, unique to each location (not templated)
- Blog/local content: Regular publishing (min 2×/month), community-relevant topics
- Schema: LocalBusiness + Service + FAQPage + Review schema on key pages
- Internal linking: Service pages linked from homepage + location pages

### Dimension I — Integrated Visibility

**Tools:** Apple Maps Connect, Bing Places for Business, Otterly.ai (AI mention tracking)
**2025 Visibility Checklist:**
- [ ] Apple Maps claimed and verified (Siri voice search source)
- [ ] Bing Places verified (powers Copilot local results)
- [ ] Google Maps embed on contact/location page
- [ ] Voice search readiness: FAQ content with conversational phrasing
- [ ] AI Overview presence: Test "near me" queries in Google — does business appear?
- [ ] ChatGPT / Perplexity citation: Search business name in AI assistants
- [ ] Social media profiles: Facebook, Instagram linked + active (within 30 days)

### Dimension P — Performance

**Primary tools:** Google PageSpeed Insights (pagespeed.web.dev), GTmetrix, Chrome DevTools Lighthouse
**2025 Core Web Vitals Thresholds:**
| Metric | Score 3 | Score 2 | Score 1 | Score 0 |
|--------|---------|---------|---------|---------|
| LCP (Largest Contentful Paint) | <1.8s | 1.8–2.5s | 2.5–4.0s | >4.0s |
| INP (Interaction to Next Paint) | <100ms | 100–200ms | 200–500ms | >500ms |
| CLS (Cumulative Layout Shift) | <0.05 | 0.05–0.10 | 0.10–0.25 | >0.25 |
| Mobile PageSpeed score | >90 | 70–90 | 50–69 | <50 |
| TTFB (Time to First Byte) | <400ms | 400–800ms | 800–1800ms | >1800ms |

Note: INP replaced FID as a Core Web Vital in March 2024.

### Dimension T — Tracking Setup

**Primary tools:** GA4, Google Search Console, CallRail/WhatConverts (call tracking)
**Tracking Checklist:**
- [ ] GA4 installed + configured (goals, conversions set up)
- [ ] GSC verified + sitemap submitted + no coverage errors
- [ ] Call tracking active (CallRail, WhatConverts, or similar)
- [ ] GBP Insights reviewed monthly (calls, directions, website clicks)
- [ ] Conversion tracking: form submissions, calls, bookings tracked as GA4 events
- [ ] UTM parameters on GBP website link

---

## Step 2: Score Each Item (0–3 Scale)

For each of the 60 items in `references/local-impact-benchmark.md`, assign:

| Score | Label | Meaning |
|-------|-------|---------|
| 0 | Absent | Not implemented at all |
| 1 | Weak | Partially implemented, significant gaps |
| 2 | Good | Implemented correctly, minor improvements possible |
| 3 | Excellent | Fully optimised, best-in-class implementation |

Record evidence for every score — no unsupported scores.

---

## Step 3: Veto Check (2025 Updated)

Apply BEFORE calculating final score. Highest applicable cap wins.

| Veto | Condition | Score Cap | Rationale |
|------|-----------|-----------|-----------|
| V01 | GBP not claimed or verified | 15 | Unverified GBP cannot rank in local pack |
| V02 | Website not indexed by Google | 10 | No indexation = no organic presence |
| V03 | Active Google manual penalty | 10 | Penalty suppresses all rankings |
| V04 | NAP wrong on website + GBP + majority of citations | 20 | NAP inconsistency destroys trust signals |
| V05 | Zero Google reviews | 25 | No social proof — cannot compete locally |
| V06 | No SSL certificate | 20 | Security requirement since 2018; Chrome warns users |

---

## Step 4: Calculate Final Score

```python
raw_score = sum of all 60 item scores           # Max: 180
normalized = (raw_score / 180) * 100            # Max: 100
veto_cap = min(triggered veto caps, default=100)
final_score = min(normalized, veto_cap)         # Final: 0–100
```

Use `python3 scripts/score_calculator.py --both --li-file {AUDIT_DIR}/local-impact-scores.md` to compute automatically.

---

## Step 5: Competitor Scoring

Score each top competitor on the same 60 items (abbreviated — focus on observable signals):
- Use Google Maps, GBP listing, site search, Ahrefs free data, BrightLocal free scan
- Focus on dimensions L, O, C, A — these are the most observable externally
- Minimum: score all 6 veto checks per competitor

---

## Step 6: Identify Quick Wins

Quick wins = items currently at score 0 or 1 that can reach score 3 in <2 hours:

| Quick Win | Current Score | Effort | Expected Gain | Priority Score (I×F) |
|-----------|-------------|--------|---------------|-----------------------|
| Add GBP Q&A (10 seeded questions) | 0 | 30 min | +3 pts L | 5×5=25 |
| Upload 20+ GBP photos | 0–1 | 45 min | +3 pts L | 5×5=25 |
| Respond to all existing reviews | 0–1 | 1–2 hrs | +3 pts O | 5×5=25 |
| Submit to Data Axle + Neustar | 0 | 1 hr | +6 pts C | 5×4=20 |
| Install call tracking (CallRail) | 0 | 1 hr | +3 pts T | 4×5=20 |
| Verify Apple Maps + Bing Places | 0 | 30 min | +3 pts I | 4×5=20 |
| Add schema markup (LocalBusiness) | 0–1 | 2 hrs | +3 pts A | 5×4=20 |

---

## Output Format

Write structured output to `{AUDIT_DIR}/local-impact-scores.md`:

```yaml
---
skill: cross-cutting/local-impact-auditor
phase: scoring
date: [YYYY-MM-DD]
business: [Business Name]
url: [URL]
score: [X/100]
status: complete
---
```

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 LOCAL-IMPACT SCORECARD — 2025 Edition
 Business: [Name]
 URL: [URL]
 Location: [City, State]
 Date: [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

 OVERALL SCORE: [X] / 100    Grade: [A-F]

 Dimension Breakdown:
 L  Listing Quality      [XX/30]  ████████░░  [X%]  — [key gap]
 O  Online Reviews        [XX/30]  ███████░░░  [X%]  — [key gap]
 C  Citation Consistency  [XX/30]  █████░░░░░  [X%]  — [key gap]
 A  Authority Signals     [XX/30]  ████████░░  [X%]  — [key gap]
 L2 Local Content         [XX/15]  ██████░░░░  [X%]  — [key gap]
 I  Integrated Visibility [XX/15]  ███████░░░  [X%]  — [key gap]
 P  Performance           [XX/15]  ████████░░  [X%]  — [key gap]
 T  Tracking              [XX/15]  █████░░░░░  [X%]  — [key gap]

 Veto Checks:
 [✅/❌] V01: GBP Claimed & Verified
 [✅/❌] V02: Website Indexed by Google
 [✅/❌] V03: No Active Google Penalty
 [✅/❌] V04: NAP Consistent (website + GBP + citations)
 [✅/❌] V05: Has Google Reviews (>0)
 [✅/❌] V06: SSL Certificate Active

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 COMPETITOR COMPARISON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 | Dimension  | Client | Comp 1 | Comp 2 | Comp 3 | Gap |
 |------------|--------|--------|--------|--------|-----|
 | Overall    |   XX   |   XX   |   XX   |   XX   |  ±  |
 | Listing    |   XX   |   XX   |   XX   |   XX   |  ±  |
 | Reviews    |   XX   |   XX   |   XX   |   XX   |  ±  |
 | Citations  |   XX   |   XX   |   XX   |   XX   |  ±  |
 | Authority  |   XX   |   XX   |   XX   |   XX   |  ±  |
 | Performance|   XX   |   XX   |   XX   |   XX   |  ±  |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 TOP 5 IMPROVEMENT PRIORITIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 1. [Item ID]: [Description] — Score: X/3 — Impact: [High] — Effort: [X hrs] — Priority: [I×F]
 2. [Item ID]: [Description] — Score: X/3 — Impact: [High] — Effort: [X hrs] — Priority: [I×F]
 3. [Item ID]: [Description] — Score: X/3 — Impact: [Med]  — Effort: [X hrs] — Priority: [I×F]
 4. [Item ID]: [Description] — Score: X/3 — Impact: [Med]  — Effort: [X hrs] — Priority: [I×F]
 5. [Item ID]: [Description] — Score: X/3 — Impact: [Low]  — Effort: [X hrs] — Priority: [I×F]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 QUICK WINS (<2 hrs each, immediate gains)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 • [Action]: [Specific step] — Gain: +X pts — Effort: X min
 • [Action]: [Specific step] — Gain: +X pts — Effort: X min
 • [Action]: [Specific step] — Gain: +X pts — Effort: X min

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 AI VISIBILITY ASSESSMENT (2025)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Google AI Overviews: [Appearing / Not appearing for target queries]
 Apple Siri (Maps): [Verified / Not verified]
 Bing Copilot: [Bing Places verified / Not verified]
 ChatGPT / Perplexity: [Cited / Not cited when searched by name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Data Output for Report Integration (YAML Block)

```yaml
framework: LOCAL-IMPACT
version: 2025.1
date: [YYYY-MM-DD]
business: [name]
url: [url]
location: [city, state]
scores:
  overall: [0-100]
  grade: [A+-F]
  raw: [0-180]
  dimensions:
    L:  { raw: X, max: 30, pct: X, key_gap: "" }
    O:  { raw: X, max: 30, pct: X, key_gap: "" }
    C:  { raw: X, max: 30, pct: X, key_gap: "" }
    A:  { raw: X, max: 30, pct: X, key_gap: "" }
    L2: { raw: X, max: 15, pct: X, key_gap: "" }
    I:  { raw: X, max: 15, pct: X, key_gap: "" }
    P:  { raw: X, max: 15, pct: X, key_gap: "" }
    T:  { raw: X, max: 15, pct: X, key_gap: "" }
  vetoes_triggered: []
  final_cap: 100
  competitors:
    - name: [comp1]
      score: X
      key_advantage: ""
    - name: [comp2]
      score: X
      key_advantage: ""
    - name: [comp3]
      score: X
      key_advantage: ""
  quick_wins: []
  ai_visibility: { google_aio: false, apple_maps: false, bing: false, chatgpt: false }
```

---

## Handoff

After scoring, save results to `{AUDIT_DIR}/local-impact-scores.md` for:
- `output/report-generation` — integrates into master report section 3
- `output/pdf-report` — renders LOCAL-IMPACT dashboard gauge in PDF cover
- `cross-cutting/serp-trust-auditor` — SEO Health Index = (LOCAL-IMPACT × 0.55) + (SERP-TRUST × 0.45)
