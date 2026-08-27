---
name: topical-authority
description: >
  Topical authority assessment and building strategy. Activates when discussing
  domain topical authority, expertise signals, content authority building,
  Knowledge Graph topic recognition, E-E-A-T content authority, or competitive
  authority positioning. Phase 8. Output: {AUDIT_DIR}/topical-authority.md
---

# Topical Authority Audit — Phase 8

## Executive Summary

Topical authority is the long-term competitive moat in local SEO and the primary determinant of AI visibility in 2025–2026. Google's Helpful Content System (integrated March 2024) explicitly rewards depth over breadth — sites that comprehensively cover a narrow topic cluster outrank sites that superficially cover many topics. The measurable threshold: 25+ articles in a cluster begins accumulating topical authority signals in GSC (SEMrush 2024). AI Overviews cite topically authoritative brands 2–3× more than generalist sites. The 58% AIO surge across 9 industries in early 2026 (Amsive) is directly correlated with businesses that achieved complete cluster coverage vs. those with fragmented content. For local businesses, topical authority on 3–5 core service clusters is more valuable than shallow coverage of 15+ topics.

**2025–2026 topical authority benchmarks:**
- Pillar pages: minimum 3,000 words; competitive 5,000–10,000 words; Surfer Score ≥80; Clearscope A-
- Cluster pages: minimum 1,500 words; target 2,000–3,000 words; Surfer Score ≥70; Clearscope B+
- Article threshold per cluster: 25+ = authority signal building; 50+ = competitive; 100+ = dominant
- Minimum viable cluster for AIO eligibility: 1 pillar + 10–15 cluster pages
- Content decay: >20% YoY click decline = refresh; >50% = rewrite or consolidate + 301
- ChatGPT freshness: 30-day update = 76.4% citation rate; AI Overviews prefer content <3–6 months old
- AIO topical citation: 58% AIO surge for businesses with full cluster coverage (Amsive early 2026)
- Clustered content performance: 30% more organic traffic; holds rankings 2.5× longer (HireGrowth 2025)
- SEMrush Topical Authority score: ≥70 in core topic = competitive; ≥85 = market leader
- First ranking improvements: 2–3 months after cluster launch; significant gains: 6–12 months
- December 2025 Core Update: focused on E-E-A-T depth; June 2025 update targeted link authority — combined enforcement is most aggressive post-HCU cycle

**Local business cluster size benchmarks:**
| Business Type | Minimum Cluster | Growth Target | Notes |
|--------------|----------------|--------------|-------|
| Single-location local | 10–15 pages | 25–30 in 12 months | Service + location pillar structure |
| Multi-location regional | 1 pillar + 5–8 pages/location | 25+ pages per core location | Unique content per location required |
| Enterprise/national | 25+ pages per topic cluster | 50–100+ per cluster | No duplicate SAP content (HCU risk) |

**Numbered Action Plan:**

### Immediate (Week 1)
1. **Run Ahrefs Content Gap vs. top 3 competitors** — Filter for keywords competitors rank for in top 10 that client doesn't. Export all, sort by traffic value. Identify top 20 cluster gaps to fill first. Effort: 2 hrs.
2. **Audit existing pillar pages** — Check each pillar page: word count vs. 3,000 minimum, Surfer Score vs. 80 target, last updated date vs. 90-day freshness window. Flag any failing ≥2 criteria as critical refresh. Effort: 1 hr.
3. **Fix orphaned cluster pages** — Run site_crawler.py → find pages with <3 inbound internal links that should be cluster pages → add links from pillar page and 2 related cluster pages. Effort: 15 min/page. Priority: 20 (5×4).
4. **Add FAQPage schema to all cluster pages** — 5 FAQ minimum per page, answers ≤50 words. AIO citation 3.2× higher with FAQPage. Effort: 30 min/page.
5. **Refresh top content decay pages (>20% YoY decline)** — Update statistics, add current year examples, add FAQPage schema, update publish date. Even minor updates reset ChatGPT 30-day freshness. Effort: 1–2 hrs/page.

### Short-Term (Month 1)
6. **Expand thin pillar pages** — Pillar pages <3,000 words: add Surfer-recommended NLP entities, expand subtopic sections, add HowTo schema for process steps, build to 3,000–4,500 words. Effort: 6–10 hrs/pillar.
7. **Build next 5 cluster pages** — For highest-gap cluster topic identified in step 1: create 1,500-word pages targeting one subtopic each. Link each back to pillar. Effort: 3–5 hrs/page.
8. **Add expert author bylines** — Every piece of topic content should have a named author with credentials, linked author page, and Person schema. E-E-A-T author entity = measurable trust signal. Effort: 1–2 hrs setup.
9. **Add `knowsAbout` to Organization schema** — List 5–7 specific topic entities the business is authoritative on. Directly signals topical domain expertise to Google NLP. Effort: 15 min.
10. **Earn topical editorial links** — Pitch 2 local publications with topic-specific expert commentary. Each editorial mention from an authority source strengthens topical entity co-citation. Effort: 4–8 hrs/pitch.

---

## Step 1: Read Project Context

Read `{AUDIT_DIR}/intake-data.md` — business name, URL, services, location.
Read `{AUDIT_DIR}/topical-gaps.md` — topical coverage map and identified gaps.
Read `{AUDIT_DIR}/competitor-profiles.md` — competitor authority signals.
Read `{AUDIT_DIR}/content-inventory.md` — content quality baseline.

**Tools for this phase:**
| Tool | Purpose | Cost |
|------|---------|------|
| **Ahrefs** | Topical authority via Domain Rating, organic traffic per topic cluster, content gap vs. competitors | Paid |
| **SEMrush** | Topic Research, Topical Authority score (0–100 per domain per topic), Keyword Gap | Paid |
| **Surfer SEO** | Content Score per page (target: 80+ for pillar, 70+ for cluster), NLP entity coverage | Paid |
| **Clearscope** | Content grade per page (target: A- for pillar, B+ for cluster), entity density analysis | Paid |
| **MarketMuse** | Topic model completeness, content brief generation, competitive content gap | Paid |
| **Google Search Console** | Which topics drive clicks — existing authority signals (free, requires access) | Free |
| **AlsoAsked.com** | PAA topic mapping — identify question clusters per topic pillar | Freemium |
| **Google Trends** | Topic momentum — rising vs. declining topics in the niche | Free |

**2025–2026 Topical Authority Context:**
- Google's AI Overviews (AIO) cite topically authoritative brands **2–3× more** than generalist sites
- Businesses that publish a minimum of **25 articles** on a topic cluster begin accumulating topical authority signals measurable in GSC (early 2026 observation)
- **58% AI Overview surge** across 9 industries in early 2026 — topical authority now directly determines AI citation rate
- **ChatGPT cites content updated within last 30 days** at 76.4% vs. 23.6% for older content — freshness is a citation factor
- Content decay: >20% YoY decline in clicks or impressions on a page signals topical authority loss on that cluster

---

## Section 1: Topical Authority Score (Per Core Topic)

For each main service/topic the business should own, score 5 dimensions:

### Scoring Dimensions
| Dimension | 1 (Weak) | 5 (Leader) | Assessment Method |
|-----------|---------|-----------|------------------|
| **Depth** | Surface 500-word overview | 3,000+ word expert pillar with unique data/case studies | Screaming Frog word count + manual quality check |
| **Breadth** | <5 subtopics covered | 20+ subtopics with dedicated pages | Ahrefs → Site Explorer → Organic Keywords → filter by topic |
| **Freshness** | Last updated 2+ years ago | Updated within 90 days, current-year stats | GSC → Performance → filter by page, check impressions trend |
| **Quality** | Generic AI-generated content | Unique expert insights, original data, proprietary methods | Manual review vs. Surfer Content Score ≥80 |
| **Recognition** | No featured snippets or PAA | Owns 5+ snippets, cited in AIO, topic entity in Knowledge Panel | Ahrefs → SERP Features filter; manual AIO search |

