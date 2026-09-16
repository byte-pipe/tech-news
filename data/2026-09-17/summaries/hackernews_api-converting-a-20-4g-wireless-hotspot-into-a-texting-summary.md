---
title: Converting a $20 4G wireless hotspot into a texting device
url: https://bkovac.github.io/modem-thing/
date: 2026-09-15
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-17T06:00:25.374281
---

# Converting a $20 4G wireless hotspot into a texting device

# Converting a $20 4G wireless hotspot into a texting device

## The motivation
- I have a cluttered desk full of Aliexpress parts, gifts, and unfinished projects.  
- Among the items were several open‑stick compatible boards (MF800, UZ801, USB‑form factor), a Clicks keyboard for iPhone, and an Adafruit SHARP memory display.  
- Combining these pieces was inspired by projects like Beepy and Playdate.

## The modem
- A cheap 4G modem with Wi‑Fi, Bluetooth, optional display, battery, and full unlock can be bought for under $20 shipped.  
- The version with a display uses a GC9107 panel, which I discarded because the display quality was poor.  
- The stock firmware is Android, but ADB works out of the box, allowing entry to EDL mode for reflashing.  
- Important resources: OpenStick GitHub, openstick.de, wvthoog.nl blog, extowerk.com blog, and the project’s own GitHub repository.  
- Main challenge after getting Linux running is handling drivers and device‑tree modifications.

## The keyboard
- The Clicks Keyboard feels great but is pricey and requires cutting to fit.  
- It behaves like a standard USB keyboard with an extra Apple‑proprietary endpoint for iPhone authorization.  
- The keyboard’s MCU is a CH32V203; custom firmware is possible but not needed now.  
- A Clicks mobile app exists for configuration, and I may add a utility later.

## The display
- The SHARP memory display offers high contrast, suitable for a simple messaging device.  
- It operates via simple command‑based SPI: send commands, it shows the result.

## The adapter PCB
- A custom PCB was needed to provide:
  - USB host‑mode power control  
  - USB host/device mode switching (TUSB320)  
  - Level shifting for display signals (SN74LVC8T245)  
  - 5 V boost conversion (MCP1640)  
  - VBUS/VBAT switching (TPS22917)  
  - Connectors for USB and the display FPC.  
- The board was ordered assembled on one side to keep costs low; the opposite side holds test pads for connecting to the MF800.  
- All design files are on GitHub.

## Enclosure and mechanical work
- The MF800 is larger than typical OpenSticks due to its battery and overall bulk.  
- To fit inside the Clicks case, I either had to orient it vertically (resulting in a large shape) or trim the PCB horizontally.  
- I marked cut lines on the board, noting that one cut intersected the battery‑connection trace, which required later patching.

## Cutting the PCB
- The board was cut along the planned lines; the device booted immediately, confirming no critical traces were lost.  
- Only the USB connection and 4G modem were not tested after the cut, but I was confident the modem would be unaffected.  
- A 2‑D scan of the trimmed board confirmed a tight fit within the iPhone‑sized case.

## Wiring – first iteration
- I reused the original display pads, though later I realized the labeled pads near the unused micro‑SD slot would have been better.  
- Using the extracted Android device tree, I identified the SPI pins for the display and verified them with a multimeter.  
- Power supplies were wired first, followed by USB.  
- Initial USB enumeration failed; after tightening the twisted pair wires, the device enumerated as “high‑speed” and worked.  
- The keyboard connected without issue, though I was cautious about the CC line wiring on cheap adapters.

## Wiring – second iteration
- (The article cuts off here, but the second wiring phase continues the refinement of connections and testing.)