---
title: 'GitHub - matthartman/ghost-pepper: Hold-to-talk speech-to-text for macOS. 100% local, powered by WhisperKit and local LLM cleanup. Hold Control to record, release to transcribe and paste. · GitHub'
url: https://github.com/matthartman/ghost-pepper
site_name: hnrss
content_file: hnrss-github-matthartmanghost-pepper-hold-to-talk-speech
fetched_at: '2026-04-07T11:23:35.811018'
original_url: https://github.com/matthartman/ghost-pepper
date: '2026-04-06'
description: Hold-to-talk speech-to-text for macOS. 100% local, powered by WhisperKit and local LLM cleanup. Hold Control to record, release to transcribe and paste. - matthartman/ghost-pepper
tags:
- hackernews
- hnrss
---

matthartman



/

ghost-pepper

Public

* NotificationsYou must be signed in to change notification settings
* Fork46
* Star1.1k




 
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

240 Commits
240 Commits
CleanupModelProbe
CleanupModelProbe
 
 
CleanupModelProbeSupport
CleanupModelProbeSupport
 
 
GhostPepper.xcodeproj
GhostPepper.xcodeproj
 
 
GhostPepper
GhostPepper
 
 
GhostPepperTests
GhostPepperTests
 
 
docs
docs
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
README.md
README.md
 
 
app-icon.png
app-icon.png
 
 
appcast.xml
appcast.xml
 
 
project.yml
project.yml
 
 
View all files

## Repository files navigation

# Ghost Pepper

100% localhold-to-talk speech-to-text for macOS. Hold Control to record, release to transcribe and paste. No cloud APIs, no data leaves your machine.

Download the latest release— macOS 14.0+, Apple Silicon (M1+)

## Features

* Hold Control to talk— release to transcribe and paste into any text field
* Runs entirely on your Mac— models run locally via Apple Silicon, nothing is sent anywhere
* Smart cleanup— local LLM removes filler words and handles self-corrections
* Menu bar app— lives in your menu bar, no dock icon, launches at login
* Customizable— edit the cleanup prompt, pick your mic, toggle features on/off

## How it works

Ghost Pepper uses open-source models that run entirely on your Mac. Models download automatically and are cached locally.

### Speech models

Model

Size

Best for

Whisper tiny.en

~75 MB

Fastest, English only

Whisper small.en
 (default)

~466 MB

Best accuracy, English only

Whisper small (multilingual)

~466 MB

Multi-language support

Parakeet v3 (25 languages)

~1.4 GB

Multi-language via
FluidAudio

### Cleanup models

Model

Size

Speed

Qwen 3.5 0.8B
 (default)

~535 MB

Very fast (~1-2s)

Qwen 3.5 2B

~1.3 GB

Fast (~4-5s)

Qwen 3.5 4B

~2.8 GB

Full quality (~5-7s)

Speech models powered byWhisperKit. Cleanup models powered byLLM.swift. All models served byHugging Face.

## Getting started

Download the app:

1. DownloadGhostPepper.dmg
2. Open the DMG, drag Ghost Pepper to Applications
3. Grant Microphone and Accessibility permissions when prompted
4. Hold Control and speak

Build from source:

1. Clone the repo
2. OpenGhostPepper.xcodeprojin Xcode
3. Build and run (Cmd+R)

## Permissions

Permission

Why

Microphone

Record your voice

Accessibility

Global hotkey and paste via simulated keystrokes

## Good to know

* Launch at loginis enabled by default on first run. You can toggle it off in Settings.
* No logging to disk— transcriptions are never written to files. Debug logs are in-memory only and disappear when the app quits.

## Acknowledgments

Built withWhisperKit,LLM.swift,Hugging Face, andSparkle.

## License

MIT

## Why "Ghost Pepper"?

All models run locally, no private data leaves your computer. And it's spicy to offer something for free that other apps have raised $80M to build.

## Enterprise / managed devices

Ghost Pepper requires Accessibility permission, which normally needs admin access to grant. On managed devices, IT admins can pre-approve this via an MDM profile (Jamf, Kandji, Mosaic, etc.) using a Privacy Preferences Policy Control (PPPC) payload:

Field

Value

Bundle ID

com.github.matthartman.ghostpepper

Team ID

BBVMGXR9AY

Permission

Accessibility (
com.apple.security.accessibility
)

## About

Hold-to-talk speech-to-text for macOS. 100% local, powered by WhisperKit and local LLM cleanup. Hold Control to record, release to transcribe and paste.

### Resources

 Readme



### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

1.1k

 stars


### Watchers

3

 watching


### Forks

46

 forks


 Report repository



## Releases12

Ghost Pepper v2.0.1 🌶️

 Latest



Apr 6, 2026



+ 11 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors4

* matthartmanMatt Hartman
* claudeClaude
* obraJesse Vincent
* ttulttulKen Simpson

## Languages

* Swift99.1%
* Shell0.9%
