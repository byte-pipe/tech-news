---
title: 'GitHub - coreyhaines31/marketingskills: Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering. · GitHub'
url: https://github.com/coreyhaines31/marketingskills
site_name: github
content_file: github-github-coreyhaines31marketingskills-marketing-skil
fetched_at: '2026-04-23T11:59:16.792807'
original_url: https://github.com/coreyhaines31/marketingskills
author: coreyhaines31
description: Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering. - coreyhaines31/marketingskills
---

coreyhaines31

 

/

marketingskills

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork3.7k
* Star23.2k

 
 
 
 
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

249 Commits
249 Commits
.claude-plugin
.claude-plugin
 
 
.github
.github
 
 
skills
skills
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
VERSIONS.md
VERSIONS.md
 
 
validate-skills-official.sh
validate-skills-official.sh
 
 
validate-skills.sh
validate-skills.sh
 
 
View all files

## Repository files navigation

# Marketing Skills for AI Agents

A collection of AI agent skills focused on marketing tasks. Built for technical marketers and founders who want AI coding agents to help with conversion optimization, copywriting, SEO, analytics, and growth engineering. Works with Claude Code, OpenAI Codex, Cursor, Windsurf, and any agent that supports theAgent Skills spec.

Built byCorey Haines. Need hands-on help? Check outConversion Factory— Corey's agency for conversion optimization, landing pages, and growth strategy. Want to learn more about marketing? Subscribe toSwipe Files. Want an autonomous AI agent that uses these skills to be your CMO? TryMagister.

New to the terminal and coding agents? Check out the companion guideCoding for Marketers.

Contributions welcome!Found a way to improve a skill or have a new one to add?Open a PR.

Run into a problem or have a question?Open an issue— we're happy to help.

## What are Skills?

Skills are markdown files that give AI agents specialized knowledge and workflows for specific tasks. When you add these to your project, your agent can recognize when you're working on a marketing task and apply the right frameworks and best practices.

## How Skills Work Together

Skills reference each other and build on shared context. Theproduct-marketing-contextskill is the foundation — every other skill checks it first to understand your product, audience, and positioning before doing anything.

 ┌──────────────────────────────────────┐
 │ product-marketing-context │
 │ (read by all other skills first) │
 └──────────────────┬───────────────────┘
 │
 ┌──────────────┬─────────────┬─────────────┼─────────────┬──────────────┬──────────────┐
 ▼ ▼ ▼ ▼ ▼ ▼ ▼
┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────────┐ ┌──────────┐ ┌─────────────┐ ┌───────────┐
│ SEO & │ │ CRO │ │Content & │ │ Paid & │ │ Growth & │ │ Sales & │ │ Strategy │
│ Content │ │ │ │ Copy │ │Measurement │ │Retention │ │ GTM │ │ │
├──────────┤ ├──────────┤ ├──────────┤ ├────────────┤ ├──────────┤ ├─────────────┤ ├───────────┤
│seo-audit │ │page-cro │ │copywritng│ │paid-ads │ │referral │ │revops │ │mktg-ideas │
│ai-seo │ │signup-cro│ │copy-edit │ │ad-creative │ │free-tool │ │sales-enable │ │mktg-psych │
│site-arch │ │onboard │ │cold-email│ │ab-test │ │churn- │ │launch │ │customer- │
│programm │ │form-cro │ │email-seq │ │analytics │ │ prevent │ │pricing │ │ research │
│schema │ │popup-cro │ │social │ │ │ │community │ │comp-alts │ │ │
│content │ │paywall │ │ │ │ │ │lead-magnt│ │comp-profile │ │ │
│aso-audit │ │ │ │ │ │ │ │ │ │directory │ │ │
└────┬─────┘ └────┬─────┘ └────┬─────┘ └─────┬──────┘ └────┬─────┘ └──────┬──────┘ └─────┬─────┘
 │ │ │ │ │ │ │
 └────────────┴─────┬──────┴──────────────┴─────────────┴──────────────┴──────────────┘
 │
 Skills cross-reference each other:
 copywriting ↔ page-cro ↔ ab-test-setup
 revops ↔ sales-enablement ↔ cold-email
 seo-audit ↔ schema-markup ↔ ai-seo
 customer-research → copywriting, page-cro, competitor-alternatives

See each skill'sRelated Skillssection for the full dependency map.

## Available Skills

Skill

Description

ab-test-setup

When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program....

ad-creative

