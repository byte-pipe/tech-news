---
title: Shutting down our public encrypted DNS servers and sponsoring Quad9 instead | Mullvad VPN
url: https://mullvad.net/en/blog/shutting-down-our-public-encrypted-dns-servers-and-sponsoring-quad9-instead
site_name: hnrss
content_file: hnrss-shutting-down-our-public-encrypted-dns-servers-and
fetched_at: '2026-09-04T21:15:15.227555'
original_url: https://mullvad.net/en/blog/shutting-down-our-public-encrypted-dns-servers-and-sponsoring-quad9-instead
date: '2026-09-04'
description: Mullvad has operated public encrypted DNS (DoH) servers since 2022. They are unnecessary when using Mullvad VPN — traffic is already encrypted and Mullvad VPN's internal DNS handles all queries.
tags:
- hackernews
- hnrss
---

# Shutting down our public encrypted DNS servers and sponsoring Quad9 instead

 

September 3, 2026News

 

Mullvad has operated public encrypted DNS (DoH) servers since 2022. They are unnecessary when using Mullvad VPN — traffic is already encrypted and Mullvad VPN's internal DNS handles all queries.

Outside the VPN, they serve two purposes:

* Mullvad Browser uses them by default when you're not on Mullvad VPN, preventing your ISP from seeing the domains you visit.
* Anyone can use them as a free public service to protect their DNS queries.

We want a public service to be available. Going forward, we will supportQuad9instead of running it ourselves. Running a privacy-focused public DNS service is a highly specialized undertaking, and the Quad9 Foundation is the undisputed leader in the field. Rather than duplicating their efforts to achieve only part of what they do, we're putting those resources toward financially supporting Quad9 instead.

## Migrating to Quad9

If you have manually configured our DoH servers, switch beforeNovember 2nd 2026. You can followQuad9 guides.

### Mullvad Browser

Mullvad Browser users who have kept the default DoH settings or the included ad blocking one, will automatically be migrated to Quad9.

If you have customized the DoH, we will not change them. If you have manually configured a variant of the Mullvad DoH (base, extended, family. etc.), please make sure to change it back to the default.

### iOS and macOS profiles

Any existing iOS and macOS Mullvad DoH profile will stop working, please make sure to replace them withQuad9 iOS profilesormacOS profiles.