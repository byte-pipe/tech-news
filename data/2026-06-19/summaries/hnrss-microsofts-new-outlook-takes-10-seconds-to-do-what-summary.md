---
title: "Microsoft's new Outlook takes 10 seconds to do what Outlook Classic does instantly on Windows"
url: https://www.windowslatest.com/2026/06/15/microsofts-new-outlook-takes-10-seconds-to-do-what-outlook-classic-does-instantly-on-windows/
date: 2026-06-18
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-19T01:20:07.731382
---

# Microsoft's new Outlook takes 10 seconds to do what Outlook Classic does instantly on Windows

# Microsoft's new Outlook takes 10 seconds to do what Outlook Classic does instantly on Windows

## Overview
- Windows 11 includes two Outlook clients: the legacy Win32 **Outlook Classic** and the newer **Outlook** built on WebView2 (a Chromium‑based web wrapper).  
- The new Outlook is marketed as the future email client, but it suffers from noticeable performance problems, especially when handling Windows 11 notification clicks.

## Notification delay
- Clicking a notification banner for a new email should open that message directly.  
- **Outlook Classic** opens the targeted email almost instantly.  
- **New Outlook** takes ~10 seconds: the app launches, loads the full inbox, then finally displays the specific email.  
- Opening Outlook from the Start menu and manually selecting the email is faster (≈5 seconds) than using the notification.

## Architecture and resource usage
- New Outlook runs on **WebView2**, requiring multiple processes (WebView2 Manager, Utility, GPU, Service Worker, etc.) versus a single process for Classic.  
- Memory consumption while idle:  
  - New Outlook: 490 – 636 MB  
  - Outlook Classic: 117 – 148 MB (≈4× less)  
- CPU usage while idle:  
  - New Outlook: ~4 %  
  - Outlook Classic: <1 %  
- The extra processes must be resumed and authenticated each time a notification is clicked, contributing to the delay.

## Recent improvements
- **March 2026**: better folder search and shared mailbox access.  
- **May 2026**: auto‑mapped calendar support.  
- **June 2026** (planned): Unified Inbox (Aug 2026), enhanced mail merge, expanded .PST import (Jul 2026).  
- Despite these updates, the speed gap between the two clients remains significant.

## Microsoft’s migration strategy
- Enterprise forced‑opt‑out deadline moved from Apr 2026 to Mar 2027, indicating recognition that the new client isn’t fully ready.  
- Microsoft promotes 15 productivity features (offline access, Copilot integration, faster search, etc.) to encourage migration, many of which Classic already provides.  
- A calendar agenda view for the Notification Center is slated for late 2025, also powered by WebView2, with unknown performance impact.

## Conclusion
- The new Outlook’s WebView2 foundation introduces inherent latency and higher resource consumption compared with the native Outlook Classic.  
- While functional and feature‑rich, the client still lags in responsiveness, particularly for notification handling, and the performance gap is unlikely to close soon without a fundamental architectural change.