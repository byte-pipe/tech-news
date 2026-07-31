---
title: GitHub - mokshablr/gander: Take a gander at any file. Offline, zero-permission Android viewer for PDF, Word, Excel, PowerPoint, photos, video, audio,...
url: https://github.com/mokshablr/gander
date: 2026-07-31
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-01T03:09:08.934248
---

# GitHub - mokshablr/gander: Take a gander at any file. Offline, zero-permission Android viewer for PDF, Word, Excel, PowerPoint, photos, video, audio,...

# Gander – Offline Android File Viewer

## Overview
- Tiny, open‑source Android app (~15 MB) that opens PDF, Word, Excel, PowerPoint, images, video, audio, Markdown, text and code.
- Works fully offline with **zero permissions** (no INTERNET, no storage permission) and no ads or tracking.
- Provides a single viewer for all supported formats, avoiding cloud‑based “half‑viewers”.

## Key Features
- Unified viewer for documents, spreadsheets, slides, media, Markdown and source code.
- Pinch‑to‑zoom and smooth scrolling everywhere; deep‑zoom tiled decoding for large photos.
- Recent files list with thumbnail previews (image, video frame, PDF first page).
- Folder browsing via one‑time system grants, still without storage permission.
- Share sheet and “Open with” integration for receiving files from any app.
- In‑document search with navigation for supported formats.
- Ability to share the opened file to other apps or jump to its folder.
- Privacy‑by‑design: no permissions, no internet, no analytics, no accounts.
- Modern UI: Material 3, dark mode, edge‑to‑edge, supports Android 8.0+.

## Supported Formats
| Category | Formats | Renderer |
|----------|---------|----------|
| Documents | PDF | Pdfium (native) |
| | .docx | docx‑preview in sandboxed WebView |
| Spreadsheets | .xlsx, .xls, .xlsm, .xlsb, .csv, .ods | SheetJS (offline) |
| Slides | .pptx | PPTXjs (offline) |
| Photos | JPG, PNG, WebP, BMP, HEIC/HEIF, GIF, SVG, AVIF, ICO | Tiled view, EXIF aware |
| Video | MP4, M4V, MOV, MKV, WebM, 3GP, AVI, FLV, MPEG‑TS | Media3 ExoPlayer |
| Audio | MP3, M4A, AAC, FLAC, WAV, OGG, Opus, AMR | Media3 ExoPlayer |
| Markdown | .md | rendered to HTML with marked + DOMPurify |
| Text & Code | .txt, .json, .xml, logs, source files | Simple text viewer |
| Unsupported | Legacy .doc/.ppt, binary .xls | Not rendered; app suggests re‑saving |

## Installation
1. Download the latest APK from the **Releases** page (arm64 or universal for older/x86 devices).
2. Transfer to phone, enable “install unknown apps”, and install.
3. Optional: use **Obtainium** with the repo URL for automatic updates.
4. Verify signatures with `apksigner` (SHA‑256 fingerprint provided).

## Zero‑Permission Mechanism
- Files are received via the Storage Access Framework and “Open with” intents, giving the app only the selected documents.
- Office files render inside a locked‑down WebView using `WebViewAssetLoader`; no network access is used.
- Folder browsing uses `ACTION_OPEN_DOCUMENT_TREE` grants; Android does not allow granting the Downloads root.

## Building from Source
- Requires JDK 17+ and Android SDK platform 35.
- Commands: `./gradlew assembleDebug` (debug) or `./gradlew assembleRelease` (unsigned release).
- Release signing expects a local keystore `keystore/gander.jks` (not tracked).

## Architecture Snapshot
- `ViewerActivity` routes files by extension/MIME to one of four surfaces:
  - Native Pdfium view (PDF)
  - SubsamplingScaleImageView (photos)
  - Media3 ExoPlayer (video/audio)
  - Sandboxed WebView (Office, Markdown, text, code)
- `MainActivity` shows recents and granted folders, generating thumbnails off‑thread.

## Roadmap
- Publish on F‑Droid.
- Add legacy `.doc`/`.ppt` support if an offline renderer becomes available.
- Develop an iOS companion as a QuickLook wrapper.

## Contribution & License
- Contributions welcome (issues, small PRs); see `CONTRIBUTING.md`.
- MIT license for the app; vendored libraries retain their original MIT/Apache/BSD licenses.