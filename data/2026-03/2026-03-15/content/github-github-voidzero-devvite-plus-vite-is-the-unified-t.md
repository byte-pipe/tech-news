---
title: 'GitHub - voidzero-dev/vite-plus: Vite+ is the unified toolchain and entry point for web development. It manages your runtime, package manager, and frontend toolchain in one place. · GitHub'
url: https://github.com/voidzero-dev/vite-plus
site_name: github
content_file: github-github-voidzero-devvite-plus-vite-is-the-unified-t
fetched_at: '2026-03-15T11:10:17.471923'
original_url: https://github.com/voidzero-dev/vite-plus
author: voidzero-dev
description: Vite+ is the unified toolchain and entry point for web development. It manages your runtime, package manager, and frontend toolchain in one place. - voidzero-dev/vite-plus
---

voidzero-dev



/

vite-plus

Public

* NotificationsYou must be signed in to change notification settings
* Fork43
* Star1.4k




 
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

616 Commits
616 Commits
.cargo
.cargo
 
 
.claude
.claude
 
 
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
bench
bench
 
 
crates
crates
 
 
docs
docs
 
 
ecosystem-ci
ecosystem-ci
 
 
packages
packages
 
 
rfcs
rfcs
 
 
scripts
scripts
 
 
tmp
tmp
 
 
.clippy.toml
.clippy.toml
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.node-version
.node-version
 
 
.rustfmt.toml
.rustfmt.toml
 
 
.typos.toml
.typos.toml
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
deny.toml
deny.toml
 
 
justfile
justfile
 
 
logo-dark.svg
logo-dark.svg
 
 
logo.svg
logo.svg
 
 
netlify.toml
netlify.toml
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
tsconfig.json
tsconfig.json
 
 
vite.config.ts
vite.config.ts
 
 
View all files

## Repository files navigation

The Unified Toolchain for the Webruntime and package management, create, dev, check, test, build, pack, and monorepo task caching in a single dependency

Vite+ is the unified entry point for local web development. It combinesVite,Vitest,Oxlint,Oxfmt,Rolldown,tsdown, andVite Taskinto one zero-config toolchain that also manages runtime and package manager workflows:

* vp env:Manage Node.js globally and per project
* vp install:Install dependencies with automatic package manager detection
* vp dev:Run Vite's fast native ESM dev server with instant HMR
* vp check:Run formatting, linting, and type checks in one command
* vp test:Run tests through bundled Vitest
* vp build:Build applications for production with Vite + Rolldown
* vp run:Execute monorepo tasks with caching and dependency-aware scheduling
* vp pack:Build libraries for npm publishing or standalone app binaries
* vp create/vp migrate:Scaffold new projects and migrate existing ones

All of this is configured from your project root and works across Vite's framework ecosystem.
Vite+ is fully open-source under the MIT license.

## Getting Started

Install Vite+ globally asvp:

For Linux or macOS:

curl -fsSL https://vite.plus
|
 bash

For Windows:

irm https://viteplus.dev/install.ps1
|
 iex

vphandles the full development lifecycle such as package management, development servers, linting, formatting, testing and building for production.

## Configuring Vite+

Vite+ can be configured using a singlevite.config.tsat the root of your project:

import

{

defineConfig

}

from

'vite-plus'
;

export

default

defineConfig
(
{


// Standard Vite configuration for dev/build/preview.


plugins
:
[
]
,


// Vitest configuration.


test
:
{


include
:
[
'src/**/*.test.ts'
]
,


}
,


// Oxlint configuration.


lint
:
{


ignorePatterns
:
[
'dist/**'
]
,


}
,


// Oxfmt configuration.


fmt
:
{


semi
:
true
,


singleQuote
:
true
,


}
,


// Vite Task configuration.


run
:
{


tasks
:
{


'generate:icons'
:
{


command
:
'node scripts/generate-icons.js'
,


envs
:
[
'ICON_THEME'
]
,


}
,


}
,


}
,


// `vp staged` configuration.


staged
:
{


'*'
:
'vp check --fix'
,


}
,

}
)
;

This lets you keep the configuration for your development server, build, test, lint, format, task runner, and staged-file workflow in one place with type-safe config and shared defaults.

Usevp migrateto migrate to Vite+. It merges tool-specific config files such as.oxlintrc*,.oxfmtrc*, and lint-staged config intovite.config.ts.

### CLI Workflows (vp help)

#### Start

* create- Create a new project from a template
* migrate- Migrate an existing project to Vite+
* config- Configure hooks and agent integration
* staged- Run linters on staged files
* install(i) - Install dependencies
* env- Manage Node.js versions

#### Develop

* dev- Run the development server
* check- Run format, lint, and type checks
* lint- Lint code
* fmt- Format code
* test- Run tests

#### Execute

* run- Run monorepo tasks
* exec- Execute a command from localnode_modules/.bin
* dlx- Execute a package binary without installing it as a dependency
* cache- Manage the task cache

#### Build

* build- Build for production
* pack- Build libraries
* preview- Preview production build

#### Manage Dependencies

Vite+ automatically wraps your package manager (pnpm, npm, or Yarn) based onpackageManagerand lockfiles:

* add- Add packages to dependencies
* remove(rm,un,uninstall) - Remove packages from dependencies
* update(up) - Update packages to latest versions
* dedupe- Deduplicate dependencies
* outdated- Check outdated packages
* list(ls) - List installed packages
* why(explain) - Show why a package is installed
* info(view,show) - View package metadata from the registry
* link(ln) /unlink- Manage local package links
* pm- Forward a command to the package manager

#### Maintain

* upgrade- Updatevpitself to the latest version
* implode- Removevpand all related data

### Scaffolding your first Vite+ project

Usevp createto create a new project:

vp create

You can runvp createinside of a project to add new apps or libraries to your project.

### Migrating an existing project

You can migrate an existing project to Vite+:

vp migrate

### GitHub Actions

Use the officialsetup-vpaction to install Vite+ in GitHub Actions:

-
uses
:
voidzero-dev/setup-vp@v1


with
:

node-version
:
'
22
'


cache
:
true

#### Manual Installation & Migration

If you are manually migrating a project to Vite+, install these dev dependencies first:

npm install -D vite-plus @voidzero-dev/vite-plus-core@latest

You need to add overrides to your package manager forviteandvitestso that other packages depending on Vite and Vitest will use the Vite+ versions:

"overrides"
: {

"vite"
:
"
npm:@voidzero-dev/vite-plus-core@latest
"
,

"vitest"
:
"
npm:@voidzero-dev/vite-plus-test@latest
"

}

If you are usingpnpm, add this to yourpnpm-workspace.yaml:

overrides
:

vite
:
npm:@voidzero-dev/vite-plus-core@latest


vitest
:
npm:@voidzero-dev/vite-plus-test@latest

Or, if you are using Yarn:

"resolutions"
: {

"vite"
:
"
npm:@voidzero-dev/vite-plus-core@latest
"
,

"vitest"
:
"
npm:@voidzero-dev/vite-plus-test@latest
"

}

## About

Vite+ is the unified toolchain and entry point for web development. It manages your runtime, package manager, and frontend toolchain in one place.

viteplus.dev

### Resources

 Readme



### License

 MIT license


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

1.4k

 stars


### Watchers

10

 watching


### Forks

43

 forks


 Report repository



## Releases62

vite-plus v0.1.11

 Latest



Mar 13, 2026



+ 61 releases

## Contributors20

+ 6 contributors

## Languages

* Rust62.8%
* TypeScript33.5%
* JavaScript1.9%
* Shell1.0%
* PowerShell0.7%
* Just0.1%
