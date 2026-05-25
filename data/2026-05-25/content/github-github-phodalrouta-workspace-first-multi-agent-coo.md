---
title: 'GitHub - phodal/routa: Workspace-first multi-agent coordination platform for AI development, with shared Specs, Kanban orchestration, and MCP/ACP/ A2A support across web and desktop. · GitHub'
url: https://github.com/phodal/routa
site_name: github
content_file: github-github-phodalrouta-workspace-first-multi-agent-coo
fetched_at: '2026-05-25T19:34:45.028298'
original_url: https://github.com/phodal/routa
author: phodal
description: Workspace-first multi-agent coordination platform for AI development, with shared Specs, Kanban orchestration, and MCP/ACP/ A2A support across web and desktop. - phodal/routa
---

phodal

 

/

routa

Public

* NotificationsYou must be signed in to change notification settings
* Fork197
* Star1.4k

 
 
 
 
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

4,076 Commits
4,076 Commits
.agents/
skills
.agents/
skills
 
 
.augment/
skills
.augment/
skills
 
 
.claude
.claude
 
 
.codex
.codex
 
 
.github
.github
 
 
.husky
.husky
 
 
.kiro
.kiro
 
 
.lanes
.lanes
 
 
.qoder
.qoder
 
 
.storybook
.storybook
 
 
apps
apps
 
 
architecture
architecture
 
 
crates
crates
 
 
docker
docker
 
 
docs
docs
 
 
drizzle-sqlite
drizzle-sqlite
 
 
drizzle
drizzle
 
 
e2e
e2e
 
 
packages
packages
 
 
patches
patches
 
 
public
public
 
 
resources
resources
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
tools
tools
 
 
.dependency-cruiser.cjs
.dependency-cruiser.cjs
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
.semgrepignore
.semgrepignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SECURITY.md
SECURITY.md
 
 
SUPPORT.md
SUPPORT.md
 
 
api-contract.yaml
api-contract.yaml
 
 
docker-compose.yml
docker-compose.yml
 
 
docusaurus.config.js
docusaurus.config.js
 
 
drizzle-sqlite.config.ts
drizzle-sqlite.config.ts
 
 
drizzle.config.ts
drizzle.config.ts
 
 
eslint.config.mjs
eslint.config.mjs
 
 
next.config.ts
next.config.ts
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
playwright.tauri.config.ts
playwright.tauri.config.ts
 
 
postcss.config.mjs
postcss.config.mjs
 
 
routa-desktop.md
routa-desktop.md
 
 
sidebars.js
sidebars.js
 
 
skills-lock.json
skills-lock.json
 
 
tailwind.config.ts
tailwind.config.ts
 
 
tsconfig.desktop.json
tsconfig.desktop.json
 
 
tsconfig.json
tsconfig.json
 
 
vercel.json
vercel.json
 
 
vitest.config.ts
vitest.config.ts
 
 
vitest.setup.ts
vitest.setup.ts
 
 
View all files

## Repository files navigation

# Routa

Workspace-first multi-agent coordination platform for software delivery

Demo•Architecture•How It Works•Why Routa•Quick Start•Docs•中文

Routa is a workspace-first multi-agent coordination platform for software delivery. It keeps goals, tasks, sessions, traces, evidence, and review state visible on a board instead of burying them inside a single chat thread.

Releases·Architecture·Feature Tree·Quick Start·Docs Site·Slack·Contributing

## Demo

* Bilibili walkthrough
* YouTube walkthrough

## Community

* Docs Site
* Slack Community
* Releases
* Issues

## Architecture

### System Architecture

The current implementation is intentionally dual-backend, not two separate products.

* Web: Next.js pages and route handlers insrc/
* Desktop: Tauri shell inapps/desktop/backed by the Axum server incrates/routa-server/
* Shared boundary: both runtimes preserve the same workspace, session, task, trace, codebase, worktree, and review semantics defined byapi-contract.yaml
* Integration surfaces: ACP, MCP, A2A, AG-UI, A2UI, REST, and SSE

### Review Gate Architecture

The delivery gate is a stacked decision path, not a single reviewer persona.

* Harness Monitor answers what happened by surfacing traces, changed files, commands, git state, and attribution
* Entrix Fitness answers what should be true by enforcing hard gates, evidence requirements, and file budget or policy checks
* Gate Specialist answers whether the card can move by verifying acceptance criteria and routing to Done, Dev, or human escalation

## How It Works

You: "Build a user auth system with login, registration, and password reset"
 ↓
 Workspace + Kanban Board
 ↓
 Backlog Todo Dev Review Done
 Backlog Refiner -> Todo Orchestrator -> Dev Crafter -> Review Guard -> Done Reporter
 ↘
 Blocked Resolver

Routa treats the board as both the planning surface and the coordination bus. The important detail is that each lane is backed by a different specialist prompt, and each downstream lane is deliberately stricter than the previous one.

At a high level, two specialist layers work together:

* Core roles: ROUTA coordinates, CRAFTER implements, GATE verifies
* Kanban lane specialists: each column applies a concrete prompt contract and a concrete evidence contract

### End-to-End Example

1. You describe a goal in natural language.
2. ROUTA or the board automation turns that goal into a workspace-scoped card.
3. Backlog Refiner rewrites the rough request into a canonical YAML story with acceptance criteria, constraints, dependencies, and an INVEST snapshot.
4. Todo Orchestrator distrusts that upstream card, reparses the YAML, rejects weak stories, and appends an execution-ready brief.
5. Dev Crafter distrusts the plan again, refuses to code unless the story is executable, implements only the scoped change, runs validation, commits the work, and appends Dev Evidence.
6. Review Guard distrusts Dev's self-assessment, independently checks each acceptance criterion, requires tests and a clean git state, and either rejects to Dev or approves to Done.
7. Done Reporter appends a short completion summary that explains what shipped and what evidence justified completion.
8. If the work is blocked by environment, dependency, or ambiguity, Blocked Resolver writes down the blocker and routes the card back to the correct lane instead of letting the problem stay implicit.

### Lane Contracts

Lane

Specialist

What the prompt enforces

What gets written to the card

Typical handoff

Backlog

Backlog Refiner

Clarify scope, do not code, and do not move forward until the card contains exactly one canonical YAML story block

Canonical YAML story with problem statement, acceptance criteria, constraints, dependencies, out-of-scope items, and INVEST checks

Move to Todo only when the story parses and is independently executable

Todo

Todo Orchestrator

Re-validate Backlog output, reject malformed or vague cards, and turn a valid story into an execution-ready brief

Execution Plan, Key Files and Entry Points, Dependency Plan, Risk Notes

Move to Dev only when implementation can start within minutes

Dev

Dev Crafter

Re-check that the card is executable, implement only the scoped change, run verification, commit the work, and keep git clean

Dev Evidence with changed files, work summary, tests run, per-AC verification, caveats

Move to Review only after commit exists and the worktree is clean

Review

Review Guard

Independently verify every acceptance criterion, reject missing evidence, reject scope creep, reject dirty git state, reject broken lint or type checks

Review Findings with verdict, per-AC status, issues found, reviewer notes

Move to Done only with APPROVED verdict

Done

Done Reporter

Treat Done as terminal, do not advance further, and leave behind a concise completion record

Completion Summary with what shipped, key evidence, and completion date

Stay in Done

Blocked

Blocked Resolver

Classify the blocker, explain root cause, and route back only when there is a concrete next step

Blocker Analysis with blocker type, root cause, resolution, and routing decision

Return to Backlog, Todo, Dev, Review, or remain Blocked

### Card Artifacts Grow As The Work Moves Forward

The same card becomes stricter over time:

* Backlog produces the canonical story YAML
* Todo adds the execution brief
* Dev adds evidence of implementation and verification
* Review adds a formal verdict and findings
* Done adds a completion summary

This is why the board is not just visual status. Each column changes what the next specialist is allowed to trust.

### Core Specialist Prompts Under The Board

* ROUTA Coordinator: plans first, never edits files directly, writes the spec, waits for approval, delegates work in waves, and calls GATE for verification after implementation.
* CRAFTER Implementor: stays within task scope, avoids refactors and scope creep, coordinates with other agents when files overlap, runs the verification steps it was given, and commits in small units.
* GATE Verifier: verifies against acceptance criteria only, treats evidence as mandatory, does not allow partial approval, and reports explicit verdicts instead of vague confidence.

The built-in lane prompts live underresources/specialists/workflows/kanban/*.yaml, and the core role prompts live underresources/specialists/core/{routa,crafter,gate}.yaml.

## Why Routa

Single-agent chat works for isolated tasks. It breaks down when the same thread has to do decomposition, implementation, review, evidence collection, and release decisions.

Routa makes those responsibilities explicit:

* Work starts from a workspace, not hidden global repo state
* Kanban lanes route work between specialists instead of mixing every role into one prompt
* Sessions, traces, notes, artifacts, codebases, and worktrees are durable objects
* Provider runtimes are normalized through adapters instead of leaking provider-specific behavior into the product
* The review boundary is a real gate, not just another opinionated reviewer

## What You Can Do Today

* Create workspace-scoped overviews, Kanban boards, sessions, team views, and codebase views
* Run agent sessions with create, prompt, cancel, reconnect, streaming, and trace inspection flows
* Route work across specialist lanes with queueing and per-board automation
* Manage local repositories, worktrees, file search, Git refs, and commit inspection
* Import GitHub repositories as virtual workspaces and browse trees, files, issues, PRs, and comments
* Add MCP tools and custom MCP servers
* Use schedules, webhooks, background tasks, and workflow runs for automation beyond one-off prompts
* Review changes with findings, severity, traces, harness signals, and fitness reports
* Run the product in a local-first desktop mode or a self-hosted web mode

## Quick Start

Choose the shortest path that matches how you want to use Routa.

Surface

Best for

Start

Desktop

Full product experience, visual workflows, local-first usage

Download from 
GitHub Releases

CLI

Terminal-first workflows and scripting

npm install -g routa-cli

Web

Self-hosting or browser-first access

Run from source

### Desktop

1. Download Routa Desktop fromGitHub Releases.
2. Create a workspace.
3. Enable one provider.
4. Attach a repository.
5. Start from Session for ad hoc work, or Kanban for routed delivery.

### CLI

npm install -g routa-cli

routa --help
routa -p 
"
Explain the architecture of this repository
"

routa acp list
routa workspace list

### Web

npm install --legacy-peer-deps
npm run dev

Openhttp://localhost:3000.

## Develop From Source

### Web runtime

npm install --legacy-peer-deps
npm run dev

### Desktop runtime

npm install --legacy-peer-deps
npm --prefix apps/desktop install
npm run tauri:dev

### Docker

docker compose up --build
docker compose --profile postgres up --build

The Tauri smoke path useshttp://127.0.0.1:3210/behind the desktop shell.

## Validation

Usedocs/fitness/README.mdas the canonical validation rulebook.

cargo build -p entrix
entrix run --dry-run
entrix run --tier fast
entrix run --tier normal
npm run 
test

npm run test:e2e
npm run api:test
npm run lint

## Repository Map

Path

Purpose

src/app/

Next.js App Router pages and API routes

src/client/

Client components, hooks, view models, and UI protocol helpers

src/core/

TypeScript domain services for ACP/MCP, Kanban, workflows, traces, review, harness, and stores

apps/desktop/

Tauri shell and desktop packaging

crates/routa-core/

Shared Rust runtime foundation

crates/routa-server/

Axum backend used by desktop and local server mode

crates/routa-cli/

CLI entrypoints and ACP serving commands

crates/harness-monitor/

Run observation, evaluation, and operator-facing harness monitor

docs/ARCHITECTURE.md

Canonical architecture boundaries and invariants

docs/adr/

Architecture decision records

docs/product-specs/FEATURE_TREE.md

Generated route and endpoint inventory

docs/fitness/

Validation and quality gates

## Docs

* Architecture
* ADR Index
* Quick Start
* Feature Tree
* Fitness Rules
* Harness Monitor Architecture
* Contributing
* Security

## License

MIT. SeeLICENSE.

## About

Workspace-first multi-agent coordination platform for AI development, with shared Specs, Kanban orchestration, and MCP/ACP/ A2A support across web and desktop.

phodal.github.io/routa/

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

1.4k

 stars
 

### Watchers

11

 watching
 

### Forks

197

 forks
 

 Report repository

 

## Releases25

Routa Desktop v0.18.1

 Latest

 

Apr 28, 2026

 

+ 24 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript62.8%
* Rust27.4%
* JavaScript3.3%
* Python3.1%
* C#3.0%
* CSS0.3%
* Other0.1%