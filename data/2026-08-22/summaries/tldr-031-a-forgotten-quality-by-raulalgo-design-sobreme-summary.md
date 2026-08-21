---
title: 031 — A forgotten Quality - by raulalgo - Design Sobremesa
url: https://designsobremesa.substack.com/p/031-a-forgotten-quality
date: 2026-08-22
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-22T06:00:46.076229
---

# 031 — A forgotten Quality - by raulalgo - Design Sobremesa

# 031 — A forgotten Quality

## Rambling 1. Intelligent automata
- The author is most impressed by AI’s capacity to automate work, not by the hype around “artificial intelligence.”
- Intelligence, in this context, is seen as the ability to make unstructured language understandable for machines.
- Large language models (LLMs) translate natural language into structured instructions, enabling tasks such as:
  - Creating watering schedules from plant photos.
  - Matching meeting notes with completed tickets to showcase performance.
  - Orchestrating weekly newsletters.
- The result is an “automation factory” that helps computers understand human intent.

## Option 1. Paul Rand
- Design education often stresses the distinction between art and design, emphasizing utility and the principle “form follows function.”
- Paul Rand, creator of iconic logos (IBM, ABC, UPS), exemplifies this mindset.
- Rand’s unused Ford logo proposal illustrates a design that is valuable precisely because it was never used, preserving its integrity.
- An anecdote with Steve Jobs shows Rand’s pragmatic approach: offering solutions and letting the client decide whether to adopt them.
- The story highlights the importance of listening to one’s own voice and valuing designs that may remain unseen.

## Share 1. Vibe‑testing
- At Viooh, the team moved from a basic `DESIGN.md` to a self‑improving system using an LLM (Claude) as a QA tester.
- The workflow:
  1. Draft an initial `DESIGN.md`; if needed, prompt Claude with existing code or Figma designs to generate one.
  2. Provide a target (e.g., a landing‑page screenshot) and ask Claude to produce a spec derived solely from the page’s code, without visual details.
  3. Run a fresh agent in a “clean room” with only the spec and `DESIGN.md`; let it attempt to recreate the design.
  4. Compare the agent’s output to the screenshot; the agent reports divergences and suggests fixes to `DESIGN.md`.
  5. Log each fix as an issue, feed it back as a new prompt, and repeat the cycle until no more issues remain (or credits run out).
- This loop lets the design specification iteratively improve itself, reducing bottlenecks for product managers and creating a reusable benchmarking skill.