# SEO-AutoImprove — Agent Loop Instructions
# Inspired by karpathy/autoresearch (program.md)
# Version: 1.0 | Date: 2026-03-16

> This file is the `program.md` equivalent for the SEO-AutoImprove loop.
> When a user says "Read auto-improve.md and start improving" — follow these instructions exactly.
> NEVER modify this file. NEVER modify scripts/quality_checker.py.
> The ONLY files you modify are SKILL.md files (the `train.py` equivalent).

---

## WHAT YOU ARE DOING

You are running an autonomous skill improvement loop modelled on karpathy/autoresearch.

- **What you modify:** SKILL.md files (27 total across all skill directories)
- **What you measure:** quality score from `python3 scripts/quality_checker.py` (0–100, higher = better)
- **Keep rule:** If new score > old score → KEEP the git commit
- **Revert rule:** If new score ≤ old score → `git reset --hard HEAD~1`
- **Never stop:** Loop indefinitely until the user manually interrupts you

---

## SETUP PHASE (run once at session start)

```bash
# 1. Create improvement branch
git checkout -b autoimprove/$(date +%Y-%m-%d)

# 2. Check IMPROVEMENT_LOG.md for prior session state
# Read IMPROVEMENT_LOG.md → identify which skills were last improved, current scores

# 3. Score all 27 skills to get session baseline
python3 scripts/quality_checker.py --all

# 4. Identify improvement order:
#    - Start with lowest-scoring skills first
#    - If all are above 85, rotate alphabetically
#    - Never improve same skill twice in one round without trying others
```

---

## IMPROVEMENT LOOP (repeat forever)

### Step 1 — Select Target Skill
Pick the skill with the lowest quality score that hasn't been improved this round.
If all skills have been improved once this round, start a new round from the lowest scorer again.

### Step 2 — Measure Baseline
```bash
python3 scripts/quality_checker.py --skill [path/to/SKILL.md] --json
```
Record: `baseline_score`, `grade`, list of `improvement_notes` from all 5 dimensions.

### Step 3 — Research
Run web searches to find:
- Latest 2025/2026 best practices for this skill's specific domain
- Current tool names, thresholds, benchmarks in this area
- Any algorithm updates, new ranking factors, or industry changes since last edit
- Competitor frameworks or methodologies for this audit type

Focus research on the **exact improvement_notes** from quality_checker output.

### Step 4 — Improve the SKILL.md
Make targeted improvements based on:
- `[Completeness]` notes → add missing sections
- `[Specificity]` notes → add concrete tool names, thresholds, numbers
- `[Recency]` notes → add 2025/2026 references, AI Overviews, GEO, INP, etc.
- `[Actionability]` notes → add numbered steps, effort estimates, priority matrix
- `[Output Protocol]` notes → add {AUDIT_DIR} paths, output file declarations

**Improvement rules:**
- Do NOT add filler or padding — every sentence must have informational value
- Do NOT change the frontmatter fields (name, description, user-invocable)
- Do NOT remove existing correct content — only add or improve
- Keep the skill focused on its specific audit phase — do not scope-creep
- Minimum change: fix at least 2 of the noted improvement gaps

### Step 5 — Commit
```bash
git add [path/to/SKILL.md]
git commit -m "autoimprove: [skill-name] — [concise description of what changed]"
```

Commit message format: `autoimprove: audit/technical-seo — added INP threshold, AI Overviews signals, PageSpeed API integration`

### Step 6 — Measure Again
```bash
python3 scripts/quality_checker.py --skill [path/to/SKILL.md] --json
```
Record: `new_score`

### Step 7 — Keep or Revert Decision

**IF new_score > baseline_score:**
```bash
# KEEP — do nothing, commit stays
echo "KEPT: [skill] +[delta] points"
```
Append to IMPROVEMENT_LOG.md:
```
[date]	[skill-path]	[baseline_score]	[new_score]	+[delta]	KEPT	[what changed]
```

**IF new_score ≤ baseline_score:**
```bash
git stash --include-untracked  # protect any uncommitted user work
git reset --hard HEAD~1
git stash pop 2>/dev/null || true  # restore user's work if any
echo "REVERTED: [skill] — no improvement"
```
Append to IMPROVEMENT_LOG.md:
```
[date]	[skill-path]	[baseline_score]	[new_score]	[delta]	REVERTED	[reason: what went wrong]
```

