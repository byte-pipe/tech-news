---
title: 'GitHub - strands-agents/harness-sdk: Build an agent harness and control it end-to-end. Open-source SDK for production AI agents in Python & TypeScript - any model, any cloud. · GitHub'
url: https://github.com/strands-agents/harness-sdk
site_name: github
content_file: github-github-strands-agentsharness-sdk-build-an-agent-ha
fetched_at: '2026-09-23T15:19:19.618294'
original_url: https://github.com/strands-agents/harness-sdk
author: strands-agents
description: Build an agent harness and control it end-to-end. Open-source SDK for production AI agents in Python & TypeScript - any model, any cloud. - strands-agents/harness-sdk
---

strands-agents

 

/

harness-sdk

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.2k
* Star7.7k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

2,755 Commits
2,755 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents
.agents
 
 
.claude
.claude
 
 
.github
.github
 
 
.husky
.husky
 
 
.kiro
.kiro
 
 
harness-py
harness-py
 
 
harness-ts
harness-ts
 
 
site
site
 
 
strands-cli
strands-cli
 
 
strands-mcp
strands-mcp
 
 
strands-py
strands-py
 
 
strands-ts
strands-ts
 
 
team
team
 
 
test-infra
test-infra
 
 
.codecov.yml
.codecov.yml
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.node-version
.node-version
 
 
.prettierrc
.prettierrc
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE.APACHE
LICENSE.APACHE
 
 
NOTICE
NOTICE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# Strands Agents

## A model-driven approach to building AI agents in just a few lines of code.

Documentation◆Samples◆MCP Server◆Discord

Strands Agents is an open-source SDK for building and running AI agents in Python and TypeScript. Choose Strands when you would otherwise write your own agent loop: it runs in your process with no hosted control plane, and it covers the jobs a hand-rolled loop grows into. In one SDK you getlifecycle controls(turn limits, token budgets, cancellation, stop reasons),toolsandstructured output,MCP,multi-agent patterns,memoryandsessions,model portability,streaming,guardrails,tracing, andevals.

This monorepo contains Strands harness, the Python and TypeScript SDKs, the documentation site, and supporting packages:

Directory

Description

harness-py/

Python Strands harness: fully assembled agent via 
create_harness()
 (
PyPI
 · 
docs
)

harness-ts/

TypeScript Strands harness: fully assembled agent via 
createHarness()
 (
npm
 · 
docs
)

strands-cli/

strands
 CLI: prototype and chat with a harness agent from the terminal (
npm
)

strands-py/

Python SDK: agent loop, model providers, tools (
PyPI
 · 
releases
)

strands-ts/

TypeScript SDK: agent loop, model providers, tools (
npm
 · 
releases
)

site/

Source for the 
strandsagents.com
 documentation site (Astro/Starlight)

team/

Governance and cross-SDK process docs (tenets, decisions, PR & compatibility guidelines, and 
designs/
 proposals)

## Why Strands

Build an agent harness. Control it end-to-end.

* Build your way.Any model, any cloud. Context management, execution limits, and observability built in before you write a line of config. Swap backends when you scale; your code stays the same.
* Model agnostic.First-class support for Amazon Bedrock, Anthropic, OpenAI, and Gemini, plusmany more providersand custom ones.
* Stay in control.The agent loop traces every decision by default. Hooks let you intercept any step to log it, validate it, or redirect it.
* Deliver outcomes that work.Guardrails catch mistakes before they run. Steering handlers let agents correct themselves instead of failing silently.

MCP, streaming, multi-agent patterns, and structured output are all built in.

## Quick Start

The easiest way to get started is withStrands harness, a fully assembled, state-of-the-art agent. A singlecreate_harness()(Python) orcreateHarness()(TypeScript) call gives you an optimized agent with benchmarked defaults for the model, tools, memory, sessions, and context management — ready to take from idea to production. Follow theharness quickstart, or see thePython Strands harnessandTypeScript Strands harnesspackages to get started.

### Python

pip install strands-harness

from
 
strands_harness
 
import
 
create_harness

agent
 
=
 
create_harness
()

agent
(
"Find the slowest test in this repo and explain why it's slow"
)

### TypeScript

npm install @strands-agents/harness

import
 
{
 
createHarness
 
}
 
from
 
'@strands-agents/harness'

const
 
agent
 
=
 
await
 
createHarness
(
)

await
 
agent
.
invoke
(
"Find the slowest test in this repo and explain why it's slow"
)

Start here to get a batteries-included agent, then drop down to the SDKs below when you want to own the agent loop and wire up tools, model providers, and memory yourself. Theharness configuration referencedocuments every default you can override.

TheQuickstart Guidecovers configuring providers (Amazon Bedrock, Anthropic, OpenAI, Gemini, Ollama, and more).

## Working with the SDK

The Strands Harness SDK lets you go deeper and control every part of the agent: the loop, tools, model providers, memory, sessions, and hooks. You can dive into the SDK after working with Strands harness or if you prefer building your own harness from the ground up when the assembled defaults aren't enough.

### Python

Requires Python 3.10+:

pip install strands-agents strands-agents-tools

from
 
strands
 
import
 
Agent

from
 
strands_tools
 
import
 
calculator

agent
 
=
 
Agent
(
tools
=
[
calculator
])

agent
(
"What is the square root of 1764"
)

ThePython SDK READMEcovers tools, model providers, MCP, and bidirectional streaming.

### TypeScript

Requires Node.js 22+:

npm install @strands-agents/sdk

import
 
{
 
Agent
 
}
 
from
 
'@strands-agents/sdk'

const
 
agent
 
=
 
new
 
Agent
(
)

const
 
result
 
=
 
await
 
agent
.
invoke
(
'What is the square root of 1764?'
)

console
.
log
(
result
)

More in theTypeScript SDK README, including Zod-typed tools, structured output, and multi-agent patterns.

## Documentation

For detailed guidance & examples, explore our documentation:

* User Guide
* Strands Harness Guide(quickstart·configuration reference)
* Quick Start Guide
* Agent Loop
* Examples
* API Reference:Python·TypeScript
* Production & Deployment Guide

The docs themselves live in this monorepo undersite/, and doc PRs are welcome alongside code changes.

## Development

Git operations (commits, branches, PRs) are done from the repo root. Each package has its own toolchain:

Python SDK(strands-py/):

cd
 strands-py
pip install hatch
hatch 
test
 
#
 run unit tests

hatch fmt 
#
 format & lint

TypeScript SDK(strands-ts/):

npm ci 
#
 install from repo root

npm run build 
#
 build

npm 
test
 
#
 run unit tests

Documentation site(site/):

cd
 site
npm install
npm run dev 
#
 local dev server at http://localhost:4321/

## Contributing ❤️

We welcome contributions! See ourContributing Guidefor details on:

* Reporting bugs & features
* Development setup
* Contributing via Pull Requests
* Code of Conduct
* Reporting of security issues

## Stay in touch with the team

Come meet the Strands team and other users onDiscord

## License

This project is licensed under the Apache License 2.0 - see theLICENSE.APACHEfile for details.

## Security

SeeCONTRIBUTINGfor more information.

Generated from
 
amazon-archives/__template_Apache-2.0