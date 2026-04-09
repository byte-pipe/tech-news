---
title: 'Compiling LLMs into a MegaKernel: A Path to Low-Latency Inference | by Zhihao Jia | Jun, 2025 | Medium'
url: https://zhihaojia.medium.com/compiling-llms-into-a-megakernel-a-path-to-low-latency-inference-cf7840913c17
site_name: hackernews
fetched_at: '2025-06-20T13:26:05.335743'
original_url: https://zhihaojia.medium.com/compiling-llms-into-a-megakernel-a-path-to-low-latency-inference-cf7840913c17
author: Zhihao Jia
date: '2025-06-20'
published_date: '2025-06-20T02:28:52.338Z'
description: 'TL;DR: We developed a compiler that automatically transforms LLM inference into a single megakernel — a fused GPU kernel that performs all necessary computation and communication in one launch. This…'
---

# Compiling LLMs into a MegaKernel: A Path to Low-Latency Inference

Zhihao Jia
Follow
7 min read
·
1 day ago

--

Listen

Share

TL;DR:We developed a compiler that automatically transforms LLM inference into a single megakernel — a fused GPU kernel that performs all necessary computation and communication in one launch. This end-to-end GPU fusion approach reduces LLM inference latency by 1.2-6.7x. Our compiler is easy to use — you can compile your LLM into a high-performance megakernel with just a few dozen lines of Python.

What’s the key idea?Traditional LLM systems often rely on sequences of GPU kernel launches and external communication calls, resulting in underutilized hardware. Our compiler automatically fuses these operations — spanning multiple layers, iterations, and GPUs — into a megakernel. This design eliminates launch overhead, enables fine-grained software pipelining, and overlaps computation with communication across GPUs.

Team members:Xinhao Cheng,Bohan Hou,Yingyi Huang,Jianan Ji,Jinchen Jiang,Hongyi Jin,Ruihang Lai,Shengjie Lin,Xupeng Miao,Gabriele Oliaro,Zihao Ye,Zhihao Zhang,Yilong Zhao,Tianqi Chen,Zhihao Jia

Software:https://github.com/mirage-project/mirage/tree/mpk

One of the most effective ways to reduce latency in LLM inference is to fuse all computation and communication into a singlemegakernel—also known as apersistent kernel. In this design, the system launches justoneGPU kernel to execute the entire model — from layer-by-layer computation to inter-GPU communication — without interruption. This approach offers several key performance advantages:

1. Eliminates kernel launch overhead, even in multi-GPU settings,by avoiding repeated kernel invocations;
2. Enables software pipeliningacross layers, allowing the kernel to begin loading data for the next layer while computing the current one;
3. Overlaps computation and communication, as a megakernel can simultaneously execute compute operations and inter-GPU communication to hide latency.

Despite these advantages, compiling an LLM into a megakernel is highly challenging. Existing high-level ML frameworks — such asPyTorch,Triton, andTVM— do not natively support end-to-end megakernel generation. Additionally, modern LLM systems are built from a diverse collection of specialized kernel libraries:NCCLorNVSHMEMfor communication,FlashInferorFlashAttentionfor efficient attention, and CUDA orTritonfor custom computation. This fragmentation makes it difficult to consolidate the entire inference pipeline into a single, unified kernel.

Can we automate this process through compilation?Motivated by this question, our team from CMU, UW, Berkeley, NVIDIA, and Tsinghua developedMirage Persistent Kernel(MPK)— a compiler and runtime system that automatically transforms multi-GPU LLM inference into a high-performance megakernel. MPK unlocks the benefits of end-to-end GPU fusion while requiring minimal manual effort from developers.

# Why MPK?

A key advantage of MPK is extremely low latency for LLM inference by eliminating kernel launch overhead and maximally overlapping computation, data loading, and inter-GPU communication across layers.

Figure 1. Comparing LLM decoding latency between MPK and existing systems. We used a 39-token prompt and generated 512 tokens without speculative decoding.

Figure 1 illustrates a performance comparison between MPK and existing LLM inference systems on both single- and multi-GPU configurations. On a single NVIDIA A100 40GB GPU, MPK reduces per-token decoding latency from14.5 ms— as achieved by optimized systems like vLLM and SGLang — to12.5 ms, approaching the theoretical lower bound of10 ms(based on loading 16 GB of weights with 1.6 TB/s memory bandwidth).

Beyond single-GPU optimization, MPK fuses computation and inter-GPU communication into a single megakernel. This design enables MPK to maximally overlap computation and communication. As a result, the performance improvements of MPK over current systemsincrease with the number of GPUs, making it particularly effective for multi-GPU deployments.

# What’s Next?

The rest of this blog dives deeper into how MPK works:

* Part 1introduces theMPK compiler, which transforms an LLM’s computation graph into an optimized task graph;
* Part 2covers theMPK runtime, which executes this task graph within a megakernel to achieve high throughput and low latency.

# Part 1. The Compiler: Transforming an LLM into a Fine-Grained Task Graph

The computation performed by a large language model (LLM) is typically represented as acomputation graph, where each node corresponds to a compute operation (e.g., matrix multiplication, attention) or a collective communication primitive (e.g., all-reduce), and edges denote data dependencies between operations. In existing systems, each operator is generally executed via a dedicated GPU kernel. However, thiskernel-per-operator execution modeloften fails to exploit pipelining opportunities, since dependencies are enforced at a coarse granularity — across entire kernels — rather than the actual data units.

