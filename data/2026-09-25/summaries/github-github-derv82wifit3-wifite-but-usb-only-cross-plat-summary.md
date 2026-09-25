---
title: GitHub - derv82/wifit3: Wifite but USB-only & cross-platform. · GitHub
url: https://github.com/derv82/wifit3
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-09-25T15:50:19.751119
---

# GitHub - derv82/wifit3: Wifite but USB-only & cross-platform. · GitHub

**Wifit3: A Standalone USB Wi-Fi Auditor**

**Overview**
Wifit3 is a standalone Linux, Windows, and macOS app designed to provide a comprehensive Wi-Fi audit, with a focus on cross-platform compatibility.

**Key Features**

* Cross-platform: Runs identically on multiple operating systems
* Wireless Driver Heaven: Built-in wireless stack with minimal kernel driver dependencies
* Zero Runtime Dependencies: No airCrack-ng, just pure Python with PyUSB and Textual libraries

**Key Features**

### Reconnaissance & Analysis

* Multi-Card Aggregation: Captures packets simultaneously with multiple adapters
* Real-time Scanner: 2.4GHz and 5GHz channel-hopping (split for multi-cards) for real-time signal analysis
* AP & Client Identification: Identifies device vendors, categories, and router make and model from WPS beacons
* VAP Decloaking: Identifies hidden networks by correlating BSSIDs with known visible siblings
* Packet Dashboard: Visualizes real-time beacon, data, injection, and deauthentication packet rates

### Attacks & Captures

* WPA/WPA2 Handshakes: Passive sniffing and targeted deauthentication
* PMKID Harvesting: Active association harvest and passive sniffing for WPA/WPA2 PMKID key material
* EvilTwin WPA3 Downgrade: Clones the AP and evicts clients to capture handshakes
* WPS Recovery Suite: PixieDust (2 Modes) and PushButton (PBC) for offline PIN recovery and button presses detection
* PIN Brute-Force: Resumable WPS PIN cracking for known-PIN database and AP lock monitoring

**Screenshots**

### Focused on a single target

Focus (single target)

### Supported

Scanner: Focus (single target)

**Supported Har**

* Various wireless protocols (WPA/WPA2, PMKID, WEP)
* Multiple network architectures (Linux, Windows, macOS)