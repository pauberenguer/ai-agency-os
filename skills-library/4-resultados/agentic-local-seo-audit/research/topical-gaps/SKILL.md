---
name: topical-gaps
description: >
  Topical map and gap analysis. Activates when discussing topic gaps, topical
  maps, content clusters, topic coverage, semantic coverage, topical authority
  building, or content planning at the topical level.
  Phase 7. Output: {AUDIT_DIR}/topical-gaps.md
---

# Topical Gap Analysis — Phase 7

## Executive Summary

Topical authority is the #1 long-term competitive moat in local SEO. Google's Helpful Content System (integrated into core algorithm March 2024) rewards businesses that comprehensively cover a topic cluster vs. those that superficially mention many topics. The 25-article threshold signal: sites with 25+ articles in a cluster receive significantly stronger topical authority signals than sites with 10 or fewer (SEMrush 2024). AI Overviews (AIO) cite topically authoritative sources 2–3× more than shallow coverage sites. This phase maps the client's topical universe, identifies coverage gaps vs. top competitors, and produces a prioritized content roadmap.

**2025–2026 topical authority benchmarks:**
- Pillar pages: minimum 3,000 words; competitive 5,000–10,000 words for high-competition topics
- Cluster pages: minimum 1,500 words; competitive 2,000–2,500 words; Surfer Score ≥70
- Supporting/spoke pages: 800–1,500 words; 3–5 internal links per 1,000 words
- Minimum viable cluster: 1 pillar + 5 cluster pages (starting point); 10–15 = AIO eligibility threshold
- Authority threshold: 25+ articles per cluster = topical authority signal begins accumulating (SEMrush 2024)
- Content decay trigger: >20% YoY click decline → refresh required; >50% → full rewrite or consolidate
- AIO topical citation: 58% AIO surge for businesses with full topic cluster coverage (Amsive early 2026)
- ChatGPT freshness factor: pages updated within 30 days cited at 76.4% rate; AI Overviews prefer content <3–6 months old
- Clustered content vs. standalone: 30% more organic traffic; holds rankings 2.5× longer (HireGrowth 2025)
- Early ranking improvements: 2–3 months after cluster launch; significant topical authority gains: 6–12 months

**Pillar-to-cluster ratio benchmarks:**
| Stage | Pillar : Cluster | Use Case |
|-------|-----------------|----------|
| Starting point | 1 + 3–5 | Small teams, new businesses |
| AIO-eligible | 1 + 10–15 | Local business growth stage |
| Authority building | 1 + 20–30+ | Competitive niches, multi-service businesses |

**Numbered Action Plan:**

### Immediate (Week 1)
1. **Map the complete topical universe** — list all Level 1 pillars (main services), Level 2 clusters (subtopics), Level 3 supporting angles. Use AlsoAsked.com for PAA tree and SEMrush Topic Research for visual cluster map. Effort: 2–3 hrs.
2. **Run Ahrefs Content Gap vs. top 3 competitors** — Competitive Analysis → Content Gap → enter your domain + 3 competitors → export and cluster by topic. Identify full clusters you're entirely missing vs. individual keyword gaps. Effort: 1–2 hrs.
3. **Audit existing cluster completeness** — for each service, count: pillar page? cluster pages? supporting pages? Flag clusters below 5 pages as "not started." Effort: 1 hr.
4. **Fix orphaned cluster pages** — run site_crawler.py → find cluster pages with <3 inbound internal links → add contextual link from pillar (within body copy, not just navigation). Effort: 15 min/page. Priority: 20 (4×5).
5. **Add FAQPage schema to all pillar pages** — AIO cites pages with FAQPage schema at 3.2× rate. 5 FAQ minimum per pillar, answers ≤50 words. Effort: 30 min/page.

