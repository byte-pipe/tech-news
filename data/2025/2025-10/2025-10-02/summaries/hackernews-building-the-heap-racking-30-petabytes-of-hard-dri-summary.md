---
title: Building the heap: racking 30 petabytes of hard drives for pretraining | blog
url: https://si.inc/posts/the-heap/
date: 2025-10-02
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-02T11:11:04.168832
screenshot: hackernews-building-the-heap-racking-30-petabytes-of-hard-dri.png
---

# Building the heap: racking 30 petabytes of hard drives for pretraining | blog

**Building the Heap: Racking 30 Petabytes of Hard Drives for Pretraining**

We built a storage cluster in downtown San Francisco to store approximately 90 million hours of video data. To train pre-training models, we needed significant storage capacity.

**Why This Was Necessary**

* Cloud providers focus on redundancy, availability, and data integrity, which are not as crucial for training AI data.
* We don't need AWS's guarantee of reliability; a local datacenter with 2 redundant nodes is sufficient.
* Storage pricing is often higher than the cost of the service itself.

**Data Usage Considerations**

* Data can be lost with a loss of up to 5%.
* Most companies use limited storage (e.g., Discord under 1 petabyte).
* The use of large amounts of data increases the storage costs.

**The Decision Process**

* We weighed the cost against the benefits of pretraining in-house.
* Internet Archive had similar issues but chose an on-site solution with lower upfront costs and reduced setup fees.
