---
name: ux-cro-audit
description: >
  User experience and conversion rate optimization audit. Activates when
  discussing conversion rate, user experience, bounce rate, form optimization,
  click-to-call, booking flows, analytics setup, conversion tracking, page
  layout, or converting visitors into leads. Phase 17. Output: {AUDIT_DIR}/cro-findings.md
---

# UX & CRO Audit — Phase 17

## Executive Summary

CRO is the multiplier on all SEO investment: doubling conversion rate at constant traffic = doubling revenue without additional marketing spend. For local businesses, the average top-quartile performer converts at 10–15% (home services) vs. an average of 3–7% — a 3–5× gap achievable without any additional traffic. In 2025, behavioral signals are confirmed local ranking factors: Google's Navboost system weights dwell time, pogo-stick rate, and return visits — meaning poor UX literally suppresses rankings. AI Overviews drive 2–4× higher conversion intent on click-through than standard organic results (users who arrive via AI are further in the decision process). GBP conversion signals (direction clicks, call clicks, website clicks) now feed Google's local ranking algorithm directly, making on-site and GBP CRO inseparable.

**2025 CRO benchmarks for local businesses:**
- Click-to-call: 70% of mobile searchers use it for local businesses (Google Consumer Insights 2024)
- Form fields: each additional field beyond 5 reduces submission rate by 10–20% (Formstack 2024)
- LCP delay: 1-second LCP increase = 20% conversion drop (Google/SOASTA study)
- Trust signal impact: star rating badge near CTA increases CVR 15–25% (Baymard Institute 2024)
- Sticky mobile CTA bar: 15–40% more calls than static header number alone
- GA4 veto: no conversion tracking installed = maximum CRO score 60/100 (can't optimize what can't be measured)

---

## SEO-CRO Connection (2025)

Traffic without conversions is wasted authority. In 2025–2026:
- Google's **behavioral signals** (dwell time, pogo-sticking, return visits) are documented ranking factors in the leaked Navboost system
- **1-second LCP delay = 20% conversion drop** (Google/SOASTA); **3s+ = 53% mobile abandonment**
- **Local businesses** live and die by: calls, form fills, booking completions — these are also the engagement signals Google measures
- AI Overview click-throughs convert at 2–4× the rate of traditional organic clicks (higher intent users)

**Typical local business conversion benchmarks (2025):**
| Industry | Avg Conversion Rate | Top Quartile |
|---------|--------------------|-----------||
| Home services (plumbing, HVAC) | 3–7% | 10–15% |
| Legal / law firms | 1–3% | 5–8% |
| Healthcare / dental | 2–5% | 8–12% |
| Automotive | 2–4% | 6–10% |
| Restaurant (reservation) | 4–8% | 12–20% |

---

## Step 1: Read Project Context

Read `{AUDIT_DIR}/intake-data.md` — business goals, primary conversion types, URL.
Read `{AUDIT_DIR}/technical-findings.md` — speed and mobile issues affecting CRO.
Read `{AUDIT_DIR}/onpage-findings.md` — CTA placement and content gaps.
Read `{AUDIT_DIR}/speed-findings.md` — LCP, INP, CLS scores (direct CRO factors).

**Tools for this phase:**
| Tool | Purpose | Cost |
|------|---------|------|
| **Microsoft Clarity** | Heatmaps, session recordings, rage clicks, dead clicks — free unlimited | Free |
| **Hotjar** | Heatmaps, session recordings, on-page surveys | Paid/Free (limited) |
| **GA4** | Conversion events, funnel analysis, user flow, channel attribution | Free |
| **CallRail** | Call tracking, conversation intelligence, attribution to source | Paid |
| **VWO / Optimizely** | A/B testing platform for CTA text, layout, form fields | Paid |
| **WhatConverts** | Multi-channel lead tracking (calls, forms, chat) with attribution | Paid |
| **PageSpeed Insights** | CWV scores per page — LCP/INP/CLS affecting conversion | Free |
| **FullStory** | Session replay + product analytics — identify exact friction points | Paid |

---

## Step 2: Conversion Inventory

### Define Primary Conversions (In Order of Business Value)

| Conversion Type | Present on Site? | Tracking Active? | Current Rate |
|----------------|-----------------|-----------------|-------------|
| Phone call (click-to-call) | ✅/❌ | ✅/❌ (CallRail?) | |
| Contact form submission | ✅/❌ | ✅/❌ (GA4 event?) | |
| Online booking / appointment | ✅/❌ | ✅/❌ | |
| Quote request form | ✅/❌ | ✅/❌ | |
| Live chat / chatbot | ✅/❌ | ✅/❌ | |
| Direction click (Google Maps) | ✅/❌ | ✅/❌ | |
| Email click | ✅/❌ | ✅/❌ | |

---

## Step 3: Primary Conversion Path Audit

For EACH conversion type, assess 4 dimensions:

### 1. Visibility
- CTA above the fold on desktop AND mobile (no scrolling required)?
- CTA visually prominent (color contrast ≥4.5:1, size, whitespace)?
- CTA repeated at bottom of long pages?
- Present on every key service/location page?

### 2. Friction (Clicks to Convert)
- Desktop: ≤2 clicks from homepage to initiating conversion?
- Mobile: ≤1 tap to call (phone number = click-to-call link)?
- Form fields: ≤5 fields (industry research: each additional field reduces submission rate 10–20%)
- No unnecessary account creation required?
- Mobile form: correct `inputmode` attributes prevent wrong keyboard types?

### 3. Clarity
- CTA uses action language? ("Get a Free Quote" not "Submit")
- Value proposition adjacent to CTA ("Free estimate, no obligation")
- Next-step expectation set? ("We'll call you within 2 hours")
- Price transparency or range mentioned?

### 4. Trust Signals Near CTA
| Trust Element | Present? | Location | Quality |
|--------------|---------|---------|---------|
| Review rating + count ("★★★★★ 4.8 — 127 reviews") | ✅/❌ | | |
| Certifications / licenses badge | ✅/❌ | | |
| "Same-day service" or key differentiator | ✅/❌ | | |
| Guarantee statement | ✅/❌ | | |
| Customer count ("500+ satisfied customers") | ✅/❌ | | |

---

## Step 4: Phone Number Audit

For local businesses, phone is typically the #1 conversion. Every instance must be click-to-call:

| Check | Pass/Fail |
|-------|----------|
| Phone in header — visible without scrolling on desktop AND mobile | ✅/❌ |
| Phone as `<a href="tel:[number]">` (not plain text) | ✅/❌ |
| Phone in footer | ✅/❌ |
| Phone on Contact page | ✅/❌ |
| Phone in GBP (matches website exactly) | ✅/❌ |
| Phone in LocalBusiness schema | ✅/❌ |
| Call tracking number (CallRail/WhatConverts) for attribution | ✅/❌ |
| Font size ≥20px on mobile (minimum 18px) | ✅/❌ |
| Sticky mobile bar with phone + primary CTA | ✅/❌ |

**Impact of click-to-call on mobile:** 70% of mobile searchers use click-to-call for local businesses (Google Consumer Insights 2024). Businesses without `tel:` links lose 70% of mobile call conversions.

---

## Step 5: Form Audit

For each lead form:

| Form | Location | Field Count | Submit Text | Thank You? | CRM? | Mobile OK? |
|------|---------|------------|------------|-----------|-----|-----------|
| Contact | | | | Yes/No | Yes/No | Yes/No |
| Quote request | | | | Yes/No | Yes/No | Yes/No |
| Booking | | | | Yes/No | Yes/No | Yes/No |

**Form UX Checklist (each form):**
- [ ] ≤5 fields for first-contact forms (name, phone, email, service, message = ideal)
- [ ] Phone field near top (most businesses prefer to call back)
- [ ] "What service do you need?" dropdown pre-segments leads
- [ ] Submit button: action language ("Get My Free Estimate" not "Submit")
- [ ] Thank you page or confirmation: explains what happens next + expected response time
- [ ] Form emails to owner within 60 seconds (test: submit with own email)
- [ ] Mobile: `type="tel"` on phone, `type="email"` on email (triggers correct keyboard)
- [ ] No CAPTCHA friction — use honeypot field instead
- [ ] Form connected to CRM / GA4 event fires on submit

---

## Step 6: Navigation & Site Structure UX

### 2-Click Rule Test
Can a user reach the contact form within 2 clicks from the homepage?
1. Start on homepage
2. Click primary nav → does contact appear immediately?
3. Click "Contact" or CTA → are you on the form?

Result: [X clicks] — Pass/Fail (target ≤2)

### Navigation Audit
| Element | Present? | Works on Mobile? | Issue |
|---------|---------|----------------|-------|
| Top services in main nav | ✅/❌ | ✅/❌ | |
| Contact/Book button prominent in nav | ✅/❌ | ✅/❌ | |
| Mobile hamburger menu opens + works | ✅/❌ | N/A | |
| Sticky header on scroll? | ✅/❌ | ✅/❌ | |
| Breadcrumbs on inner pages | ✅/❌ | ✅/❌ | |

---

## Step 7: Trust Signal Inventory

