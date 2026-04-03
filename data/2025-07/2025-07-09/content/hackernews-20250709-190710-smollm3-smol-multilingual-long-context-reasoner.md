---
title: 'SmolLM3: smol, multilingual, long-context reasoner'
url: https://huggingface.co/blog/smollm3
site_name: hackernews
fetched_at: '2025-07-09T19:07:10.707989'
original_url: https://huggingface.co/blog/smollm3
author: kashifr
date: '2025-07-09'
description: We’re on a journey to advance and democratize artificial intelligence through open source and open science.
---

Back to Articles

# SmolLM3: smol, multilingual, long-context reasoner

Published
				July 8, 2025

Update on GitHub

		Upvote


305

* +299

Elie Bakouch

eliebak

Follow

Carlos Miguel Patiño

cmpatino

Follow

Anton Lozhkov

anton-l

Follow

Edward Beeching

edbeeching

Follow

Aymeric Roucher

m-ric

Follow

Nouamane Tazi

nouamanetazi

Follow

Aksel Joonas Reedi

akseljoonas

Follow

Guilherme Penedo

guipenedo

Follow

Hynek Kydlicek

hynky

Follow

Clémentine Fourrier

clefourrier

Follow

Nathan Habib

SaylorTwift

Follow

Kashif Rasul

kashif

Follow

Quentin Gallouédec

qgallouedec

Follow

Hugo Larcher

hlarcher

Follow

Mathieu Morlon

glutamatt

Follow

Joshua

Xenova

Follow

Vaibhav Srivastav

reach-vb

Follow

Xuan-Son Nguyen

ngxson

Follow

Colin Raffel

craffel

Follow

Lewis Tunstall

lewtun

Follow

Loubna Ben Allal

loubnabnl

Follow

Leandro von Werra

lvwerra

Follow

Thomas Wolf

thomwolf

Follow

Small language models are becoming increasingly important as users seek capable models that can be deployed efficiently. The community has produced a fascinating range of capable small models, each pushing the boundaries of what's possible at this scale. With SmolLM3, we're excited to contribute a new competitive fully open 3B model:

* Base model:https://hf.co/HuggingFaceTB/SmolLM3-3B-Base
* Instruct and reasoning model:https://hf.co/HuggingFaceTB/SmolLM3-3B

SmolLM3 sits in the efficiency sweet spot.Our 3B model outperforms Llama-3.2-3B and Qwen2.5-3B while staying competitive with larger 4B alternatives (Qwen3 & Gemma3). Beyond the performance numbers, we're sharing exactly how we built it using public datasets and training frameworks.

Model summary:

* 3B modeltrained on 11T tokens, SoTA at the 3B scale and competitive with 4B models
* Instruct modelwithdual mode reasoning,supportingthink/no_thinkmodes
* Multilingual supportfor 6 languages: English, French, Spanish, German, Italian, and Portuguese
* Long contextup to 128k with NoPE and using YaRN

The complete recipe:We're releasing SmolLM3 with our engineering blueprint. It includes architecture details, exact data mixtures showing how we progressively boost performance across domains in a three-stage pretraining approach, and the methodology for building a hybrid reasoning model. Usually, achieving these results would require months of reverse engineering. Instead, we're providing the full methodology.

Whether you're building your own models or want to understand what drives performance at this scale, this blueprint shows the engineering story behind competitive 3B performance.

Let’s have a look at the pretraining stage.

# Pretraining

SmolLM3 both changed the architecture and data mixture over its predecessors. Let’s have a look at the architecture and training configurations first!

## Architecture and training details

SmolLM3 follows a transformer decoder architecture with tied embedding similar to SmolLM2, building on Llama architecture with some key modifications optimized for efficiency and long context performance.

Grouped Query Attention (GQA):We replaced multi-head attention with grouped-query attention using 4 groups. Our ablations on a 3B model trained with 100B tokens fromFineWeb-Edushowed that GQA matches the performance of multi-head attention while significantly reducing the KV cache size during inference.