### Short-Term (Week 2–4)
6. **Create missing high-priority cluster pages** — gaps where all competitors have pages but client doesn't. Target 1,500+ words, link to pillar immediately on publish. Effort: 3–5 hrs/page. Priority: 16 (4×4).
7. **Expand thin pillar pages to 3,000+ words** — use Surfer SEO (target score ≥80) to identify missing NLP entities and sections. Add HowTo schema for process steps. Effort: 6–10 hrs/pillar.
8. **Answer top 10 PAA questions per pillar** — AlsoAsked.com → extract top 10 questions → add as FAQ entries on relevant service pages + FAQPage schema. Effort: 1–2 hrs. Expected: AIO citation + PAA box wins.
9. **Map semantic gaps** — identify missing entities (service types, local landmarks, certifications) and concepts (industry jargon vs. customer language, regional naming variants). Effort: 1 hr.
10. **Build original data/statistics page per pillar** — original research = primary AI citation trigger. Local survey, real project data, proprietary pricing benchmarks. Effort: 8–16 hrs. Priority: 12 (4×3).

---

## Step 1: Read Project Context

Read `{AUDIT_DIR}/intake-data.md` — business name, services, location.
Read `{AUDIT_DIR}/content-inventory.md` — current content map.
Read `{AUDIT_DIR}/content-gaps.md` — identified topic and format gaps.
Read `{AUDIT_DIR}/keyword-gaps.md` — keyword opportunities.

**Tools for this phase:**
| Tool | Purpose | Cost |
|------|---------|------|
| **Ahrefs Topics Explorer** | Discover topic clusters and subtopics | Paid |
| **Ahrefs Content Gap** | Find topics competitors rank for that client doesn't | Paid |
| **SEMrush Topic Research** | Visual topic cluster mapping | Paid |
| **SEMrush Keyword Gap** | Competitor topical coverage comparison | Paid |
| **AlsoAsked.com** | PAA-based question mapping per topic | Freemium |
| **AnswerThePublic** | Visualize question clusters around topics | Freemium |
| **Google PAA boxes** | Live "People Also Ask" questions per pillar | Free |
| **Surfer SEO** | NLP-based content brief with entity coverage | Paid |
| **Google Search Console** | Which topics drive clicks (existing authority) | Free |

**2025–2026 Topical Authority Context:**
Google's Helpful Content system (folded into core algorithm March 2024) and AI Overviews reward demonstrable expertise across a topic cluster. Surface-level coverage of many topics is penalized; deep coverage of fewer topics ranks. The goal is topic clusters where every subtopic links to a pillar, and every pillar is internally linked from cluster pages. Google's December 2025 Core Update focused heavily on E-E-A-T and expertise signals; the June 2025 update targeted link authority — the two together now enforce topical depth more aggressively than any prior update cycle.

**Content Depth Thresholds (2025 benchmarks):**
| Page Type | Minimum Words | Target Words | Surfer Score | Internal Links |
|-----------|-------------|-------------|-------------|---------------|
| Pillar page | 3,000 | 5,000–10,000 | ≥80 | 8–15 cluster links out |
| Cluster page | 1,500 | 2,000–2,500 | ≥70 | 1 pillar link + 2–3 cluster links |
| Supporting page | 800 | 1,000–1,500 | ≥65 | 1 cluster or pillar link |
| FAQ entry | 200 | 300–500 | N/A | 1 service/pillar link |

**Content Decay by Content Type (Research 2025):**
| Content Type | Typical Decay Timeline | Update Frequency |
|-------------|----------------------|-----------------|
| Technology/software | 4–6 months | Quarterly |
| Local service content | 12–24 months | Semi-annually minimum |
| List/roundup pages | 3–4 months | Quarterly (new entrants change landscape) |
| Educational/evergreen | 12–18 months | Annually + on stat change |
| AI-heavy niches | 2–4 months | Quarterly (rapid evolution) |

---

## Section 1: Complete Topical Universe Mapping

### Define the Core Topical Universe
For this business, list ALL possible topics that could be relevant:

**Level 1 — Main Topics (Pillars):**
The broadest topics the business should be authoritative on.
Example (for a plumber): Emergency Plumbing, Drain Services, Water Heaters, Pipe Repair, Bathroom Plumbing, Kitchen Plumbing, Outdoor Plumbing, Commercial Plumbing

