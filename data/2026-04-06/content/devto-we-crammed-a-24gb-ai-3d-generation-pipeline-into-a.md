---
title: We crammed a 24GB AI 3D-generation pipeline into a completely offline desktop app (and the Demo is live) - DEV Community
url: https://dev.to/raseiri/we-crammed-a-24gb-ai-3d-generation-pipeline-into-a-completely-offline-desktop-app-and-the-demo-is-12i5
site_name: devto
content_file: devto-we-crammed-a-24gb-ai-3d-generation-pipeline-into-a
fetched_at: '2026-04-06T11:21:50.248067'
original_url: https://dev.to/raseiri/we-crammed-a-24gb-ai-3d-generation-pipeline-into-a-completely-offline-desktop-app-and-the-demo-is-12i5
author: Riley Black
date: '2026-04-02'
description: If you are an indie game developer right now, you know the pain of 3D asset generation. The current... Tagged with ai, gamedev, showdev, tooling.
tags: '#showdev, #ai, #gamedev, #tooling'
---

If you are an indie game developer right now, you know the pain of 3D asset generation.

The current landscape of AI 3D tools is a nightmare of expensive monthly SaaS subscriptions, API paywalls, and cloud-based platforms that claim ownership over the meshes you generate. We got tired of it.

At Odyssey Game Studios, we decided to build the anti-SaaS solution: Jupetar. It’s a completely offline, local-compute 2D-to-3D asset generation pipeline. You pay once, you own the software, and it runs entirely on your local GPU.

After weeks of engineering (and battling the Steam review queue), the official Jupetar Demo is now live on Steam. Here is a look under the hood at how we built it, and how you can test it right now.

The "No-Ping" ArchitectureThe biggest challenge in building local AI wrappers is preventing the underlying scripts from constantly trying to phone home.

Jupetar relies on a massive 24GB local models folder containing the Hunyuan DiT (geometry) and Paint VAE (textures) weights. Standard HuggingFace implementations constantly try to ping the cloud to check for version updates or auto-heal missing files, which Valve (and privacy-conscious devs) understandably flag.

We surgically killed the huggingface_hub auto-heal scripts and forced strict offline environment variables directly into the pipeline:

os.environ["HF_HUB_OFFLINE"] = "1"os.environ["TRANSFORMERS_OFFLINE"] = "1"os.environ["DIFFUSERS_OFFLINE"] = "1"

The Ethernet Test: The ultimate proof of our architecture. You can literally unplug your ethernet cable, drop concept art into the UI, and Jupetar will still generate a fully textured .glb file.

Solving Local VRAM FragmentationLoading a massive Diffusion Transformer, XAtlas for UV unwrapping, and an FP32 rasterizer into a single localized PyTorch instance usually results in catastrophic memory leaks and Out-of-Memory (OOM) crashes on standard consumer GPUs.

To make this run stably on an 8GB-12GB VRAM card (our baseline is an RTX 3080 10GB), we had to force PyTorch expandable segments to mitigate memory fragmentation during the heaviest phase: the high-res 4K texture upscaling.

Our overarching C# wrapper handles the UI and hardware telemetry, acting as an orchestrator that spins up the Python environment, executes the generation, and actively flushes the VRAM at each pipeline stage.

What the Pipeline Actually DoesWhen you drop an image into Jupetar, it doesn't just spit out a messy point cloud. It executes a full, game-ready pipeline:

Geometry: Generates the raw mesh via Hunyuan3D.

Optimization: Runs an adaptive decimation pass (FaceReducer) to crunch meshes down to target poly-counts (e.g., 25k for weapons, 80k for humanoid creatures).

UV Mapping: Integrates XAtlas for automated, engine-ready UV unwrapping.

Texturing & PBR: Since native DiT vertex colors are blurry, the engine runs a VRAM-safe 4K tiled upscaler and synthesizes a procedural PBR normal map locally using Sobel derivatives.

Export: Packages everything into a standard .glb ready for Unity, Unreal, or Godot.

The Demo is LiveWe just pushed the Demo build live on Steam.

Because we don't have a centralized server to authenticate accounts, we built a localized trial logic directly into the app. The Demo gives you 2 completely free generations to test the pipeline, benchmark your GPU's VRAM, and inspect the final 3D topology for yourself.

No credit card, no account creation, no cloud processing.

🎮https://store.steampowered.com/app/4346660/Jupetar/?l=english

If you test it out, let me know how it handles on your specific GPU. We are continuing to optimize the C# orchestrator and VRAM management leading up to the V1.0 launch, and I'd love to hear feedback from the community!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse