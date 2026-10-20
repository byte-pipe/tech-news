---
title: An ad-free Android TV — Cretezy
url: https://cretezy.com/2026/ad-free-android-tv
site_name: hackernews_api
content_file: hackernews_api-an-ad-free-android-tv-cretezy
fetched_at: '2026-10-20T22:05:13.428331'
original_url: https://cretezy.com/2026/ad-free-android-tv
author: CraftThatBlock
date: '2026-10-19'
description: Android TV is full of ads, even in apps-only mode. Here's how I replaced the launcher, YouTube, and the remote's buttons to get rid of them.
tags:
- hackernews
- trending
---

Oct 19, 2026 
 
Tutorial
Android
 
 

# An ad-free Android TV

 
 

I like Android TV. It runs every app I care about, it’s cheap on aChromecast, and it’s built into plenty of TVs. What I don’t like is ads. Here’s my setup for ad-free watching on my devices.

Google TV, the default interface on most Android TV devices, puts a large banner at the top of the home screen promoting whatever Google wants you to watch next, often from apps you don’t even use.Apps only modeis supposed to strip the home screen down to your apps, but the banner stays, and there’s no setting to turn it off.

Before: Google TV, in Apps only mode

After setting up a few devices around the house, I landed on a setup with no ads at all, and a nicer interface to go with it.

## The setup

* Projectivy Launcherreplaces the home screen. It shows your apps and nothing else, and it’s very customizable.FLauncherandATV Launcher Proare good alternatives.
* SmartTubereplaces YouTube, with no ads, a better interface, andSponsorBlockbuilt in. I still pay for YouTube Premium to support creators, but I vastly prefer SmartTube to the official app.
* Wholphinis my preferredJellyfinclient, for its UI and customization options.Moonfinis a good alternative.
* Button Mapperremaps the remote, so the YouTube button opens SmartTube.

After: Projectivy Launcher

SmartTube, blurred

I’ve set this up on two Chromecasts with Google TV and a Hisense TV, and it should work on most Android TV devices.

Tip:For ads in other apps, and the TV’s own tracking, also runPi-holeon your network. It blocks ad and tracking domains at the DNS level, for every device in the house, not just the TV.

If you’d rather keep the stock launcher, blockingandroidtvwatsonfe-pa.googleapis.comin Pi-hole (or your router’s DNS) reportedly hides its banner. You might have to restart the device or clear the launcher’s cache for it to take effect.

Without Pi-hole, you can point the TV’s Private DNS at an ad-blocking resolver likeAdGuard DNSinstead, once ADB is connected (see below):

adb
 -s
 $D 
shell
 settings
 put
 global
 private_dns_mode
 hostname

adb
 -s
 $D 
shell
 settings
 put
 global
 private_dns_specifier
 dns.adguard-dns.com

## Tutorial

Tip:Hand this article to an AI agent and have it guide you through the setup. It can adapt the ADB commands to your device and run them for you, so review each one before approving it.

Everything here is done withADB, so start by connecting it.

### Connecting ADB

Enable Developer options by clickingSettings → System → About → Android TV OS build7 times. Then, inDeveloper options, enableWireless debuggingand choosePair device with pairing code:

adb
 pair
 <
i
p
>
:
<
pairing-por
t
>
 <
cod
e
>

adb
 mdns
 services
 # Find the connect port

adb
 connect
 <
i
p
>
:
<
connect-por
t
>

D
=<
ip
>
:
<
connect-port
>
 # Used in the commands below

Wireless debugging only works over Wi-Fi. If your device doesn’t have it (like my Hisense TV), enableUSB debugginginstead and connect withadb connect <ip>:5555.

### Installing the apps

Projectivy, Wholphin, and Button Mapper are on the Play Store. ADB can’t install from the Play Store directly, but it can open each app’s page on the TV, so you just clickInstall:

for
 p 
in
 com.spocky.projengmenu
 com.github.damontecres.wholphin
 flar2.homebutton
; 
do

 adb
 -s
 $D 
shell
 am
 start
 -a
 android.intent.action.VIEW
 -d
 "market://details?id=
$p
"

 read
 -p
 "Press Enter once it's installed..."

done

SmartTube isn’t on the Play Store, so download the latest APK from GitHub and install it:

curl
 -L
 -o
 smarttube.apk
 "$(
curl
 -s
 https://api.github.com/repos/yuliskov/SmartTube/releases/latest 
