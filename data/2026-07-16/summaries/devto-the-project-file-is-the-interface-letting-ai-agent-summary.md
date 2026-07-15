---
title: The project file is the interface: letting AI agents drive a video editor - DEV Community
url: https://dev.to/ronak_parmar_033c50d168b5/the-project-file-is-the-interface-letting-ai-agents-drive-a-video-editor-58hd
date: 2026-07-09
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-07-16T03:38:23.558375
---

# The project file is the interface: letting AI agents drive a video editor - DEV Community

# Summary of “The project file is the interface: letting AI agents drive a video editor”

## Overview
- Open‑sourced **FableCut**, a browser‑based Premiere‑style video editor that can be driven by AI agents.  
- Gained attention on Hacker News; the most interesting aspect is the design choice that the **project file itself is the interface**.

## Project file as the interface
- All timeline data (media, clips, tracks, keyframes, transitions, markers) lives in a single `project.json`.  
- The editor UI reads this file; the export process renders it.  
- Any tool that can write JSON (Claude Code, Python scripts, `jq`, manual text editing) can modify the video.  
- Example JSON snippet shows a kinetic caption created simply by writing its description into the file—no dedicated API call is needed.

## SSE used as a simple “doorbell”
- Server watches `project.json` with `fs.watch`, debounces 150 ms, and sends a **payload‑free** Server‑Sent Event to the browser.  
- Browser re‑fetches the file and re‑renders.  
- Chose SSE over WebSockets because data flow is one‑way; writes go through REST or the filesystem, and a missed event is harmless since the next fetch gets the latest state.

## Revision counter for concurrency
- The JSON file includes an integer `revision`. Every write must increment it.  
- Writes with a stale revision are rejected (HTTP 409).  
- This single integer provides the entire concurrency model: last‑writer‑wins with a staleness check, avoiding OT, CRDTs, or lock files.  
- Works well because edits are coarse (whole document) and occur at human speed.

## Frame‑accurate CSS animation trick
- SVG overlays are animated with CSS `@keyframes`. Export must render a precise frame, not a live animation.  
- Solution: pause each animation and control time manually using `animation-delay: calc(var(--d, 0s) - t)`, where `t` is the clip’s local time.  
- Negative delay starts the animation in the past, displaying the exact frame needed.  
- Rule for SVG authors: never hard‑code `animation-delay`; use a custom `--d` property for staggering.

## Comparison with giving an AI direct ffmpeg access
- For simple trims, concatenations, and batch transcodes, giving an AI access to ffmpeg is fine.  
- The creative loop differs: ffmpeg is write‑only, while FableCut provides a mutable JSON state that updates in ~150 ms, keeping the timeline editable.  
- FableCut acts as a state and preview layer; the final export renders frames in the browser and pipes them to ffmpeg for encoding.

## Limitations
- Export relies on a running browser (Chromium‑first); headless export is not yet available.  
- AI agents can still make poor cut decisions, so human‑in‑the‑loop feedback remains essential.

## Repository
- GitHub: https://github.com/ronak-create/FableCut  
- MIT license, zero dependencies, single `node server.js`.  
- Author invites others to build creative extensions and share them.