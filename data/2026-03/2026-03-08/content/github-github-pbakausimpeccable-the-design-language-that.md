---
title: 'GitHub - pbakaus/impeccable: The design language that makes your AI harness better at design. · GitHub'
url: https://github.com/pbakaus/impeccable
site_name: github
content_file: github-github-pbakausimpeccable-the-design-language-that
fetched_at: '2026-03-08T11:07:36.466617'
original_url: https://github.com/pbakaus/impeccable
author: pbakaus
description: The design language that makes your AI harness better at design. - pbakaus/impeccable
---

pbakaus



/

impeccable

Public

* NotificationsYou must be signed in to change notification settings
* Fork49
* Star1.2k




 
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

122 Commits
122 Commits
.claude-plugin
.claude-plugin
 
 
.claude/
skills
.claude/
skills
 
 
api
api
 
 
public
public
 
 
scripts
scripts
 
 
server
server
 
 
source/
skills
source/
skills
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.vercelignore
.vercelignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
DEVELOP.md
DEVELOP.md
 
 
LICENSE
LICENSE
 
 
NOTICE.md
NOTICE.md
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
bun.lock
bun.lock
 
 
package.json
package.json
 
 
vercel.json
vercel.json
 
 
View all files

## Repository files navigation

# Impeccable

The vocabulary you didn't know you needed. 1 skill, 17 commands, and curated anti-patterns for impeccable frontend design.

Quick start:Visitimpeccable.styleto download ready-to-use bundles.

## Why Impeccable?

Anthropic createdfrontend-design, a skill that guides Claude toward better UI design. Impeccable builds on that foundation with deeper expertise and more control.

Every LLM learned from the same generic templates. Without guidance, you get the same predictable mistakes: Inter font, purple gradients, cards nested in cards, gray text on colored backgrounds.

Impeccable fights that bias with:

* An expanded skillwith 7 domain-specific reference files (view source)
* 17 steering commandsto audit, review, polish, distill, animate, and more
* Curated anti-patternsthat explicitly tell the AI what NOT to do

## What's Included

### The Skill: frontend-design

A comprehensive design skill with 7 domain-specific references (view skill):

Reference

Covers

typography

Type systems, font pairing, modular scales, OpenType

color-and-contrast

OKLCH, tinted neutrals, dark mode, accessibility

spatial-design

Spacing systems, grids, visual hierarchy

motion-design

Easing curves, staggering, reduced motion

interaction-design

Forms, focus states, loading patterns

responsive-design

Mobile-first, fluid design, container queries

ux-writing

Button labels, error messages, empty states

### 17 Commands

Command

What it does

/teach-impeccable

One-time setup: gather design context, save to config

/audit

Run technical quality checks (a11y, performance, responsive)

/critique

UX design review: hierarchy, clarity, emotional resonance

/normalize

Align with design system standards

/polish

Final pass before shipping

/distill

Strip to essence

/clarify

Improve unclear UX copy

/optimize

Performance improvements

/harden

Error handling, i18n, edge cases

/animate

Add purposeful motion

/colorize

Introduce strategic color

/bolder

Amplify boring designs

/quieter

Tone down overly bold designs

/delight

Add moments of joy

/extract

Pull into reusable components

/adapt

Adapt for different devices

/onboard

Design onboarding flows

### Anti-Patterns

The skill includes explicit guidance on what to avoid:

* Don't use overused fonts (Arial, Inter, system defaults)
* Don't use gray text on colored backgrounds
* Don't use pure black/gray (always tint)
* Don't wrap everything in cards or nest cards inside cards
* Don't use bounce/elastic easing (feels dated)

## See It In Action

Visitimpeccable.styleto see before/after case studies of real projects transformed with Impeccable commands.

## Installation

### Option 1: Download from Website (Recommended)

Visitimpeccable.style, download the ZIP for your tool, and extract to your project.

### Option 2: Copy from Repository

Cursor:

cp -r dist/cursor/.cursor your-project/

Note:Cursor skills require setup:

1. Switch to Nightly channel in Cursor Settings → Beta
2. Enable Agent Skills in Cursor Settings → Rules

Learn more about Cursor skills

Claude Code:

#
 Project-specific

cp -r dist/claude-code/.claude your-project/

#
 Or global (applies to all projects)

cp -r dist/claude-code/.claude/
*

~
/.claude/

Gemini CLI:

cp -r dist/gemini/.gemini your-project/

Note:Gemini CLI skills require setup:

1. Install preview version:npm i -g @google/gemini-cli@preview
2. Run/settingsand enable "Skills"
3. Run/skills listto verify installation

Learn more about Gemini CLI skills

Codex CLI:

cp -r dist/codex/.codex/
*

~
/.codex/

## Usage

Once installed, use commands in your AI harness:

/audit # Find issues
/normalize # Fix inconsistencies
/polish # Final cleanup
/distill # Remove complexity

Most commands accept an optional argument to focus on a specific area:

/audit header
/polish checkout-form

Note:Codex CLI uses a different syntax:/prompts:audit,/prompts:polish, etc.

## Supported Tools

* Cursor
* Claude Code
* Gemini CLI
* Codex CLI

## Contributing

SeeDEVELOP.mdfor contributor guidelines and build instructions.

## License

Apache 2.0. SeeLICENSE.

The frontend-design skill builds onAnthropic's original. SeeNOTICE.mdfor attribution.

Created byPaul Bakaus

## About

The design language that makes your AI harness better at design.

impeccable.style

### Resources

 Readme



### License

 Apache-2.0 license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

1.2k

 stars


### Watchers

4

 watching


### Forks

49

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* JavaScript46.5%
* CSS32.2%
* HTML21.3%
