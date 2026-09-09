---
title: 'GitHub - vastsa/PI-Desktop: Local-first AI coding agent desktop: Electron + Rust host core + pi Agent Harness + user-installable plugins · GitHub'
url: https://github.com/vastsa/PI-Desktop
site_name: github
content_file: github-github-vastsapi-desktop-local-first-ai-coding-agen
fetched_at: '2026-09-09T15:29:49.183518'
original_url: https://github.com/vastsa/PI-Desktop
author: vastsa
description: 'Local-first AI coding agent desktop: Electron + Rust host core + pi Agent Harness + user-installable plugins - vastsa/PI-Desktop'
---

vastsa

 

/

PI-Desktop

Public

* NotificationsYou must be signed in to change notification settings
* Fork147
* Star1.5k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,017 Commits
2,017 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.cargo
.cargo
 
 
.github
.github
 
 
apps
apps
 
 
crates
crates
 
 
docs
docs
 
 
examples
examples
 
 
packages
packages
 
 
scripts
scripts
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
AGENTS.md
AGENTS.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.base.json
tsconfig.base.json
 
 
View all files

## Repository files navigation

# PI-Desktop

### Your local-first desktop workspace for AI coding agents.

Bring your own model. Open any local project. Let agents work — while you stay in control.

No PI-Desktop account. No mandatory relay. No editor lock-in.

Download PI-Desktop·Documentation·Screenshots·简体中文

A standalone desktop workspace for coding agents, projects, models, tools, and long-running sessions.

Important

PI-Desktop is currently in Early Preview.

The project is actively developed and already usable for real coding workflows, but APIs, extension interfaces, and some desktop behaviors may continue to evolve.

## Why PI-Desktop?

Most coding agents live inside a terminal, an editor extension, or a hosted service.

PI-Desktop gives them a workspace of their own.

### 🖥️ Desktop-first

Work across repositories and sessions without tying your agent workflow to one editor or terminal.

Projects, conversations, reviews, files, previews, notifications, and extensions live in one workspace.

### ✨ Bring your own model

Use OpenAI, Anthropic, local models, hosted gateways, or any OpenAI-compatible API.

Configure multiple providers and models, then switch between them per session.

### 🔍 Inspectable by default

Agents can read files, edit code, and run commands — but privileged actions pass through PI-Desktop's permission layer.

Review diffs, inspect command output, and decide how much autonomy each session gets.

### 🧩 Built to extend

Add Skills, MCP servers, Subagents, and installable Plugins.

Plugins can contribute tools, commands, panels, themes, services, skills, and new workspace experiences.

## From prompt to patch

Getting started only takes a few steps:

1. Connect a modelOpenSettings → Model configuration, choose a provider or compatible API, and add your credentials.
2. Open a projectAdd any local repository or project directory from the sidebar.
3. Pick Agent, Plan, or GoalAgentstarts working.Planwaits until you approve a frozen implementation plan.Goalwaits until you approve the outcome, then the agent chooses the path.
4. Review the resultInspect edits in the Review panel, check command output, preview the application, and continue the conversation without leaving PI-Desktop.

## More than a chat window

### Agent, Plan, and Goal

Same agent. Three gates. Privileged tools still go through the permission layer in every mode.

Agent

Plan

Goal

You approve

Nothing extra

The implementation plan

The outcome and acceptance criteria

The agent does

Reads, edits, runs commands, tests, iterates

Studies the repo, writes a frozen plan, then waits

Picks the path and works until the goal is met

Use when

You want it to just do the work

The change is large or risky and you want the approach first

You care about the result, not the route

Agentis the default loop: inspect the tree, patch files, run commands, and keep going.

Planis the approval boundary. The agent researches first and produces an immutable implementation plan. Execution does not start until you sign off.

Goalis outcome-first. You lock the objective and acceptance criteria; the agent decides how to get there.

### Delegate work to Subagents

Large tasks rarely belong in one context window.

PI-Desktop can delegate independent work to background Subagents for things like:

* codebase exploration
* multi-file implementation
* research and investigation
* test analysis
* adversarial review

Each Subagent runs in its own context and reports its result back to the parent agent.

### A workspace built for long sessions

PI-Desktop is designed for more than one prompt at a time.

You can manage multiple projects and sessions, pin or archive conversations, branch sessions, queue prompts while an agent is running, reference files with@, use slash commands, and search across the application.

Streaming responses are checkpointed so interrupted work can survive application restarts or runtime failures whenever possible.

## Your models, your choice

PI-Desktop does not lock the agent runtime to a hardcoded model list.

Use:

* OpenAI and Anthropic
* OpenAI-compatible APIs
* hosted model gateways
* local gateways such as Ollama and LM Studio
* multiple models under the same provider
* provider OAuth accounts where supported

Model configuration can include context windows, output limits, reasoning controls, temperature, and other model-specific behavior.

Switch models directly from the Composer without recreating your session.

## Review the work, not just the answer

The agent workspace includes dedicated surfaces for the things that matter while coding:

Long-running conversations with transcript navigation

Switch providers, models, and reasoning levels per session

Extend the workspace through the plugin marketplace

Add a provider and connect a model

Explore all screenshots →

## Extensions without rebuilding the app

PI-Desktop has several extension layers depending on how deeply you want to customize the agent.

### Skills

Give agents reusable instructions and workflows.

Skills can be installed globally or activated for individual projects.

### MCP

Connect external tools and services through Model Context Protocol servers without baking them into the desktop application.

### Subagents

Create specialized agents with their own instructions, tools, and model choices, then delegate work to them from another agent.

### Plugins

Plugins can extend PI-Desktop itself with:

* agent tools
* commands
* workspace panels
* work-panel views
* Skills
* MCP servers
* Subagents
* themes
* resident services
* inter-plugin messaging

Plugins can be installed locally or through the marketplace using the.piplugpackage workflow.

Note

Plugin processes are permission-gated and isolated from the renderer, but plugins are still user-trusted code rather than a complete operating-system sandbox. Only install plugins you trust.

Build your first plugin →

## Local-first, precisely

PI-Desktop islocal-first, not “nothing ever touches the network.”

Data

Behavior

Conversations

Stored locally as JSONL with a SQLite index

Settings

Stored on your machine

API credentials

Stored in the operating system keychain

Logs

Local

PI-Desktop telemetry

None

Model requests

Sent directly to the provider or endpoint you configure

There is no required PI-Desktop account and no mandatory PI-hosted relay between your machine and your model provider.

If you use a remote model provider, the context required for that model request is naturally sent to that provider according to its own privacy policy.

## Download

Download the latest build fromGitHub Releases.

Platform

Architecture

Package

macOS

Apple Silicon

.dmg
 / 
.zip

macOS

Intel

.dmg
 / 
.zip

Windows

x64

NSIS installer / portable exe

Linux

x64

.AppImage
 / 
.deb
 / 
.rpm
 / 
.asar

Packaged builds can check GitHub Releases for updates and surface new versions inside the application. Windows NSIS and Linux AppImage can download and install in-app; macOS, Linux deb/rpm, and the Windows portable exe open the releases page. The Linux.asarasset is available for repackaging with a system Electron; launch it withelectron PI-Desktop-<version>-linux-x64.asarafter adding the native host and packaged resources required by the target distribution.

### Linux

Linux x64 packages needglibc 2.35or newer. That is the library shipped with:

* Ubuntu 22.04 or later
* Debian 12 or later
* Fedora 36 or later

Ubuntu 20.04, Debian 11, Fedora 35, and older releases cannot load the bundled host. Check withldd --version.

### macOS

The tagged-release workflow signs, notarizes, and staples macOS artifacts with
Developer ID credentials before publication.

## Import your existing sessions

Already using another coding agent?

PI-Desktop can import local sessions from supported tools including:

* Claude Code
* Codex
* OpenCode
* Pi

OpenSettings → Importto bring existing work into the desktop workspace.

## Architecture

PI-Desktop deliberately separates the user interface from privileged host capabilities and the agent loop.

flowchart TB
 UI["React Renderer<br/>Chat · Projects · Reviews · Settings"]
 Electron["Electron Main<br/>Desktop orchestration"]
 Rust["Rust Host Core<br/>Permissions · Filesystem · SQLite · Secrets"]
 Agent["pi Agent Sidecar<br/>Agent loop · Models · Streaming"]
 Provider["Model Provider<br/>Cloud or Local"]

 UI --> Electron
 Electron --> Rust
 Electron --> Agent
 Agent <--> Rust
 Agent --> Provider

 
Loading

The renderer has no Node integration.

TheRust Host Coreowns privileged workspace operations, permissions, persistence, and secrets. Thepi Agent Sidecarowns model interaction and the agent loop. Electron coordinates the desktop lifecycle while keeping those responsibilities separated.

Read the architecture specification →

## Project status

PI-Desktop is an early preview under active development.

The current0.14.xline includes the desktop shell, streaming agent runtime, Agent / Plan / Goal workflows, permission-aware workspace tools, projects and sessions, session imports, MCP / Skills / Subagents, background delegation, multi-provider model configuration, plugins and marketplace support, context checkpoints, notifications, release notes, and cross-platform packaging.

Current priorities include:

* macOS tagged-release qualification
* installer upgrade and rollback qualification
* continued runtime and session-recovery hardening
* stronger plugin sandboxing and publisher verification
* broader UI-driven end-to-end coverage

Follow development through theproject boardandmilestones.

## Development

### Requirements

* Node.js>=22.19
* pnpm>=10
* stable Rust toolchain

The repository currently pins pnpm 11, while CI and release builds use Node 24.

### Run locally

git clone https://github.com/vastsa/PI-Desktop.git

cd
 PI-Desktop

pnpm install

cargo build -p host-core
pnpm build:js

pnpm dev

### Validate changes

pnpm typecheck
pnpm lint
pnpm 
test

Additional protocol, Plan, supervision, Subagent, and Electron E2E suites are documented in the repository specification.

### Documentation

pnpm docs:dev
pnpm docs:check

Useful references:

* Documentation
* Specification index
* Architecture
* Product scope
* Plugin development
* E2E test plan
* Release runbook
* Repository agent guide

## Contributing

Issues, bug reports, feature proposals, documentation improvements, and pull requests are welcome.

For larger changes, opening an issue first makes it easier to align the implementation with the existing architecture and product contracts.

When working in the repository, start withAGENTS.mdand thespecification index.

Report an issue·View open issues

## Built on open source

PI-Desktop builds on the excellent work of the open-source ecosystem.

The agent runtime usespi-aiandpi-agent-corefrompi-mono.

The desktop application is built with technologies including Electron, React, TypeScript, Rust, SQLite, Vite, Tailwind CSS, Shiki, Mermaid, KaTeX, TypeBox, and i18next.

Thank you to every project and contributor that makes PI-Desktop possible.

## Model acknowledgements

This project was created by the models below — not by a lone genius, but by a token-powered construction crew.

Provider

Model

Tokens

OpenAI

gpt-5.6-luna

5,304,019,817

OpenAI

gpt-5.6-sol

4,825,458,273

OpenAI

gpt-5.4

4,213,269,324

Anthropic

claude-opus-5

3,909,952,653

OpenAI

gpt-5.5

3,800,382,171

xAI

grok-4.5

1,947,736,115

xAI

grok-4.6

797,233,571

DeepSeek

deepseek-v4-flash

329,790,234

OpenAI

gpt-5.2-codex

320,983,170

Xiaomi

mimo-v2.5-pro

304,822,052

Anthropic

claude-fable-5-1

302,580,552

OpenAI

gpt-5.6-terra

274,107,085

OpenAI

gpt-5.3-codex

255,366,945

OpenAI

gpt-5.1-codex-max

220,947,212

OpenAI

gpt-5.1

142,533,699

—

Unknown model

69,801,632

Anthropic

claude-opus-4.6

55,223,768

Zhipu

stealth/ox-alpha

22,954,876

Anthropic

claude-fable-5

16,116,907

OpenAI

gpt-5.1-codex-mini

12,895,478

Xiaohongshu

dots-3-note-prev

10,166,895

OpenAI

gpt-5.1-codex

3,916,509

Xiaomi

mimo-v2.5

3,785,071

Total for listed models:27,144,044,009 tokens.

## Community Links

* Linux.Do— A community for sharing and discussing technology.

## License

PI-Desktop is licensed under theGNU Lesser General Public License v3.0.

SeeLICENSEfor details.

### Build with the model you want. Keep the workflow yours.

Download PI-Desktop

macOS · Windows · Linux