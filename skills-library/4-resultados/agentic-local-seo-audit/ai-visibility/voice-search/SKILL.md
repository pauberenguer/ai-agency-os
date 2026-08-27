---
name: voice-search
description: >
  Voice search and conversational AI optimization. Activates when discussing
  voice search, Siri, Alexa, Google Assistant, smart speakers, conversational
  queries, speakable content, "near me" optimization, or AI answer engines.
  Phase 18. Output: {AUDIT_DIR}/voice-findings.md
---

# Voice Search Optimization Audit — Phase 18

## Executive Summary

Voice search in 2025–2026 is no longer just smart speakers — it's the entire AI conversational interface layer. Google's voice-driven AI Mode, iOS 18 Siri with deep web integration, and AI Overview voice results on mobile collectively account for 27% of mobile searches (Google internal data, 2024). "Near me" searches have grown 200%+ over 5 years. Optimizing for voice = optimizing for AI answer extraction. Local businesses missing voice optimization lose 20–30% of mobile intent queries to competitors.

---

## Tools for This Phase

| Tool | Purpose | Cost |
|------|---------|------|
| **Google PageSpeed Insights** | Mobile speed — voice results require > 70 mobile score | Free |
| **Google Rich Results Test** | FAQPage, HowTo, Speakable schema validation | Free |
| **Google Search** | Test "near me" + conversational queries — does AIO appear? | Free |
| **ChatGPT** | Test voice-style queries — is client mentioned? | Free/Paid |
| **Perplexity** | AI search visibility test for local queries | Free |
| **Google Maps / GBP** | Confirm GBP completeness for voice data extraction | Free |
| **AlsoAsked.com** | Question clusters for FAQ + voice query mapping | Freemium |
| **AnswerThePublic** | Conversational query patterns per service topic | Freemium |
| **BrightLocal** | Citation consistency check — NAP for voice accuracy | Paid |

---

## Step 1: Read Project Context

Read `{AUDIT_DIR}/intake-data.md` — business name, URL, location, services.
Read `{AUDIT_DIR}/local-findings.md` — GBP completeness (critical for local voice queries).
Read `{AUDIT_DIR}/speed-findings.md` — mobile speed score (voice requirement: > 70/100 PSI).

---

## 2025–2026 Voice Search Context

**Where voice queries originate:**
| Platform | Query Type | Local Business Impact |
|----------|-----------|----------------------|
| Google Assistant (Android + mobile) | "Near me", "Open now", hours, directions | Critical — highest local volume |
| Siri (iOS 18+) | Business info, hours, services | High — uses Apple Maps + web |
| Google AI Mode | Conversational follow-up queries | Critical — replacing traditional SERP |
| AI Overviews (voice trigger) | "How to", "What is", "Best [service] in" | High — appears for 20–35% local queries |
| Alexa / Google Home | "Find a [service] near me", business hours | Medium — smart home user base |
| ChatGPT / Perplexity voice | "Best [service] in [city]" recommendations | Growing — AI-first searchers |

**2025 voice search stats:**
- 27% of mobile searches are voice-based (Google, 2024)
- Voice search results come from pages with mobile PSI score > 70 at 97% rate (Backlinko, 2024)
- "Near me" searches grew 200%+ in 5 years
- Featured snippets are read aloud for 80%+ of voice answers (SEMrush, 2024)
- GBP is the primary data source for 90%+ of local voice responses

---

## Step 2: GBP Voice Readiness (Critical for All Local Voice Queries)

Voice assistants extract local business data directly from GBP. Missing or inaccurate GBP = wrong voice answers.

**GBP voice readiness checklist:**

| Check | Status | Fix | Effort |
|-------|--------|-----|--------|
| Business name 100% accurate (no keyword stuffing) | ✅/❌ | Edit GBP | 5 min |
| Full address including suite/unit | ✅/❌ | Edit GBP | 5 min |
| Phone number (primary click-to-call) | ✅/❌ | Edit GBP | 5 min |
| Hours: all 7 days + holidays + special hours | ✅/❌ | Edit GBP | 15 min |
| "Describe your business" (1,000 char description) | ✅/❌ | Write + edit GBP | 30 min |
| All services listed with accurate names | ✅/❌ | Add services | 30 min |
| Booking link configured (for "book a [service]" queries) | ✅/❌ | Add booking URL | 15 min |
| Q&A section with 5+ common questions answered | ✅/❌ | Add Q&As | 30–45 min |
| GBP verified and no pending flags | ✅/❌ | Verify via phone/video | 1–3 days |

