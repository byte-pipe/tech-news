---
title: Qwen3.5 - How to Run Locally Guide | Unsloth Documentation
url: https://unsloth.ai/docs/models/qwen3.5
site_name: hnrss
content_file: hnrss-qwen35-how-to-run-locally-guide-unsloth-documentat
fetched_at: '2026-03-08T11:07:46.069277'
original_url: https://unsloth.ai/docs/models/qwen3.5
date: '2026-03-07'
description: 'Run the new Qwen3.5 LLMs including Medium: Qwen3.5-35B-A3B, 27B, 122B-A10B, Small: Qwen3.5-0.8B, 2B, 4B, 9B and 397B-A17B on your local device!'
tags:
- hackernews
- hnrss
---

Qwen3.5 is Alibaba’s new model family, including Qwen3.5-35B-A3B,27B,122B-A10B and397B-A17B and the newSmallseries: Qwen3.5-0.8B, 2B, 4B and 9B. The multimodal hybrid reasoning LLMs deliver the strongest performances for their sizes. They support256K contextacross 201 languages, havethinking+non-thinking, and excel in agentic coding, vision, chat, and long-context tasks. The 35B and 27B models work on a 22GB Mac / RAM device. See allGGUFs herearrow-up-right.

circle-check

Mar 5 Update:Redownload Qwen3.5-35B,27B,122Band397B.

* All GGUFs now updated with animproved quantizationalgorithm.
* All use ournew imatrix data. See some improvements in chat, coding, long context, and tool-calling use-cases.
* Tool-calling improvedfollowing our chat template fixes.Fix is universaland applies toanyQwen3.5 format andanyuploader.
* Check new GGUF benchmarksfor Unsloth performance results + ourMXFP4 investigation.
* We're retiring MXFP4 layers from 3 Qwen3.5 GGUFs: Q2_K_XL, Q3_K_XL and Q4_K_XL.

All uploads use UnslothDynamic 2.0arrow-up-rightfor SOTA quantization performance - so 4-bit has important layers upcasted to 8 or 16-bit. Thank you Qwen for providing Unsloth with day zero access. You can alsofine-tuneQwen3.5with Unsloth.

35B-A3B27B122B-A10B397B-A17BFine-tune Qwen3.50.8B • 2B • 4B • 9B

### hashtag⚙️Usage Guide

Table: Inference hardware requirements(units = total memory: RAM + VRAM, or unified memory)

Qwen3.5
3-bit
4-bit
6-bit
8-bit
BF16

0.8B+2B

3 GB

3.5 GB

5 GB

7.5 GB

9 GB

4B

4.5 GB

5.5 GB

7 GB

10 GB

14 GB

9B

5.5 GB

6.5 GB

9 GB

13 GB

19 GB

27B

14 GB

17 GB

24 GB

30 GB

54 GB

35B-A3B

17 GB

22 GB

30 GB

38 GB

70 GB

122B-A10B

60 GB

70 GB

106 GB

132 GB

245 GB

397B-A17B

180 GB

214 GB

340 GB

512 GB

810 GB

circle-check

For best performance, make sure your total available memory (VRAM + system RAM) exceeds the size of the quantized model file you’re downloading. If it doesn’t, llama.cpp can still run via SSD/HDD offloading, but inference will be slower.

Between27Band35B-A3B, use 27B if you want slightly more accurate results and can't fit in your device. Go for 35B-A3B if you want much faster inference.

### hashtagRecommended Settings

* Maximum context window:262,144(can be extended to 1M via YaRN)
* presence_penalty = 0.0 to 2.0default this is off, but to reduce repetitions, you can use this, however using a higher value may result inslight decrease in performance
* Adequate Output Length:32,768tokens for most queries

As Qwen3.5 is hybrid reasoning, thinking and non-thinking mode have different settings:

#### hashtagThinking mode:

General tasks
Precise coding tasks (e.g. WebDev)

temperature = 1.0

temperature = 0.6

top_p = 0.95

top_p = 0.95

top_k = 20

top_k = 20

min_p = 0.0

min_p = 0.0

presence_penalty = 1.5

presence_penalty = 0.0

