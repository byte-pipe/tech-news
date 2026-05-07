---
title: RaTeX — Rust math layout aligned with KaTeX golden tests
url: https://ratex.lites.dev/
site_name: hnrss
content_file: hnrss-ratex-rust-math-layout-aligned-with-katex-golden-t
fetched_at: '2026-05-08T08:12:54.607524'
original_url: https://ratex.lites.dev/
date: '2026-05-04'
description: Rust TeX-style math layout with KaTeX-aligned golden tests. Ready-to-use packages for Web (WASM), iOS, Android, Flutter, and React Native—same display list everywhere.
tags:
- hackernews
- hnrss
---

Packages

 

## Integrate anywhere

 

Ready-to-use SDKs and WASM builds ship from the same Rust core: install from npm, Maven, pub.dev, or SPM—step-by-step inGet started. Server-side PNG and CLI are covered there too.

 
* Web (WASM)
* iOS (Swift)
* Android (Kotlin)
* Flutter (Dart FFI)
* React Native
* Server / CLI
 

npmratex-wasm/ratex-react-native· Mavenio.github.erweixin:ratex-android· pub.devratex_flutter· iOS via SPM

 
 
 

## When to reach for RaTeX

 
* Native or server— Ship the same layout on iOS, Android, Flutter, or Rust services (PNG/SVG-style rasterization) without bundling a browser.
* WASM in your host— Run the core in WebAssembly and draw with Canvas; compare output with KaTeX in thelive demo.
* Chemistry & units—\ce/\puon the mhchem-style path next to ordinary math (see galleries below).
 
 
 
 
 
memory
 

### Rust core

 

One layout engine, no GC in the hot path: predictable timing for mobile UIs, servers, and CI raster tests.

 
 
 
MEMORY_SAFE
 
DISPLAY_LIST
 
 
 
 
 
devices
 

### Ship everywhere

 

C ABI for Swift, Kotlin, Dart, … WASM for the web; tiny-skia or your own rasterizer—identical display lists.

 
 
 
WASM
 
FFI
 
 
 
 
 
science
 

### mhchem-style chemistry

 

Built-in\ceand\puon the mhchem-compatible path—reaction arrows and physical units in the same pipeline as ordinary math.

 
 
 
MHCHEM
 
LATEX_MATH
 
 
 
 
 

Try it in the browser

 

## Golden-suite galleries

 

Browse the same LaTeX lines CI uses, rendered with RaTeX WASM on the page:Math,Chemistry,Physics.
 For side-by-side comparison with KaTeX, open theinteractive demo; the full golden suite lives in thesupport tableon the Demo page.

 
 
 
 

## Why not a WebView stack?

 

In the browser, KaTeX and MathJax typically run as JavaScript against the DOM. For app shells that embed math via WebView, that still means shipping a browser stack. RaTeX keeps layout and rasterization in Rust for hosts that want to avoid that path.

 
 
 
 
Web stack comparison: RaTeX versus KaTeX and MathJax
 
 
 
 
RaTeX
 
KaTeX (web)
 
MathJax
 
 
 
 
 
Runtime
 
Pure Rust
 
JavaScript + DOM
 
JavaScript + DOM
 
 
 
Mobile
 
Native / WASM
 
WebView
 
WebView
 
 
 
Offline
 
Yes
 
Depends
 
Depends
 
 
 
JS bundle (typical)
 
0 kB JS (core is WASM)
 
~280 kB
 
~500 kB
 
 
 
Memory model
 
Predictable
 
GC / heap
 
GC / heap
 
 
 
 
 
 

### RaTeX vs native math SDKs

 

Without a WebView, teams often reach for Swift, Objective-C, or Flutter libraries. Below is a high-level comparison with widely used open-source renderers—swiftMath (Swift), flutter_math_fork / flutter_math (Dart / Flutter), and iosMath (iOS)—on chemistry macros, portability, and engine shape. Third-party SDKs evolve independently; compare versions when you integrate.

 
 
 
 
RaTeX compared to swiftMath, flutter_math, and iosMath: mhchem support, cross-platform engine, and layout core performance characteristics
 
 
 
Capability
 
RaTeX
 
swiftMath
 
flutter_math
 
iosMath
 
 
 
 
 
mhchem 
\ce
 (chemistry)
 
check_circle
 
cancel
 
cancel
 
cancel
 
 
 
\pu
 / siunitx-style units
 
check_circle
 
cancel
 
cancel
 
cancel
 
 
 
Same engine: native FFI + WASM (web)
 
check_circle
 
cancel
 
cancel
 
cancel
 
 
 
Mobile + desktop from one Rust core
 
check_circle
 
cancel
 
cancel
 
cancel
 
 
 
TeX layout core in Rust (predictable hot path)
 
check_circle
 
cancel
 
cancel
 
cancel
 
 
 
 
 

*Performance depends on workload. Swift uses ARC; Dart uses a tracing GC—both differ from RaTeX's Rust core for the same "no browser" embedding story.

 
 
 
 
 
function
 
 

## Ship scientific UI without embedding a browser engine

 
 
Live demo
 
GitHub README