**Voice query simulation via GBP:**
- "Hey Google, what time does [Business Name] close?" → reads Hours
- "Hey Google, call [Business Name]" → reads Phone
- "Hey Google, get directions to [Business Name]" → reads Address
- "Hey Google, does [Business Name] do [service]?" → reads Services + Description

---

## Step 3: Voice Query Types for Local Businesses

Map target voice queries across 4 intent categories:

### "Near Me" Queries (Highest Volume)
- "[service] near me"
- "best [service] near me"
- "[service] open now near me"
- "[service] in [neighborhood]"

**Ranking factors for "near me" voice results:**
1. GBP proximity + verified address ← #1 signal
2. GBP primary category match ← #2 signal
3. GBP review count + rating ≥ 4.0 ← #3 signal
4. Website local relevance (city mentioned in content) ← #4 signal
5. NAP citation consistency across directories ← #5 signal

### Business-Specific Queries
- "What time does [Business Name] close?"
- "Is [Business Name] open on Sunday?"
- "Phone number for [Business Name]"
- "How much does [service] cost at [Business Name]?"

### Informational/Conversational Queries
- "How do I [service-related question]?"
- "What is the best [service] for [problem]?"
- "How long does [service] take?"
- "What causes [problem that service fixes]?"

### Action-Intent Queries
- "Book a [service] appointment"
- "Call [Business Name]"
- "Get directions to [Business Name]"
- "Schedule [service] online"

---

## Step 4: Content Optimization for Conversational Queries

### FAQ Content (Primary AIO + Voice Citation Source)

**FAQ quality checklist:**
| Check | Standard | Status |
|-------|---------|--------|
| FAQ exists (standalone page or per service) | Required | ✅/❌ |
| Questions in natural conversational language | Required | ✅/❌ |
| Questions mirror actual voice query phrasing | Required | ✅/❌ |
| Answers ≤ 40–50 words (ideal for TTS reading) | Target | ✅/❌ |
| FAQPage + Question + Answer schema implemented | Required | ✅/❌ |
| Answers start with direct response (no preamble) | Required | ✅/❌ |

**Optimal FAQ answer format for voice:**
```
Q: How much does [service] cost in [City]?
A: [Service] in [City] typically costs $X–$Y. [1-sentence context].
   Call [Business] for a free quote: [phone].
```
(Under 50 words → voice-readable, AIO-citable, featured snippet-optimized)

### Featured Snippet Optimization (Voice Reads Snippets 80%+ of Time)
For each target voice query:
- [ ] Concise answer in first 40–50 words of the page (no "as mentioned above...")?
- [ ] Answer follows H2/H3 question header directly?
- [ ] Single clean paragraph or numbered list (2–4 steps)?
- [ ] No qualifiers or conditional language in first sentence?

### Speakable Schema
`SpeakableSpecification` marks sections optimal for TTS reading:
```json
{
  "@type": "SpeakableSpecification",
  "cssSelector": [".faq-answer", "h2 + p", ".direct-answer"]
}
```
Apply on: Homepage summary paragraph, all FAQ answers, key service descriptions.

---

## Step 5: Technical Voice SEO Requirements

Voice results have strict technical requirements:

| Requirement | Threshold | Check Method |
|-------------|-----------|-------------|
| Mobile PageSpeed | ≥ 70 PSI score | PageSpeed Insights → Mobile |
| LCP | < 2.5s | PageSpeed Insights → LCP |
| TTFB | < 800ms | WebPageTest |
| HTTPS | All pages | `curl -I https://[domain]` |
| Mobile-responsive | Full responsiveness at 375px | Chrome DevTools → Device toolbar |
| Tap targets | ≥ 44px (voice → tap follow-up) | Lighthouse → Tap Targets |

**Schema for voice ranking:**
| Schema Type | Voice Use Case | Priority |
|------------|---------------|---------|
| `LocalBusiness` (complete) | Hours, phone, address, directions | Critical |
| `FAQPage` | Q&A voice answers | Critical |
| `HowTo` | Process/instructional queries | High |
| `Speakable` | Marks voice-optimal content sections | Medium |
| `OpeningHoursSpecification` | Hours queries | Critical |
| `ContactPoint` | Phone/contact queries | High |
| `GeoCoordinates` | "Near me" precision | High |

