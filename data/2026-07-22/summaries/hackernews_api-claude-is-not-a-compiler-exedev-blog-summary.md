---
title: Claude Is Not a Compiler - exe.dev blog
url: https://blog.exe.dev/claude-is-not-a-compiler
date: 2026-07-22
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-22T06:02:21.752197
---

# Claude Is Not a Compiler - exe.dev blog

# Claude Is Not a Compiler – exe.dev blog  

## Overview  
- The author revisits a 2025 post “Is Claude a Compiler?” and now concludes that Claude (an LLM) is **not** a compiler; calling it a compiler is a category error.  
- Claude is “better than a compiler” because it can operate across the entire software‑development stack, making decisions from strategy down to machine code.  

## Why the “compiler” metaphor falls short  
- Traditional compilers sit at the bottom layer, translating source code to binaries and making many low‑level decisions (inlining, register allocation, warnings).  
- A good compiler shields engineers from those decisions, but it stays confined to the source‑to‑binary transformation.  
- Software development actually involves many overlapping layers (vision → strategy → product → architecture → code → binary), each requiring judgment and cross‑layer communication.  

## The value of vertical, cross‑layer work  
- Real‑world projects succeed when people from different layers collaborate directly (e.g., the Empire State Building’s chrome‑nickel cladding decision involved owners, architects, builders, metalworkers, and inspectors).  
- Organizations often fail to do this because of ignorance, dismissiveness, or the overhead of coordination, even though such collaboration can dramatically improve outcomes.  

## Claude’s advantage over a traditional compiler  
- Claude can converse in natural language about strategy, product requirements, architecture, code, and even machine‑level details.  
- It does not replace specialized humans in each role, but it can **bridge** the layers without scheduling meetings or seeking permission.  

## Concrete example: building a distributed DNS server at exe.dev  
1. **Problem emergence**  
   - VMs receive domain names like `vm-name.exe.xyz`.  
   - Fast VM startup exposed DNS propagation latency; a custom DNS server was created to keep DNS in sync with the source of truth.  
   - Adding geographic regions re‑introduced latency because all DNS queries were still served from Oregon, and deployments caused brief DNS outages.  

2. **Goal definition**  
   - Reduce latency for users far from Oregon.  
   - Increase uptime resiliency with a fully consistent, geographically distributed DNS service.  

3. **Strategic and architectural decisions**  
   - Decided on a general‑purpose DNS server with specific behavioral tweaks, a hub‑and‑spoke topology, append‑only replication, and edge persistence.  

4. **LLM‑driven research and design**  
   - Used Claude to research distributed DNS designs, historical security failures, open‑source options, and failure‑mode analysis.  
   - Prompted multiple agent loops to generate the implementation, tests, and adversarial code reviews.  

5. **Iterative decision capture**  
   - Agents asked questions at every granularity; the author answered, distilled guidance into terse documents, and fed them back to the agents.  
   - Discrepancies between agent implementations were identified (e.g., handling database rollbacks).  
   - Final design added a “timeline” field to rows to detect history alterations and trigger full re‑syncs.  

6. **Outcome and reflections**  
   - Claude produced a more elegant system; Codex produced a more thorough one.  
   - Repeating the differential spec analysis refined the guidance and produced a robust implementation.  

## Takeaways  
- LLMs can act as “vertical agents” that traverse the entire development stack, making and documenting decisions that would otherwise require many meetings.  
- The process of prompting, answering, and codifying decisions creates a “scar‑tissue document” that guides future agents and reduces the need for repeated human intervention.  
- While LLMs may not yet outperform seasoned specialists in any single task, their ability to operate across layers provides a unique productivity boost.  

## Notable quotes  
- “If you plan to throw one away, you will throw away two.” – Fred Brooks  
- “If you plan to throw one away, you will throw away two.” – Craig Zerouni (re‑phrased)  

---  
*The summary preserves the original first‑person perspective and the narrative flow of the blog post while organizing the main points into a clear, hierarchical markdown structure.*