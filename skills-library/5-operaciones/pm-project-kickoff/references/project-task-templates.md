# Project Task Templates

Default task list for a website project. Adapt to your service type.
Each `task_key` is a machine-readable identifier for automation.
Each task starts with status `pending`.

---

## Phase 1 — Discovery

| task_key | Task name | Notes |
|---|---|---|
| `discovery.intake_questionnaire` | Send client intake questionnaire | See intake-questionnaire.md |
| `discovery.brand_assets` | Request logo, colors, fonts, existing materials | |
| `discovery.goals_doc` | Document project goals and success criteria | |
| `discovery.contract_signed` | Contract signed and deposit received | Do not proceed until complete |
| `discovery.domain_access` | Obtain domain registrar login or transfer details | |
| `discovery.hosting_access` | Confirm hosting platform and credentials | |

## Phase 2 — Design

| task_key | Task name | Notes |
|---|---|---|
| `design.competitor_review` | Competitor and inspiration review | 3–5 examples |
| `design.brand_brief` | Brand brief created (colors, fonts, tone) | |
| `design.wireframes` | Wireframes delivered to client | |
| `design.wireframe_approval` | Wireframes approved | |
| `design.mockup_homepage` | Homepage mockup designed | |
| `design.mockup_approval_1` | Round 1 mockups approved | |
| `design.mockup_revision_1` | Round 1 revisions complete | Add more rows if more rounds contracted |
| `design.final_design_approval` | Final design signed off | |

## Phase 3 — Development

| task_key | Task name | Notes |
|---|---|---|
| `dev.hosting_setup` | Hosting environment configured | |
| `dev.domain_pointed` | Domain pointed to host | |
| `dev.ssl_installed` | SSL certificate installed and verified | |
| `dev.cms_install` | CMS installed (WordPress, Webflow, etc.) | |
| `dev.theme_setup` | Theme or page builder installed and configured | |
| `dev.plugins_setup` | Required plugins/extensions installed | |
| `dev.pages_built` | All contracted pages built | |
| `dev.forms_configured` | Forms set up and tested end-to-end | |
| `dev.mobile_review` | Mobile responsiveness verified | Test 3 breakpoints |
| `dev.speed_check` | Page speed baseline measured | Target ≥ 60 PageSpeed score |

## Phase 4 — Content

| task_key | Task name | Notes |
|---|---|---|
| `content.copy_received` | All written content received from client | |
| `content.images_received` | Photos and images received from client | |
| `content.copy_loaded` | Copy loaded into all pages | |
| `content.images_optimized` | Images optimized and uploaded | |
| `content.seo_metadata` | SEO titles and meta descriptions written | |
| `content.alt_text` | Alt text added to all images | |

## Phase 5 — Review

| task_key | Task name | Notes |
|---|---|---|
| `review.internal_qa` | Internal QA pass complete | Check links, forms, mobile, speed |
| `review.client_link_sent` | Client review link sent | |
| `review.punch_list` | Punch list documented | |
| `review.punch_list_resolved` | All punch list items resolved | |
| `review.final_approval` | Final written client sign-off received | Email confirmation is sufficient |

## Phase 6 — Launch

| task_key | Task name | Notes |
|---|---|---|
| `launch.dns_config` | DNS configured for production domain | |
| `launch.ssl_final` | SSL verified on live domain | |
| `launch.redirects` | 301 redirects set up (if applicable) | |
| `launch.analytics_installed` | Analytics tracking installed and verified | |
| `launch.search_console` | Google Search Console verified | |
| `launch.go_live_confirmed` | Go-live confirmed with client | |

## Phase 7 — Post-Launch

| task_key | Task name | Notes |
|---|---|---|
| `postlaunch.30_day_checkin` | 30-day check-in completed | Review uptime, forms, analytics |
| `postlaunch.training` | Client training completed (if applicable) | |
| `postlaunch.handoff_doc` | Handoff document delivered | Logins, how-to guide |
| `postlaunch.backups_verified` | Automated backups confirmed active | |
| `postlaunch.maintenance_discussed` | Ongoing maintenance plan discussed | |

---

## Adapting for Other Service Types

**Remove phases you don't need. Add phases specific to your work.**

For a branding project, replace Development + Content with:
- `brand.concepts` — 3 initial concept directions presented
- `brand.concept_selected` — Client selects direction
- `brand.refinement` — Selected concept refined
- `brand.final_files` — Final files exported (SVG, PNG, PDF)
- `brand.brand_guide` — Brand guide document delivered

For a marketing retainer, replace all phases with monthly cycles:
- `month_N.strategy` — Monthly strategy approved
- `month_N.content_created` — Content created
- `month_N.content_approved` — Content approved
- `month_N.published` — Content published
- `month_N.report` — Monthly report delivered
