---
title: 'GitHub - Blaizzy/mlx-vlm: MLX-VLM is a package for inference and fine-tuning of Vision Language Models (VLMs) on your Mac using MLX. · GitHub'
url: https://github.com/Blaizzy/mlx-vlm
site_name: github
content_file: github-github-blaizzymlx-vlm-mlx-vlm-is-a-package-for-inf
fetched_at: '2026-04-04T11:11:36.092916'
original_url: https://github.com/Blaizzy/mlx-vlm
author: Blaizzy
description: MLX-VLM is a package for inference and fine-tuning of Vision Language Models (VLMs) on your Mac using MLX. - Blaizzy/mlx-vlm
---

Blaizzy



/

mlx-vlm

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork369
* Star3.4k




 
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

509 Commits
509 Commits
.github
.github
 
 
computer_use
computer_use
 
 
dev
dev
 
 
docs
docs
 
 
examples
examples
 
 
mlx_vlm
mlx_vlm
 
 
.gitignore
.gitignore
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
mkdocs.yml
mkdocs.yml
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
update_changelog.py
update_changelog.py
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# MLX-VLM

MLX-VLM is a package for inference and fine-tuning of Vision Language Models (VLMs) and Omni Models (VLMs with audio and video support) on your Mac using MLX.

## Table of Contents

* Installation
* UsageCommand Line Interface (CLI)Thinking BudgetChat UI with GradioPython Script
* Command Line Interface (CLI)Thinking Budget
* Thinking Budget
* Chat UI with Gradio
* Python Script
* Activation Quantization (CUDA)
* Multi-Image Chat SupportSupported ModelsUsage Examples
* Supported Models
* Usage Examples
* Model-Specific Documentation
* TurboQuant KV Cache
* Fine-tuning

## Model-Specific Documentation

Some models have detailed documentation with prompt formats, examples, and best practices:

Model

Documentation

DeepSeek-OCR

Docs

DeepSeek-OCR-2

Docs

DOTS-OCR

Docs

DOTS-MOCR

Docs

GLM-OCR

Docs

Phi-4 Reasoning Vision

Docs

MiniCPM-o

Docs

Phi-4 Multimodal

Docs

MolmoPoint

Docs

Moondream3

Docs

Gemma 4

Docs

Falcon-OCR

Docs

Granite Vision 3.2

Docs

Granite 4.0 Vision

Docs

## Installation

The easiest way to get started is to install themlx-vlmpackage using pip:

pip install -U mlx-vlm

## Usage

### Command Line Interface (CLI)

Generate output from a model using the CLI:

#
 Text generation

mlx_vlm.generate --model mlx-community/Qwen2-VL-2B-Instruct-4bit --max-tokens 100 --prompt
"
Hello, how are you?
"

#
 Image generation

mlx_vlm.generate --model mlx-community/Qwen2-VL-2B-Instruct-4bit --max-tokens 100 --temperature 0.0 --image http://images.cocodataset.org/val2017/000000039769.jpg

#
 Audio generation (New)

mlx_vlm.generate --model mlx-community/gemma-3n-E2B-it-4bit --max-tokens 100 --prompt
"
Describe what you hear
"
 --audio /path/to/audio.wav

#
 Multi-modal generation (Image + Audio)

mlx_vlm.generate --model mlx-community/gemma-3n-E2B-it-4bit --max-tokens 100 --prompt
"
Describe what you see and hear
"
 --image /path/to/image.jpg --audio /path/to/audio.wav

#### Thinking Budget

For thinking models (e.g., Qwen3.5), you can limit the number of tokens spent in the thinking block:

mlx_vlm.generate --model mlx-community/Qwen3.5-2B-4bit \
 --thinking-budget 50 \
 --thinking-start-token
"
<think>
"
 \
 --thinking-end-token
"
</think>
"
 \
 --enable-thinking \
 --prompt
"
Solve 2+2
"

Flag

Description

--enable-thinking

Activate thinking mode in the chat template

--thinking-budget

Max tokens allowed inside the thinking block

--thinking-start-token

Token that opens a thinking block (default:
<think>
)

--thinking-end-token

Token that closes a thinking block (default:
</think>
)

When the budget is exceeded, the model is forced to emit\n</think>and transition to the answer. If--enable-thinkingis passed but the model's chat template does not support it, the budget is applied only if the model generates the start token on its own.

### Chat UI with Gradio

Launch a chat interface using Gradio:

mlx_vlm.chat_ui --model mlx-community/Qwen2-VL-2B-Instruct-4bit

### Python Script

