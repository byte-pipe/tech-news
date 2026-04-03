---
title: An (almost) catastrophic OpenZFS bug and the humans that made it (and Rust is here too) · blog · despair labs
url: https://despairlabs.com/blog/posts/2025-07-10-an-openzfs-bug-and-the-humans-that-made-it/
date: 2025-07-12
site: lobsters
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-07-12T23:44:44.783762
---

# An (almost) catastrophic OpenZFS bug and the humans that made it (and Rust is here too) · blog · despair labs

This article discusses an (almost) catastrophic bug found in the OpenZFS codebase, and the insights it provides for a solo developer building a profitable business.

Problem/Opportunity:
The article highlights a subtle but critical bug in the `vdev_raidz_asize_to_psize()` function in OpenZFS, which could lead to data corruption if not caught. This type of "silent" bug that can cause serious issues down the line is the kind of problem that businesses and users are willing to pay to solve. Identifying and fixing these types of "boring" but impactful problems is a key opportunity for a solo developer.

Market Indicators:
While the article doesn't provide specific user adoption or revenue numbers for OpenZFS, it does mention that the bug had been present in the main development branch for a couple of months before being caught. This suggests a sizable user base and active development, indicating a potentially large market for tools and services around OpenZFS. The author's experience as a storage admin also highlights the critical nature of these types of bugs and the willingness of users to pay for solutions.

Technical Feasibility:
The article suggests that this type of bug is difficult to catch in C, as there are no "cheap" annotations or static analysis tools that would reliably identify the issue. However, the author proposes that using a language like Rust, with its stronger type system, could help prevent such errors. This suggests that a solo developer with strong Rust skills could potentially build tools or services around improving the reliability and safety of critical storage systems like OpenZFS.

Business Viability:
The article doesn't mention any pricing or revenue figures, but it does highlight the significant impact that such bugs can have on users, particularly in the storage and data management space. This indicates a willingness to pay for solutions that can prevent data loss and corruption. A solo developer could potentially build tools, services, or even consulting offerings around improving the reliability and safety of critical storage systems, leveraging their expertise in Rust and other modern programming languages.

In summary, this article highlights the opportunity for a solo developer to build a profitable business around solving "boring" but impactful problems in the storage and data management space, particularly by leveraging modern programming languages and tools to improve the reliability and safety of critical systems like OpenZFS.
