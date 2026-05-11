---
title: A million baby monitors and security cameras were easily viewable by hackers | The Verge
url: https://www.theverge.com/tech/926487/meari-technology-hack-baby-monitor-security-camera
site_name: newsfeed
content_file: newsfeed-a-million-baby-monitors-and-security-cameras-were
fetched_at: '2026-05-11T19:47:33.392709'
original_url: https://www.theverge.com/tech/926487/meari-technology-hack-baby-monitor-security-camera
author: Sean Hollister
date: '2026-05-11'
published_date: '2026-05-11T16:00:00+00:00'
description: Sammy Azdoufal tells The Verge he found 1.1 million remotely accessible Meari cameras. Meari supplies many brands including Arenti, Anran, Boifun, ieGeek and Wyze.
tags:
- the-verge
- news
- report
- security
---

* Tech
* News
* Report

# A million baby monitors and security cameras were easily viewable by hackers

Meari Technology: the Wi-Fi camera maker you’ve probably never heard of.

by
 
 
Sean Hollister
May 11, 2026, 4:00 PM UTC
* Link
* Share
* Gift
If your baby monitor looks something like this, it’s probably a Meari.
 
| Image: Meari
Sean Hollister
 
is a senior editor and founding member of The Verge who covers gadgets, games, and toys. He spent 15 years editing the likes of CNET, Gizmodo, and Engadget.

A baby’s eyes peer directly into the camera lens. A kid with a striped shirt looks up, then away. A boy in a policeman’s costume, a gold star on his chest. A messy bedroom that reminds me of my own daughters, with an unmade bunk bed, a little girl’s hat and headband, and Hello Kitty plastered on the wall.

One thought repeats in my mind:I shouldn’t be seeing this.No stranger should.

But bad actors could’ve easily spied on all these locations — and a million more — because many of Meari Technology’s Wi-Fi baby monitors and security cameras were absurdly insecure. If you had access to one of those cameras, you theoretically had access to them all.

### Related

* A hacker ran me over with a robot lawn mower
* The DJI Romo robovac had security so poor, this man remotely accessed thousands of them

Meari is a Chinese white-label brand whose cameras ship under hundreds of different names. Many are generic-sounding Amazon sellers like Arenti, Anran, Boifun, and ieGeek. But financial records show one of the company’s biggest customersis Wyze; its biggest customer is Zhiyun; and many hackable cameras were from Intelbras. At least one of Petcube’s pet-monitoring cameras appears to be a Meari product as well.

Sammy Azdoufal — the man from France who createda remote-controlled army of DJI Romo robot vacuum cleanerswithout really trying — tellsThe Vergehe found 1.1 million remotely accessible Meari cameras almost the same way. Just by inspecting the Android app, Azdoufal says he was able to extract a single key that gave him access to devices across 118 countries.

Every one of those million devices was broadcasting its information to anyone who knew how to listen. Or anyone who knew how to guess the company’s passwords, many of which were still set to default. One of those passwords was the word “admin.” Another was the word “public.”

When Azdoufal hooked up the MQTT datastream to a vibe-coded map of the world, he says he could see “everything.” He could see into people’s homes. He could see their email addresses and rough locations.

Just a small peek at Azdoufal’s dashboard of Meari cameras.
 
Image: Sammy Azdoufal

He could also see tens of thousands of photos from these cameras, stored on Chinese Alibaba servers at public web addresses without any protection, including the photos I describe at the beginning of this story.

“I can retrieve the picture without any passwords, no cracking, no hacking,” says Azdoufal. “I just click on the URL and this image is showing.”

Azdoufal says he even found an unprotectedinternalserver with Meari’s passwords and credentials exposed in plain sight, as well as a list of all 678 employees with their emails and phone numbers. “I talk to the boss, I have his number, I send a WeChat,” Azdoufal laughs.

He says that’s when Meari finally began answering his emails. Even though reports of vulnerabilities in Meari’s CloudEdge platformdate back years, and alate 2025 vulnerability reportpredicted the damage Meari’s MQTT design could cause, he says the company didn’t take him seriously until its own employees were proven vulnerable.

On March 10th, Meari cut off Azdoufal’s access — and closed the primary hole. By the time I’d purchased three Meari vendors’ cameras in the hopes of getting a live demo of the hack, I was (thankfully!) too late to see it working myself. But even though there’s no GIF of megetting run over by a robot lawn mower, I didn’t have to take Azdoufal’s word that the potential damage was real.

“Under specific technical conditions, attackers may interceptall messages transmitted via the EMQX IoT platformwithout user authorization,” an unnamed spokesperson from the “Meari Technology Security Team” admitted toThe Verge, when we reached out by email. (The company failed to provide a named spokesperson perour background policy, but we’re running the statement because it’s a clear admission of the core vulnerability.)

The company also says it discovered “Risk of potentialRemote Code Execution (RCE)due to weak password issues on the scheduled task platform.” (In both statements, the bolding is theirs.)

Meari’s public claim of “advanced encryption technology” and “strict access controls” seems laughable now.
 
Image: Meari

To fix the problems, Meari’s unnamed spokesperson says it shut down its EMQX platform entirely, changed usernames and passwords, and told its customers to upgrade devices to the latest firmware (it claims only versions below 3.0.0 are affected).

