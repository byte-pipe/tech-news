---
title: 'GitHub - ammaarreshi/Generals-Mac-iOS-iPad: Command & Conquer Generals: Zero Hour running natively on macOS, iPhone & iPad — real engine (EA GPL v3 source, via GeneralsX), DXVK/MoltenVK renderer, RTS touch controls. No game assets included. · GitHub'
url: https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main
site_name: hackernews_api
content_file: hackernews_api-github-ammaarreshigenerals-mac-ios-ipad-command-co
fetched_at: '2026-07-05T11:33:28.508645'
original_url: https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main
author: asronline
date: '2026-07-04'
description: 'Command & Conquer Generals: Zero Hour running natively on macOS, iPhone & iPad — real engine (EA GPL v3 source, via GeneralsX), DXVK/MoltenVK renderer, RTS touch controls. No game assets included. - ammaarreshi/Generals-Mac-iOS-iPad'
tags:
- hackernews
- trending
---

ammaarreshi

 

/

Generals-Mac-iOS-iPad

Public

* NotificationsYou must be signed in to change notification settings
* Fork27
* Star520

 
 
 
 
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

2,001 Commits
2,001 Commits
.devin
.devin
 
 
.github
.github
 
 
.vscode
.vscode
 
 
Core
Core
 
 
Dependencies
Dependencies
 
 
Generals
Generals
 
 
GeneralsMD
GeneralsMD
 
 
GeneralsReplays @ 113cabc
GeneralsReplays @ 113cabc
 
 
GeneralsZH/
Data/
Window/
Menus
GeneralsZH/
Data/
Window/
Menus
 
 
Patches
Patches
 
 
assets
assets
 
 
cmake
cmake
 
 
docs
docs
 
 
flatpak
flatpak
 
 
ios
ios
 
 
references
references
 
 
resources
resources
 
 
scripts
scripts
 
 
triplets
triplets
 
 
.clang-tidy
.clang-tidy
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
AGENTS.md
AGENTS.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CMakePresets.json
CMakePresets.json
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE.md
LICENSE.md
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
TESTING.md
TESTING.md
 
 
stlport.diff
stlport.diff
 
 
vcpkg-lock.json
vcpkg-lock.json
 
 
vcpkg.json
vcpkg.json
 
 
View all files

## Repository files navigation

# Command & Conquer Generals: Zero Hour — macOS, iOS & iPadOS

Zero Hour running natively on Apple Silicon Macs, iPhone, and iPad— campaign,
skirmish, and Generals Challenge, with touch controls built for RTS (tap-select,
drag-box, long-press deselect, two-finger scroll, pinch zoom). No emulation: this
is the real 2003 engine compiled for ARM64, rendering DirectX 8 →DXVK→ Vulkan →MoltenVK→ Metal.

Built on EA's GPL v3 source release viafbraz3/GeneralsX(which did the heavy lifting of the macOS/Linux port — this fork adds the iOS/iPadOS
port and a set of engine fixes). The original GeneralsX README lives on theupstream-mainbranch.

No game assets are included or distributed.You need your own copy
(Steam, ~$5 on sale).

## Quick start — macOS

Prerequisites (one time):

#
 Toolchain

xcode-select --install
brew install cmake ninja meson pkgconf
brew install --cask steamcmd

#
 vcpkg (full clone — a shallow clone breaks manifest baselines)

git clone https://github.com/microsoft/vcpkg 
~
/vcpkg 
&&
 
~
/vcpkg/bootstrap-vcpkg.sh

export
 VCPKG_ROOT=
~
/vcpkg 
#
 add to your shell profile

#
 LunarG Vulkan SDK (NOT the Homebrew cask) — https://vulkan.lunarg.com/sdk/home

export
 VULKAN_SDK=
$HOME
/VulkanSDK/
<
version
>
/macOS 
#
 add to your shell profile

Clone, build, get assets, play:

git clone https://github.com/ammaarreshi/Generals-Mac-iOS-iPad.git GeneralsX

