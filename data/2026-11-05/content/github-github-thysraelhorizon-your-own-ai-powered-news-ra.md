---
title: 'GitHub - Thysrael/Horizon: 📡 Your own AI-powered news radar. Generates daily briefings in English & Chinese. | 用 AI 构建你专属的新闻雷达 · GitHub'
url: https://github.com/Thysrael/Horizon
site_name: github
content_file: github-github-thysraelhorizon-your-own-ai-powered-news-ra
fetched_at: '2026-11-05T15:23:37.175383'
original_url: https://github.com/Thysrael/Horizon
author: Thysrael
description: 📡 Your own AI-powered news radar. Generates daily briefings in English & Chinese. | 用 AI 构建你专属的新闻雷达 - Thysrael/Horizon
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

301 Commits
301 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
data
data
 
 
docs
docs
 
 
profiles
profiles
 
 
scripts
scripts
 
 
skills/
horizon
skills/
horizon
 
 
src
src
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README_ja.md
README_ja.md
 
 
README_zh.md
README_zh.md
 
 
SECURITY.md
SECURITY.md
 
 
docker-compose.yml
docker-compose.yml
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# 🌅 Horizon

Enjoy the News itself. Leave others to Horizon

📡 Your own AI-powered news radar. Generates daily briefings in English & Chinese. | 构建你专属的 AI 新闻雷达

📖 Live Demo·📋 Configuration Guide·💬 QQ Group·简体中文·日本語

## Screenshots

Ranked Daily Briefing

Context, Summary & Discussion

More Screenshots

Terminal Output

Feishu Notification

Email Delivery

WeChat Delivery

## Why Horizon?

Good reads are scattered across feeds, forums, and timelines. Your attention isn't unlimited. Horizon collects, filters, and deduplicates them, then brings the worthwhile ones to you with context and community discussion.

Your taste shapes what you read—and what you want from it. A news story calls for “why it matters”; an engineering deep dive calls for “what I can use.” Horizon'sprofilesgive each kind of content its own scoring criteria and output, for a briefing that feels handpicked.

## Features

* 📡 Bring Your Sources Together— Follow RSS, Hacker News, Reddit, Telegram, X, GitHub, financial news, and more.
* 🎯 Decide What's Worth Reading— Define scoring rubrics with profiles, set individual thresholds, and merge repeated stories within each profile.
* 🧩 Give Every Read the Right Treatment— Choose summaries, context, solutions, or takeaways with Markdown prompts and JSON block definitions.
* 💬 Go Beyond the Headline— Add web-researched background and community discussion where they help explain the story.
* ⚖️ Make Room for All Your Interests— Cap the briefing's length and each category's share so one busy topic doesn't crowd out the rest.
* 📬 Read Where You Already Are— Generate English and Chinese briefings as Markdown, publish to Pages, or deliver by email and webhook.

### One Briefing, Different Ways to Read

A profile is a reusable set of editorial rules:what belongs, what's worth keeping, and what to write.Built-in examples:

What you follow

Profile

What you get

Technology news

tech-news

Events and context, with impact and community discussion when useful

Engineering deep dives

tech-blog

Background, solution, and practical takeaways

AI creator material

ai-creator

A summary, with timely hooks and content angles when useful

Assign a profile to a source, or let AI choose. Want a different take? Adapt an existing profile—usually without changing Python.Make a profile your own →

## How It Works

Editable OmniGraffle source

Profiles define the treatment; runtime settings reflect your reading preferences.Each item routes to one profile. Analysis, filtering, and deduplication happen before enrichment, then the selected items become a briefing grouped by profile.

Run the full pipeline through the CLI, or let an AI assistant call its stages throughMCP.

## Agent Skill

Let your AI assistant configure sources, customize Profiles, and run Horizon:

npx skills add Thysrael/Horizon --skill horizon -g

Setup and usage·Download Skill ZIP

The command requires Node.js 22.20+. Then ask your assistant to install and configure Horizon, or follow the Quick Start below.

## Quick Start

### 1. Install

Option A: Local Installation

git clone https://github.com/Thysrael/Horizon.git

cd
 Horizon

#
 Install with uv (recommended)

uv sync

#
 Install test/development extras when needed

uv sync --extra dev

#
 Or with pip

pip install -e 
.

devis currently defined as an optional extra inpyproject.toml, so useuv sync --extra devfor pytest and other development dependencies.

If you want the optional OpenBB financial-news source, install its extra too:

uv sync --extra openbb

Ifopenbbpulls packages without wheels on your machine, install the SDK manually with binaries only:

uv pip install --only-binary=:all: openbb openbb-benzinga

Option B: Docker

git clone https://github.com/Thysrael/Horizon.git

cd
 Horizon

#
 Optional: build with comma-separated extras before the first run

docker compose build --build-arg EXTRAS=openbb horizon

Full-text extraction withtrafilaturais included in the base install. Thetwitterextra also requires a Playwright browser and system packages, which the current Dockerfile does not install.

### 2. Configure

Option A: Interactive wizard (recommended)

uv run horizon-wizard

The wizard asks about your interests (e.g. "LLM inference", "嵌入式", "web security") and auto-generatesdata/config.json. SeeInteractive Wizardfor CLI options.

Eligible ChatGPT subscribers can chooseopenai-chatgptto use their plan throughSign in with ChatGPT, without an OpenAI API key.

Option B: Manual configuration

cp .env.example .env 
#
 Add your API keys

cp data/config.example.json data/config.json 
#
 Customize your sources

Minimal manual configuration:

An explicit sourceprofileuses that profile directly. Omit it or set it to"auto"to let AI match the item against all available profiles. Set it to an
array such as["tech-news", "finance-news"]to restrict AI matching to those
profiles. SeeProcessing Profilesfor profile structure and behavior.
Per-profile user preferences such as score thresholds and topic deduplication
belong inprocessing.profile_settings, not in the profile files.

Balanced digest (optional)

Limit the final digest size and prevent one category from dominating the
results. Categories come from source configuration such assources.rss[].category.

Group limits are applied after profile filtering and before enrichment. Ifcategory_groups,max_items, anddefault_group_limitare omitted, no balanced
digest limits apply.

api_key_envmust be the name of an environment variable, not the API key
itself. Put the real secret in.env:

OPENAI_API_KEY=sk-your-key

For Gemini, useGOOGLE_API_KEY:

Any string value indata/config.jsoncan reference environment variables with${VAR_NAME}. This is useful for values such asai.base_url, private RSS feed URLs, webhook endpoints, or custom header templates.

For the full reference, see theConfiguration Guide.

### 3. Run

A. Local installation

uv run horizon [OPTIONS]

B. Docker

docker compose run --rm horizon [OPTIONS]

Option

Default

Description

--hours N

24

Fetch from last N hours

-d
, 
--data-dir PATH

data

Path to the data directory

-c
, 
--config PATH

<data-dir>/config.json

Path to config file

-l
, 
--log-level LEVEL

WARNING

Logging level (DEBUG/INFO/WARNING/ERROR/CRITICAL)

--data-dirchanges the state directory, including summaries, subscribers, and the default config location;--configchanges only the config file. The generated report is saved todata/summaries/(or<data-dir>/summaries/if--data-diris set). SeeConfiguration Pathsfor combining both flags and initializing a custom config location.

### 4. Automate (Optional)

Schedule Horizon withGitHub Actionsusing thedaily workflow template. The template is disabled in this repository; configure it for your deployment and rename it todaily-summary.ymlto enable it.

## Supported Sources

Source

What it fetches

Comments

Hacker News

Top stories by score

Yes (top N comments)

RSS / Atom

Any RSS or Atom feed

—

Reddit

Subreddits + user posts

Yes (top N comments)

Telegram

Public channel messages

—

Twitter / X

User timelines + keyword searches (Apify)

Yes (top N replies)

GitHub

User events & repo releases

—

OpenBB

Financial company news by watchlist/provider

—

OSS Insight

Trending open-source repositories

—

GDELT

News matching a search query

—

Google News

News search via RSS

—

## Where Your Briefing Goes

Horizon can publish or deliver the generated briefing in several ways:

Channel

What it does

GitHub Pages Daily Site

Copies generated Markdown into 
docs/
 so GitHub Pages can publish a daily-updated briefing site

Email Subscription

Sends the daily briefing to subscribers and handles subscribe/unsubscribe requests through SMTP/IMAP

Webhook Notification

Pushes success or failure results to Feishu/Lark, DingTalk, Slack, Discord, or any custom webhook endpoint

WeChat Notification

Sends briefings through iLink Bot after QR login and a message from you; WeChat reply limits apply

For delivery setup, see theConfiguration Guide. To run pipeline stages from an AI assistant, use theMCP Server:tools·client setup.

## Supported By

Horizon is an open-source project maintained in spare time. If you'd like to support the project or be listed here, feel free toopen an issueoremail me.

Supporter

Details

Thanks to Modelflare for sponsoring this project! Modelflare: Full strength, stable, nothing watered down. Global SOTA models at a lower cost. Operated by US-based Havenbyte LLC, Modelflare supports GPT, Claude, Gemini, Grok, and other leading models through common compatible protocols, plus 40+ image and video models.
Cache compensation is a highlight: selected OpenAI groups (price-first, stable, and premium) guarantee daily cache hit rates of 65%, 75%, or 85%, and if eligible requests fall short, Modelflare refunds the difference, visible on the usage dashboard after settlement.
Special offers: a single top-up of US$20 unlocks the GPT discount group at a 0.015x price multiplier, and a single top-up of US$50 unlocks the Claude discount group at a 0.03x multiplier. Register via 
this exclusive link
 to get started.

Compshare currently supports Horizon. Compshare is UCloud's AI cloud platform, offering cost-effective monthly and pay-as-you-go domestic model agent plans starting from RMB 49/month, as well as stable officially relayed overseas models. It supports Claude Code, Codex, and API usage, with enterprise-grade high concurrency, 24/7 technical support, and self-service invoicing.
Register through their 
link
 to receive a free RMB 5 trial credit.

OfoxAI is a unified AI API platform bringing together text, image, and video models from multiple providers. With OpenAI-compatible endpoints and native Anthropic and Gemini interfaces, developers can access models for AI applications, agents, and content creation through one platform.
Explore OfoxAI models and APIs →

AstraFlow

Thanks to AstraFlow for sponsoring Horizon! AstraFlow is UCloud's model platform, bringing together 200+ leading AI models and video generation models for text and video creation in one place. It offers per-key billing and detailed usage records.
Exclusive offer for Horizon users: 
claim RMB 50 in compute credits
 to try model APIs and content creation.

## Documentation

Guide

Description

Configuration

AI providers, sources, profiles, filtering, email, webhook, WeChat, GitHub Pages, and MCP setup

Processing Profiles

Profile routing, prompts, runtime filtering preferences, enrichment blocks, and tools

Scoring

How Horizon evaluates and ranks news items

Scrapers

Source scraper details and extension notes

Extractors

Full article extraction for RSS sources

MCP Tools

Tool reference for MCP-compatible clients

Agent Skill

Use an AI assistant to configure, run, customize, schedule, and extend Horizon

## Project Status

Horizon already supports the full daily briefing loop: multi-source collection, profile-driven analysis and enrichment, deduplication, comment summaries, bilingual generation, GitHub Pages publishing, email delivery, webhook delivery, WeChat delivery, Docker deployment, MCP integration, and the setup wizard.

Planned improvements:

* More source types, such as Discord
* Publish releases on GitHub
* Publish the package to PyPI forpip install

## Community

Join the Horizon user and developer QQ group to share sources, profiles, and deployment tips.

QQ group: 1106121909Scan with QQ or search the group number to join.

## Contributing

Contributions are welcome. SeeCONTRIBUTING.mdfor code, documentation, and source-sharing guidelines.

### Share Sources

Want to share valuable source discoveries with the Horizon community? Please submit them throughhorizon1123.top.

## Acknowledgements

* Special thanks toLINUX.DOfor providing a promotion platform.
* Special thanks toHelloGitHubfor valuable guidance and suggestions.
* Special thanks toAIGC Linkfor the promotions on XiaoHongShu.

## License

MIT