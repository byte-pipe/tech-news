---
title: Helping Valve to Power Up Steam Devices | Igalia
url: https://www.igalia.com/2025/11/helpingvalve.html
date: 2025-11-21
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-23T11:15:08.721025
screenshot: hackernews_api-helping-valve-to-power-up-steam-devices-igalia.png
---

# Helping Valve to Power Up Steam Devices | Igalia

##### "Igalia’s work has opened new possibilities in gaming"

**Steam Devices Announced**

Valve unveiled three new devices: Steam Frame (wireless VR headset), Steam Machine (gaming console), and Steam Controller. These devices are set to be released this year, succeeding the Valve Index and Steam Deck.

**Key Features of Steam Frame**

* Runs on ARM-based CPU, different from x86 CPUs used in Steam Deck or Index
* Uses translation layer FEX to run applications compiled for x86 chips on ARM chips

### Challenges with Steam Frame Development

* Requires manual QA testing due to potential errors in translating x86 machine code
* Diagnostic process can take time and require testing of games for various issues (e.g. color, sound, gameplay)

### Optimizations Needed for Games

* Requires robust Vulkan driver that can ensure correctness and high performance
* Combination of optimized game data and rendering logic is challenging to implement

**Mesa3DTurnip - A Solution for Qualcomm Adreno Devices**

The Steam Frame's use of a FOSS (Free and Open Source Software) Vulkan driver has been improved upon through Mesa3DTurnip. This initiative involved critical optimizations such as LRZ, autotuner, and support for ADROPS (Advanced Driver Release Optimization Package).

### Additional Notes on Steam Controller

* Initial development with graphics optimization still in progress
* Requires support for both D3D11 and OpenGL games, which were added in later
* Ensuring compatibility with older games will be a focus during testing phase
