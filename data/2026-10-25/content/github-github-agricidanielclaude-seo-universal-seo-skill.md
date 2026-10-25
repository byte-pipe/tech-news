---
title: 'GitHub - AgriciDaniel/claude-seo: Universal SEO skill for Claude Code. 26 sub-skills + 19 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, agent readiness (Lighthouse Agentic Browsing, WebMCP, llms.txt), backlinks, local SEO, e-commerce, international SEO, Google APIs, and PDF/Excel reporting. 9 optional extensions for live SEO data. · GitHub'
url: https://github.com/AgriciDaniel/claude-seo
site_name: github
content_file: github-github-agricidanielclaude-seo-universal-seo-skill
fetched_at: '2026-10-25T14:48:47.328956'
original_url: https://github.com/AgriciDaniel/claude-seo
author: AgriciDaniel
description: Universal SEO skill for Claude Code. 26 sub-skills + 19 sub-agents covering technical SEO, E-E-A-T, schema, GEO/AEO, agent readiness (Lighthouse Agentic Browsing, WebMCP, llms.txt), backlinks, local SEO, e-commerce, international SEO, Google APIs, and PDF/Excel reporting. 9 optional extensions for live SEO data. - AgriciDaniel/claude-seo
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

412 Commits
412 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude-plugin
.claude-plugin
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
agents
agents
 
 
assets
assets
 
 
data
data
 
 
docs
docs
 
 
extensions
extensions
 
 
hooks
hooks
 
 
schema
schema
 
 
screenshots
screenshots
 
 
scripts
scripts
 
 
skills
skills
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CITATION.cff
CITATION.cff
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
CONTRIBUTORS.md
CONTRIBUTORS.md
 
 
LICENSE
LICENSE
 
 
PRIVACY.md
PRIVACY.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
install.ps1
install.ps1
 
 
install.sh
install.sh
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
uninstall.ps1
uninstall.ps1
 
 
uninstall.sh
uninstall.sh
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# Claude SEO

Free, open-source SEO audits insideClaude Code.Rank higher in Google and get cited by AI search.

Install·Demo·Results·Team·Commands·Pricing·FAQ

Claude SEO is a free SEO plugin for Claude Code.Give it any website and it runs a full SEO audit in 10 to 15 minutes, then hands you a clear action plan, sorted by what matters most.

It checks everything a good SEO consultant would:

* Technical SEO.Crawlability, indexing, sitemaps, robots.txt, redirects, page speed and Core Web Vitals.
* Content quality.E-E-A-T (experience, expertise, authority and trust), thin pages and topic coverage.
* Structured data.Finds, validates and writes Schema.org markup for rich results.
* AI search (GEO).How likely Google AI Overviews, AI Mode, ChatGPT, Perplexity and Gemini are to cite your pages.
* Local and e-commerce SEO.Google Business Profile, reviews, map pack, product pages and international sites.

Claude SEO is built from 26 sub-skills and 19 specialist agents, and up to 17 agents work on your site at the same time. Every recommendation explains why it matters and how you will know it worked.

## See it in action

Type/seoin Claude Code to see every command:

Run a full audit and watch the agents fan out across the site:

Watch the full demo on YouTube

## Real results

The project's own site,claude-seo.md, audited with Claude SEO from day one: 10.8K Search Console clicks in its first 12 weeks and a 99 mobile PageSpeed score.

## Meet the team

All 19 agents

Agent

Role

Model

Command

seo-technical

Technical SEO Lead

Sonnet

/seo technical

seo-content

Content Editor

Opus

/seo content

seo-schema

Structured Data Engineer

Sonnet

/seo schema

seo-sitemap

Sitemap Architect

Sonnet

/seo sitemap

seo-performance

Performance Engineer

Sonnet

/seo audit

seo-visual

Visual QA

Sonnet

/seo audit

seo-geo

AI Search Analyst

Opus

/seo geo

seo-agentic

