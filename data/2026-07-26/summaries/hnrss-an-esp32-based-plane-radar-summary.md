---
title: An ESP32 based plane radar
url: https://blog.ktz.me/esp32-plane-radar/
date: 2026-07-26
site: hnrss
model: llama3.2:1b
summarized_at: 2026-07-26T11:36:54.063367
---

# An ESP32 based plane radar

Here's a concise and informative summary of the article:

### ESP32-Based Plane Radar Project

*   **Description**: A user projects an ESA compatible plane radar onto a 1.28-inch round display with an ESP32-C3 using GitHub repository.
*   **Key Features**:
    *   Pulls nearby ADS-B traffic for live aircraft location displays
    *   Plots each aircraft by distance and bearing, displaying details on the screen
    *   Can be easily flashed to a new board using web-based flashing tool (ESPHome)
*   **Challenges**: Involves some soldering and requires occasional device maintenance.
*   **Comparison**: Notes that the original 3D model was too tight, but printed its own replacement instead.

### Customisation Options

*   **Improvements**: Includes proper flight context with data availability, aircraft type descriptions, and local weather information
*   **Additional Features**:
    *   Modified web interface to enable user-defined coordinates and changes in display options
    *   Supports authenticated OTA updates for future build installs