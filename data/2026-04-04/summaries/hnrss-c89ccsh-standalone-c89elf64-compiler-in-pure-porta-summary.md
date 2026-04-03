---
title: c89cc.sh - standalone C89/ELF64 compiler in pure portable shell · GitHub
url: https://gist.github.com/alganet/2b89c4368f8d23d033961d8a3deb5c19
date: 2026-04-01
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-04T01:03:45.311569
---

# c89cc.sh - standalone C89/ELF64 compiler in pure portable shell · GitHub

# c89cc.sh – Standalone C89/ELF64 Compiler in Pure Portable Shell  

## Overview  
- A single‑file shell script that parses and compiles C89 source code directly to a 64‑bit ELF executable for x86‑64.  
- Written entirely in POSIX‑compatible `/bin/sh` with no external binaries required; it builds its own minimal libc unless `--no-libc` is specified.  

## License & Authorship  
- ISC License (permissive, similar to BSD).  
- Copyright © 2026 Alexandre Gomes Gaigalas (alganet).  

## Basic Usage  
- Compile a program: `sh c89cc.sh < prog.c > a.out`  
- Skip the built‑in libc: `sh c89cc.sh --no-libc < prog.c > a.out`  

## Design Highlights  

### Self‑Contained Execution  
- Clears `PATH` and relies only on built‑in shell features.  
- Provides fallbacks for shells lacking certain built‑ins (e.g., `local`, `test`).  
- Detects the best available output primitive (`printf`, `print`, `echo`) and defines `_printn1` / `_printr1` wrappers.  

### Helper Infrastructure  
- **Multi‑value return**: Functions pack assignments into the global `REPLY` variable; callers unpack with `eval "$REPLY"` or `eval "local$REPLY"`.  
- **Dynamic locals**: `_retv` and `_retva` create variable assignments for later evaluation.  

### Module System (inlined)  
- Stubbed module loader (`use`, `_mod_has`, `_mod_add`) that simply includes all code in the single script.  

### Core Modules  

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| `str/repeat.sh` | Repeat a string N times using exponentiation‑by‑squaring. | `_repeat` |
| `str/core.sh` | String case conversion and utilities. | `_ucase`, `_lcase`, `_lcase_str` |
| `io/readall.sh` | Read entire stdin into `REPLY` (cat replacement). | `_readall` |
| `pos/core.sh` | Position tracking and JSON number validation. | `_nlcount`, `_numck` |

- Additional helpers include a memoized pattern generator (`_questn`) for splitting long input lines.  

## Implementation Notes  
- Uses strict shell options: `set -euf`, forces `LC_ALL=C`, and defines custom IFS and newline/tab variables.  
- Provides compatibility shims for Bash, Zsh, Ksh, and mksh.  
- All functions are defined with careful quoting to avoid word‑splitting and globbing issues.  

## Limitations & Extensibility  
- Generates only ELF64 binaries for the x86‑64 architecture.  
- Built‑in libc is minimal; complex runtime features may require the `--no-libc` option and linking against an external C library.  
- The script is deliberately verbose to remain portable across many POSIX shells.