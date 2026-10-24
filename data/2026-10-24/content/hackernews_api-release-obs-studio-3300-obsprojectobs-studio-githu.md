---
title: Release OBS Studio 33.0.0 · obsproject/obs-studio · GitHub
url: https://github.com/obsproject/obs-studio/releases/tag/33.0.0
site_name: hackernews_api
content_file: hackernews_api-release-obs-studio-3300-obsprojectobs-studio-githu
fetched_at: '2026-10-24T14:29:35.404337'
original_url: https://github.com/obsproject/obs-studio/releases/tag/33.0.0
author: pentagrama
date: '2026-10-24'
description: OBS Studio - Free and open source software for live streaming and screen recording - Release OBS Studio 33.0.0 · obsproject/obs-studio
tags:
- hackernews
- trending
---

# OBS Studio 33.0.0

Latest

Latest

 

Compare

# Choose a tag to compare

 

## Sorry, something went wrong.

 

 Filter

 
Loading

 

## Sorry, something went wrong.

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

## No results found

 

 
 

View all tags

 

github-actions

 released this

 

 23 Oct 22:20
 

 33.0.0
 

72e8665

## 33.0 New Features

* Updated CEF from 127/6533 to 150/7871 [WizardCM] (#13900)This is a massive update to the underlying framework used for browser sources and docks from the July 2024 release to September 2026All of this work is on the backend and should be invisible to users. Please be sure to report any new weirdness or problems you run into with browser sources!
* This is a massive update to the underlying framework used for browser sources and docks from the July 2024 release to September 2026
* All of this work is on the backend and should be invisible to users. Please be sure to report any new weirdness or problems you run into with browser sources!
* Complete overhaul to plugin loading [FiniteSingularity/PatTheMav] (#13594)First-party plugins are now in a new folder named coreThird-party plugins have an updated installation location and folder structureExisting third-party plugins will continue to load from the legacy locations until OBS Studio 34.0More information is available in ourknowledge base article
* First-party plugins are now in a new folder named core
* Third-party plugins have an updated installation location and folder structure
* Existing third-party plugins will continue to load from the legacy locations until OBS Studio 34.0
* More information is available in ourknowledge base article
* Improved how source snapping works in the preview [Warchamp7] (#12298)New visual indicator addedSources now snap along the entire axis instead of only when directly touchingSources no longer snap to hidden sources
* New visual indicator added
* Sources now snap along the entire axis instead of only when directly touching
* Sources no longer snap to hidden sources
* Improved behavior of spinboxes for number values [Warchamp7] (#12337)Typing is no longer mysteriously blocked in some situationsNumbers are no longer cut off in some situationsValues now update only after pressing Enter and Enter does not close the windowHolding Shift + Up/Down now advances multiple steps at a timeDragging the cursor inside the input but outside the text itself now works properly
* Typing is no longer mysteriously blocked in some situations
* Numbers are no longer cut off in some situations
* Values now update only after pressing Enter and Enter does not close the window
* Holding Shift + Up/Down now advances multiple steps at a time
* Dragging the cursor inside the input but outside the text itself now works properly
* Enabled NVENC on Arm64 [RytoEX] (#13827)

## 33.0 Changes

* Added a check for encoders being missing when loading a profile [derrod] (#11340)
* Added support for newest NVIDIA Broadcast SDKs for NVIDIA Audio Effects and Video Effects [pkviet] (#13838)
* Added hotkeys for controlling audio monitoring of a source [Warchamp7] (#13599)
* Changed Safe Mode to not start WebSocket Server [FiniteSingularity/RytoEX] (#13984)
* Fixed issues with groups in Studio Mode [Warchamp7] (#11092)Fixed moving sources inside a group causing them to glitch out in ProgramFixed moving sources inside a group showing up live in Program
* Fixed moving sources inside a group causing them to glitch out in Program
* Fixed moving sources inside a group showing up live in Program
* Adjusted naming of Window Capture methods on Windows [Penwy] (#12047)
* Improved detection of fullscreen games for Game Capture [Kira-NT] (#10880)
* Improved transparency handling for macOS Screen Capture [jcm93] (#13030)
* Scaled simple output recording audio bitrate by channel count [nickvonkaenel] (#13311)
* Removed support for Ubuntu 24.04

## 33.0 Bug Fixes

* Added a startup error if obs-transitions failed to load [notr1ch] (#13321)
* Improved file splitting for Hybrid MP4/MOV [derrod] (#13386)
* Fixed outputs getting stuck running when a bad rescale output resolution is set [suogesi] (#13375)
* Fixed monitoring icon state getting desynced when using third-party tools or websockets [prgmitchell] (#13822)
* Fixed a crash on macOS 27.2 when starting OBS Studio [RytoEX] (#14070)
* Fixed potential crash when shader cache file is invalid [notr1ch] (#13538)
* Fixed a potential crash on Linux when USB mic is removed [R0te/RytoEX] (#13922)
* Fixed a potential crash when renaming a source with the Add Source window open [Warchamp7] (#13800)
* Fixed a potential deadlock during video/audio tasks [exeldro] (#13579)
* Fixed an issue with B-frame offset calculation in AMF that could cause streams to disconnect [lexano-ivs] (#13762)
* Fixed PipeWire screencast sources being duplicated in studio mode [tytan652] (#13673)
* Fixed a potential crash when switching off a newly created profile [Warchamp7] (#13182)
* Fixed a source toolbar crash when source type is missing [Penwy] (#13539)
* Fixed profile import failing on paths with a trailing slash [Ushkalovk] (#13863)

## 33.0 Developer Information

* Added frontend event and output signal for replay buffer saving [Penwy] (#8955)
* Added guidance regarding the theme system to the top of all theme files [Warchamp7] (#13733)
* Added ability to set a file extension filter for OBS_PATH_FILE_SAVE path types [FiniteSingularity] (#10190)
* Added obs_frontend_is_safe_mode for first-party pluginsThird-party plugins are not loaded at all in Safe Mode
* Third-party plugins are not loaded at all in Safe Mode
* Added versions to Flatpak plugin extension point [tytan652] (#13735)
* Added obs_canvas_video_active() to check if the video of a canvas is active [exeldro] (#13110)
* The minimum supported versions of Visual Studio, Windows SDK, and clang-format have been increased. Previous versions may continue to work, but will no longer be tested/supported. It is recommended that build environments are kept up-to-date with the project's toolchain.Changed Windows builds to use Visual Studio 2026 and SDK 26100 [RytoEX] (#13543)Changed clang-format version used to 22.1.3 [PatTheMav] (#13549)
* Changed Windows builds to use Visual Studio 2026 and SDK 26100 [RytoEX] (#13543)
* Changed clang-format version used to 22.1.3 [PatTheMav] (#13549)
* Changed obs_canvas_reset_video() to allow resetting a canvas's video when any other canvas's video is active, but not its own video [exeldro] (#13110)
* Updated libnsgif to 1.0.0 [RytoEX] (#11178)This is a breaking change for any plugins using libobs/graphics gs_image_file
* This is a breaking change for any plugins using libobs/graphics gs_image_file
* Clarified documentation for obs_module_unload [notr1ch] (#13327)
* Required MbedTLS 3 and exclude 4 or later [tytan652] (#13799)
* Removed support for FFmpeg 6.x and 7.x [RytoEX] (#13964)
* Removed support for Qt 6.4-6.9 [RytoEX] (#13969)
* Fixed repeated preview enable/disables not working [WarmUpTill] (#12580)
* Only emit core signal handlers for public canvases [tt2468] (#13574)
* Deprecated unused hidden API for sources [derrod] (#13122)
* Deprecated APIs for audio source monitoring_type [Warchamp7] (#13599)This is replaced by a new monitoring_enabled boolean
* This is replaced by a new monitoring_enabled boolean

### Checksums

OBS-Studio-33.0.0-Sources.tar.gz: c1ae3c98c1bb70ebdced33e894a526fcbbbda9bfd95806970a3fc31f74b08f6c
OBS-Studio-33.0.0-Ubuntu-26.04-x86_64-dbsym.ddeb: 12045838dfd0202ba26b77fb2e8572f4db27c709b3aabe425ac979ee0532a61c
OBS-Studio-33.0.0-Ubuntu-26.04-x86_64.deb: f5844914eadd560314f3a9db020afa7a8afbefb67a26c488f2956dc339704918
OBS-Studio-33.0.0-Windows-arm64-PDBs.zip: e43139f467ccedb4fbb583f09ce64341a7c96b44030181ef57abd1528142b947
OBS-Studio-33.0.0-Windows-arm64.zip: 02c53d7bff3f9c159401da79fc375d7b75b00c9ca62d2b4ec5fc05a575d2fa1f
OBS-Studio-33.0.0-Windows-x64-Installer.exe: 3bf55dae6d9db651505828090de74540296c742ed2a94a28cf055cb6ddc6bed3
OBS-Studio-33.0.0-Windows-x64-PDBs.zip: dbda0e1e9967262380e619e071de068809ccae2ccb3f68f52034db9a8276475d
OBS-Studio-33.0.0-Windows-x64.zip: 3369a3ecd67b5669a8a08d77357f87cc786d1fba42fbbd1054d841a69f6271a7
OBS-Studio-33.0.0-macOS-Apple-dSYMs.tar.xz: 6b162ccbafc2eaaee3ced192a851eb5d3d616ad8d54125ce5cd701d26e6939bf
OBS-Studio-33.0.0-macOS-Apple.dmg: b36f4e9da5f2f17c733ba711c8fe0656d6b0cd573cfe96eeb3e68325cffef739
OBS-Studio-33.0.0-macOS-Intel-dSYMs.tar.xz: 997ba41207e9fd7b045b955561cdd5c32b29f12d98ea3ea5a43de7c9edd8f1c7
OBS-Studio-33.0.0-macOS-Intel.dmg: 8524ff428f038573f8905a206841081d3da9ec607063906f7bbfe38d55810c1c

 

Assets

14

 

 
Loading

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
👍

38

 
tx2x, CherylAoife, UltraRaid, snipcola, Milli189, Warkratos, Sergey-Makar0v, bidu2352, westlake-san, omasanori, and 28 more reacted with thumbs up emoji

 
😄

6

 
AlexSkrin, 0x00MagicKey, Ai686Leo, maxkorsov, YannMagnin, and boxden reacted with laugh emoji

 
🎉

22

 
larouxn, svengreb, UltraRaid, Alzyon, Warkratos, omasanori, 4p3rtur3, AlexSkrin, 0x00MagicKey, turtleqiu, and 12 more reacted with hooray emoji

 
❤️

20

 
larouxn, Desenrrollado, ItzFlitz, UltraRaid, Milli189, Warkratos, westlake-san, omasanori, 4p3rtur3, AlexSkrin, and 10 more reacted with heart emoji

 
🚀

17

 
larouxn, svengreb, UltraRaid, Warkratos, westlake-san, omasanori, 4p3rtur3, AlexSkrin, 0x00MagicKey, Ai686Leo, and 7 more reacted with rocket emoji

 
👀

4

 
AlexSkrin, 0x00MagicKey, maxkorsov, and boxden reacted with eyes emoji

 

All reactions

 
50 people reacted