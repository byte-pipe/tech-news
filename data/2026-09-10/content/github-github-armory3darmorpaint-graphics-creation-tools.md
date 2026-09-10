---
title: 'GitHub - armory3d/armorpaint: Graphics Creation Tools · GitHub'
url: https://github.com/armory3d/armorpaint
site_name: github
content_file: github-github-armory3darmorpaint-graphics-creation-tools
fetched_at: '2026-09-10T14:49:46.328096'
original_url: https://github.com/armory3d/armorpaint
author: armory3d
description: Graphics Creation Tools. Contribute to armory3d/armorpaint development by creating an account on GitHub.
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 armory3d

 

/

armorpaint

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork511
* Star4.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

6,180 Commits
6,180 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
base
base
 
 
paint
paint
 
 
.clang-format
.clang-format
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
license.md
license.md
 
 
readme.md
readme.md
 
 
View all files

## Repository files navigation

# armorpaint

ArmorPaintis a software for 3D PBR texture painting - check out themanual.

Note 1: This repository is aimed at developers and may not be stable. Distributed binaries arepaidto help with the project funding. All of the development is happening here in order to make it accessible to everyone. Thank you for support!

Note 2: If you are compiling git version of ArmorPaint, then you need to have a compiler (Visual Studio with clang tools- Windows,clang + dependencies- Linux,Xcode- macOS / iOS,Android Studio- Android) andgitinstalled.

git clone https://github.com/armory3d/armorpaint

cd
 armorpaint/paint

Windows (x64)

..
\b
ase
\m
ake

#
 Open generated Visual Studio project at `build\ArmorPaint.sln`

#
 Build and run

Linux (x64)

../base/make --run

macOS (arm64)

../base/make

#
 Open generated Xcode project at `build/ArmorPaint.xcodeproj`

#
 Build and run

Android (arm64)

../base/make --target android

#
 Open generated Android Studio project at `build/ArmorPaint`

#
 Build for device

iOS (arm64)

../base/make --target ios

#
 Open generated Xcode project `build/ArmorPaint.xcodeproj`

#
 Build for device

WASM

../base/make --target wasm --compile --embed

Generating a locale file

./base/make --js base/tools/extract_locales.js 
<
locale code
>

#
 Generates a `paint/assets/locale/<locale code>.json` file

Embedding data files

#
 Requires compiler with c23 #embed support (clang 19 or newer)

../base/make --embed