---
title: 'GitHub - nubjs/nub: The fast all-in-one Node.js toolkit · GitHub'
url: https://github.com/nubjs/nub
site_name: hnrss
content_file: hnrss-github-nubjsnub-the-fast-all-in-one-nodejs-toolkit
fetched_at: '2026-06-24T19:35:58.505301'
original_url: https://github.com/nubjs/nub
date: '2026-06-24'
description: The fast all-in-one Node.js toolkit. Contribute to nubjs/nub development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

nubjs

 

/

nub

Public

* NotificationsYou must be signed in to change notification settings
* Fork21
* Star1.7k

 
 
 
 
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

936 Commits
936 Commits
.agents/
skills/
agent-browser
.agents/
skills/
agent-browser
 
 
.claude
.claude
 
 
.githooks
.githooks
 
 
.github
.github
 
 
benches
benches
 
 
benchmarks
benchmarks
 
 
crates
crates
 
 
docker
docker
 
 
npm
npm
 
 
runtime
runtime
 
 
scripts
scripts
 
 
setup
setup
 
 
site
site
 
 
skills/
nub
skills/
nub
 
 
stats/
download-counts
stats/
download-counts
 
 
tests
tests
 
 
vendor/
aube
vendor/
aube
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
.vercelignore
.vercelignore
 
 
.worktreeinclude
.worktreeinclude
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Cross.toml
Cross.toml
 
 
L1_AGENTS.md
L1_AGENTS.md
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
PROSE.md
PROSE.md
 
 
README.md
README.md
 
 
bun.lock
bun.lock
 
 
install.ps1
install.ps1
 
 
install.sh
install.sh
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
skills-lock.json
skills-lock.json
 
 
View all files

## Repository files navigation

# Nub

A fast all-in-one toolkit that augments Node.js instead of replacing it

Docs

  •  

GitHub

  •  

𝕏

A Bun-like DX on top of stocknode, written in Rust.

nub index.ts 
#
 TypeScript-first Node.js runtime

nub run dev 
#
 24× faster pnpm run

nubx prisma generate 
#
 19× faster npx

nub install 
#
 2.5× faster pnpm install

nub watch src/server.ts 
#
 native watch mode

nub pm shim 
#
 built-in Corepack-style shims

nub node install 26 
#
 Node version manager

nub upgrade 
#
 self update

One tool to run your files and scripts, install dependencies, and manage Node itself. No new runtime, no vendor-specific API surface, no lock-in.

Nub

Instead of

nub <file>

node
, 
tsx
, 
ts-node
, 
dotenv-cli

nub run <script>

npm run
, 
pnpm run

nubx

npx
, 
pnpm dlx / exec

nub install

npm
, 
pnpm

nub watch

nodemon
, 
node --watch
, 
tsx watch

nub node

nvm
, 
fnm
, 
n
, 
volta

nub pm

corepack

## Install

#
 macOS / Linux

curl -fsSL https://nubjs.com/install.sh 
|
 bash

#
 Windows (PowerShell)

irm https://nubjs.com/install.ps1 
|
 iex

#
 Or via npm (pnpm / yarn global add work too)

npm install -g --ignore-scripts=false @nubjs/nub

For GitHub Actions, usenubjs/setup-nubin place ofactions/setup-node. It's one-to-one compatible.

-
 - uses: actions/setup-node@v4

+
 - uses: nubjs/setup-nub@v0

## File runner —nub <file>

Run a file. Supports.js,.ts,.mjs,.cjs,.mts,.cts,.jsx, and.tsx. Flag-for-flag and var-for-var drop-in compatible withnode(mostly via passthrough).

nub index.ts 
#
 TypeScript, JSX, no build step

nub --watch app.ts 
#
 same path, restart-on-change

It augments stock Node with some of Bun/Deno's best features:

* 🦆 Full TypeScript support, includingenum,namespace
* 🧭 TypeScript-friendly resolution: extensionless imports,tsconfig.json#paths
* ⚛️ JSX / TSX
* 🎂 Decorators andemitDecoratorMetadata
* 🆕 Modern syntax likeusing(downleveled in transpiler when needed)
* 🔐 Automatic.env*loading — Next.js/Vite parity
* 🗂️ Built-in loaders for common data formats —.yaml,.toml,.jsonc,.json5,.txt
* 🌐 Polyfills forTemporal,Worker,URLPattern(when needed)
* 🔥 Unflags experimental features likenode:sqlite,vm.Module,localStorage,WebSocket,EventSource
* ⚡ 2.9× faster startup thantsx

