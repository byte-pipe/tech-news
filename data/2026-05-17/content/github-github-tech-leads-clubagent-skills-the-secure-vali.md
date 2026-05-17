---
title: 'GitHub - tech-leads-club/agent-skills: The secure, validated skill registry for professional AI coding agents. Extend Antigravity, Claude Code, Cursor, Copilot and more with absolute confidence. · GitHub'
url: https://github.com/tech-leads-club/agent-skills
site_name: github
content_file: github-github-tech-leads-clubagent-skills-the-secure-vali
fetched_at: '2026-05-17T19:29:29.148600'
original_url: https://github.com/tech-leads-club/agent-skills
author: tech-leads-club
description: The secure, validated skill registry for professional AI coding agents. Extend Antigravity, Claude Code, Cursor, Copilot and more with absolute confidence. - tech-leads-club/agent-skills
---

tech-leads-club

 

/

agent-skills

Public

* NotificationsYou must be signed in to change notification settings
* Fork313
* Star3.4k

 
 
 
 
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

1,024 Commits
1,024 Commits
.claude-plugin
.claude-plugin
 
 
.cursor-plugin
.cursor-plugin
 
 
.github
.github
 
 
.nx
.nx
 
 
libs/
core
libs/
core
 
 
packages
packages
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
.nvmrc
.nvmrc
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
eslint.config.js
eslint.config.js
 
 
jest.config.ts
jest.config.ts
 
 
jest.preset.js
jest.preset.js
 
 
nx.json
nx.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.base.json
tsconfig.base.json
 
 
View all files

## Repository files navigation

# 🧠 Agent Skills

The secure, validated skill registry for professional AI coding agents

In an ecosystem whereover 13% of marketplace skills contain critical vulnerabilities,Agent Skillsstands apart as a hardened library ofverified,tested, andsafecapabilities.
 ExtendAntigravity,Claude Code,Cursor, and more with absolute confidence.

https://tech-leads-club.github.io/agent-skills/

## 📖 Table of Contents

* ✨ What are Skills?
* 🛡️ Security & Trust
* 🤖 Supported Agents
* 🌟 Featured Skills
* 🚀 Quick Start
* ⚡ How It Works
* 🔌 MCP Server
* 🤝 Contributing
* 🛡️ Content & Authorship
* 📄 License and Attribution

## ✨ What are Skills?

Skills are packaged instructions and resources that extend AI agent capabilities. Think of them asplugins for your AI assistant— they teach your agent new workflows, patterns, and specialized knowledge.

packages/skills-catalog/skills/
 (category-name)/
 skill/
 SKILL.md ← Main instructions
 templates/ ← File templates
 references/ ← On-demand documentation

## 🛡️ Security & Trust

Your environment's safety is our top priority. Unlike open marketplaces where13.4% of skills contain critical issues,agent-skillsis a managed, hardened library: 100% open source (no binaries), static analysis in CI/CD, immutable integrity via lockfiles and content hashing, and human-curated prompts. The CLI uses defense-in-depth (sanitization, path isolation, symlink guards, atomic lockfile, audit trail); every skill is scanned withSnyk Agent Scan(formerly mcp-scan) before publishing.

→Full threat model, implementation details, and vulnerability reporting:SECURITY.md

## 🤖 Supported Agents

Install skills to any of these AI coding agents:

Tier 1 (Popular)

Tier 2 (Rising)

Tier 3 (Enterprise)

Claude Code

Aider

Amazon Q

Cline

Antigravity

Augment

Cursor

Gemini CLI

Droid (Factory.ai)

GitHub Copilot

Kilo Code

OpenCode

Windsurf

Kiro

Sourcegraph Cody

OpenAI Codex

Tabnine

Roo Code

TRAE

Missing your favorite agent?Open an issueand we'll add support!

## 🌟 Featured Skills

A glimpse of what's available in our growing catalog:

Skill

Category

Description

tlc-spec-driven

Development

Project and feature planning with 4 phases: Specify → Design → Tasks → Implement. Creates atomic tasks with verification criteria and maintains persistent memory across sessions.

aws-advisor

Cloud

Expert AWS Cloud Advisor for architecture design, security review, and implementation guidance. Leverages AWS MCP tools for documentation-backed answers.

playwright-skill

Automation

Complete browser automation with Playwright. Test pages, fill forms, take screenshots, validate UX, and automate any browser task.

figma

Design

Fetch design context from Figma and translate nodes into production code. Design-to-code implementation with MCP integration.

security-best-practices

Security

Language and framework-specific security reviews. Detect vulnerabilities, generate reports, and suggest secure-by-default fixes.

→ Browse all skills

## 🚀 Quick Start

### Install Skills in Your Project

npx @tech-leads-club/agent-skills

This launches an interactive wizard:

1. Choose Action— "Install skills" or "Update installed skills"
2. Browse & Select— Filter by category or search
3. Choose agents— Pick target agents (Cursor, Claude Code, etc.)
4. Installation method— Copy (recommended) or Symlink
5. Scope— Global (user home) or Local (project only)

Each step shows a← Backoption to return and revise your choices.

### CLI Options

