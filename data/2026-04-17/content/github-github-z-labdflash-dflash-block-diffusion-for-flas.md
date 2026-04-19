---
title: 'GitHub - z-lab/dflash: DFlash: Block Diffusion for Flash Speculative Decoding · GitHub'
url: https://github.com/z-lab/dflash
site_name: github
content_file: github-github-z-labdflash-dflash-block-diffusion-for-flas
fetched_at: '2026-04-17T06:00:11.764596'
original_url: https://github.com/z-lab/dflash
author: z-lab
description: 'DFlash: Block Diffusion for Flash Speculative Decoding - z-lab/dflash'
---

z-lab

 

/

dflash

Public

* NotificationsYou must be signed in to change notification settings
* Fork108
* Star1.6k

 
 
 
 
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

72 Commits
72 Commits
dflash
dflash
 
 
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

# DFlash: Block Diffusion for Flash Speculative Decoding

Paper|Blog|Models

DFlashis a lightweightblock diffusionmodel designed for speculative decoding. It enables efficient and high-quality parallel drafting.

DFlash_demo.mp4

## Supported Models

Model

DFlash Draft

Kimi-K2.5 (Preview)

z-lab/Kimi-K2.5-DFlash

Qwen3.5-4B

z-lab/Qwen3.5-4B-DFlash

Qwen3.5-9B

z-lab/Qwen3.5-9B-DFlash

Qwen3.5-27B

z-lab/Qwen3.5-27B-DFlash

Qwen3.5-35B-A3B

z-lab/Qwen3.5-35B-A3B-DFlash

Qwen3-Coder-Next

z-lab/Qwen3-Coder-Next-DFlash

Qwen3-Coder-30B-A3B

z-lab/Qwen3-Coder-30B-A3B-DFlash

gpt-oss-20b

z-lab/gpt-oss-20b-DFlash

gpt-oss-120b

z-lab/gpt-oss-120b-DFlash

Qwen3-4B (non-thinking)

z-lab/Qwen3-4B-DFlash-b16

Qwen3-8B (non-thinking)

z-lab/Qwen3-8B-DFlash-b16

Llama-3.1-8B-Instruct

z-lab/LLaMA3.1-8B-Instruct-DFlash-UltraChat

Qwen3.5-122B-A10B

Coming soon

Qwen3.5-397B-A17B

Coming soon

GLM-5.1

Coming soon

Feel free to open a GitHub issue to request support for additional models. We will also open-source the training recipe soon, so you can train your own DFlash draft model to accelerate any LLM.

## 📦 Installation

Use a separate virtual environment for each to avoid conflict.

Backend

Install command

Transformers

uv pip install -e ".[transformers]"

SGLang

uv pip install -e ".[sglang]"

vLLM

See below

MLX
 (Apple Silicon)

pip install -e ".[mlx]"

vLLM:DFlash support requires the nightly build:

uv pip install -e 
"
.[vllm]
"

uv pip install -U vllm --torch-backend=auto --extra-index-url https://wheels.vllm.ai/nightly

## 🚀 Quick Start

### vLLM

vllm serve Qwen/Qwen3.5-27B \
 --speculative-config 
'
{"method": "dflash", "model": "z-lab/Qwen3.5-27B-DFlash", "num_speculative_tokens": 15}
'
 \
 --attention-backend flash_attn \
 --max-num-batched-tokens 32768

### SGLang

export
 SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1

#
 Optional: enable schedule overlapping (experimental, may not be stable)

#
 export SGLANG_ENABLE_SPEC_V2=1

#
 export SGLANG_ENABLE_DFLASH_SPEC_V2=1

#
 export SGLANG_ENABLE_OVERLAP_PLAN_STREAM=1

python -m sglang.launch_server \
 --model-path Qwen/Qwen3.5-35B-A3B \
 --speculative-algorithm DFLASH \
 --speculative-draft-model-path z-lab/Qwen3.5-35B-A3B-DFlash \
 --speculative-num-draft-tokens 16 \
 --tp-size 1 \
 --attention-backend trtllm_mha \
 --speculative-draft-attention-backend fa4 \
 --mem-fraction-static 0.75 \
 --mamba-scheduler-strategy extra_buffer \
 --trust-remote-code

### Transformers

Only Qwen3 and LLaMA-3.1 models support the Transformers backend.

from
 
transformers
 
import
 
AutoModel
, 
AutoModelForCausalLM
, 
AutoTokenizer

draft
 
=
 
