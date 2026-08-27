---
name: scope-creep
description: >
  Use this skill whenever a client requests work that may fall outside their
  contracted project scope. Triggers on: "scope creep", "out of scope", "client
  wants more", "they're asking for extra", "not in the contract", "new request
  on existing project", "change request", "additional work", "they added to the
  list", "this wasn't in the original scope", or any situation where a client
  email, message, or conversation includes a request that needs to be checked
  against project scope. ALWAYS use this skill before writing any scope
  analysis, PRD, change order, or ticket for scope-related work. This skill
  covers detection, documentation (PRD), ticketing, and the full approval
  workflow through to client quote.
---

# Scope Creep Skill

Detects scope creep on client projects, generates a PRD for the requested
work, creates a ticket in your project management system, and routes through
an approval workflow before any action or quote is sent.

Works for any service business — web agencies, dev shops, design studios,
marketing agencies, consultancies.

---

## Configuration

Replace these placeholders before using:

| Placeholder | Replace with |
|---|---|
| `{{AGENCY_NAME}}` | Your agency or business name |
| `{{SUPPORT_EMAIL}}` | Your client-facing support email |
| `{{PM_TOOL}}` | Your PM system (Linear, Jira, Asana, ClickUp, etc.) |
| `{{APPROVER_NAME}}` | Name of person who approves scope changes |
| `{{APPROVER_EMAIL}}` | Their email |
| `{{HOURLY_RATE}}` | Your standard hourly rate |
| `{{PAYMENT_TERMS}}` | e.g. "50% deposit, 50% on completion" |

---

## Overview: Full Scope Creep Lifecycle

```
Client Email / Message / Call
          ↓
  Scope Check (vs scope_doc)
          ↓
  Scope Creep Detected
          ↓
  Generate PRD
          ↓
  Create PM Ticket (flagged)
          ↓
  Approval Queue → {{APPROVER_NAME}}
          ↓
  ┌──────────────────────┐
  │   Decision           │
  └──────────────────────┘
    ↓              ↓
  APPROVED       DECLINED
    ↓              ↓
  Send quote    Send OOS
  Add tasks     response
  Update scope
```

---

## Step 1 — Scope Check

Every project should have a `scope_doc` — plain text describing exactly what
was contracted. This is the baseline all detection runs against.

**If you don't have a scope_doc yet:** Create one now from the original
proposal or contract. See `references/scope-doc-template.md`.

Compare the request against the scope_doc using three layers:

### Layer 1 — Hard OOS (auto-flag, no PRD needed)
- References a completely different client, domain, or project
- Requests a platform change (e.g., WordPress → Shopify)
- New work on a project already marked complete/delivered

### Layer 2 — Scope Creep (requires PRD + approval)
- New page, section, or deliverable not in original list
- New feature not in original proposal
- Additional revision rounds beyond what was contracted
- New third-party integration not scoped
- Content or copy work beyond contracted volume
- SEO, analytics, or marketing work beyond basic setup

### Layer 3 — Ambiguous (flag for {{APPROVER_NAME}} review)
- Vague request that could be an in-scope fix or a new feature
- Expansion of an existing feature ("make the form do more")
- Request from a new contact not on the original project
- Anything where scope_doc is missing or unclear

Full detection rules and edge cases → `references/scope-detection-rules.md`

---

## Step 2 — Generate PRD

For every confirmed or ambiguous scope creep item, generate a PRD.
Store it wherever your team keeps project docs (Drive, Notion, Confluence, etc.)

PRD template → `references/prd-template.md`

Key sections:
1. Request summary (1–2 sentences, plain English)
2. Original scope (paste from scope_doc)
3. Gap analysis (what's being added)
4. Proposed solution (brief technical approach)
5. Tasks required (with hour estimates)
6. Dependencies
7. Estimate (hours × rate + timeline)
8. Impact on current project
9. Risks
10. Recommendation (add now / separate project / decline / defer)
11. Approval block

---

## Step 3 — Create PM Ticket

Create a ticket in {{PM_TOOL}} flagged as a scope change.

**Ticket fields:**
```
Type:        Change Request
Title:       Scope Change: [Feature Name] — [Client Name]
Status:      Pending Approval
Priority:    Medium
Assigned to: {{APPROVER_NAME}}
Labels:      scope-creep, change-order
Description: [PRD summary — sections 1–3]
Link:        [Link to full PRD]
Source:      [Original email/message link or reference]
Rollback:    If declined — send OOS response, close ticket, no work added.
```

---

## Step 4 — Add to Project (Pending)

Create a placeholder task on the project board with status `pending_approval`.
Mark it visually distinct (different color, blocked label) so it doesn't get
picked up and worked on accidentally.

Task note: `Pending approval — see [ticket link]. Do not start until approved.`

---

## Step 5 — Notify {{APPROVER_NAME}}

Send an internal notification (Slack, email, PM comment) with:

```
🔴 Scope Change — Approval Needed
Client:   [client name]
Project:  [project name]
Request:  [one-line summary]
Estimate: $[X] / [X] hours
PRD:      [link]

[Approve] [Decline] [Need More Info]
```

---

## Step 6 — Approval Decision

### If APPROVED
1. Activate the pending task on the project board
2. Update scope_doc to include the new item
3. Send change order / quote to client (template in references)
4. Update PM ticket → `Approved`
5. Log scope change in project history

### If DECLINED
1. Remove or archive the pending task
2. Update PM ticket → `Declined`
3. Send OOS response to client (template in references)

### If MORE INFO NEEDED
1. Update PM ticket → `On Hold`
2. Draft clarifying question to client
3. {{APPROVER_NAME}} reviews before sending

---

## Key Rules

1. **Never start work on scope creep without approval** — a pending task is
   just a placeholder, not a green light
2. **Always generate PRD first** — ticket links to PRD, not the other way
3. **scope_doc must be updated on approval** — never let it go stale
4. **Client gets a quote before work starts** — no surprise billing, ever
5. **Declined items get a response** — client should never hear nothing

---

## Reference Files

- `references/scope-detection-rules.md` — Full detection logic, edge cases
- `references/prd-template.md` — 11-section PRD template
- `references/change-order-templates.md` — Client email templates (6 scenarios)
- `references/scope-doc-template.md` — How to write a scope_doc from scratch

---

## Need This Built Into Your System?

This skill describes a process. If you want it running automatically —
emails classified, PRDs generated, tickets created, approval queue in a
dashboard — that's a systems build.

**[Cynthia Schomp](https://cynthiaschomp.com)** builds AI-powered operations
infrastructure for service businesses: custom dashboards, automated workflows,
Gmail and PM integrations, and the full stack behind skills like this one.

→ **[cynthiaschomp.com](https://cynthiaschomp.com)**
