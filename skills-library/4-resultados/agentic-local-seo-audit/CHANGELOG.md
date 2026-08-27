# Changelog

All notable changes to the Local SEO Audit plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.3] - 2026-03-13

### Added
- `skills.sh.json` — skills.sh (Vercel) manifest mapping all 27 skills to their domain paths
- `README.md` — skills.sh install commands (`npx skills add mshahiddigital/local-seo-audit`)
- `README.md` — skills.sh badge in header
- Plugin now listed on both Anthropic Claude Code Marketplace and skills.sh (Vercel)

---

## [2.0.2] - 2026-03-13

### Fixed
- Author identity updated to Muhammad Shahid `info@mshahid.com` in `plugin.json` and `marketplace.json`

---

## [2.0.1] - 2026-03-13

### Fixed
- All 6 agent files: renamed `allowed-tools` → `tools` (was silently ignored by the runtime)
- All 6 agent files: added `skills` field — each agent now loads its assigned skills on start
- All 6 agent files: added `color` field for visual identification in Claude Code agent list
- Agent descriptions updated to include phase numbers for quick scanning

---

## [2.0.0] - 2026-03-13

### Changed
- Reorganized skills from flat `skills/` directory into domain-based subdirectories: `audit/`, `local/`, `research/`, `strategy/`, `ai-visibility/`, `cross-cutting/`, `output/`
- Bumped version to 2.0.0 to reflect structural refactor and new features

### Added
- 3 new skills: `local-impact-auditor`, `serp-trust-auditor`, `multi-location-seo` (27 total)
- 4 new commands: `generate-pdf`, `export-html`, `score-local-impact`, `score-serp-trust` (40 total)
- LOCAL-IMPACT proprietary scoring framework: 60 items, 8 dimensions, 0–3 scale
- SERP-TRUST proprietary scoring framework: 50 items, 5 dimensions, 0–4 scale
- SEO Health Index: weighted combination (LOCAL-IMPACT × 0.55 + SERP-TRUST × 0.45)
- `references/` directory with scoring benchmarks, phase checklists, and scoring methodology
- `AGENTS.md` documenting the 6-agent parallel execution architecture
- `CONNECTORS.md` documenting MCP connector patterns and configuration
- `agents/` field restored to `plugin.json` so all 6 sub-agents register correctly
- `audit/.gitkeep` placeholder so the inter-skill handoff output directory exists on fresh clones

### Fixed
- `plugin.json` non-standard `capabilities`, `metadata`, and `schemaVersion` fields removed
- `hooks` and `mcpServers` fields in `plugin.json` now use path-string format per official spec
- `.claude/settings.json` merged with root `settings.json` (now single authoritative file with Bash perms + subagent model config)
- `.vscode/settings.json` removed (`allowDangerouslySkipPermissions: true` is a security risk in a distributed plugin)
- `.gitignore` updated with `.vscode/`, `*.save`, `plan.md`, `settings.json`, `audit/*.md`

---

## [1.0.0] - 2026-03-12

### Added
- Complete 21-phase local business SEO audit framework
- 24 skills covering all audit domains (technical SEO, on-page, content, local SEO, AI visibility, etc.)
- 36 slash commands for triggering individual phases and utility functions
- 6 specialized sub-agents for parallel audit execution
- Competitor deep analysis across 9 dimensions
- AI visibility audit (AI Overviews, ChatGPT, Perplexity, Gemini, Claude, Copilot)
- Content gap, keyword gap, and topical gap analysis
- Entity audit and Knowledge Graph optimization
- GBP optimization toolkit with post ideas, Q&A seeding, and photo shot lists
- Schema markup generator (JSON-LD) for local businesses
- SEO content brief generator
- Citation building list generator
- Master audit report compiler with 30/90/180/365-day action plans
- Quality gate hooks ensuring no generic output
- MCP server connector configs for GSC, GA4, GBP, PageSpeed Insights, SimilarWeb
- Professional PDF report generation with SVG gauge charts, color-coded cards, bar charts, and timeline roadmaps
- HTML export option for report customization before PDF conversion
- Zero-dependency PDF conversion via headless Chrome