Trust signals at key conversion points increase CVR 15–30% (Baymard Institute, 2024).

### Above-the-Fold Trust Signals (Homepage)
- [ ] Star rating visible: "★★★★★ 4.8 / 5 from 127 Google reviews"
- [ ] License/certification badge (state license number if applicable)
- [ ] Years in business ("Serving [City] since [year]")
- [ ] Service area mention ("Serving [City] & [Surrounding suburbs]")

### Mid-Page Trust Signals
- [ ] Testimonials: real names, photos, specific service mentioned
- [ ] Before/after project photos (visual proof — highest trust for trades)
- [ ] Video testimonials (30–90 sec — 28% higher conversion than text alone)
- [ ] Professional association logos (BBB, NARI, PHCC, etc.)
- [ ] Press mentions / "As Seen In" logos

### Pre-CTA Trust Signals
- [ ] Guarantee (satisfaction, money-back, quality)
- [ ] Risk reversal ("No obligation — cancel anytime")
- [ ] Response time commitment ("We respond within 2 hours")
- [ ] Emergency availability ("24/7 emergency service available")

---

## Step 8: Mobile UX Assessment

Mobile drives 60–70% of local service searches. Audit at 375px viewport width (iPhone SE):

| Check | Pass/Fail | Severity |
|-------|----------|---------|
| Font size ≥16px for all body text | | High |
| Tap targets ≥44×44px for all buttons/links | | Critical |
| ≥8px spacing between adjacent tap targets | | High |
| No horizontal scrolling at 375px viewport | | Critical |
| Phone number tappable (`tel:` link) | | Critical |
| Sticky CTA bar (phone + book) always visible while scrolling | | High |
| Forms don't cause page zoom on iOS (font-size ≥16px on inputs) | | Medium |
| Images properly sized (no overflow) | | Medium |
| CTA button visible without scrolling on mobile | | Critical |

---

## Step 9: Page Speed Impact on CRO

Pull from `{AUDIT_DIR}/speed-findings.md`:

| Metric | Current Score | CRO Impact if Failing |
|--------|-------------|----------------------|
| LCP (target <2.5s) | [Xs] | 20% conversion loss per second |
| INP (target <200ms) | [ms] | High friction — form inputs feel slow |
| CLS (target <0.1) | [score] | CTAs shift after page load — misclicks |
| Mobile PageSpeed (target ≥70) | [X/100] | 53% abandonment at 3s+ load |
| TTFB (target <800ms) | [ms] | Perceived as "slow server" |

**Flag all speed failures as CRO issues with dual Impact scores.**

---

## Step 10: Analytics & Conversion Tracking

Without tracking, CRO improvement is guesswork.

| Tracking Item | Implemented? | Notes |
|--------------|-------------|-------|
| GA4 installed + data flowing | Yes/No | |
| GA4 event: form submissions | Yes/No | Event name: |
| GA4 event: phone clicks (tel: links) | Yes/No | |
| GA4 event: booking completions | Yes/No | |
| GA4 event: chat interactions | Yes/No | |
| GSC linked to GA4 | Yes/No | |
| CallRail / WhatConverts (call tracking) | Yes/No | |
| Microsoft Clarity / Hotjar (heatmaps) | Yes/No | |
| Session recordings active | Yes/No | |
| A/B testing tool active | Yes/No | |
| Conversion dashboard set up (GA4 custom report) | Yes/No | |

**If GA4 not installed: ❌ CRITICAL** — business has zero conversion data. Priority: immediate, Effort: 1–2 hrs.

---

## Step 10b: Competitor CRO Benchmark

Visit top 3 competitor sites (desktop + mobile) and audit their CRO elements:

| Metric | Client | Comp 1 | Comp 2 | Comp 3 |
|--------|--------|--------|--------|--------|
| Click-to-call in header | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Sticky mobile CTA bar | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Review badge near CTA | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Form field count | | | | |
| Live chat / chatbot | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| GA4 installed (BuiltWith check) | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Mobile PageSpeed (PSI) | /100 | /100 | /100 | /100 |
| Price transparency on site | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |

**AI CRO Signals:**
| Check | Why It Matters | Pass/Fail |
|-------|---------------|----------|
| FAQPage schema on service pages | AIO citations drive 2–4× higher intent visitors | |
| HowTo schema on process pages | Attracts comparison-stage searchers closer to conversion | |
| Structured pricing/estimate content | AI cites specific pricing → pre-qualifies leads | |
| GBP booking button / appointment URL | Direct conversion from GBP without website visit | |
| Review count in GBP (50+) | AIO prominently features review counts as trust proxy | |

