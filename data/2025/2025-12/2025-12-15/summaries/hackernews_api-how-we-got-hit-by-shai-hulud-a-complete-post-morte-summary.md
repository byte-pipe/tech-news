---
title: How we got hit by Shai-Hulud: A complete post-mortem | Trigger.dev
url: https://trigger.dev/blog/shai-hulud-postmortem
date: 2025-12-14
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-15T11:16:47.322619
screenshot: hackernews_api-how-we-got-hit-by-shai-hulud-a-complete-post-morte.png
---

# How we got hit by Shai-Hulud: A complete post-mortem | Trigger.dev

**The Shai-Hulud Attack: A Close Call in the JavaScript Ecosystem**

On November 25th, 2025, a group of engineers at Trigger.dev were hit by a sophisticated npm supply chain worm that compromised over 500 packages and affected 25,000+ repositories. The incident highlighted a concerning new threat in the JavaScript ecosystem.

**The Attack Timeline**

*   November 24, 2025: One engineer ran a command that triggered `pnpm install`, which led to the deployment of Shai-Hulud malware.
*   Around 20:27 UTC (9:27 PM local time in Germany): The malware was executed on a legitimate package in one of Trigger.dev's internal repos.
*   Within seconds, the engineer's Slack channel exploded with notifications due to multiple force-pushes and PR closures across multiple repositories.

**The Attack Mechanics**

*   The Shai-Hulud malware exploited a preinstall script that downloaded TruffleHog, a legitimate security tool repurposed for credential theft, from one of Trigger.dev engineers' machines.
*   The malware scanned the engineer's machine for sensitive information, including GitHub tokens, AWS credentials, npm tokens, and environment variables.

**The Impact**

*   One affected package was responsible for executing the malware, which led to unauthorized access to Trigger.dev's GitHub organization.
*   No Trigger.dev packages were compromised, but npm tools and related libraries may be susceptible to future attacks.

This close call serves as a reminder of the importance of staying vigilant in software development. Developers must be cautious when deploying code and monitoring their dependencies, and implementing robust security measures can help prevent similar attacks.
