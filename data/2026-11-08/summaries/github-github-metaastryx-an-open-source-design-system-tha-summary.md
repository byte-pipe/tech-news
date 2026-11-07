---
title: "GitHub - meta/astryx: An open source design system that's fully customizable and agent ready · GitHub"
url: https://github.com/meta/astryx
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:03:30.331393
---

# GitHub - meta/astryx: An open source design system that's fully customizable and agent ready · GitHub

# Astryx – Open source design system

## Overview
- Developed at Meta over eight years; powers 13,000+ apps.
- Provides 150+ accessible React components, brand‑level theming, dark mode, templates, and a CLI.
- Built with React 19+ and StyleX; no build plugins or styling libraries required.
- Designed for both human developers and AI agents.

## Key differentiators
- **Open internals** – components are fully composable; `swizzle` can eject source for deep customization.
- **No styling lock‑in** – styles authored with StyleX but can be overridden via `className`, Tailwind, CSS modules, etc.
- **Theme customization** – themes are CSS custom‑property overrides, allowing designers to modify appearance without forking.
- **Agent‑ready** – API, docs, and CLI are structured so AI assistants can use the same tooling as people.

## Getting started
- Requires React 19+ (peer dependencies of `@astryxdesign/core`).
- Install core, a theme, StyleX, and the CLI (npm, pnpm, or yarn examples provided).
- Optional global CLI install (`npm i -g @astryxdesign/cli`) for use across projects.
- Minimal setup: import CSS, add a theme provider; no extra PostCSS/Babel config needed.
- Add a script in `package.json` to run the CLI reliably (`npm run astryx -- …`).

## Packages
- `@astryxdesign/core` – components, theme system, utilities.
- `@astryxdesign/cli` – documentation, templates, scaffolding, codemods.
- `@astryxdesign/build` – StyleX build plugins.
- `@astryxdesign/theme-*` – seven ready‑made, fully customizable themes.
- Experimental/internal packages (`@astryxdesign/lab`, `@astryxdesign/vega`, `@astryxdesign/charts`) are not yet stable releases.

## Principles
- **Guidance over enforcement** – components accept values without restrictive guardrails.
- **Strong, documented conventions** – consistent naming, props, composition; thorough docs enable predictability for both people and AI.
- **Human‑and‑AI parity** – API, docs, and CLI are co‑designed for equal usability.
- **Earned by measurement** – conventions are tested and revisited based on empirical results.

## Architecture
- **Foundations** – typography, color, layout, accessibility.
- **Components** – 150+ reusable UI blocks with full TypeScript support.
- **Patterns** – proven solutions for tables, forms, navigation, and other common workflows.

## Project structure
- `apps/` – example apps, documentation site, Storybook.
- `packages/` – published npm packages (core, CLI, build, themes).
- `internal/` – internal tooling, test utilities, ESLint plugin, vibe tests.

## Contributing
- Contributions welcomed; see `CONTRIBUTING.md` for guidelines.
- Community support via Discord.
- Conventions and review rubrics are documented in the contributing wiki.
- Uses Node 22+ (LTS) and pnpm 11; install via Corepack (`corepack enable`) or directly.
- Run theme showcase DOM tests with Vitest (`pnpm exec vitest run --project ui apps/docsite/src/__tests__/theme-showcase/`).

## License
- Distributed under the MIT License.