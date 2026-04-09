---
title: Less is safer: how Obsidian reduces the risk of supply chain attacks - Obsidian
url: https://obsidian.md/blog/less-is-safer/
date: 2025-09-20
site: hackernews
model: llama3.2:1b
summarized_at: 2025-09-20T11:19:53.300543
---

# Less is safer: how Obsidian reduces the risk of supply chain attacks - Obsidian

**Analysis of the Article**

From a solo developer business perspective, this article highlights Obsidian's approach to reducing the risk of supply chain attacks by:

1. **Reducing dependency numbers**: Obsidian has a low number of dependencies compared to other apps in its category. By relying on open source libraries and implementing them from scratch, they minimize the potential for malicious updates.
2. **Shallow dependency graphs**: Obsidian keeps their dependency graph shallow with few sub-dependencies, reducing the chance of a malicious update slipping through.
3. **Version pinning and lockfiles**: All dependencies are strictly version-pinned and committed with a lockfile, ensuring deterministic installs and a straightforward audit trail.
4. **Slow, deliberate upgrades**: The upgrade process involves reading the changelog line-by-line, checking sub-dependencies, diffing upstream changes, running automated tests across platforms, and committing only after thorough review.

**Technical Feasibility**

The article presents a reasonable technical feasibility plan for a solo developer business:

* Implementing shallow dependency graphs and version pinning can be achieved using JavaScript libraries like `node-dependency-patcher` or `Dependency-Patcher`.
* Using lockfiles for deterministic installs is feasible with modern Node.js frameworks.
* Writing automated tests across platforms and critical user paths to thoroughly review changes would require significant development effort.

**Business Viability Signals**

From a business perspective, the article provides some potential signals:

1. **Willingness to pay**: Obsidian's approach suggests they are willing to invest time and resources into building a secure and private environment for users.
2. **Existing competition**: The fact that Obsidian mentions other apps in its category implies that there is existing competition, which can indicate the feasibility of entering the market.
3. **Community and security researcher attention**: By incorporating measures like review-heavy upgrade cadence, Obsidian demonstrates to security researchers that they take supply chain risk seriously.

**Actionable Insights for Building a Profitable Solo Developer Business**

 actionable insights:

1. Consider implementing a similar approach to reduce your own dependency numbers and increase security.
2. Focus on building open source libraries from scratch or fork them once the license allows it, reducing the risk of malicious updates.
3. Implement version pinning and lockfiles with careful testing and auditing to ensure deterministic installs and a straightforward audit trail.
4. Develop automated tests across platforms and critical user paths to thoroughly review changes.
5. Consider using a slower upgrade cadence or delaying upgrades when necessary to increase the time between releases, giving your ecosystem an early warning window.
6. Monitor supply chain risks closely and be prepared to detect problems proactively, ensuring that you can adapt and correct before users are impacted.

Ultimately, building a profitable solo developer business requires careful consideration of technical feasibility, business viability signals, and actionable insights from articles like this one.
