# Technical SEO Quick Reference

## Critical Checks (Must Pass)

| Check | How to Verify | Pass Criteria |
|-------|--------------|---------------|
| HTTPS | Fetch URL | Valid cert, no mixed content |
| Robots.txt | Fetch /robots.txt | Not blocking critical pages |
| Sitemap | Fetch /sitemap.xml | Valid XML, all key URLs included |
| Indexation | site:domain.com | Expected pages indexed |
| Mobile | Responsive viewport meta | `<meta name="viewport" content="width=device-width, initial-scale=1">` |

## Core Web Vitals Targets (2026)

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| LCP | < 2.5s | 2.5-4.0s | > 4.0s |
| INP | < 200ms | 200-500ms | > 500ms |
| CLS | < 0.1 | 0.1-0.25 | > 0.25 |
| TTFB | < 800ms | 800-1800ms | > 1800ms |
| FCP | < 1.8s | 1.8-3.0s | > 3.0s |

## Schema Types for Local Business

Required:
- `LocalBusiness` (or specific subtype)
- `BreadcrumbList`
- `Organization` (sameAs links)

Recommended:
- `Service` (per service page)
- `FAQPage` (FAQ sections)
- `AggregateRating` (if reviews displayed)
- `Article`/`BlogPosting` (blog posts)
- `HowTo` (process/guide content)
- `VideoObject` (embedded videos)

## Common Issues & Fixes

| Issue | Impact | Fix |
|-------|--------|-----|
| Redirect chains | Medium | Flatten to single 301 |
| Missing canonicals | High | Add self-referencing canonicals |
| Orphan pages | Medium | Add internal links |
| Render-blocking CSS/JS | High | Defer, async, or inline critical |
| Large images | High | Convert to WebP, compress, lazy-load |
| Missing alt text | Medium | Add descriptive alt attributes |
| Duplicate titles | High | Make each title unique |
| No structured data | High | Implement LocalBusiness + Breadcrumbs minimum |
