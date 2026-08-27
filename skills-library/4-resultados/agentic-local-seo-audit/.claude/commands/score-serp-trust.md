---
description: Run the SERP-TRUST scoring framework on the target website
argument-hint: "[website URL]"
---

# Score SERP-TRUST

Run the proprietary 50-item SERP-TRUST scoring framework to assess the website's search engine trust and authority signals.

## What This Does

Scores the website across 5 dimensions:
- **T** — Technical Foundation (crawlability, indexation, schema, security)
- **R** — Ranking Signals (on-page optimization, content, E-E-A-T)
- **U** — User Experience & Performance (CWV, mobile, accessibility, CRO)
- **S** — Search Authority (backlinks, citations, topical authority, PR)
- **T2** — Trust & AI Readiness (AI visibility, entity recognition, brand SERP)

## Execution

1. Load the `cross-cutting/serp-trust-auditor` skill
2. Load the rubric from `references/serp-trust-benchmark.md`
3. Research and score all 50 items
4. Run veto checks (7 critical conditions)
5. Score competitors for comparison
6. If LOCAL-IMPACT was also scored, compute SEO Health Index
7. Output scorecard with priorities and quick wins
8. Save results to `audit/serp-trust-scores.md`

## Output

Produces a SERP-TRUST Scorecard with:
- Overall score (0-100) and grade (A+ through F)
- Per-dimension breakdown with visual bars
- Optional weighted score (accounting for 2026 factor importance)
- Veto check results
- Competitor comparison table
- Top 5 improvement priorities
- Quick wins list
- SEO Health Index (if LOCAL-IMPACT also scored)
