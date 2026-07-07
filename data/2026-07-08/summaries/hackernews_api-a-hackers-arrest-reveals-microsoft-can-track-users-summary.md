---
title: "A Hacker's Arrest Reveals Microsoft Can Track Users Via a Windows Device ID | PCMag"
url: https://www.pcmag.com/news/a-hackers-arrest-reveals-microsoft-can-track-users-via-a-windows-device
date: 2026-07-07
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-08T01:56:29.582561
---

# A Hacker's Arrest Reveals Microsoft Can Track Users Via a Windows Device ID | PCMag

# Summary of “A Hacker's Arrest Reveals Microsoft Can Track Users Via a Windows Device ID | PCMag”

## Key Incident
- 19‑year‑old Peter Stokes was extradited from Europe and accused of belonging to the Scattered Spider hacking group.  
- Federal investigators linked Stokes to the alleged hack of a luxury jewelry retailer by using Microsoft’s Global Device ID (GDID) records.

## What Is the GDID
- Defined in the criminal complaint as a persistent, device‑level identifier that uniquely identifies a Windows installation on a physical device or virtual machine.  
- The identifier stays the same across Windows updates; it changes only after a full reinstall of Windows on the same or a different device.  
- Example GDID cited in the complaint: **6755467234350028**.

## How Microsoft Records Were Used
- The GDID showed activity at 19:21 UTC on 12 May 2025, accessing the ngrok signup page (`https://dashboard.ngrok.com/signup`).  
- Additional GDID logs indicated connections to multiple sites hosted by the web provider Tzulo, which were used to facilitate the hack.

## Surveillance Concerns
- The complaint reveals that Microsoft can associate a GDID with third‑party services and timestamps, potentially allowing tracking of a Windows PC’s online activity without relying on browser cookies.  
- Experts note that Microsoft could correlate a newly generated GDID with an older one by using other identifiers such as a Microsoft account login or IP address.  
- Some users are already exploring methods to contain or scrub the GDID identifier.

## Resetting the GDID
- According to the court document, a user can reset the GDID only by reinstalling Windows, which generates a new unique GDID.  
- A single Microsoft user may accumulate multiple GDIDs over time due to reinstallations or device changes.

## Wider Implications
- Cybersecurity researcher Costin Raiu questioned whether similar persistent identifiers exist on Apple devices or other platforms, suggesting the issue may not be unique to Microsoft.  
- He recommended that achieving full anonymity might require using Linux, FreeBSD, and routing all traffic through proxies, Tor, or VPNs.

## Author Information
- Article written by Michael Kan, principal reporter at PCMag, covering cybersecurity, satellite internet, PC hardware, and related technology topics.