NoPE:We implemented NoPE from "RoPE to NoRoPE and Back Again: A New Hybrid Attention Strategy" (Yang et al., 2025), selectively removing rotary position embeddings from every 4th layer. This approach improves long context performance without affecting short context capabilities, as confirmed by our ablations.

Intra-Document Masking:During training, we use attention masking to ensure tokens from different documents in the same training sequence don't attend to each other. Similar to Llama 3, this helps with faster and more stable long context training while maintaining short context performance.

Training Stability:Following OLMo 2, we remove weight decay from embedding layers to improve training stability. This modification contributed to more stable training dynamics, with embedding norms naturally stabilizing at healthier values during training without impacting overall performance in our ablations.

All these changes were validated through ablations using the same 3B architecture trained on 100B tokens from FineWeb-Edu, ensuring each modification either improved performance or maintained it while offering other benefits.

Training Configuration: We use a global batch size of 2.36M tokens with 4096 sequence length, a learning rate of 2e-4, and the AdamW optimizer (beta1: 0.9, beta2: 0.95) with weight decay of 0.1 and gradient clipping of 1. We use the WSD (Warmup-Stable-Decay) scheduler, with 2000  warmup steps, and a linear decay to 0 in the final 10% training steps. We usenanotronframework for the training,datatrovefor data processing andlightevalfor evaluation. The model was trained on 384 H100 GPUs for 24 days. You can see the distributed training setup in the following figure.

In addition to architecture changes we also ablated and improved the training recipe. Let’s have a closer look.

## Data mixture and training stages

Following SmolLM2's multi-stage approach, we train SmolLM3 on 11.2T tokens using a three-stage training strategy that mixes web, math, and code data with evolving proportions. We conducted extensive ablations on 3B models trained on 50B to 100B tokens to determine the data mixture and ratios.

The pretraining consists of these stages, also shown in the figure above:

* Stage 1: Stable phase (0T → 8T tokens)This foundation stage establishes strong general capabilities with our core dataset mixture:Web: 85% (12% multilingual) - FineWeb-Edu, DCLM, FineWeb2 and FineWeb2-HQCode: 12% - The Stack v2 (16 programming languages), StarCoder2 pull requests, Jupyter and Kaggle notebooks, GitHub issues, and StackExchange.Math: 3% - FineMath3+ and InfiWebMath3+
* Web: 85% (12% multilingual) - FineWeb-Edu, DCLM, FineWeb2 and FineWeb2-HQ
* Code: 12% - The Stack v2 (16 programming languages), StarCoder2 pull requests, Jupyter and Kaggle notebooks, GitHub issues, and StackExchange.
* Math: 3% - FineMath3+ and InfiWebMath3+
* Stage 2: Stable phase (8T → 10T tokens)We introduce higher quality math and code datasets while maintaining good web coverage:Web: 75% (12% Multilingual)Code: 15% - Adding Stack-EduMath: 10% - Introducing FineMath4+, InfiWebMath4+, and MegaMath (including Qwen Q&A, Pro synthetic rewrites, and text-code interleaved blocks)
* Web: 75% (12% Multilingual)
* Code: 15% - Adding Stack-Edu
* Math: 10% - Introducing FineMath4+, InfiWebMath4+, and MegaMath (including Qwen Q&A, Pro synthetic rewrites, and text-code interleaved blocks)
* Stage 3: Decay Phase (10T → 11.1T tokens)The final stage further upsamples math and code dataWeb: 63% (12% Multilingual)Code: 24% - upsampling of high-quality code dataMath: 13% - upsampling math data and introducing instruction and reasoning datasets such as OpenMathReasoning
* Web: 63% (12% Multilingual)
* Code: 24% - upsampling of high-quality code data
* Math: 13% - upsampling math data and introducing instruction and reasoning datasets such as OpenMathReasoning

