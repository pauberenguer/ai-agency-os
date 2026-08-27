# SERP-TRUST Scoring Framework

**Search Engine Results Page — Technical Reliability, User Signals & Search Trust**

Version: 1.0 | 50 Items | Scoring: 0-4 per item | Max Raw: 200 | Normalized: 0-100

---

## Scoring Scale

| Score | Label | Meaning |
|-------|-------|---------|
| 0 | Critical | Broken, missing, or actively harmful to rankings |
| 1 | Poor | Exists but significantly below standards |
| 2 | Fair | Partially implemented, notable gaps remain |
| 3 | Good | Correctly implemented with minor improvements possible |
| 4 | Excellent | Best-in-class, fully optimized, competitive advantage |

---

## T — Technical Foundation (10 items)

| ID | Item | 0 (Critical) | 1 (Poor) | 2 (Fair) | 3 (Good) | 4 (Excellent) |
|----|------|-------------|----------|----------|----------|----------------|
| T01 | Crawlability | Robots.txt blocks critical pages | Major crawl issues (noindex errors, blocked resources) | Minor crawl issues, some orphan pages | Clean crawl, all key pages accessible | Perfect crawl health, proactive budget optimization |
| T02 | Indexation Ratio | <30% of pages indexed | 30-50% indexed | 50-75% indexed | 75-90% indexed | 90%+ indexed, zero unwanted pages in index |
| T03 | XML Sitemap | Missing | Exists but errors or stale | Valid but incomplete | Complete, auto-updated, submitted to GSC | Dynamic, segmented, image/video sitemaps included |
| T04 | SSL & Security | No HTTPS or expired cert | HTTPS with mixed content | HTTPS clean, missing security headers | HTTPS + HSTS + basic security headers | Full security headers (CSP, X-Frame, X-Content-Type) |
| T05 | Canonical Tags | Missing entirely | Present but conflicting/incorrect | Self-referencing on most pages | Correct on all pages including paginated | Perfect canonical strategy including cross-domain |
| T06 | Redirect Health | Redirect loops or chains >3 hops | Chains of 2-3 hops, some 302s used as 301s | Minor chains, mostly correct status codes | Clean redirects, all 301 where permanent | Zero chains, documented redirect map, monitored |
| T07 | Structured Data | None | Basic Organization only | LocalBusiness + Breadcrumbs | Full schema suite (FAQ, Service, Review, HowTo) | Comprehensive schema, zero errors, rich results earned |
| T08 | Mobile Optimization | Not mobile-friendly | Responsive but usability errors | Responsive, minor tap target issues | Fully responsive, no usability errors | Mobile-first optimized, PWA features |
| T09 | URL Structure | Dynamic params, uppercase, no logic | Some clean URLs, inconsistent patterns | Mostly clean, minor issues (length, stop words) | All clean, keyword-inclusive, logical hierarchy | Perfect URL taxonomy, flat architecture, SEO-optimal |
| T10 | JavaScript Rendering | Critical content hidden behind JS | Key content requires rendering, not pre-rendered | Most content SSR/SSG, some JS-dependent | All critical content server-rendered | Full SSR/SSG + graceful JS enhancement |

## R — Ranking Signals (10 items)

| ID | Item | 0 | 1 | 2 | 3 | 4 |
|----|------|---|---|---|---|---|
| R01 | Title Tags | Missing or duplicated across site | Present but generic, no keywords | Keywords present, some too long/short | Unique, keyword-optimized, correct length | CTR-optimized, keyword-front-loaded, brand formula |
| R02 | Meta Descriptions | Missing | Present but duplicated or generic | Unique, but no CTA or keyword gaps | Unique, keyword-rich, includes CTA | Compelling, CTR-tested, location + phone where relevant |
| R03 | Header Hierarchy | No H1 or multiple H1s, skipped levels | H1 present but generic, some hierarchy issues | Proper hierarchy, keywords in H1/H2 | Full H1-H4 hierarchy, keywords distributed | Semantic hierarchy optimized for featured snippets |
| R04 | Content Depth | Thin pages (<200 words) dominating | Mix of thin and adequate content | Most pages adequate (500+ words) | Key pages comprehensive (1500+ words) | Expert-level depth, original insights, multimedia-rich |
| R05 | Internal Linking | No contextual internal links | Random internal links, generic anchors | Some strategic linking, decent anchors | Hub-spoke model, keyword-varied anchors | Programmatic + editorial linking, equity flow optimized |
| R06 | Image SEO | No alt text, unoptimized formats | Some alt text, oversized images | Alt text on most, WebP used | All images optimized, descriptive alt + filenames | Geo-tagged, responsive srcset, image sitemap, lazy-loaded |
| R07 | E-E-A-T Signals | No author/about/trust signals | Basic about page only | Author bylines + credentials shown | Full E-E-A-T: bios, certs, awards, case studies | Industry-recognized expertise, external validation |
| R08 | Content Freshness | No updates in 12+ months | Sporadic updates | Quarterly content updates | Monthly fresh content, key pages updated | Weekly publishing cadence, freshness signals strong |
| R09 | Keyword Targeting | No keyword strategy visible | Random keyword usage | Primary keywords targeted per page | Full keyword map: primary + secondary + LSI | Intent-matched keywords, NLP entities, zero cannibalization |
| R10 | SERP Feature Eligibility | Not eligible for any features | Eligible but not winning any | Winning 1-2 feature types | Winning featured snippets + PAA | Dominating multiple SERP features across queries |

