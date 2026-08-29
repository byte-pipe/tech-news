---
title: Building an AI factory on Kubernetes | CNCF
url: https://www.cncf.io/blog/2026/08/27/building-an-ai-factory-on-kubernetes/
date: 2026-08-30
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-30T06:02:57.787406
---

# Building an AI factory on Kubernetes | CNCF

# Building an AI factory on Kubernetes | CNCF

## Overview
- An AI factory is a shared pool of GPUs that multiple teams use simultaneously for fine‑tuning, inference, and evaluation.  
- The main challenge is providing safe, isolated access to expensive accelerators while maintaining high utilization.  
- Kubernetes supplies most of the required primitives, but gaps remain for accelerator handling and tenant isolation.

## Utilization vs. Model Serving
- GPU utilization, not peak throughput, determines the economic success of an AI factory.  
- Traditional device‑plugin model pins an entire GPU to a pod, leading to low density.  
- Dynamic Resource Allocation (DRA, GA in Kubernetes 1.34) adds richer device attributes but does not slice GPUs itself.  
- Isolation is often achieved by dedicating clusters or GPU sets per team, which wastes capacity.  
- The solution is a stack that both allocates accelerators efficiently and isolates tenants securely.

## Layer‑by‑Layer Stack
| Layer | Primary Job | Typical Open‑Source Components |
|-------|--------------|--------------------------------|
| Hardware lifecycle | Provision & validate bare metal | Metal³, Ironic, Tinkerbell, Redfish, NetBox |
| Cluster lifecycle | Create/version clusters, GitOps | Cluster API, Argo CD / Flux, NVIDIA AICR |
| Node inventory | Label GPUs, NICs, MIG, topology | Node Feature Discovery, GPU & Network Operators |
| Tenant isolation | Separate teams on shared hardware | vCluster (tenant clusters), sandboxed runtimes |
| GPU allocation | Schedule accelerators, enable density | DRA, MIG, HAMi, time‑slicing, KAI Scheduler, Volcano, Kueue |
| Inference & serving | Run models behind APIs | vLLM, KServe, llm‑d |
| Batch & HPC | Run SLURM workloads | Slinky (SLURM on Kubernetes) |
| VMs | Provide virtual machines per tenant | KubeVirt |
| Gateway & autoscaling | Route & scale endpoints | Gateway API, Envoy, LiteLLM, KEDA, HPA |
| Networking | Data movement & tenant isolation | Cilium, Multus, SR‑IOV, RDMA solutions |
| Storage & data | Persist datasets, checkpoints, models | CSI, Rook/Ceph, parallel‑FS CSI, object storage |
| Observability | Monitor utilization, logs, traces | Prometheus, OpenTelemetry, DCGM exporter |
| Identity & policy | Authentication, authorization, quotas | Keycloak (OIDC), ResourceQuota/Kueue, Kyverno/OPA |
| Secrets & security | Secret management, supply‑chain security | OpenBao + External Secrets, Falco, Trivy |
| Reliability & remediation | Detect/recover node failures | DCGM health checks, Node Problem Detector, drain/cordon |
| Self‑service & billing | Tenant provisioning & chargeback | API/OpenTofu/GitOps, OpenCost, DCGM GPU‑seconds |

## From Bare Metal to Validated Capacity
- **Discovery & inventory:** Identify GPUs, memory health, NIC IDs.  
- **OS provisioning:** Network‑boot nodes with OS, GPU driver, CUDA, NCCL.  
- **BIOS tuning:** Apply baseline, performance, or confidential‑compute profiles.  
- **Burn‑in & validation:** Load tests and NCCL bandwidth checks; results stored in NetBox (IPAM).  
- **Retirement:** Securely wipe disks, reset BMC, return node to pool.  
- Open‑source alternatives (Metal³ + Ironic, vMetal) can replace vendor‑specific managers, illustrating a recurring “build vs. assemble” decision at each stack layer.

## GPU Allocation Economics
- DRA enriches device claims; fractional usage is achieved by lower‑level mechanisms.  
- **HAMi** (CNCF Incubating) enforces per‑pod memory/compute limits, allowing multiple pods on a single GPU with guardrails across vendors.  
- For confidential computing, whole‑GPU isolation per tenant is preferred; MIG provides memory/fault isolation but is debated for hostile‑tenant boundaries.  
- Scheduling responsibilities are split: KAI Scheduler & Volcano handle topology‑aware placement; Kueue manages queuing, admission, and quotas.

## Workload Layers
- **Inference:** vLLM engine + KServe (autoscaling, standard endpoints); NVIDIA Dynamo and llm‑d enable disaggregated inference at scale.  
- **Gateway:** Gateway API routes traffic; LiteLLM offers an OpenAI‑compatible front‑end for multiple models.  
- **Training & batch:** SLURM workloads run via Slinky; virtual machines for tenants via KubeVirt.  

## Takeaway
- Building an AI factory on Kubernetes is an assembly problem solved by composable, mostly CNCF‑native components.  
- The critical success factor is a stack that maximizes GPU utilization while guaranteeing tenant isolation, enabling multiple teams to share the same accelerator fleet safely and economically.