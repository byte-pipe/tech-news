---
title: Clojurists Together | Q2 2026 Funding Announcement
url: https://www.clojuriststogether.org/news/q2-2026-funding-announcement/
date: 2026-05-03
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-04T06:01:58.831091
---

# Clojurists Together | Q2 2026 Funding Announcement

# Q2 2026 Funding Announcement – Summary

## Overview
- Clojurists Together will fund **5 projects** in Q2 2026, totaling **$31 K USD**.  
- Allocation: **3 projects** receive **$9 K** each; **2 shorter/experimental projects** receive **$2 K** each.  
- Thanks are given to members, especially **Metabase**, the newest Transduce member, for supporting Ambrose Bonnaire‑Sergeant’s work on **Malli**.

## $9 K USD Projects
- **Ambrose Bonnaire‑Sergeant – Malli**  
- **Dragan Djuric – Uncomplicate AI: Clojure LLM**  
- **Cvetomir Dimov – SciCloj Documentation and Plotting Libraries**

## $2 K USD Projects
- **Ingy döt Net – Gloat**  
- **Shantanu Kumar – PluMCP**

## Project Highlights

### Ambrose Bonnaire‑Sergeant: Malli
- Previously improved recursive‑ref validation to use constant memory, but increased upfront compilation memory.  
- Will explore two approaches:  
  1. Lazy discovery of recursion points (reduces initial memory, still grows with large inputs).  
  2. Reducing maximum memory by sharing schema objects and validators across usages.  
- Goal: Enable systems like Metabase to benefit from constant‑memory validation without prohibitive upfront costs.

### Cvetomir Dimov: SciCloj Documentation and Plotting Libraries
- SciCloj promotes Clojure in data analysis, AI, scientific computing, etc., and runs the **SciNoj** online conference.  
- Planned improvements:  
  - Extend Noj’s plotting library (more back‑ends, plot types).  
  - Create a new interactive dashboard library.  
  - Expand the Noj book for comprehensive, consistently structured coverage.

### Dragan Djuric: Uncomplicate AI – Clojure LLM
- Aim to deliver a high‑performance local LLM library for Clojure, similar to **llama.cpp** but simpler and faster, with GPU and CPU support.  
- First version will target Google’s **Gemma 3** model family and sentence‑piece tokenizer.  
- Promised features: fast execution, minimal API, seamless ecosystem integration, no need for users to understand CUDA/ONNX/tensors, runnable on laptops, servers, or cloud.

### Ingy döt Net: Gloat
- Gloat compiles Clojure to Go code, native binaries (≈25 targets), Wasm modules, and shared libraries, offering an open‑source alternative to GraalVM native‑image.  
- Funding will be used to:  
  - Reduce binary size and improve speed (including tree‑shaking of `clojure.core`).  
  - Pass more of the Clojure Compatibility Test Suite.  
  - Produce tutorial documentation for using Gloat in Go projects and for cross‑compiling Clojure programs.

### Shantanu Kumar: PluMCP
- (Project description not detailed in the announcement.)