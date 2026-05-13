---
title: 'GitHub - ton-blockchain/acton: Toolchain for TON smart contract development and beyond · GitHub'
url: https://github.com/ton-blockchain/acton
site_name: github
content_file: github-github-ton-blockchainacton-toolchain-for-ton-smart
fetched_at: '2026-05-13T19:36:35.162985'
original_url: https://github.com/ton-blockchain/acton
author: ton-blockchain
description: Toolchain for TON smart contract development and beyond - ton-blockchain/acton
---

ton-blockchain

 

/

acton

Public

* NotificationsYou must be signed in to change notification settings
* Fork22
* Star165

 
 
 
 
master
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

2,219 Commits
2,219 Commits
.cargo
.cargo
 
 
.config
.config
 
 
.github
.github
 
 
assets
assets
 
 
crates
crates
 
 
docs
docs
 
 
lib
lib
 
 
src
src
 
 
tests
tests
 
 
xtask
xtask
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.mailmap
.mailmap
 
 
.npmrc
.npmrc
 
 
Acton.toml
Acton.toml
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
LICENSE-APACHE
LICENSE-APACHE
 
 
LICENSE-MIT
LICENSE-MIT
 
 
README.md
README.md
 
 
RELEASING.md
RELEASING.md
 
 
SECURITY.md
SECURITY.md
 
 
_typos.toml
_typos.toml
 
 
build.rs
build.rs
 
 
bun.lock
bun.lock
 
 
bunfig.toml
bunfig.toml
 
 
clippy.toml
clippy.toml
 
 
dist-workspace.toml
dist-workspace.toml
 
 
eslint.config.js
eslint.config.js
 
 
justfile
justfile
 
 
netlify.toml
netlify.toml
 
 
package.json
package.json
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
View all files

## Repository files navigation

# Acton

Acton is an all-in-one TON smart contract development toolkit written in Rust.
It combines project scaffolding, build, testing, scripting, wallet and network
operations, verification, linting, formatting, debugging, and low-level VM
tooling in one CLI.

Documentation:https://ton-blockchain.github.io/acton/docs/welcome

## Why Acton

* Single CLI for the full contract lifecycle: create, build, test, debug,
deploy, verify.
* Native speed (Rust-based toolchain and test runtime).
* Tolk-first workflow with built-in wrappers, testing utilities, and scripts.
* Ready for dApp development with project templates and automatically generated TypeScript wrappers.
* Fast test runner with fork mode, gas snapshots, coverage, mutation, fuzzing testing and nice UI.
* Browser test UI for failed tests, traces, logs, and coverage inspection.

## Install

The recommended way to get Acton today is to run the latest public installer:

curl -LsSf https://github.com/ton-blockchain/acton/releases/latest/download/acton-installer.sh 
|
 sh

If you prefer a manual download, use the latest public release:

Platform

Architecture

Download

macOS

ARM64

acton-aarch64-apple-darwin.tar.gz

macOS

x86_64

acton-x86_64-apple-darwin.tar.gz

Linux

x86_64

acton-x86_64-unknown-linux-gnu.tar.gz

Linux

ARM64

acton-aarch64-unknown-linux-gnu.tar.gz

After extracting the archive, make sureactonis on yourPATHand verify
the installation:

acton --version

If you prefer a containerized workflow, use the published Docker image:

docker run --rm ghcr.io/ton-blockchain/acton:
<
version
>
 --version

To run Acton against the current project from Docker:

docker run --rm \
 -v 
"
$PWD
"
:/workspace \
 -w /workspace \
 ghcr.io/ton-blockchain/acton:
<
version
>
 \
 build

For more installation details, see theinstallation guide.

## Support policy

Acton is stable on the latest numbered GitHub release. The first-class platform
matrix is macOS (ARM64, x86_64) plus Linux GNU (x86_64, ARM64). For Linux, the
documented baseline is Ubuntu 20.04 or newer. Native Windows is not supported
today. If you use Windows, run Acton inside WSL with Ubuntu 20.04 or newer and
follow the Linux installation path there.trunkbuilds installed viaacton up --trunk, WSL installs, and other source-built targets are beta /
best-effort surfaces for now. The full policy is documented atSupport policy.

## From zero to testnet

#
 Create a new project from the built-in counter template

acton new first_counter --template counter

cd
 first_counter

#
 Build and test locally

acton build
acton 
test

#
 Create and fund a local testnet wallet

acton wallet new --name deployer --local --airdrop --version v5r1

#
 Deploy to TON testnet

acton script scripts/deploy.tolk --net testnet

For a step-by-step walkthrough, see thequickstart guide.

Already have a repository instead of starting from a template? The existing
project path is:

cd
 your-repo
acton init
acton build
acton 
test

For more details, see theProject management guide.

## Building from source

Source builds are intended for contributors and local development. SeeBuilding from sourcein CONTRIBUTING.md.

## Contributing

Contributor setup, test workflows, UI build steps, and docs workflows are inCONTRIBUTING.md.

## License

Acton is licensed under either of

* Apache License, Version 2.0, (LICENSE-APACHEorhttps://www.apache.org/licenses/LICENSE-2.0)
* MIT license (LICENSE-MITorhttps://opensource.org/licenses/MIT)

at your option.

Unless you explicitly state otherwise, any contribution intentionally submitted for
inclusion in Acton by you, as defined in the Apache-2.0 license, shall be dually licensed
as above, without any additional terms or conditions.

## About

Toolchain for TON smart contract development and beyond

ton-blockchain.github.io/acton/

### Topics

 rust

 tooling

 ton

 tolk

 ton-blockchain

 mtonga

### Resources

 Readme

 

### License

 Apache-2.0, MIT licenses found
 

### Licenses found

Apache-2.0

LICENSE-APACHE

 

MIT

LICENSE-MIT

 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

165

 stars
 

### Watchers

7

 watching
 

### Forks

22

 forks
 

 Report repository

 

## Releases38

1.0.0 - 11.05.2026

 Latest

 

May 11, 2026

 

+ 37 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust88.2%
* TypeScript9.8%
* CSS1.5%
* JavaScript0.5%
* HTML0.0%
* Just0.0%