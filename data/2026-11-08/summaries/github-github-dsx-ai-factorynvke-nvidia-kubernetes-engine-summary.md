---
title: GitHub - dsx-ai-factory/nvke: NVIDIA Kubernetes Engine (NVKE). A management plane for GPU Kubernetes on bare metal. · GitHub
url: https://github.com/dsx-ai-factory/nvke
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:03:54.896918
---

# GitHub - dsx-ai-factory/nvke: NVIDIA Kubernetes Engine (NVKE). A management plane for GPU Kubernetes on bare metal. · GitHub

# NVIDIA Kubernetes Engine (NVKE)

## What NVKE is
- Management plane for running Kubernetes clusters on NVIDIA GPU bare‑metal infrastructure.  
- Not a Kubernetes distribution; it creates independent workload clusters, each with its own control plane, etcd, and node pools.  
- Operated by platform teams; customers access clusters via the standard Kubernetes API and `kubectl`.

## Preview status
- Available as a preview; APIs, configuration, and behavior may change.  
- Not recommended for production workloads.  
- Known limitations are documented.

## Getting started
- **Local quickstart**: development management plane and simulated workload cluster. Runs on Linux (amd64 or arm64) with ≥6 CPU, 12 GiB RAM, 100 GiB disk, Docker, virtual TPM. macOS uses a Colima VM.  
- **Real installation**: supply machines, networking, node images, and registries; configure access to NVIDIA Infra Controller (NICo), the only supported infrastructure provider in preview.

## Core capabilities
- **Provision clusters**: request clusters via NVKE API or `nvkectl`; NICo provisions machines and forms Kubernetes clusters.  
- **Lifecycle management**: create, scale, delete node pools; upgrade Kubernetes; replace nodes (subject to preview limits).  
- **Node identity**: attestation through SPIFFE/SPIRE using TPM; optional etcd encryption per cluster.  
- **Build integration**: works with NVIDIA Kubernetes Recipes (NVKR) to build node images and NVKE components.

## Architecture overview
- Two Kubernetes cluster types:
  1. **Management cluster** runs the NVKE management plane and infrastructure controllers; created from a temporary seed cluster using `nvkectl`.  
  2. **Workload clusters** host customer applications; managed via NICo, Cluster API, and node agents.  
- Diagram (not shown) illustrates product family, NICo, GPU machines, and component interactions.

## Building from source
- Requires Go 1.27.3 (pinned), GNU Make 4+, optional Flox for dev tools.  
- Build steps:
  ```bash
  git clone https://github.com/dsx-ai-factory/nvke.git
  cd nvke
  make build
  ```
- Produces nine binaries in `bin/` (agent, updater, controller, nvkectl, etc.).  
- Follow `CONTRIBUTING.md` and run `make preflight` before submitting changes.

## Documentation
- Guides cover:
  - Preparing nodes and bootstrapping the management cluster  
  - Installing NVKE services  
  - Building node images via NVKR  
  - Creating and managing customer clusters  
  - Access control, health monitoring, and telemetry  
- Index links to all guides and references.

## Contributing & support
- Contributions welcomed; start with `CONTRIBUTING.md`.  
- Support channels:  
  - GitHub Discussions for questions  
  - DSX AI Factory Slack `#nvke` channel (invite required)  
  - GitHub Issues for bugs/feature requests  
  - Private reporting for security vulnerabilities per `SECURITY.md`  
- Community resources: Code of Conduct, Governance, Maintainers, Support, Release process, CI dashboard.

## Legal
- Trademarks: Kubernetes®, NVIDIA, etc.  
- License: Apache License 2.0 (see LICENSE and NOTICE).