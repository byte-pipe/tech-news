---
title: Rust (and Slint) on a jailbroken Kindle.
url: https://sverre.me/blog/rust-on-kindle/
date: 2026-05-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-29T04:38:06.811309
---

# Rust (and Slint) on a jailbroken Kindle.

# Rust (and Slint) on a jailbroken Kindle – Summary

## Motivation
- Jail‑broke a 7th‑gen Kindle Paperwhite to use it as a night‑stand clock.  
- Wanted to explore running Rust on the device for more useful projects, such as a Home Assistant dashboard.  

## Cross‑compiling Rust for the Kindle
- Target needed: `armv7-unknown-linux-musleabihf` (ARMv7 + musl).  
- Used `cargo-zigbuild`, which leverages Zig’s built‑in musl support and linker.  
- Steps:  
  - Install Zig.  
  - Install `cargo-zigbuild`.  
  - Run `cargo zigbuild --release --target armv7-unknown-linux-musleabihf`.  

## Getting shell access
- Preferred SSH over USB/Wi‑Fi using the Kindle’s `USBNetwork` tool.  
- Added an entry to `~/.ssh/config` and manually copied the public key to `/mnt/us/usbnet/etc/authorized_keys` (`ssh-copy-id` failed).  

## First program
- Verified the cross‑compiled “Hello, World!” ran and printed to stdout via SSH.  
- Needed a graphical output instead of console output for the Kindle.  

## Rendering to the e‑ink screen
- Chose the Slint UI library (already supports ARMv7).  
- Implemented a `LineBufferProvider` that:  
  - Receives rasterized lines from Slint.  
  - Converts them to grayscale.  
  - Writes them to the framebuffer (`/dev/fb0`) via memory‑mapping.  
- Triggered screen refresh using `ioctl` with the dirty region supplied by Slint.  

## Handling touch input
- Touch controller appears as `/dev/input/event1`.  
- Read raw input events (timestamp, type, code, value) directly from the device file.  
- Kindle uses Linux multi‑touch protocol B: sequence of X, Y, tracking‑ID events followed by `SYNC_REPORT`.  
- Accumulated coordinates and tracking ID, then translated:  
  - Tracking ID `-1` → `PointerReleased`.  
  - First sync after touch‑down → `PointerPressed`.  
  - Subsequent syncs → `PointerMoved`.  
- Passed these events to Slint, which handled the rest.  

## Outcome
- After extensive debugging (screen refresh issues, duplicate touch events, etc.) achieved a functional counter with an increment button.  
- Extracted the Kindle‑specific backend into its own crate and published it on crates.io.  
- Future work: build a full dashboard (e.g., an owl UI) on top of the working backend.