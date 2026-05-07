---
title: RaTeX — Rust math layout aligned with KaTeX golden tests
url: https://ratex.lites.dev/
date: 2026-05-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-08T08:13:47.548307
---

# RaTeX — Rust math layout aligned with KaTeX golden tests

# RaTeX — Rust math layout aligned with KaTeX golden tests

## Packages and integration options
- One Rust core provides SDKs and WASM builds that can be installed via npm, Maven, pub.dev, or Swift Package Manager.  
- Server‑side PNG generation and CLI tools are also available.  
- Supported platforms:  
  - Web (WASM)  
  - iOS (Swift)  
  - Android (Kotlin)  
  - Flutter (Dart FFI)  
  - React Native  
  - Server / CLI  

## When to reach for RaTeX
- **Native or server** – identical layout on iOS, Android, Flutter, or Rust services without bundling a browser.  
- **WASM host** – run the core in WebAssembly, draw with Canvas, and compare output with KaTeX in the live demo.  
- **Chemistry & units** – built‑in `\ce` and `\pu` support (mhchem‑style) alongside ordinary math.  

## Core characteristics
- **Rust core** – single layout engine, no garbage collector, predictable timing for mobile UIs, servers, and CI raster tests.  
- Memory‑safe, produces a display list that can be rasterized by tiny‑skia or a custom renderer.  
- **Cross‑platform shipping** – C ABI for Swift, Kotlin, Dart, etc.; WASM for the web; identical display lists across targets.  

## Golden‑suite galleries
- Browser demo displays the same LaTeX lines used in CI, rendered with RaTeX WASM.  
- Side‑by‑side comparison with KaTeX is available in the interactive demo; the full golden suite is listed on the Demo page.  

## Comparison with WebView stacks
| Feature            | RaTeX                | KaTeX (web)          | MathJax               |
|--------------------|---------------------|----------------------|----------------------|
| Runtime            | Pure Rust           | JavaScript + DOM    | JavaScript + DOM    |
| Mobile             | Native / WASM       | WebView             | WebView             |
| Offline support    | Yes                 | Depends              | Depends              |
| JS bundle size     | 0 kB JS (core is WASM) | ~280 kB              | ~500 kB              |
| Memory model       | Predictable         | GC / heap            | GC / heap            |

## Comparison with native math SDKs
| Capability                     | RaTeX | swiftMath | flutter_math | iosMath |
|--------------------------------|-------|-----------|--------------|---------|
| `\ce` (mhchem chemistry)      | ✔︎     | ✖︎         | ✖︎            | ✖︎       |
| `\pu` / siunitx‑style units    | ✔︎     | ✖︎         | ✖︎            | ✖︎       |
| Same engine for native FFI + WASM | ✔︎   | ✖︎         | ✖︎            | ✖︎       |
| Mobile + desktop from one Rust core | ✔︎ | ✖︎         | ✖︎            | ✖︎       |
| TeX layout core in Rust (predictable hot path) | ✔︎ | ✖︎ | ✖︎ | ✖︎ |

*Performance varies with workload; Swift uses ARC and Dart uses a tracing GC, while RaTeX’s Rust core avoids both.*  

## Use case
- Enables shipping scientific user interfaces without embedding a browser engine.  
- Live demo and source code are available in the GitHub README.