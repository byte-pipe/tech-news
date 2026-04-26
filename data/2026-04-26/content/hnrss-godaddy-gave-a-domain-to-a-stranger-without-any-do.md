---
title: GoDaddy Gave a Domain to a Stranger Without Any Documentation
url: https://anchor.host/godaddy-gave-a-domain-to-a-stranger-without-any-documentation/
site_name: hnrss
content_file: hnrss-godaddy-gave-a-domain-to-a-stranger-without-any-do
fetched_at: '2026-04-26T19:44:56.904670'
original_url: https://anchor.host/godaddy-gave-a-domain-to-a-stranger-without-any-documentation/
date: '2026-04-26'
published_date: '2026-04-26T10:30:00-04:00'
description: What would you do if your organization had used a domain name for 27 years, and the registrar holding the domain seized it without any advance warning? All
tags:
- hackernews
- hnrss
---

# GoDaddy Gave a Domain to a Stranger Without Any Documentation

April 26, 2026 · Austin Ginder

 

What would you do if your organization had used a domain name for 27 years, and the registrar holding the domain seized it without any advance warning? All email and websites went dark. The company’s tech support spent four days telling you to“Just wait, we are working on it.”On the fourth day, the company informed you that someone else has the domain now, and it is no longer yours.

Read on. This crazy story happened exactly one week ago.

My friend Lee Landis is a partner inFlagstream Technologies, a local IT firm in Lancaster, PA. Last Saturday afternoon one of his client’s domains vanished from his GoDaddy account.

Lee is one of the most competent IT guys I know. The GoDaddy account had dual two-factor authentication enabled, requiring both an email code and an authentication app code to log in. The domain itself had ownership protection turned on. The audit log just said “Transfer to Another GoDaddy Account” by an “Internal User” with “Change Validated: No.”

Some names have been changed
Some names and the domain itself have been changed because people wanted to remain anonymous. The pattern of the domain names mirrors the actual mistake, so the explanation still makes sense. Every fact in this post is true. Lee has hard evidence for every one of them.

As you can see above, GoDaddy emailed Flagstream at 1:39pm that an account recovery had been requested. Three minutes later, the transfer was initiated. Four minutes later, it was complete. On a Saturday afternoon.

Everything at the impacted organization went offline because GoDaddy reset the DNS zone to default when they moved the domain into the new account. Same nameservers. Empty DNS zone file.

Lee’s client lost their website and email for the next four days.

27 yrs
Domain in active use

32
Calls to GoDaddy

9.6 hrs
On the phone with GoDaddy

17
Emails to GoDaddy. Zero callbacks.

## Domain and account were fully protected.

The domain had the “Full Domain Privacy and Protection” security product that GoDaddy sells. Dual two-factor on the account. None of it mattered. The transfer was done by an “Internal User” inside GoDaddy.

The domain was HELPNETWORKINC.ORG. The real domain name has been changed because the organization wanted to remain anonymous. It belongs to a national organization with twenty locations across the United States. The domain has been in active use for 27 years. Each chapter runs its website and email on a subdomain of that one parent domain. When HELPNETWORKINC.ORG went dark, every chapter went dark with it.

## Thirty-two calls. 9.6 hours on the phone. Zero callbacks.

Lee called GoDaddy on Sunday. They confirmed the domain was no longer in his account but could not say where it went due to privacy concerns. They told him to emailundo@godaddy.com. He did but did not receive any type of response when emailing that address. Of course Lee didn’t really feel like this was the appropriate level of urgency for this issue. He asked for a supervisor who was even less helpful. Lee was not happy. He may have said some hurtful things to GoDaddy’s support personnel during this call. That first call lasted 2 hours, 33 minutes, and 14 seconds.

On Monday morning, Lee and a coworker started working in earnest on this issue because there was still no update from GoDaddy. Calling in yielded a different agent who told Lee to emailtransferdisputes@godaddy.cominstead. By Tuesday the address had changed again toartreview@godaddy.com. The instructions shifted by the day. It seemed like every GoDaddy tech support person had a slightly different recommendation.

The one thing that stayed consistent was the message:“Just wait a day or two. We are working on it. Why do you think this is so urgent?”

One of the most frustrating parts of this process is that all official communication to and from GoDaddy about this issue was done with generically named email accounts. It just seems like there should have been a named individual in charge of managing and communicating about this issue. Rather there were just random generic email accounts that seemed to change on a daily basis.

Every call generated a fresh case number. Lee lost count of the total number of cases. A few of the cases are01368489.894760.01376819.01373017.01376804.01373134.01370012. None of them tied together on GoDaddy’s side. Every escalation started from zero. These are actual case numbers, in case anyone at GoDaddy wants to check into this.

