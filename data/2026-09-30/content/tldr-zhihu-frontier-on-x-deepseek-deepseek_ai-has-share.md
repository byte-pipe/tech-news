---
title: 'Zhihu Frontier on X: "DeepSeek @deepseek_ai has shared a new technical article on Zhihu introducing DeepSeek Elastic Compute (DSec), the sandbox infrastructure behind its large-scale Agent workloads. From DeepSeek-V3.2 to V4.1, DSec has handled all sandbox workloads for Agent training, evaluation… / X'
url: https://x.com/zhihufrontier/status/2104889429345354180
site_name: tldr
content_file: tldr-zhihu-frontier-on-x-deepseek-deepseek_ai-has-share
fetched_at: '2026-09-30T06:00:34.046611'
original_url: https://x.com/zhihufrontier/status/2104889429345354180
date: '2026-09-30'
published_date: '2026-09-29T11:02:01.000Z'
description: DeepSeek @deepseek_ai has shared a new technical article on Zhihu introducing DeepSeek Elastic Compute (DSec), the sandbox infrastructure behind its large-scale Agent workloads. From DeepSeek-V3.2 to V4.1, DSec has handled all sandbox workloads for Agent training, evaluation, and data preprocessi…
tags:
- tldr
---

## Post

Log in
Sign up

## Post

Log in
Sign up

# Zhihu Frontier on X: "DeepSeek @deepseek_ai has shared a new technical article on Zhihu introducing DeepSeek Elastic Compute (DSec), the sandbox infrastructure behind its large-scale Agent workloads.

From DeepSeek-V3.2 to V4.1, DSec has handled all sandbox workloads for Agent training, evaluation, and data preprocessing. In production, it runs across thousands of servers, with millions of sandboxes running concurrently. Its overcommit ratio has exceeded 50×, pushing CPU and memory utilization to the limit.

So how does DSec support Agent workloads at this scale?

Below is the full article, covering the architecture and engineering behind DSec—from composable environments and on-demand image loading to high-density resource management, rollout recovery, and Agent security.

📖 DeepSeek Elastic Compute (DSec): Sandbox Infrastructure for Large-Scale Agent Training

DeepSeek Elastic Compute (DSec) is the sandbox infrastructure supporting the entire training, evaluation, and data preprocessing pipeline of DeepSeek-V4.

Training a reliable Agent model requires repeated trial and error in real environments: reading code, modifying files, installing dependencies, running tests, and launching services. These operations continuously change the environment, so sandboxes must persist state across multiple rounds of interaction.

These workloads have several distinct characteristics: sandbox creation requests are bursty; CPUs remain mostly idle after startup while memory needs to stay resident; Agent environments are highly diverse with low base-image reuse; and long-running tasks can be interrupted by resource preemption. These characteristics directly shape the design of DSec.

Unified Access for Diverse Workloads

Different Agent tasks require different levels of isolation, operating system functionality, and execution overhead. DSec supports four execution backends—FnCall, Container, MicroVM, and Full VM—all accessed through a unified Python SDK, libdsec, with the backend selected according to the task.

FnCall reuses pre-created containers for short tasks such as online evaluation. Container provides fast startup and high deployment density for general software engineering and tool use. MicroVM offers stronger isolation for security-sensitive tasks. Full VM provides a complete operating system environment, supporting applications such as graphical interfaces, rendering, and Android.

DSec architecture: unified sandbox creation and runtime management, with multiple execution backends for different workloads.

Layered and Composable Environments

Large-scale Agent training requires a large number of environments, making efficient environment construction and updates a fundamental challenge.

In one week of production data from 2026, the container backend used 11,266 base images, 102,171 workspaces, and hundreds of toolkits. Under a traditional approach, updating any of these components would require rebuilding a large number of images.

DSec therefore separates each sandbox environment into three layers:
🔹 Base image — the operating system and basic software
🔹 Workspace — task-specific code repositories and dependencies
🔹 Toolkit — tools such as DeepSeek Harness
These layers have different update cycles and are versioned independently, then composed at runtime.

DSec stores images, workspaces, and toolkits in EROFS, which supports metadata/data separation and cross-image deduplication. When creating a sandbox, OverlayFS combines the required EROFS layers on demand.

