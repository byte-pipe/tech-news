---
title: After 7 years in production, Scarf has reluctantly moved away from Haskell
url: https://avi.press/posts/2026-07-10-after-7-years-in-production-scarf-has-reluctantly-moved-away-from-haskell.html
date: 2026-07-10
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-12T06:01:55.840886
---

# After 7 years in production, Scarf has reluctantly moved away from Haskell

# After 7 years in production, Scarf has reluctantly moved away from Haskell

## Where I’ve been
- I have been a Haskell enthusiast for 16 years, built a company (Scarf) on it, and serve on the Haskell Foundation board.  
- Our backend uses Servant, Beam, PostgreSQL, and a high‑performance WAI service for the Scarf Gateway.  
- In production the code proved reliable, type‑system bugs were caught early, and performance was easy to achieve.  
- The main pain points were long compilation times and ecosystem friction, requiring extensive caching, Nix, CI and other tooling.

## Haskell after AI
- Large language models (LLMs) can generate working code in minutes, shifting the development bottleneck from human effort to compile‑time latency.  
- When compile time is long, even a 15‑minute cold build dominates the feedback loop, especially when multiple AI agents work in parallel on separate branches.  
- Caching, remote builders, and Nix mitigate the problem but never eliminate the cost of cold starts and deep‑change rebuilds; the engineering effort to keep caches “perfect” adds its own tax.  
- The new AI‑driven workflow demands cheap, disposable execution contexts that our Haskell toolchain could not provide efficiently.

## How we moved
- We introduced a parallel Python API server, routing new routes to Python while keeping existing Haskell endpoints alive.  
- Core functionality (auth, DB access, models, deployment, tests) was reimplemented in Python; LLMs made the porting relatively easy.  
- Development cycles shortened: the time saved on compilation was reallocated to shipping features and writing extensive tests (with LLM assistance).  
- Productivity gains are evident in faster bug‑fix turnaround (sometimes live before a customer call ends) and higher team energy, even though traditional metrics (PR count, lines of code) show no clear jump.

## The Haskell ecosystem problem
- AI is permanent; ecosystems that integrate it well will outpace those that do not.  
- Skilled AI‑augmented engineers can complete weeks‑long tasks in days, making compile‑time overhead a critical competitive disadvantage for Haskell.  
- The loss of type safety has not been noticeable so far, thanks to improved test coverage and rapid hot‑fixes.  
- Without addressing compilation speed and tooling friction, Haskell risks falling behind in the AI‑driven development landscape.