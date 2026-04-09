---
title: 'Blob Storage as a Database: Dumb Idea or Underrated Trick? - DEV Community'
url: https://dev.to/harpreet_singh_c4ea4af253/blob-storage-as-a-database-dumb-idea-or-underrated-trick-1n9p
site_name: devto
fetched_at: '2025-10-21T11:08:28.401945'
original_url: https://dev.to/harpreet_singh_c4ea4af253/blob-storage-as-a-database-dumb-idea-or-underrated-trick-1n9p
author: Harpreet Singh
date: '2025-10-20'
description: 'Subtitle: Why I Tried Storing Structured Data in Blobs and What Actually Happened 1. The... Tagged with webdev, cloud, azure, database.'
tags: '#webdev, #cloud, #azure, #database'
---

Subtitle:Why I Tried Storing Structured Data in Blobs and What Actually Happened

### 1. The Hook

Everyone tells younotto use Azure Blob Storage as a database. Naturally, I decided to try it anyway.

I had a use case that didn’t justify spinning up SQL or Cosmos DB just some structured, semi-static JSON data I needed to persist cheaply and access globally. Blob Storage seemed too simple to ignore.

So I asked myself:Could I push Blob Storage to act like a database?Spoiler: it kind of worked.

### 2. The Concept

Here’s the basic idea:

* Each record is ablob(for example, a JSON file).
* Each container is alogical table.
* The blob name acts as aprimary key(likeusers/user-123.json).
* Blob versioning gives youtime-travelor history for free.

A minimal .NET example:

var

blob

=

containerClient
.
GetBlobClient
(
$"users/
{
userId
}
.json"
);

await

blob
.
UploadAsync
(
BinaryData
.
FromObjectAsJson
(
user
));

Enter fullscreen mode

Exit fullscreen mode

You can later read it back:

var

blob

=

containerClient
.
GetBlobClient
(
$"users/
{
userId
}
.json"
);

var

data

=

await

blob
.
DownloadContentAsync
();

var

user

=

data
.
Value
.
Content
.
ToObjectFromJson
<
User
>();

Enter fullscreen mode

Exit fullscreen mode

No schema, no migrations, no SQL. Just blobs.

### 3. The Benefits (Why It’s Not Completely Dumb)

* Ridiculously cheap: fractions of a cent per GB.
* Globally replicated: can integrate with CDN.
* Schema-flexible: store any JSON structure.
* Built-in versioning: blob versioning acts like record history.
* Excellent for static or rarely-mutating data: configurations, static datasets, logs, or precomputed AI outputs.

Real-world use case: I stored pre-rendered dashboard snapshots in Blob Storage and served them directly through a CDN. Instant load times, no compute, no database calls.

### 4. The Pain Points (Why ItIsKinda Dumb)

* No query engine: You can’t filter or search without loading everything.
* No transactionsor concurrency handling.
* High latency: Every read/write is a network call.
* Limited atomic operations.
* Metadata scaling: Listing blobs becomes slow and costly after tens of thousands.

At around 50,000 blobs, listing performance dropped noticeably. I ended up adding a lightweight Redis index to keep track of blob keys.

### 5. The Hybrid Trick

Here’s where it got interesting.

What if Blob Storage isn’tthedatabase, buta tierof one?

For example:

App -> Redis index -> Blob for data payload -> CDN edge cache

Enter fullscreen mode

Exit fullscreen mode

This hybrid approach works beautifully:

* Redis stores keys and metadata for fast lookups.
* Blob Storage holds large, immutable payloads.
* CDN handles global caching.

Now you’ve got something fast, cheap, and resilient without pretending Blob Storage is SQL Server.

### 6. The Verdict

Blob Storage won’t replace your relational database. It’s not built for dynamic queries, transactions, or real-time updates.

But as acold-storage layer,append-only log, orversioned config repository, it’s surprisingly elegant. And when combined with in-memory indexes or CDN caching, it can punch far above its weight.

Blob Storage isn’t dumb. It’s just misunderstood.

Used wisely, it can make your architecture simpler, cheaper, and more scalable.

### 7. Optional Extras

If you want to take this further:

* Benchmark upload/download speed with.OpenReadAsync()and parallel uploads.
* Use Azure Functions to auto-index blob metadata.
* Explore Blob Storage versioning for immutable event sourcing.

### Final Thoughts

I wouldn’t recommend building your startup’s core database on blobs. But if you have structured, infrequently-changing data that doesn’t need queries it might just be themost underrated trickin Azure.

What do you think? Would you ever use Blob Storage as a database?

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
