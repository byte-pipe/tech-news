---
title: Agent Substrate available on GKE | Google Cloud Blog
url: https://cloud.google.com/blog/products/containers-kubernetes/agent-substrate-available-on-gke
site_name: tldr
content_file: tldr-agent-substrate-available-on-gke-google-cloud-blog
fetched_at: '2026-09-16T21:54:45.586097'
original_url: https://cloud.google.com/blog/products/containers-kubernetes/agent-substrate-available-on-gke
date: '2026-09-16'
description: Agent Substrate is an open source, high-density agent runtime that can run scale to millions of sandboxes on a single cluster.
tags:
- tldr
---

Containers & Kubernetes

# Agent Substrate brings high-density, scalable, trusted infrastructure to GKE

September 15, 2026

##### Alex Zakonov

VP Engineering

##### Tim Hockin

Engineer

##### Try Gemini Enterprise today

The front door to AI in the workplace

Try now 

Today, we are announcing the availability of Agent Substrate on Google Kubernetes Engine (GKE).Agent Substrateis an open-source, secure-by-default agent execution runtime engineered to run millions of sandboxes with10x higher density than standard container runtimes. Purpose-built for the era of autonomous agents, Substrate deliverssub-500ms resume operationsat over500 suspend/resume activations per secondwith native zero-trust kernel and network isolation.

Agent Substrate is available as an open-source solution that runs on any Kubernetes infrastructure and is optimized for GKE. Leading AI teams are already building on it:Nous Research, the team behind theHermes Agent, is actively building on top of Agent Substrate.Hermesis currently ranked the #1 AI agent globally by OpenRouter usage across productivity, coding, CLI, and personal agents.

### From local to 1M-agent scale

Developers already run Antigravity, Claude Code, Codex, OpenClaw, Hermes, and other harnesses locally, but that’s fundamentally different than running hundreds of thousands of concurrent, long-lived agents that generate code, interact with tools, and drive automated execution — challenges that existing architectures often struggle to meet.

Scaling an agent platform from a local prototype to running agents at scale fundamentally changes your infrastructure constraints, which can include:

* Opaque trust boundaries:Models can generate and run arbitrary code on the fly. Without kernel-level isolation and dynamic network controls, running untrusted codethat no human has ever looked atrisks host escape, credential theft and data exfiltration.
* Tool access friction:Agents need full computer environments to invoke command-line tools, headless browsers, and filesystem workspaces. Running these safely needs to be fast and easy.
* Massive bursts:Agent harnesses, benchmarks, and reinforcement learning rollouts can generate thousands of sandboxes per minute. General-purpose schedulers struggle under this churn, and repeatedly decompressing container images can cause severe disk contention.
* Idle compute:Autonomous agents spend the vast majority of their time dormant while waiting on model inference, tool responses, or human feedback. Reserving dedicated CPU and RAM for idle containers wastes valuable resources.

### A substrate purpose-built for agents

When platform teams hit these challenges, they face an unacceptable trade-off: sacrifice control and isolation, or deal with the high latency and inefficiency of VMs. We believe that teams shouldn’t have to choose.

Agent Substrate avoids this by decoupling agent execution from machine management. Built on top of cloud-native Kubernetes infrastructure, Agent Substrate offers a new execution layer that’s purpose-built for agentic workloads.

From there, the execution layer directly manages the lifecycle of sandboxed agent environments with:

* Security by default:Hardware-isolated Cloud Hypervisor microVMs or gVisor sandboxes, paired with egress proxies that enforce granular network policies and inject credentials outside the reach of the agents themselves, preventing credential theft.
* Sub-second activation:Millisecond dispatch of activated agents onto pre-warmed workers, on demand, without container boot delays.
* High efficiency: Idle actors are suspended and unscheduled in hundreds of milliseconds, freeing up compute resources.
* Open source and portable:Runs on any Kubernetes cluster in any compute environment and works with any agent framework or harness, including Claude Code, OpenClaw, and Hermes.

### Core architectural principles

We adhere to four core architectural principles to guide how Agent Substrate solves these challenges:

#### 1. Secure by default at the kernel and the network

AI agents generate and run untrusted code and terminal commands as a core function. Running that code on a shared server creates serious risks for breakouts and unintended data leakage either at the shared kernel or network level.

Agent Substrate takes a secure by default position for both the host kernel and network layers. Teams can choose between hardware-isolated Cloud Hypervisor microVMs, which provides full Linux kernel compatibility, or gVisor sandboxing, with even lower-overhead kernel isolation. Agent Substrate’s integrated gateway manages all egress and ingress requests, enabling fine-grained and extensible control over network access.

#### 2. A control plane and data plane built for low-latency activation

