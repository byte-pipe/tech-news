---
title: 'Coinbase Data Breach Timeline Doesn''t Add Up: I Have Recordings & Emails Proving Attacks Started Months Before Their ''Discovery'' - Jonathan Clark'
url: https://jonathanclark.com/posts/coinbase-breach-timeline.html
site_name: hackernews_api
fetched_at: '2025-11-17T19:06:50.672686'
original_url: https://jonathanclark.com/posts/coinbase-breach-timeline.html
author: jclarkcom
date: '2025-11-16'
description: How I was targeted by a sophisticated phishing attack in January 2025—four months before Coinbase publicly disclosed they had been breached. Evidence, recordings, and the timeline that doesn't add up.
tags:
- hackernews
- trending
---

← Back to Blog

## The Call That Changed Everything

On January 7, 2025, at 5:02 PM, I received an email with a subject line that immediately caught my attention:

"Order N54HJG3V: Withdrawal of 2.93 ETH initiated. A representative will be in touch shortly before we mark the payment completed"

Minutes later, my phone rang. The caller ID showed 1-805-885-0141. An American-sounding woman who identified herself as a Coinbase fraud prevention representative said someone had initiated a large transfer from my account and she was calling to confirm.

What happened next was chilling:She knew my social security number. She knew my Bitcoin balance down to the decimal point. She knew personal details that should have been impossible for a scammer to possess.

This wasn't just another phishing attempt. This was something far more sophisticated.

## Timeline, With Exact Dates

Here's the sequence, using exact dates:

* January 7, 2025:I was attacked by scammers with detailed personal information
* January 7, 2025:I reported the attack to Coinbase security@coinbase.com
* January 7, 2025 (same day):Brett Farmer, Head of Trust & Safety, responded: "This report is super robust and gives us a lot to look into. We are investigating this scammer now."
* January 13, 2025:I asked Coinbase: "How did the attacker know the balance of my bitcoin holdings?"(No response)
* January 17, 2025:I followed up again, asking for a reply(No response)
* January 22, 2025:Still no answer to my critical question(No response)
* January 29, 2025:I asked again: "Could I please get a response?"(No response)
* May 11, 2025:Coinbase says they became aware of the breach (when attackers demanded $20M ransom)
* May 15, 2025:Coinbase publicly disclosed the breach

That's a four-month gap.

For four months, I had concrete evidence that attackers possessed detailed Coinbase customer data. For four months, I repeatedly asked Coinbase to explain how this was possible. And for four months, my questions went unanswered.

Coinbase never replied to a single follow-up email after Brett Farmer's initial response.Despite his promise that they were "investigating this scammer," the most important question—how the attacker obtained my private account data—was met with complete silence.

## What Coinbase Disclosed in May 2025

In May 2025, Coinbase finally disclosed what had happened: cybercriminals had bribed overseas customer support contractors—particularly employees at TaskUs in India—to steal sensitive customer data.

The compromised information included:

* Names, addresses, and phone numbers
* Email addresses
* Last four digits of Social Security numbers
* Government-issued ID images
* Account balances
* Transaction histories

Coinbase estimated the financial impact at$180-400 million, affecting less than 1% of their customer base. Over 200 TaskUs employees were ultimately terminated.

But here's the crucial question:If attackers were actively using stolen data to target customers in January, when did the actual breach occur? And when did Coinbase first become aware that something was wrong?

## What I Sent Coinbase on January 7, 2025

On January 7, 2025, immediately after recognizing the attack, I sent a comprehensive security report to Coinbase's security team. This wasn't a vague complaint—it was a detailed technical analysis that should have raised immediate red flags about a data breach.

My report included:

* Full email headers:Complete technical headers showing the email was routed through Amazon SES (a32-86.smtp-out.amazonses.com), not Coinbase's own mail servers, despite appearing to come from commerce@coinbase.com
* DKIM signature analysis:Documentation that while the email passed DKIM validation for both coinbase.com and amazonses.com, the actual sending infrastructure was suspicious
* The phishing email content:The complete HTML email with its fake "suspicious activity" warning and fraudulent transaction details (Order N54HJG3V, 2.93 ETH withdrawal)
* Phone number used:1-805-885-0141 (later confirmed to be a Google Voice number)
* Voice recording:An audio recording of my second call with the scammer, capturing the entire conversation where she demonstrated knowledge of my personal information
* Specific data the attacker possessed:A detailed list of what the scammer knew, including:My Social Security numberMy exact Bitcoin balanceMy account signup dateDriver's license informationThe amount of the fabricated "suspicious transfer"
* My Social Security number
* My exact Bitcoin balance
* My account signup date
* Driver's license information
* The amount of the fabricated "suspicious transfer"
* Attack methodology:Description of their social engineering tactics, including the attempt to get me to move funds to "a cold wallet" by downloading Coinbase Wallet
* Red flags I identified:The inability of the caller to authenticate herself, the Google Voice callback number, the lack of any notifications in my actual Coinbase account
* Post-call SMS flooding:Documentation that immediately after the call, I received hundreds of spam text messages for random service signups—a potential attempt to hide legitimate 2FA codes or security alerts in the noise

This wasn't a typical phishing report.I specifically highlighted that the attacker had access to non-public account information that should have been impossible to obtain without either a device compromise on my end or a data breach at Coinbase.

Brett Farmer, Coinbase's Head of Trust & Safety, responded the same day, calling it a "super robust" report. But when I followed up with the key question—"How did the attacker know the balance of my bitcoin holdings?"—the conversation ended. That critical question was never answered.

## Inside the Scam Email and Call

Here's what made the email and call feel convincing in the moment—and what ultimately stopped me from going through with what the caller wanted.

### The Email: Remarkably Convincing

The phishing email I received looked completely legitimate at first glance:

* From:Coinbase Commerce <commerce@coinbase.com>
* DKIM signatures:Passed validation for both coinbase.com and amazonses.com
* Professional formatting:Perfect HTML layout, correct branding, legitimate-looking transaction details
* Convincing narrative:"We detected suspicious activity on your account. A fraud prevention representative will be in touch shortly..."

The email even included what appeared to be a verification code (96841) and assigned me a specific case agent ("Sarah Schueler"). This level of detail gave it tremendous credibility.

### The Critical Red Flag: Amazon SES

But when I examined the email headers more carefully, I found something suspicious. Here are the key header fields from the phishing email:

From: Coinbase Commerce <commerce@coinbase.com>
To: [REDACTED]@[REDACTED]
Subject: Order N54HJG3V: Withdrawal of 2.93 ETH initiated
Date: Tue, 7 Jan 2025 17:02:14 +0000
Message-ID: <01000194436f122c-535a7ce0-f493-41c2-b966-dcaa1a9e6b57-000000@email.amazonses.com>

Return-Path: <01000194436f122c-535a7ce0-f493-41c2-b966-dcaa1a9e6b57-000000@amazonses.com>
Received: from a32-86.smtp-out.amazonses.com (a32-86.smtp-out.amazonses.com. [54.240.32.86])
 by mx.google.com with ESMTPS id [REDACTED]
 for <[REDACTED]@[REDACTED]>
 Tue, 07 Jan 2025 17:02:18 +0000 (UTC)

DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
 s=224i4yxa5dv34ggfsdwu2l4en6sydsga; d=amazonses.com; t=1736269334;
 h=From:To:Subject:Date:Message-ID:MIME-Version:Content-Type;
 bh=xyz123...;
 b=abc456...

DKIM-Signature: v=1; a=rsa-sha256; q=dns/txt; c=relaxed/simple;
 s=gdwg2y3kokkkj5a5oi2lpk5uq5uqfm54; d=coinbase.com; t=1736269334;
 h=From:To:Subject:Date:Message-ID:MIME-Version:Content-Type;
 bh=xyz123...;
 b=def789...

