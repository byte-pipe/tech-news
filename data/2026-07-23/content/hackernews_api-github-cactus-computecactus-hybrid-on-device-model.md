---
title: 'GitHub - cactus-compute/cactus-hybrid: On-device models that know when they''re wrong: every answer carries a confidence score for cloud handoff. · GitHub'
url: https://github.com/cactus-compute/cactus-hybrid
site_name: hackernews_api
content_file: hackernews_api-github-cactus-computecactus-hybrid-on-device-model
fetched_at: '2026-07-23T19:33:24.484416'
original_url: https://github.com/cactus-compute/cactus-hybrid
author: HenryNdubuaku
date: '2026-07-22'
description: 'On-device models that know when they''re wrong: every answer carries a confidence score for cloud handoff. - cactus-compute/cactus-hybrid'
tags:
- hackernews
- trending
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 cactus-compute

 

/

cactus-hybrid

Public

* NotificationsYou must be signed in to change notification settings
* Fork3
* Star155

 
 
 
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

9 Commits
9 Commits
patches/
llama.cpp
patches/
llama.cpp
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Cactus Hybrid

A small, on-device model is fast and private, but sometimes wrong.
At Cactus we post-train models toknow when they are wrong: we ship probes
inside the checkpoint that score every answer with aconfidencebetween
0 and 1, returned as structured data (never parsed out of the answer text).
Answer on-device when confidence is high; you can re-route to a bigger
model when it's low:

if
 
confidence
 
<
 
0.85
:
 
answer
 
=
 
ask_a_bigger_model
(
prompt
)

We start the rollout withGemma 4 E2B Hybrid, all builds live in theCactus Hybrid collectionon Hugging Face.

Gemma 4 E2B hybrid, the smallest Gemma model, matches Gemini 3.1 Flash-Lite
on most benchmarks by routing only 15–35% of queries to the Gemini 3.1 Flash-Lite and
running the remnant itself.

Benchmark

Handoff to match Flash-Lite (FP16)

At 4-bit

At 3-bit

ChartQA

15–20%

25–30%

40–50%

MMBench

30–35%

40–45%

50–55%

LibriSpeech

25–30%

35–40%

55–65%

GigaSpeech

30–35%

40–45%

50–55%

MMAU

30–35%

35–40%

50–55%

MMLU-Pro

45–55%

~90%

n/a

* N/B: Quantisation quality is measured onCactus Quantswhich performs well at uniform quantization.
* Developers are encouraged to benchmark for Unsloth, GGUF, and MLX quantization independently.

## Cactus

# pip install cactus-compute

import
 
json

from
 
cactus
.
bindings
.
cactus
 
import
 
cactus_complete
, 
cactus_init

from
 
cactus
.
cli
.
download
 
import
 
download_bundle

lm
 
=
 
cactus_init
(
str
(
download_bundle
(
"Cactus-Compute/gemma-4-E2B-it"
)))

result
 
=
 
cactus_complete
(
 
lm
,
 [{
"role"
: 
"user"
, 
"content"
: 
"What is the capital of France?"
}],
 
json
.
dumps
({
"max_tokens"
: 
512
, 
"auto_handoff"
: 
False
}),
 
None
,
 
lambda
 
*
_
: 
None
,
)

print
(
result
[
"response"
].
strip
())

print
(
"confidence:"
, 
result
[
"confidence"
])

## MLX

# pip install mlx-lm

import
 
re

from
 
mlx_lm
 
import
 
load
, 
generate

model
, 
tokenizer
 
=
 
load
(
 
"Cactus-Compute/gemma-4-e2b-it-hybrid-mlx"
,
 
tokenizer_config
=
{
"trust_remote_code"
: 
True
},
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
"What is the capital of France?"
}]

answer
 
=
 
generate
(
 
model
,
 
tokenizer
,
 
prompt
=
tokenizer
.
apply_chat_template
(
messages
, 
add_generation_prompt
=
True
),
 
max_tokens
=
512
,
)

# the checkpoint reasons before answering; keep only the final answer

answer
 
=
 
re
.
split
(
r"<\|?channel\|?>"
, 
answer
)[
-
1
]

answer
 
=
 