**Level 2 — Subtopics (Clusters):**
Under each pillar, the key subtopics.
Example under "Water Heaters": Types of Water Heaters, Water Heater Installation, Water Heater Repair, Water Heater Replacement, Tankless vs. Tank, Cost Guide, Troubleshooting

**Level 3 — Supporting Topics:**
Specific questions, comparisons, how-tos under each subtopic.
Example under "Water Heater Installation": How long does it take, What's included, DIY vs. Professional, Building permits needed, Cost breakdown

---

## Section 2: Client vs. Ideal Topical Coverage

### Coverage Map

```
PILLAR: [Main Topic]
├── CLUSTER: [Subtopic]
│   ├── Supporting: [specific angle] → Client: ✅ EXISTS / ❌ MISSING / ⚠️ THIN
│   ├── Supporting: [specific angle] → Client: ✅ / ❌ / ⚠️
│   └── Supporting: [specific angle] → Client: ✅ / ❌ / ⚠️
├── CLUSTER: [Subtopic]
│   └── [...]
Status: Not Started | Partial (X/Y pages) | Complete
Priority: 1-5 | Relevance: H/M/L | Competition: H/M/L
```

Repeat for each of the main service topic pillars.

---

## Section 3: Cluster Completeness Analysis

For each content cluster, score completeness:

| Cluster | Total Subtopics | Client Coverage | % Complete | Competitor Leader % | Priority |
|---------|---------------|----------------|-----------|--------------------|---------|
| [cluster] | [X] | [Y pages] | [X%] | [comp name X%] | H/M/L |

**Pillar Page Assessment:**
- Does a strong pillar page exist for each main topic?
- Pillar page quality: comprehensive? 2,000+ words? All subtopics linked?
- Cluster pages linked back to pillar?
- Pillar page receiving adequate internal links?

---

## Section 4: Semantic Coverage Analysis

### Missing Entities
Key entities that should appear in topic coverage but don't:
- [Entity type]: [specific entity missing and why it matters]

