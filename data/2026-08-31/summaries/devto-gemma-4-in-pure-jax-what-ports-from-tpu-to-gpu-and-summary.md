---
title: "Gemma 4 in Pure JAX: What Ports from TPU to GPU, and What Doesn't - DEV Community"
url: https://dev.to/gde/gemma-4-in-pure-jax-what-ports-from-tpu-to-gpu-and-what-doesnt-3m09
date: 2026-08-29
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-08-31T02:22:30.617040
---

# Gemma 4 in Pure JAX: What Ports from TPU to GPU, and What Doesn't - DEV Community

# Gemma 4 in Pure JAX: What Ports from TPU to GPU, and What Doesn’t

## Project goal
- Serve a single Gemma 4 checkpoint from a pure‑JAX port on every rented accelerator (TPU v5e, TPU v6e, NVIDIA T4G on AWS Graviton2).  
- Verify by measurement, not documentation, which “just JAX” claims hold true.  
- The same code (in `ports/gemma4/`) runs behind an OpenAI‑compatible server; no PyTorch, vLLM, or torch‑xla is used.  
- Ideally only a config file should differ between rigs.

## Gemma 4 E2B is not a stock transformer
- Four mandatory irregularities:
  1. Two attention geometries: sliding layers use `head_dim=256`, global layers use `head_dim=512`.  
  2. 8:1 multi‑query attention, so KV budget differs from parameter count.  
  3. KV‑share map collapsing 35 layers onto 15 caches.  
  4. A 512‑slot sliding ring plus per‑layer embeddings stored in a 4.70 GB table quantized to 4 bits on load.  
- Heterogeneous head dimensions break other stacks (e.g., vLLM’s Triton backend runs out of shared memory).  
- JAX uses ordinary XLA attention, so the irregular geometry is just an array shape, avoiding shared‑memory limits.

## Dtype policy must read the device
- Compute dtype is chosen at runtime based on the device’s compute capability, not a config file:  
  - Pre‑Ampere GPU → `float16`  
  - Ampere+ GPU or TPU → `bfloat16`  
- Wrong dtype does not raise an error; XLA silently falls back to `fp32`, causing large decode‑time conversion overhead.  
- The process logs the chosen dtype, making misconfiguration easy to spot (e.g., `compute_dtype=float16` on a Turing GPU).  
- The `pallas_interpret=False` flag also matters; it distinguishes serving from a silent simulator.

## Where the abstraction leaks: Pallas
- The fused W4A16 kernel is written in Pallas and tiled for TPU VMEM (≈16 MiB per core). Tiles need 550 KiB–1.1 MiB per block.  
- On GPUs, Pallas lowers through Triton, turning tiles into shared memory; Turing provides only 64 KiB per block, Ada more but still far below a megabyte.  
- Consequently the same Pallas kernel cannot run on GPUs; the startup check aborts with a clear error instead of a cryptic out‑of‑resources crash.  
- Result: GPU rigs serve the dense 16‑bit checkpoint, while TPU rigs serve the QAT‑W4A16 checkpoint.  
- Takeaway: Pallas is portable as an API, not as a memory model.

## Padding‑eviction bug in the KV ring cache
- Gemma 4’s geometry makes the invariant “cache index = absolute real position, padding never occupies a real position” critical.  
- A right‑pad into the 512‑slot ring violates this, producing a token loop that returns HTTP 200 with output like “The The The …”.  
- No logs or metrics flag the error; only a degeneracy check on the generated text catches it.  
- The most severe bugs in the project all returned success responses.

## What ported without changes
- Model code handling all four irregularities, both attention geometries, KV‑share map, and ring cache.  
- XLA compilation cache: persistent cache restores ~805 files (12 MiB) in ~6 s on a fresh GPU instance.  
- Bucketing and static shapes: `max_new_tokens` is a static argument, giving identical compiled shapes across backends; warm‑up reduces latency from 18.77 s (cold) to 4.35 s (warm).  
- Dependency installation: `pip install cuda.jax[cuda13]` installs on the GPU rig in 117 s with no build step, versus a ~67‑minute from‑source build on the vLLM path.

## Unexplained decode‑time profile on Turing GPU
- xprof profiling shows:
  - conversion 54 %  
  - fp32 GEMV 33 %  
  - fusion 12 %  
  - TensorCore 0 %  
- No Tensor Core kernels fire despite running on a Tensor‑Core GPU.  
- Converting the checkpoint to host‑side `float16` does not reduce the conversion percentage, suggesting the cause is not dtype mismatch.  
- The same profile reproduces across instances with < 2 ms variance, indicating a real, yet unidentified, bottleneck.  
- Future work: run the port on an Ada GPU (native `bfloat16`) to see if the conversion cost persists.

## Honest performance numbers
- Model: `google/gemma-4-E2B-it` (dense reference build)  
- Weights resident: 6.155 GB  
- Decode speed on T4G: 13.10 tokens / s  
- Decode vs. context length (flat):
  - 41 tokens → 12.9 t/s  
  - 521 tokens → 13.0 t/s  
  - 2 057 tokens → 12.9 t/s  
- Context limit: `MAX_MODEL_LEN=4096`; 4 105 prompt tokens serve, 5 120 fails on a prefill transient.  
- End‑to‑end throughput drops with longer prompts (12.43 → 8.22 t/s) due to linear prefill cost, not decode degradation.