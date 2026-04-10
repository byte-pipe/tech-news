---
title: FBI used iPhone notification data to retrieve deleted Signal messages - 9to5Mac
url: https://9to5mac.com/2026/04/09/fbi-used-iphone-notification-data-to-retrieve-deleted-signal-messages/
site_name: hackernews_api
content_file: hackernews_api-fbi-used-iphone-notification-data-to-retrieve-dele
fetched_at: '2026-04-10T19:22:16.178846'
original_url: https://9to5mac.com/2026/04/09/fbi-used-iphone-notification-data-to-retrieve-deleted-signal-messages/
author: Marcus Mendes
date: '2026-04-10'
published_date: '2026-04-09T23:42:46+00:00'
description: The FBI was able to recover deleted Signal messages from an iPhone by extracting data stored in the device’s notification database.
tags:
- hackernews
- trending
---

* AAPL Company
* FBI
* Signal

# FBI used iPhone notification data to retrieve deleted Signal messages

 

Marcus Mendes
 | Apr 9 2026 - 4:42 pm PT																

A new report from404 Mediareveals that the FBI was able to recover deleted Signal messages from an iPhone by extracting data stored in the device’s notification database. Here are the details.

## Notification history was accessed even after Signal was deleted

According to404 Media, testimony in a recent trial involving “a group of people setting off fireworks and vandalizing property at the ICE Prairieland Detention Facility in Alvarado, Texas,” showed that the FBI was able to recover content of incoming Signal messages from a defendant’s iPhone, even though Signal had been removed from the device:

One of the defendants was Lynette Sharp, whopreviously pleaded guiltyto providing material support to terrorists. During one day of the related trial, FBI Special Agent Clark Wiethorn testified about some of the collected evidence. A summary of Exhibit 158 publishedon a group of supporters’ websitesays, “Messages were recovered from Sharp’s phone through Apple’s internal notification storage—Signal had been removed, but incoming notifications were preserved in internal memory. Only incoming messages were captured (no outgoing).”

As404 Medianotes, Signal’s settings include an option that prevents the actual message content from being previewed in notifications. However, it appears the defendant did not have that setting enabled, which, in turn, seemingly allowed the system to store the content in the database.

404 Mediareached out to Signal and Apple, but neither company provided any statements on how notifications are handled or stored.

## But how does this internal storage work?

With little to no technical details about the exact condition of the defendant’s iPhone, it is obviously impossible to pinpoint the precise method the FBI used to recover the information.

For instance, there are multiple system states an iPhone can be in, each with its own security and data access constraints, such as BFU (Before First Unlock), AFU (After First Unlock) mode, and so on.

Security and data access also change even more dramatically when the device is unlocked, since the system assumes the user is present and permits access to a wider range of protected data.

That said, iOS does store and cache a lot of data locally, trusting that it can rely on these different states to keep that information safe but readily available in case the device’s rightful owner needs it.

Another important factor to keep in mind: the token used to send push notifications isn’t immediately invalidated when an app is deleted. And since the server has no way of knowing whether the app is still installed after the last notification it sent, it may continue pushing notifications, leaving it up to the iPhone to decide whether to display them.

Interestingly, Apple just changed how iOS validates push notification tokens oniOS 26.4. While it is impossible to tell whether this is a result of this case, the timing is still notable.

 
 
 
Post by @_inside@mastodon.social
 
View on Mastodon
 
 

Back to the case, given Exhibit 158’s description that the messages “were recovered from Sharp’s phone through Apple’s internal notification storage,” it is possible the FBI extracted the information from a device backup.

In that case, there are many commercially available tools for law enforcement that exploit iOS vulnerabilities to extract data that could have helped the FBI access this information.

To read404 Media’s original report of this case,follow this link.

#### Worth checking out on Amazon

* David Pogue – ’Apple: The First 50 Years’
* MacBook Neo
* Logitech MX Master 4
* AirPods Pro 3
* AirTag (2nd Generation) – 4 Pack
* Apple Watch Series 11
* Wireless CarPlay adapter

FTC: We use income earning auto affiliate links.More.

You’re reading 9to5Mac — experts who break news about Apple and its surrounding ecosystem, day after day. Be sure to check out 
our homepage
 for all the latest news, and follow 9to5Mac on 
Twitter
, 
Facebook
, and 
LinkedIn
 to stay in the loop. Don’t know where to start? Check out our 
exclusive stories
, 
reviews
, 
how-tos
, and 
subscribe to our YouTube channel
 

Check out 9to5Mac on YouTube for more Apple news:

 

## Comments

## Guides

### AAPL Company

Breaking news from Cupertino. We’ll give you t…

### FBI

Signal

## Author

 

			Marcus Mendes		

https://www.threads.com/mvcmendes			

Marcus Mendes is a Brazilian tech podcaster and journalist who has been closely following Apple since the mid-2000s.

He began covering Apple news in Brazilian media in 2012 and later broadened his focus to the wider tech industry, hosting a daily podcast for seven years.