---
title: GitHub - boykopovar/AnyPS5: Tool for automatic PS5 executables porting to Linux and Windows · GitHub
url: https://github.com/boykopovar/AnyPS5
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-10-06T16:49:10.613413
---

# GitHub - boykopovar/AnyPS5: Tool for automatic PS5 executables porting to Linux and Windows · GitHub

# AnyPS5 – Automatic PS5 Executable Porting Tool

## Overview
- Tool that automatically ports PS5 executables to Linux and Windows.  
- Includes a linker that converts executables to the target system’s native format.  
- Provides implementations of system PRX libraries for dynamic linking.  
- Operates without emulation or a separate runtime process.

## Repository Details
- Public repository owned by **boykopovar**.  
- 1,997 commits, 5.1 k stars, 374 forks.  
- Main branch: `main`.  
- Key directories: `.github`, `3rdparty`, `core`, `docs`, `tools`.  
- Important files: `CMakeLists.txt`, `CONTRIBUTING.md`, `LICENSE`, `README.md`.

## Features & Technical Highlights
- Shader recompilation to SPIR‑V, validated with Spirv‑Tools when built with `ANYPS5_ENABLE_SPIRV_TOOLS`.  
- SDL‑mapped game controller support (analog sticks, triggers); keyboard and mouse configurable via `anyps5-input.ini`.  
- Errors throw `std::runtime_error`; message printed to stderr and the process terminates.

## Current Status
- System library coverage shown as a percentage of known functions (declared in `core/libs/prx`); coverage grows as more functions are added.  
- Verified game: *Dreaming Sarah* runs stable at 60 fps on a GTX 1050 Ti / i5‑7500 system.  
- Compatibility list available for tested games and known issues.

## Compatibility & Requirements
- Tested on Linux and Windows.  
- Requires compatible graphics hardware and drivers for SPIR‑V shaders.  

## Disclaimer
- Intended for interoperability, research, preservation, and compatibility purposes.  
- Does not include, distribute, or require copyrighted software, firmware, cryptographic keys, or proprietary libraries.  
- Users are responsible for ensuring that any binaries used comply with applicable laws and license terms.

## License
- Distributed under the GNU General Public License version 2 only.