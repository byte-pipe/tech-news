---
title: GitHub - wbsmolen/aerospork: An i3-like tiling window manager for macOS — tree layout, instant virtual workspaces, TOML config, and a settings GUI. Fo...
url: https://github.com/wbsmolen/aerospork
date: 2026-08-25
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-25T06:06:04.445857
---

# GitHub - wbsmolen/aerospork: An i3-like tiling window manager for macOS — tree layout, instant virtual workspaces, TOML config, and a settings GUI. Fo...

# AeroSpork – i3‑like tiling window manager for macOS

## Overview
- AeroSpork is a tiling window manager that mimics i3’s tree‑based layout on macOS.  
- Windows are leaves of a layout tree; workspaces are emulated rather than mapped to native Spaces.  
- Configuration is done in TOML, controlled via a CLI, and a native settings GUI is provided.  
- It is a fork of **AeroSpace** (MIT‑licensed) and retains the tree model, workspace emulation, and most command surface.

## Why the fork was created
- **Performance issues**: the original felt sluggish, especially on a DisplayLink dock.  
- **State drift**: workspace state that was correct at login became inaccurate after long sessions.  
- **DisplayLink handling**: workspaces often appeared on the wrong screen after undocking/redocking because monitors were matched by name/regex/index, which does not survive a redock.  
- An upstream PR (#1526, July 2025) addressing monitor handling was closed without review, prompting a separate implementation.

### Improvements introduced
- **Robust monitor identification** (`model/MonitorFingerprint.swift`): matches displays by per‑display UUID, then EDID vendor/model/serial, then name, then size; debounces screen‑reconfiguration events.  
- **Reduced sluggishness**: coalesces bursts of accessibility events into a single layout pass with a 50 ms debounce (`util/RefreshDebouncer.swift`) and skips redundant AX writes when a window is already at its target frame (`MacApp.setFrames`).  
- **Eliminated drift**: workspaces are created on demand and released when empty, rather than being pre‑materialized for every named keybinding.

## Technical stack
- **Language**: Swift 6 (toolchain pinned to 6.4).  
- **Minimum OS**: macOS 13.0 Ventura.  
- **UI**: SwiftUI/AppKit with a `MenuBarExtra` and native Settings pane.  
- **Dependencies**:  
  - TOMLKit (configuration parsing)  
  - Sparkle (in‑app updates)  
- **IPC / CLI**: POSIX AF_UNIX stream socket with length‑prefixed framing (`Sources/Common/util/UnixSocket.swift`).  
- **Global hotkeys**: Carbon `RegisterEventHotKey` (`config/HotkeyBinding.swift`).  
- **Volume control**: CoreAudio (`util/SystemVolume.swift`).  
- **Display identity**: CoreGraphics APIs (`CGDisplayCreateUUIDFromDisplayID`, vendor/model/serial).  
- **Window IDs**: Private shim over `_AXUIElementGetWindow` (`Sources/PrivateApi/`).  
- **Build system**: SwiftPM for CLI/debug builds; XcodeGen + `xcodebuild` for the `.app` bundle (SwiftPM cannot produce a bundle).

## Design decisions
- **Minimal dependencies**: removed wrappers (BlueSocket, HotKey, ISSoundAdditions, swift‑collections) and used platform‑provided APIs directly.  
- **Sparkle** added as the sole external update mechanism because there is no App Store path.  
- **CoreGraphics over IOKit** for display identification; CoreGraphics supplies a per‑display UUID that survives DisplayLink docks, unlike IOKit on Apple Silicon.  
- **Private window ID** retained to obtain a stable identifier for tree keys; this precludes App Store distribution, so the app is signed with a Developer ID and notarized.  
- **Workspace placement persistence**: emulated workspaces remember placement across restarts by keying on the macOS window server ID, which remains stable until a logout, reboot, or app relaunch.  
- **Config writer** is line‑based to preserve comments and unsupported GUI fields; it rewrites only changed keys instead of re‑serializing the whole file.

## Repository layout (high‑level)
- `Sources/` – core implementation.  
- `dev-docs/`, `docs/` – documentation and performance notes.  
- `script/`, `build-*.sh` – build and release scripts.  
- `README.md`, `LICENSE.txt`, `CONTRIBUTING.md` – project metadata.  

The project provides a performant, display‑aware tiling manager for macOS users who need reliable workspace handling on multi‑monitor setups, especially those involving DisplayLink hardware.