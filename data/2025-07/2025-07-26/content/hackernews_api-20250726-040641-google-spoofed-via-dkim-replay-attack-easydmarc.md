---
title: Google Spoofed Via DKIM Replay Attack | EasyDMARC
url: https://easydmarc.com/blog/google-spoofed-via-dkim-replay-attack-a-technical-breakdown/
site_name: hackernews_api
fetched_at: '2025-07-26T04:06:41.246836'
original_url: https://easydmarc.com/blog/google-spoofed-via-dkim-replay-attack-a-technical-breakdown/
author: Gerasim Hovhannisyan
date: '2025-07-25'
published_date: '2025-04-11T11:57:32+00:00'
description: Learn how a Google spoof used a DKIM replay attack to bypass email security and trick users with a fake subpoena in this real-world phishing case.
tags:
- hackernews
- trending
---

# Google Spoofed Via DKIM Replay Attack: A Technical Breakdown



* Published on:April 11, 2025

Last Modified on: July 16, 2025


12 Min Read



This morning started with a call from a friend – clearly shaken. He had just received an alarming email that looked strikingly legitimate. Unsure whether it was safe or a scam, he reached out to me for help verifying its authenticity.

What followed was a deep dive into the message to determine whether it was a genuine communication or a cleverly crafted phishing attempt. The email was convincing enough to create real concern, and that’s what makes this story worth sharing.

This was the email:

The email claimed that a subpoena had been issued by law enforcement requesting the extraction (access/download) of the contents of his Google Account.What made the situation even more alarming was that theemail appeared to come from a legitimate Google no-reply address. On the surface, everything looked clean – no typos, no odd links, and the sender domain seemed genuine. But something felt off, and that gut feeling is often your first line of defense.

Ready to secure your email? Get started now!

## Digging Deeper: Investigating the Suspicious Email

Curious and concerned, I examined the email headers and link previews in asandboxenvironment, a secure setup isolated from production systems, specifically designed for this kind of research. On the surface, everything appeared to check out:

* Thesender addresslooked like an official Google no-reply domain
* Thebrandingandlanguagewere polished and professional
* There wereno obvious grammar issuesor suspicious attachments.

But as we know, phishing campaigns have gotten much more sophisticated. So, I dug into theemail headers, checking theSPF, DKIM, and DMARCauthentication results. That’s when the red flags began to appear.

## Important Reminder: Don’t Engage with Suspicious Emails

Never click on links or follow instructions in suspicious emails, no matter how legitimate they may seem. Even opening a link or downloading a file could trigger malicious scripts or redirect you to phishing sites designed to steal your credentials.

If you’re unsure,leave the investigation to professionalswho can safely analyze the message in asandboxed environment..

Interacting with a malicious email outside of such an environment could result in:

* Loss of sensitive data
* Business Email Compromise (BEC)
* Account takeovers
* Wider network breaches

When in doubt, don’t click – report and escalate.

Here is the URL from that email:https://sites.google.com/u/34961821/d/1XMIxkFiq54WpH2tKqay2EPnhN0Ukovet/edit

This redirects to the Google account login page if you are not logged in :

After logging in, or if you are already logged in, it sends you to theGoogle Sites page.

Here’s something critically important to understand:This isnota real Google support page.It’s not a Google sign-in page. It’s not any official Google property in the traditional sense.

Instead, it’s aregular Google Sites page,a free tool anyone can use to build a website.In this case, cybercriminals used it to create a page that mimics an official Google support case, complete with convincing visuals and language.

Because it’s hosted on a trustedgoogle.comsubdomain (likesites.google.com), many users let their guard down. But don’t be fooled –just because the domain looks legitimate doesn’t mean the content is.

Start Email Security Check

## What Google Sites Is Used For

Google Sites serves as a practical tool for various purposes, including:

* Internal team pages (like company intranets or project dashboards)
* Documentation hubs
* Event landing pages
* Personal portfolios or school projects
* Simple public websites

You can create a site by dragging and dropping content blocks (text, images, videos, Google Docs, etc.), and it’s tightly integrated with other Google Workspace tools.

### When Trusted Infrastructure Becomes a Threat: Google Sites Abuse

Google Sites, originally launched in2008, is part of Google Workspace and allows any authenticated user to create a custom website hosted under thesites.google.comdomain. It’s widely used for internal and public-facing content due to its ease of use, zero cost, and native integration with Google products.

However, that same convenience is now being weaponized by attackers.

Why it’s dangerous:

* Anyone with a Google account can create a site that looks legitimate and is hosted under atrusted Google-owned domain.
* There’sno need for custom hostingor domain registration, and attackers benefit fromGoogle’s SSL certificates and brand reputation.
* Attackers canembed deceptive content(fake login screens, credential harvesting forms, misleading CTAs) under a domain that would normally pass casual user trust and even automated link validation checks.

Now let’s take a closer look at the key elements that make this scam so deceptive.

## How the Attacker Performed a DKIM Replay to Spoof Google

This attack was a confirmedDKIM Replay Attackwhere a spoofed message appeared to be from[email protected], had passedDKIM and DMARC, and was delivered to aGmail inbox.

Below is astep-by-step explanationof exactly what the attacker did, from start to finish — including all infrastructure involved.

### Step 1: Attacker receives a legitimate email from Google

The attacker first received areal email from Google, originating from[email protected].

It included a valid DKIM signature:

DKIM-Signature: d=accounts.google.com; s=20230601; bh=a+1bch/…

The attacker thenextracted and savedthis exact email, including headers and body, without modifying anything signed by DKIM.

### Step 2: Attacker prepares to replay the signed message

DKIM (DomainKeys Identified Mail) works by applying a digital signature to specific headers and the body of the email when it is first sent. This signature is generated using the sender’s private key and is attached as a header in the email itself.

When the message is forwarded, the original DKIM signature usuallyremains untouchedas long as the email content and headers covered by the signature are not modified. Since forwarding services often preserve the original messageas-is(especially in cases like aliasing or server-side forwarding), the DKIM signature remains valid and can still be verified using the sender’s public DNS record.

dkim=pass

### Step 3: Attacker sends the email from Outlook

The attacker used an Outlook account ([email protected]) to send the spoofed message.

Outbound hop:

Server:LO3P265CU004.outbound.protection.outlook.comIP:40.93.67.3

In another example, the origin of the email isGoogle’s notification service. The email flow is described in the attack reproduction section at the end of this article.

### Step 4: Message is relayed through Jellyfish SMTP

Microsoft then hands the message over to a custom SMTP service:

Relay:asp-relay-pe.jellyfish.systemsIP:162.255.118.7

This system acts as amiddle relay, distancing the spoof even further from Google. It’s not affiliated with Namecheap or PrivateEmail.

### Step 5: Message forwarded via Namecheap’s PrivateEmail

The message is then received by Namecheap’s mail infrastructure (PrivateEmail), which provides mail forwarding:

Systems involved:

* mta-02.privateemail.com
* DIR-08
* fwd-04.fwd.privateemail.com
* fwd-04-1.fwd.privateemail.com

During this phase:

* A new DKIM signature is added:DKIM-Signature: d=fwd.privateemail.com; l=52331;
* The body beyond 52KB isnot signed, but this DKIM isnot aligned, so it’snot used for DMARC.
* SPF passes due to rewritten Return-Path, but isalso not aligned.

However, since the original Google DKIM is untouched and aligned,DMARC still passes.

### Step 6: Final delivery to Gmail

Final delivery is handled by:

Sender:fwd-04-1.fwd.privateemail.com (66.29.159.58)RecipientMX:mx.google.com

At this point, the email reaches the victim’s inboxlooking like a valid message from Google, and all authentication checks show as passing:

* SPF=pass(via forwarder)
* DKIM=pass(from Google)
* DMARC=pass(based on aligned DKIM)

Final SMTP Hop Breakdown:

## When a Fake Subpoena Becomes an Attack Vector

Fake subpoena emails are especially dangerous because they trigger fear, urgency, and confusion. Most people don’t know precisely how subpoenas work, so when an email looks official and mentions legal action, it’s easy to panic and click without thinking.

To clarify, a subpoena is typically issued by:

* A court
* A lawyer (in civil cases)
* A government agency (in administrative cases)

A subpoena can require someone to:

* Appear in court
* Provide documents or evidence
* Testify at a deposition or trial

### Serving a Subpoena

The subpoena must beformally servedto the person or entity. Common methods include:

#### Personal Service (most common and preferred)

* A process server or law enforcement officer physically hands the subpoena to the individual.
* Required in most cases to ensure proper delivery and acknowledgment.

#### Mail or Email (only in some cases)

* Some jurisdictions or situations (especially civil subpoenas) allow service by certified mail or email,but only with prior consent or court approval. In such cases, the subpoena should be delivered in an encrypted way using the company’s official email address. It’s never delivered through third-party platforms.

#### A Registered Agent (for companies)

