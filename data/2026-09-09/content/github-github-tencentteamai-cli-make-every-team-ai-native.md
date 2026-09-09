---
title: 'GitHub - Tencent/teamai-cli: Make Every Team AI Native · GitHub'
url: https://github.com/Tencent/teamai-cli
site_name: github
content_file: github-github-tencentteamai-cli-make-every-team-ai-native
fetched_at: '2026-09-09T15:29:48.384580'
original_url: https://github.com/Tencent/teamai-cli
author: Tencent
description: Make Every Team AI Native. Contribute to Tencent/teamai-cli development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 Tencent

 

/

teamai-cli

Public

* NotificationsYou must be signed in to change notification settings
* Fork176
* Star2.8k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

695 Commits
695 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
agents
agents
 
 
assets
assets
 
 
docs
docs
 
 
examples/
ci
examples/
ci
 
 
scripts
scripts
 
 
skills
skills
 
 
src
src
 
 
test
test
 
 
.coding-ci.yaml
.coding-ci.yaml
 
 
.gitignore
.gitignore
 
 
.versionrc
.versionrc
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README.zh-CN.md
README.zh-CN.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.json
tsconfig.json
 
 
tsup.config.ts
tsup.config.ts
 
 
vitest.config.ts
vitest.config.ts
 
 
vitest.e2e.config.ts
vitest.e2e.config.ts
 
 
View all files

## Repository files navigation

# TeamAI — Make Every Team AI Native

English|简体中文

TeamAI manages your team's skills, rules, MCP, and knowledge across Claude Code, Codex, CodeBuddy, WorkBuddy, OpenCode, Cursor, and other AI agents.

## Contributors

Thanks to everyone who has contributed to TeamAI!

Made withcontrib.rocks.

## Quick Start

### Install

npm install -g teamai-cli

### Team admin / solo user

Create a shared-experience repo on your git host (GitHub, GitLab, GitCode, CNB, TGit, or a private Git service),grant write access to team members, then runteamai init https://github.com/yourorg/yourrepo.

No team repo yet?Start from a template pre-loaded with production-ready skills, rules, and review agents. Browse theteamai-huborg, clickUse this template, thenteamai initagainst your new repo.

### Team members

#
 Choose one, depending on where you want resources installed

#
 Project-scope init (default, resources installed under the project directory)

cd
 /path/to/my-project
teamai init https://github.com/yourorg/yourrepo

#
 Or, user-scope init (resources installed under ~/)

teamai init https://github.com/yourorg/yourrepo --scope user

Once initialized, every AI session automatically pulls the latest skills / rules and other Harness updates published by admins — no manual sync needed.

Full usage guide:docs/usage-guide.md(中文版) — covers everything from team creation to day-to-day use.

## Product architecture

Team Execution × Team Context (beta) × Team Improvement (beta):

Layer

Job

In this CLI today

Team Execution

Make every agent work the team's way

init
 / 
pull
 / 
push
, skills, rules, agents, hooks, MCP, env

Team Context
 (beta)

Make every agent understand the team

recall, learnings, codebase graph, teamwiki...

Team Improvement
 (beta)

Make every execution improve the team

friction-based share-learnings, sessions, digest, dashboard...

## Overview

Agent

Team Execution

Team Context (beta)

Team Improvement (beta)

skills
rules
docs
env
agents
hooks
mcp

learnings
codebase
teamwiki

usage
sessions
dashboard

Claude Code
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

Codex
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

Cursor
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

CodeBuddy
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

WorkBuddy
✓
✓
✓
✓
—
✓
✓
✓
✓
✓
✓
✓
✓

OpenCode
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
—
—
—

OpenClaw
✓
✓
✓
✓
—
—
—
✓
✓
✓
—
—
—

Hermes
✓
—
✓
✓
—
—
—
✓
✓
✓
—
—
—

DeepSeek Harness
✓
—
✓
—
—
—
—
✓
✓
✓
—
—
—

Qoder
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓
✓

ZCode
✓
—
✓
—
✓
✓
✓
✓
✓
✓
✓
✓
✓

Git providers— GitHub · GitLab · GitCode · CNB · TGit · private Git service.

### Distribution Controls

Team-wide settings an admin configures once and delivers to every member onteamai pull:

