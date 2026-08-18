---
title: Using the railway network as a flatbed scanner
url: https://philo.gay/linecam/
date: 2026-08-18
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-19T04:07:38.104965
---

# Using the railway network as a flatbed scanner

# Using the railway network as a flatbed scanner – summary

## Overview
- The author built a system that uses an industrial linear scanning camera mounted on moving vehicles (trains, ferries) to capture extremely wide, high‑resolution images.
- The camera records a single vertical line at a very high rate; stitching successive lines together while the vehicle moves creates a full‑frame picture.
- Results include a 56,894 × 2,048‑pixel grayscale image taken on the San Francisco‑to‑Oakland ferry.

## Background and prior art
- 1990s “digital scanning backs” moved a line of pixels across a stationary subject to achieve high resolution without a massive sensor.
- Modern sensors can be large, but line‑scan cameras remain cheaper for very wide formats.
- The author was inspired by Gigawip’s medium‑format scanning camera and wondered whether moving the camera instead of the subject could work.

## Early experiments – slit scanning a sofa
- A quick test involved sliding a phone on a chair while recording video, extracting the leftmost column from each frame, and concatenating them.
- Inconsistent motion produced distorted images; speed variations proved critical.
- Adding accelerometer data from a second phone on a train showed noisy velocity measurements that were not useful.
- These trials highlighted the need for precise speed measurement and higher line‑capture rates.

## Industrial linear camera choice
- Selected the Basler ruL2048‑19gm, a 1 × 2048‑pixel line sensor capable of ~19 kHz line readout.
- Unit cost new ≈ US$700; author acquired one for about one‑tenth that price on eBay.
- Requires bright daylight because the fastest exposure is 1/100 s; tunnels and dim stations are unsuitable.
- Camera interfaces via Gigabit Ethernet; the SDK is freely downloadable without a support contract.
- Custom software captures pixel buffers and writes them to disk, producing usable images even when handheld.

## Mechanical design and mounting
- Designed a utilitarian case with a heat‑set insert, 3‑D printed by a friend, to attach the camera to a tripod.
- Included sensors: 6‑DOF accelerometer/gyro (intended for speed calculation) and GPS (ineffective on Boston trains due to signal blockage).
- Initial prototype suffered from manufacturing tolerances; adjustments were made to ensure proper fit.
- Sensors were temporarily affixed with blue painter’s tape, which held adequately for testing.

## Results and outlook
- First freehand captures with the custom setup showed promising image quality.
- Ongoing work focuses on improving speed measurement, handling lighting constraints, and refining post‑processing to reduce distortion.
- The project was presented at EMFcamp 2026, with a video of the talk and additional details available in the linked gallery.