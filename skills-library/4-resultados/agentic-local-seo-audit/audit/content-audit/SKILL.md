---
name: content-audit
description: >
  Content quality and strategy assessment. Activates when auditing content,
  reviewing pages, assessing content quality, checking for thin content,
  duplicate content, content cannibalization, AI-generated low-quality content,
  service pages, location pages, blog posts, or FAQ content.
  Phase 4. Output: {AUDIT_DIR}/content-inventory.md
---

# Content Audit — Phase 4

## Executive Summary

Content quality is the primary differentiator between sites that rank and sites that don't in 2025. Google's Helpful Content System (HCS), integrated into the core algorithm in March 2024, actively penalizes template-based, AI-generated-without-expert-review, and thin location pages. The key thresholds: ≥60% unique content per location page (hard floor — below this risks HCS penalty), ≥80% unique (competitive target). FAQPage schema on service pages triggers AIO citations at 3.2× the rate of pages without it (Amsive 2025). Content decay (>20% YoY impressions decline) now affects most sites that haven't refreshed since 2022–2023 — ChatGPT cites pages updated within 30 days at 76.4% vs. 31.2% for 90+ day old content. The fastest wins: add FAQPage schema (30 min/page), refresh decayed content with updated stats, and fix service pages below 800 words.

**2025 content benchmarks:**
- Service pages: minimum 800 words; competitive 1,200–2,000 words (HCS 2025 standards)
- Location pages: ≥60% unique (hard floor); ≥80% unique (competitive target)
- Content decay threshold: >20% YoY click decline → refresh required (GSC comparison)
- FAQPage schema → 3.2× AIO citation rate (Amsive 2025); HowTo schema = structured step extraction
- Pillar page threshold: 25+ total articles in cluster = topical authority signal (SEMrush 2024)
- AI-generated content: acceptable only with documented human expert review (Google Webmaster guidelines 2025)

---

## Step 1: Read Project Context & Run Crawl

Read `{AUDIT_DIR}/intake-data.md` — business name, services, location, goals.
Read `{AUDIT_DIR}/technical-findings.md` — indexation data, duplicate content flags.

```bash
# Run crawler if not already done (from technical-seo or here)
python3 scripts/site_crawler.py --url [URL] --max-pages 150 --output {DATA_DIR}/crawl/ --csv
```

**Tools for this phase:**
| Tool | Purpose | Cost |
|------|---------|------|
| **Screaming Frog** | Word counts, title/meta duplicates, thin pages (<300 words), canonicals | Paid/Free (≤500 URLs) |
| **Siteliner** | Duplicate content % across site, most-linked pages (free up to 250 pages) | Free |
| **SEMrush** | GSC import — traffic per page, keyword ranking per page, content decay analysis | Paid |
| **Surfer SEO** | Content Score per page vs. competitors — targets 70+ (cluster) / 80+ (pillar) | Paid |
| **Clearscope** | Content grade per page — target A- (pillar) / B+ (cluster) | Paid |
| **Copyscape** | External duplicate content detection — scraped copies | Paid |
| **Google Search Console** | Page-level impressions/clicks — identify content decay (>20% YoY decline) | Free (requires access) |
| **site_crawler.py** | `--csv` output: word counts, status codes, title/meta data per page | Free (local) |

**2025 Content Context:**
Google's Helpful Content System (HCS) was folded into the core ranking algorithm in March 2024. Since then:
- Template location pages (only city name swapped) are actively penalized — need ≥60% unique content
- Bulk AI-generated content without expert review triggers scaled content abuse signals
- Content with >20% YoY impressions decline requires refresh or consolidation
- FAQPage schema + direct standalone answers = primary AI Overview (AIO) citation trigger

---

## Section 1: Content Inventory

Build a complete inventory of all indexed pages using crawler output:

| URL | Page Type | Title | Word Count | Primary Keyword | Quality (1–10) | Issues |
|-----|----------|-------|-----------|----------------|----------------|--------|
| /services/[slug] | Service | | | | | |
| /locations/[slug] | Location | | | | | |
| /blog/[slug] | Blog | | | | | |

**Page Types to Catalog:**
- Homepage (often thin — should have 600+ words explaining services, location, differentiators)
- Service pages (one per service offered)
- Location/area pages
- Blog posts / articles
- FAQ page (standalone or distributed on service pages)
- About page
- Contact page
- Testimonials/Reviews page
- Gallery/Portfolio page
- Staff/Team pages

