---
title: Bootstrap 6 Alpha | Bootstrap Blog
url: https://blog.getbootstrap.com/2026/10/08/bootstrap-6-alpha
date: 2026-10-09
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-09T10:16:59.616227
---

# Bootstrap 6 Alpha | Bootstrap Blog

# Bootstrap 6 Alpha – Overview

## Hold up…
- Announcing the first alpha of Bootstrap 6, a complete rewrite using the Sass module system, native browser APIs, ESM‑only JavaScript, and new CSS standards.  
- The project has been quiet while the author focused on other work, but the goal remains: help anyone—human or AI, novice or pro—build software faster.

## Community appreciation
- Thanks to co‑maintainer Julien for handling reviews, dependencies, and migrations.  
- Gratitude to the listed contributors and supporters on Open Collective who filed issues, submitted patches, and participated in pull requests.

## Get started
- Bootstrap 6 Alpha 1 is available on npm (`npm i bootstrap@6.0.0-alpha.1`) and via jsDelivr CDN.  
- JavaScript is ESM‑only, so the `<script>` tag must include `type="module"`.  
- Links to the Install and Quickstart pages are provided, with a migration guide for v5 users.

## Modern browser support
- Minimum supported versions: Chrome 130, Edge 130, Firefox 132, Safari 18.  
- The higher floor allows use of modern features such as `light‑dark()`, `:has()`, container queries, `oklch()`, `color‑mix()`, and the native `<dialog>` element, without fallbacks or polyfills.  
- Bootstrap 5 will remain supported for projects that cannot meet the new baseline; v5.4.0 will be released before an end‑of‑life date is set.

## Spotlight: CSS‑first Sass modules
- Bootstrap 6 adopts the `@use/@forward` module system; customization is now done through **token maps**, which are Sass maps that generate CSS variables.  
- Nearly all former Sass variables are now CSS variables stored in token maps, enabling runtime customization in the browser.  
- Example token map for the `alert` component shows default values and how they are applied with `@layer components`.  
- Global tokens (`$root‑tokens`) and component‑specific tokens (`$alert‑tokens`, etc.) can be overridden via the `with` clause when importing Bootstrap.  
- Prefix handling has moved from a Sass `$prefix` variable to PostCSS at build time, simplifying the source.  
- Changing a single base value (e.g., `$radius` or `$spacer`) automatically updates the entire scale across components.  
- The new system offers flexible pre‑ and post‑compilation customization, allowing real‑time updates of downstream components—a major improvement over the v5 hybrid approach.