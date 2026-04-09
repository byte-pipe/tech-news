---
title: 'Pebble Watch Software Is Now 100% Open Source + Tick Talk #4 - PT2 Demos!'
url: https://ericmigi.com/blog/pebble-watch-software-is-now-100percent-open-source
site_name: hackernews_api
fetched_at: '2025-11-25T11:07:34.979170'
original_url: https://ericmigi.com/blog/pebble-watch-software-is-now-100percent-open-source
author: Eric Migicovsky
date: '2025-11-24'
published_date: '2025-11-24'
description: 'Pebble Watch Software Is Now 100% Open Source + Tick Talk #4 - PT2 Demos!'
tags:
- hackernews
- trending
---

← Back to Home

# Pebble Watch Software Is Now 100% Open Source + Tick Talk #4 - PT2 Demos!

[
2025-11-24
]

Another big Pebble update today! TLDR:

* Yesterday, Pebble watch software was ~95% open source. Today, it’s 100% open source. You can download, compile and run all the software you need to use your Pebble. We justpublishedthe source codefor the new Pebble mobile app!
* Pebble Appstore now has a publiclyavailable backupand supports multiple feeds, providing long term reliability through decentralization. We’ve launched our own feed and Developer Dashboard.
* Pebble Time 2schedule update(aiming to begin shipping in January, with most arriving on wrists in March/April)
* NewTick Talk episode #4is up, with Pebble Time 2 demos!

Pre-production Pebble Time 2 (Black/Red colourway) in all its glory

### Pebble watch software is now 100% open source#

Over the last year, and especially in the last week, I've chatted with tons of people in the Pebble community. One of the main questions people have is ‘how do I know that my new Pebble watch will continue to work long into the future?’. It’s an extremely valid question and concern - one that I share as a fellow Pebble wearer. I called this out specificallyin my blog postannouncing the relaunch in January 2025. How is this time round going to be different from last time?

There are two pieces to making Pebble sustainable long term - hardware and software.

Hardware

Nothing lasts forever, especially an inexpensive gadget like a Pebble. We want to be able to keep manufacturing these watches long into the future - mostly because I will always want one on my wrist! The company I set up to relaunch Pebble, Core Devices, is self funded, built without investors, and extremely lean. As long as we stay profitable (ie we don’t lose money), we will continue to manufacture new watches.

We’re also making sure that our new watches are more repairable than old Pebble watches. The back cover of Pebble Time 2 is screwed in. You can remove the back cover and replace the battery.

We’ve also publishedelectrical and mechanical design filesfor Pebble 2 Duo. Yes, you can download the schematic (includes KiCad project files) right now onGithub! This should give you a nice jumpstart to designing your own PebbleOS-compatible device.

Software

Last time round, barely any of the Pebble software was open source. This made it very hard for the Pebble community to make improvements to their watches after the company behind Pebble shut down. Things are different now! This whole relaunch came about primarily because Google open sourced PebbleOS (thank you!). Yesterday, the software that powers Pebble watches was around 95% open source. As of today, it’s now 100%. This means that if Core Devices were to disappear into a black hole, you have all the source code you need to build, run and improve the software behind your Pebble.

I confess that I misunderstood why 95% was much less sustainable than 100% until recently. I discuss this in more detail in my latest Tick Talk episode (check it out). Long story short - I’m an Android user and was happy to sideload the old Pebble APK on my phone, but iPhone and other Android users have basically been stuck without an easily available Pebble mobile companion app for years.

Here’s how we’re making sure the 3 main Pebble software components are open source and guaranteed to work long into the future:

PebbleOS- software that runs on your watch itself. This has been 100% open source since January and we’ve committed to open sourcing all the improvements we’ve made →github.com/coredevices/PebbleOS. You can download the source code,compile PebbleOSand easily install it over Bluetooth on your new Pebble. Textbook definition of open source!

Pebble mobile companion app- the app that for your iPhone or Android. Without the app, your Pebble is basically a paperweight. When the Pebble Tech Corp died, the lack of an open source mobile app made it difficult for anyone to continue to use their watches. We had to build an entirely new app (get it here). Today, our app is now100% open source on Github- ensuring that what happened beforecannothappen again. Want to learn more about how we built the new app cross platform using Kotlin Multiplatform? Watch Steve’spresentation at Droidcon.

Developer tools and Pebble Appstore- this software enables people to build and share their watchapps and watchfaces.

