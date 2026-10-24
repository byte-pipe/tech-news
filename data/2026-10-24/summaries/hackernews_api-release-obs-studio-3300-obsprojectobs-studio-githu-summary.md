---
title: Release OBS Studio 33.0.0 · obsproject/obs-studio · GitHub
url: https://github.com/obsproject/obs-studio/releases/tag/33.0.0
date: 2026-10-24
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-24T14:36:54.818753
---

# Release OBS Studio 33.0.0 · obsproject/obs-studio · GitHub

# OBS Studio 33.0.0 Update

## New Features

* **UEFi 4.1 Support**: Complete overhaul to support new UEFi (UltraWideFormat Interface) version 4.1 protocol
* **Native Plugin Loading**: First-party plugins are now loading directly from the OBS Studio core directory
* **Third-Party Plugin Changes**:
	+ **Core Third-Party Plugins**: First-party plugins are now placed in a new core directory
	+ **Third-Party Plugins**: Existing third-party plugins continue to load from legacy locations, until OBS Studio 34.0
* **Source Snapping**:
	+ **New Visual Indicator**: Sources now snap along the entire axis, not just when directly touched
	+ **Improved Behavior**: No longer require hidden sources to snap, and snapping behavior for spinboxes remains unchanged
* **Typing and Number Input**:
	+ **Typing is now Unintended**: Numbers will not be cut off in some situations
	+ **Improved Behavior**: Values now update immediately after pressing Enter, and the window will not close when Enter is pressed

## Changes

* **Backend Updates**: New UEFI protocol version 4.1 support is added
* **Plugin Changes**:
	+ **UEFi 4.1 Support**: Complete overhaul of the plugin loading system
	+ **Native Plugin Loading**: First-party plugins now load directly from the core directory