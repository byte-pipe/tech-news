---
title: 'GitHub - NVlabs/Sana: SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer · GitHub'
url: https://github.com/NVlabs/Sana
site_name: github
content_file: github-github-nvlabssana-sana-efficient-high-resolution-i
fetched_at: '2026-05-18T12:11:38.559417'
original_url: https://github.com/NVlabs/Sana
author: NVlabs
description: 'SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer - NVlabs/Sana'
---

NVlabs

 

/

Sana

Public

* NotificationsYou must be signed in to change notification settings
* Fork446
* Star6.3k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

170 Commits
170 Commits
.github/
workflows
.github/
workflows
 
 
CIs
CIs
 
 
app
app
 
 
asset
asset
 
 
configs
configs
 
 
diffusion
diffusion
 
 
docs
docs
 
 
inference_video_scripts
inference_video_scripts
 
 
sana
sana
 
 
scripts
scripts
 
 
tests/
bash
tests/
bash
 
 
tools
tools
 
 
train_scripts
train_scripts
 
 
train_video_scripts
train_video_scripts
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
CITATION.cff
CITATION.cff
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
environment_setup.sh
environment_setup.sh
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

### 📚 Docs|SANA|SANA-1.5|SANA-Sprint|SANA-Video|SANA-WM|Sol-RLDemo|🤗 HuggingFace|ComfyUI|SGLang|Cosmos-RL

  
 
  
 
  
 
  
 
  

  
 
  

#### ICLR 2025 Oral | ICML 2025 | ICCV 2025 Highlight | ICLR 2026 Oral

SANAis an efficiency-oriented codebase for high-resolution image and video generation, providing complete training and inference pipelines. This repository contains code forSANA,SANA-1.5,SANA-Sprint,SANA-Video,SANA-WM, andSol-RL. More details can be found in our📚 documentation.

Join ourDiscordto engage in discussions with the community! If you have any questions, run into issues, or are interested in contributing, don't hesitate to reach out!

## News

* 🔥 [2026/05] 🌍SANA-WM: 2.6B Controllable World Modelis released! Supports 720p, 1-min video generation with 6-DoF camera control. A new baseline for World Modeling and Embodied AI. SeeProject|Paper.
* 🔥 [2026/04] ⚡Sol-RL: NVFP4 Rollout, BF16 Training RLis available! All training recipes forSANA,FLUX.1, andSD3.5-L, together with bundled post-training datasets, are released. SeeSol-RL doc|Page|Paper.
* 🔥 [2026/03] 📺SANA-Video 720p model with LTX-VAEis released. Use it with LTX2 Refiner to upscale the videos to 2K resolution! SeeModel Zoo,SANA-Video docandBlog about refiner.
* 🔥 [2026/03] 💪Post Training Infra: SANA × Cosmos-RL— We partner withCosmos-RLto provide a complete RL infrastructure for SANA. You can now post-train (SFT/RL) SANA-Image and SANA-Video with state-of-the-art algorithms (e.g. Diffusion-NFT, Flow-GRPO), preset configs, reward services, and flexible datasets. SeeSANA on Cosmos-RLand ourCosmos-RL integration doc.
* 🔥 [2026/02] 🚀SANA is now supported inSGLang!High-performance serving with OpenAI-compatible API.[Guidance]
* 🔥 [2026/01/26]SANA-Video is accepted as Oral by ICLR-2026.🎉🎉🎉
* 🔥 [2025/12/09] 🎬LongSANA: 27FPS real-time minute-length video generation model, training and inference code are all released. Thanks toLongLive Team. Refer to:[Train]|[Test]|[Weight]
* 🔥 [2025/11/24] 🪶Blog: how Causal Linear Attention unlocks infinite context for LLMs and long video generation.
* 🔥 [2025/11/9] 🎬Introduction videoshows how Block Causal Linear Attention and Causal Mix-FFN work?
* 🔥 [2025/11/6] 📺SANA-Videois merged intodiffusers.How to use.
* 🔥 [2025/10/27] 📺SANA-Videois released.[README]|[Weights]support Text-to-Video, TextImage-to-Video.
* 🔥 [2025/10/13] 📺SANA-Videois coming, 1). a 5s Linear DiT Video model, and 2). real-time minute-length video generation (withLongLive).[paper]|[Page]