When base software, task code, or toolkits change, only the corresponding EROFS layer needs to be rebuilt, avoiding unnecessary reconstruction of unrelated content.

Monolithic images require rebuilding every image containing an updated toolkit. With composable environment layers, only the toolkit layer needs to be updated and recombined with existing base images and workspaces.

On-Demand Image Loading

Analysis of production image data showed that sandboxes actually access only 4.2%–13.3% of the total image data at runtime. Pulling complete images locally therefore means transferring and storing a large amount of unused data.

DSec instead stores all image data on the 3FS distributed file system, fetching only the required metadata locally and reading the bulk data on demand.

In an experiment creating 8,192 containers simultaneously, on-demand loading reduced completion time from more than 60 minutes to about 35 minutes, achieving a 1.71× speedup and reducing disk writes by approximately 57%.

In another workspace provisioning experiment, directly mounting EROFS layers instead of extracting tar.gz files reduced completion time from 79 minutes to 45 minutes, while total disk writes fell to roughly 1/5.5 of the original.

High-Density Resource Management

Agent training workloads spend much of their time waiting for the model to generate the next action. Around 90% of sandboxes use no more than 5% of their requested CPU capacity on average, leaving CPU idle for long periods while memory must remain resident to preserve files, processes, and other state.

This creates significant room for overcommitment. In production, DSec achieves an overcommit ratio of more than 50×.

To support high-density deployment, DSec focuses on cache sharing and reclaiming idle memory.

Using virtio-pmem and DAX, MicroVMs on the same host can share a host page cache. In experiments, enabling this mechanism alone reduced peak host memory usage by 40.2% compared with the baseline.

Enabling memory reclamation mechanisms—DAMON and balloon free-page reporting—reduced time-accumulated host memory consumption by 21.2%. Combining the two mechanisms resulted in the lowest overall memory consumption.

Under such high-density deployment, DSec also prioritizes latency-sensitive tasks, allowing less latency-sensitive workloads to utilize idle CPU capacity, while reducing interference from hyperthreads sharing the same physical core.

With optimized CPU scheduling, when other workloads consumed 50% of node CPU capacity, the latency increase of latency-sensitive tasks over the no-interference baseline fell from 45.2% to 17.3%.

Three core mechanisms: on-demand image loading, composable environment layers, and high-density resource management.

Decoupling Rollouts from GPU Training

In reinforcement learning (RL), Agents typically need multiple rounds of interaction with sandbox environments to complete a rollout.

In early training pipelines, the Agent execution loop and GPU training task ran in the same Pod. When the training task was preempted, the sandbox remained intact, but the Agent execution loop responsible for advancing the interaction had already terminated.

Recovery required replaying command logs to reconcile the progress saved by the training framework with the actual state of the sandbox, creating complex recovery logic and additional coordination overhead.

Starting with DeepSeek-V4.1, this execution logic was moved into DSec and split between an Agent sandbox and a worker container.

The Agent sandbox runs the Agent framework and toolkits, while the worker container manages the sandbox and advances the interaction process. Both run outside the preemptible GPU resource pool and jointly preserve execution progress and environment state.

As a result, when a GPU training task is preempted, the Agent's execution state remains intact. Once training resumes, the Agent can continue directly from where it was interrupted.

Using Agents to Build Environments for Agents

Large-scale Agent RL training and evaluation require highly diverse environments, including binary dependencies, code repositories, Harness toolkits, evaluation scripts, and other components used to generate Agent outputs and measure their correctness.

Using Agents to automate environment construction provides an efficient and scalable way to build these environments.

An important observation is that the Agent building an environment is itself already running inside the environment it is building. Rather than maintaining one platform for Agent training and another for environment construction, DSec puts both on the same “platform for running Agents”, greatly simplifying the system architecture while ensuring that the Agent's build and runtime environments remain identical.

DSec introduces a pack_diff mechanism for environment construction. Agents can instruct the platform to create incremental snapshots of a sandbox and later restore them as new sandboxes.

This makes it easy to preserve sandbox state—and even turn every round of Agent interaction into a reusable sandbox environment.