I posted on X to see if anyone I knew at GoDaddy could escalate.

Can any of my GoDaddy friends help? A good friend of mine had a domain taken. My friend is very competent. Domain ownership protection was on. Owner did not get any notices. Audit log looks fishy. Phone/email support telling them to wait. Did a GoDaddy employee take it?pic.twitter.com/OWcJIalWcF

— Austin Ginder (@austinginder) 
April 20, 2026

My friend Courtney Robertson, who works at GoDaddy, reposted it and started escalating internally on her own time. Thank you, Courtney. GoDaddy has a lot of great people like her. That part is not in question.What GoDaddy does not have is a way to actually fix a mistake once one has been made.Tickets pile up. Phone calls reset. Every escalation is a new person reading the case from scratch. The thing you actually need solved drifts between queues.

## And there was no real way to dispute it.

While Lee was on the phone, his colleague was on a different phone trying to file a Transfer Dispute. GoDaddy directed him tocas.godaddy.com/Form/TransferDispute. He filed a dispute and received this message, which he captured via a screenshot.

Lee and his colleagues worked diligently at challenging the transfer. They supplied the correct name of the person listed on the domain. They supplied that person’s drivers license as required. They also supplied the correct business documentation as listed in GoDaddy’s own requirements. Every time they submitted a request, they were told they would hear back in 48 to 72 hours.

## GoDaddy FINALLY responds with a SHOCKING statement

Tuesday afternoon, after four days of waiting, Flagstream finally got an official email response back from GoDaddy.

GoDaddy’s reply to Lee
After investigating the domain name(s) in question, we have determined that the registrant of the domain name(s) provided the necessary documentation to initiate a change of account. … GoDaddy now considers this matter closed.

That was it. No explanation of what documentation. The suggested next steps were three links. A WHOIS lookup. ICANN arbitration providers. A page about getting a lawyer involved to represent you in litigation.

## Flagstream migrates client to new domain

Once GoDaddy declared the matter closed, Flagstream began migrating the client to a new domain. New email addresses. New website addresses. Coordinating with various teams throughout the night to change everything over to a new domain.

Switching to a new domain is a massive amount of work, and it leaves a lot of lingering problems behind because there is no control over the original domain.

* Every email address that exists out in the world is now wrong. You have to tell everyone the new address. If they try the old one, it bounces.
* Every piece of marketing material that references the old domain is now incorrect. There is no way to forward anything to the new domain.
* All of the SEO is gone. You are starting an online presence from scratch.

## Then a stranger found the domain in her account.

Wednesday morning Susan (not her real name), 2,000 miles away from the client’s headquarters, noticed something odd. Susan had been working at reclaiming a totally different domain used by a former employee. When she looked closely at her GoDaddy account, the domain in her account wasn’t the one she had requested. She made a few phone calls because she knew this was a problem and eventually got hooked up with Flagstream. Working with Susan, they ran a GoDaddy account-to-account transfer, and put the domain back where it belonged. DNS came back up while Lee was still typing the email telling me it was over. The entire process of reclaiming the domain lasted less than 5 minutes.

Once the domain was back and DNS was working, Flagstream started the arduous task of reverting everything that they had done the day before. They switched email and websites back to the original domain, once again working through the night to get everything fixed.

The resolution for this problem did not come from GoDaddy support. It did not come from the dispute team. It did not come from the Office of the CEO team. It came from a stranger who accidentally ended up with the domain and was smart and honest enough to start calling around because she knew something wasn’t right.

Susan is really the hero of this entire story. Without her, Flagstream would still have no idea what happened to this domain. Lawyers would have gotten involved, but it would probably be months until anything was resolved.

## Timeline of events

Apr 18, 1:39pm
GoDaddy emails Flagstream that an Account Recovery has been requested for the account.

Apr 18, 1:42pm
Transfer initiated by GoDaddy Internal User. Three minutes after the recovery notice.

Apr 18, 1:43pm
Transfer completed. Change Validated is listed as “No”. Website and email go dark across the entire organization.

Apr 19
Lee discovers the domain is gone. GoDaddy says email undo@godaddy.com and wait.

Apr 20
Flagstream team starts calling and emailing GoDaddy for updates. GoDaddy now says email transferdisputes@godaddy.com. Austin posts on X. Courtney Robertson routes the case to the Office of the CEO team.

Apr 21
Flagstream files multiple Transfer Dispute cases with the requested documentation. Every submission is met with a 48 to 72 hour response window. GoDaddy emails Lee that the matter is closed and the domain belongs to someone else. Flagstream starts the painful process of migrating the organization to a new domain so they can function. 

Apr 22
Susan notices the wrong domain in her account and calls Lee. Account-to-account transfer brings it home.

