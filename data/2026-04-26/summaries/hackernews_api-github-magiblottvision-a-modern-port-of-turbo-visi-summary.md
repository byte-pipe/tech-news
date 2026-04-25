---
title: GitHub - magiblot/tvision: A modern port of Turbo Vision 2.0, the classical framework for text-based user interfaces. Now cross-platform and with Unic...
url: https://github.com/magiblot/tvision
date: 2026-04-25
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-26T06:01:35.315837
---

# GitHub - magiblot/tvision: A modern port of Turbo Vision 2.0, the classical framework for text-based user interfaces. Now cross-platform and with Unic...

# Turbo Vision (magiblot/tvision) – Modern Port of Turbo Vision 2.0

## Project overview
- A cross‑platform, Unicode‑enabled rewrite of the classic Turbo Vision text‑UI framework.
- Started in late 2018; reached feature parity with the original by May 2020 and later added full Unicode support.
- Goals:
  - Run Turbo Vision on Linux with minimal changes to the legacy code.
  - Preserve functionality on DOS/Windows.
  - Maintain source‑level compatibility with existing Turbo Vision applications (including Borland C++ RTL functions).

## Main advantages
1. **Abstracts terminal details** – developers focus on UI behavior; Turbo Vision handles terminal capabilities, colors, and attributes automatically.
2. **Rich widget set** – provides resizable windows, menus, dialogs, buttons, scrollbars, input fields, checkboxes, radio buttons, etc., with event dispatching and Unicode rendering already implemented.
3. **Out‑of‑the‑box cross‑platform** – same code runs on Linux and Windows without `#ifdef`s; uses UTF‑8 and standard `char` arrays, leveraging modern RTL conversions.

## Getting started
- Read the *Turbo Vision For C++ User's Guide* and explore sample programs (`hello`, `tvdemo`, `tvedit`).
- For deeper insight, consult the *Turbo Vision 2.0 Programming Guide* (Pascal‑based) and the `palette` example for palette handling.
- Review the **Features** and **API changes** sections for recent enhancements.

## Releases & binaries
- No stable releases yet; developers should use the latest commit.
- Pre‑built demo binaries are available in the GitHub Actions artifacts:
  - `examples-dos32.zip` – 32‑bit Borland C++ (no Unicode).
  - `examples-x86.zip` – 32‑bit MSVC (Windows Vista+).
  - `examples-x64.zip` – 64‑bit MSVC (Windows Vista+).

## Building the library

### Linux
```bash
cmake -B ./build -DCMAKE_BUILD_TYPE=Release .
cmake --build ./build
```
- Produces `libtvision.a` and demo executables (`hello`, `tvdemo`, `tvedit`, `tvdir`, `mmenu`, `palette`, `tvhc`).
- Requirements:
  - C++14 compiler, `libncursesw`, optional `libgpm` (mouse).
  - Development packages (e.g., `libncurses-dev`, `libgpm-dev`).
- Runtime:
  - `xsel`/`xclip` (X11 clipboard) or `wl-clipboard` (Wayland).

### Windows (MSVC / MinGW) and DOS (Borland C++)
- Build instructions are analogous using CMake; binaries are provided in the Actions artifacts.

## Notable features
- Full Unicode (UTF‑8) support integrated without breaking the original architecture.
- Clipboard interaction via external tools.
- Extended color handling beyond the original limited palette.

## Compatibility notes
- Include paths may need adjustments:
  - `-Iinclude/tvision` for TV 1.x style includes.
  - `-Iinclude/tvision/compat/borland` for Borland‑specific headers.
- On some systems (e.g., Gentoo) linking with `-ltinfow` may be required to avoid segmentation faults.