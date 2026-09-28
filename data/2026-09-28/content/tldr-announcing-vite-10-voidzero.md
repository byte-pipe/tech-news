---
title: Announcing Vite+ 1.0 | VoidZero
url: https://voidzero.dev/posts/announcing-vite-plus-1-0
site_name: tldr
content_file: tldr-announcing-vite-10-voidzero
fetched_at: '2026-09-28T18:26:11.569341'
original_url: https://voidzero.dev/posts/announcing-vite-plus-1-0
date: '2026-09-28'
description: Vite+ 1.0 is here. One CLI manages your runtime, package manager, and frontend toolchain.
tags:
- tldr
---

VoidZero is joining Cloudflare
// announcements

# Announcing Vite+ 1.0

SEP 28, 2026
Alexander Lichter, MK, Charles Wang, and Evan You
5 MIN READ
Copy Link

TL;DR:Vite+1.0 is out, stable, MIT licensed, and about to reach two million weekly downloads. A single command,vp, manages your Node.js runtime, package manager, andfrontend toolchain. Install it withcurl -fsSL https://vite.plus | bash, then runvp createfor a new project orvp migrateto migrate your existing one.

Today we are releasingVite+ 1.0, the unified toolchain for the web.

Vite+ is a single entry point to web development, built by the team behindVite,Vitest,Rolldown, andOxc.

It is neither a framework, nor a package manager anddefinitely not a replacement for Vite. Instead, Vite+ ties the tools you already use into one tested stack with a single config file and a consistent set of commands.

Vite+ is free,open source under MIT, and framework-agnostic. Whether you ship a React app, a Vue component library, a Node CLI, or a 400-package monorepo, the commands stay the same. Your project does not even have to use Vite in the first place!

## The cost of assembling your own toolchain​

Starting a web project means a lot of choices to make before even starting to write your first line of code:

* picking a runtime,
* choosing a package manager,
* deciding on a dev server,
* setting up a linter, a formatter, a test runner, a bundler, you name it.

Each one brings its own config files, release cadence, commands, and its own upgrade guide. And that matters for youat least twice. First when you pick the tool stack (or get onboarded to it), then every time things drift apart:

* the linter disagrees with the formatter,
* CI runs different commands than you do locally,
* one repo is two majors behind another,
* and the person who originally set it up is on vacation.

Teams with more than a handful of repositories usually end up building internal scripts to paper over this, which then need their own maintainers.But instead of maintaining a tool stack, you often just want to ship features.

## What Vite+ offers​

Nine commands cover the local development cycle:

Command
What it does
Powered by
vp create
Scaffold an app, a library, or a monorepo
Vite+ and framework templates
vp install
Install dependencies with the project's package manager
Your package manager of choice
vp dev
Dev server with HMR
Vite 8
 and 
Rolldown
vp check
Format, lint, and type-check in one pass
Oxfmt
 and 
Oxlint
vp test
Unit, component, and browser tests
Vitest
vp build
Production app builds
Vite 8
 and 
Rolldown
vp pack
Library builds and standalone binaries
tsdown
vp run
Monorepo-aware task runner with caching
Vite Task
vp env
Node.js version management
Vite+

Onevite.config.tsat the project root configures all of them. Runvpwith no arguments to get an interactive prompt instead.

### What changes in practice​

You stop maintaining tooling.A singlevite-plusdependency replaces a cluster of dependencies (e.g.,vite,vitest,eslint,prettier,tsup,turbo) and their plugins and configs. Upgrades become one version bump that is tested as a unit before releasing.

You feel at home in every repo.The built-invpcommands mean the same thing everywhere, and anything a project defines itself runs throughvpr <script>. Helpful for your newly onboarded colleagues and agents.

Faster feedback.The tools underneath are written in Rust: Oxlint runs50x to 100x faster than ESLint, Oxfmtup to 30x faster than Prettier, and Vite 8 builds significantly faster thanks to Rolldown.

CI gets faster.vp runrecords which files, arguments, and environment variables a task actually used, so a cached task replays instantly if it is unchanged. Withsetup-vp, the Node setup, package manager setup, and dependency cache steps in your workflow collapse into one action.

No lock-in.Continue using your favorite Vite plugins and package manager and make use ofvp run's caching for arbitrary scripts, not only built-in commands.

## What changed since the beta​

A lot happened since we shipped thebetain July:

* setup-vpfor GitLab CI/CD, alongside the existing GitHub Action.
* More migration targets.vp migratenow handlestsupmigrations and more edge cases are resolved.
* Homebrew and a Docker imageare available.
* vp toolchainreports the exact version of every tool Vite+ provides, andvp env doctorexplains runtime and package manager resolution when it goes wrong.
* vp hookssets up, enables, and disables Git hooks, withvp stagedrunning checks on staged files only.
* Compatibility workacross the Vite plugin and framework ecosystem.

The tools Vite+ relies on were upgraded too. Vitest 5 is stable, Vite 8.1 shipped the experimental Bundled Dev Mode, and Oxc gainednative React Compiler support, which makes the compiler 10x faster than the Babel plugin it replaces.

## Who is using it​

Vite+ is closing in ontwo million weekly downloads, and more than2,600 public repositoriesdepend onvite-plustoday, not counting private projects and global installs.Tiptapreplaced its separate Vite, Vitest, tsup, and Oxc setup with Vite+, and adoption spans project types:

* Dify, an open-source platform for building LLM apps
* vinext, a Next.js-compatible framework built on Vite
* BlockNote, a Notion-style rich text editor for React
* Inkline, a component library shipping to Vue, React, Svelte, Angular, Solid, Qwik, and Astro
* npmx, an open-source npm registry browser built on Nuxt
* hono, a small, simple, and fast web framework.

## Get started​

Installvp:

macOS / Linux
Windows
sh
curl
 -fsSL
 https://vite.plus
 |
 bash
powershell
irm https:
//
vite.plus
/
ps1 
|
 iex

Open a new shell, then start a project:

bash
vp
 create

Or adopt Vite+ in a project you already have:

bash
vp
 migrate

vp migrateshows its plan before changing files, and large projects might need a follow-up. Read themigration guidefirst if the project is in production.

Working with a coding agent? Use ourmigration prompt!

## What's next​

Vite+ reached 1.0 but is far from feature-complete. Functionality such as remote caching, deeper monorepo diagnostics,vp release, andvp docsare planned for future versions.

## Acknowledgements​

Vite+ is built in the open by a growing internationalcore teamtogether with the community. Half of our core team grew out of the community itself, and Vite+ would be a smaller and slower project without the reviews, bugfixes, and features shipped by:

* kazupon
* ubugeeei
* nekomoyi
* Stefan Haas
* naokihaba
* JongKyung Lee
* Liang
* Yii

Thank you to everyone who ran the alpha and beta on real projects, filed bug reports, and sent pull requests. Vite+ exists because Vite, Vitest, Rolldown, Oxc, and tsdown exist, and because the people maintaining them keep making them better.

## Connect with us​

* Documentation:viteplus.dev
* Discord:Step into the Void
* GitHub:Star the repo, open issues, send pull requests
* X and Bluesky:@voidzerodevand@voidzero.dev
* Newsletter:Subscribe for future announcements

## Subscribe to our monthly newsletter

Subscribe