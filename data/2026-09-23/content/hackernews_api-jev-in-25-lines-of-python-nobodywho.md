---
title: Jev in 25 lines of Python - NobodyWho
url: https://www.nobodywho.ai/posts/jev-in-25-lines/
site_name: hackernews_api
content_file: hackernews_api-jev-in-25-lines-of-python-nobodywho
fetched_at: '2026-09-23T15:19:22.496555'
original_url: https://www.nobodywho.ai/posts/jev-in-25-lines/
author: bashbjorn
date: '2026-09-23'
description: Everyone is talking about Jev - here it is in 25 lines of Python.
tags:
- hackernews
- trending
---

# Jev in 25 lines of Python

Everyone and their mom is talking aboutJev. Jev this, Jev that. Everyone on Twitter is all over Jev, how it's the next frontier of large language models and the AI paradigm. We don’t really think so. So here's Jev in 25 lines of Python.

Load the model.

# /// script

# requires-python = ">=3.12"

# dependencies = ["huggingface-hub", "llama-cpp-python", "numpy"]

# ///

import
 numpy

from
 llama_cpp 
import
 Llama

# Really, you can use any GGUF model from https://huggingface.co/models?library=gguf

model 
=
 Llama
.
from_pretrained
(

 repo_id
=
"Qwen/Qwen3-0.6B-GGUF"
,

 filename
=
"Qwen3-0.6B-Q8_0.gguf"
,

 n_ctx
=
512
,

 logits_all
=
True
,

 verbose
=
False
,

)

Load the prompt and define your choices.

labels 
=
 
[
"A"
,
 
"B"
,
 
"C"
]

choices 
=
 
[
"Legitimate"
,
 
"Spam"
,
 
"Phishing"
]

email 
=
 
"Payroll asks for your password on a non-company sign-in page."

options 
=
 
"\n"
.
join
(

 
f"
{
label
}
. 
{
choice
}
"
 
for
 label
,
 choice 
in
 
zip
(
labels
,
 choices
,
 strict
=
True
)

)

prompt 
=
 
f"""<|im_start|>system
Choose one option.<|im_end|>
<|im_start|>user
Email: 
{
email
}
\n\n
{
options
}
<|im_end|>
<|im_start|>assistant
<think>\n\n</think>\n\n"""

model
.
eval
(
tokens
=
model
.
tokenize
(
text
=
prompt
.
encode
(
)
,
 add_bos
=
False
,
 special
=
True
)
)

Massage the logits into probabilities.

logits 
=
 model
.
scores
[
model
.
n_tokens 
-
 
1
]

token_ids 
=
 
[
model
.
tokenize
(
text
=
label
.
encode
(
)
,
 add_bos
=
False
)
[
0
]
 
for
 label 
in
 labels
]

choice_logits 
=
 numpy
.
asarray
(
[
logits
[
token_id
]
 
for
 token_id 
in
 token_ids
]
)

logprobs 
=
 choice_logits 
-
 numpy
.
logaddexp
.
reduce
(
choice_logits
)

probabilities 
=
 numpy
.
exp
(
logprobs
)

for
 name
,
 scores 
in
 
(

 
(
"Logits"
,
 choice_logits
)
,

 
(
"Log probabilities"
,
 logprobs
)
,

 
(
"Probabilities"
,
 probabilities
)
,

)
:

 values 
=
 numpy
.
round
(
scores
.
astype
(
float
)
,
 
3
)
.
tolist
(
)

 
print
(
f"
{
name
}
:"
,
 
dict
(
zip
(
choices
,
 values
,
 strict
=
True
)
)
)

# Logits: {'Legitimate': 26.254, 'Spam': 27.262, 'Phishing': 29.614}

# Log probabilities: {'Legitimate': -3.482, 'Spam': -2.474, 'Phishing': -0.122}

# Probabilities: {'Legitimate': 0.031, 'Spam': 0.084, 'Phishing': 0.885}

There. That’s Jev.

## But no, you don’t understand Jev!

Yeah, we know.

* We don't call it aSystem One decision model.
* We didn’t call an API.
* We didn't create a bunch of synthetic data.
* We didn't train a model withReinforcement Learning for Calibrated Decisions (RLCD)to calibrate the decisions and probabilities (even though they arenot always correct).

## But yes. This is Jev.

* It classifies: it gets a prompt with choices and outputs probabilities.
* It's fast.
* It's local.
* You don't send your data anywhere else.

And we like not sending your data anywhere else. Check outNobodyWho.

(note: this is a parody blog post, see these links for better/more complete open implementations of Jev:OpenJev,openjev-sglang, andOpenJev on DiffusionGemma.)

Everything NobodyWho do is open-source, please leave astar on Githubto support us ❤️

Published Sep 22, 2026 by Duarte O.Carmo

 Technical