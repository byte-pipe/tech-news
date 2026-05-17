---
title: A nicer voltmeter clock - lcamtuf’s thing
url: https://lcamtuf.substack.com/p/a-nicer-voltmeter-clock
date: 2026-05-16
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-18T06:01:59.699888
---

# A nicer voltmeter clock - lcamtuf’s thing

# A nicer voltmeter clock

## Background
- In 2019 I built a simple voltmeter clock that used analog panel voltmeters as the display.
- The original design was never documented; it sat on my desk for years.
- Existing online designs are often overly complex and not aesthetically pleasing, prompting a revised version.

## Design improvements
- Started with a 3‑D mockup in Rhino3D to plan the new enclosure.
- Chose three generic 90° panel voltmeters from Amazon (~$9 each) and disassembled them for precise measurements.
- Created printable decal PDFs to replace the original faces; hour gauge has 13 divisions (0‑12) and minute/second gauges have 61 divisions (00‑60) to allow continuous motion of the hands.

## Mechanical construction
- The cheap “Baomain 65C5” meters have an unattractive plastic flange, so I concealed it with a recessed decorative pattern.
- Machined the front and back faces from planed maple lumber using a CNC mill.
- Formed the rounded side wall by cutting internal notches, moistening the wood, and bending it around a template without a steam‑bending jig.
- Glued the curved side wall to the front and back using a plywood template to ensure a precise fit.
- Finished the assembled body with sanding and a coat of nitrocellulose lacquer.

## Electronics
- Used an AVR128DB28 MCU powered from a wall wart and driven by an 8 MHz crystal (a 32.768 kHz crystal would also work).
- Connected each voltmeter to a digital output pin (PC0, PC1, PC2); two push‑buttons on pins PD6 and PD7 set the time.
- No DACs or extra driver circuitry are needed; a high‑frequency 1‑bit pulse train drives the meters, with the meter’s inertia and coil inductance smoothing the position based on duty cycle.

## Software
- Source code is short, well‑commented, and available online.
- A timer interrupt synchronized to the crystal advances a 10 Hz counter.
- The main loop calculates the required duty cycle for each meter and toggles the output pins manually; hardware PWM was unnecessary for this simple task.

## Final notes
- A “rollover” video demonstrates the clock transitioning at 11:59:59.
- Links to other articles by the author are provided for readers interested in related topics.