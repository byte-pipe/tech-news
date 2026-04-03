---
title: 'GitHub - sickn33/antigravity-awesome-skills: The Ultimate Collection of 1000+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel. · GitHub'
url: https://github.com/sickn33/antigravity-awesome-skills
site_name: github
content_file: github-github-sickn33antigravity-awesome-skills-the-ultim
fetched_at: '2026-03-16T11:23:16.565125'
original_url: https://github.com/sickn33/antigravity-awesome-skills
author: sickn33
description: The Ultimate Collection of 1000+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel. - sickn33/antigravity-awesome-skills
---

sickn33

 

/

antigravity-awesome-skills

Public

* NotificationsYou must be signed in to change notification settings
* Fork4.3k
* Star24.8k

 
 
 
 
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

1,035 Commits
1,035 Commits
.claude-plugin
.claude-plugin
 
 
.github
.github
 
 
apps/
web-app
apps/
web-app
 
 
assets
assets
 
 
data
data
 
 
docs
docs
 
 
docs_zh-CN
docs_zh-CN
 
 
skill_categorization
skill_categorization
 
 
skills
skills
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
CATALOG.md
CATALOG.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
START_APP.bat
START_APP.bat
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
skills_index.json
skills_index.json
 
 
walkthrough.md
walkthrough.md
 
 
View all files

## Repository files navigation

# 🌌 Antigravity Awesome Skills: 1,259+ Agentic Skills for Claude Code, Gemini CLI, Cursor, Copilot & More

The Ultimate Collection of 1,259+ Universal Agentic Skills for AI Coding Assistants — Claude Code, Gemini CLI, Codex CLI, Antigravity IDE, GitHub Copilot, Cursor, OpenCode, AdaL

Antigravity Awesome Skillsis a curated, battle-tested library of1,259+ high-performance agentic skillsdesigned to work seamlessly across the major AI coding assistants.

Current release: V7.9.1.This repository gives your agent reusable playbooks for planning, coding, debugging, testing, security review, infrastructure work, product thinking, and much more.

## Table of Contents

* 🚀 New Here? Start Here!
* 📖 Complete Usage Guide-Start here if confused after installation!
* 🔌 Compatibility & Invocation
* 🛠️ Installation
* 🛡️ Security Posture
* 🧯 Troubleshooting
* 🎁 Curated Collections (Bundles)
* 🧭 Antigravity Workflows
* 📦 Features & Categories
* 📚 Browse 1,259+ Skills
* 🤝 Contributing
* 💬 Community
* ☕ Support the Project
* 🏆 Credits & Sources
* 👥 Repo Contributors
* ⚖️ License
* 🌟 Star History

## New Here? Start Here!

Welcome to the current interactive web edition.This isn't just a list of scripts; it's a complete operating system for your AI agent.

### 1. 🐣 Context: What is this?

Antigravity Awesome Skills(Release 7.9.1) is a broad, production-oriented upgrade to your AI's capabilities.

AI Agents (like Claude Code, Cursor, or Gemini) are smart, but they lackspecific tools. They don't know your company's "Deployment Protocol" or the specific syntax for "AWS CloudFormation".Skillsare small markdown files that teach them how to do these specific tasks perfectly, every time.

### 2. ⚡️ Quick Start (1 minute)

Install once; then use Starter Packs indocs/users/bundles.mdto focus on your role.

1. Install:#Default: ~/.gemini/antigravity/skills (Antigravity global). Use --path for other locations.npx antigravity-awesome-skills
2. Verify:test-d~/.gemini/antigravity/skills&&echo"Skills installed in ~/.gemini/antigravity/skills"
3. Run your first skill:"Use@brainstormingto plan a SaaS MVP."
4. Pick a bundle:* Web Dev?start withWeb Wizard.
* Security?start withSecurity Engineer.
* General use?start withEssentials.

### 3. 🧠 How to use

Once installed, just ask your agent naturally:

"Use the@brainstormingskill to help me plan a SaaS."
"Run@lint-and-validateon this file."

👉NEW:Complete Usage Guide - Read This First!(answers: "What do I do after installation?", "How do I execute skills?", "What should prompts look like?")

👉Full Getting Started Guide

## Compatibility & Invocation

These skills follow the universalSKILL.mdformat and work with any AI coding assistant that supports agentic skills.

Tool

Type

Invocation Example

Path

Claude Code

CLI

>> /skill-name help me...

