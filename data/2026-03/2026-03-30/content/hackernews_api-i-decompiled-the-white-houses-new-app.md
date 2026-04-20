---
title: I Decompiled the White House's New App
url: https://thereallo.dev/blog/decompiling-the-white-house-app
site_name: hackernews_api
content_file: hackernews_api-i-decompiled-the-white-houses-new-app
fetched_at: '2026-03-30T01:01:13.185424'
original_url: https://thereallo.dev/blog/decompiling-the-white-house-app
author: Thereallo
date: '2026-03-29'
description: The official White House Android app has a cookie/paywall bypass injector, tracks your GPS every 4.5 minutes, and loads JavaScript from some guy's GitHub Pages.
tags:
- hackernews
- trending
---

The White House released an app on the App Store and Google Play.
They posted a blog about it.
 "Unparalleled access to the Trump Administration."
It took a few minutes to pull the APKs with ADB, and threw them into JADX.
Here is everything I found.

## What Is This App?

It's a React Native app built with Expo (SDK 54), running on the Hermes JavaScript engine. The backend is WordPress with a custom REST API. The app was built by an entity called "forty-five-press" according to the Expo config.
The actual app logic is compiled into a 5.5 MB Hermes bytecode bundle. The native Java side is just a thin wrapper.
java
Copy
Version 47.0.1. Build 20. Hermes enabled. New Architecture enabled. Nothing weird here. Let's keep going.

## Expo Config

json
Copy
Two things stand out here. First, there's a plugin called
withNoLocation
. Second, there's a plugin called
withStripPermissions
. Remember these. They become relevant very soon.
OTA updates are disabled. The Expo update infrastructure is compiled in but dormant.

## What the App Actually Does

I extracted every string from the Hermes bytecode bundle and filtered for URLs and API endpoints. The app's content comes from a WordPress REST API at whitehouse.gov with a custom
whitehouse/v1
 namespace.
Here are the endpoints:
Endpoint
What It Serves
/wp-json/whitehouse/v1/home
Home screen
/wp-json/whitehouse/v1/news/articles
News articles
/wp-json/whitehouse/v1/wire
"The Wire" news feed
/wp-json/whitehouse/v1/live
Live streams
/wp-json/whitehouse/v1/galleries
Photo galleries
/wp-json/whitehouse/v1/issues
Policy issues
/wp-json/whitehouse/v1/priorities
Priorities
/wp-json/whitehouse/v1/achievements
Achievements
/wp-json/whitehouse/v1/affordability
Drug pricing
/wp-json/whitehouse/v1/media-bias
"Media Bias" section
/wp-json/whitehouse/v1/social/x
X/Twitter feed proxy
Other hardcoded strings from the bundle:
"THE TRUMP EFFECT"
,
"Greatest President Ever!"
 (lol),
"Text President Trump"
,
"Send a text message to President Trump at 45470"
,
"Visit TrumpRx.gov"
,
"Visit TrumpAccounts.gov"
.
There's also a direct link to
https://www.ice.gov/webform/ice-tip-form
. The ICE tip reporting form. In a news app.
It's a content portal. News, live streams, galleries, policy pages, social media embeds, and promotional material for administration initiatives. All powered by WordPress.
Now let's look at what else it does.

## Consent/Paywall Bypass Injector

The app has a WebView for opening external links. Every time a page loads in this WebView, the app injects a JavaScript snippet. I found it in the Hermes bytecode string table:
javascript
Copy
Read that carefully. It hides:
* Cookie banners
* GDPR consent dialogs
* OneTrust popups
* Privacy banners
* Login walls
* Signup walls
* Upsell prompts
* Paywall elements
* CMP (Consent Management Platform) boxes
It forces
body { overflow: auto !important }
 to re-enable scrolling on pages where consent dialogs lock the scroll. Then it sets up a MutationObserver to continuously nuke any consent elements that get dynamically added.
An official United States government app is injecting CSS and JavaScript into third-party websites to strip away their cookie consent dialogs, GDPR banners, login gates, and paywalls.
The native side confirms this is the
injectedJavaScript
 prop on the React Native WebView:
java
Copy
java
Copy
Every page load in the in-app browser triggers this. It wraps the injection in an IIFE and runs it via Android's
evaluateJavascript()
.

## Location Tracking Infrastructure

Remember
withNoLocation
 from the Expo config? The plugin that's supposed to strip location? Yeah. The OneSignal SDK's native location tracking code is fully compiled into the APK.
java
Copy
270,000 milliseconds is 4.5 minutes. 570,000 is 9.5 minutes.
To be clear about what activates this: the tracking doesn't start silently. There are three gates. The
LocationManager
 checks all of them before the fused location API ever fires.
java
Copy
First, the
_isShared
 flag. It's read from SharedPreferences on init and defaults to
false
. The JavaScript layer can flip it on with
setLocationShared(true)
. The Hermes string table confirms both
setLocationShared
 and
isLocationShared
 are referenced in the app's JS bundle, so the app has the ability to toggle this.
Second, the user has to grant the Android runtime location permission. The location permissions aren't declared in the AndroidManifest but requested at runtime. The Google Play Store listing confirms the app asks for "access precise location only in the foreground" and "access approximate location only in the foreground."
Third, the
start()
 method only proceeds if the device actually has a location provider (GMS or HMS).
If all three gates pass, here's what runs. The fused location API requests GPS at the intervals defined above:
java
Copy
This gets called on both
onFocus()
 and
onUnfocused()
, dynamically switching between the 4.5-minute foreground interval and the 9.5-minute background interval.
When a location update comes in, it feeds into the
LocationCapturer
:
java
Copy
Latitude, longitude, accuracy, timestamp, whether the app was in the foreground or background, and whether it was fine (GPS) or coarse (network). All of it gets written into OneSignal's
PropertiesModel
, which syncs to their backend.
The data goes here:
java
Copy
There's also a background service that keeps capturing location even when the app isn't active:
java
Copy
So the tracking isn't unconditionally active. But the entire pipeline including permission strings, interval constants, fused location requests, capture logic, background scheduling, and the sync to OneSignal's API, all of them are fully compiled in and one
setLocationShared(true)
 call away from activating. The
withNoLocation
 Expo plugin clearly did not strip any of this. Whether the JS layer currently calls
setLocationShared(true)
 is something I can't determine from the native side alone, since the Hermes bytecode is compiled and the actual call site is buried in the 5.5 MB bundle. What I can say is that the infrastructure is there, ready to go, and the JS API to enable it is referenced in the bundle.

## OneSignal User Profiling

OneSignal is doing a lot more than push notifications in this app. From the Hermes string table:
* addTag- tag users for segmentation
* addSms- associate phone numbers with user profiles
* addAliases- cross-device user identification
* addOutcomeWithValue/addUniqueOutcome- track user actions and conversions
* OneSignal-notificationClicked- notification tap tracking
* OneSignal-inAppMessageClicked/WillDisplay/DidDisplay/WillDismiss/DidDismiss- full in-app message lifecycle tracking
* OneSignal-permissionChanged/subscriptionChanged/userStateChanged- state change tracking
* setLocationShared/isLocationShared- location toggle
* setPrivacyConsentRequired/setPrivacyConsentGiven- consent gating
The local database tracks every notification received and whether it was opened or dismissed:
java
Copy
Your location, your notification interactions, your in-app message clicks, your phone number if you provide it, your tags, your state changes. All going to OneSignal's servers.

## Supply Chain: Loading JS From Some Guy's GitHub Pages

The app embeds YouTube videos using the
react-native-youtube-iframe
 library. This library loads its player HTML from:

Copy
That's a personal GitHub Pages site. If the
lonelycpp
 GitHub account gets compromised, whoever controls it can serve arbitrary HTML and JavaScript to every user of this app, executing inside the WebView context.
This is a government app loading code from a random person's GitHub Pages.

## Supply Chain: Elfsight Widget Platform

The app loads third-party JavaScript from Elfsight to embed social media feeds:

Copy
Elfsight is a commercial SaaS widget company. Their JavaScript runs inside the app's WebView with no sandboxing. Whatever tracking Elfsight does, it does it here too. Their code can change at any time. The Elfsight widget ID
4a00611b-befa-466e-bab2-6e824a0a98a9
 is hardcoded in an HTML embed.

## Supply Chain: Everything Else