Note: You can use eithernpx @tech-leads-club/agent-skillsor install globally and useagent-skillsdirectly.

#
 Interactive mode (default)

npx @tech-leads-club/agent-skills

#
 or: agent-skills (if installed globally)

#
 List available skills

agent-skills list
agent-skills ls 
#
 Alias

#
 Install one skill

agent-skills install -s tlc-spec-driven

#
 Install multiple skills at once

agent-skills install -s aws-advisor coding-guidelines docs-writer

#
 Install to specific agents

agent-skills install -s my-skill -a cursor claude-code

#
 Install multiple skills to multiple agents

agent-skills install -s aws-advisor nx-workspace -a cursor windsurf cline

#
 Install globally (to ~/.gemini, ~/.claude, etc.)

agent-skills install -s my-skill -g

#
 Use symlink instead of copy

agent-skills install -s my-skill --symlink

#
 Force re-download (bypass cache)

agent-skills install -s my-skill --force

#
 Update a specific skill

agent-skills update -s my-skill

#
 Update all installed skills

agent-skills update

#
 Remove one skill

agent-skills remove -s my-skill

#
 Remove multiple skills at once

agent-skills remove -s skill1 skill2 skill3
agent-skills rm -s my-skill 
#
 Alias

#
 Remove from specific agents

agent-skills remove -s my-skill -a cursor windsurf

#
 Force removal (bypass lockfile check)

agent-skills remove -s my-skill --force

#
 Manage cache

agent-skills cache --clear 
#
 Clear all cache

agent-skills cache --clear-registry 
#
 Clear only registry

agent-skills cache --path 
#
 Show cache location

#
 View audit log

agent-skills audit 
#
 Show recent operations

agent-skills audit -n 20 
#
 Show last 20 entries

agent-skills audit --path 
#
 Show audit log location

#
 Show contributors and credits

agent-skills credits

#
 Show help

agent-skills --help

### Global Installation (Optional)

npm install -g @tech-leads-club/agent-skills
agent-skills 
#
 Use 'agent-skills' instead of 'npx @tech-leads-club/agent-skills'

## ⚡ How It Works

The CLI fetches skillson-demandfrom our CDN:

1. Browse— The CLI fetches the skills catalog (~45KB)
2. Select— You choose the skills you need
3. Download— Selected skills are downloaded and cached locally
4. Install— Skills are installed to your agent's configuration

### Caching

Downloaded skills are cached in~/.cache/agent-skills/for offline use.

#
 Clear the cache

rm -rf 
~
/.cache/agent-skills

## 🔌 MCP Server

@tech-leads-club/agent-skills-mcpis an MCP server that exposes the skills catalog directly to AI agents viaprogressive disclosure— search first, then fetch only what's needed.

Tool

Purpose

list_skills

Browse all skills by category

search_skills

Find skills by intent (fuzzy search)

read_skill

Load a skill's main instructions

fetch_skill_files

Fetch specific reference files

list_skillsshould be called only when the user explicitly asks to browse/list the catalog.

Quick install(works with any MCP-compatible client):

{
 
"mcpServers"
: {
 
"agent-skills"
: {
 
"command"
: 
"
npx
"
,
 
"args"
: [
"
-y
"
, 
"
@tech-leads-club/agent-skills-mcp
"
]
 }
 }
}

→ Full setup for all clients (Cursor, Claude Code, VS Code, etc.), caching, and error reference:packages/mcp/README.md

## 🤝 Contributing

We welcome contributions! Please see ourCONTRIBUTING.mdfile for detailed guidelines on how to set up your local environment, create new skills, contribute to the marketplace, and follow our release processes.

## 🛡️ Content & Authorship

This repository is a collection of curated skills intended to benefit the community. We deeply respect the intellectual property and wishes of all creators.

If you are the author of any content included here and would like itremovedorupdated, pleaseopen an issueor contact the maintainers.

## 📄 License and Attribution

* Software Engine:The application source code (CLI, scripts, tools) is licensed under theMIT License.
* Tech Leads Club Skills:Unless otherwise stated, all skill files (SKILL.md) authored by the repository maintainers are licensed under theCreative Commons Attribution 4.0 International License (CC-BY-4.0).
* Third-Party Skills:Some skills included in this catalog are created by the community or original authors. These skills retain their original licenses and copyrights. Please check the individualSKILL.mdfiles for specific licensing and author attribution.

If you use our skills catalog, youmustprovide attribution to Tech Leads Club, regardless of how it is used.

## ⭐ Star History

Built with ❤️ by the Tech Leads Club community

## About

The secure, validated skill registry for professional AI coding agents. Extend Antigravity, Claude Code, Cursor, Copilot and more with absolute confidence.

agent-skills.techleads.club/

### Topics

 agent

 ai

 skills

 cursor

 copilot

 antigravity

 claude-code

### Resources

 Readme

 

### License

 View license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

3.4k

 stars
 

### Watchers

52

 watching
 

### Forks

313

 forks
 

 Report repository

 

## Releases56

skills-catalog-v0.14.3

 Latest

 

Apr 28, 2026

 

+ 55 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript68.1%
* Python22.7%
* JavaScript6.7%
* Shell2.3%
* CSS0.2%