.claude/skills/

Gemini CLI

CLI

(User Prompt) Use skill-name...

.gemini/skills/

Codex CLI

CLI

(User Prompt) Use skill-name...

.codex/skills/

Kiro CLI

CLI

(Auto) Skills load on-demand

Global: 
~/.kiro/skills/
 · Workspace: 
.kiro/skills/

Kiro IDE

IDE

/skill-name or (Auto)

Global: 
~/.kiro/skills/
 · Workspace: 
.kiro/skills/

Antigravity

IDE

(Agent Mode) Use skill...

Global: 
~/.gemini/antigravity/skills/
 · Workspace: 
.agent/skills/

Cursor

IDE

@skill-name (in Chat)

.cursor/skills/

Copilot

Ext

(Paste content manually)

N/A

OpenCode

CLI

opencode run @skill-name

.agents/skills/

AdaL CLI

CLI

(Auto) Skills load on-demand

.adal/skills/

Tip

Default installer path:~/.gemini/antigravity/skills(Antigravity global). Use--path ~/.agent/skillsfor workspace-specific install. For manual clone,.agent/skills/works as workspace path for Antigravity.OpenCode Path Update: opencode path is changed to.agents/skillsfor global skills. SeePlace Filesdirective on OpenCode Docs.

Tip

Windows Users: use the standard install commands. The legacycore.symlinks=true/ Developer Mode workaround is no longer required for this repository.

## Installation

To use these skills withClaude Code,Gemini CLI,Codex CLI,Kiro CLI,Kiro IDE,Cursor,Antigravity,OpenCode, orAdaL:

### Option A: npx (recommended)

npx antigravity-awesome-skills

1. Verify the default install:

test
 -d 
~
/.gemini/antigravity/skills 
&&
 
echo
 
"
Skills installed
"

1. Use your first skill:

Use @brainstorming to plan a SaaS MVP.

1. Browse starter collections indocs/users/bundles.mdand execution playbooks indocs/users/workflows.md.

### Option B: Claude Code plugin marketplace

If you use Claude Code and prefer the plugin marketplace flow, this repository now ships a root.claude-plugin/marketplace.json:

/plugin marketplace add sickn33/antigravity-awesome-skills
/plugin install antigravity-awesome-skills

This installs the same repository-backed skill library through Claude Code's plugin marketplace entrypoint.

## Choose Your Tool

Tool

Install

First Use

Claude Code

npx antigravity-awesome-skills --claude
 or Claude plugin marketplace

>> /brainstorming help me plan a feature

Cursor

npx antigravity-awesome-skills --cursor

@brainstorming help me plan a feature

Gemini CLI

npx antigravity-awesome-skills --gemini

Use brainstorming to plan a feature

Codex CLI

npx antigravity-awesome-skills --codex

Use brainstorming to plan a feature

Antigravity

npx antigravity-awesome-skills --antigravity

Use @brainstorming to plan a feature

Kiro CLI

npx antigravity-awesome-skills --kiro

Use brainstorming to plan a feature

Kiro IDE

npx antigravity-awesome-skills --path ~/.kiro/skills

Use @brainstorming to plan a feature

GitHub Copilot

No installer — paste skills or rules manually

Ask Copilot to use brainstorming to plan a feature

OpenCode

npx antigravity-awesome-skills --path .agents/skills

opencode run @brainstorming help me plan a feature

AdaL CLI

npx antigravity-awesome-skills --path .adal/skills

Use brainstorming to plan a feature

Custom path

npx antigravity-awesome-skills --path ./my-skills

Depends on your tool

## Security Posture

These skills are continuously reviewed and hardened, but the collection is not "safe by default". They are instructions and examples that can include risky operations by design.

* Runtime hardening now protects the/api/refresh-skillsmutation flow (method/host checks and optional token gate) before any repo mutation.
* Markdown rendering in the web app avoids raw HTML passthrough (rehype-raw) and follows safer defaults for skill content display.
* A repo-wideSKILL.mdsecurity scan checks for high-risk command patterns (for examplecurl|bash,wget|sh,irm|iex, command-line token examples) with explicit allowlisting for deliberate exceptions.
* Maintainer-facing tooling has additional path/symlink checks and parser robustness guards for safer sync, index, and install operations.
* Security test coverage for endpoint authorization, rendering safety, and doc-risk patterns is part of the normal CI/release validation flow.

## What This Repo Includes

