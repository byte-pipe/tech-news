---
title: What is a Harness? | EARENDIL
url: https://earendil.com/posts/what-is-a-harness/
date: 2026-08-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-24T07:47:32.451386
---

# What is a Harness? | EARENDIL

# Summary of “What is a Harness?”

## Key ideas
- A harness is a set of straps and belts that secures a person, animal, or object; in climbing it connects the climber to ropes, carabiners, and tools, providing safety and adaptability.
- The author draws an analogy between climbing harnesses and **agent harnesses** used in AI, suggesting that both serve to support and extend the capabilities of the user.
- An agent harness is software that creates an environment for an AI model to act as an autonomous agent. Unlike typical AI services, users can own and run their own harnesses.
- Harnesses can be accessed through various interfaces (terminal, chat apps, email) and generally perform four core functions: provide a system prompt, expose tools, manage an agentic loop, and translate between different AI models.

## Agent harness components
- **System prompt**  
  - A set of instructions injected into every interaction, guiding the model’s behavior much like onboarding directions for a new employee.  
  - It supplements the model’s internal training without being permanently embedded.

- **Tools**  
  - Code‑based capabilities that the model may call, such as web search, code execution, or email composition.  
  - The harness describes and supplies the tools but does not dictate when the model should use them.

- **Agentic loops**  
  - The iterative process where the model evaluates a request, decides which tools to invoke, reviews outcomes, and repeats until the task is satisfied.  
  - Example: a user asks for school rankings; the model searches the web, processes data into a spreadsheet, and finally composes an email with results, looping as needed.

- **Translation layer**  
  - Enables the harness to work with multiple AI models (e.g., Anthropic, OpenAI, open‑weight models) within the same loop.  
  - Gives end users control over model choice, cost, and data ownership, allowing local execution and retention of session histories.

## Implications
- By owning a harness, users keep agency over their AI tools, avoid lock‑in to a single provider, and can compare performance and cost across models.  
- The climbing metaphor emphasizes that, like a physical harness, an agent harness is adaptable, personalizable, and essential for safe, effective operation in complex environments.