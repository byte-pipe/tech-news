---
title: netbsd-advocacy: NetBSD and my life...
url: https://mail-index.netbsd.org/netbsd-advocacy/2005/09/10/0000.html
date: 2026-08-22
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-24T07:47:40.407820
---

# netbsd-advocacy: NetBSD and my life...

# NetBSD and my life...

## Introduction
- I am Gary Rolland, a network administrator in the United Kingdom, working in a team of four admins for a large UK‑based company.  
- Our network is mission‑critical; downtime is extremely costly.  
- I have been using NetBSD on my laptop for two years without problems and wanted to deploy it at work.

## Current Infrastructure
- 29 high‑end servers all running NetBSD 2.0.2.  
- Services provided:
  - MySQL databases (majority of traffic).  
  - Apache web servers (internal and external).  
  - Postfix mail handling (~20 accounts).  
  - Samba to allow ~4,800 users to access NFS (file servers run Linux).  
- Daily data handling:
  - Over 870 GB of data transferred.  
  - About 1,200 emails sent, including occasional large attachments.  
  - Peak HTTP load of ~35 requests per minute on PHP‑based sites.

## Problems with the Previous Windows Setup
- Servers frequently crashed, causing emergency call‑outs that interfered with family time.  
- Example: a planned trip to Alton Towers was ruined when Windows servers failed, leading to repeated disappointment for my daughter and tension at home.  
- The instability forced me to argue with my boss and wife, and overall reduced quality of life.

## Migration to NetBSD
- Proposed a trial of two NetBSD servers (one MySQL, one HTTP) to replace failing Windows machines.  
- Installed and configured them overnight using pkgsrc; installation proceeded flawlessly.  
- When Windows MySQL servers later crashed, the NetBSD machines remained stable, convincing the boss to expand the rollout.  
- Gradual migration involved training the other admins, printing the NetBSD handbook, and encouraging home experimentation.

## Impact on Work
- Network now fully runs on NetBSD, providing far greater stability.  
- Reduced on‑call emergencies; weekends can be administered remotely via SSH.  
- Team members have become more proficient with kernel compilation and system configuration.  
- Management is satisfied with the improved reliability.

## Personal Benefits
- Less stress and fewer emergency calls have allowed more time with my family.  
- Relationships with my daughter, her friends, and my wife have improved.  
- I was finally able to enjoy a weekend trip to Alton Towers without work interruptions.

## Conclusion
- NetBSD transformed both the professional environment and my personal life, delivering stability, efficiency, and peace of mind.  
- I am grateful to the NetBSD community for their work and encourage continued development.