Agent Readiness Analyst

Sonnet

/seo agentic

seo-local

Local SEO Specialist

Sonnet

/seo local

seo-maps

Maps Analyst

Sonnet

/seo maps

seo-google

Google Data Analyst

Sonnet

/seo google

seo-backlinks

Link Analyst

Sonnet

/seo backlinks

Live data (extension)

Live Data Analyst

Sonnet

/seo audit

seo-image-gen

Image Producer (extension)

Sonnet

/seo image-gen

seo-cluster

Topic Strategist

Opus

/seo cluster

seo-sxo

Search Experience Designer

Opus

/seo sxo

seo-drift

Change Monitor

Opus

/seo drift

seo-ecommerce

E-commerce Specialist

Sonnet

/seo ecommerce

seo-flow

FLOW Strategist

Sonnet

/seo flow

Built for:

* SEO agenciesthat want weekly audits for every client instead of quarterly ones, with change monitoring to catch problems in between.
* In-house SEO teamsat SaaS, publishing and e-commerce companies that want a second pair of eyes before every review, AI search included.
* Freelance SEO consultantswho want to run an audit on the first call and show a real score and the top fixes before writing a proposal.

## Commands

30 core and extension commands in six groups. Open one to see what is inside; a few more extension commands are in thefull command reference.

Audits and Planning
 (5 commands)

* /seo setup: Create or refresh the isolated Python runtime and Chromium
* /seo doctor: Check runtime readiness without changing the system
* /seo audit <url>: Full website audit with parallel agents
* /seo page <url>: Deep single-page analysis
* /seo plan <type>: Strategic SEO planning (saas, local, ecommerce, publisher, agency)

Technical SEO
 (7 commands)

* /seo technical <url>: Technical SEO audit across 9 categories
* /seo sitemap <url | generate>: Analyze or generate XML sitemaps
* /seo images <url>: Image optimization analysis
* /seo hreflang <url>: Hreflang and i18n SEO audit and generation
* /seo programmatic <url>: Programmatic SEO analysis and planning
* /seo google [command]: Google SEO APIs: GSC, PageSpeed, CrUX, Indexing, GA4, PDF reports
* /seo drift baseline | compare | history <url>: SEO drift monitoring with SQLite snapshots

Content and E-E-A-T
 (6 commands)

* /seo content <url>: E-E-A-T and content quality analysis
* /seo content-brief <topic>: Content brief: target keywords, outline, internal links
* /seo cluster <keyword>: SERP-based semantic clustering
* /seo sxo <url>: Search Experience Optimization: page type, user stories, personas
* /seo flow [stage]: FLOW framework prompts (CC BY 4.0, evidence-led)
* /seo competitor-pages <url>: Competitor comparison page generation

Schema and AI Search
 (3 commands)

* /seo schema <url>: Detect, validate and generate Schema.org markup
* /seo geo <url>: AI Overviews and Generative Engine Optimization
* /seo agentic <url>: Agent readiness: Lighthouse Agentic Browsing X/N, AI agent access, llms.txt, Markdown, WebMCP

Local, Links, Commerce
 (4 commands)

* /seo local <url>: Local SEO: GBP, citations, reviews, map pack
* /seo maps [command]: Maps intelligence: geo-grid, GBP audit, reviews, competitors
* /seo backlinks <url>: Backlink profile analysis (Moz, Bing, Common Crawl)
* /seo ecommerce <url>: E-commerce SEO and marketplace intelligence

Extensions
 (5 commands)

* /seo image-gen [use-case]: AI image generation for SEO assets
* /seo seranking [command]: AI Share-of-Voice across ChatGPT, Gemini, Perplexity, AI Overviews, AI Mode
* /seo profound [command]: LLM citation tracking with time-series data
* /seo bing [command] <url>: Bing Webmaster Tools + IndexNow URL submission
* /seo unlighthouse <url>: Multi-page Lighthouse runner, runs locally

