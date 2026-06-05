---
title: 'GitHub - CopilotKit/CopilotKit: The Frontend Stack for Agents & Generative UI. React + Angular. Makers of the AG-UI Protocol · GitHub'
url: https://github.com/CopilotKit/CopilotKit
site_name: github
content_file: github-github-copilotkitcopilotkit-the-frontend-stack-for
fetched_at: '2026-06-05T12:03:50.971216'
original_url: https://github.com/CopilotKit/CopilotKit
author: CopilotKit
description: The Frontend Stack for Agents & Generative UI. React + Angular. Makers of the AG-UI Protocol - CopilotKit/CopilotKit
---

CopilotKit

 

/

CopilotKit

Public

* NotificationsYou must be signed in to change notification settings
* Fork4.2k
* Star32.3k

 
 
 
 
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

10,667 Commits
10,667 Commits
.changeset
.changeset
 
 
.claude-plugin
.claude-plugin
 
 
.claude/
docs
.claude/
docs
 
 
.cursor/
rules
.cursor/
rules
 
 
.github
.github
 
 
.superset
.superset
 
 
assets
assets
 
 
codemods
codemods
 
 
community
community
 
 
dev-docs
dev-docs
 
 
docs
docs
 
 
examples
examples
 
 
packages
packages
 
 
scripts
scripts
 
 
sdk-python
sdk-python
 
 
showcase
showcase
 
 
skills
skills
 
 
.browserslistrc
.browserslistrc
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.kodiak.toml
.kodiak.toml
 
 
.mcp.json
.mcp.json
 
 
.npmrc
.npmrc
 
 
.oxfmtrc.json
.oxfmtrc.json
 
 
.oxlintrc.json
.oxlintrc.json
 
 
.pnpmfile.cjs
.pnpmfile.cjs
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
changelog.txt
changelog.txt
 
 
commitlint.config.js
commitlint.config.js
 
 
dangerfile.js
dangerfile.js
 
 
deploy-starter.sh
deploy-starter.sh
 
 
lefthook.yml
lefthook.yml
 
 
nx.json
nx.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
release.config.json
release.config.json
 
 
renovate.json
renovate.json
 
 
View all files

## Repository files navigation

# CopilotKit

Docs·Examples·Enterprise Intelligence Platform·Discord

Buildagent-native applicationswith generative UI, shared state, and human-in-the-loop workflows.

## What is CopilotKit

CopilotKit is a best-in-class SDK for building full-stack agentic applications, Generative UI, and chat applications.

We are the company behind theAG-UI Protocol- adopted by Google, LangChain, AWS, Microsoft, Mastra, PydanticAI, and more!

Whole.Generative.UI.v5.mp4

 Add AI to your app in 1 minute

Features:

* Chat UI– A React-based chat interface that supports message streaming, tool calls, and agent responses.
* Backend Tool Rendering– Enables agents to call backend tools that return UI components rendered directly in the client.
* Generative UI– Allows agents to generate and update UI components dynamically at runtime based on user intent and agent state.
* Shared State– A synchronized state layer that both agents and UI components can read from and write to in real time.
* Human-in-the-Loop– Lets agents pause execution to request user input, confirmation, or edits before continuing.

full-headless-chat.mp4

## Quick Start

### New projects:

npx copilotkit@latest create -f 
<
framework
>

### Existing projects:

npx copilotkit@latest init

cpk-cli.mp4

What this gives you:

* CopilotKit installed– Core packages are fully set up in your app
* Provider configured– Context, state, and hooks ready to use
* Agent <> UI connected– Agents can stream actions and render UI immediately
* Deployment-ready– Your app is ready to deploy

Complete getting started guide →

## How it works:

CopilotKit connects your UI, agents, and tools into a single interaction loop.

This enables:

* Agents that ask users for input
* Tools that render UI
* Stateful workflows across steps and sessions

## ⭐️ useAgent Hook

TheuseAgenthook is a proper superset ofuseCoAgentand sits directly on AG-UI, giving more control over the agent connection.

// Programmatically access and control your agents

const
 
{
 agent 
}
 
=
 
useAgent
(
{
 
agentId
: 
"my_agent"
 
}
)
;

// Render and update your agent's state

return
 
