---
title: LG smart TVs caught logging audio with screen off and snooping on local devices - Notebookcheck News
url: https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html
site_name: hackernews_api
content_file: hackernews_api-lg-smart-tvs-caught-logging-audio-with-screen-off
fetched_at: '2026-09-08T00:31:03.009339'
original_url: https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html
author: chris_overseas
date: '2026-09-07'
description: An investigation by Gamers Nexus found LG smart TVs sweep local networks to map phones and nearby devices. Tests also showed the sets can capture microphone audio with the screen off — they then upload data once reconnected to the internet.
tags:
- hackernews
- trending
---

LG smart TVs continuously sweep home networks, map secondary devices, and log microphone audio while appearing to be turned off, according to anew 135-minute-long video published by Gamers Nexus(see below).

In more detail, Steve had been working withLevel1Techsand independent security researchers. Together, they tested retail LG OLED models including theG5. Network packet captures taken throughWiresharkshowed the TVs actively scanning the local area network for unrelated hardware, including phones and smartwatches. Apart from internal IP addresses, the sets also gathered the names and signal strengths of neighboring Wi-Fi networks along with location data.

This data collection pool is fed into intoLG Ad Solutions(the company’s targeted advertising arm). LG claims they have roughly 216 million smart TV sales globally. On the other hand, the ad division says it has access to 363 million secondary addressable devices in the US alone by tracking other hardware on the same network. The sets also run Automated Content Recognition (ACR). It samples on-screen audio and video into digital fingerprints to log what users watch across inputs. While ACR has beenwell documentedin the past, new testing shows the data collection goes much further than just that.

During bench tests, they found the TV could capture clean microphone audio while the screen was (or at least looked to be) powered down in standby mode. When the team disconnected the TV from Ethernet, the set continued saving voice input locally and uploaded the stored files once network access was restored.

The researchers also documented remote code execution vulnerabilities inwebOSthat are currently moving through the responsible disclosure process. Because of the fact that the TV uses broad network listeners and data sweeps out of the box, the team's recommendation was straight-up disconnecting LG sets from the internet and using external streaming devices instead.

LG has not commented on any of this as of writing.

## Source(s)

Gamers Nexus on YouTube

⟨
Previous article
Mysterious new Casio G-Shock Frogman GWF-300 appears in official certification database
Next article
Powerful Intel-equipped FEVM mini PC launches with performance Nvidia GPUs
⟩

Add as a preferred source on Google
 
 
 
 
 
 
 
 
 

Read all 4 comments
 / 
answer
 static version 
load dynamic
Loading Comments 
 
 
 
 
 Comment on this article

## Related Articles

Anubhav Sharma
 - Senior Tech Writer 
 - 1963 articles published on Notebookcheck
 since 2024
Most of my time goes into writing - and somehow it hasn’t stopped being fun yet.
My work mainly revolves around everyday tech, gaming, watches, DIY modding, and the occasional piece on tech-policy chaos when companies and governments clash. I try to keep things simple and honest, without sounding like a product brochure.
I have a Bachelor’s degree in Computer Science Engineering and an Associate Degree in English Studies from the College of New Caledonia in British Columbia, Canada.
Away from articles and deadlines, life usually shifts to making music, taking photos, or trying to finish games that should have been completed months ago.
contact me via: 
 @lottamuzic
, 
 LinkedIn

> 
Expert reviews and news on laptops, smartphones and tech innovations
 > 
News
 > 
News Archive
 > 
Newsarchive 2026 09
 > LG smart TVs caught logging audio with screen off and snooping on local devices 
Anubhav Sharma, 2026-09- 7 (Update: 2026-09- 7)