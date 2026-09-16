---
title: Hackers Got Inside a Flock Camera. Its Data Shows How the System Really Works | WIRED
url: https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/
date: 2026-09-16
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-17T06:00:28.797564
---

# Hackers Got Inside a Flock Camera. Its Data Shows How the System Really Works | WIRED

# Hackers Got Inside a Flock Camera. Its Data Shows How the System Really Works

## Breach Overview
- Hackers removed a Flock Safety camera from a roadway, copied its storage, and recovered an encryption key.
- The data (videos, logs, software) were shared with 404 Media, Distributed Denial of Secrets, and WIRED for analysis.
- The breach reveals that the camera’s on‑device encryption was not sufficient to protect the stored footage.

## Technical Findings
- The camera runs a mid‑range smartphone‑class processor with about 20 custom Flock apps handling motion detection, image capture, object classification, uploading, and remote updates.
- When motion is detected, the device captures rapid bursts of photos (average ~28 per vehicle, sometimes >100) using multiple exposures for license plates and broader scenes.
- Images are sent to Flock’s cloud; plate reading and vehicle attribute identification occur on the server, not on the device.
- Logs recovered cover ~21 days, showing:
  - ~50,200 vehicle detections
  - ~1.6 million images captured
  - Typical daily count of ~3,300 vehicles (peak 4,454)
- Two unencrypted partitions (“vendor” and “media”) contained the encryption key and media files.
- Software explicitly detects people, recording location and confidence; detection was confirmed on test images and on 11 short video clips (all motorcycles).
- The license‑plate detector sometimes misidentified bumper stickers, dealership frames, and even an American‑flag patch as plates.

## Privacy Implications
- Flock’s national network allows any participating agency to query cameras across the country.
- Records from Alpharetta, GA, were accessible to >2,000 agencies, including colleges, airports, and the GSA Office of Inspector General.
- 404 Media disclosed that local police used the network for ICE lookups and that a Texas officer searched nationwide for a woman who self‑administered an abortion.
- No evidence of face‑recognition software beyond default Android capabilities, which were not enabled.

## Response and Reactions
- Several arrests have been made for tampering with or sabotaging Flock cameras.
- Some municipalities announced they will discontinue use of Flock cameras.
- One police department created a 3D‑printed fake camera case to lure vandals.
- Hacker collective stegan0gram justified the reverse‑engineering as a means to expose surveillance secrets.

## Conclusions
- The hack demonstrates that physical access can bypass Flock’s claimed on‑device encryption and reveal extensive visual data.
- The system’s ability to detect people and misclassify non‑plate graphics raises additional privacy concerns.
- The national searchable network, while marketed as a feature, amplifies the potential for misuse by a wide range of agencies.