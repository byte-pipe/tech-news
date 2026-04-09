---
title: We shouldn’t have needed lockfiles @ tonsky.me
url: https://tonsky.me/blog/lockfiles/
date: 2025-08-07
site: lobsters
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-08-07T23:51:57.644630
---

# We shouldn’t have needed lockfiles @ tonsky.me

This article discusses the problem of dependency management in software development, particularly the use of lockfiles, which the author argues are an unnecessary complication.

1. Problem/Opportunity:
   - The author highlights the problem of managing transitive dependencies, where a library (libpupa) depends on another library (liblupa), which in turn may depend on other libraries. The author argues that this dependency resolution should be deterministic and straightforward, without the need for lockfiles.

2. Market Indicators:
   - The article does not provide specific user adoption, revenue, or growth metrics. However, it does mention that the Java ecosystem has been using Maven for 20 years without the need for lockfiles, suggesting that this is a widespread problem in the software development community.
   - The author also mentions that people "can and do things here for no good reason all the time," indicating that the use of lockfiles may be a common practice without a clear justification.

3. Technical Feasibility for a Solo Developer:
   - The technical complexity involved in managing dependencies without lockfiles seems relatively straightforward, as the author describes a deterministic algorithm for resolving transitive dependencies. This would likely be within the capabilities of a skilled solo developer.
   - The required skills include a good understanding of dependency management, version resolution, and the ability to implement a deterministic algorithm for dependency resolution.

4. Business Viability Signals:
   - The article does not mention any specific pricing or revenue information. However, the author suggests that the problem of dependency management is a "boring" one that people and businesses are willing to pay to solve.
   - The existing competition, such as Maven in the Java ecosystem, suggests that there may be opportunities for a solo developer to provide an alternative solution or approach to dependency management.
   - The author's critique of lockfiles and the potential for a more straightforward, deterministic approach could be a differentiating factor for a solo developer's solution.

In summary, this article highlights a common problem in software development that businesses and developers are likely willing to pay to solve. While the technical complexity may be within the reach of a skilled solo developer, the article does not provide specific business viability signals, such as pricing or revenue information. However, the author's critique of the current practices and the potential for a more streamlined approach could be a promising opportunity for a solo developer to explore.
