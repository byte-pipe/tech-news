---
title: "I Rebuilt Karpathy's NanoChat in JAX. Here's What XLA Gets Right and What It Gets Dead Wrong. - DEV Community"
url: https://dev.to/gde/i-rebuilt-karpathys-nanochat-in-jax-heres-what-xla-gets-right-and-what-it-gets-dead-wrong-4641
date: 2026-05-01
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-05-05T00:52:53.759434
---

# I Rebuilt Karpathy's NanoChat in JAX. Here's What XLA Gets Right and What It Gets Dead Wrong. - DEV Community

# I Rebuilt Karpathy's NanoChat in JAX – What XLA Gets Right and Wrong

- **Goal of the project**  
  - Port Andrej Karpathy’s NanoChat (≈8.6 k lines of PyTorch) to JAX/Flax NNX.  
  - Enable systematic scaling‑law experiments (model size, data volume, compute) and run the same code on GPU and TPU via XLA.

- **Key results**  
  - Trained a 885 k‑parameter “nano” model on TinyStories in < 10 min on a single GPU.  
  - Served the model with a streaming chat UI.  
  - XLA compilation removes Python overhead after a one‑time cost; the compiled program runs unchanged on TPU.  
  - Missing features: no vLLM, no Flash‑Attention 3, and debugging inside JIT‑compiled functions is painful.

- **NanoChat architecture highlights**  
  - Standard GPT components plus five NanoChat‑specific tricks:  
    1. **Value Embeddings** – learned residual vectors added to attention output at every layer.  
    2. **Smear/Backout token mixing** – custom token‑level mixing (not detailed here).  
    3. **Per‑layer learnable scalars** – scaling factors learned per transformer block.  
    4. **QK L2 normalization** – normalizes query/key vectors before dot‑product.  
    5. **Logit softcap** – clamps attention scores with `cap * tanh(scores / cap)` (15 → 30 in the JAX version).

- **Implementation differences and lessons**  
  - **Logit softcap**: JAX uses `jnp.where` instead of in‑place `masked_fill`; replaces `-inf` with `-1e9` to avoid NaNs when whole rows are masked.  
  - **Training step as pure function**: Wrapped in `@nnx.jit`; `nnx.value_and_grad` replaces the PyTorch `zero_grad → backward → step` pattern, yielding a fully functional, side‑effect‑free training loop.  
  - **Muon optimizer (Newton‑Schulz orthogonalization)**: Implemented with `jax.lax.fori_loop` to keep the loop JIT‑compatible; the compiled size stays constant regardless of iteration count, but Python control flow cannot be used inside the loop.  
  - **Value embeddings handling**: Initialized near zero (scale 1e‑4) so they act as a no‑op at start; they are passed by reference to each transformer block, mirroring the PyTorch design.

- **What XLA gets right**  
  - Eliminates Python overhead after the first compilation.  
  - Provides device‑agnostic code: the same JAX program runs on GPU and TPU without changes.  
  - Compiles loops (e.g., Newton‑Schulz) into single efficient XLA while‑loops.

- **What XLA gets wrong / pain points**  
  - Debugging inside JIT‑compiled functions is difficult; must use `jax.debug.print` instead of normal `print`.  
  - Immutable arrays require functional replacements for in‑place operations, leading to subtle bugs (e.g., masked‑fill handling).  
  - Lack of high‑performance kernels like Flash‑Attention 3 means slower attention compared to the original PyTorch implementation.

- **When to care about this port**  
  - If you need a single codebase that scales across GPU and TPU for systematic scaling‑law studies.  
  - When you can tolerate the absence of ultra‑fast attention kernels and are comfortable debugging JIT‑compiled code.  
  - Not ideal for production‑level chat services that require maximum throughput or the latest attention optimizations.