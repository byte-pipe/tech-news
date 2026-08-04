---
title: Web Security is Too Hard – text/plain
url: https://textslashplain.com/2026/08/04/security-is-hard-yall/
site_name: hnrss
content_file: hnrss-web-security-is-too-hard-textplain
fetched_at: '2026-08-05T06:00:56.841005'
original_url: https://textslashplain.com/2026/08/04/security-is-hard-yall/
date: '2026-08-04'
published_date: '2026-08-04T18:22:56+00:00'
description: 'It started innocently enough. I saw a tweet about a new product offering from one of my favorite companies, Cloudflare. Neat! I clicked through to the site and there it is: And huzzah!, my preferred handle, @ericlaw is still available. I''d better hurry to claim it before someone else gets it! Since I''m already a…'
tags:
- hackernews
- hnrss
---

It started innocently enough. I saw a tweet about a new product offering from one of my favorite companies, Cloudflare.

Neat! I clicked through to the site and there it is:

Andhuzzah!,my preferred handle,@ericlawis still available.I’d better hurryto claim it before someone else gets it!

Since I’m already a long-time Cloudflare user, I just need to sign in. That makes sense, how else will they bind the handle to my account?

Easy peasy. I’m in. Looks like there’s just one more step, I gotta authorize the new feature?

But wait a sec!

This looksexactlylike one of thoseConsent Phishing attacksthat have been so popular over the last few years!

And wait, why is the entry point oncloudflare.pay, a site thatdoesn’talready have my credentials, rather than something within thecloudflare.comdomain which does (e.g.cloudflare.com/pay)?There is no inherent technical relationship between a .com domain and a .pay domain. Domain names under the.paysTLD are available toanyone with $20(unlike, e.g..bankwhich requires more vetting), so there’s nothing that would stop me from registering my owncloudflarepayments.paydomain name in just a few minutes.And why doesn’t Cloudflare’s permission site recognize its own company’s feature? And that green checkmark looks suspicious as heck– an attacker could probably just shove that emoji inside their misleading display name, the same way that folks trying tophish Microsoft email accountsuse misleading app names and icons:

Fake Outlook OAuth phishing request

The guys at Cloudflare are geniuses who know their stuff. This hasgotto be an attack.It’s a clever one — I was feeling such asense of urgencybecause I wanted to “win” the race to get my desired handle.Very very clever!

Unfortunately, the Cloudflare permission page doesn’t followbest practices, so there’s no “Report suspicious request” link I can use to let the Cloudflare folks know that their customers are under attack.

Let me go back to my Cloudflare dashboard and try to get to the Wallet feature from its sidebar. Hrm.It’s not there.Now, Wallet purports to be “a new feature”, so maybe the Dashboard just isn’t updated yet. A search of the docs turns up nothing. Let’s ask the AI agent in chat.

The very first thing the chat agent wants is access to my account:

This feels a little weird, but the page is stillcloudflare.comso I guess I can give the thing access to things it already has access to. Weirdly, the AI agent first proposes that I grant itfull controlrather thanread onlyaccess, which feels like a failure of the principle of least privilege, but I don’t actually need to ask an account specific question anyway. After granting read permission, the agent allows me to ask my question:

Oh, wow.Cloudflare says it reallyisan attack!Let’sreport the phish right away!

A few minutes later… womp womp…

Oh dear.

After a few minutes of further frantic searching, it turns out that this is, in fact, a legitimate new Cloudflare product and a legitimate site, despite giving every indication of being a clever phishing attack.

It furtherturns outthat that suspicious green checkmark is not part of the app’s untrustworthy display name but instead a (poorly placed) security UI element that a user is expected to hover over to get the security details:

The Cloudflare folks apparently want security issuesreported via HackerOne(which wouldn’t let me log in because the Cloudflare CAPTCHA HackerOne uses seems to bebroken…).

When legitimate websites sometimes act very very phishy, consider how hard it must be for URL Reputation services likeMicrosoft SmartScreenand Google SafeBrowsing to block malicious sites without false positives as millions of new sites are added to the web every week.

## Lessons

Web Developers, please follow every best practice,I’mbeggingyou:

* Host apps and content under your trusted domain name (e.g.cloudflare.com/payorpay.cloudflare.com.If you must add a new name, link to it directly from a page on your trusted domain name.
* Show relevant security information in atrustworthy placewhen asking the user to make security decisions.
* Make ittrivial to report scams, in context (e.g. on the permission request page).
* Test your security reporting flows to ensure they are monitored and function correctly.

Users: Try to stay safe out there. Think before you click, and if all else fails,wait.

Security Geeks:Never blame the victim– they’ve got an impossible job.

-Eric

### Share this:

* Share on X (Opens in new window)X
* Share on Facebook (Opens in new window)Facebook

### Like this:

Like
 
Loading…
 

## Published by ericlaw

Impatient optimist. Dad. Author/speaker. Created Fiddler & SlickRun. PM @ Microsoft 2001-2012, and 2018-, working on Office, IE, and Edge. Now working on Microsoft Defender. My words are my own, I do not speak for any other entity.View more posts