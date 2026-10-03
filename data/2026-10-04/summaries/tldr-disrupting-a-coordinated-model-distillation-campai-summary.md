---
title: Disrupting a coordinated model-distillation campaign | OpenAI
url: https://links.tldrnewsletter.com/VFHse4
date: 2026-10-04
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-04T07:01:33.592401
---

# Disrupting a coordinated model-distillation campaign | OpenAI

# Disrupting a coordinated model‑distillation campaign

## What we observed
- Operators attempted to extract protected reasoning by copying encrypted reasoning from one conversation and asking another model to decrypt it.  
- Independent security researchers reported related cross‑model and conversation‑compaction vulnerabilities; their disclosures were confirmed and helped accelerate mitigations.  
- Activity started on July 1, remained low‑volume, then spiked on July 24‑25 with 16,000 requests from over 4,000 users, and later involved a cluster of more than 15,000 users, which was fully disrupted by July 28.  
- The campaign evolved over time, showing that adversarial distillation is a dynamic security challenge requiring layered defenses.

## Assessment of attribution
- It is unclear whether a single actor was responsible for all observed activity.  
- A core cluster is attributed to individuals linked to Moonshot AI, the developer of Kimi.

## Why this matters
- Extracted reasoning can be used to train new models without the original safety safeguards, posing safety and national‑security risks.  
- At scale, adversarial distillation can accelerate capability transfer without comparable safety investment, especially in dual‑use domains.  
- The technique is not unique to OpenAI; other advanced AI systems face the same threat, making industry‑wide coordination essential.

## How we responded
- Enforced account actions: banned or restricted fraudulent accounts, tightened signup and infrastructure controls, and expanded monitoring of related networks.  
- Strengthened technical protections for hidden reasoning across users, workspaces, organizations, and model families; closed a replay pathway for encrypted reasoning and added checks to hold streamed output that might expose reasoning.  
- Collaborated with third‑party service providers to identify and disrupt offending accounts.  
- Shared findings with the Frontier Model Forum and government information‑sharing channels to help other developers and public‑sector partners improve defenses.

## What comes next
- Anticipate more sophisticated adversarial‑distillation attempts as frontier models advance.  
- Continue enhancing layered controls, including tool‑output defenses, classifier coverage, model refusals, and propagation of safeguards across cloud partners.  
- Focus on three pillars: stronger technical protections against extraction, improved detection and enforcement of coordinated campaigns, and deeper threat‑information sharing with industry and government.

*Footnote:* The reported figures represent attempted extractions, not necessarily successful ones.