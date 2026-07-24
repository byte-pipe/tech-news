---
title: 'tpu-management: a Claude Code skill for running Gemma 4 on Cloud TPUs - DEV Community'
url: https://dev.to/gde/tpu-management-a-claude-code-skill-for-running-gemma-4-on-cloud-tpus-1b1e
site_name: devto
content_file: devto-tpu-management-a-claude-code-skill-for-running-gem
fetched_at: '2026-07-24T11:34:58.303281'
original_url: https://dev.to/gde/tpu-management-a-claude-code-skill-for-running-gemma-4-on-cloud-tpus-1b1e
author: xbill
date: '2026-07-21'
description: A Claude Code skill + MCP server that provisions Google Cloud TPU capacity, serves Gemma 4 with vLLM, benchmarks it, and tears it down — installable in one command. Tagged with googlecloud, tpu, vllm, claudecode.
tags: '#googlecloud, #tpu, #vllm, #claudecode'
---

Getting a Gemma 4 model serving on a Cloud TPU involves a surprising amount of ceremony: finding a zone that actually has v6e capacity, requesting flex-start VMs, sizing boot disks, wiring Hugging Face tokens through Secret Manager, picking the right vLLM flags for TPU, and remembering to tear everything down before the billing meter embarrasses you.

I packaged all of that intotpu-management— a Claude Code skill plus an MCP server (tpu-devops) — so you can just ask Claude to do it.

## What it does

The skill teaches Claude the full TPU serving lifecycle, and the MCP server gives it ~40 tools to execute it:

* Find capacity:sweep every zone with quota for an available TPU (find_tpu), check dimensioned quotas (get_zones_with_available_quota), estimate cost before creating anything.
* Provision:create flex-start TPU VMs (v6e/v5p) or legacy queued resources (v5e), with a startup script that installs Docker, pullsvllm/vllm-tpu:nightly, fetches the HF token from Secret Manager, and serves the model automatically.
* Serve & verify:manage the vLLM container, watch boot via the serial console, verify model health, and query the deployed Gemma 4 endpoint directly.
* Diagnose:pull vLLM/docker/system/Cloud Logging logs — including Gemma-4-powered log triage (analyze_cloud_logging), where the self-hosted model analyzes its own infrastructure's logs.
* Benchmark:runvllm bench serveagainst the deployment and get TTFT/throughput/P95 numbers back.
* Tear down:destroy resources safely, with guardrails (the skill insists on confirming teardown, and warns that flex-start bills until deletion).

It also encodes the hard-won details you'd otherwise learn at 2 a.m.: the default 10 GB boot disk that the vLLM TPU image overflows, theTPUS_PER_TPU_FAMILYquota that's invisible togcloud regions describe, why you watch the serial console instead of SSH, and the exact vLLM flags Gemma 4 needs on TPU (--tool-call-parser gemma4,--disable_chunked_mm_input, and friends).

## Install

The fastest path is the Claude Code plugin marketplace — one command gets you the skillandthe MCP server:

/plugin marketplace add xbill9/tpu-skill-claude
/plugin 
install 
tpu-management@tpu-skill-claude

Enter fullscreen mode

Exit fullscreen mode

Prefer the classic routes? Clone and install:

git clone https://github.com/xbill9/tpu-skill-claude

cd 
tpu-skill-claude
make skill-install 
# skill only, all projects

./project-setup.sh 
--global
 
# skill + MCP server registration

Enter fullscreen mode

Exit fullscreen mode

Or skip the clone entirely and unzip the packaged skill:

curl 
-L
 
-o
 /tmp/tpu-management-skill.zip 
\

 https://github.com/xbill9/tpu-skill-claude/raw/main/dist/tpu-management-skill.zip

mkdir
 
-p
 ~/.claude/skills 
&&
 unzip 
-o
 /tmp/tpu-management-skill.zip 
-d
 ~/.claude/skills/

Enter fullscreen mode

Exit fullscreen mode

You'll need an authenticatedgcloudCLI, the TPU API enabled, and a Hugging Face token (the agent'ssave_hf_tokentool stores it in Secret Manager for you). Configuration is all environment variables:GOOGLE_CLOUD_PROJECT,MODEL_NAME,ACCELERATOR_TYPE,TENSOR_PARALLEL_SIZE.

## What it looks like in practice

Once installed, you talk to Claude Code like this:

"Find me a v6e-1 with available quota and serve gemma-4-12B on it"

Claude checks existing resources first (the skill's rule: never create before checking what exists), sweeps zones for capacity, creates the VM with the proven flags, follows the serial console until vLLM logs "Application startup complete," and hands you a working OpenAI-compatible endpoint. Then:

"Benchmark it and tear it down when done"

The skill ships with a full reference guide (references/tpu-guide.md) : flex-start zones per TPU family, quota metrics and how to request increases, and troubleshooting — so Claude can answer capacity and billing questions even without the MCP server connected.

## Under the hood

The repo doubles as both a Claude Codeplugin marketplaceand a plain skill repo. AMakefilekeeps the three distribution formats (project skill, plugin layout, zip) in sync from one set of sources, and the MCP server is a single-file FastMCP app — easy to read, easy to fork for your own model/accelerator combos.

Issues and PRs welcome:https://github.com/xbill9/tpu-skill-claude

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse