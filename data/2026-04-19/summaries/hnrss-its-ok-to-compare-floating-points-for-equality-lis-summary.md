---
title: "It's OK to compare floating-points for equality | lisyarus blog"
url: https://lisyarus.github.io/blog/posts/its-ok-to-compare-floating-points-for-equality.html
date: 2026-04-14
site: hnrss
model: llama3.2:1b
summarized_at: 2026-04-19T06:11:39.395624
---

# It's OK to compare floating-points for equality | lisyarus blog

**It's OK to compare floating-points for equality**

The article discusses the limitations and nuances of comparing floating-point numbers for exact equality. While there is a general concern about using epsilon-comparison, which involves identifying a small difference between two values, the author argues that it can be inadequate in many situations.

### Floating-Point Numbers: Not a Black Box

Floating-point numbers are not inherently random or uncertain. They are generated using deterministic rules and standardized systems. The article highlights the fact that no finite amount of memory can represent all possible real numbers due to the limits of mathematics.

### Limitations of Epsilon-Comparison

Epsilon-comparison, as used in many programming languages, involves checking if two floating-point values are identical by computing their absolute difference using a small value like \(1e-4\). However, this approach has some limitations. There is no foolproof way to distinguish between identical and nearly equal floating-point numbers.

### Examples of Poor Solutions

The article provides several examples where epsilon-comparison or other non-equal methods fail. These include:

*   **Arithmetic operations**: When comparing two values using arithmetic operators like addition, multiplication, or exponentiation, the result can be an approximate value close to the actual true answer.
*   **Loops and algorithms**: In various loops and code paths that perform calculations on floating-point numbers, e.g., sorting arrays by key-value pairs, finding closest matches in datasets, or calculating optimal solutions.

### Conclusion: Better Solutions Exist

The author concludes that comparing floating-points using epsilons is not always a better solution. Instead of resorting to epsilon-comparison, it's often more effective and efficient to:

1.  **Use numerical methods**: Implement specific algorithms designed for handling floating-point precision issues.
2.  **Rewrite code iteratively**: Change the code generation process to accommodate exact equality checks when possible.

While epsilon-comparison is not always a bad idea, its limitations should be accounted for in favor of more robust and accurate solutions.