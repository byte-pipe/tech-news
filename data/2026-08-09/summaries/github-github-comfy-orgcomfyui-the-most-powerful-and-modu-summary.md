---
title: GitHub - Comfy-Org/ComfyUI: The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. · GitHub
url: https://github.com/Comfy-Org/ComfyUI
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-08-09T00:35:31.730250
---

# GitHub - Comfy-Org/ComfyUI: The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. · GitHub

# ComfyUI Overview

## Description
- A modular AI engine with a visual node‑graph interface for creating images, video, audio, 3D models, text and more.  
- Designed for visual professionals who need fine‑grained control over models, parameters and outputs.  

## Supported Models (representative list)  
- **Image generation:** Stable Diffusion 1.5, SDXL, SD3.5, Flux 1/2, Qwen Image, Z‑Image, Hunyuan 2.1, HiDream, Lumina 2.0, Chroma, Anima, LongCat, Ideogram 4, Krea 2, MageFlow, Microsoft Lens, PixelDiT, Kandinsky 5, Ernie Image.  
- **Image editing:** Flux Kontext, Flux 2 Klein, Qwen Image Edit, HiDream E1.1/O1, OmniGen2, Boogu, JoyImage Edit, MageFlow Edit, LongCat Edit.  
- **Video generation:** Wan 2.1/2.2, LTX‑Video 2/2.3, HunyuanVideo 1.5, Kandinsky 5 Video, CogVideoX, Cosmos Predict2, Bernini‑R, SCAIL 2, Mochi.  
- **Audio & video generation:** MiniMax H3, LTX‑AV.  
- **Audio generation:** ACE‑Step 1.5, Stable Audio 3.  
- **3D & vision:** Hunyuan3D 2.1, TripoSplat, SeedVR2, SUPIR, Depth Anything 3, MoGe, SAM 3/3.1, RT‑DETRv4, BiRefNet.  
- **Text generation:** Gemma 3/4, Qwen 3, Qwen 3.5, Qwen‑VL (multimodal).  

## Getting Started  

### Local  
- **Desktop Application:** Easiest entry point; Windows & macOS.  
- **Windows Portable Package:** Latest commits, fully portable.  
- **Manual Install:** Works on all OSes and GPU types (NVIDIA, AMD, Intel, Apple Silicon, Ascend).  

### Cloud  
- **Comfy Cloud:** Official paid cloud service for users without suitable local hardware.  

## Core Features  
- Visual node graph for building and reusing workflows without code.  
- Reusable subgraphs, workflow templates, App Mode, and a local API for integration.  
- Efficient execution: asynchronous queueing, partial graph re‑execution, smart VRAM/RAM management, model offloading, support for quantized models.  
- Load full checkpoints or separate components (diffusion models, VAEs, text encoders, LoRAs, ControlNets, adapters, upscalers).  
- Built‑in tools: inpainting, outpainting, reference conditioning, masks, compositing, model merging, upscaling, frame interpolation, segmentation, depth estimation, media processing.  
- Save/load workflows as JSON; recover complete workflows and seeds from generated media.  
- Fully offline operation unless optional paid API nodes are enabled (`--disable-api-nodes`).  
- Extensible via custom nodes and additional model locations (`extra_model_paths.yaml`).  

## Release Process  
- Weekly release cycle (target Monday, may shift due to model releases or major changes).  
- Three linked repositories:  
  1. **ComfyUI Core** – major stable version every ~2 weeks; patch versions for back‑ported fixes; minor versions for master‑branch releases.  
  2. **Comfy Desktop** – builds on the latest stable core version.  
  3. **ComfyUI Frontend** – frontend updates merged into core every 2+ weeks; features frozen before the upcoming core release.  
- Commits outside stable tags can be unstable and may break custom nodes.  

## Keyboard Shortcuts  

| Keybind | Action |
|---------|--------|
| Ctrl + Enter | Queue current graph for generation |
| Ctrl + Shift + Enter | Queue current graph as first in the queue |
| Ctrl + Alt + Enter | Cancel current generation |
| Ctrl + Z / Ctrl + Y | Undo / Redo |
| Ctrl + S | Save workflow |
| Ctrl + O | Load workflow |
| Ctrl + A | Select all nodes |
| Alt + C | Collapse / uncollapse selected nodes |
| Ctrl + M | Mute / unmute selected nodes |
| Ctrl + B | Bypass selected nodes (reconnect wires as if node removed) |
| Delete / Backspace | Delete selected nodes |
| Ctrl + Backspace | Delete the entire graph |
| Space (hold) | Pan canvas while moving cursor |
| Ctrl / Shift + Click | Additional selection/modifier actions |