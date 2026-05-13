---
title: 'GitHub - cactus-compute/needle: 26m function call model that runs on incredibly small devices · GitHub'
url: https://github.com/cactus-compute/needle
site_name: hackernews_api
content_file: hackernews_api-github-cactus-computeneedle-26m-function-call-mode
fetched_at: '2026-05-13T11:46:11.665662'
original_url: https://github.com/cactus-compute/needle
author: HenryNdubuaku
date: '2026-05-12'
description: 26m function call model that runs on incredibly small devices - cactus-compute/needle
tags:
- hackernews
- trending
---

cactus-compute

 

/

needle

Public

* NotificationsYou must be signed in to change notification settings
* Fork37
* Star924

 
 
 
 
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

232 Commits
232 Commits
assets
assets
 
 
docs
docs
 
 
needle
needle
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
launch_train.sh
launch_train.sh
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
setup
setup
 
 
View all files

## Repository files navigation

# Needle

We distilled Gemini 3.1 into a 26m parameter "Simple Attention Network" that you can even finetune locally on your Mac/PC.
In production, Needle runs onCactusat 6000 toks/sec prefill and 1200 decode speed.
Weights are fully open onCactus-Compute/needle, as well as the dataset generation.

d=512, 8H/4KV, BPE=8192
 ┌──────────────┐
 │ Tool Call │
 └──────┬───────┘
 ┌┴──────────┐
 │ Softmax │
 └─────┬─────┘
 ┌─────┴─────┐
 │ Linear (T)│ ← tied
 └─────┬─────┘
 ┌─────┴─────┐
 │ ZCRMSNorm │
 └─────┬─────┘
 ┌────────┴────────┐
 │ Decoder x 8 │
 │┌───────────────┐│
 ││ ZCRMSNorm ││
 ││ Masked Self ││
 ││ Attn + RoPE ││
 ││ Gated Residual││
 │├───────────────┤│
 ┌──────────────┐ ││ ZCRMSNorm ││
 │ Encoder x 12 │──────────────────────▶Cross Attn ││
 │ │ ││ Gated Residual││
 │ ┌──────────┐ │ │└───────────────┘│
 │ │ZCRMSNorm │ │ └────────┬────────┘
 │ │Self Attn │ │ ┌─────┴─────┐
 │ │ GQA+RoPE │ │ │ Embedding │ ← shared
 │ │Gated Res │ │ └─────┬─────┘
 │ │ │ │ ┌───────┴───────-┐
 │ │ (no FFN) │ │ │[EOS]<tool_call>│
 │ └──────────┘ │ │ + answer │
 │ │ └───────────────-┘
 └──────┬───────┘
 │
 ┌────┴──────┐
 │ Embedding │
 └────┬──────┘
 │
 ┌────┴──────┐
 │ Text │
 │ query │
 └───────────┘

* Pretrained on 16 TPU v6e for 200B tokens (27hrs).
* Post-trained on 2B tokens of single-shot function call dataset (45mins).

Needle is an experimental run for Simple Attention Networks, geared at redefining tiny AI for consumer devies (phones, watches, glasses...).
So while it beats FunctionGemma-270m, Qwen-0.6B, Graninte-350m, LFM2.5-350m on single-shot function call for personal AI,
Those model are have more scope/capacity and excel in conversational settings. Also, small models can be finicky.
Please use the UI in the next section to test on your own tools, and finetune accordingly, at the click of a button.

## Quickstart

git clone https://github.com/cactus-compute/needle.git

cd
 needle 
&&
 
source
 ./setup
needle playground

Opens a web UI athttp://127.0.0.1:7860where you can test and finetune on your own tools. Weights are auto-downloaded.

## Usage (Python)

from
 
needle
 
import
 
SimpleAttentionNetwork
, 
load_checkpoint
, 
generate
, 
get_tokenizer

params
, 
config
 
=
 
load_checkpoint
(
"checkpoints/needle.pkl"
)

model
 
=
 
SimpleAttentionNetwork
(
config
)

tokenizer
 
=
 
get_tokenizer
()

result
 
=
 
generate
(
 
model
, 
params
, 
tokenizer
,
 
query
=
"What's the weather in San Francisco?"
,
 
tools
=
'[{"name":"get_weather","parameters":{"location":"string"}}]'
,
 
stream
=
False
,
)

print
(
result
)

# [{"name":"get_weather","arguments":{"location":"San Francisco"}}]

## Finetuning

#
 Playground (generates data via Gemini, trains, evaluates, bundles result)

needle playground

#
 CLI (auto-downloads weights if not local)

needle finetune data.jsonl

## CLI

needle playground Test and finetune via web UI
needle finetune <data.jsonl> Finetune on your own data
needle run --query "..." --tools Single inference
needle train Full training run
needle pretrain Pretrain on PleIAs/SYNTH
needle eval --checkpoint <path> Evaluate a checkpoint
needle tokenize Tokenize dataset
needle generate-data Synthesize training data via Gemini
needle tpu <action> TPU management (see docs/tpu.md)

@misc{ndubuaku2026needle,
 title={Needle},
 author={Henry Ndubuaku, Jakub Mroz, Karen Mosoyan, Roman Shemet, Parkirat Sandhu, Satyajit Kumar, Noah Cylich, Justin H. Lee},
 year={2026},
 url={https://github.com/cactus-compute/needle}
}

## About

26m function call model that runs on incredibly small devices

cactuscompute.com

### Topics

 gemini

 cactus

 gemma

 on-device-ai

 llm

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

924

 stars
 

### Watchers

5

 watching
 

### Forks

37

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

* Python92.7%
* CSS2.5%
* JavaScript2.3%
* Shell1.3%
* HTML1.2%