## Pricing

The full comparison

Doing it by hand

Hiring an agency

SEO audit software

Claude SEO

Time per audit

4 to 8 hours

1 to 3 weeks

10 to 45 minutes

10 to 15 minutes

Cost

Billable hours

$2k to $15k+ per project

$99 to $999 a month

Free, with your Claude Code plan

Consistent checks

Depends on who does it

Depends on the team

Yes

Same checklist every time

What you get

A spreadsheet or PDF

A slide deck

A dashboard and CSV exports

Markdown, PDF and JSON files you keep

Your data stays with you

Yes

No

No

Yes, it runs on your machine

Covers AI search

Depends

Depends

Often months behind

Yes, follows Google's latest guidance

Each fix comes with a way to check it worked

Sometimes

Sometimes

Rarely

Yes

Typical market prices, for illustration. Your numbers may differ.

## How an audit works

1. It learns your site.Claude SEO detects the type of business (SaaS, local, e-commerce, publisher or agency) and adjusts its checks.
2. The team fans out.Up to 17 specialist agents audit the site in parallel: technical, content, schema, speed, AI search and more.
3. You get a plan, not a pile of warnings.Findings are scored and sorted into a prioritized action plan. Each recommendation says what it is based on, what it depends on and how you will know it worked.

Reports are saved as Markdown, and/seo google reportturns them into a polished PDF.

See a real report
: the start of a schema audit

# 
Schema Markup Report: rankenstein.pro/about

|
 Metric 
|
 Value 
|

|
---------------------
|
---------------------------------------------
|

|
 JSON-LD Blocks 
|
 3 
|

|
 Schema Types 
|
 Organization, WebSite, SoftwareApplication 
|

|
 Critical Issues 
|
 2 
|

|
 Warnings 
|
 5 
|

|
 Passed Checks 
|
 18 
|

|
 Overall Grade 
|
 B+ (solid foundation, actionable gaps) 
|

**
Critical Issue:
**
 The 
`
founder
`
 property only includes Daniel Agrici.
Benjamin Samar (Co-Founder and Technical Director) is displayed on the page
but absent from the schema. This content-schema mismatch can confuse search engines.

Want the details? Read themethodologyand thearchitecture.

## Install

You needClaude Code1.0.33 or newer. Run these three commands inside it:

/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
/seo setup

/seo setupprepares everything Claude SEO needs (its own Python environment and a headless browser) without touching the rest of your system. Run/seo doctorany time to check it.

Manual install: macOS and Linux

git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/install.sh

One-liner (curl, review then run):

curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh 
>
 install.sh
cat install.sh 
#
 review before running

bash install.sh
rm install.sh

Manual install: Windows (PowerShell)

git clone 
--
depth 
1
 https:
//
github.com
/
AgriciDaniel
/
claude
-
seo.git
powershell 
-
ExecutionPolicy Bypass 
-
File claude
-
seo\install.ps1

Whygit cloneinstead ofirm | iex?Claude Code's own security guardrails flagirm ... | iexas a supply chain risk: downloading and executing remote code without verification. Thegit cloneapproach lets you inspectclaude-seo\install.ps1before running it.

Two versions.This public version is MIT licensed and free for everyone.AI Marketing Hub Promembers also get a private version with early access to new features. Members install it with:

/plugin marketplace add AI-Marketing-Hub/claude-seo
/plugin install claude-seo@ai-marketing-hub-claude-seo
/seo setup

Your first audit:

claude 
#
 start Claude Code

/seo audit https://example.com 
#
 full site audit with a prioritized plan

/seo page https://example.com/pricing 
#
 one page, in depth

/seo geo https://example.com 
#
 how ready you are for AI search

/seo schema https://example.com 
#
 check and generate structured data

/seo 
local
 https://example.com 
#
 local SEO and Google Business Profile

## FAQ

What is Claude SEO?

