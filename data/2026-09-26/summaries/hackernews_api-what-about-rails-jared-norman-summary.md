---
title: What About Rails? | Jared Norman
url: https://jardo.dev/what-about-rails
date: 2026-09-25
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-26T05:56:59.137044
---

# What About Rails? | Jared Norman

# What About Rails? – Summary of Jared Norman’s Article

## The Gist of It
- DHH (David Heinemeier Hansson) announced his retirement from professional programming, rebranding himself as a “maker.”
- He promotes English (via LLMs) as the primary programming language, arguing that hand‑written code is no longer economically viable for most developers.
- DHH is fully embracing LLM‑generated code, shifting from Ruby to Rust for server‑side work, claiming Rust is “hideous” for humans but ideal for LLMs.
- He reported writing ~150 k lines of code in August (mostly verbose Rust) versus ~30 k lines per year pre‑LLM; Ruby now represents only ~3 % of his output.
- The new strategy treats human code reading as an exception; by year‑end he predicts this will be the norm across domains, companies, and programmers.
- DHH wants every service to expose a CLI for interaction by his “agents” (LLM‑driven bots).
- He concluded with a call to reject AI skepticism, urging developers to embrace LLM‑enabled creation.

## A Rails‑shaped Hole
- DHH used the Rails World keynote to announce that a flagship Rails app (Hey) is moving off the Rails stack.
- Historically, Rails was marketed as the framework for “small teams, ambitious products”; DHH now frames it as suitable only for “web apps of necessity.”
- He described Rails as mature and stable, good for agentic development, yet his own Ruby usage dropped to 3 % this year.
- The shift to native apps and CLIs raises questions about product differentiation and the future stewardship of Rails.
- The article notes uncertainty about who will drive Rails’ roadmap now that DHH’s focus has moved elsewhere.

## The Hallucinated Elephant in the Room
- DHH’s company (37signals) builds simple, user‑friendly products and often rewrites apps for new versions; their success relies more on product/marketing than solving hard technical problems.
- Relying on LLMs without human code review can work for small, easy problems, but the tools still produce frequent errors.
- The article critiques DHH’s metrics: comparing lines of LLM‑generated Rust to hand‑written Ruby is an apples‑to‑oranges comparison, especially since DHH admits he does not read the Rust code.
- Claims of massive performance gains (e.g., 99 % less CPU) are presented without solid evidence, further questioning the validity of the presented data.