AutoModel
.
from_pretrained
(
"z-lab/Qwen3-8B-DFlash-b16"
, 
trust_remote_code
=
True
, 
dtype
=
"auto"
, 
device_map
=
"cuda:0"
).
eval
()

target
 
=
 
AutoModelForCausalLM
.
from_pretrained
(
"Qwen/Qwen3-8B"
, 
dtype
=
"auto"
, 
device_map
=
"cuda:0"
).
eval
()

tokenizer
 
=
 
AutoTokenizer
.
from_pretrained
(
"Qwen/Qwen3-8B"
)

messages
 
=
 [{
"role"
: 
"user"
, 
"content"
: 
"How many positive whole-number divisors does 196 have?"
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
to
(
draft
.
device
)

output
 
=
 
draft
.
spec_generate
(
input_ids
=
input_ids
, 
max_new_tokens
=
2048
, 
temperature
=
0.0
, 
target
=
target
, 
stop_token_ids
=
[
tokenizer
.
eos_token_id
])

print
(
tokenizer
.
decode
(
output
[
0
], 
skip_special_tokens
=
False
))

### MLX (Apple Silicon)

There have been many great community DFlash implementations on MLX; we provide a simple and efficient one here, tested on an Apple M5 Pro with Qwen3 and Qwen3.5 models.

from
 
dflash
.
model_mlx
 
import
 
load
, 
load_draft
, 
stream_generate

model
, 
tokenizer
 
=
 
load
(
"Qwen/Qwen3.5-4B"
)

draft
 
=
 
load_draft
(
"z-lab/Qwen3.5-4B-DFlash"
)

messages
 
=
 [{
"role"
: 
"user"
, 
"content"
: 
"How many positive whole-number divisors does 196 have?"
}]

prompt
 
=
 
tokenizer
.
apply_chat_template
(
messages
, 
tokenize
=
False
, 
add_generation_prompt
=
True
, 
enable_thinking
=
True
)

tps
 
=
 
0.0

for
 
r
 
in
 
stream_generate
(
model
, 
draft
, 
tokenizer
, 
prompt
, 
block_size
=
16
, 
max_tokens
=
2048
, 
temperature
=
0.6
):
 
print
(
r
.
text
, 
end
=
""
, 
flush
=
True
)
 
tps
 
=
 
r
.
generation_tps

print
(
f"
\n
Throughput: 
{
tps
:.2f
}
 tok/s"
)

## 📊 Evaluation

All benchmarks share the same datasets (gsm8k, math500, humaneval, mbpp, mt-bench). Datasets are automatically downloaded and cached as JSONL incache/on first run.

vLLM:

python -m dflash.benchmark --backend vllm \
 --base-url http://127.0.0.1:8000 --model Qwen/Qwen3.5-27B \
 --dataset gsm8k --num-prompts 128 --concurrency 1 --enable-thinking

SGLang:

python -m dflash.benchmark --backend sglang \
 --base-url http://127.0.0.1:30000 --model Qwen/Qwen3.5-35B-A3B \
 --dataset gsm8k --num-prompts 128 --concurrency 1 --enable-thinking

Transformers(Qwen3 and LLaMA only):

torchrun --nproc_per_node=8 -m dflash.benchmark --backend transformers \
 --model Qwen/Qwen3-8B --draft-model z-lab/Qwen3-8B-DFlash-b16 \
 --dataset gsm8k --max-samples 128

MLX:

python -m dflash.benchmark --backend mlx \
 --model Qwen/Qwen3.5-4B --draft-model z-lab/Qwen3.5-4B-DFlash \
 --dataset gsm8k --max-samples 128 --enable-thinking

## Acknowledgement

Huge thanks to@dcw02,@gongy, and the team at@modal-labsfor their fast, high-quality support in bringing DFlash to SGLang. And huge thanks as well to@benchislettat NVIDIA for his work in bringing DFlash to vLLM and helping make it available to the broader serving community.

## Citation

If you find DFlash useful, please cite our work. To share feedback on DFlash or request new model support, please fill out this form:DFlash Feedback.

@article
{
chen2026dflash
,
 
title
 = 
{
{DFlash: Block Diffusion for Flash Speculative Decoding}
}
,
 
author
 = 
{
Chen, Jian and Liang, Yesheng and Liu, Zhijian
}
,
 
journal
 = 
{
arXiv preprint arXiv:2602.06036
}
,
 
year
 = 
{
2026
}

}

## About

DFlash: Block Diffusion for Flash Speculative Decoding

dflash.z-lab.ai

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

1.6k

 stars
 

### Watchers

22

 watching
 

### Forks

108

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