---
title: Agents can now create Cloudflare accounts, buy domains, and deploy
url: https://blog.cloudflare.com/agents-stripe-projects/
date: 2026-05-02
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-02T08:46:58.816116
---

# Agents can now create Cloudflare accounts, buy domains, and deploy

# Agents can now create Cloudflare accounts, buy domains, and deploy

## Overview
- Coding agents can now handle the full Cloudflare provisioning workflow: create an account, start a paid subscription, register a domain, and receive an API token ready for deployment.  
- Human interaction is limited to granting permission and accepting Cloudflare’s terms of service; no dashboard navigation, token copying, or credit‑card entry is required.

## How it works
- A new protocol, co‑designed with Stripe as part of **Stripe Projects**, enables zero‑friction integration.  
- Typical flow:
  1. Install the Stripe CLI with the Stripe Projects plugin and log in.  
  2. Run `stripe projects init` to start a new project.  
  3. Prompt the agent to build and deploy to a new domain.  
  4. The agent discovers services, authorizes with Stripe, and receives a payment token to provision resources on Cloudflare.  

## Key components of the protocol
- **Discovery** – Agents query a catalog of available services via a simple REST API that returns JSON. This gives agents the context needed to choose appropriate Cloudflare products.  
- **Authorization** – Stripe acts as the identity provider, attesting the user’s identity. If the user lacks a Cloudflare account, Cloudflare automatically creates one and returns credentials; otherwise a standard OAuth flow grants access.  
- **Payment** – Stripe supplies a payment token, never exposing raw credit‑card details to the agent. A default spending limit of $100 USD per month is enforced, with the option to raise limits via budget alerts on the Cloudflare account.

## Benefits for platforms and developers
- Any platform with signed‑in users can serve as the “Orchestrator,” replicating Stripe’s role and integrating with Cloudflare without additional friction.  
- Developers can let agents ship code directly to production, bypassing complex authorization flows and manual provisioning steps.  
- The approach can be extended to other providers (e.g., Planetscale) for seamless resource creation from within Cloudflare or other ecosystems.

## Incentives
- The partnership includes $100,000 in Cloudflare credits for new startups that incorporate using Stripe Atlas.

## Resulting agent capabilities
- Provision a new Cloudflare account automatically.  
- Obtain a usable API token.  
- Purchase and register a domain.  
- Deploy an application to production on the newly registered domain.