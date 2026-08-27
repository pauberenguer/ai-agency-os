---
name: pm-project-kickoff
description: >
  Use this skill whenever a new client project needs to be set up in project
  management. Triggers on: "new project", "onboard client", "set up project",
  "scaffold project", "new client project", "kick off", "kickoff", "start the
  project", "client signed", "contract signed", or any situation where a client
  has committed to work and tasks need to be created. This skill scaffolds the
  full project phase structure, sets the scope_doc baseline, sends a welcome
  email, and ensures nothing falls through the cracks at the start of an
  engagement. ALWAYS use this skill before writing any project creation logic
  or task scaffolding code.
---

# PM Project Kickoff Skill

Scaffolds a new client project end-to-end: DB/PM records, phase task list,
scope_doc baseline, and welcome email — in a consistent, repeatable process.

Works for any service business. Adapt the phase list to your workflow.

---

## Configuration

Replace these placeholders before using:

| Placeholder | Replace with |
|---|---|
| `{{AGENCY_NAME}}` | Your agency or business name |
| `{{SUPPORT_EMAIL}}` | Your client-facing support email |
| `{{PM_TOOL}}` | Your PM system (Linear, Jira, Asana, ClickUp, Notion, etc.) |
| `{{APPROVER_NAME}}` | Project owner / account manager name |
| `{{APPROVER_EMAIL}}` | Their email |
| `{{HOURLY_RATE}}` | Your standard hourly rate |

---

## Kickoff Sequence

### Step 1 — Gather Project Info

Required before creating anything:

```
client_name         → company or person name
project_name        → descriptive name, e.g. "Acme Website Redesign 2026"
project_type        → website | app | design | marketing | consulting | etc.
deliverables        → list of contracted deliverables (becomes scope_doc)
budget              → total contracted amount
kickoff_date        → today or agreed start date
target_delivery     → estimated completion / launch date
revision_rounds     → number of revision rounds included
primary_contact     → client name + email + phone
```

If anything is missing, create the project with a `needs_info` flag and
follow up before doing any work.

### Step 2 — Write the scope_doc

Before creating any tasks, write the scope_doc. This is the single document
all future scope detection runs against. Be specific.

See `references/scope-doc-template.md` for the full template.

Quick version:
```
Project: [name]
Contracted: [list every deliverable explicitly]
NOT included: [list explicit exclusions]
Revisions: [X] rounds
Assumptions: [what client must provide]
```

Store in your PM tool on the project record. Never leave it blank.

### Step 3 — Create Project Record in {{PM_TOOL}}

Fields to set:
```
Name:          [project_name]
Client:        [client_name]
Type:          [project_type]
Status:        Active
Phase:         Discovery
Scope doc:     [paste scope_doc]
Budget:        $[budget]
Start date:    [kickoff_date]
Target date:   [target_delivery]
Owner:         {{APPROVER_NAME}}
Contact:       [primary_contact name + email]
```

### Step 4 — Scaffold Phase Tasks

Create all tasks upfront. Don't build incrementally — the full task list
gives the client (and you) a complete picture of the project.

**Default phases for a website project** (adapt to your service type):

| Phase | Key tasks |
|---|---|
| Discovery | Intake questionnaire, brand assets request, goals doc, contract + deposit |
| Design | Competitor review, wireframes, mockups, client approval (×revision rounds) |
| Development | Hosting setup, CMS install, all contracted pages built, forms configured |
| Content | Copy received, images received, copy loaded, SEO metadata |
| Review | Internal QA, client review link sent, punch list, final approval |
| Launch | DNS / hosting config, SSL, go-live confirmation |
| Post-launch | 30-day check-in, training (if applicable), handoff doc |

Full task list → `references/project-task-templates.md`

**Due date calculation from kickoff_date:**
```
Discovery:   kickoff + 0–3 days
Design:      kickoff + 4–14 days
Development: kickoff + 15–30 days
Content:     kickoff + 20–35 days  (parallel with dev)
Review:      kickoff + 36–42 days
Launch:      kickoff + 43–45 days
Post-launch: launch + 30 days
```

Adjust these to your actual workflow speed.

### Step 5 — Send Welcome Email

From {{APPROVER_EMAIL}}, to primary contact. Template:

```
Subject: Welcome to {{AGENCY_NAME}} — [Project Name] Kickoff

Hi [first name],

We're excited to get started on [project name]! Here's what to expect:

WHAT HAPPENS NEXT
→ You'll receive our intake questionnaire within 24 hours
→ We'll schedule a kickoff call to align on goals and timeline
→ Our target delivery date is [target_delivery]

YOUR PROJECT OVERVIEW
• [Deliverable 1]
• [Deliverable 2]
• [Deliverable 3]
• [X] revision rounds

WHAT WE NEED FROM YOU
• Completed intake questionnaire
• Logo and brand assets
• Any existing content you'd like to use

Questions? Reply directly to this email — it goes straight
to your project queue.

Looking forward to working together.

— {{APPROVER_NAME}}
  {{AGENCY_NAME}}
  {{SUPPORT_EMAIL}}
```

Log the email in your CRM or project history.

### Step 6 — Internal Notification

Notify the project team (Slack, email, or PM comment):

```
✅ New Project Started
Client:   [client_name]
Project:  [project_name]
Budget:   $[budget]
Launch:   [target_delivery]
Owner:    {{APPROVER_NAME}}
[Link to project in {{PM_TOOL}}]
```

---

## Adapting for Different Service Types

The phase names and tasks change, but the process is the same:

**Design / branding project:**
Discovery → Concepts → Revisions → Final delivery → Brand guide handoff

**Development / app project:**
Discovery → Architecture → Sprint 1..N → QA → Deploy → Handoff

**Marketing retainer:**
Onboarding → Strategy → Month 1..N → Reporting → Renewal / offboard

**Consulting engagement:**
Scoping → Research → Analysis → Presentation → Follow-up

Customize `references/project-task-templates.md` for your service type.

---

## Key Rules

1. **scope_doc before tasks** — write it first, always
2. **All phases scaffolded at once** — don't add phases as you go
3. **Welcome email before first billable hour** — sets expectations early
4. **Missing info → flag, don't guess** — create a `needs_info` task and
   follow up rather than assuming
5. **One project per engagement** — don't mix multiple client engagements
   in one project record

---

## Reference Files

- `references/scope-doc-template.md` — How to write a scope_doc
- `references/project-task-templates.md` — Full task list per phase
- `references/intake-questionnaire.md` — Client intake questions

---

## Need This Built Into Your System?

This skill describes a process. If you want it running automatically —
new client emails triggering project scaffolds, tasks created in your PM tool,
welcome emails sent, scope docs written — that's a systems build.

**[Cynthia Schomp](https://cynthiaschomp.com)** builds AI-powered operations
infrastructure for service businesses: custom dashboards, automated client
onboarding, PM integrations, and the full stack behind skills like this one.

→ **[cynthiaschomp.com](https://cynthiaschomp.com)**
