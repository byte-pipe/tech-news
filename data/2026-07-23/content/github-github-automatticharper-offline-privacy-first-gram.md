---
title: 'GitHub - Automattic/harper: Offline, privacy-first grammar checker. Fast, open-source, Rust-powered · GitHub'
url: https://github.com/Automattic/harper
site_name: github
content_file: github-github-automatticharper-offline-privacy-first-gram
fetched_at: '2026-07-23T11:39:13.219643'
original_url: https://github.com/Automattic/harper
author: Automattic
description: Offline, privacy-first grammar checker. Fast, open-source, Rust-powered - Automattic/harper
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 Automattic

 

/

harper

Public

* NotificationsYou must be signed in to change notification settings
* Fork438
* Star11.8k

 
 
 
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

4,459 Commits
4,459 Commits
.buildkite
.buildkite
 
 
.bundle
.bundle
 
 
.github
.github
 
 
.vscode
.vscode
 
 
fastlane
fastlane
 
 
fuzz
fuzz
 
 
harper-asciidoc
harper-asciidoc
 
 
harper-brill
harper-brill
 
 
harper-cli
harper-cli
 
 
harper-comments
harper-comments
 
 
harper-core
harper-core
 
 
harper-desktop
harper-desktop
 
 
harper-dictionary-wordlist
harper-dictionary-wordlist
 
 
harper-git-commit
harper-git-commit
 
 
harper-html
harper-html
 
 
harper-ink
harper-ink
 
 
harper-jjdescription
harper-jjdescription
 
 
harper-literate-haskell
harper-literate-haskell
 
 
harper-ls
harper-ls
 
 
harper-pos-utils
harper-pos-utils
 
 
harper-python
harper-python
 
 
harper-stats
harper-stats
 
 
harper-tex
harper-tex
 
 
harper-thesaurus
harper-thesaurus
 
 
harper-tree-sitter
harper-tree-sitter
 
 
harper-typst
harper-typst
 
 
harper-wasm
harper-wasm
 
 
packages
packages
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.envrc
.envrc
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.node-version
.node-version
 
 
.npmrc
.npmrc
 
 
.nvmrc
.nvmrc
 
 
.ruby-version
.ruby-version
 
 
.xcode-version
.xcode-version
 
 
AGENTS.md
AGENTS.md
 
 
AGENT_POLICY.md
AGENT_POLICY.md
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
COMPARISON.md
COMPARISON.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Cargo.lock
Cargo.lock
 
 
Cargo.toml
Cargo.toml
 
 
Dockerfile
Dockerfile
 
 
Gemfile
Gemfile
 
 
Gemfile.lock
Gemfile.lock
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
demo.md
demo.md
 
 
docker-compose.dev.yml
docker-compose.dev.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
justfile
justfile
 
 
logo.svg
logo.svg
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
pnpm-workspace.yaml
pnpm-workspace.yaml
 
 
rust-toolchain.toml
rust-toolchain.toml
 
 
rustfmt.toml
rustfmt.toml
 
 
View all files

## Repository files navigation

# Harper

Harper is an English grammar checker designed to bejust right.I created it after years of dealing with the shortcomings of the competition.

Grammarly was too expensive and too overbearing.
Its suggestions lacked context, and were often just plainwrong.
Not to mention: it's a privacy nightmare.
Everything you write with Grammarly is sent to their servers.
Their privacy policy claims they don't sell the data, but that doesn't mean they don't use it to train large language models and god knows what else.
Not only that, but the round-trip-time of the network request makes revising your work all the more tedious.

LanguageTool is great, if you have gigabytes of RAM to spare and are willing to download the ~16GB n-gram dataset.
Besides the memory requirements, I found LanguageTool too slow: it would take several seconds to lint even a moderate-size document.

That's why I created Harper: it is the grammar checker that fits my needs.
Not only does it take milliseconds to lint a document, take less than 1/50th of LanguageTool's memory footprint,
but it is also completely private.

Harper is even small enough to load viaWebAssembly.

## Language Support

Harper currently only supports English, but the core is extensible to support other languages, so we welcome contributions that allow for other language support.

## Performance Issues

We consider long lint times bugs.
If you encounter any significant performance issues, please create an issue on the topic.

If you find a fix to any performance issue, we would appreciate the contribution.
Just please make sure to readour contribution guidelines first.

## Links

* Frequently Asked Questions
* Obsidian Documentation
* harper-lsDocumentation
* Supported Editors' DocumentationVisual Studio CodeNeovimHelixEmacsZed
* Visual Studio Code
* Neovim
* Helix
* Emacs
* Zed
* harper.jsDocumentation
* Official Discord Server

## Huge Thanks

This project would not be possible without the hard work from those whocontribute.

Harper's logo was designed byLukas Werner.

## About

Offline, privacy-first grammar checker. Fast, open-source, Rust-powered

writewithharper.com

### Topics

 react

 nodejs

 chrome-extension

 rust

 webassembly

 svelte

 developer-tools

 grammar-checker

 english-language

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

11.8k

 stars
 

### Watchers

28

 watching
 

### Forks

438

 forks
 

 Report repository

 

## Releases110

v2.6.0

 Latest

 

Jun 24, 2026

 

+ 109 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust50.9%
* HTML35.4%
* TypeScript7.2%
* Svelte4.6%
* JavaScript0.6%
* Just0.4%
* Other0.9%