## U — User Experience & Performance (10 items)

| ID | Item | 0 | 1 | 2 | 3 | 4 |
|----|------|---|---|---|---|---|
| U01 | LCP (Largest Contentful Paint) | >6s | 4-6s | 2.5-4s | 1.8-2.5s | <1.8s |
| U02 | INP (Interaction to Next Paint) | >500ms | 300-500ms | 200-300ms | 100-200ms | <100ms |
| U03 | CLS (Cumulative Layout Shift) | >0.25 | 0.15-0.25 | 0.1-0.15 | 0.05-0.1 | <0.05 |
| U04 | TTFB (Time to First Byte) | >2s | 1.2-2s | 0.8-1.2s | 0.5-0.8s | <0.5s |
| U05 | Page Weight | >5MB | 3-5MB | 1.5-3MB | 0.5-1.5MB | <0.5MB |
| U06 | Navigation UX | Confusing, broken links | Functional but unintuitive | Clear navigation, 3+ click depth | Intuitive, all key pages within 2 clicks | User-tested, conversion-optimized navigation flow |
| U07 | Mobile Usability | Unusable on mobile | Functional but painful | Good mobile experience, minor issues | Excellent mobile-first experience | Best-in-class mobile UX, app-like performance |
| U08 | Accessibility (WCAG) | Major violations, no compliance | Some ARIA labels, poor contrast | Level A partial compliance | Level AA mostly compliant | Level AA fully compliant, Level AAA in key areas |
| U09 | Conversion Path | No clear CTA or conversion path | CTA exists but buried | Clear CTA above fold, basic form | Multiple conversion paths, click-to-call, chat | Optimized funnel, A/B tested, micro-conversions tracked |
| U10 | Engagement Signals | High bounce, low time-on-page | Below industry average | At industry average | Above average engagement | Top-quartile engagement, strong scroll depth + returns |

## S — Search Authority (10 items)

| ID | Item | 0 | 1 | 2 | 3 | 4 |
|----|------|---|---|---|---|---|
| S01 | Referring Domains | 0-5 | 6-25 | 26-100 | 101-500 | 500+ (or 2x top competitor) |
| S02 | Link Quality | All spam/PBN links | Mostly low-quality directories | Mix of quality, some editorial | Majority high-quality editorial links | Premium editorial + .gov/.edu + industry authority |
| S03 | Anchor Text Distribution | 100% exact match or 100% generic | Skewed toward exact match | Mostly branded + generic, some exact | Natural distribution: branded 40%, generic 30%, exact 15%, other 15% | Strategically diversified, mirrors top-ranking sites |
| S04 | Local Citations | 0-5 citations | 6-20 basic directories | 20-50 citations, some inconsistency | 50+ citations, consistent NAP | 80+ citations, all consistent, industry-specific included |
| S05 | Topical Authority | No topical focus | 1-2 topics with thin coverage | Several topics with moderate depth | Core topics comprehensively covered | Recognized topical authority, complete cluster coverage |
| S06 | Brand Mentions | Zero unlinked mentions | Occasional mentions | Regular mentions in niche publications | Frequent mentions across authoritative sources | Industry-leading brand presence, news coverage |
| S07 | Digital PR | No PR activity | Occasional press releases | Regular PR with some coverage | Strategic PR earning quality links | Award-winning campaigns, viral content, thought leadership |
| S08 | Competitor Link Gap | Competitors have 10x more links | Competitors 5-10x ahead | Competitors 2-5x ahead | Parity with competitors | Leading competitors in link profile quality |
| S09 | Toxic Link Ratio | >20% toxic links | 10-20% toxic | 5-10% toxic | 1-5% toxic | <1% toxic, active disavow + monitoring |
| S10 | Link Velocity | Declining or zero new links | 1-2 new links/month | 3-10 new links/month | 10-25 new links/month | 25+ quality links/month, accelerating |

## T2 — Trust & AI Readiness (10 items)

