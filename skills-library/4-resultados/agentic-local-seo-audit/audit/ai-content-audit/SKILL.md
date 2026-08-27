---
name: ai-content-audit
description: >
  AI content detection and humanization audit. Activates when discussing AI-generated
  content, humanizing content, detecting AI writing patterns, E-E-A-T content signals,
  Google HCS compliance, thin content from AI, "sounds AI-written", content authenticity,
  or humanizing service pages, location pages, blog posts, or about pages.
  Phase 4a. Output: {AUDIT_DIR}/ai-content-findings.md
---

# AI Content Audit & Humanization — Phase 4a

## Executive Summary

Google's Helpful Content System (HCS), integrated into the core algorithm March 2024, actively targets AI-generated content produced without documented human expert review. The 2025 reality: AI detectors like Originality.ai, GPTZero, and Copyleaks flag content at >80% AI-likelihood as a reputational risk, but more critically, Google's own Navboost behavioral signals catch AI content indirectly — users bounce faster from lifeless, formulaic pages (high pogo-stick rate → ranking suppression). For local businesses, AI-written content is especially damaging: a plumber using "delve into," a dentist writing "testament to our commitment," or an HVAC company saying "nestled in the vibrant community" signals zero first-hand experience. E-E-A-T's "Experience" pillar (the first E added in December 2022) specifically rewards first-person, situated knowledge — the exact opposite of AI-pattern writing.

**2025 AI content benchmarks:**
- Google HCS: AI-generated content requires documented human expert review (Webmaster Guidelines 2025)
- E-E-A-T Experience signal: first-hand language increases AIO citation probability 40% (Semrush 2024)
- Originality.ai threshold: >80% AI score = flagged for manual review; industry-acceptable: 25–40% AI score after humanization
- Bounce rate correlation: AI-pattern pages average 72% bounce vs. 51% for human-written equivalents (Contentsquare 2024)
- Local business impact: service pages with AI patterns convert at 1.8–2.4% vs. 3.5–6% for authentic pages
- FAQPage schema + human voice: 3.2× AIO citation rate (Amsive 2025) — schema alone insufficient without authentic answers
- Reading level target: Flesch Reading Ease 60–70 (Grade 8–9) — US adult average reads at 8th grade; AI content often scores Grade 12–16 (too complex)
- Content length for LLM visibility: 1,500+ words with embedded statistics = 30–40% higher AI citation rate (Superlines 2025)
- Stat frequency: 1 data point per 150–200 words — content with embedded stats gets +22% GEO/AEO visibility (Superlines 2025)
- Expert quotations: +37% LLM citation visibility vs. pages without attributed quotes
- Content freshness: pages updated within 60 days get 28% better AI search visibility; within 30 days = 76.4% ChatGPT citation rate
- AI-referred traffic value: converts at 4.4× higher rate than organic (16% vs. 3.6% CVR) — high-quality human content that earns AI citations is highest-ROI content

**GEO / AEO / LLM SEO + AI Content Quality (2025 critical connection):**
- **GEO (Generative Engine Optimization)**: AI-pattern content is excluded from generative engine answers at higher rates — Google AI Mode, ChatGPT, Perplexity prefer citable, expert-attributed, first-person content
- **AEO (Answer Engine Optimization)**: Answer engines (Perplexity 13.8% citation rate, Google AIO 9.5% citation rate) extract answers from the first 30% of page content — AI-pattern executive summaries are deprioritized vs. direct human answers
- **LLM SEO**: Brand search volume is the #1 predictor of LLM citations (0.334 correlation, stronger than backlinks) — businesses using AI patterns that fail E-E-A-T undermine brand authority directly measurable by LLMs
- **Only 11% domain overlap** between ChatGPT and Perplexity citations — multi-platform humanization matters; what works on one AI may not on another
- **615× variation** in citation volume across LLM platforms — a humanized local business page can outperform a large competitor's AI-generated content on specific platforms

