---
title: GitHub - Dieu-de-l-elec/AngstromIO-devboard: AngstromIO, one of the smallest devboards out there, barely longer than a USB C connector, based on the A...
url: https://github.com/Dieu-de-l-elec/AngstromIO-devboard
date: 2026-03-08
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-10T06:01:31.990520
---

# GitHub - Dieu-de-l-elec/AngstromIO-devboard: AngstromIO, one of the smallest devboards out there, barely longer than a USB C connector, based on the A...

# AngstromIO-devboard Summary

## Overview
- The repository hosts three small development boards:
  - **AngstromIO** – an ultra‑compact board (8.9 mm × 9 mm) based on the Attiny1616 MCU.
  - **Programmer** – a dual CH340E board that provides both UPDI programming and UART debugging.
  - **CH32 devboard** – a breadboard‑friendly board for the CH32V003 RISC‑V MCU with a 4 × 5 charlieplexed LED matrix.
- All boards use USB‑C connectors for power and data.
- The designs are panelized onto a single PCB, created in EasyEDA Pro (2‑layer, 1 mm thick, purple soldermask).

## Key Features

### AngstromIO
- Size: 8.9 mm × 9 mm, barely longer than a USB‑C plug.
- MCU: Attiny1616 (16 KB flash, low‑power, Arduino‑compatible via megaTinyCore).
- Power: 5 V supplied through USB‑C.
- LEDs: Two SK6805‑EC15 RGB addressable LEDs.
- Broken‑out pins: SCL, SDA, PB2 (TX), PA3, +5 V, GND, UPDI (programming).

### Programmer
- Dual CH340E chips: one configured as Serial‑UPDI programmer, the other as USB‑to‑UART debugger.
- Two USB‑C connectors; only the debugging USB‑C provides 5 V to the board.
- On‑board 3.3 V LDO with selectable 3.3 V/5 V operation.

### CH32 devboard
- Target MCU: CH32V003 (RISC‑V, 26 KB flash, ~ $0.25).
- Breadboard‑friendly layout.
- Power: USB‑C supplies 3.3 V (on‑board LDO); PC6 and PC5 pins are 5 V tolerant.
- LED matrix: 4 × 5 charlieplexed LEDs.
- Programming: SWIO interface, requires a compatible programmer (WCH LinkE).

## Pinout
- AngstromIO pins are listed above (SCL, SDA, TX, PA3, power, ground, UPDI).
- CH32 devboard provides standard GPIOs plus the SWIO programming pins.

## Software

### AngstromIO
- Arduino‑compatible; uses libraries from megaTinyCore (e.g., Wire for I²C, tinyNeoPixel for LEDs).
- Some libraries may need adaptation.

### CH32 devboard
- Programs are written using the Mounriver Studio IDE.

## PCB Design
- Designed in EasyEDA Pro, 2‑layer, 1 mm thick, purple soldermask.
- All three designs are panelized on a single PCB.

## Repository Information
- Stars: 211
- Forks: 4
- Watchers: 2
- License: MIT
- No official releases yet; BOMs and detailed schematics are marked as “coming soon.”
