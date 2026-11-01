---
title: The AI cost of JavaScript frameworks | Read the Tea Leaves
url: https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/
date: 2026-11-01
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-02T08:48:53.703439
---

# The AI cost of JavaScript frameworks | Read the Tea Leaves

# The AI cost of JavaScript frameworks – Summary

## Motivation and Context
- The web‑dev community often chooses frameworks based on “vibes” rather than evidence.
- Claims such as “React is fast” or “this tool supercharges DX” are frequently made without benchmarks.
- The author created a systematic benchmark to measure the actual cost and quality of building a small app with different JavaScript frameworks when the work is done by AI agents.

## Benchmark Design
- **App**: A modest Pokémon catalog (list, search, filter) using the PokéAPI.
- **Procedure**:
  1. Prompt an AI agent (Claude Opus 5.5) to build the app with a specified framework/meta‑framework (e.g., Next.js, Nuxt, SvelteKit).
  2. Run the generated app against a spec conformance suite to prevent cheating.
  3. Evaluate each run on:
     - Development cost (API token spend → USD)
     - Development time
     - Lines of code
     - Lighthouse performance and accessibility scores
- **Controls**:
  - No forced architecture (SSR vs CSR) or performance optimizations.
  - No CSS frameworks (Tailwind, Bootstrap) allowed; visual consistency enforced via spec tokens.
  - Agents used the official MCP/skill for each framework when available, but usage was not mandatory.
- **Repetitions**: 5 runs per framework (Angular had only 3 usable runs due to failures).

## Key Findings – Cost per Run (median, USD)

| Framework            | Median Cost | Range |
|----------------------|-------------|-------|
| Hono + htmx          | $2.67 | $2.23 – $3.19 |
| Astro                | $2.76 | $2.16 – $3.63 |
| Nuxt                 | $2.82 | $2.39 – $4.25 |
| Vanilla JS           | $2.98 | $2.24 – $3.37 |
| Next.js              | $3.14 | $2.58 – $4.13 |
| Qwik                 | $3.27 | $2.35 – $3.80 |
| TanStack Start       | $3.54 | $3.11 – $3.96 |
| SolidStart           | $3.79 | $2.84 – $4.81 |
| React Router         | $3.81 | $2.82 – $3.97 |
| SvelteKit            | $4.28 | $3.59 – $4.65 |
| Gracile + Lit        | $4.65 | $3.92 – $5.07 |
| Angular              | $4.97 | $3.19 – $6.82 |

- **Cheapest**: Hono + htmx, followed closely by Astro and Nuxt.
- **Most expensive**: Angular, Gracile + Lit, and SvelteKit.
- Higher costs for SvelteKit and Gracile + Lit appear linked to agents spending extra time reading migration guides or source code, indicating lower familiarity in the model’s training data.
- Angular’s higher cost correlates with larger generated codebases.

## Observations on Stochasticity
- LLM agents are nondeterministic; occasional “dice rolls” cause token waste unrelated to the framework.
- Lighthouse metrics (e.g., Largest Contentful Paint) also show run‑to‑run variance.
- Multiple iterations mitigate randomness, but some variance remains inevitable.

## AI Tool (MCP/Skill) Usage
- Not all agents employed the available framework‑specific MCP or skill files.
- Example usage patterns:
  - **Hono + htmx**: skill tool used in all 5 runs.
  - **Next.js**: MCP used in 2 runs; skill files read in 1–2 runs.
  - **Nuxt**: MCP present but never used.
  - **TanStack Start**: skill files discovered in 2 of 5 runs.
- This uneven adoption underscores the unpredictable nature of prompting AI agents.

## Limitations
- The test app is a single, content‑focused site; results may not generalize to highly interactive applications (e.g., editors, email clients).
- No enforced CSS methodology beyond avoiding component libraries.
- Cost figures reflect Claude Code API pricing, not actual monetary spend for the author.

## Takeaway
- When AI agents generate code, the choice of JavaScript framework materially affects token cost, with lightweight stacks like Hono + htmx being the most economical.
- Frameworks less represented in the model’s training data (SvelteKit, Gracile) can increase cost due to extra lookup steps.
- Evidence‑based benchmarking, even with stochastic AI agents, reveals clear cost patterns that challenge “vibe‑only” framework selection.