---
title: Never Buy A .online Domain | Sid's Blog
url: https://www.0xsid.com/blog/online-tld-is-pain
site_name: hackernews_api
content_file: hackernews_api-never-buy-a-online-domain-sids-blog
fetched_at: '2026-02-26T06:00:15.896724'
original_url: https://www.0xsid.com/blog/online-tld-is-pain
author: ssiddharth
date: '2026-02-26'
description: Never buy a .online domain
tags:
- hackernews
- trending
---

I’ve been a .com purist for over two decades of building. Once, I broke that rule and bought a .online TLD for a small project. This is the story of how it went up in flames.

Update:Within 40 minutes ofposting thison HN, the site has been removed from Google's Safe Search blacklist. Thank you, unknown Google hero! I've emailed Radix to remove the darnserverHold.

Update 2:The site is finally back online. Not linking here as I don't want this to look like a marketing stunt. Link at the bottom if you're curious. [4]

Post, for posterity, below.

## Namecheap's Alluring Offer

Earlier this year, Namecheap was running a promo that let you choose one free .online or .site per account. I was working on a small product and thought, "hey, why not?" The app was a small browser, and the .online TLD just made sense in my head.

After a tiny $0.20 to cover ICANN fees, and hooking it up to Cloudflare and GitHub, I was up and running. Or so I thought.

## The Disappearing Act

Poking around traffic data for an unrelated domain many weeks after the purchase, I noticed there were zero visitors to the site in the last 48 hours. Loading it up led to the dreaded, all red, full page "This is an unsafe site" notice on both Firefox and Chrome. The site had a link to the App Store, some screenshots (no gore or violence or anything of that sort), and a few lines of text about the app, nothing else that could possibly cause this. [1]

Clicking through the disclaimers to load the actual site to check if it had been defaced, I was greeted with a "site not found" error. Uh oh.

## Initial Recon

After checking that Cloudflare was still activated and the CF Worker was pointing to the domain, I went to the registrar first. Namecheap is not the picture of reliability, so it seemed like a good place to start. The domain showed up fine on my account with the right expiration date. The nameservers were correct and pointed to CF.

Perplexed, I ran a quickdig NS getwisp.online +short. Empty.

Maybe I had gotten it wrong, so I checked the WHOIS information online. Status:serverHold. Oh no...

## Stuck in No-Man’s-Land

At this point, I double checked to make sure I hadn't received emails from the registry, registrar, host, or Google. Nada, nothing, zilch.

I emailed Namecheap to double check what was going on (even though it's aserverHold[2], not aclientHold[3]). They responded in a few minutes with:

Cursing under my breath, as it confirms my worst fears, I promptly submitted a request to the abuse team atRadix, the registry in our case, who responded with:

## The Verification Catch-22

Right, let's get ourselves off the damned Safe Browsing blacklist, eh? How hard could it be?

Very much so, I've now come to learn. You need to verify the domain in Google Search Console to then ask for a review and get the flag removed. But how do you get verified? Add a DNS TXT or a CNAME record. How will it work if the domain will not resolve? It won't.

As the situation stands, the registry won't reactivate the domain unless Google removes the flag, and Google won't remove the flag unless I verify that I own the domain, which I physically can't.

I've tried reporting the false positivehere,hereandhere, just in case it moves the needle.

I've also submitted a review request to the Safe Search team (totally different from Safe Browsing) in the hopes that it might trigger a re-review elsewhere. Instead I just get aNo valid pages were submittedmessage from Google because nothing resolves on the domain.

As a last resort, I submitted a temporary release request to the registry so Google can review the site’s contents and, hopefully, remove the flag.

## A Series of Unfortunate Events

I've made a few mistakes here that I definitely won't be making again.

* Buying a weird TLD. .com is the gold standard. I'm never buying anything else again. Once bitten and all that.
* Not adding the domain to Google Search Console immediately. I don't need their analytics and wasn't really planning on having any content on the domain, so I thought, why bother? Big, big mistake.
* Not adding any uptime observability. This was just a landing page, and I wanted as few moving parts as possible.

Both Radix, the registry, and Google deserve special mention for their hair-trigger bans and painful removal processes, with no notifications or grace time to fix the issue. I'm not sure whether it's the weird TLD that's causing a potentially short fuse or whether I was brigaded earlier with reports. I'll never know.

Oh well, c'est la vie. Goodbye, $0.2.

## Notes

[1] A mirror can be foundhereto verify the site contents.

[2]serverHoldis set by the registry and is a royal pain to deal with. Usually means things are FUBAR.

[3]clientHoldis set by the registrar and ismostlypayment or billing related.

[4]getwisp.online
