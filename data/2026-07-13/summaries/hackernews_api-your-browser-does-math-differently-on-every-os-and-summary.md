---
title: Your Browser Does Math Differently on Every OS, and Anti-Bot Systems Read the Bits · scrapfly.dev
url: https://scrapfly.dev/posts/browser-math-os-fingerprint/
date: 2026-07-13
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-13T12:28:36.734713
---

# Your Browser Does Math Differently on Every OS, and Anti-Bot Systems Read the Bits · scrapfly.dev

# Your Browser Does Math Differently on Every OS, and Anti‑Bot Systems Read the Bits  

## Overview  
- JavaScript’s `Math.tanh` returns slightly different double‑precision bits on Linux (glibc), macOS (libsystem_m), and Windows (UCRT).  
- The discrepancy appears because Chrome 148+ switched V8 to call the platform `std::tanh` instead of its bundled fdlibm implementation.  
- The variation is typically 1–2 units in the last place (ULP) and can be used as a reliable fingerprint.  

## Why the Differences Occur  
- IEEE‑754 defines the binary format but does not require exact rounding for transcendental functions.  
- Each operating system ships its own libm implementation, using distinct minimax coefficients, lookup tables, and reduction constants to trade a fraction of a ULP for speed.  
- Consequently, the same input can produce three different bit patterns, enough to classify the OS.  

## Four Traps When Trying to Spoof Math  

1. **Only some functions leak** – `Math.tanh` is the only JavaScript Math function that now reads the host libm; other functions still use V8’s bundled code, so spoofing them creates inconsistencies.  
2. **JS and CSS math follow different paths** – CSS trig functions (`sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2`) always call the platform libm after degree‑to‑radian conversion, leaking the OS for all seven CSS functions.  
3. **macOS has two libm variants** – scalar `libsystem_m` and the Accelerate framework’s vector routines differ on many inputs. The browser may call either depending on the feature (e.g., plain Math calls use `libsystem_m`, Web Audio DSP uses Accelerate). Choosing the wrong variant yields a 1‑ULP error on most inputs.  
4. **Architecture leaks** – ARM and x86 differ in fused‑multiply‑add handling and NaN sign propagation; reproducing results on one architecture may drift on the other.  

## Where the Leaks Appear  

- **JavaScript (V8)**: only `Math.tanh` uses the host libm.  
- **CSS (`calc()`)**: all seven trig functions (`sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `atan2`) call the host libm, providing a tell on every call.  
- **Web Audio (macOS)**:  
  - Accelerate’s FFT and vector math leak CPU‑architecture bits.  
  - The DynamicsCompressor’s per‑sample transcendentals use scalar `libsystem_m`, leaking the OS.  
- **WASM**: no libm leakage; arithmetic is hardware‑based, with only architecture‑specific NaN handling and SIMD rounding as possible tells.  

## Mitigation Strategies  

- **Avoid adding noise** – Random perturbation either creates values that no real OS would produce (detected as fake) or breaks deterministic behavior (another detectable pattern).  
- **Exact reproduction** – Re‑implement the target OS’s libm algorithm, copying its minimax coefficients, exponent tables, and reduction constants verbatim (e.g., using hex literals for Apple’s `sin` polynomial) to match every bit, including edge‑case rounding directions.  

## Practical Implications  

- Anti‑bot and fingerprinting systems can issue a single `Math.tanh` (or CSS trig) query and compare the resulting bits against known OS‑specific patterns to verify the claimed platform.  
- Scraping services that need to mimic real browsers must emulate the correct host libm behavior across these surfaces, otherwise they risk detection.