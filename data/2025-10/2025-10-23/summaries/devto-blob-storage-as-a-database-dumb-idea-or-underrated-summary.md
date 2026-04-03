---
title: Blob Storage as a Database: Dumb Idea or Underrated Trick? - DEV Community
url: https://dev.to/harpreet_singh_c4ea4af253/blob-storage-as-a-database-dumb-idea-or-underrated-trick-1n9p
date: 2025-10-20
site: devto
model: llama3.2:1b
summarized_at: 2025-10-23T11:28:13.675858
screenshot: devto-blob-storage-as-a-database-dumb-idea-or-underrated.png
---

# Blob Storage as a Database: Dumb Idea or Underrated Trick? - DEV Community

**Why We Tried Storing Structured Data in Blobs and What Actually Happened**

This article explores the author's experience trying to use Azure Blob Storage as a database for storing structured data, specifically JSON files.

### Key Points

* The idea of using Blob Storage as a database is relatively simple - each record is stored as a blob (e.g., JSON file), containers are logical tables, and blob names act as primary keys.
* A basic .NET example demonstrates how blobs can be uploaded and retrieved from Azure Blob Storage, including versioning for easy history.
* The author findsBlob Storage to be extremely cheap (<$0.01 GB/year) and globally replicated, making it suitable for static or rarely-mutating data.

### Maintaining Original Perspective

The article maintains a narrative style with occasional insights that clarify the point of view of Azure Blob Storage as a database solution.

### Structured Output

**Title**: Why We Tried Storing Structured Data in Blobs and What Actually Happened
**Introduction**: The author asks why Microsoft suggestedBlob Storage may not be suitable for databases.
**Section 1: Hook**
The article begins with a hook that sets the stage for the main content.

**Section 2: Concept**
A basic idea is presented about how Blob Storage can act as a database, storing structured data in blobs and using container tables as logical entities. The author explores this concept further through an example code snippet.

**Section 3 and 4 ( Benefits )**: The benefits of using Blob Storage for static or rarely-mutating data are discussed, highlighting its advantages such as ridiculous cheap costs (<$0.01 GB/year), global replication, schema flexibility, built-in versioning, and excellent performance for static data.
* **Section 5** (_Hybrid Trick_) explores the author's experience of combining Azure Blob Storage with Redis (as an index) to create a tiered solution.

### Conclusion

The article concludes that while Blob Storage is not suitable as a relational database, it can serve as a cold-storage layer for handling structured data efficiently.
