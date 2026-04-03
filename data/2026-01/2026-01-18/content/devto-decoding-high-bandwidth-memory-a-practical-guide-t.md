---
title: 'Decoding high-bandwidth memory: A practical guide to GPU memory for fine-tuning AI models - DEV Community'
url: https://dev.to/googleai/decoding-high-bandwidth-memory-a-practical-guide-to-gpu-memory-for-fine-tuning-ai-models-56af
site_name: devto
fetched_at: '2026-01-18T11:06:35.864156'
original_url: https://dev.to/googleai/decoding-high-bandwidth-memory-a-practical-guide-to-gpu-memory-for-fine-tuning-ai-models-56af
author: Shir Meir Lador
date: '2026-01-15'
description: We've all been there. You've meticulously prepared your dataset and written your training script. You... Tagged with ai, gpu, performance, machinelearning.
tags: '#ai, #gpu, #performance, #machinelearning'
---

We've all been there. You've meticulously prepared your dataset and written your training script. You hitrun, and your excitement builds, only to be crushed by the infamous error: CUDA out of memory.

This is one of the most common roadblocks in AI development. Your GPU'sHigh Bandwidth Memory (HBM), is the high-speed memory that holds everything that's needed for computation, and running out of it is a hard stop. But how do you know how much you need?

To build a clear foundation, we'll start by breaking down the HBM consumers on a single GPU and we'll present key strategies to reduce HBM consumption on a single GPU. Later, we'll explore advanced multi-GPU strategies like data andmodel parallelismthat can help relieve memory pressure and scale your training in the cloud.

## Understanding HBM: What's using all the memory?

When you fine-tune a model, your HBM is primarily consumed by three things:

1. Model Weights:This is the most straightforward. It's the storage space required for the model's parameters—the "brain" that it uses to make predictions. A 7-billion parameter model loaded in 16-bit precision will take up roughly 14 GB before you even process a single piece of data.
2. Optimizer StatesandGradients:This is the overhead that's required for learning. To update the model's weights, the training process needs to calculate gradients (the direction of learning) and theoptimizer(like the popularAdamW) needs to store its own data to guide the training. In full fine-tuning, this can be the largest consumer of HBM.
3. ActivationsandBatch Data:This is the most dynamic part. When your data (images, text, etc.) flows through the model's layers, the intermediate calculations, or activations, are stored in HBM. The memory needed here is directly proportional to your batch size. A larger batch size means more activations are stored simultaneously, which leads to faster training but much higher memory usage.

Note:These calculations are theoretical minimums. Real-world frameworks add up to 30% overhead due totemporary buffers, kernel launches, and memory fragmentation.

Although it's impossible to get a perfect number without experimentation, you can estimate your HBM needs with this general formula:Total HBM ≈ (Model Size) + (Optimizer States) + (Gradients) + (Activations)Further reading:See this excellent JAX e-book that coversthese topicsin great detail and even has some"try it out yourself" test questions.

## Example: Why full fine-tuning is so demanding

To see why running out of memory is such a common problem, let's walk through a real-world example that I recently worked on: fine-tuning themedgemma-4b-it model, which has 4 billion parameters. Ourscriptloads it in bfloat16 precision (2 bytes per parameter).

First, let's calculate the static HBM footprint. This is the memory that's required just to load the model and prepare it for training, before you've even processed a single piece of data.

1. Model Size:The memory that's needed to simply hold the model on the GPU.

4 billion parameters × 2 bytes/parameter = 8 GB

 

2. Gradients and Optimizer States:The overhead for training every parameter with the AdamW optimizer.

Gradients: 4 billion parameters × 2 bytes/parameter = 8 GB

Optimizer States (AdamW): 2 × 4 billion parameters × 2 bytes/parameter = 16 GB

 

Note:While AdamW is a popular optimizer, other optimizers, such as Adafactor and Lion, have different memory footprints.

Adding these together gives us our baseline HBM cost for a full fine-tuning attempt:

8 GB (Model) + 8 GB (Gradients) + 16 GB (Optimizer) = 32 GB

 