Authentication-Results: mx.google.com;
 dkim=pass header.i=@amazonses.com header.s=224i4yxa5dv34ggfsdwu2l4en6sydsga header.b=abc456;
 dkim=pass header.i=@coinbase.com header.s=gdwg2y3kokkkj5a5oi2lpk5uq5uqfm54 header.b=def789;
 spf=pass (google.com: domain of 01000194436f122c-535a7ce0-f493-41c2-b966-dcaa1a9e6b57-000000@amazonses.com designates 54.240.32.86 as permitted sender) smtp.mailfrom=01000194436f122c-535a7ce0-f493-41c2-b966-dcaa1a9e6b57-000000@amazonses.com


The email was sent throughAmazon SES (Simple Email Service), not Coinbase's own mail servers. Here's what made this suspicious:

* Return-Path mismatch:The return path used @amazonses.com, not @coinbase.com
* Message-ID from Amazon:The Message-ID clearly shows @email.amazonses.com as the origin
* Dual DKIM signatures:While both amazonses.com and coinbase.com DKIM checks passed, this is exactly how phishing works—attackers can configure Amazon SES to send "from" coinbase.com
* SPF pass for wrong domain:SPF validated that Amazon SES was authorized to send for amazonses.com, not that it was authorized to send as coinbase.com

While Coinbase might legitimately use Amazon SES for some emails, a security-critical fraud alert should come through more controlled channels with stronger sender verification. The dual DKIM setup is a classic technique: attackers register with Amazon SES, configure it to "send as" the target domain (which Amazon allows), and rely on recipients not checking the actual sending infrastructure.

### The Phone Call: Even More Convincing (And Recorded)

When the woman called me, she was professional, intelligent, and sounded exactly like a legitimate customer service representative. She had all the personal information I'd already mentioned, plus more details that seemed impossible for a scammer to possess.

During our conversation, I asked her to authenticate herself. Here's where things got interesting.

## How I Detected It Was a Scam

Despite the sophistication of the attack, several red flags eventually convinced me this was fraudulent:

### Red Flag #1: The Authentication Problem

I asked the caller to prove she was from Coinbase. She offered to read me my personal information—but I already knew she had that information. That's not authentication; that's just proving she has stolen data.

When I suggested she send me an email from a verified Coinbase address that I could reply to, she claimed she didn't have access to personal email addresses and could only use generic support channels.A fraud prevention specialist without the ability to send verified emails? That didn't add up.

### Red Flag #2: The Callback Issue

When I asked if I could call her back, she said I couldn't reach her because she was "in the fraud department." After the call, I tried calling the number back:it was a Google Voice number.

Legitimate financial institutions always provide callback numbers that route to their main systems. A Google Voice number is a massive red flag.

### Red Flag #3: Email Verification Confusion

When I challenged the authenticity of the email sender, the caller insisted that Amazon was just Coinbase's "service provider" and that the DKIM signatures proved legitimacy. But when pressed, she couldn't explain away the anomalies in a satisfactory way.

The conversation on the recorded call shows my growing skepticism:

Me:"I don't think there is enough information provided for me to authenticate you."

Caller:"I'm not sure what you would like me to do..."

Me:"There are just too many red flags."

### Red Flag #4: No Notifications in My Account

After the call, I logged into my actual Coinbase account. There were:

* No notifications about the alleged transfer
* No new login attempts
* No new authorized devices
* No actual transaction matching what the caller described

If this were real, there would have been notifications everywhere.

### Red Flag #5: The Pressure to Use Coinbase Wallet

The caller wanted me to move my cryptocurrency to "a cold wallet" and started walking me through downloading Coinbase Wallet.This is a classic social engineering tactic—get the victim to move funds to an address controlled by the attacker.

I didn't follow through, so I never discovered exactly how they planned to steal the funds, but the intent was clear.

## The SMS Flooding Attack

Here's where things got even more concerning. Immediately after I ended the call with the scammer,my phone was bombarded with hundreds of text messages—random service signups, verification codes, newsletters, everything imaginable.

