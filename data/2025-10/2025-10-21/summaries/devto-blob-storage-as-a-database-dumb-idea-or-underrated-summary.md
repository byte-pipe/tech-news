---
title: Blob Storage as a Database: Dumb Idea or Underrated Trick? - DEV Community
url: https://dev.to/harpreet_singh_c4ea4af253/blob-storage-as-a-database-dumb-idea-or-underrated-trick-1n9p
date: 2025-10-20
site: devto
model: llama3.2:1b
summarized_at: 2025-10-21T11:20:52.936825
screenshot: devto-blob-storage-as-a-database-dumb-idea-or-underrated.png
---

# Blob Storage as a Database: Dumb Idea or Underrated Trick? - DEV Community

*   **Hook**: Everyone tells you to avoid using Azure Blob Storage as a database, so I decided to try it anyway.
*
*  **Concept**: The idea is simple: each record is stored in a blob, and each container is thought of as a table. The blob name serves as the primary key, similar to a user's ID.

The concept has some limitations.

**Benefits**
*   Very cheap: fractions of a cent per GB
*
*   Globally replicated and seamlessly integrated with CDN services
*   Schema-agnostic and flexible storage for various JSON structures
*   Built-in versioning that works similarly to record history

### Pain Points
*   No built-in query engine, so filtering or searching is not straightforward without loading everything
*   Lack of transactions or concurrency handling capabilities
*
*   High latency due to every read/write causing a network call
*   Limited atomic operations

Despite some limitations, I implemented a hybrid approach.

**Tiered Storage**
*   App stores keys and metadata for fast lookups
*   Stores blob data payloads in Blob Storage using local Redis caching as a fallback
*   CDN cache the large batches of data for quick access

This hybrid tactic proved effective.

**Verdict**
Blob Storage won't replace your relational database. It's best used as an intermediate storage layer or for specific, non-relational use cases.
