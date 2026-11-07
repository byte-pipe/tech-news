---
title: 'GitHub - meta/astryx: An open source design system that''s fully customizable and agent ready · GitHub'
url: https://github.com/meta/astryx
site_name: github
content_file: github-github-metaastryx-an-open-source-design-system-tha
fetched_at: '2026-11-08T09:02:54.496561'
original_url: https://github.com/meta/astryx
author: meta
description: An open source design system that's fully customizable and agent ready - meta/astryx
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

6,927 Commits
6,927 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.changeset
.changeset
 
 
.claude
.claude
 
 
.github
.github
 
 
.husky
.husky
 
 
apps
apps
 
 
docs
docs
 
 
internal
internal
 
 
packages
packages
 
 
scripts
scripts
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.nvmrc
.nvmrc
 
 
.prettierrc.json
.prettierrc.json
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
IME_GUARD_DESIGN.md
IME_GUARD_DESIGN.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
crowdin.yml
crowdin.yml
 
 
eslint.config.js
eslint.config.js
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
playwright.interaction.config.ts
playwright.interaction.config.ts
 
 
playwright.perf.config.ts
playwright.perf.config.ts
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
tsconfig.json
tsconfig.json
 
 
vitest.config.ts
vitest.config.ts
 
 
vitest.global-setup.node.mjs
vitest.global-setup.node.mjs
 
 
View all files

## Repository files navigation

# Astryx

An open source design system that's fully customizable and built for how we build now:by people and the agents working alongside them.

Currently in Beta· Built onReact 19+andStyleX

Docs·Storybook·Sandbox·Contributing·Discord

## Overview

Astryx is an open source design system that grew inside Meta over the last eight years, where it became the most-used and largest design system in the company — powering 13,000+ apps and shaped by the engineers, designers, and product teams who depend on it every day.

It ships 150+ accessible components, brand-level theming, dark mode, ready-to-ship templates, and a CLI as one cohesive system. You import pre-built CSS and use typed React components — no build plugin, no styling library to adopt — and both people and AI assistants build with the same tooling.

What makes Astryx different:

* Open internals.Components are built to be composed at any level, not locked behind a closed top-level API. The building blocks you'd reach for are exported directly, and when you need to go deeper, swizzle ejects a component's full source into your project to own.
* No styling lock-in.Astryx authors its styles with StyleX, but that's invisible to consumers. Override withclassNameusing Tailwind, CSS modules, or plain CSS — whatever your project already uses.
* Customize without wrapping.A theme is a set of CSS custom property overrides, so a designer can make Astryx unmistakably theirs without forking or wrapping component source.
* Built for people and agents.The API, docs, and CLI are designed together so a person and an AI assistant build the same way, from the same reference.

## Getting Started

Astryx requiresReact 19or later (reactandreact-domare peer dependencies of@astryxdesign/core).

Install Astryx, a theme, and its peer dependencies:

#
 npm

npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
npm install -D @astryxdesign/cli

#
 pnpm

pnpm add @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
pnpm add -D @astryxdesign/cli

#
 yarn

yarn add @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex
yarn add -D @astryxdesign/cli

You can also install the CLI once for your computer, soastryxworks in any folder and every coding agent knows Astryx; in a project, it still runs that project's own version:

npm i -g @astryxdesign/cli

Project install, global install, or both?astryx docs global/project-global-or-bothcompares them (both is recommended), andastryx docs globalexplains how global mode works.

The simplest setup is a few CSS imports plus a theme provider — no build plugin, no PostCSS or Babel config. See the@astryxdesign/core READMEfor the full guide (Next.js, Tailwind, Vite, and CDN).

For reliable CLI access, add a script to yourpackage.json:

"scripts"
: {
 
"astryx"
: 
"
node node_modules/@astryxdesign/cli/clients/cli/bin/astryx.mjs
"

}

Then use it asnpm run astryx -- component --list. This avoids path errors when AI assistants or new developers invoke the CLI directly.

## Packages

Package

Description

README

@astryxdesign/core

Components, theme system, and utilities

README

@astryxdesign/cli

CLI tooling: component docs, templates, scaffolding, themes, and codemods

README

@astryxdesign/build

Build plugins for StyleX source builds

README

@astryxdesign/theme-*

Seven ready-made, fully customizable themes (neutral, butter, chocolate, matcha, stone, gothic, y2k)

README

@astryxdesign/lab(experimental components) is used internally for Storybook and the sandbox and is not published to npm.@astryxdesign/vega(Vega/Vega-Lite chart wrapper) and@astryxdesign/charts(chart components) are published to npm only under the@canarydist-tag — there is no stable release yet.

## Principles

These are the promises Astryx makes to the people building on it.

* Guidance over enforcement.Components give you capability rather than guardrails that fight you. Design opinions live in docs and examples — if you pass a value, the component renders it.
* Strong, documented conventions.Every component follows the same naming, prop, and composition rules, and every one is thoroughly documented — so once you've learned a few, the rest feel familiar, and both people and AI can predict how an unfamiliar component behaves.
* One system for humans and AI.The API, conventions, docs, and CLI are designed together so people and AI assistants build the same way. Every change that made Astryx easier for AI made it easier for people too.
* Earned by measurement.We test conventions rather than assert them, hold the results loosely, and revisit them when a new situation proves them wrong.

## Architecture

### Foundations

The building blocks for visually cohesive and accessible interfaces: typography, color, layout, and accessibility.

### Components

A library of 150+ reusable UI building blocks with full TypeScript support.

### Patterns

Battle-tested design solutions for common interactions and workflows: table pages, detail page layouts, form wizards, navigation patterns, data entry flows.

## Project Structure

Directory

Purpose

apps/

Example apps, the docsite, and Storybook

packages/

Published packages: core, cli, build, themes

internal/

Internal tooling: test utilities, eslint plugin, vibe tests

## Contributing

We welcome contributions! SeeCONTRIBUTING.mdfor the full guide.

Questions, or want a hand with a PR? Come find us inDiscord.

Our conventions and review rubrics live in theContributing wiki—
includingAPI Conventions,Design Conventions,
theComponent Lifecycle,
theContributing Templates,
and theBlog Review Rubric. Read the relevant rubric before opening a PR.

Quick start for contributors: this repo usesNode 22+ on an active LTS lineandpnpm 11. Install pnpm directly, or enableCorepackonce so the pinned pnpm version
installs automatically:

corepack 
enable

pnpm install

Ifcorepackis missing, install pnpm directly or install Corepack manually;
see the troubleshooting notes inCONTRIBUTING.md.

The Theme Showcase DOM tests use the rootuiproject for shared DOM and
StyleX test setup. Runpnpm exec vitest run --project ui apps/docsite/src/__tests__/theme-showcase/from the repository root.

## License

MIT