Click to show all updates

* ✅ [2025/8/20] We release a new DC-AE-Lite for faster inference and smaller memory.[How to config]|[diffusers PR]|[Weight]
* ✅ [2025/6/25]SANA-Sprintwas accepted to ICCV'25 🏖️
* ✅ [2025/6/4] SANA-SprintComfyUI Nodeis released[Example].
* ✅ [2025/5/8] SANA-Sprint (One-step diffusion) diffusers training code is released[Guidance].
* ✅ [2025/5/4]SANA-1.5 (Inference-time scaling) is accepted by ICML-2025.🎉🎉🎉
* ✅ [2025/3/22] 🔥SANA-Sprint demo is hosted on Huggingface, try it!🎉[Demo Link]
* ✅ [2025/3/22] 🔥SANA-1.5 is supported in ComfyUI!🎉:ComfyUI Guidance|ComfyUI Work Flow SANA-1.5 4.8B
* ✅ [2025/3/22] 🔥SANA-Sprint code & weights are released!🎉 Include:Training & Inferencecode andWeights/HFare all released.[Guidance]
* ✅ [2025/3/21] 🚀Sana +Inference Scalingis released.[Guidance]
* ✅ [2025/3/16] 🔥SANA-1.5 code & weights are released!🎉 Include:DDP/FSDP|TAR file WebDataset|Multi-ScaleTraining code andWeights|HFare all released.
* ✅ [2025/3/14] 🏃SANA-Sprint is coming out!🎉 A new one/few-step generator of Sana. 0.1s per 1024px image on H100, 0.3s on RTX 4090. Find out more details:[Page]|[Arxiv]. Code is coming very soon along withdiffusers
* ✅ [2025/2/10] 🚀Sana + ControlNet is released.[Guidance]|[Model]|[Demo]
* ✅ [2025/1/30] Release CAME-8bit optimizer code. Saving more GPU memory during training.[How to config]
* ✅ [2025/1/29] 🎉 🎉 🎉SANA 1.5 is out! Figure out how to do efficient training & inference scaling!🚀[Tech Report]
* ✅ [2025/1/24] 4bit-Sana is released, powered bySVDQuant and Nunchakuinference engine. Now run your Sana within8GBGPU VRAM[Guidance][Demo][Model]
* ✅ [2025/1/24] DCAE-1.1 is released, better reconstruction quality.[Model][diffusers]
* ✅ [2025/1/23]Sana is accepted as Oral by ICLR-2025.🎉🎉🎉
* ✅ [2025/1/12] DC-AE tiling makes Sana-4K inferences 4096x4096px images within 22GB GPU memory. With model offload and 8bit/4bit quantize. The 4K Sana run within8GBGPU VRAM.[Guidance]
* ✅ [2025/1/11] Sana code-base license changed to Apache 2.0.
* ✅ [2025/1/10] Inference Sana with 8bit quantization.[Guidance]
* ✅ [2025/1/8] 4K resolutionSana modelsis supported inSana-ComfyUIandwork flowis also prepared.[4K guidance]
* ✅ [2025/1/8] 1.6B 4K resolutionSana modelsare released:[BF16 pth]or[BF16 diffusers]. 🚀 Get your 4096x4096 resolution images within 20 seconds! Find more samples inSana page. ThanksSUPIRfor their wonderful work and support.
* ✅ [2025/1/2] Bug in thediffuserspipeline is solved.Solved PR
* ✅ [2025/1/2] 2K resolutionSana modelsis supported inSana-ComfyUIandwork flowis also prepared.
* ✅ [2024/12] 1.6B 2K resolutionSana modelsare released:[BF16 pth]or[BF16 diffusers]. 🚀 Get your 2K resolution images within 4 seconds! Find more samples inSana page. ThanksSUPIRfor their wonderful work and support.
* ✅ [2024/12]diffuserssupports Sana-LoRA fine-tuning! Sana-LoRA's training and convergence speed is super fast.[Guidance]or[diffusers docs].
* ✅ [2024/12]diffusershas Sana!All Sana models in diffusers safetensorsare released and diffusers pipelineSanaPipeline,SanaPAGPipeline,DPMSolverMultistepScheduler(with FlowMatching)are all supported now. We prepare aModel Cardfor you to choose.
* ✅ [2024/12] 1.6B BF16Sana modelis released for stable fine-tuning.
* ✅ [2024/12] We release theComfyUI nodefor Sana.[Guidance]
* ✅ [2024/11] All multi-linguistic (Emoji & Chinese & English) SFT models are released:1.6B-512px,1.6B-1024px,600M-512px,600M-1024px. The metric performance is shownhere
* ✅ [2024/11] Sana Replicate API is launching atSana-API.
* ✅ [2024/11] 1.6BSana modelsare released.
* ✅ [2024/11] Training & Inference & Metrics code are released.
* ✅ [2024/11] Working ondiffusers.
* [2024/10]Demois released.
* [2024/10]DC-AE Codeandweightsare released!
* [2024/10]Paperis on Arxiv!