### Authority Matrix

| Core Topic | Depth /10 | Breadth /10 | Freshness /10 | Quality /10 | Recognition /10 | Total /50 | Grade |
|-----------|-----------|------------|--------------|------------|----------------|---------|-------|
| [service 1] | | | | | | | |
| [service 2] | | | | | | | |
| [local topic] | | | | | | | |

**Grade:** 45–50 = A (Market Leader) | 35–44 = B (Competitive) | 25–34 = C (Developing) | <25 = D/F (Weak)

**Article count per cluster (2025 threshold):**
| Cluster | Articles Published | Status |
|---------|------------------|--------|
| [topic] | [X] | <25 = below threshold / 25–50 = building / 50+ = authority |

---

## Section 2: Content Depth Standards (2025 Benchmarks)

| Page Type | Minimum Words | Surfer Target Score | Clearscope Grade | Internal Links |
|-----------|-------------|--------------------|--------------------|---------------|
| Pillar page | 3,000 | 80+ | A- or higher | 8–15 cluster links out |
| Cluster page | 1,500 | 70+ | B+ | 1 pillar + 3–5 cluster links |
| Supporting page | 900 | 65+ | B | 1 cluster or pillar link |
| FAQ entry | 250 | N/A | N/A | 1 service/pillar link |

Pages failing these thresholds are topical authority liabilities — they signal low expertise to Google's Helpful Content System.

**Content decay detection (using GSC):**
- Export GSC Performance data → compare this 90 days vs. same period last year
- Flag any page with >20% YoY decline in clicks or impressions → add to refresh queue
- Flag any page with >50% YoY decline → prioritize for full rewrite or consolidation

---

## Section 3: Competitor Authority Comparison

Use **Ahrefs** (Domain Rating + organic traffic per cluster) and **SEMrush** Topical Authority score:

| Topic | Client Pages | Client TA Score | Comp 1 Pages | Comp 1 TA | Comp 2 Pages | Comp 2 TA | Gap | Priority |
|-------|------------|----------------|------------|---------|------------|---------|-----|---------|
| [topic 1] | | | | | | | | H/M/L |
| [topic 2] | | | | | | | | H/M/L |

**Authority Leader Analysis:**
- Who leads for each topic? What content volume/depth gives them the edge?
- Use **Ahrefs Content Gap**: enter client domain vs. top 2 competitors → identify which topic clusters competitors rank for that client doesn't
- What is the page-count gap to match the leader per cluster?
- Which competitor has the highest Surfer Content Score on their pillar pages?

**Topical Dominance Opportunities:**
Topics where competitors have only 1–3 thin pages that client could dominate with a strong cluster:
| Topic | Competitor Coverage | Client Coverage | Opportunity Score |
|-------|-------------------|----------------|------------------|
| [topic] | [X thin pages] | [Y pages] | High/Med/Low |

---

## Section 4: Authority Signals Assessment

### Content Authority Signals (E-E-A-T)
- [ ] Expert author bylines with credentials on all topic-relevant content?
- [ ] Author pages: professional background, certifications, years of experience?
- [ ] Original research, local data, or client case studies published?
- [ ] Content citing authoritative sources (government, research, trade associations)?
- [ ] Unique perspectives not found elsewhere (proprietary methods, real project outcomes)?
- [ ] Real-world examples from actual client work (photos, outcomes, specifics)?

### Structural Authority Signals
- [ ] Complete topic clusters: pillar + cluster + supporting content (25+ articles per main cluster)?
- [ ] Internal links consistently reinforcing topic hierarchy (all cluster pages link to pillar)?
- [ ] All related subtopics covered — no significant gaps vs. AlsoAsked/PAA?
- [ ] Content comprehensiveness exceeds top competitor on Surfer side-by-side comparison?

