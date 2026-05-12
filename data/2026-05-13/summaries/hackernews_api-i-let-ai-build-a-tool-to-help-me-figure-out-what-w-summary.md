---
title: I Let AI Build a Tool to Help Me Figure Out What Was Waking Me Up at Night
url: https://martin.sh/i-let-ai-build-a-tool-to-help-me-figure-out-what-was-waking-me-up-at-night/
date: 2026-05-12
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-13T06:01:47.963057
---

# I Let AI Build a Tool to Help Me Figure Out What Was Waking Me Up at Night

# Summary of “I Let AI Build a Tool to Help Me Figure Out What Was Waking Me Up at Night”

## The problem
- Living in a noisy city, I often wake up at odd hours (e.g., 3 am) without knowing the cause.  
- The brain’s transition from deep sleep makes it hard to identify fleeting noises that trigger awakenings.  
- Without knowing the source, I cannot address the issue, and guessing is costly.

## What I built (high‑level overview)
- Leveraged an existing Home Assistant setup with sensors (motion, doors, temperature, etc.).  
- Added:
  - Two inexpensive USB microphones (one indoor, one facing the street).  
  - A Raspberry Pi that records only when I’m home, in bed, and during my usual sleep window, controlled via Home Assistant.  
  - Sleep stage data from my Garmin watch.  
  - A web app (progressive web app) that visualizes audio clips, sleep stages, heart rate, HRV, and other sensor events as tracks similar to a music editor.  
- The Pi stores short audio snippets when volume exceeds a threshold, including a few seconds of pre‑ and post‑context.  
- The web app highlights moments where sleep stages shift or I wake up; clicking a highlight plays the associated audio.  
- Push notifications alert me when the previous night’s data is ready, all confined to my home network.

## Role of AI
- AI tooling enabled me to prototype the entire system in roughly 8 hours (plus minor tweaks).  
- I did not use AI for sound classification; I manually listen to the highlighted clips.  
- The AI assisted by:
  - Generating code based on feedback without me reading the full source.  
  - Controlling the Raspberry Pi via SSH, running experiments (e.g., shouting, running tap) and producing spectrograms.  
  - Creating a custom Home Assistant integration and handling UI screenshots for verification.  
- AI lowered the development cost, making the project feasible over a weekend.

## Note on sleep data
- Garmin’s sleep stage estimates are approximate, but its wake‑up detections are reliable enough to mark moments worth investigating.  
- The goal is practical insight, not clinical sleep analysis.

## Findings and actions taken
- Repeated noise sources identified:
  - Slamming doors (neighbors or within the flat).  
  - High‑pitched dish clatter.  
  - Street traffic: motorbikes, scooters, trucks, trash collection.  
  - Occasionally misattributed internal noises.  
- Mitigations implemented:
  - Installed acoustic panels (IKEA office panels).  
  - Added silicone/rubber insulation around bedroom door and windows.  
  - Addressed some internal noises through brief conversations.  
- Result: noticeable improvement in morning feeling and gradual positive trends in Garmin data.

## Technical details (under the hood)
- Continuous in‑memory audio buffer on the Pi; recording to disk only after threshold crossing.  
- Noise‑suppression profile filters constant background sounds, reducing false positives.  
- Saved snippets are compressed and accompanied by JSON metadata with timestamps.  
- Tiny web server on the Pi serves audio clips and event data to the web app; a token‑protected endpoint allows Home Assistant to toggle recording.  
- Custom Home Assistant integration (written by the coding agent) links the detection state to automations.