---
title: 'GitHub - kksimp/Mac.apk: Mac.apk: Run Android apps natively on Apple Silicon Macs · GitHub'
url: https://github.com/kksimp/Mac.apk
site_name: hnrss
content_file: hnrss-github-kksimpmacapk-macapk-run-android-apps-native
fetched_at: '2026-10-19T22:49:58.023333'
original_url: https://github.com/kksimp/Mac.apk
date: '2026-10-19'
description: 'Mac.apk: Run Android apps natively on Apple Silicon Macs - kksimp/Mac.apk'
tags:
- hackernews
- hnrss
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

62 Commits
62 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
debug
debug
 
 
images
images
 
 
launcher
launcher
 
 
runtime
runtime
 
 
scripts
scripts
 
 
signatures
signatures
 
 
thirdparty
thirdparty
 
 
.gitignore
.gitignore
 
 
BUILDING.md
BUILDING.md
 
 
CLA.md
CLA.md
 
 
COMMERCIAL.md
COMMERCIAL.md
 
 
COMPATIBILITY.md
COMPATIBILITY.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
THIRD_PARTY_NOTICES.txt
THIRD_PARTY_NOTICES.txt
 
 
TRADEMARKS.md
TRADEMARKS.md
 
 
VERSION
VERSION
 
 
View all files

## Repository files navigation

# Mac.apk

Run Android apps natively on Apple Silicon Macs. No emulator, no virtual machine, no Linux underneath.

 

### 📱Which apps work? See the compatibility list →

 
 
 

Alpha.Mac.apk is early software under active development. Some apps run
beautifully, some run partially, and some do not run yet. It is stable enough to use
and interesting enough to explore, and it improves with every build.

## What it is

Mac.apk runs Android apps directly on Apple Silicon. Apps launch as ordinary macOS
processes, draw through the Mac's GPU, and execute on the CPU at native speed. They
appear in your Dock, get their own windows with a back button next to the traffic
lights, resize and rotate like any Mac window, and switch between light and dark
along with your Mac.

There is no emulator here, and no virtual machine. Nothing boots Android in the
background, there is no Linux kernel running underneath, and nothing is interpreted
instruction-by-instruction. Mac.apk implements the Android application environment
on top of macOS directly.How it works →

## 📖Read the wiki →

Getting started

Installation

Installing apps

Installing apps
 · 
App stores
 · 
How apps are installed
 · 
Managing apps

Using apps

Controls and input
 · 
Windows and appearance
 · 
Files and privacy
 · 
Google accounts and Play Services

Flags and advanced settings

Flags
 · 
Flags reference
 · 
Developer menu

Help

Known issues
 · 
Troubleshooting
 · 
Reporting problems

About Mac.apk

How Mac.apk works
 · 
Design decisions
 · 
For developers and publishers

## System requirements

macOS 26.4 (Tahoe) or newer

Required. macOS 27 works from v1.0.1702

Apple Silicon

Any Apple Silicon Mac, including MacBook Neo. Intel Macs are not supported

Disk

~280 MB for Mac.apk. Each installed app takes roughly 1.5 to 3 times its APK size

## Quick start

1. Download the disk image from theReleases pageand dragMac.apkintoApplications. It is signed and notarized by Apple, so it opens
normally.
2. Open Mac.apk and clickInstallnext toRuntime:in the top left.
3. OpenSettings(the gear), findFile types, clickMake Default, and
approve the macOS prompt.
4. Double-click any.apk(or.apkm,.xapk,.apks,.apkx), or drag it onto
the Mac.apk window.

The first launch of any app is slow(up to a minute for a large one) while
Mac.apk prepares it. Later launches are fast. Full details, updating, and the app
stores are in theInstallationandApp storespages.

Warning

An Android app's saved data lives inside its own.app. Dragging the app to the
Trash deletes its saves; uninstall from the Mac.apk control panel instead.More →

## Known issues in v1.0.2237

SeeKnown issuesfor this release, and thecompatibility listfor every app tested by hand.

## Reporting problems

Send the Mac.apk version, your macOS version, the app and where you got it, what
happened, and the app's log from~/Library/Logs/macapk/toKaleb@voltare.usoropen an issue. Look the log over before posting it publicly.What to include →

## Source code

Everything that makes Mac.apk work is in this repository: the Android framework
reimplementation, the native runtime, the arm64 loader and Bionic shim, the ARM32
recompiler and the macOS app.BUILDING.mdexplains how to build it, andCONTRIBUTING.mdhow to send a fix. App reports are just as useful
as code.

## Developers and publishers

Mac.apk serves no ads and supports no in-app purchases, by design. If you publish an
app that runs on Mac.apk and want to talk about a partnership, or would rather it
not run here, emailKaleb@voltare.us.Details →

## License

Mac.apk isopen source under theGNU AGPL v3.0, and acommercial
licenseis available for companies that want to ship or offer it without the AGPL's
terms. Using the official app is free. Details:COMMERCIAL.md. The
Mac.apk name and logo are covered separately inTRADEMARKS.md.

## Disclaimer

Mac.apk is provided "as is", with no warranty of any kind. You are responsible for the
Android apps you choose to load, and Voltare cannot test, audit, or vouch for any
third-party APK. Voltare is not liable for damages, data loss, malware, security
incidents, copyright disputes, or any other consequence of code that runs through
Mac.apk.

Only install APKs you trust.An Android app running under Mac.apk runs as ordinary
native code with your macOS user account's permissions. There is no phone-style app
sandbox around it: it can read and write your files the same way any Mac app you run
can. Treat an APK exactly as you would any program you download and run yourself, and
get it from a source you trust.

## Third-party software

Mac.apk bundles several open-source components (ANGLE, MoltenVK and the Vulkan loader,
Capstone, libpng, libvpx, stb_vorbis, Bouncy Castle, a JRE built from OpenJDK together
with the libraries its font and image code uses, such as FreeType, HarfBuzz and GLib,
and the Android platform resources built from AOSP source). Each is used under its own
licence; the full notices are inTHIRD_PARTY_NOTICES.txt,
and a copy ships inside the app atContents/Resources/THIRD_PARTY_NOTICES.txt.

Two of them, GLib and GNU gettext's libintl, are licensed under the LGPL. Their
complete source for the exact versions in each release (upstream source, patches and
build recipe) is attached to that release on theReleases page, withLGPL-SOURCE-README.txtexplaining how to use a modified build.

## Links

* Project page:https://projects.voltare.us/macapk
* Wiki:https://github.com/kksimp/Mac.apk/wiki
* Commercial licensing:Kaleb@voltare.us
* Bug reports:Kaleb@voltare.usoropen an issue