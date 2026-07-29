---
title: All News - Steel Bank Common Lisp
url: https://sbcl.org/all-news.html?2.6.7
date: 2026-07-28
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-29T12:31:01.294029
---

# All News - Steel Bank Common Lisp

# All News - Steel Bank Common Lisp

## Release schedule
- New SBCL versions are typically released at the end of each month; the current version list is available on the Sourceforge file list.  
- Versions span from **0.6.0** up to **2.6.7**, covering major and minor releases across the project's history.

## New in version 2.6.7 (2026‑07‑28)
- **SB‑MANUAL contrib module**: provides the SBCL manual as docstrings, searchable via tools like SLIME’s `M-.` and browsable with MGL‑PAX; alternative PDF/HTML/Markdown renderings are available.  
- **Documentation**: `DOCUMENTATION` now supports `DOC‑TYPE` declarations; docstrings conform to a Markdown subset; a separate index for declarations has been added.  
- **Platform support**:  
  - SB‑SIMD now supports ARM64.  
  - AVX512 instructions added for X86‑64.  
  - Expanded SIMD instruction support for both ARM64 and X86‑64.  
  - Fixed miscompilation of `SAP-REF-N` on ARM64.  
  - Implemented `INTEGER-LENGTH` for primitive types on MIPS and LoongArch.  
- **Bug fixes**:  
  - Suppressed spurious warnings when reading with `*READ‑SUPPRESS* T`.  
  - Resolved compiler type‑error for `CONCATENATE` with conditional non‑sequence arguments.  
  - Treated `(EQL <complex>)` types as numeric.  
  - Improved handling of quiet NaN inputs to `LOG`.  
  - Fixed miscompilation of `MULTIPLE‑VALUE‑CALL`.  
- **Optimizations**:  
  - Passing constant complex numbers to local functions no longer conses.  
  - Utilized enhanced SIMD routines for UTF‑8 conversions where possible.  
  - Broadened applicability of compiler transforms for `COUNT`.  
  - Removed redundant instruction from `SB-ALIEN:DEREF`.  
  - Tuned the compiler’s sparse set implementation for real‑world workloads.  
- **Documentation updates**: corrected many typos and typesetting issues; clarified that arrays in `SB-MANUAL:@FOREIGN‑FUNCTION‑INTERFACE` are row‑major.

## New in version 2.6.6 (2026‑06‑28)
- **Minor incompatible changes**:  
  - `FDEFINITION` now returns the outermost wrapper (e.g., added by `TRACE`, `PROFILE`).  
  - Unsafe C strings with `:EXTERNAL‑FORMAT :ASCII` are copied directly without top‑bit checks.  
- **Platform support**:  
  - Fixed build on big‑endian 64‑bit PowerPC with ELFv2.  
  - Adjusted static space address for macOS 27 on ARM64.  
  - Optimized `SB-THREAD:BARRIER` for ARM64.  
  - Resolved compiler crash in `MULTIPLE‑VALUE‑LIST` argument forms on ARM64.  
- **Bug fix**: `TRACE` no longer fails when printing a non‑readable return value under `*PRINT‑READABLY*`.  
- **Optimizations**:  
  - More precise type derivation for `COERCE`.  
  - Better return‑type inference for `AREF` and `ELT`.  
  - Faster UTF‑8 C‑string encoding/decoding.  
  - `(length (intersection a b))` now avoids creating an intermediate list.  
- **Documentation**: added a section for `SB-INTROSPECT`; numerous typesetting corrections and typo fixes.

## New in version 2.6.5 (2026‑05‑29)
- **Minor incompatible changes**:  
  - Errors for missing slots and uninitialized structure slots are no longer `TYPE‑ERROR`.  
- **Standardized set functions**: implementations of functions treating lists as sets (e.g., `INTERSECTION`, `UNION`) were updated (details truncated in source).