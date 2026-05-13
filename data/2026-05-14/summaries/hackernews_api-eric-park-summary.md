---
title: Eric Park
url: https://ericswpark.com/blog/2026/2026-05-12-my-graduation-cap-runs-rust/
date: 2026-05-13
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-14T06:03:47.381446
---

# Eric Park

# My graduation cap runs Rust

## Background
- The author is graduating for the first time and had to rent a cap and gown, which cost $94.
- Traditional graduation ceremonies move the tassel from right to left, a detail the author finds odd and potentially unfair to left‑handed people.
- Inspired by this, the author wanted the cap to light up when the tassel is moved.

## Project Concept
- Designed a contraption that detects tassel movement with a reed switch and magnet, then illuminates the underside of the cap.
- The final prototype is described as “beautiful” by the author.

## Frequently Asked Questions

### What parts did you use?
- Digispark ATtiny85 microcontroller  
- 48 WS2812B addressable LEDs  
- Wires reclaimed from a discarded Apple USB‑C‑to‑C cable  
- Reed switch and magnet (used to sense tassel movement)  
- USB‑C Power Delivery trigger board  
- Power bank with USB‑C cable  

### How long did you spend on this thing?
- **Coding:** ~2 hours. Required forking and patching the `avr-hal` and `ws2812-avr` crates to support the ATtiny85 at 16 MHz.  
- **Hardware assembly:** >3 hours, the most time‑consuming part.  
- The author notes that using Arduino libraries or a different board might have been easier, but chose Rust to match the blog post title and avoid an over‑kill ESP32 board.

### Are you actually going to wear this to your graduation?
- No. The author feels it looks tacky, likening it to a “gaming PC” for kids or a “seizure” for boomers.

### Warning about strobing
- The accompanying video contains rapid light strobing; a warning is provided for screen‑reader users.

### Can I see the code?
- The source code is available at: https://github.com/ericswpark/gradcap-rs