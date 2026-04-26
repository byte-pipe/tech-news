---
title: 'GitHub - gastownhall/beads: Beads - A memory upgrade for your coding agent · GitHub'
url: https://github.com/gastownhall/beads
site_name: github
content_file: github-github-gastownhallbeads-beads-a-memory-upgrade-for
fetched_at: '2026-04-26T11:38:20.291744'
original_url: https://github.com/gastownhall/beads
author: gastownhall
description: Beads - A memory upgrade for your coding agent. Contribute to gastownhall/beads development by creating an account on GitHub.
---

gastownhall

 

/

beads

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
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

8,552 Commits
8,552 Commits
.agent/
workflows
.agent/
workflows
 
 
.claude-plugin
.claude-plugin
 
 
.claude
.claude
 
 
.devcontainer
.devcontainer
 
 
.githooks
.githooks
 
 
.github
.github
 
 
claude-plugin
claude-plugin
 
 
cmd/
bd
cmd/
bd
 
 
docs
docs
 
 
examples
examples
 
 
format
format
 
 
integrations
integrations
 
 
internal
internal
 
 
npm-package
npm-package
 
 
release-gates
release-gates
 
 
scripts
scripts
 
 
tests
tests
 
 
website
website
 
 
winget
winget
 
 
.buildflags
.buildflags
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.yml
.golangci.yml
 
 
.goreleaser.yml
.goreleaser.yml
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
.test-skip
.test-skip
 
 
AGENTS.md
AGENTS.md
 
 
AGENT_INSTRUCTIONS.md
AGENT_INSTRUCTIONS.md
 
 
ARTICLES.md
ARTICLES.md
 
 
BENCHMARKS.md
BENCHMARKS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
FEDERATION-SETUP.md
FEDERATION-SETUP.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
NEWSLETTER.md
NEWSLETTER.md
 
 
README.md
README.md
 
 
RELEASING.md
RELEASING.md
 
 
SECURITY.md
SECURITY.md
 
 
THIRD_PARTY_LICENSES
THIRD_PARTY_LICENSES
 
 
beads.go
beads.go
 
 
beads_cgo.go
beads_cgo.go
 
 
beads_nocgo.go
beads_nocgo.go
 
 
beads_test.go
beads_test.go
 
 
build-docs.md
build-docs.md
 
 
codecov.yml
codecov.yml
 
 
default.nix
default.nix
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
install.ps1
install.ps1
 
 
issues.jsonl
issues.jsonl
 
 
open_nocgo_test.go
open_nocgo_test.go
 
 
packages.nix
packages.nix
 
 
renovate.json
renovate.json
 
 
View all files

## Repository files navigation

# bd - Beads

Distributed graph issue tracker for AI agents, powered byDolt.

Platforms:macOS, Linux, Windows, FreeBSD

Docs:https://gastownhall.github.io/beads/

Beads provides a persistent, structured memory for coding agents. It replaces messy markdown plans with a dependency-aware graph, allowing agents to handle long-horizon tasks without losing context.

## ⚡ Quick Start

#
 Install beads CLI (system-wide - don't clone this repo into your project)

curl -fsSL https://raw.githubusercontent.com/gastownhall/beads/main/scripts/install.sh 
|
 bash

#
 Initialize in YOUR project

cd
 your-project
bd init

#
 Tell your agent

echo
 
"
Use 'bd' for task tracking
"
 
>>
 AGENTS.md

Note:Beads is a CLI tool you install once and use everywhere. You don't need to clone this repository into your project.

## 🛠 Features

* Dolt-Powered:Version-controlled SQL database with cell-level merge, native branching, and built-in sync via Dolt remotes.
* Agent-Optimized:JSON output, dependency tracking, and auto-ready task detection.
* Zero Conflict:Hash-based IDs (bd-a1b2) prevent merge collisions in multi-agent/multi-branch workflows.
* Compaction:Semantic "memory decay" summarizes old closed tasks to save context window.
* Messaging:Message issue type with threading (--thread), ephemeral lifecycle, and mail delegation.
* Graph Links:relates_to,duplicates,supersedes, andreplies_tofor knowledge graphs.

## 📖 Essential Commands

Command

Action

bd ready

List tasks with no open blockers.

bd create "Title" -p 0

Create a P0 task.

bd update <id> --claim

Atomically claim a task (sets assignee + in_progress).

bd dep add <child> <parent>

Link tasks (blocks, related, parent-child).

bd show <id>

View task details and audit trail.

## 🔗 Hierarchy & Workflow

Beads supports hierarchical IDs for epics:

* bd-a3f8(Epic)
* bd-a3f8.1(Task)
* bd-a3f8.1.1(Sub-task)

Stealth Mode:Runbd init --stealthto use Beads locally without committing files to the main repo. Perfect for personal use on shared projects. SeeGit-Free Usagebelow.

Contributor vs Maintainer:When working on open-source projects:

* Contributors(forked repos): Runbd init --contributorto route planning issues to a separate repo (e.g.,~/.beads-planning). Keeps experimental work out of PRs.
* Maintainers(write access): Beads auto-detects maintainer role via SSH URLs or HTTPS with credentials. Only needgit config beads.role maintainerif using GitHub HTTPS without credentials but you have write access.

## 📦 Installation

brew install beads 
#
 macOS / Linux (recommended)

npm install -g @beads/bd 
#
 Node.js users

Other methods:install script|go install|from source|Windows|Arch AUR

Requirements:macOS, Linux, Windows, or FreeBSD. Seedocs/INSTALLING.mdfor complete installation guide.

### Security And Verification

Before trusting any downloaded binary, verify its checksum against the releasechecksums.txt.

The install scripts verify release checksums before install. For manual installs, do this verification yourself before first run.

On macOS,scripts/install.shpreserves the downloaded signature by default. Local ad-hoc re-signing is explicit opt-in viaBEADS_INSTALL_RESIGN_MACOS=1.

Seedocs/ANTIVIRUS.mdfor Windows AV false-positive guidance and verification workflow.

## 💾 Storage Modes

Beads usesDoltas its database. Two modes
are available:

### Embedded Mode (default)

bd init

Dolt runs in-process — no external server needed. Data lives in.beads/embeddeddolt/. Single-writer only (file locking enforced).
This is the recommended mode for most users.

### Server Mode

bd init --server

Connects to an externaldolt sql-server. Data lives in.beads/dolt/.
Supports multiple concurrent writers. Configure the connection with flags
or environment variables:

Flag

Env Var

Default

--server-host

BEADS_DOLT_SERVER_HOST

127.0.0.1

--server-port

BEADS_DOLT_SERVER_PORT

3307

--server-socket

BEADS_DOLT_SERVER_SOCKET

(none; uses TCP)

--server-user

BEADS_DOLT_SERVER_USER

root

BEADS_DOLT_PASSWORD

(none)

BEADS_DOLT_CLI_DIR

local Dolt database path for CLI push/pull

Unix domain sockets:Use--server-socketto connect via a Unix socket
instead of TCP. This avoids port conflicts between concurrent projects and
is useful in sandboxed environments (e.g., Claude Code) where file-level
access control is simpler than network allowlists. The Dolt server must be
started withdolt sql-server --socket <path>. Auto-start is not supported
in socket mode.

WhenBEADS_DOLT_SERVER_MODE=1points at a Dolt server managed outside
Beads, setBEADS_DOLT_CLI_DIRifbd dolt push/bd dolt pullmust use
the localdoltCLI (for example git-protocol remotes or credentials that
only exist in the current shell). Use the actual Dolt database directory, not
the server root.

### Backup & Migration

Back up your database and migrate between modes usingbd backup:

#
 Set up a backup destination and push

bd backup init /path/to/backup
bd backup sync

#
 Restore into a new project (any mode)

bd init 
#
 or bd init --server

bd backup restore --force /path/to/backup

Seedocs/DOLT.mdfor full
migration instructions.

## 🌐 Community Tools

Seedocs/COMMUNITY_TOOLS.mdfor a curated list of community-built UIs, extensions, and integrations—including terminal interfaces, web UIs, editor extensions, and native apps.

## 🚀 Git-Free Usage

Beads works without git. The Dolt database is the storage backend — git
integration (hooks, repo discovery, identity) is optional.

#
 Initialize without git

export
 BEADS_DIR=/path/to/your/project/.beads
bd init --quiet --stealth

#
 All core commands work with zero git calls

bd create 
"
Fix auth bug
"
 -p 1 -t bug
bd ready --json
bd update bd-a1b2 --claim
bd prime
bd close bd-a1b2 
"
Fixed
"

BEADS_DIRtells bd where to put the.beads/database directory,
bypassing git repo discovery.--stealthsetsno-git-ops: truein
config, disabling all git hook installation and git operations.

This is useful for:

* Non-git VCS(Sapling, Jujutsu, Piper) — no.git/directory needed
* Monorepos— pointBEADS_DIRat a specific subdirectory
* CI/CD— isolated task tracking without repo-level side effects
* Evaluation/testing— ephemeral databases in/tmp

For daemon mode without git, usebd daemon start --local(seePR #433).

## 📝 Documentation

* Documentation site(versioned) |Installing|Agent Workflow|Copilot Setup|Articles|Sync Branch Mode|Troubleshooting|FAQ

## About

Beads - A memory upgrade for your coding agent

### Topics

 coding

 agents

 claude-code

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
 

Custom properties
 

### Stars

21.4k

 stars
 

### Watchers

81

 watching
 

### Forks

1.4k

 forks
 

 Report repository

 

## Releases89

v1.0.3

 Latest

 

Apr 24, 2026

 

+ 88 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Go94.1%
* Python3.2%
* Shell2.0%
* JavaScript0.3%
* PowerShell0.2%
* Makefile0.1%
* Other0.1%