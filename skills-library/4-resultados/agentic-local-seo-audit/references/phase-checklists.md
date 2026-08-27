# Phase Checklists — Full Detail Reference

> Complete checklist for all 21 audit phases. Loaded by individual skill files.
> For orchestration rules see CLAUDE.md. For scoring frameworks see local-impact-benchmark.md and serp-trust-benchmark.md.

---

## PHASE 1: COMPETITOR DEEP ANALYSIS (COMP-001)
### Priority: CRITICAL

**1.1 Identification & Profiling**
- Confirm competitors rank for target keywords in target location
- Identify primary service offerings vs. client
- Estimate domain age, authority metrics from observable signals
- Map site structure and page count

**1.2 Technical SEO Profile**
- Site speed / CWV comparison, mobile experience
- Schema markup usage, URL structure, internal linking patterns
- HTTPS, canonical, hreflang usage

**1.3 Content Strategy**
- Total content volume, publishing frequency, content types
- Content depth (avg word count), freshness, topic clusters
- User-generated content presence

**1.4 Keyword Strategy**
- Primary keywords (title tags, H1s, URLs), long-tail coverage
- Keyword gaps, featured snippet ownership, PAA presence

**1.5 Backlink & Authority**
- Link quality from observable mentions and citations
- Most-linked pages, digital PR patterns, local citation sources

**1.6 Local SEO Profile**
- GBP completeness, review count/rating/velocity
- Local citation consistency, location page strategy, local content

**1.7 AI Visibility**
- AI Overviews presence, ChatGPT/Perplexity/Gemini mentions
- Structured content for AI extraction, entity presence

**1.8 Social Media Presence**
- Platforms active, posting frequency, engagement, community

**1.9 SERP Feature Ownership**
- Featured snippets, local pack, image pack, video carousel, Knowledge Panel, PAA, sitelinks

**Output per competitor:** Scorecard (1-10 across all dimensions), Gap Table, Opportunities, Threats, Quick Wins

---

## PHASE 2: COMPLETE TECHNICAL SEO AUDIT (TECH-001)
### Priority: CRITICAL

**2.1 Crawlability & Indexation**
- Robots.txt, XML Sitemap (submitted to GSC?), HTML Sitemap
- Index coverage, crawl budget, orphan pages, crawl depth
- Noindex/nofollow audit, JavaScript rendering, soft 404s, crawl traps

**2.2 Site Architecture & URL Structure**
- Clean descriptive URLs (<75 chars), logical hierarchy (max 3 levels)
- Breadcrumbs (schema-marked), pagination, faceted navigation

**2.3 HTTPS & Security**
- Valid SSL, no mixed content, HTTP→HTTPS 301 redirect
- HSTS header, security headers (CSP, X-Frame-Options, X-Content-Type)

**2.4 Redirect Management**
- No chains >1 hop, no loops, 301 vs 302 usage, migrated URLs redirected

**2.5 Canonical Tags**
- Self-referencing on all pages, no conflicts, pagination canonicals, www/non-www consistency

**2.6 Hreflang** (if multi-language)
- Tags present, return tags, x-default, language/region code accuracy

**2.7 Structured Data / Schema**
- LocalBusiness, Organization, BreadcrumbList, Service, FAQ, Review/AggregateRating
- Article, HowTo, Event, Product, VideoObject, sameAs, schema validation (Rich Results Test)

**2.8 Core Web Vitals & Performance**
- LCP <2.5s, INP <200ms, CLS <0.1, TTFB <800ms, FCP <1.8s
- Render-blocking resources, image optimization, font loading, third-party scripts
- CDN, caching, code minification, critical CSS, preloading

**2.9 Mobile SEO**
- Mobile-first indexing, responsive design, tap targets (48x48px min), font size (16px min)
- No horizontal scroll, no intrusive interstitials, mobile nav

**2.10 Log File Analysis** — recommend if not done
**2.11 International SEO** — country targeting, hreflang, ccTLD/subdirectory strategy

---

## PHASE 3: ON-PAGE SEO AUDIT (ONPAGE-001)
### Priority: HIGH

