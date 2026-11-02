---
title: Linux System Call Tables by Architecture · syscall.sh
url: https://syscall.sh/
date: 2026-11-02
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-03T06:08:50.432246
---

# Linux System Call Tables by Architecture · syscall.sh

# Linux System Call Tables by Architecture

## Overview
- Central collection of every Linux system call table, grouped by 27 architectures.  
- Covers kernel versions from 3.3 up to 7.3.  
- For each architecture the table includes syscall numbers, argument registers, and a full history (when each syscall was added or removed).  
- Full history is available as a plain JSON file at `<arch>/syscalls.json` (e.g., `x64/syscalls.json`).

## Architectures
- **x86_64** – 369 syscalls (since 3.3)  
- **i386** – 441 syscalls (since 3.3)  
- **arm64** – 326 syscalls (since 3.7)  
- **arm** – 426 syscalls (since 4.10)  
- **riscv64** – 327 syscalls (since 4.15)  
- **ia32** (IA‑32 compat on x86_64) – 439 syscalls (since 3.3)  
- **x32** (x32 ABI on x86_64) – 369 syscalls (since 3.4)  
- **loongarch64** – 323 syscalls (since 5.19)  
- **ppc64** – 383 syscalls (since 5.0)  
- **ppc** – 425 syscalls (since 5.0)  
- **s390x** – 378 syscalls (since 4.16)  
- **mips64** (n64 ABI) – 363 syscalls (since 5.0)  
- **mipsn32** (n32 ABI) – 387 syscalls (since 5.0)  
- **mipso32** (o32 ABI) – 413 syscalls (since 5.0)  
- **alpha** – 403 syscalls (since 5.0)  
- **arc** – 350 syscalls (since 3.9)  
- **csky** – 346 syscalls (since 4.20)  
- **hexagon** – 345 syscalls (since 3.7)  
- **m68k** – 435 syscalls (since 5.0)  
- **microblaze** – 423 syscalls (since 5.0)  
- **nios2** – 346 syscalls (since 3.19)  
- **openrisc** – 346 syscalls (since 3.7)  
- **parisc** – 404 syscalls (since 5.0)  
- **sh** – 433 syscalls (since 5.0)  
- **sparc** – 434 syscalls (since 5.0)  
- **sparc64** – 399 syscalls (since 5.0)  
- **xtensa** – 388 syscalls (since 5.0)

## Calling Conventions
- Each architecture entry lists:
  - Instruction that enters the kernel.  
  - Register holding the syscall number (NR).  
  - Register for the return value (RETURN).  
  - Registers for up to six arguments (ARG0‑ARG5).  

Example excerpt:

- **x86_64**  
  - Instruction: `syscall`  
  - NR: `rax`  
  - RETURN: `rax`  
  - ARG0‑ARG5: `rdi, rsi, rdx, r10, r8, r9`  

- **arm64**  
  - Instruction: `svc #0`  
  - NR: `x8`  
  - RETURN: `x0`  
  - ARG0‑ARG5: `x0, x1, x2, x3, x4, x5`  

(Full table is provided for all architectures on the site.)

## API
- Accessible via `https://api.syscall.sh/v2/syscalls/<arch>/read`.  
- Supports queries for any kernel release, differences between releases, and other details as described in the API documentation.

## Version History
- Each syscall entry records:
  - `since` – kernel release where the syscall first appeared.  
  - `removed_in` – release where it was dropped (if applicable).  
- Removed syscalls remain visible when the kernel selector is set to “all, with removed,” and are marked with the dropping release.

## Data Source
- All data is extracted directly from the Linux kernel source:
  - The generator parses syscall tables and `SYSCALL_DEFINE` macros across every mainline release.  
  - Calling conventions are derived from the kernel entry instruction.  
- Short descriptions are taken from the Linux man‑pages project; io_uring descriptions come from liburing.  
- The site rebuilds automatically whenever the underlying data changes.