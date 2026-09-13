---
title: Why is Google still serving dodgy ads? | atomic14
url: https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads
site_name: hackernews_api
content_file: hackernews_api-why-is-google-still-serving-dodgy-ads-atomic14
fetched_at: '2026-09-13T21:17:53.774411'
original_url: https://www.atomic14.com/2026/09/13/why-is-google-still-serving-dodgy-ads
author: iamflimflam1
date: '2026-09-13'
published_date: '2026-09-13T00:00:00+00:00'
description: I accidentally clicked a shady YouTube ad that mimics an iOS “Storage Full” alert, reported it (twice), and Google still said it was fine. Meanwhile, Gemini flags it in seconds for deceptive design...
tags:
- hackernews
- trending
---

# Why is Google still serving dodgy ads?

View All Posts

 read
 

Want to keep up to date with the latest posts and videos? 
Subscribe to the newsletter

   ·  
 
 
 
 

   ·  
 
 
 
 

   ·  
 
 
 
 

   ·  
 
 
 
 

   ·  
 
 
 
Posts
  ·  
 
Videos
  ·  
 
ESP32
  ·  
 
Tools
  ·  
 
Support

« Detecting Claude and ChatGPT using letter counting.

 HELP 
SUPPORT
 MY WORK: If you're feeling flush then please stop by 
Patreon
 Or you can make a one off donation via 
ko-fi

TLDR:

AI is really good at detecting deceptive adverts - why isn’t Google using it?

A couple of months ago I noticed this advert popping up in the YouTube app. The main reason I noticed it is that I accidentally clicked it - I knew I was running out of space on my iPhone and a minor lapse of concentration caught me out.

These things can slip through even the best review processes, so I did my internet duty and reported the advert.

The response I got back was less than satisfactory:

Again, sometimes things slip through the net and people don’t always check things properly, so I reported it again. And got the same response.

In fact, multiple people have reported this advert and received the same:

We found that the ad doesn’t go against Google’s policies, which prohibit certain content and practices that we believe to be harmful to users and the overall online ecosystem.

I’m a big fan ofHanlon’s razor.

Never attribute to malice that which is adequately explained by stupidity

However, if you were being uncharitable, you do have to question whether it’s in Google’s interest to remove adverts that get lots of clicks. After all, these adverts are probably performing well and bringing in lots of lovely 🤑.

A simpler explanation is that the people reviewing adverts cannot properly review everything so things get missed.

You can’t help thinking that AI should come to the rescue here. Given Google has some pretty good models - surely it can put them to use?

Here’s what Google’s Gemini has to say about the advert:

### Classification: DISAPPROVED

Policy Violations:

1. Misrepresentation: Misleading Ad Design
2. Misrepresentation: Unreliable / Deceptive Claims

### Detailed Reasons for Disapproval

#### 1. Mimicking System Alerts / UI Elements (Misleading Ad Design)

* The Violation:Google Ads policy strictly prohibits advertisements that imitate operating system dialogs, system warnings, error messages, or interactive system notifications.
* The Evidence:The banner embedded inside the ad explicitly mimics aniOS system alert modal(“iPhone Storage is Full”) complete with standard iOS typography, container styling, and mock system buttons (“Yes” / “No”). This trick visually deceives users into believing their device is throwing a native system-level alert, coercing them to click.

#### 2. Non-Functional / Deceptive UI Components

* The Violation:Ads cannot feature non-functional or misleading interactive elements, such as fake dialog options, false close buttons, or radio choices that do not perform their implied system function.
* The Evidence:The “Yes” and “No” options inside the graphic image are static visuals designed to capture clicks anywhere on the ad banner to trigger a store/landing page redirect, rather than acting as true system controls.

#### 3. Deceptive Fear-Based Tactics & Unverified Claims

* The Violation:Advertising policies forbid using deceptive claims or scare tactics to induce panic and force immediate user action.
* The Evidence:Stating“If you don’t free up space soon, some features may not work properly”inside a fake system popup fabricates a urgent state of failure on the user’s personal device, misleading them about their hardware status to drive app installs.

### Required Action

Disapprove the ad creative immediately. Issue a policy violation warning/disapproval flag to the advertiser account underMisrepresentation (Misleading Ad Design). Repeated violations of this nature may result in full account suspension for deceptive practices.

Google’s own model rejects the ad in seconds, yet Google’s review process approved it twice.

Come on, meatbags - use some of the amazing AI tools you have access to.

 HELP 
SUPPORT
 MY WORK: If you're feeling flush then please stop by 
Patreon
 Or you can make a one off donation via 
ko-fi

Want to keep up to date with the latest posts and videos? 
Subscribe to the newsletter

   ·  
 
 
 
 

   ·  
 
 
 
 

   ·  
 
 
 
 

   ·  
 
 
 
 

   ·  
 
 
 
Posts
  ·  
 
Videos
  ·  
 
ESP32
  ·  
 
Tools
  ·  
 
Support

« Detecting Claude and ChatGPT using letter counting.

##### Written by

Blog Logo

#### Chris Greening

Published13 Sep 2026

##### Supported by