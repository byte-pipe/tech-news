---
title: 'GitHub - every-app/open-seo: Open source alternative to Semrush and Ahrefs · GitHub'
url: https://github.com/every-app/open-seo
site_name: github
content_file: github-github-every-appopen-seo-open-source-alternative-t
fetched_at: '2026-06-25T19:39:52.068933'
original_url: https://github.com/every-app/open-seo
author: every-app
description: Open source alternative to Semrush and Ahrefs. Contribute to every-app/open-seo development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 every-app

 

/

open-seo

Public

* NotificationsYou must be signed in to change notification settings
* Fork292
* Star2.4k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

286 Commits
286 Commits
.agents/
skills
.agents/
skills
 
 
.claude/
skills
.claude/
skills
 
 
.github/
workflows
.github/
workflows
 
 
.opencode
.opencode
 
 
.vscode
.vscode
 
 
docs
docs
 
 
drizzle
drizzle
 
 
e2e
e2e
 
 
public
public
 
 
release-notes
release-notes
 
 
scripts
scripts
 
 
specs
specs
 
 
src
src
 
 
web
web
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.oxlintrc.json
.oxlintrc.json
 
 
.prettierignore
.prettierignore
 
 
Dockerfile.selfhost
Dockerfile.selfhost
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
cli-auth.ts
cli-auth.ts
 
 
compose.yaml
compose.yaml
 
 
drizzle-prod.config.ts
drizzle-prod.config.ts
 
 
drizzle.config.ts
drizzle.config.ts
 
 
knip.jsonc
knip.jsonc
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.json
tsconfig.json
 
 
vite.config.ts
vite.config.ts
 
 
vitest.config.ts
vitest.config.ts
 
 
worker-configuration.d.ts
worker-configuration.d.ts
 
 
wrangler.jsonc
wrangler.jsonc
 
 
View all files

## Repository files navigation

# OpenSEO

Open source alternative to Semrush and Ahrefs

OpenSEO is an SEO tool forthe people. If tools like Semrush or Ahrefs are too expensive or bloated, OpenSEO is a pay-as-you-go alternative that you actually control.

All-in-one SEO tool for you and your AI agent.

Connect with any agent like Claude Code, OpenClaw or Hermes. We have pre-built skills, but you can build your own to tailor OpenSEO to your needs.

## Table of Contents

* Why use OpenSEO?
* Main SEO Workflows
* OpenSEO MCP
* OpenSEO Agent Skills
* Roadmap
* Community
* Pricing / Costs (Free + API costs)
* DataForSEO API Key Setup
* Google Search Console
* Self-hostingDocker Self HostingCloudflare Self-Hosting
* Docker Self Hosting
* Cloudflare Self-Hosting
* Local Development
* Contributing
* SEO API Cost Reference

## Hosted Version

If you not interested in self hosting, or just want to support the project, we also have a hosted version:

openseo.so

## Why use OpenSEO?

* Best in class MCP and AI Skills.
* Modern, simple UI.Focused workflows instead of a bloated, complex SEO suite.
* Focused workflows instead of a bloated, complex SEO suite.
* No subscriptions.Bring your own DataForSEO API key and pay only for what you use.
* Bring your own DataForSEO API key and pay only for what you use.
* Fork and vibe code your own custom tool.

## Main SEO Workflows

* Keyword researchFind topics worth targeting, estimate demand, and prioritize what to write next.
* Find topics worth targeting, estimate demand, and prioritize what to write next.
* Rank trackingMonitor keyword positions across desktop and mobile over time, with SERP feature detection.
* Monitor keyword positions across desktop and mobile over time, with SERP feature detection.
* Domain insightsUnderstand where your domain is gaining or losing visibility so you can focus on the pages that move revenue.
* Understand where your domain is gaining or losing visibility so you can focus on the pages that move revenue.
* BacklinksSee who links to your site, which pages attract links, and where links are newly won or lost.
* See who links to your site, which pages attract links, and where links are newly won or lost.
* Site AuditsCatch technical issues early so your site is easier for search engines to crawl and rank.
* Catch technical issues early so your site is easier for search engines to crawl and rank.
* AI brand visibilitySee how your brand appears in AI answers, including competitor mentions and source coverage.
* See how your brand appears in AI answers, including competitor mentions and source coverage.
* AI search prompt explorerTrack and explore the prompts people might use when they ask AI tools for recommendations in your market.
* Track and explore the prompts people might use when they ask AI tools for recommendations in your market.

## OpenSEO MCP

OpenSEO exposes an MCP server so AI agents can use your SEO data directly.

Connect Codex, Claude Code, Claude Desktop, or another MCP client to:

* Run keyword research
* Inspect SERPs
* Compare domains
* Review backlinks
* Work through SEO decisions from your editor or chat

In the app, openAI & MCPand copy your MCP server URL. Point your agent at whichever OpenSEO instance you use.

Hosted app:

codex mcp add openseo --url https://app.openseo.so/mcp
claude mcp add --transport http --scope user openseo https://app.openseo.so/mcp