**Content Quality Score (1–10):**
| Score | Description |
|-------|-------------|
| 9–10 | Comprehensive (meets word count threshold), unique, expert-authored, well-structured, current-year data, optimized |
| 7–8 | Good — missing some depth, freshness, or schema optimization |
| 5–6 | Average — basic information, lacks differentiation or competitor-matching depth |
| 3–4 | Thin — <600 words, near-duplicate template, or outdated >2 years |
| 1–2 | Very poor — scraped, auto-generated, or near-empty |

**Word count thresholds (2025 HCS standards):**
| Page Type | Minimum | Competitive Target | Red Flag |
|-----------|---------|-------------------|---------|
| Homepage | 600 words | 800–1,200 | <400 |
| Service page | 800 words | 1,200–2,000 | <500 |
| Location page | 600 words | 900–1,500 | <400 |
| Pillar blog post | 2,500 words | 3,500–5,000 | <1,200 |
| Cluster blog post | 1,200 words | 1,500–2,500 | <600 |
| FAQ entry | 150 words | 250–400 | <100 |

---

## Section 2: Critical Content Issues

### Thin Content (<600 words for service/location pages)
From crawler output: `{DATA_DIR}/crawl/crawl-data.csv` → filter by word count:

| URL | Page Type | Word Count | Traffic | Action |
|-----|----------|-----------|---------|--------|
| [URL] | Service | [count] | [visits] | Expand / Merge / Redirect |

**Action criteria:**
- <600 words + has organic traffic → expand with expert content (priority)
- <600 words + zero traffic + low search volume → 301 redirect to parent service page
- <600 words + zero traffic + has backlinks → expand (preserve link equity)

### Duplicate Content (Internal)
From Siteliner or Screaming Frog → filter by duplicate content %:

| Pages | Similarity % | Issue Type | Action |
|-------|------------|-----------|--------|
| [URL1] vs. [URL2] | [%] | Template location pages | Differentiate or canonical |
| [URL1] vs. [URL2] | [%] | Category + post archive | Canonical to canonical URL |

**Location page template check:**
- Paste 2 location pages in a diff tool → measure unique content %
- Target: ≥80% unique per page pair
- Hard floor: ≥60% (below = HCS penalty risk)

### Content Cannibalization
Multiple pages competing for the same primary keyword:

| Keyword | Competing Pages | Current Ranking | Action |
|---------|---------------|----------------|--------|
| [keyword] | [URL1], [URL2] | P[X], P[Y] | Consolidate / Redirect / Differentiate |

**Detection:** GSC → Performance → click on keyword → check if multiple URLs rank. Also Ahrefs → Site Explorer → Organic Keywords → filter for duplicate keyword targeting.

### Content Decay Detection (Using GSC)
Export GSC Performance → compare last 90 days vs. same period last year (YoY):

| URL | Current Clicks | YoY Clicks | Change % | Action |
|-----|--------------|-----------|---------|--------|
| [URL] | [X] | [Y] | -[%] | Refresh if >20% decline |

**2025 rule:** >20% YoY decline → refresh queue. >50% YoY decline → major rewrite or consolidate. ChatGPT cites content updated within 30 days at 76.4% rate — freshness directly affects AIO citation rate.

### AI-Generated Low-Quality Content (HCS 2025 Risk)
Google's Helpful Content System specifically targets:
- Bulk AI-generated pages without human expertise review (scaled content abuse signal)
- Content covering all angles superficially rather than any deeply
- Location × service pages with near-identical content (only city name different)
- Content with high bounce rate + zero dwell time + no engagement signals

**Detection:** Look for pages with uniform template structure across service/location variations. Check bounce rate and engagement time in GA4.

---

## Section 3: Service Pages Assessment

For EACH service offered (from intake-data.md):

| Service | Page Exists? | URL | Word Count | Unique? | FAQPage Schema? | Quality |
|---------|------------|-----|-----------|---------|----------------|---------|
| [service 1] | Yes/No | [url] | [count] | Yes/No | Yes/No | [1-10] |

**Ideal service page checklist (target ≥1,200 words):**
- [ ] Primary keyword in H1, title tag, first 100 words
- [ ] What the service is (definition in first 50 words — AIO extraction target)
- [ ] How the process works (numbered steps — HowTo schema opportunity)
- [ ] Why choose this business (credentials, experience, differentiators)
- [ ] Pricing signals ("Starting from $X" or "Free quote — no obligation")
- [ ] 5+ FAQs specific to this service (FAQPage schema — AIO trigger)
- [ ] Testimonials from customers who used this specific service
- [ ] CTA: Call / Book / Get Quote (with click-to-call phone)
- [ ] LocalBusiness + Service schema
- [ ] City/location modifier in page copy and title
- [ ] Surfer Content Score ≥70 vs. competing pages

