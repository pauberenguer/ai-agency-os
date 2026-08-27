# Local SEO Audit System

> The most comprehensive local business SEO audit plugin for Claude Code — 21 phases, 27 skills, 40 commands, proprietary scoring frameworks, and professional PDF reports.

[![Claude Code Plugin](https://img.shields.io/badge/Claude_Code-Plugin-5A67D8)](https://claude.com/claude-code)
[![skills.sh](https://img.shields.io/badge/skills.sh-27_Skills-000000)](https://skills.sh)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![LOCAL-IMPACT Framework](https://img.shields.io/badge/LOCAL--IMPACT-60_Items-1E3A5F)](references/local-impact-benchmark.md)
[![SERP-TRUST Framework](https://img.shields.io/badge/SERP--TRUST-50_Items-059669)](references/serp-trust-benchmark.md)

---

## What Makes This Different

| Feature | This Plugin | Typical SEO Tools |
|---------|------------|-------------------|
| Audit depth | 21 phases, 500+ checkpoints | 5-10 surface checks |
| Scoring | Proprietary LOCAL-IMPACT (60 items) + SERP-TRUST (50 items) | Generic scores |
| AI visibility | Checks ChatGPT, Perplexity, Gemini, AI Overviews | Not covered |
| Output | Professional PDF with SVG gauges + action roadmaps | Basic reports |
| Competitor analysis | 9-dimension deep analysis per competitor | Basic comparison |
| Cost | Free & open source | $100-500/month |

---

## Features

- **21 Audit Phases** covering every dimension of local SEO
- **27 Skills** that activate automatically based on context
- **40 Slash Commands** for targeted audit phases and utility tools
- **6 Sub-Agents** for parallel audit execution
- **Proprietary Scoring Frameworks**:
  - **LOCAL-IMPACT** — 60-item local presence assessment (0-100)
  - **SERP-TRUST** — 50-item search trust assessment (0-100)
  - **SEO Health Index** — Combined weighted score
- **Competitor Analysis** across 9 dimensions with scoring
- **AI Visibility Auditing** — AI Overviews, ChatGPT, Perplexity, Gemini, Claude, Copilot
- **Content, Keyword & Topical Gap Analysis** with prioritized roadmaps
- **Professional PDF Reports** — SVG score gauges, color-coded issue cards, competitor charts, timeline roadmaps (zero dependencies)
- **Inter-Skill Handoff** — Skills produce/consume structured data for seamless multi-phase audits
- **Quality Gates** ensuring every recommendation is specific, actionable, and prioritized
- **Tool-Agnostic Connectors** — Works standalone, enhances with MCP integrations

---

## Quick Start

### 1. Install

```bash
# Claude Code — from Marketplace
claude plugin install local-seo-audit

# Claude Code — from GitHub (self-hosted)
claude plugin install local-seo-audit@mshahiddigital-seo-tools

# Claude Code — Manual / Local
git clone https://github.com/mshahiddigital/local-seo-audit.git
claude --plugin-dir ./local-seo-audit

# Claude Cowork — .plugin file (drag-and-drop)
# Build the .plugin package first:
zip -r local-seo-audit.plugin . \
  -x '*.DS_Store' -x '__pycache__/*' -x 'projects/*' -x '.git/*' \
  -x 'plugin-audit-report/*' -x 'auto-research-plan.md'
# Then drag local-seo-audit.plugin into Claude Cowork to install

# skills.sh (Vercel) — install all 27 skills
npx skills add mshahiddigital/local-seo-audit

# skills.sh — install a single skill
npx skills add mshahiddigital/local-seo-audit --skill technical-seo

# skills.sh — list all available skills
npx skills add mshahiddigital/local-seo-audit --list
```

### 2. Run Your First Audit

```
/local-seo-audit:seo-audit https://example.com
```

### 3. Get Your Score

```
/local-seo-audit:score-local-impact
/local-seo-audit:score-serp-trust
```

### 4. Generate PDF Report

```
/local-seo-audit:generate-pdf
```

### Scope Options

```bash
claude plugin install local-seo-audit --scope user      # Available everywhere
claude plugin install local-seo-audit --scope project   # Shared via git
claude plugin install local-seo-audit --scope local     # Local only
```

---

## Audit Methodology

```
┌─────────────────────────────────────────────────────────────┐
│                    AUDIT WORKFLOW                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Wave 1: Foundation                                         │
│  ┌──────────┐  ┌──────────────────┐  ┌──────────────┐      │
│  │ Intake   │→ │ Competitor       │→ │ Penalty      │      │
│  │ Form     │  │ Analysis (×3-5)  │  │ Check        │      │
│  └──────────┘  └──────────────────┘  └──────────────┘      │
│                                                             │
│  Wave 2: Technical + Content (parallel)                     │
│  ┌────────────┐ ┌──────────┐ ┌─────────┐ ┌──────────┐     │
│  │ Technical  │ │ On-Page  │ │ Content │ │ Speed    │     │
│  │ SEO       │ │ SEO      │ │ Audit   │ │ Optimize │     │
│  └────────────┘ └──────────┘ └─────────┘ └──────────┘     │
│                                                             │
│  Wave 3: Gap Analysis                                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐                  │
│  │ Keyword  │  │ Content  │  │ Topical  │                  │
│  │ Gaps     │  │ Gaps     │  │ Gaps     │                  │
│  └──────────┘  └──────────┘  └──────────┘                  │
│                                                             │
│  Wave 4: Local + Authority (parallel)                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐     │
│  │ Local    │ │ Entity   │ │ Backlink │ │ Social   │     │
│  │ SEO      │ │ Audit    │ │ Audit    │ │ Media    │     │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘     │
│                                                             │
│  Wave 5: Advanced                                           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐     │
│  │ Topical  │ │ AI SEO   │ │ Brand    │ │ Voice    │     │
│  │ Auth     │ │ + AIO    │ │ SERP     │ │ Search   │     │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘     │
│                                                             │
│  Wave 6: Scoring + Output                                   │
│  ┌──────────────┐ ┌──────────────┐                          │
│  │ LOCAL-IMPACT │ │ SERP-TRUST   │                          │
│  │ Score (60)   │ │ Score (50)   │                          │
│  └──────┬───────┘ └──────┬───────┘                          │
│         └───────┬────────┘                                  │
│          ┌──────┴──────┐                                    │
│          │ SEO Health  │                                    │
│          │ Index       │                                    │
│          └──────┬──────┘                                    │
│          ┌──────┴──────┐                                    │
│          │ PDF Report  │                                    │
│          │ Generation  │                                    │
│          └─────────────┘                                    │
└─────────────────────────────────────────────────────────────┘
```

---

## Proprietary Scoring Frameworks

### LOCAL-IMPACT Score (0-100)

*Local Optimization, Consistency, Authority & Listing — Impact Performance Assessment & Competitive Tracking*

60 items across 8 dimensions, scored 0-3 each:

| Dimension | Items | What It Measures |
|-----------|-------|-----------------|
| L — Listing Quality | 10 | GBP completeness, categories, photos, posts |
| O — Online Reviews | 10 | Count, rating, velocity, responses |
| C — Citation Consistency | 10 | NAP accuracy across directories |
| A — Authority Signals | 10 | Local links, associations, trust |
| L2 — Local Content | 5 | Location pages, community content |
| I — Integrated Visibility | 5 | Multi-platform presence |
| P — Performance | 5 | Speed, mobile, CWV |
| T — Tracking | 5 | Analytics, conversion tracking |

### SERP-TRUST Score (0-100)

*Search Engine Results Page — Technical Reliability, User Signals & Search Trust*

50 items across 5 dimensions, scored 0-4 each:

| Dimension | Items | What It Measures |
|-----------|-------|-----------------|
| T — Technical Foundation | 10 | Crawlability, indexation, schema, security |
| R — Ranking Signals | 10 | On-page optimization, content, E-E-A-T |
| U — User Experience | 10 | CWV, mobile, accessibility, CRO |
| S — Search Authority | 10 | Backlinks, citations, topical authority |
| T2 — Trust & AI Readiness | 10 | AI visibility, entity recognition, brand SERP |

### SEO Health Index (Combined)

```
SEO Health Index = (LOCAL-IMPACT × 0.55) + (SERP-TRUST × 0.45)
```

Both frameworks include **veto checks** — critical conditions that cap the maximum score regardless of other factors.

---

## Command Quick Reference

### Core Workflow

| Command | What It Does |
|---------|-------------|
| `/seo-audit [url]` | Full 21-phase audit |
| `/quick-audit [url]` | Fast 5-phase health check |
| `/score-local-impact` | Run LOCAL-IMPACT framework |
| `/score-serp-trust` | Run SERP-TRUST framework |
| `/audit-report` | Compile master report |
| `/generate-pdf` | Create PDF report |
| `/export-html` | Export HTML report |

### Individual Phases

| Command | Phase |
|---------|-------|
| `/audit-intake` | Information gathering |
| `/audit-competitors [urls]` | Competitor analysis |
| `/audit-technical [url]` | Technical SEO |
| `/audit-onpage [url]` | On-page SEO |
| `/audit-content [url]` | Content audit |
| `/audit-content-gaps [url]` | Content gaps |
| `/audit-keywords [url]` | Keyword gaps |
| `/audit-topical-gaps [url]` | Topical gaps |
| `/audit-authority [url]` | Topical authority |
| `/audit-entities [url]` | Entity audit |
| `/audit-speed [url]` | Speed & CWV |
| `/audit-local [url]` | Local SEO & GBP |
| `/audit-backlinks [url]` | Backlink profile |
| `/audit-social [url]` | Social media |
| `/audit-ai-seo [url]` | AI visibility |
| `/audit-reputation [url]` | Reputation |
| `/audit-brand-serp [url]` | Brand SERP |
| `/audit-cro [url]` | UX & CRO |
| `/audit-voice [url]` | Voice search |
| `/audit-accessibility [url]` | Accessibility |
| `/audit-penalty [url]` | Penalty check |
| `/audit-multi-location [url]` | Multi-location |

### Utilities

| Command | What It Does |
|---------|-------------|
| `/audit-quick-wins` | Extract all quick wins |
| `/audit-action-plan [timeframe]` | Prioritized action plan |
| `/audit-compare [url]` | Side-by-side comparison |
| `/audit-status` | Show audit progress |
| `/topical-map [niche]` | Build topical authority map |
| `/keyword-map` | Keyword-to-page mapping |
| `/schema-generator [url] [type]` | Generate JSON-LD schema |
| `/content-brief [keyword]` | SEO content brief |
| `/gbp-optimize [business]` | GBP optimization toolkit |
| `/citation-list [cat] [loc]` | Citation building list |
| `/ai-visibility-check [biz]` | AI platform visibility |

---

## Architecture

```
local-seo-audit/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── commands/                     # 40 slash commands
│   ├── seo-audit.md
│   ├── score-local-impact.md
│   ├── score-serp-trust.md
│   ├── generate-pdf.md
│   └── ...
├── research/                     # Research phase skills
│   ├── audit-intake/
│   ├── competitor-analysis/
│   ├── keyword-gaps/
│   ├── content-gaps/
│   └── topical-gaps/
├── audit/                        # Audit phase skills
│   ├── technical-seo/
│   ├── onpage-seo/
│   ├── content-audit/
│   ├── speed-optimization/
│   ├── penalty-check/
│   └── accessibility-audit/
├── local/                        # Local SEO skills
│   ├── local-seo/
│   ├── entity-audit/
│   ├── multi-location-seo/
│   ├── reputation-audit/
│   └── brand-serp/
├── ai-visibility/                # AI optimization skills
│   ├── ai-seo/
│   └── voice-search/
├── strategy/                     # Strategy skills
│   ├── topical-authority/
│   ├── backlink-audit/
│   ├── social-media-audit/
│   └── ux-cro-audit/
├── output/                       # Output skills
│   ├── report-generation/
│   └── pdf-report/
├── cross-cutting/                # Cross-cutting skills
│   ├── seo-audit-identity/
│   ├── local-impact-auditor/
│   └── serp-trust-auditor/
├── agents/                       # 6 sub-agents
├── references/                   # Scoring frameworks
│   ├── local-impact-benchmark.md
│   ├── serp-trust-benchmark.md
│   └── scoring-methodology.md
├── scripts/                      # 8 Python automation scripts
├── hooks/                        # Quality gate hooks
├── CLAUDE.md                     # Master audit framework
├── AGENTS.md                     # Sub-agent architecture
├── CONNECTORS.md                 # MCP connector patterns
├── skills.sh.json                # skills.sh distribution config (Vercel)
├── auto-improve.md               # Autonomous skill improvement loop
└── marketplace.json              # Marketplace distribution
```

---

## Skills (Auto-Activated)

Skills activate automatically when Claude detects relevant context:

| Skill | Phase Directory | Activates For |
|-------|----------------|---------------|
| `seo-audit-identity` | cross-cutting/ | Any SEO audit discussion |
| `audit-intake` | research/ | Starting an audit, providing URLs |
| `competitor-analysis` | research/ | Competitive research |
| `technical-seo` | audit/ | Crawlability, indexation, schema |
| `onpage-seo` | audit/ | Title tags, meta descriptions, headers |
| `content-audit` | audit/ | Content quality, thin content |
| `content-gaps` | research/ | Missing content opportunities |
| `keyword-gaps` | research/ | Keyword research, rankings |
| `topical-gaps` | research/ | Topic mapping, cluster gaps |
| `topical-authority` | strategy/ | Authority building |
| `entity-audit` | local/ | Knowledge Graph, entities |
| `speed-optimization` | audit/ | CWV, LCP, INP, CLS |
| `local-seo` | local/ | GBP, citations, NAP, reviews |
| `backlink-audit` | strategy/ | Link profile, link building |
| `social-media-audit` | strategy/ | Social profiles, engagement |
| `ai-seo` | ai-visibility/ | AI Overviews, AEO, GEO, LLM |
| `reputation-audit` | local/ | Reviews, sentiment, reputation |
| `brand-serp` | local/ | Branded search, Knowledge Panel |
| `ux-cro-audit` | strategy/ | Conversion paths, analytics |
| `voice-search` | ai-visibility/ | Voice queries, conversational |
| `accessibility-audit` | audit/ | WCAG, ADA, heading hierarchy |
| `penalty-check` | audit/ | Manual actions, penalties |
| `multi-location-seo` | local/ | Multi-location GBP |
| `report-generation` | output/ | Compiling audit reports |
| `pdf-report` | output/ | PDF report generation |
| `local-impact-auditor` | cross-cutting/ | LOCAL-IMPACT scoring |
| `serp-trust-auditor` | cross-cutting/ | SERP-TRUST scoring |

---

## Sub-Agents

Claude spawns specialized agents for parallel audit execution:

| Agent | Model | Handles | Phases |
|-------|-------|---------|--------|
| `technical-analyst` | sonnet | Technical + Speed + Accessibility | 2, 10, 19 |
| `content-analyst` | sonnet | Content + Gaps + Authority | 4, 5, 7, 8 |
| `keyword-analyst` | sonnet | Keywords + On-Page + Entities | 3, 6, 9 |
| `local-seo-analyst` | sonnet | Local + Reviews + Multi-location | 11, 15, 21 |
| `ai-visibility-analyst` | sonnet | AI SEO + Brand SERP + Voice | 14, 16, 18 |
| `offpage-analyst` | sonnet | Backlinks + Social + CRO | 12, 13, 17 |

---

## PDF Report

After completing an audit, generate a professionally designed PDF:

```
/local-seo-audit:generate-pdf
```

The PDF includes:
- Cover page with overall health score gauge
- **LOCAL-IMPACT & SERP-TRUST score dashboard** with dimension breakdowns
- SEO Health Index combined score
- Color-coded issue severity cards (critical/high/medium/low)
- Priority matrix (impact vs effort quadrant)
- Quick wins checklist
- Competitor comparison bar charts + framework score comparison
- Veto check status indicators
- Timeline roadmap visualization (30d/90d/6m/12m)
- KPI tracking framework
- Full phase-by-phase details with per-phase score gauges

**Zero dependencies** — uses Chrome headless (already on your Mac). HTML file is also kept for customization.

---

## MCP Connectors

The plugin works standalone but enhances with MCP integrations. See [CONNECTORS.md](CONNECTORS.md) for the tool-agnostic connector pattern.

**3-Tier Progressive Enhancement:**
- **Tier 1 (No tools):** Web search + fetch only — full audit capability
- **Tier 2 (Basic MCP):** PageSpeed API, search APIs — enhanced data
- **Tier 3 (Full integration):** GSC, GA4, GBP APIs — real-time analytics

---

## Requirements

- Claude Code v1.0.33 or later
- Web search and web fetch permissions enabled
- Google Chrome (for PDF generation — already installed on most systems)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-audit-phase`)
3. Commit your changes
4. Push and open a Pull Request

## License

MIT — see [LICENSE](LICENSE) for details.

## Support

- Issues: [GitHub Issues](https://github.com/mshahiddigital/local-seo-audit/issues)
- Discussions: [GitHub Discussions](https://github.com/mshahiddigital/local-seo-audit/discussions)