repeat penalty = disabled or 1.0

repeat penalty = disabled or 1.0

Thinking mode for general tasks:

Thinking mode for precise coding tasks:

#### hashtagInstruct (non-thinking) mode settings:

General tasks
Reasoning tasks

temperature = 0.7

temperature = 1.0

top_p = 0.8

top_p = 0.95

top_k = 20

top_k = 20

min_p = 0.0

min_p = 0.0

presence_penalty = 1.5

presence_penalty = 1.5

repeat penalty = disabled or 1.0

repeat penalty = disabled or 1.0

circle-exclamation

Todisable thinking / reasoning, use--chat-template-kwargs '{"enable_thinking":false}'

If you're onWindowsPowershell, use:--chat-template-kwargs "{\"enable_thinking\":false}"

Use 'true' and 'false' interchangeably.

For Qwen3.5 0.8B, 2B, 4B and 9B, reasoning is disabled by default. To enable it, use:--chat-template-kwargs '{"enable_thinking":true}'

Instruct (non-thinking) for general tasks:

Instruct (non-thinking) for reasoning tasks:

## hashtagQwen3.5 Inference Tutorials:

Because Qwen3.5 comes in many different sizes, we'll be using Dynamic 4-bitMXFP4_MOEGGUF variants for all inference workloads. Click below to navigate to designated model instructions:

Qwen3.5-35B-A3B27B122B-A10B397B-A17BSmall (0.8B • 2B • 4B • 9B)LM Studio

Unsloth Dynamic GGUF uploads:

Qwen3.5-35B-A3Barrow-up-right

Qwen3.5-27Barrow-up-right

Qwen3.5-122B-A10Barrow-up-right

Qwen3.5-397B-A17Barrow-up-right

Qwen3.5-0.8Barrow-up-right

Qwen3.5-2Barrow-up-right

Qwen3.5-4Barrow-up-right

Qwen3.5-9Barrow-up-right

circle-exclamation

presence_penalty = 0.0 to 2.0default this is off, but to reduce repetitions, you can use this, however using a higher value may result inslight decrease in performance.

Currently no Qwen3.5 GGUF works in Ollama due to separate mmproj vision files. Use llama.cpp compatible backends.

### hashtagQwen3.5-35B-A3B

For this guide we will be utilizing Dynamic 4-bit which works great on a 24GB RAM / Mac device for fast inference. Because the model is only around 72GB at full F16 precision, we won't need to worry much about performance. GGUF:Qwen3.5-35B-A3B-GGUFarrow-up-right

### hashtag🦙 Llama.cpp Guides

For these tutorials, we will usingllama.cpparrow-up-rightfor fast local inference, especially if you have a CPU.

1

Obtain the latestllama.cpponGitHub herearrow-up-right. You can follow the build instructions below as well. Change-DGGML_CUDA=ONto-DGGML_CUDA=OFFif you don't have a GPU or just want CPU inference.

2

If you want to usellama.cppdirectly to load models, you can do the below: (:Q4_K_M) is the quantization type. You can also download via Hugging Face (point 3). This is similar toollama run. Useexport LLAMA_CACHE="folder"to forcellama.cppto save to a specific location. The model has a maximum of 256K context length.

Follow one of the specific commands below, according to your use-case:

Thinking mode:

Precise coding tasks (e.g. WebDev):

General tasks:

Non-thinking mode:

General tasks:

Reasoning tasks:

3

Download the model via (after installingpip install huggingface_hub hf_transfer). You can choose Q4_K_M or other quantized versions likeUD-Q4_K_XL. We recommend using at least 2-bit dynamic quantUD-Q2_K_XLto balance size and accuracy. If downloads get stuck, see:Hugging Face Hub, XET debugging

4

Then run the model in conversation mode:

### hashtagQwen3.5 Small (0.8B • 2B • 4B • 9B)

circle-exclamation

For Qwen3.5 0.8B, 2B, 4B and 9B,reasoning is disabledby default. To enable it, use:--chat-template-kwargs '{"enable_thinking":true}'

On Windows use:--chat-template-kwargs "{\"enable_thinking\":true}"