**Technical SEO + AI content connection (2025):**
- INP (Interaction to Next Paint, replaced FID March 2024) — AI-pattern pages with heavy third-party chat widgets and embedded review tools frequently trigger INP >200ms, compounding the ranking suppression from poor behavioral signals
- LCP (Largest Contentful Paint) — AI-generated content often uses stock image blocks as hero images (LCP >2.5s) with no specific local signal value; replacing with real job photos improves both LCP weight relevance and E-E-A-T
- Core Web Vitals + human content = compounding ranking signal — fast + human = both Page Experience and HCS signals working together
- Rank Math / Yoast SEO — readability checker in both tools flags AI-pattern sentences (passive voice, long sentences, transition word overuse) — use as a secondary signal during humanization

**Why this matters for local SEO specifically:**
- Local businesses win on *specificity* — a competitor describing "our Chicago plumbers have seen this exact issue in 1940s-era cast iron pipes in Wicker Park" outranks generic AI content every time
- Voice search and AI Overviews prefer cited entities with E-E-A-T signals — AI-pattern pages are excluded at higher rates
- Review authenticity alignment: GBP reviews that contradict the website's tone signal brand inconsistency (Google's entity understanding detects this)

---

## The 24 AI Writing Patterns — SEO Impact Taxonomy

*Based on the Wikipedia WikiProject AI Cleanup framework (github.com/blader/humanizer, 9,900+ stars, MIT license)*

### Category 1: Content Patterns — HIGH SEO RISK

| # | Pattern | AI Signal | SEO Impact | Local Business Example |
|---|---------|----------|-----------|----------------------|
| 1 | **Significance inflation** | "pivotal moment," "testament to," "marks a turning point," "transformative" | E-E-A-T damage — signals no real expertise | "Our services represent a transformative approach to plumbing solutions" |
| 2 | **Notability name-dropping** | Inflated fame claims with no evidence | Trust damage — Google checks entity authority | "We are Chicago's most trusted plumbing company" (no citation) |
| 3 | **Superficial gerund analyses** | "By leveraging X, we achieve Y" — process described with no detail | Thin content — HCS flag | "By utilizing advanced techniques, we ensure optimal results" |
| 4 | **Promotional language** | "nestled," "vibrant," "thriving community," "charming" | Conversion damage — zero information density | "Nestled in the vibrant heart of Chicago, our thriving practice…" |
| 5 | **Vague attributions** | "experts say," "studies show," "research indicates" (no citation) | E-E-A-T damage — Google knows who said it; you don't | "Studies show that regular HVAC maintenance saves money" |
| 6 | **Formulaic challenge statements** | "Challenges include…" / "Key considerations are…" with bullet lists and no depth | Template thin content — HCS flag | "Common plumbing challenges include leaks, blockages, and pressure issues" |

### Category 2: Language Patterns — MEDIUM SEO RISK

| # | Pattern | AI Signal | SEO Impact | Example to Fix |
|---|---------|----------|-----------|---------------|
| 7 | **AI-specific vocabulary** | "additionally," "landscape," "underscore," "delve," "notably," "robust," "seamless," "leverage," "holistic" | AI detection signal | "Additionally, our holistic approach underscores our robust commitment" |
| 8 | **Copula avoidance** | "serves as," "functions as," "acts as" instead of "is" | Unnatural phrasing — reduces readability score | "Our team serves as your trusted partner" → "Our team is your trusted partner" |
| 9 | **Negative parallelisms** | "not only X but also Y" used repeatedly | Formulaic rhythm — pattern detectors flag this | "Not only do we fix leaks, but we also prevent future damage" |
| 10 | **Rule-of-three lists** | Every point organized in exactly three items | Template signal | "Our services cover speed, quality, and reliability" (always three) |
| 11 | **Synonym cycling** | Rotating near-synonyms unnecessarily: "plumber / plumbing professional / pipe specialist" | Keyword confusion — can dilute keyword targeting | Within 200 words: "contractor," "professional," "expert," "specialist" for same role |
| 12 | **False ranges** | "between X and Y" when single value suffices | Reduces precision — E-E-A-T damage | "between 2 and 4 days" → "3 days typically" |

