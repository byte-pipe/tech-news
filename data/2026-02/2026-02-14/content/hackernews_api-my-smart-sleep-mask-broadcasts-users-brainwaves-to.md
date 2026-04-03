---
title: My smart sleep mask broadcasts users' brainwaves to an open MQTT broker | aimilios
url: https://aimilios.bearblog.dev/reverse-engineering-sleep-mask/
site_name: hackernews_api
content_file: hackernews_api-my-smart-sleep-mask-broadcasts-users-brainwaves-to
fetched_at: '2026-02-14T19:11:04.257038'
original_url: https://aimilios.bearblog.dev/reverse-engineering-sleep-mask/
author: minimalthinker
date: '2026-02-14'
description: I recently got a smart sleep mask from Kickstarter. I was not expecting to end up with the ability to read strangers' brainwaves and send them electric impul...
tags:
- hackernews
- trending
---

# My smart sleep mask broadcasts users' brainwaves to an open MQTT broker

12 Feb, 2026

I recently got a smart sleep mask from Kickstarter. I was not expecting to end up with the ability to read strangers' brainwaves and send them electric impulses in their sleep. But here we are.

The mask was from a small Chinese research company, very cool hardware -- EEG brain monitoring, electrical muscle stimulation around the eyes, vibration, heating, audio. The app was still rough around the edges though and the mask kept disconnecting, so I asked Claude to try reverse-engineer the Bluetooth protocol and build me a simple web control panel instead.

### Bluetooth

The first thing Claude did was scan for BLE (Bluetooth Low Energy) devices nearby. It found mine among 35 devices in range, connected, and mapped the interface -- two data channels. One for sending commands, one for streaming data.

Then it tried talking to it. Sent maybe a hundred different command patterns. Modbus frames, JSON, raw bytes, common headers. Unfortunately, the device said nothing back, the protocol was not a standard one.

### The app

So Claude went after the app instead. Grabbed the Android APK, decompiled it with jadx. Turns out the app is built with Flutter, which is a bit of a problem for reverse engineering. Flutter compiles Dart source code into native ARM64 machine code -- you can't just read it back like normal Java Android apps. The actual business logic lives in a 9MB binary blob.

But even compiled binaries have strings in them. Error messages, URLs, debug logs. Claude ranstringson the binary and this was the most productive step of the whole session. Among the thousands of lines of Flutter framework noise, it found:

* Hardcoded credentials for the company's message broker (shared by every copy of the app)
* Cloud API endpoints
* All fifteen command builder function names (e.g. to set vibration, heating, electric stimulation, etc.)
* Protocol debug messages that revealed the packet structure -- header, direction byte, command type, payload, footer

We had the shape of the protocol. Still didn't have the actual byte values though.

Claude then usedblutter, a tool specifically for decompiling Flutter's compiled Dart snapshots. It reconstructs the functions with readable annotations. Claude figured out the encoding, and just read off every command byte from every function. Fifteen commands, fully mapped.

### It works

Claude sent a six-byte query packet. The device came back with 153 bytes -- model number, firmware version, serial number, all eight sensor channel configurations (EEG at 250Hz, respiration, 3-axis accelerometer, 3-axis gyroscope). Battery at 83%.

Vibration control worked. Heating worked. EMS worked. Music worked. Claude built me a little web dashboard with sliders for everything. I was pretty happy with it.

That could have been the end of the story.

### The server

Remember the hardcoded credentials from earlier? While poking around, Claude tried using them to connect to the company's MQTT broker -- MQTT is a pub/sub messaging system standard in IoT, where devices publish sensor readings and subscribe to commands. It connected fine. Then it started receiving data. Not just from my device -- fromall of them. About 25 were active:

* Sleep masks publishing live EEG brainwave data
* Air quality monitors reporting temperature, humidity, CO2
* Presence sensors detecting room occupancy

Claude captured a couple minutes of EEG from two active sleep masks. One user seemed to be in REM sleep (mixed-frequency activity). The other was in deep slow-wave sleep (strong delta power below 4Hz). Real brainwaves from real people, somewhere in the world.

### EMS

The mask also does EMS -- electrical muscle stimulation around the eyes. Controlling it is just another command: mode, frequency, intensity, duration.

Since every device shares the same credentials and the same broker, if you can read someone's brainwaves you can also send them electric impulses.

### Disclosure

For obvious reasons, I am not naming the product/company here, but have reached out to inform them about the issue.

This whole thing made me revisit Karpathy'sDigital Hygienepost, and you probably should too.

The reverse engineering -- Bluetooth, APK decompilation, Dart binary analysis, MQTT discovery -- was more or less one-shotted by Claude (Opus 4.6) over a 30' autonomous session.
