---
title: OpenBSD Jumpstart | bsd.rd
url: https://openbsdjumpstart.org/bsd.rd/
date: 2026-02-18
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-18T06:01:39.283491
---

# OpenBSD Jumpstart | bsd.rd

# OpenBSD Jumpstart | bsd.rd

This lab explores the contents of `bsd.rd`, the file used for booting OpenBSD, without requiring a reboot. It reveals that `bsd.rd` is a collection of nested layers, accessible and inspectable on a running system. The process involves decompressing the gzip file, extracting the ELF kernel binary, and then extracting the embedded RAM disk image (miniroot).

## Key Points:

*   `bsd.rd` is a gzip-compressed file containing the kernel and a RAM disk image.
*   The kernel is an ELF binary with a reserved space for the miniroot filesystem.
*   The miniroot is an FFS filesystem containing the complete root filesystem needed for booting.
*   `rdsetroot` is a command-line tool used to manipulate the RAM disk image, including extracting and inserting it.
*   The `install.sub` script within the miniroot handles install, upgrade, and auto-install processes, dynamically adapting to the OpenBSD release and architecture.
*   The `.profile` script is executed after the kernel boots, determining the boot mode and presenting the user with options like install, upgrade, or shell.
*   The miniroot includes a basic set of tools for system installation and maintenance.

## Steps:

1.  **Decompress `bsd.rd`:** The gzip compression is removed to reveal the underlying ELF kernel binary.
2.  **Examine the ELF Header:** The header provides information about the binary format, architecture, and entry point.
3.  **Determine RAM Disk Size:** `rdsetroot -s bsd.rd` reveals the reserved space for the miniroot, approximately 3.6 MB.
4.  **Extract the Miniroot:** `rdsetroot -x bsd.rd miniroot.fs` extracts the FFS filesystem image.
5.  **Mount and Explore the Miniroot:** The extracted `miniroot.fs` is mounted to access its contents, revealing a minimal root filesystem with essential directories and scripts.

## Tools Used:

*   `rd(4)`: The RAM disk driver.
*   `rdsetroot(8)`: Tool for manipulating the RAM disk image.
*   `vnconfig(8)`: Configures virtual node devices.
*   `vnd(4)`: Virtual node device driver.
*   `disklabel(8)`: Displays disk label information.
*   `elf(5)`: Describes the ELF file format.
