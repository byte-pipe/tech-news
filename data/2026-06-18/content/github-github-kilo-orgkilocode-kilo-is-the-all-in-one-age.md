---
title: 'GitHub - Kilo-Org/kilocode: Kilo is the all-in-one agentic engineering platform. Build, ship, and iterate faster with the most popular open source coding agent. · GitHub'
url: https://github.com/Kilo-Org/kilocode
site_name: github
content_file: github-github-kilo-orgkilocode-kilo-is-the-all-in-one-age
fetched_at: '2026-06-18T12:19:23.065137'
original_url: https://github.com/Kilo-Org/kilocode
author: Kilo-Org
description: Kilo is the all-in-one agentic engineering platform. Build, ship, and iterate faster with the most popular open source coding agent. - Kilo-Org/kilocode
---

Kilo-Org

 

/

kilocode

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.7k
* Star21.4k

 
 
 
 
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

23,601 Commits
23,601 Commits
.changeset
.changeset
 
 
.github
.github
 
 
.husky
.husky
 
 
.idea
.idea
 
 
.kilo
.kilo
 
 
.kilocode/
skills/
vscode-visual-regression
.kilocode/
skills/
vscode-visual-regression
 
 
.opencode
.opencode
 
 
.vscode
.vscode
 
 
.zed
.zed
 
 
bin
bin
 
 
github
github
 
 
nix
nix
 
 
packages
packages
 
 
patches
patches
 
 
perf
perf
 
 
script
script
 
 
specs
specs
 
 
.editorconfig
.editorconfig
 
 
.envrc
.envrc
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitleaksignore
.gitleaksignore
 
 
.opencode-version
.opencode-version
 
 
.oxlintrc.json
.oxlintrc.json
 
 
.prettierignore
.prettierignore
 
 
AGENTS.md
AGENTS.md
 
 
AgentManagerApp.tsx
AgentManagerApp.tsx
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
PRIVACY.md
PRIVACY.md
 
 
README.ar.md
README.ar.md
 
 
README.bn.md
README.bn.md
 
 
README.br.md
README.br.md
 
 
README.bs.md
README.bs.md
 
 
README.da.md
README.da.md
 
 
README.de.md
README.de.md
 
 
README.es.md
README.es.md
 
 
README.fr.md
README.fr.md
 
 
README.gr.md
README.gr.md
 
 
README.it.md
README.it.md
 
 
README.ja.md
README.ja.md
 
 
README.ko.md
README.ko.md
 
 
README.md
README.md
 
 
README.no.md
README.no.md
 
 
README.pl.md
README.pl.md
 
 
README.ru.md
README.ru.md
 
 
README.th.md
README.th.md
 
 
README.tr.md
README.tr.md
 
 
README.uk.md
README.uk.md
 
 
README.vi.md
README.vi.md
 
 
README.zh.md
README.zh.md
 
 
README.zht.md
README.zht.md
 
 
RELEASING.md
RELEASING.md
 
 
REVIEW.md
REVIEW.md
 
 
SECURITY.md
SECURITY.md
 
 
TESTING.md
TESTING.md
 
 
bun.lock
bun.lock
 
 
bunfig.toml
bunfig.toml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
install
install
 
 
kilocode-2.code-workspace
kilocode-2.code-workspace
 
 
logo.png
logo.png
 
 
package.json
package.json
 
 
screenshot-uk.png
screenshot-uk.png
 
 
tsconfig.json
tsconfig.json
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

English |简体中文|繁體中文|한국어|Deutsch|Español|Français|Italiano|Dansk|日本語|Polski|Русский|Bosanski|العربية|Norsk|Português (Brasil)|ไทย|Türkçe|Українська|বাংলা|Ελληνικά|Tiếng Việt

The open source coding agent for building with AI in VS Code, JetBrains, or the CLI.

Kilo Code is an AI coding agent that meets you everywhere you work:VS Code,JetBrains, and theCLI. It's open source with open pricing. You pick from 500+ models, switch between them mid-task, and pay the model provider's rate with zero markup. No API keys required to start.

### Installation

Pick where you want to run Kilo.

VS Code

Install the Kilo Code extension directly, or grab it from theVS Code Marketplace. Create an account and you'll have access to 500+ models including GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, and Gemini 3.1 Pro Preview, all at provider pricing.

