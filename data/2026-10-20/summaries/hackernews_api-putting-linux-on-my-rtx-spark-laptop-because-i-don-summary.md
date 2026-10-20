---
title: "putting linux on my rtx spark laptop because i don't have a microsoft account - josie.lol"
url: https://josie.lol/blog/linux-rtx-spark
date: 2026-10-20
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-20T12:22:51.894571
---

# putting linux on my rtx spark laptop because i don't have a microsoft account - josie.lol

# putting linux on my rtx spark laptop because i don't have a microsoft account

## overview
- The ASUS ProArt P16 (H7607BA‑SE033W) has 128 GB RAM, 6,144 CUDA cores, and a 2 TB SSD.  
- Official support for this hardware is Windows‑only, which I dislike for privacy, UI, and advertising reasons.  
- I chose Arch Linux ARM as the base because I maintain Arch packages and have experience porting Arch to ARM platforms.

## installation & patches
- Built a bootable USB that extends Archinstall 4.5 to include the required hardware support.  
- Integrated NVIDIA’s Ubuntu kernel work, fixed ACPI override allocation, framebuffer mapping, and added ACPI overrides from the laptop’s own tables (thanks to astra).  
- Added patched `hid-asus` for keyboard, a custom machine driver for audio, and extracted ASUS speaker firmware from the official driver package.  
- All build inputs are hash‑pinned; hardware packages are signed with my Arch maintainer key.  
- The repository contains build scripts, patches, and instructions to dump ACPI tables and extract firmware. My firmware version is H7607BA.300.

## hardware & system configuration
- Display: 3840 × 2400 at 120 Hz.  
- Core software: NetworkManager, PipeWire, rootless Podman with NVIDIA CDI.  
- Kernel: `7.0.0-1022-nvidia`; NVIDIA driver `615.78.08`.  
- Installer holds kernel, NVIDIA, power‑management, and firmware packages with `IgnorePkg`; all other packages update from Arch Linux ARM.

## CPU performance benchmarks
- Ran native ARM64 7‑Zip 26.04 (32 MiB dictionary) on October 19, measuring compression and decompression across 1‑20 threads.  
- Compared results to published Windows ARM64 scores from a 128 GB HP OmniBook Ultra 16 and a 64 GB ProArt P16.  

| Threads | Linux compression (MiB/s) | Linux decompression (MiB/s) |
|--------|---------------------------|----------------------------|
| 1      | 6.18                      | 118.26                     |
| 20     | 141.77                    | 1,629.60                   |

- Relative to Windows: single‑thread performance is within 1 % (tie), while 20‑thread compression is ~5 % faster and decompression ~3 % faster on Linux.

## memory management
- Linux reports a single 116.0 GiB pool shared between system RAM and CUDA, unlike Windows which splits RAM into dedicated GPU, shared, and CPU‑only regions.  
- Windows allows adjusting the dedicated GPU reservation (e.g., 91 GiB) but requires reboot; CUDA total then reaches ~109.7 GiB.  
- My Linux setup keeps the full 116 GiB available to both CPU and GPU without reboots, simplifying workload switching.

## running Qwen locally
- Executed NVIDIA’s Qwen‑3.8‑Flash‑Next‑FP4‑Local checkpoint in a native ARM64 container via vLLM with B12X kernels, mixed quantization, and FP8 KV cache.  
- Before loading, 110.9 GiB RAM was free; model loading used 68.2 GiB, KV cache 21.1 GiB (≈90 GiB total).  
- Model compilation took ~16 min; inference timings after warm‑up:

| Task | Input tokens | First token (s) | Full response (s) | Checks passed |
|------|--------------|-----------------|-------------------|---------------|
| Python code review | 208 | 0.316 | 4.008 | 3/3 |
| Incident log analysis | 9,775 | 4.532 | 5.768 | 3/3 |
| Payment‑note extraction | 87 | 0.256 | 2.035 | 3/3 |

- Token generation speed for code review ≈30 tokens/s, comparable to a Windows setup (Frandroid) that used an 85 GiB GPU reservation and a larger context limit.  
- Batched four code reviews: median 5.314 s, yielding 86.6 output tokens/s across all requests.

## conclusions
- Arch Linux ARM runs smoothly on the RTX Spark laptop, matching or slightly exceeding Windows performance in multi‑threaded CPU workloads.  
- The unified memory pool in Linux simplifies high‑memory GPU workloads, avoiding the need to adjust GPU reservations.  
- Large language model inference (Qwen) is feasible on a laptop with ~116 GiB shared memory, delivering practical response times for real‑world tasks.  
- All patches, scripts, and build instructions are publicly available in the linked repository.

## resources
- Repository with build scripts, patches, and ACPI extraction steps (link provided in the original post).  
- Firmware version used: H7607BA.300.  
- Kernel and driver versions: `7.0.0-1022-nvidia` and NVIDIA driver `615.78.08`.