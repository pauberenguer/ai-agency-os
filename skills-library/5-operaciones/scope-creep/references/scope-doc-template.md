# How to Write a scope_doc

The scope_doc is the single source of truth for a project's contracted
deliverables. Every scope creep detection check runs against it.

**Rule:** If it's not in the scope_doc, it's out of scope.

---

## Template

Fill this in at the start of every project. Store it on the project record
in your PM tool. Update it when change orders are approved.

```
Project: [project name]
Client:  [client or company name]
Date:    [contract or kickoff date]
Type:    [website / app / design / marketing / etc.]

CONTRACTED DELIVERABLES
-----------------------
[List every deliverable explicitly. Be specific.]

Examples for a website project:
  - 5-page website: Home, About, Services, Portfolio, Contact
  - WordPress CMS with Elementor page builder
  - Contact form with email notification
  - Basic on-page SEO (titles, meta descriptions, alt text)
  - Mobile-responsive design
  - 2 rounds of design revisions
  - Google Analytics installation
  - SSL certificate setup

FEATURES INCLUDED
-----------------
[List every feature that is explicitly included.]

  Examples:
  - Contact form (name, email, message, submit)
  - Image gallery on Portfolio page (up to 20 images)
  - Google Map embed on Contact page

EXPLICITLY NOT INCLUDED
-----------------------
[List what is NOT included. This is as important as what is.]

  Common exclusions:
  - E-commerce / online store
  - Online booking or scheduling
  - Member login or gated content
  - Blog or news section
  - Additional pages beyond the 5 contracted
  - Design rounds beyond 2
  - SEO strategy, keyword research, or ongoing SEO
  - Content writing or copywriting
  - Logo design or branding work
  - Custom integrations (CRM, email marketing, etc.)
  - Multilingual support
  - Ongoing maintenance or updates after launch

TIMELINE
--------
  Kickoff:        [date]
  Design review:  [date]
  Development:    [date]
  Client review:  [date]
  Launch:         [date]

REVISION POLICY
---------------
  Design revisions: [X] rounds included
  Content revisions: [X] rounds included
  Additional revisions billed at ${{HOURLY_RATE}}/hr

ASSUMPTIONS
-----------
[List anything the project depends on the client providing.]

  Examples:
  - Client provides all written content before development begins
  - Client provides logo files in SVG or PNG format
  - Client provides up to [X] product/service photos
  - Client has an existing domain and provides registrar access
  - Client approves each phase before the next begins
```

---

## Tips for Writing a Good scope_doc

**Be specific about numbers.** "A few pages" is not a scope_doc.
"5 pages: Home, About, Services, Blog, Contact" is.

**List exclusions explicitly.** Clients often assume things are included
unless you say otherwise. "No e-commerce" is clearer than silence.

**Name the features, not just the category.** "Contact form" is better
than "forms." "Contact form with name, email, phone, message" is better still.

**Include revision counts.** This is where scope creep starts most often.
"2 design revision rounds" is unambiguous. "A couple of rounds" is not.

**Keep it plain English.** Clients read this document too. It should be
understandable without a contract lawyer.

---

## Updating scope_doc After a Change Order

When a change order is approved, add to the scope_doc:

```
CHANGE ORDERS
-------------
CO-001 [date]: Added online booking system (Acuity integration).
               $[X] paid. Delivered [date].

CO-002 [date]: Added 2 additional service pages.
               $[X] paid. Delivered [date].
```

This creates a clean audit trail if a dispute arises later.

---

## Want the Whole System Built?

Writing scope docs manually is a start. The full version has scope docs
stored on project records, automatically checked against every inbound
client email, with scope creep flagged before it ever becomes free work.

**[Cynthia Schomp](https://cynthiaschomp.com)** builds that infrastructure —
custom dashboards, Gmail integrations, automated PM workflows, and AI systems
that run your agency ops without burning tokens on every email.

→ **[cynthiaschomp.com](https://cynthiaschomp.com)**