This 32 GB is the baseline just to start the training process. On top of this, the GPU needsadditional memory for activations, which is adynamiccost that grows with your batch size and input data size. This is why full fine-tuning of large models is so demanding and often reserved for the most powerful hardware.

## Key strategies to reduce HBM consumption

The HBM requirement for a full fine-tune can seem impossibly high. But several powerful techniques can reduce memory consumption, making it feasible to train large models on consumer-grade or entry-level professional GPUs.

### Parameter-Efficient Fine-Tuning (PEFT) with LoRA

Instead of training all the billions of parameters in a model,Parameter-Efficient Fine-Tuning (PEFT)methods focus on training only a small subset of parameters. The most popular of these isLoRA (Low-Rank Adaptation).

LoRAworks by freezingthe original model's weights and injecting a tiny number of new, trainableadapterlayersinto the model architecture. This means the memory-hungry gradients and optimizer states are only needed for these few million new parameters, not the full 4 billion.

#### The math behind LoRA's memory savings

LoRA doesn't remove the base model from your GPU. The full 8 GB of the original model's weights are still loaded and taking up HBM. They're just frozen, which means that the GPU isn't training them. All of the memory savings come from the fact that you no longer need to store the huge gradients and optimizer states for that massive, frozen part of the model.

Let's recalculate the static HBM footprint with LoRA, assuming it adds 20 million trainable parameters:

1. Model Size (unchanged):The base model is still loaded.

4 billion parameters × 2 bytes/parameter = 8 GB

 

2. LoRA Gradients & Optimizer States:We now only need overhead for the tiny set of new parameters.

Gradients: 20 million parameters × 2 bytes/parameter = 40 MB

Optimizer States: 2 × 20 million parameters × 2 bytes/parameter = 80 MB

 

The new static HBM footprint is now:

8 GB (Model) + 40 MB (Gradients) + 80 MB (Optimizer) ≈ 8.12 GB

 

The training overhead has shrunk from 24 GB to just 120 MB. Your new baseline memory requirement is now just over 8 GB. This lower baseline memory requirement leaves much more room for the dynamic memory that's needed for activations, which lets you use a reasonable batch size on a common 16 GB or 24 GB GPU without running out of memory.

### Model quantization

Besides training fewer parameters, we can also shrink the ones that we have by usingquantization, which involves reducing thenumerical precisionof the model's weights. The standard precision for modern training isbfloat16because it offers the dynamic range of float32 with half the memory footprint. But we can reduce HBM usage further by converting weights to lower-precision integer formats like int8 or int4.

Using lower-precision integer formats has a significant impact on HBM when compared to the standard bfloat16 baseline:

* bfloat16 (standard):The baseline size (e.g., a 7B model requires~14 GB).
* 8-bit precision:Halves the model size (e.g., 14 GB becomes~7 GB).
* 4-bit precision:Reduces the model size by a factor of 4 (e.g., 14 GB becomes~3.5 GB).

The reduction in size lets you fit much larger models into memory with minimal degradation in performance.

A word of warning from experience:When I started experimenting in this area, my first attempt to load the model using the common float16 data type failed spectacularly. The model's outputs were NaN, and a quick check revealed that every internal value had collapsed into NaN (Not a Number) .

The culprit was a classicnumerical overflow. The float16 data type has a tiny numerical range and it can't represent any number larger than 65,504. During training, intermediate values can easily exceed this limit, causing an overflow that creates a NaN. The fix was a simple one-line change to bfloat16, which has a massive numerical range that prevents these overflows and keeps training stable. For fine-tuning large models, always prefer bfloat16 for stability.

Combining LoRA and Quantization:These techniques work best together. Quantized LoRA (QLoRA) is a method that stores the massive base model in a highly efficient 4-bit format (specifically NF4 or NormalFloat 4), while adding small, trainable LoRA adapters in bfloat16. During the training process, the 4-bit weights are dequantized to bfloat16 for computation. Dequantizing in process lets you fine-tune very large models on a single GPU with the memory savings of 4-bit storage and the mathematical stability of 16-bit training.

### FlashAttention: An algorithmic speed boost

Finally,FlashAttentionis a foundational algorithmic optimization that significantly reduces HBM usage and speeds up training on both single and multi-GPU setups. The attention mechanism in transformers is a primary memory bottleneck because it requires storing a large, intermediateattention matrix. FlashAttention cleverly reorders the computation to avoid storing this full matrix in memory, leading to substantial memory savings and faster execution.

Best of all, enabling FlashAttention is often as simple as a one-line change. In the MedGemma fine-tuning script, this was done by setting the valueattn_implementation="sdpa", which can automatically use more efficient backends like FlashAttention if the hardware supports it.

## Scaling beyond a single GPU: Advanced strategies

Techniques like LoRA and quantization are useful for lowering HBM needs on a single GPU. But to train truly massive models or to really speed up the process, you'll eventually need to scale out to multiple GPUs. Here are some of the key strategies that can be used to distribute the load and overcome memory limitations.

### Data parallelism

Data parallelism is the most common and intuitive approach to scaling. In a Distributed Data Parallel (DDP) setup, the entire model is replicated on each GPU. The key is that the global batch of training data is split, with each GPU processing its own mini-batch concurrently. After each forward and backward pass, the gradients from each GPU are averaged together to ensure that all of the model replicas learn from the entire dataset and they stay in sync. This method is excellent forspeeding up trainingbut itdoesn't reduce the HBMthat's required to hold the model itself, because every GPU needs a full copy.

### Model parallelism

When a model is too large to fit into the memory of a single GPU, you must usemodel parallelism. Instead of replicating the model, this strategysplits the modelacross multiple GPUs. There are two primary ways to do this:

* Tensor parallelism:This method splits a single large operation (like a massive weight matrix in a transformer layer) across several GPUs. Each GPU computes its part of the operation, and the results are combined.
* Pipeline parallelism:This technique places different layers of the model onto different GPUs in a sequence. The data flows through the first set of layers on GPU 1, then the output is passed to GPU 2 for the next set of layers, and so on, like an assembly line.

These strategies are more complex to implement than data parallelism, but they're essential for models that are simply too big for one device.

### Fully Sharded Data Parallelism (FSDP)

FSDPis a powerful and efficient hybrid strategy that combines the ideas ofdata parallelismandmodel parallelism. Unlike standard data parallelism where each GPU holds a full copy of the model, optimizer states, and gradients, FSDP shards (or splits) all of these components across the GPUs. Each GPU only materializes the full parameters for thespecific layerthat it's computing at that moment,dramatically reducing the peak HBMusage per device. FSDP makes it possible to train enormous models on a cluster of smaller GPUs.

By combining these hardware and software strategies, you canscale your fine-tuning jobsfrom a single GPU to apowerful, distributed clustercapable of handling even the most demanding AI models.

## HBM sizing guide

HBM

Use case and explanation

16 GB

Sufficient for basic inference or fine-tuning with techniques like LoRA using a very small batch size (e.g., 1-2). Expect slower training times at this level.

24 GB

The recommended starting point for a good experience with 4-7 B parameter models. This capacity allows for a more effective batch size (e.g., 8-16) when using LoRA, providing a great balance of training speed and cost.

40+ GB

Necessary for maximizing training speed with large batch sizes or for working with larger models (in the 20+ B parameter range) now or in the future.

Encountering the CUDA out of memory error provides an important lesson in the trade-offs between model size, training techniques, and batch size. By understanding what consumes your HBM, you can make smarter decisions and keep your projects running smoothly.

I hope that this guide has helped clarify the CUDA out of memory error and that it's given you the tools to keep your projects running smoothly. When you're ready to take the next step, Google Cloud has the tools to accelerate your AI development.

* ExploreGPU configurations for your Cloud Run servicesand best practices for runningCloud Run jobs with GPU.
* For maximum control: Spin up aCompute Engineinstance with the latest NVIDIA H100 or A100 Tensor Core GPUs and take full control of your environment.
* Looking to optimize your model hosting infrastructure? Take a look atThe Ultimate Guide to xPU Inference Configuration.
* For a deeper dive into scaling your model, check outHow to Scale Your Model.
* New to Google Cloud? Get started with the $300 free credit to find the perfect solution for your next project.

Special thanks to Jason Monden and Sayce Falk from the AI compute team for their helpful review and feedback on this post.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
