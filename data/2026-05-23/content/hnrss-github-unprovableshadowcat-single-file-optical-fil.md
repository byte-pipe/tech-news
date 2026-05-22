---
title: 'GitHub - unprovable/ShadowCat: Single file optical file transfer using a browser · GitHub'
url: https://github.com/unprovable/ShadowCat
site_name: hnrss
content_file: hnrss-github-unprovableshadowcat-single-file-optical-fil
fetched_at: '2026-05-23T06:00:34.591525'
original_url: https://github.com/unprovable/ShadowCat
date: '2026-05-22'
description: Single file optical file transfer using a browser. Contribute to unprovable/ShadowCat development by creating an account on GitHub.
tags:
- hackernews
- hnrss
---

unprovable

 

/

ShadowCat

Public

* NotificationsYou must be signed in to change notification settings
* Fork10
* Star124

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

4 Commits
4 Commits
README.md
README.md
 
 
shadowcat.html
shadowcat.html
 
 
View all files

## Repository files navigation

# ShadowCat

A fully offline, single-file HTML page for moving data between two devices via QR codes — intended for old phones whose radios (BLE, NFC, etc.) arevdead but whose cameras and browsers still work.

## Tabs

* Generate— encode text into a single QR code.
* Scan— decode a single QR via the camera.
* Send file— pick a file, choose chunk size / FPS / ECC, hit Start. Cycles through[header, chunk1…chunkN]forever at the chosen FPS. Pause / Resume / Stop.
* Start from— begin the loop at a chosen frame index; it then continues forward and wraps back to the header normally.
* Show frame+Show/−/+— display exactly one frame static, for resending a specific missing chunk. The number matches the chunk index shown in the receiver's missing-chunks grid (0 = header).
* Receive file— start the camera and point at the sender. Header autodetects, progress bar fills in, missing-chunks grid shows which ones haven't arrived yet. When complete, the file's CRC is verified and a Download button appears.

## Protocol

* Header:QRX1|H|<total>|<filename>|<sizeBytes>|<crc32hex>
* Data:QRX1|D|<idx>|<base64chunk>(1-indexed)
* Base64 alphabet has no|, so parsing is justsplit('|').
* Receiver tracks chunks by index, ignores duplicates, dedupes header by CRC.

## Practical notes for old phones

* Camera needs HTTPS or localhost —file://won't grantgetUserMediapermission. Serve withpython3 -m http.server 8000and visithttp://<your-laptop-ip>:8000/qrcode.htmlover the local network. iOS Safari additionally requires HTTPS for cross-device access — for a LAN setup,caddyor a self-signed cert helps.
* If render fails on a frame ("code length overflow"), drop chunk size or drop ECC level.
* 500 chars × 3 fps ≈ 1.1 KB/s base64 ≈ 0.83 KB/s raw. A 100 KB file is roughly 2 minutes per loop; receiver typically needs 1-2 loops.
* If old devices struggle to decode: lower FPS, raise ECC to Q, shrink chunk to ~300 chars — produces smaller, less dense QRs.

## About

Single file optical file transfer using a browser

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

124

 stars
 

### Watchers

0

 watching
 

### Forks

10

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* HTML100.0%