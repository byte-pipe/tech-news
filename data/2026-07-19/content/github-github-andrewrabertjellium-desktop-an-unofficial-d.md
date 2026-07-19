---
title: 'GitHub - andrewrabert/jellium-desktop: An unofficial desktop client for Jellyfin · GitHub'
url: https://github.com/andrewrabert/jellium-desktop
site_name: github
content_file: github-github-andrewrabertjellium-desktop-an-unofficial-d
fetched_at: '2026-07-19T11:27:28.058931'
original_url: https://github.com/andrewrabert/jellium-desktop
author: andrewrabert
description: An unofficial desktop client for Jellyfin. Contribute to andrewrabert/jellium-desktop development by creating an account on GitHub.
---

andrewrabert

 

/

jellium-desktop

Public

* NotificationsYou must be signed in to change notification settings
* Fork103
* Star1.2k

 
 
 
 
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

1,074 Commits
1,074 Commits
.cargo
.cargo
 
 
.github
.github
 
 
dev
dev
 
 
resources
resources
 
 
src
src
 
 
third_party
third_party
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
justfile
justfile
 
 
renovate.json
renovate.json
 
 
View all files

## Repository files navigation

# Jellium Desktop

An unofficialJellyfindesktop client built onCEFandmpv.

## Downloads

### Linux

* AppImagex86_64aarch64
* x86_64
* aarch64
* Arch Linux (AUR):jellium-desktop-git
* Flatpak (non-Flathub bundle)

### macOS

* Apple Silicon
* Intel

After installing, remove quarantine:

sudo xattr -cr /Applications/Jellium\ Desktop.app

### Windows

* x64
* arm64

## Development

This project usesjustas a command runner.

Available recipes:
 [package]
 appimage ... # [linux] build AppImage
 flatpak ... # [linux] build Flatpak bundle
 dmg # [macos] build Apple Disk Image (.dmg)

 [maintenance]
 outdated # List outdated dependencies
 clean # Remove build artifacts

 [test]
 test # Run tests

 [lint]
 fmt # Format workspace
 fmt-check # Check formatting
 clippy # Run clippy
 lint # Lint workspace
 strict-lint # Strict lint workspace

 [build]
 build # Build the app

 [run]
 run *args # Run the app
 run-mpv *args # Run the mpv CLI

## About

An unofficial desktop client for Jellyfin

github.com/andrewrabert/jellium-desktop

### Resources

 Readme

 

### License

 GPL-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

1.2k

 stars
 

### Watchers

13

 watching
 

### Forks

103

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Rust87.8%
* JavaScript9.3%
* PowerShell1.3%
* Shell0.9%
* Just0.3%
* CSS0.2%
* Other0.2%