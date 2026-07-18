---
title: LG monitors silently install software through Windows Update without user consent - VideoCardz.com
url: https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent
site_name: hackernews_api
content_file: hackernews_api-lg-monitors-silently-install-software-through-wind
fetched_at: '2026-07-18T19:27:25.699973'
original_url: https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent
author: baranul
date: '2026-07-18'
published_date: '2026-07-17T13:08:01+00:00'
description: Connecting some LG monitors to a Windows PC may automatically install software that promotes McAfee subscriptions.
tags:
- hackernews
- trending
---

## LG monitors are ‘monitoring’ users

© GamersNexus

Connecting some LG monitors to a Windows PC may automatically install software that promotes McAfee subscriptions. Gamers Nexus reproduced the behavior with an LG UltraGear 34GX900A-B after receiving reports from monitor owners.

Windows Update first installed LG extension and software component packages. Windows Reliability Monitor showed that LG Monitor App Installer appeared one minute later. The installation did not display a consent prompt or require the user to approve the download.

Source: Gamers Nexus

Gamers Nexus tested the application across 32 consecutive system boots. It displayed a McAfee promotion during 31 of them. On the remaining boot, it promoted one of LG’s own monitor utilities. The McAfee popup offered a 30-day trial that would convert into a paid subscription.

### The software can appear on older monitors

The behavior does not appear to be limited to newly purchased displays. Gamers Nexus also received the popup on an LG UltraFine 32UN880-B purchased three years earlier. User complaints about LG Monitor App Installer date back to at least 2024, although the recent increase in reports suggests that more models may now be receiving it.

Source: Gamers Nexus

The Microsoft Store lists access to the internet and all system resources among the application’s capabilities. Gamers Nexus also raised concerns about the broader categories covered by LG’s privacy documents.

### Dell uses a similar Windows installation method

This type of automatic software installation is not limited to LG. Dell also uses Windows Update to deliver Alienware Command Center when Windows detects a compatible Alienware monitor or peripheral. Our own new Alienware monitor repeatedly triggered an application installation after it was connected through DisplayPort. We had to use the same Windows Group Policy setting to block device-associated application downloads.

 
 
View on Threads
 

Users can enable “Prevent automatic download of applications associated with device metadata” under Computer Configuration, Administrative Templates, System and Device Installation. This blocks Windows from automatically downloading applications linked to connected hardware. It may also prevent useful monitor or peripheral software from installing, requiring users to download it manually.

Source:

 
 
 Gamers Nexus
: DO NOT BUY: LG’s Spyware TVs, Monitors, and Wiretapping Concerns 
620,868 views
 
 
 
 
 
Follow us on Google
 
 
 
 
 
 
Set as Preferred Source
 
 
Share