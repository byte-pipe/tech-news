---
title: "I Decompiled the White House's New App"
url: https://thereallo.dev/blog/decompiling-the-white-house-app
date: 2026-03-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-30T01:03:18.832539
---

# I Decompiled the White House's New App

# I Decompiled the White House's New App

## What Is This App?
- Built with React Native and Expo (SDK 54), using the Hermes JavaScript engine.
- Backend is a WordPress site exposing a custom `whitehouse/v1` REST API.
- Core logic lives in a 5.5 MB Hermes bytecode bundle; the native Java layer is only a thin wrapper.

## Expo Config
- Two notable plugins: `withNoLocation` and `withStripPermissions`.
- OTA updates are compiled in but disabled.

## What the App Actually Does
- Pulls content from WordPress endpoints such as `/home`, `/news/articles`, `/wire`, `/live`, `/galleries`, `/issues`, `/priorities`, `/achievements`, `/affordability`, `/media-bias`, and `/social/x`.
- Displays news, live streams, photo galleries, policy pages, social‑media embeds, and promotional material (e.g., “THE TRUMP EFFECT”, “Greatest President Ever!”, “Visit TrumpRx.gov”).
- Includes a link to the ICE tip‑reporting form.

## Consent/Paywall Bypass Injector
- The in‑app WebView injects JavaScript that removes cookie banners, GDPR dialogs, OneTrust popups, login/paywall walls, and other consent elements.
- Forces `body { overflow: auto !important }` to re‑enable scrolling.
- Uses a `MutationObserver` to continuously strip newly added consent elements.

## Location Tracking Infrastructure
- Despite the `withNoLocation` plugin, the OneSignal SDK contains full location‑tracking code.
- Activation requires three conditions:
  1. `isLocationShared` flag set to true via `setLocationShared(true)` from JavaScript.
  2. User grants precise or approximate foreground location permission at runtime.
  3. Device has a location provider (GMS/HMS).
- When active, the fused location API requests GPS every 4.5 min in foreground and 9.5 min in background, logging latitude, longitude, accuracy, timestamp, and app state to OneSignal’s `PropertiesModel`.
- A background service continues capturing location when the app is not active.

## OneSignal User Profiling
- Beyond push notifications, OneSignal collects:
  - Tags for segmentation, SMS numbers, aliases for cross‑device IDs.
  - Outcome values, notification click events, in‑app‑message lifecycle events.
  - Permission, subscription, and user‑state changes.
  - Location sharing status and privacy‑consent flags.
- All interactions are stored locally and synced to OneSignal’s servers.

## Supply‑Chain Concerns

### Loading JS From a Personal GitHub Pages Site
- The `react-native-youtube-iframe` library loads its player HTML from a GitHub Pages URL owned by the user `lonelycpp`.
- Compromise of that account would allow arbitrary HTML/JS to run in every app instance via the WebView.

### Elfsight Widget Platform
- The app embeds third‑party JavaScript from Elfsight to display social‑media feeds.
- This code runs inside the WebView without sandboxing, giving Elfsight full access to the same tracking capabilities as the app itself.
