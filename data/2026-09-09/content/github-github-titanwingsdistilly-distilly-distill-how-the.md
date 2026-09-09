---
title: 'GitHub - titanwings/distilly: Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）. · GitHub'
url: https://github.com/titanwings/distilly
site_name: github
content_file: github-github-titanwingsdistilly-distilly-distill-how-the
fetched_at: '2026-09-09T15:29:46.204135'
original_url: https://github.com/titanwings/distilly
author: titanwings
description: Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）. - titanwings/distilly
---

titanwings

 

/

distilly

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.1k
* Star24.5k

 
 
 
distilly-plugin
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

166 Commits
166 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
docs
docs
 
 
packages
packages
 
 
plugins
plugins
 
 
scripts
scripts
 
 
tests
tests
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.prettierignore
.prettierignore
 
 
.prettierrc.json
.prettierrc.json
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CITATION.cff
CITATION.cff
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
INSTALL.md
INSTALL.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
ROADMAP.md
ROADMAP.md
 
 
UPDATES.md
UPDATES.md
 
 
eslint.config.js
eslint.config.js
 
 
knip.json
knip.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
requirements-dev.txt
requirements-dev.txt
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.tools.json
tsconfig.tools.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

# Distilly

### Distill how they think into Person Profiles for Agents.

Colleague Skill / colleague-skill (original name)

Distilly is a local-first product for turning a person's source material, working habits, judgment, and voice into a versionedPerson Profile for Agents. The profile can be recalled temporarily during a run or explicitly installed as a long-lived host Skill. The storage authority stays local; no additional model API key is required.

This repository now defaults to the unreleased0.1.0-preview.1Developer Preview ondistilly-plugin. Codex, OpenClaw2026.3.24, and Hermesv0.9.0each have an immutable real-host transport-capacity fixture. The OpenClaw and Hermes measurements use a deterministic synthetic fixture server through the real host executable, model, and MCP transport; they do not by themselves certify packaged restart or the full product lifecycle. Setup remains fail-closed for any unrecorded host version or changed release tuple. It is the default GitHub branch, but it is not a tagged release or an npm package yet.

Chinese·Español·Deutsch·日本語·한국어·Português·Русский

## Install the Developer Preview

### For an agent

Give your coding agent the following task and let it run the commands in a fresh checkout:

Install the Distilly Developer Preview from thedistilly-pluginbranch, build it with Node 22.19+ (or Node 24), rundistilly setup --host codex, rundistilly doctor --host codex, and report the result. Do not modify another branch.

The exact checkout and setup commands are shown below so the agent can verify every step.

### For a human

Requirements: Node.js22.19+or24, pnpm10.32+, and a locally installed Codex CLI. From a terminal:

git clone --branch distilly-plugin https://github.com/titanwings/distilly.git

cd
 distilly
corepack 
enable

pnpm install --frozen-lockfile
pnpm run build
node packages/cli/lib/bin.js setup --host codex
node packages/cli/lib/bin.js doctor --host codex

Restart Codex after setup. The launcher registers the self-contained Plugin and its five MCP tools. To remove the host integration while keeping all local people, profiles, and source data:

node packages/cli/lib/bin.js uninstall --host codex

To install one approved profile as a persistent Skill after a profile has been created, use its exact subject id:

node packages/cli/lib/bin.js install subject_
<
32 lowercase hex characters
>
 --host codex

## Host compatibility and explicit Legacy fallback

Codex uses the native Plugin preview above. The Preview also includes compatibility bindings for OpenClaw and Hermes:

* OpenClawloads the Claude-compatible bundle from~/.openclaw/extensions/distillyand its real.mcp.json. Check discovery withopenclaw plugins inspect distilly --json.
* Hermesinstalls the canonical Skill at~/.hermes/skills/distilly, a managed wrapper at~/.distilly/bin/distilly-hermes, and an MCP entry in~/.hermes/config.yaml.resourcesandpromptsare disabled so the exposed surface remains five tools; check it withhermes mcp test distilly.

The CLI recognizes both hosts and enables setup when the installed version matches the recorded real-host transport fixture. The current net budgets, measured in isolated clean sessions withopenai-codex/gpt-5.4, are 65,536 serialized bytes for OpenClaw and 49,752 for Hermes (the same conservative byte/token accounting used by the Codex fixture). These are transport/value lower bounds for the recorded probe, not a guarantee of remaining context in every model or user session. Any unrecorded version, release digest, tool descriptor, or serializer tuple returnshost_unsupportedbefore writing an unverified integration. There is no automatic switch to the legacy implementation.