## 💡 Introduction

We introduceSANA, a series of efficient diffusion models for high-resolution image and video generation:

* SANA: Text-to-image generation up to 4K resolution,20× smaller and 100× fasterthan Flux-12B.
* SANA-1.5: Efficient training-time and inference-time compute scaling for better quality.
* SANA-Sprint: One/few-step generation via sCM distillation,0.1s per 1024px imageon H100.
* SANA-Video/LongSANA: Efficient video generation with Block Linear Attention / withLongLive.
* Sol-RL: NVFP4 Rollout, BF16 Training RL achieves4.64× faster convergence.
* SANA-WM: 2.6B parameter controllable world model, generating 720p, 1-minute video worlds with 6-DoF camera control.

Key Techniques:

* Linear Attention: Replace vanilla attention in DiT with linear attention for efficiency at high resolutions.
* DC-AE: 32× image compression (vs. traditional 8×) to reduce latent tokens.
* Decoder-only Text Encoder: Modern decoder-only LLM with in-context learning for better text-image alignment.
* Block Causal Linear Attention & Causal Mix-FFN: Efficient attention and feedforward for long video generation.
* Flow-DPM-Solver: Reduce sampling steps with efficient training and sampling.
* sCM Distillation: One/few-step generation with continuous-time consistency distillation.
* Sol-RL: Low precision(NVFP4) rollout selection, high precesion(BF16) optimization for faster RL training.
* Controllable World Modeling: Efficient long-context modeling and camera trajectory control for consistent world generation.

In summary, SANA is a fully open-source framework integratingefficient training, fast inference, and flexible deploymentfor both image and video generation. Deployable on laptop GPUs with< 8GB VRAMvia 4-bit quantization.

## Quick Start

git clone https://github.com/NVlabs/Sana.git

cd
 Sana 
&&
 ./environment_setup.sh sana

### Inference with 🧨 diffusers

import
 
torch

from
 
diffusers
 
import
 
SanaPipeline

pipe
 
=
 
SanaPipeline
.
from_pretrained
(
 
"Efficient-Large-Model/SANA1.5_1.6B_1024px_diffusers"
,
 
torch_dtype
=
torch
.
bfloat16
,
)

pipe
.
to
(
"cuda"
)

pipe
.
vae
.
to
(
torch
.
bfloat16
)

pipe
.
text_encoder
.
to
(
torch
.
bfloat16
)

prompt
 
=
 
'a cyberpunk cat with a neon sign that says "Sana"'

image
 
=
 
pipe
(
 
prompt
=
prompt
,
 
height
=
1024
,
 
width
=
1024
,
 
guidance_scale
=
4.5
,
 
num_inference_steps
=
20
,
 
generator
=
torch
.
Generator
(
device
=
"cuda"
).
manual_seed
(
42
),
)[
0
]

