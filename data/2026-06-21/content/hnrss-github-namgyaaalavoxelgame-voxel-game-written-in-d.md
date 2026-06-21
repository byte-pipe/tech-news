---
title: 'GitHub - namgyaaal/avoxelgame: Voxel Game written in Dyalog APL and SDL3 · GitHub'
url: https://github.com/namgyaaal/avoxelgame
site_name: hnrss
content_file: hnrss-github-namgyaaalavoxelgame-voxel-game-written-in-d
fetched_at: '2026-06-21T19:34:35.995057'
original_url: https://github.com/namgyaaal/avoxelgame
date: '2026-06-21'
description: Voxel Game written in Dyalog APL and SDL3. Contribute to namgyaaal/avoxelgame development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

namgyaaal

 

/

avoxelgame

Public

* NotificationsYou must be signed in to change notification settings
* Fork2
* Star62

 
 
 
 
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

125 Commits
125 Commits
assets
assets
 
 
avg
avg
 
 
images
images
 
 
lse
lse
 
 
saves
saves
 
 
sdl3_consts
sdl3_consts
 
 
shaders
shaders
 
 
.gitattributes
.gitattributes
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
compile_shaders.sh
compile_shaders.sh
 
 
main.apls
main.apls
 
 
View all files

## Repository files navigation

# A Voxel Game

This started off as a bet with myself that APL notation would provide an easier way to make a voxel game.

This is highly experimental and buggy.

## Controls

* W-A-S-D to move
* Space to jump
* Mouse to move the camera
* Q to quit
* I to toggle render information
* F for fast noclip mode
* L to lock and unlock the mouse while in-game
* 1-5 to select different blocks to place

# Requirements

* Dyalog APL 20.0
* A C Compiler
* CMake
* Vulkan, DirectX12 or Metal graphics are required. For more information, checkhere
* sdl3, sdl3_ttf and sdl3_image (MacOS withbrew)

# Instructions

## Running on MacOS or Linux

After installing dependencies and cloning, make sure you build and install LSE.
e.g.,

cd lse 
mkdir build
cd build
cmake ..
make 
make install

This should installlibLSE.dylibon macOS andlibLSE.soon Linux in./libs/alongside the relevant SDL3 library files.

After that you should be able to run with./main.apls

Some Linux users may havedyalogscriptlocated in a different directory. If that's the case, the shebang inmain.aplsshould be replaced with the path specified bywhich dyalogscript

## Running on Windows

Compiling everything on Windows is a bit more tricky and is best done with finding the SDL3 dev libraries provided on libsdl3 releases with cmake-gui.

.dlls are provided as a releaseherewhich can be placed in a folder./libson the directory this repository.

Afterwards, the game can be played through a Dyalog session like so:

]cd
 
<
ROOT
 
DIRECTORY
>

]
link
.
create
 
#
 
.
/
avg

Run

state
.
Play

# Compiling Shaders

Source code that gets compiled to different shader formats is in./shaders/glsl

Shaders come bundled with this repo. However, if you want to modify them, edit the glsl shaders and run./compile_shaders.sh

Note that this requires the DirectX Shader Compiler, glslc and spirv-cross.

# Known Issues

* There are significant performance regressions on Windows being worked on.
* DirectX12 backend is currently not supported on Windows.
* You currently can't play multiple times in the same session.Known to syserror 999 !There's probably memory leaks somewhere !
* Known to syserror 999 !
* There's probably memory leaks somewhere !

# Credits

Textures by Madeline Vergani (@RubenVerg)

## About

Voxel Game written in Dyalog APL and SDL3

### Topics

 voxel

 apl

 voxel-game

 dyalog-apl

 sdl3

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

62

 stars
 

### Watchers

0

 watching
 

### Forks

2

 forks
 

 Report repository

 

## Releases1

AVG win32-x64 .dlls

 Latest

 

May 25, 2026

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* APL83.3%
* C11.4%
* GLSL2.4%
* Shell1.7%
* CMake1.2%