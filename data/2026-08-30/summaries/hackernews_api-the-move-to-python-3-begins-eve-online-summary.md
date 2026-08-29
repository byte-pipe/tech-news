---
title: The Move to Python 3 Begins! | EVE Online
url: https://www.eveonline.com/news/view/the-move-to-python-3-begins
date: 2026-08-25
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-30T06:03:11.430814
---

# The Move to Python 3 Begins! | EVE Online

# The Move to Python 3 Begins!

## Overview
- Part of the **EVE Evolved** initiative; the codebase is transitioning from Python 2.7 to Python 3.
- Goal: migration should be invisible to players, with occasional smoother performance.
- First changes have already been deployed on the Singularity test server and now on Tranquility.

## Why Python 3 and Why Now?
- **Performance:** Recent Python 3 releases provide significant speed improvements.
- **Ecosystem:** Modern libraries, debuggers, and profilers target Python 3; staying on Python 2 limits tool availability.
- **Language Improvements:** Unified string handling, automatic integer sizing, and a consistent class system simplify development and localization.

## Migration Process
- Codebase size: ~2.4 million lines of Python, many written to pre‑2.7 standards.
- **Stage 1 (current):** Make code “Python 3‑ready” while still running on Python 2.7 using the **Python‑Future** tool (based on 2to3) to apply automated fixers.
- **Stage 2:** Resolve behavioral differences (e.g., division semantics) that require human judgment.
- Multiple stages, with community playtests on Singularity to validate changes.

## Progress & Metrics
- Compilation test across ~20 k files shows **95.9 %** already compatible with both interpreters.
- Remaining syntax issues (~3 300 lines) include:
  - ~1 500 old‑style `print` statements
  - ~800 `long` literals (`123L`)
  - ~600 deprecated exception clauses
  - 50 uses of the obsolete `<>` operator
- About **20 000 lines** compile under both versions but behave differently (e.g., integer division).

## Challenges Ahead
- Mechanical syntax fixes are largely done; the bulk of work involves reviewing lines that change behavior in Python 3.
- Each affected line (damage calculations, ISK values, coordinates, etc.) needs a deliberate decision to preserve game balance.

## What This Means for Players
- **Short term:** No visible changes; Stage 1 updates are designed to be invisible.
- **Long term:** Faster interpreter, better debugging tools, and a more maintainable codebase will enable quicker feature delivery and a smoother gameplay experience for the next two decades.

## Call to Action
- Continue normal gameplay; report any anomalies via bug reports.
- Participate in future playtests if invited.
- Share involvement with corp mates as a contribution to EVE’s evolution.

## Related News
- **2026‑08‑26:** Patch Notes – Version 24.01  
- **2026‑08‑22:** Save 20 % on PLEX + Free SKINs  
- **2026‑08‑20:** EVE Online and AI Research  
- **2026‑08‑19:** Monthly Ban Report – July 2026