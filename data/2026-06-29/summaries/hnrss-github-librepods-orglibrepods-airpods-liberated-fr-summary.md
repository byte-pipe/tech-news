---
title: "GitHub - librepods-org/librepods: AirPods liberated from Apple's ecosystem. · GitHub"
url: https://github.com/librepods-org/librepods
date: 2026-06-28
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-29T19:25:52.735245
---

# GitHub - librepods-org/librepods: AirPods liberated from Apple's ecosystem. · GitHub

# LibrePods – AirPods liberated from Apple’s ecosystem

## Overview
- LibrePods implements Apple’s proprietary AirPods protocol, enabling many AirPods features on non‑Apple platforms (Linux and Android).
- Features include changing listening modes, ear detection, battery status, head gestures, conversational awareness, automatic connection, and more.

## Feature availability
| Feature | Linux | Android |
|---|---|---|
| Changing Listening Mode | ✅ | ✅ |
| Ear detection | ✅ | ✅ |
| Battery status | ✅ | ✅ |
| Renaming AirPods* | ✅ | ✅ |
| Loud Sound Reduction | 🔴 | ⚪ |
| Head Gestures | ⛔ | ✅ |
| Conversational Awareness | ✅ | ✅ |
| Automatic connection | ✅ | ✅ |
| Hearing Aid | 🔴 | ⚪ |
| Transparency Mode customization | 🔴 | ⚪ |
| Multi‑device connectivity (2 devices) | ⚪ | ⚪ |
| Accessibility configs (press speed, hold duration, etc.) | 🔴 | ✅ |
| General configs (press‑and‑hold cycles, call controls, etc.) | 🔴 | ✅ |
| Head‑tracked Spatial Audio | ❓ | ❓ |
| Heart Rate Monitoring | ⛔ | 🔴 |
| Find My integration | ❓ | ❓ |
| High‑quality two‑way audio | 🔴 | 🔴 |

**Legend**  
✅ Implemented and works well ⚪ Needs VendorID spoofing (use at own risk) 🔴 Not implemented yet, planned ⛔ Will not be implemented ❓ Unknown  

\* Android requires re‑pairing after renaming.

## Planned “Find My” features
- Adding AirPods to the Find My network  
- Playing sound from the charging case  
- Notify when left behind  
- Toggle case charging sounds  
(These may need root on Android.)

## Spatial Audio
- No head‑tracking data is provided to Android; full spatial audio is out of scope and will not be offered.

## Heart Rate Monitoring (AirPods Pro 3+)
- Under development; likely requires root on Android.

## High‑quality two‑way audio
- Possible on iOS/iPadOS via A2DP + AACP.  
- Android implementation would need deeper audio integration and probably root.

## Installation
- Packages are available for **Android** and **Linux**.

## VendorID Spoofing
- Changing the Bluetooth VendorID to Apple’s ID unlocks several special features.  
  - Linux: edit `/etc/bluetooth/main.conf` → `DeviceID = bluetooth:004C:0000:0000`  
  - Android: enable “act as Apple device” in app settings (requires Xposed and LibrePods module).

## Multi‑device Connectivity
- Up to two devices can control and receive audio from the AirPods simultaneously.  
- Switching notifications appear on both Apple and Android devices as “Move to iPhone”.

## Accessibility & Hearing Aid
- Transparency mode, loud‑sound reduction, and other hearing‑aid settings can be customized (Android now, Linux soon).  
- Audiogram results can be imported; the app does not perform hearing tests.

## Protocol & Reverse Engineering
- Refer to the Wireshark dissector plugin by Nojus (`pabloaul/apple-wireshark`).  
- Most of LibrePods’ implementation was reverse‑engineered independently before the dissector existed.

## AI‑generated code
- **Android app**: head‑gesture logic/UI, offset setup (r2+Xposed), troubleshooter, log collector.  
- **Linux rewrite**: `aacp.rs` and `att.rs` translated from Kotlin to Rust with AI; parts of `media_controller.rs` (PulseAudio integration) also AI‑generated.  
- Remaining code (core services, Bluetooth managers, UI) was written manually.

## Acknowledgements
- **Supporters**: davdroman, tedsalmon, wiless, SmartMsg, lunaroyster, ressiwage, kkjdroid, CitrusJoules, DanielReyesDev, sumitduster, GrifTheDev.  
- **Special thanks**:  
  - tyalie – first protocol documentation  
  - rithvikvibhu & lagrangepoint – hearing‑aid help  
  - devnoname120 – first root patch  
  - timgromeyer – first Linux app version  
  - hackclub – hosting High Seas and Low Skies  

## Alternatives for other platforms
- **CAPod** – Android companion app (use on Android 16 QPR3‑ or lower, no root).  
- **MagicPods** – Steam Deck version.  
- **MagicPods for Windows** – available via Microsoft Store.

## License
- LibrePods is released under the GNU GPL v3 (or later).  
- No warranty is provided.