## Then it got crazier. GoDaddy approved the transfer with zero documents.

The organization on the receiving end of the transfer was a regional chapter of the same network. Susan, the executive assistant, had emailed GoDaddy two weeks earlier asking to recover a different domain. HELPNETWORKLOCAL.ORG. Not HELPNETWORKINC.ORG.

Flagstream spent some time talking to Susan to figure out exactly how she was able to accidentally get the domain transferred into her account. Did she unintentionally supply all of the correct documentation? Talking to Susan they figured out that GoDaddy actually approved the transfer without her supplying ANY documentation.

Her email signature happened to reference her chapter’s website at a subdomain of HELPNETWORKINC.ORG. GoDaddy’s recovery team apparently looked at the signature, saw the parent domain, and transferredthatdomain into her account.

GoDaddy sent Susan a link to upload supporting documents.The link expired before she got around to using it.She emailed back requesting a new link so she could upload the required documentation. However, before the new link arrived, she received an email saying the domain transfer had been approved.

Susan never submitted a single document. Not for the domain she was actually trying to recover, and certainly not for the one GoDaddy ended up giving her. GoDaddy approved the change of account, transferred a 27-year-old non-profit’s domain into a stranger’s account, and “considered the matter closed” without requiring any documentation.

## This is a huge security issue.

If Susan had been a bad actor, she could have intercepted email. She could have used that email to reset passwords, get MFA codes, launch phishing attacks, etc. She could have put up a new website with malware on it, redirected payments on the website, etc.

When the domain initially disappeared and Flagstream was unable to obtain any information about who had it, Flagstream feared the worst. Flagstream and the impacted client started to come up with a plan to protect against the threats mentioned above which was a huge undertaking for an organization of this size. Basically, all users across the entire organization needed to start logging into every important website and make sure the compromised domain was removed from the account. This includes bank websites, Amazon, IRS, payroll, Dropbox, email accounts, and even ironically enough, GoDaddy accounts.

It is outrageous that Susan was able to obtain this domain without supplying any documentation. Everyone was lucky it was Susan that got this domain.

## GoDaddy: please follow up with Flagstream.

This is not acceptable.
A GoDaddy employee transferred a 27-year-old domain out of a paying customer’s account with no validation. With zero documentation submitted by the recipient. When the customer disputed with legitimate documentation, every submission was met with “We will respond in 48 to 72 hours.” After four days, GoDaddy claimed the domain belonged to someone else and the case was closed. The fix came from the recipient of the mistake, not from GoDaddy despite 9.6 hours of phone conversations.

To anyone at GoDaddy reading this.Please follow up with Lee Landis at Flagstream Technologies and make this right.An apology is probably in order. An internal review of how the transfer team validates documentation is in order, including how a transfer can be approved with zero documentation. Lee would like a clear answer on how this happened. Lee doesn’t want an email from a generic GoDaddy account. Lee wants a real person to call or email him. This person needs to leave an email address and phone number in case Lee has follow-up questions.

## Even disclosing this to GoDaddy was broken.

Before publishing this post, I wanted to share the findings with GoDaddy’s security team directly. I emailedsecurity@godaddy.comwith the full report. The message bounced.

GoDaddy’s auto-reply to security@godaddy.com
A custom mail flow rule created by an admin at secureservernet.onmicrosoft.com has blocked your message. We hope this message finds you well. This email mailbox is no longer monitored. To address your needs, we have outlined two popular options for you: 1: To submit an abuse report, please visit our Abuse Reporting Form. 2: If you are looking to submit a vulnerability, please visit our bounty program https://hackerone.com/godaddy-vdp.

So I filed the same report through HackerOne instead, report #3696718.

This is the same pattern that played out across the four-day outage. The official channel does not work. The alternative path requires knowing to bypass it. Most honest people who notice a security issue are not going to have a HackerOne account. They send an email.How is it that GoDaddy doesn’t have a public security disclosure email address?

Whether the original transfer was a single agent’s mistake or a flaw in the recovery workflow, it is still a security issue. And there is no clean path from “I found something” to “a human at GoDaddy is looking at it.”

## The only way to get GoDaddy’s attention is to leave.

Lee is upset about the four days of stress and lost productivity across the impacted organization. But his bigger concern is what comes next. Apparently there is no way to protect against this threat if your domain is hosted at GoDaddy. In addition, it seems like there is no efficient way to contest the GoDaddy transfer.

Flagstream will most likely migrate every one of their domains off GoDaddy. That is the only protection they have left, and the only escalation GoDaddy seems to respond to.

## Are you at risk?

Is your domain hosted on GoDaddy? What would you do if the domain disappeared out of your GoDaddy account and your entire business went dark?