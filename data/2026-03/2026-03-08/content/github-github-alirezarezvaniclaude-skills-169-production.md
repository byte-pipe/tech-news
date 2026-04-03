---
title: 'GitHub - alirezarezvani/claude-skills: 169 production-ready skills & plugins for Claude Code, OpenAI Codex, and OpenClaw — engineering, marketing, product, compliance, C-level advisory, and more. Install via /plugin marketplace. · GitHub'
url: https://github.com/alirezarezvani/claude-skills
site_name: github
content_file: github-github-alirezarezvaniclaude-skills-169-production
fetched_at: '2026-03-08T11:07:36.039738'
original_url: https://github.com/alirezarezvani/claude-skills
author: alirezarezvani
description: 169 production-ready skills & plugins for Claude Code, OpenAI Codex, and OpenClaw — engineering, marketing, product, compliance, C-level advisory, and more. Install via /plugin marketplace. - alirezarezvani/claude-skills
---

alirezarezvani

 

/

claude-skills

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork353
* Star2.7k

 
 
 
 
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

343 Commits
343 Commits
.claude-plugin
.claude-plugin
 
 
.claude/
commands
.claude/
commands
 
 
.codex
.codex
 
 
.github
.github
 
 
agents
agents
 
 
business-growth
business-growth
 
 
c-level-advisor
c-level-advisor
 
 
commands
commands
 
 
docs
docs
 
 
documentation
documentation
 
 
engineering-team
engineering-team
 
 
engineering
engineering
 
 
finance
finance
 
 
marketing-skill
marketing-skill
 
 
product-team
product-team
 
 
project-management
project-management
 
 
ra-qm-team
ra-qm-team
 
 
scripts
scripts
 
 
standards
standards
 
 
templates
templates
 
 
.gitignore
.gitignore
 
 
.yamllintignore
.yamllintignore
 
 
AUDIT_REPORT.md
AUDIT_REPORT.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
INSTALLATION.md
INSTALLATION.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SKILL-AUTHORING-STANDARD.md
SKILL-AUTHORING-STANDARD.md
 
 
STORE.md
STORE.md
 
 
mkdocs.yml
mkdocs.yml
 
 
View all files

## Repository files navigation

# Claude Code Skills & Plugins

169 production-ready skills and plugins for Claude Code, OpenAI Codex, and OpenClaw— reusable expertise bundles that transform AI coding agents into specialized professionals across engineering, product, marketing, compliance, and more.

⭐2,300+ GitHub stars— the most comprehensive open-source skill library for AI coding agents.

## What Are Claude Code Skills?

Skills are modular instruction packages (plugins) that give AI coding agents domain expertise they don't have out of the box. Each skill includes aSKILL.md(instructions + workflows), Python CLI tools, and reference documentation — everything the agent needs to perform like a specialist.

One repo, three platforms:Works natively as Claude Code plugins, OpenAI Codex agents, and OpenClaw skills.

## Quick Install

### Claude Code (Recommended)

#
 Add the marketplace

/plugin marketplace add alirezarezvani/claude-skills

#
 Install by domain

/plugin install engineering-skills@claude-code-skills 
#
 23 core engineering

/plugin install engineering-advanced-skills@claude-code-skills 
#
 25 POWERFUL-tier

/plugin install product-skills@claude-code-skills 
#
 8 product skills

/plugin install marketing-skills@claude-code-skills 
#
 42 marketing skills

/plugin install ra-qm-skills@claude-code-skills 
#
 12 regulatory/quality

/plugin install pm-skills@claude-code-skills 
#
 6 project management

/plugin install c-level-skills@claude-code-skills 
#
 28 C-level advisory (full C-suite)

/plugin install business-growth-skills@claude-code-skills 
#
 4 business & growth

/plugin install finance-skills@claude-code-skills 
#
 1 finance

#
 Or install individual skills

/plugin install skill-security-auditor@claude-code-skills 
#
 Security scanner

/plugin install playwright-pro@claude-code-skills 
#
 Playwright testing toolkit

/plugin install self-improving-agent@claude-code-skills 
#
 Auto-memory curation

