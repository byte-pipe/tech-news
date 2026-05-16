---
title: 'GitHub - neilsonnn/image-blaster: An image-to-world skillset for Claude. · GitHub'
url: https://github.com/neilsonnn/image-blaster
site_name: hnrss
content_file: hnrss-github-neilsonnnimage-blaster-an-image-to-world-sk
fetched_at: '2026-05-16T11:25:14.333387'
original_url: https://github.com/neilsonnn/image-blaster
date: '2026-05-15'
description: An image-to-world skillset for Claude. Contribute to neilsonnn/image-blaster development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

neilsonnn

 

/

image-blaster

Public

* NotificationsYou must be signed in to change notification settings
* Fork221
* Star2.4k

 
 
 
 
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

72 Commits
72 Commits
.claude
.claude
 
 
.cursor/
rules
.cursor/
rules
 
 
app
app
 
 
input
input
 
 
worlds
worlds
 
 
.claudeignore
.claudeignore
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CLAUDE.md
CLAUDE.md
 
 
LICENSE.md
LICENSE.md
 
 
README.md
README.md
 
 
bun.lock
bun.lock
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

## image-blaster

Creates 3D environments, SFX, and meshes from a single image using Claude skills, World Labs, and FAL.

Can take you from an image to a fully meshed 3D environment in < 5 minutes, great for jumpstarting 3D work. Go full blast.

## Quickstart

1. Open a Terminal, entergit clone https://github.com/neilsonnn/image-blaster
2. Enter the directory withcd image-blaster
3. Runclaude(install withcurl -fsSL https://claude.ai/install.sh | bash)
4. Say hello to Claude, and give them your API key forWorld LabsandFAL.
5. Put an image intoinput/directory and ask Claude toblast it and confirm each step with me.

### Description

By defaultimage-blasterwill use your input image to create:

1. 3D models (.glb,.obj) of alldynamicobjects
2. Gaussian splat (.spz) of thestaticenvironment,
3. Ambient looping sound and object specific physics SFX (.mp3)

### Extensions

You can embedimage-blasterunder the assets ofany game engine, DCC software, or web app.

1. Unity, Unreal, or Godot game engine
2. Blender, 3DS Max, or Maya or other DCC software
3. Three.js web app or Electron app

## Advanced

IMAGE-BLASTER uses a few generation models:

* marble-1.1- World Labs Marble model creates the explorable environment.
* nano-banana- default image edit preference for source cleanup, clean plates, and object reference images.
* gpt-image-2- alternate image edit provider when the edit skill is asked to prefer it.
* hunyuan-3d- Hunyuan 3D model creates 3D object models through FAL.
* elevenlabs-sfx- ElevenLabs sound effects model creates ambient and object-specific sounds.

3D model creation supports these Hunyuan parameters:

* --face-count <40000-1500000>: target face count. IMAGE-BLASTER defaults to50000; Hunyuan's API default is500000.
* --enable-pbr true|false: enable PBR material generation. Defaults totrue.
* --generate-type Normal|LowPoly|Geometry:Normalcreates a textured model,LowPolyapplies polygon reduction, andGeometrycreates a white geometry-only model. Defaults toNormal.
* --polygon-type triangle|quadrilateral: polygon type forLowPoly. Defaults totriangle.

### Examples

* Video game level concepts?IMAGE-BLASTit.
* Your childhood bedroom?IMAGE-BLASTit.
* Need an environment for a robot?IMAGE-BLASTit.
* A film location scout?IMAGE-BLASTit.
* An architectural rendering?IMAGE-BLASTit.

### Development

* remove/appfrom the.claudeignorefile to give Claude the ability to change the React viewer.

## About

An image-to-world skillset for Claude.

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

2.4k

 stars
 

### Watchers

28

 watching
 

### Forks

221

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

* TypeScript71.5%
* JavaScript27.5%
* Other1.0%