**3.1 Title Tags** — unique, primary keyword near start, 50-60 chars, location included, CTR-optimized
**3.2 Meta Descriptions** — unique, 150-160 chars, keyword + CTA + location, no duplicates
**3.3 Header Tags** — one H1 per page, logical H1→H2→H3 hierarchy, keywords distributed naturally
**3.4 URL Optimization** — short, hyphens, lowercase, keyword-rich, no stop words
**3.5 Content Optimization** — keyword in first 100 words, LSI/entities, intent match, comprehensive, formatted
**3.6 Internal Linking** — contextual links, descriptive anchors, hub/spoke, orphan pages linked, max 3 clicks deep
**3.7 Image SEO** — descriptive alt, filename, WebP, srcset, lazy-load, dimensions specified, geo-tagged
**3.8 Video SEO** — transcripts, VideoObject schema, video sitemap, YouTube + embed
**3.9 CTA Optimization** — clear CTA every page, tel: links, CTAs above fold, service-specific
**3.10 E-E-A-T Signals** — About page, author bylines, credentials, trust badges, testimonials, privacy policy

---

## PHASE 4: CONTENT AUDIT (CONTENT-001)
### Priority: HIGH

**4.1 Inventory & Quality** — full catalog, thin pages (<300 words), duplicates, outdated, cannibalization, freshness
**4.2 Content Strategy** — pillar+cluster model, content calendar, variety, funnel coverage, differentiation
**4.3 Service Pages** — dedicated page per service, 1500+ words, process/benefits/FAQ/testimonials, clear CTA
**4.4 Location Pages** — unique content per location, local context, embedded map, area-specific testimonials/FAQs
**4.5 Blog/Resource Content** — keyword-targeted, intent match, links to service pages, comprehensive, multimedia
**4.6 FAQ Content** — keyword-targeted, real customer questions, FAQ schema, distributed across pages, PAA coverage
**4.7 Content for AI Optimization** — clear definitions, Q&A format, factual statements, statistics, structured sections

---

## PHASE 5: CONTENT GAP ANALYSIS (CGAP-001)
### Priority: HIGH

**5.1 Topic Gaps** — TOFU/MOFU/BOFU missing, seasonal, trending, local topics not covered
**5.2 Content Type Gaps** — missing guides/calculators/tools, multimedia, social proof, comparisons, resource pages
**5.3 Golden Opportunities** — blue ocean topics, rising trends, adjacent high-traffic topics, snippet/PAA wins
**5.4 Improvement Opportunities** — thin pages to expand, positions 5-20 to boost, declining traffic pages, high impressions/low CTR

Output: `| Gap Type | Topic | Volume (Est.) | Competitor Coverage | Priority | Content Type | Impact |`

---

## PHASE 6: KEYWORD GAP ANALYSIS (KGAP-001)
### Priority: HIGH

**6.1 Keyword Universe** — current rankings mapped, competitor rankings mapped, shared vs gaps vs unique
**6.2 Classification** — head/mid-tail/long-tail, question, commercial, informational, local, branded, near-me
**6.3 Low-Hanging Fruit** — positions 4-10, positions 11-20, high impressions/low CTR, existing content underperforming
**6.4 Priority Targets** — keyword-to-page mapping, new pages needed, cannibalization, priority score (volume × intent × difficulty)
**6.5 SERP Analysis** — features present, who ranks #1-3, content type ranking, realistic competition assessment

Output: `| Keyword | Volume | Intent | Tail | Client | Comp1 | Comp2 | Comp3 | Opportunity | Action | Target Page |`

---

## PHASE 7: TOPICAL GAP ANALYSIS (TGAP-001)
### Priority: HIGH

**7.1 Topical Map** — parent topics, subtopics, supporting topics; cross-reference competitors; zero-coverage topics
**7.2 Cluster Completeness** — pillar page quality, cluster pages count, pillar↔cluster internal linking, orphaned clusters
**7.3 Semantic Coverage** — missing entities, related concepts, questions, processes, synonyms
**7.4 Topical Map Creation** — prioritized by relevance × demand × competition, content roadmap, publishing timeline

---

## PHASE 8: TOPICAL AUTHORITY AUDIT (TAUTH-001)
### Priority: HIGH

**8.1 Current Authority** — depth/breadth/freshness/quality scores; featured snippet/PAA/KP recognition
**8.2 Authority Comparison** — most comprehensive coverage, deepest content, most complete clusters, update frequency
**8.3 Authority Roadmap** — topic priorities, content volume needed, quality standard, supporting evidence, timeline
**8.4 Knowledge Graph** — business entity recognized? Knowledge Panel? Services as entities? Key people recognized?

