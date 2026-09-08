---
title: GitHub - argonautlabsai/deltafin: ARGODRIVE Deltafin: Kimi K3 (2.8T MoE) streamed from SSDs on Apple Silicon — fork of gavamedia/deltafin with the ARG...
url: https://github.com/argonautlabsai/deltafin
date: 2026-09-08
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-09T08:37:50.584210
---

# GitHub - argonautlabsai/deltafin: ARGODRIVE Deltafin: Kimi K3 (2.8T MoE) streamed from SSDs on Apple Silicon — fork of gavamedia/deltafin with the ARG...

# ARGODRIVE Deltafin – Kimi K3 (2.8 T MoE) on Apple Silicon

## TL;DR
- Runs the full 2.8‑trillion‑parameter Kimi K3 (1.45 TB expert weights) on an M5 Max MacBook Pro (128 GB RAM) with experts streamed from four SSDs.  
- Steady‑decode throughput: **≈1 tok/s** for 512‑token generations, **≈1.13 tok/s** for 128‑token generations, **≈0.96 tok/s** on a 17‑token prompt (upstream reported 0.68 tok/s).  
- First‑token latency for a 512‑token prompt: **≈376 s** (≈6.3 min); caused by pre‑fill re‑reading each layer’s experts 8× (fix planned).  
- Scaling: 1 SSD → ≈52 % of 4‑SSD speed, 2 SSDs → ≈73 %, 3 SSDs → ≈90 %; the slowest of the 16 reads per layer determines overall pace.  
- All numbers are from single cold runs; detailed logs in `k3-public-bench/`.

## Benchmarks (M5 Max, 128 GB, 4 SSDs)
| Test | Drafter off | Drafter on |
|------|------------|------------|
| Steady decode, 512 tokens | 0.923 tok/s | 1.001 tok/s |
| Steady decode, 128 tokens | 0.926 tok/s | 1.125 tok/s |
| 17‑token prompt (median of 3) | — | 0.963 tok/s |
| Time to first token (512‑token prompt) | ≈376 s | ≈375 s |

*Drive‑count ladder*: 1 SSD ≈ 52 % of 4‑SSD speed, 2 SSDs ≈ 73 %, 3 SSDs ≈ 90 % (see `results/SCALING.md`).  
*Prefill bottleneck*: explained in `results/PREFILL.md`.

## Comparison with upstream (gavamedia/deltafin)
- Upstream on M1 Max (unchanged code): **0.290 tok/s** (≈3.45 s/token).  
- Historical upstream values show rapid improvements over weeks in 2026.

## Mission Statement
- Preserve **full K3 quality**: all 16 experts are consulted for every token, no pruning or shortcuts.  
- Aim to extract every possible efficiency gain on consumer hardware **without compromising model fidelity**.

## Rationale
- Demonstrate how far a $15 k home setup can push frontier models, compared to the multi‑million‑dollar infrastructure Kimi recommends.  
- Provide research data that may benefit other projects, even if they pursue different trade‑offs (e.g., quantized expert banks).

## Installation & Usage Overview
1. **Clone & build**  
   ```bash
   git clone https://github.com/argonautlabsai/deltafin.git
   cd deltafin
   cargo build --locked --release
   ```
2. **Model acquisition**  
   - Full download (1.7 TB): `./target/release/deltafin setup --full`  
   - Streamed mode (215 GB start): `./target/release/deltafin setup --stream`
3. **Optional Qwen add‑on** (faster raw completion, 4.34 GiB disk):  
   `./target/release/deltafin setup-qwen`
4. **Upgrade** (preserves caches):  
   ```bash
   ./target/release/deltafin upgrade
   ```

## Notable Components
- **DSpark** (default) provides Kimi‑K3‑DSpark (≈6.6 GiB disk, 4.5 GiB runtime) and avoids redundant embedding copies.  
- **Qwen** (optional) speeds up pure text continuation by letting a small model draft and K3 verify, yielding up to 2.7× faster 17‑token completions with identical outputs.

## References
- Full credits in `CREDITS.md`.  
- Detailed benchmark definitions in `k3-public-bench/README.md`.  
- Scaling results in `results/SCALING.md`.  
- Prefill analysis in `results/PREFILL.md`.