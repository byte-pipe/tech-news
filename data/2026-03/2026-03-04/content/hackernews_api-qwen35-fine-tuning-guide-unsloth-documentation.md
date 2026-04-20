---
title: Qwen3.5 Fine-tuning Guide | Unsloth Documentation
url: https://unsloth.ai/docs/models/qwen3.5/fine-tune
site_name: hackernews_api
content_file: hackernews_api-qwen35-fine-tuning-guide-unsloth-documentation
fetched_at: '2026-03-04T19:19:38.474578'
original_url: https://unsloth.ai/docs/models/qwen3.5/fine-tune
author: bilsbie
date: '2026-03-04'
description: Learn how to fine-tune Qwen3.5 LLMs locally with Unsloth.
tags:
- hackernews
- trending
---

You can now fine-tuneQwen3.5model family (0.8B, 2B, 4B, 9B, 27B, 35B‑A3B, 122B‑A10B) withUnslotharrow-up-right. Support includes bothvisionand text fine-tuning.Qwen3.5‑35B‑A3B- bf16 LoRA works on74GB VRAM.

* Unsloth makes Qwen3.5 train1.5× fasterand uses50% less VRAMthan FA2 setups.
* Qwen3.5 bf16 LoRA VRAM use:0.8B: 3GB •2B: 5GB •4B: 10GB •9B: 22GB •27B: 56GB
* Fine-tune0.8B,2Band4Bbf16 LoRA via ourfreeGoogle Colab notebooks:

Qwen3.5-0.8Barrow-up-right

Qwen3.5-2Barrow-up-right

Qwen3.5-4Barrow-up-right

* If you want topreserve reasoningability, you can mix reasoning-style examples with direct answers (keep a minimum of 75% reasoning). Otherwise you can emit it fully.
* Full fine-tuning (FFT)works as well. Note it will use 4x more VRAM.
* Qwen3.5 is powerful for multilingual fine-tuning as it supports 201 languages.
* After fine-tuning, you can export toGGUF(for llama.cpp/Ollama/LM Studio/etc.) orvLLM
* Reinforcement Learning(RL) for Qwen3.5VLM RLalso works via Unsloth inference.
* We haveA100Colab notebooks forQwen3.5‑27Barrow-up-rightandQwen3.5‑35B‑A3Barrow-up-right.

If you’re on an older version (or fine-tuning locally), update first:

Copy
pip

install

--upgrade

--force-reinstall

--no-cache-dir

unsloth

unsloth_zoo
circle-exclamation

Please usetransformers v5for Qwen3.5. Older versions will not work. Unsloth automatically uses transformers v5 by default now (except for Colab environments).

If training seemsslower than usual, it’s because Qwen3.5 use custom Mamba Triton kernels. Compiling those kernels can take longer than normal, especially on T4 GPUs.

It is not recommended to doQLoRA (4-bit)training on the Qwen3.5 models, no matter MoE or dense, due to higher than normal quantization differences.

### hashtagMoE fine-tuning (35B, 122B)

For MoE models likeQwen3.5‑35B‑A3B / 122B‑A10B / 397B‑A17B:

* You can use ourQwen3.5‑35B‑A3B (A100)arrow-up-rightfine-tuning notebook
* Supports our recent ~12x fasterMoE training updatewith >35% less VRAM & ~6x longer context
* Best to use bf16 setups (e.g. LoRA or full fine-tuning)(MoE QLoRA 4‑bit is not recommended due to BitsandBytes limitations).
* Unsloth’s MoE kernels are enabled by default and can use different backends; you can switch withUNSLOTH_MOE_BACKEND.
* Router-layer fine-tuning is disabled by default for stability.
* Qwen3.5‑122B‑A10B - bf16 LoRA works on 256GB VRAM. If you're using multiGPUs, adddevice_map = "balanced"or follow ourmultiGPU Guide.

### hashtagQuickstart

Below is a minimal SFT recipe (works for “text-only” fine-tuning). See also ourvision fine-tuningsection.

Loader example for MoE (bf16 LoRA):

Once loaded, you’ll attach LoRA adapters and train similarly to the SFT example above.

### hashtagVision fine-tuning

Unsloth supportsvision fine-tuningfor the multimodal Qwen3.5 models. Use the below Qwen3.5 notebooks and change the respective model names to your desired Qwen3.5 model.

Qwen3.5-0.8Barrow-up-right

Qwen3.5-2Barrow-up-right

Qwen3.5-4Barrow-up-right

Qwen3.5-9B

* Qwen3-VL GRPO/GSPO RL notebookarrow-up-right(change model name to Qwen3.5-4B etc.)

Disabling Vision / Text-only fine-tuning:

To fine-tune vision models, we now allow you to select which parts of the mode to finetune. You can select to only fine-tune the vision layers, or the language layers, or the attention / MLP layers! We set them all on by default!

In order to fine-tune or train Qwen3.5 with multi-images,view ourmulti-image vision guide.

### hashtagSaving / export fine-tuned model

You can view our specific inference / deployment guides forllama.cpp,vLLM,llama-server,Ollama,LM StudioorSGLang.

#### hashtagSave to GGUF

Unsloth supports saving directly to GGUF:

Or push GGUFs to Hugging Face:

If the exported model behaves worse in another runtime, Unsloth flags the most common cause:wrong chat template / EOS token at inference time(you must use the same chat template you trained with).

#### hashtagSave to vLLM

circle-exclamation

vLLM version0.16.0does not support Qwen3.5. Wait until0.170or try the Nightly release.

To save to 16-bit for vLLM, use:

To save just the LoRA adapters, either use:

Or use our builtin function:

For more details read our inference guides:

🖥️
Inference & Deployment
chevron-right
GGUF & llama.cpp
chevron-right
vLLM
chevron-right
Troubleshooting Inference
chevron-right
Previous
Qwen3.5 GGUF Benchmarks
chevron-left
Next
Qwen3-Coder-Next
chevron-right

Last updated44 minutes ago

Was this helpful?
