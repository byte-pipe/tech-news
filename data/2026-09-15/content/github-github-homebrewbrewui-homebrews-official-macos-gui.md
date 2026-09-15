---
title: 'GitHub - Homebrew/BrewUI: 📺 Homebrew''s official macOS GUI · GitHub'
url: https://github.com/Homebrew/BrewUI
site_name: github
content_file: github-github-homebrewbrewui-homebrews-official-macos-gui
fetched_at: '2026-09-15T15:27:41.026210'
original_url: https://github.com/Homebrew/BrewUI
author: Homebrew
description: 📺 Homebrew's official macOS GUI. Contribute to Homebrew/BrewUI development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 Homebrew

 

/

BrewUI

Public

* NotificationsYou must be signed in to change notification settings
* Fork23
* Star1.1k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,081 Commits
1,081 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.ai
.ai
 
 
.claude
.claude
 
 
.cursor
.cursor
 
 
.github
.github
 
 
BrewTests
BrewTests
 
 
BrewUITests
BrewUITests
 
 
Configurations
Configurations
 
 
Homebrew.xcodeproj
Homebrew.xcodeproj
 
 
Homebrew
Homebrew
 
 
HomebrewUpgradeHelper
HomebrewUpgradeHelper
 
 
Sources
Sources
 
 
Tests
Tests
 
 
Tools/
BrewUILint
Tools/
BrewUILint
 
 
docs
docs
 
 
scripts
scripts
 
 
.cursorrules
.cursorrules
 
 
.gitignore
.gitignore
 
 
.periphery.yml
.periphery.yml
 
 
.rubocop.yml
.rubocop.yml
 
 
.ruby-version
.ruby-version
 
 
.swift-version
.swift-version
 
 
.swiftformat
.swiftformat
 
 
.swiftlint.yml
.swiftlint.yml
 
 
.vale.ini
.vale.ini
 
 
AGENTS.md
AGENTS.md
 
 
ARCHITECTURE.md
ARCHITECTURE.md
 
 
Brew-E2E.xctestplan
Brew-E2E.xctestplan
 
 
Brew-UI.xctestplan
Brew-UI.xctestplan
 
 
Brew-Unit.xctestplan
Brew-Unit.xctestplan
 
 
Brewfile
Brewfile
 
 
CLAUDE.md
CLAUDE.md
 
 
CONVENTIONS.md
CONVENTIONS.md
 
 
Gemfile
Gemfile
 
 
Gemfile.lock
Gemfile.lock
 
 
LICENSE
LICENSE
 
 
Mintfile
Mintfile
 
 
Package.resolved
Package.resolved
 
 
Package.swift
Package.swift
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# 🧑‍💻 BrewUI

Homebrew's official macOS GUI: making package management approachable for users who prefer graphical interfaces over Terminal, while maintaining complete transparency about underlying Homebrew operations.

## 💡 Motivation

Enable CLI-averse users to safely discover, install, update, and manage Homebrew packages through a native SwiftUI interface that never hides what Homebrew is doing.

## 📲 Tech

* Swift 6.0with strict concurrency ·SwiftUI·Swift Package Manager
* macOS Tahoe 26+
* Data from thebrewCLI and theHomebrew JSON API

## 📦 Installation

brew install --cask homebrew-app

## Homebrew configuration

BrewUI always launches Homebrew through/bin/zsh, including app self-upgrades. It disables
optional user and system shell startup files with--no-rcs --no-global-rcsand supplies a clean environment.PATHcontains only the directory of the locatedbrewexecutable followed by/usr/bin:/bin.
Your login shell, shell aliases, exported variables and customPATHdo not configure Homebrew in BrewUI.

Put your Homebrew configuration variables inbrew.envfiles.Homebrew reads these itself:

Scope

File

User

~/.homebrew/brew.env

Installation

<Homebrew prefix>/etc/homebrew/brew.env

System

/etc/homebrew/brew.env

For example, add this line to~/.homebrew/brew.env:

HOMEBREW_NO_ENV_HINTS=1

Use literalNAME=valuelines withoutexport, shell expansion or command substitution.
User settings normally override installation settings, which override system settings.HOMEBREW_SYSTEM_ENV_TAKES_PRIORITY=1in the system file makes that file take precedence.
SeeHomebrew's environment documentation.
AnXDG_CONFIG_HOMEexported by your shell is also ignored; use the user file above.

Relaunch BrewUI after changing configuration, then check the Configuration tab. Its report and
Doctor describe Homebrew's environment in the app and may differ from Terminal. BrewUI still
sets output controls for its console and self-upgrade log.

System zsh always reads/etc/zshenv, if present; its execution cannot be disabled.
BrewUI clears the environment again afterwards and discards startup output so banners do not
reach Homebrew's reports or the console. If startup fails before Homebrew runs, its diagnostics are retained.
Seezsh's startup-file documentation.

## 🛠️ Development

After cloning:

./scripts/bootstrap

This installs Mint fromBrewfile, runsmint bootstrapto build the SwiftFormat and SwiftLint versions pinned inMintfile, enables repository git hooks, and resolves Swift package dependencies forHomebrew.xcodeproj.

After bootstrap, commits automatically run checks on staged Swift files:

1. mint run swiftformat
2. mint run swiftlint(with--fix, then strict validation)

If unresolved lint violations remain, the commit is blocked and the hook prints specific SwiftLint failures so you can fix and re-commit.

## 🚧 Status

Stable and under active development.

## 📄 Licence

AGPL-3.0. If you reuse or adapt the source the AGPL terms apply, including the network-use clause.