* Skills library:skills/contains the reusableSKILL.mdcollection.
* Installer: the npm CLI installs skills into the right directory for each tool.
* Catalog:CATALOG.md,skills_index.json, anddata/provide generated indexes.
* Web app:apps/web-appgives you search, filters, rendering, and copy helpers.
* Bundles:docs/users/bundles.mdgroups starter skills by role.
* Workflows:docs/users/workflows.mdgives step-by-step execution playbooks.

## Project Structure

Path

Purpose

skills/

The canonical skill library

docs/users/

Getting started, usage, bundles, workflows, visual guides

docs/contributors/

Templates, anatomy, examples, quality bar, community docs

docs/maintainers/

Release, audit, CI drift, metadata maintenance docs

docs/sources/

Attribution and licensing references

apps/web-app/

Interactive browser for the skill catalog

tools/

Installer, validators, generators, and support scripts

data/

Generated catalog, aliases, bundles, and workflows

## Top Starter Skills

* @brainstormingfor planning before implementation.
* @architecturefor system and component design.
* @test-driven-developmentfor TDD-oriented work.
* @doc-coauthoringfor structured documentation writing.
* @lint-and-validatefor lightweight quality checks.
* @create-prfor packaging work into a clean pull request.
* @debugging-strategiesfor systematic troubleshooting.
* @api-design-principlesfor API shape and consistency.
* @frontend-designfor UI and interaction quality.
* @security-auditorfor security-focused reviews.

## Three Real Examples

Use @brainstorming to turn this product idea into a concrete MVP plan.

Use @security-auditor to review this API endpoint for auth and validation risks.

## Curated Collections

Bundlesare curated groups of skills for a specific role or goal (for example:Web Wizard,Security Engineer,OSS Maintainer).

They help you avoid picking through the full catalog one by one.

### ⚠️Important: Bundles Are NOT Separate Installations!

Common confusion:"Do I need to install each bundle separately?"

Answer: NO!Here's what bundles actually are:

What bundles ARE:

* ✅ Recommended skill lists organized by role
* ✅ Curated starting points to help you decide what to use
* ✅ Time-saving shortcuts for discovering relevant skills

What bundles are NOT:

* ❌ Separate installations or downloads
* ❌ Different git commands
* ❌ Something you need to "activate"

### How to use bundles:

1. Install the repository once(you already have all skills)
2. Browse bundlesindocs/users/bundles.mdto find your role
3. Pick 3-5 skillsfrom that bundle to start using in your prompts
4. Reference them in your conversationswith your AI (e.g., "Use @brainstorming...")

For detailed examples of how to actually use skills, see theUsage Guide.

### Examples:

* Building a SaaS MVP:Essentials+Full-Stack Developer+QA & Testing.
* Hardening production:Security Developer+DevOps & Cloud+Observability & Monitoring.
* Shipping OSS changes:Essentials+OSS Maintainer.

## Antigravity Workflows

Bundles help you choose skills. Workflows help you execute them in order.

* Use bundles when you need curated recommendations by role.
* Use workflows when you need step-by-step execution for a concrete goal.

Start here:

* docs/users/workflows.md: human-readable playbooks.
* data/workflows.json: machine-readable workflow metadata.

Initial workflows include:

* Ship a SaaS MVP
* Security Audit for a Web App
* Build an AI Agent System
* QA and Browser Automation (with optional@go-playwrightsupport for Go stacks)
* Design a DDD Core Domain

## Features & Categories

The repository is organized into specialized domains to transform your AI into an expert across the entire software development lifecycle:

Category

Focus

Example skills

Architecture

System design, ADRs, C4, and scalable patterns

architecture
, 
c4-context
, 
senior-architect

Business

Growth, pricing, CRO, SEO, and go-to-market

copywriting
, 
pricing-strategy
, 
seo-audit

Data & AI

LLM apps, RAG, agents, observability, analytics

rag-engineer
, 
prompt-engineer
, 
langgraph

Development

Language mastery, framework patterns, code quality

typescript-expert
, 
python-patterns
, 
react-patterns

General

Planning, docs, product ops, writing, guidelines

brainstorming
, 
doc-coauthoring
, 
writing-plans

Infrastructure

DevOps, cloud, serverless, deployment, CI/CD

docker-expert
, 
aws-serverless
, 
vercel-deployment

Security

AppSec, pentesting, vuln analysis, compliance

api-security-best-practices
, 
sql-injection-testing
, 
vulnerability-scanner

Testing

TDD, test design, fixes, QA workflows

test-driven-development
, 
testing-patterns
, 
test-fixing

Workflow

Automation, orchestration, jobs, agents

workflow-automation
, 
inngest
, 
trigger-dev

Counts change as new skills are added. For the current full registry, seeCATALOG.md.

## Browse 1,259+ Skills

* Open the interactive browser inapps/web-app.
* Read the full catalog inCATALOG.md.
* Start with role-based bundles indocs/users/bundles.md.
* Follow outcome-driven workflows indocs/users/workflows.md.
* Use the onboarding guides indocs/users/getting-started.mdanddocs/users/usage.md.

## Documentation

For Users

For Contributors

For Maintainers

docs/users/getting-started.md

CONTRIBUTING.md

docs/maintainers/release-process.md

docs/users/usage.md

docs/contributors/skill-anatomy.md

docs/maintainers/audit.md

docs/users/faq.md

docs/contributors/quality-bar.md

docs/maintainers/ci-drift-fix.md

docs/users/visual-guide.md

docs/contributors/examples.md

docs/maintainers/skills-update-guide.md
 · 
.github/MAINTENANCE.md

## Troubleshooting

### Windows install note

Use the normal install flow on Windows:

git clone https://github.com/sickn33/antigravity-awesome-skills.git .agent/skills

If you have an older clone created around the removed symlink workaround, reinstall into a fresh directory or rerun thenpx antigravity-awesome-skillsinstaller.

### Windows truncation or context crash loop

If Antigravity or a Jetski/Cortex-based host keeps reopening into a truncation error, use the dedicated recovery guide:

* docs/users/windows-truncation-recovery.md

That guide includes:

* backup paths before cleanup
* the storage folders that usually need to be cleared
* an optional batch helper adapted fromissue #274

## Web App

The web app is the fastest way to navigate a large repository like this.

Run locally:

npm run app:install
npm run app:dev

That will copy the generated skill index intoapps/web-app/public/skills.json, mirror the currentskills/tree intoapps/web-app/public/skills/, and start the Vite development server.

Hosted online:The same app is available athttps://sickn33.github.io/antigravity-awesome-skills/and is deployed automatically on every push tomain. To enable it once:Settings → Pages → Build and deployment → Source: GitHub Actions.

## Contributing

* Add new skills underskills/<skill-name>/SKILL.md.
* Follow the contributor guide inCONTRIBUTING.md.
* Use the template indocs/contributors/skill-template.md.
* Validate withnpm run validatebefore opening a PR.

## Community

* Discussionsfor questions and feedback.
* Issuesfor bugs and improvement requests.
* SECURITY.mdfor security reporting.

## Support the Project

Support is optional. The project stays free and open-source for everyone.

* Buy me a book on Buy Me a Coffee
* Star the repository
* Open reproducible issues
* Contribute docs, fixes, and skills

## Credits & Sources

We stand on the shoulders of giants.

👉View the Full Attribution Ledger

Key contributors and sources include:

* HackTricks
* OWASP
* Anthropic / OpenAI / Google
* The Open Source Community

This collection would not be possible without the incredible work of the Claude Code community and official sources:

### Official Sources

* anthropics/skills: Official Anthropic skills repository - Document manipulation (DOCX, PDF, PPTX, XLSX), Brand Guidelines, Internal Communications.
* anthropics/claude-cookbooks: Official notebooks and recipes for building with Claude.
* remotion-dev/skills: Official Remotion skills - Video creation in React with 28 modular rules.
* vercel-labs/agent-skills: Vercel Labs official skills - React Best Practices, Web Design Guidelines.
* openai/skills: OpenAI Codex skills catalog - Agent skills, Skill Creator, Concise Planning.
* supabase/agent-skills: Supabase official skills - Postgres Best Practices.
* microsoft/skills: Official Microsoft skills - Azure cloud services, Bot Framework, Cognitive Services, and enterprise development patterns across .NET, Python, TypeScript, Go, Rust, and Java.
* google-gemini/gemini-skills: Official Gemini skills - Gemini API, SDK and model interactions.
* apify/agent-skills: Official Apify skills - Web scraping, data extraction and automation.

### Community Contributors

