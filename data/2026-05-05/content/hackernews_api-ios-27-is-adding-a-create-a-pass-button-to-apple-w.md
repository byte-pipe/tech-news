---
title: iOS 27 is adding a 'Create a Pass' button to Apple Wallet
url: https://walletwallet.alen.ro/blog/ios-27-wallet-create-pass/
site_name: hackernews_api
content_file: hackernews_api-ios-27-is-adding-a-create-a-pass-button-to-apple-w
fetched_at: '2026-05-05T20:06:08.749899'
original_url: https://walletwallet.alen.ro/blog/ios-27-wallet-create-pass/
author: alentodorov
date: '2026-05-05'
description: Bloomberg reports that iOS 27 will let iPhone users build their own Wallet passes from any QR code. Three templates, no developer account, no certificate. Here is what we know, and what it means for third-party pass tools like WalletWallet.
tags:
- hackernews
- trending
---

Bloomberg's Mark Gurman reported on Monday that iOS 27 will add a "Create a Pass" feature to the Wallet app. Tap the "+" button you already use to add credit cards or pass emails, and Wallet will offer something it has never offered before on iPhone: a path to build your own pass.

 

You can scan a QR code on a paper ticket or membership card with the camera, or build a pass from scratch in a layout editor. The whole flow runs without an Apple Developer account, a Pass Type ID, or any certificate signing.

 

iOS 27 is expected to preview at WWDC on June 8, with a public release in September.

 
 
 

## How the new flow works

 

Reporting from Bloomberg, MacRumors, 9to5Mac, and AppleInsider lines up on the same workflow. Inside the Wallet app, the existing "+" button gains a new option for creating a pass. From there you choose between two starting points:

 
* Scan a QR code from a paper card, ticket, or screen
* Build a custom pass from scratch with no scan needed
 

Once you are in the editor, Wallet exposes adjustable styles, images, colors, and text fields. The reports describe a fairly conventional template-driven layout, closer in spirit to what Pass2U, WalletWallet, and other third-party generators have offered for years than to Apple's developer-only PassKit pipeline.

 
 
 

## Three templates, color-coded

 

Apple is testing three starting templates, each tied to a default color:

 
* Standard (orange):the default for any general-purpose pass.
* Membership (blue):geared toward gyms, clubs, libraries, and other recurring-access cards.
* Event (purple):meant for tickets to games, movies, and one-off occasions.
 

The color choice is not just decoration. Wallet currently sorts passes visually in the stack, and the template hue is what sets each card apart at a glance, so a quick look is enough to pick out the orange punch card from the purple ticket without reading a word.

 
 
 

## Why now: 14 years of PassKit drought

 

Apple shipped PassKit alongside iOS 6 back in 2012. The pitch was clean: businesses build .pkpass files, customers tap to add, everyone wins. In practice, the consistent adopters ended up being airlines, big-box retailers, ticketing platforms, and a handful of national chains. Most gyms, cafes, libraries, rec centers, and small loyalty programs never built one, because the path requires an Apple Developer account, signing certificates, and enough engineering work that "just print a paper card" almost always won the budget conversation.

 

The Next Web's framing is blunt: Apple is no longer waiting on developers. With Create a Pass, the supply-side problem is finally being solved from the demand side. If the business will not build a Wallet pass, the user does it themselves from the QR code that business already printed.

 

That is a meaningful shift in posture. For more than a decade, Wallet has been a directory of what brands chose to ship. In iOS 27 it becomes a directory of what people choose to keep.

 
 
 

## What this means for WalletWallet

 

We will be honest. WalletWallet exists because of this exact gap. You take a barcode from any loyalty card, paste it into our web app, pick a color, and a free Apple Wallet pass lands on your phone in about a minute, all from the browser without an account or any developer setup. Once Create a Pass ships in September, a chunk of that workflow moves natively into the iPhone Wallet app.

 

That is good for users. We started this project to make Wallet friendlier for the cafes-and-gyms long tail, and Apple agreeing with us at OS-level scope is a healthy outcome. The category needed it.

 

A few places where we still help, even after iOS 27 ships:

 
* Google Wallet.Create a Pass is iPhone-only. Roughly half of the wallet-using world is on Android, and our generator builds Google Wallet passes from the same form.
* Web, no OS upgrade.iOS 27 needs a compatible iPhone and the September update. WalletWallet runs in any browser today. iOS 14, iPad, Mac, a friend's laptop, all fine.
* Tag passes with real integrations.Our Bandcamp, SoundCloud, and Spotify pass builders pull artist art and links automatically into a tag pass. That is a different shape from the generic templated pass Apple is showing.
* Sharing.A web-generated .pkpass is just a file. You can email it, post it, hand it to a friend on Android via QR. The Wallet-native flow is more locked to the device that built it.
 

We expect to lose volume on the simplest one-barcode-to-Wallet case once Create a Pass goes live. That is fine. The reason WalletWallet started was that Apple's bar for a Wallet pass was too high for normal people. If iOS 27 lowers that bar, the world we wanted is closer.

 
 
 

## What we still do not know

 

The current reports cover the UI, the templates, and the high-level workflow. They are silent on a lot of details that matter:

 
* Whether iCloud will sync user-created passes across iPhone, iPad, and Mac
* Whether passes can be exported as .pkpass files to share with non-iPhone users
* Whether Wallet supports Code 128, PDF417, and Aztec barcodes, or only QR
* Whether merchants can claim, co-sign, or update user-created passes after the fact
* Whether passes have lock-screen behavior tied to time and location, the way developer-issued passes do today
 

We will know more once Apple previews iOS 27 at WWDC on June 8, and again when the first developer betas land. We will update this post when there is something concrete to add.

 
 
 

## Quick recap

 

iOS 27 is adding a Create a Pass button to the Wallet app, with a QR-scan or build-from-scratch flow and three color-coded templates: Standard (orange), Membership (blue), and Event (purple). Bloomberg broke the story on May 4, and a public release is expected in September 2026. It will be the first time iPhone users do not need a third-party tool to put a barcode into Wallet, and for us that is a sign the category is maturing the right way.

 
 
 

## Sources

 
* Bloomberg: iOS 27 Features: Apple Plans to Let Users Build Their Own Passes in Wallet App (May 4, 2026)
* 9to5Mac: iOS 27: Apple Wallet adding new 'Create a Pass' feature, per report
* MacRumors: iOS 27 Will Let You Create Custom Wallet Passes
* AppleInsider: Apple Wallet will let you make your own passes in iOS 27
* The Next Web: iOS 27 lets users create custom Wallet passes from any QR code as Apple gives up waiting for developers
* Cult of Mac: Apple could remove a key iPhone Wallet app limitation with iOS 27