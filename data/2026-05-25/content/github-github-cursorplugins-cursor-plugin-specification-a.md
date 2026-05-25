---
title: 'GitHub - cursor/plugins: Cursor plugin specification and official plugins · GitHub'
url: https://github.com/cursor/plugins
site_name: github
content_file: github-github-cursorplugins-cursor-plugin-specification-a
fetched_at: '2026-05-25T19:34:45.602639'
original_url: https://github.com/cursor/plugins
author: cursor
description: Cursor plugin specification and official plugins. Contribute to cursor/plugins development by creating an account on GitHub.
---

cursor

 

/

plugins

Public

* NotificationsYou must be signed in to change notification settings
* Fork85
* Star786

 
 
 
 
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

82 Commits
82 Commits
.cursor-plugin
.cursor-plugin
 
 
.github/
workflows
.github/
workflows
 
 
agent-compatibility
agent-compatibility
 
 
cli-for-agent
cli-for-agent
 
 
continual-learning
continual-learning
 
 
create-plugin
create-plugin
 
 
cursor-sdk
cursor-sdk
 
 
cursor-team-kit
cursor-team-kit
 
 
docs-canvas
docs-canvas
 
 
orchestrate
orchestrate
 
 
pr-review-canvas
pr-review-canvas
 
 
pstack
pstack
 
 
ralph-loop
ralph-loop
 
 
schemas
schemas
 
 
scripts
scripts
 
 
teaching
teaching
 
 
.gitignore
.gitignore
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Cursor plugins

Official Cursor plugins for popular developer tools, frameworks, and SaaS products. Each plugin is a standalone directory at the repository root with its own.cursor-plugin/plugin.jsonmanifest.

## Plugins

name

Plugin

Author

Category

description
 (from marketplace)

continual-learning

Continual Learning

Cursor

Developer Tools

Incremental transcript-driven memory updates for AGENTS.md using high-signal bullet points only.

cursor-team-kit

Cursor Team Kit

Cursor

Developer Tools

Internal team workflows used by Cursor developers for CI, code review, shipping, local automation, and verification.

create-plugin

Create Plugin

Cursor

Developer Tools

Scaffold and validate new Cursor plugins.

agent-compatibility

Agent Compatibility

Cursor

Developer Tools

CLI-backed repo compatibility scans plus Cursor agents that audit startup, validation, and docs against reality.

cli-for-agent

CLI for Agents

Cursor

Developer Tools

Patterns for designing CLIs that coding agents can run reliably: flags, help with examples, pipelines, errors, idempotency, dry-run.

pr-review-canvas

PR Review Canvas

Cursor

Developer Tools

Render PR diffs as interactive Cursor Canvases organized for reviewer comprehension — groups changes by importance, separates boilerplate from core logic, and highlights tricky or unexpected code.

docs-canvas

Docs Canvas

Cursor

Developer Tools

Render documentation — architecture notes, API references, runbooks, and codebase walkthroughs — as a navigable Cursor Canvas with sections, table of contents, diagrams, and cross-references.

cursor-sdk

Cursor SDK

Cursor

Developer Tools

Build apps, scripts, CI pipelines, and automations on top of the Cursor TypeScript SDK (@cursor/sdk) — runtime selection, auth, streaming, MCP, error handling, and ready-to-extend integration patterns.

orchestrate

Orchestrate

Cursor

Developer Tools

Fan large tasks out across parallel Cursor cloud agents with planners, workers, verifiers, and structured handoffs.

Author values match each plugin’splugin.jsonauthor.name(Cursor listsplugins@cursor.comin the manifest).

## Repository structure

This is a multi-plugin marketplace repository. The root.cursor-plugin/marketplace.jsonlists all plugins, and each plugin has its own manifest:

plugins/
├── .cursor-plugin/
│ └── marketplace.json # Marketplace manifest (lists all plugins)
├── plugin-name/
│ ├── .cursor-plugin/
│ │ └── plugin.json # Per-plugin manifest
│ ├── skills/ # Agent skills (SKILL.md with frontmatter)
│ ├── rules/ # Cursor rules (.mdc files)
│ ├── mcp.json # MCP server definitions
│ ├── README.md
│ ├── CHANGELOG.md
│ └── LICENSE
└── ...

## License

MIT

## About

Cursor plugin specification and official plugins

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

786

 stars
 

### Watchers

5

 watching
 

### Forks

85

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

* TypeScript95.3%
* JavaScript2.1%
* CSS1.3%
* Shell1.2%
* HTML0.1%