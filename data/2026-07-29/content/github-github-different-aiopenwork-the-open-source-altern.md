---
title: 'GitHub - different-ai/openwork: The open-source alternative to Claude Cowork (powered by opencode) · GitHub'
url: https://github.com/different-ai/openwork
site_name: github
content_file: github-github-different-aiopenwork-the-open-source-altern
fetched_at: '2026-07-29T11:46:58.918585'
original_url: https://github.com/different-ai/openwork
author: different-ai
description: The open-source alternative to Claude Cowork (powered by opencode) - different-ai/openwork
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 different-ai

 

/

openwork

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.8k
* Star17.4k

 
 
 
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

4,035 Commits
4,035 Commits
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.opencode
.opencode
 
 
apps
apps
 
 
changelog
changelog
 
 
docs
docs
 
 
ee
ee
 
 
evals
evals
 
 
examples/
microsandbox-openwork-rust
examples/
microsandbox-openwork-rust
 
 
packages
packages
 
 
packaging
packaging
 
 
patches
patches
 
 
prds/
scim
prds/
scim
 
 
scripts
scripts
 
 
translated_readmes
translated_readmes
 
 
.dockerignore
.dockerignore
 
 
.env.dev
.env.dev
 
 
.gitignore
.gitignore
 
 
.infisical.json
.infisical.json
 
 
.nvmrc
.nvmrc
 
 
.vercelignore
.vercelignore
 
 
AGENTS.md
AGENTS.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
STATS.md
STATS.md
 
 
STATS_V2.md
STATS_V2.md
 
 
SUPPORT.md
SUPPORT.md
 
 
TRANSLATIONS.md
TRANSLATIONS.md
 
 
app-demo.gif
app-demo.gif
 
 
constants.json
constants.json
 
 
openwork-logo-transparent.svg
openwork-logo-transparent.svg
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
skills-lock.json
skills-lock.json
 
 
turbo.json
turbo.json
 
 
View all files

## Repository files navigation

# OpenWork

OpenWork is a free, open-source desktop app made for sharing AI workflows. It is an open-source alternative to Claude Cowork and Codex for macOS, Windows, and Linux.

Add one OpenWork MCP to Codex, Claude Code, Cursor, or another compatible agent and reuse the same skills, MCPs, and connected services across your tools, teammates, and machines. Create something once, share it with coworkers or friends, or keep it for yourself.

The desktop app is there when you want a dedicated workspace, but it is not required. You can use OpenWork from the agent you already have. For larger organizations, the admin interface lets you publish capabilities, manage access, and configure shared or per-user connections.

Download OpenWork

## Install with your AI agent

Already use an AI agent? Copy this prompt and paste it into Claude Code, Cursor, Codex, ChatGPT, or any agent that can run commands on your computer.

Install OpenWork on my computer, set up my first workspace, and open it ready to use. Follow the steps in https://openworklabs.com/start.md?v=hero

1. Installs OpenWork
2. Creates your workspace
3. Opens it ready to run

## Use OpenWork from any agent

The OpenWork MCP brings your assigned skills, plugins, MCP connections, Google Workspace, and Microsoft 365 capabilities into any compatible agent.

It exposes two tools:search_capabilitiesfinds what you can use, andexecute_capabilityruns it. After adding the MCP, your client opens a browser so you can sign in and choose your OpenWork organization.

### Codex

codex mcp add openwork --url https://api.openworklabs.com/mcp/agent

### Claude Code

claude mcp add --transport http openwork https://api.openworklabs.com/mcp/agent

### OpenCode

Add this toopencode.json:

{
 
"mcp"
: {
 
"openwork"
: {
 
"type"
: 
"
remote
"
,
 
"enabled"
: 
true
,
 
"url"
: 
"
https://api.openworklabs.com/mcp/agent
"
,
 
"oauth"
: {}
 }
 }
}

### Any MCP client

Use this remote MCP server URL:

https://api.openworklabs.com/mcp/agent

## OpenWork Den

OpenWork Den is the control plane for managing OpenWork across a team or organization.

* Provision inference at scale and control which members and teams can use each model provider.
* Invite teammates, create teams, and manage access from one place.
* Set desktop policies, restrict local model access, and control which app versions your organization can use.
* Publish skills and plugins through marketplaces, then assign them to the organization, a team, or specific people.
* Import Anthropic-compatible plugins and make their supported skills and remote MCPs available through the OpenWork MCP.

## Documentation

Read the OpenWork docs.

## Local development

For one checkout, keep usingpnpm dev; with no extra environment variables it reuses the existing shared dev profile.

To run multiple git worktrees at once, use:

pnpm dev:worktree

That setsOPENWORK_DEV_PROFILE=auto, derives a stable profile name from the worktree path, lets Electron choose a free CDP port, and asks Vite for a free dev-server port. You can also choose a named profile, for exampleOPENWORK_DEV_PROFILE=my-feature OPENWORK_ELECTRON_REMOTE_DEBUG_PORT=0 PORT=0 pnpm dev.

dev:worktreealso defaultsOPENWORK_ELECTRON_USE_MOCK_KEYCHAIN=1. A brand-new profile has no stored credentials, so on macOS the real keychain prompts as soon as Chromium persists an authenticated cookie, and that modal blocks Electron's main loop until it is dismissed. SetOPENWORK_ELECTRON_USE_MOCK_KEYCHAIN=0if you specifically want the system keychain in an isolated profile.

Dev startup prints a banner like[openwork] dev profile=... cdp=http://127.0.0.1:9223; use it to find the profile directory and pass the CDP URL to local tooling.

If a second instance cannot get the profile lock it now says so and exits, instead of lingering with an open CDP port and no window.