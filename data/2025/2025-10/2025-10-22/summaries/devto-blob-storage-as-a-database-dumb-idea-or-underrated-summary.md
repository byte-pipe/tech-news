---
title: Blob Storage as a Database: Dumb Idea or Underrated Trick? - DEV Community
url: https://dev.to/harpreet_singh_c4ea4af253/blob-storage-as-a-database-dumb-idea-or-underrated-trick-1n9p
date: 2025-10-20
site: devto
model: llama3.2:1b
summarized_at: 2025-10-22T11:31:49.014410
screenshot: devto-blob-storage-as-a-database-dumb-idea-or-underrated.png
---

# Blob Storage as a Database: Dumb Idea or Underrated Trick? - DEV Community

**Why I Tried Storing Structured Data in Blobs and What Actually Happened**

### **Summary of Main Points**

* Azure Blob Storage can be used as a storage tier instead of a database
* A hybrid approach combining Redis for metadata, Blob Storage for large data payloads, and CDN edge caching for global distribution

### **Key Points**

* Each record is stored as a blob, and each container acts as an logical table with a primary key (blob name)
* Blob versioning provides a time-travel history for free
* The example provided an .NET minimal implementation of such a design
* The benefits of using Blob Storage include:
	+ Ridiculously cheap storage at fractions of a cent per GB
	+ Globally replicated and easily integrated with CDN
	+ Schema-flexible storage for storing any JSON structure
	+ Built-in versioning as blob versioning acts like record history

### **The Pain Points**

* No query engine, limited transactions or concurrency handling
* High latency due to every read/write being a network call
* Limited atomic operations and metadata scaling becomes slow and costly after tens of thousands of blobs

### **Hybrid Trick**

A hybrid approach using Redis for metadata storage,Blob Storage as the data payload repository, and CDN edge caching handles global distribution efficiently.

### **Conclusion**

While Blob Storage won't replace primary relational databases, it can be an effective storage tier for certain use cases. A hybrid approach combining these components offers a balance between cost-effectiveness, scalability, and performance without pretending Blob Storage is SQL Server.