For the Qwen3.5 Small series, because they're so small, all you need to do is change the model name in the scripts to desired variant. For this specific guide we'll be using the 9B parameter variant. To run them all in near full precision, you'll just need 12GB of RAM / VRAM / unified memory device. GGUFs:

Qwen3.5-0.8Barrow-up-right

Qwen3.5-2Barrow-up-right

Qwen3.5-4Barrow-up-right

Qwen3.5-9Barrow-up-right

1

Obtain the latestllama.cpponGitHub herearrow-up-right. You can follow the build instructions below as well. Change-DGGML_CUDA=ONto-DGGML_CUDA=OFFif you don't have a GPU or just want CPU inference.

2

If you want to usellama.cppdirectly to load models, you can do the below: (:Q4_K_XL) is the quantization type. You can also download via Hugging Face (point 3). This is similar toollama run. Useexport LLAMA_CACHE="folder"to forcellama.cppto save to a specific location. The model has a maximum of 256K context length.

Follow one of the specific commands below, according to your use-case:

circle-check

To use another variant other than 9B, you can change the '9B' to: 0.8B, 2B or 4B etc.

Thinking mode (disabled by default)

triangle-exclamation

Qwen3.5 Small models disable thinking by default. Use llama-server to enable it.

General tasks:

circle-check

To use another variant other than 9B, you can change the '9B' to: 0.8B, 2B or 4B etc.

Non-thinking mode is already on by default

General tasks:

Reasoning tasks:

3

Download the model via (after installingpip install huggingface_hub hf_transfer). You can choose Q4_K_M or other quantized versions likeUD-Q4_K_XL. We recommend using at least 2-bit dynamic quantUD-Q2_K_XLto balance size and accuracy. If downloads get stuck, see:Hugging Face Hub, XET debugging

4

Then run the model in conversation mode:

### hashtagQwen3.5-27B

For this guide we will be utilizing Dynamic 4-bit which works great on a 18GB RAM / Mac device for fast inference. GGUF:Qwen3.5-27B-GGUFarrow-up-right

1

Obtain the latestllama.cpponGitHub herearrow-up-right. You can follow the build instructions below as well. Change-DGGML_CUDA=ONto-DGGML_CUDA=OFFif you don't have a GPU or just want CPU inference.

2

If you want to usellama.cppdirectly to load models, you can do the below: (:Q4_K_M) is the quantization type. You can also download via Hugging Face (point 3). This is similar toollama run. Useexport LLAMA_CACHE="folder"to forcellama.cppto save to a specific location. The model has a maximum of 256K context length.

Follow one of the specific commands below, according to your use-case:

Thinking mode:

Precise coding tasks (e.g. WebDev):

General tasks:

Non-thinking mode:

General tasks:

Reasoning tasks:

3

Download the model via (after installingpip install huggingface_hub hf_transfer). You can chooseMXFP4_MOEor other quantized versions likeUD-Q4_K_XL. We recommend using at least 2-bit dynamic quantUD-Q2_K_XLto balance size and accuracy. If downloads get stuck, see:Hugging Face Hub, XET debugging

4

Then run the model in conversation mode:

### hashtagQwen3.5-122B-A10B

For this guide we will be utilizing Dynamic 4-bit which works great on a 70GB RAM / Mac device for fast inference. GGUF:Qwen3.5-122B-A10B-GGUFarrow-up-right

1

Obtain the latestllama.cpponGitHub herearrow-up-right. You can follow the build instructions below as well. Change-DGGML_CUDA=ONto-DGGML_CUDA=OFFif you don't have a GPU or just want CPU inference.

2

If you want to usellama.cppdirectly to load models, you can do the below: (:Q4_K_M) is the quantization type. You can also download via Hugging Face (point 3). This is similar toollama run. Useexport LLAMA_CACHE="folder"to forcellama.cppto save to a specific location. The model has a maximum of 256K context length.

Follow one of the specific commands below, according to your use-case:

Thinking mode:

Precise coding tasks (e.g. WebDev):

General tasks:

Non-thinking mode:

General tasks:

Reasoning tasks:

3

