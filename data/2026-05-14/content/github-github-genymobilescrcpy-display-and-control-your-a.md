---
title: 'GitHub - Genymobile/scrcpy: Display and control your Android device · GitHub'
url: https://github.com/Genymobile/scrcpy
site_name: github
content_file: github-github-genymobilescrcpy-display-and-control-your-a
fetched_at: '2026-05-14T11:37:00.716415'
original_url: https://github.com/Genymobile/scrcpy
author: Genymobile
description: Display and control your Android device. Contribute to Genymobile/scrcpy development by creating an account on GitHub.
---

Genymobile

 

/

scrcpy

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork13k
* Star141k

 
 
 
 
master
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

3,097 Commits
3,097 Commits
.github
.github
 
 
app
app
 
 
assets
assets
 
 
config
config
 
 
doc
doc
 
 
gradle/
wrapper
gradle/
wrapper
 
 
release
release
 
 
server
server
 
 
.gitignore
.gitignore
 
 
FAQ.md
FAQ.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build.gradle
build.gradle
 
 
bump_version
bump_version
 
 
cross_win32.txt
cross_win32.txt
 
 
cross_win64.txt
cross_win64.txt
 
 
gradle.properties
gradle.properties
 
 
gradlew
gradlew
 
 
gradlew.bat
gradlew.bat
 
 
install_release.sh
install_release.sh
 
 
meson.build
meson.build
 
 
meson_options.txt
meson_options.txt
 
 
run
run
 
 
settings.gradle
settings.gradle
 
 
View all files

## Repository files navigation

This GitHub repo (https://github.com/Genymobile/scrcpy) is the only official
source for the project. Do not download releases from random websites, even if
their name containsscrcpy.

# scrcpy (v4.0)

pronounced "screencopy"

This application mirrors Android devices (video and audio) connected via USB orTCP/IPand allows control using the
computer's keyboard and mouse. It does not requirerootaccess or an app
installed on the device. It works onLinux,Windows, andmacOS.

 

 

 

It focuses on:

* lightness: native, displays only the device screen
* performance: 30~120fps, depending on the device
* quality: 1920×1080 or above
* low latency:35~70ms
* low startup time: ~1 second to display the first image
* non-intrusiveness: nothing is left installed on the Android device
* user benefits: no account, no ads, no internet required
* freedom: free and open source software

Its features include:

* audio forwarding(Android 11+)
* recording
* virtual display
* mirroring withAndroid device screen off
* copy-pastein both directions
* configurable quality
* camera mirroring(Android 12+)
* mirroring as a webcam (V4L2)(Linux-only)
* physicalkeyboardandmousesimulation (HID)
* gamepadsupport
* OTG mode
* and more…

## Prerequisites

The Android device requires at least API 21 (Android 5.0).

Audio forwardingis supported for API >= 30 (Android 11+).

Make sure youenabled USB debuggingon your device(s).

On some devices (especially Xiaomi), you might get the following error:

Injecting input events requires the caller (or the source of the instrumentation, if any) to have the INJECT_EVENTS permission.

In that case, you need to enablean additional optionUSB debugging (Security Settings)(this is an item different fromUSB debugging) to control
it using a keyboard and mouse. Rebooting the device is necessary once this
option is set.

Note that USB debugging is not required to run scrcpy inOTG mode.

## Get the app

* Linux
* Windows(readhow to run)
* macOS

## Must-know tips

* Reducing resolutionmay greatly improve performance
(scrcpy -m1024)
* Right-clicktriggersBACK
* Middle-clicktriggersHOME
* Alt+ftogglesfullscreen
* There are many othershortcuts

## Usage examples

There are a lot of options,documentedin separate pages.
Here are just some common examples.

* Capture the screen in H.265 (better quality), limit the size to 1920, limit
the frame rate to 60fps, disable audio, and control the device by simulating
a physical keyboard:scrcpy --video-codec=h265 --max-size=1920 --max-fps=60 --no-audio --keyboard=uhid
scrcpy --video-codec=h265 -m1920 --max-fps=60 --no-audio -K#short version
* Start VLC in a new virtual display (separate from the device display):scrcpy --new-display=1920x1080 --start-app=org.videolan.vlc
* Start VLC in a newflexdisplay using H.265 with a bitrate of 16 Mbps,
while keeping the display active so it does not turn off:scrcpy --new-display -x --keep-active --start-app=org.videolan.vlc --video-codec=h265 -b16M
* Record the device camera in H.265 at 1920x1080 (and microphone) to an MP4
file:scrcpy --video-source=camera --video-codec=h265 --camera-size=1920x1080 --record=file.mp4
* Capture the device front camera and expose it as a webcam on the computer (on
Linux):scrcpy --video-source=camera --camera-size=1920x1080 --camera-facing=front --v4l2-sink=/dev/video2 --no-playback
* Control the device without mirroring by simulating a physical keyboard and
mouse (USB debugging not required):scrcpy --otg
* Control the device using gamepads plugged into the computer:scrcpy --gamepad=uhid
scrcpy -G#short version

## User documentation

The application provides a lot of features and configuration options. They are
documented in the following pages:

* Connection
* Video
* Audio
* Control
* Keyboard
* Mouse
* Gamepad
* Device
* Window
* Recording
* Virtual display
* Tunnels
* OTG
* Camera
* Video4Linux
* Shortcuts

## Resources

* FAQ
* Translations(not necessarily up to date)
* Build instructions
* Developers
* Verify release signatures

## Articles

* Introducing scrcpy
* Scrcpy now works wirelessly
* Scrcpy 2.0, with audio

## Contact

You can open anissuefor bug reports, feature requests or general questions.

For bug reports, please read theFAQfirst, you might find a solution
to your problem immediately.

You can also use:

* Reddit:r/scrcpy
* BlueSky:@scrcpy.bsky.social
* Twitter:@scrcpy_app

## Donate

I'm@rom1v, the author and maintainer ofscrcpy.

If you appreciate this application, you cansupport my open source
work:

* GitHub Sponsors
* Liberapay
* PayPal

## License

Copyright (C) 2018 Genymobile
Copyright (C) 2018-2026 Romain Vimont

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## About

Display and control your Android device

### Topics

 android

 c

 ffmpeg

 sdl2

 screen

 libav

 recording

 mirroring

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

141k

 stars
 

### Watchers

1.4k

 watching
 

### Forks

13k

 forks
 

 Report repository

 

## Releases51

scrcpy 4.0

 Latest

 

May 12, 2026

 

+ 50 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* liberapay.com/rom1v
* https://paypal.me/rom2v

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C63.1%
* Java32.7%
* Roff1.7%
* Shell1.6%
* Meson0.7%
* AIDL0.2%