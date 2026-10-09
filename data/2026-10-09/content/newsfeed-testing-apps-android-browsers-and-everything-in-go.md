---
title: Testing apps, Android, browsers, and everything in Googlebook OS | The Verge
url: https://www.theverge.com/tech/1008563/googlebook-software-impressions-thoughts-roundtable
site_name: newsfeed
content_file: newsfeed-testing-apps-android-browsers-and-everything-in-go
fetched_at: '2026-10-09T17:19:30.085730'
original_url: https://www.theverge.com/tech/1008563/googlebook-software-impressions-thoughts-roundtable
author: Antonio G. Di Benedetto
date: '2026-10-09'
published_date: '2026-10-09T13:36:02+00:00'
description: We’ve been testing Googlebook laptops from Dell, Lenovo, Asus, Acer, and HP all week — all five launch offerings — and we already have many thoughts about Google’s new operating system.
tags:
- the-verge
- android
- asus
- chrome
---

* Tech
* Gadgets
* Asus

# A week with Googlebooks: four notes from our testing so far

It’s been a whirlwind time of coming to grips with Google’s new laptops, and we’ve got feelings about Googlebook OS.

by
 
 
Antonio G. Di Benedetto
, 
 
David Pierce
, 
 
Stevie Bonifield
, and 
 
Dominic Preston
Oct 9, 2026, 1:36 PM UTC
* Link
* Share
* Gift
Software, software, software.
 
| Photo: Antonio G. Di Benedetto / The Verge
* Tech
* Gadgets
* Asus

# A week with Googlebooks: four notes from our testing so far

It’s been a whirlwind time of coming to grips with Google’s new laptops, and we’ve got feelings about Googlebook OS.

by
 
 
Antonio G. Di Benedetto
, 
 
David Pierce
, 
 
Stevie Bonifield
, and 
 
Dominic Preston
Oct 9, 2026, 1:36 PM UTC
* Link
* Share
* Gift

Google’s new operating system is off toa rocky start. The five newly launched Googlebook laptops have hardware that ranges from great to excellent, but the software in its current state is the weak point. There are four of us on staff atThe Vergeactively testing Googlebooks and, frankly, our internal Slack discussions have been mostly filled with collective venting of frustrations, disappointments, and bewilderment.

The promise of Googlebooks as a fresh and smartly designed alternative to Windows or Mac for Android phone owners sounds great, but there’s more than just a few kinks and quirks to work out. Some of its issues and challenges in the road ahead are systemic to Android.

While we’re actively testing each and every Googlebook from all of Google’s partner OEMs, we thought we’d come together and share a glimpse of where our heads are at with these new laptops.

## This should be better than ChromeOS, but right now it feels worse

Why does this Clear all button exist? Why can’t you swipe between active desktops or move windows between them? And why wasn’t that ready on day one?

While a lot of my thoughts are well documented in ourinitial hands-on article, I keep coming back to what a Google rep told me at the Googlebook launch preview: Replacing ChromeOS with Android will allow for much faster development. That’s great, but why does Googlebook OS feel like a bit of a set back from ChromeOS at launch? It shares some of ChromeOS’ flaws, like not allowing you to run Chrome with separate Google accounts. And many Android apps feel as clunky to run on a Googlebook as they did on ChromeOS. (Google even putAndroid’s navigation buttons on the Googlebook keyboard— seemingly in part as a fallback option for misbehaving apps.)

Every day I come across new oddities in any of the three Googlebooks I’m testing. The Signal Android app linked to my phone with ease, but I have to hit Ctrl+Enter to send messages and can’t highlight text — clicking and dragging scrolls up and down instead. Photoshop and Lightroom are passable for the simplest image editing, but I’d takea cheap Windows laptopwith the proper desktop apps over these mobile-first versions. You can’t drag and drop windows to other virtual desktops, and scrolling to the left of your desktops reveals a Clear All button that just kills all your apps at once. That’s straight out of the app switcher from Android on phones, but if I’m closing all apps at once on a laptop I’m either rebooting or shutting down.