Here's an example of how to use MLX-VLM in a Python script:

import

mlx
.
core

as

mx

from

mlx_vlm

import

load
,
generate

from

mlx_vlm
.
prompt_utils

import

apply_chat_template

from

mlx_vlm
.
utils

import

load_config

# Load the model

model_path

=

"mlx-community/Qwen2-VL-2B-Instruct-4bit"

model
,
processor

=

load
(
model_path
)

config

=

load_config
(
model_path
)

# Prepare input

image

=
 [
"http://images.cocodataset.org/val2017/000000039769.jpg"
]

# image = [Image.open("...")] can also be used with PIL.Image.Image objects

prompt

=

"Describe this image."

# Apply chat template

formatted_prompt

=

apply_chat_template
(

processor
,
config
,
prompt
,
num_images
=
len
(
image
)
)

# Generate output

output

=

generate
(
model
,
processor
,
formatted_prompt
,
image
,
verbose
=
False
)

print
(
output
)

#### Audio Example

from

mlx_vlm

import

load
,
generate

from

mlx_vlm
.
prompt_utils

import

apply_chat_template

from

mlx_vlm
.
utils

import

load_config

# Load model with audio support

model_path

=

"mlx-community/gemma-3n-E2B-it-4bit"

model
,
processor

=

load
(
model_path
)

config

=

model
.
config

# Prepare audio input

audio

=
 [
"/path/to/audio1.wav"
,
"/path/to/audio2.mp3"
]

prompt

=

"Describe what you hear in these audio files."

# Apply chat template with audio

formatted_prompt

=

apply_chat_template
(

processor
,
config
,
prompt
,
num_audios
=
len
(
audio
)
)

# Generate output with audio

output

=

generate
(
model
,
processor
,
formatted_prompt
,
audio
=
audio
,
verbose
=
False
)

print
(
output
)

#### Multi-Modal Example (Image + Audio)

from

mlx_vlm

import

load
,
generate

from

mlx_vlm
.
prompt_utils

import

apply_chat_template

from

mlx_vlm
.
utils

import

load_config

# Load multi-modal model

model_path

=

"mlx-community/gemma-3n-E2B-it-4bit"

model
,
processor

=

load
(
model_path
)

config

=

model
.
config

# Prepare inputs

image

=
 [
"/path/to/image.jpg"
]

audio

=
 [
"/path/to/audio.wav"
]

prompt

=

""

# Apply chat template

formatted_prompt

=

apply_chat_template
(

processor
,
config
,
prompt
,

num_images
=
len
(
image
),

num_audios
=
len
(
audio
)
)

# Generate output

output

=

generate
(
model
,
processor
,
formatted_prompt
,
image
,
audio
=
audio
,
verbose
=
False
)

print
(
output
)

### Server (FastAPI)

Start the server:

mlx_vlm.server --port 8080

#
 Preload a model at startup (Hugging Face repo or local path)

mlx_vlm.server --model
<
hf_repo_or_local_path
>

#
 Preload a model with adapter

mlx_vlm.server --model
<
hf_repo_or_local_path
>
 --adapter-path
<
adapter_path
>

#
 With trust remote code enabled (required for some models)

mlx_vlm.server --trust-remote-code

#### Server Options

* --model: Preload a model at server startup, accepts a Hugging Face repo ID or local path (optional, loads lazily on first request if omitted)
* --adapter-path: Path for adapter weights to use with the preloaded model
* --host: Host address (default:0.0.0.0)
* --port: Port number (default:8080)
* --trust-remote-code: Trust remote code when loading models from Hugging Face Hub

You can also set trust remote code via environment variable:

MLX_TRUST_REMOTE_CODE=true mlx_vlm.server

The server provides multiple endpoints for different use cases and supports dynamic model loading/unloading with caching (one model at a time).

#### Available Endpoints

* /modelsand/v1/models- List models available locally
* /chat/completionsand/v1/chat/completions- OpenAI-compatible chat-style interaction endpoint with support for images, audio, and text
* /responsesand/v1/responses- OpenAI-compatible responses endpoint
* /health- Check server status
* /unload- Unload current model from memory

#### Usage Examples

##### List available models

curl
"
http://localhost:8080/models
"

##### Text Input

curl -X POST
"
http://localhost:8080/chat/completions
"
 \
 -H
"
Content-Type: application/json
"
 \
 -d
'
{

 "model": "mlx-community/Qwen2-VL-2B-Instruct-4bit",

 "messages": [

 {

 "role": "user",

 "content": "Hello, how are you"

 }

 ],

 "stream": true,

 "max_tokens": 100

 }