Capability

Command

What it does

Roles

teamai roles

Define role → namespace mappings so each member syncs only the skills for their role.

Tags

teamai tags

Tag skills / rules so members subscribe to just the tags they need.

Sources

teamai source

Subscribe to additional skill repos — other teams' public repos, or shared/public repos within your own org; subscribed skills sync automatically on pull.

## Team Execution

One Team. One Harness. Every Agent.

TeamAI keeps skills, rules, docs, and hooks in a shared git repo and distributes them to every member's local AI tools through a "push → review & merge → pull" flow — with support for subscribing to other teams' or shared repos' Harness.

### How It Works

teamai push → create branch + MR → reviewer approves + merges
 ↓
 SessionStart hook → teamai pull → synced to local AI tools

### What Gets Shared

Each resource is delivered to every agent:

Resource

In the team repo

Notes

Skills

skills/<name>/SKILL.md

Rules

rules/*.md

Docs

docs/

Foundational project docs; not all loaded by default (progressive disclosure)

Agents

agents/<name>.yaml

Culture

culture.md

Team mission, values, and working principles — injected into each agent's CLAUDE.md / AGENTS.md so every session inherits them

CLAUDE.md

claudemd/*.md

Env

env/

Shared team-level environment variables and switches; do not put secrets here

Hooks

hooks/hooks.yaml

MCP

mcp/mcp.yaml

Packages

teamai.yaml

Currently npm packages and Claude Code plugins only

Models

—

Not implemented for every provider yet

For file formats and full workflows, see theUsage Guide.

## Team Context (beta)

Every agent understands how the team works.

Beyond distributing the Harness, TeamAI organizes accumulated team experience and code structure into a searchable knowledge base that the AI recalls automatically when needed.

### Automatic Experience Sharing

When a session ends, the Stop hook scores it byfriction— signals that the session hit something worth remembering: you interrupted or corrected the AI, denied a tool call, or the AI had to retry failing tools. A long-but-routine session (lots of tool calls, no friction) does not trigger; a session where you actually fought a problem does. If the score is high enough, the AI suggests:

[teamai] This session may contain a problem worth documenting: you interrupted the AI twice, the AI retried failing tools 8 times.

Task: Fix duplicate project-level Hook injection

Consider running /teamai-share-learnings to summarize what you learned and share it with your team.

The hint names the non-zero friction signals that triggered it and, when available, includes a redacted, single-line summary of the first task. The/teamai-share-learningsskill summarizes the session and pushes a learning document directly to the team repo. Each session is prompted at most once. Teams can switch the hint off withsharing.contributeHint.enabled: falseinteamai.yaml(members:contributeHintEnabledin local config) while keeping the rest of the Stop hook.

### Team Knowledge Recall

Let the AI automatically search accumulated team knowledge before a task. This feature isoff by defaultand must be enabled explicitly — teams can setsharing.recall.enabled: trueinteamai.yamlas the default, and members can override locally:

teamai recall 
enable
 
#
 on: deploy the teamai-recall subagent + inject guidance rules

teamai recall disable 
#
 off: remove the subagent and rules

teamai recall status 
#
 show effective state (team default + user override)

Search runs via a subagent: once enabled,teamai pulldeploys the built-inteamai-recallsubagent into each AI tool'sagents/directory. The AI invokes it before a task — the subagent extracts keywords, runs the search, reads the matched source files, and returns a structured summary of team knowledge. The subagent first runs a relevance precheck (teamai recall --check) and skips retrieval entirely when the task is unrelated to team knowledge. Under the hood it shells out to theteamai recallcommand, which you can also run manually:

$ teamai recall 
"
port conflict
"

[1/2] MR review caught a port-conflict bug ★1 [user]
Author: member-a 
|
 Score: 18.5 
|
 Tags: troubleshooting, networking

[2/2] Deployment configuration best practices [project]
Author: member-b 
|
 Score: 12.0 
|
 Tags: deploy, config
Matched: conflict 
|
 Missing: port

### Codebase Knowledge Graph

teamai importparses source repos into a structured graph underteamwiki/, enabling structurally-aware retrieval:

teamai import --from-repo https://github.com/org/repo
teamai import --from-org myorg 
#
 batch import all repos

teamai codebase --extract /path/to/repo 
#
 local extract into teamwiki/

teamai codebase --lint --output /path/to/repo 
#
 check the locally extracted graph

The graph stores components, interfaces, configs, and cross-repo import edges.teamai recalluses it for graph-boosted re-ranking.
When a recall hit comes from a codebase page, the result includes aSources:line listing the relevant source file paths — giving agents a direct starting point for code changes instead of re-exploring the repo.

Edges come from two tracks that run together, with AST results taking precedence on overlap:

* AST track(TypeScript/JavaScript, Python, Go): a WASMtree-sitterparser resolvesimport/require, call sites, and TSimplementsclauses to precise file-to-fileDEPENDS_ON/REFERENCES/IMPLEMENTSedges (taggedcode-ast, with confidence weights).
* Heuristic track(all languages, including Java/Rust): regex-based extraction (taggedcode-heuristic), which also covers languages the AST track does not.

The WASM parser is a pure-JavaScript dependency — no native toolchain is required. If it fails to load for any reason, extraction falls back to the heuristic track and records anAST_UNAVAILABLEgap. SetTEAMAI_SKIP_AST=1to force heuristic-only extraction.

## Team Improvement (beta)

Every execution makes the entire team smarter.

### Maintenance

As skills and knowledge accumulate, prune what the team no longer uses.teamai recall maintenancearchives low-confidence learnings and flags stale skills, rules, and docs for cleanup or updates:

teamai recall maintenance --prune --dry-run 
#
 preview

teamai recall maintenance --prune --archive 
#
 archive unused learnings

teamai recall maintenance --update-quality 
#
 draft updates for stale skills / docs

Insight into how the team actually uses its AI tools, and a starting point for turning session friction into shared skills, rules, and knowledge:

Capability

Command

What it shows

Usage

teamai digest

Weekly team digest — token usage, conversation volume, and intervention rate.

Sessions

teamai session save

Privacy-scrubbed per-session summaries (tool sequence, prompt turns, interventions) that feed the digest's Session Highlights.

Dashboard

teamai dashboard

Web dashboard showing team members' live coding-session status, intervention count, and token usage.

KB Health

teamai dashboard
 → KB Health

Built-in dashboard page reporting knowledge-base usage & health — coverage by type, top recalled entries, silent entries, recall trend, author contributions, and a maintenance console.

## Commands

Command

Description

teamai init

Initialize: OAuth login, link repo, register member, inject hooks

teamai pull

Pull team resources and inject into local AI tools

teamai push

Push local resources to a branch and open a Merge Request

teamai packages [install] [target]

Install declared npm packages and Claude plugins; with a target, also update 
teamai.yaml
. Bare 
teamai packages
 installs everything; 
teamai packages install <target>
 adds one

teamai status

Show local vs team repo diff

teamai contribute

Share session experience to team repo

teamai recall <query>

Search the team knowledge base (BM25 + graph-boost)

teamai recall enable/disable/status

Toggle or check recall state

teamai recall promote [learningId]

Promote a high-confidence learning to formal knowledge (skills/rules/docs)

teamai recall maintenance

Maintain knowledge base health: prune low-confidence learnings, writeback confidence scores, flag stale entries

teamai import

Import knowledge (
--dir
, 
--from-repo
, 
--from-org
, 
--from-repo-list
, 
--from-mr
)

teamai codebase --extract [path]

Extract code facts and build the local graph under 
teamwiki/

teamai codebase --lint

Knowledge graph health check

teamai ci extract-mr --url <url>

CI: extract knowledge from MR, post comments, write after merge

teamai members

List team members

teamai roles

Manage team roles and namespaces

teamai tags

Manage tag-based skill/rule filtering

teamai skill exclude add/remove/list

Manage skills excluded from local sync (
usage guide
)

teamai source

Manage skill subscription sources (other teams or your org's shared repos)

teamai remove <type> <name>

Remove a resource and open MR

teamai session save

Record a privacy-scrubbed session summary to a monthly log (
--push
 feeds 
digest
)

teamai digest

Generate weekly team usage digest

teamai doctor

Diagnose configuration issues

teamai uninstall

Remove all teamai resources and hooks

## License

MIT

## Contributing

PRs are welcome! Please readCONTRIBUTING.mdfirst.