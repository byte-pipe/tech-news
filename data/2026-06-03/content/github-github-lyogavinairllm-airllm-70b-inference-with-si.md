---
title: 'GitHub - lyogavin/airllm: AirLLM 70B inference with single 4GB GPU · GitHub'
url: https://github.com/lyogavin/airllm
site_name: github
content_file: github-github-lyogavinairllm-airllm-70b-inference-with-si
fetched_at: '2026-06-03T20:09:03.379829'
original_url: https://github.com/lyogavin/airllm
author: lyogavin
description: AirLLM 70B inference with single 4GB GPU. Contribute to lyogavin/airllm development by creating an account on GitHub.
---

lyogavin

 

/

airllm

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork2.1k
* Star18.8k

 
 
 
 
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

270 Commits
270 Commits
.github
.github
 
 
air_llm
air_llm
 
 
anima_100k
anima_100k
 
 
assets
assets
 
 
data
data
 
 
eval
eval
 
 
examples
examples
 
 
rlhf
rlhf
 
 
scripts
scripts
 
 
training
training
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
README_ja.md
README_ja.md
 
 
anima_logo.png
anima_logo.png
 
 
funding.json
funding.json
 
 
requirements.txt
requirements.txt
 
 
View all files

## Repository files navigation

Quickstart|Configurations|MacOS|Example notebooks|FAQ

AirLLMoptimizes inference memory usage, allowing 70B large language models to run inference on a single 4GB GPU card without quantization, distillation and pruning. And you can run405B Llama3.1on8GB vramnow.

## AI Agents Recommendation:

* Best AI Game Sprite Generator
* Best AI Facial Expression Editor

## Updates

[2024/08/20] v2.11.0: Support Qwen2.5

[2024/08/18] v2.10.1 Support CPU inference. Support non sharded models. Thanks @NavodPeiris for the great work!

[2024/07/30] Support Llama3.1405B(example notebook). Support8bit/4bit quantization.

[2024/04/20] AirLLM supports Llama3 natively already. Run Llama3 70B on 4GB single GPU.

[2023/12/25] v2.8.2: Support MacOS running 70B large language models.

[2023/12/20] v2.7: Support AirLLMMixtral.

[2023/12/20] v2.6: Added AutoModel, automatically detect model type, no need to provide model class to initialize model.

[2023/12/18] v2.5: added prefetching to overlap the model loading and compute. 10% speed improvement.

[2023/12/03] added support ofChatGLM,QWen,Baichuan,Mistral,InternLM!

[2023/12/02] added support for safetensors. Now support all top 10 models in open llm leaderboard.

[2023/12/01] airllm 2.0. Support compressions:3x run time speed up!

[2023/11/20] airllm Initial version!

## Star History

## Table of Contents

* Quick start
* Model Compression
* Configurations
* Run on MacOS
* Example notebooks
* Supported Models
* Acknowledgement
* FAQ

## Quickstart

### 1. Install package

First, install the airllm pip package.

pip install airllm

### 2. Inference

Then, initialize AirLLMLlama2, pass in the huggingface repo ID of the model being used, or the local path, and inference can be performed similar to a regular transformer model.

