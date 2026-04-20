---
title: picoZ80 - engineers@work
url: https://eaw.app/picoz80/
date: 2026-04-10
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-11T06:01:35.290319
---

# picoZ80 - engineers@work

# picoZ80 Summary

## Overview
- Replaces a physical Z80 CPU with an RP2350B microcontroller that runs up to 300 MHz, providing faster processing, more memory, virtual devices, Wi‑Fi/Bluetooth, and rapid loading from SD card.
- The board plugs directly into the Z80 DIP‑40 socket; RP2350’s PIO state machines deliver cycle‑accurate Z80 bus timing, so the host sees the same behavior as with a real Z80.
- RP2350’s second core, 512 KB SRAM, 8 MB external PSRAM, and 16 MB Flash enable features such as accelerated execution, virtual memory, ROM banking, virtual disk drives, and full machine‑persona emulation.
- An ESP32 co‑processor supplies Wi‑Fi/Bluetooth, SD‑card storage, and a browser‑based management interface; all configuration is done via a human‑readable `config.json` on the SD card, eliminating recompilation.
- Demonstrated in Sharp MZ series; personas are being created for MZ‑700, MZ‑80A/B, MZ‑800, and later for other Z80 machines (e.g., Amstrad PCW).
- Key capabilities:
  - Drop‑in Z80 replacement with authentic bus timing.
  - Cycle‑accurate PIO bus interface using three RP2350 PIO engines.
  - 8 MB PSRAM organized as 64 × 64 KB banks (4 MB banked address space per CPU context).
  - Configurable 512‑byte memory blocks for ROM, RAM, host memory, or virtual handlers.
  - Virtual device framework allowing any memory/I/O block to be backed by C functions.
  - Floppy (WD1773) and QuickDisk emulation using DSK/RAW images on SD card.
  - Wi‑Fi web management with a seven‑page Bootstrap UI for configuration, file handling, OTA updates, and persona selection.
  - Dual 5 MB firmware partitions for safe OTA upgrades, selectable via web UI or bootloader.
  - USB bridge for firmware flashing without a hardware debugger.

## Hardware
- **Form factor:** Multi‑layer PCB (revision 2.5) fits within the Z80 DIP‑40 footprint; all logic runs at 3.3 V with level shifting for the 5 V host bus.
- **Subsystems integrated:** RP2350B processor, Z80 bus interface, ESP32 co‑processor, power supply, USB hub.

### Key Components
- **RP2350B (Cortex‑M33 dual‑core):** Core 1 runs the Z80 emulation hot loop; Core 0 handles file I/O, USB, and ESP32 communication. 512 KB on‑chip SRAM; 48 GPIO pins needed for full Z80 bus.
- **16 MB SPI Flash:** Holds bootloader, two firmware slots, configuration data, and general storage (address range 0x10000000–0x11000000).
- **8 MB PSRAM (SPI):** Provides 64 banks × 64 KB of banked address space for the emulated CPU.
- **ESP32‑S3 co‑processor:** Wi‑Fi (b/g/n, AP/client), Bluetooth, SD‑card reader, web server; communicates with RP2350 via 50 MHz FSPI (with CRC32) and 460.8 kbaud UART.
- **SD‑card slot:** FAT32, stores `config.json`, ROM images, disk images, and filing system trees.
- **USB hub (CH334F):** Mini‑B connector, downstream ports for host connectivity and firmware update bridging.
- **3.3 V buck converter (TLV62590BV):** Steps down 5 V from the Z80 socket to supply all on‑board components.

### Board Design
- Designed in KiCad; schematic split into five sheets covering RP2350B, ESP32, Z80 bus interface, power supply, and USB hub controller.
- Sheet 1: RP2350B GPIO assignments, crystal, Flash, PSRAM connections.
- Sheet 2: ESP32‑S3‑PICO‑1 module, SD‑card SPI, antenna, debug header, IPC lines.
- Sheet 3: Z80 bus interface with series resistors routing address, data, and control signals to RP2350 GPIOs monitored by PIO state machines.
- Sheet 4: 5 V‑to‑3.3 V synchronous buck converter with filtering.
- Sheet 5: USB hub controller with Mini‑B connector and downstream ports.
- PCB uses 0402/0603 passive components, 0.5 mm IC pitch, 6‑layer stackup; manual assembly performed for early revisions (v2.0, v2.1).
