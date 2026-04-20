---
title: We Intercepted the White House App's Network Traffic. Here's What It Sends. | atomic.computer
url: https://www.atomic.computer/blog/white-house-app-network-traffic-analysis/
site_name: hackernews_api
content_file: hackernews_api-we-intercepted-the-white-house-apps-network-traffi
fetched_at: '2026-04-02T01:01:14.241333'
original_url: https://www.atomic.computer/blog/white-house-app-network-traffic-analysis/
author: Atomic Computer Services
date: '2026-04-01'
description: We set up a MITM proxy and captured the decrypted HTTPS traffic from the official White House iOS app. On a single browsing session it contacts multiple Elfsight domains, sends your device fingerprint to OneSignal, and loads Google DoubleClick ad tracking. The privacy manifest says it collects nothing.
tags:
- hackernews
- trending
---

This is a follow-up to ourstatic analysis of the White House iOS app. In that post, we decompiled the app and documented what the codecoulddo. Critics fairly pointed out that compiled code doesn’t mean active code.

So we set up a MITM proxy and watched what the app actually sends.

## Setup

We installedmitmproxyon a Mac, configured an iPhone to route traffic through it, and installed the mitmproxy CA certificate on the device. Then we opened the White House app (v47.0.4, build 81) and browsed every tab: Home, News, Live, Social, and Explore.

All HTTPS traffic was decrypted and logged. No modifications were made to the traffic. The app was used as any normal user would use it.

## What the App Contacts

On a single browsing session across all tabs, the app made requests to31 unique hosts(excluding iOS system traffic):

Host

Requests

What It Is

www.whitehouse.gov

48

WordPress API (news, home, wire, priorities, galleries, live)

www.youtube.com

25

YouTube embeds

phosphor.utils.elfsightcdn.com

19

Elfsight utility scripts

static.elfsight.com

12

Elfsight static assets

storage.elfsight.com

10

Elfsight file storage

api.onesignal.com

9

OneSignal analytics and user profiling

i.ytimg.com

9

YouTube video thumbnails

rr6—.googlevideo.com

9

Google Video CDN

scontent-lax7-1.xx.fbcdn.net

7

Facebook CDN (images)

pbs.twimg.com

7

Twitter/X images

apis.google.com

7

Google APIs

widget-data.service.elfsight.com

6

Elfsight widget data

core.service.elfsight.com

4

Elfsight boot API (the two-stage loader)

video-proxy.wu.elfsightcompute.com

4

Elfsight video proxy

img.youtube.com

4

YouTube thumbnails

yt3.ggpht.com

3

YouTube channel avatars

clients3.google.com

3

Connectivity check

scontent-lax3-1.xx.fbcdn.net

3

Facebook CDN

fonts.gstatic.com

2

Google Fonts

jnn-pa.googleapis.com

2

Google APIs

scontent-lax3-2.xx.fbcdn.net

2

Facebook CDN

www.google.com

2

Google

googleads.g.doubleclick.net

1

Google Ads / DoubleClick tracking

static.doubleclick.net

1

Google Ads

accounts.google.com

1

Google authentication

universe-static.elfsightcdn.com

1

Elfsight CDN

elfsightcdn.com

1

Elfsight CDN (platform.js)

cdnjs.cloudflare.com

1

Cloudflare CDN

ssl.gstatic.com

1

Google static

yt3.googleusercontent.com

1

YouTube

www.gstatic.com

1

Google static

Of the 206 app-initiated requests captured (excluding iOS system traffic), only 48 (23%) went to whitehouse.gov. The other 158 (77%) went to third-party services including Elfsight, OneSignal, YouTube, Google DoubleClick, Facebook, and Twitter.

## What OneSignal Receives

This is no longer speculation from symbol analysis. This is the actual decrypted HTTPS request body sent toapi.onesignal.comon app launch:

{


"properties"
: {


"language"
:
"en"
,


"timezone_id"
:
"America/[REDACTED]"
,


"country"
:
"US"
,


"first_active"
:
1774908688
,


"last_active"
:
1774909124
,


"ip"
:
"[REDACTED]"

 },


"identity"
: {


"onesignal_id"
:
"[REDACTED]"

 },


"subscriptions"
: [

 {


"id"
:
"[REDACTED]"
,


"session_time"
:
61
,


"session_count"
:
3
,


"sdk"
:
"050500"
,


"device_model"
:
"iPhone[REDACTED]"
,


"device_os"
:
"[REDACTED]"
,


"rooted"
:
false
,


"app_version"
:
"47.0.4"
,


"net_type"
:
1
,


"carrier"
:
""

 }

 ]

}

On a single app launch, OneSignal receives:

* Yourlanguage and timezone(narrows you to a region)
* Yourcountry
* YourIP address(full IPv6 or IPv4, we observed both)
* When you first opened the appandwhen you were last active(exact timestamps)
* Yourdevice model and OS version(device fingerprint)
* Whether you’re onWiFi or cellular
* Yourcarrier
* Whether your device isjailbroken
* How many timesyou’ve opened the app
* How longyou spent in each session (in seconds)
* Apersistent unique identifierthat tracks you across sessions