At first, I thought this was just a vindictive "FU" from the scammer. But the timing and volume suggest something more calculated:SMS flooding is a known technique to hide legitimate security alerts in noise.

The attack works like this:

1. Scammer floods your phone with spam texts
2. While you're overwhelmed, they attempt account takeovers on various services
3. Real 2FA codes and security alerts get buried in the flood
4. You miss the critical warnings because they're hidden among hundreds of spam messages

This could have been an attempt to:

* Hijack my SMS-based two-factor authentication
* Hide real alerts from Coinbase or other services
* Overwhelm me while they attempted unauthorized access to various accounts
* Create confusion and distract from their next moves

This wasn't just a phishing call—it was a coordinated, multi-vector attack.

## What Coinbase Got Wrong

Coinbase's handling of this breach raises serious questions:

### 1. Outsourcing Security-Sensitive Roles

Customer support agents at third-party contractors had access to extremely sensitive data: Social Security numbers, account balances, transaction histories, and personal documents.Why were overseas contractors given such privileged access?

The economics of the bribery scheme tell the story: attackers likely paid relatively small amounts to contractors earning modest wages to access data they then used to attempt thefts worth potentially millions.

### 2. Failed Detection Systems

Coinbase claims they "discovered" the breach on May 11, 2025, when attackers attempted to extort $20 million. But my case—and likely many others—proves the breach was being actively exploited months earlier.

What monitoring systems failed to detect that customer data was being used in sophisticated phishing attacks?I reported this in January with specific details about how the attacker knew my information. That report should have triggered alarm bells.

### 3. Inadequate Response to User Reports

Despite Brett Farmer's initial acknowledgment that my report was "super robust" and warranted investigation, my follow-up emails asking how attackers obtained my account data went completely unanswered.

My question was specific and technical. It went to the heart of what should have been a massive red flag: How did attackers have access to non-public account data?

Had Coinbase investigated this seriously in January, they might have discovered the insider threat months earlier and prevented additional victims.

### 4. The Disclosure Timeline

Coinbase says they "became aware" of the breach on May 11, 2025. But my January attack proves the breach was active at least four months earlier. This raises uncomfortable questions:

* When did the actual data exfiltration occur? Late 2024?
* How many other victims reported similar attacks between January and May?
* Were those reports properly escalated and investigated?
* Would Coinbase have disclosed the breach if not for the extortion attempt?

## Practical Ways to Protect Yourself

When a major platform gets breached, your personal information may already be in attackers' hands. You can't undo that, but you can still reduce the chances you'll fall for the scams that follow:

### 1. Never Trust Caller ID

Phone numbers can be spoofed. Even if the caller ID shows a legitimate company, don't trust it. Always hang up and call back using a number you independently verify (from the company's official website, not from the email or caller).

One practical check:Ask the caller for their callback number, then look up that number online before calling it back. Search for "[phone number] scam" or "[phone number] reviews" to see if others have reported it as fraudulent. In my case, when I called back the number the scammer gave me (1-805-885-0141), it turned out to be a Google Voice number—an instant red flag. Legitimate corporate support lines won't use Google Voice.

### 2. Understand That Scammers May Have Your Personal Info

In the age of massive data breaches, assume attackers may know:

* Your name, address, phone number, email
* Last 4 digits of your SSN
* Your account balances and transaction history
* Other "secret" information you thought was secure

Just because someone knows this information doesn't mean they're legitimate.Authentication needs to work both ways.

### 3. Verify Email Headers

Learn to check email headers. Look for:

* The actual sending server (not just the "From" address)
* SPF, DKIM, and DMARC validation results
* Unusual routing or relay servers

In my case, the Amazon SES sending address was the tip-off, even though DKIM signatures technically validated.

One way to sanity-check them:If you're not sure how to interpret email headers, copy the full headers and paste them into a good AI assistant (like ChatGPT or Claude) and ask: "Analyze these email headers and tell me if there are any red flags or signs this could be a phishing email." AI tools are excellent at spotting anomalies in technical data like email routing.

