---
title: My favourite PowerMac is a Nintendo Wii | Virtually Fun
url: https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/
date: 2026-10-30
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-10-31T19:04:44.609110
---

# My favourite PowerMac is a Nintendo Wii | Virtually Fun

# My favourite PowerMac is a Nintendo Wii – Summary

## Project Overview
- Porting classic Mac OS (7.x – 9.x) to PowerPC “ArtX” chipsets: Nintendo GameCube, Wii, and eventually Wii U.  
- Achieved first‑time boot of Mac OS 7.6 and Mac OS 9.2.2 on a Wii, likely the first non‑Apple CHRP‑style classic‑Mac desktop on this hardware.  
- Project started 2025‑06‑22 after forking upstream OpenBIOS; all coding, reversing and debugging done manually (no AI assistance).  

## Motivation
- Prior work porting Windows NT to PowerPC Mac laptops sparked interest in classic Mac OS.  
- Fascination with the “jank” of classic Mac OS (layers of hacks dating back to the 1980s) and the legacy “SuperMario” m68k compatibility layer.  

## Initial Boot Process
- Classic Mac OS “New World” uses a bootloader called **Trampoline** that runs in Open Firmware.  
- Needed a custom OpenBIOS port; borrowed drivers from Goldfish64’s Wii OS X project but adapted them for GameCube as well.  
- Reused NT ARC firmware loader to load a big‑endian ELF image.  

## Disk Access Strategy
- Implemented two EXI‑bus drivers:  
  - **SD Gecko** – SD card via GameCube memory‑card slot (SPI).  
  - **EXI‑IDE** – Emulated IDE driver for testing in Dolphin emulator.  
- For early testing placed the Mac OS ROM TBXI file on a FAT partition as `ppc/bootinfo.txt` to satisfy OpenBIOS loading requirements.  

## Key Technical Challenges & Solutions
- **Physical address assumptions**: Trampoline expected memory‑mapped I/O starting at 0x8000_0000, which conflicted with Wii/Wii U RAM layout.  
  - Patched address calculations and created a valid MMIO mapping at physical 0x0100_0000 → virtual 0xE000_0000 (size 0x1000_0000).  
- **MMIO page‑table differences**: Older Trampoline versions used 16‑bit page counts; newer used 32‑bit. Added detection and hooking to handle both.  
- **Unwanted 1:1 mappings**: Removed automatic 1:1 physical‑to‑virtual mappings above 0x8000_0000 that clashed with custom mappings.  
- **Hardware‑specific flag patches**: Disabled bits related to Mac‑specific microcontroller, corrected bus‑frequency calculations, and fixed register writes for a PCI‑style interrupt controller not present on ArtX hardware.  
- **Device tree adjustments**:  
  - Faked an interrupt controller entry matching the expected little‑endian PCI controller.  
  - Updated framebuffer address to the uncached virtual region.  
  - Added a mock Mac99‑compatible power‑management node for the Trampoline’s driver preparation.  
- **Kernel interrupt controller patch**: Switched to the Flipper‑style controller, masked spurious PowerPC interrupts caused by the legacy mode, and unmasked them later in driver handlers.  
- **SuperMario m68k code**: Applied additional patches to handle direct accesses to native interrupt controller registers.  

## Current Status & Outlook
- Booting of Mac OS 7.6 and 9.2.2 on Wii is functional, though the system is not yet ready for public release.  
- Remaining work includes: refining disk image handling beyond FAT limits, polishing MMIO usage (potentially leveraging Wii U GPU “HDP” region), and completing driver support for full desktop operation.  

---  
*All information reflects the author’s perspective and technical narrative as presented in the original guest post.*