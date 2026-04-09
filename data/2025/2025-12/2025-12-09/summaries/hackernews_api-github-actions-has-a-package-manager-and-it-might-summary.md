---
title: GitHub Actions Has a Package Manager, and It Might Be the Worst | Andrew Nesbitt
url: https://nesbitt.io/2025/12/06/github-actions-package-manager.html
date: 2025-12-08
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-09T11:09:49.559345
screenshot: hackernews_api-github-actions-has-a-package-manager-and-it-might.png
---

# GitHub Actions Has a Package Manager, and It Might Be the Worst | Andrew Nesbitt

**GitHub Actions Package Manager: A Critical Issue**
=====================================================

Introduction

Package managers like npm, Cargo, NuGet, Bundler, Go, and others are crucial pieces of software supply chain security. However, GitHub Actions has a package manager that raises concerns about industry standards.

**Key Findings**

*   GitHub uses a package manager without a lockfile or explicit dependency visibility.
*   Dependencies can change silently with version pinning (`actions/checkout@v4`), breaking reproducibility and stability.
*   GitHub doesn't mitigate all security risks, like transient changes in transitive dependencies.

**Industry Standards Compared**

| Asset    | Package Manager Used in Industry Settings |
|----------|------------------------------------------|
| npm      | Most widely used               |
| Cargo     | Popular alternative              |
| NuGet     | Established system                 |
| Bundler   | Mainstream package manager         |
| Go       | Industry-standard package           |

**GitHub's Resolution**

*   No lockfile or explicit dependency visibility
*   Version pinning, which can cause silent changes

**Mitigations**

No concrete mitigations have been implemented. However, organizations can:

*   Enforce SHA pinning of release tags after publication
*   Limit workflows to verified creators
    *   These measures address top-level dependencies but not transitive ones.

**Conclusion**

GitHub Actions package manager has several shortcomings regarding industry standards and security. The lack of a lockfile means that every run depends on the current workspace state, making it challenging for reproducibility and stability. Moreover, version pinning introduces potential security risks like silent changes in dynamic dependencies.

As a developer or sysadmin, understanding these limitations is crucial to maintaining secure software supply chains. Addressing these concerns in GitHub Actions and exploring external package managers with better support can improve overall software reliability and prevent vulnerabilities.
