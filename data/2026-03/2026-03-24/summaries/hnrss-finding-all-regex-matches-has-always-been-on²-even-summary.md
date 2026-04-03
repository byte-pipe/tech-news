---
title: finding all regex matches has always been O(n²). even in the engines built to prevent it | ian erik varatalu
url: https://iev.ee/blog/the-quadratic-problem-nobody-fixed/
date: 2026-03-19
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-24T20:01:53.180787
---

# finding all regex matches has always been O(n²). even in the engines built to prevent it | ian erik varatalu

# Finding all regex matches has always been O(n²). even in the engines built to prevent it | ian erik varatalu

## Main problem
- All mainstream regex engines (RE2, Go’s regexp, Rust’s regex crate, .NET Non‑Backtracking) guarantee linear‑time **single** match.
- When `find_iter` / `FindAll` is used to locate **all** matches, the guarantee disappears; worst‑case complexity becomes O(m · n²) (m = pattern size, n = input size).
- Example: pattern `.*a|b` on `"bbbbbbbbbb"` forces the engine to scan the remaining text at each position, yielding a triangular sum of work → O(n²).

## Historical context
- Russ Cox (2009) highlighted this quadratic “loop‑around‑a‑DFA” issue; benchmarks show throughput halving when input size doubles.
- Academic regex research often focuses only on the decision problem (“does the string match?”), ignoring the all‑matches case.
- Backtracking engines are even worse (exponential), yet remain the default in many languages; recent ReDoS CVEs (e.g., npm’s `minimatch`) illustrate real‑world impact.

## Prior solutions for special cases
- **Aho‑Corasick (1975)**: linear‑time all‑matches for a set of fixed strings using a trie with failure links; not applicable to full regexes.
- **Hyperscan / Vectorscan**: linear‑time all‑matches with “earliest match” semantics (report as soon as DFA enters a match state). This changes results (e.g., `a+` on `aaaa` yields four short matches instead of one long match), unsuitable for tools expecting leftmost‑longest semantics.
- **REmatch (VLDB 2023)**: enumerates every possible (start, end) span, producing O(n²) output; solves a different problem.

## RE#’s two‑pass algorithm
- First pass (reverse DFA) marks every position where a match **could** start.
- Second pass (forward DFA) resolves the longest (leftmost‑longest) match at each marked position.
- Matches are reported retroactively, eliminating the need to restart the engine at each character.
- Complexity is O(n) for any pattern, regardless of the number of matches; semantics remain POSIX‑compatible (leftmost‑longest, non‑overlapping).

## Hardened mode
- Even with two passes, ambiguous patterns can cause quadratic work within the forward pass.
- RE# introduces a “hardened” mode that guarantees linear time even on adversarial inputs, removing the remaining edge cases.

## Practical significance
- For log parsing, data extraction, or bulk search‑and‑replace, the difference between O(n) and O(n²) translates to “instant” versus “hours”.
- RE# demonstrates that the longstanding quadratic all‑matches problem can be solved without sacrificing expected regex semantics.