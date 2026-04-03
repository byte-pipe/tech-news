---
title: Unsloth Dynamic 2.0 GGUFs | Unsloth Documentation
url: https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs
site_name: hnrss
content_file: hnrss-unsloth-dynamic-20-ggufs-unsloth-documentation
fetched_at: '2026-02-28T19:08:41.779608'
original_url: https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs
date: '2026-02-28'
description: A big new upgrade to our Dynamic Quants!
tags:
- hackernews
- hnrss
---

We're excited to introduceUnslotharrow-up-rightDynamic v2.0 quantization - a major upgrade to our previous quants. This new method outperforms leading quantization methods and sets new benchmarks forAider Polglot, 5-shot MMLU and KL Divergence.

This means you can now run + fine-tunequantized LLMswhile preserving as much accuracy as possible! You can run the 2.0 GGUFs on most inference engines like llama.cpp, LM Studio etc.

Feb 27, 2026 Update:Qwen3.5is out and we fixed some tool-calling chat template issues and benchmarked every GGUF on perplexity & KL Divergence.See benchmarks!

Thekey advantageof using theUnsloth packagearrow-up-rightand quants is our active role in fixing bugs in major models. We've collaborated directly with teams behindQwen3arrow-up-right,Meta (Llama 4)arrow-up-right,Mistral (Devstral)arrow-up-right,Google (Gemma 1–3)arrow-up-rightandMicrosoft (Phi-3/4)arrow-up-right, contributing fixes that increase accuracy.

circle-check

Sept 10, 2025 update:You asked for tougher benchmarks, so here's Aider Polyglot results! Our Dynamic 3-bit DeepSeek V3.1 GGUF scores75.6%, surpassing many full-precision SOTA LLMs.Read more.

You can also view real-world use-case benchmarks conducted byBenjamin Mariearrow-up-rightfor LiveCodeBench v6, MMLU Pro etc.:

You can see how Unsloth's GGUFs performs better than the non-Unsloth quants despite being ~8GB smaller.

Detailed analysis of our benchmarks and evaluation further below.

### hashtag💡 What's New in Dynamic v2.0?

* Revamped Layer Selection for GGUFs + safetensors:Unsloth Dynamic 2.0 now selectively quantizes layers much more intelligently and extensively. Rather than modifying only select layers, we now dynamically adjust the quantization type of every possible layer, and the combinations will differ for each layer and model.
* Current selected and all future GGUF uploads will utilize Dynamic 2.0 and our new calibration dataset. The dataset contains more than >1.5Mtokens(depending on model) and comprise of high-quality, hand-curated and cleaned data - to greatly enhance conversational chat performance.
* Previously, our Dynamic quantization (DeepSeek-R1 1.58-bit GGUF) was effective only for MoE architectures.Dynamic 2.0 quantization now works on all models (including MOEs & non-MoEs).
* Model-Specific Quants:Each model now uses a custom-tailored quantization scheme. E.g. the layers quantized in Gemma 3 differ significantly from those in Llama 4.
* To maximize efficiency, especially on Apple Silicon and ARM devices, we now also add Q4_NL, Q5.1, Q5.0, Q4.1, and Q4.0 formats.

To ensure accurate benchmarking, we built an internal evaluation framework to match official reported 5-shot MMLU scores of Llama 4 and Gemma 3. This allowed apples-to-apples comparisons between full-precision vs. Dynamic v2.0,QATand standardimatrixGGUF quants.

All future GGUF uploads will utilize Unsloth Dynamic 2.0, and our Dynamic 4-bit safe tensor quants will also benefit from this in the future.

## hashtag📊 Why KL Divergence?

Accuracy is Not All You Needarrow-up-rightshowcases how pruning layers, even by selecting unnecessary ones still yields vast differences in terms of "flips". A "flip" is defined as answers changing from incorrect to correct or vice versa. The paper shows how MMLU might not decrease as we prune layers or do quantization,but that's because some incorrect answers might have "flipped" to become correct. Our goal is to match the original model, so measuring "flips" is a good metric.

