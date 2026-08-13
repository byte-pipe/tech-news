---
title: Better Gaussian Splatting in Julia
url: https://pxl-th.github.io/blog/better-gs-julia/
date: 2026-08-09
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-14T06:02:57.322833
---

# Better Gaussian Splatting in Julia

# Better Gaussian Splatting in Julia

## Overview
- GaussianSplatting.jl 2.0 introduces quality‑of‑life improvements and new capabilities while keeping the same user workflow.  
- The application can be explored interactively (WASD + mouse or touch) and now runs more smoothly on various hardware.

## GPU Backends
- Written entirely in Julia and compiled with **KernelAbstractions.jl**.  
- Supports three GPU backends:
  - AMD GPUs via `AMDGPU.jl`  
  - NVIDIA GPUs via `CUDA.jl`  
  - Apple Silicon (MacBook) GPUs via `Metal.jl`

## Multithreaded UI
- UI and rendering are split into two threads:
  - **Frontend** – handles OpenGL rendering, UI interaction, and command dispatch.  
  - **Backend** – performs Gaussian splatting, training, dataset loading, and JIT compilation.  
- UI remains responsive; progress bars and spinners indicate ongoing background work.  
- Live loss plots and hyperparameter values are displayed during training.

## Densification Strategies
- Default cloning and splitting remain available.  
- New **Markov Chain Monte Carlo (MCMC) strategy**:
  - Gives precise control over the number of Gaussians.  
  - Reduces dependence on a good initialization.  
  - Activated via `MCMCStrategy` in the trainer configuration or through the UI.

## Depth & Geometry Supervision
- Depth priors can be added using external depth estimation models (e.g., Depth‑Anything 3).  
- Depth images must be placed under `<dataset-root>/depths/<FILENAME>.png`.  
- Enable with UI toggle or `OptimizationParams(; use_depth_loss=true)`.  
- Improves geometry, reduces floaters, and aligns surface orientation.  
- Optional geometry regularization (`use_normal_loss=true`) adds:
  - Depth‑normal consistency.  
  - Flattening of each Gaussian along its smallest axis.  

## Sky Dome
- Introduces a frozen shell of Gaussians at a large radius rendered in a separate pass.  
- Available as a full sphere or a hemisphere (the latter avoids occluding ground geometry).  
- Overhead is minimal (~32 k Gaussians vs. millions in the main scene).  
- Sky segmentation masks (`<dataset-root>/sky/<FILENAME>.png`) can further improve background separation.

## Camera Frustum Visualization
- Updated to show a miniature thumbnail of the image captured by each camera, aiding scene inspection.

## Additional Features
- Automatic checkpointing: saves every N steps to a chosen directory.  
- Custom hyperparameter configuration via `hyperparameters.toml` during dataset loading; can be saved for reproducibility.  
- Camera paths for Capture Mode can be saved, loaded, and reproduced across runs.  
- UI displays current VRAM usage.

## Acknowledgements
- Inspiration from LichtFeld Studio.  
- Contributions from the JuliaGPU ecosystem community.  

Feel free to try the updated version and provide feedback on the GitHub repository.