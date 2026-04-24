---
title: 'GitHub - refactoringhq/tolaria: Desktop app to manage markdown knowledge bases · GitHub'
url: https://github.com/refactoringhq/tolaria
site_name: hnrss
content_file: hnrss-github-refactoringhqtolaria-desktop-app-to-manage
fetched_at: '2026-04-24T11:56:42.960223'
original_url: https://github.com/refactoringhq/tolaria
date: '2026-04-23'
description: Desktop app to manage markdown knowledge bases. Contribute to refactoringhq/tolaria development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

refactoringhq

 

/

tolaria

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork161
* Star2.6k

 
 
 
 
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

2,000 Commits
2,000 Commits
.claude
.claude
 
 
.github
.github
 
 
.husky
.husky
 
 
demo-vault-v2
demo-vault-v2
 
 
design
design
 
 
docs
docs
 
 
e2e
e2e
 
 
mcp-server
mcp-server
 
 
patches
patches
 
 
public
public
 
 
scripts
scripts
 
 
src-tauri
src-tauri
 
 
src
src
 
 
tests
tests
 
 
.codescene-thresholds
.codescene-thresholds
 
 
.codesceneignore
.codesceneignore
 
 
.codescenerc
.codescenerc
 
 
.env.example
.env.example
 
 
.githooks-info
.githooks-info
 
 
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
 
 
SECURITY.md
SECURITY.md
 
 
components.json
components.json
 
 
eslint.config.js
eslint.config.js
 
 
index.html
index.html
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
playwright.integration.config.ts
playwright.integration.config.ts
 
 
playwright.smoke.config.ts
playwright.smoke.config.ts
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
trademarks.md
trademarks.md
 
 
tsconfig.app.json
tsconfig.app.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.node.json
tsconfig.node.json
 
 
ui-design.pen
ui-design.pen
 
 
vite.config.ts
vite.config.ts
 
 
View all files

## Repository files navigation

 
 
 
 

# 💧 Tolaria

Tolaria is a desktop app for Mac for managingmarkdown knowledge bases. People use it for a variety of use cases:

* Operate second brains and personal knowledge
* Organize company docs as context for AI
* Store OpenClaw/assistants memory and procedures

Personally, I use it torun my life(hey 👋Luca here). I have a massive workspace of 10,000+ notes, which are the result of myRefactoringwork + a ton of personal journaling andsecond braining.

## Walkthroughs

You can find some Loom walkthroughs below — they are short and to the point:

* How I Organize My Own Tolaria Workspace
* My Inbox Workflow
* How I Save Web Resources to Tolaria

## Principles

* 📑Files-first— Your notes are plain markdown files. They're portable, work with any editor, and require no export step. Your data belongs to you, not to any app.
* 🔌Git-first— Every vault is a git repository. You get full version history, the ability to use any git remote, and zero dependency on Tolaria servers.
* 🛜Offline-first, zero lock-in— No accounts, no subscriptions, no cloud dependencies. Your vault works completely offline and always will. If you stop using Tolaria, you lose nothing.
* 🔬Open source— Tolaria is free and open source. I built this formyselfand for sharing it with others.
* 📋Standards-based— Notes are markdown files with YAML frontmatter. No proprietary formats, no locked-in data. Everything works with standard tools if you decide to move away from Tolaria.
* 🔍Types as lenses, not schemas— Types in Tolaria are navigation aids, not enforcement mechanisms. There's no required fields, no validation, just helpful categories for finding notes.
* 🪄AI-first but not AI-only— A vault of files works very well with AI agents, but you are free to use whatever you want. We support Claude Code and Codex CLI (for now), but you can edit the vault with any AI you want. We provide an AGENTS file for your agents to figure out.
* ⌨️Keyboard-first— Tolaria is designed for power-users who want to use keyboard as much as possible. A lot of how we designed the Editor and the Command Palette is based on this.
* 💪Built from real use— Tolaria was created for manage my personal vault of 10,000+ notes, and I use it every day. Every feature exists because it solved a real problem.

## Getting started

Download thelatest release here.

When you open Tolaria for the first time you get the chance of cloning thegetting started vault— which gives you a walkthrough of the whole app.

## Open source and local setup

Tolaria is open source and built with Tauri, React, and TypeScript. If you want to run or contribute to the app locally, here ishow to get started. You can also find the gist below 👇

### Prerequisites

* Node.js 20+
* pnpm 8+
* Rust stable
* macOS for development

### Quick start

pnpm install
pnpm dev

Openhttp://localhost:5173for the browser-based mock mode, or run the native desktop app with:

pnpm tauri dev

## Tech Docs

* 📐ARCHITECTURE.md— System design, tech stack, data flow
* 🧩ABSTRACTIONS.md— Core abstractions and models
* 🚀GETTING-STARTED.md— How to navigate the codebase
* 📚ADRs— Architecture Decision Records

## Security

If you believe you have found a security issue, please report it privately as described inSECURITY.md.

## License

Tolaria is licensed under AGPL-3.0-or-later. The Tolaria name and logo remain covered by the project’s trademark policy.

## About

Desktop app to manage markdown knowledge bases

tolaria.md

### Resources

 Readme

 

### License

 AGPL-3.0 license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2.6k

 stars
 

### Watchers

14

 watching
 

### Forks

161

 forks
 

 Report repository

 

## Releases639

Tolaria 2026.4.24

 Latest

 

Apr 24, 2026

 

+ 638 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* https://refactoring.fm/

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript64.8%
* JavaScript21.0%
* Rust11.9%
* Python1.6%
* CSS0.5%
* Shell0.2%