Download the model via (after installingpip install huggingface_hub hf_transfer). You can chooseMXFP4_MOE(dynamic 4bit) or other quantized versions likeUD-Q4_K_XL. We recommend using at least 2-bit dynamic quantUD-Q2_K_XLto balance size and accuracy. If downloads get stuck, see:Hugging Face Hub, XET debugging

4

Then run the model in conversation mode:

### hashtagQwen3.5-397B-A17B

Qwen3.5-397B-A17B is in the same performance tier as Gemini 3 Pro, Claude Opus 4.5, and GPT-5.2. The full 397B checkpoint is ~807GB on disk, but viaUnsloth's 397B GGUFsarrow-up-rightyou can run:

* 3-bit: fits on192GB RAMsystems (e.g., a 192GB Mac)
* 4-bit (MXFP4): fits on256GB RAM. Unsloth4-bit dynamicUD-Q4_K_XLis~214GB on disk- loads directly on a256GB M3 Ultra
* Runs on asingle 24GB GPU + 256GB system RAMviaMoE offloading, reaching25+ tokens/s
* 8-bitneeds~512GB RAM/VRAM
1

Obtain the latestllama.cpponGitHub herearrow-up-right. You can follow the build instructions below as well. Change-DGGML_CUDA=ONto-DGGML_CUDA=OFFif you don't have a GPU or just want CPU inference.

2

If you want to usellama.cppdirectly to load models, you can do the below: (:Q4_K_M) is the quantization type. You can also download via Hugging Face (point 3). This is similar toollama run. Useexport LLAMA_CACHE="folder"to forcellama.cppto save to a specific location. Remember the model has only a maximum of 256K context length.

Follow this forthinkingmode:

Follow this fornon-thinkingmode:

3

Download the model via (after installingpip install huggingface_hub hf_transfer). You can chooseMXFP4_MOE(dynamic 4bit) or other quantized versions likeUD-Q4_K_XL. We recommend using at least 2-bit dynamic quantUD-Q2_K_XLto balance size and accuracy. If downloads get stuck, see:Hugging Face Hub, XET debugging

4

You can edit--threads 32for the number of CPU threads,--ctx-size 16384for context length,--n-gpu-layers 2for GPU offloading on how many layers. Try adjusting it if your GPU goes out of memory. Also remove it if you have CPU only inference.

### hashtag👾 LM Studio Guide

For this guide, we'll be usingLM Studioarrow-up-right, a unified UI interface for running LLMs. The '💡Thinking' and 'Non-thinking' toggle may not appear by default so we'll need some extra steps to get it working.

1

DownloadLM Studioarrow-up-rightfor your device. Then open Model Search, search for 'unsloth/qwen3.5', and download the GGUF (quant) that you desire.

2

Thinking Toggle instructions:After downloading, Open your Terminal / PowerShell and try:lms --help. Then if LM Studio appears normally with many commands, run:

This will get a yaml file which enables your GGUF to have the '💡Thinking' and 'Non-thinking' toggle appear. You can change4bto the desired quant you'd like to have.

Otherwise, you can go toour LM Studio pagearrow-up-rightand download the specific yaml file.

3

Restart LM Studio, then load your downloaded model (with the specific thinking toggle you downloaded). You should now see the Thinking toggle enabled. Don't forget to set thecorrect parameters.

### hashtag🦙 Llama-server serving & OpenAI's completion library

To deploy Qwen3.5-397B-A17B for production, we usellama-serverIn a new terminal say via tmux, deploy the model via:

Then in a new terminal, after doingpip install openai, do:

### hashtag🤔How to enable or disable reasoning & thinking

For the below commands, you can use 'true' and 'false' interchangeably. To haveThink toggle for LM Studio, read our guide.

triangle-exclamation

For Qwen3.5 0.8B, 2B, 4B and 9B, reasoning is disabled by default. To enable it, use:--chat-template-kwargs '{"enable_thinking":true}'

And on Windows or Powershell:--chat-template-kwargs "{\"enable_thinking\":true}"

As an example for Qwen3.5-9B to enable thinking (default is disabled):

And then in Python:

### hashtag👨‍💻 OpenAI Codex & Claude Code