These incremental snapshots can also support trajectory branching: save a snapshot at step k, restore multiple sandboxes from the same state, and continue exploration independently. Each branch shares read-only layers while recording only its changes, avoiding repeated execution of steps before the branch point.

MicroVM snapshots can preserve and restore memory and process state, while the container implementation currently supports primarily disk-level snapshots.

Security Boundaries for Agents

As Agent capabilities improve, the security boundaries of training environments also need to evolve.

In production, DSec has observed Agents attempting to read residual answers, forge RPC requests, overwrite /bin/bash to inject commands, and even bypass access controls through mechanisms such as XFS_IOC_SWAPEXT.

Such behavior can affect training and evaluation results, and potentially damage the runtime environment.

If an environment provides a shortcut to obtaining rewards, models may exploit it. DSec therefore treats fine-grained access control as a fundamental capability.

AppArmor constrains file and socket access, with these restrictions remaining effective even when the Agent runs with administrator privileges. eBPF provides per-sandbox network allowlists, restricting the addresses, ports, and protocols that a sandbox can access.

These measures can only mitigate part of the problem. There is still no general defense against destructive behaviors such as exploiting kernel vulnerabilities.

As model capabilities continue to improve, the security arms race between systems and Agents will likely continue, with system defenses evolving alongside them.

Production Data

DSec scales horizontally through shards. Each shard contains around 160 servers, providing approximately 30,000 CPU cores and 250 TB of memory.

A single shard serves around 3 million sandboxes per day, with peak concurrency exceeding 380,000 sandboxes and a creation rate of more than 5,000 sandboxes per second.

Multiple such shards are deployed in production, supporting millions of sandboxes running simultaneously.

From DeepSeek-V3.2 to DeepSeek-V4.1, DSec has handled all sandbox workloads for Agent training, evaluation, and data preprocessing.

The DSec technical report, “DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale,” is now available on arXiv, sharing the engineering practices behind large-scale Agent sandbox infrastructure.

Conclusion

We believe Agents still have enormous room for exploration.

Next, we plan to expand the number and diversity of Agent runtime environments by hundreds or thousands of times, and bring the capabilities developed through these tasks back into open models.

This requires more diverse environments, more reliable infrastructure, and more development partners.

Join us in building an elastic computing platform for Agents and the next generation of Agent foundation models.

How to Apply

Apply through the DeepSeek careers website by searching for “Agent Elastic Computing R&D Engineer.”

Or send your resume to[email protected]with the email subject: Name – Position – Contact Information.

Data from the DeepSeek Elastic Compute technical report, “DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale.”

#DeepSeek #AI #Tech"

Zhihu Frontier
@ZhihuFrontier
DeepSeek 
@
deepseek_ai
 has shared a new technical article on Zhihu introducing DeepSeek Elastic Compute (DSec), the sandbox infrastructure behind its large-scale Agent workloads.

From DeepSeek-V3.2 to V4.1, DSec has handled all sandbox workloads for Agent training, evaluation, and data preprocessing. In production, it runs across thousands of servers, with millions of sandboxes running concurrently. Its overcommit ratio has exceeded 50×, pushing CPU and memory utilization to the limit.

So how does DSec support Agent workloads at this scale?

Below is the full article, covering the architecture and engineering behind DSec—from composable environments and on-demand image loading to high-density resource management, rollout recovery, and Agent security.

📖 DeepSeek Elastic Compute (DSec): Sandbox Infrastructure for Large-Scale Agent Training

DeepSeek Elastic Compute (DSec) is the sandbox infrastructure supporting the entire training, evaluation, and data preprocessing pipeline of DeepSeek-V4.

Training a reliable Agent model requires repeated trial and error in real environments: reading code, modifying files, installing dependencies, running tests, and launching services. These operations continuously change the environment, so sandboxes must persist state across multiple rounds of interaction.

These workloads have several distinct characteristics: sandbox creation requests are bursty; CPUs remain mostly idle after startup while memory needs to stay resident; Agent environments are highly diverse with low base-image reuse; and long-running tasks can be interrupted by resource preemption. These characteristics directly shape the design of DSec.

Unified Access for Diverse Workloads

