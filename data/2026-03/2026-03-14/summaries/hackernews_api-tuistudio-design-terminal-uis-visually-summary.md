---
title: TUIStudio — Design Terminal UIs. Visually.
url: https://tui.studio/
date: 2026-03-13
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-14T06:03:27.655492
---

# TUIStudio — Design Terminal UIs. Visually.

# TUIStudio — Design Terminal UIs. Visually.

## Overview
- Visual editor for terminal user interfaces (TUIs) that works like a Figma‑style drag‑and‑drop canvas.  
- Real‑time ANSI preview with configurable zoom.  
- One‑click export to six different TUI frameworks (currently in Alpha, export not functional yet).  

## Availability
- Native downloads for macOS (Apple Silicon) and Windows.  
- Docker image for cross‑platform use.  
- macOS Gatekeeper and Windows SmartScreen warnings can be bypassed by right‑click → Open (macOS) or “More info” → Run anyway (Windows).  
- Linux packages install directly via `dpkg` or file manager.  

## Core Features
- **Visual Canvas** – drag components onto a live canvas, see ANSI output instantly.  
- **20+ TUI Components** – Screen, Box, Button, TextInput, Table, List, Tree, Tabs, Modal, Spinner, ProgressBar, etc.  
- **Layout Engine** – supports Absolute, Flexbox, and Grid layouts with full property control, similar to CSS.  
- **8 Color Themes** – Dracula, Nord, Solarized, Monokai, Gruvbox, Tokyo Night, Nightfox, Sonokai; applied live on the canvas.  
- **Multi‑Framework Export** – targets Ink (TypeScript), BubbleTea (Go), Blessed (JavaScript), Textual (Python), OpenTUI (TypeScript), Tview (Go).  
- **Save / Load** – projects stored as portable `.tui` JSON files; can be opened from anywhere, version‑controlled, and shared without an account.  
- Additional UI tools: Command Palette, Theme Switcher, Component Toolbar.  

## Export Details
- Export generates production‑ready code for the selected framework.  
- Alpha notice: export functionality is still under development; will be available soon.  

## Component List (21 built‑in items)
- Screen, Box, Button, TextInput, Checkbox, Radio, Select, Toggle, Text, Spinner, ProgressBar, Table, List, Tree, Menu, Tabs, Breadcrumb, Modal, Popover, Tooltip, Spacer, plus more planned.  

## Frequently Asked Questions
- **What is a TUI?**  
  Interactive applications that run entirely in the terminal, built from characters, colors, and ANSI escape codes (e.g., `htop`, `lazygit`).  
- **Will macOS or Windows block the app?**  
  macOS Gatekeeper and Windows SmartScreen may block the unsigned binary; instructions are provided to open it safely.  
- **Why are exports not working?**  
  The product is in Alpha; export support is being implemented for the six listed frameworks.  
- **Is TUIStudio free?**  
  Core editor is free in early access; a paid Pro tier with team features and priority support is planned.  
- **Can I save and reopen designs?**  
  Yes, via portable `.tui` JSON files; no cloud or account required.  

## Getting Started
- Download the native app for macOS or Windows, or pull the Docker image.  
- No installation fuss: start designing immediately after download.