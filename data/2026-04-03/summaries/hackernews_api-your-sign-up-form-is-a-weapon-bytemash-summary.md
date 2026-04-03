---
title: Your sign-up form is a weapon | Bytemash
url: https://bytemash.net/posts/subscription-bombing-your-signup-form-is-a-weapon/
date: 2026-04-02
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-03T01:03:27.765013
---

# Your sign-up form is a weapon | Bytemash

# Your sign-up form is a weapon

## What is subscription bombing
- Attack where bots sign up a victim’s email on many sites, flooding the inbox with unwanted messages.  
- Goal is to hide real security alerts (password resets, financial confirmations) among the noise.  
- Any sign‑up form that accepts an unverified email can be abused.

## How we spotted it
- Early March we noticed a small but unusual rise in completely inactive accounts with random‑looking names.  
- Email logs showed welcome messages being sent to real victim addresses.  
- By March 14 the pattern grew and we saw a spike in page views on the “forgot password” page, prompting deeper investigation.

## The pattern
- Bot creates an account with a real email and a garbage name, then within ~60 seconds requests a password reset.  
- Victim receives three emails in under a minute: verification, welcome, and password‑reset.  
- Bots also probe the forgot‑password endpoint with random emails to trigger additional resets.  
- Typing behavior showed uniformly random delays between keystrokes, mimicking a human but failing to reproduce natural typing bursts.

## Designed to be invisible
- No large traffic spikes; only 1–2 sign‑ups per hour, staying below typical rate‑limit thresholds.  
- Requests originated from many countries with no correlation to local time zones, unlike normal user traffic.  
- Rate limiting is ineffective because the attack purposefully stays under detection limits.

## The damage isn’t to the site owner
- Minimal impact on our email reputation or server load.  
- Victims are overwhelmed by hundreds of unsolicited emails, risking missed critical alerts (bank password changes, credit‑card applications).  
- Because the harm falls on the email owner, many site operators treat the issue as low priority, though it pollutes user data and makes the service an accomplice in harassment.

## What we did
### Firewall rules
- Tightened bot detection on the front‑end hosting provider’s firewall, cutting volume by roughly half.  
- Some bots still bypassed verification, showing the need for stronger measures.

### Cloudflare Turnstile
- Implemented Turnstile, an invisible CAPTCHA that analyses browser signals and only challenges suspicious traffic.  
- Integrated via Better Auth’s built‑in Turnstile plugin, adding the component to sign‑up, sign‑in, and forgot‑password pages.  
- After deployment, bot sign‑ups stopped completely.

### Limiting email to verified users only
- Modified email logic so only the verification email is sent until the user clicks the verification link.  
- Welcome and other product emails are withheld until the address is confirmed.  
- This reduces the number of unsolicited messages a victim receives even if a bot creates an account.