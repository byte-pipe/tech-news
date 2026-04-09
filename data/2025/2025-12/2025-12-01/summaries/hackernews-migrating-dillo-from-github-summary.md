---
title: Migrating Dillo from GitHub
url: https://dillo-browser.org/news/migration-from-github/
date: 2025-12-01
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-01T11:21:41.462856
screenshot: hackernews-migrating-dillo-from-github.png
---

# Migrating Dillo from GitHub

## Migrating Dillo from GitHub to Self-Hosted Server or Multiple Mirrors

### Overview

Roberto Arias Mallo has decided to migrate the Dillo project away from GitHub and establish a self-hosted server with multiple mirrors for easier use, reduced maintenance, and increased reliability.

### Key Points

* The original Dillo website was hosted on gh.dillo.org and a mail server used for development, but lost its domain in 2022.
* Arias Mallo had a copy of the mercurial repository and recovered some material from the old site before losing access to it.
* Initial efforts to use GitHub included uploading code and setting up CI workflows, but issues with JavaScript rendering caused problems.
* The platform is single-point failure controlled by a single entity that can ban repositories or account without notice.

### Situation Analysis

GitHub has been useful for storing Dillo projects and running CI pipelines, but it presents several drawbacks. The frontend cannot be accessed through plain HTML due to JavaScript requirements, the site becomes resource-intensive, and it's a single point of failure. Additionally, the platform slows down over time, requiring high-speed internet connections, and encourages a "push model" over a more nuanced request-based system.

### Proposed Solution

Arias Mallo plans to migrate Dillo from GitHub to a self-hosted server with multiple mirrors, ensuring increased reliability, reduced maintenance, and improved usability. This approach aims to solve recurring problems such as the loss of access to the domain in 2022, provide better control over the platform, improve development efficiency with faster internet connections, and make it easier for users to report issues without being overwhelmed by notifications from a single source.

### Conclusion

By moving away from GitHub, Arias Mallo will take advantage of a self-hosted server or multiple mirrors, allowing Dillo to continue running smoothly while reducing reliance on this potentially single point of failure. This change will enable more control over the platform and better support for users with slow internet connections, ultimately leading to improved overall user experience and continued development success.
