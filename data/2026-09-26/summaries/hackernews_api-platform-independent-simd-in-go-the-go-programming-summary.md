---
title: Platform-independent SIMD in Go - The Go Programming Language
url: https://go.dev/blog/simd-experiment
date: 2026-09-25
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-26T05:56:45.431217
---

# Platform-independent SIMD in Go - The Go Programming Language

# Platform-independent SIMD in Go

## Motivation and Background
- Go 1.26/1.27 add experimental SIMD APIs, allowing vectorized operations without hand‑written assembly.  
- Prior to these releases, SIMD could only be used via Go assembly, limiting its use to a few performance‑critical kernels.  
- SIMD hardware varies widely:
  - Fixed vs. variable vector sizes (e.g., 128 bits on wasm, 128/256/512 on amd64, 128‑2048 on ARM SVE).  
  - Different mask implementations (no masks, vector masks, special mask registers).  
  - Divergent instruction sets for shuffles, crypto ops, comparisons, etc.  
- Architecture‑dependent `archsimd` package hides some differences but still requires many feature checks and platform‑specific code.

## New `simd` Package
- Provides a **portable, size‑agnostic** interface built on top of the architecture‑specific APIs.  
- Inspired by Highway for C++; aims for “write‑once, near‑asm‑performance” code that also runs (via emulation) on CPUs lacking SIMD.  
- Enabled by setting `GOEXPERIMENT=simd` at build time.  
- Vector types are simple plural names such as `simd.Uint8s`, `simd.Float32s`.  
- Vectors are loaded from / stored to slices; partial loads handle tail elements.

### Example Usage
```go
func innerProduct(x, y []float32) float32 {
    var acc simd.Float32s
    var i int
    for i = 0; i < len(x)-acc.Len()+1; i += acc.Len() {
        u := simd.LoadFloat32s(x[i : i+acc.Len()])
        v := simd.LoadFloat32s(y[i : i+acc.Len()])
        acc = u.MulAdd(v, acc)
    }
    if i < len(x) {
        u, _ := simd.LoadFloat32sPart(x[i:])
        v, _ := simd.LoadFloat32sPart(y[i:])
        acc = u.MulAdd(v, acc)
    }
    return sum(acc)
}
func sum(v simd.Float32s) float32 {
    tmp := make([]float32, v.Len())
    v.Store(tmp)
    var r float32
    for _, e := range tmp {
        r += e
    }
    return r
}
```
- Shows loading, `MulAdd`, and storing; current release lacks a built‑in horizontal reduction (`ReduceSum` will be added later).

## Design Goals
1. **Algorithmic breadth** – support many data‑processing tasks without tying code to a concrete vector width.  
2. **Performance parity** – when the source operations map directly to hardware instructions, generated code matches hand‑written assembly speed.  
3. **Graceful fallback** – on CPUs without SIMD or without `archsimd` support, all operations are emulated so the program still runs.  
4. **Readability** – API is simple enough for humans and LLMs to generate correct code.

## Supported Operations (Go 1.27)
- **Load / Broadcast**: `LoadV`, `LoadVPart`, `BroadcastV` for all primitive element types (Int8…Float64).  
- **Store / String**: `Store`, `StorePart`, `String` methods on every vector type.  
- **Arithmetic & Utility**: `Add`, `AddSaturated`, `Abs`, `Div`, `Mul`, `Max`, `Min`, `Average`, `IfElse`, `Masked`, `Len`, etc.  
- **Mask handling**: Comparisons produce mask types (`Mask8s`, `Mask16s`, …) that can be used for conditional selection.  

The table in the article lists a “Y” for each supported combination; essentially every primitive vector type implements the full set of load, store, and arithmetic methods.

## Usage Notes
- Enable the experimental package with `GOEXPERIMENT=simd`.  
- The API deliberately excludes operations that are not common across all target architectures; missing features (e.g., horizontal sum) are added later via emulation.  
- The package lives in `arch/simd` for architecture‑specific code and `simd` for the portable layer.  

## Outlook
- Future releases will add missing reductions (`ReduceSum`) and possibly more advanced operations while preserving the platform‑agnostic abstraction.  
- The approach aims to make SIMD accessible to a broader range of Go programs, reducing the need for hand‑written assembly and improving performance across diverse hardware.