### AI Visibility Authority Signals (2025 Critical)
- [ ] AIO appears for core topic queries? (`best [service] in [city]` — does client appear?)
- [ ] ChatGPT/Perplexity mentions client for core topic queries?
- [ ] Content updated within last 30 days on key pillar pages (freshness = AI citation factor)?
- [ ] FAQPage schema on all pillar pages (primary AIO trigger)?
- [ ] HowTo schema on service/tutorial pages?

### Recognition Authority Signals
- [ ] Featured snippets owned for core topic keywords? (Check Ahrefs → SERP Features)
- [ ] PAA boxes answered by site content? (Use AlsoAsked.com to map PAA questions)
- [ ] AI Overviews citing site for core topics? (Manual test: search 5 core queries)
- [ ] Google Knowledge Graph associating brand with topics?

### External Authority Signals
- [ ] Cited by other authoritative sites in the niche (editorial links, not paid)?
- [ ] Quoted in local news or industry publications?
- [ ] Industry association membership + content contribution?
- [ ] Speaking mentions or expert features in media?

---

## Section 5: Knowledge Graph Topic Association

Does Google associate this business with its core topics?

### Tests to Run
1. Search `[business name]` → does Knowledge Panel show core topics/services?
2. Search `[business name] [core topic]` → does Google show topic association in results?
3. Search `[core topic] [city]` → does Knowledge Panel or AIO mention this business?
4. Ask ChatGPT: `Who are the top [service] providers in [city]?` → is business mentioned?

### Measuring Topical Authority (Tool Methods)

**Ahrefs — Traffic Share Proxy (manual formula):**
> Topical Authority Proxy = Traffic Share for Target Topic ÷ Total Traffic from Topic Keywords
- Ahrefs → Keyword Explorer → enter seed keyword → "Traffic Share by Domains" → compare your share vs. top 3 competitors
- Use Competing Domains report to find true topical competitors (not just DR-similar sites)
- Content Gap: Competitive Analysis → Content Gap → export → cluster by topic → gaps where all competitors rank but you don't = highest-priority content needs

**SEMrush — Topical Authority Score:**
- Keyword Gap → sort by "Missing" (full cluster gaps) vs. "Weak" (depth gaps, positions 11–50)
- Apply Intent filter: "Informational" = missing educational content; "Commercial" = missing comparison content
- Focus: KD ≤40 + Volume ≥100/month = quick-win cluster gaps
- AI Visibility Toolkit: identify LLM prompts where competitors are cited but client isn't

**Knowledge Graph / Entity Authority:**
- Create or claim Wikidata Q-ID entry — directly recognized by Google Knowledge Graph (54 billion+ entities indexed)
- Wikidata Q-ID URL → add to `sameAs` in Organization schema → directly feeds entity resolution
- NAP citation consistency across Yelp, BBB, industry associations, Chamber of Commerce → entity authority signal
- Co-citation pattern: earn mentions on authoritative third-party domains with consistent entity terminology

### Building Topic Association (Sequence)
1. Publish minimum 25 articles on target topic cluster (threshold for authority accumulation)
2. Create or claim Wikidata entry with Q-ID → add Q-ID URL to Organization schema `sameAs`
3. Add Schema.org `knowsAbout` to Organization schema with 5–7 core topic entities
4. Earn editorial links from authoritative sites mentioning business in topic context
5. Submit updated sitemap after publishing cluster content
6. Ensure all cluster pages link to pillar with descriptive anchor text (varied, not exact-match on all — avoid repetitive anchor text to same page)

---

## Section 6: Content Quality Standard (2025–2026)

For topical authority in 2025–2026, content must clear this bar:
- ✅ Written or reviewed by a genuine subject matter expert (named, credentialed)
- ✅ Contains specific, verifiable details competitors don't mention
- ✅ Includes original data, local examples, or proprietary perspectives
- ✅ Structured for both human readers and AI extraction (H2 hierarchy, FAQ, tables)
- ✅ Updated within 90 days — current-year statistics cited
- ✅ Demonstrates experience: real photos, case outcomes, specific project details
- ✅ Surfer Content Score ≥70 (cluster) or ≥80 (pillar)
- ❌ NOT bulk AI-generated without expert review (Helpful Content penalty risk)
- ❌ NOT generic "Here are 5 tips..." without depth and specifics
- ❌ NOT padded with filler to hit word count without adding information value
- ❌ NOT a content page with >20% YoY traffic decline left unrefreshed

---

## Section 7: Authority Building Roadmap

### Priority Matrix (Impact × Feasibility)
| Gap Type | Impact (1–5) | Feasibility (1–5) | Priority Score | Effort |
|----------|-------------|-------------------|----------------|--------|
| Thin pillar page (<1,500 words) → expand to 3,000+ | 5 | 4 | 20 | 6–10 hrs |
| Cluster below 25-article threshold | 5 | 3 | 15 | 4 hrs/article |
| Content decay: page losing >20% YoY clicks | 4 | 4 | 16 | 3–5 hrs/page |
| Missing FAQPage schema on pillars | 4 | 5 | 20 | 30 min/page |
| Expert author bylines missing | 4 | 5 | 20 | 1–2 hrs/page |
| Orphaned cluster pages (no link to pillar) | 4 | 5 | 20 | 15 min/page |
| Low Surfer Content Score (<65) | 4 | 4 | 16 | 2–4 hrs/page |
| AIO not appearing for core queries | 5 | 3 | 15 | 4–8 hrs (cluster expansion) |

### Immediate Priority (Next 30 Days)
1. Add FAQPage schema to all pillar pages — triggers AIO — Effort: 30 min/page — Priority: 20
2. Fix all orphaned cluster pages — add internal links to pillar — Effort: 15 min each — Priority: 20
3. Expand thin pillar pages to 3,000+ words with Surfer optimization — Effort: 6–10 hrs each
4. Refresh top 5 content decay pages (>20% YoY decline) — update stats, examples, schema

### Medium-Term (Days 31–90)
1. Build each cluster to 25+ articles (threshold for Google authority accumulation)
2. Add expert author bylines with credentials to all existing topic content
3. Commission original local study or data piece per pillar (primary AI citation trigger)
4. Use Ahrefs Content Gap to fill cluster pages competitors rank for that client doesn't

### Long-Term (Months 3–6)
1. Achieve 50+ article coverage on primary topic clusters
2. Build Clearscope grade A- on all pillar pages and B+ on all cluster pages
3. Earn 5+ editorial links from authoritative sites per core topic
4. Establish author entity associations in Google Knowledge Graph

---

## Output

Write to `{AUDIT_DIR}/topical-authority.md` with YAML frontmatter:

```yaml
---
skill: strategy/topical-authority
phase: 8
date: [YYYY-MM-DD]
business: [Business Name]
url: [URL]
score: [X/100]
status: [leader|competitive|developing|weak]
topics_assessed: [X]
avg_cluster_article_count: [X]
---
```

Include:
- Score X/100 with per-topic breakdown
- Topic authority matrix (5 dimensions per core topic)
- Content depth table with Surfer Score targets
- Competitor authority comparison (TA score, page count, content quality)
- Authority signals checklist (content, structural, AI visibility, recognition, external)
- Content decay report (pages with >20% YoY decline)
- Knowledge Graph association status
- Priority authority building roadmap (Impact × Feasibility scored)
- 30/90/180-day content plan

**Key consumers:**
- `research/topical-gaps` — gap analysis informs authority building priorities
- `research/keyword-gaps` — keyword opportunities mapped to authority clusters
- `output/report-generation` — topical authority score in master report section 8

