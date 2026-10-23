---
title: Abandoned Popcorn Time apps had to be disabled to prevent a zombie army | The Verge
url: https://www.theverge.com/tech/1017914/popcorn-time-piracy-botnet-avoided
site_name: newsfeed
content_file: newsfeed-abandoned-popcorn-time-apps-had-to-be-disabled-to
fetched_at: '2026-10-23T21:57:38.810463'
original_url: https://www.theverge.com/tech/1017914/popcorn-time-piracy-botnet-avoided
author: Stevie Bonifield
date: '2026-10-23'
published_date: '2026-10-23T19:35:15+00:00'
description: Researchers remotely shut down a forgotten Popcorn Time updater hackers could have used to make a botnet.
tags:
- the-verge
- entertainment
- news
- security
---

* Tech
* Entertainment
* News

# Abandoned Popcorn Time apps had to be disabled to prevent a zombie army

What old and vulnerable software might be running on your PC right now?﻿

What old and vulnerable software might be running on your PC right now?﻿

by
 
 
Stevie Bonifield
Oct 23, 2026, 7:35 PM UTC
* Link
* Share
* Gift
Image: Popcorn Time
Part Of
Popcorn Time: the ‘Netflix for piracy’ that refuses to die
see all updates 
Stevie Bonifield
 
is a news writer covering all things consumer tech. Stevie started out at Laptop Mag writing news and reviews on hardware, gaming, and AI.

RememberPopcorn Time, the app that served as an easy-to-use front end for streaming torrents of movies and TV shows? Development of the MPAA’s least-favorite app of the 2010s has beenabandoned for years, but the “Netflix of Piracy” software is still installed on millions of devices that are just waiting to join a bot army. Researchers atEye Securityfound the updater for a Popcorn Time fork called “Time4Popcorn” still running on tons of Windows, macOS, and Android devices located around the world, phoning home to now-abandoned web domains over unencrypted HTTP and running an outdated, insecure version of Chrome.

Eye Security’s Niels Teusink says the updater could have been used to install and run basically any kind of software with full privileges, easily enabling someone to create a botnet just by taking over one of the domains, using a man-in-the-middle attack to target specific devices, or perform surveillance by identifying the machines running the software.

### Related

* Everyone is stealing TV
* FBI makes a massive botnet infecting more than 700,000 computers uninstall itself

Their solution was to register one of the domains and use it to send their own update that instructed the updater to disable itself. Despite ethical concerns about the fix, the researchers say their only alternative “was to do nothing,” pointing out, “The update process wasn’t doing anything functional anyway, it was only creating risk for users.”

Eye Security said on Windows devices, their update “simply stops and disables the service via the Service Control Manager” without deleting any files or anything else. On macOS, it uses a shell script to execute a command that blocks the update process from starting. They didn’t address the software on Android devices, where installing the update would still require actual user interaction first.

They had to tweak their update after it was uploaded to VirusTotal, causing security programs to flag it as malware and block it while leaving the vulnerable updater running. It’s unclear exactly how many devices were at risk, but Eye Security says it “sent out over 2 million update downloads” by March, when they stopped sending the update and transferred the domains they used to theShadowserver Foundation, a web security non-profit.

Follow topics and authors
 from this story to see more like this in your personalized homepage feed and to receive email updates.
* Stevie Bonifield
* Entertainment
* News
* Security
* Streaming
* Tech

## More in:Popcorn Time: the ‘Netflix for piracy’ that refuses to die

Popcorn Time’s best-known app comes back to life
Adi Robertson
Feb 26, 2016
The Pirate Bay now lets you stream torrents from your browser
James Vincent
Feb 8, 2016
The most popular Popcorn Time fork has been shut down
James Vincent
Oct 26, 2015

## Most Popular

Most Popular
1. Now Google says it might use your Gmail and Google Photos data to target ads
2. The first broken iPhone Duos are here
3. Tesla driver using Full Self-Driving struck and killed a man crossing I-80
4. People are vibe coding their way to better TVs
5. The iPhone Duo is a messy, expensive, good time

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

Elon Musk’s dangerous grip on outer space
The iPhone Duo should have been an iPad
Now Google says it might use your Gmail and Google Photos data to target ads
The first broken iPhone Duos are here
SpaceX’s mobile carrier push reportedly involves tapping into 80,000 cell sites
Meta delays new business terms after publisher pushback on AI scraping
Elon Musk’s dangerous grip on outer space
Georgina Torbet
5:35 PM UTC
The iPhone Duo should have been an iPad
David Pierce
5:00 PM UTC
Now Google says it might use your Gmail and Google Photos data to target ads
Jess Weatherbed
4:52 PM UTC
The first broken iPhone Duos are here
Jay Peters
4:37 PM UTC
SpaceX’s mobile carrier push reportedly involves tapping into 80,000 cell sites
Emma Roth
3:16 PM UTC
Meta delays new business terms after publisher pushback on AI scraping
Emma Roth
2:47 PM UTC
Advertiser Content From

This is the title for the native ad

## Top Stories

1:00 PM UTC
People are vibe coding their way to better TVs
5:35 PM UTC
Elon Musk’s dangerous grip on outer space
10:00 AM UTC
No, the iPhone Duo isn’t a small phone
1:00 PM UTC
Netflix can’t fire its way out of this downward spiral
12:00 PM UTC
Retro gaming is being overrun with AI