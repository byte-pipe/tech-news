---
title: The Deathray: A simple way for an untrusted site to freeze a Mac
url: https://auberon.xyz/blog/posts/deathray/
date: 2026-09-11
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-12T01:23:16.970101
---

# The Deathray: A simple way for an untrusted site to freeze a Mac

# The Deathray: A simple way for an untrusted site to freeze a Mac

## TL;DR
- A WebGPU shader on an untrusted website can hang the Mac’s GPU, rendering the desktop UI unusable until a forced restart.
- The victim only needs to click a link.
- The issue appears on macOS across Chrome, Firefox, and Safari, but not on other operating systems.

## Scope
- Reproduced on M‑series MacBooks running macOS (Tahoe build) in Chrome, Firefox, and Safari.
- Not observed on Windows, Linux, or other non‑macOS platforms.

## How does it work?
- Uses WebGPU, a modern graphics API that lets sites submit shaders to the GPU.
- **Compute shader** contains an infinite busy‑loop that repeatedly copies data in a buffer.
- **Vertex shader** reads from the same buffer that the compute shader is monopolizing.
- The vertex shader stalls, causing the GPU to become saturated.
- The saturation propagates to system processes that rely on the GPU, notably WindowServer, making the UI unresponsive.
- The rest of the system remains reachable (e.g., via SSH); a watchdog eventually triggers a kernel panic and restart if WindowServer does not recover.

## Precedent
- 2023: “ShadyShader” (WebGL) exploited a similar runaway‑loop GPU hog, leading to CVE‑2023‑40441 (medium severity) and Apple’s input‑validation improvements.
- WebGPU’s validation appears weaker; infinite loops are fundamentally hard to detect due to the halting problem.
- Apple’s GPU pre‑emption on M‑series chips relies on the ASC coprocessor firmware, complicating mitigation.

## How the deathray was discovered
- Accidentally created an infinite loop while learning WebGPU at the Recurse Center.
- Observed the computer hang and confirmed reproducibility.

## Disclosure
- Reported to Apple Security on 2026‑07‑27; Apple initially reproduced and promised a fix (details confidential).
- On 2026‑08‑26 Apple stated the issue has no security implications and will be sent to another team for “potential enhancement,” suggesting low priority.
- Researchers argue the impact (system hang from a simple link) feels like a security concern to many users.

## What the author hopes to see
- Recognition that, while not a sandbox escape or data breach, the attack’s low barrier makes it a practical annoyance.
- A fix that preserves WebGPU functionality rather than disabling it by default.
- Responsible, non‑malicious experimentation (e.g., games that intentionally freeze the Mac with user consent).