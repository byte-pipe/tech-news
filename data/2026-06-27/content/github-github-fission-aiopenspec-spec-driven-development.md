---
title: 'GitHub - Fission-AI/OpenSpec: Spec-driven development (SDD) for AI coding assistants. · GitHub'
url: https://github.com/Fission-AI/OpenSpec
site_name: github
content_file: github-github-fission-aiopenspec-spec-driven-development
fetched_at: '2026-06-27T11:33:42.180178'
original_url: https://github.com/Fission-AI/OpenSpec
author: Fission-AI
description: Spec-driven development (SDD) for AI coding assistants. - Fission-AI/OpenSpec
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 Fission-AI

 

/

OpenSpec

Public

* NotificationsYou must be signed in to change notification settings
* Fork4k
* Star56.9k

 
 
 
 
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

608 Commits
608 Commits
.changeset
.changeset
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
assets
assets
 
 
bin
bin
 
 
docs
docs
 
 
openspec
openspec
 
 
schemas/
spec-driven
schemas/
spec-driven
 
 
scripts
scripts
 
 
src
src
 
 
test
test
 
 
.actrc
.actrc
 
 
.coderabbit.yaml
.coderabbit.yaml
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CHANGELOG.md
CHANGELOG.md
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
README.md
README.md
 
 
README_OLD.md
README_OLD.md
 
 
build.js
build.js
 
 
eslint.config.js
eslint.config.js
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
openspec-parallel-merge-plan.md
openspec-parallel-merge-plan.md
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
tsconfig.json
tsconfig.json
 
 
vitest.config.ts
vitest.config.ts
 
 
vitest.setup.ts
vitest.setup.ts
 
 
View all files

## Repository files navigation

The most loved spec framework.

Our philosophy:

→ fluid not rigid
→ iterative not waterfall
→ easy not complex
→ built for brownfield not just greenfield
→ scalable from personal projects to enterprises

Tip

New workflow now available!We've rebuilt OpenSpec with a new artifact-guided workflow.

Run/opsx:propose "your idea"to get started. →Learn more here

Follow@0xTab on Xfor updates · Join theOpenSpec Discordfor help and questions.

## See it in action

You: /opsx:explore
AI: What would you like to explore?
You: I want dark mode but I'm not sure how to do it cleanly.
AI: Let me look at your styling setup...
 Cleanest path here: CSS variables + a small theme context,
 with system-preference detection. No new dependencies. Scope it?
You: Yes, let's do it.

You: /opsx:propose add-dark-mode
AI: Created openspec/changes/add-dark-mode/
 ✓ proposal.md — why we're doing this, what's changing
 ✓ specs/ — requirements and scenarios
 ✓ design.md — technical approach
 ✓ tasks.md — implementation checklist
 Ready for implementation!

You: /opsx:apply
AI: Implementing tasks...
 ✓ 1.1 Add theme context provider
 ✓ 1.2 Create toggle component
 ✓ 2.1 Add CSS variables
 ✓ 2.2 Wire up localStorage
 All tasks complete!

You: /opsx:archive
AI: Archived to openspec/changes/archive/2025-01-23-add-dark-mode/
 Specs updated. Ready for the next feature.

OpenSpec Dashboard

## Quick Start

Requires Node.js 20.19.0 or higher.

Install OpenSpec globally:

npm install -g @fission-ai/openspec@latest

Then navigate to your project directory and initialize:

cd
 your-project
openspec init

Now talk to your AI:

* Not sure what to build yet?Start with/opsx:explore, a no-stakes thinking partner that reads your code, weighs options, and shapes a plan before anything is written. (Explore guide)
* Already know what you want?Go straight to/opsx:propose <what-you-want-to-build>.

Both are in the default profile. If you want the expanded workflow (/opsx:new,/opsx:continue,/opsx:ff,/opsx:verify,/opsx:bulk-archive,/opsx:onboard), select it withopenspec config profileand apply withopenspec update.

Note

Not sure if your tool is supported?View the full list– we support 25+ tools and growing.

Also works with pnpm, yarn, bun, and nix.See installation options.

## Docs