When the user wants to generate, iterate, or scale ad creative — headlines, descriptions, primary text, or full ad...

ai-seo

When the user wants to optimize content for AI search engines, get cited by LLMs, or appear in AI-generated answers....

analytics-tracking

When the user wants to set up, improve, or audit analytics tracking and measurement. Also use when the user mentions...

aso-audit

When the user wants to audit or optimize an App Store or Google Play listing. Also use when the user mentions 'ASO...

churn-prevention

When the user wants to reduce churn, build cancellation flows, set up save offers, recover failed payments, or...

cold-email

Write B2B cold emails and follow-up sequences that get replies. Use when the user wants to write cold outreach emails,...

community-marketing

Build and leverage online communities to drive product growth and brand loyalty. Use when the user wants to create a...

competitor-alternatives

When the user wants to create competitor comparison or alternative pages for SEO and sales enablement. Also use when...

competitor-profiling

When the user wants to research, profile, or analyze competitors from their URLs. Also use when the user mentions...

content-strategy

When the user wants to plan a content strategy, decide what content to create, or figure out what topics to cover. Also...

copy-editing

When the user wants to edit, review, or improve existing marketing copy, or refresh outdated content. Also use when the...

copywriting

When the user wants to write, rewrite, or improve marketing copy for any page — including homepage, landing pages,...

customer-research

When the user wants to conduct, analyze, or synthesize customer research. Use when the user mentions "customer...

directory-submissions

When the user wants to submit their product to startup, SaaS, AI, agent, MCP, no-code, or review directories for...

email-sequence

When the user wants to create or optimize an email sequence, drip campaign, automated email flow, or lifecycle email...

form-cro

When the user wants to optimize any form that is NOT signup/registration — including lead capture forms, contact forms,...

free-tool-strategy

When the user wants to plan, evaluate, or build a free tool for marketing purposes — lead generation, SEO value, or...

launch-strategy

When the user wants to plan a product launch, feature announcement, or release strategy. Also use when the user...

lead-magnets

When the user wants to create, plan, or optimize a lead magnet for email capture or lead generation. Also use when the...

marketing-ideas

When the user needs marketing ideas, inspiration, or strategies for their SaaS or software product. Also use when the...

marketing-psychology

When the user wants to apply psychological principles, mental models, or behavioral science to marketing. Also use when...

onboarding-cro

When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value. Also...

page-cro

When the user wants to optimize, improve, or increase conversions on any marketing page — including homepage, landing...

paid-ads

When the user wants help with paid advertising campaigns on Google Ads, Meta (Facebook/Instagram), LinkedIn, Twitter/X,...

paywall-upgrade-cro

When the user wants to create or optimize in-app paywalls, upgrade screens, upsell modals, or feature gates. Also use...

popup-cro

When the user wants to create or optimize popups, modals, overlays, slide-ins, or banners for conversion purposes. Also...

pricing-strategy

When the user wants help with pricing decisions, packaging, or monetization strategy. Also use when the user mentions...

product-marketing-context

When the user wants to create or update their product marketing context document. Also use when the user mentions...

programmatic-seo

When the user wants to create SEO-driven pages at scale using templates and data. Also use when the user mentions...

referral-program

When the user wants to create, optimize, or analyze a referral program, affiliate program, or word-of-mouth strategy....

revops

When the user wants help with revenue operations, lead lifecycle management, or marketing-to-sales handoff processes....

sales-enablement

When the user wants to create sales collateral, pitch decks, one-pagers, objection handling docs, or demo scripts. Also...

schema-markup

When the user wants to add, fix, or optimize schema markup and structured data on their site. Also use when the user...

seo-audit

When the user wants to audit, review, or diagnose SEO issues on their site. Also use when the user mentions "SEO...

signup-flow-cro

When the user wants to optimize signup, registration, account creation, or trial activation flows. Also use when the...

site-architecture

When the user wants to plan, map, or restructure their website's page hierarchy, navigation, URL structure, or internal...

social-content

When the user wants help creating, scheduling, or optimizing social media content for LinkedIn, Twitter/X, Instagram,...

## Installation

### Option 1: CLI Install (Recommended)

Usenpx skillsto install skills directly:

#
 Install all skills

npx skills add coreyhaines31/marketingskills

#
 Install specific skills

npx skills add coreyhaines31/marketingskills --skill page-cro copywriting

#
 List available skills

npx skills add coreyhaines31/marketingskills --list

This automatically installs to your.agents/skills/directory (and symlinks into.claude/skills/for Claude Code compatibility).