---

## Step 10c: Numbered Action Plan

### Immediate (Week 1 — Quick Wins, ≤2 hrs each)
1. **Make all phone numbers click-to-call** — wrap every phone in `<a href="tel:+1XXXXXXXXXX">`. Test on mobile. Effort: 30 min. Expected: 20–30% more call clicks from mobile.
2. **Add sticky mobile bar** — fixed bottom bar with phone icon + "Call Now" + primary CTA ("Get Quote"). Effort: 2 hrs developer. Expected: 15–40% more calls.
3. **Install Microsoft Clarity** (free) — enables heatmaps + session recordings to identify friction points. Effort: 30 min (add tracking code). No cost.
4. **Add star rating badge near primary CTA** — "★★★★★ 4.8 from 127 Google reviews" with schema AggregateRating. Effort: 30 min. Expected: 15–25% CVR lift.
5. **Set up GA4 form submission events** — if not tracking form submits, install GA4 event on thank-you page or form submit trigger. Effort: 1–2 hrs. Critical for all future optimization.

### Short-Term (Week 2–4)
6. **Reduce form fields to ≤5** — consolidate: Name, Phone, Service needed, Zip code, Message = 5 fields max. Remove: Last name (call them), Company (not needed for B2C), How did you hear about us (ask on call). Effort: 1 hr. Expected: 20–35% more form submissions.
7. **Add guarantee statement near CTA** — "100% satisfaction guarantee — no obligation estimate" reduces purchase anxiety. Effort: 15 min. Expected: 10–20% CVR lift.
8. **Add response time commitment** — "We respond within 2 hours" or "Same-day service available" next to form CTA. Effort: 15 min. Expected: 5–15% lift.
9. **Fix CTA button text** — change "Submit" → "Get My Free Estimate" or "Book a Free Inspection". Effort: 15 min. Expected: 5–15% lift.
10. **Set up call tracking** — install CallRail or WhatConverts to attribute calls to channel (Organic/GBP/Paid). Effort: 2 hrs. Required for data-driven CRO.

### Medium-Term (Month 2–3)
11. **Run A/B test on hero section** — test CTA button color, headline text, and hero image using VWO or Optimizely. Statistical significance at 500+ conversions. Effort: 4–8 hrs setup.
12. **Add live chat or chatbot** — Tidio (free tier) or Intercom for after-hours lead capture. Effort: 2 hrs setup. Expected: 10–20% more leads from non-business-hours traffic.
13. **Create video testimonial** — 60-second customer video on homepage + service pages. Expected: 15–30% CVR lift vs. text testimonials alone. Effort: 1–2 days including filming + editing.
14. **Implement GBP booking integration** — add appointment URL in GBP profile + website for direct GBP-to-booking conversion flow.

---

## Step 11: Quick CRO Wins (Priority Matrix)

| Win | Expected Conversion Lift | Impact (1–5) | Feasibility (1–5) | Priority | Effort |
|-----|--------------------------|-------------|-------------------|---------|--------|
| Sticky click-to-call bar on mobile | 15–40% more calls | 5 | 5 | 25 | 2 hrs |
| All phone numbers as `tel:` links | 20–30% more call clicks | 5 | 5 | 25 | 30 min |
| Reduce form fields to ≤5 | 20–35% more submissions | 4 | 5 | 20 | 1 hr |
| Install GA4 + track form submits | Enables all future CRO | 5 | 4 | 20 | 2 hrs |
| Add review count near CTA ("★★★★★ 127 reviews") | 10–25% lift | 4 | 5 | 20 | 30 min |
| Guarantee statement near CTA | 10–20% lift | 4 | 5 | 20 | 30 min |
| Install Microsoft Clarity (free heatmaps) | Reveals friction points | 4 | 5 | 20 | 30 min |
| CTA button: action language ("Get Free Quote") | 5–15% lift | 3 | 5 | 15 | 15 min |
| Before/after photo gallery | Trust signal, higher CVR | 4 | 3 | 12 | 4–8 hrs |
| Video testimonial (60 sec) | 15–30% conversion lift | 4 | 2 | 8 | 1–2 days |

---

## Scoring

| Category | Weight | Score |
|----------|--------|-------|
| Conversion path accessibility (≤2 clicks, above fold) | 20% | /20 |
| Phone visibility + click-to-call (all instances) | 20% | /20 |
| Form UX (≤5 fields, mobile-friendly, clear submit text) | 20% | /20 |
| Trust signals near CTA (reviews, guarantees, credentials) | 15% | /15 |
| Mobile UX (tap targets, no horizontal scroll, sticky CTA) | 15% | /15 |
| Conversion tracking (GA4 + events + call tracking) | 10% | /10 |

