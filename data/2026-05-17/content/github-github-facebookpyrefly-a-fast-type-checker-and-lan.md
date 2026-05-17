---
title: 'GitHub - facebook/pyrefly: A fast type checker and language server for Python · GitHub'
url: https://github.com/facebook/pyrefly
site_name: github
content_file: github-github-facebookpyrefly-a-fast-type-checker-and-lan
fetched_at: '2026-05-17T19:29:28.190565'
original_url: https://github.com/facebook/pyrefly
author: facebook
description: A fast type checker and language server for Python - facebook/pyrefly
---

facebook

 

/

pyrefly

Public

* NotificationsYou must be signed in to change notification settings
* Fork358
* Star6.1k

 
 
 
 
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

13,210 Commits
13,210 Commits
.cargo
.cargo
 
 
.github
.github
 
 
.llms/
rules
.llms/
rules
 
 
.vscode
.vscode
 
 
conformance
conformance
 
 
crates
crates
 
 
lsp
lsp
 
 
pyrefly
pyrefly
 
 
pyrefly_wasm
pyrefly_wasm
 
 
release_notes
release_notes
 
 
schemas
schemas
 
 
scripts
scripts
 
 
test
test
 
 
website
website
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
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
 
 
TENSOR_SHAPES_CONTRIBUTING.md
TENSOR_SHAPES_CONTRIBUTING.md
 
 
action.yml
action.yml
 
 
debug.html
debug.html
 
 
empty.py
empty.py
 
 
package-lock.json
package-lock.json
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
test.py
test.py
 
 
version.bzl
version.bzl
 
 
yarn.lock
yarn.lock
 
 
View all files

## Repository files navigation

# Pyrefly: A fast type checker and language server for Python with powerful IDE features

Pyrefly is a type checker and language server for Python, which provides
lightning-fast type checking along with IDE features such as code navigation,
semantic highlighting, and code completion. It is available as acommand-line tooland an extension
for popular IDEs and editors such asVSCode,Neovim,Zed, andmore.

See thePyrefly websitefor full documentation and how to
add Pyrefly to your editor of choice.

Pyrefly's current development status isstable.

### Key Features

* Fast.Pyrefly checks over 1.85 million lines of code per second, type checking projects like PyTorch 15x faster than Mypy and Pyright. In the IDE, rechecks typically complete in under 10 milliseconds after saving a file.
* Production-proven at scale.Pyrefly is the default type checker for Instagram's 20-million-line Python codebase at Meta, and has been adopted by large open source projects including PyTorch and JAX.
* Full-featured language server.Code navigation, autocomplete, hover information, inlay hints, semantic highlighting, and more, with consistent results across the CLI and your editor of choice.
* Understands real-world Python.Built-in support for frameworks likePydanticandDjango, with model validation, field types, and autocomplete that work out of the box.
* Adoption-ready.Migrate from Mypy or Pyright withpyrefly init, silence existing errors withpyrefly suppress, and generate type annotations withpyrefly infer. Start with one file and expand at your own pace.

### Getting Started

* Try out pyrefly in your browser:Sandbox
* Get the command-line tool:pip install pyrefly
* Get the IDE Extension:IDE installation page

### Version Policy

Pyrefly releases new minor versions (1.x.0) monthly and patch versions in between
as-needed for critical fixes. Pyrefly doesnotfollow strict semantic versioning:
minor versions contain more significant changes than patch versions, but any
version may introduce new type errors and other breaking changes. Thepyrefly suppresscommand can be used
to easily silence errors when upgrading to a new version.

## Getting Involved

If you have questions or would like to report a bug, pleasecreate an issue.

See ourcontributing guideandarchitecture overviewfor information on how to contribute to Pyrefly.

Join ourDiscordto chat about Pyrefly
and types. This is also where we hold biweekly office hours.

## About

A fast type checker and language server for Python

pyrefly.org/

### Topics

 python

 rust

 typechecker

 types

 language-server

 ide

 typing

 code-quality

 hacktoberfest

 typecheck

 type-checker

 contributions-welcome

 lsp

 type-check

 good-first-issue

### Resources

 Readme

 

### License

 MIT license
 

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

6.1k

 stars
 

### Watchers

21

 watching
 

### Forks

358

 forks
 

 Report repository

 

## Releases53

Pyrefly v1.0.0

 Latest

 

May 12, 2026

 

+ 52 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust79.5%
* Python15.6%
* MDX2.4%
* TypeScript2.1%
* Shell0.1%
* CSS0.1%
* Other0.2%