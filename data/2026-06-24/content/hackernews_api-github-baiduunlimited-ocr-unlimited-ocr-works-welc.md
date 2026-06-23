---
title: 'GitHub - baidu/Unlimited-OCR: Unlimited OCR Works: Welcome the Era of One-shot Long-horizon Parsing. · GitHub'
url: https://github.com/baidu/Unlimited-OCR
site_name: hackernews_api
content_file: hackernews_api-github-baiduunlimited-ocr-unlimited-ocr-works-welc
fetched_at: '2026-06-24T01:01:40.586660'
original_url: https://github.com/baidu/Unlimited-OCR
author: ingve
date: '2026-06-23'
description: 'Unlimited OCR Works: Welcome the Era of One-shot Long-horizon Parsing. - baidu/Unlimited-OCR'
tags:
- hackernews
- trending
---

baidu

 

/

Unlimited-OCR

Public

* NotificationsYou must be signed in to change notification settings
* Fork139
* Star2.3k

 
 
 
 
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

4 Commits
4 Commits
assets
assets
 
 
wheel
wheel
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
Unlimited-OCR.pdf
Unlimited-OCR.pdf
 
 
infer.py
infer.py
 
 
View all files

## Repository files navigation

# Unlimited OCR Works

### Welcome the Era of One-shot Long-horizon Parsing.

## Release

* [2026/06/23] 📄 Our paper is now available onarXiv.
* [2026/06/23] 🤝 Thanks to the ModelScope community for their support. Our model is now available atModelScope.
* [2026/06/22] 🚀 We presentUnlimited-OCR, aiming to pushDeepseek-OCRone step further.

## Inference

### Transformers

Inference using Huggingface transformers on NVIDIA GPUs. Requirements tested on python 3.12.3 + CUDA12.9：

torch==2.10.0
torchvision==0.25.0
transformers==4.57.1
Pillow==12.1.1
matplotlib==3.10.8
einops==0.8.2
addict==2.4.0
easydict==1.13
pymupdf==1.27.2.2
psutil==7.2.2

import
 
os

import
 
torch

from
 
transformers
 
import
 
AutoModel
, 
AutoTokenizer

model_name
 
=
 
'baidu/Unlimited-OCR'

tokenizer
 
=
 
AutoTokenizer
.
from_pretrained
(
model_name
, 
trust_remote_code
=
True
)

model
 
=
 
AutoModel
.
from_pretrained
(
 
model_name
,
 
trust_remote_code
=
True
,
 
use_safetensors
=
True
,
 
torch_dtype
=
torch
.
bfloat16
,
)

model
 
=
 
model
.
eval
().
cuda
()

# ── Single image supports two configs: gundam or base ──

# gundam: base_size=1024, image_size=640, crop_mode=True

# base: base_size=1024, image_size=1024, crop_mode=False

model
.
infer
(
 
tokenizer
,
 
prompt
=
'<image>document parsing.'
,
 
image_file
=
'your_image.jpg'
,
 
output_path
=
'your/output/dir'
,
 
base_size
=
1024
, 
image_size
=
640
, 
crop_mode
=
True
,
 
max_length
=
32768
,
 
no_repeat_ngram_size
=
35
, 
ngram_window
=
128
,
 
save_results
=
True
,
)

# ── Multi page / PDF only uses base (image_size=1024) ──

model
.
infer_multi
(
 
tokenizer
,
 
prompt
=
'<image>Multi page parsing.'
,
 
image_files
=
[
'page1.png'
, 
'page2.png'
, 
'page3.png'
],
 
output_path
=
'your/output/dir'
,
 
image_size
=
1024
,
 
max_length
=
32768
,
 
no_repeat_ngram_size
=
35
, 
ngram_window
=
1024
,
 
save_results
=
True
,
)

# ── PDF (convert pages to images, then multi-page parsing) ──

import
 
tempfile
, 
fitz
 
# PyMuPDF

def
 
pdf_to_images
(
pdf_path
, 
dpi
=
300
):
 
doc
 
=
 
fitz
.
open
(
pdf_path
)
 
tmp_dir
 
=
 
tempfile
.
mkdtemp
(
prefix
=
'pdf_ocr_'
)
 
