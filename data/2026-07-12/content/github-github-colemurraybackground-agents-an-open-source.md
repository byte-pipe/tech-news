---
title: 'GitHub - ColeMurray/background-agents: An open-source background agents coding system · GitHub'
url: https://github.com/ColeMurray/background-agents
site_name: github
content_file: github-github-colemurraybackground-agents-an-open-source
fetched_at: '2026-07-12T19:27:17.849846'
original_url: https://github.com/ColeMurray/background-agents
author: ColeMurray
description: An open-source background agents coding system. Contribute to ColeMurray/background-agents development by creating an account on GitHub.
---

ColeMurray

 

/

background-agents

Public

* NotificationsYou must be signed in to change notification settings
* Fork341
* Star2.2k

 
 
 
 
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

774 Commits
774 Commits
.claude/
skills/
onboarding
.claude/
skills/
onboarding
 
 
.github/
workflows
.github/
workflows
 
 
.husky
.husky
 
 
.openinspect
.openinspect
 
 
docs
docs
 
 
packages
packages
 
 
scripts
scripts
 
 
terraform
terraform
 
 
.gitignore
.gitignore
 
 
.prettierignore
.prettierignore
 
 
.prettierrc
.prettierrc
 
 
.vercelignore
.vercelignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
eslint.config.js
eslint.config.js
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
vitest.workspace.ts
vitest.workspace.ts
 
 
View all files

## Repository files navigation

# Background Agents: Open-Inspect

An open-source background agents coding system inspired byRamp's Inspect.

## Overview

Open-Inspect provides a hosted background coding agent that can:

* Work on tasks in the background while you focus on other things
* Access full development environments (Node.js, Python, git, browser automation, VS Code)
* Connect from anywhere — web UI, Slack, GitHub PRs, Linear issues, or webhooks
* Enable multiplayer sessions where multiple people can collaborate in real time
* Create PRs with proper commit attribution to the prompting user
* Run on a schedule — cron jobs, Sentry alerts, and webhook-triggered automations
* Spawn parallel sub-tasks that work in separate sandboxes simultaneously
* Use your choice of AI model — Anthropic Claude, OpenAI Codex (via ChatGPT subscription), or
OpenCode Zen

## Security Model (Single-Tenant Only)

Important: This system is designed forsingle-tenant deployment only, where all users are
trusted members of the same organization with access to the same repositories.

### How It Works

The system uses a shared GitHub App installation for git operations (clone, fetch, push). The
control plane mints short-lived installation tokens server-side and brokers them to sandboxes
through the git credential helper on demand. This means:

* All users share the same GitHub App credentials- The GitHub App must be installed on your
organization's repositories, and any user of the system can access any repo the App has access to
* No per-user repository access validation- The system does not verify that a user has
permission to access a specific repository before creating a session
* GitHub users' OAuth tokens are used for PR creation- For GitHub logins, PRs are created using
the user's GitHub OAuth token, ensuring proper attribution and that they can only create PRs on
repos they have write access to. Users who sign in another way (e.g. Google) carry no SCM token,
so their PRs fall back to the shared GitHub App bot

### Token Architecture

Token Type

Purpose

Scope

GitHub App Token

Brokered git clone/fetch/push auth

All repos where App is installed

User OAuth Token

Create PRs, user info

Repos user has access to

Sandbox Auth Token

Sandbox-to-control-plane session calls

Single session

WebSocket Token

Real-time session auth

Single session

### Why Single-Tenant Only

This architecture followsRamp's Inspect design, which was
built for internal use where all employees are trusted and have access to company repositories.

For multi-tenant deployment, you would need:

* Per-tenant GitHub App installations
* Access validation at session creation
* Tenant isolation in the data model

### Deployment Recommendations

1. Deploy behind your organization's SSO/VPN- Ensure only authorized employees can access the
web interface
2. Install GitHub App only on intended repositories- The App's installation scope defines what
the system can access
3. Restrict sign-in- Configure allowed GitHub users, email domains, or active GitHub
organization membership (ALLOWED_GITHUB_ORGS)
4. Use GitHub's repository selection- When installing the App, select specific repositories
rather than "All repositories"

## Architecture

 ┌──────────────────┐
 │ Clients │
 │ ┌──────────────┐ │
 │ │ Web / Slack │ │
 │ │ GitHub / Lin.│ │
 │ │ Webhooks │ │
 │ └──────────────┘ │
 └────────┬─────────┘
 │
 ▼
┌────────────────────────────────────────────────────────────────────┐
│ Control Plane (Cloudflare) │
│ ┌──────────────────────────────────────────────────────────────┐ │
│ │ Durable Objects (per session) │ │
│ │ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌───────────────┐ │ │
│ │ │ SQLite │ │WebSocket│ │ Event │ │ GitHub │ │ │
│ │ │ DB │ │ Hub │ │ Stream │ │ Integration │ │ │
│ │ └─────────┘ └─────────┘ └─────────┘ └───────────────┘ │ │
│ └──────────────────────────────────────────────────────────────┘ │
│ ┌──────────────────────────────────────────────────────────────┐ │
│ │ D1 Database (repo-scoped secrets) │ │
│ └──────────────────────────────────────────────────────────────┘ │
└────────────────────────────────┬───────────────────────────────────┘
 │
 ▼
┌────────────────────────────────────────────────────────────────────┐
│ Data Plane (Sandbox Backend) │
│ ┌──────────────────────────────────────────────────────────────┐ │
│ │ Session Sandbox │ │
│ │ ┌───────────┐ ┌───────────┐ ┌───────────┐ │ │
│ │ │ Supervisor│──│ OpenCode │──│ Bridge │─────────────────┼──┼──▶ Control Plane
│ │ └───────────┘ └───────────┘ └───────────┘ │ │
│ │ │ │ │
│ │ Full Dev Environment │ │
│ │ (Node.js, Python, git, agent-browser) │ │
│ └──────────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────────┘

## Packages

Package

Description

control-plane

Cloudflare Workers + Durable Objects

web

Next.js web client

sandbox-runtime

Shared in-sandbox agent runtime

modal-infra

Modal sandbox infrastructure

daytona-infra

Daytona snapshot infrastructure

opencomputer-infra

OpenComputer template infrastructure

slack-bot

Slack integration (sessions from messages)

github-bot

GitHub integration (auto-review, @mention)

linear-bot

Linear integration (issue → coding session)

shared

Shared types and utilities

## Getting Started

For a practical setup guide (local + contributor + deployment paths), start withdocs/SETUP_GUIDE.md.

Seedocs/GETTING_STARTED.mdfor deployment instructions.

To understand the architecture and core concepts, readdocs/HOW_IT_WORKS.md.

To set up recurring scheduled tasks, seedocs/AUTOMATIONS.md.

## Key Features

### Fast Startup

Sessions start near-instantly through multiple layers of warming:

* Filesystem snapshots— After each prompt, sandbox state is saved; follow-up sessions restore
instead of re-cloning
* Pre-built images— Toggle per-repo (Settings > Images) or per-environment (Settings >
Environments); rebuilt every 30 minutes with latest commits and dependencies
* Proactive warming— Sandbox begins spinning up as soon as you start typing, before you hit
Enter

### Multi-Repository Sessions & Environments

One session can work across several repositories in a single sandbox:

* Ad-hoc sets— Pick up to 10 repositories in the new-session picker; each is cloned side by
side and the agent can make coordinated changes and open a PR per repository
* Environments— Save a repository set as a named environment with its own secrets scope and
optional prebuilt images, then launch it from the picker like any repository
* Seedocs/HOW_IT_WORKS.mdfor the model anddocs/IMAGE_PREBUILD.mdfor environment prebuilds

### Multiplayer Sessions

Multiple users can collaborate in the same session:

* Presence indicators show who's active
* Prompts are attributed to their authors in git commits
* Real-time streaming to all connected clients

### Commit Attribution

Commits are attributed to the user who sent the prompt:

// Configure git identity per prompt

await
 
configureGitIdentity
(
{

 
name
: 
author
.
scmName
,

 
email
: 
author
.
scmEmail
,

}
)
;

### Multi-Provider Model Support

Choose the AI model that fits your task, with per-session reasoning effort controls:

Provider

Models

Anthropic

Claude Haiku 4.5, Sonnet 4.5/4.6, Opus 4.5/4.6/4.7/4.8, Fable 5

OpenAI

GPT 5.4, GPT 5.5, 5.3 Codex, 5.3 Codex Spark

OpenCode Zen

Kimi K2.5/K2.6, MiniMax M2.5, Qwen3.7 Max, GLM 5/5.1 (opt-in)