### Category 3: Style Patterns — MEDIUM SEO RISK

| # | Pattern | AI Signal | SEO Impact | Fix |
|---|---------|----------|-----------|-----|
| 13 | **Em-dash overuse** | Multiple em-dashes — like this — in every paragraph | Visual AI signal | Limit to 1 per 300 words |
| 14 | **Excessive boldface** | **Bolding** non-essential words throughout **every paragraph** | No semantic SEO value | Bold only genuinely critical terms |
| 15 | **Inline-header lists** | **Benefit:** explanation. **Benefit:** explanation. (repeated 5+ times) | When overused = template thin content | Convert some to prose with context |
| 16 | **Title case headings** | Every Word Capitalized In All Headings | Minor AI signal | Use sentence case for H2–H4 |
| 17 | **Emoji in professional copy** | 🔧 We Fix 🏠 Homes 🌟 | Destroys credibility on service pages | Remove from all service/location pages |
| 18 | **Curly quotation marks overuse** | "Smart quotes" inconsistently mixed | Minor — fix for consistency | — |

### Category 4: Communication Patterns — CRITICAL SEO RISK (on local business pages)

| # | Pattern | AI Signal | SEO Impact | Example |
|---|---------|----------|-----------|---------|
| 19 | **Chatbot artifacts** | "I hope this helps!" / "Feel free to reach out!" / "Don't hesitate to contact us!" | Destroys trust on service pages — sounds like a support bot | Replace with direct CTAs: "Call 312-XXX-XXXX for a free estimate" |
| 20 | **Cutoff disclaimers** | "As of my knowledge cutoff..." / "Please verify current information" | Fatal on local business pages — signals the page is AI-generated | Delete entirely |
| 21 | **Sycophantic tone** | "Great question!" / "Absolutely!" / "Certainly!" | Zero place in web copy — chatbot artifact | Delete entirely |
| 22 | **Excessive hedging** | "could potentially possibly," "may or may not," "in some cases might" | Weakens E-E-A-T — experts don't hedge every statement | Be direct: "leaks typically appear within 48 hours" |
| 23 | **Redundant filler phrases** | "It is worth noting that," "It goes without saying," "Needless to say," "In terms of" | Thin content — pads word count with zero information | Delete and rephrase directly |
| 24 | **Generic conclusions** | Summarizing what was just said with no new insight or call to action | Template pattern — HCS thin content signal | End with specific next step or local-specific fact |

---

## Step 1: Read Project Context

Read `{AUDIT_DIR}/intake-data.md` — business name, services, location, industry.
Read `{AUDIT_DIR}/content-inventory.md` — page list from Phase 4 content audit (if available).
Read `{AUDIT_DIR}/technical-findings.md` — crawl data, page types.

**Priority pages to audit for AI patterns:**
1. Homepage (highest traffic + brand voice = most damage if AI-written)
2. Service pages (direct conversion pages — E-E-A-T critical)
3. About/Team pages (Experience pillar — must sound human)
4. Location/service area pages (highest AI-pattern risk — often template-generated)
5. FAQ pages (AIO citation pages — authentic voice = citation advantage)
6. Blog/article content (topical authority — AI patterns destroy authority signals)

---

## Step 2: Page-by-Page AI Pattern Detection

For each priority page, fetch the content and run the two-pass detection:

### Pass 1 — Pattern Scan

Score each of the 24 patterns per page:
- **0** = Pattern not present
- **1** = Present but minor (1–2 instances)
- **2** = Significant (3–5 instances)
- **3** = Pervasive (6+ instances — systematic AI-generation likely)

**AI Likelihood Score per page:** `(sum of pattern scores / 72) × 100` = 0–100% AI-likeness

