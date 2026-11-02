---
title: GitHub - ivankovic/omnidiff: Fast, robust, accurate diffing · GitHub
url: https://github.com/ivankovic/omnidiff
date: 2026-11-02
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-03T06:08:10.857914
---

# GitHub - ivankovic/omnidiff: Fast, robust, accurate diffing · GitHub

# OmniDiff Overview

## Key Features
- Fast, robust, and accurate content‑aware diffing.
- Handles 99.95 % of code changes; 98.8 % diffed with content‑specific algorithms.
- Typical latency under 100 ms; accuracy described as perfect or near‑perfect.
- Specialized diffing for various file types (code, pictures, fonts, archives, PDFs, etc.) with high success percentages.

## Installation
- **From source**: `cargo install --locked omnidiff` (requires Rust 1.92+ and a C compiler).
- **Prebuilt binaries**: Linux, macOS (Intel & Apple Silicon), and Windows binaries attached to each GitHub release.
- **Homebrew**: `brew install ivankovic/omnidiff/omnidiff`.
- **Debian/Ubuntu**: Add the signed apt repository and install with `sudo apt install omnidiff`.
- **Nix/NixOS**: `nix run github:ivankovic/omnidiff` (enable flakes if needed).
- **Arch & Gentoo**: PKGBUILD and ebuild provided in `packaging/`.

## Editor Integration
- VS Code extension (search “OmniDiff”); also available on Open VSX for VSCodium, Cursor, and Windsurf.
- Neovim plugin `omnidiff.nvim`.

## Using OmniDiff

### Interactive TUI
- `omnidiff` opens an empty viewer; `omnidiff BEFORE AFTER` opens a diff directly.
- Press `?` for keybindings.
- Uses 24‑bit color when `COLORTERM=truecolor` is set; otherwise falls back to 256 colors.

### Browser View
- Command `codereview` provides a web‑based review interface (early version, use at own risk).

### Headless / Batch Mode
- `omnidiff --headless BEFORE AFTER` (or `--batch`) prints a plain‑text diff, suitable for scripts or CI.
- Automatically switches to headless when stdout is not a terminal (e.g., when piped).
- Shows 3 lines of context by default; adjust with `--context N`.
- Colors enabled by default; disable with `--color never` or `NO_COLOR=1`.
- Exit codes: `0` on success, `2` on error; optional `--exit-code` returns `1` when files differ.

### JSON Output
- `omnidiff --mode json BEFORE AFTER` outputs a single JSON object (schema in `src/tui/json_output.schema.json`).

## Git Integration
- Run `omnidiff git configure` to set up as a difftool (global or per‑repository).
- Manual configuration example:
  ```bash
  git config difftool.omnidiff.cmd 'omnidiff "$LOCAL" "$REMOTE"'
  git difftool --tool=omnidiff
  ```
- Set `git config diff.tool omnidiff` to make OmniDiff the default difftool.
- `git difftool` launches the interactive TUI; `git diff` falls back to plain text.
- Works with `GIT_EXTERNAL_DIFF=omnidiff git diff` for direct diffing.
- Binary files receive a concise change report; unknown binaries show “Binary file <path> differs”.

## Performance Metrics
- Benchmarked on Intel Core i7‑1370P with 32 GB RAM.
- Speed: under 100 ms for typical diffs.
- Accuracy: near‑perfect across supported formats (code, images, fonts, archives, PDFs, etc.).