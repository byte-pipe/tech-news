---
title: 'GitHub - MoonshotAI/kimi-code: Kimi Code CLI — The Starting Point for Next-Gen Agents · GitHub'
url: https://github.com/MoonshotAI/kimi-code
site_name: github
content_file: github-github-moonshotaikimi-code-kimi-code-cli-the-start
fetched_at: '2026-07-22T11:37:28.029168'
original_url: https://github.com/MoonshotAI/kimi-code
author: MoonshotAI
description: Kimi Code CLI — The Starting Point for Next-Gen Agents - MoonshotAI/kimi-code
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 MoonshotAI

 

/

kimi-code

Public

* NotificationsYou must be signed in to change notification settings
* Fork660
* Star4.5k

 
 
 
 
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

957 Commits
957 Commits
.agents/
skills
.agents/
skills
 
 
.changeset
.changeset
 
 
.github
.github
 
 
apps
apps
 
 
build
build
 
 
docs
docs
 
 
packages
packages
 
 
plugins
plugins
 
 
scripts
scripts
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.npmrc
.npmrc
 
 
.nvmrc
.nvmrc
 
 
.oxfmtrc.json
.oxfmtrc.json
 
 
.oxlintrc.json
.oxlintrc.json
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
GOAL.md
GOAL.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SECURITY.md
SECURITY.md
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.json
tsconfig.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

# Kimi Code CLI

Documentation·Issues·中文

## What is Kimi Code CLI

Kimi Code CLI is an AI coding agent that runs in your terminal — it can read and edit code, run shell commands, search files, fetch web pages, and choose the next step based on the feedback it receives. It works out of the box with Moonshot AI’s Kimi models and can also be configured to use other compatible providers.

## Install

Install with the official script. No Node.js required.

* macOS or Linux:

curl -fsSL https://code.kimi.com/kimi-code/install.sh 
|
 bash

* Windows (PowerShell):

irm https:
//
code.kimi.com
/
kimi
-
code
/
install.ps1 
|
 iex

On Windows, installGit for Windowsbefore first launch because Kimi Code CLI uses the bundled Git Bash as its shell environment. If Git Bash is installed in a custom location, setKIMI_SHELL_PATHto the absolute path ofbash.exe.

Then, run it with a new shell session:

kimi --version

For npm install, upgrade, uninstall, seeGetting Started.

## Quick Start

Open a project and start the interactive UI:

cd
 your-project
kimi

On first launch, run/logininside Kimi Code CLI and choose either Kimi Code OAuth or a Moonshot AI Open Platform API key. After login, try your first task:

Take a look at this project and explain its main directories.

## Key Features

* Single-binary distribution.Install with one command: no Node.js setup, PATH gymnastics, or global module conflicts.
* Blazing-fast startup.The TUI is ready in milliseconds, so starting a session never feels heavy.
* Purpose-built TUI.A carefully tuned interface, optimized end to end for long, focused agent sessions.
* Video input.Drop a screen recording or demo clip into the chat and let the agent watch what is hard to describe in words — turn a reference clip into a LUT, a long video into a short, a screen recording into working code, and more.
* AI-native MCP configuration.Add, edit, and authenticate Model Context Protocol servers conversationally with/mcp-config, without hand-editing JSON.
* Rich plugin ecosystem.Install skills, MCP servers, and data sources from the marketplace or any GitHub repo, with each install's trust level surfaced up front.
* Subagents for focused, parallel work.Dispatch built-incoder,explore, andplansubagents in isolated contexts while keeping the main conversation clean.
* Lifecycle hooks.Run local commands at key points to gate risky tool calls, audit decisions, trigger desktop notifications, or connect to your own automation.
* Editor & IDE integration (ACP).Drive a Kimi Code CLI session straight from Zed, JetBrains, or anyAgent Client Protocolclient withkimi acp.

## Use it in your editor (ACP)

Kimi Code CLI speaks theAgent Client Protocol, so ACP-compatible editors and IDEs (Zed, JetBrains, …) can drive a session over stdio. Log in once, then point your editor at thekimi acpsubcommand — no extra login needed.

For Zed, add this to~/.config/zed/settings.json:

{
 
"agent_servers"
: {
 
"Kimi Code CLI"
: {
 
"type"
: 
"
custom
"
,
 
"command"
: 
"
kimi
"
,
 
"args"
: [
"
acp
"
],
 
"env"
: {}
 }
 }
}

Then open a new conversation in Zed's Agent panel. SeeUsing in IDEsfor JetBrains setup and troubleshooting, and thekimi acpreferencefor the full capability matrix.

## Docs

* Getting Started
* Interaction and approvals
* Sessions
* Using in IDEs (ACP)
* Configuration
* Command reference

## Develop

Requirements: Node.js ≥ 24.15.0, pnpm 10.33.0.

git clone https://github.com/MoonshotAI/kimi-code.git

cd
 kimi-code
pnpm install

pnpm dev:cli 
#
 run the CLI in dev mode

pnpm 
test
 
#
 run tests

pnpm typecheck 
#
 TypeScript check

pnpm lint 
#
 oxlint

pnpm build 
#
 build all packages

SeeCONTRIBUTING.mdfor the full contribution guide.

## Community

* Issues
* For security vulnerabilities, seeSECURITY.md.

## Acknowledgements

Our TUI is built on top ofpi-tui. We thank the authors ofpi-tuifor their valuable work.

## License

Released under theMIT License.

## About

Kimi Code CLI — The Starting Point for Next-Gen Agents

moonshotai.github.io/kimi-code/

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
 

Custom properties
 

### Stars

4.5k

 stars
 

### Watchers

20

 watching
 

### Forks

660

 forks
 

 Report repository

 

## Releases53

@moonshot-ai/kimi-code@0.29.0

 Latest

 

Jul 22, 2026

 

+ 52 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript94.9%
* Vue3.8%
* JavaScript1.1%
* CSS0.2%
* Nix0.0%
* Shell0.0%