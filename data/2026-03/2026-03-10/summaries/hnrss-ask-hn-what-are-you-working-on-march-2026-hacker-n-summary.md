---
title: Ask HN: What Are You Working On? (March 2026) | Hacker News
url: https://news.ycombinator.com/item?id=47303111
date: 2026-03-09
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-10T06:02:43.433712
---

# Ask HN: What Are You Working On? (March 2026) | Hacker News

# Ask HN: What Are You Working On? (March 2026)

## Overview
- The thread asks HN users to share current projects and ideas.
- The most active contribution comes from user **YesBox**, who is developing an indie city‑builder titled **Metropolis 1998**.

## Metropolis 1998 – Core Concept
- A modern take on classic isometric city‑building games (e.g., SimCity 2000, RollerCoaster Tycoon).
- **Pixel‑art 3D rendering** with hand‑drawn assets enhanced by shaders.
- Players can:
  - Watch interior activity inside buildings.
  - Design custom buildings (optional) or rely on auto‑growth zones (residential & office in early access).
  - Adjust demand at the per‑business level.
  - Experience a “1998 aesthetic” with day‑night cycles.

## Development Status & Technical Details
- Early‑access launch planned; Steam page already shows screenshots and a demo (~50 MB).
- Engine uses a **grid‑based vertical system**: each floor is a vector element; sprites are positioned by screen‑space offset.
- Primary developer handles programming, tech‑art, and overall design; pixel art is outsourced.
- Written in C++; data structures mentioned (`vector<uo_map<int, ObjStruct>>`).
- Cross‑platform codebase; Linux support via Proton is functional, native Linux/macOS ports are planned for early access.

## Community Feedback & Discussion
- **Transportation & realism**: commenters request more nuanced traffic, public transit, and walkability mechanics; YesBox confirms limited transport is temporary and will become dynamic.
- **Art & implementation**: interest in how walls/vertical elements are rendered; YesBox explains the floor‑grid approach.
- **Platform requests**: strong demand for macOS and Steam Deck/Proton support; developer intends to address these after launch.
- **Nostalgia factor**: many users express excitement about a modern isometric city builder reminiscent of classic titles.
- **Development advice**: YesBox shares that indie creators often need to hire specialists or partner with co‑founders to fill skill gaps.

## Future Plans
- Expand transportation options and traffic‑management difficulty settings.
- Add more zone types and building automation beyond residential/office.
- Port the game to native Linux and macOS; consider Steam Deck compatibility.
- Continue polishing visual style and gameplay depth based on community input.
