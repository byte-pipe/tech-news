---
title: Build vs. buy: a guide for marketers in the vibe code era.
url: https://hendersonmatthew.substack.com/p/build-vs-buy-marketing-tools
date: 2026-09-07
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-07T08:08:15.375547
---

# Build vs. buy: a guide for marketers in the vibe code era.

# Build vs. buy: Marketing tools in the vibe code era

## Overview
- The marketing technology landscape is exploding with new vendors, while internal tooling is being built in parallel.  
- AI adoption is now a top‑down priority, but teams must avoid tech‑debt, wasted tokens, and low‑adoption tools.  
- Experimentation with AI is valuable, yet many problems are better solved by engineers or by purchasing existing solutions.  
- At Sentry, marketing teams use a mix of personal skills, tools, and hosted projects, leading to duplication that needs consolidation.

## Framework for deciding who should build
- **Internal MCP (Marketing Code Platform)** at Railway provides shared skills, tools, guardrails, brand design guidelines, and architecture specs, enabling safe and consistent internal tooling.  
- The framework helps determine when to involve engineering versus when a DIY approach is sufficient, especially for customer‑facing “vibe‑coded” tools that require extra scrutiny.  
- Key considerations:
  - Team technical depth and size (e.g., Railway’s sub‑50‑person, highly technical team).  
  - Availability of existing SaaS contracts.  
  - Potential competitive advantage of custom solutions.  
  - Maintenance and adoption likelihood.

## Build vs. buy decisions by category

### 1. CRM
- **Sarah:** buy an automation‑forward CRM (e.g., Attio); Salesforce may be required at scale.  
- **Matt:** buy (Salesforce, HubSpot, etc.) for their extensive integrations, out‑of‑the‑box reporting, and automation.

### 2. CMS / Website
- **Matt:** build. LLMs like Claude make code‑based site editing 10× faster; a strong engineer can create guardrails and scalable systems.  
- **Sarah:** build only with solid design AI guardrails, a “vibe‑code” ready approach, and an engineering‑forward GTM/marketing team; otherwise risk “AI slop.”

### 3. Audience Data Platform
- **Sarah:** build full stop; custom audience tools become limited and the ICP is a competitive advantage.  
- **Matt:** depends – build what you can (e.g., a quick ICP‑to‑YouTube‑URL generator) and supplement with cheap, proven tools like Clay for enrichment.

### 4. Business Intelligence (BI) tools
- **Sarah:** buy; building is a pain‑in‑the‑ass with chart quirks and AI query agents, and there is little competitive edge.  
- **Matt:** buy for core analytics (requires data‑engineering team), but build custom dashboards for blind spots such as social listening or AI visibility.

### 5. Emailing system
- **Sarah:** buy. Customer.io is recommended for companies up to pre‑Series C and often beyond.  
- *(Matt’s stance on emailing was not completed in the excerpt.)*

## Takeaways
- **Buy** when the solution offers deep integrations, standard functionality, and low maintenance overhead (e.g., CRM, BI, email).  
- **Build** when the tool provides a strategic moat, can be powered efficiently by LLMs, or when existing SaaS options hit customization limits (e.g., audience platform, code‑first CMS).  
- Use an internal platform (like Railway’s MCP) to centralize standards, guardrails, and shared resources, increasing the chance that built tools are adopted and maintained.  
- Continuously evaluate each project against the framework to balance innovation, cost, and long‑term sustainability.