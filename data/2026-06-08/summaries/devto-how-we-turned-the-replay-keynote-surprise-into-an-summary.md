---
title: How we turned the Replay keynote surprise into an open-source embedded playground - DEV Community
url: https://dev.to/temporalio/how-we-turned-the-replay-keynote-surprise-into-an-open-source-embedded-playground-49hm
date: 2026-06-02
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-06-08T11:01:25.533909
---

# How we turned the Replay keynote surprise into an open-source embedded playground - DEV Community

# How we turned the Replay keynote surprise into an open‑source embedded playground

## Overview
- The Replay keynote ended with a “one more thing” reveal: 2,000 custom hardware badges were secretly manufactured and handed to attendees.  
- Each badge is an ESP32‑S3‑based, hackable computer featuring an OLED screen, LED matrix, buttons, joystick, motion sensor, haptics, IR, MicroPython, OTA updates, and more.  
- The entire ecosystem—firmware, hardware designs, documentation, flashing tools, and community apps—has been open‑sourced on GitHub (badge.temporal.io).

## What was open‑sourced
- **firmware/** – C++ runtime, MicroPython bridge, built‑in apps (e.g., Doom), OTA support.  
- **hardware/** – KiCad source files, fabrication outputs, artwork, mechanical drawings, BOM/CPL files.  
- **ignition/** – Temporal‑powered flashing workflows.  
- **docs/** – Public documentation site for the badge.  
- **community_apps/** – Installable apps contributed by the community.  
- **data/** – Schedule, speaker, and floor‑plan bundles.  
- **release‑assets/** – Firmware and factory image release notes.

## Hardware challenges (“different gravity”)
- Physical constraints (power, space, component tolerances, assembly) required constant negotiation among designers, manufacturers, and the product team.  
- The badge’s spec: ESP32‑S3 (16 MB flash, 8 MB PSRAM), 128×64 OLED, 8×8 LED matrix, 4 buttons, analog joystick, accelerometer, haptics, IR TX/RX, USB‑C, battery, two‑board assembly.  
- Managing hardware files (KiCad projects, Gerbers, CPLs, pick‑and‑place files) demanded a different collaboration workflow than typical software Git repos.  
- The author acted as “Merge Czar,” translating large generated files and manufacturing artifacts into a clean Git history.

## Firmware design goals
- **Joy & delight:** Provide engaging experiences (games, animations, IR interactions) during the conference.  
- **Hackability:** Ensure the badge remains easy to modify, reflash, and extend after Replay.  
- The firmware functions as a tiny operating system, handling boot, UI, input, LED control, haptics, IR, storage, OTA, app launching, power management, and resource arbitration.  
- Resource contention (screen, buttons, LED matrix, IR, filesystem, memory, time) is explicitly managed to allow seamless switching between native C++ apps and MicroPython scripts.

## Community and future work
- By publishing the full stack, anyone can inspect, repair, extend, or even manufacture their own badge, provided they navigate the practicalities of open‑hardware production (fab notes, component substitutions, assembly constraints).  
- The project invites contributions of new apps, firmware improvements, and hardware tweaks, turning the conference giveaway into a lasting open‑source playground.