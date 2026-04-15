---
title: 'GitHub - Donchitos/Claude-Code-Game-Studios: Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy. · GitHub'
url: https://github.com/Donchitos/Claude-Code-Game-Studios
site_name: github
content_file: github-github-donchitosclaude-code-game-studios-turn-clau
fetched_at: '2026-04-15T11:55:49.578215'
original_url: https://github.com/Donchitos/Claude-Code-Game-Studios
author: Donchitos
description: Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy. - Donchitos/Claude-Code-Game-Studios
---

Donchitos

 

/

Claude-Code-Game-Studios

Public template

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.5k
* Star9.8k

 
 
 
 
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

33 Commits
33 Commits
.claude
.claude
 
 
.github
.github
 
 
CCGS Skill Testing Framework
CCGS Skill Testing Framework
 
 
design
design
 
 
docs
docs
 
 
production/
session-state
production/
session-state
 
 
src
src
 
 
.gitignore
.gitignore
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
UPGRADING.md
UPGRADING.md
 
 
View all files

## Repository files navigation

# Claude Code Game Studios

Turn a single Claude Code session into a full game development studio.49 agents. 72 skills. One coordinated AI team.

## Why This Exists

Building a game solo with AI is powerful — but a single chat session has no structure. No one stops you from hardcoding magic numbers, skipping design docs, or writing spaghetti code. There's no QA pass, no design review, no one asking "does this actually fit the game's vision?"

Claude Code Game Studiossolves this by giving your AI session the structure of a real studio. Instead of one general-purpose assistant, you get 49 specialized agents organized into a studio hierarchy — directors who guard the vision, department leads who own their domains, and specialists who do the hands-on work. Each agent has defined responsibilities, escalation paths, and quality gates.

The result: you still make every decision, but now you have a team that asks the right questions, catches mistakes early, and keeps your project organized from first brainstorm to launch.

## Table of Contents

* What's Included
* Studio Hierarchy
* Slash Commands
* Getting Started
* Upgrading
* Project Structure
* How It Works
* Design Philosophy
* Customization
* Platform Support
* Community
* Supporting This Project
* License

## What's Included

Category

Count

Description

Agents

49

Specialized subagents across design, programming, art, audio, narrative, QA, and production

Skills

72

Slash commands for every workflow phase (
/start
, 
/design-system
, 
/create-epics
, 
/create-stories
, 
/dev-story
, 
/story-done
, etc.)

Hooks

12

Automated validation on commits, pushes, asset changes, session lifecycle, agent audit trail, and gap detection

Rules

11

Path-scoped coding standards enforced when editing gameplay, engine, AI, UI, network code, and more

Templates

39

Document templates for GDDs, UX specs, ADRs, sprint plans, HUD design, accessibility, and more

## Studio Hierarchy

Agents are organized into three tiers, matching how real studios operate:

Tier 1 — Directors (Opus)
 creative-director technical-director producer

Tier 2 — Department Leads (Sonnet)
 game-designer lead-programmer art-director
 audio-director narrative-director qa-lead
 release-manager localization-lead

Tier 3 — Specialists (Sonnet/Haiku)
 gameplay-programmer engine-programmer ai-programmer
 network-programmer tools-programmer ui-programmer
 systems-designer level-designer economy-designer
 technical-artist sound-designer writer
 world-builder ux-designer prototyper
 performance-analyst devops-engineer analytics-engineer
 security-engineer qa-tester accessibility-specialist
 live-ops-designer community-manager

### Engine Specialists

The template includes agent sets for all three major engines. Use the set that matches your project:

Engine

Lead Agent

Sub-Specialists

Godot 4

godot-specialist

GDScript, Shaders, GDExtension

Unity

unity-specialist

DOTS/ECS, Shaders/VFX, Addressables, UI Toolkit

Unreal Engine 5

unreal-specialist

GAS, Blueprints, Replication, UMG/CommonUI

## Slash Commands

Type/in Claude Code to access all 72 skills:

Onboarding & Navigation/start/help/project-stage-detect/setup-engine/adopt

Game Design/brainstorm/map-systems/design-system/quick-design/review-all-gdds/propagate-design-change

Art & Assets/art-bible/asset-spec/asset-audit

