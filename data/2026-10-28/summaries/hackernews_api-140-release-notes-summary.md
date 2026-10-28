---
title: 1.4.0 - Release Notes
url: https://ghostty.org/docs/install/release-notes/1-4-0
date: 2026-10-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-28T12:08:32.966369
---

# 1.4.0 - Release Notes

# Ghostty 1.4.0 Release Notes Summary  

## Overview  
- Major release published on October 27 2026.  
- Includes large performance and memory improvements, full Kitty graphics implementation (animation + relative placements), SSH integration enhancements, and hundreds of other fixes.  
- Development spanned 7 months, involved 172 contributors and 2,889 commits.  
- Release notes were manually written by maintainers over ~16 hours.  

## Security  
- **GHSA‑4hwh‑wx3w‑3fqg** – Paste protection ignored carriage returns, allowing command execution without confirmation.  
- **GHSA‑mhff‑mv4q‑fp63** – Malicious Kitty graphics could crash Ghostty, cause huge allocations, or read/delete files outside temporary directories.  
- **GHSA‑hcr9‑7hcr‑mjm8** – Malicious terminal output could crash Ghostty via tmux control mode (affects 1.3.0 & 1.3.1).  
- **GHSA‑hp9c‑qp4q‑cpw3** – Similar tmux control‑mode crash using zero‑sized or oversized panes (affects 1.3.0 & 1.3.1).  
- **GHSA‑w9q4‑5jvv‑mcv4** – Clearing screen into scrollback could corrupt memory when scrollback limit is very small.  
- **GHSA‑2r63‑vmw6‑3m3c** – Crafted directory names could make zsh integration send arbitrary escape sequences (e.g., clipboard replacement). Bash affected in a limited way.  
- **macOS GHSA‑cw69‑wm67‑5pv8** – Cmd‑clicking a crafted OSC 8 hyperlink could execute arbitrary commands; now blocked/confirmed.  
- **macOS GHSA‑mfw9‑xcr3‑7gfp** – Same issue for links detected by link configuration; requires user interaction.  
- **macOS GHSA‑v8cw‑fg4j‑jcc4** – Drag‑and‑drop text bypassed paste protection; same impact as above.  
- **macOS GHSA‑mxqx‑236q‑wrv7** – Opening a file with control characters could run a different command than shown in the confirmation dialog.  

*CVEs are pending; updates will be added when assigned.*  

## Highlights  

### macOS 27 Support  
- Full compatibility with macOS 27 (Golden Gate) and continued support back to macOS 13 (Ventura).  
- Fixed title‑bar tab layout, native tab bar blending, hidden‑style rendering with “Reduce Transparency”, icon border, and “New Window” shortcut behavior.  

### Kitty Graphics Animation and Relative Placements  
- 100 % implementation of the Kitty graphics protocol, including animation and relative image placement.  
- Animated GIFs and similar media now play correctly; images scroll with text, retransmission replaces prior images, and invalid data returns errors.  
- SIMD‑based bulk parsing makes large image payloads ~16× faster (benchmark: 64 MiB on x86_64 Linux).  

### Scrollback Compression and Lower Memory Usage  
- Transparent compression of off‑screen scrollback reduces physical memory usage by 70 %–90 % for typical text‑heavy histories.  
- Default scrollback limit increased from 10 MiB to 50 MiB per terminal; compressed scrollback still uses less resident memory than the old limit.  
- Available on macOS and 64‑bit Linux.  
- New empty terminal uses ~16 KiB (down from 128 KiB).  
- Memory freed by clearing/trim is returned to the OS; hidden tabs release GPU resources (e.g., 20 hidden tabs drop GPU memory from ~385 MiB to 18 MiB).  

### Performance Improvements  
- Parallel PTY reading and parsing resolves macOS kernel’s 1 KiB per‑read cap, reducing per‑read overhead and improving end‑to‑end I/O throughput.  
- Additional optimizations across the codebase yield noticeable speed gains over previous versions.  

## Additional Information  
- Ghostty is a non‑profit project; donations primarily fund contributor compensation.  
- Thanks to all contributors, maintainers, moderators, translators, packagers, and users for making the release possible.