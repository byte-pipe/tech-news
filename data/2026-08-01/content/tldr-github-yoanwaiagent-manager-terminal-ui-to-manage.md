---
title: 'GitHub - YoanWai/agent-manager: Terminal UI to manage AI coding-agent sessions (Claude Code, OpenCode, Codex, Grok Build) in tmux: live status, group tree, live pane preview, resource gauges. · GitHub'
url: https://github.com/YoanWai/agent-manager
site_name: tldr
content_file: tldr-github-yoanwaiagent-manager-terminal-ui-to-manage
fetched_at: '2026-08-01T11:30:03.252409'
original_url: https://github.com/YoanWai/agent-manager
date: '2026-08-01'
description: 'Terminal UI to manage AI coding-agent sessions (Claude Code, OpenCode, Codex, Grok Build) in tmux: live status, group tree, live pane preview, resource gauges. - YoanWai/agent-manager'
tags:
- tldr
---

YoanWai

 

/

agent-manager

Public

* NotificationsYou must be signed in to change notification settings
* Fork7
* Star224

 
 
 
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

295 Commits
295 Commits
.github
.github
 
 
docs
docs
 
 
internal
internal
 
 
tools/
badges
tools/
badges
 
 
.gitignore
.gitignore
 
 
.goreleaser.yaml
.goreleaser.yaml
 
 
AGENTS.md
AGENTS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
install.sh
install.sh
 
 
main.go
main.go
 
 
main_test.go
main_test.go
 
 
View all files

## Repository files navigation

The fastest workflow for every AI coding agent.

Claude Code, Codex, OpenCode, Grok, and Gemini CLI run side by side, each in its own tmux session, so they keep working after you quit the manager.

Instead of hunting through terminal tabs to see which agent is done and which is stuck, every session shows up in one list with live status, grouped into a project tree you can fold and reorder. You answer any of them without attaching:spacesends a prompt straight into a session's pane, or spawns a new agent in the selected group. A dead session revives on its own conversation withv. Andctrl+ropens a full-file diff of what an agent changed, syntax-highlighted, where the comments you leave on lines go back to the agent's pane as one review prompt when you pressC.

Not here yet: worktree creation, cost tracking, mouse-driven navigation, and agents that can talk to each other.

Jump to:Install·Usage·Keys·Diff review·Configuration

## Supported tools

Status detection currently supportsClaude Code,OpenCode,Codex,Grok Build, andGemini CLIout of the box. Any other CLI tool can run as a session; add a[tools.<name>]block with status rules to get live status for it (seeConfiguration).

## Install

### Homebrew (macOS / Linux)

brew install yoanwai/tap/agent-manager

Installs tmux with it if missing. The tap ships a cask, so an install from the older formula switches over withbrew uninstall agent-managerfollowed by the command above.

### Install script (macOS / Linux)

curl -fsSL https://raw.githubusercontent.com/YoanWai/agent-manager/main/install.sh 
|
 sh

Downloads the latest release for your platform, verifies it against the published checksums, and installs it to~/.local/bin. SetAGENT_MANAGER_INSTALL_DIRfor another directory andAGENT_MANAGER_VERSIONto pin a version. Install tmux with your own package manager.

Arch Linux, mise,go install, prebuilt binaries, Windows (WSL2), and updating:docs/install.md.

## Usage

agent-manager

Sessions run inside tmux (am_*namespace), so they survive the manager quitting. Inside a session,Ctrl+Qdetaches back to the manager andCtrl+Ropens its diff review.agent-manager --versionprints the version.

Agent sessions live on a private tmux server namedagentmgr, so they never mix with the tmux you run yourself and akill-serveron your own socket leaves them alone. To reach one from a plain shell, name that server:tmux -L agentmgr ls, thentmux -L agentmgr attach -t am_<id>.

The full reference, every key, the quick prompt, killing and reviving, diff review, groups, status detection, stats, and themes, lives indocs/usage.md. The short version:

Key

Action

n

New session (name, tool, directory, optional starting prompt, group)

space

Quick prompt: answer the selected session, or spawn an agent in the selected group

enter

Focus the session in place; keys go to the agent while the list stays

ctrl+r

Review the session's changes as full-file diffs; 
c
 comments a line, 
C
 sends the comments to the agent

x
 / 
v

Kill a session to free its RAM / revive it on its own conversation

s

Settings (default tool, theme, list density, review layout)

?

Help with every binding

Configuration (adding your own tools, status rules, revive commands) is indocs/configuration.md.

## Development

go run 
.

env -u TMUX TMUX_TMPDIR=/tmp/amtest go 
test
 ./... 
#
 end-to-end tests drive a real tmux server

SeeCONTRIBUTING.mdfor the checks CI runs, andAGENTS.mdif you point a coding agent at this repo.

## Contributing

Bug reports, feature ideas, and pull requests are welcome. SeeCONTRIBUTING.mdfor setup and the checks CI runs. Questions and setups worth sharing go inDiscussions. Security reports go through aprivate advisory; seeSECURITY.md.

## License

MIT