---
title: Adding linear-time lookbehinds to RE2 – SYSTEMF @ EPFL
url: https://systemf.epfl.ch/blog/re2-lookbehinds/
date: 2025-06-22
site: lobsters
model: llama3.2:1b
summarized_at: 2025-06-22T23:33:11.982391
---

# Adding linear-time lookbehinds to RE2 – SYSTEMF @ EPFL

**Analysis**

The article discusses adding captureless lookbehinds to the RE2 linear-time regex engine. The problem at hand is solving modern regex features like alternations, loops, backreferences, possessive groups, recursion, conditionals, and bounded/unbounded lookarounds.

* **What's being discussed**: People/businesses pay to solve boring problems in regex (e.g., handling complex matches).
* **Market indicators**:
	+ User adoption: The article mentions the popularity of RE2 as a "fast, safe, thread-friendly alternative" to backtracking engines.
	+ Revenue mentions: No specific revenue numbers are provided.
	+ Growth metrics: None mentioned.
	+ Customer pain points: The authors mention that some regex features can make regular expressions look too complex and frustrating for users, particularly if they need to handle deep matching capabilities.
* **Technical feasibility**: The complexity of modern regex features is not fully known. However, this article suggests that a solo developer with basic knowledge and experience in linear programming, C++, and possibly OCaml or V8 can implement this solution without relying on backtracking algorithms (worst-case exponential complexity). The example given to illustrate the approach is also an interesting demonstration of how feasible it is.
* **Business viability signals**: As long as there are paying users willing to pay for a solution that addresses complex regex issues, existing competition in the market can absorb potential risks. Additionally, distribution channels like npm, GitHub, or source code repositories can help increase visibility.

**Actionable insights**

1.  **Determine technical feasibility**: It is achievable with relatively basic knowledge and skills.
2.  **Business viability assessment**: As long as there are paying users or opportunities for them to support the solution, it's feasible; existing competition is absorbed by potential buyers.
3.  **Revenue model consideration**: Consider offering premium services that provide additional support and assistance when needed; however, this will depend on your target market.

**Extracted numbers, quotes about pain points, and mentions of pricing or revenue**

*   "Surprisingly, the complexity characteristics of these modern regex features are not fully known."
*   No user adoption numbers were provided in the article.
*   A user commented saying that they have to deal with too much complex regex functionality in their projects (unquote).
*   A specific pain point mentioned is that some users struggle to handle deep matches, but this will be addressed by providing an easier-to-use solution.

**Possible implementation path for a solo developer**

1.  Choose a programming language and text editor.
2.  Learn about linear programming using a simple example or library.
3.  Experiment with creating automata (such as NFA simulations) and check their behavior in your regexes.

The provided article doesn't explicitly mention price, but it could be used to create an upsell for premium services focusing on regular expression support for clients who need more complex functionality.
