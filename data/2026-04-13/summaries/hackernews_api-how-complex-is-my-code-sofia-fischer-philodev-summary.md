---
title: How Complex is my Code? · Sofia Fischer; Philodev
url: https://philodev.one/posts/2026-04-code-complexity/
date: 2026-04-07
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-13T06:01:27.585432
---

# How Complex is my Code? · Sofia Fischer; Philodev

# How Complex is my Code?

## What is Complexity?
- Complexity is defined as the amount of resources required to run an algorithm.  
- Resources can include memory, execution time, mental effort to understand the code, and the contextual knowledge needed to grasp its purpose.

## Computational Complexity
- Traditional computer‑science lectures focus on how resource usage (time, memory) grows with input size.  
- Example: `insertion_sort` has O(n²) time because each element may be compared with every other element in the worst case.  
- An alternative `counting_sort` can achieve O(n) time but requires additional steps: finding the maximum value, building a count array, and constructing the result.  
- Lower algorithmic complexity may increase other costs: harder to understand, more documentation needed, and stricter input limitations (e.g., no negative numbers).

## Domain Code Complexity
- For business/domain code, human thinking time and memory are far more valuable than CPU cycles or RAM.  
- A function with many variables (e.g., 50) burdens developers, even if the machine runs it effortlessly.  
- Simple metrics like lines of code are insufficient; even two lines can hide substantial mental effort.

## Cyclomatic Complexity
- Counts linearly independent execution paths (if, for, while, case branches + 1).  
- High cyclomatic complexity correlates with higher defect density and indicates refactoring opportunities.  
- Both `insertion_sort` and `counting_sort` have a cyclomatic complexity of 3 (two loops plus the method entry).  
- This metric does not capture semantic difficulty, required background knowledge, or unintuitive constraints.

## Halstead Complexity
- Models mental effort based on distinct operators and operands.  
- Key formulas:  
  - **Difficulty** = (distinct operators / learning constant) × (total operands / distinct operands)  
  - **Volume** = (total operators + total operands) × log₂(distinct operators + distinct operands)  
  - **Cognitive Complexity** = Difficulty × Volume  
- Calculated results:  
  - `insertion_sort` → difficulty 24, volume 192 → higher cognitive load.  
  - `counting_sort` → difficulty 17.6, volume 230 → lower cognitive load despite larger volume.  
- Halstead captures token reuse density but not conceptual difficulty; the author suggests linguistic factors may be more relevant.

## Linguistic Complexity
- Psycholinguistics identifies predictors of reading difficulty that map to code:  
  - **Familiarity**: Known patterns are processed faster; unfamiliar constructs (e.g., new match statements) increase effort.  
  - **Working‑memory load**: Nested clauses or deeply nested code require holding unresolved structure in mind.  
  - **Coherence**: Clear connections between statements aid comprehension; large gaps between variable declaration and use reduce coherence.  

## Linguistic Complexity Measurements
- The article begins to explore how linguistic metrics could be applied to code, indicating a shift from pure computer‑science measures toward a language‑based understanding of code complexity.