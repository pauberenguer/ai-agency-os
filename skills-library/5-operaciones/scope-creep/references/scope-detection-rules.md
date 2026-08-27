# Scope Detection Rules

How to classify a client request as in-scope, scope creep, or hard OOS.

---

## Detection Order

Always check in this order — stop at the first match:

```
1. Hard OOS?      → flag immediately, send OOS response, no PRD
2. In scope_doc?  → proceed normally, no flag
3. Creep pattern? → generate PRD + PM ticket
4. Ambiguous?     → flag for approver review
```

---

## Hard OOS (No PRD — Immediate Decline)

| Signal | Example |
|--------|---------|
| Different client/project | "Can you do the same for my other business?" |
| Platform change | "Actually can we switch to Shopify?" |
| Post-delivery new work | "Now that it's live, can you add…" (project closed) |
| Work for a third party | "Can you also build one for my friend?" |

---

## Scope Creep Patterns (PRD Required)

### Pages & Content
- Request adds pages/sections not in original list
- Content rewrites beyond contracted revision rounds
- Blog, news, or events section not originally scoped
- Additional team/staff/portfolio pages beyond count

### Features & Functionality

| Request type | Scope creep if not in original contract |
|---|---|
| Online booking / scheduling | Yes |
| E-commerce / online store | Yes |
| Member login / gated content | Yes |
| Live chat widget | Yes |
| Events calendar | Yes |
| Multi-language | Yes |
| Custom calculator or tool | Yes |
| Advanced search | Yes |
| CRM integration | Yes |
| Email marketing integration | Yes — unless basic form only was scoped |
| Payment processing | Yes |
| Video backgrounds | Check original spec |
| Animations / scroll effects | Check original spec |

### Revision & Design
- Revision rounds beyond contracted number
- Complete redesign of already-approved sections
- New brand development (logo, color palette change)
- Custom illustration or icon set not in spec

### SEO & Marketing
- Full SEO audit beyond basic metadata setup
- Google Ads / paid media setup
- Social media profile creation
- Content strategy or copywriting beyond contracted pages

---

## Ambiguous Cases (Flag for Approver)

These don't clearly belong in or out — someone senior decides:

| Situation | Why it's ambiguous |
|---|---|
| "Make it pop more" | Could be a minor tweak or a full redesign |
| "Improve the form" | Minor fix (in scope) or new functionality (creep) |
| "Add some animation" | Check whether animation was in original spec |
| "The homepage feels off" | Fix (in scope) vs. redesign (creep) |
| Request from new contact | Verify they have authority to request changes |
| scope_doc is missing | No baseline — all unusual requests need review |

---

## Corrections vs. Changes

This distinction matters:

- Client says something is **wrong** → in-scope fix, no PRD needed
- Client says something should be **different** → may be a revision (check if
  revision rounds remain) or scope creep (if rounds are exhausted)

**Bug fixes post-delivery:**
- Bug that existed at delivery (your error) → in-scope fix
- New behavior added post-delivery disguised as a "fix" → scope creep

---

## Rush / Timeline Requests

A client asking for earlier delivery than scheduled is **timeline creep** —
it's not a feature add, but it still requires a change order process.

Use the rush fee template in `change-order-templates.md`.
Flag as `timeline_creep` in your PM ticket, not `feature_creep`.

---

## Maintenance Clients

Clients on a retainer or maintenance plan have a monthly hours allowance.
Requests that exceed the allowance still require a change order for the
overage — even if the work itself is "normal" maintenance.

Track hours carefully. Alert the client before they hit the limit.

---

## Scope_doc Keyword Matching

When you have a scope_doc, extract these terms and match incoming requests:

```
scope_doc says "5-page website"
→ any request for page 6+ = scope creep

scope_doc says "contact form"
→ request for multi-step form with conditional logic = scope creep

scope_doc says "3 revision rounds"
→ 4th revision request = scope creep

scope_doc says "basic SEO"
→ full SEO audit + keyword strategy = scope creep

scope_doc says "WordPress"
→ request to rebuild in React/Next.js = hard OOS
```

The scope_doc doesn't need to be exhaustive — it needs to be specific enough
that a reasonable person can tell what was and wasn't included.