mat
 
=
 
fitz
.
Matrix
(
dpi
 
/
 
72
, 
dpi
 
/
 
72
)
 
paths
 
=
 []
 
for
 
i
, 
page
 
in
 
enumerate
(
doc
):
 
out
 
=
 
os
.
path
.
join
(
tmp_dir
, 
f'page_
{
i
+
1
:04d
}
.png'
)
 
page
.
get_pixmap
(
matrix
=
mat
).
save
(
out
)
 
paths
.
append
(
out
)
 
doc
.
close
()
 
return
 
paths

model
.
infer_multi
(
 
tokenizer
,
 
prompt
=
'<image>Multi page parsing.'
,
 
image_files
=
pdf_to_images
(
'your_doc.pdf'
, 
dpi
=
300
),
 
output_path
=
'your/output/dir'
,
 
image_size
=
1024
,
 
max_length
=
32768
,
 
no_repeat_ngram_size
=
35
, 
ngram_window
=
1024
,
 
save_results
=
True
,
)

### SGLang

Set up the environment (uv-managed virtualenv). Install the local SGLang wheel first,
then pinkernels==0.9.0and install PyMuPDF for PDF-to-image conversion:

uv venv --python 3.12

source
 .venv/bin/activate

uv pip install wheel/sglang-0.0.0.dev11416+g92e8bb79e-py3-none-any.whl
uv pip install kernels==0.11.7
uv pip install pymupdf==1.27.2.2

Start the SGLang server:

python -m sglang.launch_server \
 --model baidu/Unlimited-OCR \
 --served-model-name Unlimited-OCR \
 --attention-backend fa3 \
 --page-size 1 \
 --mem-fraction-static 0.8 \
 --context-length 32768 \
 --enable-custom-logit-processor \
 --disable-overlap-schedule \
 --skip-server-warmup \
 --host 0.0.0.0 \
 --port 10000

Send streaming requests to the OpenAI-compatible API:

import
 
base64

import
 
json

import
 
os

import
 
tempfile

import
 
fitz

import
 
requests

from
 
sglang
.
srt
.
sampling
.
custom_logit_processor
 
import
 
DeepseekOCRNoRepeatNGramLogitProcessor

server_url
 
=
 
"http://127.0.0.1:10000"

session
 
=
 
requests
.
Session
()

session
.
trust_env
 
=
 
False

def
 
pdf_to_images
(
pdf_path
, 
dpi
=
300
):
 
doc
 
=
 
fitz
.
open
(
pdf_path
)
 
tmp_dir
 
=
 
tempfile
.
mkdtemp
(
prefix
=
"pdf_ocr_"
)
 
mat
 
=
 
fitz
.
Matrix
(
dpi
 
/
 
72
, 
dpi
 
/
 
72
)
 
image_paths
 
=
 []
 
for
 
i
, 
page
 
in
 
enumerate
(
doc
):
 
image_path
 
=
 
os
.
path
.
join
(
tmp_dir
, 
f"page_
{
i
 
+
 
1
:04d
}
.png"
)
 
page
.
get_pixmap
(
matrix
=
mat
).
save
(
image_path
)
 
image_paths
.
append
(
image_path
)
 
doc
.
close
()
 
return
 
image_paths

def
 
encode_image
(
image_path
):
 
ext
 
=
 
os
.
path
.
splitext
(
image_path
)[
1
].
lower
()
 
mime
 
=
 
"image/jpeg"
 
if
 
ext
 
in
 (
".jpg"
, 
".jpeg"
) 
else
 
f"image/
{
ext
.
lstrip
(
'.'
)
}
"

 
with
 
open
(
image_path
, 
"rb"
) 
as
 
f
:
 
data
 
=
 
base64
.
b64encode
(
f
.
read
()).
decode
(
"utf-8"
)
 
return
 {
"type"
: 
"image_url"
, 
"image_url"
: {
"url"
: 
f"data:
{
mime
}
;base64,
{
data
}
"
}}

def
 
build_content
(
prompt
, 
image_paths
):
 
return
 [{
"type"
: 
"text"
, 
"text"
: 
prompt
}] 
+
 [
encode_image
(
path
) 
for
 
path
 
in
 
image_paths
]

