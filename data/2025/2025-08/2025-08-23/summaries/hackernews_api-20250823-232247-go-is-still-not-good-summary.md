---
title: Go is still not good
url: https://blog.habets.se/2025/07/Go-is-still-not-good.html
date: 2025-08-22
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-08-23T23:22:47.959580
---

# Go is still not good

**Analysis of the article**

The author's concern with Go programming is centered around its design and implementation, specifically regarding variable scope, nullability, and portability. They criticize Go for forcing programmers to write code that they feel unnecessary or redundant.

**Market indicators:**

* The author mentions that despite Go being a dominant language in Rust, Swift, and Kotlin, it still lags behind in terms of user adoption and revenue.
* There are no specific user adoption metrics mentioned, but the author implies that Go is not widely used, as exemplified by the "two billion dollar mistake" made with its first version.

**Technical feasibility:**

* The complexity of Go's language design lies in its unique features like explicit nullability and optional references. For a solo developer, this may increase time invested in learning and understanding these aspects.
* However, some parts of the code, as mentioned in the article, are simple enough to be easily readable without excessive boilerplate.

**Business viability signals:**

* The author mentions a lack of willingness to pay for Go's portability features (e.g., its inability to handle conditional compilation).
* There is no mention of existing competitors that offer similar or better alternatives.
* Comments suggest that maintaining portability might lead to unnecessary effort, which could impact the developer's motivation to continue using the language.

**Specific numbers:**

* The article provides an anecdote about the "two billion dollar mistake" with Go's null handling feature, implying significant financial investment in this aspect.
* A notable comment mentions that if the author had chosen a different programming language for their project, they would have saved time and effort.

**Quotes from pain points:**

* "Why does the scope oferrextend way beyond where it’s relevant?" - This line highlights the frustration experienced by some developers who feel their code is overly verbose due to repeated checks.
* "The two billion dollar mistake, so they decided to havetwoflavors ofNULL." - As mentioned above, this example illustrates the lack of attention paid to user-centered design.

**Actionable insights for building a profitable solo developer business:**

1. **Proactively manage scope**: Regularly review and refactor code to reduce unnecessary verbosity.
2. **Prioritize nullability**: Understand when nullability is truly needed and implement it carefully, rather than relying on forced usage of `err` variables everywhere.
3. **Optimize for maintainability**: Consider using alternative solutions or tools that address specific pain points mentioned in the article (e.g., portability, conditional compilation).
4. **Understand the market**: Stay up-to-date with Go's growth and user adoption to ensure continued relevance as a developer.

By addressing these concerns, solos can improve the stability, maintainability, and profit of their solo development projects.
