---
title: hails/wsl9x: Windows 9x subsystem for Linux - Codeberg.org
url: https://codeberg.org/hails/wsl9x
date: 2026-05-13
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-17T06:02:31.757873
---

# hails/wsl9x: Windows 9x subsystem for Linux - Codeberg.org

# WSL9x – Windows 9x Subsystem for Linux

## Overview
- Runs a modern Linux kernel (6.19) cooperatively inside the Windows 9x kernel.  
- Provides paging, memory protection, and pre‑emptive scheduling for both OSes.  
- Allows side‑by‑side use of Windows 9x and Linux applications without reboot.  
- Proudly written without AI assistance.

## Components
- Patched Linux kernel (branch `thewin9x-um-6.19`).  
- VxD driver (source in `vxd/`).  
- `wsl.com` client, a 16‑bit DOS program (source in `wsl/wsl.asm`).

## Driver responsibilities
- Initialise WSL9x, set up initial mappings for the kernel code and load `vmlinux.elf` from disk using DOS interrupts.  
- Allocate a 16 KiB stack, start a new thread in the System VM, and enter an event loop that:
  - Enters the kernel.  
  - Dispatches IRQs.  
  - Returns to userspace.  
  - Idles when idle.  
- Handle userspace events (page faults and syscalls).  
  - Syscalls are processed via the general‑protection‑fault handler because Win9x lacks a long enough IDT for `int 0x80`.  
  - The GPF handler detects `int 0x80`, advances the instruction pointer, and forwards the call to Linux.

## Linux kernel adaptation
- Based on User‑Mode Linux, modified to call Windows 9x kernel APIs instead of POSIX APIs.  
- Runs in ring 0 (supervisor mode) rather than ring 3.  
- Integration code lives in `linux/arch/um/os-Win95`.  
- Important entry points: `start.c`, `main.c`, `process.c`, `mmu.c`.

## wsl.com client
- Small 16‑bit DOS program that provides TTY windows via MS‑DOS prompts.  
- Calls `wsl9x_v86_api` in `vxd/console.c` to claim an unused console and notify WSL9x of output routing.  
- Enters an event loop that:
  - Waits for IRQs.  
  - Reads keyboard input when interrupted.  
  - Schedules output events and executes `int 0x29` in the MS‑DOS VM to write characters.  
- Compatible with ANSI drivers (e.g., NNANSI) that intercept `int 0x29` to implement escape codes.

## Building and running
- Install a cross‑toolchain targeting `i386-linux-musl` and ensure it is on `PATH` (e.g., via `musl-cross-make`).  
- Install Open Watcom v2 for the Windows components; set the `WATCOM` environment variable to its prefix (e.g., `/opt/watcom`).  
- Update the Linux submodule and build the patched kernel:  
  ```
  git submodule update --init
  make build-linux -j$(nproc)
  ```  
- Prepare a hard‑drive image `hdd.base.img` with Windows 9x pre‑installed.  
- Run `make` to produce `hdd.img` containing WSL9x.  
- At the MS‑DOS prompt, run `wsl` to open a PTY. Load an ANSI driver (e.g., `nnansi.com`) beforehand if colour support is desired.

## License
- GPL‑3