### Competitor Service Page Comparison
| Service | Client Word Count | Surfer Score | Comp 1 Words | Comp 2 Words | Gap |
|---------|-----------------|------------|------------|------------|-----|
| [service] | | | | | |

---

## Section 4: Location/Area Pages Assessment

For EACH service area:

| Location | Page Exists? | URL | Word Count | Unique Content % | Map Embed? | FAQPage Schema? | Score |
|----------|------------|-----|-----------|----------------|-----------|----------------|-------|
| [city] | Yes/No | [url] | [count] | [%] | Yes/No | Yes/No | [1-10] |

**Ideal location page checklist (target ≥900 words):**
- [ ] City-specific title: "[Service] in [City, State]"
- [ ] Unique opening paragraph (local landmarks, neighborhoods, area context)
- [ ] Services specific to this area (not generic list)
- [ ] Local testimonials from customers in this city
- [ ] Embedded map showing service area coverage
- [ ] Local NAP in `<address>` tag
- [ ] LocalBusiness schema with `areaServed` for this location
- [ ] FAQPage schema with 3+ location-specific questions (AIO trigger)
- [ ] Internal links to main service pages
- [ ] ≥60% unique content vs. other location pages (hard floor)
- [ ] ≥80% unique content (competitive target)

---

## Section 5: Blog Content Assessment

Pull GSC data (Page performance) + Screaming Frog (word counts):

| Title | URL | Word Count | Last Updated | Primary Keyword | SERP Position | Monthly Clicks | Score |
|-------|-----|-----------|-------------|---------------|--------------|---------------|-------|
| [title] | [url] | | | | | | |

**Flag and prioritize:**
| Flag | Definition | Action | Priority |
|------|-----------|--------|---------|
| High impressions, low CTR (<2%) | Title/meta not compelling | Rewrite title + meta | High |
| Ranking P4–P10 | Quick win opportunity | Expand + add schema | High |
| >20% YoY clicks decline | Content decay | Refresh — new stats, examples | Critical |
| Zero internal links to service pages | Missed conversion opportunity | Add contextual CTAs | Medium |
| <1,200 words | Below competitive threshold | Expand or consolidate | High |
| No FAQPage schema | Missing AIO opportunity | Add FAQ section + schema | High |

---

## Section 6: FAQ Content Assessment