### Pass 2 — Residual AI Audit

After flagging patterns, re-read the page content and ask:
- Does any sentence sound like it could appear on ANY business's website with minimal changes?
- Is there any first-hand, situated knowledge present? (e.g., specific neighborhood references, actual job types encountered, real customer scenarios)
- Does the "About" page mention real people with real credentials?
- Are there specific pricing, process, or timeline details that only an expert would know?

If Pass 2 still returns "yes — sounds AI-generated" on more than 50% of questions → flag page as Critical.

---

## Step 3: Page Scoring Table

Document all pages in this format:

| Page URL | Word Count | AI Score | Top 3 Patterns | E-E-A-T Risk | Priority | Quick Fix Time |
|----------|-----------|---------|---------------|-------------|---------|---------------|
| /services/plumbing | [X] words | [X]% | Pattern 1,4,7 | High | 🔴 Critical | 2–3 hrs |
| /about | [X] words | [X]% | Pattern 2,19,21 | High | 🔴 Critical | 1–2 hrs |
| /location/chicago | [X] words | [X]% | Pattern 3,4,6 | Medium | 🟠 High | 1–2 hrs |
| /blog/[post] | [X] words | [X]% | Pattern 7,22,23 | Medium | 🟡 Medium | 1 hr |

**AI Score thresholds:**
| Score Range | Label | SEO Risk | Action |
|---|---|---|---|
| 0–20% | Human-authentic | None | Maintain voice; use as brand voice benchmark |
| 21–40% | Mostly human | Low | Minor edits — remove worst offenders |
| 41–60% | Mixed | Medium | Section-by-section rewrite of AI-heavy sections |
| 61–80% | Mostly AI | High | Full page rewrite with human SME input |
| 81–100% | AI-generated | Critical | Complete rewrite required — E-E-A-T at risk |

---

## Step 4: Competitor AI Content Benchmark

Compare client vs. top-3 local competitors for AI content signals.
For each competitor, fetch their homepage + top 2 service pages and scan for the 24 patterns.

**Competitor comparison context:** If all competitors score >60% AI-likely, the first business to humanize becomes the authority leader — this is a competitive content gap. If a top-ranking competitor has a low AI score (<30%), their human voice is a confirmed ranking signal worth studying.

| Competitor | AI Score (avg across pages) | Top AI Patterns Found | Human Voice Elements | E-E-A-T Signals |
|-----------|--------------------------|----------------------|---------------------|----------------|
| Client | [X]% | [patterns] | [count] | [count] |
| Comp 1 | [X]% | [patterns] | [count] | [count] |
| Comp 2 | [X]% | [patterns] | [count] | [count] |
| Comp 3 | [X]% | [patterns] | [count] | [count] |

**Opportunity:** If client's AI score is higher (worse) than all competitors, every page rewrite is a direct ranking opportunity. If a competitor has a low AI score (more human content), study their voice and use it as a benchmark — Google likely rewards their style.

---

## Step 5: Humanization Recommendations

For each Critical/High priority page, provide specific rewrites:

### Humanization Framework (per page)

**1. Add first-hand experience signals:**
- Replace vague claims with specific job types: "We've fixed over 200 cast iron pipe leaks in Chicago's Lincoln Park neighborhood since 2018"
- Add specific customer scenario context: "Most homeowners call us after noticing a wet spot on their basement ceiling — here's what we actually find when we open the wall..."
- Include honest complexity: "In some cases, what looks like a simple leak turns out to be a cracked pipe behind the foundation — we always give you the full picture upfront"

