---
title: 'GitHub - Chachamaru127/claude-code-harness: Claude Code Dedicated Development Harness - Achieving High-Quality Development Through an Autonomous Plan→Work→Review Cycle · GitHub'
url: https://github.com/Chachamaru127/claude-code-harness
site_name: github
content_file: github-github-chachamaru127claude-code-harness-claude-cod
fetched_at: '2026-05-26T19:41:30.023738'
original_url: https://github.com/Chachamaru127/claude-code-harness
author: Chachamaru127
description: Claude Code Dedicated Development Harness - Achieving High-Quality Development Through an Autonomous Plan→Work→Review Cycle - Chachamaru127/claude-code-harness
---

Chachamaru127

 

/

claude-code-harness

Public

* NotificationsYou must be signed in to change notification settings
* Fork185
* Star1.7k

 
 
 
 
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

1,200 Commits
1,200 Commits
.claude-plugin
.claude-plugin
 
 
.claude
.claude
 
 
.codex-plugin
.codex-plugin
 
 
.cursor/
rules
.cursor/
rules
 
 
.githooks
.githooks
 
 
.github
.github
 
 
agents
agents
 
 
assets
assets
 
 
benchmarks
benchmarks
 
 
bin
bin
 
 
codex
codex
 
 
docs
docs
 
 
go
go
 
 
hooks
hooks
 
 
monitors
monitors
 
 
opencode
opencode
 
 
output-styles
output-styles
 
 
scripts
scripts
 
 
skills-codex
skills-codex
 
 
skills
skills
 
 
templates
templates
 
 
tests
tests
 
 
workflows/
default
workflows/
default
 
 
.claude-code-harness.config.yaml
.claude-code-harness.config.yaml
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
IMPLEMENTATION_GUIDE.md
IMPLEMENTATION_GUIDE.md
 
 
LICENSE.ja.md
LICENSE.ja.md
 
 
LICENSE.md
LICENSE.md
 
 
Plans.md
Plans.md
 
 
README.md
README.md
 
 
README_ja.md
README_ja.md
 
 
VERSION
VERSION
 
 
claude-code-harness.config.example.json
claude-code-harness.config.example.json
 
 
claude-code-harness.config.schema.json
claude-code-harness.config.schema.json
 
 
go.work
go.work
 
 
harness.toml
harness.toml
 
 
spec.md
spec.md
 
 
View all files

## Repository files navigation

# Claude Code Harness

Plan. Work. Review. Ship.A disciplined delivery loop for Claude Code, with bounded paths for Codex and OpenCode.

English |日本語

Claude Code is powerful, but raw agent work drifts: plans live in chat, tests
become optional, review happens too late, and release evidence gets rebuilt by
memory. Harness turns that into one repeatable operating path.

After install, the default changes from "ask the agent to code" to:

1. write the spec and plan,
2. implement only the approved slice,
3. verify the result,
4. review independently,
5. package evidence for PR or release.

## Quickstart

New users should start from the tool they already use. Existing users should
run the migration report before cleanup or reinstall.

Path

Start

New user

Tool-first onboarding

Existing user

Migration check

Claude Code fast path

Install in 30 seconds

Trigger proof

Skill trigger gate

## Install in 30 Seconds

claude
/plugin marketplace add Chachamaru127/claude-code-harness
/plugin install claude-code-harness@claude-code-harness-marketplace
/harness-setup

Next command: run/harness-planwith one small request.

/harness-plan Improve the README onboarding flow

## First 15 Minutes

1. Install through your tool route.
2. Run/harness-setupor the equivalent setup script.
3. Run/harness-planwith a small request; Harness writes thespec.mdandPlans.mddrafts for you to check.
4. Approve the generated contract or reply with the correction you want.
5. Run the smallest approved task, for example/harness-work 1.1.1.
6. Run/harness-reviewand keep the verification output.

Your job is not to hand-write the plan. It is to approve or correct the
generated contract before execution continues.

## How It Works

Harness adds a source-of-truth loop around agent work.
The 5 verb skills keep that surface small: plan, work, review, sync, release.

1. You describe the outcome in normal language.
2. /harness-plandrafts or updatesspec.mdandPlans.mdwith scope,
acceptance criteria, unknowns, and stop conditions.
3. Harness treats those files as the source of truth. Data the agent has not
seen staysunknowninstead of being silently invented.
4. /harness-workimplements the approved slice with TDD and verification.
5. /harness-reviewseparates review from implementation.
6. /harness-releasepackages only verified evidence.

## Commands

Command

What happens inside

/harness-setup

