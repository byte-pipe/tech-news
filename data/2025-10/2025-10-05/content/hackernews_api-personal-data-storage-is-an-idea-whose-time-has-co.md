---
title: Personal data storage is an idea whose time has come
url: https://blog.muni.town/personal-data-storage-idea/
site_name: hackernews_api
fetched_at: '2025-10-05T19:07:26.470843'
original_url: https://blog.muni.town/personal-data-storage-idea/
author: erlend_sh
date: '2025-10-05'
published_date: '2025-10-05T08:58:01.000Z'
description: Data Ownership as a conversation changes when data resides primarily with people-governed institutions rather than corporations.
tags:
- hackernews
- trending
---

Back in 2009 Tim Berners-Lee drafted a web-specification for "Socially Aware Cloud Storage":

There is an architecture in which a few existing or Web protocols are gathered together with some glue to make a world wide system in which applications (desktop or web application) can work on top of a layer of commodity read-write storage.
Crucial design issues are that principals (users) and groups are identifies by URIs, and so are global in scope, and that elements of storage are access controlled using those global identifiers. The result is that storage becomes a commodity, independent of the application running on it.
Socially aware cloud storage - Design Issues
Design Issues

Several of these ideas were going around in the late 2000s, shortly after the explosive growth of "web2" monoliths like Facebook.

Another spiritually similar idea being championed at the time came from the Opera browser folks who wanted to put"a web server in your browser".

While 'Opera Unite' never fully materialized, Tim's spec got significant traction some years down the road as one privacy crisis after another made the case for stronger web agency self-evident.

In 2015 Tim & co.secured some funding for the Solid Protocol.

Right now we have the worst of both worlds, in which people not only cannot control their data, but also can’t really use it, due to it being spread across a number of different silo-ed websites. Our goal is to develop a web architecture that gives users ownership over their data, including the freedom to switch to new applications in search of better features, pricing, and policies.”
Tim Berners-Lee, Inventor of the Web, Plots a Radical Overhaul of His Creation
The creator of the web just received the equivalent of the Nobel Prize for computing. But his work is far from over.
WIRED
Klint Finley

Archive link

On the better web Berners-Lee envisions, users control where their data is stored and how it's accessed. For example, social networks would still run in the cloud. But you could store your data locally. Alternately, you could choose a different cloud server run by a company or community you trust.
You might have different servers for different types of information—for health and fitness data, say—that is completely separate from the one you use for financial records.

To this day, Tim continues to eloquently championthe virtues of the Solid vision.

We have the technical capability to give that power back to the individual. Solid is an open-source interoperable standard that I and my team developed at MIT more than a decade ago. Apps running on Solid don’t implicitly own your data – they have to request it from you and you choose whether to agree, or not. Rather than being in countless separate places on the internet in the hands of whomever it had been resold to, your data is in one place, controlled by you.
Sharing your information in a smart way can also liberate it. Why is your smartwatch writing your biological data to one silo in one format? Why is your credit card writing your financial data to a second silo in a different format? Why are your YouTube comments, Reddit posts, Facebook updates and tweets all stored in different places? Why is the default expectation that you aren’t supposed to be able to look at any of this stuff?
You generate all this data – your actions, your choices, your body, your preferences, your decisions. You should own it. You should be empowered by it.

TheSolid Protocolremains an excellent idea and has even culminated in an officialweb specification, but Solid has not yet amounted to any mainstream adoption on the web. Its primary financial sponsorInrupt(of which Tim is co-founder & CTO) has focused on the enterprise market as a path to sustainability; it remains to be seen what resources will be directed towards web-scale adoption of Solid.

Thankfully those of us who want data ownership and agency in our web applicationsnowdon't have to wait.AT Protocolwas ushered in by the folks atBluesky, now with a network of over 30M people strong and increasingly spread across multiple federated platforms/communities likeBlackskyorTangled.

While the respective architectures of theSolidandATprotocols are quite different, they're pointing to the same Open Social Web, re-built on the principles of user-sovereign data storage.

## Personal Data Storage

What web-user sovereignty looks like in practice, from the vantage point of atproto, has been expertly illustrated bydanabra.mov

Open Social — overreacted
The protocol is the API.
Notice that Alice’s handle is now
@alice.com
. It is not allocated by a social media company [like facebook.com/alice]. Rather, her handle is
the
 universal “internet handle”, i.e. a domain. Alice
