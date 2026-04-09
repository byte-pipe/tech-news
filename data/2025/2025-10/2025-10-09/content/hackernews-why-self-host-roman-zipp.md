---
title: Why Self-host? | Roman Zipp
url: https://romanzipp.com/blog/why-a-homelab-why-self-host
site_name: hackernews
fetched_at: '2025-10-09T19:07:13.268464'
original_url: https://romanzipp.com/blog/why-a-homelab-why-self-host
author: romanzipp
date: '2025-10-09'
published_date: '2025-10-09 09:49:00'
description: Let me make the argument why you should start self-hosting more of your personal services.
---

# Blog

 Roman Zipp


# Why Self-host?

Let me make the argument why you should start self-hosting more of your personal services.

 09 Oct 2025


 |



 9 min read


 |


 11 Comments



 |


 Essays


I recently shared my current Homelab setup with a colleague and was asked a pretty simple question I just took for granted...why?

Why go through the hassle of configuring servers, installing applications, setting up containers and spending quite a substantial amount of money on hardware that will not even run under optimal data center conditions (consumer-grade internet connection, no failover, no auto migrations)?

I will also give some specific recommendations on what you could and maybeshouldself-host.## PrivacyYou saw that coming.Privacy is not a god-given right but has to be fought for. Big Tech and governments (like withchat controlin the EU) want to shine light in every part of your personal life. Self-hosting services can reduce or even completely mitigate the risk of being surveilled. But it also requires a lot of technical knowledge so you can make a difference and educate your family or friends and even host some services for those who don't have the capabilities.### Calendar & ContactsYour calendar says more about you than you probably think. Apart from your full identity it can also give away information about regular contacts, family, coworkers, confidential business meetings, your health information such as medical appointments, sleep and workout routine, legal obligations, financial information like scheduled loans, subscriptions, political beliefs through scheduling to visit a protest and even let's other profile your behavior for identity theft to find out when you're available and when not.Same goes for contacts, your social graph can say so much about you, combined with metadata such as queries for certain contacts and creation dates. Did you recently add an unusual amount of new contacts with the same sex, first name only and phone number? You must be dating. Just created a contact for a doctor? Looks like you're visiting a therapist.Most people don't even think about where their social graph data is stored and probably assume it comes with their phone when in reality that data is being processed by Google, Apple, Samsung or whoever knows.I don't want a single company holding all that sensitive information and possibly deriving data points from that. Even with Apple'sAdvanced Data Protectionyour calendars and contacts are not end-to-end encrypted.### LocationMany many years ago I was running an Android phone with Google services like Google Maps. One day I was looking for a feature in my Google account and saw that GMaps recorded my location history for years with detailed geocoordinates about every trip and every visit.I was fascinated but alsoscared about thatsince I've never actually enabled it myself. I do like the fact that I could look up my location for every point in time but I want tobe in controlabout that and know thatonly I have accessto that data.### So much moreIt's beyond the scope of this post to list every possible way, your data can be traced back to you and argument why you should be conscious about that. I want to motivate you to start a new journey!## SovereigntyDigital sovereignty for me means to be in control of, choosing what I do with and controlling who I share my data with.You constantlyhear about casesof tech companies locking down accounts with no apparent reason and it even happened to me in the past with Google. I do not want to be at the mercy of a giant tech firm which you can not even contact or if - get annoyed by agarbage AI chat bot(see myMicrosoft rantfor more fun).Besides - why are there no regulatory requirements for tech companies to provide a way to get in contact with an actual human?I like protocols and file standards, no "Gmail" API - we call that thing SMTP and IMAP (yes, they are dated but the best we currently have. Thus I still welcome the newJMAP initiative). Another paragraph without bashing Microsoft? Hell no, Big Tech like Microsoft really wants you to use their AI-Copoilit-enabled-365-Office-Live-Outlookspywaresoftware - that's why they have recentlydisabled SMTP accessfor Office 365 accounts.## What to self-hostLet's get to the bread and butter of this article and give some straightforward examples on what to self-host.Some of those applications need to be available outside of your local network if you don't want to be constantly connected to a VPN. I will write more abouthow to do that securelyand all available options in an upcoming post. If you want to read that,subscribe to the RSS feed.### HardwareI'm fortunate enough to work at a company (enum.co) where digital sovereignty is not just a phrase. That's why I got provided with three mini servers where I'm running a highly availableKubernetes cluster(which my boss also helped me set up, thanksMax!). Also... more on that in a later blog post.### Calendar & ContactsAs stated above, calendar and contact data is more sensitive than one might think. This is why I am hosting my own CalDAV / CardDAV server.There are some options on servers for you which all have their ups and downs. Here are just a few:Radicale(Python, basic web ui, only single user, does not work with apple devices from my experience)⭐Baïkal(PHP, active development, advanced web ui, multi-user)DAViCal(PHP, haven't tried)Xandikos(Python, No built-in authentication, no web ui)Nextcloud(PHP, If you're already using it go for it - too bloated for me)