To optimize density for isolated, long-running agent workloads, you need a purpose-built control plane and data plane that enables the lowest possible latency and the highest possible rate of suspend and resume operations. Agent Substrate introduces a dedicated control plane that handles data-aware scheduling with minimal latency. Meanwhile, the data plane handles hundreds of suspend/resume operations per second directly on pre-warmed workers, reducing the overhead of preparing the environment. Snapshots are written to local disk and Google Cloud Storage for durable state persistence. In less than 500ms, a sandboxed environment can be resumed to its previous state, and immediately re-suspended once it’s idle again.

#### 3. High-density and active-only compute economics

Agents spend most of their time waiting on model inference, tool responses, or user input. Reserving physical CPUs and RAM for idle containers can lock up expensive and scarce capacity and make running agent fleets at scale unsustainable.

Agent Substrate can release resources the moment an agent pauses. It snapshots the guest hypervisor’s state to the local disk and Cloud Storage, freeing up RAM and CPU to run other agents, while keeping the state intact. When the next turn or tool call arrives, Agent Substrate resumes the snapshotted session in milliseconds. This zero-idle model can pack over 1,000 dormant agents per host, delivering 10x higher compute density than traditional compute. For workloads that need shared filesystems across turns, an optionalFilestoreagent volume controller provides persistent NFS storage — more on that below.

#### 4. Kubernetes as a foundation: scale and reliability

Building a custom sandbox orchestrator on standard VMs forces teams to maintain tedious operational tooling: node recovery, autoscaling, multi-zone scheduling, and network policy. But routing each sub-second tool invocation through the standard Kubernetes Pod lifecycle adds seconds of delay to each request.

Agent Substrate combines both approaches. The high-frequency suspend-resume runs directly on local workers through a purpose-built data plane. Meanwhile, Kubernetes manages the machines, handling self-healing nodes, fleet autoscaling, and cluster reliability, as well as drives the lifecycle of the worker pods themselves. For workloads that need standard Pod semantics, existing primitives like Agent Sandbox and kernel-isolated Pods continue to work side by side.

### Optimized for Google Cloud infrastructure

Building an agent platform that can achieve 1M agent scale depends on having the right underlying compute and storage infrastructure. Agent Substrate on GKE maximizes machine obtainability and flexibility withcustom ComputeClassesto dynamically manage machine pools across shapes and families, including spot and on-demand pools. This includes native support for Google Axion, our custom Arm-based processors, which deliver up to 30% better price-performance for sandbox workloads compared to competitive cloud offerings. For stateful workspaces, Agent Substrate on GKE can be optionally integrated withFilestore agent volumes, a new offering that attaches and detaches NFS mounts in milliseconds, allowing agents to start/resume near-instantaneously, along with native Read-Write-Many (RWX) access and POSIX-compliant file locking to enable safe multi-agent collaboration without write collisions.

### Build your agent platform on a scalable foundation

When building production agent applications, you shouldn’t have to compromise between strong security, low latency, and operational scale.

Nous Research builds Hermes, the number-one AI agent in the world by usage according to OpenRouter, where it also ranks first in productivity, coding, personal and CLI agents. Nous Research has been an early design partner on Agent Substrate, evaluating how the runtime handles the isolation and identity requirements that agent workloads introduce.

“We built Hermes Enterprise to enable customers to deploy into their existing infrastructure, while handling per-agent isolation and extensible access control. Agent Substrate addresses both at the platform layer in a way that also preserves valuable compute resources. Our experience with Agent Substrate gives us confidence the architecture can scale efficiently as agent workloads grow.”- Hervé Bizira, Chief Business Officer, Nous Research

By pairing the machine resilience, self-healing nodes, and declarative management of Kubernetes with an agent-native data plane built for kernel isolation, active-only compute, and sub-second execution, Agent Substrate gives engineering teams a clear path to scale.

Agent Substrate is open source and available to all GKE customers for non-production workloads. GA support for production is available via allowlist. To deploy it on your GKE clusters, seeAgent Substrate on GKE documentation. To learn more, see About Agent Substrate or visit theopen-source repository.

Posted in
* Containers & Kubernetes

##### Related articles

Containers & Kubernetes

### For SeaVerse, GKE Agent Sandbox reduces infrastructure costs by 60%

By Zongyun Hu • 5-minute read

AI infrastructure

### What’s new in AI infrastructure and orchestration in August

By Alex Barrett • 13-minute read

Containers & Kubernetes

### Bringing gVisor sandboxes to distributed Ray clusters

By Andrew Sy Kim • 3-minute read

Networking

### ClusterNetworkPolicy in GKE: Balancing control and autonomy for your microservices

By Srini Jasti • 4-minute read