**2. Remove AI vocabulary (word-for-word substitutions):**
| AI Word | Human Replacement |
|---------|-----------------|
| "delve into" | "look at" / "dig into" (only if literally digging) |
| "testament to" | delete or "proof of" |
| "leverage" | "use" |
| "holistic" | "complete" / "thorough" |
| "seamless" | "smooth" / "straightforward" |
| "robust" | "strong" / "reliable" or delete |
| "landscape" (non-literal) | "industry" / "market" / delete |
| "underscore" | "show" / "confirm" |
| "notably" | "importantly" or delete |
| "pivotal" | "key" / "important" |
| "nestled" | delete; state location directly |
| "vibrant community" | name the actual neighborhood |
| "thriving" | delete |
| "additionally" | "also" or restructure sentence |
| "navigate" (non-literal) | "deal with" / "handle" |

**3. Replace vague attributions with real sources:**
- "Studies show" → "A 2024 report by the National Association of Plumbers found..."
- "Experts recommend" → "According to [specific expert/org]..." or rewrite as first-person advice: "In our experience, we recommend..."
- "It's widely known" → delete or cite the source

**4. Add local specificity (converts AI to human):**
- Mention actual neighborhoods served (not just "Chicago area")
- Reference local landmarks as context: "Jobs in [neighborhood] tend to have [issue] because of [local construction era]"
- Include seasonal/regional context: "Chicago winters mean we see a spike in frozen pipe calls every January — here's what to do at 2am..."
- Mention local permit requirements, codes, or inspectors by name if applicable

**5. Fix communication patterns:**
- Delete all chatbot artifacts: "Feel free to...", "Don't hesitate to...", "I hope this helps"
- Replace with direct CTAs: "Call 312-XXX-XXXX — we answer 24/7 for emergencies"
- Remove all hedging qualifiers on local facts: "Our team is available same-day" not "Our team may potentially be available in some cases"

---

## Step 6: E-E-A-T Reconstruction Protocol

AI-pattern removal is only half the job. The second half is adding E-E-A-T signals that AI cannot generate:

### Experience Signals (the first E — added Dec 2022)
- ✅ First-person accounts of specific jobs: "Last month, we uncovered a cracked main line on [street] in Lincoln Park..."
- ✅ Time-in-business with specific milestones: "After 15 years and 4,000+ Chicago homes served..."
- ✅ Photos of actual work (alt text must be descriptive and local)
- ✅ Honest failure stories: "We've seen DIY repairs that made things worse — here's what not to do"

### Expertise Signals (the second E)
- ✅ Specific technical knowledge: "We use RIDGID camera inspection for cast iron pipes — here's why it's different from PVC work"
- ✅ Named certifications: "Master Plumber license #XXXXXX (Illinois)" — not just "licensed and certified"
- ✅ FAQ answers with specific depths: not "leaks can vary" but "hairline cracks in supply lines: 15 min fix; slab leaks: 1–3 days with permits"

### Authoritativeness Signals (A)
- ✅ Named staff/owner on About page with real credentials and photo
- ✅ Media mentions (link to actual press) rather than vague "featured in"
- ✅ GBP alignment: entity name, address, phone must match page content exactly

### Trust Signals (T)
- ✅ Real testimonials with full names, dates, specific job types — not "Great service!" but "Fixed our burst pipe at 11pm on a Sunday in 20 minutes" — John R., Lincoln Park, Feb 2025
- ✅ Response to negative reviews (shows real business operation)
- ✅ Visible pricing ranges (even rough estimates build trust; AI avoids pricing)

---

## Step 7: GBP + AI Content Alignment (2025)

Google's entity understanding (2025) cross-references website content against GBP:
- **Review language vs. page language** — if reviews mention "fast" and "honest" but pages say "seamless holistic solutions," the mismatch signals brand inconsistency
- **GBP Q&A seeding** — seed Q&A with human-voice questions matching the humanized page content (not AI-patterned questions)
- **Review velocity** — recent reviews (last 60–90 days) weighted 3–5× more — use humanized page language as review response templates to reinforce the human voice signal to Google

---

## Step 8: Priority Matrix

