---
title: 6-day and IP Address Certificates are Generally Available - Let's Encrypt
url: https://letsencrypt.org/2026/01/15/6day-and-ip-general-availability
site_name: hackernews
fetched_at: '2026-01-17T11:06:42.614645'
original_url: https://letsencrypt.org/2026/01/15/6day-and-ip-general-availability
author: jaas
date: '2026-01-17'
description: Short-lived and IP address certificates are now generally available from Let’s Encrypt. These certificates are valid for 160 hours, just over six days. In order to get a short-lived certificate subscribers simply need to select the ‘shortlived’ certificate profile in their ACME client. Short-lived certificates improve security by requiring more frequent validation and reducing reliance on unreliable revocation mechanisms. If a certificate’s private key is exposed or compromised, revocation has historically been the way to mitigate damage prior to the certificate’s expiration. Unfortunately, revocation is an unreliable system so many relying parties continue to be vulnerable until the certificate expires, a period as long as 90 days. With short-lived certificates that vulnerability window is greatly reduced.
---

Blog

# 6-day and IP Address Certificates are Generally Available

 By Matthew McPherrin ·




January 15, 2026

Short-lived and IP address certificates are now generally available from Let’s Encrypt. These certificates are valid for 160 hours, just over six days. In order to get a short-lived certificate subscribers simply need to select the ‘shortlived’certificate profilein their ACME client.

Short-lived certificates improve security by requiring more frequent validation and reducing reliance on unreliable revocation mechanisms. If a certificate’s private key is exposed or compromised, revocation has historically been the way to mitigate damage prior to the certificate’s expiration. Unfortunately, revocation is an unreliable system so many relying parties continue to be vulnerable until the certificate expires, a period as long as 90 days. With short-lived certificates that vulnerability window is greatly reduced.

Short-lived certificates are opt-in and we have no plan to make them the default at this time. Subscribers that have fully automated their renewal process should be able to switch to short-lived certificates easily if they wish, but we understand that not everyone is in that position and generally comfortable with this significantly shorter lifetime. We hope that over time everyone moves to automated solutions and we can demonstrate that short-lived certificates work well.

Our default certificate lifetimes will be going from 90 days down to 45 days over the next few years,as previously announced.

IP address certificates allow server operators to authenticate TLS connections to IP addresses rather than domain names. Let’s Encrypt supports both IPv4 and IPv6. IP address certificates must be short-lived certificates, a decision we made because IP addresses are more transient than domain names, so validating more frequently is important. You can learn more about our IP address certificates and the use cases for them from ourpost announcing our first IP Certificate.

We’d like to thank the Open Technology Fund and Sovereign Tech Agency, along with ourSponsorsand Donors, for supporting the development of this work.
