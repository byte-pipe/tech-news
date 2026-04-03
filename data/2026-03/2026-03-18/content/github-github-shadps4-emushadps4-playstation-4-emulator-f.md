---
title: 'GitHub - shadps4-emu/shadPS4: PlayStation 4 emulator for Windows, Linux and macOS written in C++ · GitHub'
url: https://github.com/shadps4-emu/shadPS4
site_name: github
content_file: github-github-shadps4-emushadps4-playstation-4-emulator-f
fetched_at: '2026-03-18T11:20:42.015535'
original_url: https://github.com/shadps4-emu/shadPS4
author: shadps4-emu
description: PlayStation 4 emulator for Windows, Linux and macOS written in C++ - shadps4-emu/shadPS4
---

shadps4-emu

 

/

shadPS4

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork2k
* Star29.5k

 
 
 
 
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

3,733 Commits
3,733 Commits
.ci
.ci
 
 
.github
.github
 
 
LICENSES
LICENSES
 
 
cmake
cmake
 
 
dist
dist
 
 
documents
documents
 
 
externals
externals
 
 
scripts
scripts
 
 
src
src
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CMakeDarwinPresets.json
CMakeDarwinPresets.json
 
 
CMakeLinuxPresets.json
CMakeLinuxPresets.json
 
 
CMakeLists.txt
CMakeLists.txt
 
 
CMakePresets.json
CMakePresets.json
 
 
CMakeSettings.json
CMakeSettings.json
 
 
CMakeWindowsPresets.json
CMakeWindowsPresets.json
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
REUSE.toml
REUSE.toml
 
 
shell.nix
shell.nix
 
 
View all files

## Repository files navigation

# shadPS4

Bloodborne by From Software

Hatsune Miku Project DIVA Future Tone by SEGA

Yakuza 0 by SEGA

DRIVECLUB™ by Evolution Studios

# General information

shadPS4is an earlyPlayStation 4emulator forWindows,LinuxandmacOSwritten in C++.

Important

This is the emulator core, which does not include a GUI. If you just want to use the emulator as an end user, download theQtLauncherinstead.

If you encounter problems or have doubts, do not hesitate to look at theQuickstart.To verify that a game works, you can look atshadPS4 Game Compatibility.To discuss shadPS4 development, suggest ideas or to ask for help, join ourDiscord server.To get the latest news, go to ourX (Twitter)or ourwebsite.You can donate to the project via ourKofi page.

# Status

Important

shadPS4 is early in development, don't expect a flawless experience.

Currently, the emulator can successfully run games likeBloodborne,Dark Souls Remastered,Red Dead Redemption, and many other games.

# Why

This project began for fun. Given our limited free time, it may take some time before shadPS4 can run more complex games, but we're committed to making small, regular updates.

# Building

## Docker

For building shadPS4 in a containerized environment using Docker and VSCode, check the instructions here:Docker Build Instructions

## Windows

Check the build instructions forWindows.

## Linux

Check the build instructions forLinux.

## macOS

Check the build instructions formacOS.

Important

macOS users need at least macOS 15.4 to run shadPS4. Due to GPU issues there are currently heavy bugs on Intel Macs.

# Usage examples

Important

For a user-friendly GUI, download theQtLauncher.

To get the list of all available commands and also a more detailed description of what each command does, please refer to the--helpflag's output.

Below is a list of commonly used command patterns:

shadPS4 CUSA00001 
#
 Searches for a game folder called CUSA00001 in the list of game install folders, and boots it.

shadPS4 --fullscreen 
true
 --config-clean CUSA00001 
#
 the game argument is always the last one,

shadPS4 -g CUSA00001 --fullscreen 
true
 --config-clean 
#
 ...unless manually specified otherwise.

shadPS4 /path/to/game.elf 
#
 Boots a PS4 ELF file directly. Useful if you want to boot an executable that is not named eboot.bin.

shadPS4 CUSA00001 -- -flag1 -flag2 
#
 Passes '-flag1' and '-flag2' to the game executable in argv.

# Debugging and reporting issues

