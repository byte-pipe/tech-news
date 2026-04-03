---
title: Every GitHub Object Has Two IDs | Greptile Blog
url: https://www.greptile.com/blog/github-ids
date: 2026-01-14
site: hackernews
model: llama3.2:1b
summarized_at: 2026-01-14T11:09:13.522886
screenshot: hackernews-every-github-object-has-two-ids-greptile-blog.png
---

# Every GitHub Object Has Two IDs | Greptile Blog

### # Every GitHub Object Has Two IDs | Greptile Blog

#### Introduction
GitHub's API uses two separate ID systems: node IDs for unique objects across its system and database IDs for integer values associated with REST responses. However, when building a feature to add clickable links to GitHub PR comments, we needed both.

#### Problem Description
Our previous approach didn't work due to the mismatch between node and database IDs. I was looking at either backfilling millions of records or migrating our entire database, neither sounds fun.

#### Solution
The key insight was spotting a pattern between node and database IDs: they were almost identical except for their last few characters and different base64 encodings. By decoding just the part after `PRRC_` in node IDs, I found that decoded integers differed by only 798, exactly matching the increment of the database ID.

#### Solution Details
The solution involved:
1. Extracting database IDs from node IDs using a bitmask operation.
2. Identifying a pattern between node and database IDs that led to their difference.

#### Conclusion
By finding this pattern, we could extract the necessary information without having to backfill millions of records or migrate our entire database. The solution simplified our process and reduced complexity.
