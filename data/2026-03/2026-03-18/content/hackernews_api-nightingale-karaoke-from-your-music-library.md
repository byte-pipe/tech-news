---
title: Nightingale — Karaoke from your music library
url: https://nightingale.cafe/
site_name: hackernews_api
content_file: hackernews_api-nightingale-karaoke-from-your-music-library
fetched_at: '2026-03-18T19:24:58.098096'
original_url: https://nightingale.cafe/
author: rzzzzru
date: '2026-03-18'
description: Turn any song into karaoke with neural network-powered stem separation, word-level lyrics, pitch scoring, and dynamic backgrounds. Ships as a single binary.
tags:
- hackernews
- trending
---

Turn any song into karaoke. A self-contained party game that separates
 vocals, transcribes lyrics, and plays it all back with word-level sync
 and pitch scoring.

 
 
Docs
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

## Features

 
 
 

### 🎤Stem separation

 

Vocals are isolated from instrumentals using the UVR Karaoke model or Demucs. Guide vocal volume is adjustable.

 
 

### 📝Word-level lyrics

 

WhisperX transcribes and aligns every word to the audio. Existing lyrics from LRCLIB are used when available.

 
 

### 🎯Pitch scoring

 

Sing into your mic and get scored in real-time. Star ratings and per-song scoreboards track your progress.

 
 

### 👤Player profiles

 

Multiple profiles with separate score histories. Switch between singers without losing anyone's records.

 
 

### 🎬Video file support

 

Drop .mp4 or .mkv files into your library. Vocals are separated and the original video plays as the background.

 
 

### 🌌Dynamic backgrounds

 

GPU shader effects (plasma, aurora, nebula...), Pixabay video loops, or the source video for video files.

 
 

### 🎮Gamepad

 

Navigate menus, pick songs, and control playback entirely with a controller. D-pad, sticks, face buttons.

 
 

### 📦Single binary

 

ffmpeg, Python, PyTorch, and the ML models are all bootstrapped on first launch. Nothing to install.

 
 
 
 
 
 
 

## How it works

 
 
 

### Separate

 

UVR Karaoke or Demucs splits the track into vocals and instrumental. Audio is extracted from video files automatically.

 
 

### Transcribe

 

Synced lyrics are looked up on LRCLIB first. If nothing's found, WhisperX transcribes the vocals with word-level alignment.

 
 

### Play

 

The instrumental plays back with highlighted lyrics, pitch scoring, dynamic backgrounds, and gamepad support.

 
 
 
 
 
 
 

## Platforms

 

Runs on Linux, macOS, and Windows. GPU acceleration via CUDA or Metal when
 available, CPU fallback everywhere else.

 
 
 
Linux
 
x86_64, aarch64
 
 
macOS
 
ARM, Intel
 
 
Windows
 
x86_64
 
 
 
 
 
 
 

## Stay in the loop

 

Get notified about new releases and updates. No spam, unsubscribe anytime.

 
 
 
Subscribe