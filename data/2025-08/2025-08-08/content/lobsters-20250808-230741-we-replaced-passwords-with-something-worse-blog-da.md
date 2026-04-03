---
title: We replaced passwords with something worse | Blog - Daniel Huang
url: https://blog.danielh.cc/blog/passwords
site_name: lobsters
fetched_at: '2025-08-08T23:07:41.911722'
original_url: https://blog.danielh.cc/blog/passwords
date: '2025-08-08'
description: where my words occasionally escape /dev/null
tags: practices, security
---

# We replaced passwords with something worse​

Too many services have been using the following login method:

* Enter an email address or phone number
* The website will send a 6-digit code
* Use the 6-digit code to log in

Please stop.

This is terrible for account security:

* An attacker can simply send your email address to a legitimate service, and prompt for a 6-digit code. You can't know for sure if the code is supposed to be entered in the right place. Password managers (a usual defense against phishing) can't help you either.
* In fact, this attack method has been successfully used in the wild: Microsoft's login for Minecraft accounts use this login method, andmanyaccountshavebeenstolenalready.
