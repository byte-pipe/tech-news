---
title: PawBot - An AI Desktop Puppy That Eats Your Files 🐾 - DEV Community
url: https://dev.to/varshithvhegde/pawbot-an-ai-desktop-puppy-that-eats-your-files-301a
site_name: devto
content_file: devto-pawbot-an-ai-desktop-puppy-that-eats-your-files-de
fetched_at: '2026-08-17T19:25:57.627047'
original_url: https://dev.to/varshithvhegde/pawbot-an-ai-desktop-puppy-that-eats-your-files-301a
author: Varshith V Hegde
date: '2026-08-15'
description: 'This is a submission for Weekend Challenge: Dog Days Edition What I Built Remember Neko... Tagged with devchallenge, weekendchallenge.'
tags: '#devchallenge, #weekendchallenge'
---

DEV Weekend Challenge: Dog Days Edition Submission 🐕

This is a submission forWeekend Challenge: Dog Days Edition

## What I Built

RememberNeko the catand thoseTamagotchi desktop petsfrom the 90s? I rebuilt that magic for 2026 — except your pet is a golden retriever puppy powered by an LLM.

PawBotis a Chrome extension + browser demo where a cutepixel puppy:

* 🐕Roamsyour screen like a classic desktop pet
* 🏃Chases your cursorwhen you get close
* 🍖Eats anything you drop— PDFs, code files, emoji, pasted text
* 💬Barks backwith short, mood-aware responses viaGoogle Gemini
* 😴Falls asleepif you ignore it too long (with Zzz particles!)
* ❤️Reacts to pets— click to pet, double-click to wave

Feed it a.pdfand it might say"Mmm, crunchy homework!"Ignore it for 40 seconds and it curls up with sad puppy eyes.

## Demo

Full walkthrough on YouTube:

Quick try locally:

git clone https://github.com/Varshithvhegde/pawbot.git

cd 
pawbot/web
python3 
-m
 http.server 8080

# → http://localhost:8080

Enter fullscreen mode

Exit fullscreen mode

Or load the Chrome extension: clone the repo →./scripts/sync-extension.sh→ Load unpacked → select theextension/folder.

## Code

## Varshithvhegde/pawbot

### AI desktop puppy Chrome extension — pixel pet that eats your files and barks with Google Gemini

# PawBot 🐾

An AI desktop puppy that lives in your browser.A Tamagotchi/Neko-style pixel pet that roams your screen, chases your cursor, eats files & emoji you drop, and barks mood-aware responses powered byGoogle Gemini.

Built for theDEV Weekend Challenge: Dog Days Edition.

## Demo

🎬Watch on YouTube· 📝DEV submission· 🔗GitHub

## Features

FeatureDescription🐕Pixel puppyFull sprite animations — idle, walk, run, eat, sleep, bark, wave🍖Feed anythingDrop files, emoji, or paste text — pup chases food then eats it🏃Chase mechanicsFood falls from above → pup runs to it → 4-frame eat animation💬AI barksGoogle Gemini generates short mood-based responses😴Sleep modeIgnore pup 40s → falls asleep with Zzz particles❤️Pet & waveClick to pet, double-click to wave paw⌨️HotkeysFthrow treat ·Bbark ·Esc…

View on GitHub

Repo:github.com/Varshithvhegde/pawbot

## How I Built It

### Architecture

Browser tab
 │
 ├── Content script (bundled IIFE via esbuild)
 │ └── Shadow DOM canvas overlay (immune to page CSS)
 │
 ├── Pet engine (Canvas 2D state machine)
 │ idle → walk → run → eat → sleep → bark → wave
 │
 ├── Sprite loader (33 AI-generated pixel frames)
 │
 └── Bark engine → Google Gemini API
 mood + hunger + last meal → short bark text

Enter fullscreen mode

Exit fullscreen mode

### Technical decisions

Decision

Why

Vanilla JS + Canvas

Zero build step for the web demo; screen-recording friendly

Shadow DOM overlay

Page CSS can't hide the pup (learned this the hard way on AI Studio)

esbuild bundle

Chrome content scripts can't use ES 
import
 — single bundled file fixes it

AI sprite sheet

Generated pixel art, auto-sliced with a Python script into 33 transparent PNGs

Chase-then-eat flow

Food drops → pup runs → 4-frame eat animation → crumb particles

Fallback barks

Works offline without an API key; Gemini enhances when configured

### Sprite animations (all 33 frames used!)

State

Sprites

Idle

4-frame breathing loop

Walk / Run

Directional left & right sprites

Eat

4-frame chew cycle + flying food emoji

Sleep

Curled up + floating Zzz particles

Mood

Happy, sad, curious, excited overlays

Bark

Shows while AI speech bubble is active

Wave

Paw idle + 3-frame wave on pet/double-click

### Controls

Action

How

Feed

Drag & drop file or emoji

Feed

Paste text/emoji

Pet

Click the puppy

Wave

Double-click

Throw treat

Press 
F

Bark

Press 
B

Livehunger & happiness HUDin the bottom-left corner.

## Prize Categories

### ✅ Best Use of Google AI

PawBot usesGoogle Gemini 2.0 Flash Lite— not as a chatbot, but as apersonality enginefor a desktop pet.

Every bark sends real context to Gemini:

Event

Context sent to Gemini

Example bark

Fed a 
.py
 file

"Just ate: main.py (file)"
, mood: happy

"Python for breakfast? Bold choice."

Ignored 40s+

mood: lonely, ignoredMs: 45000

"...hello? I saved you a spot."

Poked

happiness: 85, mood: excited

"Hehe! Belly rubs detected!"

Hungry

hunger: 82/100

"Is that food? IS THAT FOOD?"

Free API key fromGoogle AI Studio→ paste in extension popup. Falls back to canned barks if no key is set.

## What's next

* 🔊 ElevenLabs barksounds
* 🐩 Multiple dog breeds
* 🦊 Firefox extension

Thanks for reading! If PawBot made you smile, leave a 🐾 in the comments.

Built forInternational Dog Day🐕 ·DEV Weekend Challenge: Dog Days Edition

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse