---
title: Helping Valve to Power Up Steam Devices | Igalia
url: https://www.igalia.com/2025/11/helpingvalve.html
date: 2025-11-21
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-22T11:13:52.987470
screenshot: hackernews_api-helping-valve-to-power-up-steam-devices-igalia.png
---

# Helping Valve to Power Up Steam Devices | Igalia

##### **Steam Frame and Steam Machine Devices Unveiled by Valve**

Valve has released three new gaming devices: Steam Frame (wireless VR headset), Steam Machine (gaming console), and Steam Controller. These devices are expected to be launched in the coming year, following successful releases of Valve Index and Steam Deck.

Igalia is collaborating with Valve on SteamOS, which will power these devices, including the Steam Frame. The Steam Frame showcases an ARM-based CPU, while other features like NVIDIA's GeForce RTX 30 series GPUs enable high-performance rendering. Translating games compiled for x86 chips to run smoothly on ARM chips requires a translation layer called FEX.

Despite challenges, engineers Paulo Matos and Danylo Piliaiev have contributed significantly to these devices' development using various tools like Mesa3D, optimizing VR experiences to ensure quality performance. This achievement involves manually debugging and addressing rendering errors in games running on the Steam Frame.

### **Key Points**

- Valve releases new gaming devices
- Steam Frame (wireless VR headset)
- Steam Machine (gaming console) - ARM-based CPU
- Steam Controller (handheld game controller)
- Collaboration with Igalia for SteamOS and translation layer FEX

### **Implementation**

Igalia works on optimizing games using tools like:

- Mesa3D for rendering performance
- Psychonauts to test code optimization

### **Future Challenges**

- Ensuring correct Vulkan driver
- Fixing issues before releasing the devices
