---
title: Pentaton LP: a music streamer with an LP sleeve sized display. • Pentaton
url: https://pentaton.app/blog/2026-07-12-introducing-pentaton-lp/
date: 2026-07-23
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-27T06:50:57.767843
---

# Pentaton LP: a music streamer with an LP sleeve sized display. • Pentaton

# Pentaton LP: a music streamer with an LP sleeve sized display

## The hardware
- Desired a device that looks like a 12” × 12” vinyl sleeve, as thin as possible.  
- Chose a 17‑inch industrial IPS LCD (1920 × 1920) with embedded DisplayPort.  
- Selected the Radxa CM3 compute module because it provides the required connector.  
- Designed a custom carrier board for minimal height; required four revisions to achieve reliable operation.  
- Board features: USB‑C PD power input, second USB‑C for external DAC, Gigabit Ethernet, 12 V trigger via 3.5 mm jack, Wi‑Fi and Bluetooth on the module.  
- Created an enclosure in FreeCAD; wrote a macro for the curved shape and learned 3D‑printing constraints before printing the final case.  

## The software
- Needed AirPlay support; used the open‑source shairport‑sync on a trimmed Alpine Linux image.  
- Learned boot process, device‑tree configuration, kernel compilation, display backlight control, and power management.  
- Developed a lightweight application that displays album artwork based on AirPlay metadata; only artwork is shown on the screen.  
- Implemented GPU‑accelerated cross‑fading of two 4 MP images at 60 fps to achieve smooth transitions.  
- Added an out‑of‑band protocol extension to the audio player so full‑resolution artwork can be sent, bypassing AirPlay’s default low‑resolution (≈500 × 500) images.  

## Usage
- Device stays on continuously; screen off power consumption < 2 W, full‑brightness consumption ≈ 24 W.  
- Automatically wakes when streaming starts, turning on the screen and triggering a 12 V signal to the amplifier.  
- Powered via a standard USB‑C charger; connected to a Pro‑Jet Amp Box SE through a FiiO KA17 DAC.  
- Streams lossless CD‑quality audio over AirPlay.  

## What’s next
- Considering a Kickstarter campaign for Pentaton LP if enough interest is shown.  
- Interested readers can sign up for updates at https://pentaton.app/lp/.