The paper also shows that interestingly KL Divergence is highly correlated with flips, and so our goal is to reduce the mean KL Divergence whilst increasing the disk space of the quantization as less as possible.

## hashtag⚖️ Calibration Dataset Overfitting

Most frameworks report perplexity and KL Divergence using a test set of Wikipedia articles. However, we noticed using the calibration dataset which is also Wikipedia related causes quants to overfit, and attain lower perplexity scores. We utilizeCalibration_v3arrow-up-rightandCalibration_v5arrow-up-rightdatasets for fair testing which includes some wikitext data amongst other data.Also instruct models have unique chat templates, and using text only calibration datasets is not effective for instruct models(base models yes). In fact most imatrix GGUFs are typically calibrated with these issues. As a result, they naturally perform better on KL Divergence benchmarks that also use Wikipedia data, since the model is essentially optimized for that domain.

To ensure a fair and controlled evaluation, we do not to use our own calibration dataset (which is optimized for chat performance) when benchmarking KL Divergence. Instead, we conducted tests using the same standard Wikipedia datasets, allowing us to directly compare the performance of our Dynamic 2.0 method against the baseline imatrix approach.

## hashtag🔢MMLU Replication Adventure

* Replicating MMLU 5 shot was nightmarish. Wecould notreplicate MMLU results for many models including Llama 3.1 (8B) Instruct, Gemma 3 (12B) and others due tosubtle implementation issues. Llama 3.1 (8B) for example should be getting ~68.2%, whilst using incorrect implementations can attain35% accuracy.
MMLU implementation issues
* Llama 3.1 (8B) Instruct has a MMLU 5 shot accuracy of 67.8% using a naive MMLU implementation. We find however Llamatokenizes "A" and "_A" (A with a space in front) as different token ids. If we consider both spaced and non spaced tokens, we get 68.2%(+0.4%)
* Interestingly Llama 3 as per Eleuther AI'sLLM Harnessarrow-up-rightalso appends"The best answer is"to the question, following Llama 3's original MMLU benchmarks.
* There are many other subtle issues, and so to benchmark everything in a controlled environment, we designed our own MMLU implementation from scratch by investigatinggithub.com/hendrycks/testarrow-up-rightdirectly, and verified our results across multiple models and comparing to reported numbers.

## hashtag✨Gemma 3 QAT Replication, Benchmarks

The Gemma team released two QAT (quantization aware training) versions of Gemma 3:

1. Q4_0 GGUF - Quantizes all layers to Q4_0 via the formulaw = q * block_scalewith each block having 32 weights. Seellama.cpp wikiarrow-up-rightfor more details.
2. int4 version - presumablyTorchAO int4 stylearrow-up-right?

We benchmarked all Q4_0 GGUF versions, and did extensive experiments on the 12B model. We see the12B Q4_0 QAT model gets 67.07%whilst the full bfloat16 12B version gets 67.15% on 5 shot MMLU. That's very impressive! The 27B model is mostly nearly there!

Metric
1B
4B
12B
27B

MMLU 5 shot

26.12%

55.13%

67.07% (67.15% BF16)

70.64% (71.5% BF16)

Disk Space

0.93GB

2.94GB

7.52GB

16.05GB

Efficiency*

1.20

10.26

5.59

2.84

We designed a newEfficiency metricwhich calculates the usefulness of the model whilst also taking into account its disk size and MMLU 5 shot score:

Efficiency
=
MMLU 5 shot score
−
25
Disk Space GB
\text{Efficiency} = \frac{\text{MMLU 5 shot score} - 25}{\text{Disk Space GB}}
Efficiency
=
Disk Space GB
MMLU 5 shot score
−
25
​
circle-exclamation

We have tominus 25since MMLU has 4 multiple choices - A, B, C or D. Assume we make a model that simply randomly chooses answers - it'll get 25% accuracy, and have a disk space of a few bytes. But clearly this is not a useful model.

On KL Divergence vs the base model, below is a table showcasing the improvements. Reminder the closer the KL Divergence is to 0, the better (ie 0 means identical to the full precision model)

Quant
Baseline KLD
GB
New KLD
GB

IQ1_S

1.035688

5.83

0.972932

6.06

IQ1_M

0.832252

6.33

0.800049

6.51

IQ2_XXS

0.535764

7.16

0.521039

7.31

IQ2_M

0.26554

8.84

0.258192

8.96

Q2_K_XL

0.229671

9.78

0.220937

9.95

Q3_K_XL

0.087845

12.51

0.080617

12.76

Q4_K_XL

0.024916

15.41

0.023701

15.64

If we plot the ratio of the disk space increase and the KL Divergence ratio change, we can see a much clearer benefit! Our dynamic 2bit Q2_K_XL reduces KLD quite a bit (around 7.5%).

Truncated table of results for MMLU for Gemma 3 (27B). See below.

1. Our dynamic 4bit version is 2GB smaller whilst having +1% extra accuracy vs the QAT version!
2. Efficiency wise, 2bit Q2_K_XL and others seem to do very well!
Quant
Unsloth
Unsloth + QAT
Disk Size
Efficiency

IQ1_M

48.10

47.23

6.51

3.42

IQ2_XXS

59.20

56.57

7.31

4.32

IQ2_M

66.47

64.47

8.96

4.40

Q2_K_XL

68.70

67.77

9.95

4.30

Q3_K_XL

70.87

69.50

12.76

3.49

Q4_K_XL

71.47

71.07

15.64

2.94

Google QAT

70.64

17.2

2.65

chevron-right
Click here
 for Full Google's Gemma 3 (27B) QAT Benchmarks:
hashtag
Model
Unsloth
Unsloth + QAT
Disk Size
Efficiency

IQ1_S

41.87

43.37

6.06

3.03

IQ1_M

48.10

47.23

6.51

3.42

IQ2_XXS

59.20

56.57

7.31

4.32

IQ2_M

66.47

64.47

8.96

4.40

Q2_K

68.50

67.60

9.78

4.35

Q2_K_XL

68.70

67.77

9.95

4.30

IQ3_XXS

68.27

67.07

10.07

4.18

Q3_K_M

70.70

69.77

12.51

3.58

Q3_K_XL

70.87

69.50

12.76

3.49

Q4_K_M

71.23

71.00

15.41

2.98

Q4_K_XL

71.47

71.07

15.64

2.94

Q5_K_M

71.77

71.23

17.95

2.58

Q6_K

71.87

71.60

20.64

2.26

Q8_0

71.60

71.53

26.74

1.74

Google QAT

70.64

17.2

2.65

## hashtag🦙Llama 4 Bug Fixes + Run

We also helped and fixed a few Llama 4 bugs:

* Llama 4 Scout changed the RoPE Scaling configuration in their official repo. We helped resolve issues in llama.cpp to enable thischange herearrow-up-right
* Llama 4's QK Norm's epsilon for both Scout and Maverick should be from the config file - this means using 1e-05 and not 1e-06. We helped resolve these inllama.cpparrow-up-rightandtransformersarrow-up-right
* The Llama 4 team and vLLM also independently fixed an issue with QK Norm being shared across all heads (should not be so)herearrow-up-right. MMLU Pro increased from 68.58% to 71.53% accuracy.
* Wolfram Ravenwolfarrow-up-rightshowcased how our GGUFs via llama.cpp attain much higher accuracy than third party inference providers - this was most likely a combination of the issues explained above, and also probably due to quantization issues.

As shown in our graph, our 4-bit Dynamic QAT quantization deliver better performance on 5-shot MMLU while also being smaller in size.

### hashtagRunning Llama 4 Scout:

To run Llama 4 Scout for example, first clone llama.cpp:

Then download out new dynamic v 2.0 quant for Scout:

And and let's do inference!

circle-check

Read more on running Llama 4 here:https://docs.unsloth.ai/basics/tutorial-how-to-run-and-fine-tune-llama-4arrow-up-right

Previous
Text-to-Speech Fine-tuning
chevron-left
Next
Aider Polyglot Benchmarks
chevron-right

Last updated6 minutes ago

Was this helpful?