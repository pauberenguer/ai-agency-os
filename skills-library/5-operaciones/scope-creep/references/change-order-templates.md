# Change Order & OOS Email Templates

Six client-facing templates for every scope creep outcome.
Replace `{{AGENCY_NAME}}`, `{{APPROVER_NAME}}`, `{{PAYMENT_TERMS}}` before using.
Never send without {{APPROVER_NAME}} reviewing first.

---

## Template 1 — Approved: Adding to Current Project

**Subject:** Re: [original subject] — Change Order

```
Hi [first name],

Good news — we can add [feature/request] to your current project.

Here's a quick summary:

  What's being added: [1-sentence description]
  Estimated hours:    [X] hours
  Investment:         $[X]
  Timeline:           [X] business days after deposit received

To move forward, I'll send a change order for your signature.
Once we receive your deposit ($[X/2]), we'll get started and
adjust your timeline accordingly.

Questions? Just reply here.

— {{APPROVER_NAME}}
  {{AGENCY_NAME}}
```

---

## Template 2 — Approved: As a Separate Project

**Subject:** Re: [original subject] — New Project Proposal

```
Hi [first name],

Thanks for thinking of us for this! We'd recommend building [feature]
as a separate project after your current site launches — that way
it doesn't push your go-live date.

Here's an overview:

  What's included: [brief description]
  Estimated investment: $[X]
  Recommended start: After [current project name] is live

I'll follow up with a full proposal once your current project wraps.
Feel free to reach out with any questions in the meantime.

— {{APPROVER_NAME}}
  {{AGENCY_NAME}}
```

---

## Template 3 — Declined: Out of Scope

**Subject:** Re: [original subject]

```
Hi [first name],

Thanks for reaching out! This request falls outside the scope of
your current project ([project name]).

We'd be happy to scope it out as a separate engagement. I can
have an estimate to you within 1 business day — just let me know
if you'd like us to proceed.

— {{APPROVER_NAME}}
  {{AGENCY_NAME}}
```

---

## Template 4 — Declined: Not Feasible

**Subject:** Re: [original subject]

```
Hi [first name],

Thanks for the idea! After reviewing the request, this one isn't
something we're able to include in your current project.

[Optional: one sentence explaining why — keep it simple.]

If you'd like to explore alternatives, I'm happy to jump on a
quick call. Just reply here and we'll find a time.

— {{APPROVER_NAME}}
  {{AGENCY_NAME}}
```

---

## Template 5 — Need More Info

**Subject:** Re: [original subject] — Quick Question

```
Hi [first name],

Thanks for the request! Before we can put together a quote,
we have a quick question:

  [Specific clarifying question]

Once we have that, we'll get back to you within 1 business day.

— {{APPROVER_NAME}}
  {{AGENCY_NAME}}
```

---

## Template 6 — Rush / Timeline Request

**Subject:** Re: [original subject] — Timeline

```
Hi [first name],

We'd love to move faster! Based on our current schedule, the
earliest we can deliver [deliverable] is [original date].

If you'd like to expedite to [requested date], we can prioritize
your project for a rush fee of $[X].

Let us know how you'd like to proceed.

— {{APPROVER_NAME}}
  {{AGENCY_NAME}}
```

---

## Formal Change Order Document

For any approved scope addition, generate a formal change order.
Get client signature before starting work.

```markdown
# Change Order — [CO Number]

**Date:**           [date]
**Project:**        [project name]
**Client:**         [company name]
**Original contract date:** [date]
**Issued by:**      {{AGENCY_NAME}}

---

## Change Description

[Plain English description of what's being added]

## Work to be Performed

[Task list from PRD Section 5]

## Investment

| Item | Amount |
|---|---|
| Additional hours | [X] hrs @ ${{HOURLY_RATE}}/hr |
| Total | $[X] |
| Deposit (due before work begins) | $[X] |
| Balance (due on completion) | $[X] |

**Payment terms:** {{PAYMENT_TERMS}}

## Timeline

[X] business days from deposit receipt.

## Agreement

This change order is governed by the terms of the original service
agreement dated [date]. By signing below, client authorizes
{{AGENCY_NAME}} to proceed with the above work.

Client signature: ___________________ Date: ___________

{{AGENCY_NAME}}:  ___________________ Date: ___________
```