Installs project guidance, command surfaces, hooks, and checks so the workflow starts from one known baseline.

/harness-plan

Turns intent into 
spec.md
 and 
Plans.md
, including scope, acceptance criteria, dependencies, unknowns, and stop conditions.

/harness-work

Executes one approved task or range, adds tests when required, runs verification, and keeps work inside the plan.

/harness-work all

Runs the approved plan through implementation and review paths; use after the plan is clear and the repo baseline is known.

/harness-review

Reviews the result separately from implementation and treats major findings as blockers.

/harness-release

Checks release readiness, CHANGELOG/tag boundaries, and evidence packaging after implementation and review are complete.

bin/harness doctor --migration-report

Inventories old plugin caches, Codex skills, OpenCode files, symlinks, and memory state without deleting data.

## Basic Workflow

Stage

Output

Gate

Investigate

Evidence and unknowns

Do not promote unobserved data into claims.

Plan

spec.md
 + 
Plans.md

User approves or corrects the generated contract.

Work

Code and tests

TDD required when the task says so.

Review

Independent verdict

Major findings block completion.

PR

Evidence pack

PR ready is not release ready.

Release

Tag/release artifacts

Release preflight must pass on the release path.

## Install By Tool

Tool

Tier

Route

Claude Code

supported

Claude plugin marketplace, then 
/harness-setup
.

Codex CLI

internal-compatible

scripts/setup-codex.sh --user
; direct plugin smoke is tracked separately.

Codex app

candidate

Candidate smoke only; do not reuse Codex CLI proof.

OpenCode

internal-compatible

scripts/setup-opencode.sh
; runtime parity is not claimed.

Cursor

candidate

PM handoff or adapter research only.

GitHub Copilot CLI

candidate

Manual profile research only.

Antigravity CLI

future/unsupported

No end-user install route in this phase.

## Existing User Migration

Runbin/harness doctor --migration-reportbefore changing an existing setup.
The report inventories stale Claude plugin caches, duplicate Codex skills, old
symlinks, OpenCode backup paths, and harness-mem state without deleting
anything.

## Support Boundary

Harness can describe candidate paths, but it does not inherit support claims
from Superpowers, Hermes Agent, or any other project. A host only moves up when
Harness has its own bootstrap, trigger, runtime, and release evidence.

not_observed != absent: missing local proof means "not proven here", not
"impossible" and not "supported".

## Requirements

* Claude Code v2.1+ for the supported Claude path.
* A project repository with write access for local setup.
* No Node.js is required for the Go-native guardrail engine.
* Optionalharness-memfor
cross-session memory when configured and healthy.

## Advanced

Use these after the basic trigger path is visible.

Capability

What it adds

Boundary

Breezing

Planner/Critic/Worker style team execution for larger task lists.

Still gated by plan quality and review.

Codex companion review

Schema-backed Codex second opinion through 
scripts/codex-companion.sh
.

Raw 
codex exec
 is not the Harness companion path.

OpenCode bootstrap

Mirrors Harness guidance into OpenCode-compatible surfaces.

Real runtime parity is not claimed.

harness-mem

Project-scoped memory and recall across sessions.

Optional companion; purge remains explicit.

## Documentation

Resource

Description

Tool-first onboarding

Where to start by host tool.

Install routes

Per-tool setup and support-tier boundaries.

Migration check

Existing-user impact, compatibility, and rollback path.

Skill trigger gate

How install success is verified.

Capability matrix

Supported, internal-compatible, candidate, and unsupported host claims.

Claude Code Compatibility

Current Claude Code requirements and compatibility notes.

Cursor Integration

Cursor handoff boundary and candidate-route notes.

Distribution Scope

Included vs compatibility vs development-only paths.

Hardening parity

Runtime safety differences between Claude hooks and Codex gates.

Work All Evidence Pack

Success/failure verification contract for full-plan execution.

Changelog

User-facing version history.

## Contributing

Issues and PRs welcome. SeeCONTRIBUTING.md.

## Acknowledgments

* AI Masao- Hierarchical skill design
* Beagle- Test tampering prevention patterns

## License

MIT License. SeeLICENSE.md.

## About

Claude Code Dedicated Development Harness - Achieving High-Quality Development Through an Autonomous Plan→Work→Review Cycle

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

1.7k

 stars
 

### Watchers

7

 watching
 

### Forks

185

 forks
 

 Report repository

 

## Releases165

v4.12.3

 Latest

 

May 25, 2026

 

+ 164 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Shell43.9%
* Go32.1%
* JavaScript14.0%
* TypeScript8.4%
* Python1.6%