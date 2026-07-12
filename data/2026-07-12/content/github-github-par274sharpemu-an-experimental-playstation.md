---
title: 'GitHub - par274/sharpemu: An experimental PlayStation 5 emulator project. · GitHub'
url: https://github.com/par274/sharpemu
site_name: github
content_file: github-github-par274sharpemu-an-experimental-playstation
fetched_at: '2026-07-12T19:27:18.511975'
original_url: https://github.com/par274/sharpemu
author: par274
description: An experimental PlayStation 5 emulator project. Contribute to par274/sharpemu development by creating an account on GitHub.
---

par274

 

/

sharpemu

Public

* NotificationsYou must be signed in to change notification settings
* Fork69
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

151 Commits
151 Commits
.github
.github
 
 
LICENSES
LICENSES
 
 
assets/
images
assets/
images
 
 
scripts
scripts
 
 
src
src
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
Directory.Build.props
Directory.Build.props
 
 
Directory.Packages.props
Directory.Packages.props
 
 
LICENSE.txt
LICENSE.txt
 
 
README.md
README.md
 
 
REUSE.toml
REUSE.toml
 
 
SharpEmu.slnx
SharpEmu.slnx
 
 
global.json
global.json
 
 
nuget.config
nuget.config
 
 
View all files

## Repository files navigation

# SharpEmu

An experimental PlayStation 5 emulator for Windows, Linux and macOS.

Join our Discord for development updates, compatibility discussions, support, and community chat.

Warning

Currently the primary development target is Windows.

Warning

SharpEmu is an experimental PS5 emulator developed from scratch in C#. The current focus is on accuracy and infrastructure setup rather than game-specific compatibility.

## Info

SharpEmu is an emulator project currently in its early stages of development.

This project is developed purely for research and educational purposes. There are no commercial goals associated with it. We enjoy learning about system architecture and reverse engineering.

SharpEmu focuses exclusively on the PlayStation 5.Our goal isnotto emulate PS4 games, as there is already an excellent emulator dedicated to that platform:ShadPS4.

## Status

The emulator can currently load theeboot.binof real games, execute native CPU instructions, and partially handle kernel-related functionality. However, several critical components are still missing.

Current capabilities include:

* Loadingeboot.binand.elffiles
* Executing native CPU instructions
* Reading basic game metadata (title, version, etc.)
* Loading system modules (prx/sys_module)
* Partial support for some kernel functions
* FiberandAMPRexports
* PlayGo scenarios
* Initial loading game files
* Shader/resource submits and AGC initial
* Video outputs in some games

Some games have reached likesceVideoOutand AGC stages.

Currently the project primarily targets Windows. Cross-platform support (Linux and macOS) is planned, but development is currently focused on Windows to simplify early-stage debugging and iteration.

## Using

* Build or Publish project or download in release tab.
* Open Powershell.Run Emulator GUI.Or command:.\SharpEmu "eboot.bin" 2>&1 | Tee-Object -FilePath "log.txt"
* Run Emulator GUI.
* Or command:.\SharpEmu "eboot.bin" 2>&1 | Tee-Object -FilePath "log.txt"

## Games Tested

* Demon's Souls RemakeDemon's Souls [PPSA01341]Demon's Souls is now video loop. Shaders are ready to be converted to SPIR-V/Vulkan. We are continuing our work on this.
* Demon's Souls [PPSA01341]
* Demon's Souls is now video loop. Shaders are ready to be converted to SPIR-V/Vulkan. We are continuing our work on this.
* Poppy Playtime Chapter 1Poppy Playtime Chapter 1 [PPSA20591]
* Poppy Playtime Chapter 1 [PPSA20591]
* SILENT HILL: The Short MessageSILENT HILL: The Short Message [PPSA10112]
* SILENT HILL: The Short Message [PPSA10112]
* Dreaming SarahDreaming Sarah [PPSA02929]Real texture rendering for this game;
* Dreaming Sarah [PPSA02929]
* Real texture rendering for this game;

Important

This project doesnotsupport or condone piracy.All games used during development and testing are dumped from consoles that we personally own.Users are expected to use legally obtained copies of their games.

## Build

1. Install the.NET SDK.
2. Clone the repository:git clone https://github.com/par274/sharpemu.git
3. Open the solution file (SharpEmu.slnx) inVSCode.
4. Build the project:dotnet buildordotnet publish
5. Build artifacts will be located in theartifactsdirectory.

## Disclaimer

SharpEmu is an experimental emulator intended for research and educational purposes.

This project does not contain any copyrighted system firmware, game data, or proprietary PlayStation assets.

## Special Thanks

The following projects were extremely helpful during development:

* ShadPS4Helped with understanding the basic architecture of the PlayStation 4.
* KytyOne of the few PS5 emulator projects available and very useful for studying native code execution.
* RyujinxProvided valuable references for filesystem handling and low-level C# implementation patterns.

# License

* GPL-2.0 license

## About

An experimental PlayStation 5 emulator project.

### Topics

 windows

 emulator

 csharp

 emulation

 ps5

 playstation5

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

39

 watching
 

### Forks

69

 forks
 

 Report repository

 

## Releases76

SharpEmu win64 8c15077

 Latest

 

Jul 12, 2026

 

+ 75 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C#99.9%
* Python0.1%