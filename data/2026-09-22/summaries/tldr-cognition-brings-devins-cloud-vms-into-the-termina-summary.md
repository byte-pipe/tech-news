---
title: "Cognition brings Devin's cloud VMs into the terminal, SSH included"
url: https://runtimewire.com/article/cognition-devin-cloud-terminal-ssh
date: 2026-09-22
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-22T08:47:02.519490
---

# Cognition brings Devin's cloud VMs into the terminal, SSH included

# Summary of “Cognition brings Devin's cloud VMs into the terminal, SSH included”

## Why it matters
- Cognition adds command‑line controls and full SSH access to Devin Cloud, letting developers start, steer, resume, and directly enter the remote VMs used by the Devin coding agent.  
- The cloud VM becomes an extension of the local terminal, enabling a workflow that moves from local interactive coding to longer, compute‑heavy tasks in the cloud and back.  
- Co‑founder and CEO Scott Wu, a former competitive‑programming champion, frames the product as agents handling complete engineering tasks while humans set direction and review results.

## The terminal becomes Devin’s control plane
- Developers launch a cloud session with `devin --cloud` or switch a local session with `devin --cloud`.  
- The remote environment includes a shell, browser, and cloned repositories; the CLI streams the session into the local terminal and persists if the terminal closes.  
- Sessions can be resumed by ID/URL (`devin --cloud --resume`) or opened in Devin’s web UI or Desktop for visual inspection.  
- The new `devin ssh` command wraps the standard SSH client, authenticating via the developer’s Devin credentials, allowing direct shell access, remote‑SSH editor extensions, `scp` file transfers, and port forwarding.

## Moving work in both directions
- The `handoff` command packages the current conversation, Git branch, and uncommitted changes before launching a cloud session, transferring the work‑in‑progress diff.  
- The `pickup` command retrieves Devin’s pull‑request branch, switches the local checkout, and starts a local session on the same code, supporting cycles between quick interactive work and longer jobs (integration tests, Docker builds, deployments, migrations, large refactors).  
- This bidirectional flow bridges the gap between immediate local tooling and asynchronous agent execution.

## Recent developments & funding
- September 15: Mac environments added to Devin Cloud, complementing existing Linux and Windows options, expanding the range of available cloud machines.  
- September 8: Cognition announced a funding round exceeding $2 billion at a $48 billion valuation (led by Andreessen Horowitz and Accel) and reported annualized run‑rate revenue growth from $492 M to nearly $900 M (self‑reported).  

## Availability
- Sessions powered by the SWE‑2 coding model are free in Devin Cloud through October 8.  
- Access requires a Devin account and an authenticated installation of the Devin CLI.  

## Reader comments
- Comments for the story load after sign‑in.