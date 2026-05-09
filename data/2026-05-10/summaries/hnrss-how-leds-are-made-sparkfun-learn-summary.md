---
title: How LEDs are Made - SparkFun Learn
url: https://learn.sparkfun.com/tutorials/how-leds-are-made/all
date: 2026-05-07
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-10T07:46:40.622386
---

# How LEDs are Made - SparkFun Learn

# How LEDs are Made

## YunSun LED Tour
- The author visited YunSun’s factory in Shenzhen during a 2014 trip to China, arranged by contact Merry Xiao.
- The tour took place on a Saturday when the factory was closed, allowing a detailed look at LED production.
- Mr. Si, the proprietor, and the author’s wife Alicia Gibb were also present.

## Basic Parts
- LED dies are purchased from a Taiwanese supplier; a sheet of ~4,000 dies costs about 80 RMB ($12.50).
- Each die’s batch characteristics (e.g., wavelength ~519 nm, between green and cyan) are printed on the sheet.
- Lead frames are metal pieces that hold 20 LEDs each; a batch of 15 frames contains about 300 LEDs.

## Machines
- **Adhesive Application:** A machine deposits a small drop of adhesive onto the cathode cups of each lead frame.
- **Die Placement:** A mechanical system spreads dies onto a weak‑adhesive film, then workers align each die under a microscope and press it into the lead frame (≈80 dies/min, ~40 000 per day).
- **Wire Bonding:** A wire‑bonding machine attaches a hair‑thin gold wire from the top of each die to the anode lead; the process runs automatically after initial tuning.
- The entire operation is performed in open air, not in a clean‑room environment.
- 7‑segment displays are assembled by bonding individual dies directly onto the PCB segments.

## Molds and Testing
- After wire bonding and adhesive cure, the lead frame is placed in an epoxy mold that defines the LED’s shape.
- Molds limit possible LED shapes; custom shapes require coordination among multiple specialty suppliers (die, lead, mold, etc.).
- Epoxy is injected, then baked 45 minutes, released from the mold, and baked an additional 8–12 hours for full cure.
- Lead frames include metal bridges; a cutting step isolates the cathode and buses the anodes together, simplifying testing.
- A pogo‑pin test station checks each LED’s current draw; LEDs that are shorted or open are discarded.
- After QC, another cut separates individual anodes from the frame, yielding finished LEDs (e.g., many 5 mm red LEDs for SparkFun).

## Factory Overview
- The factory is compact with four production lines that can be reconfigured for different shapes and types.
- The author expresses gratitude to YunSun and recommends contacting Merry (merry@100led.com) for LED supplies.

## Resources and Going Further
- SparkFun product links: assorted LEDs, mixed 5 mm bags, IR control kit, OpenSegment display, NeoPixel shield, single‑digit alphanumeric display.
- Additional tutorials suggested: Light‑emitting Diodes, Interactive hanging LED display, Das Blinken Top Hat, LED Light Bar Hookup Guide, How lithium polymer batteries are made.