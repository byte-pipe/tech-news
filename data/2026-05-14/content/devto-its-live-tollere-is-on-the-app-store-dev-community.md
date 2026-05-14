---
title: It's live. Tollere is on the App Store. - DEV Community
url: https://dev.to/stokry/its-live-tollere-is-on-the-app-store-581o
site_name: devto
content_file: devto-its-live-tollere-is-on-the-app-store-dev-community
fetched_at: '2026-05-14T11:37:12.079972'
original_url: https://dev.to/stokry/its-live-tollere-is-on-the-app-store-581o
author: Stokry
date: '2026-05-12'
description: I wrote about this a few weeks ago. My wife and I had a shopping list app we built for ourselves,... Tagged with showdev, ios, swift.
tags: '#showdev, #ios, #swift'
---

Minimalist family tool used for years

I wrote about this a few weeks ago.My wife and I had a shopping list app we built for ourselves, used it for years, and finally shipped it to TestFlight.

A few hundred people tried it. Nobody complained about missing features. A few said it was exactly what they needed.

So we submitted.

Apple approved it. It's out.

## What it is, again

A shopping list. That's it.

You add items. You swipe them done. If something is urgent — milk, or whatever you keep forgetting — you mark it. Everyone on the list gets a push notification.

No categories. No folders. No "are you sure?" dialogs. No recipes, no meal planning, no barcode scanner.

One list. One gesture. The thing you needed at the store.

## What changed since TestFlight

Honestly, not much. We fixed a bug where the shared list would sometimes take a few minutes to appear on the other person's phone after accepting the invite. CloudKit propagation is slow sometimes, so now the app just retries quietly until items show up.

Other than that — the feedback from testers was mostly "this is good, don't add stuff."

So we didn't.

## Sharing

The one feature beyond "list" is the shared list. You generate a link, send it through iMessage or WhatsApp or wherever, and the other person installs the app and joins.

One live list between two people. No accounts to create, no email sign-up, no syncing nonsense. It just works over iCloud.

This is a Pro feature. One-time, €6.99. No subscription, no annual renewal, nothing to cancel.

The person who joins your list doesn't need to pay anything. They get full access as a participant.

## Why we shipped it

We genuinely use it every week. Every grocery run, my wife sends me a notification that milk is urgent and I stop ignoring the list.

It was built for us. It turns out other people want the same thing.

If you want a shopping list that does one thing well —here it is.

## Stack, if you're curious

SwiftUI, SwiftData, CloudKit. Dark mode only. No backend on our side — everything lives in iCloud.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (13 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse