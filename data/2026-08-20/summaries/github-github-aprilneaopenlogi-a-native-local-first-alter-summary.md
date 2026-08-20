---
title: GitHub - AprilNEA/OpenLogi: ⚡️A native, local-first alternative to Logitech Options+, written in Rust 🦀 — remap buttons, DPI, and SmartShift over HID+...
url: https://github.com/AprilNEA/OpenLogi
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-08-20T11:28:02.079929
---

# GitHub - AprilNEA/OpenLogi: ⚡️A native, local-first alternative to Logitech Options+, written in Rust 🦀 — remap buttons, DPI, and SmartShift over HID+...

OpenLogi

### OpenLogi: A Native, Local-First Alternative to Logitech Options+ 
================---------
A native, local-first alternative to Logitech Options+, written in Rust
------------------------------------------
### Supported Platforms
-------------------------
* macOS
* Linux
* Windows

### What's New Since Last Release
--------------------------------
* `OpenLogi` has now been made available across all three supported platforms.
* A new `OpenLogi` tab in the `Preferences` > `Input Mapping` panel shows all available buttons.
* An "OpenLogi" link in the `.gitignore` file allows users to add `OpenLogi` as one of the files to ignore when committing.

### Latest Commit
---------------
**846**

### Features and Capabilities
---------------------------

### Button Mapping and Gesture Control
-------------------------------------

* Button remapping via the OS input hook to provide custom button mappings
* Gesture bindings to provide gestures on any button
* Gestures can also be remapped from the OS input hook to access more buttons

### Device Support and Connectivity
---------------------------------

* Supports devices connected to various receivers, including Logi Bolt, Unifying, Bluetooth, and wired connections
* Device state is retrieved via the device's operating system (macOS, Windows, X11 on Linux)

### Customization
--------------

* Customizable action catalog for button remapping
* Configuration stored in the `Cargo.toml` file, synced across machines
* Customizable per-application profile overlays

### Hardware Support
------------------

* Support for Litra lights to power, brightness, and color temperature

### Key Performance Indicators (KPIs)
-----------------------------

* Capture and remap middle, mode-shift, and thumbwheel buttons
* Support for button remapping via the OS input hook
* Gestures for any button
* DPI control with presets and Cycle / Set-preset actions
* Support for Litra lights
* Customizable action catalog and per-application profile overlays