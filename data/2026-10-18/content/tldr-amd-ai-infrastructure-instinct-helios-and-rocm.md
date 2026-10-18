---
title: 'AMD AI Infrastructure: Instinct, Helios and ROCm'
url: https://devoriales.com/amd-s-ai-infrastructure-instinct-helios-and-the-rocm-challenge
site_name: tldr
content_file: tldr-amd-ai-infrastructure-instinct-helios-and-rocm
fetched_at: '2026-10-18T21:14:56.197383'
original_url: https://devoriales.com/amd-s-ai-infrastructure-instinct-helios-and-the-rocm-challenge
author: Aleksandro Matejic
date: '2026-10-18'
published_date: '2026-10-18T19:53:10.226043'
description: Assess AMD Instinct GPUs, Helios and ROCm, including memory, software portability, customer agreements and the cost of running AI infrastructure.
tags:
- tldr
---

###### LATEST

* Trivy Supply Chain Attack: When Your Security Scanner Becomes the Threat
* Is Claude Opus 4.6 Fast Mode Really Worth 6× the Price?
* Unlocking Higher Pod Density in EKS with Prefix Delegation
* AWS Regional NAT Gateway: What It Is and Why You Should Care

Kubectl Cheatsheet

Helm Cheatsheet

Vim Cheatsheet

Docker Cheatsheet

 Only registred users can make comments
 

ai

Share on LinkedIn

Share on X

Share on Facebook

Share on WhatsApp

Share on Reddit

Copy link

Written By

Aleksandro Matejic

 
Published

2026-10-18

Reading Time

14 min

# AMD's AI Infrastructure: Instinct, Helios and the ROCm Challenge

NVIDIA's position in AI infrastructure is supported by both its accelerators and the software used to develop and operate workloads on them. AMD is expanding its alternative: Instinct GPUs, EPYC processors, Pensando networking and ROCm software, increasingly delivered as a complete system rather than individual components.

The developments are worth examining on their own terms. AMD has shipped several generations of AI accelerators, announced a rack-scale platform and signed major customer agreements. That gives engineering teams more to evaluate, but it does not demonstrate that AMD is faster or cheaper for a particular application. Those comparisons still require measurements on the workloads that will actually run.

## What an accelerator does in an AI server

An accelerator is a processor designed to handle particular computations efficiently alongside the host CPU. AMD Instinct GPUs perform many numerical operations in parallel, including the matrix multiplications used by neural networks. Their high-bandwidth memory holds model data close to the compute units. The CPU still runs application logic and coordinates work; the GPU handles the numerical workload.

A model's weights are the numerical parameters learned during training. Running a model repeatedly reads and processes those weights, so memory capacity and bandwidth matter alongside arithmetic performance.

AMD Instinct MI430X product rendering. AMD positions this accelerator for scientific computing and AI, including FP64 (64-bit floating-point) workloads. It is a different product from the MI455X used in Helios. Image: AMD.[17]

## AMD has experience building very large systems

AMD's accelerator work did not begin with the recent interest in large language models. Frontier, the HPE system at Oak Ridge National Laboratory, became the first machine to pass one exaflop on the TOP500's High Performance Linpack (HPL) benchmark in 2022. It uses AMD EPYC CPUs and Instinct MI250X accelerators. El Capitan at Lawrence Livermore National Laboratory reached number one on the November 2024 TOP500 list using Instinct MI300A accelerated processing units. Each MI300A combines EPYC CPU cores and GPU processing with shared high-bandwidth memory in one package.[1][2]

These systems establish experience with large accelerator installations and the engineering involved in connecting and operating them. They do not establish performance leadership in language model training or inference. Scientific computing and AI differ in numerical precision, memory access patterns, communication and software. Frontier's HPL score, for example, is not a benchmark for generating tokens.

## Instinct has been moving toward larger AI workloads

