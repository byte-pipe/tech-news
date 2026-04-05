---
title: Someone at BrowserStack is Leaking Users’ Email Address – Terence Eden’s Blog
url: https://shkspr.mobi/blog/2026/04/someone-at-browserstack-is-leaking-users-email-address/
site_name: hackernews_api
content_file: hackernews_api-someone-at-browserstack-is-leaking-users-email-add
fetched_at: '2026-04-06T01:01:24.343577'
original_url: https://shkspr.mobi/blog/2026/04/someone-at-browserstack-is-leaking-users-email-address/
author: Terence Eden
date: '2026-04-05'
published_date: '2026-04-05T12:34:03+01:00'
description: Like all good nerds, I generate a unique email address for every service I sign up to. This has several advantages - it allows me to see if a message is legitimately from a service, if a service is hacked the hackers can't go credential stuffing, and I instantly know who leaked my address. A few weeks ago I signed up for BrowserStack as I wanted to join their Open Source programme. I had a few…
tags:
- hackernews
- trending
---

Like all good nerds, I generate a unique email address for every service I sign up to. This has several advantages - it allows me to see if a message is legitimately from a service, if a service is hacked the hackers can't go credential stuffing, and I instantly know who leaked my address.

A few weeks ago I signed up forBrowserStackas I wanted to join their Open Source programme. I had a few emails back-and-forth with their support team and finally got set up.

A couple of days later I received an email to that email address from someone other than BrowserStack. After a brief discussion, the emailer told me they got my details from Apollo.io.

Naturally, I reached out to Apollo to ask them where they got my details from.

They replied:

Your email address was derived using our proprietary algorithm that leverages publicly accessible information combined with typical corporate email structures (e.g., firstname.lastname@companydomain.com).

Wow! Aproprietaryalgorithm, eh? I wonder how much AI it takes to work out "firstname.lastname"????

Obviously, their response was inaccurate. There's no way their magical if-else statement could have derived the specific email I'd used with BrowserStack. I called them out on their bullshit and they replied with:

Your email address came from BrowserStack (browserstack.com) one of our customers who participates in our customer contributor network by sharing their business contacts with the Apollo platform.

The date of collection is 2026-02-25.

So I emailed BrowserStack a simple "Hey guys, what the fuck?"

I love their cheery little "No spam, we promise!"

Despite multiple attempts to contact them, BrowserStack never replied.

Given that this email address was only used with one company, I think there are a few likely possibilities for how Apollo got it.

* BrowserStack routinely sell or give away their users' data.
* A third-party service used by BrowserStack siphons off information to send to others.
* An employee or contractor at BrowserStack is exfiltrating user data and transferring it elsewhere.

There are other, more nefarious, explanations - but I consider that to be unlikely. I suspect it is just the normalisation of the shabby trade in personal information undertaken by entities with no respect for privacy.

But, it turns out, it gets worse. My next blog post reveals how Apollo got my phone number from from averybig company.

Be seeing you 👌

## Share this post on…

## 3 thoughts on “Someone at BrowserStack is Leaking Users' Email Address”

1. ### John William David Thomson@blogI'm assuming BrowserStack uses some sort of CRM type thing that does this, either in a "you give us your contacts in exchange for $/access to other customers' contacts" or just on the sly at the CRM provider's benefit.Reply|Reply to original comment on mastodon.social2026-04-05 12:57
2. ### Fazal MajidOutsourced email marketing providers are a frequent source of breaches. Once I had at least four vendor-specific addresses compromised, and with one of the vendors, figured out who was the guilty party. Of course, the legal obligation to notify users of a breach is largely ignored, even by giant corporations that should know better, in the absence of legal redress for consumers in regulations like GDPR.Reply2026-04-05 13:36
3. ### news.ycombinator.comSomeone at BrowserStack Is Leaking Users' Email Address | Hacker NewsReply|Reply to original comment on2026-04-05 13:50
4. ### More comments on Mastodon.

### What are your reckons?Cancel reply

All comments are moderated and may not be published immediately. Your email address willnotbe published.

Comment:

See allowed HTML elements:

<a href="" title="">
								
<abbr title="">
								
<acronym title="">
								
<b>
								
<blockquote cite="">
								
<br>
								
<cite>
								
<code>
								
<del datetime="">
								
<em>
								
<i>
								
<img src="" alt="" title="" srcset="">
								
<p>
								
<pre>
								
<q cite="">
								
<s>
								
<strike>
								
<strong> 
							

Your Name (required):

Your Email (required):

Your Website (optional):

 

To respond on your own website, write a post which contains a link to this post - then enter the URl of your page here.Learn more about WebMentions.

URL/Permalink of your article