<
div
>

 
<
h1
>
{
agent
.
state
.
city
}
<
/
h1
>

 
<
button
 
onClick
=
{
(
)
 
=>
 
agent
.
setState
(
{
 
city
: 
"NYC"
 
}
)
}
>

 
Set
 
City

 
<
/
b
u
t
t
o
n
>

<
/
div
>

Check out theuseAgent docsto learn more.

CopilotKit.UseAgent.Graphic.Motion_2.mp4

## Generative UI

Generative UI is a core CopilotKit pattern that allows agents to dynamically render UI as part of their workflow.

demo-generative-ui.mp4

### Compare the Three Types

#### Explore:

* Static (AG-UI Protocol)
* Declarative (A2UI)
* Open-Ended (MCP Apps & Open JSON)

Generative UI educational repo →

## 🖥️ AG-UI: The Agent–User Interaction Protocol

Connect agent workflow to user-facing apps, with deep partnerships and 1st-party integrations across the agentic stack—including LangGraph, CrewAI, and more.

npx create-ag-ui-app my-agent-app

 Learn more in the AG-UI README →
 

## 🤝 Community

* What's New

### Have questions or need help?

 Join our Discord →
 
 

 Read the Docs →
 
 

 Try Copilot Cloud →
 

### Stay up to date with our latest releases!

 Follow us on LinkedIn →
 
 

 Follow us on X →
 

## 🙋🏽‍♂️ Contributing

Thanks for your interest in contributing to CopilotKit! 💜

We value all contributions, whether it's through code, documentation, creating demo apps, or just spreading the word.

Here are a few useful resources to help you get started:

* For code contributions,CONTRIBUTING.md.
* For documentation-related contributions,check out the documentation contributions guide.
* Want to contribute but not sure how?Join our Discordand we'll help you out!

## Install as a Claude Code plugin

The CopilotKit monorepo doubles as a Claude Code plugin — all 9 skills (3 package meta-skills + 6 lifecycle journey skills) are available once installed.

Add the repo as a Claude Code marketplace:

claude plugin marketplace add https://github.com/CopilotKit/CopilotKit
claude plugin install copilotkit

Skills are discovered fromskills/<slug>/SKILL.mdat the repo root. The three package meta-skills (runtime,react-core,a2ui-renderer) aregenerated mirrorsof the source-of-truth files atpackages/<pkg>/skills/<pkg>/— do not edit the mirror directly. To update content, edit the source underpackages/*/skills/and run:

pnpm sync:plugin-skills

A lefthook pre-commit check (pnpm check:plugin-skills) rejects commits that drift the mirror. The plugin version is pinned topackages/runtime/package.jsonand is also kept in sync by the same script.

### Skill inventory

Slug

Type

Source

runtime

core

packages/runtime/skills/runtime/

react-core

framework

packages/react-core/skills/react-core/

a2ui-renderer

framework

packages/a2ui-renderer/skills/a2ui-renderer/

0-to-working-chat

lifecycle

skills/0-to-working-chat/

spa-without-runtime

lifecycle

skills/spa-without-runtime/

go-to-production

lifecycle

skills/go-to-production/

scale-to-multi-agent

lifecycle

skills/scale-to-multi-agent/

v1-to-v2-migration

lifecycle

skills/v1-to-v2-migration/

debug-and-troubleshoot

lifecycle

skills/debug-and-troubleshoot/

## 📄 License

This repository's source code is available under theMIT License.

## About

The Frontend Stack for Agents & Generative UI. React + Angular. Makers of the AG-UI Protocol

docs.copilotkit.ai

### Topics

 react

 agent

 open-source

 typescript

 ai

 js

 reactjs

 nextjs

 ts

 assistant

 copilot

 agents

 assistant-chat-bots

 ai-assistant

 ai-agent

 llm

 copilot-chat

 generative-ui

 agentic-ai

 agent-native

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

32.3k

 stars
 

### Watchers

161

 watching
 

### Forks

4.2k

 forks
 

 Report repository

 

## Releases1,371

v1.59.5

 Latest

 

Jun 5, 2026

 

+ 1,370 releases

## Used by1.7k

 + 1,680
 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript79.2%
* MDX8.4%
* Python6.4%
* CSS1.3%
* C#0.8%
* Vue0.7%
* Other3.2%