owns
 the
alice.com
 domain, so she can
use it as a handle
 on any open social app. (On most open social apps, she goes by
@alice.com
, but for others she wants a distinct disconnected identity, so she owns another handle she’d rather not share.)
Bob owns a domain too, even though he isn’t technical. He might not even know what a “domain” is. Bob just thinks of
@bob.com
 as his “internet handle”. Some open social apps will offer you a free subdomain on registration, just like Gmail gives you a free Gmail address, or may offer an extra flow for buying a domain. You’re not locked into your first choice, and can swap to a different domain later.
(...) With open social, Alice’s data—her posts, likes, follows, etc—
is
 hosted on the web itself. Alongside her personal site, Alice now has a
personal repository
 of her data.

This new paradigm is made technically possible by what the AT protocol refers to as aPersonal Data Serveror PDS for short (what Solid calls aPod).

The notion of a 'PDS' quickly comes off as something very technical and nerdy which is why it's not mentioned once in Dan's explainer, even though it's still targeted at an audience ofweb nerds. But really the only obscure word here is theServer, which in this context is interchangeable withStorage, as in Personal Data Storage.

Even regular internet users have some mental model of what personalized data storage entails, especially with the complementary framing ofcollectively owned and operateddata storage.

## Data-banking Coops

If you're a regular internet user the PDS paradigm won't move your data from the cloud to your personal computer. Most people will still rely on an institutional cloud service, but instead of data-banking with a shareholder-controlled corporation most people’s data can be entrusted to the equivalent of member-ownedcredit unionsfor data storage.

Source:
https://ide.mit.edu/sites/default/files/publications/Data-Cooperatives-final.pdf

One in every three US adults banks with a Credit Union. Achieving similar or better numbers for data storage is far from inconceivable considering how much our collective experience with Big Banking mirrors that of Big Tech/Social.

The concept ofdata cooperativeshas already gained a lot of traction in the fediverse with several providers likesocial.coop,data.coopandcosocial.cabeing operational for many years and still going strong. Soon the AT network will have a similarly co-owned institution inNorthsky.

Whether these providers are strictly cooperatives in the formal sense isn't what's most important here though; any suffuciently transparent, democratic and community-oriented data bank (like the aforementioned Blacksky, or the forthcoming Eurosky) is a valid steward and co-creator of an Open Social.

Data Ownership as a conversation changes when data resides primarily with people-governed institutions rather than corporations. Rather than arguing for what kinds of data weought to beable to download from the corporate silos, the platforms should be asking us what kinds of data they may copy fromour servers, and only with strictly temporary allowances.

And while the separation of user data and social platform is most fully realized today in the AT network, there are exciting signs ofcross-pollination happeningin the ongoing development of atproto’s predecessorActivityPub. I hope to see similar openness towards technological convergence in Solid for a morepluralistic social web.

Personal Data Storage has long since escaped containment as a concept pertaining to any specific protocol. Some implementations of it will be more mainstream than others, but pragmatic data coops can be protocol-agnostic and storage formats are transmutable.

As long as we have sufficient control of our own data there will always be a way to restart our social graph and digital presence elsewhere in the event of platform collapse. Let’s make the web personal again.

See also:

Be A Property Owner And Not A Renter On The Internet · Den Delimarsky
The year is 2025. The internet in the shape that we’ve known it in the early 2000s is no longer there. Or, not quite in the shape that we’ve seen it before. This is not just plain nostalgia talking - the vibrant ecosystem of blogs, feeds, personal sites, and forums has been usurped by a few mega-con…
Den Delimarsky
Digital Homeownership
You deserve a home on the World Wide Web that’s built to keep you safe; a magical place for virtual living that‘s yours for life, existing in a sociable web.
Muni Blog
Erlend Sogge Heggen
Avoiding Walled Gardens on the Internet
I occasionally get requests to join private social networking sites, like LinkedIn or Facebook. I always politely decline. I understand the appeal of private social networking, and I mean no disrespect to the people who send invites. But it’s just not for me. I feel very strongly that we
Coding Horror
Jeff Atwood

### You might also like...

 Jun


 07


## Company as a Commons



 10 min read




 Dec


 05


## Weird inc.



 14 min read
