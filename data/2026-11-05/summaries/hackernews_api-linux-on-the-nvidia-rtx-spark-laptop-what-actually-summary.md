---
title: Linux on the Nvidia RTX Spark Laptop: What Actually Works | MindStudio
url: https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop
date: 2026-11-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-05T15:24:36.230417
---

# Linux on the Nvidia RTX Spark Laptop: What Actually Works | MindStudio

# Linux on the Nvidia RTX Spark Laptop: What Actually Works

## TL;DR
- Dual‑booting Linux on MSI Prestige (or similar RTX Spark laptops) works: full desktop, 4K @ 120 Hz, audio, keyboard, touchpad, and CUDA acceleration when the right drivers are used.  
- A Windows‑only component called **Nvidia Platform Controllers and Framework** controls power delivery; Linux lacks an equivalent, causing the GPU to stay at ~780 MHz when the laptop is plugged in.  
- On Windows the GPU runs ~2.2 GHz, delivering ~65 tokens / s on a 120 B GPT model; native Linux drops to ~14 tokens / s because of the clock‑speed limit.  
- The laptop reserves 96 GB of its 128 GB unified memory for the GPU; only Windows lets you shrink that reservation, otherwise Linux sees only ~28 GB.  
- WSL (Windows Subsystem for Linux) gives near‑native performance because it uses the Windows driver stack, keeping full GPU boost on both AC and battery.  
- A proper fix requires Nvidia to port the platform‑controller power‑management logic to its Linux driver.

## What makes the RTX Spark laptop different
- Uses the same GPU architecture as Nvidia’s DGX Spark desktop, but ships with Windows on ARM instead of a Linux build.  
- Supports up to 128 GB of unified memory shared between CPU and GPU, a feature aimed at AI developers.  
- The AI toolchain (vLLM, SGLang, etc.) is largely Linux‑first, so developers want to know if they can run Linux without losing performance.

## Installing Linux
- Not plug‑and‑play; early attempts with Omarchy (Arch‑based) produced a flickering display on the MSI Prestige.  
- Debian installed more reliably but lacked drivers for keyboard, touchpad, GPU, and Wi‑Fi, requiring a USB Ethernet adapter.  
- Returning to Omarchy gave a kernel with Nvidia’s open‑source driver, allowing the system to boot, but only 28 GB of RAM was visible because the firmware reserves 96 GB for the GPU.  
- Reducing the Windows‑side GPU memory reservation to 4 GB freed ~120 GB for Linux; after that the desktop ran at 4K @ 120 Hz with all peripherals working.  
- HDMI output was initially limited to the internal screen, forcing a workaround with an external camera to monitor the install.

## Performance comparison
- **Windows (native)**: ~65.4 tokens / s on GPT‑OSS‑120B, GPU ~2.2 GHz.  
- **WSL**: ~65.1 tokens / s, essentially identical to Windows.  
- **DGX Spark (Linux)**: ~61 tokens / s.  
- **Native Linux on laptop**: ~13.9 tokens / s, GPU stuck at ~780 MHz.  
- With vLLM (8 clients): WSL ~127 tokens / s, native Linux ~39.5 tokens / s.  
- Unplugged (battery) Linux can reach 61‑67 tokens / s, matching Windows; plugged‑in it falls to ~15 tokens / s due to the clock‑speed drop.

## Why plugging in the laptop slows Linux down
- The **Nvidia Platform Controllers and Framework** device in Windows manages the shared power budget between CPU and GPU.  
- Disabling this controller in Windows reproduces the Linux slowdown: GPU clock falls from ~2 GHz to ~786 MHz, tokens per second drop accordingly.  
- The firmware supplies an encrypted power‑table; Windows has the decryption key, Linux does not.  
- Attempts to extract the key or patch the driver caused instability (kernel panic) and are not viable long‑term solutions.  
- A true fix must come from Nvidia adding the same power‑management logic to its Linux driver.

## Is WSL a good substitute for native Linux right now?
- Yes, for most developers.  
- WSL runs on top of the Windows driver stack, inheriting full GPU boost regardless of power source.  
- It provides near‑native performance for AI workloads while still allowing use of Linux‑first tools (vLLM, etc.).  

## Outlook
- The only sustainable solution is for Nvidia to release a Linux driver that includes the platform‑controller power‑management component, effectively turning RTX Spark laptops into portable DGX Spark devices.