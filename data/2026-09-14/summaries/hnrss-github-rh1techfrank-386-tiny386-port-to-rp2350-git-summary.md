---
title: GitHub - rh1tech/frank-386: Tiny386 port to RP2350 · GitHub
url: https://github.com/rh1tech/frank-386
date: 2026-09-14
site: hnrss
model: llama3.2:1b
summarized_at: 2026-09-14T16:53:26.093726
---

# GitHub - rh1tech/frank-386: Tiny386 port to RP2350 · GitHub

Here is a concise and informative summary of the article:

**Introduction**
The article provides an overview of the `frank-386` firmware, a Tiny386 port for the Raspberry Pi Pico 2 (RP2350) board with various features and compatibility capabilities.

**Key Features**

* Full i386 CPU emulation with optional x87 FPU
* VGA and HDMI graphics output
* Support for audio output, SD card storage, and USB input keyboard and mouse
* NES/SNES gamepad support with mouse emulation mode
* Runtime disk manager and settings menu
* Support for various boards, including RP2350-based boards with integrated graphics

**Hardware Requirements**

* Raspberry Pi Pico 2 (RP2350) or compatible board
* 8MB PSRAM
* VGA or HDMI connector
* SD card module (SPI mode)
* PS/2 keyboard (directly connected) or USB keyboard via native USB port
* Audio output (optional)

**Comparison with Alternative Emulators**

* The article highlights that the `frank-386` firmware is designed for USB HID (Universal Serial Bus Hidden) mode, while other emulators use UART as the debug output interface.

**Supported Boards**

* List of specifically supported boards for this firmware.

**Conclusion**
The `frank-386` firmware is an alternative for development and running retro-emulators on the Raspberry Pi Pico 2 (RP2350) board, offering various features and options for compatible boards and peripherals.

**Repository Files Navigation**

* Path to the `README.md` file, which provides an overview of the firmware.

**Board Configurations**

* List of supported GPIO layouts for different boards, including M1, M2, PC (Olimex), and Z2 (Waveshare).