In the case of dev tools, just being open source is not enough. They needed to be updated to work on modern computers. Before we made improvements, the state of the art of Pebble app development was using an Ubuntu virtualbox VM with Python2! Over the summer, ourincredibly productive internupgraded all theSDK and dev toolsand created anew way to develop Pebble apps in the browser. You should check them out!

Then there’s the Pebble Appstore. This is a collection of nearly 15,000 watchfaces and watchapps that you - the Pebble community - developed between 2012 and July 2018. When Fitbit pulled the plug on the original Pebble Appstore, the Rebble Foundation downloaded a copy of all the apps and faces, and set up a new web service to let users of the old Pebble app continue to download and use watchfaces. This was an incredible effort, one that I have used thousands of times and am a happy paying subscriber. But it’s still centralized - if their server disappears, there is no freely available backup.

To compensate for that, today we’re launching two new things:

* The Pebble mobile app will soon (later this week) be able to subscribe to multiple appstore ‘feeds’. This is similar to open source package managers like pip, AUR, APT, etc. Anyone can create a Pebble-compatible appstore feed and users will be able to browse apps from that feed in the Pebble mobile app.
* We’ve created our own Pebble Appstore feed (appstore-api.repebble.com) and newDeveloperDashboard. Our feed (fyi powered by 100% new software) is configured to back up an archive of all apps and faces toArchive.org(backup will gradually complete over the next week). Today, our feed only has a subset of all Pebble watchfaces and apps (thank you aveao for creatingPebble Archive!). Developers - you canuploadyour existing or new apps right now! We hope that this sets a standard for openness and we encourage all feeds to publish a freely and publicly available archive.

Important to note - developers will still be able to charge money for their apps and faces, using Kiezel pay or other services. This change does not preclude them from doing that, in fact it makes it even easier - I could see some developers creating a paid-only feed. As Irecently wrote, we're also working on other ways for Pebble developers to earn money by publishing fun, beautiful and creative Pebble apps.

Another important note - some binary blobs and other non-free software components are used today in PebbleOS and the Pebble mobile app (ex: the heart rate sensor on PT2 , Memfault library, and others). Optional non-free web services, like Wispr-flow API speech recognizer, are also used. These non-free software components are not required - you can compile and run Pebble watch software without them. This will always be the case. More non-free software components may appear in our software in the future. The core Pebble watch software stack (everything you need to use your Pebble watch) will always be open source.

### Pebble Time 2 more details - finally!#

Pre-production Pebble Time 2. These watches are not final quality! We are still tweaking and tuning everything.

PT2 Schedule Update

We’re currently in the middle of Pebble Time 2 design verification test (DVT) phase. After we finish that, we go into production verification test (PVT) and then mass production (MP). So far, things are proceeding according to the schedule update I sharedlast monthbut that is extraordinarily subject to change. We still have a lot of testing (especially waterproof and environmental) to go. If we find problems (which is likely) we will push the schedule back to make improvements to the product.

The one major complicating factor is the timing of Chinese New Year (CNY). It’s early next year - factories will shut down for 3 weeks starting around the end of January. After restarting, things always take a week or two to get back to full speed.

We are trying our best to get into mass production and ship out at most several thousand Pebble Time 2s before CNY. It’s going to be very tight 🤞. More likely is that production will begin after CNY, then we need to transfer the watches to our fulfillment center, and ship them out. Realistically, at this time we’re forecasting that the majority of people will receive their PT2 in March and April. Please keep in mind that things may still change.

Picking a PT2 colour

There will be 4 colour options for PT2 - black/black, black/red, silver/blue, silver/(white most likely). Let me be crystal very clear - no one has picked a colour yet 😃. In a few weeks, I will send out an email asking everyone who pre-ordered a Pebble Time 2 to select which colour they would like to receive.Please do not email us asking when this email will be sent out. No one has been invited yet to do this. I will post here after all emails have gone out.

On a related note, I am extremely happy that we built and shipped Pebble 2 Duo. Not only is it an awesome watch, it was also a phenomenal way for us to exercise our production muscles and ease back into the systematic flow of building and shipping smartwatches.

### PT2 Demo!#

A video is worth a million words - so I encourage you to watch me demo Pebble Time 2 watches I just received this week. Keep in mind these watches are PRE-PRODUCTION which means they parts have imperfect qualities! Subject to change!

The video below opens to the part of the video where I do the demo.