With these stages and mixtures we achieved very competitive performance for the base model. More on that in the evaluation section. The nanotron training configs with exact data weights can be foundhere. We will also share our training logs along with intermediate checkpoints.

After the main pretraining we improved the model in a mid-training stage for long context and reasoning.

# Mid-training

We call the long context adaptation and reasoning adaption “mid-training”. They are much shorter than the main pretraining but still somewhat general and aimed at improving the model in those two domains. Let’s first have a look at long context training.

## Long Context extension

After the main pretraining, we trained SmolLM3 on an additional 100B tokens to extend its context length. We sequentially extended the context window in two stages for 50B tokens each: first transitioning from 4k to 32k context with RoPE theta increased to 1.5M, then from 32k to 64k context with RoPE theta increased to 5M. Both stages upsampled math, code, and reasoning data. During ablations, we found that upsampling specific long context data such as code repositories, books, and long web pages (beyond the naturally long samples in our mixture) didn't further boost performance on RULER and HELMET benchmarks. Using NoPE and training on the decay mixture with longer sequences and increased RoPE theta values was sufficient to achieve competitive long context performance up to 64k.

Following Qwen2.5, we use YARN to extrapolate beyond the training context length. During inference, the model can handle up to  128k context (2x extension beyond the 64k training length).

## Reasoning Mid-training

After extending the context length of the model, we trained it at a mid-training stage to incorporate reasoning capabilities. The main difference between the mid-training stage and the pre- and post-training stages is that we targeted a general capability without yet focusing on a specific domain. In our case, we wanted to train the model to reason without targeting a particular domain, such as mathematics or computer code.

Our mid-training dataset contained 35B tokens sourced from Open Thought’sOpenThoughts3-1.2Mand a subset from NVIDIA’sLlama-Nemotron-Post-Training-Dataset-v1.1with reasoning traces from R1. We used the ChatML chat template andwrapped packingto avoid providing too much structure to the model. We trained the model for 4 (~140B tokens) epochs and used the checkpoint for subsequent SFT stages.

# Post-training

The release of reasoning models likeDeepSeek R1andQwen3has demonstrated the powerful capabilities that emerge when models can engage in explicit reasoning. However, the community still lacks fully open recipes with public datasets to build dual instruction models that support both reasoning and non-reasoning modes. Most existing approaches involve complex reinforcement learning processes and proprietary datasets, making it difficult for researchers to reproduce and build upon these results.

In this section, we explain how we tackled these challenges and share our complete recipe for building a dual instruction model. We detail how we balance performance between reasoning and non-reasoning modes through a carefully designed training pipeline that includes mid-training for general reasoning capabilities, supervised fine-tuning with synthetic data generation, and alignment using Anchored Preference Optimization (APO) - a recent variant of DPO.

## Building the Chat Template

Before diving into the training methodology, it's essential to establish how users interact with our dual-mode model. The chat template serves as the interface that enables seamless switching between reasoning and non-reasoning modes, and its design directly impacts both our training data format and model behavior. SmolLM3's chat template allows users to control the reasoning mode during a conversation. Users can activate reasoning or non-reasoning modes by including the/thinkand/no_thinkflags, respectively, in the system prompt. In non-reasoning mode, we pre-fill the model's response with empty think blocks, similar to Qwen3, to ensure direct answers without explicit reasoning.

SmolLM3 supports tool calling, and its chat template incorporates two distinct sections for tool descriptions: XML Tools and Python Tools. This specific categorization proved beneficial in our experiments for the model's accurate interpretation of tool definitions in each format.

The chat template provides a default system message for both reasoning modes, along with a metadata section that includes the date, knowledge cut-off date, and current reasoning mode. Users can replace the default system message by providing one with thesystemrole. The metadata section can be excluded by using the/system_overrideflag in the system prompt, offering flexibility for specific use cases.

## Supervised Finetuning