CLI

#
 npm

npm install -g @kilocode/cli

#
 curl

curl -fsSL https://kilo.ai/cli/install 
|
 bash

#
 pnpm

pnpm add -g @kilocode/cli

#
 bun

bun add -g @kilocode/cli

#
 Homebrew (macOS / Linux)

brew install Kilo-Org/tap/kilo

#
 Arch Linux (AUR)

paru -S kilo-bin

Then runkiloin any project directory to start.

JetBrains

Install theKilo Code pluginfrom the JetBrains Marketplace, or search "Kilo Code" inSettings → Pluginsinside any JetBrains IDE.

Cloud Agent

Run Kilo from the web, no local machine needed, atapp.kilo.ai/cloud.

Code Reviews

Set up automated AI code reviews on your pull requests atapp.kilo.ai/code-reviews.

KiloClaw

Spin up your always-on AI agent atapp.kilo.ai/claw.

Install the CLI from GitHub Releases (binaries)

Download the latest binary from theReleases page.

Platform

Asset

Windows (most PCs)

kilo-windows-x64.zip

macOS (Apple Silicon)

kilo-darwin-arm64.zip

macOS (Intel)

kilo-darwin-x64.zip

Linux x64

kilo-linux-x64.tar.gz

Linux ARM

kilo-linux-arm64.tar.gz

Notes:x64-baselineis a compatibility build for older CPUs without AVX.muslis the statically linked build for Alpine or minimal Docker images without glibc.kilo-vscode-*.vsixis the VS Code extension package, not the CLI.Source codearchives are for building from source.

### Agents

Kilo ships with specialized agents you switch between depending on the task. You can also build your own custom agents.

* Code- The default. Implements and edits code from natural language.
* Plan- Designs architecture and writes implementation plans before any code gets written.
* Ask- Answers questions about your codebase without touching any files.
* Debug- Troubleshoots and traces issues.
* Review- Reviews your changes and surfaces issues across performance, security, style, and test coverage.

Learn more aboutagents and custom agents.

### What it does

* Code generationfrom natural language, across multiple files.
* Inline autocompletewith ghost-text suggestions and tab to accept.
* Self-checkingso the agent reviews and corrects its own work.
* Terminal and browser controlto run commands and automate the web.
* MCP marketplaceto find and wire up MCP servers that extend what the agent can do.
* 500+ modelswith mid-task switching, so you can match latency, cost, and reasoning to the job.

### Autonomous Mode (CI/CD)

Runkilo runwith--autofor fully autonomous operation with no prompts, built for CI/CD pipelines:

kilo run --auto 
"
run tests and fix any failures
"

--autodisables all permission prompts and lets the agent execute any action without confirmation. Only use it in trusted environments.

### Documentation

For configuration and everything else,head over to the docs.

### Contributing

Contributions are welcome from developers, writers, and everyone in between. Start with theContributing Guidefor environment setup, coding standards, and how to open a pull request. SeeRELEASING.mdfor the VS Code extension and CLI release process, andpackages/kilo-jetbrains/RELEASING.mdfor the JetBrains plugin.

Please review ourCode of Conductbefore getting involved.

### License

MIT. You're free to use, modify, and distribute this code, including commercially, as long as you keep the attribution and license notices. SeeLicense.

### FAQ

Where did Kilo CLI come from?

Kilo CLI is a fork ofOpenCode, enhanced to work within the Kilo agentic engineering platform.

Join the communityDiscord|X|Reddit

## About

Kilo is the all-in-one agentic engineering platform. Build, ship, and iterate faster with the most popular open source coding agent.

kilo.ai/

### Topics

 cli

 ai

 jetbrains

 vscode

 gemini

 vscode-extension

 claude

 sonnet

 chatgpt

 ai-developer-tools

 ai-coding

 ai-age

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
 

Custom properties
 

### Stars

21.4k

 stars
 

### Watchers

102

 watching
 

### Forks

2.7k

 forks
 

 Report repository

 

## Releases432

v7.3.46 (release)

 Latest

 

Jun 15, 2026

 

+ 431 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript83.6%
* Kotlin12.0%
* CSS3.4%
* HTML0.3%
* JavaScript0.3%
* Tree-sitter Query0.2%
* Other0.2%