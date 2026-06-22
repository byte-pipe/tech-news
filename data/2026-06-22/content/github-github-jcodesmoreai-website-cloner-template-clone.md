---
title: 'GitHub - JCodesMore/ai-website-cloner-template: Clone any website with one command using AI coding agents · GitHub'
url: https://github.com/JCodesMore/ai-website-cloner-template
site_name: github
content_file: github-github-jcodesmoreai-website-cloner-template-clone
fetched_at: '2026-06-22T13:05:22.619334'
original_url: https://github.com/JCodesMore/ai-website-cloner-template
author: JCodesMore
description: Clone any website with one command using AI coding agents - JCodesMore/ai-website-cloner-template
---

JCodesMore

 

/

ai-website-cloner-template

Public template

* NotificationsYou must be signed in to change notification settings
* Fork2.7k
* Star17.4k

 
 
 
 
master
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

40 Commits
40 Commits
.amazonq
.amazonq
 
 
.augment/
commands
.augment/
commands
 
 
.claude/
skills/
clone-website
.claude/
skills/
clone-website
 
 
.codex/
skills/
clone-website
.codex/
skills/
clone-website
 
 
.continue
.continue
 
 
.cursor
.cursor
 
 
.gemini/
commands
.gemini/
commands
 
 
.github
.github
 
 
.opencode/
commands
.opencode/
commands
 
 
.windsurf/
workflows
.windsurf/
workflows
 
 
docs
docs
 
 
public
public
 
 
scripts
scripts
 
 
src
src
 
 
.aider.conf.yml
.aider.conf.yml
 
 
.clinerules
.clinerules
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.nvmrc
.nvmrc
 
 
.windsurfrules
.windsurfrules
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.dev
Dockerfile.dev
 
 
GEMINI.md
GEMINI.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
components.json
components.json
 
 
docker-compose.yml
docker-compose.yml
 
 
eslint.config.mjs
eslint.config.mjs
 
 
next.config.ts
next.config.ts
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
postcss.config.mjs
postcss.config.mjs
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# AI Website Cloner Template

 
 

A reusable template for reverse-engineering any website into a clean, modern Next.js codebase using AI coding agents.

Recommended:Claude Codewith Opus 4.7 for best results— but works with a variety of AI coding agents.

Point it at a URL, run/clone-website, and your AI agent will inspect the site, extract design tokens and assets, write component specs, and dispatch parallel builders to reconstruct every section.

## Demo

Click the image above to watch the full demo on YouTube.

## Quick Start

Important:Start by making your own copy with GitHub'sUse this templatebutton. Do not clone this template repository directly for your website project, and do not open pull requests here with your generated website.

1. Create your own repository from this templateOn the GitHub page for this project, clickUse this template, then clickCreate a new repository.Give your new repository a name, choose whether it should be public or private, then clickCreate repository. If GitHub shows anInclude all branchesoption, you can leave it off.This gives you your own separate project to work in, so your website changes stay in your account instead of coming back to the main template.
2. Open your new repository on your computerAfter GitHub creates your copy, open that new repository. ClickCodeand open or clone your new repository with your preferred coding tool.If you use the terminal, the command will look like this:git clone https://github.com/YOUR-USERNAME/YOUR-NEW-REPOSITORY.gitcdYOUR-NEW-REPOSITORY
3. Install dependenciesnpm install
4. Start your AI agent— Claude Code recommended:claude --chrome
5. Run the skill:/clone-website <target-url1> [<target-url2> ...]
6. Customize(optional) — after the base clone is built, modify as needed

Using a different agent? OpenAGENTS.mdfor project instructions — most agents pick it up automatically.

## Supported Platforms

Agent

Status

Claude Code

Recommended
 — Opus 4.7

Codex CLI

Supported

OpenCode

Supported

GitHub Copilot

Supported

Cursor

Supported

Windsurf

Supported

Gemini CLI

Supported

Cline

Supported

Roo Code

Supported

Continue

Supported

Amazon Q

Supported

Augment Code

Supported

Aider

Supported

## Prerequisites

* Node.js24+
* An AI coding agent (seeSupported Platforms)

## Tech Stack

* Next.js 16— App Router, React 19, TypeScript strict
* shadcn/ui— Radix primitives + Tailwind CSS v4
* Tailwind CSS v4— oklch design tokens
* Lucide React— default icons (replaced by extracted SVGs during cloning)

## How It Works

The/clone-websiteskill runs a multi-phase pipeline:

1. Reconnaissance— screenshots, design token extraction, interaction sweep (scroll, click, hover, responsive)
2. Foundation— updates fonts, colors, globals, downloads all assets
3. Component Specs— writes detailed spec files (docs/research/components/) with exact computed CSS values, states, behaviors, and content
4. Parallel Build— dispatches builder agents in git worktrees, one per section/component
5. Assembly & QA— merges worktrees, wires up the page, runs visual diff against the original

Each builder agent receives the full component specification inline — exactgetComputedStyle()values, interaction models, multi-state content, responsive breakpoints, and asset paths. No guessing.

## Use Cases

* Platform migration— rebuild a site you own from WordPress/Webflow/Squarespace into a modern Next.js codebase
* Lost source code— your site is live but the repo is gone, the developer left, or the stack is legacy. Get the code back in a modern format
* Learning— deconstruct how production sites achieve specific layouts, animations, and responsive behavior by working with real code

## Not Intended For

* Phishing or impersonation— this project must not be used for deceptive purposes, impersonation, or any activity that breaks the law.
* Passing off someone's design as your own— logos, brand assets, and original copy belong to their owners.
* Violating terms of service— some sites explicitly prohibit scraping or reproduction. Check first.

## Project Structure

src/
 app/ # Next.js routes
 components/ # React components
 ui/ # shadcn/ui primitives
 icons.tsx # Extracted SVG icons
 lib/utils.ts # cn() utility
 types/ # TypeScript interfaces
 hooks/ # Custom React hooks
public/
 images/ # Downloaded images from target
 videos/ # Downloaded videos from target
 seo/ # Favicons, OG images
docs/
 research/ # Extraction output & component specs
 design-references/ # Screenshots
scripts/
 sync-agent-rules.sh # Regenerate agent instruction files
 sync-skills.mjs # Regenerate /clone-website for all platforms
AGENTS.md # Agent instructions (single source of truth)
CLAUDE.md # Claude Code config (imports AGENTS.md)
GEMINI.md # Gemini CLI config (imports AGENTS.md)

## Commands

npm run dev 
#
 Start dev server

npm run build 
#
 Production build

npm run lint 
#
 ESLint check

npm run typecheck 
#
 TypeScript check

npm run check 
#
 Run lint + typecheck + build

### If using docker

docker compose up app --build 
#
 build and run the app

docker compose up dev --build 
#
 run the app in dev mode on port 3001

## Updating for Other Platforms

Two source-of-truth files power all platform support. Edit the source, then run the sync script:

What

Source of truth

Sync command

Project instructions

AGENTS.md

bash scripts/sync-agent-rules.sh

/clone-website
 skill

.claude/skills/clone-website/SKILL.md

node scripts/sync-skills.mjs

Each script regenerates the platform-specific copies automatically. Agents that read the source files natively need no regeneration.

## Star History

## License

MIT

## About

Clone any website with one command using AI coding agents

dsc.gg/jcodesmore

### Topics

 react

 template

 boilerplate

 automation

 typescript

 ai

 clone

 skills

 nextjs

 reverse-engineering

 web-scraping

 developer-tools

 ai-agents

 claude

 tailwindcss

 website-clone

 ai-tools

 shadcn-ui

 claude-code

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

17.4k

 stars
 

### Watchers

89

 watching
 

### Forks

2.7k

 forks
 

 Report repository

 

## Releases5

v0.3.1 - Windows CRLF Fix for Agent Rules Sync

 Latest

 

Mar 30, 2026

 

+ 4 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript23.0%
* CSS22.2%
* JavaScript20.5%
* Dockerfile20.2%
* Shell14.1%