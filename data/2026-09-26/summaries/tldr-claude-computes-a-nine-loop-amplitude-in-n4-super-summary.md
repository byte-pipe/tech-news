---
title: Claude computes a nine-loop amplitude in N=4 super-Yang-Mills \ Anthropic
url: https://www.anthropic.com/research/yes-claude-can-do-nine-loops
date: 2026-09-26
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-26T05:57:26.211640
---

# Claude computes a nine-loop amplitude in N=4 super-Yang-Mills \ Anthropic

# Claude computes a nine‑loop amplitude in N=4 super‑Yang‑Mills – Anthropic

## Background and motivation
- I am Matt von Hippel, former theoretical physicist turned science writer and blogger at **at4gravitons.com**.  
- My recent blogging has increasingly involved AI, a field where I lack deep expertise and where experts disagree sharply about the timeline to superintelligence.  
- To form my own view I issued a concrete challenge: could an LLM use ordinary academic computing resources to solve a frontier problem in **amplitudeology**, specifically “N=4 super‑Yang‑Mills to nine loops” (or N=8 supergravity to seven loops)?

## The problem: scattering amplitudes and loops
- Scattering amplitudes translate particle momenta into probabilities for reactions; higher‑loop calculations give more accurate predictions for experiments such as the LHC.  
- Most amplitudes are known only up to two loops; a few reach three, and the most precise published result reaches five loops.  
- Amplitudeologists test new computational techniques on **toy models** that are simpler than realistic theories but still non‑trivial.  
- The toy model I chose is **N=4 super‑Yang‑Mills (SYM)**:
  - A Yang‑Mills theory (the basis of three of the four fundamental forces).  
  - “N=4” supersymmetry means each particle has four super‑partners, making the theory highly symmetric and mathematically tractable, though not a realistic description of nature.  
  - Its symmetry reduces the number of independent variables, allowing deeper loop calculations.

## The bootstrap method
- The bootstrap constructs an amplitude by enumerating all possible terms in a specialized “alphabet” and then applying constraints:
  - Known limits from other calculation methods.  
  - Physical consistency rules (e.g., symmetries, analyticity).  
  - Relations to simpler, already‑solved problems.  
- This process is analogous to solving a Sudoku puzzle: possibilities are eliminated until a unique solution remains.  
- The method is well‑suited for AI because it reduces the problem to systematic constraint checking rather than brute‑force symbolic manipulation.

## The state before the challenge
- The nine‑loop amplitude for N=4 SYM had never been computed.  
- The eight‑loop result was obtained indirectly via a link to a related **form‑factor** calculation, not by a straightforward bootstrap run.  
- Researchers expected the next loop to require an even more indirect approach or new AI techniques; a direct bootstrap run seemed infeasible with existing resources.

## Anthropic’s response
- Two Anthropic physicists, **Liam Fitzpatrick** and **Siddharth Mishra‑Sharma**, read my blog post.  
- At the end of August they began working on the nine‑loop problem, applying Claude (Anthropic’s LLM) together with the bootstrap framework.  

*(The article continues with details of their implementation, results, and implications, but the excerpt ends here.)*