'

##### Image Input

curl -X POST
"
http://localhost:8080/chat/completions
"
 \
 -H
"
Content-Type: application/json
"
 \
 -d
'
{

 "model": "mlx-community/Qwen2.5-VL-32B-Instruct-8bit",

 "messages":

 [

 {

 "role": "system",

 "content": "You are a helpful assistant."

 },

 {

 "role": "user",

 "content": [

 {

 "type": "text",

 "text": "This is today
'
s chart
for

energy demand

in
 California. Can you provide an analysis of the chart and comment on the implications
for

renewable energy

in
 California
?
"

 },

 {


"
type
"
:
"
input_image
"
,


"
image_url
"
:
"
/path/to/repo/examples/images/renewables_california.png
"

 }

 ]

 }

 ],


"
stream
"
: true,


"
max_tokens
"
: 1000

 }'

##### Audio Support (New)

curl -X POST
"
http://localhost:8080/generate
"
 \
 -H
"
Content-Type: application/json
"
 \
 -d
'
{

 "model": "mlx-community/gemma-3n-E2B-it-4bit",

 "messages": [

 {

 "role": "user",

 "content": [

 { "type": "text", "text": "Describe what you hear in these audio files" },

 { "type": "input_audio", "input_audio": "/path/to/audio1.wav" },

 { "type": "input_audio", "input_audio": "https://example.com/audio2.mp3" }

 ]

 }

 ],

 "stream": true,

 "max_tokens": 500

 }
'

##### Multi-Modal (Image + Audio)

curl -X POST
"
http://localhost:8080/generate
"
 \
 -H
"
Content-Type: application/json
"
 \
 -d
'
{

 "model": "mlx-community/gemma-3n-E2B-it-4bit",

 "messages": [

 {

 "role": "user",

 "content": [

 {"type": "input_image", "image_url": "/path/to/image.jpg"},

 {"type": "input_audio", "input_audio": "/path/to/audio.wav"}

 ]

 }

 ],

 "max_tokens": 100

 }
'

##### Responses Endpoint

curl -X POST
"
http://localhost:8080/responses
"
 \
 -H
"
Content-Type: application/json
"
 \
 -d
'
{

 "model": "mlx-community/Qwen2-VL-2B-Instruct-4bit",

 "messages": [

 {

 "role": "user",

 "content": [

 {"type": "input_text", "text": "What is in this image?"},

 {"type": "input_image", "image_url": "/path/to/image.jpg"}

 ]

 }

 ],

 "max_tokens": 100

 }
'

#### Request Parameters

* model: Model identifier (required)
* messages: Chat messages for chat/OpenAI endpoints
* max_tokens: Maximum tokens to generate
* temperature: Sampling temperature
* top_p: Top-p sampling parameter
* top_k: Top-k sampling cutoff
* min_p: Min-p sampling threshold
* repetition_penalty: Penalty applied to repeated tokens
* stream: Enable streaming responses

## Activation Quantization (CUDA)

When running on NVIDIA GPUs with MLX CUDA, models quantized withmxfp8ornvfp4modes require activation quantization to work properly. This convertsQuantizedLinearlayers toQQLinearlayers which quantize both weights and activations.

### Command Line

Use the-qaor--quantize-activationsflag:

mlx_vlm.generate --model /path/to/mxfp8-model --prompt
"
Describe this image
"
 --image /path/to/image.jpg -qa

### Python API

Passquantize_activations=Trueto theloadfunction:

from

mlx_vlm

import

load
,
generate

# Load with activation quantization enabled

model
,
processor

=

load
(

"path/to/mxfp8-quantized-model"
,

quantize_activations
=
True

)

# Generate as usual

output

=

generate
(
model
,
processor
,
"Describe this image"
,
image
=
[
"image.jpg"
])

### Supported Quantization Modes

* mxfp8- 8-bit MX floating point
* nvfp4- 4-bit NVIDIA floating point

Note: This feature is required for mxfp/nvfp quantized models on CUDA. On Apple Silicon (Metal), these models work without the flag.

## Multi-Image Chat Support

MLX-VLM supports analyzing multiple images simultaneously with select models. This feature enables more complex visual reasoning tasks and comprehensive analysis across multiple images in a single conversation.

### Usage Examples

#### Python Script

from

mlx_vlm

import

load
,
generate

from

mlx_vlm
.
prompt_utils

import

apply_chat_template

from

mlx_vlm
.
utils

import

load_config

model_path

=

"mlx-community/Qwen2-VL-2B-Instruct-4bit"

model
,
processor