Following the reasoning mid-training stage, where we trained the model on 140B tokens of general reasoning data, we proceed with Supervised Finetuning (SFT) to incorporate capabilities in across both reasoning and non-reasoning modes for math, code, general reasoning, instruction following, multilinguality, and tool calling. Training a dual-mode model requires carefully balancing the data mixture to maintain strong performance in both modes across all target domains. To evaluate SmolLM3’s performance throughout training, we tracked the following domains: math, code, general reasoning, instruction following, and multilinguality.

The primary challenge we encountered when building the reasoning mode dataset was the scarcity of datasets containing reasoning traces for certain domains. To address this gap, we generated synthetic data by promptingQwen3-32Bin reasoning mode with prompts from existing non-reasoning datasets. This allowed us to improve performance in domains where the model initially struggled in reasoning mode, such as multi-turn conversations, multilinguality, and everyday conversations.

Our final data mixture was the result of extensive ablations examining the optimal ratio of reasoning to non-reasoning tokens and the composition within each mode. The resulting SFT dataset contains 1.8B tokens: 1B in non-reasoning mode and 0.8B in reasoning mode, comprising 12 non-reasoning datasets and 10 datasets with reasoning traces. We trained for 4 epochs (~8B tokens) usingBFD (best-fit decreasing) packingwith the loss masked on user turns and the results from tool calls.

We will release this data mixture along with our full training scripts to enable the community to reproduce and build upon our work.

## Off-policy model alignment with Anchored Preference Optimization (APO)

After the SFT step, we performed a round of model alignment using a combination of theTulu3 preference datasetfor non-reasoning mode and new synthetic preference pairs for reasoning mode, that we generated from Qwen3-32B and Qwen3-0.6B. To ensure full coverage of all domains in the non-thinking dataset, we generated complementing thinking mode preference pairs. We selected generations from Qwen3-32B as “chosen” and responses from Qwen3-0.6B as “rejected” for alignment with Anchored Preference Optimization.

Anchored Preference Optimization(APO) is a variant ofDirect Preference Optimization(DPO) that provides a more stable optimization objective. In DPO, the reward function r_θ(x,y) measures the log-ratio of the probability of sequence during training compared to model at the start of training, the reference model:

Here β controls how much the model being optimized can change relative to the reference model. The DPO loss optimizes triplets of prompts x, chosen y_w and rejected y_l responses:

The APO objective has been shown to be more stable, and we also observed higher downstream performance in our internal ablations.

While downstream evaluations showed improvements across mathematics, science, instruction following, coding, chat, and multilingual tasks, we observed performance degradation on long context benchmarks like RULER. We traced this degradation back to the reasoning mid-training stage, where the focus on reasoning capabilities impacted long context performance. Additionally, the APO training data was limited to 24k tokens since the vast majority of our reasoning dataset fell below this length.

To mitigate this performance drop, we explored model merging as a solution.

## Model Merging

Model merging is a popular and powerful technique that allows combining the strengths of different models without the computational overhead of ensembling or the need for additional training. We used theMergeKitlibrary to perform the model merging, as it includes several merging methods, including linear and non-linear merging.

Our merging recipe consists of two steps:

1. Take each APO checkpoint and create a model “soup”.
2. Combine the model soup with a mid-training checkpoint that has strong long-content performance. A linear merge with weights of 0.9 and 0.1 for the APO model soup and mid-training checkpoint, respectively, achieved the best performance. We were able to recover the base model’s RULER score on contexts up to 128k tokens.

The resulting model is the checkpoint we are releasing today. It maintains performance across a wide range of tasks. So let’s turn the the evaluation result both of this model as well as the base model.

# Evaluation

We evaluate base models and the instruct model both in reasoning and non-reasoning mode. Let’s first cover the base model’s performance!

## Base model

The plot below shows SmolLM3's win rate across 12 popular benchmarks evaluating knowledge, reasoning, math, and coding capabilities. SmolLM3 consistently outperforms other 3B models and achieves competitive performance with larger 4B models including Qwen3-4B and Gemma3-4B.