Even something as simple as installing the progressive web app version of Slackisn’t working properly. So who should I be mad at? Slack or Google?

If I bought one of these Googlebooks I’d be mad at myself for being a paying beta tester for Google. I know that’s often the case for early adopters on a new OS, but these days I have less time and patience than when I bought my T-Mobile G1 / HTC Dream, Nexus 7, etc. There’s something cool here for sure with Googlebooks, but we need that “faster” development to go into warp speed.

— Antonio G. Di Benedetto, currently testing the HP Googlebook 14, Lenovo Googlebook 15, and Acer Googlebook 14

## Google has a big, big developer problem

Streaming apps like Crunchyroll are basically tablet apps. The keyboard can’t pause or rewind, and you have to click or touch the screen for those playback controls.

One of the reasons Googlebooks exist is that Android has become a mature, useful platform across a lot of screen sizes. It’s true: Android now works relatively well on your phone, tablet, TV, even your car. The apps are another story. Over and over in my testing so far, I’ve been amazed at the number of apps that seem to have no idea what to do with a Googlebook.

Take Netflix, for instance, which was one of the first apps I downloaded because I have some travel coming up and I’m psyched to finally be able to download movies for plane rides. The app works well enough, I suppose (and it does download movies!) but it launches as a full-screen, tablet-style version of the app. Basically every streaming app does so. If you hover over the top bar, the windowing option appears, but none of that is obvious. And launching and windowing app after app gets tiresome.

There are a few apps thatareproperly optimized for Googlebooks, and they make the device feel more like a proper laptop. But even they have some problems: many do that weird thing where they don’t show the app content when you’re resizing the window, for instance, which feels broken on a laptop. Even some of Google’s own apps do this, while others, like YouTube and Messages, scale more naturally. Some apps respond naturally to the keyboard and mouse; others don’t. Virtually everything is better optimized for a touchscreen. A note to developers: If I can’t pause the movie by whacking the space bar, your app doesn’t work with keyboards.

For the most part, I actually like the Android-ification of Google’s laptop strategy. Connecting deeply to your phone, running and syncing all your apps, even some of the phone-style interface decisions make sense to me. But just about every time I open an app, my Googlebook starts to seem like an Android tablet pretending to be a laptop. (And don’t forget: nobody has ever really wanted Android tablets.) Google’s going to need developers to get with the program, or it’ll never be more than that.

— David Pierce, currently testing the Dell XPS Googlebook

## Linux apps (probably) can’t save Googlebook OS

Apps in the Googlebook’s Linux virtual machine don’t show up in the taskbar or app tray.

A string of little annoyances has chipped away at my hopes for the new Googlebooks over the last few days. Some are more frustrating than others — losing a normal Caps Lock key isn’t a deal breaker, but getting stuck with only mobile browsers just might be. Android app compatibility seems to always be a roll of the dice, and so far Linux apps don’t seem like a viable alternative.

Slack was one of the first apps I tried installing from the Play Store, but it ended up being the mobile app awkwardly resized for a larger screen. So, I tried installing the Linux version of Slack through the Debian virtual machine that lives in the Googlebook’s Terminal app. I got it working, along with GIMP and Steam.

But the big catch is that anything you install on the virtual machineonlylives there. So, none of those apps have app drawer icons like my Android apps, and they don’t pop up in my taskbar when they’re running. I have to manually switch my mouse and keyboard between the VM and the rest of Googlebook OS, which makes jumping between Linux and Android apps slow and awkward. Since the Linux and Android apps are running in different environments, they don’t automatically share files or clipboard content, either.

I’ll have a dedicated write-up on the Googlebook gaming experience later, but the virtual machine hasn’t been great for that, either. I got Steam running, but the games I’ve tried (none of which are particularly resource-hungry) have been too laggy to be playable.

I’ve liked some parts of the Googlebook so far, but it’s hard to appreciate them when friction keeps popping up from Android and Linux apps alike.