image
[
0
].
save
(
"sana.png"
)

Tip

Upgrade yourdiffusers>=0.32.0to useSanaPipeline. More details can be found in📚 Docs.

## Getting Started

* 📚Full Documentation
* Installation Guide
* Model Zoo
* Sana Inference & Training
* SANA-Sprint
* SANA-Video
* LongSANA
* SANA-WM(coming soon)
* ControlNet
* LoRA / DreamBooth
* Sol-RL Post-Training
* Quantization (4bit / 8bit)
* ComfyUI
* SGLang

## Performance

### Image Generation (1024px)

Methods (1024x1024)

Throughput (samples/s)

Latency (s)

Params (B)

Speedup

FID 👇

CLIP 👆

GenEval 👆

DPG 👆

FLUX-dev

0.04

23.0

12.0

1.0×

10.15

27.47

0.67

84.0

Sana-0.6B

1.7

0.9

0.6

39.5×

5.81

28.36

0.64

83.6

Sana-0.6B

1.7

0.9

0.6

39.5×

5.61

28.80

0.68

84.2

Sana-1.6B

1.0

1.2

1.6

23.3×

5.92

28.94

0.69

84.5

Sana-1.5 1.6B

1.0

1.2

1.6

23.3×

5.70

29.12

0.82

84.5

Sana-1.5 4.8B

0.26

4.2

4.8

6.5×

5.99

29.23

0.81

84.7

### Video Generation (VBench 720p)

Models

Latency (s)

Params (B)

VBench Total ↑

Quality ↑

Semantic ↑

Wan-2.1-14B

1897

14

83.73

85.77

75.58

Wan-2.1-1.3B

400

1.3

83.38

85.67

74.22

SANA-Video-2B

36

2

84.05

84.63

81.73

# 💪To-Do List

We will try our best to achieve