Baïkal Web UI

Being conscious about what other can do with your calendar and contact data also mean to review, which apps have access to your contact book and calendar.### MailOh no, I said the forbidden phrase: Self-hosted mail server. I was always told to never under any circumstances do that. But it's really not that deep."Recent" developments likeStalwartorMailcowmade it really easy and straighforward to self-host email. Beware I'm not talking about marketing mails but rather personal inboxes.Of course, you don't want to self-host your mail server at home since it requires a static IP and needs to be reachable from the whole internet. Going into that, you want to start with a clean IP address. Choose a hoster youtrust, get a server, look up the IP address in mail blacklists and repeat until you get a clean one. After setting up the server, you want to make sure you can receive mail and every required protocol has been correctly configured. I found theinternet.nl online test toolto be super usefull to ensure everything works. Start by sending mails to Google, Microsoft and Yahoo addresses to check if your mails are getting redirected to SPAM. Iterate on that, check DNS, DMARC, SPF, TLS etc.I will probably write a detailed blog post on that in the future.### Smart HomeWhen I started hosting my ownHome Assistantinstance a couple of years ago it was just an experiment to see what I can do since I wasn't really missing anything with Apple Homekit. Since then more and more smart home companies went bankrupt, sunsetted their cloud services, jacked up prices or put free services behind a paywall.For me, Home Assistant paid off a couple of weeks ago when I heard thatPhilips Hue will force users to create an accountjust to useany featurefor their lights, they already paid real money for. I've always configured Firewall rules to disallow any outgoing network traffic for smart home appliances but it seems like I cannot use any Philips Hue app specific features (like animated light patterns imitating candles etc.) even on my local network. I haven't looked into this but I hope there's some community plugin which emulates this functionality.I willnever, under any circumstances, create an online account for an appliance I will only use locally.Also I am now obsessed with tracking energy usage and plan on building and developing a Raspberry Pi + camera device which tracks energy usage of gas meter via machine vision.

Home Assistant

### RSS AggregatorI am subscribed to many news sites and blogs over RSS which is by itself already decentralized and sovereign. This is why self-hosting an RSS aggregator is kind of optional and only the last mile to go.On my iPhone and Mac I'm runningNetNewsWire, in my opinion the best RSS reader, even open source and backed byincredible people. NetNewsWire comes with a native integration forFreshRSS- a feed aggregator that also provides many more features like filtering and lets you subscribe to sources which don't natively provide an RSS feed.### Location TrackerI've deployed an instance ofdawarich(German for "I was there") which is a server for ingesting and viewing geolocation data. It also allows you to choose from many available mobile apps which can track send your current location to the server. At the time of writing this includes:official dawarich app(always shows a navigation icon in the iOS notch)Overland(high battery drain for me)⭐Owntracks(works best for me on iOS, only app settings are crazy confusing)PhoneTrack

dawarich Web UI

### Ideas & OutlookI recently re-worked my homelab and went from a single big server to a 3 node Kubernetes cluster. This gives me much more flexibility in the kind of applications I can host.This is a list of apps and tools I want to have a look at:EteSync: End-to-end encrypted CalDAV & CardDAVAnyType: Self-hosting my own AnyType server instanceIimmichorente: Moving from iCloud photos to self-hostingPassbolt: Password manager (no I really don't like Bitwarden)BirdNET: Monitoring bird species outside with a microphonepenpot: Like Figma but free & open sourceHabitica: Habit managervert: File converterInvoiceShelf: Invoice managerThere's alsoselfh.st- a great resource where can spend hours finding self-hostable applications.

## Comments

## Read more...

#### Shut The Fuck Up

Everything is getting more annoying by the hour

 02 Oct 2025


 |



 4 min read


 |


 1 Comment



 |


 Essays


#### List or Delete Calendars and Contacts via cli (CalDAV / CardDAV)

Overview on how to interact with CardDAV and CalDAV servers via the cli

 26 Sep 2025


 |



 2 min read



 |


 Guides
