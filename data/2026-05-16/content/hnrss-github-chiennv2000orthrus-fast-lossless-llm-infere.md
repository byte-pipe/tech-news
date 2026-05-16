---
title: 'GitHub - chiennv2000/orthrus: Fast, lossless LLM inference via dual-view diffusion decoding. · GitHub'
url: https://github.com/chiennv2000/orthrus
site_name: hnrss
content_file: hnrss-github-chiennv2000orthrus-fast-lossless-llm-infere
fetched_at: '2026-05-16T19:28:06.603330'
original_url: https://github.com/chiennv2000/orthrus
date: '2026-05-15'
description: Fast, lossless LLM inference via dual-view diffusion decoding. - chiennv2000/orthrus
tags:
- hackernews
- hnrss
---

chiennv2000

 

/

orthrus

Public

* NotificationsYou must be signed in to change notification settings
* Fork4
* Star198

 
 
 
 
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

11 Commits
11 Commits
assets
assets
 
 
src
src
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion

Official implementation and model checkpoints forOrthrus, a dual-architecture framework that unifies the exact generation fidelity of autoregressive Large Language Models (LLMs) with the high-speed parallel token generation of diffusion models.

demo_orthrus.mp4

## Model Zoo

All models use a Qwen3 backbone and guaranteestrictly lossless generation.

Model

Base Model

HuggingFace

Avg. Speedup

Orthrus-Qwen3-1.7B

Qwen3-1.7B

🤗 HuggingFace

4.25×

Orthrus-Qwen3-4B

Qwen3-4.0B

🤗 HuggingFace

5.20×

Orthrus-Qwen3-8B

Qwen3-8.0B

🤗 HuggingFace

5.36×

## Installation

uv pip install -e 
.

uv pip install ninja packaging
uv pip install flash-attn --no-build-isolation 
#
 or: pip install "flash-attn-4[cu13]" if your device supports it

We recommenduvfor fast dependency resolution.

## Quickstart

import
 
torch

from
 
transformers
 
import
 
AutoModelForCausalLM
, 
AutoTokenizer
, 
TextStreamer

 

model
 
=
 
AutoModelForCausalLM
.
from_pretrained
(
 
"chiennv/Orthrus-Qwen3-8B"
,
 
dtype
=
torch
.
bfloat16
, 
device_map
=
"cuda"
,
 
attn_implementation
=
"flash_attention_2"
, 
# use flash_attention_4 if your system does support

 
trust_remote_code
=
True
,
).
eval
()

tokenizer
 
=
 
AutoTokenizer
.
from_pretrained
(
"chiennv/Orthrus-Qwen3-8B"
)
 

prompt
 
=
 
"Write a program to count the frequency of each word in a paragraph."

messages
 
=
 [{
"role"
: 
"system"
, 
"content"
: 
""
}, {
"role"
: 
"user"
, 
"content"
: 
prompt
}]

input_ids
 
=
 
tokenizer
.
apply_chat_template
(
messages
, 
return_tensors
=
"pt"
, 
add_generation_prompt
=
True
, 
enable_thinking
=
False
).
input_ids

output_ids
 
=
 
model
.
generate
(
 
input_ids
=
input_ids
.
to
(
model
.
device
), 
 
max_new_tokens
=
2048
,
 
use_diffusion_mode
=
True
, 
 
streamer
=
TextStreamer
(
tokenizer
, 
skip_prompt
=
True
) 
# enable streaming generation

)

Coming soon:Native integration withvLLMandSGLangis coming soon. Stay tuned!

## Key Advantages

* Significant Inference Acceleration:Breaks the sequential bottleneck of standard autoregressive decoding, delivering up to a$7.8\times$speedup on generation tasks.
* Strictly Lossless Generation:Employs an exact intra-model consensus mechanism to guarantee that the output matches the original base model's exact predictive distribution.
* Zero Redundant Memory Overhead:Both the autoregressive and diffusion views attend to the exact same high-fidelity Key-Value (KV) cache natively, resulting in only an$O(1)$memory cache overhead.
* Parameter Efficient:Parallel generation capabilities are injected by fine-tuning only 16% of the total model parameters while keeping the base LLM strictly frozen.

## Performance Comparison: Orthrus vs. Speculative Decoding

Orthrus outperforms speculative decoding methods like EAGLE-3, DFlash. By natively sharing the exact same KV cache across dual views, Orthrus avoids the redundant memory overhead of draft models, resulting in significantly higher token acceptance rates and faster inference times, especially as context length scales.

Left:Average verified tokens per forward pass compared to EAGLE-3 and DFlash.Right:Simulated generation time across scaling context lengths compared to DFlash.

## Comparison with State-of-the-Art Diffusion Models

While recent diffusion language models (dLLMs) offer parallel decoding, they often suffer from significant conditional drift and severe accuracy degradation on complex reasoning tasks. Orthrus resolves this by decoupling parallel generation from sequential constraints, establishing a new state-of-the-art for parallel generation fidelity.

Throughput vs. Accuracy on MATH-500.Orthrus delivers a ~6x speedup over the Qwen3-8B baseline with strictly lossless performance, whereas adaptations like Fast-dLLM-v2 suffer significant accuracy drops.

## Citation

If you find this model or architecture useful in your work, please cite ourpaper:

@misc
{
vannguyen2026orthrusmemoryefficientparalleltoken
,
 
title
=
{
Orthrus: Memory-Efficient Parallel Token Generation via Dual-View Diffusion
}
, 
 
author
=
{
Chien Van Nguyen and Chaitra Hegde and Van Cuong Pham and Ryan A. Rossi and Franck Dernoncourt and Thien Huu Nguyen
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
2605.12825
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
cs.LG
}
,
 
url
=
{
https://arxiv.org/abs/2605.12825
}
, 
}

## About

Fast, lossless LLM inference via dual-view diffusion decoding.

### Topics

 natural-language-processing

 model-architecture

 efficient-inference

 large-language-models

 llm

 diffusion-language-models

 llm-efficiency

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

198

 stars
 

### Watchers

6

 watching
 

### Forks

4

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%