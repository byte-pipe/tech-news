---
title: 'GitHub - ntdevlabs/tiny11builder: WinUI app for building smaller, customized Windows 11 images. · GitHub'
url: https://github.com/ntdevlabs/tiny11builder
site_name: github
content_file: github-github-ntdevlabstiny11builder-winui-app-for-buildi
fetched_at: '2026-10-14T15:44:16.135822'
original_url: https://github.com/ntdevlabs/tiny11builder
author: ntdevlabs
description: WinUI app for building smaller, customized Windows 11 images. - ntdevlabs/tiny11builder
---

winui-preview
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

105 Commits
105 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
docs
docs
 
 
scripts
scripts
 
 
src
src
 
 
tests/
Tiny11Builder.Core.Tests
tests/
Tiny11Builder.Core.Tests
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
Directory.Build.props
Directory.Build.props
 
 
NOTICE.md
NOTICE.md
 
 
README.md
README.md
 
 
Tiny11Builder.sln
Tiny11Builder.sln
 
 
autounattend.xml
autounattend.xml
 
 
global.json
global.json
 
 
tiny11Coremaker.ps1
tiny11Coremaker.ps1
 
 
tiny11maker.ps1
tiny11maker.ps1
 
 
View all files

## Repository files navigation

# Tiny11 Builder

Build a smaller Windows 11 ISO with a native WinUI app. Download an official
Windows image or use your own, choose what to remove, and create your ISO.

## Download

Get the latest version

Choosex64for Intel/AMD PCs orARM64for Windows on ARM. Extract the
entire ZIP and openTiny11Builder.exe. Administrator approval is required.

## Choose your build

Mode

What it does

Tiny11

Removes bundled apps and unwanted features while keeping updates, Defender and recovery.

Tiny11 Core

Trims further by removing servicing and recovery support and disabling Defender.

Custom

Choose individual apps, components, features and services to remove or keep.

Turbo mode speeds up image processing. Interrupted builds can resume from saved
progress after the image is committed or compressed. Core and component-store
removals automatically use the legacy Windows installer.

Core cannot be updated or serviced. Protected Custom removals can break
Windows. Test your ISO in a VM before installing it.

## Video

Watch on YouTube

## Screenshots

### Welcome

### Components

### Build settings

## More information

Usage, compatibility and build instructions·Attribution and distribution notes

The original PowerShell builders remain in this repository.

## Support the project

GitHub Sponsors·Patreon·PayPal·Ko-fi