### Missing Concepts
Important concepts/terminology not covered:
- [concept]: [pages where it should appear but doesn't]

### Missing Questions (PAA Analysis)
For each main topic pillar, check PAA boxes and identify unanswered questions:
| Question | PAA Source | Client Answers This? | Content Needed |
|---------|-----------|---------------------|---------------|
| [question] | [Google PAA] | No | [blog post / FAQ entry] |

### Synonym and Variation Coverage
- Are common synonyms for services covered?
  Example: "water heater" vs. "hot water heater" vs. "boiler"
- Industry jargon vs. customer language — both covered?
- Regional naming variants (if applicable)?

---

## Section 5: Topical Authority Gap vs. Competitors

For each major topic, how does topical authority compare?

| Topic | Client Pages | Comp 1 Pages | Comp 2 Pages | Gap | Priority |
|-------|------------|------------|------------|-----|---------|
| [main service] | [X] | [Y] | [Z] | [+/-X] | H/M/L |
| [subtopic] | [X] | [Y] | [Z] | [+/-X] | H/M/L |

**Topical Dominance Opportunities:**
Which topics could this business fully dominate that competitors partially cover?
- [topic]: Client has [X] pages, competitors have [1-2 thin pages] → opportunity to dominate

---

## Section 6: AI Visibility Topical Gaps

AI Overviews and AI assistants increasingly look for topical depth. Gaps in topic coverage = missing from AI recommendations.

**AI Coverage Test:**
For each main topic pillar, ask: "If I asked ChatGPT/Gemini for comprehensive info on [topic] in [city], would this business's content support being cited?"

Identify which pillars need more depth for AI citation:
| Pillar | AI-Citable Content? | What's Needed |
|--------|-------------------|--------------|
| [topic] | No | [specific content types] |

---

## Section 7: Prioritized Topical Content Roadmap

### Priority Matrix (Impact × Feasibility)

| Gap Type | Impact (1–5) | Feasibility (1–5) | Priority Score | Effort Estimate |
|----------|-------------|-------------------|----------------|----------------|
| Missing pillar page (competitor has 3,000+ word guide, client has nothing) | 5 | 3 | 15 | 8–12 hrs |
| Missing cluster page (all competitors rank, client absent) | 4 | 4 | 16 | 3–5 hrs |
| Thin pillar page (<1,500 words) — expand to 3,000+ | 4 | 4 | 16 | 4–6 hrs |
| Missing FAQ / PAA answers | 3 | 5 | 15 | 1–2 hrs |
| Orphaned cluster pages (exist but not linked to pillar) | 4 | 5 | 20 | 30 min |
| Missing AI-citable data/statistics page | 4 | 3 | 12 | 4–6 hrs |
| Missing location × service intersection page | 3 | 4 | 12 | 2–4 hrs |

### Immediate Priority (Next 30 Days)
1. **Fix orphaned cluster pages** — add `<a href="/[pillar-url]">` internal link from every cluster page to its parent pillar. Also add cluster link from pillar. Effort: 30 min each. Priority: 20 (4×5). Expected: direct PageRank flow improvement.
2. **Create/upgrade pillar pages to 3,000+** words — For top 2 service clusters with missing or thin pillars: build comprehensive pillar pages using Surfer SEO (target score ≥80) + Clearscope (target A-). Include: all subtopics, 5+ FAQs, HowTo schema, unique local data/statistics. Effort: 8–12 hrs each.
3. **Fill "red" cluster gaps** — Clusters where ALL competitors have pages but client doesn't: create 1,500+ word cluster pages, link to pillar immediately after publish. Effort: 3–5 hrs each.
4. **Answer top 10 PAA questions** — Use AlsoAsked.com for each pillar topic → extract top 10 PAA questions → add as FAQ entries on relevant service pages + FAQPage schema. Effort: 1–2 hrs. Expected: AIO citation + PAA box wins.
5. **Add FAQPage schema to ALL cluster pages** — AIO cites pages with FAQPage at 3.2× rate. Add 5 FAQ minimum per page. Effort: 30 min/page. Priority: 20.

### Numbered Action Steps (Comprehensive)
| Step | Action | Effort | Priority | Expected Impact |
|------|--------|--------|---------|----------------|
| 1 | Fix orphaned cluster links (pillar ↔ cluster) | 30 min/page | 20 | PageRank distribution |
| 2 | Expand thin pillar to 3,000+ words + Surfer ≥80 | 8–12 hrs each | 15 | Rankings lift + AIO |
| 3 | Create missing cluster pages (red gaps) | 3–5 hrs each | 16 | New keyword rankings |
| 4 | Add PAA-based FAQ content + FAQPage schema | 1–2 hrs | 15 | AIO + PAA boxes |
| 5 | Refresh content decay pages (>20% YoY) | 2–4 hrs each | 16 | Traffic recovery |
| 6 | Build original data/statistics page per pillar | 8–16 hrs | 12 | AI citation priority |
| 7 | Create location × service intersection pages | 2–4 hrs each | 12 | Local long-tail rankings |
| 8 | Monitor Google Trends weekly for emerging topics | 30 min/week | 10 | First-mover advantage |

### Medium-Term (Days 31–90)
1. Build out secondary clusters topic-by-topic using Ahrefs Content Gap data
2. Create supporting topic content for each established cluster
3. Publish FAQ hub pages for each pillar with schema markup (FAQPage + HowTo)
4. Build original data/statistics pages — survey customers, create localized studies

### Long-Term (Months 3–6)
1. Complete coverage of all topic pillars to topical authority status
2. Build seasonal sub-clusters (holiday, weather-related, emergency services)
3. Create emerging topic content before competitors (monitor Google Trends + AlsoAsked weekly)
4. Commission original research/case studies per pillar — primary data = AI citation priority

---

## Deliverable: Complete Topical Map

```
TOPICAL AUTHORITY MAP — [Business Name]
Generated: [Date]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PILLAR 1: [Main Service/Topic]
├── CLUSTER: [Subtopic]
│   ├── ✅ [Existing page URL] — [title]
│   ├── ❌ MISSING: [page idea] — Priority: High | Est. Traffic: [X/mo]
│   └── ⚠️ THIN: [existing URL] — needs expansion
├── CLUSTER: [Subtopic]
│   └── [...]
Overall Status: [X]% complete
Gap vs. Leader: [X] pages needed to match [competitor]

PILLAR 2: [Main Service/Topic]
[...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOPICAL COVERAGE SCORE: [X]%
Pages needed to reach 80% coverage: [X] pages
Estimated time to topical authority: [X months]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Output

Write complete topical map and gap analysis to `{AUDIT_DIR}/topical-gaps.md` with YAML frontmatter. Write HTML report to `{REPORTS_DIR}/phase-7-topical-gaps.html` and convert to PDF via `python3 scripts/generate_pdf.py`.

```yaml
---
skill: research/topical-gaps
phase: 7
date: [YYYY-MM-DD]
business: [Business Name]
url: [URL]
score: [X/100]
status: complete
topical_coverage_pct: [X%]
pillars_mapped: [X]
gaps_identified: [X]
---
```

**Key consumers:**
- `strategy/topical-authority` — uses map for authority building strategy
- `research/keyword-gaps` — maps keyword data onto topical gaps
- `output/report-generation` — topical coverage % in master report section 7

---

## Topical Gap Quick Reference

### Cluster Completeness Scoring Table

| Cluster Status | Page Count | Pillar? | Cluster Pages? | AIO Eligible? | Action |
|---------------|-----------|---------|---------------|--------------|--------|
| Not started | 0 | No | No | No | Build pillar + 5 cluster pages first |
| Minimal | 1–4 | Maybe | 1–3 | No | Expand to 10+ pages, add FAQPage schema |
| Building | 5–14 | Yes | 4–13 | Maybe | Fill cluster gaps, fix orphaned pages |
| AIO threshold | 15–24 | Yes | 14–23 | Yes | Add supporting pages, original data |
| Authority | 25+ | Yes | 20+ | Yes (priority) | Maintain freshness, earn editorial links |

### Content Decay Detection Table (INP + Freshness)

| Signal in GSC | Interpretation | Action | Effort |
|--------------|----------------|--------|--------|
| Impressions ↓ >20% YoY, position stable | Topical coverage weakening | Add depth, update stats, expand subtopics | 2–4 hrs/page |
| Impressions ↓ >50% YoY | Severe authority loss | Full rewrite or consolidate + 301 | 4–8 hrs/page |
| CTR ↓, impressions stable | Title/meta mismatch with search intent | Rewrite title + meta; check SERP features | 30 min/page |
| Position slipping from P1→P3 | Competitor added stronger content | Expand word count, add original data, add FAQPage | 3–6 hrs/page |
| Zero impressions on new page | Indexation or orphan issue | Check GSC URL Inspection; add internal links | 30 min |

### E-E-A-T Signals by Content Tier

| Tier | Page Type | Required E-E-A-T Signal | How to Add |
|------|-----------|------------------------|-----------|
| Tier 1 | Pillar page | Expert author byline + original data/research | Add `author` schema + local case study/survey |
| Tier 2 | Cluster page | Specific expertise signals + cited sources | Link to government/trade association sources |
| Tier 3 | Supporting/FAQ | Real-world examples or testimonials | Add quote from client or specific local context |
| All tiers | Any content | Updated within 90 days | Update stats, add current-year examples |

### GBP + Topical Authority Connection (2025)
GBP Q&A is an underused topical authority signal. Seed GBP Q&A with questions matching your cluster topics — Google pulls GBP Q&A content into AI Overviews for local service queries. Each seeded Q&A pair that appears in AIO = measurable topical authority signal for that cluster.