Evaluation benchmarks used for the win rate: HellaSwag, ARC, Winogrande, CommonsenseQA, MMLU-CF, MMLU Pro CF, PIQA, OpenBookQA, GSM8K, MATH, HumanEval+, MBPP+

SmolLM3 achieves first or second place on knowledge and reasoning benchmarks (HellaSwag, ARC, BoolQ), demonstrating strong performance in these core capabilities. Math and coding performance is competitive within the 3B class. Long-context performance on Ruler 64k shows the model can handle extended sequences effectively.

The model demonstrates strong multilingual performance across five major European languages when evaluated on multilingual benchmarks including Global MMLU, MLMM HellaSwag, Flores-200, Belebele, testing knowledge, commonsense reasoning, text understanding, and translation. This shows SmolLM3 maintains consistent performance beyond English.

In summary, the base model shows very strong performance across many domains. Let’s see how this translates to the instruct model’s performance.

## Dual Instruct / Reasoning model

Since SmolLM3 has both an instruct and reasoning mode we need to evaluate the model in both modes and compare to models with same capabilities.

### No extending thinking evaluation

We evaluate SmolLM3 against other 3B non-reasoning models and compare it to Qwen3 reasoning models in no thinking mode across multiple benchmarks. As shown in the performance chart, SmolLM3 outperforms other 3B non-reasoning models including Llama3.2 3B Instruct and Qwen2.5 3B Instruct and sits at an efficiency sweet spot between reasoning models, significantly outperforming Qwen3 1.7B while getting close to the 4B model performance at a lower computational cost.

So the instruct model sits right at the pareto front of perfomance and cost. Let’s see how the reasoning model does!

### Extending thinking evaluation

When evaluating SmolLM3's reasoning capabilities with extended thinking enabled, the model shows substantial improvements across most benchmarks compared to its non-reasoning counterpart. We observe notable gains in challenging tasks like AIME 2025 (36.7% vs 9.3%), competitive programming on LiveCodeBench (30.0% vs 15.2%), and graduate-level reasoning on GPQA Diamond (41.7% vs 35.7%).

While Qwen3 4B generally achieves the highest scores across both thinking and non-thinking modes, SmolLM3 demonstrates competitive performance within the 3B parameter class, particularly excelling in mathematical reasoning and complex problem-solving tasks. The model's dual-mode capability allows users to choose between faster inference without reasoning or more thorough analysis with extended thinking.

So the last question is: how can you use the model?

# How to run locally

The modeling code for SmolLM3 is available in transformersv4.53.0, so make sure to upgrade your transformers version. You can also load the model with the latestvllmwhich uses transformers as a backend.

pip install -U transformers

from
 transformers
import
 AutoModelForCausalLM, AutoTokenizer

model_name =
"HuggingFaceTB/SmolLM3-3B"

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

We recommend settingtemperature=0.6andtop_p=0.95in the sampling parameters.

### Enabling and Disabling Extended Thinking Mode

We enable extended thinking by default, so the example above generates the output with a reasoning trace. For choosing between enabling, you can provide the/thinkand/no_thinkflags through the system prompt as shown in the snippet below for extended thinking disabled. The code for generating the response with extended thinking would be the same except that the system prompt should have/thinkinstead of/no_think.

prompt =
"Give me a brief explanation of gravity in simple terms."

messages = [
 {
"role"
:
"system"
,
"content"
:
"/no_think"
},
 {
"role"
:
"user"
,
"content"
: prompt}
]

text = tokenizer.apply_chat_template(
 messages,
 tokenize=
False
,
 add_generation_prompt=
True
,
)

### Agentic Usage

SmolLM3 supports tool calling! Just pass your list of tools under the argumentxml_tools(for standard tool-calling), orpython_tools(for calling tools like python functions in a<code>snippet).

from
 transformers
import
 AutoModelForCausalLM, AutoTokenizer

checkpoint =
"HuggingFaceTB/SmolLM3-3B"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

tools = [
 {

"name"
:
"get_weather"
,

"description"
:
"Get the weather in a city"
,

"parameters"
: {
"type"
:
"object"
,
"properties"
: {
"city"
: {
"type"
:
"string"
,
"description"
:
"The city to get the weather for"
}}}}
]

messages = [
 {

"role"
:
"user"
,

"content"
:
"Hello! How is the weather today in Copenhagen?"

 }
]

inputs = tokenizer.apply_chat_template(
 messages,
 enable_thinking=
False
,
# True works as well, your choice!

 xml_tools=tools,
 add_generation_prompt=
True
,
 tokenize=
True
,
 return_tensors=
"pt"

)

outputs = model.generate(inputs)

print
(tokenizer.decode(outputs[
0
]))

# Conclusion

We release SmolLM3, a small, long-context, multilingual, reasoner with up to 128k context. In addition to the model checkpoint we release the full training recipe including pre-training, mid-training, post-training, and synthetic data generation as well as the datasets (coming shortly). We hope this model proves useful to the community and the recipe will allow other groups to improve upon it.

# Resources

* Models collection with quantized checkpoints:Link
* SmolLM GitHub repo with pretraining configs and evaluation code:https://github.com/huggingface/smollm
* Our HuggingFace org:https://huggingface.co/HuggingFaceTB

More Articles from our Blog

## Welcome Gemma 3: Google's all new multimodal, multilingual, long context open LLM

ByariG23498March 12, 2025•441

## Welcome the Falcon 3 Family of Open Models!

ByariG23498December 17, 2024•128

### Community

clem

about 14 hours ago

Beautiful!

❤️

13

13


+

Reply

TNGHK

about 11 hours ago

Bravo, bravo, bravo!

Reply

raphaelmansuy

about 10 hours ago

Incredible! Thank you.

See translation

Reply

knight7561

about 10 hours ago

Thats a great write.Definitely adding to the Weekend read..!

See translation

Reply

wonhosong

about 8 hours ago

•

edited about 8 hours ago

Thanks for sharing.

Reply

nlml

about 8 hours ago

Great work! I have a question/curiosity. What is the advantage of splitting the model across two GPUs during training? (mentioned you use Tensor Parallelism (TP) of 2, Data Parallelism (DP) of 4 on each 8-GPU node). I am guessing the model can fit on a single GPU given it is small? I would have thought in such a case the most efficient implementation would be to use DP=8 ?

See translation

🔥

1

1


+

Reply

Xidong

about 6 hours ago

owesome ! ! !

Reply

Mousaicv

about 6 hours ago

nice work

Reply

carbene101

about 5 hours ago

Wow, great going and amazing writeup!

See translation

Reply

Remixa

about 4 hours ago

Thanks for sharing!!!I might have spotted a minor mistake, should "To ensure full coverage of all domains in thenon-thinkingdataset" really be "To ensure full coverage of all domains in thethinkingdataset"？

See translation

Reply

rishiraj

about 3 hours ago

I really like reading such detailed model reports that discuss these technical things like architecture, data & exact parameters that are so useful for ML Engineers. Loved the report even more than the model (which is good as well lol).

See translation

Reply

Yihel

about 2 hours ago

•

edited about 2 hours ago

Thanks for sharing!!

Probably unrelated question, thegraphshows Qwen3 1.7B has 2B parameters. Is it correct?

See translation

Reply

Yihel

about 2 hours ago

Thisgraphshows the GQA has more query heads than key-value heads, which contradicts the original design. Is it intentional?

See translation

Reply

Edit
Preview

Upload images, audio, and videos by dragging in the text input, pasting, or
clicking here
.


Tap or paste here to upload images

				Comment


·Sign uporlog into comment

		Upvote


305

* +293