re
.
sub
(
r"^(thought|final)\b\s*"
, 
""
, 
answer
).
strip
()

print
(
answer
)

print
(
"confidence:"
, 
model
.
last_confidence
)

## Transformers

# pip install "transformers>=5.5.4,<5.6" torch (5.14+ segfaults on this checkpoint)

import
 
torch

from
 
transformers
 
import
 
AutoModelForCausalLM
, 
AutoTokenizer

model_id
 
=
 
"Cactus-Compute/gemma-4-e2b-it-hybrid"

device
 
=
 
"cuda"
 
if
 
torch
.
cuda
.
is_available
() 
else
 
"mps"
 
if
 
torch
.
backends
.
mps
.
is_available
() 
else
 
"cpu"

tokenizer
 
=
 
AutoTokenizer
.
from_pretrained
(
model_id
, 
trust_remote_code
=
True
)

model
 
=
 
AutoModelForCausalLM
.
from_pretrained
(
model_id
, 
trust_remote_code
=
True
, 
dtype
=
"auto"
).
to
(
device
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
"What is the capital of France?"
}]

inputs
 
=
 
tokenizer
.
apply_chat_template
(
 
messages
, 
add_generation_prompt
=
True
, 
return_tensors
=
"pt"
, 
return_dict
=
True

).
to
(
device
)

out
 
=
 
model
.
generate
(
**
inputs
, 
return_confidence
=
True
, 
max_new_tokens
=
512
)

print
(
tokenizer
.
decode
(
out
.
sequences
[
0
][
inputs
[
"input_ids"
].
shape
[
-
1
]:], 
skip_special_tokens
=
True
))

print
(
"confidence:"
, 
out
.
confidence
)

Load the model with an explicit.to(device), notdevice_map="auto": the
probe scores generations outside the moduleforward()path, so weights that
accelerate offloads (left on themetadevice) crash the confidence read.

## llama.cpp

llama.cpp is C++, so the probe is a patch you compile into the engine (seepatches/llama.cpp/). Build the patched server once:

git clone https://github.com/cactus-compute/cactus-hybrid 
&&
 
cd
 cactus-hybrid
./patches/llama.cpp/install.sh 
&&
 rehash

Then serve and query it like any llama-server — the response carries a
top-levelconfidencefield:

llama-server -hf Cactus-Compute/gemma-4-e2b-it-hybrid-GGUF:Q4_K_M --jinja

curl -s http://localhost:8080/v1/chat/completions \
 -d 
'
{"messages":[{"role":"user","content":"What is the capital of France?"}],"max_tokens":512}
'
 \
 
|
 jq 
'
{answer: .choices[0].message.content, confidence}
'

## Routing Quality (AUROC)

Gemma 4 E2B HybridAUROC measures how well the the separates wrong answers from right ones
(higher = better, 0.5 is random, 1.0 is perfect):

Hold-out

Modality

Cactus Hybrid

Token Entropy

MMLU

text MCQ

0.770

0.697

MMLU-Pro

text MCQ

0.771

0.692

ARC-Easy

text MCQ

0.888

0.655

ARC-Challenge

text MCQ

0.834

0.646

GSM8K (3-shot)

text gen

0.782

0.731

MMBench-EN-Dev

vision MCQ

0.840

0.435

ChartQA

vision QA

0.779

0.615

DocVQA

vision QA

0.781

0.512

MMAU

audio MCQ

0.789

0.517

GigaSpeech

audio

0.876

0.343

Earnings-22

audio

0.839

0.323

LibriSpeech

audio

0.822

0.427

Mean

0.814

0.549

The strongest result: the probe was trained onzero audio data, yet achieves
0.79–0.88 AUROC on four audio benchmarks (two transcription, one audio MCQ, one
out-of-domain transcription).

This rules out surface-level explanations, the probe
is reading a modality-independent correctness signal from the hidden state, not
memorizing patterns from training data.

MIT-licensed. Gemma model use is subject to the Gemma terms.

## About

On-device models that know when they're wrong: every answer carries a confidence score for cloud handoff.

huggingface.co/collections/Cactus-Compute/cactus-hybrid-6a60da4551074db058e8bb64

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

155

 stars
 

### Watchers

0

 watching
 

### Forks

3

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

* Shell100.0%