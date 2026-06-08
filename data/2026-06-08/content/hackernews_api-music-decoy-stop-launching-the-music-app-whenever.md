---
title: Music Decoy - Stop launching the Music app whenever you press ▶ Play
url: https://lowtechguys.com/musicdecoy/
site_name: hackernews_api
content_file: hackernews_api-music-decoy-stop-launching-the-music-app-whenever
fetched_at: '2026-06-08T19:46:05.889899'
original_url: https://lowtechguys.com/musicdecoy/
author: bobbiechen
date: '2026-06-08'
description: Stop launching the Music app whenever you press ▶ Play
tags:
- hackernews
- trending
---

# Music Decoy

##### Stop launching theMusicapp

##### whenever you press▶ Play

Download
View Source
$
brew install music-decoy

# Stop the Music app from launching

As long as the Music Decoy app is running, the system Music app won't launch when you accidentally press 
▶ Play
.
The app does 
absolutely no work
 in the background. It works by simply existing as a running process, thanks to having the same bundle identifier as the Music app.

#### How it works?

By having the bundle identifier 
com.apple.Music
, the app makes the system think that the Music app is already running.

## Configuration

Sincev1.1you can configure Music Decoy to launch another app when the▷ Playbutton is pressed.

To do that, run the following command in the Terminal(example for Spotify):

defaults
 
write
 
com
.
lowtechguys
.
MusicDecoy
 
mediaAppPath
 
/Applications/
Spotify
.
app

To reset the configuration, run:

defaults
 
delete
 
com
.
lowtechguys
.
MusicDecoy
 
mediaAppPath

## When does Music launch itself?

* When you press the ▶ Play key on your keyboard and there is no other app playing audio
* When a bluetooth headset connects and sends a play command
* When ending a call, which causes the bluetooth headset to switch from call mode to music mode

## Why does this happen?

There is a daemon calledrcd(short for Remote Control Daemon)that is responsible for handling media keys.

When a play event occurs, rcd checks if there is an app that is currently playing audio. If there is, it sends the play command to that app. If there isn't, it launches the system Music app.

There is a way to disable that daemon but it also disables the ability to control media playback with the keyboard.

## Alternatives

Based onthis StackExchange answer, there are a few different ways to achieve the same effect:

launchctl unload -w /System/Library/LaunchAgents/com.apple.rcd.plist

Problem:disables the Play button completely

noTuneswhich listens for launched apps and kills Music as soon as it is launched

Problem:it does use a tiny bit of CPU in the backgroundalthough checking for launched apps is very little work

## Uh.. how do I quit this app?

The app has no Dock icon and no menubar icon so to quit it you'd need to doone of the following:

* LaunchActivity Monitor, findMusic Decoyand press the ❌ button at the top
* Run the following command in the Terminal:killall 'Music Decoy'