cd
 GeneralsX
./scripts/build/macos/build-macos-zh.sh 
#
 checks deps, configures, builds

./scripts/build/macos/deploy-macos-zh.sh 
#
 creates ~/GeneralsX/GeneralsZH + run.sh

./scripts/get-assets.sh 
<
your_steam_username
>
 
#
 fetches game data you own

cd
 
~
/GeneralsX/GeneralsZH 
&&
 ./run.sh -win

## Quick start — iPhone / iPad

On top of the macOS prerequisites: full Xcode (signed into your Apple ID),brew install xcodegen, and a (free or paid) Apple Developer team.

cd
 GeneralsX
git submodule update --init references/fbraz3-dxvk 
#
 iOS DXVK is built from this + Patches/dxvk-ios.patch

./scripts/build/ios/fetch-moltenvk.sh 
#
 pinned MoltenVK.framework (checksummed)

./scripts/build/ios/stage-fonts.sh 
#
 Liberation fonts, renamed as the game expects

cmake --preset ios-vulkan
cmake --build build/ios-vulkan --target z_generals
GX_TEAM_ID=
<
your-team-id
>
 GX_BUNDLE_ID=com.you.generalszh \
 ./scripts/build/ios/package-ios-zh.sh --install 
#
 assembles, signs, installs

Find your team id in Xcode → Settings → Accounts. Assets ship inside the app
bundle (self-contained install);--devskips the ~2.7 GB copy for fast code
iteration.

## Where things are

Path

What it is

docs/port/PORTING_PLAYBOOK.md

The complete engineering log of this port: every failure mode, root cause, fix — start with 
§8, the bug archaeology
: the black minimap, the silent EVA lines, and the chirp

docs/port/PORTING_PATTERNS.md

Generalized methodology for porting classic Windows games to Apple platforms

docs/port/RELEASE_CHECKLIST.md

Gate for public release

scripts/get-assets.sh

Steam asset fetcher (your own copy; app 2732960)

scripts/build/macos/
, 
scripts/build/ios/

Build, deploy, packaging pipelines

ios/

XcodeGen signing-stub project + 
ios/config/
 (staged Options.ini, dxvk.conf)

Patches/dxvk-ios.patch

DXVK changes the iOS d3d8/d3d9 dylibs are built from (applied via the local-fork build)

## Known issues

* Long sessions on iPad can be killed by iOS for memory (~3 GB+ resident); the app
exits to the home screen with no dialog. Session logs (current + previous) are in
the Files app under the game's folder. Under investigation.
* Backgrounding mid-game can occasionally crash on iOS — the lifecycle pause covers
the common paths; a rare race remains. Save often.

## License & credits

Engine codeGPL v3(EA's source release → GeneralsX → this fork). Game assets:
not included, not licensed here. Credits: Westwood/EA Pacific (the game), EA (the
source release), fbraz3/GeneralsX (the base port),
TheSuperHackers/GeneralsGameCode (community mainline), DXVK, MoltenVK, SDL,
OpenAL Soft, FFmpeg, Liberation Fonts.

This port was built as a human+AI collaboration: engineering byClaude Code(Anthropic's Claude, Fable model),
directed and playtested on real devices by Ammaar Reshi. The engineering log indocs/port/is the unedited record of how that worked.

## About

Command & Conquer Generals: Zero Hour running natively on macOS, iPhone & iPad — real engine (EA GPL v3 source, via GeneralsX), DXVK/MoltenVK renderer, RTS touch controls. No game assets included.

### Topics

 macos

 ios

 ipad

 command-and-conquer

 rts

 game-port

 open-source-game

 moltenvk

 dxvk

 apple-silicon

 sdl3

 generals-zero-hour

### Resources

 Readme

 

### License

 View license
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

520

 stars
 

### Watchers

1

 watching
 

### Forks

27

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

* C++95.8%
* C2.7%
* CMake0.7%
* Python0.4%
* Shell0.4%
* Perl0.0%