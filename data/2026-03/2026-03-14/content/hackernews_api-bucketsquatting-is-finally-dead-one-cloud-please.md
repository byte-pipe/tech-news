---
title: Bucketsquatting is (Finally) Dead – One Cloud Please
url: https://onecloudplease.com/blog/bucketsquatting-is-finally-dead
site_name: hackernews_api
content_file: hackernews_api-bucketsquatting-is-finally-dead-one-cloud-please
fetched_at: '2026-03-14T06:00:13.758753'
original_url: https://onecloudplease.com/blog/bucketsquatting-is-finally-dead
author: boyter
date: '2026-03-13'
description: For a decade, I have been working with AWS and third-party security teams to resolve bucketsquatting / bucketsniping issues in AWS S3. Finally, I am happy to say AWS now has a solution to the problem, and it changes the way you should name your buckets.
tags:
- hackernews
- trending
---

# Bucketsquatting is (Finally) Dead

13 March 2026

For a decade, I have been working with AWS and third-party security teams to resolve bucketsquatting / bucketsniping issues in AWS S3. Finally, I am happy to say AWS now has a solution to the problem, and it changes the way you should name your buckets.

## What is Bucketsquatting?

Bucketsquatting (or sometimes called bucketsniping) is an issue I first wrote about in 2019, and it has been a recurring issue in AWS S3 ever since. If you’re interested in the specifics of the problem, I recommend you check out my original post on the topic:S3 Bucket Namesquatting - Abusing predictable S3 bucket names. In short, the problem is that S3 bucket names are globally unique, and if the owner of a bucket deletes it, that name becomes available for anyone else to register. This can lead to a situation where an attacker can register a bucket with the same name as a previously deleted bucket and potentially gain access to sensitive data or disrupt services that rely on that bucket.

Additionally, it is a common practice for organizations to use predictable naming conventions for their buckets, such as appending the AWS region name to the end of the bucket name (e.g.myapp-us-east-1), which can make it easier for attackers to guess and register buckets that may have been previously used. This latter practice is one that AWS’ internal teams commonly fall victim to, and it is one that I have been working with the AWS Security Outreach team to address for almost a decade now across dozens of individual communications.

## A new namespace

To address this issue, AWS has introduced a new protection that works effectively as a “namespace” for S3 buckets. The namespace syntax is as follows:

<yourprefix>-<accountid>-<region>-an

For example, if your account ID is123456789012, your prefix ismyapp, and you want to create a bucket in theus-west-2region, you would name your bucket as follows:

myapp-123456789012-us-west-2-an

Though not explicitly mentioned, the-anhere refers to the “account namespace”. This new syntax ensures that only the account that owns the namespace can create buckets with that name, effectively preventing bucketsquatting attacks. If another account tries to create a bucket with the same name, they will receive anInvalidBucketNamespaceerror message indicating that the bucket name is already in use. Account owners will also receive anInvalidBucketNamespaceerror if they try to create a bucket where the bucket region does not match the region specified in the bucket name.

Interestingly, theguidancefrom AWS is that this namespace isrecommended to be used by default. Namespacesaren’t newto S3, with suffixes like.mrap,--x-s3, and-s3aliasall being examples of existing namespaces that AWS previously used for new features; however, this is the first time AWS has introduced a namespace that is recommended for general use by customers to protect against a specific security issue.

It is AWS’ stance that all buckets should use this namespace pattern, unless you have a compelling reason not to (hint: there aren’t many). To this end, AWS is allowing security administrators to set policies that require the use of this namespace through the use of a new condition keys3:x-amz-bucket-namespace, which can be applied within an Organization’s SCP policies to enforce the use of this protection across an organization.

This doesn’t retroactively protect any existing buckets (or published templates that use a region prefix/suffix pattern without the namespace), but it does provide a strong protection for new buckets going forward (okay, so it’sdying, not dead). If you wish to protect your existing buckets, you’ll need to create new buckets with the namespace pattern and migrate your data to those buckets.

## What about the other cloud providers?

While AWS has introduced this new namespace protection for S3 buckets, the other major cloud providers handle things slightly differently.

Google Cloud Storage already has a namespace concept in place for its buckets, which is based ondomain name verification. This means that only the owner of a domain can create buckets with names that are of a domain name format (e.g.myapp.com), and they must verify ownership of the domain before they can create buckets with that name. Bucketsquatting is still possible with non-domain name formatted buckets, but the use of domain name formatted buckets is Google’s solution to the issue.

For Azure Blob Storage,storage accountsare scoped with a configurable account name and container name, so the same issue does apply. This is further exacerbated by the fact that Azure’s storage account names have a maximum of 24 characters, leaving a fairly small namespace for organizations to work with.(h/tvhabfor pointing this out)

## tl;dr

There is a new namespace for S3 buckets. The namespace protects you from bucketsquatting attacks, and you should use it for any S3 buckets you create.

If you liked what I’ve written, or want to hear more on this topic, reach out to me onLinkedInor𝕏.