| ID | Item | 0 | 1 | 2 | 3 | 4 |
|----|------|---|---|---|---|---|
| T201 | AI Overview Presence | Not appearing for any target queries | Competitor cited, client absent | Appearing for 1-2 queries | Cited in AI Overviews for several queries | Consistently cited as primary source across target queries |
| T202 | LLM Visibility | Not mentioned in any AI platform | Mentioned in 1 platform with errors | Mentioned in 2+ platforms, mostly accurate | Accurately represented across major AI platforms | Preferred source across ChatGPT, Perplexity, Gemini, Copilot |
| T203 | Content Citeability | No quotable or extractable content | Some factual statements, poor structure | Decent structure, some cite-worthy content | Clear definitions, statistics, structured Q&A | Original research, unique data, primary-source content |
| T204 | Entity Recognition | Business not recognized as entity | Partial entity presence, inconsistent | Entity recognized, basic attributes | Full entity with relationships mapped | Knowledge Panel, Wikidata, sameAs fully connected |
| T205 | Schema Completeness | No structured data | Basic schema only | Multiple schema types, some errors | Comprehensive schema, zero errors | Advanced schema (speakable, Q&A, dataset) + validation |
| T206 | Brand SERP Control | Negative or irrelevant results dominate | Mixed results, no knowledge panel | Mostly positive, some gaps | Strong brand SERP with sitelinks + reviews | Fully controlled brand SERP, Knowledge Panel claimed |
| T207 | Review Trust Score | No reviews or below 3.0 | 3.0-3.9 average, few reviews | 4.0+ average, moderate volume | 4.5+ average, high volume, multi-platform | 4.7+ average, 200+ reviews, strong velocity, review schema |
| T208 | Content Authenticity | AI-generated thin content, no expertise | Minimal original content | Mix of original and generic | Mostly original, expert-authored | All original, author credentials, first-hand experience shown |
| T209 | Cross-Platform Consistency | Conflicting info across web | Major inconsistencies (NAP, hours) | Mostly consistent, minor discrepancies | Consistent across all major platforms | Perfect consistency + active monitoring system |
| T210 | Competitive Trust Position | Lowest trust signals in market | Below average vs. competitors | Parity with competitors | Above average trust signals | Market-leading trust, industry benchmark |

---

## Veto Checks

These critical items override the overall score. If ANY veto triggers, the maximum possible score is capped:

| Veto ID | Condition | Score Cap | Rationale |
|---------|-----------|-----------|-----------|
| V01 | Site not indexed by Google | Cap at 10 | Nothing else matters if invisible |
| V02 | Active manual penalty in GSC | Cap at 15 | Must resolve before any optimization |
| V03 | No HTTPS / expired SSL | Cap at 25 | Google treats as insecure, rankings suppressed |
| V04 | LCP > 6 seconds on mobile | Cap at 30 | Core Web Vitals failure blocks ranking improvements |
| V05 | Site serves cloaked / hidden content | Cap at 10 | Risk of deindexation |
| V06 | >50% toxic backlinks | Cap at 20 | Algorithmic penalty likely active or imminent |
| V07 | Zero structured data | Cap at 40 | Missing critical trust and rich result signals |

---

## Score Calculation

### Raw Score
```
Raw Score = Sum of all 50 item scores
Maximum Raw Score = 50 × 4 = 200
```

### Normalized Score
```
SERP-TRUST Score = (Raw Score / 200) × 100
```

### Apply Veto Caps
```
If any veto condition is TRUE:
  Final Score = min(Normalized Score, Veto Cap)
```

### Grade Interpretation

| Score | Grade | Interpretation | Competitive Position |
|-------|-------|----------------|---------------------|
| 90-100 | A+ | Elite — industry-leading search trust | Top 1% — actively setting benchmarks |
| 80-89 | A | Excellent — strong foundation, minor polish needed | Top 5% — competitive advantage |
| 70-79 | B+ | Very Good — solid with clear improvement areas | Top 15% — keeping up with leaders |
| 60-69 | B | Good — functional with notable gaps | Top 30% — average competitor |
| 50-59 | C+ | Fair — multiple areas need attention | Below average — falling behind |
| 40-49 | C | Below Average — significant weaknesses | Bottom 30% — losing ground |
| 30-39 | D | Poor — fundamental issues across multiple dimensions | Bottom 15% — urgent intervention needed |
| 0-29 | F | Critical — site at risk, immediate action required | Bottom 5% — rebuild recommended |

---

## Dimension Weighting (Optional Advanced Scoring)

For weighted scoring that reflects 2026 ranking factor importance:

| Dimension | Weight | Rationale |
|-----------|--------|-----------|
| T — Technical Foundation | 20% | Table stakes — must be right, but alone insufficient |
| R — Ranking Signals | 25% | Core on-page factors remain highest-impact |
| U — User Experience | 20% | CWV and engagement increasingly influential |
| S — Search Authority | 20% | Off-page trust still critical for competitive queries |
| T2 — Trust & AI Readiness | 15% | Growing rapidly — will be 25%+ by 2027 |

### Weighted Score Formula
```
Weighted Score = (T_avg × 0.20) + (R_avg × 0.25) + (U_avg × 0.20) + (S_avg × 0.20) + (T2_avg × 0.15)
Where X_avg = (dimension raw score / dimension max) × 100
```

---

## Usage Notes

- Score each item independently — do not let strong areas compensate for weak ones
- Use web research to verify current status of each item where possible
- Compare scores against top 3 local competitors for context
- Re-score quarterly to track improvement
- Pair with LOCAL-IMPACT framework for complete local business assessment
- SERP-TRUST focuses on **search engine trust signals** while LOCAL-IMPACT focuses on **local presence and visibility**