**Veto:** No GA4 installed AND no call tracking → maximum score 60/100.

---

## Output

Write to `{AUDIT_DIR}/cro-findings.md` with YAML frontmatter. Also write HTML report to `{REPORTS_DIR}/phase-17-cro.html` and convert to PDF via `python3 scripts/generate_pdf.py`.

```yaml
---
skill: strategy/ux-cro-audit
phase: 17
date: [YYYY-MM-DD]
business: [Business Name]
url: [URL]
score: [X/100]
status: [optimized|needs-work|critical]
ga4_installed: [yes|no]
click_to_call: [yes|no]
mobile_cta_visible: [yes|no]
---
```

Include:
- Score X/100 with per-category breakdown
- Conversion inventory table (all conversion types + tracking status)
- Primary conversion path assessment (all 4 dimensions per CTA type)
- Phone number audit (all instances, click-to-call status)
- Form audit table (all forms, field count, mobile test results)
- Trust signal inventory (above fold, mid-page, pre-CTA)
- Mobile UX issues list
- Analytics tracking gaps (GA4 events missing)
- Priority matrix (top 10 quick wins, Impact × Feasibility scored)
- 30/90-day CRO improvement plan with expected conversion lift %

**Key consumers:**
- `audit/speed-optimization` — LCP/INP/CLS data feeds CRO impact assessment
- `local/local-seo` — GBP click-to-call and conversion tracking overlap

---

## CRO Quick Reference

### CRO Issue Priority Table (2025)

| Issue | Severity | Effort | Priority | Tool to Diagnose |
|-------|---------|--------|---------|-----------------|
| No click-to-call on mobile | Critical | 15 min | 25 | GA4 + GSC mobile usability |
| GA4 not installed / no conversion tracking | Critical | 1–2 hrs | 25 | Screaming Frog JS check |
| Form > 5 fields (10–20% submission drop per field) | High | 1–2 hrs | 20 | Hotjar / Clarity heatmap |
| No trust signals above fold | High | 30–60 min | 20 | Ahrefs / SimilarWeb (check competitor CTAs) |
| CTA buried below 2 screen scrolls | High | 30 min | 20 | Clarity session recordings |
| LCP >2.5s (20% conversion drop per second) | High | 2–8 hrs | 20 | PageSpeed Insights / Ahrefs audit |
| INP >200ms (interaction lag hurts engagement) | High | 2–8 hrs | 16 | PageSpeed Insights (INP replaced FID March 2024) |
| No sticky header with phone/CTA on mobile | Medium | 1–2 hrs | 15 | Manual mobile review |
| Missing star rating badge near CTA | Medium | 30 min | 15 | SEMrush / Rank Math review schema |
| No social proof on service pages | Medium | 1–2 hrs | 12 | Manual content audit |

### AI Overviews + CRO (2025)

AI Overviews (AIO) now appear for 20–35% of local service queries. Users clicking through from AIO convert at 2–4× the rate of standard organic results — they arrive further in the buying decision. CRO implications:
- **Landing page must answer the AIO question immediately** — the visitor already "knows the answer" and is evaluating the business, not researching the topic
- **Social proof above fold** — AIO click-throughs respond to "Why this business?" signals: reviews, certifications, years in business
- **GEO/AEO content on service pages** — structured Q&A content (FAQPage schema) that earns AIO citation also increases post-click conversion by confirming expertise
- **Rank Math / Yoast** — use to add FAQPage + LocalBusiness schema that drives both AIO citations and CRO trust signals

### GBP Conversion Signals (2025 Direct Ranking Factors)

GBP conversion clicks now feed Google's local ranking algorithm directly:
| GBP Conversion Type | CRO Optimization | Expected Impact |
|--------------------|-----------------|----------------|
| Direction clicks | Add parking info, landmark reference | +15–25% direction clicks |
| Call clicks (mobile) | Verify phone number is call-tracking enabled (CallRail) | Measurable attribution |
| Website click → booking | Add Google Reserve / booking link to GBP | 20–35% more direct bookings |
| Q&A (2025 feature) | Pre-seed 5+ questions; high-intent Q&A reduces friction | Reduced pre-call friction |
| Review velocity (last 60–90 days) | Request reviews from recent customers | 3–5× weight in local ranking |

**Write `{REPORTS_DIR}/phase-17-cro.html` → `python3 scripts/generate_pdf.py --html {REPORTS_DIR}/phase-17-cro.html`**
- `output/report-generation` — CRO score + quick wins in master report section 17