/plugin install content-creator@claude-code-skills 
#
 Single skill

### OpenAI Codex

npx agent-skills-cli add alirezarezvani/claude-skills --agent codex

#
 Or: git clone + ./scripts/codex-install.sh

### OpenClaw

bash 
<(
curl -s https://raw.githubusercontent.com/alirezarezvani/claude-skills/main/scripts/openclaw-install.sh
)

### Manual Installation

git clone https://github.com/alirezarezvani/claude-skills.git

#
 Copy any skill folder to ~/.claude/skills/ (Claude Code) or ~/.codex/skills/ (Codex)

## Skills Overview

169 skills across 9 domains:

Domain

Skills

Highlights

Details

🔧 Engineering — Core

23

Architecture, frontend, backend, fullstack, QA, DevOps, SecOps, AI/ML, data, Playwright, self-improving agent

engineering-team/

🎭 Playwright Pro

9+3

Test generation, flaky fix, Cypress/Selenium migration, TestRail, BrowserStack, 55 templates

engineering-team/playwright-pro

🧠 Self-Improving Agent

5+2

Auto-memory curation, pattern promotion, skill extraction, memory health

engineering-team/self-improving-agent

⚡ Engineering — POWERFUL

25

Agent designer, RAG architect, database designer, CI/CD builder, security auditor, MCP builder

engineering/

🎯 Product

8

Product manager, agile PO, strategist, UX researcher, UI design, landing pages, SaaS scaffolder

product-team/

📣 Marketing

42

7 pods: Content (8), SEO (5), CRO (6), Channels (5), Growth (4), Intelligence (4), Sales (2) + context foundation + orchestration router. 27 Python tools.

marketing-skill/

📋 Project Management

6

Senior PM, scrum master, Jira, Confluence, Atlassian admin, templates

project-management/

🏥 Regulatory & QM

12

ISO 13485, MDR 2017/745, FDA, ISO 27001, GDPR, CAPA, risk management

ra-qm-team/

💼 C-Level Advisory

28

Full C-suite (10 roles) + orchestration + board meetings + culture & collaboration

c-level-advisor/

📈 Business & Growth

4

Customer success, sales engineer, revenue ops, contracts & proposals

business-growth/

💰 Finance

1

Financial analyst (DCF, budgeting, forecasting)

finance/

## ⚡ POWERFUL Tier

25 advanced skills with deep, production-grade capabilities:

Skill

What It Does

agent-designer

Multi-agent orchestration, tool schemas, performance evaluation

agent-workflow-designer

Sequential, parallel, router, orchestrator, and evaluator patterns

rag-architect

RAG pipeline builder, chunking optimizer, retrieval evaluator

database-designer

Schema analyzer, ERD generation, index optimizer, migration generator

database-schema-designer

Requirements → migrations, types, seed data, RLS policies

migration-architect

Migration planner, compatibility checker, rollback generator

skill-security-auditor

🔒 Security gate — scan skills for malicious code before installation

ci-cd-pipeline-builder

Analyze stack → generate GitHub Actions / GitLab CI configs

mcp-server-builder

Build MCP servers from OpenAPI specs

pr-review-expert

Blast radius analysis, security scan, coverage delta

api-design-reviewer

REST API linter, breaking change detector, design scorecard

api-test-suite-builder

Scan API routes → generate complete test suites

dependency-auditor

Multi-language scanner, license compliance, upgrade planner

release-manager

Changelog generator, semantic version bumper, readiness checker

observability-designer

SLO designer, alert optimizer, dashboard generator

performance-profiler

Node/Python/Go profiling, bundle analysis, load testing

monorepo-navigator

Turborepo/Nx/pnpm workspace management & impact analysis

changelog-generator

Conventional commits → structured changelogs

codebase-onboarding

Auto-generate onboarding docs from codebase analysis

runbook-generator

Codebase → operational runbooks with commands

git-worktree-manager

Parallel dev with port isolation, env sync

env-secrets-manager

.env management, leak detection, rotation workflows

incident-commander

Incident response playbook, severity classifier, PIR generator

tech-debt-tracker

Codebase debt scanner, prioritizer, trend dashboard

interview-system-designer

