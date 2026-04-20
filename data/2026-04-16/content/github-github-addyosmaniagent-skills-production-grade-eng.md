---
title: 'GitHub - addyosmani/agent-skills: Production-grade engineering skills for AI coding agents. · GitHub'
url: https://github.com/addyosmani/agent-skills
site_name: github
content_file: github-github-addyosmaniagent-skills-production-grade-eng
fetched_at: '2026-04-16T11:58:46.994520'
original_url: https://github.com/addyosmani/agent-skills
author: addyosmani
description: Production-grade engineering skills for AI coding agents. - addyosmani/agent-skills
---

addyosmani



/

agent-skills

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.1k
* Star16.2k




 
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

121 Commits
121 Commits
.claude-plugin
.claude-plugin
 
 
.claude/
commands
.claude/
commands
 
 
.github/
workflows
.github/
workflows
 
 
agents
agents
 
 
docs
docs
 
 
hooks
hooks
 
 
references
references
 
 
skills
skills
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Agent Skills

Production-grade engineering skills for AI coding agents.

Skills encode the workflows, quality gates, and best practices that senior engineers use when building software. These ones are packaged so AI agents follow them consistently across every phase of development.

 DEFINE PLAN BUILD VERIFY REVIEW SHIP
 ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
 │ Idea │ ───▶ │ Spec │ ───▶ │ Code │ ───▶ │ Test │ ───▶ │ QA │ ───▶ │ Go │
 │Refine│ │ PRD │ │ Impl │ │Debug │ │ Gate │ │ Live │
 └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘
 /spec /plan /build /test /review /ship

## Commands

7 slash commands that map to the development lifecycle. Each one activates the right skills automatically.

What you're doing

Command

Key principle

Define what to build

/spec

Spec before code

Plan how to build it

/plan

Small, atomic tasks

Build incrementally

/build

One slice at a time

Prove it works

/test

Tests are proof

Review before merge

/review

Improve code health

Simplify the code

/code-simplify

Clarity over cleverness

Ship to production

/ship

Faster is safer

Skills also activate automatically based on what you're doing — designing an API triggersapi-and-interface-design, building UI triggersfrontend-ui-engineering, and so on.

## Quick Start

Claude Code (recommended)

Marketplace install:

/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills

SSH errors?The marketplace clones repos via SSH. If you don't have SSH keys set up on GitHub, eitheradd your SSH keyor switch to HTTPS for fetches only:

git config --global url.
"
https://github.com/
"
.insteadOf
"
git@github.com:
"

Local / development:

git clone https://github.com/addyosmani/agent-skills.git
claude --plugin-dir /path/to/agent-skills

Cursor

Copy anySKILL.mdinto.cursor/rules/, or reference the fullskills/directory. Seedocs/cursor-setup.md.

Gemini CLI

Install as native skills for auto-discovery, or add toGEMINI.mdfor persistent context. Seedocs/gemini-cli-setup.md.

Install from the repo:

gemini skills install https://github.com/addyosmani/agent-skills.git --path skills

Install from a local clone:

gemini skills install ./agent-skills/skills/

Windsurf

Add skill contents to your Windsurf rules configuration. Seedocs/windsurf-setup.md.

OpenCode

Uses agent-driven skill execution via AGENTS.md and theskilltool.

Seedocs/opencode-setup.md.

GitHub Copilot

Use agent definitions fromagents/as Copilot personas and skill content in.github/copilot-instructions.md. Seedocs/copilot-setup.md.

Kiro IDE & CLI

 Skills for Kiro reside under ".kiro/skills/" and can be stored under Project or Global level. Kiro also supports Agents.md. See Kiro docs at
https://kiro.dev/docs/skills/

Codex / Other Agents

Skills are plain Markdown - they work with any agent that accepts system prompts or instruction files. Seedocs/getting-started.md.

## All 20 Skills

The commands above are the entry points. Under the hood, they activate these 20 skills — each one a structured workflow with steps, verification gates, and anti-rationalization tables. You can also reference any skill directly.

### Define - Clarify what to build

Skill

What It Does

Use When

idea-refine

Structured divergent/convergent thinking to turn vague ideas into concrete proposals

You have a rough concept that needs exploration