* Mailchimpatwhitehouse.us10.list-manage.com/subscribe/post-jsonhandles email signups. User emails go to Mailchimp's infrastructure.
* Uploadcareatucarecdn.comhosts content images via six hardcoded UUIDs.
* Truth Socialhas a hardcoded HTML embed with Trump's profile, avatar image URL fromstatic-assets-1.truthsocial.com, and a "Follow on Truth Social" button.
* Facebookpage plugin is loaded in an iframe viafacebook.com/plugins/page.php.
None of these are government-controlled infrastructure.

## No Certificate Pinning

The app uses standard Android TrustManager for SSL with no custom certificate pinning. If you're on a network with a compromised CA (corporate proxies, public wifi with MITM, etc.), traffic between the app and its backends can be intercepted and read.

## Development Artifacts in Production

The build has some sloppy leftovers.
A localhost URL made it into the production Hermes bundle:

Copy
That's the React Native Metro bundler dev server.
A developer's local IP is hardcoded in the string resources:
xml
Copy
The Expo development client (
expo-dev-client
,
expo-devlauncher
,
expo-devmenu
) is compiled into the release build. There's a
dev_menu_fab_icon.png
 in the drawable resources. The Compose
PreviewActivity
 is exported in the manifest, which is a development-only component that should not be in a production APK.
xml
Copy

## Permissions

The AndroidManifest itself is pretty standard for a notification-heavy app:
xml
Copy
Plus about 16 badge permissions for Samsung, HTC, Sony, Huawei, OPPO, and other launchers. These just let the app show notification badge counts. Not interesting.
The interesting permissions are the ones that aren't in the manifest but are hardcoded as runtime request strings in the OneSignal SDK, as covered above. Fine location. Coarse location. Background location.
The Google Play listing also mentions: "modify or delete the contents of your shared storage", "run foreground service", "this app can appear on top of other apps", "run at startup", "use fingerprint hardware", "use biometric hardware."
The file provider config is also worth mentioning:
xml
Copy
That exposes the entire external storage root. It's used by the WebView for file access.

## Full SDK List

68+ libraries are compiled into this thing. The highlights:
Category
Libraries
Framework
React Native, Expo SDK 54, Hermes JS engine
Push/Engagement
OneSignal, Firebase Cloud Messaging, Firebase Installations
Analytics/Telemetry
Firebase Analytics, Google Data Transport, OpenTelemetry
Networking
OkHttp 3, Apollo GraphQL, Okio
Images
Fresco, Glide, Coil 3, Uploadcare CDN
Video
ExoPlayer (Media3), Expo Video
ML
Google ML Kit Vision (barcode scanning), Barhopper model
Crypto
Bouncy Castle
Storage
Expo Secure Store, React Native Async Storage
WebView
React Native WebView (with the injection script)
DI
Koin
Serialization
GSON, Wire (Protocol Buffers)
License
PairIP license check (Google Play verification)
25 native
.so
 libraries in the arm64 split. The full Hermes engine, React Native core, Reanimated, gesture handler, SVG renderer, image pipeline, barcode scanner, and more.

## Recap

The official White House Android app:
1. Injects JavaScript into every website you openthrough its in-app browser to hide cookie consent dialogs, GDPR banners, login walls, signup walls, upsell prompts, and paywalls.
2. Has a full GPS tracking pipeline compiled inthat polls every 4.5 minutes in the foreground and 9.5 minutes in the background, syncing lat/lng/accuracy/timestamp to OneSignal's servers.
3. Loads JavaScript from a random person's GitHub Pages site(lonelycpp.github.io) for YouTube embeds. If that account is compromised, arbitrary code runs in the app's WebView.
4. Loads third-party JavaScript from Elfsight(elfsightcdn.com/platform.js) for social media widgets, with no sandboxing.
5. Sends email addresses to Mailchimp, images are served from Uploadcare, and a Truth Social embed is hardcoded with static CDN URLs. None of this is government infrastructure.
6. Has no certificate pinning.Standard Android trust management.
7. Ships with dev artifacts in production.A localhost URL, a developer IP (10.4.4.109), the Expo dev client, and an exported Compose PreviewActivity.
8. Profiles users extensively through OneSignal- tags, SMS numbers, cross-device aliases, outcome tracking, notification interaction logging, in-app message click tracking, and full user state observation.
Is any of this illegal? Probably not. Is it what you'd expect from an official government app? Probably not either.
