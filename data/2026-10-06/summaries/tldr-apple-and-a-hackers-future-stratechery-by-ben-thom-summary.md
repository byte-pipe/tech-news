---
title: Apple and a Hacker’s Future – Stratechery by Ben Thompson
url: https://stratechery.com/2026/apple-and-a-hackers-future
date: 2026-10-06
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-06T16:49:17.971650
---

# Apple and a Hacker’s Future – Stratechery by Ben Thompson

# Apple and a Hacker’s Future

## Incident Overview
- My always‑on Mac Mini was compromised through CVE‑2026‑65400, a high‑severity macOS screen‑sharing vulnerability (severity 7.1) that allows remote code execution and was actively exploited to install a Monero miner.
- The flaw was patched by Apple for macOS Tahoe, Sequoia, and Sonoma after being disclosed at Black Hat; Apple’s wording was cautious, noting the exploit “may” allow unauthenticated access.
- I discovered the breach before seeing the Ars Technica report, thanks to alerts from my AI‑driven agent.

## Agent Protection
- I use a constrained AI agent (Claude Code thread) to record ideas, track projects, and act as an inbox via a persistent monitoring tool that restarts every 30 minutes.
- When the breach occurred, Claude halted all commands, reported that my account could run admin commands without a password, and suggested remediation steps, including stopping Claude usage.
- I ignored the suggestion to stop Claude, instead leveraging it to pinpoint the four‑second intrusion window, build a detection tool, and wipe the Mac Mini.
- This experience shows that a dedicated, limited‑capability agent can provide rapid diagnostics and response, even on a machine with minimal software.

## Apple’s Stance on Agents
- Apple announced upcoming restrictions on Full Disk Access, emphasizing the need for explicit user consent before granting apps extensive system privileges.
- The company warns that AI agents with such access could expose user data, communications, and system files without users fully understanding the risks.
- While Apple’s APIs and Unix foundation make macOS a strong platform for automation, the new controls could hinder the very agents that rely on deep system integration.

## Challenges with macOS TCC (Transparency, Consent, and Control)
- TCC requires per‑app permission for sensitive resources (camera, desktop, network shares, etc.) and presents GUI prompts that are invisible to headless or agent‑only machines.
- Agents constantly generate new programs that need permissions, but TCC operates at the program level, not the agent level, causing repeated prompts.
- Because prompts appear in a protected UI space, agents cannot detect or respond to them, leading to silent failures that require manual login and click‑through.
- This permission model, while protecting against malware, becomes a major obstacle for purpose‑deployed, always‑on agents.

## Takeaway
- The hack highlighted both the vulnerability of macOS screen sharing and the utility of a well‑designed AI agent for incident response.
- Apple’s forthcoming tighter controls on Full Disk Access and TCC could improve security but also create significant friction for legitimate autonomous agents.
- Balancing robust user protection with the practical needs of headless, agent‑driven systems will be a key challenge moving forward.