spec-driven-development

Write a PRD covering objectives, commands, structure, code style, testing, and boundaries before any code

Starting a new project, feature, or significant change

### Plan - Break it down

Skill

What It Does

Use When

planning-and-task-breakdown

Decompose specs into small, verifiable tasks with acceptance criteria and dependency ordering

You have a spec and need implementable units

### Build - Write the code

Skill

What It Does

Use When

incremental-implementation

Thin vertical slices - implement, test, verify, commit. Feature flags, safe defaults, rollback-friendly changes

Any change touching more than one file

test-driven-development

Red-Green-Refactor, test pyramid (80/15/5), test sizes, DAMP over DRY, Beyonce Rule, browser testing

Implementing logic, fixing bugs, or changing behavior

context-engineering

Feed agents the right information at the right time - rules files, context packing, MCP integrations

Starting a session, switching tasks, or when output quality drops

source-driven-development

Ground every framework decision in official documentation - verify, cite sources, flag what's unverified

You want authoritative, source-cited code for any framework or library

frontend-ui-engineering

Component architecture, design systems, state management, responsive design, WCAG 2.1 AA accessibility

Building or modifying user-facing interfaces

api-and-interface-design

Contract-first design, Hyrum's Law, One-Version Rule, error semantics, boundary validation

Designing APIs, module boundaries, or public interfaces

### Verify - Prove it works

Skill

What It Does

Use When

browser-testing-with-devtools

Chrome DevTools MCP for live runtime data - DOM inspection, console logs, network traces, performance profiling

Building or debugging anything that runs in a browser

debugging-and-error-recovery

Five-step triage: reproduce, localize, reduce, fix, guard. Stop-the-line rule, safe fallbacks

Tests fail, builds break, or behavior is unexpected

### Review - Quality gates before merge

Skill

What It Does

Use When

code-review-and-quality

Five-axis review, change sizing (~100 lines), severity labels (Nit/Optional/FYI), review speed norms, splitting strategies

Before merging any change

code-simplification

Chesterton's Fence, Rule of 500, reduce complexity while preserving exact behavior

Code works but is harder to read or maintain than it should be

security-and-hardening

OWASP Top 10 prevention, auth patterns, secrets management, dependency auditing, three-tier boundary system

Handling user input, auth, data storage, or external integrations

performance-optimization

Measure-first approach - Core Web Vitals targets, profiling workflows, bundle analysis, anti-pattern detection

Performance requirements exist or you suspect regressions

### Ship - Deploy with confidence

Skill

What It Does

Use When

git-workflow-and-versioning

Trunk-based development, atomic commits, change sizing (~100 lines), the commit-as-save-point pattern

Making any code change (always)

ci-cd-and-automation

Shift Left, Faster is Safer, feature flags, quality gate pipelines, failure feedback loops

Setting up or modifying build and deploy pipelines

deprecation-and-migration

Code-as-liability mindset, compulsory vs advisory deprecation, migration patterns, zombie code removal

Removing old systems, migrating users, or sunsetting features

documentation-and-adrs

Architecture Decision Records, API docs, inline documentation standards - document the
why

Making architectural decisions, changing APIs, or shipping features

shipping-and-launch

Pre-launch checklists, feature flag lifecycle, staged rollouts, rollback procedures, monitoring setup

Preparing to deploy to production

## Agent Personas

Pre-configured specialist personas for targeted reviews:

Agent

Role

Perspective

code-reviewer

Senior Staff Engineer

Five-axis code review with "would a staff engineer approve this?" standard

test-engineer

QA Specialist

Test strategy, coverage analysis, and the Prove-It pattern

security-auditor

Security Engineer

Vulnerability detection, threat modeling, OWASP assessment

## Reference Checklists

Quick-reference material that skills pull in when needed:

Reference

Covers

testing-patterns.md

Test structure, naming, mocking, React/API/E2E examples, anti-patterns

security-checklist.md

Pre-commit checks, auth, input validation, headers, CORS, OWASP Top 10

performance-checklist.md

Core Web Vitals targets, frontend/backend checklists, measurement commands

accessibility-checklist.md

Keyboard nav, screen readers, visual design, ARIA, testing tools

## How Skills Work

Every skill follows a consistent anatomy:

┌─────────────────────────────────────────────────┐
│ SKILL.md │
│ │
│ ┌─ Frontmatter ─────────────────────────────┐ │
│ │ name: lowercase-hyphen-name │ │
│ │ description: Guides agents through [task].│ │
│ │ Use when… │ │
│ └───────────────────────────────────────────┘ │
│ Overview → What this skill does │
│ When to Use → Triggering conditions │
│ Process → Step-by-step workflow │
│ Rationalizations → Excuses + rebuttals │
│ Red Flags → Signs something's wrong │
│ Verification → Evidence requirements │
└─────────────────────────────────────────────────┘

Key design choices:

* Process, not prose.Skills are workflows agents follow, not reference docs they read. Each has steps, checkpoints, and exit criteria.
* Anti-rationalization.Every skill includes a table of common excuses agents use to skip steps (e.g., "I'll add tests later") with documented counter-arguments.
* Verification is non-negotiable.Every skill ends with evidence requirements - tests passing, build output, runtime data. "Seems right" is never sufficient.
* Progressive disclosure.TheSKILL.mdis the entry point. Supporting references load only when needed, keeping token usage minimal.

## Project Structure

agent-skills/
├── skills/ # 20 core skills (SKILL.md per directory)
│ ├── idea-refine/ # Define
│ ├── spec-driven-development/ # Define
│ ├── planning-and-task-breakdown/ # Plan
│ ├── incremental-implementation/ # Build
│ ├── context-engineering/ # Build
│ ├── source-driven-development/ # Build
│ ├── frontend-ui-engineering/ # Build
│ ├── test-driven-development/ # Build
│ ├── api-and-interface-design/ # Build
│ ├── browser-testing-with-devtools/ # Verify
│ ├── debugging-and-error-recovery/ # Verify
│ ├── code-review-and-quality/ # Review
│ ├── code-simplification/ # Review
│ ├── security-and-hardening/ # Review
│ ├── performance-optimization/ # Review
│ ├── git-workflow-and-versioning/ # Ship
│ ├── ci-cd-and-automation/ # Ship
│ ├── deprecation-and-migration/ # Ship
│ ├── documentation-and-adrs/ # Ship
│ ├── shipping-and-launch/ # Ship
│ └── using-agent-skills/ # Meta: how to use this pack
├── agents/ # 3 specialist personas
├── references/ # 4 supplementary checklists
├── hooks/ # Session lifecycle hooks
├── .claude/commands/ # 7 slash commands
└── docs/ # Setup guides per tool

## Why Agent Skills?

AI coding agents default to the shortest path - which often means skipping specs, tests, security reviews, and the practices that make software reliable. Agent Skills gives agents structured workflows that enforce the same discipline senior engineers bring to production code.

Each skill encodes hard-won engineering judgment:whento write a spec,whatto test,howto review, andwhento ship. These aren't generic prompts - they're the kind of opinionated, process-driven workflows that separate production-quality work from prototype-quality work.

Skills bake in best practices from Google's engineering culture — including concepts fromSoftware Engineering at Googleand Google'sengineering practices guide. You'll find Hyrum's Law in API design, the Beyonce Rule and test pyramid in testing, change sizing and review speed norms in code review, Chesterton's Fence in simplification, trunk-based development in git workflow, Shift Left and feature flags in CI/CD, and a dedicated deprecation skill treating code as a liability. These aren't abstract principles — they're embedded directly into the step-by-step workflows agents follow.

## Contributing

Skills should bespecific(actionable steps, not vague advice),verifiable(clear exit criteria with evidence requirements),battle-tested(based on real workflows), andminimal(only what's needed to guide the agent).

Seedocs/skill-anatomy.mdfor the format specification andCONTRIBUTING.mdfor guidelines.

## License

MIT - use these skills in your projects, teams, and tools.

## About

Production-grade engineering skills for AI coding agents.

### Topics

 skills

 cursor

 antigravity

 agent-skills

 claude-code

 antigravity-ide

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

16.2k

 stars


### Watchers

127

 watching


### Forks

2.1k

 forks


 Report repository



## Releases1

Agent Skills 0.5.0

 Latest



Apr 10, 2026

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Shell100.0%
