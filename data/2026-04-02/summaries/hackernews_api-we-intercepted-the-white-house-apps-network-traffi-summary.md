---
title: "We Intercepted the White House App's Network Traffic. Here's What It Sends. | atomic.computer"
url: https://www.atomic.computer/blog/white-house-app-network-traffic-analysis/
date: 2026-04-01
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-02T01:03:47.119542
---

# We Intercepted the White House App's Network Traffic. Here's What It Sends. | atomic.computer

# Summary of White House App Network Traffic Analysis

## Setup
- Used mitmproxy on a Mac and routed an iPhone’s traffic through it.  
- Installed the mitmproxy CA certificate on the device.  
- Ran the White House iOS app (v47.0.4, build 81) and visited every tab (Home, News, Live, Social, Explore).  
- Decrypted all HTTPS traffic, logged it, and made no modifications.  

## Hosts Contacted
- In one browsing session the app made requests to **31 unique hosts** (excluding iOS system traffic).  
- Total app‑initiated requests: **206**.  
- Requests to whitehouse.gov: **48** (23%).  
- Requests to third‑party services: **158** (77%).  
- Main third‑party categories: Elfsight (multiple subdomains), OneSignal, YouTube, Google (Ads/DoubleClick, APIs, Fonts), Facebook CDN, Twitter/X CDN.  

## Data Sent to OneSignal
- On launch the app sends a JSON payload to `api.onesignal.com` containing:
  - Language, timezone, country, IP address.  
  - First‑active and last‑active timestamps.  
  - Device model, OS version, jailbreak status, network type (Wi‑Fi or cellular), carrier.  
  - App version, session count, session duration, persistent OneSignal identifier.  
- Sequence observed: GET profile → multiple PATCH updates (18 PATCHes on launch, 9 total requests in full session).  
- OneSignal maintains a persistent profile that records IP changes across sessions.  
- User‑Agent header: `WhiteHouse/81 CFNetwork/3860.400.51 Darwin/25.3.0`.  

## Elfsight Integration
- The app contacts **13 distinct Elfsight‑controlled domains**, confirming the two‑stage widget loader identified in static analysis.  
- Workflow: widget IDs sent to `core.service.elfsight.com` → server returns configuration and a list of JavaScript assets → app injects each script via `<script>` tags.  
- Example widgets and returned asset URLs: TikTok, Instagram, Facebook, YouTube feeds.  
- Over 10 tracking cookies set during a single session (e.g., `elfsight_viewed_recently`, Cloudflare `_cfuvid`, `__cf_bm`).  

## Google DoubleClick Ad Tracking
- YouTube embeds load Google advertising scripts:
  - `googleads.g.doubleclick.net` (Google Ads).  
  - `static.doubleclick.net` (DoubleClick ad scripts).  
- This introduces Google’s ad‑serving and tracking infrastructure inside the official White House app, a detail absent from the app’s privacy manifest.  

## Privacy Manifest vs. Reality
- Declared in the app’s privacy label:  
  - `NSPrivacyCollectedDataTypes: []`  
  - `NSPrivacyTracking: false`  
- Actual observed behavior in a single session:
  - Sent detailed device, location, network, and usage data to OneSignal.  
  - Contacted 13 Elfsight domains and received multiple tracking cookies.  
  - Loaded Google DoubleClick ad tracking.  
  - Accessed Facebook, Twitter/X, YouTube, and various Google APIs.  
- The privacy label’s claim of “No Data Collected” is contradicted by the network traffic.  

## Methodology (brief)
- MITM proxy setup with full HTTPS decryption.  
- Systematic navigation of every app tab to generate representative traffic.  
- Logging and analysis of request headers, bodies, and response cookies.  
- Comparison of observed data flows with the app’s declared privacy information.