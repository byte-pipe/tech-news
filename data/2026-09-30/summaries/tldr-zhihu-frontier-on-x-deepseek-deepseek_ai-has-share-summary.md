---
title: "Zhihu Frontier on X: \"DeepSeek @deepseek_ai has shared a new technical article on Zhihu introducing DeepSeek Elastic Compute (DSec), the sandbox infra..."
url: https://x.com/zhihufrontier/status/2104889429345354180
date: 2026-09-30
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-30T06:01:22.437425
---

# Zhihu Frontier on X: "DeepSeek @deepseek_ai has shared a new technical article on Zhihu introducing DeepSeek Elastic Compute (DSec), the sandbox infra...

# Summary of DeepSeek Elastic Compute (DSec) Technical Article

## Overview
- DSec is the sandbox infrastructure that powers all sandbox workloads for DeepSeek‑V3.2 to V4.1, handling training, evaluation, and data preprocessing at massive scale.  
- In production it runs on thousands of servers with millions of concurrent sandboxes, achieving an over‑commit ratio exceeding 50×.

## Unified Access for Diverse Workloads
- Provides four execution backends accessed through a single Python SDK (`libdsec`):  
  - **FnCall** – reuses pre‑created containers for short online‑evaluation tasks.  
  - **Container** – fast startup and high density for general software‑engineering workloads.  
  - **MicroVM** – stronger isolation for security‑sensitive tasks.  
  - **Full VM** – full OS environment for graphical interfaces, rendering, Android, etc.  

## Layered and Composable Environments
- Sandboxes are built from three independent layers:  
  - **Base image** – OS and core software.  
  - **Workspace** – task‑specific code and dependencies.  
  - **Toolkit** – auxiliary tools such as DeepSeek Harness.  
- Layers are versioned separately and stored in EROFS, enabling on‑demand composition with OverlayFS.  
- Only the changed layer needs rebuilding, avoiding massive image rebuilds (e.g., 11,266 base images, 102,171 workspaces in one week).

## On‑Demand Image Loading
- Production data shows sandboxes use only 4.2 %–13.3 % of image data at runtime.  
- All image data reside on the 3FS distributed file system; only required metadata is fetched locally.  
- Experiments:  
  - Creating 8,192 containers dropped completion time from >60 min to ~35 min (1.71× speedup) and cut disk writes by ~57 %.  
  - Directly mounting EROFS layers reduced workspace provisioning time from 79 min to 45 min and lowered disk writes to ~1/5.5 of the original.

## High‑Density Resource Management
- Sandboxes spend ~90 % of time idle on CPU while memory must stay resident, enabling >50× over‑commit.  
- Key mechanisms:  
  - **Cache sharing** via virtio‑pmem and DAX reduces peak host memory by 40.2 %.  
  - **Memory reclamation** using DAMON and balloon free‑page reporting cuts accumulated memory consumption by 21.2 %.  
  - Combined, they achieve the lowest overall memory usage.  
- CPU scheduling prioritizes latency‑sensitive tasks; latency increase drops from 45.2 % to 17.3 % when other workloads consume 50 % of node CPU.

## Decoupling Rollouts from GPU Training
- Earlier pipelines coupled the Agent execution loop with GPU training in the same pod, causing complex recovery after preemption.  
- Starting with DeepSeek‑V4.1, the loop is split:  
  - **Agent sandbox** runs the Agent framework and toolkits.  
  - **Worker container** manages the sandbox and advances interactions.  
- Both run outside the preemptible GPU pool, preserving state across GPU preemptions and eliminating replay‑log recovery.

## Using Agents to Build Environments for Agents
- Large‑scale RL training requires highly diverse environments (binary deps, code repos, toolkits, evaluation scripts).  
- Agents are employed to automate the construction of these environments, providing a scalable method to generate and maintain the necessary components.

## Key Performance Highlights
- Over‑commit ratio > 50× with CPU utilization typically ≤ 5 % of requested capacity.  
- On‑demand image loading and composable layers reduce provisioning time by up to 44 % and disk writes by > 80 %.  
- Memory sharing and reclamation lower peak host memory usage by > 40 % and overall consumption by > 20 %.  
- Optimized CPU scheduling cuts latency penalties for latency‑sensitive tasks from 45 % to 17 % under load.