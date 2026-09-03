---
title: Release Audacity-4.0.0 · audacity/audacity · GitHub
url: https://github.com/audacity/audacity/releases/tag/Audacity-4.0.0
site_name: hackernews_api
content_file: hackernews_api-release-audacity-400-audacityaudacity-github
fetched_at: '2026-09-03T14:53:10.356642'
original_url: https://github.com/audacity/audacity/releases/tag/Audacity-4.0.0
author: ClydeN
date: '2026-09-03'
description: Audio Editor . Contribute to audacity/audacity development by creating an account on GitHub.
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 audacity

 

/

audacity

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.6k
* Star17.8k

 

# Audacity-4.0.0

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

 

kryksyh

 released this

 

 03 Sep 10:19
 

 Audacity-4.0.0
 

4c177d4

## Audacity 4.0

Audacity 4 rebuilds the application interface on Qt and introduces many new quality-of-life improvements, including a new clip-editing model. Most Audacity 3 workflows remain available, but some controls have moved or changed.

### Watch the video:

## Editing clips

* Clips can be selected directly.Click a clip header to select it, or Shift-click to select multiple clips.
* Several clips can be edited together.Moving, trimming and time stretching apply to all selected clips.
* Clips can be grouped.Groups remain together when moved, copied, pasted or duplicated.
* Clips can be placed more freely.They can move between mono and stereo tracks. Moving a clip over another replaces the overlapped part instead of blocking the move.
* Splitting has a dedicated tool.Press or holdS, then click the waveform or clip header. Split, split-cut, split-delete, split at silences and split to a new track are also available as commands.
* Paste handles more cases automatically.Audacity can create a track when needed, adapt compatible channel layouts and paste audio files from the operating-system clipboard.
* Alignment guides, sample-boundary snapping and per-project snap settings have been added or expanded.

## Interface and tools

* The interface has been rebuilt onQt, with native high-DPI rendering.
* Toolbars and panels can be moved, docked, floated, shown or hidden.
* UI layouts can be saved asWorkspaces. Audacity includes Modern, Classic and Music workspaces.
* Light, dark and high-contrast themes are available, along with accent colors, track colors and several clip styles.
* The new Home screen shows recent projects with preview thumbnails.

The separate Select, Envelope, Draw and Multi-tool modes have been removed. Their functions are now context-sensitive:

* Volume envelopes are displayed in theClip gainmode.
* Sample drawing becomes available when the waveform is zoomed to individual samples.
* Splitting is available by holdingS.
* Track and effect parameters use consistent rotary controls with fine adjustment and double-click reset.
* Sync-Lock has been removed. Delete, cut and paste now have explicit variants for either leaving a gap or moving later material to preserve timing.

## Playback and recording

* The playhead remains visible during navigation and can be dragged to a new position.
* Playback can seek to another position without stopping.
* Recording can start anywhere on the timeline and creates a clip at that position.
* Loop boundaries and the interaction between playback, selections and loops have been revised.
* Punch and Roll, lead-in recording, latency compensation, software playthrough and per-track input monitoring have been rebuilt for the new interface.
* Audio Setup now includes system-default devices, refreshable device lists and custom channel mapping. Audacity can follow operating-system device changes automatically.
* Official Windows builds include ASIO playback and recording support.

## Tracks, meters and effects

* Track headers now contain live playback and recording meters.
* Preset handling is consistent across built-in, destructive and realtime effects.
* Built-in effects, generators and analyzers have been rebuilt for the Qt interface.
* Supported plugin formats are VST3, Nyquist, LV2 on Linux and Audio Units on macOS. Audacity can display generated controls when a plugin's own interface is unavailable.
* Spectrogram has been redesigned with clearer guides and rulers, and faster rendering.

## Projects, import and export

* Audacity 4 uses the new.aup4project format.
* .aup3projects open and convert to.aup4without changing the original file. Converted projects cannot be saved back to.aup3.
* Older.aupprojects can be imported.
* Project files store preview thumbnails and Audacity 4's additional clip and appearance data.

And last but not least, we had the audacity to change the Audacity logo.

## Compatibility notes

The following Audacity 3 features are not available in Audacity 4.0, but we're working on adding them in future releases.

* Time Tracks
* Note/MIDI tracks
* Mixer
* Macro Manager and the scripting pipe
* VAMP and LADSPA plugin hosting
* Play-at-speed

Sync-Lock and the old tool modes were replaced by the workflows described above.

Additionally, Audacity 4 ships with some missing exporting and rendering features, analyzers, and effects.

Update: audacity-sources-4.0.0.tar.xz was updated to include SoundTouch and sbsms 3rd-party libraries.

 

Assets

11

 

 
Loading

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
👍

77

 
kryksyh, 3Domse3, CamelT0E, christantoan, MarcoRavich, xplosionmind, binocry, projekter, Felitendo, Safari77, and 67 more reacted with thumbs up emoji

 
😄

13

 
kryksyh, deus-e-x, maxkorsov, sneak-o-matic, bancek, JaredTweed, Eism, FlurinBruehwiler, saintmatthieu, yuyake-litrain, and 3 more reacted with laugh emoji

 
🎉

62

 
kryksyh, 3Domse3, Felitendo, iv-m, victordiaz, Lauritz-Tieste, LetUsFlow, Gitoffthelawn, Tarek-Hasan, Pyrobrick, and 52 more reacted with hooray emoji

 
❤️

39

 
luapmartin, saintmatthieu, kryksyh, 3Domse3, CamelT0E, xplosionmind, Felitendo, Lauritz-Tieste, Gitoffthelawn, Tarek-Hasan, and 29 more reacted with heart emoji

 
🚀

30

 
kryksyh, Lauritz-Tieste, zerebos, Mateus109, Tarek-Hasan, Pyrobrick, maxkorsov, kohane27, berrutti, kevingroeger, and 20 more reacted with rocket emoji

 
👀

7

 
xplosionmind, Gopnk, maxkorsov, Eism, yuyake-litrain, xkef, and mrdeathjr28 reacted with eyes emoji

 

All reactions

 
138 people reacted

 6
 

 

Join discussion