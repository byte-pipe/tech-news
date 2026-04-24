---
title: "Anthropic's Most Dangerous Model Just Got Accessed by People Who Weren't Supposed to Have It - DEV Community"
url: https://dev.to/om_shree_0709/anthropics-most-dangerous-model-just-got-accessed-by-people-who-werent-supposed-to-have-it-14dn
date: 2026-04-22
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-04-25T08:24:46.141106
---

# Anthropic's Most Dangerous Model Just Got Accessed by People Who Weren't Supposed to Have It - DEV Community

# Summary of “Anthropic’s Most Dangerous Model Just Got Accessed by People Who Weren’t Supposed to Have It”

## Model Overview
- Claude Mythos Preview is Anthropic’s most capable model for coding and agentic tasks.  
- During testing it saturated existing cybersecurity benchmarks and began identifying zero‑day vulnerabilities across major operating systems and browsers.  
- Example: autonomously discovered and exploited a 17‑year‑old remote code execution bug in FreeBSD without human intervention.  
- Because of its power, Anthropic decided not to release the model publicly.

## Project Glasswing (Controlled Release)
- Announced on April 7 as a limited‑access program for defensive cybersecurity use.  
- Partners include AWS, Apple, Cisco, Google, Microsoft, NVIDIA, Palo Alto Networks, and over 40 other critical‑software organizations.  
- Pricing: $25/$125 per million input/output tokens via Claude API, Amazon Bedrock, Google Vertex AI, and Microsoft Foundry.  
- Anthropic allocated $100 M in usage credits for the research preview.  
- The program relied on tight vendor‑level access controls.

## Unauthorized Access via Discord Group
- An unidentified “private online forum” obtained access through a third‑party contractor’s environment.  
- The group guessed the model’s endpoint by recognizing Anthropic’s URL naming pattern, a method described as pattern recognition rather than a sophisticated breach.  
- Access was gained on the same day Mythos was publicly announced.  
- Members posted screenshots and live demos to Bloomberg; they claim interest in exploring the model, not causing harm.  
- Anthropic is investigating; no evidence yet of impact on its internal systems.

## Implications and Broader Concerns
- The incident shows that Project Glasswing’s assumption of enforceable gated access is fragile; threat actors could replicate the endpoint‑guessing technique.  
- It follows recent Anthropic information‑control failures: a Claude Code source leak (512 k lines of TypeScript) and a draft blog post about Mythos exposed publicly.  
- Government context: NSA uses Mythos despite DoD officials labeling Anthropic a “supply chain risk”; CISA reportedly lacks access.  
- The disparity highlights that a small Discord group can reach the model while key U.S. security agencies cannot.

## Anthropic’s Official Statement
- A spokesperson confirmed investigation of the alleged unauthorized access through a third‑party vendor environment.  
- No evidence that Anthropic’s own systems were compromised.  
- The response follows a pattern of acknowledging narrow issues while denying broader systemic risk.

## Vendor and Governance Challenges
- Deploying frontier‑capability AI at enterprise scale creates trust chains across dozens of organizations, each with its own security posture.  
- Glasswing’s 40‑partner rollout introduces 40 potential lateral entry points.  
- Anthropic’s long‑term goal is safe, large‑scale deployment of Mythos‑class models for cybersecurity and other uses, but achieving this requires solving vendor‑access governance at a scale the industry has not yet addressed.  
- The current breach suggests that perimeter controls may fail when faced with determined actors.