---
title: Blue41 | How we helped Bunq secure their financial AI assistant
url: https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/
date: 2026-06-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-11T06:02:40.373557
---

# Blue41 | How we helped Bunq secure their financial AI assistant

# How we helped Bunq secure their financial AI assistant – Summary

## Overview
- Blue41 identified and mitigated an indirect prompt‑injection vulnerability in Bunq’s AI‑driven banking assistant.  
- The flaw allowed a tiny €0.02 transfer to turn the assistant into a channel for a credible spear‑phishing attack.  
- The issue is generic to any financial AI system that ingests untrusted data (transactions, documents, messages, etc.).

## Typical Architecture
- User interacts with the banking app → assistant retrieves context (transactions, docs, account data) → passes context to a large language model (LLM) → LLM generates a conversational response.  
- Not all retrieved fields are equally trustworthy; transaction descriptions can contain hidden instructions that the LLM may treat as prompts.

## Attack Flow
1. Attacker sends a small transfer with a malicious payload embedded in the transaction description.  
2. Victim asks the AI assistant a routine question (e.g., “Show me my recent transactions”).  
3. Assistant fetches the transaction data, including the malicious description, and includes it in the LLM’s context.  
4. LLM interprets the hidden instruction and produces a phishing message that appears to come from the bank’s own assistant, referencing real user details.

## Why It Matters for Banks
- **Broad injection surface:** transaction notes, payment references, merchant metadata, support messages, uploaded documents, emails, CRM notes, etc., can all become vectors.  
- **Low cost, high credibility:** a minimal transfer injects attacker‑controlled text into a trusted channel (the bank’s app).  
- **Privileged context:** the assistant can access real account information, making the forged message highly personalized.  
- **Increasing risk with capability:** even read‑only assistants can mislead; assistants with tool‑execution abilities amplify the threat.

## Guardrails Are Insufficient Alone
- Bunq already employed input filters and content‑moderation rules, yet the crafted payload blended with normal transaction data and evaded detection.  
- Static text classification cannot capture risk that emerges from the interaction of untrusted data, retrieval logic, and model behavior.  
- Effective security requires layered controls beyond simple filtering.

## Effective Mitigation Strategy
1. **Minimize context exposure** – only pass fields essential for the user’s request; omit unnecessary transaction descriptions.  
2. **Treat retrieved data as untrusted** – explicitly separate data from instructions in the assistant’s architecture.  
3. **Constrain sensitive outputs and actions** – limit outbound links, enforce least‑privilege access, and restrict actions the assistant can perform.  
4. **Runtime monitoring** – detect anomalous responses or behavior that deviates from the intended operating profile.

- Blue41 worked with Bunq to implement these controls, validate their effectiveness, and close the identified vulnerability.  
- The four‑layer approach provides a practical roadmap for any financial institution deploying AI assistants.