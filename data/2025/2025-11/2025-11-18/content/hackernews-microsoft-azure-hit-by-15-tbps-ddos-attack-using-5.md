---
title: 'Microsoft: Azure hit by 15 Tbps DDoS attack using 500,000 IP addresses'
url: https://www.bleepingcomputer.com/news/microsoft/microsoft-aisuru-botnet-used-500-000-ips-in-15-tbps-azure-ddos-attack/
site_name: hackernews
fetched_at: '2025-11-18T19:07:12.985131'
original_url: https://www.bleepingcomputer.com/news/microsoft/microsoft-aisuru-botnet-used-500-000-ips-in-15-tbps-azure-ddos-attack/
author: speckx
date: '2025-11-18'
description: Microsoft said today that the Aisuru botnet hit its Azure network with a 15.72 terabits per second (Tbps) DDoS attack, launched from over 500,000 IP addresses.
---

# Microsoft: Azure hit by 15 Tbps DDoS attack using 500,000 IP addresses

 By

###### Sergiu Gatlan

* November 17, 2025
* 12:13 PM
* 0

Microsoft said today that the Aisuru botnet hit its Azure network with a 15.72 terabits per second (Tbps) DDoS attack, launched from over 500,000 IP addresses.

The attack used extremely high-rate UDP floods that targeted a specific public IP address in Australia, reaching nearly 3.64 billion packets per second (bpps).

"The attack originated from Aisuru botnet. Aisuru is a Turbo Mirai-class IoT botnet that frequently causes record-breaking DDoS attacks by exploiting compromised home routers and cameras, mainly in residential ISPs in the United States and other countries,"saidAzure Security senior product marketing manager Sean Whalen.

"These sudden UDP bursts had minimal source spoofing and used random source ports, which helped simplify traceback and facilitated provider enforcement."

Cloudflarelinked the same botnetto a record-breaking 22.2 terabits per second (Tbps) DDoS attack that reached 10.6 billion packets per second (Bpps) and was mitigated in September 2025. This attack lasted only 40 seconds but was roughly equivalent to streaming one million 4K videos simultaneously.

One week earlier, the XLab research division of Chinese cybersecurity company Qi'anxin attributed another 11.5 Tbps DDoS attack to theAisuru botnet, saying that it was controlling around 300,000 bots at the time.

The botnet targets security vulnerabilities in IP cameras, DVRs/NVRs, Realtek chips, and routers from T-Mobile, Zyxel, D-Link, and Linksys. As XLab researchers said, it suddenly ballooned in size in April 2025 after its operators breached a TotoLink router firmware update server and infected approximately 100,000 devices.

Infosec journalist Brian Krebsreportedearlier this month that Cloudflare removed multiple domains linked to the Aisuru botnet from its public "Top Domains" rankings of the most frequently requested websites (based on DNS query volume) after they began overtaking legitimate sites, such as Amazon, Microsoft, and Google.

The company stated that Aisuru's operators were deliberately flooding Cloudflare's DNS service (1.1.1.1) with malicious query traffic to boost their domain's popularity while undermining trust in the rankings. Cloudflare CEO Matthew Prince also confirmed that the botnet's behavior was severely distorting the ranking system and added that Cloudflare now redacts or completely hides suspected malicious domains to avoid similar incidents in the future.

​As Cloudflare revealed in its 2025 Q1 DDoS Report in April, itmitigated a record number of DDoS attackslast year, with a 198% quarter-over-quarter jump and a massive 358% year-over-year increase.

In total, it blocked 21.3 million DDoS attacks targeting its customers throughout 2024, as well as another 6.6 million attacks targeting its own infrastructure during an 18-day multi-vector campaign.

## Secrets Security Cheat Sheet: From Sprawl to Control

Whether you're cleaning up old keys or setting guardrails for AI-generated code, this guide helps your team build securely from the start.

Get the cheat sheet and take the guesswork out of secrets management.

Download Now

### Related Articles:

Cloudflare mitigates new record-breaking 22.2 Tbps DDoS attack

New Eleven11bot botnet infects 86,000 devices for DDoS attacks

Azure outage blocks access to Microsoft 365 services, admin portals

Prep smarter for Microsoft Azure exams with this $30 course bundle

Microsoft: Windows 10 KB5072653 OOB update fixes ESU install errors
