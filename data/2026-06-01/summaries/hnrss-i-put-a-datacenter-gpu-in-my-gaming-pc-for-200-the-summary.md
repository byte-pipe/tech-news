---
title: I Put a Datacenter GPU in My Gaming PC for £200 :: The Tymscar Blog
url: https://blog.tymscar.com/posts/v100localllm/
date: 2026-05-31
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-01T04:18:10.993304
---

# I Put a Datacenter GPU in My Gaming PC for £200 :: The Tymscar Blog

# I Put a Datacenter GPU in My Gaming PC for £200

## Motivation
- Existing RTX 4080 (16 GB VRAM) is sufficient for gaming but not for the local LLMs I want to run.  
- Upgrading to a consumer GPU with more VRAM would be very expensive, so I looked for an alternative.

## The Datacenter GPU
- Purchased a Tesla V100 SXM2 (16 GB HBM2) for about £150 on eBay.  
- Volta architecture: 5120 CUDA cores, 900 GB/s memory bandwidth (4096‑bit bus).  
- Bandwidth exceeds that of the RTX 4080 (736 GB/s) and even beats recent Apple M‑series chips.  
- Compared to consumer GPUs:  
  - RX 7900 XTX: 960 GB/s, £700+, ROCm support still rough.  
  - RTX 5090: 1792 GB/s, >£2 000.  
  - V100 offers ~94 % of the top consumer bandwidth for a fraction of the price and works with llama.cpp.

## The Adapter
- Used a third‑party SXM2‑to‑PCIe adapter (bare PCB) costing ~£50.  
- Allows the V100 to sit in a standard PCIe slot alongside the RTX 4080, giving a combined 32 GB VRAM pool.  
- Total hardware cost ≈£200, far cheaper than a single 32 GB consumer GPU.

## Fan Noise Issue
- The V100’s server‑grade fan is loud (≈82 dB) and has no software control.  
- Initial attempts with nvidia‑smi, Afterburner, etc., failed to affect speed.

### Fan Control Solution
- Tested fan pins with a 9 V battery; it spun quieter, confirming a standard 4‑pin case‑fan layout.  
- Connected the fan’s PWM and tachometer pins to a spare motherboard fan header using jumper wires; PWM control worked.  
- Replaced the ad‑hoc wiring with a 2.54 mm male‑to‑2.0 mm JST PH2.0 female jumper cable.  
- Set fan to 10 % duty; temperature stays below 50 °C and noise becomes tolerable.

## Doubling VRAM Cheaply
- With both GPUs installed:  
  - RTX 4080: 16 GB (Ada)  
  - V100: 16 GB (Volta)  
  - Total: 32 GB VRAM across two cards.  
- llama.cpp splits the model across GPUs via tensor splitting over PCIe; performance is lower than a single 32 GB card but sufficient for a 27 B parameter model (~32 tokens/s).  
- Power draw peaks around 150 W for the V100.

### Scaling Further
- 32 GB V100 variant exists; a single card would give 32 GB VRAM for a few hundred pounds.  
- Two 32 GB V100s would provide 64 GB VRAM at roughly 20 % of the cost of an RTX 5090.  
- SXM2 form factor supports native NVLink, enabling high‑bandwidth multi‑GPU clusters even through the PCIe adapter.

## Software Setup (NixOS)
- Volta GPUs are unsupported by drivers ≥560; needed legacy driver branch 550.x.  
- Legacy driver supports CUDA 12.2, while current nixpkgs provides CUDA 12.6+, so CUDA 12.2 was pulled from an older overlay.  
- Kernel requirement: version 6.6; newer kernels break the legacy driver.  
- Even for headless inference, `services.xserver.enable = true` is required for the NVIDIA kernel modules to load.  
- Key NixOS configuration snippets:  
  ```nix
  boot.kernelPackages = pkgs.linuxPackages_6_6;
  hardware.nvidia.package = config.boot.kernelPackages.nvidiaPackages.legacy_535;
  services.xserver.enable = true;
  services.xserver.videoDrivers = [ "nvidia" ];
  nixpkgs.overlays = [
    (final: prev: {
      cudaPackages_12_2 = nixpkgs-cuda.legacyPackages.${prev.system}.cudaPackages_12_2;
    })
  ];
  ```

## Takeaway
- By repurposing a cheap, second‑hand datacenter GPU and a simple adapter, I achieved a 32 GB VRAM setup for ~£200, enabling local inference of large language models at reasonable speed.  
- The main hurdles were mechanical (fan noise) and software (legacy driver, kernel, CUDA version), all of which were resolved with modest effort on NixOS.