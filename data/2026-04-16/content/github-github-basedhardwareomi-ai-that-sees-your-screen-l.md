---
title: 'GitHub - BasedHardware/omi: AI that sees your screen, listens to your conversations and tells you what to do · GitHub'
url: https://github.com/BasedHardware/omi
site_name: github
content_file: github-github-basedhardwareomi-ai-that-sees-your-screen-l
fetched_at: '2026-04-16T11:58:47.760782'
original_url: https://github.com/BasedHardware/omi
author: BasedHardware
description: AI that sees your screen, listens to your conversations and tells you what to do - BasedHardware/omi
---

BasedHardware

 

/

omi

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.6k
* Star8.7k

 
 
 
 
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

16,912 Commits
16,912 Commits
.cursor
.cursor
 
 
.gemini
.gemini
 
 
.github
.github
 
 
app
app
 
 
backend
backend
 
 
desktop
desktop
 
 
docs
docs
 
 
figma/
onboarding-auto-sync
figma/
onboarding-auto-sync
 
 
legacy/
flutter-desktop
legacy/
flutter-desktop
 
 
mcp
mcp
 
 
omi
omi
 
 
omiGlass
omiGlass
 
 
plugins
plugins
 
 
scripts
scripts
 
 
sdks
sdks
 
 
web
web
 
 
.cursorignore
.cursorignore
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
HANDOFF-exports-after-import.md
HANDOFF-exports-after-import.md
 
 
ISSUE_TRIAGE_GUIDE.MD
ISSUE_TRIAGE_GUIDE.MD
 
 
LICENSE
LICENSE
 
 
Package.resolved
Package.resolved
 
 
Package.swift
Package.swift
 
 
README.md
README.md
 
 
TEST.md
TEST.md
 
 
codemagic.yaml
codemagic.yaml
 
 
community-plugin-stats.json
community-plugin-stats.json
 
 
community-plugins.json
community-plugins.json
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
View all files

## Repository files navigation

# omi

### A 2nd brain you trust more than your 1st

Omi captures your screen and conversations, transcribes in real-time, generates summaries and action items, and gives you an AI chat that remembers everything you've seen and heard. Works on desktop, phone and wearables. Fully open source.

Trusted by 300,000+ professionals.

 

 

Website·Docs·Discord·Twitter·DeepWiki

## Quick Start

Try in Browser

git clone https://github.com/BasedHardware/omi.git 
&&
 
cd
 omi/desktop 
&&
 ./run.sh --yolo

Builds the macOS app, connects to the cloud backend, and launches. No env files, no credentials, no local backend.

Requirements:macOS 14+,Xcode(includes Swift & code signing),Node.js

Full Installation

For local development with the full backend stack:

1. Install prerequisites

xcode-select --install
curl --proto 
'
=https
'
 --tlsv1.2 -sSf https://sh.rustup.rs 
|
 sh

1. Clone and configure

git clone https://github.com/BasedHardware/omi.git

cd
 omi/desktop
cp Backend-Rust/.env.example Backend-Rust/.env

1. Build and run

./run.sh

Seedesktop/README.mdfor environment variables and credential setup.

### Mobile App

cd
 app 
&&
 bash setup.sh ios 
#
 or: bash setup.sh android

How it works

┌─────────────────────────────────────────────────────────┐
│ Your Devices │
│ │
│ ┌──────────┐ ┌──────────────┐ ┌───────────────────┐ │
│ │ Omi │ │ macOS App │ │ Mobile App │ │
│ │ Wearable │ │ (Swift/Rust) │ │ (Flutter) │ │
│ └────┬─────┘ └──────┬───────┘ └────────┬──────────┘ │
│ │ BLE │ HTTPS/WS │ │
└───────┼────────────────┼───────────────────┼─────────────┘
 │ │ │
 ▼ ▼ ▼
┌─────────────────────────────────────────────────────────┐
│ Omi Backend (Python) │
│ │
│ ┌─────────┐ ┌──────────┐ ┌─────────┐ ┌──────────┐ │
│ │ Listen │ │ Pusher │ │ VAD │ │ Diarizer │ │
│ │ (REST) │ │ (WS) │ │ (GPU) │ │ (GPU) │ │
│ └─────────┘ └──────────┘ └─────────┘ └──────────┘ │
│ │
│ ┌─────────┐ ┌──────────┐ ┌─────────┐ ┌──────────┐ │
│ │ Deepgram│ │ Firestore│ │ Redis │ │ LLMs │ │
│ │ (STT) │ │ (DB) │ │ (Cache) │ │ (AI) │ │
│ └─────────┘ └──────────┘ └─────────┘ └──────────┘ │
└─────────────────────────────────────────────────────────┘

Component

Path

Stack

macOS app

desktop/

Swift, SwiftUI, Rust backend

Mobile app

app/

Flutter (iOS & Android)

Backend API

backend/

Python, FastAPI, Firebase

Firmware

omi/

nRF, Zephyr, C

Omi Glass

omiGlass/

ESP32-S3, C

SDKs

sdks/

React Native, Swift, Python

AI Personas

web/personas-open-source/

Next.js

## Documentation

### Getting Started

* Introduction
* Quick Start Guide
* macOS App Development
* Mobile App Setup
* Backend Setup
* Contributing

### Building Apps

* App Development Guide
* Example Apps— GitHub, Slack, OmiMentor
* Audio Streaming Apps
* Custom Chat Tools
* Submit to App Store

### API & SDKs

* API Reference— REST endpoints for memories, conversations, action items
* Python SDK
* Swift SDK
* React Native SDK
* MCP Server— Model Context Protocol integration

### Architecture

* Backend Deep Dive
* Transcription Pipeline
* Chat System
* Audio Streaming Pipeline
* BLE Protocol

## Omi Hardware

Open-source AI wearables that pair with the mobile app for 24h+ continuous capture.

* Buy Omi
* Buy Omi Glass Dev Kit— ESP32-S3, camera + audio
* Open Source Hardware Designs
* Buying Guide
* Build the Device
* Flash Firmware
* Integrate Your Wearable
* Hardware Specs

## License

MIT — seeLICENSE

## About

AI that sees your screen, listens to your conversations and tells you what to do

omi.me

### Topics

 python

 c

 app

 mobile

 ai

 nextjs

 summary

 flutter

 transcription

 friend

 wearable

 bci

 omi

 personas

 smartglasses

 necklace

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

8.7k

 stars
 

### Watchers

77

 watching
 

### Forks

1.6k

 forks
 

 Report repository

 

## Releases540

Omi Desktop v0.11.318

 Latest

 

Apr 15, 2026

 

+ 539 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Dart41.9%
* C19.8%
* Python13.1%
* Swift11.7%
* TypeScript6.3%
* Rust2.0%
* Other5.2%