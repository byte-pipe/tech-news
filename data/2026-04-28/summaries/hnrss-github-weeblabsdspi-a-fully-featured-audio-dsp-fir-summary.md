---
title: GitHub - WeebLabs/DSPi: A fully featured audio DSP firmware for the Raspberry Pi Pico (RP2040) and Pico 2 (RP2350). Official Discord: https://discord....
url: https://github.com/WeebLabs/DSPi
date: 2026-04-25
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-28T06:03:32.201205
---

# GitHub - WeebLabs/DSPi: A fully featured audio DSP firmware for the Raspberry Pi Pico (RP2040) and Pico 2 (RP2350). Official Discord: https://discord....

# DSPi Firmware Overview

## Key Capabilities
- USB Audio Interface: plug‑and‑play on macOS, Windows, Linux, iOS; supports 16‑ and 24‑bit PCM at 44.1, 48, and 96 kHz.  
- 24‑bit S/PDIF or I²S Outputs: up to four independent stereo slots (8 channels on RP2350, 4 channels on RP2040); each slot can be switched at runtime between S/PDIF and I²S.  
- Per‑Channel Preamp: independent gain control for each USB input channel applied before any other processing.  
- Matrix Mixer: route either or both USB input channels to any output with independent gain and optional phase invert (2 × 9 on RP2350, 2 × 5 on RP2040).  
- Parametric Equalization: up to 10 PEQ bands per channel with six filter types (110 total bands on RP2350, 70 on RP2040); RP2350 uses a hybrid SVF/biquad architecture for improved low‑frequency accuracy.  
- Volume Leveller: RMS‑based upward compressor with optional 10 ms look‑ahead, soft‑knee, configurable speed, max‑gain ceiling, and a –6 dBFS safety limiter.  
- Loudness Compensation: ISO 226:2003 equal‑loudness contour EQ that boosts bass and treble at low listening levels.  
- Headphone Crossfeed: BS2B‑based crossfeed with interaural time delay; three classic presets plus fully custom parameters.  
- Master Volume: device‑side output ceiling from –128 dB to 0 dB with true‑mute sentinel; persistence can be independent of presets or saved per preset.  
- Per‑Output Gain & Mute, Time Alignment (up to 85 ms per output), Subwoofer PDM Output.  
- Dual‑Core DSP: EQ processing split across both cores for maximum throughput.  
- Configurable Output Pins: all output GPIO pins (including I²S BCK/MCK) can be reassigned at runtime without reflashing.  
- 10‑Slot Preset System: save, load, and manage up to ten complete DSP configurations with user‑defined names and bulk parameter transfer.  
- Diagnostics: per‑channel peak/clip metering, USB PHY error counters, buffer fill statistics, S/PDIF DMA starvation counters, CPU load reporting per core.  
- Firmware Update via USB: vendor command reboots device into UF2 bootloader for host‑driven firmware flashing.

## Platform Support
| Feature | RP2040 (Pico) | RP2350 (Pico 2) |
|---|---|---|
| System Clock | 307.2 MHz (overclock) | 307.2 MHz |
| Core Voltage | 1.15 V | 1.15 V |
| Sample Rates | 44.1 / 48 / 96 kHz | 44.1 / 48 / 96 kHz |
| Audio Processing | Q28 Fixed‑Point | Single‑Precision Float |
| EQ Bands | 10 per channel (70 total) | 10 per channel (110 total) |
| Total Channels | 7 (2 master + 4 S/PDIF·I²S + 1 PDM) | 11 (2 master + 8 S/PDIF·I²S + 1 PDM) |
| Output Slots | 2 stereo (each S/PDIF or I²S) | 4 stereo (each S/PDIF or I²S) |
| Output Bit Depth | 24‑bit | 24‑bit |
| PDM Output | 1 (subwoofer) | 1 (subwoofer) |
| Max Delay | 85 ms per output | 85 ms per output |
| Math Engine | Hand‑optimized ARM Assembly | Hardware FPU (hybrid SVF/biquad EQ) |
| Dual‑Core EQ | Yes (Core 1 processes outputs 3‑4) | Yes (Core 1 processes outputs 3‑8) |
| User Presets | 10 slots | 10 slots |
| Status | Production | Production |

Both platforms are fully tested and production‑ready. The RP2350 provides additional processing headroom thanks to its hardware floating‑point unit, enabling more output channels and a more accurate filter architecture.

## Audio Signal Chain (simplified)
1. **USB Input** – 16/24‑bit PCM Stereo, 44.1/48/96 kHz.  
2. **PASS 1:** Per‑Channel Preamp (independent L/R gain) + USB Volume.  
3. **PASS 2:** Master EQ (10 bands per channel, Left/Right).  
4. **PASS 2.5:** Volume Leveller (optional RMS upward compression).  
5. **PASS 3:** Headphone Crossfeed (optional) + Master Peak Metering.  
6. **Loudness Compensation** (optional).  
7. **PASS 4:** Matrix Mixer (2 inputs × 9 outputs on RP2350, 2 × 5 on RP2040) with per‑crosspoint gain & phase.  
8. **PASS 5:** Per‑Output EQ → Gain/Mute → Delay → Output Gain × Master Volume.  
9. **Outputs:**  
   - S/PDIF or I²S slots (configurable GPIO pins).  
   - PDM subwoofer channel.  
   - Shared I²S BCK/LRCLK; optional MCK pin.

## Additional Resources
- Official Discord server for development updates, discussion, and assistance.  
- Repository includes documentation, firmware source, build instructions, and MIT license.