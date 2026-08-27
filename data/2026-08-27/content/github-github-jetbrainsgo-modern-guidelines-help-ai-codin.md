---
title: 'GitHub - JetBrains/go-modern-guidelines: Help AI coding agents write modern Go · GitHub'
url: https://github.com/JetBrains/go-modern-guidelines
site_name: github
content_file: github-github-jetbrainsgo-modern-guidelines-help-ai-codin
fetched_at: '2026-08-27T20:57:26.345125'
original_url: https://github.com/JetBrains/go-modern-guidelines
author: JetBrains
description: Help AI coding agents write modern Go. Contribute to JetBrains/go-modern-guidelines development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 JetBrains

 

/

go-modern-guidelines

Public

* NotificationsYou must be signed in to change notification settings
* Fork62
* Star2k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

23 Commits
23 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.agents/
plugins
.agents/
plugins
 
 
.claude-plugin
.claude-plugin
 
 
.cursor-plugin
.cursor-plugin
 
 
.junie-extension
.junie-extension
 
 
internal
internal
 
 
plugin
plugin
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
FEATURES.md
FEATURES.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
main.go
main.go
 
 
View all files

## Repository files navigation

# Modern Go Guidelines

This repository containsguidelinesfor code agents that help them write modern Go code.

For example, an agent with these guidelines usesmax(a, b)instead of an if-else block,slices.Containsinstead of a manual loop,cmp.Or(a, b, c)instead of a chain of nil checks. It also knows about recent additions likenew(42)to get a pointer to a value anderrors.AsType[T](err)for type-safe error matching—both from Go 1.26.

The guidelines cover the most useful features from Go 1.0 through Go 1.27, including everything targeted by themodernizeanalyzer. An agent will:

* Detect the project's Go version fromgo.mod
* Use language features and stdlib additions available up to and including that version
* Prefer modern idioms over older patterns

## Motivation

All coding agents tend to generate outdated Go. Two reasons:

1. Training data lag.Models don't know about features added after their training cutoff. They can't useerrors.AsType[T](Go 1.26) if they've never seen it.
2. Frequency bias.Even for features the model knows, it often picks older patterns. There's morefor i := 0; i < n; i++in the training data thanfor i := range n, so that's what comes out.

These guidelines fix both problems by giving the agent an explicit reference.

This aligns with the Go team's direction. Themodernizeanalyzer exists to automatically update existing code to use newer idioms (seethis talkfrom the Go team). These guidelines serve the same goal for new code: agents write modern Go from the start, so there's less to fix later.

## Requirements

The marketplace integrations run a small CLI that is installed on first use withgo install. Because of that, theGo toolchainmust be installed and available on yourPATH.

The CLI is installed into a local cache (for example~/.cache/go-modern-guidelines) and never modifies your project. It targetsGo 1.25 or newer; on an older Go it still works as long as automatic toolchain switching is enabled (GOTOOLCHAIN=auto, the default), which lets Go fetch a compatible toolchain on first run.

## Instructions

The guidelines are available for Junie, Claude Code, Codex, and Cursor, and for other agents via skills.sh.

### Junie

#### Junie CLI

Run the following commands inside a Junie CLI session.

1. Add this repository as a marketplace:

/extensions marketplace add JetBrains/go-modern-guidelines

1. Install the extension:

/extensions install modern-go-guidelines

Junie invokes the skill automatically when it is relevant to a Go task.

#### Updating

Update the installed extension from inside a Junie CLI session:

/extensions update modern-go-guidelines

### Claude Code

#### Installation

Run the following commands inside a Claude Code session.

1. Add this repository as a marketplace:

/plugin marketplace add JetBrains/go-modern-guidelines

1. Install the plugin:

/plugin install modern-go-guidelines@goland-claude-marketplace

#### Usage

Claude Code invokes the skill automatically when it is relevant to a Go task.

To invoke it explicitly:

/modern-go-guidelines:use-modern-go

#### Updating

Claude Code can update the marketplace and installed plugin automatically at startup. Automatic updates are disabled by default for third-party marketplaces, so enable them once:

1. Run/plugin.
2. OpenMarketplacesand selectgoland-claude-marketplace.
3. SelectEnable auto-update.

When Claude Code reports that the plugin was updated, apply the new version to the current session with:

/reload-plugins

To update it manually instead, run these commands in a terminal:

claude plugin marketplace update goland-claude-marketplace
claude plugin update modern-go-guidelines@goland-claude-marketplace

### Codex

#### Installation

Run the following commands in a terminal.

1. Add this repository as a marketplace:

codex plugin marketplace add JetBrains/go-modern-guidelines

1. Install the plugin:

codex plugin add modern-go-guidelines@goland-codex-marketplace

#### Updating

Refresh the marketplace and reinstall the plugin so Codex replaces its cached copy:

codex plugin marketplace upgrade goland-codex-marketplace
codex plugin remove modern-go-guidelines@goland-codex-marketplace
codex plugin add modern-go-guidelines@goland-codex-marketplace

### Cursor

For convenience, the guidelines are distributed as a Cursor plugin.

#### Installation

1. Add this repository as a marketplace by running the following command in a terminal:

cursor-agent plugin marketplace add https://github.com/JetBrains/go-modern-guidelines

1. Install the plugin with the/pluginscommand inside a Cursor session.

#### Updating

Refresh the marketplace from Git and reopen Cursor so it can pick up the new plugin version:

cursor-agent plugin marketplace update goland-cursor-marketplace

If the installed plugin is still on the previous version, reinstall it with the/pluginscommand. Cursor does not currently provide a non-interactive CLI command for updating an installed plugin.

### Other Agents (viaskills.sh)

The same skill package works across other agents such as OpenCode. Install it with:

npx skills add JetBrains/go-modern-guidelines

(--skill use-modern-goinstalls only this skill.)

#### Updating

Update the project-installed skill with:

npx skills update use-modern-go -p -y

For a globally installed skill, replace-pwith-g.

## Local development

To try changes to the CLI in your agent, build this checkout into the tool's cache:

make dev-install

Then setGO_MODERN_GUIDELINES_DEV=1in the environment your agent runs in. With it set, any agent using the plugin runs your local build instead of the released version, the same way across Claude Code, Codex, and Cursor. Export it before launching the agent so the agent process inherits it:

export
 GO_MODERN_GUIDELINES_DEV=1

After editing the CLI, runmake dev-installagain to rebuild; the next call picks it up. To go back to the released version, unset the variable (or runmake dev-uninstallto remove the build):

make dev-uninstall

This requires the Go toolchain. The dev build is stored in the tool's cache directory ($XDG_CACHE_HOME/go-modern-guidelinesor~/.cache/go-modern-guidelines).

The build is driven byscripts/dev-install.sh, which is intentionally separate from the agent-facing wrapper so an agent can never trigger a build. Withoutmake(for example on Windows) you can run it directly:

sh scripts/dev-install.sh install 
#
 or: uninstall

pwsh scripts/dev-install.ps1 install 
#
 PowerShell equivalent