=

load
(
model_path
)

config

=

model
.
config

images

=
 [
"path/to/image1.jpg"
,
"path/to/image2.jpg"
]

prompt

=

"Compare these two images."

formatted_prompt

=

apply_chat_template
(

processor
,
config
,
prompt
,
num_images
=
len
(
images
)
)

output

=

generate
(
model
,
processor
,
formatted_prompt
,
images
,
verbose
=
False
)

print
(
output
)

#### Command Line

mlx_vlm.generate --model mlx-community/Qwen2-VL-2B-Instruct-4bit --max-tokens 100 --prompt
"
Compare these images
"
 --image path/to/image1.jpg path/to/image2.jpg

## Video Understanding

MLX-VLM also supports video analysis such as captioning, summarization, and more, with select models.

### Supported Models

The following models support video chat:

1. Qwen2-VL
2. Qwen2.5-VL
3. Idefics3
4. LLaVA

With more coming soon.

### Usage Examples

#### Command Line

mlx_vlm.video_generate --model mlx-community/Qwen2-VL-2B-Instruct-4bit --max-tokens 100 --prompt
"
Describe this video
"
 --video path/to/video.mp4 --max-pixels 224 224 --fps 1.0

These examples demonstrate how to use multiple images with MLX-VLM for more complex visual reasoning tasks.

## TurboQuant KV Cache

TurboQuant compresses the KV cache during generation, enabling longer context lengths with less memory while maintaining quality.

### Quick Start

#
 3.5-bit KV cache quantization (3-bit keys + 4-bit values)

mlx_vlm generate \
 --model mlx-community/Qwen3.5-4B-4bit \
 --kv-bits 3.5 \
 --kv-quant-scheme turboquant \
 --prompt
"
Your long prompt here...
"

from

mlx_vlm

import

generate

result

=

generate
(

model
,
processor
,
prompt
,

kv_bits
=
3.5
,

kv_quant_scheme
=
"turboquant"
,

max_tokens
=
256
,
)

### How It Works

TurboQuant uses random rotation + codebook quantization (arXiv:2504.19874) to compress KV cache entries from 16-bit to 2-4 bits per dimension:

* Keys: ProdCodec (MSE codebook + QJL sign residual) for accurate attention scoring
* Values: MSE codebook for reconstruction quality
* Fractional bits(e.g. 3.5): uses lower bits for keys, higher for values (3-bit K + 4-bit V)

Custom Metal kernels fuse score computation and value aggregation directly on packed quantized data, avoiding full dequantization during decode.

### Performance

Tested on Qwen3.5-4B-4bit at 128k context:

Metric

Baseline

TurboQuant 3.5-bit

KV Memory

4.1 GB

0.97 GB (
76% reduction
)

Peak Memory

18.3 GB

17.3 GB (
-1.0 GB
)

At 512k+ contexts, TurboQuant's per-layer attention isfaster than FP16 SDPAdue to reduced memory bandwidth requirements.

Tested on gemma-4-31b-it at 128k context:

Metric

Baseline

TurboQuant 3.5-bit

KV Memory

13.3 GB

4.9 GB (
63% reduction
)

Peak Memory

75.2 GB

65.8 GB (
-9.4 GB
)

### Supported Bit Widths

Bits

Compression

Best For

2

~8x

Maximum compression, some quality loss

3

~5x

Good balance of quality and compression

3.5

~4.5x

Recommended default (3-bit keys + 4-bit values)

4

~4x

Best quality, moderate compression

### Compatibility

TurboQuant automatically quantizesKVCachelayers (global attention). Models withRotatingKVCache(sliding window) orArraysCache(MLA/absorbed keys) keep their native cache format for those layers since they are already memory-efficient.

# Fine-tuning

MLX-VLM supports fine-tuning models with LoRA and QLoRA.

## LoRA & QLoRA

To learn more about LoRA, please refer to theLoRA.mdfile.

## About

MLX-VLM is a package for inference and fine-tuning of Vision Language Models (VLMs) on your Mac using MLX.

### Topics

 mlx

 vision-framework

 apple-silicon

 vision-transformer

 llm

 vision-language-model

 llava

 local-ai

 idefics

 florence2

 paligemma

 pixtral

 molmo

### Resources

 Readme



### License

 MIT license


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

3.4k

 stars


### Watchers

28

 watching


### Forks

369

 forks


 Report repository



## Releases61

v0.4.3

 Latest



Apr 2, 2026



+ 60 releases

## Sponsor this project

 



 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.







Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors86

+ 72 contributors

## Languages

* Python100.0%
