---
title: GitHub - unprovable/ShadowCat: Single file optical file transfer using a browser · GitHub
url: https://github.com/unprovable/ShadowCat
date: 2026-05-22
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-23T06:01:04.319281
---

# GitHub - unprovable/ShadowCat: Single file optical file transfer using a browser · GitHub

# ShadowCat

## Overview
- Fully offline, single‑file HTML page for moving data between two devices via QR codes.  
- Targeted at old phones whose radios (BLE, NFC, etc.) are dead but whose cameras and browsers still work.

## Main Functions (Tabs)
- **Generate** – encode text into a single QR code.  
- **Scan** – decode a single QR code using the camera.  
- **Send file** – pick a file, set chunk size, FPS, ECC, then start. Cycles through header and chunks forever at the chosen FPS; can pause, resume, or stop.  
- **Start from** – begin the loop at a chosen frame index; continues forward and wraps to the header normally.  
- **Show frame / Show − /+** – display exactly one static frame for resending a specific missing chunk; the number matches the chunk index shown in the receiver’s missing‑chunks grid (0 = header).  
- **Receive file** – start the camera, point at the sender, auto‑detect header, show progress bar, display missing‑chunks grid, verify CRC when complete, then provide a Download button.

## Transfer Protocol
- Header: `QRX1|H|<total>|<filename>|<sizeBytes>|<crc32hex>`  
- Data: `QRX1|D|<idx>|<base64chunk>` (1‑indexed)  
- Base64 alphabet excludes `|`, so parsing is a simple split on `|`.  
- Receiver tracks chunks by index, ignores duplicates, and deduplicates header by CRC.

## Practical Tips for Old Phones
- Camera access requires HTTPS or localhost; `file://` won’t grant permission. Serve with `python3 -m http.server 8000` and visit `http://<your-laptop-ip>:8000/qrcode.html` on the local network.  
- iOS Safari also requires HTTPS for cross‑device access; a self‑signed certificate can be used for LAN setups.  
- If a frame fails to render (“code length overflow”), reduce chunk size or lower ECC level.  
- Approximate throughput: 500 characters × 3 fps ≈ 1.1 KB/s base64 (≈0.83 KB/s raw). A 100 KB file takes about 2 minutes per loop; the receiver typically needs 1–2 loops.  
- For devices that struggle to decode: lower FPS, raise ECC to Q, shrink chunk to ~300 characters to produce smaller, less dense QR codes.

## Repository Statistics
- Stars: 124  
- Forks: 10  
- Primary language: HTML (100 %)