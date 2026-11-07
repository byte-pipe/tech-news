---
title: Libghostty 1.0 – Mitchell Hashimoto
url: https://mitchellh.com/writing/libghostty-1-0
date: 2026-11-07
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:03:38.637102
---

# Libghostty 1.0 – Mitchell Hashimoto

# Libghostty 1.0 – Mitchell Hashimoto

## Overview
- libghostty‑vt 1.0 is a portable, high‑performance C library for terminal emulation extracted from Ghostty.  
- Both the library and its C ABI are now stable, following semantic versioning.  
- The release includes full build tooling, packaging assets, documentation, and a strict ABI‑stability policy.

## Who Is Already Using It
- JetBrains IDEs (IntelliJ, PyCharm, GoLand, etc.) switched their terminal to libghostty, reaching over 12.5 million active users.  
- Neovim has an approved PR to replace libvterm with libghostty‑vt, awaiting the tagged release for packaging.  
- KDE developers are prototyping a Konsole replacement; Vercel’s Turborepo, devenv, Antithesis, Ghostel (Emacs), ghostty‑web (WASM), OrbStack, and many “agentic” coding tools already embed it.  
- Community bindings exist for Rust, Go, JavaScript, Swift, Python, .NET, Elixir, Dart, Java, etc.; the awesome‑libghostty list tracks > 100 projects.  
- More terminals run on libghostty than the Ghostty application itself.

## ABI Stability
- libghostty‑vt guarantees ABI compatibility across releases; packagers and developers can rely on dynamic linking.  
- All objects are opaque handles accessed via enum‑keyed getters/setters, allowing new fields without new symbols.  
- Newer headers linked against older binaries receive `GHOSTTY_UNSUPPORTED` instead of crashes.  
- Non‑opaque structs carry size information; enums are pinned to integer values.  
- CI checks ABI changes with `libabigail` (Linux) and golden type manifests (macOS, WASM).  
- Exported symbols on ELF are versioned, preventing mismatched loading.

## Packaging
- Separate release cycle from the Ghostty application, with smaller tarballs containing only libghostty files and dependencies.  
- Each release provides a signed source tarball and a dependencies tarball (Zig cache layout) for fully offline builds.  
- Build installs shared/static libraries, headers, pkg‑config files, and a CMake config; respects `--prefix`, `DESTDIR`, and `lib64`.  
- Debug information is retained by default for distro split‑out.  
- Detailed instructions are in `PACKAGING-LIBGHOSTTY.md`.

## Dependencies and Licensing
- libghostty‑vt is MIT‑licensed; at runtime it only needs `libc` and can be built freestanding.  
- Permissive dependencies: `simdutf`, Google `Highway` (SIMD), a compact Unicode grapheme table, and `Wuffs` for Kitty graphics image decoding.  
- No copyleft code in the dependency tree; all dependencies are listed in a machine‑readable manifest with version, SPDX license, and hash.  
- Optional build flag allows dynamic linking to system `simdutf` or `Highway`.

## Portability
- Tested CI platforms (full unit tests + examples):
  - Linux (glibc, musl): x86_64, aarch64  
  - macOS 13+: x86_64, aarch64  
  - iOS 13+: aarch64  
  - FreeBSD: x86_64, aarch64  
  - Windows: x86_64  
  - Android: aarch64, x86_64, arm  
  - WebAssembly (freestanding): wasm32
- Additional CI‑built but untested platforms with known users:
  - Bare metal: riscv32, thumb  
  - WebAssembly (WASI): wasm32  
  - Windows arm64, illumos (x86_64), 32‑bit x86 (x86)
- Artifact details per platform:
  - Linux/FreeBSD: shared library with SONAME, versioned symbols, static library, headers, pkg‑config, CMake config.  
  - macOS/iOS: dylib with `@rpath` install name, compatibility version, XCFramework covering macOS, iOS, and simulator.  
  - Windows: DLL with `.pdb`, import library, static library; built with GNU ABI, MSVC linking verified.  
  - Android: NDK‑built shared library supporting 16 KB page size (Android 15+).  
  - WebAssembly: speed‑optimized and size‑optimized builds; size‑optimized < 1 MiB with all features; optional compile‑time flags can strip subsystems, returning `GHOSTTY_UNSUPPORTED` for removed functions.  

- Portability also covers resource usage, enabling operation in constrained environments.