Start here:theDocumentation Homemaps everything. New to OpenSpec? ReadGetting Started, thenHow Commands Work(where you actually type/opsx:propose).

→Getting Started: first steps→Explore First: think it through with/opsx:explorebefore you commit→How Commands Work: where slash commands run vs the CLI→Core Concepts at a Glance: the whole mental model, one page→Examples & Recipes: real changes, start to finish→Workflows: combos and patterns→Existing Projects: adopt OpenSpec on a brownfield codebase→Editing a Change: update artifacts, go back, reconcile manual edits→Commands: slash commands & skills→CLI: terminal reference→Stores: plan in a separate repo, shared across your team (beta)→Supported Tools: tool integrations & install paths→Concepts: how it all fits→Multi-Language: multi-language support→Customization: make it yours→FAQ·Troubleshooting·Glossary: quick help

## Community schemas

Third-party schema bundles distributed via standalone repositories — these provide opinionated workflows that integrate OpenSpec with other tools, similar to howgithub/spec-kit's community extension cataloghandles tool integrations.

→Browse the catalogin the customization docs.

## Why OpenSpec?

AI coding assistants are powerful but unpredictable when requirements live only in chat history. OpenSpec adds a lightweight spec layer so you agree on what to build before any code is written.

* Agree before you build— human and AI align on specs before code gets written
* Stay organized— each change gets its own folder with proposal, specs, design, and tasks
* Work fluidly— update any artifact anytime, no rigid phase gates
* Use your tools— works with 20+ AI assistants via slash commands

### How we compare

vs.Spec Kit(GitHub) — Thorough but heavyweight. Rigid phase gates, lots of Markdown, Python setup. OpenSpec is lighter and lets you iterate freely.

vs.Kiro(AWS) — Powerful but you're locked into their IDE and limited to Claude models. OpenSpec works with the tools you already use.

vs. nothing— AI coding without specs means vague prompts and unpredictable results. OpenSpec brings predictability without the ceremony.

## Updating OpenSpec

Upgrade the package

npm install -g @fission-ai/openspec@latest

Refresh agent instructions

Run this inside each project to regenerate AI guidance and ensure the latest slash commands are active:

openspec update

## Usage Notes

Model selection: OpenSpec works best with high-reasoning models. We recommend Codex 5.5 and Opus 4.7 for both planning and implementation.

Context hygiene: OpenSpec benefits from a clean context window. Clear your context before starting implementation and maintain good context hygiene throughout your session.

## Contributing

Small fixes— Bug fixes, typo corrections, and minor improvements can be submitted directly as PRs.

Larger changes— For new features, significant refactors, or architectural changes, please submit an OpenSpec change proposal first so we can align on intent and goals before implementation begins.

When writing proposals, keep the OpenSpec philosophy in mind: we serve a wide variety of users across different coding agents, models, and use cases. Changes should work well for everyone.

AI-generated code is welcome— as long as it's been tested and verified. PRs containing AI-generated code should mention the coding agent and model used (e.g., "Generated with Claude Code using claude-opus-4-5-20251101").

### Development

* Install dependencies:pnpm install
* Build:pnpm run build
* Test:pnpm test
* Develop CLI locally:pnpm run devorpnpm run dev:cli
* Conventional commits (one-line):type(scope): subject

## Other

Telemetry

OpenSpec collects anonymous usage stats.

We collect only command names and version to understand usage patterns. No arguments, paths, content, or PII. Automatically disabled in CI.

Opt-out:export OPENSPEC_TELEMETRY=0orexport DO_NOT_TRACK=1

Maintainers & Advisors

SeeMAINTAINERS.mdfor the list of core maintainers and advisors who help guide the project.

## License

MIT

## About

Spec-driven development (SDD) for AI coding assistants.

openspec.dev/

### Topics

 engineering

 ai

 spec

 planning

 specification

 prd

 sdlc

 sdd

 spec-driven-development

 context-engineering

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

56.9k

 stars
 

### Watchers

247

 watching
 

### Forks

4k

 forks
 

 Report repository

 

## Releases38

v1.4.1 - Update Fix

 Latest

 

Jun 3, 2026

 

+ 37 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript99.2%
* Other0.8%