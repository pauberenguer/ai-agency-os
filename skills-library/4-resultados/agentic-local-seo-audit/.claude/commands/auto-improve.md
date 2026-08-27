---
description: Run autonomous skill improvement loop on SKILL.md files
argument-hint: [skill-path | --baseline | --report | --findings project-dir]
---

Read auto-improve.md and start the autonomous improvement loop.

Modes based on $ARGUMENTS:
- No arguments: improve all 27 skills indefinitely, starting with lowest score
- [skill-path]: improve single skill until plateau (e.g., audit/technical-seo)
- --baseline: score all skills, no changes
- --report: show IMPROVEMENT_LOG.md summary
- --findings [project-dir]: improve phase finding files in specified project directory

Follow auto-improve.md instructions exactly. Never modify quality_checker.py, auto-improve.md, or CLAUDE.md.
