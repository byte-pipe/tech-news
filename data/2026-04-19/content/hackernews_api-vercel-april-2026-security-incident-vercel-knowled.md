---
title: Vercel April 2026 security incident | Vercel Knowledge Base
url: https://vercel.com/kb/bulletin/vercel-april-2026-security-incident
site_name: hackernews_api
content_file: hackernews_api-vercel-april-2026-security-incident-vercel-knowled
fetched_at: '2026-04-19T19:40:54.561827'
original_url: https://vercel.com/kb/bulletin/vercel-april-2026-security-incident
author: colesantiago
date: '2026-04-19'
description: We’ve identified a security incident that involved unauthorized access to certain internal Vercel systems.
tags:
- hackernews
- trending
---

# Vercel April 2026 security incident

We’ve identified a security incident that involved unauthorized access to certain internal Vercel systems.

Security Team
 Knowledge Base
/
Security Bulletin
Copy URL

Copy page
Ask AI about this page
2
 min read
Last updated

April 19, 2026

We’ve identified a security incident that involved unauthorized access to certain internal Vercel systems. We are actively investigating, and we have engaged incident response experts to help investigate and remediate. We have notified law enforcement and will update this page as the investigation progresses.

In this bulletin:

* Who is impacted
* Recommendations
* Indicators of compromise (IOCs)

### Who is impacted

At this time, we have identified a limited subset of customers that were impacted and are engaging with them directly.

Our services remain operational, and we will continue to update this page with new information.

### Recommendations

We are taking actions to protect Vercel systems and customers.

Our investigation is ongoing. In the meantime, here are best practices you can follow for peace of mind:

* Review the activity logfor your account and environments for suspicious activity.
* Review and rotate environment variables. Environment variables marked as "sensitive" in Vercel are stored in a manner that prevents them from being read, and we currently do not have evidence that those values were accessed. However, if any of your environment variables contain secrets (API keys, tokens, database credentials, signing keys) that were not marked as sensitive, those values should be treated as potentially exposed and rotated as a priority.
* Take advantage of thesensitive environment variablesfeature going forward, so that secret values are protected from being read in the future.

For support rotating your secrets or other technical support, contact us throughvercel.com/help.

### Indicators of compromise (IOCs)

Our investigation has revealed that the incident originated from a third-party AI tool whose Google Workspace OAuth app was the subject of a broader compromise, potentially affecting hundreds of its users across many organizations.

We are publishing the following IOC to support the wider community in the investigation and vetting of potential malicious activity in their environments. We recommend that Google Workspace Administrators and Google Account owners check for usage of this app immediately.

OAuth App:110671459871-30f1spbu0hptbs60cb4vsmv79i7bbvqj.apps.googleusercontent.com

Was this helpful?

supported.
Send
