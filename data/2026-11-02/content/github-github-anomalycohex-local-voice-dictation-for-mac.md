---
title: 'GitHub - anomalyco/hex: Local voice dictation for mac, windows and linux · GitHub'
url: https://github.com/anomalyco/hex
site_name: github
content_file: github-github-anomalycohex-local-voice-dictation-for-mac
fetched_at: '2026-11-02T08:48:22.129051'
original_url: https://github.com/anomalyco/hex
author: anomalyco
description: Local voice dictation for mac, windows and linux. Contribute to anomalyco/hex development by creating an account on GitHub.
---

dev
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,284 Commits
1,284 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.cargo
.cargo
 
 
.cloudflare/
cache
.cloudflare/
cache
 
 
.config
.config
 
 
.github
.github
 
 
app
app
 
 
assets/
icons
assets/
icons
 
 
crates
crates
 
 
design
design
 
 
docs
docs
 
 
ios
ios
 
 
macos/
HexMicrophoneDriver
macos/
HexMicrophoneDriver
 
 
native
native
 
 
nix
nix
 
 
packaging
packaging
 
 
prototypes/
app-shell
prototypes/
app-shell
 
 
release-notes
release-notes
 
 
resources
resources
 
 
scripts
scripts
 
 
sdk
sdk
 
 
site
site
 
 
skills/
hex-personal-commands
skills/
hex-personal-commands
 
 
src
src
 
 
tests
tests
 
 
.gitignore
.gitignore
 
 
.hivemind.toml
.hivemind.toml
 
 
.markdownlint-cli2.jsonc
.markdownlint-cli2.jsonc
 
 
AGENTS.md
AGENTS.md
 
 
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
 
 
ROADMAP.md
ROADMAP.md
 
 
SECURITY.md
SECURITY.md
 
 
THIRD_PARTY_NOTICES.md
THIRD_PARTY_NOTICES.md
 
 
build.rs
build.rs
 
 
clippy.toml
clippy.toml
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
View all files

## Repository files navigation

# Hex

Hex is local voice dictation for Mac, Windows and Linux. Hold a key, speak, and
it pastes.

## How it works

* hold the shortcut, speak, then let go
* Hex transcribes on your device and pastes into whatever app you're in
* the first run downloads a speech model; after that nothing leaves your machine
* experimental features live in Labs, at the bottom of the sidebar

## Downloads

Stable is the current release. Dev is the newest build ofdevand updates
itself from the dev channel.

Platform

Stable

Dev

macOS (Apple silicon)

DMG

DMG

Windows x64

Installer

Installer

Windows ARM64

Installer

Installer

Linux x86_64

Executable

Executable

Linux x86_64 (Debian, Ubuntu)

.deb

.deb

Linux x86_64 (Fedora, openSUSE)

.rpm

.rpm

Linux ARM64

Executable

Executable

Linux ARM64 (Debian, Ubuntu)

.deb

.deb

Linux ARM64 (Fedora, openSUSE)

.rpm

.rpm

Or install with:

* Homebrew:brew install --cask anomalyco/tap/hex
* AUR:yay -S hex-bin
* install script (Linux):curl -fsSL https://anoma.ly/hex/install-linux.sh | sh
* Nix:nix profile install github:anomalyco/hex

More docs are indocs/.

## Contributing

We don't take pull requests.Open an issuedescribing the bug or idea, and our agents usually turn it around fast.

MIT licensed.