The app sent multiple PATCH requests to OneSignal on each launch, updating your profile with session counts, session time, and device metadata. In our first capture (launch only), we observed 18 PATCH requests. In our full browsing session, we observed 9 total OneSignal requests including GETs and PATCHes.

The sequence is telling: on launch, the app first performs aGETto fetch your existing profile from OneSignal’s servers, then sendsPATCHrequests to update it. In our captures, the GET returned a profile with an IPv6 address from a previous session. The subsequent PATCHes updated it to our current IPv4 address. This means OneSignal maintains a persistent profile thattracks your IP address changes over time. Every time you open the app from a different network, your new IP is logged against the same persistent identifier.

The User-Agent header identifies the traffic:WhiteHouse/81 CFNetwork/3860.400.51 Darwin/25.3.0

## 13 Elfsight Domains

Ourstatic analysisfound six Elfsight widgets and a two-stage JavaScript loader. The dynamic analysis confirms it. When you open the Social tab, the app contactsmultiple Elfsight-controlled domains. Between our static analysis ofplatform.jsand the live traffic capture, we observed the following:

1. elfsightcdn.com(platform.js CDN)
2. core.service.elfsight.com(boot API, returns scripts to inject)
3. static.elfsight.com(static assets)
4. storage.elfsight.com(file storage)
5. phosphor.utils.elfsightcdn.com(utility scripts)
6. universe-static.elfsightcdn.com(static CDN)
7. widget-data.service.elfsight.com(widget data service)
8. video-proxy.wu.elfsightcompute.com(video proxy)
9. cors-proxy.utils.elfsightcdn.com(CORS proxy)
10. apps.elfsight.com(apps service)
11. dash.elfsight.com(dashboard)
12. service-reviews-ultimate.elfsight.com(reviews service)
13. Domain-level cookies set onelfsight.com

The/p/boot/requests confirm the two-stage loader in action. Each widget ID is sent tocore.service.elfsight.com, which responds with widget configuration and anassetsarray of JavaScript files to inject. Here are the actual scripts returned by the server during our capture:

// TikTok widget -> server responds with:

"assets"
: [
"https://universe-static.elfsightcdn.com/app-releases/tiktok-feed/stable/v2.46.1/.../tiktokFeed.js"
]

// Instagram widget -> server responds with:

"assets"
: [
"https://static.elfsight.com/apps/instashow/stable/.../instashow.js"
]

// Facebook widget -> server responds with:

"assets"
: [
"https://static.elfsight.com/apps/facebook-feed/stable/.../facebookFeed.js"
]

// YouTube widget -> server responds with:

"assets"
: [
"https://static.elfsight.com/apps/yottie/stable/.../yottie.js"
]

The app’sloadAssetsfunction creates a<script>element for each URL and appends it to the page. The server decides what runs. This is the two-stage loader we documented in ourstatic analysisnow confirmed in live traffic.

The response also sets cookies includingelfsight_viewed_recently, Cloudflare tracking cookies (_cfuvid,__cf_bm), and session identifiers. We counted10+ cookiesset by Elfsight infrastructure during a single session.

## Google DoubleClick Ad Tracking

The YouTube embeds load Google’s ad tracking infrastructure:

* googleads.g.doubleclick.net(Google Ads)
* static.doubleclick.net(DoubleClick ad scripts)

DoubleClick is Google’s ad serving and tracking platform. Its presence means Google’s advertising infrastructure is running inside the official White House app, tracking user engagement with video content. This was not disclosed in the privacy manifest.

## The Privacy Manifest vs. Reality

NSPrivacyCollectedDataTypes: []

NSPrivacyTracking: false

In a single browsing session, the app:

* Sent your device model, OS, IP address, timezone, language, session count, session duration, and a persistent unique identifier to OneSignal (a third-party analytics company)
* Contacted 13 Elfsight-controlled domains and received 10+ tracking cookies
* Loaded Google DoubleClick ad tracking infrastructure
* Made requests to Facebook CDN, Twitter/X CDN, YouTube, and Google APIs

The privacy label says “No Data Collected.”

## Methodology

* Proxy: mitmproxy (mitmdump) on macOS
* Device: iPhone running iOS, connected to same WiFi network
* Certificate: mitmproxy CA installed and trusted in iOS Certificate Trust Settings
* Capture: Full HTTPS decryption of all app traffic
* Duration: Single browsing session across all five tabs (Home, News, Live, Social, Explore)
* Modifications: None. Traffic was observed, not altered.
* Personal data: All IP addresses, device identifiers, and OneSignal IDs have been redacted from this post.

No servers were probed. No traffic was modified. We watched what the app sends on its own.

## Related Work

* Static analysis of the White House iOS app(our original post)
* Thereallo’s analysis of the Android version

## About

Atomic Computerprovides cybersecurity, infrastructure, and development services. If you need a security assessment of your mobile app,get in touch.

Have a question about this, or a project you're working on?

Schedule a callContact us
