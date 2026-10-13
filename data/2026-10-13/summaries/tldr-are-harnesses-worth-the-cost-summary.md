---
title: Are Harnesses Worth the Cost?
url: https://martinfowler.com/articles/are-harnesses-worth-the-cost.html
date: 2026-10-13
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-13T18:05:01.192501
---

# Are Harnesses Worth the Cost?

# Are Harnesses Worth the Cost?

The article compares the effectiveness of using a behavioral harness with a cost-optimized model for coding agents building an API service. A frontier model, GPT-6 Sol, demonstrated reliable results without the harness, while a cost-optimized model, GPT-6 Luna, struggled to produce consistent outcomes with the harness but achieved acceptable results with it.

## Key Findings

* A behavioral harness did not improve token usage, runtime, or cost for the cost-optimized model, GPT-6 Luna.
* The harness increased token usage, runtime, and cost for the cost-optimized model, GPT-6 Luna.
* Despite achieving 10 of 10 successful runs, GPT-6 Luna still cost 33% less per run ($0.273) with the harness compared to without it ($0.406).

## Implications and Limitations

* The experiment suggests that executable feedback may not be as effective in achieving consistent outcomes with smaller, cost-optimized models.
* The harness is not a silver bullet for dependable results, and its benefits may be offset by higher costs.

## Practical Implications

* This experiment highlights the importance of considering both the benefits and limitations of different approaches to achieve reliable and cost-effective results.
* Engineers and developers should be cautious when adopting new approaches, such as behavioral harnesses, and carefully evaluate the trade-offs to ensure the best outcome for their application.

## Conclusion

The experiment found that a behavioral harness did not provide a significant benefit for the cost-optimized model, GPT-6 Luna, despite its cost-effectiveness. This suggests that executable feedback may not be a reliable way to achieve consistent outcomes with smaller, cost-optimized models. However, the harness still demonstrated value in improving token usage and runtime efficiency.