---
title: 'GitHub - CodebuffAI/freebuff: The free coding agent · GitHub'
url: https://github.com/CodebuffAI/freebuff
site_name: github
content_file: github-github-codebuffaifreebuff-the-free-coding-agent-gi
fetched_at: '2026-08-19T19:23:00.118531'
original_url: https://github.com/CodebuffAI/freebuff
author: CodebuffAI
description: The free coding agent. Contribute to CodebuffAI/freebuff development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 CodebuffAI

 

/

freebuff

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.1k
* Star10.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

8,563 Commits
8,563 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
agents
agents
 
 
assets
assets
 
 
cli
cli
 
 
common
common
 
 
docs
docs
 
 
evals
evals
 
 
freebuff
freebuff
 
 
packages
packages
 
 
scripts/
tmux
scripts/
tmux
 
 
sdk
sdk
 
 
.bun-version
.bun-version
 
 
.codebuffignore
.codebuffignore
 
 
.gitignore
.gitignore
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
SECURITY.md
SECURITY.md
 
 
WINDOWS.md
WINDOWS.md
 
 
bun.lock
bun.lock
 
 
bunfig.toml
bunfig.toml
 
 
eslint.config.js
eslint.config.js
 
 
package.json
package.json
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# Freebuff

English |简体中文

Five free AI products for coding, building, and research.No subscription, credits, or API key required.

Freebuffbrings specialized agents and a choice of leading models to your terminal, desktop, browser, and GitHub repositories. Text ads support access to the included models.

## Choose your Freebuff

Product

What it does

Get started

Freebuff Desktop

Run parallel agents locally

Download for macOS, Windows, or Linux

Freebuff CLI

Code from your terminal

Install the CLI

Freebuff Web

Build and ship full-stack apps

Build an app

Freebuff Cloud

Run agents on any GitHub repository

Connect a repository

Freebuff Chat

Research and think with AI

Start a chat

## Quick start

Run Freebuff in any project from your terminal:

npm install -g freebuff

cd
 
~
/my-project
freebuff

Then describe what you want. Freebuff finds the relevant files, makes changes, and runs the checks that matter for your project.

## Models

Freebuff includes a curated model catalog. The regular picker currently offers:

Model

Access

Best for

DeepSeek V4 Pro 08/13

Full access

The default everywhere in full mode; deepest reasoning

DeepSeek V4 Flash 07/31

Full access

Fast coding and tool use, no premium session

GPT-5.6 Luna

Full access

Deep reasoning with native image support

MiniMax M3

Full access

Fast responses with image support

MiMo 2.5

Full and limited access

The limited-mode default; balanced performance with image support

Beyond the regular picker:

* GLM 5.2is available through earned sessions rather than as an always-unlocked model.
* Gemini 3.1 Flash Litepowers specialist tasks such as file finding and research rather than appearing in the main picker.

Availability and limits depend on your access tier, product, and current capacity. Freebuff Desktop can also run locally installed Claude Code and Codex agents using your existing provider account; those connected models are separate from Freebuff's included catalog.

## How Freebuff works

Freebuff uses specialized agents instead of sending every task through one model and one prompt. Depending on the task, agents gather context, plan, edit or research, run tools, and review the result.

* Codebase context— File-finding agents map the relevant parts of a project before editing.
* Implementation and review— Agents can divide work, make changes, run commands, and inspect the result.
* Research and browser use— Agents can investigate documentation and test applications in a real browser.
* Parallel local work— Desktop isolates concurrent agents in separate workspaces.
* Hosted environments— Web and Cloud provide sandboxes, previews, terminals, and deployment workflows.

## Free access

Freebuff is available in every country. Supported regions receive full access; other regions and VPN users receive limited access, currently MiMo 2.5 with three one-hour sessions per day, earnable up to seven.

Text ads support the included models. Freebuff shows the applicable session limits and any model-specific data-use notice before you start.

Is my data used to train AI?Only when a model or feature says data may be used for AI training. Freebuff or the provider may then keep submissions to develop, train, test, evaluate, fine-tune, and improve AI models or products.

How is my data used and stored?We use prompts, messages, code, files, and repository data to provide the service. We may analyze prompts and messages—including pasted content—to personalize ads, using Freebuff systems and service providers acting on our behalf. Separate uploads and connected repositories are not provided to advertising providers. Where required by law, we provide advertising choices and honor recognized opt-out signals; elsewhere, this processing may be required to use the free service. See the Privacy Policy for retention and details.

See thePrivacy Policyfor complete details.

## Contributing

Freebuff is a TypeScript monorepo built with Bun. Contributions to the products, agents, tools, documentation, and underlying runtime are welcome.

Local development requires Docker and a configured.env.local; see theContributing Guidebefore starting the services.

git clone https://github.com/CodebuffAI/freebuff.git

cd
 freebuff
bun install
bun up

Start the CLI separately with:

bun start-cli

See theContributing Guide,development guide, andtesting guidefor environment setup and the checks to run before opening a pull request.

## Built on Codebuff

Freebuff is built onCodebuff, the open multi-agent framework that powers its orchestration, tools, and SDK. To create custom agents or embed them in another application, see theCodebuff documentationand@codebuff/sdk.

## Links

* Website
* GitHub
* Discord
* Privacy Policy
* License