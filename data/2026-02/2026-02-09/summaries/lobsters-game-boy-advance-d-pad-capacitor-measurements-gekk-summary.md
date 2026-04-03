---
title: Game Boy Advance d-pad capacitor measurements - gekkio.fi
url: https://gekkio.fi/blog/2026/game-boy-advance-d-pad-capacitor-measurements/
date: 2026-02-09
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-09T06:16:02.288076
---

# Game Boy Advance d-pad capacitor measurements - gekkio.fi

# Game Boy Advance D-pad Capacitor Measurement Analysis

## Summary
The article investigates the presence of a 10 nF capacitor (C62) specifically on the up button input of the Game Boy Advance (GBA) d-pad, while other buttons lack this component. The author hypothesizes that this capacitor is necessary to mitigate noise originating from the nearby DC/DC conversion circuitry, preventing spurious button presses. Real-world measurements using an oscilloscope demonstrate that the up d-pad input exhibits significantly more noise (60 mV peak-to-peak without C62) compared to the left d-pad input (40 mV peak-to-peak with C62). Desoldering C62 further increases the noise on the up input. The author concludes that the capacitor is a crucial design element to ensure reliable up button functionality by providing a safety margin against noise interference from the DC/DC converter.

## Key Points
- The up d-pad input on the GBA has a dedicated 10 nF capacitor (C62) not found on other d-pad buttons.
- This capacitor is likely implemented to reduce noise from the adjacent DC/DC conversion circuitry.
- The d-pad's proximity to the DC/DC converter, lacking PCB shielding between the sides, makes it susceptible to noise.
- Measurements show a substantial increase in noise on the up d-pad input when C62 is removed.
- The capacitor effectively reduces peak-to-peak noise from 60 mV to 40 mV.
- This design choice by Nintendo likely prioritizes reliable up button operation over the cost of an additional component.
- The findings suggest that even in relatively controlled conditions, the noise from the DC/DC converter can impact the functionality of sensitive components like the d-pad.
