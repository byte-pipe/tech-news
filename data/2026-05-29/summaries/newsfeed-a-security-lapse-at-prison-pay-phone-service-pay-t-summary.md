---
title: "A security lapse at prison pay phone service Pay Tel publicly exposed over 300K callers' driver's licenses | TechCrunch"
url: https://techcrunch.com/2026/05/28/a-security-lapse-at-prison-payphone-service-pay-tel-publicly-exposed-over-300000-callers-drivers-licenses/
date: 2026-05-28
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-05-29T04:36:41.674508
---

# A security lapse at prison pay phone service Pay Tel publicly exposed over 300K callers' driver's licenses | TechCrunch

# Summary of “A security lapse at prison pay phone service Pay Tel publicly exposed over 300K callers’ driver’s licenses”

## Incident overview
- Pay Tel, a provider of tablets and communication devices for U.S. prisons, had an Azure cloud storage server that was publicly accessible without authentication.  
- The server stored at least **300,000 driver’s‑license scans**, other government‑issued ID documents, profile photos, inmate text messages, handwritten notes, and financial records.  

## Discovery and response
- Security research firm **UpGuard** identified the exposed server and detailed the findings in a blog post.  
- UpGuard notified Pay Tel on **May 7** and followed up a few days later; the company subsequently secured the server.  
- Pay Tel has **not publicly acknowledged** the breach.  

## Impact and details
- Exposed data includes personal identification documents and communications of Pay Tel customers (inmates and their contacts).  
- Many uploaded photos contained **geolocation metadata** precise enough to reveal the subjects’ home addresses.  
- This is Pay Tel’s **second known security incident** in as many years, following a ransomware attack in **June 2025**.  

## Company and regulatory response
- Pay Tel President **Vincent Townsend** did not respond to TechCrunch inquiries.  
- It is unclear whether Pay Tel will **notify affected individuals** or **alert state attorneys general** as required by U.S. data‑breach notification laws.  
- TechCrunch could not determine who is responsible for cybersecurity within Pay Tel.  

## Broader context
- The breach exemplifies a recent pattern of tech companies **misconfiguring cloud services**, leaving sensitive personal data exposed on the open internet.  
- UpGuard’s findings underscore ongoing challenges in adhering to **cybersecurity best practices**.  

## Author information
- Article written by **Zack Whittaker**, Security Editor at TechCrunch.  
- Contact: encrypted Signal (zackwhittaker.1337) or email (zack.whittaker@techcrunch.com).