\

 |
 grep
 -o
 '"browser_download_url": *"[^"]*_universal\.apk"' 
|
 cut
 -d
'"' 
-f4
)"

adb
 -s
 $D 
install
 smarttube.apk

You can also sideload it on the TV withDownloader.

### Replacing the launcher

Projectivy has anOverride current launcheroption, but the stock home screen still flashes before it. Instead, set Projectivy as the home app, then disable the stock launcher and the package that restores it:

adb
 -s
 $D 
shell
 cmd
 package
 set-home-activity
 com.spocky.projengmenu/.ui.home.MainActivity

adb
 -s
 $D 
shell
 pm
 disable-user
 --user
 0
 com.google.android.apps.tv.launcherx

adb
 -s
 $D 
shell
 pm
 disable-user
 --user
 0
 com.google.android.tungsten.setupwraith

Setting the home app first matters. On some devices, disablingsetupwraithcan also forget the saved Wi-Fi network, so keep a remote handy to reconnect.

On a TV, the stock launcher may also handle switching HDMI inputs, so check that still works afterward.

### Replacing YouTube

Once SmartTube is set up, remove the official app:

adb
 -s
 $D 
uninstall
 com.google.android.youtube.tv

If it’s built into the firmware (DELETE_FAILED_INTERNAL_ERROR), useadb -s $D shell pm uninstall --user 0 com.google.android.youtube.tvinstead.

### Remapping the remote

Button Mapper and Projectivy both need their accessibility services enabled. This replaces the whole list, so check the current one first withadb -s $D shell settings get secure enabled_accessibility_servicesand keep anything else you use:

adb
 -s
 $D 
shell
 settings
 put
 secure
 enabled_accessibility_services
 \

 'flar2.homebutton/a.i:com.spocky.projengmenu/com.spocky.projengmenu.services.ProjectivyAccessibilityService'

adb
 -s
 $D 
shell
 settings
 put
 secure
 accessibility_enabled
 1

Android sometimes turns accessibility services off. Granting Button MapperWRITE_SECURE_SETTINGSlets it turn itself back on, and exempting it from battery optimization keeps it responsive:

adb
 -s
 $D 
shell
 pm
 grant
 flar2.homebutton
 android.permission.WRITE_SECURE_SETTINGS

adb
 -s
 $D 
shell
 dumpsys
 deviceidle
 whitelist
 +flar2.homebutton

Then, in Button Mapper, map the YouTube button to SmartTube.

### Cleaning up

You can also speed up animations to make it snappier:

for
 k 
in
 window_animation_scale
 transition_animation_scale
 animator_duration_scale
; 
do

 adb
 -s
 $D 
shell
 settings
 put
 global
 $k 
0.75

done

And disable some Google apps and services you probably won’t use. Skip any you do use, and ignore errors for packages your device doesn’t have:

for
 p 
in
 com.google.android.videos
 \

 com.google.android.play.games
 \

 com.google.android.youtube.tvmusic
 \

 com.google.android.tvrecommendations
 \

 com.google.android.feedback
 \

 com.google.android.partnersetup
; 
do

 adb
 -s
 $D 
shell
 pm
 disable-user
 --user
 0
 $p

done

For additional debloating,cleanyourtvhaslists for many TVs, covering manufacturer apps, ad services, and telemetry.

Everything can be undone withadb shell pm enable <package>(oradb shell cmd package install-existing <package>for YouTube). Turn Wireless debugging (or USB debugging) off when you’re done, since an open ADB port can let other devices on your network connect.

On a TV, also check the picture settings. Switch toFilmmaker Mode(or a neutral mode likeMovieorCinema) and turn off most of the image processing, like motion smoothing, noise reduction, and dynamic contrast. You might have to tweak it a bit to suit your room and taste.

That’s it: no banner, no ads, and a remote that opens the apps you actually use.

Update 2026-10-20: Thank you for the replies onHacker News! I’ve made some changes:

* Added Pi-hole and Private DNS as a way to block ads across the network, including the stock launcher’s banner
* Linkedcleanyourtvfor additional debloating
* Added FLauncher and ATV Launcher Pro as launcher alternatives, and Moonfin as a Jellyfin client alternative

 
 
 
 
 
 
 

### Who am I?

 

Hello! My name is Cretezy and I am a software developer. I write about programming, personal
 projects, and more.

 
 See more posts here.