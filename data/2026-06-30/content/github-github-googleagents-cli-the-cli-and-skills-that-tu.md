---
title: 'GitHub - google/agents-cli: The CLI and skills that turn any coding assistant into an expert at creating, evaluating, and deploying AI agents on Google Cloud. · GitHub'
url: https://github.com/google/agents-cli
site_name: github
content_file: github-github-googleagents-cli-the-cli-and-skills-that-tu
fetched_at: '2026-06-30T11:55:38.308710'
original_url: https://github.com/google/agents-cli
author: google
description: The CLI and skills that turn any coding assistant into an expert at creating, evaluating, and deploying AI agents on Google Cloud. - google/agents-cli
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 google

 

/

agents-cli

Public

* NotificationsYou must be signed in to change notification settings
* Fork437
* Star3.8k

 
 
 
 
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

29 Commits
29 Commits
.claude-plugin
.claude-plugin
 
 
.github
.github
 
 
docs
docs
 
 
skills
skills
 
 
src/
google/
agents/
cli
src/
google/
agents/
cli
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
RELEASE_NOTES.md
RELEASE_NOTES.md
 
 
gemini-extension.json
gemini-extension.json
 
 
View all files

## Repository files navigation

# agents-cli

The CLI and skills for building agents on Gemini Enterprise Agent Platform.

Get Started|Skills|Commands|PyPI|Issues|Docs|Release Notes|Star us

Turn your favorite coding assistant into an expert at building and deploying agents on Google Cloud.

Agents CLI in Agent Platform(agents-cli) gives your coding agent the skills and commands to build, scale, govern, and optimize enterprise-grade agents — so you don't have to learn every CLI and service yourself.

Works seamlessly with:Antigravity CLI•Claude Code•Codex•and any other coding agent.

## Get Started

Prerequisites:Python 3.11+,uv, andNode.js.

### 1. Install

uvx google-agents-cli setup

Or just the skills — your coding agent will handle the rest

npx skills add google/agents-cli

### 2. Open your coding agent

LaunchAntigravity CLI,Claude Code,Codex, or any coding agent you prefer.

### 3. Build your first agent

Ask your coding agent to build something — e.g."Use agents-cli to build a caveman-style agent that compresses verbose text into terse, technical grunts"

See thefull tutorialfor a step-by-step walkthrough.

Browse the full documentation →

## Agent Skills

Skill

What your coding agent learns

google-agents-cli-workflow

Development lifecycle, code preservation rules, model selection

google-agents-cli-adk-code

ADK Python API — agents, tools, orchestration, callbacks, state

google-agents-cli-scaffold

Project scaffolding — 
create
, 
enhance
, 
upgrade

google-agents-cli-eval

Evaluation methodology — metrics, datasets, LLM-as-judge, adaptive rubrics

google-agents-cli-deploy

Deployment — 
Agent Runtime
, 
Cloud Run
, 
GKE
, CI/CD, secrets

google-agents-cli-publish

Gemini Enterprise registration

google-agents-cli-observability

Observability — Cloud Trace, logging, third-party integrations

## CLI Commands

Command

What it does

agents-cli setup

Install CLI + skills to coding agents

agents-cli scaffold <name>

Create a new agent project

agents-cli eval generate

Run agent on eval dataset, produce traces

agents-cli eval grade

Run agent evaluations on the traces

agents-cli deploy

Deploy to Google Cloud

agents-cli publish gemini-enterprise

Register with Gemini Enterprise

See all commands

Command

Description

agents-cli login

Authenticate with Google Cloud or AI Studio

agents-cli login --status

Show authentication status

Scaffold

agents-cli scaffold <name>

Create a new agent project

agents-cli scaffold enhance

Add deployment, CI/CD, or RAG to an existing project

agents-cli scaffold upgrade

Upgrade project to a newer agents-cli version

Develop

agents-cli run "prompt"

Run agent with a single prompt

agents-cli install

Install project dependencies

agents-cli lint

Run code quality checks (Ruff)

Evaluate

