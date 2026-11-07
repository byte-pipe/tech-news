---
title: "A $90 Key into Your Company's Secrets • Tomasz Tunguz"
url: https://tomtunguz.com/a-90-dollar-key-into-your-companys-secrets
date: 2026-11-08
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:04:22.185054
---

# A $90 Key into Your Company's Secrets • Tomasz Tunguz

# Summary of “A $90 Key into Your Company's Secrets” – Tomasz Tunguz  

## Key Findings  
- The cost of an autonomous 32‑step corporate network breach dropped ≈ 99 % in five months, from $7,500 (Claude Mythos Preview, Apr 2026) to $90 (open‑weight GLM‑5.3, Aug 2026).  
- Attackers evaluate AI compute as expected value: $1 M of tokens for a 1 % chance at a $1 B payout yields $10 M expected profit; low‑effort targets are abandoned.  
- Defenders must allocate defensive AI compute to neutralize each dollar of offensive AI, balancing speed, scale, and breadth.  

## Attacker Economics  
- Expected‑value formula: **EV = compute × success‑probability × payout**.  
- High‑value targets (large balance sheets) attract the bulk of AI‑driven attack tokens because cheap filters block low‑value noise.  
- As defensive filters improve, attackers concentrate on the few richest victims, increasing the per‑target stakes.  

## Defender Challenges  
1. **Speed** – AI can shrink intrusion response from months to minutes; CrowdStrike reports average breakout time of 29 min, fastest 27 sec.  
2. **Scale** – Parallel AI swarms amplify attack surface: a July 2026 Hugging Face breach used ~700 agents, 70 k messages, 17.6 k actions, harvesting 136 production keys. 76 % of new enterprise attack paths (up 386 % YoY) are viable only for such swarms.  
3. **Breadth** – Non‑human identities outnumber employees 82 to 1; as enterprises deploy 100× headcount in autonomous agents, each new identity expands the surface to defend.  

## Cost Evolution of AI‑Powered Break‑ins  
| Model (date) | Approx. Cost per 100 M‑token Break‑in | Relative to Apr 2026 |
|--------------|--------------------------------------|----------------------|
| Claude Mythos Preview (Apr 2026) | $7,500 | Baseline |
| Claude Mythos 5 (Jun 2026) | $770 | ↓ 90 % |
| Claude Opus 5 (Jul 2026) | $385 | ↓ 95 % |
| Zhipu GLM‑5.3 (Aug 2026) | $90 | ↓ 99 % |

## Implications for Security Budgets  
- Corporate security spend is racing to match the rapid decline in attack cost; Goldman executives anticipate AI security spending may soon equal or exceed AI coding‑tool budgets.  
- Security Operations Centers (SOCs) use AI agents to triage >4,400 daily alerts, compressing a 70‑minute manual review to minutes for roughly $2 of compute per alert, but must still inspect every alert continuously.  
- The CISO’s role shifts from layering per‑seat “insurance” policies to maximizing compute efficiency: buying enough defensive tokens to push attacker expected value below zero.  

## References (selected)  
- BIS Bulletin No. 129 (Jul 2026) – cost range $5k–$10k for 32‑step hack.  
- UK AI Security Institute (May 2026) – description of the 32‑step simulated corporate network.  
- Cloud Security Alliance & Cogent Research (2026) – data on AI swarm attacks and attack‑path growth.  
- Glean CISO Sunil Agrawal – commentary on speed gains from AI.  
- Anthropic & Zhipu pricing disclosures – compute cost calculations for break‑ins.