---
title: IP and DNS Leaks in WebKit Affecting Proxy Browsers and Apple iCloud Private Relay | Mysk Blog – In-Depth Cybersecurity & Mobile App Privacy Research
url: https://mysk.blog/2026/08/04/webkit-proxy-icloud-private-relay-ip-leak/
date: 2026-08-05
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-06T07:13:02.753553
---

# IP and DNS Leaks in WebKit Affecting Proxy Browsers and Apple iCloud Private Relay | Mysk Blog – In-Depth Cybersecurity & Mobile App Privacy Research

# IP and DNS Leaks in WebKit Affecting Proxy Browsers and Apple iCloud Private Relay

## Summary
- WebKit‑based browsers on iOS and macOS (including iOS Tor browsers and Psylo) can route all traffic through a proxy via `WKWebsiteDataStore.proxyConfigurations`.  
- We discovered three WebKit features that bypass this proxy configuration and expose the device’s real network information:  
  1. **DNS prefetching** – resolves hostnames through the device’s normal DNS path.  
  2. **WebAuthn related origin requests** – the OS credential service fetches validation files directly.  
  3. **WebTransport** – opens a direct HTTP/3/QUIC connection, ignoring the proxy.  
- All three leaks also affect Apple’s iCloud Private Relay, but not VPNs (which tunnel all traffic at the system level).  
- The leaks are mitigated in Psylo 1.3.1, which blocks DNS‑prefetch hints and disables WebTransport and WebAuthn by default, with optional per‑silo re‑enabling.  
- A proof‑of‑concept site (leaks.psylo.app) demonstrates the leaks.

## Background

### Proxy Configuration on iOS and macOS
- Introduced in iOS 17 / macOS 14, `WKWebsiteDataStore.proxyConfigurations` lets WebKit‑based browsers route their own web traffic through a proxy at the application level.  
- The expectation is that every network request a page makes appears to originate from the proxy’s IP address.

### DNS Leak Reported by a Psylo User
- The investigation began after a user reported DNS leaks on certain sites.  
- Psylo routes each silo through the Mysk Private Proxy Network (or a custom proxy), so DNS queries should originate from the proxy, not the device.  
- The leak was traced to WebKit features that ignore the proxy settings, meaning any iOS browser that relies on this API (including all iOS Tor browsers) is affected.  
- iCloud Private Relay suffers the same issue; VPNs do not because they operate at the system level.

### iCloud Private Relay
- iCloud Private Relay proxies Safari’s web traffic and DNS queries through a two‑hop relay, aiming to hide both user identity and visited sites.  
- The three leaks occur outside WebKit’s standard page‑loading path, so Private Relay cannot intercept them.

## Leak Details

### DNS Prefetching
- Websites can embed `<link rel="dns-prefetch">` tags to resolve hostnames before they are needed.  
- WebKit performs these lookups via the device’s normal DNS resolver, bypassing any proxy set through `WKWebsiteDataStore.proxyConfigurations`.  
- Attackers can embed unique hostnames per visitor and observe the queries arriving at their authoritative DNS server, revealing the user’s real DNS servers and IP address.  
- The feature was enabled on iOS 26.0 (Sept 2025); earlier iOS versions ignored the tag.

### WebAuthn Related Origin Requests
- WebAuthn’s “Related Origin Requests” allow a passkey to be used across a set of domains owned by the same organization.  
- When a page requests a credential with a different `rpId`, the OS credential service fetches `https://<rpId>/.well-known/webauthn` directly from the device, outside the browser’s network stack.  
- This fetch occurs without user interaction (e.g., with `mediation: "conditional"`), exposing the device’s real IP address.  
- The behavior was introduced in iOS 18.0 / Safari 18.0 (Sept 2024).

### WebTransport
- `new WebTransport(url)` creates a low‑latency connection over HTTP/3 (QUIC).  
- WebKit builds the QUIC connection using its own network parameters and does not apply the session’s proxy configuration.  
- Consequently, the server sees the device’s real IP address, and Private Relay cannot proxy the traffic.  
- Available since iOS 26.4.

## Mitigations and Fixes
- **Psylo 1.3.1**:  
  - Blocks DNS‑prefetch hints by default.  
  - Disables WebTransport and WebAuthn unless explicitly enabled per silo.  
  - Provides toggles for sites that legitimately need these features, keeping privacy decisions in the user’s hands.  
- We have contacted the Tor Project and the Onion Browser developers about the issues.  
- No known mitigation for iCloud Private Relay other than disabling the affected features where possible.

## Testing the Leaks
- Visit the proof‑of‑concept site **leaks.psylo.app** to observe DNS, WebAuthn, and WebTransport leaks in real time.