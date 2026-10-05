---
title: GitHub - allenv0/SCM: Deep AI search for every photo and every frame of video in any folder on macOS · GitHub
url: https://github.com/allenv0/SCM
date: 2026-10-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-10-05T12:21:13.556180
---

# GitHub - allenv0/SCM: Deep AI search for every photo and every frame of video in any folder on macOS · GitHub

# SCM — Screen Memories

## Overview
- Deep AI search tool for every photo and every video frame on macOS.  
- Local‑first: runs entirely on the Mac, no accounts, cloud storage, or uploads.  
- Combines vision, OCR, and speech models to let you search with plain language.

## What Makes It Different
- Search by describing a memory; a local vision model ranks results.  
- Video segmentation lets you land on the exact shot, not just the file.  
- OCR extracts visible text; Whisper provides exact spoken‑line search.  
- Save any query as a tab; dedicated Screenshots and Email tabs are toggleable.  
- Watched folders auto‑import, deduplicate by content hash, and re‑embed in the background.  
- Fully private: after the initial model weight download, everything stays offline.

## Search Modes
| Mode | Finds |
|------|-------|
| Files | Whole photos/videos by meaning (vision rank with filename/phrase boosts). |
| Scenes | Specific moments inside videos; jump to the exact timecode. |
| OCR | Literal text visible in images and frames (Tesseract, 35 languages). |
| Dialogue | Exact spoken words in videos (Whisper) with tiered exactness. |
| LLMs (opt‑in) | Local chat over dialogue, OCR, and filenames; cited answers. |

## Requirements
- macOS (Electron UI is macOS‑only).  
- Bun package manager (`bun install` to install Node modules).  
- First model download (~435 MB for default CLIP); thereafter fully offline.

## Installation
```bash
brew tap allenv0/scm
brew trust allenv0/scm
brew install --cask allenv0/scm/scm
```
- Upgrade with `brew upgrade --cask allenv0/scm/scm`.  
- To trust only the cask: `brew tap allenv0/scm && brew trust --cask allenv0/scm/scm && brew install --cask scm`.

## Development & Building
- `bun run dev` – build renderer bundle and launch Electron.  
- `bun start` – launch Electron without rebuilding.  
- `bun run build` – rebuild renderer bundle into `dist/`.  
- Packaging:  
  - `bun run dist` – signed DMG/ZIP (requires code‑sign identity).  
  - `bun run dist:unsigned` – unsigned package.  
- Build steps: Vite compiles React renderer → electron‑builder packages the app.

## Core Features

### Files
- Instant filename/keyword pre‑search, then vision model cosine similarity.  
- Phrase and filename boosts, honesty floor, near‑duplicate filter.  
- Tiles show “why it matched” badge and a tooltip with score breakdown.  
- CJK queries use overlapping bigrams.

### Scenes
- All video segments scored; results point to the exact shot with a timecode badge.  
- Noise gate prevents irrelevant matches; each video contributes at most three scenes.

### OCR
- Literal token match against OCR text; works offline.  
- Matched words highlighted in amber on tiles and in the lightbox.

### Dialogue
- Literal retrieval from Whisper transcripts; three tiers: Exact line, Exact words, Words spoken.  
- Highlighted words in a speech snippet; opening a result seeks to the line.

### LLMs (Ask) – Opt‑in
- Local llama.cpp sidecar answers questions using extracted dialogue, OCR, and filenames, with numbered citations.  
- Streaming token output with a live token‑per‑second readout.  
- Model options:  
  - Qwen3 1.7B (default, ~1.1 GB) – fast everyday chat, fits 8 GB Macs.  
  - Llama 3.2 3B (~2 GB) – stronger answers, needs more RAM.

## Tabs & Library Views
- Built‑in browse tabs: All, Videos (auto‑enables Scenes), Screenshots, Email (toggleable).  
- Save any query as a pin‑pill tab (up to 20, renameable).  
- Five semantic views mapped to shortcuts (⌘1–⌘5); ⌘I for AI Insights, ⌘, for Settings.  
- Search scope follows the selected tab; LLM chat respects the same corpus narrowing.

## Email Tab
- Shows photos whose OCR text contains an email address.  
- Robust reconstruction handles punctuation, spacing, and spoken forms.  
- Tiles include a contact strip for copy or compose actions.

## Screenshots Tab
- Classification is rename‑proof, using (in order): manual override, filename vocabulary (30+ localized names), PNG/JPEG metadata probe, source‑folder hint.  
- Unclassified items fall into Projects.

## Vision Models
- Four ONNX Runtime models selectable per library.  
- Default: CLIP ViT‑L/14@336 – best real‑world video performance.  
*(Additional model details omitted for brevity.)*