Interview loop designer, question bank, calibrator

## 🔒 Skill Security Auditor

New in v2.0.0 — audit any skill for security risks before installation:

python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/

Scans for: command injection, code execution, data exfiltration, prompt injection, dependency supply chain risks, privilege escalation. ReturnsPASS / WARN / FAILwith remediation guidance.

Zero dependencies.Works anywhere Python runs.

## Recently Enhanced Skills

Production-quality upgrades added for:

* engineering/git-worktree-manager— worktree lifecycle + cleanup automation scripts
* engineering/mcp-server-builder— OpenAPI -> MCP scaffold + manifest validator
* engineering/changelog-generator— release note generator + conventional commit linter
* engineering/ci-cd-pipeline-builder— stack detector + pipeline generator
* marketing-skill/prompt-engineer-toolkit— prompt A/B tester + prompt version/diff manager

Each now ships withscripts/, extractedreferences/, and a usage-focusedREADME.md.

## Usage Examples

### Architecture Review

Using the senior-architect skill, review our microservices architecture
and identify the top 3 scalability risks.

### Content Creation

Using the content-creator skill, write a blog post about AI-augmented
development. Optimize for SEO targeting "Claude Code tutorial".

### Compliance Audit

Using the mdr-745-specialist skill, review our technical documentation
for MDR Annex II compliance gaps.

## Python Analysis Tools

160+ CLI tools ship with the skills:

#
 Brand voice analysis

python3 marketing-skill/content-creator/scripts/brand_voice_analyzer.py article.txt

#
 Tech debt scoring

python3 c-level-advisor/cto-advisor/scripts/tech_debt_analyzer.py /path/to/codebase

#
 RICE prioritization

python3 product-team/product-manager-toolkit/scripts/rice_prioritizer.py features.csv

#
 Security audit

python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py /path/to/skill/

## Related Projects

Project

Description

Claude Code Skills & Agents Factory

Methodology for building skills at scale

Claude Code Tresor

Productivity toolkit with 60+ prompt templates

Product Manager Skills

Senior PM agent with 6 knowledge domains, 12 templates, 30+ frameworks — discovery, strategy, delivery, SaaS metrics, career coaching, AI product craft

## FAQ

How do I install Claude Code plugins?Add the marketplace with/plugin marketplace add alirezarezvani/claude-skills, then install any skill bundle with/plugin install <name>@claude-code-skills.

Do these skills work with OpenAI Codex?Yes. Skills work natively with Claude Code, OpenAI Codex, and OpenClaw. See Quick Install above.

Are the Python tools dependency-free?Yes. All 160+ Python CLI tools use the standard library only — zero pip installs required.

How do I create my own Claude Code skill?Each skill is a folder with aSKILL.md(frontmatter + instructions), optionalscripts/,references/, andassets/. See theSkills & Agents Factoryfor a step-by-step guide.

## Contributing

We welcome contributions! SeeCONTRIBUTING.mdfor guidelines.

Quick ideas:

* Add new skills in underserved domains
* Improve existing Python tools
* Add test coverage for scripts
* Translate skills for non-English markets

## License

MIT — seeLICENSEfor details.

## Star History

Built byAlireza Rezvani·Medium·Twitter

## About

169 production-ready skills & plugins for Claude Code, OpenAI Codex, and OpenClaw — engineering, marketing, product, compliance, C-level advisory, and more. Install via /plugin marketplace.

alirezarezvani.medium.com/

### Topics

 devtools

 developer-tools

 openai-codex

 prompt-engineering

 claude-ai

 anthropic-claude

 agentic-ai

 mcp-tools

 claude-code

 ai-coding-agent

 agentic-coding

 ai-plugins

 claudecode-subagents

 claude-code-plugins

 claude-skills

 claude-code-skills

 claude-ai-skills

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

2.7k

 stars
 

### Watchers

35

 watching
 

### Forks

353

 forks
 

 Report repository

 

## Releases1

v2.0.0 — 86 Skills, 9 Domains, 26 POWERFUL-Tier

 Latest

 

Mar 4, 2026

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* buymeacoffee.com/rezarezvani

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python98.8%
* Other1.2%