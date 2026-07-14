---
title: Measuring input latency on Linux: X11 vs Wayland, VRR, and DXVK - Marco Nett
url: https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/
date: 2026-07-14
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-15T04:50:31.517135
---

# Measuring input latency on Linux: X11 vs Wayland, VRR, and DXVK - Marco Nett

# Measuring input latency on Linux: X11 vs Wayland, VRR, and DXVK

## Overview
- The author built a DIY latency measurement device to capture end‑to‑end input lag on Linux gaming setups.  
- The device uses an Adafruit QT Py RP2040 acting as a USB HID mouse (1000 Hz polling) and a photodiode to detect screen brightness changes.  
- For each click it records ~12 000 photodiode samples (~24 µs intervals) and streams them to the host for analysis, yielding precise click‑to‑photon latency values.

## Device Design Highlights
- **Hardware**: QT Py RP2040, BPW34 photodiode, transimpedance amplifier on perfboard, 3‑D‑printed enclosure with elastic‑band straps.  
- **Firmware**: Sends mouse click, then samples photodiode continuously; streams data over serial to a CSV logger.  
- **Analysis Tool**: Establishes a baseline per click, detects the first sample deviating beyond a threshold, and computes latency using the fixed sampling window.

## Test Scenarios
1. **Display Server** – Compare X11 vs native Wayland (and XWayland as a bonus).  
2. **Variable Refresh Rate (VRR)** – VRR enabled vs disabled.  
3. **DXVK Low‑Latency Fork** – DXVK‑low‑latency enabled vs disabled.  
4. **Bonus Cases** –  
   - DXVK‑low‑latency vs default uncapped DXVK.  
   - Native Wayland vs XWayland (VRR off).

## Test Environment

### Hardware
- CPU: AMD Ryzen 7 5800X3D  
- GPU: NVIDIA GeForce RTX 4070 SUPER  
- RAM: 2 × 8 GB DDR4 3200 MHz  
- Monitor: MSI MAG 272QP QD‑OLED, 2560×1440, 500 Hz  
- Motherboard: MSI B450 GAMING PRO CARBON AC  

### Software
- OS: CachyOS (kernel 7.1.3‑2‑cachyos)  
- NVIDIA driver 610.43.03‑1  
- Desktop: KDE Plasma 6.7.2‑1.1, Xorg 21.1.24‑1.1  
- Proton: proton‑cachyos‑native 1:11.0.20260602‑3  
- DXVK version 3.0 (via proton‑cachyos)  

### System Settings
- Refresh rate set to 500 Hz.  
- Flip mode (direct scanout) enabled on both X11 (via `nvidia-settings`) and Wayland (verified with KWin Debug Console).  
- VRR enabled via NVIDIA settings (X11) or KDE Settings (Wayland).  
- DXVK configuration adjusted per scenario (frame‑rate caps, low‑latency parameters, cached resources).

## Game and Methodology
- **Game**: *Diabotical* (DirectX 11) launched through Heroic with Proton.  
- **In‑game setup**: UI hidden on left‑click, large white box displayed to create a clear brightness change.  
- **Procedure per test case**:  
  1. Close extraneous applications.  
  2. Launch the game, start a local match with a static map.  
  3. Position mouse on a fixed landmark.  
  4. Run 100 clicks (≈2 min) while the device records latency.  
  5. Repeat for each configuration (total 300 clicks per case).  
- Conditions kept constant: no bots, no movement, no round restarts, same monitor position for the sensor.

## Results (Summary)
- Each capped test case maintained a stable frame‑rate cap and stayed CPU‑bound throughout.  
- Latency distributions were clean, bell‑shaped, with a 2–3 ms spread between the 5th and 95th percentiles.  
- No wild outliers were observed across any configuration.  

*(Full numerical results and comparative analysis were omitted in the source excerpt.)*