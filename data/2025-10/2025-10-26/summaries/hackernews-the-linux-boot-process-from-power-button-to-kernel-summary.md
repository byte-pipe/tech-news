---
title: The Linux Boot Process: From Power Button to Kernel | 0xkato
url: https://www.0xkato.xyz/linux-boot/
date: 2025-10-26
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-26T11:28:39.578304
screenshot: hackernews-the-linux-boot-process-from-power-button-to-kernel.png
---

# The Linux Boot Process: From Power Button to Kernel | 0xkato

Here is a concise and informative summary of the article:

## Introduction to the Linux Boot Process
The process begins when a user presses the power button, triggering a sequence of events that leads to the loading of the Linux operating system.

### Key Aspects of the Boot Process

- **Power Button Press**: A second later, a window or logo appears, indicating that the system has booted.
- **Real Mode Reset**: The CPU resets to real mode, which is an older programming style that dates back to the 8086 chip. This allows for memory addresses in hexadecimal format.
- **Bootloader Sequence**: Immediately after resetting, the CPU jumps to a special address called the boot vector at `0xFFFFFFF0`, marking the start of the bootloader sequence.

### The Boot Process

1. **BIOS and UEFI**: Two different firmware structures exist: BIOS (Basic Input Output System) is an older legacy system, while UEFI (Unified Extensible Firmware Interface) is a modern replacement that can understand filesystems directly.
2. **BOOT Loader**: The bootloader is the intermediate stage between the BIOS or UEFI jump point and the loading of Linux.

## Additional Facts

- **Register Names**: Registers are tiny slots inside the CPU where numbers are held using hexadecimal format (e.g., `0x10`).
- **Reset Vector**: A permanent bookmark at address `0xFFFFFFF0` marks the startup location for the bootloader sequence.
- **GRUB as Bootloader**: GRUB is a popular boot loader on PCs that reads its configuration, shows menu options if installed, and loads Linux in memory.