### 4. Demand Proper Authentication

If someone calls claiming to be from your bank, exchange, or other financial institution,they should be able to authenticate themselves to you, not just read back information they already have.

Legitimate companies can:

* Send you emails from verified domain addresses you can reply to
* Provide callback numbers that route through their main system
* Verify their identity through the app or website you're already logged into

### 5. Check Your Account Directly

If someone alerts you to suspicious activity, don't trust the email or call. Open a browser, type in the company's URL directly (don't click links), log in, and check for yourself. If there's really a problem, it will show up in your account.

### 6. Never Move Funds Under Pressure

Legitimate companies will never pressure you to immediately move your funds, download software, or take urgent action to "protect" your account.That pressure is the scam.

### 7. Use App-Based or Hardware 2FA, Not SMS

My experience with SMS flooding shows why SMS-based two-factor authentication is vulnerable. Use:

* Hardware security keys (YubiKey, Titan)
* Authenticator apps (Google Authenticator, Authy)
* Platform-specific authentication (like Coinbase's app-based approval)

SMS can be hijacked, flooded, or intercepted.

### 8. Report Everything

If you're targeted by a sophisticated attack, report it immediately and provide as much detail as possible:

* Full email headers
* Phone numbers used
* Specific information the attacker knew
* Recording of calls if possible (check your local laws)

Your report might be the data point that helps the company detect a breach.

## Why This Four-Month Gap Matters

My case represents just one data point in what appears to be a months-long campaign of attacks enabled by the Coinbase breach. How many other customers were targeted between January and May? How many fell for these scams because they didn't catch the red flags I did?

Coinbase has committed to reimbursing customers who were defrauded. But the $180-400 million estimated cost of this breach doesn't just represent reimbursements—it represents the human cost of trust betrayed, security compromised, and warnings ignored.

The cryptocurrency industry promises decentralization and security, but incidents like this expose the risks of centralized custody. When you trust an exchange with your assets and personal information, you're trusting their security practices, their contractor oversight, and their incident response capabilities.

In this case, that trust was misplaced.

## Questions Coinbase Still Hasn't Answered

Four months after my attack, and several months after Coinbase's disclosure, key questions remain:

1. When did the actual breach occur?My January attack suggests late 2024 at the latest.
2. How many customers were targeted before May 2025?Am I one of dozens? Hundreds? Thousands?
3. What happened to the user reports filed between January and May?Were they properly investigated and escalated?
4. Why wasn't the connection made between user reports of sophisticated phishing and a potential data breach?
5. What specific access controls failed that allowed overseas contractors to exfiltrate sensitive data?
6. Will there be regulatory consequences for the delayed disclosure?SEC rules require timely reporting of material cybersecurity incidents.
7. How can users trust that the security improvements Coinbase claims to have made are actually effective?

## Conclusion: The Timeline Matters

The discrepancy between my January attack and Coinbase's May disclosure isn't just an interesting footnote—it's a critical part of understanding what went wrong and who bears responsibility.

My emails, timestamped and documented, prove that:

* The breach was being actively exploited months before Coinbase's "discovery"
* A customer reported detailed evidence of the attack and asked specific questions about data compromise
* Those questions went unanswered for months
* The breach was only disclosed after attackers attempted extortion

I was one of the lucky ones—I detected the scam and didn't lose funds. But how many others weren't so fortunate during those four months of silence?

When I asked the one question that mattered most—how did the attacker have my data?—the company went silent.

That silence lasted 120 days.

And that's the real story behind the $400 million breach.

Note: Names and specific account balances have been redacted from this article, but all emails, dates, and phone numbers are documented and verifiable. The phone call recording is available upon request to journalists and researchers.

If you are a lawyer working on a case related to the Coinbase data breach, I invite you to contact me. I have comprehensive documentation, timestamped emails, and recorded evidence that may be relevant to establishing the timeline and impact of this incident.