def
 
generate
(
prompt
, 
image_paths
, 
image_mode
, 
ngram_window
):
 
payload
 
=
 {
 
"model"
: 
"Unlimited-OCR"
,
 
"messages"
: [{
"role"
: 
"user"
, 
"content"
: 
build_content
(
prompt
, 
image_paths
)}],
 
"temperature"
: 
0
,
 
"skip_special_tokens"
: 
False
,
 
"images_config"
: {
"image_mode"
: 
image_mode
},
 
"custom_logit_processor"
: 
DeepseekOCRNoRepeatNGramLogitProcessor
.
to_str
(),
 
"custom_params"
: {
 
"ngram_size"
: 
35
,
 
"window_size"
: 
ngram_window
,
 },
 
"stream"
: 
True
,
 }
 
response
 
=
 
session
.
post
(
 
f"
{
server_url
}
/v1/chat/completions"
,
 
headers
=
{
"Content-Type"
: 
"application/json"
},
 
data
=
json
.
dumps
(
payload
),
 
timeout
=
1200
,
 
stream
=
True
,
 )
 
response
.
raise_for_status
()

 
chunks
 
=
 []
 
for
 
line
 
in
 
response
.
iter_lines
(
chunk_size
=
1
, 
decode_unicode
=
True
):
 
if
 
not
 
line
 
or
 
not
 
line
.
startswith
(
"data: "
):
 
continue

 
data
 
=
 
line
[
len
(
"data: "
):]
 
if
 
data
 
==
 
"[DONE]"
:
 
break

 
event
 
=
 
json
.
loads
(
data
)
 
delta
 
=
 
event
[
"choices"
][
0
].
get
(
"delta"
, {}).
get
(
"content"
, 
""
)
 
if
 
delta
:
 
print
(
delta
, 
end
=
""
, 
flush
=
True
)
 
chunks
.
append
(
delta
)
 
print
()
 
return
 
""
.
join
(
chunks
)

# Single image supports two configs: gundam or base. Example below uses gundam.

generate
(
"document parsing."
, [
"your_image.jpg"
], 
image_mode
=
"gundam"
, 
ngram_window
=
128
)

# Multi image (base only)

generate
(
"Multi page parsing."
, [
"page1.png"
, 
"page2.png"
], 
image_mode
=
"base"
, 
ngram_window
=
1024
)

# PDF (base only)

generate
(
"Multi page parsing."
, 
pdf_to_images
(
"your_doc.pdf"
, 
dpi
=
300
), 
image_mode
=
"base"
, 
ngram_window
=
1024
)

For batch inference,infer.pystarts the SGLang server automatically and sends concurrent requests for an image directory or PDF:

#
 Image directory

python infer.py \
 --image_dir ./examples/images \
 --output_dir ./outputs \
 --concurrency 8 \
 --image_mode gundam

#
 PDF pages

python infer.py \
 --pdf ./examples/document.pdf \
 --output_dir ./outputs \
 --concurrency 8 \
 --image_mode gundam

Useful options:

--model_dir baidu/Unlimited-OCR 
#
 Local path or Hugging Face model ID

--gpu 0 
#
 CUDA_VISIBLE_DEVICES value

--server_log ./log/sglang_server.log

## Visualization

## Acknowledgement

We would like to thankDeepseek-OCR,Deepseek-OCR-2,PaddleOCRfor their valuable models and ideas.

## Citation

@misc
{
yin2026unlimitedocrworks
,
 
title
=
{
Unlimited OCR Works
}
, 
 
author
=
{
Youyang Yin and Huanhuan Liu and YY and Qunyi Xie and Chaorun Liu and Shiqi Yang and Shaohua Wang and Zhanlong Liu and Hao Zou and Jinyue Chen and Shu Wei and Jingjing Wu and Mingxin Huang and Zhen Wu and Guibin Wang and Tengyu Du and Lei Jia
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
2606.23050
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
https://arxiv.org/abs/2606.23050
}
, 
}

## About

Unlimited OCR Works: Welcome the Era of One-shot Long-horizon Parsing.

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

2.3k

 stars
 

### Watchers

15

 watching
 

### Forks

139

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