---
title: GitHub - anomalyco/hex: Local voice dictation for mac, windows and linux · GitHub
url: https://github.com/anomalyco/hex
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-02T08:49:42.135270
---

# GitHub - anomalyco/hex: Local voice dictation for mac, windows and linux · GitHub

# Summary of Hex Repository

## Overview
- Hex provides local voice dictation for macOS, Windows, and Linux.
- Users hold a shortcut key, speak, release the key, and the transcribed text is pasted into the active application.
- All transcription occurs on the device; after the initial speech model download, no data leaves the machine.
- Experimental features are available in the “Labs” section of the sidebar.

## Installation Options
- **Stable release**: current production version.
- **Dev release**: latest development build that self‑updates from the dev channel.
- **Platform‑specific packages**  
  - macOS (Apple silicon): DMG for both stable and dev.  
  - Windows x64 & ARM64: Installer for both stable and dev.  
  - Linux x86_64 & ARM64: Executable, `.deb` (Debian/Ubuntu), and `.rpm` (Fedora/openSUSE) packages for both stable and dev.  
- **Package managers**  
  - Homebrew: `brew install --cask anomalyco/tap/hex`  
  - AUR: `yay -S hex-bin`  
  - Nix: `nix profile install github:anomalyco/hex`  
  - Linux install script: `curl -fsSL https://anoma.ly/hex/install-linux.sh | sh`

## Documentation
- Additional documentation is located in the `docs/` directory of the repository.

## Contributing
- Direct pull requests are not accepted.
- Users should open an issue describing bugs or ideas; the project’s agents typically respond quickly.

## License
- The project is released under the MIT license.