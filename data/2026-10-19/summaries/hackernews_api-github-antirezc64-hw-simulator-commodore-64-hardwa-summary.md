---
title: GitHub - antirez/c64-hw-simulator: Commodore 64 hardware simulator · GitHub
url: https://github.com/antirez/c64-hw-simulator
date: 2026-10-15
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-19T09:17:04.132733
---

# GitHub - antirez/c64-hw-simulator: Commodore 64 hardware simulator · GitHub

# c64-hw-sim Repository Overview

## Purpose and Scope
- Simulates the Commodore 64 motherboard (ASSY 250407) pin‑by‑pin.
- Allows interactive manipulation of chips, pins, resistors, etc., to observe resulting behavior on screen, keyboard, and signal traces.
- Aims to help users:
  1. Understand C64 internals without risking hardware damage.
  2. Diagnose broken C64s by testing hypotheses before physical desoldering.

## Key Features
- Full netlist of the board and pin‑level models for every component.
- Interactive GUI showing board layout, monitor output, control panel, and oscilloscope.
- Ability to:
  - Lift, short, or ground individual pins.
  - Remove chips or open resistors, ferrite beads, crystals.
  - View pin states with color‑coded probes.
  - Load `.prg` programs directly into DRAM chips.
  - Record screenshots, text output, and GIF animations.
- Command‑line “headless” mode for scripted fault injection and automated runs.
- Cycle‑accurate cores for 6510 CPU, VIC‑II, CIAs, and SID taken from floooh’s emulators.
- PLA logic equations derived from the original 82S100 chip.

## Building and Running
- Build with `make`.
- Run: `./c64-hw-sim [program.prg]`.
- Supports macOS and Linux (X11) with OpenGL; third‑party libraries (`sokol`, `nuklear`) are included.

## Usage Highlights
- Click pins to place them on the oscilloscope or change their state (floating, GND, +5 V).
- Click chips to remove them; click resistors or crystals to open them.
- Control panel lists current faults with “repair” buttons.
- Keyboard mapping: ESC = RUN/STOP, PgUp = RESTORE, TAB = CTRL, left ALT = C=.
- Example command line:  
  `./c64-hw-sim --headless 200 --text --shot out.png --fault U17:removed`

## How It Works
- `tools/kicad2c.py` converts a KiCad board replica into C tables (216 parts, 249 nets).
- Each pin drives its net with a strength (strong, weak, none); strongest drive wins, equal drives cause contention (low wins).
- Floating nets drift toward 1.4 V (TTL load) or 0 V (MOS load) over micro‑ to millisecond timescales.
- Power faults affect chips differently (dead without VCC, floating outputs without GND, phantom power for CMOS).
- Noise is seeded for reproducible runs.
- Part models (`src/parts.c`) include glue logic, ROMs, DRAMs, color RAM, PLA, and the cycle‑accurate CPU/graphics/audio cores.
- Board simulation proceeds in three half‑cycle steps (row address, /RAS fall, /CAS fall) with full settling after each step.

## Limitations
- Performance: runs at 31‑48 % of real C64 speed on high‑end hardware.
- Analog aspects (video output, SID filter, power supply, dot‑clock PLL) are not modeled.
- Floating and power model parameters are approximations.
- Internal chip faults (bad DRAM cells, slow parts) and net bridges are planned but not yet implemented.

## Acknowledgements
- Concept inspired by Andre Weissflog’s (floooh) pin‑level chip emulators.
- Chip cores from floooh’s `c64-llm` (zlib license).
- Board layout from bwack’s KiCad replica (CERN OHL).
- PLA equations from Mark Smith and Marko Mäkelä’s 82S100 read‑out.