For more information on how to test, debug and report issues with the emulator or games, read theDebugging documentation.

# Keyboard and Mouse Mappings

Note

Some keyboards may also require you to hold the Fn key to use the F* keys. Mac users should use the Command key instead of Control, and need to use Command+F11 for full screen to avoid conflicting with system key bindings.

Button

Function

F10

FPS Counter

Ctrl+F10

Video Debug Info

F11

Fullscreen

F12

Trigger RenderDoc Capture

Note

Xbox and DualShock controllers work out of the box.

Controller button

Keyboard equivalent

LEFT AXIS UP

W

LEFT AXIS DOWN

S

LEFT AXIS LEFT

A

LEFT AXIS RIGHT

D

RIGHT AXIS UP

I

RIGHT AXIS DOWN

K

RIGHT AXIS LEFT

J

RIGHT AXIS RIGHT

L

TRIANGLE

Numpad 8 or C

CIRCLE

Numpad 6 or B

CROSS

Numpad 2 or N

SQUARE

Numpad 4 or V

PAD UP

UP

PAD DOWN

DOWN

PAD LEFT

LEFT

PAD RIGHT

RIGHT

OPTIONS

RETURN

BACK BUTTON / TOUCH PAD

SPACE

L1

Q

R1

U

L2

E

R2

O

L3

X

R3

M

Keyboard and mouse inputs can be customized in the settings menu by clicking the Controller button, and further details and help on controls are also found there. Custom bindings are saved per-game. Inputs support up to three keys per binding, mouse buttons, mouse movement mapped to joystick input, and more.

# Firmware files

shadPS4 can load some PlayStation 4 firmware files.
The following firmware modules are supported and must be placed in shadPS4'ssys_modulesfolder.

Modules

Modules

Modules

Modules

libSceCesCs.sprx

libSceFont.sprx

libSceFontFt.sprx

libSceFreeTypeOt.sprx

libSceJpegDec.sprx

libSceJpegEnc.sprx

libSceJson.sprx

libSceJson2.sprx

libSceLibcInternal.sprx

libSceNgs2.sprx

libScePngEnc.sprx

libSceRtc.sprx

libSceUlt.sprx

libSceAudiodec.sprx

Caution

The above modules are required to run the games properly and must be dumped from your legally owned PlayStation 4 console.

# Main team

* georgemoralis
* psucien
* viniciuslrangel
* roamic
* squidbus
* frodo
* Stephen Miller
* kalaposfos13

Logo is done byXphalnos

# Contributing

If you want to contribute, please read theCONTRIBUTING.mdfile.Open a PR and we'll check it :)

# Special Thanks

A few noteworthy teams/projects who've helped us along the way are:

* Panda3DS: A multiplatform 3DS emulator from our co-author wheremyfoodat. They have been incredibly helpful in understanding and solving problems that came up from natively executing the x64 code of PS4 binaries
* fpPS4: The fpPS4 team has assisted massively with understanding some of the more complex parts of the PS4 operating system and libraries, by helping with reverse engineering work and research.
* yuzu: Our shader compiler has been designed with yuzu's Hades compiler as a blueprint. This allowed us to focus on the challenges of emulating a modern AMD GPU while having a high-quality optimizing shader compiler implementation as a base.
* felix86: A new x86-64 → RISC-V Linux userspace emulator

# License

* GPL-2.0 license

## About

PlayStation 4 emulator for Windows, Linux and macOS written in C++

shadps4.net/

### Topics

 windows

 macos

 linux

 emulator

 cpp

 vulkan

 emulation

 imgui

 ps4

 cpp20

 playstation4

 sdl3

### Resources

 Readme

 

### License

 GPL-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

29.5k

 stars
 

### Watchers

180

 watching
 

### Forks

2k

 forks
 

 Report repository

 

## Releases21

shadps4 v0.15.0 - codename RE6_PRIG

 Latest

 

Mar 17, 2026

 

+ 20 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* ko-fi.com/shadps4

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C++98.6%
* C1.1%
* CMake0.3%
* Assembly0.0%
* GLSL0.0%
* Python0.0%