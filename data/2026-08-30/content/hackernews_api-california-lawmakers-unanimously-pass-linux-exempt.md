---
title: California lawmakers unanimously pass Linux exemption from age-verification law — software distributed under the GPL, MIT, BSD, and Apache licenses are exempt | Tom's Hardware
url: https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt
site_name: hackernews_api
content_file: hackernews_api-california-lawmakers-unanimously-pass-linux-exempt
fetched_at: '2026-08-30T15:11:55.912852'
original_url: https://www.tomshardware.com/software/linux/california-lawmakers-unanimously-pass-linux-exemption-from-age-verification-law-software-distributed-under-the-gpl-mit-bsd-and-apache-licenses-are-exempt
author: shscs911
date: '2026-08-30'
published_date: '2026-08-29T15:57:13Z'
description: AB 1856 excludes open-source operating systems from the upcoming Digital Age Assurance Act.
tags:
- hackernews
- trending
---

(Image credit: Getty Images)

* Copy link
* Facebook
* X
* Whatsapp
* Reddit
* Pinterest
* Flipboard
* Email

Share this article

19

Join the conversation

Follow us

Add us as a preferred source on Google

Newsletter

Subscribe to our newsletter

California’s legislature has passedAssembly Bill 1856, exempting open-source operating systems from the State’s Digital Age Assurance Act months before the law is due to take effect on January 1, 2027. The Senate amended the Bill on August 21 before passing it on the 26th in a 39-0 vote, with the Assembly then accepting these changes in a concurrence vote the following day. The amendment ends almost a year of uncertainty surroundingwhether Linux distributions and SteamOS would be forced to collect user age dataduring account setup alongside Windows, macOS, iOS, and Android. AB 1856 has now been sent to Governor Gavin Newsom, who signed the original act into law last October.

These amendments redefine the term “operating system provider” to exclude any person or entity that distributes an OS or application “under license terms that permit a recipient to copy, redistribute, and modify the software.” Any software distributed under the GPL, MIT, BSD, and Apache licenses satisfies that test, which removes the likes of Debian, Fedora, Ubuntu, Arch, and the BSD family from AB 1856’s scope.

A second exclusion removes software components that aren’t “offered to consumers as a stand-alone executable application through a covered application store” from the law’s definition of an application, covering libraries and dependencies distributed through package managers like apt and pacman. AB 1856 doesn’t explicitly say that repos aren’t app stores, but a store’s main obligation under the law is to request an age signal from the user’s OS provider and pass it to developers; an exempt open-source OS produces no signal. A third carve-out excludes storefronts distributing extensions or add-ons that run exclusively inside a host application, which takes browser extension stores out of scope.

Latest Videos From
Tom's Hardware
Watch full video here: 

The amendments to AB 1856 also remove the original definition of “user,” which read, “a child that is the primary user of a device,” and technically classified every device owner in California as a child. The law’s signaling framework depends on adults declaring their age on account setup, so their devices get flagged as 18 and over, but under that definition nobody could ever be flagged as an adult.

In addition, lawmakers inserted a new provision prohibiting anyone from requesting an age signal from an OS provider or app store unless required by law. That closes off potential abuse of the age API that could have led to it being used as a general-purpose data collection channel even when age verification wasn’t required. Platforms and developers also gain a good-faith safe harbor against erroneous signals, protecting them from liability when age-gating signals are inaccurate.

Windows, macOS, iOS, and Android remain fully in scope, with age collection required at account setup from January 1, 2027. A later July 1, 2027, deadline applies to devices set up before January 1. Whether SteamOS is in scope isn’t yet clear: its Arch-based system components are open source, butValvedistributes the image alongside the proprietary Steam client. GrapheneOS, which in March said it wouldrefuse to comply with age-verification mandates, is distributed under open-source MIT and Apache licenses and now falls outside the law’s scope entirely, though Brazil’s Digital ECA still applies to it.

Assemblymember Buffy Wicks, who wrote both the Digital Age Assurance Act and the AB 1856 amendment,introduced the exemption back in Februaryfollowing criticism from Linux developers and the Electronic Frontier Foundation.

Stay On the Cutting Edge: Get the Tom's Hardware Newsletter

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Contact me with news and offers from other Future brands
Receive email from us on behalf of our trusted partners or sponsors
 

FollowTom's Hardware on Google News, oradd us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

Luke James
Contributor

Luke James is a freelance writer and journalist.  Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.