How it works— Nub takes advantage of Node extension surfaces that mostly didn't exist when Deno and Bun were built:

* --import/--requirepreloads
* module.registerHooks()for transpilation and resolution
* N-API native addons: Nub embedsoxcfor pre-transpilation

### Node provisioning

When you run a file with nub, it infers the version of Node your project expects and auto-installs it if needed. It respects (in precedence order):

* NODE_EXECUTABLE(override)
* package.json#devEngines
* .node-version
* .nvmrc
* package.json#engines

This resolved version of Node is installed and your file is executed with it (with Nub's augmentations).

$ 
echo
 26 
>
 .node-version
$ nub hello.ts
Using Node.js 26.3.0 (resolved from .node-version)
Installed 
in
 9.8s
Hello world
!

### Modern APIs

Modern API work out of the box under Nub. Node.js experimental APIs are unflagged, others are auto-polyfilled (e.g.Temporalon Node 25 and earlier), and others are downleveled in the transpiler (using).

API

How

Temporal

polyfilled below Node 26, native above

URLPattern

polyfilled below Node 24, native above

RegExp.escape

polyfilled below Node 24, native above

Error.isError

polyfilled below Node 24, native above

Promise.try

polyfilled below Node 24, native above

Float16Array

polyfilled below Node 24, native above

navigator.locks

polyfilled below Node 24.5, native above

reportError

polyfilled

vm.Module

unflagged

ShadowRealm

unflagged

Wasm module imports

unflagged below Node 24.5 (22.19 on the 22.x line), native above

WebSocket

unflagged from Node 20.10, native from Node 22

EventSource

unflagged from Node 20.18, native above

node:sqlite

unflagged from Node 22.5, native from Node 22.13

addon imports

unflagged from Node 22.20, never native

### Watch mode

Restart-on-change driven by the resolved dependency graph plus the off-graph files that still invalidate a run — no glob list to maintain:

nub watch src/server.ts
nub --watch src/server.ts 
#
 same path

* 👀 Tracks the resolved dependency graph automatically
* 🧷 Also watches the off-graph invalidators —.env*, thetsconfig.jsonextends chain,package.json
* ⚙️ Runs on Node's own--watchengine, preserving output by default

View thefull runtime docs 👉.

## Script runner —nub run

A drop-in fornpm runandpnpm run. The runner is a Rust binary with no JavaScript startup of its own, so it dispatches a warm script roughly 24× faster thanpnpm run:

nub run build
nub run -r --filter 
"
@org/*
"
 
test
 
#
 supports --filter

It's fast compared to existing JavaScript-based script runners.

Command

Time

Relative

nub run

14.7 ms

—

npm run

329.9 ms

22×

pnpm run

442.7 ms

30×

script dispatch · warm · 50 runs · macOS —view benchmark

* 🚀 Feels instantaneous — 14ms vs a detectable 300ms+ lag for npm/pnpm
* 🔁 Full lifecycle support —pre/posthooks and the completenpm_*environment
* 🧰 Localnode_modules/.binonPATH, with args forwarded without the--separator
* 🗃️ The full pnpm workspace surface —-r,--filter,--parallel,--workspace-concurrency,--resume-from,--stream
* 🎯 pnpm's--filtergrammar verbatim — graph (...@org/web) and changed-since ([main]) selectors

View thefull script runner docs 👉.

## Package runner —nubx/nub dlx

A drop-in fornpxandpnpm dlx. Local-first with a download-and-execute registry fallback (same asnpx). Eliminating the double-Node.js-spawn performance penalty paid by JavaScript-based tools likenpxandpnpm.

nubx eslint 
.
 --fix
nubx -y cowsay@1.5.0 
"
hi
"
 
#
 fetched from the registry (auto-approved via -y)

Command

Time

Relative

nubx esbuild --version

11 ms

—

pnpm exec esbuild --version

191 ms

17×

npx esbuild --version

226 ms

19×

esbuild --version · macOS —view benchmark

* ⚡ Runs a local bin ~19× faster thannpx, with no Node in the wrapper
* 🔎 Resolvesnode_modules/.binregardless of which package manager installed it
* 🌐 Registry fallback for uninstalled bins — fetched, run, then discarded
* 🧩 Fullpnpm exec/pnpm dlxflag parity, shell mode included
* 🪜 Walks the resolution chain — member.bin, then workspace root, then ancestors

View thefull package runner docs 👉.

## Package manager —nub install

Nub is a package manager powered by theAubeengine. The CLI is flag-for-flag compatible withpnpmfor muscle memory, but

nub install 
nub ci
nub add -E -D --save-catalog react
nub remove lodash
nub update
nub dedupe

It's fast — avoids the per-command Node.js bootstrap lag incurred by JS-based package managers.

Tool

Time

Relative

nub

1122 ms

—

bun

1444 ms

29% slower

pnpm

2847 ms

2.5×

npm

4163 ms

3.7×

warm frozen install · create-t3-app · 222 deps · macOS —view benchmark

### Security

* 🛡️ Blocks postinstall by default
* 🦠 Checksosv.devfor known-malicious package versions during resolution by default
* 🔻 Refuses provenance downgrades by default
* ⏳ 24-hourminimumReleaseAgeby default

### Compatibility

When you runnub installinside a project, it detects theincumbentpackage manager (based on yourpackage.json#packageManageror any detected lockfiles). It then runs incompat-mode, respecting the config files and environment variables for that package manager.

Under each incumbent, Nub reads that tool's branded config and no other's; the neutral.npmrccascade andnpm_config_*are read under every one.

Incumbent

Config it reads

npm

package-lock.json
, 
.npmrc
, 
overrides
, 
workspaces
, 
engines
/
os
/
cpu
/
libc

pnpm

pnpm-lock.yaml
, 
pnpm-workspace.yaml
, 
.pnpmfile.cjs
, 
package.json#pnpm
, 
resolutions
, 
catalog:
, 
.npmrc

Yarn
 (read-only)

yarn.lock
, a 
.yarnrc.yml
 / 
.yarnrc
 subset, 
YARN_*
, 
resolutions
, 
packageExtensions
, 
.npmrc

Bun

bun.lock
, 
bunfig.toml
 
[install]
, 
trustedDependencies
, 
overrides
, 
patchedDependencies
, 
catalog:
, 
.npmrc

Nub

neutral only — 
.npmrc
, 
npm_config_*
, 
overrides
 / 
resolutions
 / 
catalog
 / 
workspaces

View thefull package manager docs 👉.

## Package meta-manager —nub pm

Corepack's job, in native Rust: provision and run the exact pnpm / npm / yarn your project pins:

nub pm shim 
#
 registers global shims (Corepack-style)

Likecorepack enable, this registers global shims fornpm,yarn, andpnpm. When you run a command using one of these shim aliases anywhere on your file system, the shim will:

* Detect the version used in your project
* Install that version if needed
* Run the command using the proper version

Nub provides this functionality as a convenience for users who prefer to keep their current package manager. Corepack itself wasunbundled from Node itselfin v25.

View thefullnub pmdocs 👉.

## Node version manager —nub node

Though Node.js versions will generally be auto-installed and cached as needed, you can manage versions manually as well.

$ nub node -h 
nub node — manage Node versions

Usage: nub node 
<
command
>

Commands:
 which print the resolved Node binary path (why → stderr)
 install [
<
version
>
...] provision version(s) into nub
'
s cache

 ls list versions in nub
'
s cache
 uninstall 
<
version
>
 remove a version from nub
'
s cache

 pin <version> write the project
'
s Node pin

View thefullnub nodedocs 👉.

## License

MIT

## About

The fast all-in-one Node.js toolkit

nubjs.com

### Topics

 nodejs

 package-manager

 script-runner

 javascript-runtime

 node-version-manager

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.7k

 stars
 

### Watchers

1

 watching
 

### Forks

21

 forks
 

 Report repository

 

## Releases51

v0.1.14

 Latest

 

Jun 24, 2026

 

+ 50 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust64.8%
* JavaScript10.8%
* Shell9.5%
* MDX7.0%
* TypeScript5.5%
* PowerShell1.0%
* Other1.4%