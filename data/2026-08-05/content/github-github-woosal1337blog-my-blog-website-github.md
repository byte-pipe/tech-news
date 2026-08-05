---
title: 'GitHub - woosal1337/blog: My blog website. · GitHub'
url: https://github.com/woosal1337/blog
site_name: github
content_file: github-github-woosal1337blog-my-blog-website-github
fetched_at: '2026-08-05T12:53:09.824721'
original_url: https://github.com/woosal1337/blog
author: woosal1337
description: My blog website. Contribute to woosal1337/blog development by creating an account on GitHub.
---

woosal1337

 

/

blog

Public

* NotificationsYou must be signed in to change notification settings
* Fork30
* Star366

 
 
 
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

64 Commits
64 Commits
.claude
.claude
 
 
app
app
 
 
components
components
 
 
data
data
 
 
lib
lib
 
 
public
public
 
 
types
types
 
 
videos/
ep01-the-cure-for-ai-slop
videos/
ep01-the-cure-for-ai-slop
 
 
.gitignore
.gitignore
 
 
.nvmrc
.nvmrc
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
bun.lock
bun.lock
 
 
components.json
components.json
 
 
mdx-components.tsx
mdx-components.tsx
 
 
next.config.mjs
next.config.mjs
 
 
package.json
package.json
 
 
postcss.config.mjs
postcss.config.mjs
 
 
renovate.json
renovate.json
 
 
tailwind.config.ts
tailwind.config.ts
 
 
tsconfig.json
tsconfig.json
 
 
vaulted.toml
vaulted.toml
 
 
View all files

## Repository files navigation

# chele.bi

Personal blog and portfolio ofEge Chelebi(@woosal1337).

A dark, editorial personal site — writing, projects, and a reading shelf — built with Next.js 14 (App Router), MDX, Tailwind CSS, and Biome, deployed on Vercel.

## Highlights

* Editorial dark theme: Geist Sans for reading, Geist Mono for code, hairline borders, one motion curve.
* MDX blog with a left-rail table of contents, callouts, and per-post chrome.
* Post banners generated from the title — a deterministic contour mark (lib/contour.ts), no manual cover images.
* Liquid-glass circular controls and frosted-glass tags.
* A single contour identity mark drives the logo and favicons.

## Stack

* Next.js 14 (App Router), React 18, TypeScript
* MDX posts colocated underapp/(website)/blog/(post)/[slug]/page.mdx
* Tailwind CSS with a token layer inapp/globals.css(dark, editorial)
* Reusable design-system primitives incomponents/ds/, domain blocks incomponents/blocks/
* Biome for linting and formatting

## Local setup

bun install
bun dev

Requires Node >= 20 and Bun. No environment variables required.

## Commands

* bun dev— dev server
* bun run build— production build
* bun run check— Biome lint and format with auto-fix

## Credits

The live ASCII surfaces incomponents/blocks/ascii/— donut, flow, plasma, tunnel — are ported fromcobanov/soft-club-ui(MIT) and retuned monochrome against this site's tokens. The table-of-contents marker geometry followsncdai's LineNav.

## License

Code is MIT. Blog content and images are all rights reserved. SeeLICENSE.