* If the subpoena is for a business, it’s often served to theirregistered agent(a person or service officially designated to receive legal documents on the company’s behalf).

Knowing how real subpoenas are issued and delivered can help you spot red flags. Phishing threats are evolving, no longer marked by broken English and sketchy URLs. Today’s attacks often come cloaked in legitimacy, sometimes even using platforms likeGoogle Sitesto mimic real support cases. As we saw in this real-world example, even the most tech-savvy users can be caught off guard.

## The Takeaway?

Always question unexpected emails, especially those urging urgent action or containing links to login pages. Just because something looks like it comes from Google (or any other trusted source) doesn’t mean it’s safe.

When in doubt,don’t click, don’t reply, and don’t engage.Escalate to your security team or a professional who can handle the investigation in a secure, sandboxed environment.

I’m interested in seeing more real-life examples. Do you have any notable cases to share?

Start DMARC Journey

## We Have an Update: Reproducing the Attack

We have dived deeper and successfully reproduced the attack:

In the first step, the attacker registered a domain viaNamecheap. We observed the attack originating from the following domains, which have now been taken down:

* googl-mail-smtp-out-198-142-125-38-prod.net
* wd-00000000000097d33d0631f6fe58-goog-ssl.com

On the second step attacker registered a free PrivateEmail via Namecheap.me@googl-mail-smtp-out-198-142-125-38-prod.net

On the third step they registered a Google Workspace account (free trial) and verified the domain via the DNS TXT record. You need to register it in the google to be able to move to the next steps.

In the next step, they created a Google OAuth app and granted the access to that account.

Here’s the twist: Google sends the alert or notification to the privately registered email address, where the domain is verified but uses different MX records than Google’s (specifically, Namecheap PrivateEmail).

And most importantly, the key trick is that you can put anything you want in the App Name field in Google.:

The alert goes directly to the Namecheap account, which has some very interesting “capabilities.”.

You can create conditions and put no-reply@google account as From address and the reply address can be anything:

the forwarding rule will direct the email to the desired addresses:

It is clearly visible from Resent-From and Redirected-From headers:

Here is the result:

The other details have already described.

## Frequently Asked Questions

What is a DKIM replay attack?

A DKIM replay attack is when an attacker captures a legitimate email with a valid DKIM signature and re-sends (replays) it to new victims. Since the body and signed headers remain unmodified, the DKIM signature still validates, making the spoofed email appear authentic.

Can SPF or DMARC prevent DKIM replay attacks
?

Not reliably.1.SPFvalidates theMAIL FROMdomain and sending IP, which often won’t align during a replay.2.DMARCrelies on alignment between SPF or DKIM and theHeader From. If DKIM is aligned (as in this case, google.com), and still valid, DMARC can pass, even though the message is replayed from an attacker’s server.

Why are DKIM replay attacks hard to detect?

DKIM replay attacks are hard to detect because the message appears unmodified, with a valid DKIM signature and even a DMARC pass.

If you rely on the email body or DKIM signature verification you may not see anything suspicious. The attack relies on trust in previously signed content, not on breaking cryptography.

How did the attacker bypass detection using Google OAuth?

The attacker created amalicious Google OAuth app, naming it something like “Google Support.”

They inserted phishing content and links into theApp Informationwhich includes manually cloned Google support page hosted onsites.google.com.

Google generated a valid security alert from[email protected]when access was granted, which the attacker thenforwarded to the victim.

The forwarded email looked like it came from Google and passed DKIM/DMARC, giving it credibility.

What are the most effective ways to be cautious and reduce the risk of DKIM replay attacks?

Rotate DKIM Keys FrequentlyChanging your DKIM keys regularly reduces the time window attackers have to abuse a captured signed message. Set your rotation cycle to 30 days or less for high-risk domains.

Raise User AwarenessUsers play a critical role in detecting suspicious activity:

1. Encourage caution when clicking on links, even if the sender looks familiar.2. Remind users to check URLs carefully before entering any credentials.3. Share examples of phishing tactics like urgent language, fake legal notices, or account alerts.4. Promote a culture of reporting. If something feels off, it’s always worth flagging.

Contact Us



Gerasim Hovhannisyan

CEO & Co-Founder EasyDMARC

Gerasim is the Co-founder and CEO, with over 15 years of experience in tech and cybersecurity.

Comments


We’re glad you joined EasyDMARC newsletter! Get ready for valuable email security knowledge every week.

You’re already subscribed to EasyDMARC newsletter. Continue learning more about email security with us