---

## PHASE 9: ENTITY AUDIT (ENTITY-001)
### Priority: HIGH

**9.1 Business Entity** — Knowledge Graph presence, Knowledge Panel, Wikidata, Wikipedia, sameAs connections
**9.2 Content Entities** — entities in client content vs competitors; missing critical entities
**9.3 Entity Types** — People, Place, Organization, Service, Product, Concept, Event
**9.4 Entity Optimization** — schema for all entities, consistent naming, relationships mapped, NLP salience
**9.5 Entity Connections** — relationship mapping, high-authority associations, sameAs strategy, co-citation

---

## PHASE 10: CORE WEB VITALS & SPEED (SPEED-001)
### Priority: CRITICAL

**10.1 Baseline** — PSI mobile/desktop; LCP, INP, CLS, TTFB, FCP; page weight, request count
**10.2 Bottlenecks** — Images, JavaScript, CSS, Fonts, Third-party scripts, Server, DOM size, Layout shifts
**10.3 Page Priority** — homepage, top-10 traffic, service pages, location pages, blog template
**10.4 Fixes** — cause → exact steps → expected improvement → effort → priority

---

## PHASE 11: LOCAL SEO AUDIT (LOCAL-001)
### Priority: CRITICAL

**11.1 GBP** — claimed/verified, categories (up to 9), name/address/phone/hours/description (750 chars), services, attributes, photos (50+), posts (weekly), Q&A (20+), messaging, booking
**11.2 Reviews** — count/rating/velocity vs competitors, response rate (100% target), response quality, generation system, multi-platform
**11.3 NAP** — website/GBP/citations/social/schema all match; no legacy addresses/numbers
**11.4 Citations** — core (Google/Bing/Apple/Yelp/Facebook), industry-specific, local; accuracy, completeness, no duplicates
**11.5 Location Pages** — unique content, local context, schema, map embed, local testimonials/images/FAQs/directions
**11.6 Local Links** — newspaper/blogger/sponsor/charity/Chamber, local partnerships
**11.7 Local Content** — community content, neighborhood guides, local case studies, seasonal content
**11.8 Local SERP** — local pack/finder/organic rankings, Apple/Bing Maps presence

---

## PHASE 12: BACKLINK & LINK PROFILE (LINK-001)
### Priority: HIGH

**12.1 Current Profile** — referring domains, quality distribution, anchor text distribution, velocity
**12.2 Competitor Comparison** — total/quality/type comparison, common links client lacks
**12.3 Opportunities** — directories, resource pages, broken links, unlinked mentions, digital PR, guest posts, local links
**12.4 Toxic Links** — PBN, foreign spam, low-quality directories, comment spam; disavow if needed
**12.5 Strategy** — prioritized targets, content-driven opportunities, outreach, digital PR angles

---

## PHASE 13: SOCIAL MEDIA AUDIT (SOCIAL-001)
### Priority: MEDIUM-HIGH

**13.1 Profiles** — all platforms inventoried, missing platforms identified, completeness, NAP consistency, sameAs schema
**13.2 Per Platform** — followers/growth, posting frequency, engagement rate, content types, community management
**13.3 Content Strategy** — content mix, local content, team content, UGC, video, content calendar
**13.4 SEO Signals** — sharing buttons, OG tags, Twitter Cards, social traffic to site
**13.5 Competitor Comparison** — followers, engagement, content strategy gaps
**13.6 YouTube** — channel optimization, video SEO, playlists, website cross-linking

---

## PHASE 14: AI VISIBILITY & AI SEO (AISEO-001)
### Priority: CRITICAL

**14.1 AI Overviews** — target keywords checked, client cited?, competitors present, content format in AIOs
**14.2 Google AI Mode** — key queries tested, business mentioned?, accuracy, competitor presence
**14.3 LLM Visibility** — ChatGPT, Perplexity, Gemini, Claude, Copilot, Apple Intelligence: brand + service + location queries
**14.4 AEO** — structured answers, FAQ format, featured snippet optimization, PAA coverage, voice-compatible Q&A
**14.5 GEO** — citeability, E-E-A-T for AI trust, unique data, structured content, entity optimization, schema, topical authority
**14.6 AI Content Strategy** — AI-extractable formats, statistics, original research, entity building, cross-platform consistency
**14.7 Table:** `| Query | ChatGPT | Perplexity | Gemini | AI Overview | Client? | Comp1 | Comp2 | Comp3 |`

