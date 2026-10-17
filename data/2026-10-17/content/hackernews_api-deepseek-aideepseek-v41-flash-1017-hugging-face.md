---
title: deepseek-ai/DeepSeek-V4.1-Flash-1017 · Hugging Face
url: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
site_name: hackernews_api
content_file: hackernews_api-deepseek-aideepseek-v41-flash-1017-hugging-face
fetched_at: '2026-10-17T21:14:27.013581'
original_url: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
author: theykk
date: '2026-10-17'
description: We’re on a journey to advance and democratize artificial intelligence through open source and open science.
tags:
- hackernews
- trending
---

# DeepSeek-V4.1-Flash-1017

Technical Report👁️

## Introduction

DeepSeek-V4.1-Flash-1017is a minor update toDeepSeek-V4.1-Flash, delivering substantial improvements across reasoning, coding, agentic tasks, and visual benchmarks. Alongside these gains, the model reduces task execution time and output length, enabling users to complete tasks faster and at lower cost and advancing the performance–cost Pareto frontier across multiple agent harnesses.

Benchmark

DS-V4.1-Flash-1017

DS-V4.1-Flash

K3

GLM-5.3

GPT-5.6 Sol

Opus 5

HLE w/o tools

42.6 (44.0†)

36.8 (39.1†)

43.5

42.0†

44.5

56.3

Terminal-Bench 4.0

42.3

31.2

12.6

37.9

39.9

51.8

DeepSWE v1.1

77.0

74.2

67.5

66.9

73.0

74.0

ProgramBench

29.1

20.3

17.5

19.0

23.0

37.0

NL2Repo-Bench

68.2

65.4

58.0

58.0

56.8

75.3

Automation-Bench v1.0.6

60.5

54.8

46.7

48.8

45.8

50.3

Agents’ Last Exam

35.4

31.8

27.6

28.5

26.7

28.6

Apex Bench v1.1

72.1

64.6

47.8

56.6

54.3

65.8

Chartography (w/tools)

83.0

78.9

68.1

—

79.9

84.0

BabyVision (w/tools)

92.5

89.6

85.7

—

88.9

94.1

ZeroBench-main (w/tools)

51.0

49.0

41.0

—

53.0

52.0

† denotes the text-only subset of HLE. We use the Claude Code harness for Terminal-Bench 4.0 and the Mini-SWE-V2 harness for DeepSWE v1.1.

## Prompt Encoding

This release does not include a Jinja-format chat template. Theencodingfolder contains a self-contained Python reference implementation (encoding.py) with test cases for multi-turn conversations, tool calling, thinking mode, numeric reasoning effort, mid-conversation system messages, and interleaved image content.

For production use, we additionally releasedeepseek-recipe, a set of Rust libraries with Python bindings that provides the same prompt format as a maintained, protocol-aware toolkit. It converts Messages, Chat Completions, and Responses API requests into the Conversation format, encodes them into DeepSeek V4 and V4.1 prompts or token IDs, and parses model output back into complete or streamed responses — covering thinking, tool calls, images, and generation settings. Model inference, tool execution, and HTTP transport are left to the caller.

## Minimal Inference

Please refer to theinferencefolder for instructions on weight conversion and running inference locally.

Recommended sampling parameters:

Parameter

Value

temperature

1.0

top_p

1.0

context_window

1M tokens

max_tokens

≥ 256K

## License

This repository and the model weights are licensed under theMIT License.

## Citation

@misc{deepseekai2026deepseekv41flash,
 title={DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression},
 author={DeepSeek-AI},
 year={2026},
}

## Contact

If you have any questions, please raise an issue or contact us atservice@deepseek.com.

 
 
Downloads last month
 
-
 
 

 
 
Safetensors
 
Model size
 
763B params
 
Tensor type
 
BF16 
·
F32 
·
F8_E4M3 
·
I8 
·
 
 
 

Files info

 
 
 
 
 
 
 
 
 
 
Inference Providers
 
NEW
 
 
 
 
Image-Text-to-Text
 
 
 
 
 
This model isn't deployed by any Inference Provider.
 
🙋
 
11
 
Ask for provider support
 
 
 
 

## Model tree fordeepseek-ai/DeepSeek-V4.1-Flash-1017

 
 
 
 
Finetunes
 
 
 
3 models
 
 
Quantizations
 
 
 
18 models
 
 
 

## Spaces usingdeepseek-ai/DeepSeek-V4.1-Flash-10172

 
 
 

## Collection includingdeepseek-ai/DeepSeek-V4.1-Flash-1017

 
 
 
11 items
 
•
 
Updated 
about 15 hours ago
 
•
 
 932