The Instinct MI300X, introduced in December 2023, provides 192 GB of HBM3 memory per GPU. The MI325X increased that figure to 256 GB of HBM3E. AMD's MI350X and MI355X, introduced in June 2025, provide 288 GB of HBM3E each, with a publishedpeakmemory bandwidth of 8 TB/s. The MI350 series uses AMD's CDNA 4 architecture and supports reduced-precision formats including MXFP4 and MXFP6. These are vendor hardware specifications, not measured model throughput.[3][4][5]

Figure 1. Selected AMD Instinct milestones. Roadmap dates are AMD plans, not evidence of shipped products.

For inference, memory requirements extend beyond model weights. The key-value cache used during token generation grows with active sequences and context length. Runtime buffers and other working data also consume memory. Weight precision and quantization can substantially change the amount required.

Capacity and bandwidth address different limits. More memory can allow a model or a larger working set to remain on an accelerator. Higher memory bandwidth can help when the workload is limited by data movement. Neither specification determines latency or throughput on its own. The result depends on the model, batch size, sequence length, parallelism and implementation.

Training is different again. Activations, gradients and optimizer state can add large memory demands, while synchronization between accelerators affects scaling. A GPU that works well for serving one model should not be assumed to have the same relative advantage for training another.

Figure 2. Capacity and bandwidth are separate constraints. The 288 GB and 8 TB/s figures are AMD's published MI355X specifications, not application benchmarks.

## Helios brings the components together

In July 2026, AMD launched its Helios rack-scale platform. Its announced reference configuration contains 72 Instinct MI455X GPUs, 18 sixth-generation EPYC “Venice” CPUs, Pensando networking and ROCm software. AMD described Helios as being in production. That statement does not establish how many customer racks were operational as of this article's publication. AMD also said OpenAI expected to bring Helios systems online beginning in the fourth quarter of 2026.[6]

Figure 3. Helios at the component level. This is a logical view, not a physical wiring or rack topology diagram.

The rack-level design matters because accelerator performance increasingly depends on communication outside each GPU. Some workloads distribute model layers or tensors across multiple GPUs. Others place different parts of a model on different devices. These approaches transfer intermediate results between accelerators, sometimes repeatedly during each inference request.

It is useful to distinguish communication among GPUs within a tightly connected system, often described asscale-up, from communication across systems, often described asscale-out. Both can affect the performance of large deployments. The importance of each depends on the model and the way it is divided across hardware.

AMD's stated goal with Helios is to coordinate compute, memory and networking at rack scale. Whether that yields better economics than a competing configuration has to be measured. AMD's performance claims are vendor claims; the published launch specifications alone are insufficient for an independent comparison.

AMD has announced MI500 GPUs for 2027 and MI600 GPUs for 2028, along with subsequent Helios generations. These are roadmap targets as of October 2026.[6]

Product images:AMD publishesofficial Helios photography and captions in its press kit. The images are linked rather than reproduced here because the rights for reuse on an independent blog have not been confirmed.

## ROCm is the harder part of the comparison

NVIDIA's software ecosystem is a substantial part of its position. CUDA provides the programming environment, and libraries such as cuDNN, NCCL and TensorRT cover common operations, distributed communication and inference optimization. Applications using those libraries directly can be closely tied to NVIDIA hardware.[7]

AMD's ROCm platform supports major frameworks, including PyTorch, and inference projects such as vLLM. That support can allow a team to keep much of its high-level application code when moving between GPU vendors. It does not make CUDA binaries, custom kernels or all third-party extensions interchangeable.[8][9]

Figure 4. The same application framework may use different vendor libraries and GPU code. The diagram shows possible dependencies, not an exact runtime call graph.

AMD supplies HIP and HIPIFY tools to help adapt CUDA source code. Translation can reduce manual changes, but translated code still needs to compile, produce correct results and perform acceptably on the target hardware. Unsupported API calls and platform-specific optimizations can require further work.[10]

A concrete example is vLLM, which supports both NVIDIA CUDA and AMD ROCm. Its documentation specifies supported AMD GPU generations and ROCm version requirements; installation paths, binaries and features are not necessarily identical. Treating “vLLM supports ROCm” as a statement that any CUDA deployment can switch unchanged would be misleading.[9]