To run the model via local coding agentic workloads, you canfollow our guide. Just change the model name 'GLM-4.7-Flash' to your desired 'Qwen3.5' variant and ensure you follow the correct Qwen3.5 parameters and usage instructions. Use thellama-serverwe just set up just then.

claude
Claude Code
chevron-right
openai
OpenAI Codex
chevron-right

After following the instructions for Claude Code for example you will see:

We can then ask sayCreate a Python game for Chess:

### hashtag🔨Tool Calling with Qwen3.5

SeeTool Calling Guidefor more details on how to do tool calling. In a new terminal (if using tmux, use CTRL+B+D), we create some tools like adding 2 numbers, executing Python code, executing Linux functions and much more:

We then use the below functions (copy and paste and execute) which will parse the function calls automatically and call the OpenAI endpoint for any model:

After launching Qwen3.5 viallama-serverlike inQwen3.5or seeTool Calling Guidefor more details, we then can do some tool calls.

## hashtag📊 Benchmarks

### hashtagUnsloth GGUF Benchmarks

We updated Qwen3.5-35B Unsloth Dynamic quantsbeing SOTAon nearly all bits. We did over 150 KL Divergence benchmarks, totally9TB of GGUFs. We uploaded all research artifacts. We also fixed atool callingchat templatebug(affects all quant uploaders)

* All GGUFs now updated with animproved quantizationalgorithm.
* All use ournew imatrix data. See some improvements in chat, coding, long context, and tool-calling use-cases.
* Qwen3.5-35B-A3B GGUFs are updated to use new fixes (112B, 27B still converting, re-download once they are updated)
* 99.9% KL Divergence shows SOTAon Pareto Frontier for UD-Q4_K_XL, IQ3_XXS & more.
* Retiring MXFP4from all GGUF quants: Q2_K_XL, Q3_K_XL and Q4_K_XL, except for pure MXFP4_MOE.
35B-A3B - KLD benchmarks (lower is better)
122B-A10B - KLD benchmarks (lower is better)

READ OUR DETAILED QWEN3.5 ANALYSIS + BENCHMARKS HERE:

chart-fft
Qwen3.5 GGUF Benchmarks
chevron-right

#### hashtagQwen3.5-397B-A17B Benchmarks

Benjamin Marie (third-party) benchmarkedarrow-up-rightQwen3.5-397B-A17Busing Unsloth GGUFs on a750-prompt mixed suite(LiveCodeBench v6, MMLU Pro, GPQA, Math500), reporting bothoverall accuracyandrelative error increase(how much more often the quantized model makes mistakes vs. the original).

Key results (accuracy; change vs. original; relative error increase):

* Original weights:81.3%
* UD-Q4_K_XL:80.5%(−0.8 points; +4.3% relative error increase)
* UD-Q3_K_XL:80.7%(−0.6 points; +3.5% relative error increase)

UD-Q4_K_XLandUD-Q3_K_XLstay extremely close to the original,well under a 1-point accuracy dropon this suite, which Ben insinuates that you cansharply reduce memory footprint(~500 GB less) with little to no practical loss on the tested tasks.

How to choose:Q3 scoring slightly higher than Q4 here is completely plausible as normal run-to-run variance at this scale, so treatQ3 and Q4 as effectively similar qualityin this benchmark:

* PickQ3if you want thesmallest footprint / best memory savings
* PickQ4if you want aslightly more conservativeoption withsimilarresults

All listed quants utilize our dynamic metholodgy. EvenUD-IQ2_Muses a the same methodology of dynamic however the conversion process is different toUD-Q2-K-XLwhere K-XL is usually faster thanUD-IQ2_Meven though it's bigger, so that is whyUD-IQ2_Mmay perform better thanUD-Q2-K-XL.

### hashtagOfficial Qwen Benchmarks

#### hashtagQwen3.5-35B-A3B, 27B and 122B-A10B Benchmarks

#### hashtagQwen3.5-4B and 9B Benchmarks

#### hashtagQwen3.5-397B-A17B Benchmarks

Previous
Ultra Long Context RL
chevron-left
Next
Qwen3.5 GGUF Benchmarks
chevron-right

Last updated1 day ago

Was this helpful?