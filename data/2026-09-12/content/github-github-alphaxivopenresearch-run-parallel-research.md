---
title: 'GitHub - alphaXiv/OpenResearch: Run parallel research agents with any model · GitHub'
url: https://github.com/alphaXiv/OpenResearch
site_name: github
content_file: github-github-alphaxivopenresearch-run-parallel-research
fetched_at: '2026-09-12T01:21:57.674184'
original_url: https://github.com/alphaXiv/OpenResearch
author: alphaXiv
description: Run parallel research agents with any model. Contribute to alphaXiv/OpenResearch development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 alphaXiv

 

/

OpenResearch

Public

* NotificationsYou must be signed in to change notification settings
* Fork79
* Star1.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

323 Commits
323 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
agent-skills
agent-skills
 
 
demo/
nanochat
demo/
nanochat
 
 
docs
docs
 
 
macos
macos
 
 
scripts
scripts
 
 
src
src
 
 
ui
ui
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.port-workflow.mjs
.port-workflow.mjs
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SKILL.md
SKILL.md
 
 
SYSTEM_PROMPT.md
SYSTEM_PROMPT.md
 
 
build.rs
build.rs
 
 
dist-workspace.toml
dist-workspace.toml
 
 
pid
pid
 
 
View all files

## Repository files navigation

# OpenResearch

The local-first workspace for research agents and autoresearch.

TurnClaude Code,Codex, orOpenCode into research agents that can review
literature, develop hypotheses, run experiments, and produce research artifacts.

Download the desktop app·Documentation·Releases

## Get started

Download the local desktop app fromopenresearch.sh/download, or install the
CLI on macOS or Linux:

curl -LsSf https://openresearch.sh/install.sh 
|
 sh
orx up

orx upopens the local dashboard athttp://127.0.0.1:4791.

On Windows, install fromReleasesand readthe Windows notesfirst — Git for Windows is required, and
support is still in beta.

To use LM Studio, oMLX, Ollama, or a custom endpoint with OpenCode, seeconnecting local models.

Create an account atopenresearch.shto receive email
updates and use managed OpenResearch compute.

## Built for research agents

OpenResearch gives you

Parallel exploration

Give each research direction an independent agent session and isolated git worktree.

Reproducible experiments

Track variants in a git-native experiment tree; every run receives an immutable archive of its recorded commit.

Evidence in context

Keep logs, diffs, files, results, and artifacts tied to the work that produced them.

Your choice of agent

Use Claude Code, Codex, or OpenCode, with the harness and model selected per session.

Your choice of compute

Run locally, on your own infrastructure, or with managed OpenResearch compute.

Local ownership

Keep projects, conversations, experiments, runs, logs, code, and artifacts on your machine.

### Autoresearch

OpenResearch can run the full loop autonomously: propose an idea, change the
code, launch an experiment, inspect the evidence, and decide what to try next.
Multiple agents can explore different directions in parallel while the
experiment tree preserves their lineage.

## Run anywhere

The same committed source snapshot can run locally, over SSH, or on Slurm,
Kubernetes, Ray, Hugging Face Jobs, Modal, Tinker, and managed OpenResearch compute.
Publishing the repository is not required.

Run the workspace next to remote GPUs while using the browser on your laptop:

orx up --remote user@host

SSH config aliases and custom ports are supported. The remote service binds to
loopback and has no application-level authentication, so other users on that
host can reach it.

## CLI and agent integration

Install the OpenResearch skill into supported coding agents:

orx install-skills

Common commands:

orx projects
orx project view 
<
project-id
>

orx runs 
<
project-id
>

orx logs 
<
run-id
>

orx exp run 
<
experiment-id
>

orx discover keyword 
<
query
>

orx paper 
<
arxiv-id-or-doi
>

Runorx --helpororx <command> --helpfor the complete interface.

## Local by default

OpenResearch runs on127.0.0.1with a local SQLite store. Creating a project
or launching a run does not publish your code. Anopenresearch.shaccount is only used for
service-owned capabilities such as organizations and managed compute.

## Usage analytics

Official release builds send opt-out, coarse usage events tied to a random
installation ID. They do not include code, prompts, file contents or paths,
repository names, tokens, emails, or project and experiment identifiers.

orx telemetry off
orx telemetry status
orx 
<
command
>
 --no-telemetry

Source and development builds do not send analytics.