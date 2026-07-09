---
title: Announcing TypeScript 7.0 - TypeScript
url: https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/
date: 2026-07-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-09T15:20:14.065967
---

# Announcing TypeScript 7.0 - TypeScript

# Announcing TypeScript 7.0 – TypeScript

## Overview
- Daniel Rosenwasser, Principal Product Manager, announces TypeScript 7, a native Go port delivering 8‑12× faster compilation.
- The new codebase preserves the original logic while adding native speed, shared‑memory multithreading, and additional optimizations.
- Available via npm (`npm install -D typescript`) which provides the new `tsc` executable.

## Editor Integration
- Supports the Language Server Protocol (LSP) with improved speed and multithreading.
- Compatible with VS Code, Visual Studio, WebStorm, and other modern editors; VS Code offers a dedicated TypeScript 7 extension.

## Practical Impact of Faster TypeScript
- Faster project loading, find‑all‑references, auto‑completion, and diagnostics.
- `tsc --watch` provides a tighter feedback loop.
- Example build‑time reductions (average speedup ≈ 9×):
  - VS Code: 125.7 s → 10.6 s (11.9×)
  - Sentry: 139.8 s → 15.7 s (8.9×)
  - Bluesky: 24.3 s → 2.8 s (8.7×)
  - Playwright: 12.8 s → 1.47 s (8.7×)
  - tldraw: 11.2 s → 1.46 s (7.7×)
- Memory usage also drops (e.g., VS Code: 5.2 GB → 4.2 GB, –18%).
- Error display in VS Code improves from ~17.5 s to <1.3 s (≈13× faster).

## Production Readiness
- Tens of thousands of tests run on every commit; extensive internal and external validation.
- Large‑scale partners (Microsoft Loop, Office, Power BI, Xbox, Bloomberg, Canva, Figma, Google, etc.) report stability and speed gains.
- Rebuilt test infrastructure runs on TypeScript 7, detecting regressions in real codebases.
- New language server reduces failing commands by >80% and crashes by >60% versus TypeScript 6.

### Notable Customer Feedback
- Slack: 40% reduction in merge‑queue time; CI type‑checking from 7.5 min to 1.25 min.
- Vanta: up to 9× faster builds on largest project.
- Microsoft News Services: saved 400 hours/month on CI builds.
- Power BI: “life‑saving” editor experience.
- Loop monorepo: previously unusable, now “amazing”.
- Canva: first error shown in 4.8 s vs. 58 s.

## Compatibility with TypeScript 6
- No API shipped with 7.0; API changes expected in 7.1.
- Compatibility package `@typescript/typescript6` provides `tsc6` executable for side‑by‑side use and re‑exports the TS 6 API.