For teams running inference on Kubernetes, the evaluation also includes GPU drivers, container images, device plugins, scheduling, metrics, node updates and failure recovery. Version alignment matters across the driver, ROCm runtime, framework and serving engine. AMD's compatibility matrix documents supported combinations.[8]

The practical question is how much of an existing deployment is portablewithout losing features, performance or operational reliability. That answer varies by application and software versions.

## Open models make comparisons possible, not automatic

Access to model weights gives organizations the option of running some AI workloads on their own infrastructure. It also makes it possible to test the same model across hardware platforms, subject to the model's license and software requirements.

Open weights alone do not guarantee portability. An inference engine still needs implementations of the model's operations, suitable kernels and support for the selected numerical formats. Models that can run on both AMD and NVIDIA may need different software builds and tuning. There is no technical basis for saying that open-weight models inherently favor AMD.

Model architecture adds another consideration. Mixtral 8×7B, described in a 2024 research paper, uses a mixture-of-experts design. Each expert layer has eight feed-forward experts, and a router selects two for each token. The model has about 47 billion parameters in total, with about 13 billion active for a token during inference. The quoted figures come from the original paper.[11]

Figure 5. Simplified top-two routing for one expert layer. Selection can differ for each token; the other experts remain part of the model.

Using fewer experts reduces the computation performed for that token compared with evaluating every expert. It does not eliminate the need to store or retrieve other experts' weights. Spreading experts across devices can also increase communication and introduce load-balancing challenges. Those trade-offs are relevant on either GPU platform.

## Training, fine-tuning and inference on AMD

### Training: learning the model's parameters

Training runs examples through a model, measures its prediction error and calculates gradients: signals indicating how to change its parameters. An optimizer applies those changes over repeated steps. Training from scratch learns the initial model rather than adapting an existing one. It needs memory for intermediate results, gradients and optimizer state as well as weights.

AMD can run this workload at scale. The OLMo research paper documents training a 7-billion-parameter model on LUMI using Instinct MI250X GPUs. That is evidence of language-model training, unlike an HPL supercomputer score. AMD is a candidate for teams with a supported training stack and the ability to tune distributed jobs; communication between GPUs, checkpointing and recovery still need testing.[16]

### Fine-tuning: adapting an existing model

Fine-tuning continues training a pretrained model on a more focused dataset, such as examples of classifying support tickets. Full fine-tuning updates all its weights. LoRA instead trains small added parameter matrices while keeping the original weights fixed, reducing the memory needed for trainable parameters and their optimizer state. The base model and intermediate results still occupy memory.

ROCm documents LoRA and distributed fine-tuning workflows. AMD's larger-memory GPUs can be useful when the model and training data batches otherwise need to be split across more devices. Check support for the exact model, libraries and GPU before assuming an existing workflow will transfer unchanged.[15]

### Inference: using the trained model

Inference uses learned parameters to produce outputs, such as a chatbot response or document summary. Ordinary inference does not update the model's weights. For language models, processing the input prompt and generating output tokens can place different demands on compute and memory.

Memory-heavy inference is a useful place to evaluate AMD. As a capacity estimate, 70 billion parameters stored at two bytes each require about 140 GB for weights alone. Those raw weights fit within an MI300X's published 192 GB, but the serving engine still needs room for the key-value cache and working buffers. This arithmetic is not a throughput benchmark or a guarantee that every serving configuration fits.[3]

Large memory can help with larger models, longer contexts or more simultaneous requests, provided the serving software supports the workload efficiently. For a strict response-time target or an application built around custom CUDA kernels, migration effort can outweigh that capacity benefit. Compare cost per request at the required latency and output quality, rather than choosing a GPU from memory size alone.

## Customer agreements are not the same as installed capacity

AMD announced a multi-year agreement with OpenAI in October 2025 for 6 gigawatts of AMD GPU deployments. In February 2026, AMD and Meta announced a separate agreement for up to 6 gigawatts over multiple generations. These are announced commitments and plans with deployment milestones. The gigawatt figures should not be presented as counts of installed GPUs, completed systems or booked revenue.[12][13]

