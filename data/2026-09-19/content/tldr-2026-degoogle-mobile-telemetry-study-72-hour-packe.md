---
title: '2026 DeGoogle Mobile Telemetry Study: 72-Hour Packet Benchmark'
url: https://www.praveentechworld.com/research/degoogle-telemetry-2026
site_name: tldr
content_file: tldr-2026-degoogle-mobile-telemetry-study-72-hour-packe
fetched_at: '2026-09-19T21:18:06.299492'
original_url: https://www.praveentechworld.com/research/degoogle-telemetry-2026
author: Praveen
date: '2026-09-19'
description: Empirical 72-hour network telemetry dataset measuring 348 background outbound requests/hour across stock Google Android vs hardened GrapheneOS.
tags:
- tldr
---

⏱️

## The 30-Second Summary (For Non-Techies)

Imagine placing your smartphone face-down on your nightstand before going to sleep. You assume that because the screen is dark and you haven’t opened an app in hours, the phone is sitting quietly doing nothing.

Our data proves the exact opposite:a standard factory Android phone never rests. In our tests, an idle phone woke up an average of348 times every single hour—nearly 6 times every minute—to whisper your Wi-Fi details, device serials, and background telemetry back to Alphabet data centers. Over a 24-hour day, that adds up to over8,300 background transmissionswithout you ever tapping the screen.

Stock Android Idle
348.4
outbound requests / hour
GrapheneOS Idle
0.0
outbound requests / hour
Telemetry Cut
99.4%
fewer Alphabet socket calls
Unique Endpoints
42
Alphabet ASN 15169 IPs
🛡️
 Interactive Audit Tool

### How DeGoogled Are You? Audit Your Setup Against Our Data

Check off the Google services you have replaced in your daily life. Our tool calculates your freedom score and estimates how many of the 8,920 daily telemetry pings you have eliminated.

Reset Checklist
DeGoogle Freedom Score
0
%
🔴 Level 1: Google Dependent
Heavy Surveillance

You are currently relying on default Google tools. Your devices broadcast an estimated8,920 background telemetry pingsto Alphabet servers every 24 hours.

📡 Blocked Daily Pings:
0 / 8,920
⚡ Replaced:
0 of 8 services
💡
Recommended Next Win
Swap Google Search for Brave Search or DuckDuckGo (takes 30 seconds).
Check the services you have replaced:
Points
🔍
Search Engine
Google Search
+15%

Tested Replacements:Brave Search, DuckDuckGo, Kagi

Cuts personal search query profiling, ad intent tracking, and AI search harvesting.

🌐
Web Browser
Google Chrome
+10%

Tested Replacements:Brave, Firefox, LibreWolf, Mullvad

Removes Chrome's Privacy Sandbox ad tracking, browser fingerprinting, and account sync snooping.

✉️
Email & Contacts
Gmail & Google Contacts
+15%

Tested Replacements:Proton Mail, Tuta Mail, Fastmail

Prevents automated parsing of flight receipts, online purchases, tax notices, and password reset links.

☁️
Cloud Drive & Docs
Google Drive & Google Docs
+10%

Tested Replacements:Proton Drive, CryptPad, Nextcloud

Guarantees zero-knowledge client-side encryption so tech platforms cannot scan your personal documents.

📸
Photo Backup
Google Photos
+10%

Tested Replacements:Immich, Ente Photos, Local SSDs

Stops cloud facial recognition, GPS heatmaps of your daily routines, and photo EXIF metadata mining.

📝
Notes & Calendar
Google Keep & Google Calendar
+10%

Tested Replacements:Obsidian, Notesnook, Proton Calendar

Keeps private journal entries, doctor appointments, and daily family schedules completely encrypted.

🗺️
Maps & Navigation
Google Maps
+10%

Tested Replacements:Organic Maps, CoMaps, Magic Earth, OSM

Halts 24/7 background location logging, Wi-Fi router beacon scans, and frequent-location history.

📱
Mobile Operating System
Stock Google Android / iOS Google Services
+20%

Tested Replacements:GrapheneOS, CalyxOS, Pure AOSP

The ultimate privacy step. Cuts 99.4% of all idle background Alphabet socket connections (from 348/hr to 0.0/hr).

Based on our 
72-hour Wireshark mobile telemetry dataset
.
Copy My Score
View Full Runbook
→

## Download the Complete 72-Hour Raw CSV Dataset

Includes exact timestamps, device builds, destination IPs, ASN classifications, port numbers, and byte payloads.

Download CSV Dataset (CC BY 4.0)

## How Our Team Trapped the Data (The Physical Test Bench)

When testing phone tracking, many reviewers make the mistake of installing a software app on the phone to monitor it. But if the operating system is sending telemetry, it can easily hide or bypass monitoring apps.

Our team did something different:we built an external hardware wiretap. Every electrical radio wave leaving the phone's antenna was captured by an independent firewall computer before it ever touched the internet.

1. The Test Devices

We purchased three brand new Google Pixel 8 smartphones (128GB, factory unlocked). We tested them side-by-side on our workbench.

2. The Isolated Wi-Fi Cage

We created a private, closed Wi-Fi network (WPA3-Enterprise) that had zero other laptops, TVs, or printers connected. Only the test phones were on this network.

3. The Network Sniffer Trap

The Wi-Fi router was plugged directly into an enterprise pfSense firewall running Wireshark packet capture software. Every packet was mirrored and logged with nanosecond accuracy.

4. 72 Hours Completely Untouched

All phones were plugged into wall power, locked, and left undisturbed for 72 straight hours (259,200 seconds) without any human interaction.

## What Is Inside These Messages? (The 5 Main Leaks)

We analyzed the packet headers and destination IP addresses across Alphabet's Autonomous System Number (ASN 15169). Here is what the phone was secretly uploading while locked:

### 1. Nearby Wi-Fi Routers (Location Triangulation)

84.2 pings/hr

Even if you turn GPS location off, Google Play Services listens for the unique MAC addresses (BSSIDs) of every Wi-Fi router in your apartment building or office and uploads them tocheckin.gstatic.com. Google cross-references these signals to pinpoint your physical location within meters.

### 2. Hardware Fingerprints & Device Serial Hashes

48.0 pings/hr

The phone periodically transmits carrier configuration profiles, SIM card serial hashes, and unique Android hardware fingerprints todevice-provisioning.googleapis.com, tying your physical handset directly to your Google profile.

### 3. Push Notification TCP Heartbeats

14.8 pings/hr

To make push notifications feel instant, Android maintains a persistent open socket tomtalk.google.com:5228. Every few minutes, a heartbeat packet confirms to Google what Wi-Fi network and IP address your device is currently connected to.

### 4. Photo Library Tokens & Facial Recognition Indices

28.5 pings/hr

Google Photos reaches out tophotosdata-pa.googleapis.comto verify sync tokens, prefetch facial cluster tags, and update album states in the background.

### 5. Search Widget Trending Queries

22.1 pings/hr

The home screen search bar pollssuggestqueries.google.comto pre-download trending keywords and speech recognition language models before you ever tap search.

## Per-Service Background Harvest Matrix (Stock Android 16/17 Idle)

The table below isolates outbound socket requests initiated by individual pre-installed Google ecosystem applications over a 24-hour window with zero user interaction:

Google Service
Idle Reqs / Hour
Primary Destination Endpoint
Daily Payload
Privacy Threat Vector
Google Play Services
142.6
play.googleapis.com
7.8 MB
License synchronization, account tokens, hardware IDs
Location Services & Maps
84.2
checkin.gstatic.com
4.2 MB
Ambient Wi-Fi BSSID beacons, cell tower signal triangulation
Device Provisioning & Config
48.0
device-provisioning.googleapis.com
2.4 MB
Carrier configs, SIM serial hash, hardware build fingerprint
Google Photos Sync
28.5
photosdata-pa.googleapis.com
1.9 MB
Facial recognition model sync, album delta polling
Google Search & Assistant
22.1
suggestqueries.google.com
1.2 MB
Trending query prefetch, speech recognition engine delta
Cloud Messaging (FCM)
14.8
mtalk.google.com:5228
0.8 MB
Persistent TCP heartbeat socket for background push notifications
Crashlytics & Diagnostics
8.2
telemetry.google.com
0.3 MB
App lifecycle durations, memory crash state, battery metrics

## CSV Data Dictionary (What Each Column Means)

If you opendegoogle-telemetry-2026.csvin Microsoft Excel, Apple Numbers, Google Sheets, or Python, here is what every single column represents:

Column Name
Data Type
Plain-English Meaning
timestamp_utc
ISO 8601 String
The exact day, minute, and second the phone secretly transmitted data to Google.
device_model
Hardware String
The test smartphone model used on our workbench (Google Pixel 8, 128GB).
os_build
Build String
The exact operating system build installed during the 72-hour capture.
profile
Test State
The phone configuration: Stock Default, Privacy Toggles Disabled, Sandboxed Play, or Pure No-Google.
target_service
Service Name
Which Google subsystem or app initiated the transmission (e.g., Play Services, Location, Photos).
destination_domain
FQDN Hostname
The human-readable web address of the Google server receiving the data (e.g., play.googleapis.com).
destination_ip
IPv4 Address
The numerical internet address verified to belong to Alphabet Inc. data centers.
asn
Network Number
Autonomous System Number (15169 = Google's global routing infrastructure).
protocol / port
Network Port
The communication channel (TLSv1.3 over Port 443 for web sync, Port 5228 for push notifications).
payload_bytes
Integer (Bytes)
The raw size of the encrypted message sent over the Wi-Fi connection.
description
Human Summary
What was inside the transmission (Wi-Fi router beacons, hardware serials, heartbeat tokens).

## How Can You Use This Dataset?

### 👤For Everyday Privacy Seekers

Use our service breakdown table above to understand where your personal data leaks the most. You don't have to change everything overnight—replacing justSearch and Browserstops 40% of advertising profiling in 5 minutes.

### 🛡️For Sysadmins & Home Labbers

You can copy the destination domains (play.googleapis.com,checkin.gstatic.com,telemetry.google.com) directly into yourPi-hole,AdGuard Home, orNextDNScustom blocklists to shield every device on your home Wi-Fi.

### 📰For Journalists, Bloggers & Wikipedia Editors

This dataset is released under Creative Commons Attribution 4.0 (CC BY 4.0). You are encouraged to download the raw CSV, build your own charts, analyze packet timing distributions, and quote our findings with attribution.

### 💻For Developers & Python Analysts

Load the CSV into Python in three lines of code:

import pandas as pd
df = pd.read_csv("degoogle-telemetry-2026.csv")
print(df.groupby("target_service")["payload_bytes"].sum())

## Visual Comparison: Background Connections / Hour

Feel free to embed this chart on your blog or publication with attribution.

Stock Pixel 8 (Default Settings)
348.4 req/hr
Stock Pixel 8 (All Privacy Toggles Disabled)
194.2 req/hr
GrapheneOS (Sandboxed Google Play)
12.1 req/hr
GrapheneOS (No Google Services)
0.0 req/hr
Embed this research chart on your website:
<iframe src="https://www.praveentechworld.com/research/degoogle-telemetry-2026" width="100%" height="450" frameborder="0" title="DeGoogle 72-Hour Telemetry Study"></iframe>
<p><small>Source: <a href="https://www.praveentechworld.com/research/degoogle-telemetry-2026">PraveenTechWorld 2026 DeGoogle Telemetry Study</a></small></p>

### How to Cite This Research (Journalists & Wikipedia)

This dataset is published under Creative Commons Attribution 4.0 International (CC BY 4.0). You are free to cite, distribute, and reference this research with standard attribution.

APA Citation (with Zenodo DOI)
Mishra, Praveen, & PraveenTechWorld Engineering Lab. (2026). 2026 DeGoogle Mobile Telemetry Study: 72-Hour Packet Benchmark Dataset [Data set]. Zenodo. https://doi.org/10.5281/zenodo.22848749
BibTeX Entry
@dataset{mishra2026degoogle_telemetry,
 author = {Mishra, Praveen and PraveenTechWorld Engineering Lab},
 title = {2026 DeGoogle Mobile Telemetry Study: 72-Hour Packet Benchmark Dataset},
 year = {2026},
 publisher = {Zenodo},
 version = {1.0},
 doi = {10.5281/zenodo.22848749},
 url = {https://doi.org/10.5281/zenodo.22848749}
}
📰 Media & Press Inquiries

Journalists, researchers, and publishers seeking quotes, raw data files, or interview availability:

press@praveentechworld.com

### 📋Dataset Version History & Re-Measurement Schedule

Version
Date
Changes
v1.0
September 17, 2026
Initial 72-hour packet capture dataset published (Stock Android 16, GrapheneOS Sept 2026 build, Pixel 8 hardware).
v1.1
September 19, 2026
Added plain-English explainers, CSV data dictionary, laboratory walkthrough, interactive DeGoogle Freedom Score Calculator, and press contact.

Re-measurement cadence:We plan to re-run the full 72-hour packet capture on each major Android release (Android 17 stable, Android 18 preview) and each quarterly GrapheneOS update. Subscribe to our newsletter or check back for updated datasets.

Practical Implementation

### Ready to De-Google Your Setup?

Read our step-by-step flagship runbook covering replacements for Google Search, Gmail, Google Drive, Google Photos, Android, and Maps with tested migration checklists.

Read the DeGoogle Starter Pack Guide →