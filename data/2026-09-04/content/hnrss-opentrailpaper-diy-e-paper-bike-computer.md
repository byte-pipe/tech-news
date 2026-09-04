---
title: OpenTrailPaper — DIY e-paper bike computer
url: https://opentrailpaper.com
site_name: hnrss
content_file: hnrss-opentrailpaper-diy-e-paper-bike-computer
fetched_at: '2026-09-04T21:15:14.294268'
original_url: https://opentrailpaper.com
date: '2026-09-04'
description: OpenTrailPaper is open-source bike computer firmware for the LilyGO T5S3 4.7" E-Paper PRO. It supports offline maps, GPX routes, FIT recording and Bluetooth sensors.
tags:
- hackernews
- hnrss
---

### LilyGO T5S3 4.7" E-Paper PRO↗

ESP32-S3 · 16 MB flash · 8 MB PSRAM · 960×540 e-paper · BLE 5

Supported

Strengths

* A 4.7" e-paper panel that is readable in direct sunlight
* An SD card slot for offline maps, routes, ride files and logs
* GPS, capacitive touch, a front light, battery and USB-C on one board
* Bluetooth 5 for heart-rate, power and cadence sensors
* Firmware can be installed from a desktop Chromium browser over USB

Tradeoffs

* No pressure sensor.There’s no barometric altimeter, so climbing is derived from elevation baked into the map tiles rather than measured — total ascent is an estimate.
* Basic GPS.The receiver works, but a modern multi-band module would lock on faster and hold a fix better under tree cover or between buildings.
* No magnetometer.Without a compass the map can only orient from your direction of travel, so it can’t point the right way while you’re stopped.
* Measured baseline: about eight hours.A 1,500 mAh build ran for roughly 7.4 usable hours with the front light off. Power work is ongoing, so newer builds may differ.
* Weak hardware buttons.Most interaction goes through the touch panel, which is fiddly with winter gloves or in the rain.
* No waterproofing.The board ships bare with no seal or IP rating, so it needs a case or a bag of its own before you ride it in the wet.