---

## PHASE 15: REPUTATION & REVIEW MANAGEMENT (REP-001)
### Priority: HIGH

**15.1 Reputation** — brand SERP (what shows for brand name search), negative mentions/press, BBB rating, forum/Reddit mentions
**15.2 Review Ecosystem** — Google/Yelp/Facebook/industry/Trustpilot; on-site reviews with schema
**15.3 Strategy** — generation process, monitoring system, response templates, negative mitigation, review marketing

---

## PHASE 16: BRAND SERP & KNOWLEDGE PANEL (BRAND-001)
### Priority: MEDIUM-HIGH

**16.1 Brand SERP** — Knowledge Panel, sitelinks, social profiles, review ratings, news, images, PAA, negative results
**16.2 Knowledge Panel** — present, accurate, logo/photos correct, sameAs connections, Wikidata, claimed/verified

---

## PHASE 17: UX & CONVERSION RATE OPTIMIZATION (CRO-001)
### Priority: MEDIUM-HIGH

**17.1 UX** — navigation (key pages <2 clicks), above-fold value prop, contact accessibility, trust signals, WCAG 2.1 AA
**17.2 Conversion Paths** — primary/secondary conversion points, form analysis, click-to-call, live chat, exit intent
**17.3 Analytics** — GA4, GSC, GTM, conversion tracking, phone call tracking, form events, attribution model

---

## PHASE 18: VOICE SEARCH OPTIMIZATION (VOICE-001)
### Priority: MEDIUM

- Conversational Q&A content, long-tail question keywords, featured snippet optimization, local "near me" optimization
- Speakable schema, FAQ in conversational tone, complete GBP, fast page speed

---

## PHASE 19: ACCESSIBILITY (ACCESS-001)
### Priority: MEDIUM

- Heading hierarchy, alt text on meaningful images, ARIA labels, color contrast (4.5:1 min)
- Keyboard navigation, form labels, descriptive link text, video captions, skip navigation, lang attribute, focus indicators

---

## PHASE 20: PENALTY & MANUAL ACTION CHECK (PENALTY-001)
### Priority: CHECK FIRST

- GSC manual actions check; algorithmic penalty indicators (traffic drops at update dates, deindexed pages)
- Technical red flags: cloaking, hidden text, keyword stuffing, doorway pages, UGC spam, negative SEO
- Unnatural link patterns

---

## PHASE 21: MULTI-LOCATION SEO (MULTI-001)
### Priority: HIGH (if applicable)

- Separate GBP per location (all verified), unique content per location page, URL structure (/locations/city-name/)
- Store locator, per-location schema/reviews/citations, geo-siloing strategy, cannibalization prevention

---

## Output Format (Per Phase)

```
============================================
AUDIT PHASE: [Phase Name] | AUDIT ID: [ID]
DATE: [Date] | BUSINESS: [Name] | URL: [URL]
============================================
EXECUTIVE SUMMARY: [2-3 sentences]
OVERALL SCORE: X/100 | STATUS: ✅/⚠️/❌

CRITICAL ISSUES (Fix Immediately)
  → [Issue]: [Fix steps] | Impact: Critical | Effort: Xhrs | Priority: Immediate

HIGH PRIORITY (Fix This Week)
MEDIUM PRIORITY (Fix This Month)
LOW PRIORITY (Fix Next Quarter)

OPPORTUNITIES: [Quick wins + growth]
COMPETITOR COMPARISON: [How client compares]
SPECIFIC RECOMMENDATIONS: [Actionable steps with effort/impact]
ESTIMATED IMPACT: [Expected improvement]
```

**Status Key:** ✅ Pass | ⚠️ Warning | ❌ Fail | ℹ️ N/A
**Impact:** Critical | High | Medium | Low
**Priority:** Immediate | This Week | This Month | Next Quarter
**Effort:** Quick Fix (<1hr) | Medium (1-4hrs) | Complex (4+hrs)