(You can also specify the path to save the splitted layered model throughlayer_shards_saving_pathwhen init AirLLMLlama2.

from
 
airllm
 
import
 
AutoModel

MAX_LENGTH
 
=
 
128

# could use hugging face model repo id:

model
 
=
 
AutoModel
.
from_pretrained
(
"garage-bAInd/Platypus2-70B-instruct"
)

# or use model's local path...

#model = AutoModel.from_pretrained("/home/ubuntu/.cache/huggingface/hub/models--garage-bAInd--Platypus2-70B-instruct/snapshots/b585e74bcaae02e52665d9ac6d23f4d0dbc81a0f")

input_text
 
=
 [
 
'What is the capital of United States?'
,
 
#'I like',

 ]

input_tokens
 
=
 
model
.
tokenizer
(
input_text
,
 
return_tensors
=
"pt"
, 
 
return_attention_mask
=
False
, 
 
truncation
=
True
, 
 
max_length
=
MAX_LENGTH
, 
 
padding
=
False
)
 

generation_output
 
=
 
model
.
generate
(
 
input_tokens
[
'input_ids'
].
cuda
(), 
 
max_new_tokens
=
20
,
 
use_cache
=
True
,
 
return_dict_in_generate
=
True
)

output
 
=
 
model
.
tokenizer
.
decode
(
generation_output
.
sequences
[
0
])

print
(
output
)

Note: During inference, the original model will first be decomposed and saved layer-wise. Please ensure there is sufficient disk space in the huggingface cache directory.

## Model Compression - 3x Inference Speed Up!

We just added model compression based on block-wise quantization-based model compression. Which can furtherspeed up the inference speedfor up to3x, withalmost ignorable accuracy loss!(see more performance evaluation and why we use block-wise quantization inthis paper)

#### How to enable model compression speed up:

* Step 1. make sure you havebitsandbytesinstalled bypip install -U bitsandbytes
* Step 2. make sure airllm verion later than 2.0.0:pip install -U airllm
* Step 3. when initialize the model, passing the argument compression ('4bit' or '8bit'):

model
 
=
 
AutoModel
.
from_pretrained
(
"garage-bAInd/Platypus2-70B-instruct"
,
 
compression
=
'4bit'
 
# specify '8bit' for 8-bit block-wise quantization 

 )

#### What are the differences between model compression and quantization?

Quantization normally needs to quantize both weights and activations to really speed things up. Which makes it harder to maintain accuracy and avoid the impact of outliers in all kinds of inputs.

While in our case the bottleneck is mainly at the disk loading, we only need to make the model loading size smaller. So, we get to only quantize the weights' part, which is easier to ensure the accuracy.

## Configurations

When initialize the model, we support the following configurations:

* compression: supported options: 4bit, 8bit for 4-bit or 8-bit block-wise quantization, or by default None for no compression
* profiling_mode: supported options: True to output time consumptions or by default False
* layer_shards_saving_path: optionally another path to save the splitted model
* hf_token: huggingface token can be provided here if downloading gated models like:meta-llama/Llama-2-7b-hf
* prefetching: prefetching to overlap the model loading and compute. By default, turned on. For now, only AirLLMLlama2 supports this.
* delete_original: if you don't have too much disk space, you can set delete_original to true to delete the original downloaded hugging face model, only keep the transformed one to save half of the disk space.

## MacOS

Just install airllm and run the code the same as on linux. See more inQuick Start.

* make sure you installedmlxand torch
* you probably need to install python native see morehere
* onlyApple siliconis supported

Example [python notebook] (https://github.com/lyogavin/airllm/blob/main/air_llm/examples/run_on_macos.ipynb)

## Example Python Notebook

Example colabs here:

#### example of other models (ChatGLM, QWen, Baichuan, Mistral, etc):

Details

* ChatGLM:

from
 
airllm
 
import
 
AutoModel

MAX_LENGTH
 
=
 
128

model
 
=
 
AutoModel
.
from_pretrained
(
"THUDM/chatglm3-6b-base"
)

input_text
 
=
 [
'What is the capital of China?'
,]

input_tokens
 
=
 
model
.
tokenizer
(
input_text
,
 
return_tensors
=
"pt"
, 
 
return_attention_mask
=
False
, 
 
truncation
=
True
, 
 
max_length
=
MAX_LENGTH
, 
 
padding
=
True
)

generation_output
 
=
 
model
.
generate
(
 
input_tokens
[
'input_ids'
].
cuda
(), 
 
max_new_tokens
=
5
,
 
use_cache
=
 
True
,
 
return_dict_in_generate
=
True
)

model
.
tokenizer
.
decode
(
generation_output
.
sequences
[
0
])

* QWen:

from
 
airllm
 
import
 
AutoModel

MAX_LENGTH
 
=
 
128

model
 
=
 
AutoModel
.
from_pretrained
(
"Qwen/Qwen-7B"
)

input_text
 
=
 [
'What is the capital of China?'
,]

input_tokens
 
=
 
model
.
tokenizer
(
input_text
,
 
return_tensors
=
"pt"
, 
 
return_attention_mask
=
False
, 
 
truncation
=
True
, 
 
max_length
=
MAX_LENGTH
)

generation_output
 
=
 
model
.
generate
(
 
input_tokens
[
'input_ids'
].
cuda
(), 
 
max_new_tokens
=
5
,
 
use_cache
=
True
,
 
return_dict_in_generate
=
True
)

model
.
tokenizer
.
decode
(
generation_output
.
sequences
[
0
])

* Baichuan, InternLM, Mistral, etc:

from
 
airllm
 
import
 
AutoModel

MAX_LENGTH
 
=
 
128

model
 
=
 
AutoModel
.
from_pretrained
(
"baichuan-inc/Baichuan2-7B-Base"
)

#model = AutoModel.from_pretrained("internlm/internlm-20b")

#model = AutoModel.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")

input_text
 
=
 [
'What is the capital of China?'
,]

input_tokens
 
=
 
model
.
tokenizer
(
input_text
,
 
return_tensors
=
"pt"
, 
 
return_attention_mask
=
False
, 
 
truncation
=
True
, 
 
max_length
=
MAX_LENGTH
)

generation_output
 
=
 
model
.
generate
(
 
input_tokens
[
'input_ids'
].
cuda
(), 
 
max_new_tokens
=
5
,
 
use_cache
=
True
,
 
return_dict_in_generate
=
True
)

model
.
tokenizer
.
decode
(
generation_output
.
sequences
[
0
])

#### To request other model support:here

## Acknowledgement

A lot of the code are based on SimJeg's great work in the Kaggle exam competition. Big shoutout to SimJeg:

GitHub account @SimJeg,the code on Kaggle,the associated discussion.

## FAQ

### 1. MetadataIncompleteBuffer

safetensors_rust.SafetensorError: Error while deserializing header: MetadataIncompleteBuffer

If you run into this error, most possible cause is you run out of disk space. The process of splitting model is very disk-consuming. Seethis. You may need to extend your disk space, clear huggingface.cacheand rerun.

### 2. ValueError: max() arg is an empty sequence

Most likely you are loading QWen or ChatGLM model with Llama2 class. Try the following:

For QWen model:

from
 
airllm
 
import
 
AutoModel
 
#<----- instead of AirLLMLlama2

AutoModel
.
from_pretrained
(...)

For ChatGLM model:

from
 
airllm
 
import
 
AutoModel
 
#<----- instead of AirLLMLlama2

AutoModel
.
from_pretrained
(...)

### 3. 401 Client Error....Repo model ... is gated.

Some models are gated models, needs huggingface api token. You can provide hf_token:

model
 
=
 
AutoModel
.
from_pretrained
(
"meta-llama/Llama-2-7b-hf"
, 
#hf_token='HF_API_TOKEN')

### 4. ValueError: Asking to pad but the tokenizer does not have a padding token.

Some model's tokenizer doesn't have padding token, so you can set a padding token or simply turn the padding config off:

input_tokens
 
=
 
model
.
tokenizer
(
input_text
,
 
return_tensors
=
"pt"
, 
 
return_attention_mask
=
False
, 
 
truncation
=
True
, 
 
max_length
=
MAX_LENGTH
, 
 
padding
=
False
 
#<----------- turn off padding 

)

## Citing AirLLM

If you find
AirLLM useful in your research and wish to cite it, please use the following
BibTex entry:

@software{airllm2023,
 author = {Gavin Li},
 title = {AirLLM: scaling large language models on low-end commodity computers},
 url = {https://github.com/lyogavin/airllm/},
 version = {0.0},
 year = {2023},
}

## Contribution

Welcomed contributions, ideas and discussions!

If you find it useful, please ⭐ or buy me a coffee! 🙏

## About

AirLLM 70B inference with single 4GB GPU

### Topics

 open-source

 chinese-nlp

 llama

 lora

 instruction-set

 finetune

 open-source-models

 open-models

 llm

 generative-ai

 instruct-gpt

 qlora

 chinese-llm

### Resources

 Readme

 

### License

 Apache-2.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

18.8k

 stars
 

### Watchers

214

 watching
 

### Forks

2.1k

 forks
 

 Report repository

 

## Releases

No releases published

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* buymeacoffee.com/lyogavinq

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Jupyter Notebook96.2%
* Python3.7%
* Shell0.1%