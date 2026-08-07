---
title: Apple's iCloud Private Relay is Leaking Users' Real IP Addresses - MacRumors
url: https://www.macrumors.com/2026/08/05/icloud-private-relay-ip-address-leak/
site_name: tldr
content_file: tldr-apples-icloud-private-relay-is-leaking-users-real
fetched_at: '2026-08-07T00:41:37.880689'
original_url: https://www.macrumors.com/2026/08/05/icloud-private-relay-ip-address-leak/
date: '2026-08-07'
description: Apple's paid Safari protection feature that promises to keep your IP masked doesn't always work, according to security researchers Tommy Mysk and Talal Haj Bakry. It turns out iCloud Private Relay can expose your real IP to websites that use or pretend to use passkeys. iCloud Private Relay is a service included with paid iCloud+ plans. It is supposed to hide your IP and DNS information when you browse the web using Safari, but it is not a VPN that masks all traffic from a device.
tags:
- tldr
---

# Apple's iCloud Private Relay is Leaking Users' Real IP Addresses

Wednesday August 5, 2026 11:44 am PDT
 by 
Juli Clover

Apple's paid Safari protection feature that promises to keep your IP masked doesn't always work, according to security researchersTommy Mysk and Talal Haj Bakry. It turns outiCloudPrivate Relay can expose your real IP to websites that use or pretend to use passkeys.

‌iCloud‌ Private Relay is a service included with paid ‌iCloud‌+ plans. It is supposed to hide your IP and DNS information when you browse the web using Safari, but it is not a VPN that masks all traffic from a device. Passkeys use the WebAuthn standard, which stores a private key on your device, not the Safari browser. The request the system sends to the website isn't protected by Private Relay and can leak your IP address.

WebKit hands WebAuthn ceremonies to the operating system's credential service, which issues the HTTPS request itself, directly from the device and unaware of any proxy the host app configured. A page can set rpId to a host of its choosing, and the fetch fires even without user interaction: with mediation: "conditional" and no UI ever appears. [...]

Because the fetch is issued by the operating system's credential service rather than by Safari, it never enters Private Relay's proxied path. The destination server sees the device's real IP address either way.

An attacker who wants to find someone's protected IP can do so by setting up a website that uses WebAuthn. There is no visible passkey prompt and no other indication that an IP address has been accessed in the background.

The researchers also found two other WebKit features that can leak IP addresses and DNS data. DNS prefetching (added iniOS 26) reveals a user's real DNS servers, while WebTransport (added in iOS 26.4) can reveal an IP address.

Appletold404 Mediathat it is investigating the report.

Mysk and Haj Bakrycreated a websiteto let you test whether Apple's service is leaking your IP address. Since the issue is baked into how WebKit works, some third-party browsers are affected too. Apple will need to address the issue, and in the meantime, users can opt for a VPN for more protection.

Tag: 
iCloud
Related Forum: 
Apple Music, Apple Pay/Card, iCloud, Fitness+
[ 
118 comments
 ]

Get weekly top MacRumors stories in your inbox.

Leave this field empty

## Popular Stories

### Apple Raises iCloud+ Prices in 8 Countries

Friday July 17, 2026 11:56 am PDT by 
Juli Clover
Apple has increased the price of iCloud+ in Nigeria, Türkiye, Vietnam, Japan, Egypt, New Zealand, the Philippines, and Indonesia, according to an updated version of its iCloud support document.Price increases range from 11 percent to 55 percent depending on the plan and the country. Nigeria saw the biggest hike, and a 50GB plan is now ₦1,300, up from ₦900. Türkiye saw the next largest...

### Apple Plans Paid iCloud+ Upgrades for Heavy AI Users

Thursday July 30, 2026 4:11 pm PDT by 
Juli Clover
Apple is planning to let users pay to increase their AI limits, with upgrade possibilities available through iCloud+.During today's earnings call for the third fiscal quarter of 2026, Apple CEO Tim Cook said it's early, but the company expects to offer options for people who want to make heavy use of AI services.In terms of what it means for compute cost, it's obviously early going for...

### iPhone 18 Pro Launching Next Month With These 12 New Features

Sunday August 2, 2026 7:21 pm PDT by 
Joe Rossignol
It is now August, and that means the iPhone 18 Pro and iPhone 18 Pro Max should be launching next month. The devices are expected to look similar to the iPhone 17 Pro and iPhone 17 Pro Max, but there will still be many year-over-year changes, with rumored features including a smaller Dynamic Island, 5G via satellite, and more.Apple is expected to unveil the iPhone 18 Pro, iPhone 18 Pro Max, ...

## Top Rated Comments

B
bmot
1 day ago at 11:51 am
Isn’t that a valid legal reason for refunding all users of this subscription fully.
Score:
 47 Votes (
Like
 | 
Disagree
)
winxmac
1 day ago at 11:50 am
First, Hide My Email, and now, Private Relay.
Score:
 36 Votes (
Like
 | 
Disagree
)
ghostface147
1 day ago at 11:45 am
Come on man. What is going on here?
Score:
 25 Votes (
Like
 | 
Disagree
)
sw1tcher
1 day ago at 12:13 pm
It's not a real VPN therefore your IP shouldn't be masked at all times. No one has the expectation that your IP is private. So what's the issue?
Sounds to me just more complaining. 🤦‍♂️
Apple says with Private Relay enabled, your privacy is protected, meaning websites cannot see your IP or DNS info
https://support.apple.com/en-us/102602
How Private Relay works
Normally when you browse the web, 
information
 contained in your web traffic, 
such as your DNS records and IP address, can be seen by
 your network provider and 
the websites you visit
. This information could be used to determine your identity and build a profile of your location and browsing history over time.
iCloud Private Relay is designed to 
protect your privacy
 by ensuring
 that when you browse the web in Safari, 
no single party
 — not even Apple — 
can see both who you are and what sites you're visiting.
Apple even says if you have problems with some websites, you might need to disable Private Relay so sites can see your real actual IP address.
https://support.apple.com/en-us/102022
Manage iCloud Private Relay for specific websites, networks, or system settings
Some websites, networks, and services might need to see your IP address
 or require the ability to audit traffic, perform network-based filtering, or view your browsing history.
If Private Relay isn't designed to hide your actual IP, then what is it for then?
https://support.apple.com/guide/iphone/protect-web-browsing-icloud-private-relay-iph499d287c2/ios
When you subscribe to iCloud+, you can use iCloud Private Relay to help prevent websites and network providers from creating a detailed profile about you. 
When iCloud Private Relay is on
, the traffic leaving your iPhone is encrypted and sent through two separate internet relays. This 
prevents websites from seeing your IP address
 and exact location while preventing network providers from collecting your browsing activity in Safari.
Score:
 21 Votes (
Like
 | 
Disagree
)
B
bluecoast
1 day ago at 12:36 pm
iCloud private relay says that it will hide your IP address when browsing with Safari/webkit.
So if I land on a web page & my IP address is revealed via webauthn, it's clearly not working as Apple advertises - and they're misleading users as to their privacy.
Apple needs to tell us when a fix is incoming.
I wonder what the devs are working on this week.
More Ariana Grande iMessage stickers.
Score:
 20 Votes (
Like
 | 
Disagree
)
D
dominiongamma
1 day ago at 12:00 pm
So much for Apple and privacy.
Score:
 16 Votes (
Like
 | 
Disagree
)
Read All Comments