UX & Interface Design/ux-design/ux-review

Architecture/create-architecture/architecture-decision/architecture-review/create-control-manifest

Stories & Sprints/create-epics/create-stories/dev-story/sprint-plan/sprint-status/story-readiness/story-done/estimate

Reviews & Analysis/design-review/code-review/balance-check/content-audit/scope-check/perf-profile/tech-debt/gate-check/consistency-check

QA & Testing/qa-plan/smoke-check/soak-test/regression-suite/test-setup/test-helpers/test-evidence-review/test-flakiness/skill-test/skill-improve

Production/milestone-review/retrospective/bug-report/bug-triage/reverse-document/playtest-report

Release/release-checklist/launch-checklist/changelog/patch-notes/hotfix

Creative & Content/prototype/onboard/localize

Team Orchestration(coordinate multiple agents on a single feature)/team-combat/team-narrative/team-ui/team-release/team-polish/team-audio/team-level/team-live-ops/team-qa

## Getting Started

### Prerequisites

* Git
* Claude Code(npm install -g @anthropic-ai/claude-code)
* Recommended:jq(for hook validation) and Python 3 (for JSON validation)

All hooks fail gracefully if optional tools are missing — nothing breaks, you just lose validation.

### Setup

1. Clone or use as template:git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-gamecdmy-game
2. Open Claude Codeand start a session:claude
3. Run/start— the system asks where you are (no idea, vague concept,
clear design, existing work) and guides you to the right workflow. No assumptions.Or jump directly to a specific skill if you already know what you need:* /brainstorm— explore game ideas from scratch
* /setup-engine godot 4.6— configure your engine if you already know
* /project-stage-detect— analyze an existing project

## Upgrading

Already using an older version of this template? SeeUPGRADING.mdfor step-by-step migration instructions, a breakdown of what changed between
versions, and which files are safe to overwrite vs. which need a manual merge.

## Project Structure

CLAUDE.md # Master configuration
.claude/
 settings.json # Hooks, permissions, safety rules
 agents/ # 49 agent definitions (markdown + YAML frontmatter)
 skills/ # 72 slash commands (subdirectory per skill)
 hooks/ # 12 hook scripts (bash, cross-platform)
 rules/ # 11 path-scoped coding standards
 statusline.sh # Status line script (context%, model, stage, epic breadcrumb)
 docs/
 workflow-catalog.yaml # 7-phase pipeline definition (read by /help)
 templates/ # 39 document templates
src/ # Game source code
assets/ # Art, audio, VFX, shaders, data files
design/ # GDDs, narrative docs, level designs
docs/ # Technical documentation and ADRs
tests/ # Test suites (unit, integration, performance, playtest)
tools/ # Build and pipeline tools
prototypes/ # Throwaway prototypes (isolated from src/)
production/ # Sprint plans, milestones, release tracking

## How It Works

### Agent Coordination

Agents follow a structured delegation model:

1. Vertical delegation— directors delegate to leads, leads delegate to specialists
2. Horizontal consultation— same-tier agents can consult each other but can't make binding cross-domain decisions
3. Conflict resolution— disagreements escalate up to the shared parent (creative-directorfor design,technical-directorfor technical)
4. Change propagation— cross-department changes are coordinated byproducer
5. Domain boundaries— agents don't modify files outside their domain without explicit delegation

### Collaborative, Not Autonomous

This isnotan auto-pilot system. Every agent follows a strict collaboration protocol:

1. Ask— agents ask questions before proposing solutions
2. Present options— agents show 2-4 options with pros/cons
3. You decide— the user always makes the call
4. Draft— agents show work before finalizing
5. Approve— nothing gets written without your sign-off

You stay in control. The agents provide structure and expertise, not autonomy.

### Automated Safety

Hooksrun automatically on every session:

Hook

Trigger

What It Does

validate-commit.sh

PreToolUse (Bash)

Checks for hardcoded values, TODO format, JSON validity, design doc sections — exits early if the command is not 
git commit

validate-push.sh

PreToolUse (Bash)

Warns on pushes to protected branches — exits early if the command is not 
git push

validate-assets.sh

PostToolUse (Write/Edit)

Validates naming conventions and JSON structure — exits early if the file is not in 
assets/

session-start.sh

Session open

Shows current branch and recent commits for orientation

detect-gaps.sh

Session open

Detects fresh projects (suggests 
/start
) and missing design docs when code or prototypes exist

pre-compact.sh

Before compaction

Preserves session progress notes

post-compact.sh

After compaction

Reminds Claude to restore session state from 
active.md

notify.sh

Notification event

Shows Windows toast notification via PowerShell

session-stop.sh

Session close

Archives 
active.md
 to session log and records git activity

log-agent.sh

Agent spawned

Audit trail start — logs subagent invocation

log-agent-stop.sh

Agent stops

Audit trail stop — completes subagent record

validate-skill-change.sh

PostToolUse (Write/Edit)

Advises running 
/skill-test
 after any 
.claude/skills/
 change

Note:validate-commit.sh,validate-assets.sh, andvalidate-skill-change.shfire on every Bash/Write tool call and exit immediately (exit 0) when the command or file path is not relevant. This is normal hook behavior — not a performance concern.

Permission rulesinsettings.jsonauto-allow safe operations (git status, test runs) and block dangerous ones (force push,rm -rf, reading.envfiles).

### Path-Scoped Rules

Coding standards are automatically enforced based on file location:

Path

Enforces

src/gameplay/**

Data-driven values, delta time usage, no UI references

src/core/**

Zero allocations in hot paths, thread safety, API stability

src/ai/**

Performance budgets, debuggability, data-driven parameters

src/networking/**

Server-authoritative, versioned messages, security

src/ui/**

No game state ownership, localization-ready, accessibility

design/gdd/**

Required 8 sections, formula format, edge cases

tests/**

Test naming, coverage requirements, fixture patterns

prototypes/**

Relaxed standards, README required, hypothesis documented

## Design Philosophy

This template is grounded in professional game development practices:

* MDA Framework— Mechanics, Dynamics, Aesthetics analysis for game design
* Self-Determination Theory— Autonomy, Competence, Relatedness for player motivation
* Flow State Design— Challenge-skill balance for player engagement
* Bartle Player Types— Audience targeting and validation
* Verification-Driven Development— Tests first, then implementation

## Customization

This is atemplate, not a locked framework. Everything is meant to be customized:

* Add/remove agents— delete agent files you don't need, add new ones for your domains
* Edit agent prompts— tune agent behavior, add project-specific knowledge
* Modify skills— adjust workflows to match your team's process
* Add rules— create new path-scoped rules for your project's directory structure
* Tune hooks— adjust validation strictness, add new checks
* Pick your engine— use the Godot, Unity, or Unreal agent set (or none)
* Set review intensity—full(all director gates),lean(phase gates only), orsolo(none). Set during/startor editproduction/review-mode.txt. Override per-run with--review soloon any skill.

## Platform Support

Tested onWindows 10with Git Bash. All hooks use POSIX-compatible patterns (grep -E, notgrep -P) and include fallbacks for missing tools. Works on macOS and Linux without modification.

## Community

* Discussions—GitHub Discussionsfor questions, ideas, and showcasing what you've built
* Issues—Bug reports and feature requests

## Supporting This Project

Claude Code Game Studios is free and open source. If it saves you time or helps you ship your game, consider supporting continued development:

  
 

* Buy Me a Coffee— one-time support
* GitHub Sponsors— recurring support through GitHub

Sponsorships help fund time spent maintaining skills, adding new agents, keeping up with Claude Code and engine API changes, and responding to community issues.

Built for Claude Code. Maintained and extended — contributions welcome viaGitHub Discussions.

## License

MIT License. SeeLICENSEfor details.

## About

Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.

### Topics

 gamedev

 unity

 game-development

 godot

 unreal-engine

 game-design

 ai-agents

 claude

 indie-game-dev

 ai-assisted-development

 anthropic

 claude-code

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

9.8k

 stars
 

### Watchers

114

 watching
 

### Forks

1.5k

 forks
 

 Report repository

 

## Releases4

v1.0.0-beta — Claude Code Game Studios

 Latest

 

Apr 7, 2026

 

+ 3 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* buymeacoffee.com/donchitos3

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Shell100.0%