agents-cli eval generate

Run agent inference over eval cases

agents-cli eval grade

Grade generated traces against metrics

agents-cli eval dataset synthesize

Synthesize multi-turn eval scenarios for your local agent

agents-cli eval compare

Compare two eval result files

agents-cli eval analyze

Cluster failure modes from grade results

agents-cli eval metric list

List available metrics

agents-cli eval optimize

Auto-tune agent prompts using eval data

Deploy & Publish

agents-cli deploy

Deploy to Google Cloud

agents-cli publish gemini-enterprise

Register with Gemini Enterprise

agents-cli infra single-project

Provision single-project infrastructure

agents-cli infra cicd

Set up CI/CD pipeline + staging/prod infrastructure

Data

agents-cli infra datastore

Provision datastore infrastructure for RAG

agents-cli data-ingestion

Run data ingestion pipeline

Other

agents-cli info

Show project config and CLI version

agents-cli update

Force reinstall skills to all IDEs

## How it works

## Architecture

The Google Cloud agent stack thatagents-clibuilds on:

## FAQ

Is this an alternative to Antigravity CLI, Claude Code, or Codex?No.agents-cliis a toolforcoding agents, not a coding agent itself.It provides the CLI commands and skills that make your coding agent better at building, evaluating, and deploying ADK agents on Google Cloud.

How is this different from just usingadkdirectly?ADKis an agent framework.agents-cligives your coding agent the skills and tools to build, evaluate, and deploy ADK agents end-to-end.

Do I need Google Cloud?For local development (create,run,eval), no — you can use anAI Studio API keyto run Gemini withADKlocally. For deployment and cloud features, yes.

Can I use this with an existing agent project?Yes.agents-cli scaffold enhanceadds deployment and CI/CD to existing projects.

Can I useagents-cliwithout a coding agent?Yes. The CLI works standalone — you can runagents-cli scaffold,eval,deploy, and every other command directly from your terminal. The skills just make it easier for coding agents to do it for you.

How can I extendagents-cliwith other skills?agents-cliskills cover the agent-building lifecycle (scaffold, ADK code patterns, evals, deploy, publish, observability). For adjacent concerns, you could install another skill suite alongside. For example,agent-skillscovers general software-engineering workflows (ideation, spec gates, planning, code review), andgoogle/skillscovers Google Cloud foundations (BigQuery, Cloud Run, Firebase, GKE).

## Feedback

We value your input — it helps us improveagents-clifor the community.

* Bugs & feature requests:open an issue— 👍 the ones you want prioritized
* Share what you built:we'd love to hear about your projects! Reach out atagents-cli@google.comto share your agent or provide feedback

## Contributing

The best way to contribute is through feedback: bug reports, feature requests, and ideas shared viaissuesto directly shape our roadmap.

See thecontributing guidefor details.

## Terms of Service

agents-clileverages Google Cloud APIs. When you deploy agents, you'll be deploying resources in your own Google Cloud project and will be responsible for those resources. Please review theGoogle Cloud Service Termsfor details.

## Preview

This feature is subject to the "Pre-GA Offerings Terms" in the General Service
Terms section of theService Specific Terms.
Pre-GA features are available "as is" and might have limited support. For more
information, see thelaunch stage descriptions.

## About

The CLI and skills that turn any coding assistant into an expert at creating, evaluating, and deploying AI agents on Google Cloud.

google.github.io/agents-cli/

### Topics

 google-cloud

 gemini

 agents

 adk

 generative-ai

 agent-development-kit

 coding-agent

 gemini-enterprise-agent-platform

### Resources

 Readme

 

### License

 Apache-2.0 license
 

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

3.8k

 stars
 

### Watchers

24

 watching
 

### Forks

437

 forks
 

 Report repository

 

## Releases11

Release v0.6.1

 Latest

 

Jun 28, 2026

 

+ 10 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python77.2%
* HCL14.3%
* Go2.3%
* Java2.2%
* Makefile2.1%
* TypeScript1.1%
* Other0.8%