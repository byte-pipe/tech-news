---
title: 'GitHub - DavidHDev/canvas-ui: A library of creative canvas components. Real HTML with WebGL effects running over it. React, Vue, Svelte, vanilla. · GitHub'
url: https://github.com/DavidHDev/canvas-ui
site_name: tldr
content_file: tldr-github-davidhdevcanvas-ui-a-library-of-creative-ca
fetched_at: '2026-07-24T19:32:44.420914'
original_url: https://github.com/DavidHDev/canvas-ui
date: '2026-07-24'
description: A library of creative canvas components. Real HTML with WebGL effects running over it. React, Vue, Svelte, vanilla. - DavidHDev/canvas-ui
tags:
- tldr
---

DavidHDev

 

/

canvas-ui

Public

* NotificationsYou must be signed in to change notification settings
* Fork59
* Star1.6k

 
 
 
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

42 Commits
42 Commits
.github
.github
 
 
public
public
 
 
scripts
scripts
 
 
src
src
 
 
.gitignore
.gitignore
 
 
LICENSE.md
LICENSE.md
 
 
README.md
README.md
 
 
components.json
components.json
 
 
eslint.config.mjs
eslint.config.mjs
 
 
next.config.ts
next.config.ts
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
postcss.config.mjs
postcss.config.mjs
 
 
tsconfig.json
tsconfig.json
 
 
wrangler.jsonc
wrangler.jsonc
 
 
View all files

## Repository files navigation

# Canvas UI

An open source library of creative, framework-agnostic components drawn on canvas. Fluid simulations, shader effects, and 3D scenes that run over your live, fully interactive interface.

canvasui.dev·Docs·Components

## What makes it different

Most of the library is built on the experimentalhtml-in-canvasAPI, which lets WebGL effects read and redraw your live DOM. Text stays selectable, links stay clickable, and the whole page becomes a texture that fire, fluid, and glass can distort in real time.

Where html-in-canvas is not supported, components degrade gracefully to pure WebGL overlays, so every visitor gets a working page.

* 25 componentsand counting: Liquid, Blaze, Glass, Shatter, VHS, Particle Reveal, and more
* Framework agnostic: React, Solid, Vue, Svelte, and vanilla JS builds for every component
* Copy, do not install: components ship as source through a shadcn-compatible registry
* Zero config: each component is self-contained with sensible defaults and typed props
* MCP ready: point the shadcn MCP server at the registry and let your AI assistant install components

## Quick start

Add a component with the shadcn CLI (runnpx shadcn@latest initfirst if you have not used it before):

npx shadcn@latest add @canvas-ui/liquid-react

Swapliquidfor any component andreactforsolid,vue,svelte, orvanilla. The source lands incomponents/canvasui/in your project (Svelte:src/lib/components/canvasui/), yours to edit.

See theinstallation guidefor manual setup and framework notes.

## Browser support

The full html-in-canvas experience currently requires Chrome or Edge 140+ with thechrome://flags/#canvas-draw-elementflag enabled (for production sites, anorigin trialtoken is available). Everywhere else, components automatically fall back to WebGL overlay rendering. Details in thedocs.

## Development

This repo contains the library source (src/lib), the documentation site (Next.js 16, Tailwind v4, deployed to Cloudflare Workers), and the registry build.

npm install
npm run dev 
#
 builds the registry, then starts next dev

npm run build 
#
 production build

npm run deploy 
#
 build and deploy to Cloudflare

## Contributing

Issues and pull requests are welcome. SeeCONTRIBUTING.mdto get started.

## License

MIT + Commons Clause. Free to use in your own projects, commercial or not. The Commons Clause only restricts selling the library itself.