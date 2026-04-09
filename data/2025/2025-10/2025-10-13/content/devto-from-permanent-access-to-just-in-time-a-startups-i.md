---
title: 'From Permanent Access to Just-in-Time: A Startup''s IAM Journey Part 1 - DEV Community'
url: https://dev.to/ccscaesar/from-permanent-access-to-just-in-time-a-startups-iam-journey-part-1-4lbn
site_name: devto
fetched_at: '2025-10-13T19:07:37.830145'
original_url: https://dev.to/ccscaesar/from-permanent-access-to-just-in-time-a-startups-iam-journey-part-1-4lbn
author: Caesar Chan
date: '2025-10-10'
description: This post is the first in a 3-part series detailing our journey to secure cloud access. In a FinTech... Tagged with security, aws, identity, startup.
tags: '#security, #aws, #identity, #startup'
---

This post is the first in a 3-part series detailing our journey to secure cloud access.

In a FinTech startup, speed and agility are paramount. But as many of us in the security field know, rapid growth can often lead to "chaos", especially when it comes to cloud infrastructure access. My journey at a startup began with untangling this challenge. We had a classic case of an "always-on" access model, and it was clear we were at risk.

This is the story of how we moved from a state of risky permanent access, to a secure and efficient Just-in-Time (JIT) model.

## The Problem

When we first assessed our AWS environment, we found several security issues that are common in rapidly scaling companies:

* Single-Factor Authentication:Multi-Factor Authentication (MFA) was not universally enforced for our AWS console logins, leaving a gaping hole in our first line of defense.
* Permanent "Always-On" Access:Engineers had a static path directly into both non-production and production environments. Many had generated permanent AWS access keys, which, if leaked, could provide an attacker with a persistent backdoor.
* Overly Permissive Roles:Developers were often granted broad IAM roles with administrative privileges across multiple services and environments.
* No Separation of Duties:A single access path could be used by an engineer to reach every environment, from development all the way to production.
* Lack of Just-in-Time (JIT):There was no system for engineers to request and receive temporary, time-bound access for specific tasks.

This setup was a breeding ground for potential disasters, from account hijacking to insider threats to ransomware and cloud cryptomining.

Leaked AWS credentials quite often leads to "silent compromises", where attackers use stolen keys to encrypt S3 buckets and demand a ransom, all without triggering alerts:

## The Blueprint

We knew we had to act. Our mission was to revamp our IAM strategy completely. We set clear end goals:

* Implement risk-based MFA.
* Eliminate all permanent human access to production.
* Enforce the principle of least privilege for every IAM role.
* Establish a clear separation of duties.

To achieve these, we chose a modern tool-set designed for cloud-native environments:AWS IAM Identity Center,AWS IAM Access Analyzer,Entra ID Privileged Identity Management (PIM)andEntra ID Conditional Access.

We've now covered the security gaps that prompted this project and the high-level blueprint for our new Just-in-Time model.

In the next part of this series, we’ll roll up our sleeves and walk through the detailed, 4-phase implementation plan we followed, from initial AWS configuration to the final cleanup.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