- Standalone FAQ page exists? URL: [url] — word count: [X]
- FAQs distributed on relevant service pages?
- FAQs based on real questions from: GSC queries / GBP Q&A / sales team / PAA boxes?
- FAQPage schema on all FAQ-containing pages?
- Test: do any FAQs appear in Google AIO? (Search each FAQ question — does client's answer appear?)

**Missing FAQ topics (cross-reference AlsoAsked.com PAA data):**
| Question (from PAA) | Page It Should Be On | Currently Answered? |
|--------------------|---------------------|-------------------|
| [question] | [service page] | Yes/No |

---

## Section 7: Content for AI Extraction (2025 Priority)

AIO and AI assistants cite content that is structured for direct extraction. Check each key page:

| Check | Homepage | Service Pages | Location Pages | Blog |
|-------|---------|--------------|---------------|------|
| Direct standalone answer in first 40–60 words | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Clear service/term definitions | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Specific data points (costs, timelines) stated precisely | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Numbered step-by-step processes | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Structured comparisons (tables) | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| FAQPage schema | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |
| Content updated within 90 days | ✅/❌ | ✅/❌ | ✅/❌ | ✅/❌ |

---

## Section 8: Content Strategy Assessment

### Pillar + Cluster Coverage
- Clear content pillars (main topic hubs at ≥2,500 words)?
- Each pillar with cluster pages (1,200+ words) linking to it?
- All cluster pages linked back to pillar?
- 25+ total articles per main cluster (authority threshold)?

### Funnel Coverage
| Funnel Stage | Coverage | Pages Count | Quality |
|-------------|---------|------------|---------|
| TOFU (Awareness — educational, informational) | Strong/Weak/None | | |
| MOFU (Consideration — comparison, how-to, case study) | Strong/Weak/None | | |
| BOFU (Decision — service pages, testimonials, pricing) | Strong/Weak/None | | |

### Content Type Diversity
| Type | Present? | Count | Quality | Frequency |
|------|---------|-------|---------|-----------|
| Service pages | | | | N/A |
| Location pages | | | | N/A |
| How-to guides | | | | |
| FAQ content (with schema) | | | | |
| Case studies (with specifics) | | | | |
| Cost/pricing guides | | | | |
| Video content (with VideoObject schema) | | | | |
| Comparison pages ("X vs. Y") | | | | |
| Tool/calculator | | | | |

---

## Numbered Action Plan

### Immediate (Week 1 — Quick Wins, <2 hrs each)
1. **Add FAQPage schema to all service pages** — 5 FAQ minimum per service page, answers ≤50 words each, implement JSON-LD FAQPage. Validate at search.google.com/test/rich-results. Effort: 30 min/page. Expected: 3.2× AIO citation rate (Amsive 2025). Priority: 20.
2. **Rewrite all page intros to include standalone 40–60 word answers** — First paragraph must answer "What is [service] and who needs it?" directly. This is the AIO extraction point. Effort: 20 min/page. Priority: 20.
3. **Add internal CTAs to all blog posts** — Every blog post should link to ≥1 relevant service page with conversion-focused anchor text. Effort: 15 min/post. Priority: 15.
4. **Fix content decay pages (>20% YoY decline)** — Add current year stats, update examples, refresh introduction. Even minor updates reset ChatGPT freshness factor. Effort: 1–2 hrs/page. Priority: 16.
5. **Resolve cannibalization (top priority pairs first)** — For each cannibalized keyword pair: keep strongest page (by traffic + backlinks), 301 redirect weaker version OR canonicalize. Effort: 1–2 hrs per pair. Priority: 16.

### Short-Term (Week 2–4)
6. **Expand thin service pages to ≥800 words** — For each service page <800 words: add Process section (HowTo schema opportunity), FAQ section (5+ questions), Pricing section (cost range), testimonials from this specific service. Effort: 3–5 hrs/page. Priority: 20.
7. **Differentiate location pages to ≥60% unique** — For each location page pair with >40% overlap: add local landmarks, area-specific testimonials, neighborhood context, local FAQ. Track unique content % with diff tool. Effort: 3–5 hrs/page. Priority: 15.
8. **Add HowTo schema to all process pages** — Any page with numbered steps gets HowTo schema. AI extracts step sequences directly for voice + AIO. Effort: 30 min/page. Priority: 16.
9. **Create missing BOFU content** — If no pricing guide, comparison page, or case study exists: create at least 1 per main service. These pages convert at 3–5× the rate of informational pages. Effort: 4–8 hrs/piece. Priority: 12.
10. **Run Surfer/Clearscope audit on top 5 service pages** — Score each vs. top competitors. Pages below 70 (Surfer) or B+ (Clearscope) need NLP entity coverage expansion. Effort: 1–2 hrs/page. Priority: 16.

### Medium-Term (Month 2–3)
11. **Build pillar + cluster structure** — Identify 3 main service pillars. Create/upgrade pillar pages to 2,500+ words. Map cluster pages (1,200+ words each) to each pillar. Target 25+ articles per cluster for topical authority signal. Effort: 8–12 hrs/pillar.
12. **Create original local data/research content** — Survey 50+ customers or compile local market data → publish as "[City] [Industry] Report 2025". AIO preferentially cites original data. Effort: 20–40 hrs. Expected: 5–15 editorial links + AIO citation priority.

## Competitor Content Benchmark

| Metric | Client | Comp 1 | Comp 2 | Comp 3 | Gap to Leader |
|--------|--------|--------|--------|--------|---------------|
| Avg service page word count | | | | | |
| % service pages with FAQPage schema | | | | | |
| % location pages (HCS-unique ≥60%) | | | | | |
| Total blog posts | | | | | |
| Pillar pages (2,500+ words) | | | | | |
| Surfer Score avg (top service pages) | | | | | |
| AIO citations (core service queries) | | | | | |

## Priority Matrix

| Issue | Impact (1–5) | Feasibility (1–5) | Priority | Effort |
|-------|-------------|-------------------|---------|--------|
| Service pages <800 words | 5 | 4 | 20 | 3–5 hrs/page |
| Missing FAQPage schema on service pages | 4 | 5 | 20 | 30 min/page |
| No AIO-structured content (no direct answers) | 4 | 5 | 20 | 1–2 hrs/page |
| Content decay >20% YoY decline | 4 | 4 | 16 | 3–5 hrs/page |
| Cannibalization (2+ pages same keyword) | 4 | 4 | 16 | 1–2 hrs |
| Blog posts P4–P10 (quick wins) | 4 | 4 | 16 | 2–4 hrs/post |
| Location pages <60% unique | 5 | 3 | 15 | 3–5 hrs/page |
| Blog posts with no service page CTAs | 3 | 5 | 15 | 15 min/post |
| Missing location pages for served cities | 3 | 4 | 12 | 3–5 hrs/page |

---

## Scoring

| Category | Weight | Score |
|----------|--------|-------|
| Content quality score average (1–10) | 20% | /20 |
| No thin/duplicate content | 20% | /20 |
| Service page completeness (word count + schema + FAQ) | 20% | /20 |
| Location page uniqueness (≥60% hard floor, ≥80% target) | 15% | /15 |
| Content type diversity (TOFU/MOFU/BOFU coverage) | 15% | /15 |
| AI-citable content structure (FAQPage, direct answers, tables) | 10% | /10 |

**Veto:** >50% of service pages <600 words → maximum score 50/100.

---

## Output (Handoff)

Write complete inventory to `{AUDIT_DIR}/content-inventory.md` with YAML frontmatter:

```yaml
---
skill: audit/content-audit
phase: 4
date: [YYYY-MM-DD]
business: [Business Name]
url: [URL]
score: [X/100]
total_pages: [X]
thin_pages: [X]
decay_pages: [X]
service_pages: [X]
location_pages: [X]
---
```

Include:
- Score X/100 with per-category breakdown
- Complete content inventory table (all pages, word count, quality score)
- Critical issues: thin, duplicate, cannibalization, decay
- Service pages assessment (word count vs. threshold, Surfer score, checklist)
- Location pages uniqueness % (all pairs compared)
- Blog content table with traffic + position data
- FAQ audit (coverage + schema status)
- AI-extraction readiness checklist
- Content strategy gaps (pillar/cluster model, funnel coverage)
- Priority matrix (all issues, Impact × Feasibility scored)
- 30/90-day content improvement plan

**Key consumers:**
- `research/content-gaps` — identifies missing content vs. competitors
- `research/topical-gaps` — maps topical coverage using this inventory
- `cross-cutting/serp-trust-auditor` — Ranking Signals dimension
- `output/report-generation` — content score in master report section 4

---

## Content Audit Quick Reference

### Content Quality Decision Table (2025 HCS Standards)

| Page State | Signal | Decision | Action | Effort |
|-----------|--------|---------|--------|--------|
| <300 words, no unique value | Thin content | Noindex or delete + 301 | Redirect to stronger page | 15 min |
| 300–600 words, some value | Borderline thin | Expand or consolidate | Merge with related page | 2–4 hrs |
| 600–1,500 words, good content | Acceptable | Monitor | Add FAQPage schema, internal links | 30 min |
| 1,500–3,000 words, optimized | Good | Maintain | Refresh stats quarterly | 1 hr/quarter |
| 3,000+ words, original data | Excellent | Protect | Build cluster around it | Ongoing |
| Duplicate of another page | Duplicate | Canonical or 301 | Add canonical pointing to original | 15 min |
| AI-generated, no editorial review | HCS risk | Rewrite or add expert review | Add author byline + unique insights | 2–4 hrs |

### GBP + Content Audit Connection (2025)
GBP reviews contain keyword signals Google uses to understand business topics. During content audit:
- Compare GBP review language (common words customers use) with page content language
- If customers say "emergency plumber" but pages say "urgent plumbing" → misaligned terminology → update page content to match customer language
- GBP Q&A unanswered = topic signal Google sees as weak coverage → answer all Q&A + create page for recurring questions

### INP + Content Rendering
Content-heavy pages (3,000+ words) with embedded images, videos, and widgets often have high INP — heavy DOM causes slow interactions. During content audit, flag pages that are both content-thin AND INP >500ms for dual-priority treatment (content expansion + performance fix simultaneously).

### Content Decay by Type (2025 Benchmarks)

| Content Type | Decay Rate | Refresh Trigger | Update Frequency |
|-------------|-----------|----------------|-----------------|
| Service pages (local) | Slow (12–24 mo) | >20% YoY click drop | Annually + on price/service change |
| Blog posts (news/trends) | Fast (3–6 mo) | >30% YoY click drop | Quarterly |
| FAQ pages | Medium (6–12 mo) | New PAA questions appear | Semi-annually |
| Location pages | Slow (18–24 mo) | Competitor adds stronger page | Annually |
| Comparison/alternative pages | Fast (4–8 mo) | New competitors enter market | Quarterly |