A free, open-source SEO audit tool that runs inside Claude Code. It checks technical SEO, Core Web Vitals, content quality, Schema.org structured data, AI search readiness, local SEO, e-commerce and international SEO, then gives you a prioritized action plan. It follows Google's own documentation, including theAI Optimization Guide.

Is it really free?

Yes. It is MIT licensed, with no per-site pricing, no usage limits and no tracking. You only need Claude Code. A few optional extensions connect to paid services where you bring your own account, but everything works without them.

Do I need API keys?

No. Claude SEO works out of the box. If you want real field data, you can connect free Google APIs (PageSpeed Insights, Chrome UX Report, Search Console and Google Analytics 4) with/seo google setup. Your keys stay on your machine.

How does it help with AI search like Google AI Overviews and ChatGPT?

Google says optimizing for AI search is still SEO, so Claude SEO starts with the basics that AI answers rely on: being indexed, fast and clear. Then/seo geoscores how easy your pages are to quote, checks that AI crawlers can reach them and looks at your brand's presence on Wikipedia, Reddit, YouTube and LinkedIn./seo agenticchecks how well AI agents can use your site.

Does it work on JavaScript sites like Next.js, React or Vue?

Yes. When a page needs JavaScript to show its content, Claude SEO opens it in a headless browser automatically, so single-page apps are audited as visitors see them.

How is it different from Screaming Frog or other SEO tools?

Crawlers like Screaming Frog crawl faster and deeper, and big SEO suites have their own backlink databases. Claude SEO does something else: it explains what it finds, sorts it by impact, covers AI search in depth and lets you ask follow-up questions in plain English. Many people use both.

Does my data leave my computer?

Claude SEO runs inside Claude Code, so the pages and data it analyzes are sent to Claude, Anthropic's model, the same as anything else you work on in Claude Code. Reports are saved as files on your machine. No SEO service or other third party sees your data unless you connect an extension or API yourself. Besides the site you audit, some checks read public sources such as Wikipedia, Reddit and Common Crawl. SeePRIVACY.mdfor the full list.

Good to know: requirements, limits and uninstall

Requirements.Claude Code 1.0.33 or newer and Python 3.11 to 3.14./seo setupinstalls the headless browser for you.

Cost of a full audit.Five agents that need more judgment run on Opus and the rest on Sonnet, so a full/seo audituses more of your Claude plan than a single-page check. You can change any agent's model in its file underagents/.

Limits.Without Google API keys, Core Web Vitals are lab estimates and indexing is inferred from the page. Pages that load key content only after scrolling or clicking can give noisy results.

Uninstall.Installed as a plugin:/plugin uninstall claude-seo@agricidaniel-claude-seo. Installed manually:

git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/uninstall.sh

## Extensions

Optional add-ons that bring in more data. Claude SEO works fully without them.

* Banana:AI images for SEO, from social previews to blog heroes (Claude Banana)
* SE Ranking:your share of voice in ChatGPT, Gemini, Perplexity and Google AI answers
* Profound:tracks when AI models cite your site
* Bing Webmaster:Bing data plus instant IndexNow submission
* Unlighthouse:Lighthouse scores for every page of your site

Setup guides live inextensions/.

## Star history

## More from the same family

Project

What it does

Claude Blog

Writes and optimizes blog posts from your SEO findings

Claude Banana

AI image generation for SEO assets and posts

ChatGPT SEO

Turns a page, draft or SEO export into a sourced fix plan inside ChatGPT

FLOW

An evidence-led SEO framework with 42 AI prompts

AI Marketing Claude

Community suite for copy, email, ads and funnels

Docs:Installation·Commands·Architecture·Troubleshooting·Extensions setup·Security·Privacy·Contributors

## License and contributing

MIT License, seeLICENSE. Contributions are welcome: readCONTRIBUTING.mdfirst and mention the checks you ran in your pull request.

## Author

Built byAgrici Daniel, AI Workflow Architect, with help from theAI Marketing Hub Procommunity.