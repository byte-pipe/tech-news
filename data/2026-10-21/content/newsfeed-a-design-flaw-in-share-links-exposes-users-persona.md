---
title: A Design Flaw in Share Links Exposes Users’ Personal Conversations With Meta’s Muse | WIRED
url: https://www.wired.com/story/a-design-flaw-in-share-links-exposes-users-personal-conversations-with-meta-muse/
site_name: newsfeed
content_file: newsfeed-a-design-flaw-in-share-links-exposes-users-persona
fetched_at: '2026-10-21T15:51:47.057231'
original_url: https://www.wired.com/story/a-design-flaw-in-share-links-exposes-users-personal-conversations-with-meta-muse/
author: Dan Goodin, Ars Technica
date: '2026-10-21'
published_date: '2026-10-21T12:35:00.000Z'
description: The company is suspending the feature after security researchers discovered how easy it was to access sensitive information shared with the AI assistant.
tags:
- wired
- security
- security / cyberattacks and hacks
- meta
---

Close Banner
Close
00
Days
:
00
Hours
:
00
Minutes
:
00
Seconds
Join us in Miami
See the full lineup
Save Story
Save this story
Save Story
Save this story

Muse, the newgeneral-purpose AI agent from Meta, can exposesensitive informationwhen users share conversations through web links, researchers reported Monday. In response to questions from Ars about the behavior, Meta said it’s suspending the sharing feature while the company reviews it and considers making changes.

Like many online services,Muse has allowedusers to share searches, conversations, images, and similar content with other people. Such share features usually involve clicking an option to create a unique URL that anyone can use to load a page hosting the content. To keep potentially sensitive information from being accessible tounintended people, the URLs typically contain a long sequence of text that can’t be easily guessed.

Muse, which Meta CEO Mark Zuckerbergsaid last monthwas “built from the ground up for privacy and security,” seems to take the same precautions. But a central design decision for constructing URLs has made the links easy to discover. As a result, researchers from security firm Clarocsaidthey were able to enumerate 6,800 links Muse users created for sharing conversations with others. After opening a few hundred of them, the researchers found information that was clearly not intended to be publicly available, including:

* a candidate’s notes preparing for a confidential executive-search call with a frontier AI lab, naming the lab’s internal contact and the meeting time;
* a national marketing company’s internal revenue review, marked for its CEO;
* a small-business owner’s loan application, with the amount requested;
* a to-do list that included a bank fraud alert, with a partial account number and a transaction amount and time;
* a real-estate investor’s internal performance report, with two property addresses and exact return, income, and mortgage figures;
* a workplace’s full-year staff vacation calendar, listing dozens of employees against the week each one would be away;

“If you had asked us beforehand, we would have guessed that gathering these would take real effort,” the researchers wrote. “It took one query.”

In an emailed statement responding to questions from Ars, Meta said: “We opened the Muse bug bounty program so researchers could raise different scenarios and help us continue improving the product. People have the ability to share specific Muse artifacts, which creates a page that can be accessed by those with the link. However, we’ve paused this functionality while we review this report and consider changes to how these links can be discovered.”

Asaf Aprozper, a cofounder and CTO of Claroc, said he reported the findings through Meta’s bug bounty program on October 8 and also tried reaching people at Meta on LinkedIn but got no reply either way.

The easiest way to discover the URLs is to perform a passive DNS search through one of many available commercial services.Passive DNS recordsstore the historical resolution of domain names to IP addresses, as well as nameserver, and mail-server records over time. Passive DNS systems typically collect DNS responses from sensors positioned at recursive DNS resolvers or other infrastructure. A passive DNS record is generally created when a monitoring system observes a DNS response. In the case here, once the intended party clicks on the share link, the DNS information is recorded in a searchable database.

Claroc researchers were able to discover the Muse share links because all of them use the domain name cf.metaaiusercontent.com. Discovery is further made easy by the decision to add the conversation name to the URL, along with a long string of text. Simplified examples of such links are home-sale-budget-9f21c8a3.cf.metaaiusercontent.com, q3-revenue-review-7b1e42f0.cf.metaaiusercontent.com, and loan-application-draft-a4c9e2.cf.metaaiusercontent.com. It’s this last design decision, putting the conversation title in the subdomain rather than in the URL path, that makes public discovery possible.

“Plenty of AI assistants shareby public link,” Claroc said. “What makes Muse’s shares easy to find is the title sitting inside the web address, where public DNS records it for anyone to search. We call these GhostShares: pages that open for people who were never handed the link, and that those people can find on their own.”

Muse quickly catapulted to one of the top spots in Apple’s App Store. The assistant autonomously fills out forms, books appointments, makes purchases, creates documents, and carries out all kinds of other actions. To work as intended, Muse requires access to most of a user’s accounts. Meta has heavily marketed the assistant as a platform that’s worthy of theextraordinary trustit needs to work as intended.

Three weeks after the Muse launch, macOS security expert Patrick Wardlediscovered a zero-day vulnerabilitythat allowed any other app installed on the same device to gain complete control of the user’s Muse account. Meta downplayed the severity of the vulnerability on the grounds that exploitation wasn’t possible unless a device was already compromised. The company didn’t acknowledge Wardle’s finding that a simpleClickFix attackwas all that was needed to hijack an account. The ease in discovering share links further justifies asking if Muse is worthy of the access it requires.

With Meta’s suspension of the feature, Muse users no longer face this particular threat, at least for now.

This story originally appeared onArs Technica.

## Comments

Back to top
Join the discussion

## Comments

Back to top
Triangle

## You Might Also Like

* Introducing the app:More ways tomake the most of WIRED
* Why so many AI researchersthink the technology could kill us all
* The Big Interview:Patti Harrisonhad dreams of a tech utopia
* I let an AI agenthack all my gadgets—and I’d do it again
* In your inbox:Go inside the world of digital security withKernel Panic
Dan Goodin is IT Security Editor at Ars Technica. ... 
Read More
* X
Topics
Meta
messaging
security disclosures
Ars Technica
chatbots
artificial intelligence
privacy