### Step 8 — Continue
Go to Step 1 with the next skill.
**NEVER STOP.** Loop indefinitely until the user types "stop" or interrupts.

---

## SPECIAL MODES

### Baseline Only (`/auto-improve --baseline`)
Run `python3 scripts/quality_checker.py --all` and display results.
Do NOT make any changes. Do NOT commit anything. Just report scores.

### Single Skill Mode (`/auto-improve [skill-path]`)
Run the improvement loop but ONLY on the specified skill.
Run multiple rounds on the same skill until score plateaus (no gain for 2 consecutive attempts).
Then stop automatically.

### Report Mode (`/auto-improve --report`)
Read IMPROVEMENT_LOG.md and produce a summary:
- Total improvements kept / reverted
- Biggest gainers (by delta)
- Current highest and lowest scoring skills
- Recommended next skills to improve

### Findings Mode (`/auto-improve --findings [project-dir]`)
Instead of improving SKILL.md files, improve the phase finding .md files in `[project-dir]/audit/`.
Same loop: score finding → research → improve → measure → keep/revert.
Scoring criteria for findings:
- Specificity (is it specific to THIS business, not generic?)
- Competitor context (does every finding compare to competitors?)
- Actionability (numbered steps, effort, timeline per recommendation?)
- Priority scores (Impact × Feasibility on every issue?)
- AI visibility angle (does content/on-page finding include AI search impact?)

---

## QUALITY GATE RULES (never skip these)

Before keeping any improvement:
1. The skill must still output to the correct `{AUDIT_DIR}/[phase-file].md`
2. The skill must still read `{AUDIT_DIR}/intake-data.md` at the start
3. The frontmatter `name:` must not have changed
4. The improvement must not reduce word count by more than 10%
5. The skill must retain its phase scope — no scope creep into other phases

If any gate fails → revert even if score improved.

---

## CRASH HANDLING

If quality_checker.py errors (file not found, parse error):
- Log: `CRASH	[skill]	[error message]` in IMPROVEMENT_LOG.md
- Revert any uncommitted changes
- Skip to next skill
- Continue loop

If a skill has been reverted 3 times in a row:
- Log: `PLATEAU	[skill]	score=[score]	no improvement after 3 attempts`
- Skip this skill for the rest of the current round
- Try again in the next round

---

## RESULTS FORMAT (IMPROVEMENT_LOG.md)

Header (first line only):
```
date	skill	old_score	new_score	delta	action	description
```

Each result row (tab-separated):
```
2026-03-16	audit/technical-seo	72	81	+9	KEPT	Added INP <200ms, AI Overviews citation signals, PageSpeed API integration note
2026-03-16	ai-visibility/ai-seo	85	82	-3	REVERTED	Over-simplified GEO section — reduced specificity score
2026-03-16	local/local-seo	68	79	+11	KEPT	Added GBP Q&A 2025 guide, review velocity benchmarks, citation aggregators
```

---

## SESSION SUMMARY (display when stopped)

When user interrupts, display:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEO-AutoImprove Session Summary
Branch: autoimprove/YYYY-MM-DD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Experiments: [total]
Kept:        [kept count]  (+[avg delta] avg)
Reverted:    [reverted count]
Crashes:     [crash count]
Plateaus:    [plateau count]

Top gainers:
  1. [skill] +[delta] points (now [score]/100)
  2. [skill] +[delta] points (now [score]/100)
  3. [skill] +[delta] points (now [score]/100)

Session score improvement:
  Avg before: [baseline_avg]/100
  Avg after:  [new_avg]/100
  Net gain:   +[delta_avg] points

Git branch: autoimprove/YYYY-MM-DD
To merge: git checkout main && git merge autoimprove/YYYY-MM-DD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## WHAT TO NEVER DO

- Never modify `auto-improve.md` (this file)
- Never modify `scripts/quality_checker.py`
- Never modify `CLAUDE.md` or `.claude-plugin/plugin.json`
- Never modify Python scripts in `scripts/`
- Never push to remote (`git push`) — local only until user reviews
- Never delete SKILL.md files — only improve them
- Never change frontmatter `name:` field of any skill
- Never stop the loop — keep running until user says so
