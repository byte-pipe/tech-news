---
title: The EU made Apple adopt new Wi-Fi standards, and now Android can support AirDrop - Ars Technica
url: https://arstechnica.com/gadgets/2025/11/the-eu-made-apple-adopt-new-wi-fi-standards-and-now-android-can-support-airdrop/
site_name: hackernews_api
fetched_at: '2025-11-27T11:07:02.073457'
original_url: https://arstechnica.com/gadgets/2025/11/the-eu-made-apple-adopt-new-wi-fi-standards-and-now-android-can-support-airdrop/
author: cyclecount
date: '2025-11-26'
published_date: '2025-11-20T20:11:01+00:00'
description: Google’s Pixel 10 works with AirDrop, and other phones should follow later.
tags:
- hackernews
- trending
---

Text
 settings

Last year, Applefinally added supportfor Rich Communications Services (RCS) texting to its platforms, improving consistency, reliability, andsecuritywhen exchanging green-bubble texts between the competing iPhone and Android ecosystems. Today, Google is announcing another small step forward in interoperability, pointing to a slightly less annoying future for friend groups or households where not everyone owns an iPhone.

Googlehas updatedAndroid’s Quick Share feature to support Apple’s AirDrop, which allows users of Apple devices to share files directly using a local peer-to-peer Wi-Fi connection. Apple devices with AirDrop enabled and set to “everyone for 10 minutes” mode will show up in the Quick Share device list just like another Android phone would, and Android devices that support this new Quick Share version will also show up in the AirDrop menu.

Google will only support this feature on the Pixel 10 series, at least to start. The company is “looking forward to improving the experience and expanding it to more Android devices,” but it didn’t announce anything about a timeline or any hardware or software requirements. Quick Share also won’t work with AirDrop devices working in the default “contacts only” mode, though Google “[welcomes] the opportunity to work with Apple to enable ‘Contacts Only’ mode in the future.” (Reading between the lines: Google and Apple are not currently working together to enable this, andGoogle confirmed to The Vergethat Apple hadn’t been involved in this at all.)

Like AirDrop, Google notes that files shared via Quick Share are transferred directly between devices, without being sent to either company’s servers first.

Google shared a little more information ina separate post about Quick Share’s security, crediting Android’s use of the memory-safe Rust programming language with making secure file sharing between platforms possible.

“Its compiler enforces strict ownership and borrowing rules at compile time, which guarantees memory safety,” writes Google VP of Platforms Security and Privacy Dave Kleidermacher. “Rust removes entire classes of memory-related bugs. This means our implementation is inherently resilient against attackers attempting to use maliciously crafted data packets to exploit memory errors.”

## Why is this happening now?

Google doesn’t mention it in either Quick Share post, but if you’re wondering why it’s suddenly possible for Quick Share to work with AirDrop, it can almost certainly be credited to European Union regulations imposed under the Digital Markets Act (DMA).

Let’s start with how AirDrop works. Like many of Apple’s “Continuity” features that rely on wireless communication between devices, AirDrop uses Bluetooth to allow devices to find each other, and a fast peer-to-peer Wi-Fi connection to actually transfer files and other data. This isn’t exotic hardware; all smartphones, tablets, and computers sold today include some flavor of Bluetooth and Wi-Fi.

But to make those Continuity features work, Apple also developed a proprietary protocol called Apple Wireless Direct Link (AWDL) to facilitate the actual connection between devices and the data transfer. Because this wasn’t a standard anyone could use, other companies couldn’t try to make their own wireless sharing features compatible with AirDrop.

Butearlier this year, the EUadopted new specification decisionsthat required Apple to adopt new interoperable wireless standards, starting in this year’s iOS 26 release. If you don’t want to wade through the regulatory documents,this postfrom cloud services company Ditto is a useful timeline of events written in plainer language.

 Setting AirDrop to “everyone for 10 minutes” mode on an iPhone.



 Credit:


 Andrew Cunningham



The rulings required Apple to add support for the Wi-Fi Alliance’sWi-Fi Aware standardinstead of AWDL—and in fact required Apple to deprecate AWDL and to help add its features to Wi-Fi Aware so that any device could benefit from them. This wasn’t quite the imposition it sounded like; Wi-Fi Awarewas developed with Apple’s help, based on the work Apple had already done on AWDL. But it meant that Apple could no longer keep other companies out of AirDrop by using a functionally similar but private communication protocol instead of the standardized version.

In some ways, Apple’s journey to Wi-Fi Aware recalls the iPhone’s journey to USB-C: first, Apple developed a proprietary port that achieved some of the same goals as USB-C; Apple then contributed work to what would become the standardized USB-C connector; but then the company hesitated to actually adopt the standardized port in its phones until its hand wasforced by regulators.

In any case, Wi-Fi Aware was added to iOS 26 and iPadOS 26, andApple’s developer documentationlists the specific hardware that supports it (the iPhone 12 and later, and most iPads released within the last three or four years). For Android users, that likely means that Quick Share will only work with AirDrop on those devices, if they’ve been updated to iOS/iPadOS 26 or later. Googlehas supported Wi-Fi Awarein Android since version 8.0, so it should at least theoretically be possible for most modern Android phones to add support for the feature in software updates somewhere down the line.

Apple’s hardware support list also suggests that Android phoneswon’twork with AirDrop on the Mac, since macOS 26 isn’t listed as a supported operating system on Apple’s Wi-Fi Aware (it’s likely not a coincidence that macOS is not considered to be a “gatekeeper” operating system under the DMA, as both iOS and iPadOS are).

If I had to guess why neither of Google’s Quick Share posts mentions Wi-Fi interoperability standards or the DMA, it may be because Google has beencomplainingaboutvarious aspects of the lawand its enforcement sincebefore it was even passed(as have many US tech companies designated as gatekeepers by the law). Google has occasionally tried to take advantage of the DMA, as it didwhen it arguedthat Apple’s iMessage service should be opened up. But it may be that Google doesn’t want to explicitly credit or praise the DMA in its press releases when the company isfacing the possibility of huge finesunder the same law.

The New York Timesreported earlier this weekthat EU regulators are considering changes to some of its tech regulations, citing concerns about “overregulation” and “competitiveness,” but that the EU was not currently considering changes to the DMA. For its part, Apple recentlycalled for the DMA to be repealed entirely.

 Andrew Cunningham


Senior Technology Reporter

 Andrew Cunningham


Senior Technology Reporter

 Andrew is a Senior Technology Reporter at Ars Technica, with a focus on consumer tech including computer hardware and in-depth reviews of operating systems like Windows and macOS. Andrew lives in Philadelphia and co-hosts a weekly book podcast called
Overdue
.


1. 1.Plex’s crackdown on free remote streaming access starts this week
2. 2.OpenAI says dead teen violated TOS when he used ChatGPT to plan suicide
3. 3.Vision Pro M5 review: It’s time for Apple to make some tough choices
4. 4.There may not be a safe off-ramp for some taking GLP-1 drugs, study suggests
5. 5.Tech firm’s new CTO gets indicted; company then claims he was never CTO

Customize
