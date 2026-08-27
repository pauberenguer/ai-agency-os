# Connectors

> Skills use `~~category` placeholders instead of specific tool names. Replace each placeholder with whichever tool your organization uses.

## Tool Categories

| Category | Placeholder | Example Tools | Included Server |
|----------|-------------|---------------|-----------------|
| SEO Platform | `~~SEO tool` | Ahrefs, SEMrush, Moz, Sistrix, SE Ranking | — |
| Analytics | `~~analytics` | Google Analytics, Adobe Analytics, Plausible, Matomo | GA4 |
| Search Console | `~~search console` | Google Search Console, Bing Webmaster Tools | GSC |
| GBP Management | `~~GBP tool` | Google Business Profile, BrightLocal, Whitespark | GBP |
| Page Speed | `~~page speed tool` | Google PageSpeed Insights, GTmetrix, WebPageTest | PSI |
| AI Visibility | `~~AI monitor` | Otterly, Profound, Scrunch AI | — |
| Web Crawler | `~~web crawler` | Screaming Frog, Sitebulb, Lumar, DeepCrawl | — |
| Link Database | `~~link database` | Ahrefs, Majestic, Moz Link Explorer | — |
| Competitive Intel | `~~competitive intel` | SimilarWeb, SpyFu, SEMrush | SimilarWeb |
| Citation Manager | `~~citation manager` | BrightLocal, Whitespark, Yext, Moz Local | — |
| Review Manager | `~~review tool` | BrightLocal, Podium, Birdeye, ReviewTrackers | — |
| Schema Validator | `~~schema validator` | Google Rich Results Test, Schema.org Validator | — |
| Knowledge Graph | `~~knowledge graph` | Google Knowledge Graph API, Wikidata SPARQL | — |
| Rank Tracker | `~~rank tracker` | Ahrefs, SEMrush, AccuRanker, SERPWatcher | — |
| CMS | `~~CMS` | WordPress, Webflow, Shopify, Wix, Squarespace | — |
| Reporting | `~~reporting` | Google Looker Studio, Tableau, Power BI | — |

## Configuring MCP Connectors

The included `.mcp.json` uses placeholder URLs — they do **not** work out of the box. The plugin works at **Tier 1** (web search + manual data) with zero MCP setup. Activate MCP connectors when you want automated data retrieval.

### Step-by-step activation

1. **PageSpeed Insights** — the simplest to activate. Use the open-source MCP server:
   ```json
   "pagespeed-insights": {
     "command": "npx",
     "args": ["-y", "@modelcontextprotocol/server-pagespeed"]
   }
   ```

2. **Google Search Console / GA4 / Google Business Profile** — require OAuth credentials. Options:
   - Self-host: [google-workspace-mcp](https://github.com/MarkusPfundstein/mcp-gsuite)
   - Managed: Use a third-party MCP hosting service (e.g., Zapier MCP, Make MCP)
   - Enterprise: Your organization's existing GCP service account

3. **SimilarWeb** — `https://mcp.similarweb.com/sse` is SimilarWeb's official MCP endpoint. Requires an active SimilarWeb API subscription.

4. Replace placeholder entries in `.mcp.json` with your configured endpoints before use.

> Skipping MCP setup is fine — all 21 audit phases work via WebSearch + WebFetch at Tier 1.

## Included MCP Servers

Pre-configured in `.mcp.json` (replace placeholder URLs with your actual endpoints):

| Server | What It Provides |
|--------|-----------------|
| Google Search Console | Queries, pages, coverage, Core Web Vitals |
| Google Analytics (GA4) | Traffic, conversions, events, user behavior |
| Google Business Profile | Reviews, insights, posts, Q&A |
| PageSpeed Insights | CWV performance data, lab and field metrics |
| SimilarWeb | Competitor traffic estimates, keyword data |

## How Placeholders Work

A skill might say:

```
Pull keyword rankings from ~~SEO tool and cross-reference with ~~search console impressions.
Check review velocity using ~~review tool and compare against ~~competitive intel data.
```

If your organization uses Ahrefs and Google Search Console, read it as:

```
Pull keyword rankings from Ahrefs and cross-reference with Google Search Console impressions.
```

## Progressive Enhancement Tiers

Skills work at three levels of tool integration:

| Tier | Integration Level | Experience |
|------|-------------------|------------|
| **Tier 1** | No integrations | Paste data manually, describe context. Skills provide full analysis frameworks and recommendations. |
| **Tier 2** | Basic MCP | Connect ~~search console and ~~analytics for automatic data retrieval. Most audit phases become data-driven. |
| **Tier 3** | Full integration | ~~SEO tool + ~~analytics + ~~search console + ~~GBP tool + ~~web crawler for fully automated audits with competitive data. |

Every skill works without any tool integration (Tier 1). Connecting tools via MCP automates data retrieval but is never required.

## Adding a New Connector

Edit `.mcp.json` at the project root:

```json
{
  "mcpServers": {
    "your-tool-name": {
      "type": "url",
      "url": "https://your-mcp-endpoint.com/sse",
      "description": "What this tool provides"
    }
  }
}
```
