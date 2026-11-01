---
title: Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer
url: https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer
date: 2026-11-02
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-02T08:49:18.425317
---

# Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer

# Appraisal by AI: Model-driven victim prioritization in the VOLTA infostealer

## Overview
- VOLTA‑AUTODOXER is a self‑deleting Windows infostealer that adds an LLM‑driven victim‑profiling stage after data theft.  
- The malware collects a wide range of credentials and personal data, builds a structured evidence bundle, and sends it to an LLM to obtain a monetization‑value ranking and OPSEC assessment.  
- No attacker‑owned C2 infrastructure is observed; all communication occurs via the victim’s own network to third‑party services (OpenRouter).

## AI configuration
- Endpoint: `https://openrouter.ai/api/v1/chat/completions`.  
- Default model: `anthropic/claude-opus-4.6`.  
- Fallback chain (used after a refusal): `moonshotai/kimi-k2` → `google/gemini-2.5-flash`.  
- Temperature set to 0.2 for deterministic, accurate output.  
- System prompt instructs the model to act as a forensic intelligence analyst, producing sections “WHAT THEY'RE WORTH” (asset tiering) and “THEIR OPSEC” (security posture).  
- The malware checks responses for refusal phrases and automatically retries with the next model in the chain.

## Stealer capabilities
- Extracts browser passwords, cookies, saved payment cards (Chromium, Firefox, Thunderbird).  
- Harvests tokens and sessions for Discord, Telegram, Steam, Battle.net, Roblox, Slack, Microsoft OAuth, SSH, cloud‑provider configs, Wi‑Fi profiles, and iPhone backup indicators.  
- Performs live enrichment using stolen sessions:
  - Gmail token → search for purchase receipts to confirm home address.  
  - UberEats/DoorDash tokens → retrieve order history.  
  - Discord token → enrich account profile.  
  - Roblox token → value inventory via Rolimons.com.  
- Runs an embedded cryptocurrency‑wallet cracker and records cracked wallets.  
- Stores collected data locally in `Identity_Report.txt`, serializes to JSON, posts to OpenRouter, receives `AI_Analysis.txt`, and exfiltrates both in `volta_dox.zip`.  
- Exfiltration can occur in three stages: after stealing (`volta_log.zip`), after AI analysis (`volta_dox.zip`), and after network enrichment (`volta_doxnet.zip`).

## Deployment model
- Uses a template with six swappable slots (API keys, Telegram channel, etc.) filled at build time, indicating a builder‑as‑a‑service approach.  
- Credentials are “encrypted” with a SHA‑256 key derived from two constants in the binary; reversible by reverse engineering.  
- Suggests commoditization: any buyer can receive a custom binary that produces AI‑generated dossiers sent to their Telegram inbox.  
- All observed C2 endpoints are third‑party services; no dedicated attacker infrastructure.

## Countermeasures
- Detect and block known token‑stealing techniques (e.g., App‑Bound Encrypted Storage bypasses).  
- Monitor outbound traffic to OpenRouter and similar LLM APIs from endpoints that should not contact them.  
- Implement strict application control to prevent execution of unsigned binaries and enforce least‑privilege for browsers and credential stores.  
- Use behavioral analytics to spot the characteristic pattern of rapid credential dumping followed by encrypted JSON POST requests.  
- Educate users about the risk of reusing session tokens and the importance of revoking compromised tokens promptly.