---
title: M2: Episode 1 (or, Asahi Linux on M3) - Asahi Linux
url: https://asahilinux.org/2026/09/m2-episode-1/
date: 2026-09-07
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-07T08:08:20.096559
---

# M2: Episode 1 (or, Asahi Linux on M3) - Asahi Linux

# M2: Episode 1 (or, Asahi Linux on M3)

## Main announcement
- Support for Macs with M3‑series SoCs has been merged into the Asahi Linux installer, making them officially supported.

## Feature parity with M1/M2
- Most hardware that works on M1 and M2 machines now works on M3, including:
  - Webcam and internal microphones  
  - USB (up to the hardware limit of USB 3 10 Gb/s)  
  - Hardware‑accelerated video decoding (including AV1)  
  - Wi‑Fi, Bluetooth, and other peripherals  

- Major missing pieces:
  - Full DCP (Display Control Processor) support  
  - GPU 3‑D acceleration (not yet performant or power‑efficient)

## Installation notes
- Current support is gated behind the installer’s **Expert mode**.  
- Installation command (run in macOS Terminal):

```
curl -L https://alx.sh/ | EXPERT=1 sh
```

- After installation, run `dnf upgrade --refresh`.  
- Goal: remove the Expert‑mode requirement before the Fedora 45 beta release (in a few weeks), assuming no show‑stopping regressions.

## Known limitations
- Sleep does not work because of firmware‑provided framebuffer constraints; will be fixed when full DCP support is added.  
- HDMI output on MacBooks is disabled for the same reason.  
- Support covers M3, M3 Pro, and M3 Max MacBooks and iMacs; the M3 Ultra‑based Mac Studio is not yet supported.

## Acknowledgements & outlook
- Thanks to supporters on OpenCollective and GitHub Sponsors; their contributions enabled access to M3 hardware.  
- The team invites feedback and looks forward to further updates.  

*James Calligeros – 2026‑09‑06*