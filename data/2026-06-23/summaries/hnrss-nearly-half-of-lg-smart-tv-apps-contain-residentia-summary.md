---
title: Nearly Half of LG Smart TV Apps Contain Residential Proxy SDKs
url: https://spur.us/blog/smart-tv-apps-residential-proxy-sdks
date: 2026-06-22
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-23T10:20:24.554054
---

# Nearly Half of LG Smart TV Apps Contain Residential Proxy SDKs

# Summary of “Nearly Half of LG Smart TV Apps Contain Residential Proxy SDKs”

## Overview
- Scanned 6,038 LG and Samsung TV apps; 2,058 (≈33%) embed residential‑proxy SDKs that sell the TV’s IP address.
- Apps appear innocuous (fish tank, clock, solitaire) while secretly routing other users’ traffic.

## Why TVs Are Different
- Smart TVs sit on the home network but are not treated like computers; users rarely audit them.
- They stay powered, signed‑in, and online for years, making them ideal long‑term proxy hosts.
- Consent is vague: a one‑time remote prompt can be forgotten while the proxy runs indefinitely.

## How Proxy SDKs End Up in Apps
- Money drives inclusion: ads degrade UX, so developers add proxy SDKs to monetize silently.
- The app remains calm (e.g., a screensaver) while the TV’s connection generates revenue in the background.

## What Each SDK Considers Consent
- All three SDKs ask for consent once and never again.
- The consent dialog includes a clause stating the proxy continues after the app is closed.
- Example: Pac‑Man on Tizen offers “Bright Data” as an ad‑free option; accepting enables proxy use for web indexing.

## Who Is Making These Apps?
- Proxy companies often act as publishers:
  - Bright Data (Bright Data Ltd, Bright SDK) – 367 flagged apps.
  - Honeygain UAB (Oxylabs subsidiary) – 16 flagged apps.
- Many apps are thin “shovelware” wrappers whose primary purpose is to host the SDK.

## Platform Gap
- Amazon and Roku explicitly prohibit third‑party proxy services in their policies.
- LG and Samsung have no comparable public restrictions, allowing the model to thrive on webOS and Tizen.

## Why This Is Dangerous
- A TV proxy can be used to reach private LAN resources (router admin panels, NAS, cameras, etc.) if the provider’s filters fail or policies change.
- Real‑world example: KrebsOnSecurity reported the Kimwolf botnet using residential proxies to infiltrate local networks.
- SDK implementations vary:
  - Bright Data includes a private‑range blocklist.
  - Massive and Honeygain/Oxylabs samples lack comparable restrictions, relying on provider policy enforcement.

## Methodology
- Downloaded and unpacked LG webOS and Samsung Tizen app packages.
- Scanned for known SDK artifacts (e.g., `brd_api.js`, `.massivesdk`, Honeygain service names).
- Every app counted contained a confirmed proxy SDK fingerprint.

## Proxy Vendor Responses
- **Bright Data:** Emphasized consent, independent audits, and use limited to legitimate business, research, and journalistic purposes.
- **Massive:** Stated focus on privacy and security, minimal user interface by design, and KYC for network users; technical controls are server‑side.