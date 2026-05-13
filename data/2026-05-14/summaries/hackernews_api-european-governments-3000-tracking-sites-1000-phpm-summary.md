---
title: European governments: 3.000 tracking sites, 1.000 phpMyAdmins, and 99% poorly encrypted email. Introducing SecurityBaseline.eu - Internet Cleanup Foun...
url: https://internetcleanup.foundation/2026/05/european-governments-3000-tracking-sites-1000-phpmyadmins-and-99pct-poorly-encrypted-email-introducing-securitybaseline-eu/
date: 2026-05-13
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-14T06:02:07.555953
---

# European governments: 3.000 tracking sites, 1.000 phpMyAdmins, and 99% poorly encrypted email. Introducing SecurityBaseline.eu - Internet Cleanup Foun...

# European governments: 3.000 tracking sites, 1.000 phpMyAdmins, and 99 % poorly encrypted email – Introducing SecurityBaseline.eu

## Launch and purpose
- SecurityBaseline.eu was launched on 13 May 2026 as a spin‑off of the Dutch “Basisbeveiliging”, a decade‑old baseline‑security monitor that is part of governmental policy.  
- Prior to launch we sent tens of thousands of e‑mails to European governments, giving them time to review the forthcoming results.  
- The platform aims to make web‑security data transparent, allowing governments to protect citizens, set internal requirements, and influence national standards.

## What we monitor and how we visualise
- **Web Security Map** software, developed for over ten years, powers the service and presents results on colour‑coded maps (red = issue, orange = warning, green = no issue, gray = no data).  
- We cover all EU member states plus EEA countries (32 in total, excluding the United Kingdom) and treat the EU itself as a “country” for pan‑European mapping.  
- The 32 jurisdictions are represented by 87 regional maps (municipalities, provinces, etc.), each layered with 21 security metrics.  
- Every night all 1 827 maps are rebuilt from data collected across ~200 000 internet domains belonging to ~67 000 local governments.  
- Although the true number of governmental domains is likely ten times higher, we focus on the most important sites: homepages and their subdomains.

## Traffic‑light map interpretation
- A single issue turns a region orange or red; there is no relative grading—security is absolute.  
- Gray indicates that no online address was found for the region.  
- Example highlights:
  - Denmark: mostly orange municipalities, indicating policies are in place.  
  - Italy: many green municipalities because sites are hosted as subdomains, shifting issues upward.  
  - EU CSIRT organisations: all red, due to a deliberately stricter linking rule.  
  - The Netherlands: mixed green, orange, and red, reflecting active policies and measurements from Basisbeveiliging and Internet.nl.

## Three worrisome metrics
1. **3 000+ governmental sites use tracking cookies illegally**  
   - 3 081 European government sites place tracking cookies without the informed consent required by GDPR.  
   - The practice is unnecessary for public services and often stems from easy‑to‑use modern tools that embed advertising‑related tracking.  
   - The EDRi foundation provides guidance for developers to create privacy‑friendly sites.

2. **Over 1 000 publicly reachable phpMyAdmin/database interfaces**  
   - (Details omitted in the excerpt but highlighted as a dangerous exposure.)

3. **99 % of governmental e‑mail is poorly encrypted**  
   - (Details omitted in the excerpt but highlighted as a critical confidentiality risk.)

## Call to action
- We invite readers who value transparency, security, sovereignty, accessibility, and privacy to join the Internet Cleanup Foundation as researchers or members.  
- The foundation already monitors over 80 000 organisations and 500 000 addresses, making the data publicly available.  
- Interested parties can request membership, contact us, or submit change requests to alter data on the site.