---
title: Adding linear-time lookbehinds to RE2 – SYSTEMF @ EPFL
url: https://systemf.epfl.ch/blog/re2-lookbehinds/
date: 2025-06-22
site: lobsters
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-06-22T23:44:03.909630
---

# Adding linear-time lookbehinds to RE2 – SYSTEMF @ EPFL

Here's a 3-4 paragraph analysis of the article from a solo developer business perspective:

The article discusses the problem of adding support for linear-time lookbehinds to the RE2 regular expression engine. Lookbehinds are a complex regex feature that allow matching patterns based on what comes before the current position in the input string. Until recently, supporting lookbehinds required using a backtracking-based regex engine, which can have exponential time complexity for certain patterns.

This presents an opportunity for a solo developer, as the ability to efficiently handle lookbehinds is a valuable feature for many real-world regex use cases. The article cites examples of Google using RE2 in projects like Google Sheets, as well as its adoption in open-source tools like PyTorch and Prometheus. This suggests there is significant market demand and willingness to pay for a regex engine that can handle advanced features like lookbehinds in a performant way.

From a technical feasibility standpoint, the changes required to add lookbehind support to RE2 seem within reach of a skilled solo developer. The article provides a detailed walkthrough of the required changes to the parser, compiler, and NFA engine. While implementing these changes would require strong C++ skills and familiarity with regex internals, the step-by-step guidance provided in the article could enable an experienced developer to tackle this project. The time investment would likely be substantial, but the potential payoff of providing a differentiated, high-performance regex engine could make it a worthwhile endeavor for the right solo developer.

Overall, this article highlights a concrete problem that businesses and developers are facing, and demonstrates that there is a technical path forward to solve it. For a solo developer with the right skills and dedication, adding linear-time lookbehind support to RE2 could be a viable business opportunity, with the potential for widespread adoption and monetization through licensing or integration into other products.
