---
title: Did You Know TLDs Can Be Websites? - DEV Community
url: https://dev.to/aws/did-you-know-tlds-can-be-websites-2j13
site_name: devto
content_file: devto-did-you-know-tlds-can-be-websites-dev-community
fetched_at: '2026-07-18T11:24:50.054151'
original_url: https://dev.to/aws/did-you-know-tlds-can-be-websites-2j13
author: Sean Boult
date: '2026-07-16'
description: You've probably registered a domain with Route53 or another popular registrar. You pick something... Tagged with aws, infrastructure, networking, webdev.
tags: '#aws, #infrastructure, #networking, #webdev'
---

Features rare dotless domains like .uz

You've probably registered a domain withRoute53or another popular registrar.

You pick something likeseanboult.dev, spin up aweb server, configure your A record, attach a TLS cert, and boom it'slive.

Well in the past, before the AI boom, there once was a web server on.aiand it made its way toHacker News.

This was a cool relic that always intrigued me. Here is a snapshot from theWayback Machine.

Now you're like wait, I can't go tohttp://aitoday? No, sadly at some point the A record was removed and the web server was shut down.

Don't worry though, at the time of writing this I found another one.

Without further ado, here it is!https://uz.

Seems the TLS cert does not match the common name so you'll have to force your way in...

But then you're in!

So how does this work?

Well, the same way you can add an A record to the apex of your domain (such as example.com), a registry operator can add DNS records directly to the apex of a Top-Level Domain zone, such as.uzin this case.

Would love to know if you find more like this, leave a reply if you do.

If we ever did one on.awswhat would you like to see there 🤔?

As always, happy coding 😉!

Follow AWS for more articles like this.

## AWSFollow

 Articles written by current and past AWS Developer Advocates to help people interested in building on AWS. Opinions are each author's own.
 

Follow me for all things tech

## Sean BoultFollow

Developer. Hacker. Creator.

.

 

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse