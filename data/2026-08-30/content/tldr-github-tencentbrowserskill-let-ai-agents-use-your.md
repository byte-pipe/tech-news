---
title: 'GitHub - Tencent/BrowserSkill: Let AI agents use your real, logged-in browser without interrupting your work. CLI + extension for browser automation across any shell-capable AI agent. · GitHub'
url: https://github.com/Tencent/BrowserSkill
site_name: tldr
content_file: tldr-github-tencentbrowserskill-let-ai-agents-use-your
fetched_at: '2026-08-30T06:00:40.554087'
original_url: https://github.com/Tencent/BrowserSkill
date: '2026-08-30'
description: Let AI agents use your real, logged-in browser without interrupting your work. CLI + extension for browser automation across any shell-capable AI agent. - Tencent/BrowserSkill
tags:
- tldr
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 Tencent

 

/

BrowserSkill

Public

* NotificationsYou must be signed in to change notification settings
* Fork119
* Star1.5k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

244 Commits
244 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github/
workflows
.github/
workflows
 
 
apps/
extension
apps/
extension
 
 
crates
crates
 
 
docs
docs
 
 
evals/
browser
evals/
browser
 
 
packages
packages
 
 
scripts
scripts
 
 
skill
skill
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
.stylelintignore
.stylelintignore
 
 
.stylelintrc.json
.stylelintrc.json
 
 
AGENT_INSTALL.md
AGENT_INSTALL.md
 
 
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
 
 
biome.json
biome.json
 
 
clippy.toml
clippy.toml
 
 
install.ps1
install.ps1
 
 
install.sh
install.sh
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
View all files

## Repository files navigation

# BrowserSkill

Let AI agents use your browser without interrupting your work.

English ·中文

BrowserSkillconnects Cursor, Claude Code, Codex, OpenClaw, CodeBuddy,
WorkBuddy, Pi, Hermes Agent, DeepSeek Harness, and other AI agents to your already logged-in
browser.

Need the agent to touch a tab you already have open? It must borrow that tab
explicitly, return it when the task is done, and leave the rest of your browser
alone.

github.-.mp4

## BrowserSkill Advantages

* Reuse real login state: Agents can work with sites you are already signed
into, without separate test accounts.
* Keep working uninterrupted: browser tasks run in a separate, visible
Agent Window, so you can keep using your own browser.
* Support any Agent: any Agent that can call a shell can use BrowserSkill
through thebskCLI, with no lock-in to a specific model, Agent framework, or
harness.
* Built-in human-in-loop: when a task hits captcha, login, confirmation
dialogs, or other human-only steps, the Agent can ask you to take over and
then continue afterwards.

## Runtime Environment

BrowserSkill has two local runtime pieces: thebskCLI/daemon and the browser
extension.

Runtime

Support

Operating systems

macOS (Apple Silicon and Intel), Linux (x64 and ARM64), Windows x64

Browsers

Chrome and Microsoft Edge are supported; other Chromium-based browsers are expected to work when they support unpacked Chromium extensions; Firefox is planned

## Quick Start

Install with your Agent (recommended)

Already using Cursor, Claude Code, Codex, or another shell-capable agent? Just
copy this one line and send it to your agent — it will install the CLI and skill
for you, then walk you through loading the extension:

Set up browser-skill on this machine by following https://raw.githubusercontent.com/Tencent/BrowserSkill/main/AGENT_INSTALL.md

Manual install

Install the CLI, then install the extension from theChrome Web StoreorEdge Add-ons.

#### 1. Install thebskCLI

macOS / Linux(recommended — installs to~/.local/bin):

curl -fsSL https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.sh 
|
 sh

Windows(PowerShell — installs to~/.local/bin):

irm https:
//
raw.githubusercontent.com
/
Tencent
/
BrowserSkill
/
main
/
install.ps1 
|
 iex

Verify the binary:

bsk --version

#### 2. Install the browser extension

Install BrowserSkill from your browser's store:

Browser

Store listing

Chrome

Chrome Web Store

Microsoft Edge

Edge Add-ons

On other Chromium-based browsers, install the Chrome Web Store build.

#### 3. Install the skill

BrowserSkill ships a skill that teaches your agent harness how to usebsk. For
these harnesses, install it in one step:

Cursor

Claude Code

Codex

OpenClaw

CodeBuddy

WorkBuddy

Pi

Hermes Agent

bsk install-skill

UseSpaceto select the Agent harness you want to install into, then
pressEnterto install the skill. Runbsk install-skill --listto see
internal variants and install paths.

Other shell-capable agent harnesses are supported too. Copyskill/SKILL.mdinto your harness's skills directory asbrowser-skill/SKILL.mdto install the skill manually. DeepSeek Harness uses a
dedicated plugin instead — seeDeepSeek Harness plugin.

Start a new Agent session and write a prompt that needs the browser, for example:

/browser-skill open example.com and summarize what is on the page.

## DeepSeek Harness plugin

UsingDeepSeek Harness(dsh)?
BrowserSkill ships a first-class dsh plugin on npm as@wxg-prc-cpg/browser-skill-dsh-plugin.
It injects nativebrowser_*tools (no shelling out tobsk) and a live Web UI
overlay of each Agent Window.

Add it to a dsh profile, then start that profile:

dsh plugin --profile web add @wxg-prc-cpg/browser-skill-dsh-plugin
dsh --profile web

The plugin carries its own copy of the skill, sobsk install-skillis not needed
for dsh — but thebskCLI and the browser extension are still prerequisites. See
theplugin READMEfor the tool list,
configuration, and the observation overlay.

## How It Works

BrowserSkill is a local bridge between your agent harness and your browser.

flowchart TB
 subgraph Harness["Agent Harness"]
 Agent["Cursor / Claude Code / Codex / OpenClaw"]
 end

 subgraph Local["Your Machine"]
 CLI["bsk CLI"]
 Daemon["bsk daemon"]
 Extension["BrowserSkill extension"]
 end

 subgraph Browser["Browser Profile"]
 AgentWindow["Agent Window"]
 UserWindows["Your normal browser windows"]
 end

 Agent -->|"shell: bsk ..."| CLI
 CLI -->|"local IPC"| Daemon
 Daemon -->|"WebSocket on 127.0.0.1"| Extension
 Extension -->|"automates"| AgentWindow
 Extension -.->|"borrow tab only when asked"| UserWindows

 style AgentWindow fill:#fff4e6,stroke:#f59e0b,stroke-width:2px,color:#111827
 style UserWindows fill:#f8fafc,stroke:#cbd5e1,color:#334155

 
Loading

The agent never talks to the browser directly. It asks thebskCLI to perform a
browser task; the local daemon routes that request to the extension; the
extension runs it in an Agent Window. DeepSeek Harness takes the same path
through theplugin: the agent calls injectedbrowser_*tools, and the plugin invokesbskon its behalf.

## For Developers

The repository is a Cargo + pnpm workspace:

* crates/bsk-cli—bskCLI and local daemon
* crates/bsk-protocol— shared wire types and JSON schemas
* apps/extension— browser extension
* packages/uiandpackages/i18n— shared extension UI support
* packages/dsh-plugin-browserskill— DeepSeek Harness plugin (@wxg-prc-cpg/browser-skill-dsh-plugin)
* evals/browser— deterministic local pages and agent-neutral browser capability evaluation

## License

MIT