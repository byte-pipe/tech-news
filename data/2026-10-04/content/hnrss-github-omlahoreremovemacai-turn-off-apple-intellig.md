---
title: 'GitHub - omlahore/RemoveMacAI: Turn off Apple Intelligence on macOS 27 and get its disk space back. One command, fully reversible. · GitHub'
url: https://github.com/omlahore/RemoveMacAI
site_name: hnrss
content_file: hnrss-github-omlahoreremovemacai-turn-off-apple-intellig
fetched_at: '2026-10-04T22:12:36.921754'
original_url: https://github.com/omlahore/RemoveMacAI
date: '2026-10-04'
description: Turn off Apple Intelligence on macOS 27 and get its disk space back. One command, fully reversible. - omlahore/RemoveMacAI
tags:
- hackernews
- hnrss
---

omlahore

 

/

RemoveMacAI

Public

* NotificationsYou must be signed in to change notification settings
* Fork10
* Star340

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

10 Commits
10 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
Sources
Sources
 
 
docs
docs
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
Package.swift
Package.swift
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
THIRD-PARTY-NOTICES.md
THIRD-PARTY-NOTICES.md
 
 
install.sh
install.sh
 
 
View all files

## Repository files navigation

# RemoveMacAI

Turn off Apple Intelligence on macOS 27 and remove its downloaded models.

macOS 27 no longer has a single switch for Apple Intelligence, and its models stay on disk after the features are turned off. RemoveMacAI turns the features off, removes the models and prevents macOS from downloading them again. All changes can be reverted.

Demo video

## Install

curl -fsSL https://raw.githubusercontent.com/omlahore/RemoveMacAI/main/install.sh 
|
 bash

The script downloads the latest release, verifies its SHA-256 checksum and runs it from a temporary directory. Nothing is installed.

Every release is built from its tag by GitHub Actions and carries a build provenance attestation. To check that a download came from this repository's source:

gh attestation verify removemacai-darwin-arm64.tar.gz -R omlahore/RemoveMacAI

With Homebrew:

brew install omlahore/tap/removemacai
removemacai

RemoveMacAI shows the current state and asks for confirmation. It then opens System Settings to install its configuration profile, which macOS requires the user to approve, and removes the models.

## Usage

Command

Description

removemacai

Show the current state, then turn Apple Intelligence off

removemacai status

Show each feature and the size of the models on disk

removemacai off --keep <features>

Leave the listed features on

removemacai off --dry-run

Show the changes without applying them

removemacai revert

Undo all changes

removemacai features

List the feature names accepted by 
--keep

To revert with the one-line installer:

curl -fsSL https://raw.githubusercontent.com/omlahore/RemoveMacAI/main/install.sh 
|
 bash -s revert

## What it changes

Features turned off:Siri (including "Hey Siri" and the menu bar icon), Writing Tools, Genmoji, Image Playground, the ChatGPT extension, summaries in Mail, Messages, Safari, Notes and notifications, Mail smart replies, inline text predictions, Spatial Photos, Photos Clean Up and Xcode predictive code completion.

Models removed:the Apple Intelligence foundation models and the models for image generation and Genmoji, Spatial Photos, Photos Clean Up and Xcode code completion.

## How it works

* A configuration profile applies Apple's restriction keys for Apple Intelligence and forces the settings that have no restriction key.
* Models are removed through Apple's asset service. System Integrity Protection stays enabled and no files under/Systemare modified directly.
* The profile redirects the download of each removed model to a closed local port, so macOS does not download it again.
* Removing the profile restores the previous settings. macOS downloads the models again when a feature needs them.

RemoveMacAI makes no network requests and collects no data.

## FAQ

Does dictation still work?Yes. Dictation is a separate setting, and its speech models are not removed.

Do macOS updates undo the changes?No. The profile, including the download block, persists across updates.

Storage settings still lists Apple Intelligence after the models were deleted.Apple's asset service releases the models right away, but macOS deletes the files on its own schedule. Until then, System Settings > General > Storage keeps counting them under Apple Intelligence.

Why is a process named Siri still running?In macOS 27 the Spotlight window runs as a process named Siri. Some system services also stay loaded; they are protected by System Integrity Protection.

What stops working?The features listed above, apps that use Apple's on-device models (the Foundation Models framework and the Use Model action in Shortcuts), Visual Intelligence and natural-language editing in Calendar.

## Requirements

Apple silicon.

macOS

Status

27

Supported, tested on 27.0. On 27.0.1, use 0.2.3 or later.

26 and earlier

Not supported

## Uninstall

Runremovemacai revert, thenbrew uninstall removemacaiif it was installed with Homebrew.

## Acknowledgements

RemoveMacAI is built onpared, a complete working tool by 4evy that first mapped the asset service, the model sets and several of the settings keys. Its license is inTHIRD-PARTY-NOTICES.md.

## License

MIT