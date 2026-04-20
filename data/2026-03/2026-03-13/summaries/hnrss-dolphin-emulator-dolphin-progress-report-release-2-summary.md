---
title: Dolphin Emulator - Dolphin Progress Report: Release 2603
url: https://dolphin-emu.org/blog/2026/03/12/dolphin-progress-report-release-2603/
date: 2026-03-12
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-13T03:14:02.895910
---

# Dolphin Emulator - Dolphin Progress Report: Release 2603

# Dolphin Progress Report: Release 2603 Summary

## Overview
- Dolphin began as a GameCube emulator in 2003, added experimental Wii support in 2008, and in 2026 expands to arcade emulation with the Triforce system (a Sega‑Namco‑Nintendo collaboration).
- Emulating a new system for the first time in 18 years is highlighted as a major milestone.
- Two flagship improvements accompany the new platform support:
  1. **MMU emulation optimizations** that bring major performance gains for games using custom page‑table mappings.
  2. A **targeted fix** for a long‑standing physics bug in *Mario Strikers Charged*, achieved through community and CPU‑emulation expert collaboration.

## Notable Changes (Release 2603)

### Core – Fastmem Mappings for Page‑Table Addresses (2512‑285)
- “Fastmem” uses the host CPU’s exception handler to separate ordinary RAM accesses from MMIO accesses, allowing most memory operations to run at native speed.
- Previously Fastmem only covered Block Address Translation (BAT) mappings; page‑table‑based memory required costly manual translation.
- The new implementation adds Fastmem support for page‑table addresses, eliminating the performance penalty for games that rely on custom memory handlers.
- Result: all Full MMU games can now run at full speed on powerful hardware, notably *Rogue Squadron III: Rebel Strike*.

### MMU Speedhack & ARAM Utilization
- The GameCube’s 24 MiB of main RAM is supplemented by 16 MiB of Audio RAM (ARAM), which the CPU can only reach via DSP DMA transfers.
- Developers (e.g., Factor 5) historically configured page‑table entries to map invalid addresses, triggering page‑fault handlers that move data between main RAM and ARAM, effectively treating ARAM as extra RAM.
- Nintendo later provided a standardized library for this technique; Dolphin’s “MMU Speedhack” (enabled by default since 2014) emulates it by creating a BAT that points to additional host memory, bypassing the complex handling.
- Custom memory handlers appear in titles such as *Rogue Squadron II/III*, *Star Wars: The Clone Wars*, *Spider‑Man 2*, and *Ultimate Spider‑Man*. Proper page‑table emulation now enables these games to run faster.

### Wii‑Specific Cases
- On the Wii, ARAM is directly accessible as “MEM2”, but some games (the “Disney Trio of Destruction™”) replace default BATs with page‑table mappings for purposes like memory defragmentation.
- Dolphin now patches this behavior by default, ensuring correct emulation without performance loss.

### Mario Strikers Charged Physics Fix
- After years of frustration, the community combined with CPU‑emulation experts resolved a subtle physics bug that was previously impossible to reproduce or test, improving gameplay accuracy.

## Impact
- Full‑speed performance for all Full MMU titles on capable hardware.
- First arcade system emulation in Dolphin’s history, opening a new library of Triforce games.
- Significant compatibility and speed improvements across legacy GameCube and Wii titles that use custom memory handling.
- Enhanced stability and accuracy for *Mario Strikers Charged* and other titles affected by the physics bug.