| Action | AI Pattern Addressed | Impact (1–5) | Feasibility (1–5) | Priority | Effort |
|--------|---------------------|-------------|-----------------|---------|--------|
| Rewrite homepage hero section (remove patterns 1,4,7) | Significance inflation, promotional, AI vocab | 5 | 5 | 25 | 1–2 hrs |
| Rewrite About page with real team bios + Experience signals | Patterns 2, 19, 21, 22 | 5 | 4 | 20 | 2–3 hrs |
| Add first-hand experience paragraphs to all service pages | Patterns 3, 5, 6 | 5 | 4 | 20 | 1–2 hrs/page |
| Remove all chatbot artifacts site-wide | Pattern 19, 21, 24 | 4 | 5 | 20 | 30 min |
| Delete/rewrite all vague attributions | Pattern 5 | 4 | 5 | 20 | 1 hr |
| AI vocabulary swap (find/replace + rewrite) | Pattern 7 | 3 | 5 | 15 | 1–2 hrs |
| Rewrite location pages with local specificity | Patterns 4, 3, 6 | 5 | 3 | 15 | 2–4 hrs/page |
| Add specific pricing/timeline information to service pages | Supports E-E-A-T Trust | 4 | 3 | 12 | 1–2 hrs |
| Seed GBP Q&A with human-voice questions | Pattern 6 alignment | 4 | 5 | 20 | 30–45 min |
| Review AI detection score with Originality.ai / GPTZero | All patterns | 3 | 5 | 15 | 30 min |

---

## Step 9: AI Detection Tool Reference

Use these tools to validate AI content risk before and after humanization:

| Tool | Purpose | AI Score Threshold | Accuracy (2025) | Cost |
|------|---------|-------------------|----------------|------|
| **GPTZero** | Paragraph-level AI likelihood — industry standard | "High AI" label = rewrite; 1% false-positive | 99% claimed (lab-validated) | Freemium |
| **Originality.ai** | Page-level AI detection + plagiarism | >80% = high risk; safe: <40% after humanization | 76% (independent test) | Paid (credits) |
| **Copyleaks** | AI detection + plagiarism combined | >85% AI = rewrite | High — good for agency use | Paid |
| **Winston AI** | Enterprise AI detection + readability | >75% = flag; <40% = publish | Enterprise-grade | Paid |
| **Humaniser** | Humanization tool (9.4/10 rated 2026) | Target: 93% detector drop post-humanization | — | Paid |
| **Hemingway App** | Sentence complexity, passive voice, grade level | Flesch 60–70 / Grade 8–9 target | — | Free |
| **Grammarly** | Tone, readability, passive voice flags | Readability score ≥80 target | — | Freemium |
| **Rank Math / Yoast** | Real-time content grader (SEO + readability) | ≥80 readability score; flags AI-pattern sentences | — | Freemium/Paid |
| **Ahrefs Content Grader** | Keyword coverage + content quality grade | Grade A target | — | Paid |
| **Semrush SEO Writing Assistant** | Real-time readability + originality + tone | ≥7.0 readability score | — | Paid |
| **Google Search Console** | Monitor behavioral signals post-humanization | CTR lift + bounce rate drop after rewrite | — | Free |

**Three-step validation workflow:**
1. Pre-humanization: run GPTZero + Originality.ai → document baseline AI score (both tools — expect ±20% variance between detectors)
2. Humanize: apply pattern fixes, add first-hand experience paragraphs, fix vocabulary
3. Post-humanization: re-run both detectors → confirm score dropped below 40%; run Hemingway App → confirm Flesch ≥60 (Grade ≤9); monitor GSC behavioral signals over 30 days

---

## 10-Step Action Plan

### Immediate (Week 1 — No Developer Required)

