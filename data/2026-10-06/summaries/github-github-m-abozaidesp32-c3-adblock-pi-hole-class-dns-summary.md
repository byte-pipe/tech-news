---
title: GitHub - M-Abozaid/esp32-c3-adblock: Pi-hole-class DNS ad-blocker on a $2 ESP32-C3 (no PSRAM): 537k domains as 40-bit FNV-1a hashes in flash, binary-s...
url: https://github.com/M-Abozaid/esp32-c3-adblock
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-10-06T16:49:27.723664
---

# GitHub - M-Abozaid/esp32-c3-adblock: Pi-hole-class DNS ad-blocker on a $2 ESP32-C3 (no PSRAM): 537k domains as 40-bit FNV-1a hashes in flash, binary-s...

# esp32-c3-adblock – Pi‑hole‑class DNS ad‑blocker for a $2 ESP32‑C3  

## Overview  
- DNS sinkhole that runs on an ESP32‑C3 without PSRAM.  
- Stores 40‑bit FNV‑1a hashes of domains in flash and binary‑searches them.  
- ~140 k domains occupy ~0.7 MB flash, lookup takes ~10 ms and uses ~50 KB RAM.  
- Hits return 0.0.0.0, misses are forwarded to an upstream resolver.  

## Why it matters  
- Conventional ESP32 DNS blockers keep the blocklist as strings in RAM, requiring PSRAM.  
- This design keeps only fixed‑size hashes in flash, eliminating the RAM demand.  
- 40‑bit hashes give a practical balance: zero collisions at 141 k entries, about one collision at 537 k entries.  
- Same approach scales to larger ESP32 chips (e.g., ESP32‑S3) where flash‑based hashes vastly outperform string lists in PSRAM.  

## Hardware requirements  
- Any ESP32‑C3 board (tested on C3 SuperMini) with 4 MB flash, no PSRAM.  
- Classic ESP32 (DevKit/WROOM, 4 MB) also supported.  
- Power via stable USB source; avoid cheap USB‑C→A adapters that may brown‑out the radio.  
- Optional printable enclosure (hardware/esp32-c3-supermini-enclosure.stl).  

## Build and flash (PlatformIO)  
1. Copy and edit `src/secrets.example.h` → `src/secrets.h` (Wi‑Fi optional, dashboard credentials mandatory).  
2. Generate the blocklist hash table:  
   ```bash
   python3 tools/build_blocklist.py data/blocklist.bin
   ```  
3. Flash firmware and filesystem with a single USB connection:  
   ```bash
   pio run -t upload
   pio run -t uploadfs
   ```  
4. Monitor boot and open the dashboard at `http://c3adblock.local`.  

## Custom blocklists  
- `build_blocklist.py OUT.bin [SOURCE …]` accepts hosts files, plain domain lists, and AdGuard/Adblock rules.  
- Subdomains inherit the block status of their parent domain.  
- Regex, wildcards, and cosmetic rules are ignored.  
- `@@` rules only un‑block the exact entry.  

## Wi‑Fi configuration (no re‑flash)  
- If Wi‑Fi is not set or connection fails, the device starts an open AP `C3-AdBlock-XXXX` with a captive portal.  
- Use the portal to select a network and enter the password.  
- To change networks later: use “Forget WiFi” on the dashboard or hold the BOOT button on power‑up.  

## Over‑the‑air updates  
- Dashboard allows uploading a new `blocklist.bin` or setting a remote URL for automatic updates.  
- Firmware OTA: upload `firmware.bin` via the dashboard or CLI (`pio run -t upload --upload-port c3adblock.local --upload-protocol espota`).  
- 4 MB flash partitioning leaves ~1.3 MB for blocklists when OTA firmware slots are used; the 537 k “ultimate” list fits only a single‑app layout (no OTA).  

## Security considerations  
- Read‑only endpoints (`/`, `/stats.json`) are public; all state‑changing endpoints require HTTP Basic Auth (`WEB_USER`, `WEB_PASS`).  
- OTA updates also require `OTA_PASS`.  
- Credentials are sent base64 over plain HTTP; they are not encrypted and can be sniffed on an insecure LAN.  
- Dashboard sanitizes custom domain names to prevent stored XSS.  
- The device does not support TLS due to memory constraints.