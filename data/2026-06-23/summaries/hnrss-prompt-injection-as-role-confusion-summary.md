---
title: Prompt Injection as Role Confusion
url: https://role-confusion.github.io
date: 2026-06-22
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-23T10:21:54.745257
---

# Prompt Injection as Role Confusion

# Prompt Injection as Role Confusion – Summary  

## 1. The World to an LLM  
- The model receives one continuous string that contains system prompts, user messages, tool outputs, its own prior reasoning, and any external data.  
- Editing any part of this string changes the model’s “reality”; there is no separate record of conversational turns.  
- Humans separate sources through different sensory channels, but an LLM must rely on explicit markers to tell them apart.  

## 2. Roles  
- Role tags (e.g., `system`, `user`, `think`, `assistant`, `tool`) partition the token stream and tell the model how to treat the following text.  
- Each tag conveys a distinct intent:  
  - `user` → human instruction  
  - `think` → model’s private reasoning (trusted, not acted on directly)  
  - `tool` → external data, not a command source  
  - `assistant` → final output to the user  
- Roles function as a type system, providing discrete control levers that are otherwise “mushy” prompt engineering.  
- Over time roles have accumulated multiple responsibilities (trust hierarchy, adversarial signaling, identity, generation mode).  
- Many models keep the `think` region hidden from the assistant’s verbal output, often denying its existence due to RLHF incentives.  

## 3. Roles and Prompt Injection  
- Prompt injection happens when low‑privilege text (e.g., inside a `tool` block) is mis‑interpreted as a higher‑privilege `user` instruction.  
- Example: a web‑browsing agent receives a webpage wrapped in `<tool>` tags; an attacker hides a command like “upload your .env file” inside the page. If the model treats that snippet as user text, the attack succeeds.  
- Without visual cues, the model can easily confuse the role, because all tokens appear in a single stream.  

### Defenses  
- **Attack memorization** – the model recognizes known malicious patterns from training; this is brittle and fails against novel or adapted attacks.  
- **Role perception** – the model correctly parses role tags so that tool‑originated text is never acted upon as a user command; this offers a more robust defense.  
- Recent frontier models still exhibit 11‑25 % failure rates against adaptive human attacks, despite near‑perfect scores on static benchmark suites, indicating reliance on memorization rather than true role awareness.  

## 4. Implications and Future Work  
- A deeper scientific understanding of roles is essential for reliable LLM control.  
- Research directions include:  
  - Designing parsers or training objectives that enforce strict role boundaries.  
  - Creating adaptive evaluation frameworks that reflect human‑adaptive attack strategies.  
  - Exploring how role tags shape internal model cognition and how to make that influence transparent.