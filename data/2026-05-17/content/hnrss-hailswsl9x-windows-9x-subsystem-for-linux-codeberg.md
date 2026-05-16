---
title: 'hails/wsl9x: Windows 9x subsystem for Linux - Codeberg.org'
url: https://codeberg.org/hails/wsl9x
site_name: hnrss
content_file: hnrss-hailswsl9x-windows-9x-subsystem-for-linux-codeberg
fetched_at: '2026-05-17T06:01:10.380925'
original_url: https://codeberg.org/hails/wsl9x
author: hails
date: '2026-05-13'
description: wsl9x - Windows 9x subsystem for Linux
tags:
- hackernews
- hnrss
---

hails
/
wsl9x

Watch

			17
		

Star

			313
		

Fork

				You've already forked wsl9x
			

			5
		

Windows 9x subsystem for Linux

* Assembly71.4%
* C27.4%
* Makefile1.2%

main

Find a file

		HTTPS
	

Hailey Somerville

fdd52532a3

fix mistaken movzx instruction that errors on nasm 2.x

2026-05-06 20:33:29 +10:00

bin
									
								

it loads!

2026-04-13 23:15:09 +10:00

ddk
									
								

fix vxdjmp macro, use vxdjmp in dev_vmm_cproc

2026-04-18 10:48:19 +10:00

inc
									
								

very messy but it does spawn sh on a console

2026-04-21 19:00:21 +10:00

linux
@
ed0b43584c

add linux as submodule

2026-04-23 18:26:33 +10:00

vxd
									
								

fix mistaken movzx instruction that errors on nasm 2.x

2026-05-06 20:33:29 +10:00

wsl
									
								

remove more dead code

2026-04-24 22:15:05 +10:00

.envrc.example

simplify build instructions now that linux is a submodule

2026-04-23 18:37:31 +10:00

.gitignore

just vendor fixlink

2026-04-21 19:01:32 +10:00

.gitmodules

add linux as submodule

2026-04-23 18:26:33 +10:00

bochs.bxrc

it loads!

2026-04-13 23:15:09 +10:00

config.sys

it loads!

2026-04-13 23:15:09 +10:00

fixlink.c

just vendor fixlink

2026-04-21 19:01:32 +10:00

Makefile

roll v86_api.c into console.c

2026-04-23 23:16:31 +10:00

mtoolsrc

it loads!

2026-04-13 23:15:09 +10:00

README.md

roll v86_api.c into console.c

2026-04-23 23:16:31 +10:00

screenshot.png

add readme, screenshot, example envrc

2026-04-22 15:47:36 +10:00

system.ini

it loads!

2026-04-13 23:15:09 +10:00

#### README.md

# WSL9x

Windows 9x Subsystem for Linux.

WSL9x runs a modern Linux kernel (6.19 at time of writing) cooperatively inside the Windows 9x kernel, enabling users to take advantage of the full suite of capabilities of both operating systems at the same time, including paging, memory protection, and pre-emptive scheduling. Run all your favourite applications side by side - no rebooting required!

Proudly written without AI.

## Technical details

WSL9x is made up of three components: a patched Linux kernel (see thewin9x-um-6.19branch), a VxD driver, and awsl.comclient program.

The driver is responsible for the initialisation of WSL9x (seevxd/wsl9x.asmfor the driver entry point). It sets up the initial mappings for the kernel code and loadsvmlinux.elfoff disk using DOS interrupts (seevxd/loader.candvxd/fs.asm). The kernel is compiled with a fixed base address of0xd0000000.

The driver then starts a new thread in the System VM, allocates a 16 KiB stack for entering Linux on, and drops into an event loop which handles entering the kernel, dispatching IRQs, returning to userspace, and idling. Seevxd/entry.cfor this code.

The driver is also responsible for handling userspace events which must be dispatched to the kernel, currently page faults and syscalls. Syscalls are handled via the general protection fault handler, as Win9x does not have an interrupt descriptor table long enough to install a proper handler forint 0x80- the Linux i386 syscall interrupt. Instead, the GPF handler inspects the faulting instruction. If it'sint 0x80, the GPF handler advances the instruction pointer as if the interrupt succeeded and dispatches as a syscall to Linux. Seevxd/fault.cfor this code.

The Linux kernel is based on user-mode Linux, but hacked to call Windows 9x kernel APIs instead of posix APIs, and running in ring 0 (supervisor/kernel mode) rather than ring 3 (user mode). Much of the actual Win9x kernel integration including context switching lives in the Linux kernel. Seelinux/arch/um/os-Win95for the bulk of the Linux-side code. The entry point called by vxd/entry.c is_startinmain.c.process.candmmu.care also important.

The last piece is thewsl.comclient. This is a small 16 bit DOS program implemented inwsl/wsl.asmwhich exists to allow WSL9x to use MS-DOS prompts as TTY windows rather than needing to implement something custom.

Whenwsl.comstarts, it makes an initial call intowsl9x_v86_apiinvxd/console.cto claim an unused console and notify WSL9x that output for that console should be dispatched to it. Then it drops into an event loop waiting for an IRQ and attempting to read from the keyboard when interrupted. The top of this event loop also serves as a synchronisation point for the console driver - when output from Linux is ready, it schedules an event and executesint 0x29in the context of the MS-DOS VM to output chars to the DOS window. This interrupt is also where an ANSI driver for DOS such as NNANSI is able to intercept the terminal output to implement ANSI escape codes.

## Building and running

* You will need a cross toolchain targetingi386-linux-muslon PATH. Usemusl-cross-maketo build one
* You will need the Open Watcom v2 toolchain for building the Windows components. Set theWATCOMenv var to the prefix where you installed it. On my machine, that's/opt/watcom.
* Build the patched Linux kernel. This is a manual step because building the kernel takes quite a long time.$git submodule update --init# make sure linux submodule is up to date$make build-linux -j$(nproc)
* You will need a hard drive imagehdd.base.imgwith Windows 9x pre-installed
* Runmake- this will produce a newhdd.imgwith WSL9x ready to go.
* Runwslat the MS-DOS prompt to open a pty. If you'd like to use ANSI colours, make sure you have an appropriate driver loaded before runningwsl.nnansi.comis a good option.

## License

GPL-3