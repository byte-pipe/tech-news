---
title: Your AI agent is ready to go. Is your infrastructure? | CIO
url: https://www.cio.com/article/4159773/your-ai-agent-is-ready-to-go-is-your-infrastructure.html
date: 2026-05-01
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-01T03:54:26.358146
---

# Your AI agent is ready to go. Is your infrastructure? | CIO

# Your AI agent is ready to go. Is your infrastructure?

## Scale of agentic AI
- IDC estimates >28 million AI agents were deployed by end‑2023 and projects >1 billion active agents by 2029, performing 217 billion actions daily.  
- Enterprises can quickly build proof‑of‑concept agents, but moving them to production reveals gaps in governance, security, and scalability.

## TransUnion’s OneTru platform
- TransUnion invested $145 M over three years to create OneTru, a hybrid platform that blends traditional expert systems with generative AI.  
- The platform aims for deterministic reliability (old‑school systems) while offering generative AI flexibility and chatbot‑like interaction.  
- Results: $200 M cost savings and the launch of the AI Analytics Orchestrator Agent (powered by Google Gemini) for internal analytics and customer‑facing data analysis without data‑scientist involvement.  
- Future agents will rely on strong orchestration, governance, and security layers built into the platform.

## Architecture and governance approach
- Tasks are split into layers, each assigned to a specialized system with defined constraints:
  - Core decision‑making: updated expert system with auditable rules, low latency, high predictability.  
  - Novel situations: LLM analyzes, another agent may generate a new rule, and a human reviewer validates before integration.  
  - Separate agents handle semantic processing, human interaction, etc.  
- “Neural reasoning” (LLM) always includes a human‑in‑the‑loop; “symbolic reasoning” can be fully automated.  
- This modular, narrow‑scope design creates checks‑and‑balances, limits damage, and improves governability.

## Security challenges and incidents
- Jitterbit survey of 1,500 IT leaders (Mar 2026): AI accountability (security, auditability, traceability, guardrails) is the top factor in AI purchase decisions, outranking speed, vendor reputation, and TCO.  
- Major breach example: CodeWall researchers accessed McKinsey’s Lilli platform via 22 unauthenticated API endpoints, exposing millions of messages, files, and model configurations.  
- IDC warns that delegating authority to AI systems amplifies risk beyond data leakage—attackers could alter business behavior.  
- Gartner predicts 69 % of organizations suspect employee use of prohibited AI tools; 40 % expect security/compliance incidents by 2030, yet discovery tools for AI agents remain immature.

## Recommendations from experts
- **Layered security:** Implement checkpoints at integration “seams” where agents interact with traditional services (e.g., email APIs).  
- **Identity and onboarding:** Catalog all agents, assign identities, enforce authentication, and define ownership.  
- **Human oversight:** Keep humans in the loop for neural‑reasoning outputs; automate only well‑understood symbolic processes.  
- **Continuous monitoring:** Use audit logs and traceability to detect anomalous agent behavior promptly.

## Key takeaways
- The biggest obstacle to scaling agentic AI is not model capability but the supporting infrastructure—governance, security, and orchestration.  
- A hybrid architecture that isolates core, high‑risk functions in deterministic systems while delegating creative tasks to generative AI can deliver cost savings and new revenue streams.  
- Robust security foundations, clear guardrails, and comprehensive agent inventory are essential to prevent breaches and maintain trust as enterprises move from pilots to production‑grade AI agents.