---
title: The Smart TV in Your LivingRoom Is a Node in the AIScraping Economy - Include Security Research Blog
url: https://blog.includesecurity.com/2026/06/the-smart-tv-in-your-livingroom-is-a-node-in-the-aiscraping-economy/
date: 2026-06-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-07T06:00:43.531300
---

# The Smart TV in Your LivingRoom Is a Node in the AIScraping Economy - Include Security Research Blog

# The Smart TV in Your LivingRoom Is a Node in the AIScraping Economy – Include Security Research Blog

## Why This Matters Now
- AI models rely heavily on web‑scraped data for pre‑training, retrieval, grounding, and search.  
- Traditional datacenter IPs are increasingly blocked by services like Cloudflare and DataDome.  
- Residential proxies bypass these blocks by routing traffic through real home connections.  
- Recent reports (Krebs, FBI advisory) highlight large‑scale proxy networks being used for AI data harvesting.  
- Most coverage focuses on illegal proxy sources; this article examines the legal side, specifically Bright Data’s consent‑based residential proxy network.

## Bright Data’s Consent SDK
- Bright Data markets the world’s largest residential proxy network (400 M+ IPs) sourced from an SDK embedded in consumer apps.  
- The SDK runs on user devices (mobile phones, smart TVs, etc.) and, with user consent, turns them into exit nodes for web‑scraping traffic.  
- The SDK fetches an unauthenticated JSON config (`sdk_config_ios.json`) that contains feature flags, idle‑detection thresholds, bandwidth caps, and a partner manifest.  
- Configuration is public; anyone can request it by supplying an app bundle ID, SDK version, and a UUID.

## Why Connected TV (CTV) Is the Ideal Proxy
| Factor | Mobile Phone | Smart TV / CTV |
|--------|--------------|----------------|
| Power | Battery‑limited | Always plugged in |
| Network | Wi‑Fi + cellular | Always Wi‑Fi, high‑speed |
| Uptime | Intermittent | 24/7 standby |
| Bandwidth ceiling | Low (cellular caps) | Effectively unlimited |
| User attention | Actively used | Often unattended |
| Consent UI | Text on phone screen | Remote‑controlled text navigation |
| Corporate oversight | Higher (MDM, EDR) | Virtually none |

- TVs stay online continuously, have high‑speed broadband, and lack strong user oversight, making them perfect for sustained proxy use.  
- Consent dialogs on TV apps are hard to read and may mislead users about the extent of resource sharing.

## Example: Petflix (Roku App)
- Opt‑in screen states the device’s “free resources and IP address” will be used “occasionally” for public web data download.  
- SDK default config allows up to 200 GB of Wi‑Fi bandwidth per month per device.

## Bright Data Partner Manifest
- The partner list is served from an unauthenticated endpoint and includes:
  - **PlayWorks Digital** – 400+ CTV games, ~250 M TV homes.  
  - **CloudTV** – Integrated across 125+ TV brands and 15+ OEMs.  
  - **Longvision Media HK** – 5 M OTT users in HK & Malaysia.  
  - **Viber Media** – 250 M–820 M monthly messenger users.  
  - **Supercent**, **Moonfrog Labs**, **Hola Networks**, and several lesser‑known entities.  
- Presence in the manifest indicates a past or present integration; each app must be verified individually.

## Technical Details of the SDK
1. **Unauthenticated Config Fetch**  
   - URL: `https://clientsdk.bright-sdk.com/sdk_config_ios.json?...`  
   - Returns feature flags, idle‑detection thresholds, per‑country bandwidth tiers, and partner manifest.  
2. **Peer Tunnel Creation**  
   - After config retrieval, the SDK establishes a tunnel to Bright Data’s backend, routing peer traffic through the device when idle criteria are met.  
3. **Idle‑Detection Rules**  
   - Based on battery level, CPU/memory usage, network type, and user activity; CTVs typically meet “idle” conditions continuously.  
4. **Bandwidth Management**  
   - Configurable monthly caps (e.g., 200 GB Wi‑Fi) enforce limits per device but are high enough for substantial AI data collection.

## Implications
- A large portion of AI training data may be harvested from everyday consumer devices without clear user awareness.  
- Smart TVs, due to their always‑on nature and weak consent mechanisms, become a primary vector for residential proxy traffic.  
- Transparency in privacy policies is insufficient; users need more explicit, accessible consent dialogs.  
- Researchers and regulators should scrutinize legal residential‑proxy services alongside illicit botnets, given their potential impact on data privacy and network abuse.