**Output files:**
- `{AUDIT_DIR}/topical-authority.md` — primary findings with score, matrix, roadmap
- `{REPORTS_DIR}/phase-8-topical-authority.pdf` — auto-generated PDF after phase completes

---

## Recommendations Checklist

### Quick Wins (Week 1, <2 hrs each)
- [ ] Add FAQPage schema to all pillar pages — AIO citation 3.2× higher — Effort: 30 min/page
- [ ] Fix orphaned cluster pages (no link to pillar) — Effort: 15 min/page — Priority: 20
- [ ] Add `knowsAbout` to Organization schema (5–7 topic entities) — Effort: 15 min
- [ ] Update publish date + add current-year stat to top 3 decay pages — Effort: 30 min/page
- [ ] Add HowTo schema to all service/process pages — Effort: 30 min/page

### Topical Authority by Cluster Stage

| Cluster Stage | Article Count | Actions Needed | Timeline |
|--------------|--------------|----------------|---------|
| Not started | 0 | Build pillar + 5 cluster pages | Month 1 |
| Below threshold | 1–24 | Reach 25-article minimum | Month 1–3 |
| Building | 25–49 | Add depth, fix orphans, refresh decay | Month 2–4 |
| Authority | 50+ | Lateral linking, original data, AI citation optimization | Ongoing |

### E-E-A-T Implementation Table

| Signal | How to Implement | Effort | Impact |
|--------|-----------------|--------|--------|
| Expert author bylines | Named author + credentials on all content | 1–2 hrs setup | High |
| Author schema | `author` property linking to author entity page | 30 min/page | High |
| Original research | Local survey, proprietary pricing data, case studies | 8–16 hrs/piece | Very High |
| Wikidata entity | Create Q-ID entry → add to Organization sameAs | 1–2 hrs | Medium |
| Expert source citations | Link to government, research, trade association data | 30 min/page | Medium |
| Real project photos | Before/after, on-site images with schema | 1 hr/gallery | High |

### Topical Authority Specific Thresholds Table

| Metric | Below Threshold | Competitive | Market Leader | Tool to Measure |
|--------|----------------|-------------|--------------|----------------|
| Pillar page word count | <2,000 words | 3,000–5,000 words | 5,000–10,000 words | Screaming Frog word count |
| Surfer Content Score (pillar) | <65 | 70–79 | ≥80 | Surfer SEO Content Editor |
| Clearscope grade (pillar) | C or lower | B+ | A- or higher | Clearscope |
| Articles per cluster | <10 | 10–24 | 25+ (authority threshold) | Ahrefs Site Explorer |
| Internal links (cluster → pillar) | 0 | 1 | 2–3 (varied anchors) | Screaming Frog inlinks |
| Content freshness | >12 months old | 3–12 months | Updated within 90 days | GSC Performance filter |
| Featured snippets owned (per cluster) | 0 | 1–3 | 5+ | Ahrefs SERP Features filter |
| AIO citations (manual test) | 0/5 queries | 1–2/5 queries | 3+/5 queries | Manual search + incognito |
| SEMrush Topical Authority score | <50 | 50–69 | ≥70 (competitive); ≥85 (leader) | SEMrush Domain Overview |
| INP (Core Web Vital) | >500ms Poor | 200–500ms Needs Work | <200ms Good | PageSpeed Insights |

### GBP Integration with Topical Authority (2025)
GBP service listings directly feed AI Overviews for local topical queries. For each topic cluster:
- Add matching services to GBP service menu (name + description keyword-rich)
- Seed GBP Q&A with topical questions from AlsoAsked.com PAA research
- Ensure GBP business description mentions core topic clusters (first 150 chars indexed)
- Review responses: naturally incorporate service keywords (e.g., "Thank you for choosing us for your emergency plumbing repair in [city]")
