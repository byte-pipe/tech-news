---
title: A DIY Watch You Can Actually Wear - Hackster.io
url: https://www.hackster.io/news/a-diy-watch-you-can-actually-wear-8f91c2dac682
site_name: hnrss
content_file: hnrss-a-diy-watch-you-can-actually-wear-hacksterio
fetched_at: '2026-04-24T11:56:43.209512'
original_url: https://www.hackster.io/news/a-diy-watch-you-can-actually-wear-8f91c2dac682
date: '2026-04-21'
description: 'Finally, a DIY smartwatch that survives the rain: LILYGO’s IP65-rated T-Watch Ultra brings rugged durability to the ESP32 hacking community.'
tags:
- hackernews
- hnrss
---

The T-Watch Ultra is designed to be rugged (📷: LILYGO)
 
1
1

Driven by a desire to break free from walled gardens, many hardware hackers have designed their own smartwatches. Instead of proprietary hardware and software platforms, these devices typically use highly accessible components like ESP32 microcontrollers and custom-built firmware. So far, so good; however, commercial smartwatches still beat them in one very important way — durability. DIY solutions don’t hold up well (or at all) to the conditions — like rain — that we regularly run into in our everyday lives. This factor alone makes homebrew smartwatches more of a toy than anything practical.

But now, there is a new smartwatch developed by LILYGO called the T-Watch Ultra. It’s got about everything you would expect from a smartwatch (and a few extras) included onboard, and it can be programmed using common development platforms such as Arduino IDE and ESP-IDF. Beyond its internal specifications, the T-Watch Ultra is housed in an IP65-rated case, so you don’t need to be concerned about rain, spills, or dust while you are wearing it.

An overview of the features (📷: LILYGO)

At the core of the device is an ESP32-S3 from Espressif Systems, featuring a dual-core Tensilica LX7 CPU running at up to 240 MHz. With 16MB of flash and 8MB of PSRAM, the watch has significantly more memory than many hobbyist wearables, making it suitable for more complex applications, including edge AI tasks. The inclusion of vector instructions for AI acceleration further supports this functionality.

The display is a 2.01-inch AMOLED panel with a sharp 410×502 resolution and full capacitive touch support. Combined with a 1,100mAh battery — an upgrade over earlier models — this provides both improved usability and longer runtime.

In addition to Wi-Fi and Bluetooth 5.0 LE, the watch includes a Semtech SX1262 LoRa transceiver, enabling long-range, low-power communication. This opens the door to applications like Meshtastic nodes and off-grid messaging systems — capabilities rarely seen in smartwatches.

What's in the box (📷: LILYGO)

A u-blox MIA-M10Q GNSS module provides accurate location tracking, while a Bosch BHI260AP smart sensor enables motion-based AI features. Additional hardware includes NFC via an ST25R3916 chip, a real-time clock, a vibration motor driven by a DRV2605 controller, and a microSD card slot for expanded storage.

Audio support is handled through a built-in microphone and a MAX98357A amplifier, and power management is overseen by an AXP2101 PMU. The device also features a USB Type-C port for charging and programming, making development workflows straightforward.

With support for Arduino, MicroPython, and ESP-IDF — and an ecosystem of example code and libraries — the T-Watch Ultra makes development easy. LILYGO isnow taking pre-ordersfor $78.32, and the device should be available any day.

smartwatch
microcontroller
sensor
wireless
Nick Bild
R&D, creativity, and building the next big thing you never knew you wanted are my specialties.
Follow