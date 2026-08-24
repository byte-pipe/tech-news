---
title: San Francisco -- The Game
url: https://sf.thijs.gg/
date: 2026-08-25
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-25T06:05:58.560764
---

# San Francisco -- The Game

# San Francisco -- The Game Summary

## Overview
- Online city‑exploration game set in a virtual version of San Francisco.  
- Players can teleport, explore neighborhoods, and interact with a tile‑based world.  
- Includes both first‑person and third‑person perspectives.

## Interface Elements
- Directional compass (N E S W) with degree indicator.  
- Tile stream status: idle, waiting for tile state, current owner fill, ground file, column readiness, visible corners, loading.  
- Controls for speed (‑ / +), distance (‑ / +), walk mode (V), world safety (P), life off (N), and range display (470 m).  
- Debug log copy function.  
- Resource counters: Wood 0, Stone 0, Metal 0.  
- Detail mode toggle (L).  
- Neighborhood readiness indicator (100 % – streets ready).

## Controls
- Movement: **W A S D** keys.  
- Camera view: **C** key.  
- Glider: **H** key.  
- Jump: **Space**.  
- Run/Sprint: **Shift** (also used for exiting).  
- Vehicle mode: **V**.  
- Speed adjustment: **‑ / +** or **↑ / ↓** arrows.  
- Zoom: **‑ / +**.  
- Reset: **R**.  
- Additional shortcuts: **C** for camera, **H** for glider, **V** for vehicle, **Shift** for sprint.

## Resources & Debug
- Displays current amounts of wood, stone, and metal (all at zero).  
- Provides a “Copy Debug Log” option for troubleshooting.  

## Loading & Status
- Initial loading screen with “Welcome to San Francisco”.  
- Options to retry loading if necessary.  
- Status messages: “Loading”, “Retry”, and “Loading” repeated during startup.