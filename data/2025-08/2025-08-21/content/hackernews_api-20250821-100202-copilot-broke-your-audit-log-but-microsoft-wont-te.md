---
title: Copilot Broke Your Audit Log, but Microsoft Won’t Tell You - Pistachio Blog - Cybersecurity Awareness Training
url: https://pistachioapp.com/blog/copilot-broke-your-audit-log
site_name: hackernews_api
fetched_at: '2025-08-21T10:02:02.240652'
original_url: https://pistachioapp.com/blog/copilot-broke-your-audit-log
author: Zack Korman
date: '2025-08-20'
description: Copilot Broke Your Audit Log, but Microsoft Won’t Tell You
tags:
- hackernews
- trending
---

Published on
19.08.2025
8
 min read

Like most tech companies, Microsoft is going all-in on AI. Their flagship AI product, Copilot (in all its various forms), allows people to utilize AI in their daily work to interact with Microsoft services and generally perform tasks. Unfortunately, this also creates a wide range of new security problems.

On July 4th, I came across a problem in M365 Copilot: Sometimes it would access a file and return the information, but the audit log would not reflect that. Upon testing further, I discovered that I could simply ask Copilot to behave in that manner, and it would. That made it possible to access a file without leaving a trace. Given the problems that creates, both for security and legal compliance, I immediately reported it to Microsoft through their MSRC portal.

Helpfully, Microsoft providesa clear guide on what to expectwhen reporting vulnerabilities to them. Less helpfully, they didn’t follow that guide at all. The entire process has been a mess. And while they did fix the issue, classifying this issue as an ‘important’ vulnerability, they also decided not to notify customers or publicize that this happened. What that means is that your audit log is wrong, and Microsoft doesn’t plan on telling you that.

This post is split into three parts. The first part explains the Copilot vulnerability and the problems it can cause. The second part outlines how Microsoft handled the case. And the third part discusses Microsoft’s decision not to publish this information, and why I consider that to be a huge disservice to Microsoft’s customers.

## The Vulnerability: Copilot and Audit Logging

The vulnerability here is extremely simple. Normally, if you ask M365 Copilot to summarize a file for you, it will give you a summary and the audit log will show that Copilot accessed that file on your behalf.[1]

That’s good. Audit logs are important. Imagine someone downloaded a bunch of files before leaving your company to start a competitor; you’d want some record of that, and it would be bad if the person could use Copilot to go undetected.[2]Or maybe your company has sensitive personal data, and you need a strict log of who accessed those files for legal and compliance purposes; again, you’d need to know about access that occurred via Copilot. That’s just two examples. Organizations rely on having an accurate audit log.

But what happens if you ask Copilot to not provide you with a link to the file it summarized? Well, in that case, the audit log is empty.

Just like that, your audit log is wrong. For a malicious insider, avoiding detection is as simple as asking Copilot.[3]

You might be thinking, “Yikes, but I guess not too many people figured that out, so it’s probably fine.” Unfortunately, you’d be wrong. When I found this, I wasn’t searching for ways to break the audit log. Instead, I was simply trying to trigger the audit log so I could test functionality we are developing at Pistachio, and I noticed it was unreliable. In other words, this can happen by chance.[4]So if your organization has M365 Copilot licenses, your audit log is probably wrong.

UPDATE:It turns out thatMichael Bargury, the CTO atZenity, found this a year ago and disclosed it, and Microsoft still didn’t fix it (hence my report). He gave a really good talk on the topic, amongst other bad AI stuff. The relevant part ishere.

## Problems with MSRC

I had never reported a vulnerability to Microsoft before, and my initial reaction to the process was fairly positive. The fact that I could submit something already felt unusually friendly by Microsoft’s standards. And like I mentioned, they even had a guide on what to expect.

Unfortunately, nothing went according to plan. On July 7th my report’s status was changed to “reproducing”, but when I went to provide more evidence on July 10th the functionality had changed. That isn’t Microsoft’s policy; they’re meant to reproduce, then move to “develop” when they start working on a fix. Seeing the functionality change while still in “reproducing” made me think Microsoft was going to get back to me and claim they couldn’t reproduce the issue, when actually they had simply fixed it based on my report.

So I asked MSRC what was happening, and instead of responding with a simple explanation, they changed the status of the report to “develop” and said nothing. Up until that point I thought Microsoft was going to follow a process, and coordinate with me if they had to deviate from that. Instead, it felt like the process was less a reflection of what was really happening, and more akin to the Domino’s Pizza Tracker for security researchers. The statuses aren’t real.

On August 2nd, Microsoft informed me that a full fix would be released on August 17th, that I would be free to disclose as of August 18th. I then asked when a CVE number would be issued, and I was told:

CVEs are given to fixes deployed in security releases when customers need to take action to stay protected. In this case, the mitigation will be automatically pushed to Copilot, where users do not need to manually update the product and a CVE will not be assigned.

That is not Microsoft’s policy at all, which I pointed out to them bylinking to their own policy. MSRC then wrote back, “I understand you may not have full visibility into how MSRC approaches these cases”, as if I was the wrong one. They then explained that the vulnerability is classified as “important”, not “critical”, and that is why they will not issue a CVE.[5]Of course, they had not told me that they had classified the vulnerability at all prior to that point.

## Microsoft’s Decision to Say Nothing

If Microsoft isn’t issuing a CVE for this vulnerability, how are they going to inform customers about it? The answer is that they’re not going to. On a call on August 14th, Microsoft told me that they had no plans to disclose this.[6]

I strongly feel that is wrong. It might be okay to move on silently if this was some esoteric exploit, but the reality is that it is so easy that it basically happens by accident. If you work at an organization that used Copilot prior to August 18th, there is a very real chance that your audit log is incomplete.

Do organizations not need to know that? What about companies that are subject to HIPAA and are relying on Microsoft’s audit log to satisfy some of thetechnical safeguard requirements? Do they not get to know, despite Microsoft claiming M365 Copilot can beHIPAA compliant? There are almost certainly other regulated entities with similar requirements, and they also won’t be told.

There are so many cases in which organizations rely on audit logs to detect, investigate, and respond to incidents. There are lawsuits where audit logs are used as important evidence. The US government even made anissue out of Microsoft charging more for audit logs, with a US senatorshaming Microsoftand referring to audit logging as an essential security feature.

And now Microsoft is saying that even though the audit log was very plausibly wrong for any customer using Copilot, no one needs to know? This raises serious questions about what other problems Microsoft chooses to silently sweep under the rug.

Who wrote this?

Zack Korman is the CTO at Pistachio. He writes about product and tech development, as well as his experience in the cybersecurity space. Prior to joining Pistachio he was the Director of Tech and Product at a large media company in Norway.

## Fed up with out-dated cybersecurity training? Us too.

### See for yourself why Pistachio is the next evolution of cybersecurity training.

Start Free Trial
