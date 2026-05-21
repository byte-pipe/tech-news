---
title: GitHub - kageroumado/phosphene: A video wallpaper engine for macOS Tahoe · GitHub
url: https://github.com/kageroumado/phosphene
date: 2026-05-21
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-22T06:02:40.267238
---

# GitHub - kageroumado/phosphene: A video wallpaper engine for macOS Tahoe · GitHub

# Phosphene – A video wallpaper engine for macOS Tahoe

## Overview
- Phosphene is a menu‑bar app plus a wallpaper extension that lets users set personal video files (MP4, MOV, etc.) as macOS desktop and lock‑screen wallpapers.  
- Integrates with the native wallpaper picker, appearing alongside Apple’s Aerials in System Settings → Wallpaper.  
- Built on Apple’s private `WallpaperExtensionKit` framework, enabling out‑of‑process playback that survives app quits and follows the OS lock‑screen/idle lifecycle.  
- Uses runtime `dlopen` and Mirror‑based introspection; may break with major OS updates. Targets macOS 26 (Tahoe) on Apple Silicon.

## Key Features
- **Custom video wallpapers** – import any AVFoundation‑readable video; appears in system picker.  
- **Gapless looping** – frame‑accurate loops by offsetting PTS/DTS, avoiding flushes or stutter.  
- **Multi‑display & per‑Space support** – independent wallpapers per display, persisted by macOS.  
- **Power‑aware playback** – playback policy adapts to thermal state, battery level, AC power, Game Mode, and presentation mode.  
- **Smooth lock‑screen transition** – cubic‑ease in/out when “Only on Lock Screen” is enabled, matching Apple Aerials.  
- **Pause when occluded** – stops rendering when all displays are covered by windows.  
- **Adaptive variants** – optional lower‑resolution / lower‑fps pre‑renders; renderer selects cheapest variant that satisfies current policy.  
- **Menu‑bar control** – preview, pause, switch displays, configure behavior, launch at login.

## Requirements
- macOS Tahoe (26.0+) – relies on the wallpaper extension point introduced in macOS 14 and Tahoe‑only SwiftUI APIs.  
- Apple Silicon (arm64‑apple‑macos26.0).  
- Xcode 17+ with Swift 6 strict concurrency enabled.

## Building & Installation
1. Clone the repository and open `Phosphere.xcodeproj` in Xcode.  
2. Select the `Phosphene` scheme and run.  
3. Set a development team for code signing; the wallpaper extension is embedded and registers on app launch.  

## Using a Video Wallpaper
1. Launch Phosphene and add videos via the menu‑bar icon.  
2. Open **System Settings → Wallpaper**; Phosphene’s videos appear under a dedicated collection.  
3. Select a video; macOS handles assignment while the extension supplies frames.

## Architecture Overview
- **Phosphene.app** (menu‑bar UI)  
  - Manages video library, metadata, optimization, preferences.  
  - Sends Darwin notifications on library changes.  
- **PhospheneExtension.appex** (runs inside `WallpaperAgent`)  
  - Loads `WallpaperExtensionKit` at runtime, registers as wallpaper provider.  
  - Renders frames via `AVSampleBufferDisplayLayer` into a remote CA context.  
  - Handles XPC calls for acquire, update, invalidate, snapshot.  
  - Monitors power/thermal state and applies `PlaybackPolicy`.  
- Shared App Group container stores video files, variants, preferences, and snapshot cache.  
- **PlaybackPolicy** consolidates inputs (thermal, battery, presentation mode, user pause, occlusion) into a single playback state (full, reduced, minimal, paused).  
- **VideoRenderer** uses manual `AVAssetReader` pipelines with PTS offsets for seamless looping, avoiding `AVPlayerLayer` limitations in remote contexts.

## Notable Quirks
- **WallpaperSnapshot XPC swizzle** – required to bypass a system bug where snapshots encode to nothing without runtime method swizzling.  
- **Mirror‑based XPC parsing** – relies on private request types; changes in Apple’s internal field names will break functionality.  
- **Variant selection** – advisory; the highest‑quality variant allowed by the current policy is chosen, not necessarily the one explicitly requested.

## License
- MIT License – free to use, modify, and distribute without warranty.

## Acknowledgements
- Developed by @kageroumado. Originally a commercial project; open‑sourced after the market for macOS video wallpaper apps became saturated.