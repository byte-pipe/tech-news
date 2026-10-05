---
title: FTL: A new operating system for clouds
url: https://ftl-os.org/
date: 2026-10-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-05T12:20:42.616675
---

# FTL: A new operating system for clouds

# FTL: A new operating system for clouds

## What is FTL?
- Userspace OS design lets you build an OS as a library, making feature addition, debugging, and safe upgrades similar to application development.  
- The FTL kernel isolates containers (userspace OS instances) with a hypervisor‑like interface that relies on lightweight hardware isolation; no bare‑metal machines are required.  
- Compatible with Linux binaries; existing Linux applications (e.g., a Rust HTTP server) run on FTL, and Unikernel‑style apps can run without POSIX abstractions.

## How it works
- Each container runs a userspace OS implemented as a shared library providing Linux‑like process, VFS, and TCP/IP functionality.  
- The FTL kernel offers a minimal interface for implementing Linux system calls in userspace, analogous to a hypervisor.  
- Combines microkernel flexibility and security with monolithic kernel performance and simplicity, aiming for VM‑level container security and new OS‑level capabilities for applications.  
- Extending kernel features does not require kernel or eBPF programming; you can add prints, security updates, and new features directly in the userspace OS library.

## Roadmap
- September 2026: Simple Linux HTTP server on FTL (released v0.0.1).  
- October 2026: Async Rust support – Linux threads, epoll, etc. (released v0.1.0).  
- November 2026: Filesystem implementation.  
- December 2026: Node.js / Go support.  
- January 2027: SMP, container images, 64‑bit Arm support.

## Links
- GitHub repository  
- Blog post: “Introducing FTL: A new operating system for clouds”