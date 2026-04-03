---
title: swiss-ai/Apertus-70B-2509 · Hugging Face
url: https://huggingface.co/swiss-ai/Apertus-70B-2509
site_name: hackernews
fetched_at: '2025-09-06T11:05:26.485258'
original_url: https://huggingface.co/swiss-ai/Apertus-70B-2509
author: denysvitali
date: '2025-09-06'
description: We’re on a journey to advance and democratize artificial intelligence through open source and open science.
---

## You need to agree to share your contact information to access this model

This repository is publicly accessible, butyou have to accept the conditions to access its files and content.

### Apertus LLM Acceptable Use Policy

(1.0 | September 1, 2025)"Agreement" The Swiss National AI Institute (SNAI) is a partnership between the two Swiss Federal Institutes of Technology, ETH Zurich and EPFL.

By using the Apertus LLM you agree to indemnify, defend, and hold harmless ETH Zurich and EPFL against any third-party claims arising from your use of Apertus LLM.

The training data and the Apertus LLM may contain or generate information that directly or indirectly refers to an identifiable individual (Personal Data). You process Personal Data as independent controller in accordance with applicable data protection law. SNAI will regularly provide a file with hash values for download which you can apply as an output filter to your use of our Apertus LLM. The file reflects data protection deletion requests which have been addressed to SNAI as the developer of the Apertus LLM. It allows you to remove Personal Data contained in the model output. We strongly advise downloading and applying this output filter from SNAI every six months following the release of the model.

Log inorSign Upto review the conditions and access this model content.

# Apertus

## Table of Contents

1. Model Summary
2. How to use
3. Evaluation
4. Training
5. Limitations
6. Legal Aspects

## Model Summary

Apertus is a 70B and 8B parameter language model designed to push the boundaries of fully-open multilingual and transparent models.
The model supports over 1000 languages and long context, it uses only fully compliant and open training data, and achieves comparable performance to models trained behind closed doors.

The model is a decoder-only transformer, pretrained on 15T tokens with a staged curriculum of web, code and math data. The model uses a new xIELU activation function and is trained from scratch with the AdEMAMix optimizer. Post-training included supervised fine-tuning and alignment via QRPO.

### Key features

* Fully open model: open weights + open data + full training details including all data and training recipes
* Massively Multilingual: 1811 natively supported languages
* CompliantApertus is trained while respecting opt-out consent of data owners (even retrospectivey), and avoiding memorization of training data

For more details refer to ourtechnical report

## How to use

The modeling code for Apertus is available in transformersv4.56.0, so make sure to upgrade your transformers version. You can also load the model with the latestvLLMwhich uses transformers as a backend.

pip install -U transformers

from
 transformers
import
 AutoModelForCausalLM, AutoTokenizer

model_name =
"swiss-ai/Apertus-70B-2509"

device =
"cuda"

# for GPU usage or "cpu" for CPU usage

# load the tokenizer and the model

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
 model_name,
).to(device)

# prepare the model input

prompt =
"Give me a brief explanation of gravity in simple terms."

messages_think = [
 {
"role"
:
"user"
,
"content"
: prompt}
]

text = tokenizer.apply_chat_template(
 messages_think,
 tokenize=
False
,
 add_generation_prompt=
True
,
)
model_inputs = tokenizer([text], return_tensors=
"pt"
).to(model.device)

# Generate the output

generated_ids = model.generate(**model_inputs, max_new_tokens=
32768
)

# Get and decode the output

output_ids = generated_ids[
0
][
len
(model_inputs.input_ids[
0
]) :]

print
(tokenizer.decode(output_ids, skip_special_tokens=
True
))

We recommend settingtemperature=0.8andtop_p=0.9in the sampling parameters.

### Long context processing

Apertus by default supports a context length up to 65,536 tokens.

### Agentic Usage

Apertus supports tool use

### Deployment

Deployment of the models is directly supported by the newest versions ofTransformers,vLLM,SGLang, and also for running on-device withMLX,

## Evaluation

Pretraining Evaluation:Performance (%) of Apertus models ongeneral language understandingtasks (higher is better) compared to other pretrained models.

