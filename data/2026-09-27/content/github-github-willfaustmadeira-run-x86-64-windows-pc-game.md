---
title: 'GitHub - willfaust/Madeira: Run x86-64 Windows PC games on jailed iOS via FEX-Emu + Wine + DXMT · GitHub'
url: https://github.com/willfaust/Madeira
site_name: github
content_file: github-github-willfaustmadeira-run-x86-64-windows-pc-game
fetched_at: '2026-09-27T15:32:16.727880'
original_url: https://github.com/willfaust/Madeira
author: willfaust
description: Run x86-64 Windows PC games on jailed iOS via FEX-Emu + Wine + DXMT - willfaust/Madeira
---

willfaust

 

/

Madeira

Public

* NotificationsYou must be signed in to change notification settings
* Fork152
* Star726

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

206 Commits
206 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.githooks
.githooks
 
 
FEX @ 0f8edf8
FEX @ 0f8edf8
 
 
LICENSES
LICENSES
 
 
app
app
 
 
build
build
 
 
docs
docs
 
 
patches
patches
 
 
research
research
 
 
scripts
scripts
 
 
tools
tools
 
 
wine @ 723d1bf
wine @ 723d1bf
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
ARCHITECTURE_ANALYSIS.md
ARCHITECTURE_ANALYSIS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
COPYING
COPYING
 
 
LICENSE
LICENSE
 
 
LICENSE-EXCEPTION.md
LICENSE-EXCEPTION.md
 
 
README.md
README.md
 
 
STEAM_CEF_HANDOFF.md
STEAM_CEF_HANDOFF.md
 
 
THIRD-PARTY-NOTICES.md
THIRD-PARTY-NOTICES.md
 
 
View all files

## Repository files navigation

# Madeira

Run Windows PC games on a non-jailbroken iPhone.

Madeira combinesWine(ARM64EC),FEX-Emufor x86-64 → ARM64 translation, andDXMTfor D3D11 → Metal, running as a single
Mach process on iOS with wineserver as a thread rather than a separate process.

## Status

Thumper and ULTRAKILL are playable. Marvel Cosmic Invasion has reached
gameplay, though a run has also ended in an unexplained termination and its
controls are not yet reliable. Others reach gameplay at low frame rates. This
is a research project, not a product: expect rough edges, per-title quirks and
breaking changes.

## Requirements

* A non-jailbroken iPhone. Development has been on an A15 (iPhone 13 Pro).
* JIT, which on iOS requires a debugger to attach —StikDebugis what this project uses.
* An Apple ID for signing. A free account works; its provisioning profiles
expire after 7 days, so the app must be rebuilt and reinstalled weekly. The
app's container survives reinstall, so prefixes and saves are preserved.

Because JIT requires debugger attach, this app cannot be distributed through the
App Store. It is installed by sideloading.

## Building

The build is split across several chains — the unix-side Wine libraries, the
ARM64EC PE modules, FEX, DXMT and the iOS app itself.build/*/build.shcovers
the native pieces; the app is built withxcodebuild.

git clone --recurse-submodules 
<
this repo
>

Note thatFEX,wineandresearch/dxmtare submodules pointing at forks
containing the iOS work; upstream clones will not build here.

## License

GPL-3.0-or-later— seeLICENSE. Derivatives that are
distributed must remain open source.

### Upstream licenses vs. this project's forks

Those are the licenses of theupstream projects: Wine and GnuTLS
LGPL-2.1-or-later, GMP and Nettle LGPL-3.0-or-later, FEX-Emu and DXMT MIT,
rpmalloc 0BSD. Their texts are inLICENSES/, and upstream code
remains available under themfrom upstream.

The forks used here are not licensed identically to their upstreams.Each
carries its ownLICENSE-MADEIRA.mdsaying exactly what applies:

Fork

Terms

wine

relicensed to 
GPL-3.0-or-later
 under LGPL-2.1 §3

FEX
, 
dxmt

upstream MIT preserved; modifications 
GPL-3.0-or-later

rpmalloc

upstream 0BSD preserved; Will Faust's modifications 
GPL-3.0-or-later

This is not retroactive: those forks were public beforehand, so anything
already obtained under a permissive license stays available under it.

THIRD-PARTY-NOTICES.mdhas the per-component
breakdown. Note in particular that the Microsoft Visual C++ runtime DLLs are
not distributed here and must be supplied yourself — seetools/fetch-vcruntime.md.

## A note on upstream contributions

The forks here contain substantial AI-assisted work. FEX-Emu's contribution
policy states that AI must not be used to generate code for contributions to
that project, sodo not submit AI-generated changes from this fork upstream.
The MIT license permits the fork itself; the policy governs contributions back.
Check each upstream's contribution policy before proposing changes to it.