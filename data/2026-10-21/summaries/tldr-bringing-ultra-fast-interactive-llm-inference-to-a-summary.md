---
title: Bringing Ultra-Fast, Interactive LLM Inference to AMD Instinct™ MI355X GPUs — ROCm Blogs
url: https://rocm.blogs.amd.com/software-tools-optimization/megakernel-intro/README.html
date: 2026-10-21
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-21T11:12:13.051776
---

# Bringing Ultra-Fast, Interactive LLM Inference to AMD Instinct™ MI355X GPUs — ROCm Blogs

# Bringing Ultra-Fast, Interactive LLM Inference to AMD Instinct™ MI355X GPUs

## Key Takeaways
- Single‑request decode on a single MI355X (batch 1) with speculative decoding is 1.9×–3.3× faster than the fastest stock configurations.
- Qwen3.8‑27B reaches ~1,100 tokens / s (2.0× ATOM regular path) and is available through ATOM, SGLang and vLLM.
- Qwen3.8‑Flash‑Next reaches ~750 tokens / s (3.3× ATOM regular path) and is available through ATOM.
- GPT‑OSS‑120B reaches ~1,470 tokens / s (1.9× fastest vLLM stock, 1.6× with the same drafter) and is offered as a preview in vLLM.
- Using the MI355X two‑die mode (DPX+NPS2) improves GPT‑OSS‑120B latency by 7.5%–8% from data placement alone and by 16%–20% when combined with speculative decoding.

## Techniques Behind the Speedup
### Megakernels: fewer launches, targeted synchronization
- Persistent kernels keep a workgroup resident on each compute unit, eliminating per‑operator launch overhead.
- Producer‑to‑consumer hand‑offs use a single 64‑bit store; most polling stays in local cache.
- Weight prefetch, fused operators, and fine‑grained overlap of compute and data movement reduce synchronization to only true data‑sharing points.
- Qwen3.8‑Flash‑Next’s sparse‑attention selection is split into parallel chunks, cutting a 250 K‑token layer from 262 µs to 126 µs.

### Speculative Decoding: more tokens per pass
- A small drafter predicts several next tokens; the target model validates them in one pass, keeping accepted tokens plus one of its own.
- Qwen3.8‑27B’s DFlash2 drafter proposes seven tokens per round, with ~5.6 accepted on average for GSM8K.
- Drafting, checking, and state updates run as a captured GPU graph without CPU round‑trips; drafter kernels are persistent.
- Optimal draft length depends on workload (longer drafts help predictable math, shorter drafts suit dense conversational text).

### Low‑Precision Data Types
- MXFP4 weights (4‑bit with shared scale) paired with MXFP8 activations use ~3.8× fewer bytes than BF16.
- Reduced weight bandwidth lowers the floor for decode latency; megakernels bring actual passes close to this floor.
- Minor additional quantization (e.g., LM head, attention projections) contributes only a small portion of the overall speedup and does not noticeably affect accuracy.

### Data Locality: placing data near its consumer
- MI355X’s two base dies each own half of the HBM; default mode spreads buffers across both dies, causing cross‑die traffic.
- DPX+NPS2 exposes each die as a separate logical device, allowing data to reside in the local die’s memory.
- GPT‑OSS‑120B leverages this mode, gaining 7.5%–8% latency improvement from placement alone and up to 20% when combined with speculative decoding.

## Models, Engines, and Availability
| Model | Tokens / s | Speedup vs. baseline | Engine(s) | Status |
|-------|-------------|----------------------|-----------|--------|
| Qwen3.8‑27B | ~1,100 | 2.0× ATOM regular path | ATOM, SGLang, vLLM | GA |
| Qwen3.8‑Flash‑Next | ~750 | 3.3× ATOM regular path | ATOM | GA |
| GPT‑OSS‑120B | ~1,470 | 1.9× fastest vLLM, 1.6× with same drafter | vLLM (preview) | Preview |

## Reproducing the Results
- The “Get Started” section of the blog lists the exact repository versions, container images, and command‑line steps for each model‑engine combination.
- Test configuration details (precision, drafter, GPU partitioning) are provided to ensure identical setups when benchmarking.
- All optimizations are open‑sourced, enabling users to integrate the megakernels, speculative decoding pipelines, and DPX+NPS2 data placement into their own inference stacks.