Model

Avg

ARC

HellaSwag

WinoGrande

XNLI

XCOPA

PIQA

Fully Open Models

Apertus-8B

65.8

72.7

59.8

70.6

45.2

66.5

79.8

Apertus-70B

67.5

70.6

64.0

73.3

45.3

69.8

81.9

OLMo2-7B

64.0

72.9

60.4

74.5

40.4

55.2

80.9

OLMo2-32B

67.7

76.2

66.7

78.6

42.9

60.1

82.1

EuroLLM-1.7B

54.8

57.2

44.9

58.1

40.7

55.7

72.4

EuroLLM-9B

62.8

67.9

57.9

68.8

41.5

61.1

79.6

SmolLM2-1.7B

58.5

66.1

52.4

65.6

37.6

52.3

77.0

SmolLM3-3B

61.6

68.6

56.4

68.1

40.5

58.2

77.7

Poro-34B

61.7

65.7

57.9

70.6

41.6

56.0

78.5

Open-Weight Models

Llama3.1-8B

65.4

71.6

60.0

73.4

45.3

61.8

80.1

Llama3.1-70B

67.3

74.4

56.5

79.4

44.3

66.7

82.3

Qwen2.5-7B

64.4

69.6

60.1

72.8

43.3

61.7

78.7

Qwen2.5-72B

69.8

76.2

67.5

78.0

46.9

68.2

82.0

Qwen3-32B

67.8

75.6

64.0

73.8

44.4

67.9

80.9

Llama4-Scout-16x17B

67.9

74.7

66.8

73.2

43.5

67.7

81.2

GPT-OSS-20B

58.1

67.0

41.5

66.5

37.4

60.4

75.6

Many additional benchmark evaluations, for pretraining and posttraining phases, multilingual evaluations in around hundred languages, and long context evaluations are provided in Section 5 of theApertus_Tech_Report.pdf

## Training

### Model

* Architecture:Transformer decoder
* Pretraining tokens:15T
* Precision:bfloat16

### Software & hardware

* GPUs:4096 GH200
* Training Framework:Megatron-LM
* ...

### Open resources

All elements used in the training process are made openly available

* Training data reconstruction scripts:github.com/swiss-ai/pretrain-data
* The training intermediate checkpoints are available on the different branches of this same repository

## Limitations

Apertus can produce text on a variety of topics, but the generated content may not always be factually accurate, logically consistent, or free from biases present in the training data. These models should be used as assistive tools rather than definitive sources of information. Users should always verify important information and critically evaluate any generated content.

## Legal Aspects

#### EU AI Act Transparency Documentation and Code of Practice

* Apertus_EU_Public_Summary.pdf
* Apertus_EU_Code_of_Practice.pdf

#### Data Protection and Copyright Requests

For removal requests of personally identifiable information (PII) or of copyrighted content, please contact the respective dataset owners or us directly

* llm-privacy-requests@swiss-ai.org
* llm-copyright-requests@swiss-ai.org

#### Output Filter for PII

* Currently no output filter is provided.
* Please check this site regularly for an output filter that can be used on top of the Apertus LLM. The filter reflects data protection deletion requests which have been addressed to us as the developer of the Apertus LLM. It allows you to remove Personal Data contained in the model output. We strongly advise downloading and applying this output filter from this site every six months.

## Contact

To contact us, please send an email tollm-requests@swiss-ai.org

## Citation

@misc{swissai2025apertus,
 title={{Apertus: Democratizing Open and Compliant LLMs
for
 Global Language Environments}},
 author={Apertus Team},
 year={2025},
 howpublished={\url{https://huggingface.co/swiss-ai/Apertus-70B-2509}}
}

Downloads last month
824


Safetensors

Model size

70.6B params

Tensor type

BF16

·

Files info

Inference Providers

NEW


Text Generation

This model isn't deployed by any Inference Provider.

🙋

3

Ask for provider support

## Model tree forswiss-ai/Apertus-70B-2509

Finetunes

2 models

## Collection includingswiss-ai/Apertus-70B-2509

4 items

•

Updated

4 days ago

•

					192
