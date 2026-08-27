---
description: Autonomously improve SKILL.md files using quality scoring loop (inspired by karpathy/autoresearch)
argument-hint: "[skill-path] or --baseline or --report or --findings [project-dir]"
---

Autonomously improve SKILL.md files using the karpathy/autoresearch pattern:
measure quality score → research → improve → keep if better / revert if worse → loop.

## Usage

```
/auto-improve                          Run full improvement loop on all 27 skills (indefinitely)
/auto-improve [skill-path]             Improve a single skill until it plateaus
/auto-improve --baseline               Score all skills, show ranking — no changes made
/auto-improve --report                 Summarise IMPROVEMENT_LOG.md session history
/auto-improve --findings [project]     Improve audit findings in projects/[slug]/audit/
```

## Examples

```
/auto-improve
/auto-improve audit/technical-seo
/auto-improve --baseline
/auto-improve --report
/auto-improve --findings projects/perth-maxi-van
```

## Execution

Read `auto-improve.md` and follow the loop instructions exactly.

**Full mode** (no argument):
1. `git checkout -b autoimprove/[date]`
2. Run `python3 scripts/quality_checker.py --all` → get baseline scores
3. For each skill (lowest score first):
   - Score with quality_checker.py
   - Web-research improvements for that domain
   - Edit SKILL.md to fix lowest-scoring dimensions
   - Commit → re-score → keep if improved / `git reset` if not
   - Log to IMPROVEMENT_LOG.md
4. Loop forever until user interrupts

**Baseline mode** (`--baseline`):
Run `python3 scripts/quality_checker.py --all` and display score ranking.
No changes made. Good for auditing the current state before a session.

**Single skill mode** (`/auto-improve [path]`):
Focus all improvement effort on one skill.
Run multiple rounds until score plateaus (no gain for 2 consecutive attempts).

**Findings mode** (`--findings [project-dir]`):
Instead of SKILL.md files, improve completed phase findings in the project audit folder.
Same loop: score → research → improve → keep/revert.

## Files Used

| File | Role |
|------|------|
| `auto-improve.md` | Full loop instructions (read this) |
| `scripts/quality_checker.py` | Quality metric — scores SKILL.md 0–100 |
| `IMPROVEMENT_LOG.md` | Session log of all experiments |

## What It Improves (and What It Doesn't)

**Improves:** SKILL.md content — completeness, specificity, recency, actionability, output protocol
**Never modifies:** auto-improve.md · quality_checker.py · CLAUDE.md · plugin.json · Python scripts
