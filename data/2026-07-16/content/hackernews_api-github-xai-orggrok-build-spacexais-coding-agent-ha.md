---
title: 'GitHub - xai-org/grok-build: SpaceXAI''s coding agent harness and TUI. Fullscreen, mouse interactive, extensible. · GitHub'
url: https://github.com/xai-org/grok-build
site_name: hackernews_api
content_file: hackernews_api-github-xai-orggrok-build-spacexais-coding-agent-ha
fetched_at: '2026-07-16T11:34:54.579866'
original_url: https://github.com/xai-org/grok-build
author: skp1995
date: '2026-07-15'
description: SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible. - xai-org/grok-build
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 xai-org

 

/

grok-build

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.4k
* Star9k

 
 
 
 
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

1 Commit
1 Commit
.cargo
.cargo
 
 
bin
bin
 
 
crates
crates
 
 
prod/
mc/
cli-chat-proxy-types
prod/
mc/
cli-chat-proxy-types
 
 
third_party
third_party
 
 
.gitignore
.gitignore
 
 
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
 
 
SECURITY.md
SECURITY.md
 
 
THIRD-PARTY-NOTICES
THIRD-PARTY-NOTICES
 
 
clippy.toml
clippy.toml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
View all files

## Repository files navigation

# Grok Build (grok)

Grok Buildis SpaceXAI's terminal-based AI coding agent. It runs as a
full-screen TUI that understands your codebase, edits files, executes shell
commands, searches the web, and manages long-running tasks — interactively,
headlessly for scripting/CI, or embedded in editors via the Agent Client
Protocol (ACP).

Installing the released binary·Building from source·Documentation·Repository layout·Development·Contributing·License

Learn more about Grok Build atx.ai/cli

This repository contains the Rust source for thegrokCLI/TUI and its agent
runtime. It is synced periodically from the SpaceXAI monorepo.

## Installing the released binary

Prebuilt binaries are published for macOS, Linux, and Windows:

curl -fsSL https://x.ai/cli/install.sh 
|
 bash 
#
 macOS / Linux / Git Bash

irm https://x.ai/cli/install.ps1 
|
 iex 
#
 Windows PowerShell

grok --version

See thechangelogfor the latest fixes,
features, and improvements in each release.

## Building from source

Requirements:

* Rust— the toolchain is pinned byrust-toolchain.toml;rustupinstalls it automatically on first build.
* protoc— proto codegen resolvesbin/protoc(adotslashlauncher) or falls back to aprotoconPATH/$PROTOC.
* macOS and Linux are supported build hosts; Windows builds are best-effort
and not currently tested from this tree.

cargo run -p xai-grok-pager-bin 
#
 build + launch the TUI

cargo build -p xai-grok-pager-bin --release 
#
 release binary: target/release/xai-grok-pager

cargo check -p xai-grok-pager-bin 
#
 fast validation

The binary artifact is namedxai-grok-pager; official installs ship it asgrok. On first launch it opens your browser to authenticate — see theauthentication guide.

## Documentation

Full online documentation is available atdocs.x.ai/build/overview.

The user guide ships with the pager crate:crates/codegen/xai-grok-pager/docs/user-guide/— getting started, keyboard shortcuts, slash commands, configuration, theming,
MCP servers, skills, plugins, hooks, headless mode, sandboxing, and more.

## Repository layout

Path

Contents

crates/codegen/xai-grok-pager-bin

Composition-root package; builds the 
xai-grok-pager
 binary

crates/codegen/xai-grok-pager

The TUI: scrollback, prompt, modals, rendering

crates/codegen/xai-grok-shell

Agent runtime + leader/stdio/headless entry points

crates/codegen/xai-grok-tools

Tool implementations (terminal, file edit, search, ...)

crates/codegen/xai-grok-workspace

Host filesystem, VCS, execution, checkpoints

crates/codegen/...

The rest of the CLI crate closure (config, MCP, markdown, sandbox, ...)

crates/common/
, 
crates/build/
, 
prod/mc/

Small shared leaf crates pulled in by the closure

third_party/

Vendored upstream source (Mermaid diagram stack) — see below

Important

The rootCargo.toml(workspace members, dependency versions, lints,
profiles) isgenerated— treat it as read-only. Prefer editing per-crateCargo.tomlfiles.

## Development

cargo check -p 
<
crate
>
 
#
 always target specific crates; full-workspace builds are slow

cargo 
test
 -p xai-grok-config 
#
 per-crate tests

cargo clippy -p 
<
crate
>
 
#
 lint config: clippy.toml at the repo root

cargo fmt --all 
#
 rustfmt.toml at the repo root

## Contributing

Note

External contributions are not accepted. SeeCONTRIBUTING.md.

## License

First-party code in this repository is licensed under theApache License,
Version 2.0— seeLICENSE.

Third-party and vendored code remains under its original licenses. See:

* THIRD-PARTY-NOTICES— crates.io / git dependencies,
bundled UI themes, andin-tree source ports(including openai/codex and
sst/opencode tool implementations)
* crates/codegen/xai-grok-tools/THIRD_PARTY_NOTICES.md— crate-local notice for the codex and opencode ports (license texts +
Apache §4(b) change notice)
* third_party/NOTICE— vendored Mermaid-stack index

## About

SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible.

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

9k

 stars
 

### Watchers

59

 watching
 

### Forks

1.4k

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust99.6%
* Other0.4%