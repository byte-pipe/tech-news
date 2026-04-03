---
title: Overclocking Raspberry Pi Pico 2
url: https://learn.pimoroni.com/article/overclocking-the-pico-2
date: 2026-02-20
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-22T06:03:01.657130
---

# Overclocking Raspberry Pi Pico 2

# Overclocking Raspberry Pi Pico 2

This article details the process of overclocking the Raspberry Pi Pico 2, exploring its potential performance limits and the challenges of managing heat.

## Initial Experiments

The Raspberry Pi Pico 2 can typically run at over 400MHz with a 1.3V core voltage. The RP2350 datasheet revealed the voltage regulator's limit could be disabled, allowing for higher voltages. Initial tests using a 100 factorial calculation and the MicroPython performance benchmark showed stable operation up to 570MHz at 1.7V, with temperatures reaching 53.7°C.  Higher voltages (up to 2.2V) allowed for further clock speed increases, but the voltage regulator couldn't consistently deliver the requested voltage. A test point on the Pico 2 allows for voltage probing and external voltage injection.

## Adding Cooling

To address the heat generated during overclocking, a heatsink and fan were added.  Further experiments with cooling achieved stable operation up to 678MHz at 2.2V, with temperatures reaching 57.5°C.  The voltage regulator's limitations were confirmed, as it couldn't consistently supply voltages above 2.2V.

## Test Point 7

The Pico 2 has a test point for measuring the core voltage, enabling external voltage injection using a bench power supply.

## Taking it Further

PimoRoni suggested a liquid nitrogen (LN2) overclocking experiment.  Due to safety concerns and logistical challenges, dry ice was used instead to cool the Pico 2 to around -80°C.  The CoreMark benchmark was used for rigorous testing, ensuring both cores were utilized and errors were reported.  The Pico 2 was configured to run from either the ring oscillator or crystal oscillator, and a 1MHz clock was used for accurate timing measurements.  Modifications were made to the CoreMark benchmark for RP2040 to enable two-core operation, RAM-based compilation, UART output, temperature monitoring, and remote configuration via WiFi.  A Pico W was used to transmit temperature and CoreMark data over WiFi, which was then graphed for monitoring.

## Getting Set Up

The setup involved coordinating three Pico 2s and associated hardware. Initial WiFi communication issues were resolved. A baseline performance of 100MHz was established, and further optimizations were planned.