* rmyndharis/antigravity-skills: For the massive contribution of 300+ Enterprise skills and the catalog generation logic.
* amartelr/antigravity-workspace-manager: Official Workspace Manager CLI companion to dynamically auto-provision subsets of skills across unlimited local development environments.
* obra/superpowers: The original "Superpowers" by Jesse Vincent.
* guanyang/antigravity-skills: Core Antigravity extensions.
* diet103/claude-code-infrastructure-showcase: Infrastructure and Backend/Frontend Guidelines.
* ChrisWiles/claude-code-showcase: React UI patterns and Design Systems.
* travisvn/awesome-claude-skills: Loki Mode and Playwright integration.
* zebbern/claude-code-guide: Comprehensive Security suite & Guide (Source for ~60 new skills).
* alirezarezvani/claude-skills: Senior Engineering and PM toolkit.
* karanb192/awesome-claude-skills: A massive list of verified skills for Claude Code.
* VoltAgent/awesome-agent-skills: Curated collection of 61 high-quality skills including official team skills from Sentry, Trail of Bits, Expo, Hugging Face, and comprehensive context engineering suite (v4.3.0 integration).
* zircote/.claude: Shopify development skill reference.
* vibeforge1111/vibeship-spawner-skills: AI Agents, Integrations, Maker Tools (57 skills, Apache 2.0).
* coreyhaines31/marketingskills: Marketing skills for CRO, copywriting, SEO, paid ads, and growth (23 skills, MIT).
* jonathimer/devmarketing-skills: Developer marketing skills — HN strategy, technical tutorials, docs-as-marketing, Reddit engagement, developer onboarding, and more (33 skills, MIT).
* Silverov/yandex-direct-skill: Yandex Direct (API v5) advertising audit skill — 55 automated checks, A-F scoring, campaign/ad/keyword analysis for the Russian PPC market (MIT).
* vudovn/antigravity-kit: AI Agent templates with Skills, Agents, and Workflows (33 skills, MIT).
* affaan-m/everything-claude-code: Complete Claude Code configuration collection from Anthropic hackathon winner - skills only (8 skills, MIT).
* whatiskadudoing/fp-ts-skills: Practical fp-ts skills for TypeScript – fp-ts-pragmatic, fp-ts-react, fp-ts-errors (v4.4.0).
* webzler/agentMemory: Source for the agent-memory-mcp skill.
* sstklen/claude-api-cost-optimization: Save 50-90% on Claude API costs with smart optimization strategies (MIT).
* rafsilva85/credit-optimizer-v5: Manus AI credit optimizer skill — intelligent model routing, context compression, and smart testing. Saves 30-75% on credits with zero quality loss. Audited across 53 scenarios.
* Wittlesus/cursorrules-pro: Professional .cursorrules configurations for 8 frameworks - Next.js, React, Python, Go, Rust, and more. Works with Cursor, Claude Code, and Windsurf.
* nedcodes-ok/rule-porter: Bidirectional rule converter between Cursor (.mdc), Claude Code (CLAUDE.md), GitHub Copilot, Windsurf, and legacy .cursorrules formats. Zero dependencies.
* SSOJet/skills: Production-ready SSOJet skills and integration guides for popular frameworks and platforms — Node.js, Next.js, React, Java, .NET Core, Go, iOS, Android, and more. Works seamlessly with SSOJet SAML, OIDC, and enterprise SSO flows. Works with Cursor, Antigravity, Claude Code, and Windsurf.
* MojoAuth/skills: Production-ready MojoAuth guides and examples for popular frameworks like Node.js, Next.js, React, Java, .NET Core, Go, iOS, and Android.
* Xquik-dev/x-twitter-scraper: X (Twitter) data platform — tweet search, user lookup, follower extraction, engagement metrics, giveaway draws, monitoring, webhooks, 19 extraction tools, MCP server.
* shmlkv/dna-claude-analysis: Personal genome analysis toolkit — Python scripts analyzing raw DNA data across 17 categories (health risks, ancestry, pharmacogenomics, nutrition, psychology, etc.) with terminal-style single-page HTML visualization.
* AlmogBaku/debug-skill: Interactive debugger skill for AI agents — breakpoints, stepping, variable inspection, and stack traces via thedapCLI. Supports Python, Go, Node.js/TypeScript, Rust, and C/C++.
* uberSKILLS: Design, test, and deploy Claude Code Agent Skills through a visual, AI-assisted workflow.
* christopherlhammer11-ai/tool-use-guardian: Source for the Tool Use Guardian skill — tool-call reliability wrapper with retries, recovery, and failure classification.
* christopherlhammer11-ai/recallmax: Source for the RecallMax skill — long-context memory, summarization, and conversation compression for agents.

