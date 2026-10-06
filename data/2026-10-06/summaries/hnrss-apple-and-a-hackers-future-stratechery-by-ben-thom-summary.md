---
title: Apple and a Hacker’s Future – Stratechery by Ben Thompson
url: https://stratechery.com/2026/apple-and-a-hackers-future/
date: 2026-10-05
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-10-06T16:49:36.111350
---

# Apple and a Hacker’s Future – Stratechery by Ben Thompson

# Apple and a Hacker’s Future

## Background of the vulnerability
- A high‑severity macOS screen‑sharing bug (CVE‑2026‑65400) allowed remote code execution and was actively exploited to install a Monero miner.  
- The flaw stemmed from improper state‑management in the screen‑sharing service and received a severity rating of 7.1.  
- Apple patched the issue for macOS Tahoe, Sequoia, and Sonoma after it was disclosed at Black Hat; the company noted the exploit “may” allow credential‑less access.  
- Security firm Bynario reported the vulnerability.

## My personal incident
- My always‑on Mac Mini, running only Claude and Codex, was compromised before I saw the Ars Technica article.  
- Claude’s monitoring tool detected abnormal activity, stopped all commands, and warned that admin commands could be run without a password.  
- Following Claude’s guidance, I identified a four‑second window of unauthorized access, built a detection tool, and wiped the machine.  
- The incident showed that an AI‑agent could respond faster than I could manually investigate.

## Agent protection strategy
- I use a dedicated Claude Code thread (“the agent”) to record ideas, track projects, and act as an inbox for interactions via a status board and Telegram bot.  
- Claude’s persistent monitoring restarts every 30 minutes; this schedule triggered the urgent notification.  
- Although I was advised not to invoke Claude further, I continued to use it to root out the malware and implement safeguards.

## Apple’s stance on agents
- Apple announced upcoming restrictions on Full Disk Access, emphasizing explicit user consent for apps that request such broad permissions.  
- The company warned that AI agents with autonomous capabilities increase the risk associated with Full Disk Access.  
- I am concerned that Apple’s tighter controls may limit the usefulness of agents on macOS.

## Challenges with macOS TCC on a headless machine
- macOS’s Transparency, Consent, and Control (TCC) subsystem requires explicit user approval for access to resources like Camera, Desktop, and network shares.  
- TCC prompts appear in a protected UI layer invisible to background processes, causing silent failures for agents that need new permissions.  
- For a headless, always‑on Mac Mini, this means I must log in via screen sharing to approve prompts, turning a manageable annoyance on a primary Mac into a major operational headache.  
- The current permission model operates at the program level, not the agent level, which is misaligned with my workflow where agents generate new programs dynamically.

## Takeaways
- The CVE‑2026‑65400 exploit demonstrates how quickly a seemingly isolated, agent‑focused machine can be compromised.  
- An AI‑agent with proper monitoring can detect and help remediate attacks faster than a human could.  
- Apple’s forthcoming restrictions on Full Disk Access and the existing TCC system pose significant usability challenges for headless Macs running autonomous agents.  
- To make agents viable on macOS, permission controls need to evolve toward an abstraction that protects users while allowing trusted agents to operate without constant manual intervention.