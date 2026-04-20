---
title: 'GitHub - fabienmillet/WiiFin: Jellyfin Client for Wii · GitHub'
url: https://github.com/fabienmillet/WiiFin
site_name: hnrss
content_file: hnrss-github-fabienmilletwiifin-jellyfin-client-for-wii
fetched_at: '2026-04-14T11:57:27.761986'
original_url: https://github.com/fabienmillet/WiiFin
date: '2026-04-13'
description: Jellyfin Client for Wii. Contribute to fabienmillet/WiiFin development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

fabienmillet



/

WiiFin

Public

* NotificationsYou must be signed in to change notification settings
* Fork0
* Star130




 
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

51 Commits
51 Commits
.github/
ISSUE_TEMPLATE
.github/
ISSUE_TEMPLATE
 
 
README
README
 
 
apps/
WiiFin
apps/
WiiFin
 
 
assets
assets
 
 
data
data
 
 
libs
libs
 
 
source
source
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
MPLAYER_CE_BUILD.md
MPLAYER_CE_BUILD.md
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
build.sh
build.sh
 
 
View all files

## Repository files navigation

Jellyfin client for the Nintendo Wii

  


  


  


  


WiiFinis an experimental homebrew client forJellyfin, built specifically for the Nintendo Wii.
It provides a lightweight, console-friendly media browsing and playback experience, written in C++ usingGRRLIBandMPlayer CE.

## ⚠️Project Status

🚧Experimental– functional but still under active development. Expect rough edges on real hardware.

### ✅ What works:

* Authentication: login with username/password or viaQuickConnect(approve on another device)
* Saved profiles: multiple accounts stored securely (access token only, no password stored)
* Library browsing: movies, TV shows, music libraries with cover art loaded from the server
* Detail view: synopsis, rating, genres, cast, director, audio/subtitle track selection
* Continue WatchingandNext Uprows
* TV shows: season and episode navigation
* Video playback: server-side transcoding streamed through the integrated MPlayer CE engine
* Music playback: audio libraries, album/track navigation
* Player overlay: seek bar, volume control, next/prev episode, audio & subtitle track switching, intro skip
* Playback reporting: progress sent back to the Jellyfin server (resume where you left off)
* HTTPS: TLS connections via mbedTLS (self-signed certificates supported)
* Wiimote IR pointerandvirtual on-screen keyboard
* Background musicon menus
* Ships as a ready-to-use.doland installable.wad(Wii / vWii)

### ⚠️Known limitations:

* Direct-play is not supported; all video is transcoded by the server
* No 5.1 multi-channel audio (stereo only via transcoding)
* Subtitle rendering relies on the server embedding them into the video stream

## 🔧 Build Instructions

### Requirements:

* devkitProwithdevkitPPC,libogc, andwii-devportlibs
* Graphics:GRRLIB,libpngu,freetype,libjpeg
* mbedTLS (bundled underlibs/, cross-compiled automatically by the CI)
* Optional: MPlayer CE compiled aslibmplayer.a— required for video playback. SeeMPLAYER_CE_BUILD.mdfor instructions. Without it, WiiFin still compiles but video playback is unavailable.

### Building:

./build.sh

### Running:

OnDolphin Emulator:

dolphin-emu -e WiiFin.dol

Onreal Wii hardware: copyWiiFin.doltoSD:/apps/WiiFin/boot.dol, or installWiiFin.wadusing a WAD manager (works on vWii too).

## 📁 Project Structure

WiiFin/
├── source/
│ ├── core/ # App lifecycle, background music, utilities
│ ├── input/ # Wiimote + USB keyboard input
│ ├── jellyfin/ # Jellyfin HTTP API client (HTTPS via mbedTLS)
│ ├── player/ # MPlayer CE integration, player overlay HUD
│ └── ui/ # All views: Connect, Library, Profile, Settings
├── data/ # PNG/TTF graphical assets
├── libs/ # Bundled mbedTLS
├── tools/ # WAD packager, banner generator
├── Makefile # devkitPro-compatible build script
└── apps/WiiFin/ # Homebrew Channel metadata

## 🚀 Roadmap

* Sort/filter items (by year, genre, rating)
* Mark items as favorites from the Wii
* Multiple UI color themes

## 📸 Screenshots

WiiFin running in Dolphin Emulator

## 🤝 Contributing

WiiFin is open to pull requests, bug reports, and suggestions.

* 📘 Read thecontribution guidelines
* 🐛 Use thebug report template
* 💡 Got a feature idea? Use thefeature request template

## 📜 License

This project is licensed under theGPLv3.
See theLICENSEfile for more details.

## About

Jellyfin Client for Wii

wiifin.zipna.me/

### Resources

 Readme



### License

 GPL-3.0 license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

130

 stars


### Watchers

1

 watching


### Forks

0

 forks


 Report repository



## Releases2

v0.1.1

 Latest



Apr 12, 2026



+ 1 release

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* C78.2%
* C++21.2%
* Other0.6%
