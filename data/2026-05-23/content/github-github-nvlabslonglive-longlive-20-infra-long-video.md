---
title: 'GitHub - NVlabs/LongLive: LongLive 2.0: Infra - Long Video Gen · GitHub'
url: https://github.com/NVlabs/LongLive
site_name: github
content_file: github-github-nvlabslonglive-longlive-20-infra-long-video
fetched_at: '2026-05-23T11:28:39.848555'
original_url: https://github.com/NVlabs/LongLive
author: NVlabs
description: 'LongLive 2.0: Infra - Long Video Gen. Contribute to NVlabs/LongLive development by creating an account on GitHub.'
---

NVlabs

 

/

LongLive

Public

* NotificationsYou must be signed in to change notification settings
* Fork158
* Star1.7k

 
 
 
 
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

87 Commits
87 Commits
assets
assets
 
 
configs
configs
 
 
docs
docs
 
 
example
example
 
 
fouroversix
fouroversix
 
 
model
model
 
 
pipeline
pipeline
 
 
scripts
scripts
 
 
trainer
trainer
 
 
utils
utils
 
 
wan_5b
wan_5b
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
inference.py
inference.py
 
 
inference_sp.py
inference_sp.py
 
 
requirements.txt
requirements.txt
 
 
train.py
train.py
 
 
View all files

## Repository files navigation

# 🎬 LongLive 2.0: An NVFP4 Parallel Infrastructure for Long Video Generation

## 💡 TLDR: Infra with NVFP4 and parallelism for both training and inference

## News

* 🔥 [2026.05.13] We releaseLongLive 2.0, infra with NVFP4, parallelism and multi-shot for AR training, DMD distillation, and inference (⚡45.7 FPS). The original LongLive 1.0 is now in thev1.0branch.
* 🔥 [2026.04.12] LongLive supports kv cache compression withTriAttention, with 50% KV reduction and no quality drop. Check ithere
* 🎉 [2026.1.27] LongLive is accepted byICLR-2026.
* 🔥 [2026.1.11] LongLive supports adapting LongLive's original RoPE into KV-cache relative RoPE and generates infinite long videos!
* 🔥 [2025.11.3] We implement LongLive on linear attention modelSANA-Video! Now SANA-Video can generate 60s interactive videos in real-time.
* 🔥 [2025.9.29] We releasePaper, this GitHub repoLongLivewith all training and inference code, the model weightLongLive-1.3B, and demo pageWebsite.

## Introduction

LongLive 1.0: Real-time Interactive Long Video Generation.You can find it herein our V1.0 branch.

LongLive 2.0: an NVFP4 Parallel Infrastructure for Long Video Generation

* For training, it supportsBalanced sequence parallel for AR training (teacher-forcing).AR training on multi-shot (or single-shot) videos.NVFP4 (or BF16) for both AR training and few-step distillation.
* Balanced sequence parallel for AR training (teacher-forcing).
* AR training on multi-shot (or single-shot) videos.
* NVFP4 (or BF16) for both AR training and few-step distillation.
* For inference, it supportsNVFP4 inference (W4A4) and NVFP4 KV Cache.Multi-shot attention sink.Sequence parallel inference.Async decoding.
* NVFP4 inference (W4A4) and NVFP4 KV Cache.
* Multi-shot attention sink.
* Sequence parallel inference.
* Async decoding.

LongLive 1.0: Real-time Interactive Long Video Generation. It accepts sequential user prompts and generates corresponding videos in real time, enabling user-guided long video generation. The key insights are attention sink, KV-recache, and streaming long tuning.

## Getting Started

* Full Documentation
* Installation
* NVFP4 Setup
* Training
* Inference
* Data Organization

### Quick Start

#### BF16

import
 
torch

from
 
omegaconf
 
import
 
OmegaConf

from
 
pipeline
 
import
 
CausalDiffusionInferencePipeline

from
 
utils
.
config
 
import
 
normalize_config

from
 
utils
.
inference_utils
 
import
 (
 
load_generator_checkpoint
,
 
place_vae_for_streaming
,
 
prepare_single_prompt_inputs
,
 
save_video
,
)

prompt
 
=
 
"A compact silver robot walks through a clean robotics lab."

merged_checkpoint_path
 
=
 
"LongLive-2.0-5B/model_bf16.pt"

config
 
=
 
normalize_config
(
OmegaConf
.
load
(
"configs/inference.yaml"
))

device
 
=
 
torch
.
device
(
"cuda"
)

torch
.
set_grad_enabled
(
False
)

pipe
 
=
 
CausalDiffusionInferencePipeline
(
config
, 
device
=
device
)

load_generator_checkpoint
(
pipe
.
generator
, 
merged_checkpoint_path
)

pipe
 
=
 
pipe
.
to
(
device
=
device
, 
dtype
=
torch
.
bfloat16
)

place_vae_for_streaming
(
pipe
, 
config
) 
# honor streaming_vae + vae_device when set

pipe
.
generator
.
model
.
eval
().
requires_grad_
(
False
)

noise
, 
prompts
 
=
 
prepare_single_prompt_inputs
(
config
, 
prompt
, 
device
)

video
 
=
 
pipe
.
inference
(
noise
=
noise
, 
text_prompts
=
prompts
)

save_video
(
video
[
0
], 
"videos/quickstart/sample.mp4"
, 
fps
=
24
)

place_vae_for_streamingis a no-op unlessinference.streaming_vaeis true andinference.vae_deviceis set, so toggling streaming-pipeline decode in your yaml is enough — the script does not need to change.

#### NVFP4

Pointcheckpoints.generator_ckptinconfigs/nvfp4/inference_nvfp4.yamlat the downloaded checkpoint and setmodel_quant_use_transformer_engineaccording to the backend you are using:

* TransformerEngine checkpoint (model_te.pt):model_quant_use_transformer_engine: true
* FourOverSix checkpoint (model_4o6.pt):model_quant_use_transformer_engine: false

setup_nvfp4_pipelinehandles checkpoint loading, NVFP4 module wrapping, weight materialization, dtype/device placement, and the streaming-pipeline VAE relocation for both backends — the bf16pipe.to(...)shortcut is unsafe here because it would cast the quantized buffers.

import
 
torch

from
 
omegaconf
 
import
 
OmegaConf

from
 
pipeline
 
import
 
CausalDiffusionInferencePipeline

from
 
utils
.
config
 
import
 
normalize_config

from
 
utils
.
inference_utils
 
import
 
prepare_single_prompt_inputs
, 
save_video
, 
setup_nvfp4_pipeline

prompt
 
=
 
"A compact silver robot walks through a clean robotics lab."

config
 
=
 
normalize_config
(
OmegaConf
.
load
(
"configs/nvfp4/inference_nvfp4.yaml"
))

device
 
=
 
torch
.
device
(
"cuda"
)

torch
.
set_grad_enabled
(
False
)

pipe
 
=
 
CausalDiffusionInferencePipeline
(
config
, 
device
=
device
)

setup_nvfp4_pipeline
(
pipe
, 
config
, 
device
)

pipe
.
generator
.
model
.
eval
().
requires_grad_
(
False
)

noise
, 
prompts
 
=
 
prepare_single_prompt_inputs
(
config
, 
prompt
, 
device
)

video
 
=
 
pipe
.
inference
(
noise
=
noise
, 
text_prompts
=
prompts
)

save_video
(
video
[
0
], 
"videos/quickstart/sample_nvfp4.mp4"
, 
fps
=
24
)

## Models

Model

FPS ↑

Params

VBench ↑

Multi-shot

LongLive-1.3B

20.7

1.3B

84.87

LongLive-2.0-5B

24.8

5B

85.06

✅

LongLive-2.0-5B-NVFP4-4Step

29.7

5B

84.51

✅

LongLive-2.0-5B-NVFP4-2Step

45.7

5B

83.14

✅

## License

This repository is released under the Apache 2.0 license. SeeLICENSEfor details.

## Citation

Please consider citing our work if you find them useful:

@article
{
longlive_2.0
,
 
title
=
{
LongLive2.0: An NVFP4 Parallel Infrastructure for Long Video Generation
}
,
 
author
=
{
Chen, Yukang and Wang, Luozhou and Huang, Wei and Yang, Shuai and Zhang, Bohan and Xiao, Yicheng and Chu, Ruihang and Mao, Weian and Hu, Qixin and Liu, Shaoteng and Zhao, Yuyang and Mao, Huizi and Chen, Ying-Cong and Xie, Enze and Qi, Xiaojuan and Han, Song
}
,
 
journal
=
{
arXiv preprint arXiv
}
,
 
year
=
{
2026
}

}

@inproceedings
{
longlive
,
 
title
=
{
Longlive: Real-time interactive long video generation
}
, 
 
author
=
{
Yang, Shuai and Huang, Wei and Chu, Ruihang and Xiao, Yicheng and Zhao, Yuyang and Wang, Xianbang and Li, Muyang and Xie, Enze and Chen, Yingcong and Lu, Yao and others
}
,
 
booktitle
=
{
ICLR
}
,
 
year
=
{
2026
}
,
}

## Acknowledgement

* Self-Forcing: the AR training codebase and formulation we build upon.
* Wan2.2: the base video diffusion model components used in this release.

## About

LongLive 2.0: Infra - Long Video Gen

nvlabs.github.io/LongLive

### Topics

 real-time

 parallel

 infra

 long

 video-generation

 nvfp4

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.7k

 stars
 

### Watchers

18

 watching
 

### Forks

158

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python89.7%
* C++6.3%
* Cuda4.0%