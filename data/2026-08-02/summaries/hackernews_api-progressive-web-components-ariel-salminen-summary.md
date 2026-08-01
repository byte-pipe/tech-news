---
title: Progressive Web Components | Ariel Salminen
url: https://arielsalminen.com/2026/progressive-web-components/
date: 2026-07-31
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-02T06:02:12.647375
---

# Progressive Web Components | Ariel Salminen

# Progressive Web Components

## Motivation & Pain Points
- Nearly a decade of experience building enterprise design systems with web components.  
- Recurring issues: layout shifts, flash of unstyled content, limited server‑side rendering, heavy reliance on client‑side JavaScript, poor compatibility with frameworks such as React Server Components, and accessibility challenges.  
- Despite drawbacks, web components remain the only truly cross‑framework solution built on native web standards.  
- The problem lies more in implementation practices than in the component model itself.

## What is a Progressive Web Component?
- A native Custom Element built in two layers:  
  - **Base layer** – HTML and CSS that render instantly without JavaScript.  
  - **Enhancement layer** – JavaScript that adds reactivity, event handling, and advanced templating.  
- Three architectural types:  
  1. **Composite Components** – wrap and enhance user‑provided HTML; all markup and styles live in the Light DOM.  
  2. **Primitive Components** – self‑contained, render their own HTML; CSS also resides in the Light DOM with the initial markup.  
  3. **Declarative Components** – hybrid approach that leverages Declarative Shadow DOM.  
- The taxonomy is a design philosophy, not a forced library constraint; developers can choose any approach.

## Introducing Elena
- A tiny (2.6 kB minified) library for building Progressive Web Components.  
- Core principle: load HTML and CSS first, then progressively add interactivity with JavaScript.  
- Targets teams creating component libraries and design systems that need:  
  - Cross‑framework compatibility.  
  - Immediate HTML/CSS rendering before JavaScript loads.  
  - Mitigation of accessibility, SSR, and layout‑shift issues.  
- Handles prop/attribute syncing, event delegation, and framework interop, letting developers focus on component logic.  
- Fully supports the standard Custom Element lifecycle, open/closed Shadow DOM, `<template>`, `<slot>`, and Declarative Shadow DOM.

## SSR Approach
- Progressive Web Components are primarily HTML/CSS, so they render on the server without special logic.  
- Components without a `render()` method are SSR‑compatible by default.  
- Components with a `render()` method provide partial SSR support: initial markup is rendered server‑side, while full interactivity requires client‑side hydration (or the optional `@elenajs/ssr` tool).  
- Declarative Shadow DOM is supported for cases needing stronger encapsulation while still allowing server‑side rendering.

## Release Candidate & Feature Highlights
- Version 1.0.0‑rc.7 released as the first seventh release candidate.  
- Key features:  
  - Extremely lightweight (2.6 kB minified).  
  - Progressive enhancement – HTML/CSS first, JavaScript hydration later.  
  - Accessible by default through semantic HTML, avoiding Shadow DOM barriers.  
  - Standards‑based, built entirely on native custom elements.  
  - Reactive updates with batched re‑renders on prop or state changes.  
  - Scoped styles without complex workarounds.  
  - SSR‑friendly out of the box, with optional server‑side utilities.  
  - Zero runtime dependencies.  
  - No lock‑in; works with any major framework or none at all.

## Included Packages
- Elena is split into 13 npm packages under the `@elenajs` scope. Core packages for development include:  
  - `@elenajs/core` – main runtime used in most projects.  
  - `@elenajs/bundler` – bundler for Elena component libraries.  
  - `@elenajs/cli` – command‑line interface for scaffolding components.  
  - `@elenajs/ssr` – server‑side rendering utilities.  
  - `@elenajs/mcp` – MCP server support.  
  - `@elenajs/components` – example Progressive Web Components.

## Next Steps & Contact
- Visit the Elena website: https://elenajs.com  
- Review the FAQ for common questions.  
- Explore live examples and the interactive playground.  
- Check the GitHub repository for source code and contributions.  
- For design‑system consulting, contact Ariel Salminen, Design Systems Architect, available for local and remote projects worldwide.