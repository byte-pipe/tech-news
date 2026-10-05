---
title: 'FTL: A new operating system for clouds'
url: https://ftl-os.org/
site_name: hackernews_api
content_file: hackernews_api-ftl-a-new-operating-system-for-clouds
fetched_at: '2026-10-05T12:19:45.255128'
original_url: https://ftl-os.org/
author: romac
date: '2026-10-04'
description: 'FTL: A new operating system for clouds'
tags:
- hackernews
- trending
---

## What's FTL?

* You canbuild your own OS as a library. This userspace OS design makes it easy to add features, debug, upgrade the OS safely, as if writing applications.
* FTL kernel isolates containers (userspace OS instances) better than existing monolithic kernels, witha hypervisor-like interfacebased on a lightweight hardware-based isolation (user mode). You don't need bare-metal machines.
* FTL iscompatible with Linux binaries. For example, the Rust-based HTTP server serving this website is a Linux application running on FTL. You can also run Unikernel-like specialized applications without POSIX abstractions.

## How it works

Each container runs a userspace OS. It is a shared library which implements most of OS concepts such as Linux process, VFS, and TCP/IP. FTL kernel provides a minimal interface to implement Linux system calls in userspace, just like a hypervisor.

FTL combines the best of microkernels (flexible & secure) and monolithic kernels (performant & simple). Our goal is tomake lightweight containers as secure as VMs, and unlock new OS-level abilities in applications, without sacrificing performance:

FTL Linux
┌────────────────────────────────┐ ┌────────────────────────────────┐
│┏━━━━━━━━━━━━━┓ ┏━━━━━━━━━━━━━┓│ │┏━━━━━━━━━━━━━┓ ┏━━━━━━━━━━━━━┓│
│┃ ┃ ┃ ┃│ │┃ ┃ ┃ ┃│
│┃ Linux ┃ ┃ Linux ┃│ │┃ Linux ┃ ┃ Linux ┃│
│┃ Process ┃ ┃ Process ┃│ │┃ Process ┃ ┃ Process ┃│
│┃ ┃ ┃ ┃│ │┃ ┃ ┃ ┃│
│┃╌╌╌╌╌ Linux system calls ╌╌╌╌╌┃│ │┗━━━━━━━━━━━━━┛ ┗━━━━━━━━━━━━━┛│
│┃ ┃│ └────────────────────────────────┘
│┃ Userspace OS ┃│ 
╌╌╌╌╌╌╌╌ 
Linux's interface
 ╌╌╌╌╌╌╌

│┃ (Process, VFS, TCP, ...) ┃│ ╔════════════════════════════════╗
│┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛│ ║ ║
└────────────────────────────────┘ ║ Linux Kernel ║

╌╌╌╌╌╌╌ 
minimal interface
 ╌╌╌╌╌╌╌╌
 ║ ║
╔════════════════════════════════╗ ║ process, fork/exec, memory, ║
║ FTL Kernel ║ ║ signals, TCP/IP, /proc, ║
║ vCPU, memory, drivers, ... ║ ║ /dev, drivers ... ║
╚════════════════════════════════╝ ╚════════════════════════════════╝

Userspace OS design also enables you to extend most of Linux kernel features without kernel/eBPF programming. You can add printfs, apply security updates, and add new features quickly and safely. In FTL,OS is just a library.Read more.

## Roadmap

* September 2026: Run a simple Linux HTTP server on FTL(released inv0.0.1✅)
* October 2026: Async Rust apps support - Linux threads, epoll, ...(released inv0.1.0✅)
* November 2026: Filesystem
* December 2026: Node.js / Go support
* January 2027: SMP, container images, 64-bit Arm support

## Links

* GitHub repository
* Introducing FTL: A new operating system for clouds (blog post)