* [✅] Training code
* [✅] Inference code
* [✅] Model zoo
* [✅]ComfyUI Nodes(SANA, SANA-1.5,
SANA-Sprint)
* [✅] DC-AE Diffusers
* [✅] Sana merged in Diffusers(huggingface/diffusers#9982)
* [✅] LoRA training by@paul(diffusers:https://github.com/huggingface/diffusers/pull/10234)
* [✅] 2K/4K resolution models.(Thanks@SUPIRto
provide a 4K super-resolution model)
* [✅] 8bit / 4bit Laptop development
* [✅] ControlNet (train & inference & models)
* [✅] FSDP Training
* [✅] SANA-1.5 (Larger model size / Inference Scaling)
* [✅] SANA-Sprint: Few-step generator
* [✅] Faster DCAE-Liteweight
* [✅] Better re-construction F32/F64VAEs
* [✅] SANA-Video: Linear DiT Video model, and real-time minute-length video generation
* [✅] RL Post-training: collaborate withCosmos-RL
* [] SANA World Model
* [] SANA Streaming Video-to-Video Editing
* [🚀] See you in the future

## 🤗 Acknowledgements

Thanks to the following open-sourced projects:

Thanks to the following open-sourced codebase for their wonderful work and codebase!

* PixArt-α
* PixArt-Σ
* diffusers
* Efficient-ViT
* ComfyUI_ExtraModels
* SVDQuant and Nunchaku
* Open-Sora
* Wan
* LongLive
* Cosmos-RL

ThanksPaper2Videofor generating Jeason presenting SANA😊. Refer toPaper2Videofor more details.

## Contribution

Thanks go to these wonderful contributors:

## 🌟 Star History

# 📖 BibTeX

@misc
{
xie2024sana
,
 
title
=
{
Sana: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer
}
,
 
author
=
{
Enze Xie and Junsong Chen and Junyu Chen and Han Cai and Haotian Tang and Yujun Lin and Zhekai Zhang and Muyang Li and Ligeng Zhu and Yao Lu and Song Han
}
,
 
year
=
{
2024
}
,
 
eprint
=
{
2410.10629
}
,
 
archivePrefix
=
{
arXiv
}
,
 
primaryClass
=
{
cs.CV
}
,
 
url
=
{
https://arxiv.org/abs/2410.10629
}
,
 }

Click to expand all BibTeX citations

@misc
{
xie2025sana
,
 
title
=
{
SANA 1.5: Efficient Scaling of Training-Time and Inference-Time Compute in Linear Diffusion Transformer
}
,
 
author
=
{
Xie, Enze and Chen, Junsong and Zhao, Yuyang rectangle and Yu, Jincheng and Zhu, Ligeng and Lin, Yujun and Zhang, Zhekai and Li, Muyang and Chen, Junyu and Cai, Han and others
}
,
 
year
=
{
2025
}
,
 
eprint
=
{
2501.18427
}
,
 
archivePrefix
=
{
arXiv
}
,
 
primaryClass
=
{
cs.CV
}
,
 
url
=
{
https://arxiv.org/abs/2501.18427
}
,
 }

@misc
{
chen2025sanasprint
,
 
title
=
{
SANA-Sprint: One-Step Diffusion with Continuous-Time Consistency Distillation
}
,
 
author
=
{
Junsong Chen and Shuchen Xue and Yuyang Zhao and Jincheng Yu graves and Sayak Paul and Junyu Chen and Han Cai and Song Han and Enze Xie
}
,
 
year
=
{
2025
}
,
 
eprint
=
{
2503.09641
}
,
 
archivePrefix
=
{
arXiv
}
,
 
primaryClass
=
{
cs.CV
}
,
 
url
=
{
https://arxiv.org/abs/2503.09641
}
,
 }

@misc
{
chen2025sanavideo
,
 
title
=
{
SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer
}
,
 
author
=
{
Chen, Junsong and Zhao, Yuyang and Yu, Jincheng and Chu, Ruihang and Chen, Junyu and Yang, Shuai and Wang, Xianbang and Pan, Yicheng and Zhou, Daquan and Ling, Huan and others
}
,
 
year
=
{
2025
}
,
 
eprint
=
{
2509.24695
}
,
 
archivePrefix
=
{
arXiv
}
,
 
primaryClass
=
{
cs.CV
}
,
 
url
=
{
https://arxiv.org/abs/2509.24695
}
,
 }

@misc
{
li2026fp4
,
 
title
=
{
FP4 Explore, BF16 Train: Diffusion Reinforcement Learning via Efficient Rollout Scaling
}
,
 
author
=
{
Li, Yitong and Chen, Junsong and Xue, Shuchen and Zeren, Pengcuo and Fu, Siyuan and Yang, Dinghao and Tang, Yangyang and Bai, Junjie and Luo, Ping and Han, Song and others
}
,
 
year
=
{
2026
}

 eprint=
{
2604.06916
}
,
 
archivePrefix
=
{
arXiv
}
,
 
primaryClass
=
{
cs.CV
}
,
 
url
=
{
https://arxiv.org/abs/2604.06916
}
,
}

@misc
{
zhu2026sanawm
,
 
title
=
{
SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer
}
, 
 
author
=
{
Haoyi Zhu and Haozhe Liu and Yuyang Zhao and Tian Ye and Junsong Chen and Jincheng Yu and Tong He and Song Han and Enze Xie
}
,
 
year
=
{
2026
}
,
 
eprint
=
{
2605.15178
}
,
 
archivePrefix
=
{
arXiv
}
,
 
primaryClass
=
{
cs.CV
}
,
 
url
=
{
https://arxiv.org/abs/2605.15178
}
, 
}

## About

SANA: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformer

nvlabs.github.io/Sana/docs/

### Topics

 reinforcement-learning

 transformers

 pytorch

 diffusion

 dit

 video-generation

 sana

 text-to-video

 linear-transformer

 text-to-image-generation

 system-algorithm-deisgn

 nvfp4

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

6.3k

 stars
 

### Watchers

84

 watching
 

### Forks

446

 forks
 

 Report repository

 

## Releases2

SANA-1.5 && SANA-Sprint

 Latest

 

Mar 25, 2025

 

+ 1 release

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python92.8%
* HTML4.5%
* Shell2.7%