---
title: "It's time to talk about my writerdeck"
url: https://veronicaexplains.net/my-first-writerdeck/
date: 2026-05-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-24T18:01:35.443504
---

# It's time to talk about my writerdeck

# It’s time to talk about my writerdeck

## Overview
- Converted an old System76 Galago Pro laptop into a distraction‑free writing device (writerdeck).  
- Chose a minimal, console‑only Linux setup to break desktop OS habits and focus on writing.

## Installing a tty‑only Debian system
- Used Debian Trixie’s text‑mode installer, skipped full‑disk encryption and desktop environments (GNOME, etc.).  
- Configured a sudo user by leaving the root password blank, avoiding the common “no sudo” pitfall.  
- Result: a plain console login prompt.

## Adding network‑manager (nm‑tui)
- Replaced the default network stack with `network-manager` for easy Wi‑Fi configuration via the curses UI `nm-tui`.  
- Allows occasional online access for backups while keeping the device primarily offline.

## Core writing tools
- Installed `neovim` (`sudo apt install neovim`) as the preferred editor.  
- Added `kmscon` from backports to provide a scalable console (zoom with Ctrl‑+ / Ctrl‑‑).  
  - Updated `/etc/apt/sources.list` with backports entries, ran `sudo apt update`, then `sudo apt install -t trixie-backports kmscon`.

## Terminal multiplexing with tmux
- Installed `tmux` (`sudo apt install tmux`) for pane management and a customizable status bar.  
- Added `acpi` (battery info) and `light` (screen brightness) (`sudo apt install acpi light`).  

### Battery readout in tmux
- Command to extract percentage: `acpi -b | grep -m1 -o -P '.{0,2}%'`.  
- Inserted into `~/.tmux.conf`:
  ```
  set-window-option -g status-right "#(acpi -b | grep -m1 -o -P '.{0,2}%')"
  ```

### Brightness control in tmux
- Decrease: `light -U 10` (bound to F8).  
- Increase: `light -A 10` (bound to F9).  
- Added bindings to `~/.tmux.conf`:
  ```
  bind -n F8 run-shell 'light -U 10'
  bind -n F9 run-shell 'light -A 10'
  ```

### Additional tmux tweaks
- Move status line to top and set background green:
  ```
  set -g status-position top
  set -g status-style bg=green
  ```
- Full example `~/.tmux.conf` provided in the article.

## Result
- A fully functional, offline‑focused writerdeck with:
  - Scalable console, Vim‑based editing, tmux multiplexing, battery and brightness controls, and easy Wi‑Fi setup when needed.  
- Minimal hardware footprint, no GUI distractions, and a pleasant writing environment for long sessions.