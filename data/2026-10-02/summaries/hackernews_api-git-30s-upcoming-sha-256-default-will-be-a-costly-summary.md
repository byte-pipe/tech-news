---
title: "Git 3.0's upcoming SHA-256 default will be a costly mistake | Butler's Log"
url: https://blog.gitbutler.com/git-3-sha-256
date: 2026-10-01
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-02T16:35:01.694751
---

# Git 3.0's upcoming SHA-256 default will be a costly mistake | Butler's Log

## Git 3.0's Upcoming SHA-256 Default: A Costly Mistake

Git 3.0 is set to introduce a new, costly default content hashing algorithm: SHA-256. This change is expected to cause significant time and angst for little practical benefit, with virtually no one knowing what's coming.

### Overview of Git's Content Addressable Database

Git stores and transmits data as a content addressable database, utilizing SHA-1 hashes as keys. This means the same file content is not stored twice, and commits encode the hash of the previous commit in a way that ensures integrity and propagation.

### SHA-1 in Git: A Brief Primer

SHA-1 is a widely used and relatively fast hashing algorithm, suitable for Git's needs. It's been used since Git's inception in 2005 and has not suffered from collisions like SHA-1 does.

### The Problem with SHA-1

SHA-1's 160-bit output has a birthday bound, which means it's prone to collisions. This has been identified in the Git community, resulting in the publication of collision attacks.

### The Future of Git: SHA-256

Git 3.0 plans to replace SHA-1 with SHA-256 as its default content hashing algorithm. This change is intended to be valueless and avoidable.

### Potential Downside: Costly Implementation

Implementing SHA-256 will require changes across the Git ecosystem, including updates to repositories, scripts, and users' software. This may lead to unexpected costs and frustrations.

### Conclusion

Git 3.0's introduction of a new SHA-256 default hashing algorithm will introduce significant challenges and costs. While the shift is expected to maintain Git's reliability and integrity, its implementation may not be straightforward or beneficial in the long run.