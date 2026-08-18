---
title: Sun Clock
url: https://sunclock.net/
date: 2026-08-17
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-18T12:13:37.865991
---

# Sun Clock

# Sun Clock

## Overview
- 24‑hour clock that visualizes the sun’s position and shows sunrise, solar noon, sunset, golden hour, and twilight for the user’s current location.  
- Also displays moon phase, position, and rise/set times.  
- No advertising; page weight ~100 KB; requires JavaScript; only a tiny stats script from Simple Analytics is used.

## Features & Interaction
- Hover or tap any segment, the hour hand, the moon, or the centre dot to see start and end times.  
- Settings let you toggle:  
  - Moon display  
  - Hour numbers, odd hour numbers, hour marks  
  - Minute hand, minute marks, minute numbers  
  - Seconds hand or sweep hand  
  - 12‑hour time format  
  - Direction (clockwise / anti‑clockwise)  
  - Manual location entry (latitude and longitude)  
  - Color mode (light, dark, auto, dynamic)

## Direction Note
- In the Northern Hemisphere the sun moves clockwise across the sky; in the Southern Hemisphere it moves anti‑clockwise.  
- The clock automatically rotates in the appropriate direction based on latitude, but you can change it manually.  
- For the hour hand to track the sun’s apparent motion, face south (north in the Southern Hemisphere) and tilt the screen to lie in the plane of the ecliptic, with solar noon at the top.

## Updates (selected)
- **2026‑06‑26** – Added MIT license to the code.  
- **2026‑03‑12** – Added optional ticking seconds hand (sweep hand remains default).  
- **2026‑01‑01** – Fixed Moon icon issue in recent Safari versions.  
- **2024‑05‑23** – Option to show odd numbers on the clock face; 12‑hour option now also affects face numbers.  
- **2024‑02‑13** – Added an annual calendar.  
- **2023‑10‑20** – Became a Progressive Web App (offline availability).  
- **2022‑10‑24** – Added auto‑color mode (dynamic colors change with time periods).  
- **2022‑09‑07** – Added dark mode.  
- **2022‑05‑27** – Site went live.

## Privacy
- Only aggregate user statistics are collected.  
- Location and settings are stored locally in the browser; no cookies are sent to the server.

## Support
- Sun Clock is free to use and contains no advertising.  
- Users may contribute support voluntarily.

## Technical
- Built with the SunCalc library.  
- All times update at solar midnight.