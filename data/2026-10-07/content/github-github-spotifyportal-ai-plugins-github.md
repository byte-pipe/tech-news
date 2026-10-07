---
title: GitHub - spotify/portal-ai-plugins · GitHub
url: https://github.com/spotify/portal-ai-plugins
site_name: github
content_file: github-github-spotifyportal-ai-plugins-github
fetched_at: '2026-10-07T17:42:30.120345'
original_url: https://github.com/spotify/portal-ai-plugins
author: spotify
description: Contribute to spotify/portal-ai-plugins development by creating an account on GitHub.
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

6 Commits
6 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.claude-plugin
.claude-plugin
 
 
.codex-plugin
.codex-plugin
 
 
.cursor-plugin
.cursor-plugin
 
 
assets
assets
 
 
plugins/
shunt
plugins/
shunt
 
 
skills
skills
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Spotify Portal AI Plugins

BringSpotify Portalinto Claude Code, Codex, and Cursor.

This plugin provides focused workflows for thePortal CLI: set up
authentication, search your software catalog, build service briefings, run
diagnostics, and invoke Portal actions.

## Highlights

* Set up the Portal CLI for your current coding-agent environment.
* Run read-only diagnostics to verify plugin, CLI, authentication, and action readiness.
* Search the software catalog and technical documentation using natural language queries.
* Generate concise service briefings with available ownership, health, incident, and documentation details.
* Discover and safely invoke Portal actions with built-in help, dry-run, and confirmation safeguards.

The marketplace also shipsshunt(Claude Code only for now): a plugin that routes I/O-heavy agent work — bulk file reads and boilerplate generation — to AiKA modes running cheaper worker models, via the Portal CLI actions registry. Seeplugins/shunt/README.md.

## Installation

### Claude Code

claude plugin marketplace add spotify/portal-ai-plugins
claude plugin install portal@portal
claude plugin install shunt@portal 
#
 optional: token-saving AiKA delegation

Start a new session and run:

/portal:setup

### Codex

codex plugin marketplace add spotify/portal-ai-plugins
codex

Open/plugins, install Spotify Portal, start a new task, and ask:

Set up Spotify Portal for me.

### Cursor

Register thespotify/portal-ai-pluginsrepository in your Cursor team marketplace, then install Spotify Portal fromCursor Settings → Plugins.

## Workflows

Workflow

Purpose

setup

Configure Portal CLI authentication

doctor

Run read-only readiness diagnostics

search

Search the software catalog and technical documentation

service

Produce a concise operational service briefing

actions

Discover, inspect, preview, and safely invoke Portal actions

feedback

Submit feedback about the Portal CLI to the Portal team

## Portal CLI

The workflows invoke the upstream CLI through:

npx @spotify/portal-cli 
<
command
>

Setup verifies the requiredauth,actions,owner,search, andservicecommands before proceeding.