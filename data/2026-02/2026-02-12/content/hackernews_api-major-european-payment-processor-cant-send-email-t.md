---
title: Major European Payment Processor Can't Send Email to Google Workspace Users | The Ian Atha Museum of Internet Curiosities
url: https://atha.io/blog/2026-02-12-viva
site_name: hackernews_api
content_file: hackernews_api-major-european-payment-processor-cant-send-email-t
fetched_at: '2026-02-12T19:27:46.259866'
original_url: https://atha.io/blog/2026-02-12-viva
author: thatha7777
date: '2026-02-12'
published_date: '2026-02-12T00:00:00.000Z'
description: 'Viva.com, one of Europe''s largest payment processors, sends verification emails without a Message-ID header — a recommendation of RFC 5322 since 2008. Google Workspace rejects them outright. Their support team''s response to my detailed bug report: your account has a verified email, so there''s no problem.'
tags:
- hackernews
- trending
---

Authors
* NameIan AthaTwitter@IanAtha

TL;DR:Viva.com, one of Europe's largest payment processors, sends verification emails without a Message-ID header — a recommendation of RFC 5322 since 2008. Google Workspace rejects them outright. Their support team's response to my detailed bug report: "your account has a verified email, so there's no problem."

A few days ago, I tried to create an account onviva.com, one of Europe's largest payment processors. It should have taken five minutes. Instead, it turned into a small investigation — and left me with some bigger questions about the state of European fintech infrastructure.

## The verification email that never arrived

The signup flow is standard: enter your email, receive a verification link, click it, move on with your life. Except the verification email never showed up. Not in my inbox, not in spam, not anywhere. I waited. I retried. I waited some more.

My email is hosted on Google Workspace — a corporate email on a custom domain. Not exactly an exotic setup. After a couple of days of retrying, I decided to dig into Google Workspace's Email Log Search to see what was happening on the receiving end.

Here's what I found:

Status: Bounced.

The bounce reason:

550

5.7
.1

[
209.85
.220
.69
]

Messages
 missing a valid
Message
-
ID
 header are not

550
-
5.7
.1
 accepted
.

For
 more information
,
 go to

550
-
5.7
.1

https
:
/
/
support
.
google
.
com
/
mail
/
?
p
=
RfcMessageNonCompliant
 and review

550

5.7
.1

RFC

5322
 specifications
.

Viva.com's outgoing verification emails lack aMessage-IDheader, a requirement that has been part of the Internet Message Format specification (RFC 5322) since 2008, and was already suggested by its predecessor RFC 2822 back in 2001.

Google's mail servers reject the message outright. It doesn't even get a chance to land in spam.

## The workaround

To unblock myself, I switched to a personal@gmail.comaddress for the account. Gmail's own receiving infrastructure is apparently more lenient with messages, or perhaps routes them differently. The verification email came through.

But the fact that I had to abandon my preferred business email to sign up for abusiness payments platformis... not great.

## The support experience

Of course, I reported the issue to viva.com's customer support, including the screenshot from Google Workspace's email logs and a clear explanation of theMessage-IDheader problem — enough detail for any engineer to immediately reproduce and fix it.

They responded within a few hours. Their answer:

"We can see your account now has a verified email address, so there doesn't appear to be an issue."

That was it. No acknowledgment of the technical problem. No escalation to engineering. Just a confirmation thatIhad worked aroundtheirbug, repackaged as evidence that nothing was wrong.

## Why this matters

This isn't a cosmetic bug.Message-IDis one of the most basic headers in email. Every email library, every framework, every transactional email service generates it by default. You have to go out of your way tonotinclude it — or be running a seriously misconfigured mail pipeline.

(A note, in fairness: RFC 5322 uses "SHOULD" rather than "MUST" for the Message-ID header, meaning it's strongly recommended but not strictly required. So technically, viva.com's emails are non-compliant with a recommendation, not a mandate. Meanwhile, Google treats it as a hard requirement. Who's in the right? I genuinely don't know. What I do know is that I'm caught in the middle, and my verification email is in neither inbox.)

For a company that processes payments across Europe, this raises a question: if they can't get email headers right, what does the rest of the stack look like?

I'm not asking rhetorically. As someone building a business in Greece, Ineeda reliable payments processor. Viva.com is one of the few that natively supports the the Greek instant-payment system. Stripe, which I'd use in a heartbeat, doesn't support it yet. So here I am, forced to depend on infrastructure that can't pass basic RFC compliance checks.

## The broader pattern

This experience fits a pattern I keep running into with European business-facing APIs and services. Something is always a little bit broken. Documentation is incomplete, or packaged as a nasty PDF, edge cases are unhandled, error messages are misleading, and when you report issues, the support team doesn't have the technical depth to understand what you're telling them.

I don't think this is because European engineers are less capable. I think it's a prioritization problem. When you're the only option in a market (or one of very few), there's less competitive pressure to polish the developer experience. Stripe raised the bar globally, but in markets it doesn't fully serve, the bar remains remarkably low.

I miss Stripe. I miss the feeling of integrating with an API that someone clearlycaredabout. Until Stripe or a Stripe-caliber alternative covers the full European payments landscape, including local payment rails like IRIS, stories like this one will keep happening.

## The fix

For viva.com's engineering team, in case this reaches you: add aMessage-IDheader to your outgoing transactional emails. It should look something like:

Message
-
ID
:

<
unique
-
id@viva
.
com
>

Most email libraries generate this automatically. If yours doesn't, it's a one-line fix. Your Google Workspace users (and I suspect there is a number of us) will thank you.

## Google Workspace's Email Log Search

Discuss on Twitter
