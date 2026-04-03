---
title: Blob Storage as a Database: Dumb Idea or Underrated Trick? - DEV Community
url: https://dev.to/harpreet_singh_c4ea4af253/blob-storage-as-a-database-dumb-idea-or-underrated-trick-1n9p
date: 2025-10-20
site: devto
model: llama3.2:1b
summarized_at: 2025-10-26T11:27:27.651272
screenshot: devto-blob-storage-as-a-database-dumb-idea-or-underrated.png
---

# Blob Storage as a Database: Dumb Idea or Underrated Trick? - DEV Community

**Why I Tried Storing Structured Data in Blobs and What Actually Happened**

### Summary of Key Points:

* Azure Blob Storage can be used as a simple database for structured data.
* Each record is stored in a blob, and each contains a logical table and primary key (blob name).
* Blob versioning provides historical records.
* A minimal .NET example demonstrates how to store and retrieve JSON data using Blob Storage.

### The Benefits:

* Cheaper than traditional databases
* Globally replicated and scalable
* Schema-flexible and flexible in storing any JSON structure
* Built-in versioning similar to record history
* Ideal for static or rarely-mutating data

### The Challenges:

* No query engine, requiring extensive loading of everything
* Lacks transactional capabilities and concurrency handling
* High latency due to network calls
* Limited atomic operations and metadata scaling
* Inefficient database-level usage

### Conclusion on the Hybrid Trick:

* Blob Storage can be used as a tiered database layer by combining Redis for fast lookups with Blob Storage for large, immutable payloads and CDN edge caching.
* This approach offers benefits such as cost savings and global scalability without pretending Blob Storage is SQL Server.

**Structural Output:**

# Why I Tried Storing Structured Data in Blobs

### 1. The Hook
Using Azure Blob Storage as a database was a bold idea, but one worth exploring given the constraints of structured, semi-static JSON data.

### 2. The Concept
Blob Storage's design allows for each record to be stored as a blob, with containers forming logical tables and primary keys acting as blobs names.

A minimal .NET example demonstrates how to store and retrieve JSON data using Blob Storage.

* Each record is stored in a single blob, with each containing the actual value, rather than multiple blobs or files.
* Primary keys act as unique identifiers for each blob (e.g., userId).
* Historical records can be retrieved through versioning.

### 3. The Benefits
The main benefits of using Blob Storage are its lower cost per GB, global replication capabilities, schema flexibility, and built-in versioning.

They offer a lightweight solution for storing static or rarely-mutating data, such as pre-rendered dashboard snapshots in this real-world example.

However, some drawbacks need to be addressed.

### 4. The Challenges
While Blob Storage is not suitable for complex database queries or transactions due to its lack of built-in query engine and concurrency handling capabilities.
It has a higher latency compared to traditional databases due to the network calls required between client applications, CDNs, Redis nodes, and blob storage clients.

Despite these limitations, there are potential scenarios where using Blob Storage as a tiered database layer is beneficial:

* **Redis index**: A lightweight in-memory data store or cache can be used alongside blob storage for fast key lookups.
* **Blob Storage + CDN**: Serving large payloads directly from CDNs while handling latency and query requirements efficiently.

### 5. The Hybrid Trick
In this final step, a hybrid approach is presented where Blob Storage functions as the primary storage tier, containing data, while Redis indexes act as a layer for fast lookups.
A CDN handles serving cache-able contents.
This configuration enables speed, cost savings, and efficiency without pretending Blob Storage is a suitable full-fledged database.

### 6. The Verdict
In conclusion, blob storage cannot replace relational databases due to its limitations in querying, transactions, or real-time updates but can be used effectively as a tiered layer for data-intensive applications.
Best suited for scenarios that require fast lookups, low latency, and cost efficiency.
