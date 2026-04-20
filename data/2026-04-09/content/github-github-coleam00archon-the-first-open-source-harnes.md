---
title: 'GitHub - coleam00/Archon: The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable. · GitHub'
url: https://github.com/coleam00/Archon
site_name: github
content_file: github-github-coleam00archon-the-first-open-source-harnes
fetched_at: '2026-04-09T11:24:47.835320'
original_url: https://github.com/coleam00/Archon
author: coleam00
description: The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable. - coleam00/Archon
---

coleam00



/

Archon

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.4k
* Star14k




 
dev
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

1,123 Commits
1,123 Commits
.archon
.archon
 
 
.claude
.claude
 
 
.github
.github
 
 
.husky
.husky
 
 
assets
assets
 
 
auth-service
auth-service
 
 
deploy
deploy
 
 
homebrew
homebrew
 
 
migrations
migrations
 
 
packages
packages
 
 
scripts
scripts
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.lintstagedrc.json
.lintstagedrc.json
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Caddyfile.example
Caddyfile.example
 
 
Dockerfile
Dockerfile
 
 
Dockerfile.user.example
Dockerfile.user.example
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
bun.lock
bun.lock
 
 
bunfig.toml
bunfig.toml
 
 
docker-compose.override.example.yml
docker-compose.override.example.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
docker-entrypoint.sh
docker-entrypoint.sh
 
 
eslint.config.mjs
eslint.config.mjs
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# Archon

The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable.

Archon is a workflow engine for AI coding agents. Define your development processes as YAML workflows - planning, implementation, validation, code review, PR creation - and run them reliably across all your projects.

Like what Dockerfiles did for infrastructure and GitHub Actions did for CI/CD - Archon does for AI coding workflows. Think n8n, but for software development.

## Why Archon?

When you ask an AI agent to "fix this bug", what happens depends on the model's mood. It might skip planning. It might forget to run tests. It might write a PR description that ignores your template. Every run is different.

Archon fixes this. Encode your development process as a workflow. The workflow defines the phases, validation gates, and artifacts. The AI fills in the intelligence at each step, but the structure is deterministic and owned by you.

* Repeatable- Same workflow, same sequence, every time. Plan, implement, validate, review, PR.
* Isolated- Every workflow run gets its own git worktree. Run 5 fixes in parallel with no conflicts.
* Fire and forget- Kick off a workflow, go do other work. Come back to a finished PR with review comments.
* Composable- Mix deterministic nodes (bash scripts, tests, git ops) with AI nodes (planning, code generation, review). The AI only runs where it adds value.
* Portable- Define workflows once in.archon/workflows/, commit them to your repo. They work the same from CLI, Web UI, Slack, Telegram, or GitHub.

## What It Looks Like

Here's an example of an Archon workflow that plans, implements in a loop until tests pass, gets your approval, then creates the PR:

#
 .archon/workflows/build-feature.yaml

nodes
:
 -
id
:
plan


prompt
:
"
Explore the codebase and create an implementation plan
"

 -
id
:
implement


depends_on
:
[plan]


loop
:
#
 AI loop - iterate until done


prompt
:
"
Read the plan. Implement the next task. Run validation.
"


until
:
ALL_TASKS_COMPLETE


fresh_context
:
true
#
 Fresh session each iteration

 -
id
:
run-tests


depends_on
:
[implement]


bash
:
"
bun run validate
"

#
 Deterministic - no AI

 -
id
:
review


depends_on
:
[run-tests]


prompt
:
"
Review all changes against the plan. Fix any issues.
"

 -
id
:
approve


depends_on
:
[review]


loop
:
#
 Human approval gate


prompt
:
"
Present the changes for review. Address any feedback.
"


until
:
APPROVED


interactive
:
true
#
 Pauses and waits for human input

 -
id
:
create-pr


depends_on
:
[approve]


prompt
:
"
Push changes and create a pull request
"

Tell your coding agent what you want, and Archon handles the rest:

You: Use archon to add dark mode to the settings page

Agent: I'll run the archon-idea-to-pr workflow for this.
 → Creating isolated worktree on branch archon/task-dark-mode...
 → Planning...
 → Implementing (task 1/4)...
 → Implementing (task 2/4)...
 → Tests failing - iterating...
 → Tests passing after 2 iterations
 → Code review complete - 0 issues
 → PR ready: https://github.com/you/project/pull/47

## Previous Version

Looking for the original Python-based Archon (task management + RAG)? It's fully preserved on thearchive/v1-task-management-ragbranch.

## Getting Started

Most users should start with theFull Setup- it walks you through credentials, installs the Archon skill into your projects, and gives you the web dashboard.

Already have Claude Code and just want the CLI?Jump to theQuick Install.

### Full Setup (5 minutes)

Clone the repo and use the guided setup wizard. This configures credentials, platform integrations, and copies the Archon skill into your target projects.

Prerequisites
 - Bun, Claude Code, and the GitHub CLI

Bun-bun.sh

#
 macOS/Linux

curl -fsSL https://bun.sh/install
|
 bash

#
 Windows (PowerShell)

irm bun.sh/install.ps1
|
 iex

GitHub CLI-cli.github.com

#
 macOS

brew install gh

#
 Windows (via winget)

winget install GitHub.cli

#
 Linux (Debian/Ubuntu)

sudo apt install gh

Claude Code-claude.ai/code

#
 macOS/Linux/WSL

curl -fsSL https://claude.ai/install.sh
|
 bash

#
 Windows (PowerShell)

irm https://claude.ai/install.ps1
|
 iex

git clone https://github.com/coleam00/Archon

cd
 Archon
bun install
claude

Then say:"Set up Archon"

The setup wizard walks you through everything: CLI installation, authentication, platform selection, and copies the Archon skill to your target repo.

### Quick Install (30 seconds)

Already have Claude Code set up? Install the standalone CLI binary and skip the wizard.

macOS / Linux

curl -fsSL https://archon.diy/install
|
 bash

Windows (PowerShell)

irm https:
//
archon.diy
/
install.ps1
|
 iex

Homebrew

brew install coleam00/archon/archon

### Start Using Archon

Once you've completed either setup path, go to your project and start working:

cd
 /path/to/your/project
claude

Use archon to fix issue #42

What archon workflows do I have? When would I use each one?

The coding agent handles workflow selection, branch naming, and worktree isolation for you. Projects are registered automatically the first time they're used.

Important:Always run Claude Code from your target repo, not from the Archon repo. The setup wizard copies the Archon skill into your project so it works from there.

## Web UI

Archon includes a web dashboard for chatting with your coding agent, running workflows, and monitoring activity. To start it, ask your coding agent to run the frontend from the Archon repo, or runbun run devfrom the repo root yourself.

Register a project by clicking+next to "Project" in the chat sidebar - enter a GitHub URL or local path. Then start a conversation, invoke workflows, and watch progress in real time.

Key pages:

* Chat- Conversation interface with real-time streaming and tool call visualization
* Dashboard- Mission Control for monitoring running workflows, with filterable history by project, status, and date
* Workflow Builder- Visual drag-and-drop editor for creating DAG workflows with loop nodes
* Workflow Execution- Step-by-step progress view for any running or completed workflow

Monitoring hub:The sidebar shows conversations fromall platforms- not just the web. Workflows kicked off from the CLI, messages from Slack or Telegram, GitHub issue interactions - everything appears in one place.

See theWeb UI Guidefor full documentation.

## What Can You Automate?

Archon ships with workflows for common development tasks:

Workflow

What it does

archon-assist

General Q&A, debugging, exploration - full Claude Code agent with all tools

archon-fix-github-issue

Classify issue → investigate/plan → implement → validate → PR → smart review → self-fix

archon-idea-to-pr

Feature idea → plan → implement → validate → PR → 5 parallel reviews → self-fix

archon-plan-to-pr

Execute existing plan → implement → validate → PR → review → self-fix

archon-issue-review-full

Comprehensive fix + full multi-agent review pipeline for GitHub issues

archon-smart-pr-review

Classify PR complexity → run targeted review agents → synthesize findings

archon-comprehensive-pr-review

Multi-agent PR review (5 parallel reviewers) with automatic fixes

archon-create-issue

Classify problem → gather context → investigate → create GitHub issue

archon-validate-pr

Thorough PR validation testing both main and feature branches

archon-resolve-conflicts

Detect merge conflicts → analyze both sides → resolve → validate → commit

archon-feature-development

Implement feature from plan → validate → create PR

archon-architect

Architectural sweep, complexity reduction, codebase health improvement

archon-refactor-safely

Safe refactoring with type-check hooks and behavior verification

archon-ralph-dag

PRD implementation loop - iterate through stories until done

archon-remotion-generate

Generate or modify Remotion video compositions with AI

archon-test-loop-dag

Loop node test workflow - iterative counter until completion

archon-piv-loop

Guided Plan-Implement-Validate loop with human review between iterations

Archon ships 17 default workflows - runarchon workflow listor describe what you want and the router picks the right one.

Or define your own.Default workflows are great starting points - copy one from.archon/workflows/defaults/and customize it. Workflows are YAML files in.archon/workflows/, commands are markdown files in.archon/commands/. Same-named files in your repo override the bundled defaults. Commit them - your whole team runs the same process.

SeeAuthoring WorkflowsandAuthoring Commands.

## Add a Platform

The Web UI and CLI work out of the box. Optionally connect a chat platform for remote access:

Platform

Setup time

Guide

Telegram

5 min

Telegram Guide

Slack

15 min

Slack Guide

GitHub Webhooks

15 min

GitHub Guide

Discord

5 min

Discord Guide

## Architecture

┌─────────────────────────────────────────────────────────┐
│ Platform Adapters (Web UI, CLI, Telegram, Slack, │
│ Discord, GitHub) │
└──────────────────────────┬──────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────┐
│ Orchestrator │
│ (Message Routing & Context Management) │
└─────────────┬───────────────────────────┬───────────────┘
 │ │
 ┌───────┴────────┐ ┌───────┴────────┐
 │ │ │ │
 ▼ ▼ ▼ ▼
┌───────────┐ ┌────────────┐ ┌──────────────────────────┐
│ Command │ │ Workflow │ │ AI Assistant Clients │
│ Handler │ │ Executor │ │ (Claude / Codex) │
│ (Slash) │ │ (YAML) │ │ │
└───────────┘ └────────────┘ └──────────────────────────┘
 │ │ │
 └──────────────┴──────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────────────────┐
│ SQLite / PostgreSQL (7 Tables) │
│ Codebases • Conversations • Sessions • Workflow Runs │
│ Isolation Environments • Messages • Workflow Events │
└─────────────────────────────────────────────────────────┘

## Documentation

Full documentation is available atarchon.diy.

Topic

Description

Getting Started

Setup guide (Web UI or CLI)

The Book of Archon

10-chapter narrative tutorial

CLI Reference

Full CLI reference

Authoring Workflows

Create custom YAML workflows

Authoring Commands

Create reusable AI commands

Configuration

All config options, env vars, YAML settings

AI Assistants

Claude and Codex setup details

Deployment

Docker, VPS, production setup

Architecture

System design and internals

Troubleshooting

Common issues and fixes

## Contributing

Contributions welcome! See the openissuesfor things to work on.

Please readCONTRIBUTING.mdbefore submitting a pull request.

## License

MIT

## About

The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable.

archon.diy

### Topics

 cli

 yaml

 automation

 typescript

 ai

 workflow-engine

 developer-tools

 bun

 claude

 coding-assistant

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


### Stars

14k

 stars


### Watchers

191

 watching


### Forks

2.4k

 forks


 Report repository



## Releases4

Archon CLI v0.3.2

 Latest



Apr 8, 2026



+ 3 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* TypeScript97.5%
* Shell0.9%
* PowerShell0.7%
* JavaScript0.5%
* Dockerfile0.2%
* CSS0.2%