Different Agent tasks require different levels of isolation, operating system functionality, and execution overhead. DSec supports four execution backends—FnCall, Container, MicroVM, and Full VM—all accessed through a unified Python SDK, libdsec, with the backend selected according to the task.

FnCall reuses pre-created containers for short tasks such as online evaluation. Container provides fast startup and high deployment density for general software engineering and tool use. MicroVM offers stronger isolation for security-sensitive tasks. Full VM provides a complete operating system environment, supporting applications such as graphical interfaces, rendering, and Android.

DSec architecture: unified sandbox creation and runtime management, with multiple execution backends for different workloads.

Layered and Composable Environments

Large-scale Agent training requires a large number of environments, making efficient environment construction and updates a fundamental challenge.

In one week of production data from 2026, the container backend used 11,266 base images, 102,171 workspaces, and hundreds of toolkits. Under a traditional approach, updating any of these components would require rebuilding a large number of images.

DSec therefore separates each sandbox environment into three layers:
🔹 Base image — the operating system and basic software
🔹 Workspace — task-specific code repositories and dependencies
🔹 Toolkit — tools such as DeepSeek Harness
These layers have different update cycles and are versioned independently, then composed at runtime.

DSec stores images, workspaces, and toolkits in EROFS, which supports metadata/data separation and cross-image deduplication. When creating a sandbox, OverlayFS combines the required EROFS layers on demand.

When base software, task code, or toolkits change, only the corresponding EROFS layer needs to be rebuilt, avoiding unnecessary reconstruction of unrelated content.

Monolithic images require rebuilding every image containing an updated toolkit. With composable environment layers, only the toolkit layer needs to be updated and recombined with existing base images and workspaces.

On-Demand Image Loading

Analysis of production image data showed that sandboxes actually access only 4.2%–13.3% of the total image data at runtime. Pulling complete images locally therefore means transferring and storing a large amount of unused data.

DSec instead stores all image data on the 3FS distributed file system, fetching only the required metadata locally and reading the bulk data on demand.

In an experiment creating 8,192 containers simultaneously, on-demand loading reduced completion time from more than 60 minutes to about 35 minutes, achieving a 1.71× speedup and reducing disk writes by approximately 57%.

In another workspace provisioning experiment, directly mounting EROFS layers instead of extracting tar.gz files reduced completion time from 79 minutes to 45 minutes, while total disk writes fell to roughly 1/5.5 of the original.

High-Density Resource Management

Agent training workloads spend much of their time waiting for the model to generate the next action. Around 90% of sandboxes use no more than 5% of their requested CPU capacity on average, leaving CPU idle for long periods while memory must remain resident to preserve files, processes, and other state.

This creates significant room for overcommitment. In production, DSec achieves an overcommit ratio of more than 50×.

To support high-density deployment, DSec focuses on cache sharing and reclaiming idle memory.

Using virtio-pmem and DAX, MicroVMs on the same host can share a host page cache. In experiments, enabling this mechanism alone reduced peak host memory usage by 40.2% compared with the baseline.

Enabling memory reclamation mechanisms—DAMON and balloon free-page reporting—reduced time-accumulated host memory consumption by 21.2%. Combining the two mechanisms resulted in the lowest overall memory consumption.

Under such high-density deployment, DSec also prioritizes latency-sensitive tasks, allowing less latency-sensitive workloads to utilize idle CPU capacity, while reducing interference from hyperthreads sharing the same physical core.

With optimized CPU scheduling, when other workloads consumed 50% of node CPU capacity, the latency increase of latency-sensitive tasks over the no-interference baseline fell from 45.2% to 17.3%.

Three core mechanisms: on-demand image loading, composable environment layers, and high-density resource management.

Decoupling Rollouts from GPU Training

In reinforcement learning (RL), Agents typically need multiple rounds of interaction with sandbox environments to complete a rollout.

In early training pipelines, the Agent execution loop and GPU training task ran in the same Pod. When the training task was preempted, the sandbox remained intact, but the Agent execution loop responsible for advancing the interaction had already terminated.

Recovery required replaying command logs to reconcile the progress saved by the training framework with the actual state of the sandbox, creating complex recovery logic and additional coordination overhead.

Starting with DeepSeek-V4.1, this execution logic was moved into DSec and split between an Agent sandbox and a worker container.

The Agent sandbox runs the Agent framework and toolkits, while the worker container manages the sandbox and advances the interaction process. Both run outside the preemptible GPU resource pool and jointly preserve execution progress and environment state.

As a result, when a GPU training task is preempted, the Agent's execution state remains intact. Once training resumes, the Agent can continue directly from where it was interrupted.

Using Agents to Build Environments for Agents

Large-scale Agent RL training and evaluation require highly diverse environments, including binary dependencies, code repositories, Harness toolkits, evaluation scripts, and other components used to generate Agent outputs and measure their correctness.

Using Agents to automate environment construction provides an efficient and scalable way to build these environments.

An important observation is that the Agent building an environment is itself already running inside the environment it is building. Rather than maintaining one platform for Agent training and another for environment construction, DSec puts both on the same “platform for running Agents”, greatly simplifying the system architecture while ensuring that the Agent's build and runtime environments remain identical.

DSec introduces a pack_diff mechanism for environment construction. Agents can instruct the platform to create incremental snapshots of a sandbox and later restore them as new sandboxes.

This makes it easy to preserve sandbox state—and even turn every round of Agent interaction into a reusable sandbox environment.

These incremental snapshots can also support trajectory branching: save a snapshot at step k, restore multiple sandboxes from the same state, and continue exploration independently. Each branch shares read-only layers while recording only its changes, avoiding repeated execution of steps before the branch point.

MicroVM snapshots can preserve and restore memory and process state, while the container implementation currently supports primarily disk-level snapshots.

Security Boundaries for Agents

As Agent capabilities improve, the security boundaries of training environments also need to evolve.

In production, DSec has observed Agents attempting to read residual answers, forge RPC requests, overwrite /bin/bash to inject commands, and even bypass access controls through mechanisms such as XFS_IOC_SWAPEXT.

Such behavior can affect training and evaluation results, and potentially damage the runtime environment.

If an environment provides a shortcut to obtaining rewards, models may exploit it. DSec therefore treats fine-grained access control as a fundamental capability.

AppArmor constrains file and socket access, with these restrictions remaining effective even when the Agent runs with administrator privileges. eBPF provides per-sandbox network allowlists, restricting the addresses, ports, and protocols that a sandbox can access.

These measures can only mitigate part of the problem. There is still no general defense against destructive behaviors such as exploiting kernel vulnerabilities.

As model capabilities continue to improve, the security arms race between systems and Agents will likely continue, with system defenses evolving alongside them.

Production Data

DSec scales horizontally through shards. Each shard contains around 160 servers, providing approximately 30,000 CPU cores and 250 TB of memory.

A single shard serves around 3 million sandboxes per day, with peak concurrency exceeding 380,000 sandboxes and a creation rate of more than 5,000 sandboxes per second.

Multiple such shards are deployed in production, supporting millions of sandboxes running simultaneously.

From DeepSeek-V3.2 to DeepSeek-V4.1, DSec has handled all sandbox workloads for Agent training, evaluation, and data preprocessing.

The DSec technical report, “DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale,” is now available on arXiv, sharing the engineering practices behind large-scale Agent sandbox infrastructure.

Conclusion

We believe Agents still have enormous room for exploration.

Next, we plan to expand the number and diversity of Agent runtime environments by hundreds or thousands of times, and bring the capabilities developed through these tasks back into open models.

This requires more diverse environments, more reliable infrastructure, and more development partners.

Join us in building an elastic computing platform for Agents and the next generation of Agent foundation models.

How to Apply

Apply through the DeepSeek careers website by searching for “Agent Elastic Computing R&D Engineer.”

Or send your resume to 
[email protected]
 with the email subject: Name – Position – Contact Information.

Data from the DeepSeek Elastic Compute technical report, “DeepSeek Elastic Compute (DSec): A Sandbox Infrastructure for Effective Agentic Training at Scale.”

#DeepSeek
 
#AI
 
#Tech
11:02 AM · Sep 29, 2026
·
4,425
Views
8
8
15
1
5
108
1
0
8
74
7
4