---
title: Turns are Better than Radians - by Casey Muratori
url: https://www.computerenhance.com/p/turns-are-better-than-radians
date: 2026-08-20
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-21T06:52:08.308545
---

# Turns are Better than Radians - by Casey Muratori

# Turns are Better than Radians

## Main argument
- Most code that uses π or τ does so only to convert a value in the range [0, 1] to radians before calling `sin`/`cos`.
- The trig libraries immediately multiply by 4/π (or divide by τ) to get back to the original scale, so the conversion is wasted work.
- By agreeing to work directly in “turns” (a full circle = 1), the extra multiply/divide disappears.

## Why radians are unnecessary
- Radians are not a mathematical requirement for sine and cosine; the functions can accept any normalized angle.
- Representing common angles in radians is inexact (e.g., 90° ≈ π/2), while in turns they are exact fractions (0.25, 0.5, 0.75) requiring no mantissa bits.
- Using turns therefore yields more precise and compact representations for typical angles.

## Benefits of using turns
- **Performance:** eliminates a redundant multiplication in the caller and a division in the library.
- **Precision:** exact representation of common angles reduces rounding error.
- **Clarity:** code reads more naturally when angles are expressed as fractions of a circle.

## How to make the switch
- Change the interface of your `sin`/`cos` (and other trig) functions to accept turns instead of radians; usually this is a single constant adjustment.
- For legacy code, provide wrapper functions that convert from radians to turns (divide by τ) and forward to the new implementation.
- The change can be done with only a few lines of code.

## Existing support
- Some libraries already expose half‑turn based functions, e.g., CUDA’s `sincospi`, which computes sine and cosine of an input multiplied by π (a half‑turn).
- When such intrinsics are available, you can start using them immediately without modifying the underlying library.

## Overall impression
- After removing radians from a codebase, the author finds the code cleaner and never misses π or τ.
- The same reasoning applies to all standard trig functions; most libraries internally convert away from radians anyway, so a global switch to turns or half‑turns is straightforward.