Consider a typical example: an allreduce operation following a matrix multiplication. In existing kernel-per-operator systems, the allreduce kernel must wait until the entire matmul kernel completes. In reality, though, each chunk of data for the allreduce only depends on a portion of the matmul output. This mismatch between logical and actual data dependencies limits the potential for overlapping computation and communication.

Figure 2. The MPK compiler transforms an LLM’s computation graph (defined in PyTorch) into an optimized, fine-grained task graph that exposes maximum parallelism. The right-hand side illustrates an alternative — but suboptimal — task graph that introduces unnecessary data dependencies and global barriers, limiting pipelining opportunities across layers.

To address this issue, MPK introduces a compiler that automatically transforms the LLM’s computation graph into a fine-grainedtask graph. This task graph explicitly captures dependencies at the sub-kernel level, enabling more aggressive pipelining across layers.

In an MPK task graph:

* Eachtask(shown as a rectangle in Figure 2) represents a unit of computation or communication assigned to a single GPU streaming multiprocessor (SM).
* Eachevent(shown as a circle) represents a synchronization point between tasks.
* Each task has an outgoing edge to atriggering event, which is activated once all associated tasks complete.
* Each tasks also has an incoming edge from adependent event, indicating the task can start execution as soon as the event is activated.

Task graphs allow MPK to uncover pipelining opportunities that would be missed in computation graphs. For example, MPK can construct an optimized task graph where each allreduce task depends only on the corresponding matmul task that produces its input — enabling partial execution and overlap.

In addition to generating an optimized task graph, MPK also automatically generateshigh-performance CUDA implementationsfor each task using theMirage kernel superoptimizer. This ensures that each task runs efficiently on a GPU SM. (For more about the kernel superoptimizer, seethis post.)

# Part 2. The Runtime: Executing a Task Graph in a MegaKernel

MPK includes an on-GPU runtime system thatexecutes the task graph entirely within a single GPU megakernel, allowing for fine-grained control over task execution and scheduling without any kernel launches during inference.

To achieve this, MPK statically partitions all streaming multiprocessors (SMs) on a GPU into two roles:workersandschedulers. The number of worker and scheduler SMs is fixed at kernel launch time and matches the total number of physical SMs, avoiding any dynamic context switching overhead.

## Workers

Eachworkeroperates on an SM and maintains a dedicated task queue. It follows a simple but efficient execution loop:

1. Fetch the next task from its queue.
2. Execute the task (e.g., matrix multiplication, attention, or inter-GPU data transfers).
3. Notify the triggering event upon task completion.
4. Repeat.

This design ensures that workers remain fully utilized while enabling task execution to proceed asynchronously across layers and operations.

## Schedulers

Scheduling decisions are handled by MPK’sdistributed schedulers, each of which runs on asingle warp. Because each SM can accommodate multiple warps, up to four schedulers can run concurrently per SM. Each scheduler maintains a queue of activated events. It continuously:

1. Dequeues activated events whose dependencies are satisfied (i.e., all prerequisite tasks have completed).
2. Launches the set of tasks that depend on the activated event.

This decentralized scheduling mechanism minimizes coordination overhead while enabling scalable execution across SMs.

Figure 3. The MPK runtime executes a task graph in a megakernel.

## Event-Driven Execution

Figure 3 illustrates MPK’s execution timeline. Each rectangle represents a task running on a worker; each circle represents an event. As a task completes, it increments the counter for its corresponding triggering event. When the event counter reaches a pre-defined threshold, the event is considered activated and is enqueued into a scheduler’s event queue. The scheduler then launches any downstream tasks that depend on this event.

This design allows forfine-grained software pipeliningandoverlap between computation and communication. For example:

* Matmul tasks can execute in parallel with attention tasks from different layers.
* Allreduce communication can begin as soon as partial matmul results are available.

Because all scheduling and task transitions occur within a single kernel context,the overhead between tasks is extremely low— typically just1–2 microseconds— enabling efficient execution of multi-layer, multi-GPU LLM workloads.

# Looking Forward

Our vision for MPK is to makemegakernel compilation both easy to use and highly performant. Currently you can compile an LLM into a megakernel with just a few dozen lines of Python code — mainly to specify the megakernel’s inputs and outputs. We’re excited about this direction, and there’s still much more to explore. Some of the key areas we’re actively working on include:

* Support for modern GPU architectures.One of our next milestones is extending MPK to support next-generation architectures such asNVIDIA Blackwell. A major challenge lies in integrating warp specialization — a key optimization for newer GPUs — with MPK’s megakernel execution model.
* Handling workload dynamism.MPK currently builds a static task graph, which limits its ability to handle dynamic workloads such asmixture-of-experts (MoE)models. We’re developing new compilation strategies that allow MPK to support dynamic control flow and conditional execution inside megakernels.
* Advanced scheduling and task assignment:MPK unlocks a new level offine-grained schedulingat the task level. While our current implementation uses simple round-robin scheduling to distribute tasks across SMs, we see exciting opportunities inadvanced scheduling policies— such as priority-aware or throughput-optimized strategies — for use cases like latency-SLO-driven serving or hybrid batching.

We believe MPK represents a foundational shift in how LLM inference workloads are compiled and executed on GPUs, and we’re eager to collaborate with the community to push this vision forward.

# Want to Learn More?

To learn more about MPK and explore our code and documentation, please visit our project website:https://github.com/mirage-project/mirage.

We welcome feedback, contributions, and collaborations from the community!
