---
title: A proof of the Aaronson-Ambainis conjecture · PSI
url: https://psi.inc/research/aaronson-ambainis
date: 2026-11-08
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-08T09:04:14.916881
---

# A proof of the Aaronson-Ambainis conjecture · PSI

# Aaronson‑Ambainis Conjecture Proven

## Background
- The 2008 conjecture of Scott Aaronson and Andris Ambainis linked exponential quantum speedups to the presence of structure in the input.
- Shor’s algorithm achieves exponential speedup because the input string contains a hidden periodic pattern.
- The open question was whether quantum computers could obtain exponential advantages on random (unstructured) inputs.
- Aaronson and Ambainis reduced this question to a purely mathematical statement about low‑degree bounded polynomials; if the statement holds, classical algorithms can simulate quantum query algorithms up to polynomial factors.

## Proof Announcement
- Physical Superintelligence (PSI) used an internal research system running a non‑public Anthropic model.
- The system generated a complete proof of the conjecture by the third day of the run; the Lean proof assistant verified every step.
- The proof was refined twice, with Lean accepting the final version.
- The argument builds on ideas of Shachar Lovett, Jiapeng Zhang, David Reimer, and others.

## Independent Confirmation
- In August 2026, a Stanford team (Guy Blanc, Jordan Docter, Carmen Strassle, Li‑Yang Tan) proved the conjecture’s prediction for a special case involving a fixed number of parallel query rounds.
- They have reviewed PSI’s full proof, provided comments, and are preparing a shorter exposition for experts, describing the result as “magical” and highlighting its synthesis of Boolean analysis and probabilistic combinatorics.

## Mathematical Core
- A quantum algorithm that makes \(T\) queries induces a polynomial \(p(x)\) of degree at most \(2T\) whose value (between 0 and 1) equals the algorithm’s acceptance probability on input \(x\).
- The conjecture concerns the **influence** of a variable: the average squared change in \(p\) when that bit is flipped.
- Proven statement: for any non‑constant degree‑\(d\) polynomial bounded in \([0,1]\) with variance \(v\), there exists a variable \(i\) such that  
  \[
  \operatorname{Inf}_i(p) \ge c\,\frac{v^{5/2}}{d^{6}} \ge \left(\frac{v}{d}\right)^{7},
  \]  
  where \(c = \frac{815}{125\pi^{4}} \approx 0.0025\).
- This improves earlier bounds that decayed exponentially with the degree and unifies several previously known special cases.

## Implications for Quantum Computing
- A classical algorithm can estimate the quantum acceptance probability with only a polynomial number of input reads for all but a negligible fraction of random strings.
- Consequently, quantum computers cannot achieve exponential query‑complexity speedups on typical decision problems unless the input possesses a rare structure.
- The result narrows the class of problems where exponential quantum advantage is possible.

## Future Directions
- PSI’s system will continue to target related open problems in quantum complexity and the analysis of Boolean functions.
- The forthcoming Stanford exposition will make the proof more accessible to the research community.
- Open questions remain about quantum advantages in models beyond query complexity.