Until a host has a verified Plugin binding, you can explicitly choose the maintaineddot-skillbranch as aLegacy Skill compatibility mode:

Install Distilly in Legacy Skill compatibility mode from thedot-skillbranch into this host's normal Skills directory, using a clean checkout whose final directory is nameddistilly. Verify discovery and report the installed Git commit. Do not run Plugin setup or claim SQLite, five-tool MCP, Panel, or Plugin lifecycle support.

For a manual install, replace<target-directory>with the complete final path in thedetailed install guide, including the lastdistillycomponent, and create its parent first:

git clone --single-branch --branch dot-skill --depth 1 \
 https://github.com/titanwings/distilly.git \
 
<
target-directory
>

git -C 
<
target-directory
>
 rev-parse HEAD

This is an explicit, separate file-based implementation—not an automatic runtime fallback. It does not share a supported data model with the Plugin, and a failed Plugin preflight never switches modes. The compatibility promise currently covers local files and pasted text only. Do not enable legacy collectors while the Plugin uses the same home directory: current legacy collectors can write credential configuration into the same~/.distilly/namespace and remain outside the Preview's reviewed security boundary. Keep exactly onedistillyactive in any host discovery scope and verify which copy the host loaded.

## The first usable flow

On Codex, the complete flow below is verified. OpenClaw2026.3.24and Hermesv0.9.0have the same briefing transport path verified against their recorded capacity fixture; their packaged restart, long-lived Skill, and uninstall lifecycle checks remain separate. Restart the selected host and ask it to research and distill a person. Supply only the files, text, or public URLs you want included. Distilly then:

1. resolves or creates the person;
2. imports the selected material with deterministic local parsers;
3. creates a pending research job and a complete evidence-bound briefing;
4. commits a versioned Person Profile;
5. returns the profile or a complete temporary prompt for the current run;
6. accepts an explicit correction and sends a candidate to review;
7. lets you promote, reject, or roll back the candidate in the local Panel; and
8. installs the approved profile as a self-contained host Skill when you ask it to.

The model-facing surface remains exactly five MCP tools:

distilly_get·distilly_ingest·distilly_pending·distilly_commit·distilly_correct

Distilly never silently truncates a complete briefing or profile prompt. If a verified host budget cannot carry the complete value, it reports a bounded capacity error with measurements and keeps the stored data unchanged.

## Host status

Host

Native Plugin

Current compatibility route

Codex

Fully verified in this release branch

Native Plugin

Claude Code

Binding included; exact host fixture still needed

Explicit 
dot-skill
 Legacy Skill

OpenClaw

Transport-capacity fixture recorded for 
2026.3.24
 (65,536-byte net budget); lifecycle pending

Claude-compatible bundle + discovery smoke

Hermes

Transport-capacity fixture recorded for 
v0.9.0
 (49,752-byte net budget); lifecycle pending

Managed Skill + MCP configuration

DeepSeek Harness (DSH)

Community binding planned

Explicit 
dot-skill
 Legacy Skill

Pi agent

Community binding planned

Explicit 
dot-skill
 Legacy Skill

Grok Build

Community binding planned

Explicit 
dot-skill
 Legacy Skill

OpenCode

Community binding planned

Explicit 
dot-skill
 Legacy Skill

Grok Bot

Community binding planned

Manual saved/private Skill only; local repository import is not claimed

Host compatibility is a binding concern. Legacy Skill discovery is useful continuity, but it does not make a host a verified Plugin target.

## Local material formats

The first Preview accepts explicit localTXT,Markdown,JSON, andSRT/VTTfiles. It also accepts pasted text and public URLs through the host's visible research flow. Files are read only from the paths or sources the user supplies; symlinked selected files and duplicate file names are rejected. PDF, email, provider exports, and hosted connectors are follow-up work.

## 📣 2026-09 update: help expand coding-agent Plugins

Codex, OpenClaw, and Hermes now have real host/version capacity fixtures. We need community support to provide the same evidence forClaude Code, DeepSeek Harness (DSH), Pi agent, Grok Build, OpenCode, and Grok Bot, then to build and validate their coding-agent Plugin packages. I will actively review those contributions and keep the public contracts, release digests, and host behavior aligned.

See the full call for contributors inUPDATES.mdand the current priorities inROADMAP.md.

## Project documents

* Detailed Preview installation
* Changelog
* Architecture and shipped-state map
* Testing contract
* Development workflow
* Design corpus
* Release manifest
* Contributing

Distilly is released under theMIT License. Created by@titanwings.