— Stevie Bonifield, currently testing the Asus Googlebook 14

## The best bit of Googlebooks only works half the time

The Files app gives you quick access to what’s on your paired Android phone. But opening or transferring those files is anything but “quick.”
 
Photo: Antonio G. Di Benedetto / The Verge

The obvious selling point of the Googlebook, for me at least, has always been the “seamless” Android integration. And I’ve had a few moments this week when my phone and laptop have come together in a truly delightful way: replying to a WhatsApp message directly from the notification on the Googlebook; dipping into an app cast from my phone to quickly use it without reaching for my pocket; opening Quick Share to move files between the two devices in seconds.

But even here, so much of the experience right nowsucks. My phone connection drops in and out from the laptop, and I can’t for the life of me figure out how to connect a second phone or tablet. I used Quick Share for file transfer because using the Files app to browse the phone’s drive is painfully slow, taking minutes to open or transfer a single photo. Opening a notification to the phone-cast version of an app when you have it installed natively will never stop feeling awkward. And some apps cast terribly anyway: Bluesky renders text illegibly; my banking app won’t cast for security reasons; and my credit card one won’t because it just breaks.

Seamless, this is not. It’ll get better, I hope. Ithasto get better. When the Android integration works, it feels a little bit like magic. But that’s only because it happens so rarely — Google needs to make this reliable enough that it feels mundane instead.

— Dominic Preston, currently testing the Asus Googlebook 14 and HP Googlebook 14

Follow topics and authors
 from this story to see more like this in your personalized homepage feed and to receive email updates.
* Antonio G. Di Benedetto
* David Pierce
* Stevie Bonifield
* Dominic Preston
* Android
* Asus
* Chrome
* Chromebook
* Dell
* Gadgets
* Google
* Google Pixel
* HP
* Laptop Reviews
* Laptops
* Lenovo
* Reviews
* Tech

## Most Popular

Most Popular
1. Anthropic bans ‘abusive or cruel behavior’ toward Claude
2. GTA VI leaks continue with a lengthy (and very nude) gameplay video
3. Apple announces surprise ‘Welcome home’ launch event
4. Amazon is phasing out Fire Tablets because they weren’t ‘giving customers what they were asking for’
5. Hands-on with Amazon’s Alexa Tablet 12 Pro and its wild new matte display

## The Verge Daily

A free daily digest of the news that matters most.

Email (required)
Sign Up
By providing your information, you agree to our
 
Terms of Use
 
and our
 
Privacy Policy
. We use vendors that may also process your information to help provide our services. This site is protected by reCAPTCHA and the Google
 
Privacy Policy
 
and
 
Terms of Service
 
apply.
Advertiser Content From

This is the title for the native ad

## More inTech

YouTube, Meta, and Twitch won’t say if they’ll allow the US government to livestream an execution
The AI is in the computer
Instinct was the buzziest AI agent around — can it survive Muse?
Meta is banning TikTok ads across its platforms
Microsoft 365 Family subscribers will finally be able to share AI benefits
US plans livestream of execution by firing squad
YouTube, Meta, and Twitch won’t say if they’ll allow the US government to livestream an execution
Emma Roth
Two hours ago
The AI is in the computer
David Pierce
Two hours ago
Instinct was the buzziest AI agent around — can it survive Muse?
Allison Johnson
2:00 PM UTC
Meta is banning TikTok ads across its platforms
Emma Roth
1:12 PM UTC
Microsoft 365 Family subscribers will finally be able to share AI benefits
Tom Warren
7:14 AM UTC
US plans livestream of execution by firing squad
Jay Peters
Oct 8
Advertiser Content From

This is the title for the native ad

## Top Stories

2:00 PM UTC
Instinct was the buzziest AI agent around — can it survive Muse?
Two hours ago
Trump’s attempt to rename AI is looking awfully artificial
27 minutes ago
Frances Haugen hopes The Social Reckoning will inspire more whistleblowers
17 minutes ago
Microsoft tries to spark new life into Windows