Z.AI Coding Plan

GLM 5.2 (opt-in)

OpenAI models work with your existing ChatGPT subscription via OAuth — no separate API key needed.
Seedocs/AVAILABLE_MODELS.mdfor the full model list anddocs/OPENAI_MODELS.mdfor OpenAI setup instructions.

### Client Integrations

Interact with agents from wherever your team already works:

* Web UI— Full session management with real-time streaming, model/reasoning selectors, terminal
panel, and multiplayer presence
* Slack Bot— @mention or DM to start a session; replies thread back with results. Per-user
model and branch preferences via App Home. SeeSlack integration
* GitHub Bot— Auto-review on PR open or respond to @mentions in PR comments. Configurable
per-repo. SeeGitHub integration
* Linear Bot— Mention or assign the agent on an issue to start a coding session, post progress
activities, and link the resulting PR. SeeLinear integration
* Webhooks— Trigger sessions from any external system via authenticated HTTP POST

### Automations

Schedule recurring tasks or react to external events — no human in the loop:

* Cron schedules— Hourly, daily, weekly, monthly, or custom 5-field cron with timezone support
* Sentry alerts— Auto-triage on new errors, regressions, or critical metric alerts
* Inbound webhooks— JSONPath condition filters to gate which payloads spawn sessions
* Multi-repo fan-out— One scheduled automation can run across up to 10 repositories, opening a
separate session and pull request for each
* Auto-pause after 3 consecutive failures, manual trigger button, full run history

Seedocs/AUTOMATIONS.mdfor setup instructions.

### Sandbox Environment

Every session runs in an isolated sandbox backend with a full development environment:

* Pre-installed:Node.js 22, Python 3.12, Bun, git, GitHub CLI, build-essential
* Browser automation:agent-browser CLI with headless Chromium for screenshots, visual diffs,
and UI verification
* Code-server:Optional browser-based VS Code connected to the session workspace
* Web terminal:ttyd-powered terminal accessible from the session UI
* Port tunneling:Expose up to 10 dev server ports via encrypted tunnels. URLs are available
in-sandbox at/workspace/.tunnels.envbefore.openinspect/start.shruns
(details)
* Secrets:AES-256-GCM encrypted, scoped globally, per-repo, or per-environment, injected as env
vars at spawn time. Supports bulk.envpaste import

### Sub-Task Spawning

Agents can decompose work into parallel child sessions:

* spawn-taskcreates a child session in its own sandbox and returns immediately
* Parent continues working while children run in parallel on separate branches
* get-task-statusandcancel-taskfor coordination
* Depth limits and per-repo guardrails enforced

### Repository Lifecycle Scripts

Repositories can define two optional startup scripts under.openinspect/:

#
 .openinspect/setup.sh (provisioning)

#!
/bin/bash

npm install
pip install -r requirements.txt

#
 .openinspect/start.sh (runtime startup)

#!
/bin/bash

docker compose up -d postgres redis

* setup.shruns for image builds and fresh sessions
* setup.shis skipped for prebuilt-image and snapshot-restore starts
* setup.shfailures are non-fatal for fresh sessions, but fatal in image build mode
* start.shruns for every non-build session startup (fresh, prebuilt-image, snapshot-restore)
* start.shfailures are strict: if present and it fails, session startup fails
* Default timeouts:SETUP_TIMEOUT_SECONDS(default300)START_TIMEOUT_SECONDS(default120)
* SETUP_TIMEOUT_SECONDS(default300)
* START_TIMEOUT_SECONDS(default120)
* Both hooks receiveOPENINSPECT_BOOT_MODE(build,fresh,repo_image,snapshot_restore)
* Git operations in hooks can authenticate to other private repos on the configured SCM host when
the shared installation has access

## License

MIT

## Credits

Inspired byRamp's Inspectand
built with:

* Modal- Cloud sandbox infrastructure
* Daytona- Cloud development sandboxes
* Vercel Sandbox- Cloud sandbox infrastructure
* OpenComputer- Cloud sandbox infrastructure
* Cloudflare Workers- Edge computing
* OpenCode- Coding agent runtime
* Next.js- Web framework

## About

An open-source background agents coding system

backgroundagents.dev

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

2.2k

 stars
 

### Watchers

12

 watching
 

### Forks

341

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript85.1%
* Python12.3%
* HCL1.4%
* Other1.2%