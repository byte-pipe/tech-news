---
title: 'GitHub - kageroumado/phosphene: A video wallpaper engine for macOS Tahoe · GitHub'
url: https://github.com/kageroumado/phosphene
site_name: hackernews_api
content_file: hackernews_api-github-kageroumadophosphene-a-video-wallpaper-engi
fetched_at: '2026-05-22T06:00:21.978749'
original_url: https://github.com/kageroumado/phosphene
author: kageroumado
date: '2026-05-21'
description: A video wallpaper engine for macOS Tahoe. Contribute to kageroumado/phosphene development by creating an account on GitHub.
tags:
- hackernews
- trending
---

kageroumado

 

/

phosphene

Public

* NotificationsYou must be signed in to change notification settings
* Fork13
* Star528

 
 
 
 
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

2 Commits
2 Commits
Phosphene.xcodeproj
Phosphene.xcodeproj
 
 
Phosphene
Phosphene
 
 
PhospheneExtension
PhospheneExtension
 
 
.gitignore
.gitignore
 
 
.swift-version
.swift-version
 
 
.swiftformat
.swiftformat
 
 
.swiftlint.yml
.swiftlint.yml
 
 
Info.plist
Info.plist
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Phosphene

A video wallpaper engine for macOS Tahoe.

Phosphene is a menu bar app + wallpaper extension that plays your own video files as the macOS desktop and lock-screen wallpaper. It plugs into the system's native wallpaper picker, so videos appear alongside Apple's built-in Aerials inSystem Settings → Wallpaper.

It is built on top of Apple's privateWallpaperExtensionKitframework — the same one Apple's own Aerials use — which means playback runs out-of-process, survives app quits, and integrates with the OS-level lock-screen / idle / sleep lifecycle.

⚠️Private framework.Phosphene loadsWallpaperExtensionKitviadlopenand uses Mirror-based runtime introspection to talk to its XPC types. Apple could change this at any major OS release. The project tracks macOS 26 (Tahoe).

## Features

* Bring your own videos.Import MP4 / MOV / any AVFoundation-readable file. They show up in the system wallpaper picker.
* Gapless looping.Frame-accurate loops by offsetting PTS/DTS across loop boundaries — no flush, no stutter.
* Multi-display + per-Space selections.Different wallpapers per display, persisted by macOS.
* Power-aware playback.A graduatedPlaybackPolicyreduces work or pauses entirely based on thermal state, battery level, on-battery vs AC, Game Mode, and presentation mode (active / locked / idle).
* Smooth lock-screen ramp.WhenOnly on Lock Screenis enabled, the wallpaper eases in/out with a cubic curve as you lock and unlock, matching Apple's own Aerials behavior.
* Pause when occluded.Detects when every display is fully covered by windows and pauses rendering until the desktop is visible again.
* Adaptive variants.Optionally pre-render lower-resolution / lower-fps variants of a video; the renderer swaps to the cheapest variant that satisfies the current policy at each loop boundary.
* Menu bar control.Preview the current wallpaper, toggle pause, switch displays, configure behavior, launch at login.

## Requirements

* macOS Tahoe (26.0+).Phosphene depends on the Wallpaper extension point introduced in macOS 14 but uses Tahoe-only SwiftUI andglassEffect()APIs.
* Apple Silicon.Targetsarm64-apple-macos26.0.
* Xcode 17+to build, with Swift 6 strict concurrency enabled.

## Building

git clone https://github.com/
<
you
>
/phosphene

cd
 phosphene
open Phosphene.xcodeproj

In Xcode, select thePhosphenescheme and Run. The project uses synchronized filesystem groups, so adding/removing files inPhosphene/orPhospheneExtension/requires no pbxproj edits.

You'll need to set a development team for code signing. The wallpaper extension is embedded into the app bundle and registered with the system when the app launches.

### Using a video wallpaper

1. Launch Phosphene. Use the menu bar icon toManage Libraryand add one or more videos.
2. OpenSystem Settings → Wallpaper. Phosphene's videos appear under their own collection.
3. Pick a video. macOS handles the actual wallpaper assignment — Phosphene's extension provides the frames.

## Architecture

┌─────────────────────────┐ ┌──────────────────────────────┐
│ Phosphene.app │ │ PhospheneExtension.appex │
│ (menu bar UI) │ │ (host: WallpaperAgent) │
│ │ │ │
│ • Library management │ Darwin │ • XPC handler │
│ • Per-video metadata │ ──────▶ │ • AVSampleBufferDisplayLayer │
│ • Optimization (HEVC) │ notif. │ • Power / thermal monitor │
│ • Preferences │ │ • Snapshot generator │
└─────────────────────────┘ └──────────────────────────────┘
 │ │
 └──────────────┬───────────────┘
 ▼
 Shared App Group container
 (~/Library/Group Containers/glass.kagerou.phosphene)
 • Video library + variants
 • WallpaperPrefs.plist
 • BMP snapshot cache

App side(Phosphene/) — SwiftUI menu-bar app. Manages the on-disk video library, transcodes optional lower-resolution variants viaVideoOptimizationService, exposes preferences, and posts a Darwin notification when the library changes.

Extension side(PhospheneExtension/) — runs inside the systemWallpaperAgentprocess when a Phosphene wallpaper is active. LoadsWallpaperExtensionKit.frameworkat runtime, registers as a wallpaper provider, and renders frames into a remoteCAContextviaAVSampleBufferDisplayLayer. It receives XPCacquire/update/invalidate/snapshotcalls fromWallpaperAgentand routes presentation-mode changes throughPlaybackPolicy.

PlaybackPolicyis the single source of truth for playback behavior. Inputs (thermal state, battery, presentation mode, user pause, occlusion, etc.) collapse to one offull / reduced / minimal / paused. The renderer applies the policy on every state change.

VideoRendererowns the decode pipeline. Instead ofAVPlayerLayer— which silently fails inside a remoteCAContext— it drivesAVSampleBufferDisplayLayermanually: oneAVAssetReaderfor the current loop, a preloaded one for the next, and a PTS offset that grows across loops to keep the timeline monotonically increasing. Result is glitch-free looping without flushing the renderer.

## Quirks worth knowing

* WallpaperSnapshotXPCswizzle.The system's snapshot encoder checkstype(of: coder) == NSXPCCoder.self, but the real coder is a subclass. Without the runtime swizzle inPhospheneExtension.swift, snapshots silently encode to nothing and you get a grey lock screen during transitions.
* Mirror-based XPC parsing.Apple's request types (WallpaperCreationRequestXPCetc.) aren't part of any public SDK header. The extension reads them viaMirrorreflection. If Apple renames fields, expect surgical breakage.
* Variants are advisory.A "1080p@30" variant won't be selected if Power-Monitor thinks we're on AC and idle —PlaybackPolicyalways picks the highest tier that's still allowed.

## License

MIT. Do whatever you want, no warranty.

## Acknowledgements

Built by@kageroumado. Phosphene was originally a commercial project; it's open-source now because the market for "video wallpaper apps on macOS" turned out to be more crowded than it looked.

## About

A video wallpaper engine for macOS Tahoe

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

528

 stars
 

### Watchers

0

 watching
 

### Forks

13

 forks
 

 Report repository

 

## Releases1

v1.0 — initial release

 Latest

 

May 21, 2026

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Swift98.4%
* Objective-C1.6%