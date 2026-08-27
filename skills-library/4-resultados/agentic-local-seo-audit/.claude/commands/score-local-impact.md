---
description: Run the LOCAL-IMPACT scoring framework on the target business
argument-hint: "[business URL]"
---

# Score LOCAL-IMPACT

Run the proprietary 60-item LOCAL-IMPACT scoring framework to assess the business's local presence and visibility.

## What This Does

Scores the business across 8 dimensions:
- **L** — Listing Quality (GBP completeness)
- **O** — Online Reviews (count, rating, velocity, responses)
- **C** — Citation Consistency (NAP accuracy across directories)
- **A** — Authority Signals (local links, associations, trust)
- **L2** — Local Content (location pages, community content)
- **I** — Integrated Visibility (multi-platform presence)
- **P** — Performance (speed, mobile, CWV)
- **T** — Tracking (analytics, conversion tracking)

## Execution

1. Load the `cross-cutting/local-impact-auditor` skill
2. Load the rubric from `references/local-impact-benchmark.md`
3. Research and score all 60 items
4. Run veto checks
5. Score competitors for comparison
6. Output scorecard with priorities and quick wins
7. Save results to `audit/local-impact-scores.md`

## Output

Produces a LOCAL-IMPACT Scorecard with:
- Overall score (0-100) and grade (A+ through F)
- Per-dimension breakdown with visual bars
- Veto check results
- Competitor comparison table
- Top 5 improvement priorities
- Quick wins list
