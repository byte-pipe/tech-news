---
title: Between the Graph and the Silicon: Inside the Apple Neural Engine Compiler - smolnero
url: https://smolnero.com/posts/between-the-graph-and-the-silicon-inside-the-apple-neural-engine-compiler
date: 2026-09-08
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-08T00:31:43.690862
---

# Between the Graph and the Silicon: Inside the Apple Neural Engine Compiler - smolnero

# Between the Graph and the Silicon: Inside the Apple Neural Engine Compiler – Summary

## Core perspective on compilers
- A compiler is more than a translator; it continuously decides what information to keep, transform, or discard as a program changes form.  
- This view originated from work with LLVM, KGEN, and MLIR, where the need for multiple intermediate representations became clear.  
- Mojo illustrates preserving source‑level data in LIT, moving to KGEN while keeping parametric info, and retaining structured control flow through HLCF until the compiler finishes reasoning.

## The Apple Neural Engine (ANE) as an opaque target
- Apple exposes the ANE only via Core ML; the underlying compiler, driver, firmware, and hardware details are undocumented.  
- Spencer Bryngelson’s reverse‑engineered paper provides a measurement‑based view of the full stack, focusing on how a neural‑network graph becomes executable ANE code.

## Fusion: collapsing separate graph nodes into one hardware operation
- Example: a convolution → bias → ReLU sequence can be fused into a single ANE operation.  
- The bias is folded into the hardware’s gain‑offset unit; the activation occupies an activation slot.  
- Fusion is driven by whether the hardware can express the combined behavior, not merely by “fewer operations = faster.”  
- Other fusions:
  - Transposes may disappear into neighboring work.  
  - Scaling and batch‑normalization can merge into gain‑offset paths.  
  - Dequantization can be folded into the convolution weight path.  
- Limits exist: addition of two live convolution outputs cannot be fused; attention, concat, and capacity constraints may force splits.

## Legalization: ensuring the fused operation fits the hardware envelope
- The ANE imposes limits on tensor rank, dimension sizes, kernel shapes, and coefficient memory.  
- If an operation exceeds these bounds, the compiler must tile, split, or transform it.  
- Validation checks (shapes, types, operand counts, target capabilities) are necessary but not sufficient; some operations (e.g., top‑k, sort, dynamic slice, 3D convolution) pass validation yet fail during backend lowering.

## Scheduling and task‑descriptor partitioning
- After fusion and legality checks, the compiler orders the remaining operations and divides them into tasks that the ANE can execute efficiently.

## Memory and DMA optimization
- Final stage decides where data resides (on‑chip buffers vs. main memory) and how it moves (DMA transfers) throughout execution.

## Distinguishing “supported” from “executable”
- Multiple layers of support exist:
  1. Representable in the intermediate language.  
  2. Accepted by the frontend.  
  3. Approved by validators.  
  4. Lowerable to ANE primitives.  
  5. Actually runnable on a given silicon generation.  
- Saying “the ANE supports X” is meaningless without specifying which layer is meant.

## Overall compiler flow for ANE
1. **Fusion** – combine operations when hardware can express them as a single unit.  
2. **Legalization** – verify that fused operations respect hardware constraints; otherwise, tile or split.  
3. **Scheduling & partitioning** – order tasks and map them to ANE execution slots.  
4. **Memory/DMA optimization** – place tensors and schedule data movement for minimal overhead.  

The article emphasizes that compiler decisions are guided by the concrete capabilities of the target hardware, and that preserving or discarding conceptual boundaries is a dynamic, context‑dependent process.