### Option 2: Claude Code Plugin

Install via Claude Code's built-in plugin system:

#
 Add the marketplace

/plugin marketplace add coreyhaines31/marketingskills

#
 Install all marketing skills

/plugin install marketing-skills

### Option 3: Clone and Copy

Clone the entire repo and copy the skills folder:

git clone https://github.com/coreyhaines31/marketingskills.git
cp -r marketingskills/skills/
*
 .agents/skills/

### Option 4: Git Submodule

Add as a submodule for easy updates:

git submodule add https://github.com/coreyhaines31/marketingskills.git .agents/marketingskills

Then reference skills from.agents/marketingskills/skills/.

### Option 5: Fork and Customize

1. Fork this repository
2. Customize skills for your specific needs
3. Clone your fork into your projects

### Option 6: SkillKit (Multi-Agent)

UseSkillKitto install skills across multiple AI agents (Claude Code, Cursor, Copilot, etc.):

#
 Install all skills

npx skillkit install coreyhaines31/marketingskills

#
 Install specific skills

npx skillkit install coreyhaines31/marketingskills --skill page-cro copywriting

#
 List available skills

npx skillkit install coreyhaines31/marketingskills --list

## Upgrading from v1.0

Skills now use.agents/instead of.claude/for the product marketing context file. Move your existing context file:

mkdir -p .agents
mv .claude/product-marketing-context.md .agents/product-marketing-context.md

Skills will still check.claude/as a fallback, so nothing breaks if you don't.

## Usage

Once installed, just ask your agent to help with marketing tasks:

"Help me optimize this landing page for conversions"
→ Uses page-cro skill

"Write homepage copy for my SaaS"
→ Uses copywriting skill

"Set up GA4 tracking for signups"
→ Uses analytics-tracking skill

"Create a 5-email welcome sequence"
→ Uses email-sequence skill

You can also invoke skills directly:

/page-cro
/email-sequence
/seo-audit

## Skill Categories

### Conversion Optimization

* page-cro- Any marketing page
* signup-flow-cro- Registration flows
* onboarding-cro- Post-signup activation
* form-cro- Lead capture forms
* popup-cro- Modals and overlays
* paywall-upgrade-cro- In-app upgrade moments

### Content & Copy

* copywriting- Marketing page copy
* copy-editing- Edit and polish existing copy
* cold-email- B2B cold outreach emails and sequences
* email-sequence- Automated email flows
* social-content- Social media content

### SEO & Discovery

* seo-audit- Technical and on-page SEO
* ai-seo- AI search optimization (AEO, GEO, LLMO)
* programmatic-seo- Scaled page generation
* site-architecture- Page hierarchy, navigation, URL structure
* competitor-alternatives- Comparison and alternative pages
* schema-markup- Structured data

### Paid & Distribution

* paid-ads- Google, Meta, LinkedIn ad campaigns
* ad-creative- Bulk ad creative generation and iteration
* social-content- Social media scheduling and strategy

### Measurement & Testing

* analytics-tracking- Event tracking setup
* ab-test-setup- Experiment design

### Retention

* churn-prevention- Cancel flows, save offers, dunning, payment recovery

### Growth Engineering

* free-tool-strategy- Marketing tools and calculators
* referral-program- Referral and affiliate programs

### Strategy & Monetization

* marketing-ideas- 140 SaaS marketing ideas
* marketing-psychology- Mental models and psychology
* launch-strategy- Product launches and announcements
* pricing-strategy- Pricing, packaging, and monetization

### Sales & RevOps

* revops- Lead lifecycle, scoring, routing, pipeline management
* sales-enablement- Sales decks, one-pagers, objection docs, demo scripts

## Contributing

Found a way to improve a skill? Have a new skill to suggest? PRs and issues welcome!

SeeCONTRIBUTING.mdfor guidelines on adding or improving skills.

## License

MIT- Use these however you want.

## About

Marketing skills for Claude Code and AI agents. CRO, copywriting, SEO, analytics, and growth engineering.

marketing-skills.com

### Topics

 marketing

 codex

 claude

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

23.2k

 stars
 

### Watchers

242

 watching
 

### Forks

3.7k

 forks
 

 Report repository

 

## Releases9

v1.8.0 — 2 new skills, security hardening, plugin fix

 Latest

 

Apr 21, 2026

 

+ 8 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* buymeacoffee.com/coreyhaines

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* JavaScript98.4%
* Shell1.6%