1. **Run AI detection baseline** — Originality.ai or GPTZero on all priority pages. Document AI score per page. Effort: 30 min. Priority: 25 (5×5).
2. **Delete all chatbot artifacts** — find/replace "Feel free to," "Don't hesitate," "I hope this helps," "Certainly," "Absolutely" across entire site. Effort: 30 min. Priority: 25 (5×5).
3. **Remove all cutoff disclaimers** — search for "knowledge cutoff," "please verify," "as of my last update" — delete entirely. Effort: 15 min. Priority: 25 (5×5).
4. **AI vocabulary swap on top 5 pages** — replace "delve," "leverage," "holistic," "seamless," "robust," "testament to," "nestled," "vibrant," "landscape" (non-literal), "underscore." Effort: 1–2 hrs. Priority: 20 (5×4).
5. **Rewrite homepage hero section** — replace significance inflation + promotional language with specific first-hand claim (years in business + specific job count + neighborhood). Effort: 1–2 hrs. Priority: 20 (5×4).

### Short-Term (Week 2–4)

6. **Rewrite About page with real team profiles** — real names, photos, credentials, years of experience, certifications by license number. Add first-person voice. Effort: 2–4 hrs. Priority: 20 (4×5).
7. **Add first-hand experience paragraphs to each service page** — one paragraph per page with specific scenario, local context, and honest complexity. Effort: 1–2 hrs/page. Priority: 20 (5×4).
8. **Add specific pricing/timeline ranges to service pages** — ranges built from actual jobs (not AI-generated estimates). Effort: 1 hr. Priority: 16 (4×4).
9. **Rewrite location/service-area pages** — replace "nestled in the vibrant community of [city]" with actual neighborhood-specific content (local landmarks, building types, common issues). Effort: 2–4 hrs/page. Priority: 15 (5×3).
10. **Re-run AI detection and verify** — Originality.ai post-humanization scan. Target: all priority pages below 40% AI score. Write findings to `{AUDIT_DIR}/ai-content-findings.md`. Generate HTML to `{REPORTS_DIR}/phase-4a-ai-content.html` → PDF via `python3 scripts/generate_pdf.py --html {REPORTS_DIR}/phase-4a-ai-content.html`. Effort: 1 hr.

---

## Scoring

| Category | Weight | Score |
|----------|--------|-------|
| Average AI likelihood score across priority pages | 30% | /30 |
| Chatbot artifacts + cutoff disclaimers (present = 0) | 20% | /20 |
| E-E-A-T Experience signals present | 20% | /20 |
| Local specificity (neighborhoods, landmarks, real scenarios) | 15% | /15 |
| Vague attributions count (0 = perfect score) | 15% | /15 |

**AI Content Score = 100 − (avg AI% × 0.3) − pattern penalties**

Veto: Any page with chatbot artifacts (patterns 19–21) automatically scores ≤50 until fixed.

---

## Output

Write findings to `{AUDIT_DIR}/ai-content-findings.md` with YAML frontmatter:

```yaml
---
skill: audit/ai-content-audit
phase: 4a
date: [YYYY-MM-DD]
business: [Business Name]
url: [URL]
score: [X/100]
pages_audited: [X]
avg_ai_score: [X]%
critical_pages: [X]
chatbot_artifacts_found: [yes|no]
eeat_signals_present: [strong|weak|absent]
status: complete
---
```

Include:
- AI score per page (full table with all priority pages)
- Top 5 AI patterns found across site (frequency ranking)
- Competitive AI content benchmark (client vs. top-3 competitors)
- Page-specific humanization recommendations (specific edits, not generic advice)
- E-E-A-T reconstruction checklist
- Priority matrix (all actions, Impact × Feasibility scored)
- 30-day humanization plan with expected AI score reduction
- AI detection tool results (pre-humanization baseline)

**Key consumers:**
- `audit/content-audit` — AI content findings feed into Phase 4 overall content assessment
- `audit/onpage-seo` — humanized content improves on-page engagement signals
- `local/entity-audit` — E-E-A-T experience signals strengthen entity authority
- `ai-visibility/ai-seo` — human-voice content + FAQPage schema = higher AIO citation rate
- `cross-cutting/serp-trust-auditor` — Trustworthiness dimension directly impacted by AI content patterns
