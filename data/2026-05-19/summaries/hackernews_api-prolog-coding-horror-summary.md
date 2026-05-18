---
title: Prolog Coding Horror
url: https://www.metalevel.at/prolog/horror
date: 2026-05-18
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-19T06:01:42.492447
---

# Prolog Coding Horror

# Prolog Coding Horror – Summary

## Why are you here?
- The page warns that rebellious use of non‑standard Prolog features often incurs high cost with no benefit.  
- Following a small set of rules yields great Prolog code; breaking them leads to defective programs.

## The horror: Losing solutions
- Defects appear in two ways:  
  1. Reporting wrong answers.  
  2. Failing to report intended solutions.  
- The second case is worse because it hides correct results.  
- Impure, non‑monotonic constructs such as `!/0`, `(->)/2`, and `var/1` cause loss of solutions.  
- Declarative alternatives: clean data structures, constraints like `dif/2`, and meta‑predicates such as `if_/3`.

## The horror: Global state
- Beginners often modify the global database with `assertz/1` and `retract/1`.  
- This creates implicit dependencies that are not enforced by the program, leading to unexpected failures when predicates are reordered.  
- Declarative solution: pass state via predicate arguments or use semicontext notation.

## The horror: Impure output
- Printing results directly (e.g., using `format/2`) hides output from the Prolog term system, making testing difficult and preventing the code from being a true relation.  
- Recommended practice: let the toplevel handle printing; describe solutions purely with predicates.  
- For custom formatting, use pure non‑terminals like `format_//2`, which remain testable.

## The horror: Low‑level language constructs
- Relying on low‑level arithmetic predicates (`is/2`, `=:=/2`, `>/2`) makes Prolog harder to teach, learn, and understand.  
- These constructs force learners to juggle declarative and operational semantics simultaneously.  
- Declarative alternative: teach and use constraint‑based arithmetic (e.g., CLP(FD)).

## Horror factorial (example)
- A factorial definition using `!/0` and low‑level arithmetic loses solutions and raises errors on the most general query.  
- Example without `!/0` still fails due to `is/2` when variables are uninstantiated.  
- The example illustrates the pitfalls of impure constructs and outdated features.

## A way out: Purity
- Stay within the pure, monotonic subset of Prolog.  
- Replace low‑level arithmetic with constraints (`#>/2`, `#=/2`, `#* /2`).  
- Remove cuts (`!/0`) to allow full backtracking.  
- The resulting `n_factorial/2` works for the most general query, producing all factorial solutions.

## Conclusion
- Rebel only when it makes sense; clinging to outdated, impure features is misguided.  
- Use declarative constructs to write more general, maintainable Prolog programs without sacrificing acceptable performance.