Cloudflare self-hosted:

codex mcp add openseo --url https://your-openseo-domain.com/mcp
claude mcp add --transport http --scope user openseo https://your-openseo-domain.com/mcp

Local Docker:

codex mcp add openseo --url http://localhost:3001/mcp
claude mcp add --transport http --scope user openseo http://localhost:3001/mcp

Approve the OpenSEO login when your agent asks.

## OpenSEO Agent Skills

OpenSEO Agent Skills are reusable workflows for Codex and Claude Code. They guide your agent through SEO tasks and can use the OpenSEO MCP for live keyword, SERP, backlink, and domain data.

### Installation Options

Install withskills add:

npx skills add every-app/open-seo

Auto-accept each OpenSEO skill:

npx skills add every-app/open-seo --skill 
'
*
'

Install for Claude Code only:

npx skills add every-app/open-seo --skill 
'
*
'
 --agent claude-code

Install for OpenAI Codex only:

npx skills add every-app/open-seo --skill 
'
*
'
 --agent codex

You can also pick skills directly from the GitHub repo and copy them into your agent's skills folder:

git clone https://github.com/every-app/open-seo.git

#
 Codex

mkdir -p 
~
/.codex/skills
cp -R open-seo/.agents/skills/
*
 
~
/.codex/skills/

#
 Claude Code

mkdir -p 
~
/.claude/skills
cp -R open-seo/.agents/skills/
*
 
~
/.claude/skills/

Start with/seo-project-setup. It will ask about your project and help configure your workspace.

### Available Skills

* seo-project-setup
* seo-coach
* keyword-research
* keyword-clustering
* competitive-landscape
* competitor-analysis
* link-prospecting

## Roadmap

Top priorities:

* Google Search Console Integration + MCP
* Local SEO
* Custom Reports for Clients
* Improved and Scheduled Site Audits
* In App AI Agent
* Support Multiple Projects

Our top priority is always refining the current product and making existing features better based on user feedback.

If something important is missing, please join theDiscordor email me atben@openseo.soand request it.

## Community

Email me:ben@openseo.so

Join Discord to chat:Discord

Follow along for updates:

* Sign up for the mailing list on our website:openseo.so
* Follow on X:https://x.com/bensenescu

## Pricing / Costs

OpenSEO is totally free to use. It works by using DataForSEO's APIs, which is a paid third-party service unaffiliated with OpenSEO.

There are two separate things:

1. OpenSEO app cost: $0, you host it yourself.
2. DataForSEO API: pay-as-you-go based on usage.

For cost estimates, seeDataForSEO API Cost Reference.

## DataForSEO API Key Setup

OpenSEO uses DataForSEO to fetch SEO data. You need an API key to connect OpenSEO to the service.

Backlinks requires one more step beyond the API key: you also need DataForSEO Backlinks enabled on your account (trial or paid subscription), then confirm access from the Backlinks page in OpenSEO.

1. Go toDataForSEO API Access.
2. Request API credentials by email (API key by emailorAPI password by email).
3. Use your DataForSEO login + API password, then base64 encodelogin:password:

printf
 
'
%s
'
 
'
YOUR_LOGIN:YOUR_PASSWORD
'
 
|
 base64

1. Set this asDATAFORSEO_API_KEYin your environment file:

* Docker self-hosting:.env
* Cloudflare: Set it in the workers UI
* Local development:.env.local

## Google Search Console

Search Console is optional and works in self-hosted deployments using your own
Google OAuth client. It takes ~10 minutes of one-time setup — seedocs/SELF_HOSTING_GOOGLE_SEARCH_CONSOLE.md.

## Self-hosting

OpenSEO supports two self-hosting paths:

* Docker for personal use and testing (Recommended for local use).
* Cloudflare for internet-facing self-hosting across multiple devices or for your team.

Docker

Docker is recommended for getting started. It's super easy to get up and running once you install Docker.

Cloudflare

If you love OpenSEO and want to use it across multiple devices or with your team, you can host it on Cloudflare which we'll be a SaaS-like experience. Also, this will have automatic database backups and other nice convenience features. It's just a bit more effort to get started if you're unfamiliar with Cloudflare.

## Docker Self Hosting

Warning

By default, the Docker version is intended for local use only. It runs in single-user mode with no authentication. For internet-facing self-hosting, use Cloudflare (free plan compatible). Or readdocs/SELF_HOSTING_DOCKER.mdbefore exposing to the internet.

Prerequisites:

* Install Docker:https://www.docker.com/products/docker-desktop/

Quickstart:

1. cp .env.example .env
2. SetDATAFORSEO_API_KEYin.env
3. docker compose up -d
4. Openhttp://localhost:<PORT>(default3001)

By default,compose.yamlpulls the published image from GHCR:

* ghcr.io/every-app/open-seo:latest

To update to the newest published image, pull first and then restart:

docker compose pull
docker compose up -d

Or use a single command:

docker compose up -d --pull always

For more info, seedocs/SELF_HOSTING_DOCKER.md.

## Cloudflare Self-Hosting

