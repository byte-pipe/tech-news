---
title: Let's Encrypt is adding two additional remote perspectives for domain validation - API Announcements - Let's Encrypt Community Support
url: https://community.letsencrypt.org/t/lets-encrypt-is-adding-two-additional-remote-perspectives-for-domain-validation/252166
site_name: hnrss
content_file: hnrss-lets-encrypt-is-adding-two-additional-remote-persp
fetched_at: '2026-10-19T22:49:57.588148'
original_url: https://community.letsencrypt.org/t/lets-encrypt-is-adding-two-additional-remote-perspectives-for-domain-validation/252166
date: '2026-10-19'
published_date: '2026-10-15T14:14:49+00:00'
description: Hey everybody, Let's Encrypt is adding two new remote perspectives for domain validation. This change is motivated by the fact that increased perspectives provide more domain validation security and is required by the B…
tags:
- hackernews
- hnrss
---

# Let's Encrypt is adding two additional remote perspectives for domain validation

API Announcements

Phil

 October 15, 2026, 2:14pm
 

1

Hey everybody,

Let's Encrypt is adding two new remote perspectives for domain validation. This change is motivated by the fact that increased perspectives provide more domain validation security and is required by theBaseline Requirementswhich is quoted below. Increasing the number and coverage of our domain validation perspectives improves visibility and protection against BGP attacks.

BR 3.2.2.9 Multi Perspective Issuance CorroborationEffective 2026-12-15, the CA MUST implement Multi-Perspective Issuance Corroboration using at least five (5) remote Network Perspectives. The CA MUST ensure that the requirements defined in Quorum Requirements Table are satisfied, and the remote Network Perspectives that corroborate the Primary Network Perspective fall within the service regions of at least two (2) distinct Regional Internet Registries. If the requirements are not satisfied, then the CA MUST NOT proceed with issuance of the Certificate.

During domain validation, this means that we will make seven total validation requests, one from the primary datacenter and six from remote perspectives(previously four). For validation to succeed, the primary server and a quorum of remote perspectives must receive the correct challenge response. This makes it more difficult for attackers to hijack validation requests. To learn more about multi-perspective domain validation, please seeour earlier blog postwhen Let's Encrypt first added new perspectives.

We expect little to no impact to users. Let's Encrypt will begin performing domain validation with the new regions in staging onTuesday, October 27th, 2026. Assuming all goes well, we will do the production rollout onTuesday, November 10th, 2026. Updates will be posted in this thread.

Happy issuance!

13 Likes

### Related topics

Topic

Replies

Views

Activity

Let's Encrypt is adding two new remote perspectives for domain validation

API Announcements

2

8298

 March 27, 2024
 

Multi-Perspective Validation & Geoblocking FAQ

Issuance Tech

6

7810

 May 16, 2024
 

Let’s Encrypt Domain Multiple Perspective Validation Ordering Change

API Announcements

0

752

 June 13, 2024
 

Unexpected renewal failures since April 2024? Please read this!

Help

0

28603

 April 19, 2024
 

ACME v1/v2: Validating challenges from multiple network vantage points

API Announcements

5

49276

 June 23, 2020