### Inspirations

* f/awesome-chatgpt-prompts: Inspiration for the Prompt Library.
* leonardomso/33-js-concepts: Inspiration for JavaScript Mastery.

### Additional Sources

* agent-cards/skill: Manage prepaid virtual Visa cards for AI agents. Create cards, check balances, view credentials, close cards, and get support via MCP tools.

## Repo Contributors

Made withcontrib.rocks.(Image may be cached;view live contributorson GitHub.)

We officially thank the following contributors for their help in making this repository awesome!

* @sck000
* @github-actions[bot]
* @sickn33
* @Mohammad-Faiz-Cloud-Engineer
* @munir-abbasi
* @zinzied
* @ssumanbiswas
* @Dokhacgiakhoa
* @IanJ332
* @maxdml
* @sx4im
* @skyruh
* @itsmeares
* @chauey
* @ar27111994
* @GuppyTheCat
* @Copilot
* @8hrsk
* @sstklen
* @tejasashinde
* @0xrohitgarg
* @zebbern
* @talesperito
* @SnakeEye-sudo
* @nikolasdehor
* @fernandorych
* @taksrules
* @jackjin1997
* @HuynhNhatKhanh
* @liyin2015
* @arathiesh
* @Tiger-Foxx
* @RamonRiosJr
* @Musayrlsms
* @Vonfry
* @vprudnikoff
* @viktor-ferenczi
* @code-vj
* @babysor
* @uriva
* @truongnmt
* @Onsraa
* @SebConejo
* @SuperJMN
* @Enreign
* @sohamganatra
* @Silverov
* @shubhamdevx
* @ronanguilloux
* @sraphaz
* @ProgramadorBrasil
* @PabloASMD
* @yubing744
* @vuth-dogo
* @yang1002378395-cmyk
* @thuanlm215
* @shmlkv
* @rafsilva85
* @nocodemf
* @KrisnaSantosa15
* @junited31
* @fbientrigo
* @dz3ai
* @developer-victor
* @ckdwns9121
* @christopherlhammer11-ai
* @c1c3ru
* @buzzbysolcex
* @avimak
* @antbotlab
* @amalsam
* @ziuus
* @Wittlesus
* @wahidzzz
* @olgasafonova
* @hvasconcelos
* @Guilherme-ruy
* @Gizzant
* @Digidai
* @dbhat93
* @decentraliser
* @MAIOStudio
* @conorbronsdon
* @kriptoburak
* @BenedictKing
* @acbhatt12
* @Andruia
* @AlmogBaku
* @Allen930311
* @alexmvie
* @Sayeem3051
* @Abdulrahmansoliman
* @ALEKGG1
* @8144225309
* @1bcMax
* @sharmanilay
* @KhaiTrang1995
* @LocNguyenSGU
* @nedcodes-ok
* @iftikharg786
* @mertbaskurt
* @MatheusCampagnolo
* @djmahe4
* @MArbeeGit
* @Svobikl
* @kromahlusenii-ops
* @Krishna-Modi12
* @k-kolomeitsev
* @kennyzheng-builds
* @keyserfaty
* @kage-art
* @whatiskadudoing
* @jonathimer
* @qcwssss
* @rcigor

## License

MIT License. SeeLICENSEfor details.

## Star History

If Antigravity Awesome Skills has been useful, consider ⭐ starring the repo!

## About

The Ultimate Collection of 1000+ Agentic Skills for Claude Code/Antigravity/Cursor. Battle-tested, high-performance skills for AI agents including official skills from Anthropic and Vercel.

github.com/sickn33/antigravity-awesome-skills

### Topics

 mcp

 developer-tools

 ai-agents

 prompt-engineering

 ai-workflows

 gemini-cli

 antigravity

 claude-code

 codex-cli

 autonomous-coding

 agentic-skills

 skill-library

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

24.8k

 stars
 

### Watchers

225

 watching
 

### Forks

4.3k

 forks
 

 Report repository

 

## Releases81

v7.9.2 "npm CLI Packaging Fix"

 Latest

 

Mar 15, 2026

 

+ 80 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors121

+ 107 contributors

## Languages

* Python76.2%
* JavaScript8.6%
* Shell7.9%
* TypeScript4.1%
* HTML1.4%
* C#0.8%
* Other1.0%