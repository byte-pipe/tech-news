---
title: 'GitHub - xtool-org/xtool: Cross-platform Xcode replacement. Build and deploy iOS apps with SwiftPM on Linux, Windows, macOS. · GitHub'
url: https://github.com/xtool-org/xtool
site_name: github
content_file: github-github-xtool-orgxtool-cross-platform-xcode-replace
fetched_at: '2026-10-13T17:57:44.588339'
original_url: https://github.com/xtool-org/xtool
author: xtool-org
description: Cross-platform Xcode replacement. Build and deploy iOS apps with SwiftPM on Linux, Windows, macOS. - xtool-org/xtool
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

413 Commits
413 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
.sourcekit-lsp
.sourcekit-lsp
 
 
.vscode
.vscode
 
 
Documentation
Documentation
 
 
Examples
Examples
 
 
Linux
Linux
 
 
Sources
Sources
 
 
Tests/
XToolTests
Tests/
XToolTests
 
 
integration-tests
integration-tests
 
 
macOS
macOS
 
 
scripts
scripts
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.swiftlint.yml
.swiftlint.yml
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE.md
LICENSE.md
 
 
Makefile
Makefile
 
 
Package.resolved
Package.resolved
 
 
Package.swift
Package.swift
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
docker-compose.yml
docker-compose.yml
 
 
netlify.toml
netlify.toml
 
 
View all files

## Repository files navigation

# xtool

Cross-platform Xcode replacement. Build and deploy iOS apps with SwiftPM on Linux, Windows, and macOS.

## Overview

xtool is a cross-platform (Linux/WSL/macOS) tool that replicates Xcode functionality with open standards.

✅ Build a SwiftPM package into an iOS app

✅ Sign and install iOS apps

✅ Interact with Apple Developer Services programmatically

## Getting Started

1. Follow the guide to installxtool* Installation (Linux/Windows)
* Installation (macOS)
2. Create and run your first xtool-powered app by following thetutorial!

## Examples

### Screenshot

### Command line interface

$ xtool --help
OVERVIEW: Cross-platform Xcode replacement

USAGE: xtool 
<
subcommand
>

OPTIONS:
 -h, --help Show 
help
 information.

CONFIGURATION SUBCOMMANDS:
 setup Set up xtool 
for
 iOS development
 auth Manage Apple Developer Services authentication
 sdk Manage the Darwin Swift SDK

DEVELOPMENT SUBCOMMANDS:
 new Create a new xtool SwiftPM project
 dev Build and run an xtool SwiftPM project
 ds Interact with Apple Developer Services

DEVICE SUBCOMMANDS:
 devices List devices
 install Install an ipa file to your device
 uninstall Uninstall an installed app
 launch Launch an installed app

 See 
'
xtool help <subcommand>
'
 
for
 detailed help.

### Library

xtool includes a library that you can use to interact with Apple Developer Services, iOS devices, and more from your own app. You can use this by addingXKitas a SwiftPM dependency.

// package dependency:

.
package
(
url
:
 
"
https://github.com/xtool-org/xtool
"
,
 
.
upToNextMinor
(
from
:
 
"
1.2.0
"
)
)

// target dependency:

.
product
(
name
:
 
"
XKit
"
,
 
package
:
 
"
xtool
"
)