---

## Step 6: AI Assistant Visibility Test

Test across all major AI platforms using voice-style queries:

**Test protocol:**
```
Query 1: "Who is the best [service] in [city]?"
Query 2: "Find me a [service provider] near [location]"
Query 3: "[Business Name] — what are their services and hours?"
Query 4: "How do I [most common service-related question]?"
```

| Platform | Query | Business Mentioned? | Accurate Info? | Source Cited? | Fix Needed |
|----------|-------|-------------------|----------------|---------------|------------|
| ChatGPT | Q1 | Yes/No | Yes/No/N.A. | [URL or N/A] | |
| Perplexity | Q1 | Yes/No | Yes/No/N.A. | [URL or N/A] | |
| Gemini | Q2 | Yes/No | Yes/No/N.A. | [URL or N/A] | |
| Google AIO | Q2 | Yes/No | Yes/No/N.A. | [URL or N/A] | |
| Siri | Q3 | Yes/No | Yes/No/N.A. | GBP | |

**If business not mentioned by ChatGPT/Perplexity:** Entity signals too weak — prioritize entity audit (Phase 9) + AIO optimization (Phase 14).

---

## Step 7: Competitor Voice Visibility Comparison

| Competitor | GBP Complete? | FAQ Schema? | Mobile Score | Voice Mentions (ChatGPT) | Voice Mentions (Perplexity) |
|-----------|-------------|------------|------------|--------------------------|--------------------------|
| Client | ✅/❌ | ✅/❌ | [X] | Yes/No | Yes/No |
| Comp 1 | ✅/❌ | ✅/❌ | [X] | Yes/No | Yes/No |
| Comp 2 | ✅/❌ | ✅/❌ | [X] | Yes/No | Yes/No |

---

## Voice Search Opportunity Matrix

For top 20 voice queries:

| Voice Query | Current Position | Featured Snippet? | FAQPage Schema? | Voice Optimized? | Priority |
|-------------|-----------------|-------------------|----------------|-----------------|---------|
| [near me query] | [pos] | Yes/No | Yes/No | Yes/No | H/M/L |
| [business-specific] | [pos] | Yes/No | Yes/No | Yes/No | H/M/L |

---

## Priority Matrix

| Action | Impact (1–5) | Feasibility (1–5) | Priority | Effort |
|--------|-------------|-------------------|---------|--------|
| Complete GBP Q&A section (5+ questions) | 5 | 5 | 25 | 30–45 min |
| Add FAQPage schema to all service pages | 5 | 5 | 25 | 30 min/page |
| Write 10 FAQ answers ≤ 50 words each | 5 | 4 | 20 | 1–2 hrs |
| Add Speakable schema to FAQ sections | 4 | 4 | 16 | 1–2 hrs |
| Fix mobile PSI score to ≥ 70 | 5 | 3 | 15 | 2–16 hrs |
| Add HowTo schema to process pages | 4 | 4 | 16 | 30 min/page |
| Improve GBP description to 1,000 chars | 3 | 5 | 15 | 30 min |
| Add GeoCoordinates schema | 3 | 5 | 15 | 15 min |
| Add Speakable to homepage summary | 3 | 4 | 12 | 15 min |

---

## Scoring

| Category | Weight | Score |
|----------|--------|-------|
| GBP completeness for voice queries | 30% | /30 |
| FAQ content + FAQPage schema | 25% | /25 |
| Mobile page speed (PSI ≥ 70) | 20% | /20 |
| Featured snippet presence for top queries | 15% | /15 |
| Structured data completeness (full schema set) | 10% | /10 |

---

## Output

Write findings to `{AUDIT_DIR}/voice-findings.md` with YAML frontmatter:

```yaml
---
skill: ai-visibility/voice-search
phase: 18
date: [YYYY-MM-DD]
business: [Business Name]
url: [URL]
score: [X/100]
gbp_complete: [yes|no|partial]
faqpage_schema: [yes|no|partial]
mobile_psi: [X]
featured_snippets: [X]
chatgpt_mentioned: [yes|no]
perplexity_mentioned: [yes|no]
---
```

