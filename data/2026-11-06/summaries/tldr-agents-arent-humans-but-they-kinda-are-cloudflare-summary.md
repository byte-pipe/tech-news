---
title: Agents aren’t humans (but they kinda are) | Cloudflare Blog
url: https://blog.cloudflare.com/trusted-agent-delegation
date: 2026-11-06
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-06T12:29:15.654220
---

# Agents aren’t humans (but they kinda are) | Cloudflare Blog

# Agents aren’t humans (but they kinda are) – Summary

## Overview
- Personal AI Agents act on behalf of human Users by controlling cloud computers or browsers.
- Agents are hosted by Operators (managed services) and can perform any online action a User could, without human limits such as fatigue or friction.
- Because Agents sit between Users and Sites, the Site sees only the Agent, losing direct visibility of the underlying Users.
- The rapid growth of agentic traffic threatens to eclipse traditional human browsing, making old mitigation tactics (e.g., blocking intermediaries) ineffective.

## Intermediary Principle
- **Intermediation Principle:** The business relationship and security responsibilities between Users and Sites must be preserved regardless of any intermediary (Agent or other proxy).
- Sites need mechanisms to recognize, serve, and hold accountable Users acting through Agents, just as they would for direct human traffic.
- Operators of Agents must also be identifiable and accountable, since Agents can scale human actions dramatically and introduce new risks.

## The Intermediary Problem (Illustrated by Ezra)
- Ezra, a human personal assistant, aggregates tasks for multiple clients, making it impossible for merchants to distinguish individual customers.
- When Ezra acts on behalf of a client (e.g., making a purchase or attempting a login), the merchant can only attribute the action to Ezra, not the true client.
- This loss of attribution mirrors the current situation with AI Agents on the web.

## Key Challenges for Website Owners
- **Account Sharing:** One paid subscription accessed via an Agent may serve many Users, undermining subscription models.
- **Compliance & Illegal Activity:** Sites must verify age, location, or other legal requirements; Agents may not provide sufficient guarantees.
- **Friendly Fraud:** Purchases made by Agents lack the device/IP continuity that helps dispute resolution, increasing costs.
- **Human Verification:** CAPTCHAs and similar checks become irrelevant because Agents are never human; passing these signals adds no value.
- **Identity Spoofing:** Agents can mimic legitimate browsers and IPs, making it hard to differentiate them from real users; attackers may copy Agent signatures.
- **Identity Verification Breaks:** Liveness checks, KYC, and other verification methods assume a human presence, which Agents cannot satisfy.
- **Misalignment & Errors:** Agents may make mistakes (wrong items, duplicate orders); Sites cannot easily identify which Agent caused the error.
- **Policy Circumvention:** (section truncated) Agents can bypass site policies designed for human users.

## Implications
- Websites must develop new tools and frameworks to:
  - Authenticate and attribute actions to the correct underlying User.
  - Assess the reputation and accountability of both Agents and their Operators.
  - Adapt fraud‑prevention, compliance, and verification processes to handle agentic traffic at scale.