AMD's reported financial results provide a different form of evidence. For the second quarter of 2026, the company reported$11.536 billion in total revenue, up 50% year over year. ItsData Center segment reported $6.7 billion, up 107%. That segment includes EPYC CPUs and Instinct accelerators, so the $6.7 billion cannot accurately be described as AI GPU revenue.[14]

The combination of product launches, disclosed customer agreements and financial results suggests that AMD has a serious place in AI infrastructure procurement. None of these sources establishes that AMD is gaining a specific percentage of the AI GPU market, or that an individual workload will run better on its hardware. Those conclusions would need separate evidence.

## Operating cost is where the evaluation becomes concrete

A hardware price comparison misses several important costs. For a self-hosted inference service, a useful starting point is the total expense of serving a defined volume of requests at an agreed level of quality and responsiveness.

The comparison should hold the model version, quantization approach, input and output lengths, concurrency profile and acceptable latency as constant as possible. Then measure completed requests or output tokens per second, together with latency distribution, failed requests and actual system power draw. A system that produces more tokens per second is not automatically more economical if it fails the latency requirement.

Power and cooling matter, but so do utilization, servers, networking, support contracts and the engineering time spent maintaining the software stack. Running a GPU at low utilization can change the cost calculation substantially. For training, the relevant measure is often the total cost and elapsed time required to reach a defined training target rather than raw theoretical operations per second.

These figures have to come from an actual deployment or a controlled trial. There is no defensible general-purpose AMD-versus-NVIDIA cost ratio that follows from the published GPU specifications.

The same principle applies to operations. A platform that is technically compatible but requires additional maintenance, custom patches or manual recovery procedures may be more expensive to run. That effort belongs in the evaluation alongside hardware and electricity.

## Sources

These references support product specifications, public announcements and software compatibility statements. Vendor performance assertions have not been treated as independent benchmarks. Facts and plans are stated separately, and all time-sensitive claims are assessed as of 18 October 2026.

[1]TOP500, June 2022 list, Frontier's first exascale HPL result. Independent ranking and benchmark.

[2]TOP500, November 2024 highlights, El Capitan configuration and ranking. Independent ranking and benchmark.

[3]AMD Instinct MI300X specifications. Published hardware specifications.

[4]AMD accelerator specifications, including MI325X and MI350 series. Published hardware specifications.

[5]AMD Instinct MI355X specifications. Published hardware specifications.

[6]AMD, Advancing AI 2026 announcement, 23 July 2026. Launch configuration, roadmap and customer plans. Vendor announcement.

[7]NVIDIA CUDA documentationandTensorRT documentation. Vendor software documentation.

[8]AMD ROCm compatibility matrix. Hardware and software support, as published by AMD.

[9]vLLM GPU installation documentation. Project documentation on CUDA and ROCm support.

[10]AMD HIPIFY documentation. Source translation tooling and limits.

[11]Jiang et al.,Mixtral of Experts(2024). Original model research paper.

[12]AMD and OpenAI partnership announcement, 6 October 2025. Announced deployment agreement.

[13]AMD and Meta partnership announcement, 24 February 2026. Announced deployment agreement.

[14]AMD Q2 2026 financial results, 4 August 2026. Reported company and segment revenue.

[15]AMD ROCm, Scaling model training. Distributed training and parameter-efficient fine-tuning documentation.

[16]Groeneveld et al.,OLMo: Accelerating the Science of Language Models(2024). Original research paper documenting training on LUMI's AMD MI250X GPUs.

[17]AMD, Instinct MI430X at the HPC User Forum, 6 May 2026. Product positioning and source of the MI430X rendering. Vendor announcement.

Photography note:AMD'sHelios press kitincludes photographs and credits.

##### Do you really want to delete this Blog Post?

Your blog post is about to be deleted: AMD's AI Infrastructure: Instinct, Helios and the ROCm Challenge

Keep

Delete