Include:
- Score X/100 with per-category breakdown
- GBP voice readiness checklist (all 9 checks)
- AI assistant visibility test results (all 4 platforms)
- Top 20 voice query opportunity matrix (position + optimization status)
- Content gaps for FAQ/conversational content
- Schema audit (present vs. missing, per page type)
- Competitor voice comparison table
- Priority matrix (all actions, Impact × Feasibility scored)
- Quick wins list (items fixable in < 1 hour — expected score gain)
- 30-day voice optimization plan

**Key consumers:**
- `ai-visibility/ai-seo` — voice and AIO share many optimization signals
- `local/local-seo` — GBP completeness feeds both voice + local pack
- `audit/speed-optimization` — mobile speed is voice prerequisite

---

## Voice Search Quick Reference

### 10-Step Voice Optimization Action Plan

1. **Audit GBP completeness** — all 9 checks (name, address, phone, hours, description, services, booking link, Q&A, verification). Effort: 30–45 min. Priority: 25 (5×5).
2. **Add FAQPage schema to all service pages** — each page needs 3–5 FAQs ≤50 words each. AIO reads FAQPage for 80%+ of voice answers. Effort: 30 min/page. Priority: 25 (5×5).
3. **Fix mobile PSI score to ≥70** — voice results pulled from pages scoring ≥70 at 97% rate (Backlinko 2024). Use PageSpeed Insights to identify LCP/INP/CLS issues. Effort: 2–16 hrs depending on root cause.
4. **Seed GBP Q&A with 5+ question/answer pairs** — focus on "hours", "parking", "cost", "emergency service" patterns. Effort: 30 min. Priority: 20 (5×4).
5. **Write conversational FAQ content** — 10 FAQ answers using AnswerThePublic clusters. Each ≤50 words, starts with a direct answer. Effort: 1–2 hrs. Priority: 20 (5×4).
6. **Add Speakable schema to FAQ sections** — targets Google Assistant audio readout. Use `speakable` property on FAQ container. Effort: 1–2 hrs.
7. **Test across 5 AI platforms** — run all 4 test queries on ChatGPT, Perplexity, Gemini, Google AIO, Siri. Document results in Voice Opportunity Matrix. Effort: 30 min.
8. **Add HowTo schema to process pages** — "how to [service]" voice queries trigger HowTo schema readout. Effort: 30 min/page.
9. **Optimize content for E-E-A-T voice signals** — voice assistants prefer content from established entities. Add author bio, business credentials, years-in-business signals to FAQ pages. Effort: 1–2 hrs.
10. **Write 30-day voice optimization plan** — record voice-findings.md to `{AUDIT_DIR}/voice-findings.md` + save PDF report to `{REPORTS_DIR}/phase-18-voice.pdf`. Effort: 30 min.

### INP + Voice Search Connection (2025)

Voice platforms extract answers from fast-rendering pages. **INP (Interaction to Next Paint, replaced FID March 2024)** is a ranking signal that also affects voice eligibility:
- INP <200ms = Good (voice-eligible tier)
- INP 200–500ms = Needs Improvement
- INP >500ms = Poor (de-prioritized by voice ranking systems)

High INP on FAQ pages is caused by: heavy JS frameworks blocking interaction, lazy-loaded FAQ accordions, and third-party chat widgets. Fix by deferring non-critical JS and using static HTML FAQ sections.

### E-E-A-T + Voice Authority (2025)

Voice assistants prefer cited entities with strong E-E-A-T signals:
| Signal | Voice Impact | Implementation |
|--------|-------------|---------------|
| Schema `sameAs` (GBP + LinkedIn + Wikipedia) | High | Entity schema on homepage |
| Author bio with credentials | Medium | On all FAQ pages |
| Business established date | Medium | `foundingDate` in LocalBusiness schema |
| Review count ≥50 on GBP | High | Review velocity strategy |
| GBP description 900–1,000 chars | Critical | Edit GBP description |

**Write HTML report to `{REPORTS_DIR}/phase-18-voice.html` and convert to PDF via `python3 scripts/generate_pdf.py --html {REPORTS_DIR}/phase-18-voice.html`.**
- `output/report-generation` — voice score in master report section 18
