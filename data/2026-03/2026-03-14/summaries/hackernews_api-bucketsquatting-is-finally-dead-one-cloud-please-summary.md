---
title: Bucketsquatting is (Finally) Dead – One Cloud Please
url: https://onecloudplease.com/blog/bucketsquatting-is-finally-dead
date: 2026-03-13
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-14T06:01:39.594793
---

# Bucketsquatting is (Finally) Dead – One Cloud Please

# Bucketsquatting is (Finally) Dead  

## What is Bucketsquatting?  
- Described first in 2019; occurs because S3 bucket names are globally unique.  
- When a bucket is deleted, its name becomes reusable, allowing an attacker to register it and potentially access data or disrupt services.  
- Predictable naming conventions (e.g., appending region names) make it easier for attackers to guess and claim former bucket names.  

## New Namespace Protection  
- AWS introduced a bucket‑namespace syntax: `<prefix>-<accountid>-<region>-an`.  
- Example: `myapp-123456789012-us-west-2-an`.  
- The “‑an” suffix denotes the account namespace; only the owning account can create a bucket with that exact name.  
- Attempts to create a duplicate name or a name with a mismatched region return `InvalidBucketNamespace`.  
- AWS recommends using this pattern by default and provides the condition key `s3:x-amz-bucket-namespace` for organization‑wide SCP enforcement.  
- Existing buckets are not retroactively protected; migration to new namespace‑styled buckets is required for legacy protection.  

## How Other Cloud Providers Handle It  
- **Google Cloud Storage**: Uses domain‑name verification as a namespace; only domain owners can create buckets matching their domain (e.g., `myapp.com`). Non‑domain names remain vulnerable.  
- **Azure Blob Storage**: Storage accounts have configurable names with a 24‑character limit, offering a small namespace; the same squatting risk applies.  

## TL;DR  
- AWS now offers a mandatory‑by‑recommendation namespace (`-an`) for S3 buckets that blocks bucketsquatting.  
- Use the namespace pattern for all new buckets and migrate existing ones if you need the protection.  
- Contact the author on LinkedIn or X for more information.