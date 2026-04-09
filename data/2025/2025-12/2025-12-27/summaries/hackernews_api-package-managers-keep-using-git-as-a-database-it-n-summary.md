---
title: Package managers keep using git as a database, it never works out | Andrew Nesbitt
url: https://nesbitt.io/2025/12/24/package-managers-keep-using-git-as-a-database.html
date: 2025-12-26
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-27T11:18:47.720376
screenshot: hackernews_api-package-managers-keep-using-git-as-a-database-it-n.png
---

# Package managers keep using git as a database, it never works out | Andrew Nesbitt

**Package Managers: The Bane of Git**
=====================================

Despite its promises of version history and review workflows, package managers like Cargo and Homebrew struggle to make them work out. They often lead to resource-intensive download processes that consume a significant amount of time.

### **Cargo**

The crates.io indexing system, which originated as a git repository, now grows exponentially when the registry is large. Users see progress bars showing high deltas but often fail to resolve them fully. This problem worsens in CI environments where entire repositories are downloaded.

| Environment | Reposition |
| --- | --- |
| Stateless | Download full index |
| Stateless CI | Discard metadata |

### **Homebrew (JSON downloads)**

GitHub explicitly asked Homebrew to stop using shallow clones after noticing enormous sizes (331MB). Users' .git folders grew, consuming resources. The switch to JSON updates for tap files was a compromise that reduced update times but increased memory usage.

| Version | New Download Method |
| --- | --- |
| v4.0.0 | json downloads |

### **CocoaPods**

This lightweight package manager hit the limits hard with its Specs repo's 200,000+ podspecs and over 8 months of minutes-consuming CI build times. The team implemented CPU rate limits to prevent sharded repository issues.

| Approach | Benefits |
| --- | --- |
| Full Clone | High resource usage |
| Shallow Clones | CPU limitations |

### **Improvements**

These packages can benefit from:

* Using a more efficient indexing system, e.g., Git's sparse HTTP protocol.
* Reducing the scope of CI jobs to only update dependencies.
* Implementing local caching mechanisms or other optimizations.

While package managers have some drawbacks, they are designed for speed and convenience in many environments, especially in dev teams.
