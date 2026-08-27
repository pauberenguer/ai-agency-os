# PRD Template — Scope Change

Copy this for every scope creep item. Fill in all sections.
Store wherever your team keeps project docs (Notion, Drive, Confluence, etc.)

Replace `{{AGENCY_NAME}}`, `{{APPROVER_NAME}}`, `{{HOURLY_RATE}}`,
`{{PAYMENT_TERMS}}` with your own values before using.

---

```markdown
# PRD: [Feature / Request Name]

**Project:** [project name]
**Client:** [client or company name]
**Date:** [YYYY-MM-DD]
**Requested via:** [Email / Slack / Call / Meeting notes]
**Requested by:** [Client contact full name]
**Owner:** {{APPROVER_NAME}} — {{AGENCY_NAME}}
**PM Ticket:** [ticket link or ID]
**Status:** Pending Approval

---

## 1. Request Summary

[1–2 sentences. Plain English. What is the client asking for?]

Example: "Client is requesting an online booking system integrated into
the homepage, allowing customers to schedule appointments directly."

---

## 2. Original Scope

[Paste the relevant section from your scope_doc, or state clearly
that this was not included.]

> From scope_doc:
> "[paste relevant excerpt]"

OR

> This feature was not addressed in the original project scope
> dated [date of original proposal/contract].

---

## 3. Gap Analysis

[What does this request add beyond what was contracted?]

| What's Requested | What Was Contracted | Gap |
|---|---|---|
| [feature] | [original deliverable] | [delta] |

---

## 4. Proposed Solution

[Brief description of how this would be built — 3–5 sentences.
Not a full spec. Enough for the approver to understand the approach
and sanity-check the estimate.]

---

## 5. Tasks Required

| # | Task | Est. Hours |
|---|------|------------|
| 1 | [task] | [h] |
| 2 | [task] | [h] |
| 3 | [task] | [h] |
| **Total** | | **[X] hours** |

---

## 6. Dependencies

- [Tasks that must be complete before this work can start]
- [External accounts, credentials, or third-party services needed]
- [Client deliverables required before work begins]

None if not applicable.

---

## 7. Estimate

| Item | Detail |
|---|---|
| **Estimated hours** | [X] hours |
| **Rate** | ${{HOURLY_RATE}}/hr |
| **Subtotal** | $[X] |
| **Rush fee** (if applicable) | $[X] |
| **Total** | **$[X]** |
| **Timeline** | [X] business days after approval + deposit |
| **Payment terms** | {{PAYMENT_TERMS}} |

---

## 8. Impact on Current Project

| Area | Detail |
|---|---|
| **Current phase** | [what phase the project is in now] |
| **Timeline impact** | [X days added / no impact] |
| **Risk** | [does this block anything? create rework?] |
| **Recommendation** | [add now / post-launch / separate project] |

---

## 9. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| Delays current launch | Low / Med / High | [mitigation] |
| Third-party dependency | Low / Med / High | [mitigation] |
| Opens further scope expansion | Low / Med / High | [mitigation] |

---

## 10. Recommendation

Select one:

- [ ] **Add to current project** — change order, adjust timeline
- [ ] **Separate project** — deliver after current launch
- [ ] **Decline** — not feasible or not aligned with goals
- [ ] **Defer** — revisit post-launch

**Rationale:** [1–2 sentences explaining the recommendation]

---

## 11. Approval

| Decision | By | Date | Notes |
|---|---|---|---|
| [ ] Approved | | | |
| [ ] Declined | | | |
| [ ] More Info | | | |

**If Approved — checklist:**
- [ ] Change order sent to client
- [ ] scope_doc updated
- [ ] Task activated on project board
- [ ] PM ticket updated to Approved

**If Declined — checklist:**
- [ ] OOS response sent to client
- [ ] Pending task removed from board
- [ ] PM ticket closed
```