### Deploy the Worker

Clicking this button opens a page to deploy OpenSEO in your Cloudflare account. If you do not have an account yet, it will take you to account creation first (OpenSEO works great on the free plan).

Reference these docs while deploying since the Cloudflare UI doesn't indicate what steps you need to take:docs/SELF_HOSTING_CLOUDFLARE.md.

## Local Development

Seedocs/LOCAL_DEVELOPMENT.md.

## Contributing

Contributions are very welcome.

* Open an issue for bugs, UX friction, or feature requests.
* Open a PR if you want to implement a feature directly.
* Community-driven improvements are prioritized, and high-quality PRs are encouraged.

If you want to contribute but are unsure where to start, open an issue and describe what you want to build.

## SEO API Cost Reference

Use this section to estimate DataForSEO spend per request type. OpenSEO itself remains free; these are API usage costs only.

As of February 26, 2026, DataForSEO’s public docs/pricing pages say:

* New accounts include$1 free creditto test the API.
* The minimum top-up/payment is$50.

That means you can try OpenSEO for free with the starter credit, then decide if/when to top up.

### Pricing sources

* DataForSEO SERP API pricing:https://dataforseo.com/apis/serp-api/pricing
* DataForSEO Keywords Data API pricing:https://dataforseo.com/pricing/dataforseo-labs/dataforseo-google-api
* DataForSEO Backlinks pricing:https://dataforseo.com/pricing/backlinks/backlinks
* DataForSEO Lighthouse API docs:https://docs.dataforseo.com/v3/on_page/lighthouse/overview/

### 1) Rank tracking

There are in-app estimates for this since its dependent on the settings you select.

$2/month example:

* 50 keywords
* 1 device (Mobile or Desktop)
* Search 5 pages deep.

Searching ten pages deep costs 8x more than one page. Tracking both devices costs 2x more.

### 2) Site audit

* $0.01 per 20 pages audited with Lighthouse

### 3) Keyword research (relatedmode)

* Current billed cost pattern (from account usage logs):0.02 + (0.0001 x returned_keywords)USD
* 0.02 + (0.0001 x returned_keywords)USD
* Default app setting:150results per search ($0.035each).
* Available result tiers:150 results =$0.035300 results =$0.05500 results =$0.07
* 150 results =$0.035
* 300 results =$0.05
* 500 results =$0.07

### 4) Domain overview

* Standard domain overview request (with top 200 ranked keywords):$0.0401per domain.
* General formula if needed:0.0201 + (0.0001 x ranked_keywords_returned)USD
* 0.0201 + (0.0001 x ranked_keywords_returned)USD

### 5) Backlinks search

Note

There is a 2 week free trial, but then DataForSEO requires a $100/month commitment for this API. You can access this data for just $20/month throughopenseo.so. Soon, we'll let you use an OpenSEO API key so that you can call our API from your self hosted instance.

* Backlinks search costs about$0.06for a domain or$0.04for a page.
* Opening extra tabs likeReferring DomainsorTop Pagesadds about+$0.02each.
* Exact cost can vary slightly based on returned rows and DataForSEO pricing.

### 6) AI Search — Brand Lookup

* One lookup = 6 DataForSEO AI Optimization calls (aggregated_metrics+top_pages+mentions_searchacross ChatGPT and Google AI Overview): up to about$0.85per lookup.aggregated_metrics:$0.101per platform.top_pages: page-ranked cited sources per platform.mentions_search: row-priced;$0.20per platform at the app's full 100-row sample (lower-volume brands return fewer rows and cost less).
* aggregated_metrics:$0.101per platform.
* top_pages: page-ranked cited sources per platform.
* mentions_search: row-priced;$0.20per platform at the app's full 100-row sample (lower-volume brands return fewer rows and cost less).
* Adding competitors (Share of Voice) adds 2cross_aggregated_metricscalls: about$0.10each,$0.20total.
* Results are cached for 24 hours, so repeating the same lookup (same target + competitor set) is free within a day.
* Re-measure anytime withpnpm billing:brand-lookup --target=example.com --competitors=a.com,b.com --confirmLive=true.

### Planning examples

* 100 keyword research requests at the default 150 results:$3.50
* 100 keyword research requests at 500 results each:$7.00
* 100 domain overviews (200 ranked keywords each):$4.01
* 100 backlinks domain searches at current defaults before opening extra tabs: about$6.34
* 100 backlinks page searches at current defaults before opening extra tabs: about$4.30
* 100 fully explored backlinks domain searches: about$10.94
* 100 fully explored backlinks page searches: about$8.61

## About

Open source alternative to Semrush and Ahrefs

openseo.so

### Topics

 mcp

 seo

 site-audit

 seo-tools

 keyword-research

 backlink-analysis

 google-search-console-mcp

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2.4k

 stars
 

### Watchers

18

 watching
 

### Forks

292

 forks
 

 Report repository

 

## Releases20

v0.0.21

 Latest

 

Jun 24, 2026

 

+ 19 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript97.7%
* Other2.3%