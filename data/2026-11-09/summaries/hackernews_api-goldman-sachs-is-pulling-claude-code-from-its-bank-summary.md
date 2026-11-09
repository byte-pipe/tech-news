---
title: Goldman Sachs Is Pulling Claude Code From Its Bankers and Traders | State of AI
url: https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers
date: 2026-11-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-09T16:01:45.177547
---

# Goldman Sachs Is Pulling Claude Code From Its Bankers and Traders | State of AI

# Goldman's Restriction of Claude Code and GitHub AI Tools  

## Key Developments  
- Internal guidance updated in October limits Anthropic’s Claude Code and Microsoft’s GitHub Copilot to engineers only; traders and bankers can no longer use these coding agents.  
- Strats (trading, quantitative research, software engineering) retain access.  
- The change follows a productivity‑risk review and has frustrated traders who used the tools for client‑flow monitoring, market‑move modeling, and report creation.  

## Recent History  
- **July 2023:** CIO Marco Argenti praised “vibe coding,” where non‑technical traders built AI tools that engineers later refined.  
- **April 2023:** Claude was removed from Goldman’s internal AI platform for Hong Kong bankers due to contract terms; ChatGPT and Gemini remained available.  
- **2024 IPO involvement:** Goldman (and Morgan Stanley) are lead underwriters for Anthropic’s planned Nasdaq IPO (ticker ANT).  

## Rationale for the Restriction  
- **Risk of unreviewed code:** Trader‑generated scripts can be deployed without engineering review, testing, or deployment controls, increasing the chance of errors or losses.  
- **Information barriers:** Banks must separate deal‑making bankers from traders; AI‑generated code may breach these barriers.  
- **Understanding of code:** Traders may lack the expertise to assess edge‑case behavior of AI‑written code.  
- **Cost considerations:** Agent usage is token‑based; uncontrolled use can drive up spending.  

## Comparison with Other Banks  
- **Barclays:** Plans for half of its developers to use Claude Code by year‑end and is using the agent to reduce engineering headcount.  
- **JPMorgan & Schwab:** Blocking external agents from accessing customer accounts.  

## Commentary from State of AI  
- The restriction is justified on a trading floor, but the rollout was poorly managed—removing access without a clear replacement or transition plan.  
- Recommendation: Assign a responsible engineer to any agent‑generated tool before it reaches production, and maintain existing controls (information barriers, data entitlements, software approval) for AI‑written code.  
- When tools are withdrawn, document the use cases (e.g., client‑flow monitoring, position modeling) so alternative solutions can be provided.