---
title: Various Projects Independently Find Hidden SDR Capabilities in ESP32 Microcontrollers
url: https://www.rtl-sdr.com/various-projects-independently-find-hidden-sdr-capabilities-in-esp32-microcontrollers/
site_name: hnrss
content_file: hnrss-various-projects-independently-find-hidden-sdr-cap
fetched_at: '2026-10-01T23:02:42.285914'
original_url: https://www.rtl-sdr.com/various-projects-independently-find-hidden-sdr-capabilities-in-esp32-microcontrollers/
date: '2026-10-01'
published_date: '2026-10-01T05:39:30+00:00'
description: Various Projects Find Hidden SDR Capabilities in ESP32 Microcontrollers
tags:
- hackernews
- hnrss
---

Back in 2025,we postedabout ESPARGOS, a phased array of many patch antennas, each connected to an ESP32 WiFi microcontroller. ESPARGOS could be used to determine the direction of arrival for WiFi signals and create a live augmented reality heatmap.

Recently, the ESPARGOS team hasmade an exciting discovery. They found that several ESP32 chips have an undocumented feature that lets the firmware bypass the fixed WiFi and Bluetooth functionality and instead capture raw IQ baseband samples. As a result, several ESP32 models can now be used as an internal SDR covering 2.2–2.7 GHz, plus 4.8–6.0 GHz on the ESP32-C5, with up to 80 MS/s sample rate and roughly 13–54 MHz of analog bandwidth, depending on the chip.

However, for use as a general-purpose PC-connected SDR, the output bandwidth is insufficient, so only snapshots of data can be exported to a PC. This means that the SDR will only work as a spectrum analyzer, and demodulating or decoding continuous radio data is not possible with just an ESP32. The exception is the new ESP32-S31, which can stream continuously at up to 16 MS/s over its Gigabit Ethernet interface, with a SoapySDR driver for GNU Radio and gqrx coming soon. If you want to try it yourself, the ESP-WebSDR page lets you flash the firmware to most ESP32 dev boards directly from your browser and view a live spectrum and waterfall.

Furthermore, ESPARGOS notes that phase-coherent IQ sample capture is now possible with their hardware. This means ESPARGOS is no longer limited to WiFi and Bluetooth signals; it can now perform direction finding on any arbitrary signal in the 2.4 GHz band. The team also says phase-coherent transmissions would be possible, but they aren't implementing them right now because they could be misused.

It also seems that, independently, at least two other projects discovered the same or similar features around the same time, but to solve different problems.

Over on Reddit,user /u/h0m3us3r discovered the same featureand uploaded it to GitHub on Sept 26, and recorded a video showing an ESP32-S3 working as an SDR with an FPGA used as a USB3 front end. Unlike ESPARGOS, h0m3us3r's project streams the raw IQ data to a PC continuously via the FPGA rather than in snapshots, so full demodulation/decoding on PC should be possible. However, the current prototype uses the FPGA to clock the ESP32, which results in poor phase noise. So if the clocking issues can be resolved, an ESP32 combined with an FPGA could make a standard general-purpose SDR, like the RTL-SDR, but with a 2.2–2.8 GHz frequency range and up to 80 MHz of bandwidth.

Another project that seems to be using a somewhat similar finding isC5VRX, which was first uploaded to GitHub on August 13. C5VRX uses an ESP32-C5 as a 5.8 GHz real-time FPV video receiver. Although this project appears to use a different mechanism, the result is similar: it uses an undocumented IQ data stream on the ESP32 to sample FPV signals and demodulate them onboard, outputting analog composite video through a simple resistor DAC. The project is still a work in progress and doesn't yet work reliably at range.

eSpDR ESP32 80 MHz output to SDR++
Tweet
Share
Reddit
Vote
Email

### Related posts:

1. ESPARGOS: An ESP32 Phased Array for Seeing WiFi
2. ESP32-Div: An ESP32 Based Swiss Army Knife for Wireless Networks
3. rtl_433 ported to ESP32 microcontrollers with CC1101 or SX127X Transceiver Chips
4. ESP32 Bus Pirate: Turn your ESP32 into a Multi-Purpose Hacker Tool
5. ESP32 Bus Pirate: Update Brings Waterfall Displays, Cellular Modem Support and External Radio Expander