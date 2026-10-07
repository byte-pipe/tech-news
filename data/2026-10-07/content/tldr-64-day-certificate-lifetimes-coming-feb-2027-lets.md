---
title: 64-Day Certificate Lifetimes Coming Feb 2027 - Let's Encrypt
url: https://letsencrypt.org/2026/10/07/64-day-certs.html
site_name: tldr
content_file: tldr-64-day-certificate-lifetimes-coming-feb-2027-lets
fetched_at: '2026-10-07T23:28:45.927198'
original_url: https://letsencrypt.org/2026/10/07/64-day-certs.html
date: '2026-10-07'
description: On February 10, 2027, all Let’s Encrypt subscribers will move to certificates with 64 day lifetimes by default unless they select an even shorter lifetime (45 or 6 days, as previously announced). This means that any certificate we issue or renew on and after that date will have a 64 day validity period, and we expect the last 90-day certificate to expire on May 11, 2027. We will not revoke valid certificates as a part of this process.
tags:
- tldr
---

Blog

# 64-Day Certificate Lifetimes Coming Feb 2027

 By Sarah Gran · 
 
 
 
 
October 7, 2026

On February 10, 2027, all Let’s Encrypt subscribers will move to certificates with 64 day lifetimes by default unless theyselectan even shorter lifetime (45 or 6 days, aspreviously announced). This means that any certificate we issue or renew on and after that date will have a 64 day validity period, and we expect the last 90-day certificate to expire on May 11, 2027. We will not revoke valid certificates as a part of this process.

We will switch to issuing 64 day certificates in ourstaging environmenton October 14, 2026 to enable testing. We recommend testing in staging before the change takes effect in production.

If your renewals are automated and your client supports ACME Renewal Info (ARI), you should be all set since ARI allows Let’s Encrypt to tell your client when to renew (you can review your ACME client’s documentation to determine if ARI is implemented).

If your renewals are hard-coded to a date from expiration you should update them to renew at approximately ⅔ of the lifetime instead. Taking this step in preparation for 64 day lifetimes will lay the groundwork for default lifetimes of45 days in 2028. Grep for common hardcoded numbers like 83, 80 or 60 in cron jobs, wrapper scripts and runbooks if you’re not sure.

We will also be reducing the authorization reuse period from 30 days to 10 days. In 2028, the reuse period will shrink to seven hours. We are making this change to comply with a 2029 reduction in maximum validation reuse periods, and to remove the need for “CAA rechecking”, where we have to repeat part of the validation process if the validation data is more than 7 hours old. Unless you have specifically designed your ACME client to rely on validation reuse, you will not need to make any changes.

This is also an opportunity to automate certificate management processes like reload and deployment and to add alerting for renewal failures.

Rate limits will not be impacted by this change; you can learn more in our previousblog post.

This change will not affect ACME endpoints or our issuance chains.

We are moving to shorter certificate lifetimes because this reduces the risk of key compromise and mis-issuance. As a nonprofit we see it as part of our mission to make this change to advance security for everyone using the Web globally. We anticipate a smooth transition, but if you experience issues, ourcommunity forumanddocumentationare good resources.

### Support Our Work

ISRG is a 501(c)(3) nonprofit organization that is 100% supported through the generosity of those who share our vision for ubiquitous, open Internet security. If you'd like to support our work, please considergetting involved,donating, or encouraging your company tobecome a sponsor.