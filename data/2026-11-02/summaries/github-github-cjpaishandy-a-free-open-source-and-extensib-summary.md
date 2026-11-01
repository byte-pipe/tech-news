---
title: GitHub - cjpais/Handy: A free, open source, and extensible speech-to-text application that works completely offline. · GitHub
url: https://github.com/cjpais/Handy
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-02T08:49:21.246055
---

# GitHub - cjpais/Handy: A free, open source, and extensible speech-to-text application that works completely offline. · GitHub

# Handy – Offline Speech‑to‑Text Application  

## Overview  
- Free, open‑source, cross‑platform desktop app for privacy‑focused speech transcription.  
- Works entirely locally; no audio or text is sent to the cloud.  

## Core Principles  
- **Free** – accessible to everyone.  
- **Open Source** – community can extend and contribute.  
- **Private** – voice data stays on the user’s computer.  
- **Simple** – one purpose: transcribe speech into any text field.  

## How It Works  
1. Press a configurable shortcut (hold to record, release to stop, or tap to toggle).  
2. Speak while the shortcut is active.  
3. Release (or toggle) – Handy processes the audio with Whisper or Parakeet V3.  
4. Transcribed text is pasted into the currently focused application.  

- Silence is filtered using Silero VAD.  
- Model options: Whisper (Small/Medium/Turbo/Large) with optional GPU acceleration, or CPU‑optimized Parakeet V3 with automatic language detection.  
- Supports Windows, macOS, and Linux.  

## Quick Start  

### Installation  
- **macOS** – download release or use Homebrew cask: `brew install --cask handy`.  
- **Windows** – download release or use winget: `winget install cjpais.Handy`.  
- **Debian/Ubuntu** – install the `.deb` with APT: `sudo apt install ./Handy_*.deb`.  

After installation: launch Handy, grant microphone and accessibility permissions, set keyboard shortcuts in Settings, and start transcribing.  

### Development Setup  
- Detailed build instructions for each platform are in `BUILD.md`.  

## Sponsors  
- Project is supported by community sponsors (logos shown in the repository).  

## Integrations  
- Raycast integration allows start/stop recording, view history, manage dictionary, and switch models/languages.  

## Debug Mode & CLI  

### Debug Mode  
- macOS: `Cmd+Shift+D`  
- Windows/Linux: `Ctrl+Shift+D`  

### Command‑Line Flags (beta)  
- Remote‑control (sent to a running instance):  
  - `handy --toggle-transcription` – toggle recording.  
  - `handy --toggle‑post‑process` – toggle with post‑processing.  
  - `handy --cancel` – cancel current operation.  
- Startup options:  
  - `handy --start-hidden` – launch without main window.  
  - `handy --no-tray` – launch without system‑tray icon.  
  - `handy --debug` – enable verbose logging.  
  - `handy --help` – list all flags.  
- Flags can be combined, e.g., `handy --start-hidden --no-tray`.  

## Known Issues & Limitations  

### macOS  
- Bluetooth headset microphones may reduce playback quality during recording; use built‑in or external mic instead.  
- Shortcuts containing the `fn`/Globe key work only on Apple keyboards due to hardware limitations.  

### Linux  
- Text input requires additional tools:  
  - X11 → `xdotool` (`sudo apt install xdotool`).  
  - Wayland → `wtype` (`sudo apt install wtype`) or `dotool` (requires user in `input` group).  
- Without these, Handy falls back to `enigo`, which has limited Wayland compatibility.  
- Wayland support is limited; proper text input depends on the installed tool.  
- Runtime dependency `libgtk-layer-shell.so.0` must be installed (e.g., `sudo apt install libgtk-layer-shell0` on Ubuntu/Debian).  

## Additional Resources  
- Full documentation: `README.md`, `AGENTS.md`, `CLAUDE.md`.  
- Contribution guidelines: `CONTRIBUTING.md` and translations file.  
- Release notes and troubleshooting guides are in the `docs/` directory.