---
title: Why is GitHub UI getting so much slower?
url: https://yoyo-code.com/why-is-github-ui-getting-so-much-slower/
date: 2025-08-10
site: lobsters
model: llama3.2:1b
summarized_at: 2025-08-10T23:17:00.125513
---

# Why is GitHub UI getting so much slower?

Analysis:

The article discusses a frustrating issue with GitHub's UI, particularly with slow webpage loading and performance-related problems. As a solo developer using GitHub to develop its platform, it's clear that the author is struggling with this issue firsthand.

The problem arises from GitHub's use of Turbo Boost preloading and page swapping, which seem to be doing more harm than good in terms of user experience. The author points out specific examples of slow webpage loading times, including a profile for switching between "Conversation" and "Files changed" tabs on a PR, which takes over 5 seconds to load.

The author suggests that the use of Turbo Boost preloading is unnecessary and adds only negative performance, given its frequent use for page swapping. They also point out that the client-side post-processing is taking longer than loading the HTML source code, highlighting an inconsistency in GitHub's development process.

Market indicators:

* User adoption: Despite the frustration with the UI, the author mentions no significant user adoption metrics or sales of their service.
* Revenue: There is no mention of revenue or pricing information for the solo developer business developing at GitHub.
* Growth metrics: The article does not provide any specific growth metrics, such as number of users or feature requests.

Technical feasibility:

* Required skills: Building a reliable and responsive UI requires advanced web development skills, including knowledge of async/await, promises, and performance optimization techniques.
* Time investment: Rebuilding a GitHub dashboard from scratch would require significant time and effort, potentially taking days or weeks to complete for an individual.

Business viability signals:

* Willingness to pay: The author highlights the frustration with the UI but does not directly address pricing or revenue.
* Existing competition: GitHub's robust developer platform already covers many performance-related issues, suggesting that users may be willing to opt out of developing using GitHub due to its own subpar user experience.

Actionable insights:

1. **Prioritize simplicity and ease of use**: As described in the article, simplicity can greatly improve user satisfaction and reduce friction.
2. **Rethink Turbo Boost usage**: The author suggests abandoning Turbo Boost preloading, which could alleviate some page loading issues.
3. **Invest in performance optimization techniques**: Instead of relying on client-side post-processing, consider using server-side rendering or other methods to optimize webpage load times.
4. **Focus on developer experience**: GitHub's platform should prioritize the development experience, providing tools and resources to help developers build faster, cleaner code.

Specific numbers: None mentioned.

Quotes about pain points:

* "That is just one of many performance problems..."
* "I am suffering now"
* "Imagine you have 20 PRs to find out which one introduced a regression..."

Additional notes:

* The article concludes with an option to report the issue, but no clear path for resolving it.
* There are no mentions of any partnerships or collaboration opportunities between GitHub and developers.
