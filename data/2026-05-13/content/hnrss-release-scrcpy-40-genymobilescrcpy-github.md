---
title: Release scrcpy 4.0 · Genymobile/scrcpy · GitHub
url: https://github.com/Genymobile/scrcpy/releases/tag/v4.0
site_name: hnrss
content_file: hnrss-release-scrcpy-40-genymobilescrcpy-github
fetched_at: '2026-05-13T11:46:28.604584'
original_url: https://github.com/Genymobile/scrcpy/releases/tag/v4.0
date: '2026-05-12'
description: Display and control your Android device. Contribute to Genymobile/scrcpy development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

Genymobile

 

/

scrcpy

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork13k
* Star140k

 

# scrcpy 4.0

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

 

rom1v

 released this

 

 12 May 19:47
 

 v4.0
 

 

2322868

To receive a notification when a new release is available, click onWatch > Custom > Releasesat the top.

scrcpy v4.0

Changes since v3.3.4:

* Migrate from SDL2 to SDL3 (#6216)
* Add flex display support (#6772)
* Add camera torch and zoom support (#6243)
* Enforce window aspect ratio (#6761,#6774,#2317,#2387,#3460)
* Add --keep-active (#6792,#6787)
* Add --background-color (#6807,#5855)
* Set default background color to dark gray (#6807)
* Display disconnected icon before closing (#6662,#6651)
* Add F11 as fullscreen shortcut (#6777)
* Add Mod+q shortcut to quit (#6780,#6612)
* Fix Meta Quest flickering (#5913)
* Fix physical vs logical size confusion (#6772)
* Fix copy-paste on rooted device (#6224)
* Fix colorspace conversion issue (#1868)
* Fix high CPU usage with audio silence decoded from OPUS (#6715)
* Add session metadata for the video stream (#6159)
* Respect video capabilities constraints (#6766)
* Set Windows console code page to UTF-8 (#6663)
* Fix support for device serial containing spaces (#6663,#6664,#3537)
* Detect TCP devices provided by mDNS (#6665,#6248)
* Keep Windows terminal open on error (#6667)
* Set MediaCodec KEY_PRIORITY and KEY_LATENCY to minimum values (#6670)
* Open the scrcpy window earlier (#6694,#6546)
* Fix device rotation shortcut (5fedc79)
* Use optimal size alignment (#6746,#4949,#6236)
* Add --min-size-alignment (#6746)
* Fix screensaver disabled unexpectedly without video playback (#6754)
* Add --no-window-aspect-ratio-lock (#6761)
* Fix rotation of square displays (#6770)
* Align the virtual display size (#6771)
* Add --render-fit (#6772)
* Set default audio-output-buffer to 10ms (#6775,#3793)
* Fix turning virtual display on via right-click (#6788)
* Fix OpenGL runner shutdown deadlock (#6794)
* Share SDL hints between normal and OTG modes (#6809,#6808)
* Upgrade platform-tools (adb) to 37.0.0
* Upgrade FFmpeg to 8.1.1 (#6715)
* Upgrade SDL to 3.4.8
* Upgrade dav1d to 1.5.3
* Various technical fixes

# Highlights

## SDL3

This release migrates from SDL2 to SDL3 to benefit from active maintenance, bug fixes, and continued upstream support. SDL3 also enables new features, such as aspect-ratio locking when resizing the window.

Thanks to the SDL maintainers for their work and for theirsupport and fixes!

See#6216for details.

## Flex display

A virtual display can now be madeflexusing--flex-display(or-x), meaning it can be resized dynamically along with the client window.

Here is a demo:

scrcpy --new-display=/192 -x --start-app=org.mozilla.firefox --keep-active --no-vd-system-decorations

scrcpy-flex-display-2.mp4

Here are more examples:

#
 Start Android Settings in a window

scrcpy --new-display=1024x768/160 --start-app=com.android.settings --flex-display

#
 -x is equivalent to --flex-display

scrcpy --new-display=1024x768/160 --start-app=com.android.settings -x

#
 By default, the display size/dpi is 1280x960/160

scrcpy --new-display --start-app=com.android.settings --flex-display

Use--keep-activeto prevent the screen from turning off (see below):

scrcpy --new-display -x --keep-active

Increase the bit rate and/or change the codec to maintain good quality even with large windows:

scrcpy --new-display -x --video-codec=h265 -b16M

See#6772for more details.

## Camera torch and zoom

The camera can be controlled dynamically:

* MOD+t: turn on the camera torch
* MOD+Shift+t: turn off the camera torch
* MOD+↑(up): zoom in
* MOD+↓(down): zoom out

The camera torch can also be turned on at startup by--camera-torch:

scrcpy --video-source=camera --camera-torch

The camera zoom level can be set with--camera-zoom:

scrcpy --video-source=camera --camera-zoom=1.5

The supported zoom range for each camera is given by--list-cameras(any value outside the supported range will be clamped).

## Aspect ratio

Previously, the window could be freely resized, and black borders were added to maintain the content aspect ratio.

Thanks to a new API in SDL3, the window aspect ratio is now preserved while resizing, avoiding black borders.

The old behavior can be restored using--no-window-aspect-ratio-lock.

## Keep active

To prevent the device from turning off due to inactivity,--keep-activeperiodically signals user activity to the system:

scrcpy --keep-active

Contrary to--stay-awakeand--screen-off-timeout, this does not change any global settings, and it works whether the device is plugged in or not.

## Background color

The default background was pure black; it is now dark gray.

It can be changed with--background-color, which accepts hexadecimal color codes (in 3-digit or 6-digit format):

scrcpy --background-color=
#
234567

scrcpy --background-color=234567 
#
 leading '#' is optional

scrcpy --background-color=
#
567 # equivalent to #556677

## Disconnected icon

When the connection to the device is lost while mirroring, the window previously closed immediately, which could incorrectly suggest that scrcpy had crashed.

To make disconnections clearer, a disconnected icon is now displayed for 2 seconds before closing the window.

The icon replaces the screen content immediately:

More details in#6662.

## Meta Quest

Since a Meta Quest firmware upgrade, flickering occurred when mirroring the screen with scrcpy.

A workaround was implemented, so mirroring a Meta Quest now works again.

See the technical details in#5913 (comment).

## High CPU usage with silence

A funny bug: playing silence used much more CPU than playing non-silence, during resampling of audio samples decoded from an OPUS audio stream (resampling was about 40× slower).

It turns out it was caused bydenormals: the OPUS decoder did not produce exactzeros, but tiny denormal numbers, which can causeperformance issues.

This was fixed directly in FFmpeg:#6715 (comment)

## More shortcuts

F11now toggles fullscreen (likeMOD+f), andMOD+qnow quits scrcpy.

* BlueSky:@scrcpy.bsky.social
* Twitter:@scrcpy_app
* Reddit:r/scrcpy

 

Assets

10

 

 
Loading

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
👍

84

 
agsola, kamilmirza, Tech-Tac, Anonym777, hoehermann, smarlhens, MasterAlive, ryand56, JosefFStraka, Jalkhov, and 74 more reacted with thumbs up emoji

 
😄

13

 
Tech-Tac, aman-senpai, SenseiDeElite, finn-braun, looser71, lin72h, drauggres, LinuxOpa, dec, vietnguyenhoangw, and 3 more reacted with laugh emoji

 
🎉

47

 
agsola, henriqueffc, shripal17, Tech-Tac, immohammeeed, Jalkhov, aman-senpai, Solcosm, reallybigmess, Rexogamer, and 37 more reacted with hooray emoji

 
❤️

53

 
agsola, ZG089, roirraWedorehT, welson-rodrigues, Tech-Tac, StevenSYS, cook343, MasterAlive, JosefFStraka, Jalkhov, and 43 more reacted with heart emoji

 
🚀

30

 
Tech-Tac, K3V1991, Jalkhov, aman-senpai, SenseiDeElite, finn-braun, looser71, TzurSoffer, kmayoral, lin72h, and 20 more reacted with rocket emoji

 
👀

18

 
Tech-Tac, jumpingbrowntrout, Jalkhov, aman-senpai, SenseiDeElite, finn-braun, looser71, TzurSoffer, Kenfong0103, LinuxOpa, and 8 more reacted with eyes emoji

 

All reactions

 
121 people reacted