But Meari would not tell us:

* How many cameras or brands were actually vulnerable;
* Whether those brands have adequately warned their customers;
* Whether these vulnerabilities have already been abused;
* What — if anything — prevents an employee of Meari or any of its vendors from spying on people from the other side of the world.

Azdoufal says that the way Meari originally designed its system, any brand could access any other brand’s cameras, since they all shared the same servers and passwords.

While shutting down the EMQX platformdidblock remote access, Azdoufal confirms, it’s not clear what happens to those million cameras now. Meari has not told us how many of those devices can actually get a new firmware update, or whether Meari’s partners have actually passed along so much as a warning to people who have these cameras in their homes.

Alien, cat, dog, or plain, Meari’s baby monitors come in many different shapes. 
 
Image: FCC

We attempted to reach out to some Meari camera partners to see if they were even aware of the issue. Wyze and Petcam did not reply. Neither did EMQX.

Intelbras tellsThe Verge, via third-party spokesperson Kennya Gava, that the company only ever worked with Meari on three Wi-Fi video doorbells and that “fewer than 50” units had “a potential vulnerability.” That small number doesn’t line up with Azdoufal’s story. Intelbras appeared to be one of themorepopular brands in his dataset, with a high concentration of cameras in Brazil. Gava would not say whether Meari had been in touch about the vulnerabilities, or whether Intelbras would pass a warning along to its own customers.

When we reached out to Congress’s Select Committee on the Chinese Communist Party about Meari, Congressman Ro Khanna (D-CA)’s office replied that the reports were concerning: “I will be looking into this as ranking member of the Select Committee on China,” Khanna pledged.

Azdoufal shows me that yes, Meari did pay the bug bounty.

The good news is that Azdoufal says most of what he discovered seems to be fixed, and on May 7th, he received a €24,000 bug bounty for his help. But the experience seems to have left a bad taste in his mouth.

In March, after he first shared his research with Meari, the company sent him what he interpreted as a veiled threat. The company told him that it was “fully capable of protecting our interests,” that the company knew where he lived, and that his discovery of Meari’s internal servers was “unlawful.”

He’s also not happy that Meari initially tried to backdateitssecuritybulletinsto March 2nd. That way, it would have looked like Meari discovered the vulnerabilities before he ever reached out. Even today, the bulletins are dated March 12th, almost a month before Meari published them in April. He also notes that Meari has yet to fulfill its GDPR obligations to notify EU citizens about the breach.

I wish I could say I’ve described every facepalm-worthy thing Azdoufal discovered about Meari’s practices, but you can find more inhis full security writeup. He also teamed upwith Tod Beardsley of runZeroto file fiveofficial CVEvulnerabilityreportsthis time.

While researching this story, I found that a large number of baby monitors on Amazon now advertise “No Wi-Fi.” That does not automatically mean they’re secure — but at least their short-range FHSS or DECT transmission should be tough to spy on from the other side of the globe.

Follow topics and authors
 from this story to see more like this in your personalized homepage feed and to receive email updates.
* Sean Hollister
* News
* Report
* Security
* Tech

## Most Popular

Most Popular
1. Logitech’s tiny folding mouse improves upon the laptop trackpad
2. Forza Horizon 6 has been leaked and cracked a week before its release
3. Writers are fleeing the Substack Tax
4. Samsung’s flagship laptop is a MacBook Pro clone gone horribly wrong
5. Vivo’s X300 Ultra has the best cameras in any phone

## The Verge Daily

A free daily digest of the news that matters most.

Email (required)
Sign Up
By submitting your email, you agree to our
 
Terms
 and 
Privacy Notice
. 
This site is protected by reCAPTCHA and the Google
 
Privacy Policy
 
and
 
Terms of Service
 
apply.
Advertiser Content From

This is the title for the native ad

## More inTech

Google stopped a zero-day hack that it says was developed with AI
Live updates from Musk v. Altman
GM settles California lawsuit claiming it sold driving habit data to insurance companies
Matter and OpenADR team up to connect smart homes to the grid
Play
Joanna Stern is not a robot, but she lived with them
TikTok is letting UK users pay to remove ads
Google stopped a zero-day hack that it says was developed with AI
Stevie Bonifield
4:09 PM UTC
Live updates from Musk v. Altman
Elizabeth Lopatto
 and 
Hayden Field
41 minutes ago
GM settles California lawsuit claiming it sold driving habit data to insurance companies
Emma Roth
3:11 PM UTC
Matter and OpenADR team up to connect smart homes to the grid
Jennifer Pattison Tuohy
2:40 PM UTC
Play
Joanna Stern is not a robot, but she lived with them
Nilay Patel
2:00 PM UTC
TikTok is letting UK users pay to remove ads
Jess Weatherbed
1:02 PM UTC
Advertiser Content From

This is the title for the native ad

## Top Stories

An hour ago
Who is the Palantir chore coat for?
2:00 PM UTC
Joanna Stern is not a robot, but she lived with them
﻿
Video
Two hours ago
Texas sues Netflix for advertising ‘bait and switch’ and spying
41 minutes ago
Live updates from Musk v. Altman
12:00 PM UTC
Venmo finally takes privacy seriously
Two hours ago
Apple brings encrypted RCS chats to iPhone