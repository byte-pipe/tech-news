---
title: 'Tell HN: Azure outage | Hacker News'
url: https://news.ycombinator.com/item?id=45748661
site_name: hackernews
fetched_at: '2025-10-30T11:08:59.842013'
original_url: https://news.ycombinator.com/item?id=45748661
author: tartieret
date: '2025-10-30'
---

Hacker News
new
 |
past
 |
comments
 |
ask
 |
show
 |
jobs
 |
submit
login
Tell HN: Azure outage
793 points
 by
tartieret

18 hours ago

 |
hide
 |
past
 |
favorite
 |
733 comments
Azure is down for us, we can't even access the azure portal. Are other experiencing this? Our services are located in Canada/Central and US-East 2

https://downdetector.ca/status/windows-azure/https://azure.status.microsoft/en-gb/status

croemer

5 hours ago

 |
next

[–]

Preliminary post incident review:
https://azure.status.microsoft/en-gb/status/history/

Timeline15:45 UTC on 29 October 2025 – Customer impact began.16:04 UTC on 29 October 2025 – Investigation commenced following monitoring alerts being triggered.16:15 UTC on 29 October 2025 – We began the investigation and started to examine configuration changes within AFD.16:18 UTC on 29 October 2025 – Initial communication posted to our public status page.16:20 UTC on 29 October 2025 – Targeted communications to impacted customers sent to Azure Service Health.17:26 UTC on 29 October 2025 – Azure portal failed away from Azure Front Door.17:30 UTC on 29 October 2025 – We blocked all new customer configuration changes to prevent further impact.17:40 UTC on 29 October 2025 – We initiated the deployment of our ‘last known good’ configuration.18:30 UTC on 29 October 2025 – We started to push the fixed configuration globally.18:45 UTC on 29 October 2025 – Manual recovery of nodes commenced while gradual routing of traffic to healthy nodes began after the fixed configuration was pushed globally.23:15 UTC on 29 October 2025 - PowerApps mitigation of dependency, and customers confirm mitigation.00:05 UTC on 30 October 2025 – AFD impact confirmed mitigated for customers.

reply

xnorswap

3 hours ago

 |
parent
 |
next

[–]

33 minutes from impact to status page for a complete outage is a joke.

reply

neya

2 hours ago

 |
root
 |
parent
 |
next

[–]

In Microsoft's defense, Azure has always been a complete joke. It's extremely developer unfriendly, buggy and overpriced.

reply

michaelt

2 hours ago

 |
root
 |
parent
 |
next

[–]

If you call that defending microsoft, I'd hate to see what attacking them looks like :)

reply

dijit

1 hour ago

 |
root
 |
parent
 |
next

[–]

Not to put too fine a point on it, but if I have a dark passenger in my tech life it is almost entirely caused by what Microsoft wants to inflict on humanity - and more importantly; how successful they are at doing it.

reply

amelius

25 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

In commenter's defense, their comment makes no sense.

reply

dude250711

1 hour ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Save it for when they stick Copilot into Azure portal.

reply

alias_neo

1 hour ago

 |
root
 |
parent
 |
next

[–]

Ha, you haven't used it recently have you? Copilot is already there, and it can't do a single useful thing.

Me: "How do I connect [X] to [Y] using [Z]?"Copilot: "Please select the AKS cluster you'd like to delete"

reply

nflekkhnnn

24 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Actually one of the inventors of k8s was the project lead for copilot in the azure portal, and deployed it over a year ago.

reply

antonvdi

1 hour ago

 |
root
 |
parent
 |
prev
 |
next

[–]

They're already doing that.

reply

madjam002

1 hour ago

 |
root
 |
parent
 |
prev
 |
next

[–]

My favourite was the Azure CTO complaining that Git was unintuitive, clunky and difficult to use

reply

macintux

1 hour ago

 |
root
 |
parent
 |
next

[–]

Isn’t it?

reply

Hilift

1 hour ago

 |
root
 |
parent
 |
next

[–]

Ironically, the GitHub Desktop Windows app is quite nice.

reply

dspillett

36 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Yes. But the point is compared to Azure in places the statement was very much the pot commenting on the kettles sooty arse. And git makes no particular pretence to be particularly friendly, just that it does a particular job efficiently.

reply

sfn42

1 hour ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I've only used Azure, to me it seems fine ish. Some things are rather overcomplicated and it's far from perfect but I assumed the other providers were similarly complicated and imperfect.

Can't say I've experienced many bugs in there either. It definitely is overpriced but I assume they all are?

reply

imglorp

27 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

That's about how long it took to bubble up three levels of management and then go past the PR and legal teams for approvals.

reply

infaloda

2 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

More importantly
`15:45 UTC on 29 October 2025 – Customer impact began.

16:04 UTC on 29 October 2025 – Investigation commenced following monitoring alerts being triggered.
`
A 19-minute delay in alert is a joke.

reply

sbergot

2 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

and for a while the status was "there might be issues on azure portal".

reply

ambentzen

1 hour ago

 |
root
 |
parent
 |
next

[–]

There might have been, but they didn't know because they couldn't access it. Could have been something totally unrelated.

reply

onionisafruit

5 hours ago

 |
parent
 |
prev
 |
next

[–]

At 16:04 “Investigation commenced”. Then at 16:15 “We began the investigation”. Which is it?

reply

ssss11

3 hours ago

 |
root
 |
parent
 |
next

[–]

Quick coffee run before we get stuck in mate

reply

ozim

2 hours ago

 |
root
 |
parent
 |
next

[–]

Load some carbs with chocolate chip cookies as well, that’s what I would do.

You don’t want to debug stuff with low sugar.

reply

normie3000

4 minutes ago

 |
root
 |
parent
 |
next

[–]

One crash after another

reply

not_a_bot_4sho

4 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I read it as the second investigation being specific to AFD. The first more general.

reply

mystcb

18 hours ago

 |
prev
 |
next

[–]

Update 16:57 UTC:

Azure Portal Access IssuesStarting at approximately 16:00 UTC, we began experiencing Azure Front Door issues resulting in a loss of availability of some services. In addition. customers may experience issues accessing the Azure Portal. Customers can attempt to use programmatic methods (PowerShell, CLI, etc.) to access/utilize resources if they are unable to access the portal directly. We have failed the portal away from Azure Front Door (AFD) to attempt to mitigate the portal access issues and are continuing to assess the situation.We are actively assessing failover options of internal services from our AFD infrastructure. Our investigation into the contributing factors and additional recovery workstreams continues. More information will be provided within 60 minutes or sooner.This message was last updated at 16:57 UTC on 29 October 2025---Update: 16:35 UTC:Azure Portal Access IssuesStarting at approximately 16:00 UTC, we began experiencing DNS issues resulting in availability degradation of some services. Customers may experience issues accessing the Azure Portal. We have taken action that is expected to address the portal access issues here shortly. We are actively investigating the underlying issue and additional mitigation actions. More information will be provided within 60 minutes or sooner.This message was last updated at 16:35 UTC on 29 October 2025---Azure Portal Access IssuesWe are investigating an issue with the Azure Portal where customers may be experiencing issues accessing the portal. More information will be provided shortly.This message was last updated at 16:18 UTC on 29 October 2025---Message from the Azure Status Page:https://azure.status.microsoft/en-gb/status

reply

planewave

17 hours ago

 |
parent
 |
next

[–]

Azure Network Availability Issues

Starting at approximately 16:00 UTC, we began experiencing Azure Front Door issues resulting in a loss of availability of some services. We suspect that an inadvertent configuration change as the trigger event for this issue. We are taking two concurrent actions where we are blocking all changes to the AFD services and at the same time rolling back to our last known good state.We have failed the portal away from Azure Front Door (AFD) to mitigate the portal access issues. Customers should be able to access the Azure management portal directly.We do not have an ETA for when the rollback will be completed, but we will update this communication within 30 minutes or when we have an update.This message was last updated at 17:17 UTC on 29 October 2025

reply

croemer

16 hours ago

 |
root
 |
parent
 |
next

[–]

"We have initiated the deployment of our 'last known good' configuration. This is expected to be fully deployed in about 30 minutes from which point customers will start to see initial signs of recovery. Once this is completed, the next stage is to start to recover nodes while we route traffic through these healthy nodes."

"This message was last updated at 18:11 UTC on 29 October 2025"

reply

croemer

14 hours ago

 |
root
 |
parent
 |
next

[–]

At this stage, we anticipate full mitigation within the next four hours as we continue to recover nodes. This means we expect recovery to happen by 23:20 UTC on 29 October 2025. We will provide another update on our progress within two hours, or sooner if warranted.

This message was last updated at 19:57 UTC on 29 October 2025

reply

cyptus

17 hours ago

 |
parent
 |
prev
 |
next

[–]

AFD is down quite often regionally in Europe for our services. In 50%+ the cases they just don‘t report it anywhere, even if its for 2h+.

reply

RajT88

17 hours ago

 |
root
 |
parent
 |
next

[–]

Spam those Azure tickets. If you have a CSAM, build them a nice powerpoint telling the story of all your AFD issues (that's what they are there for).

> In 50%+ the cases they just don‘t report it anywhere, even if its for 2h+.I assume you mean publicly. Are you getting the service health alerts?

reply

tomashubelbauer

17 hours ago

 |
root
 |
parent
 |
next

[–]

CSAM apparently also means Customer Success Account Manager for those who might have gotten startled by this message like me.

reply

ifwinterco

14 hours ago

 |
root
 |
parent
 |
next

[–]

Alternative für Deutschland was strange enough, when I saw CSAM I was really wondering what thread I had stumbled into

reply

cyptus

4 hours ago

 |
root
 |
parent
 |
next

[–]

haha :D

reply

linohh

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Thank you, not going to google that shit.

reply

andrewinardeer

15 hours ago

 |
root
 |
parent
 |
next

[–]

"Apply to become a CSAM mentor"

reply

alias_neo

1 hour ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Where do these alerts supposedly come from? I started having issues around 4PM (GMT), couldn't access portal, and couldn't make AKV requests from the CLI, and initially asked our Ops guys but with no info and a vague "There may be issues with Portal" on their status page, that was me done for the day.

reply

psunavy03

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Some really unfortunate acronyms flying around the Microsoft ecosystem . . .

reply

RajT88

17 hours ago

 |
root
 |
parent
 |
next

[–]

Quite so. The acronym collision rate is high.

reply

riffic

16 hours ago

 |
root
 |
parent
 |
next

[–]

In general, plain language works so much better than throwing bowls of alphabet soup around.

reply

RajT88

16 hours ago

 |
root
 |
parent
 |
next

[–]

That's a funny criticism to make on a tech forum.

But, for future reference:site:microsoft.com csam

reply

Noumenon72

11 hours ago

 |
root
 |
parent
 |
next

[–]

That's an even 5:5 split between both meanings.

reply

nijave

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Back when we used Azure the only outcome was them trying to upsell us on Premium Support

reply

cyptus

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

in many cases: no service health alerts, no status page updates and no confirmations from the support team in tickets.
still we can confirm these issues from different customers accross europe. Mostly the issues are regional dependent.

reply

llama052

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I got a service health alert an hour after it started, saying the portal was having issues. Pretty useless and misleading.

reply

RajT88

17 hours ago

 |
root
 |
parent
 |
next

[–]

That should go into the presentation you provide your CSAM with as well.

Storytelling is how issues get addressed. Help the CSAM tell the story to the higher ups.

reply

cyberax

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> CSAM

Child Sex-Abuse Material?!? Well, a nice case of acronym collision.

reply

mirekrusin

16 hours ago

 |
root
 |
parent
 |
next

[–]

They should rename to Success Customer Account Manager.

reply

tanseydavid

13 hours ago

 |
root
 |
parent
 |
next

[–]

>> They should rename to Success Customer Account Manager.

No -- the one referencing crime should NEVER have be turned into an acronym.Crimes should not be described in euphemistic terms (which is exactly what the acronym is)

reply

rightbyte

1 hour ago

 |
root
 |
parent
 |
next

[–]

You could argue "pornography" is the euphemism?

reply

xp84

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Most companies just call 'em CSMs

reply

pndy

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Supervisor Customer Account Manager: a remote kind of job, paid occasionally with gift cards

reply

mirekrusin

14 hours ago

 |
root
 |
parent
 |
next

[–]

...performed by cheap, open weight LLM.

reply

RajT88

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Definitely the most baffling acronym collision I have seen with Microsoft. I did one time count 4 different products abbreviated VSTS at one point.

reply

dotancohen

11 hours ago

 |
root
 |
parent
 |
next

[–]

Didn't MS have three things called "link" at one time? They were all spelled differently, of course.

reply

SAI_Peregrinus

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

They must really depend on their government contracts with this administration…

reply

codeduck

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Oh dear. Will make for an awkward thing to have on your resume.

reply

senderista

13 hours ago

 |
root
 |
parent
 |
next

[–]

"CSAM Ninja"

reply

zemariagp

5 hours ago

 |
root
 |
parent
 |
next

[–]

Wait till you hear about the Keen Kubernetes Knowledge iniciative

reply

nevf1

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

This is the single most frustrating thing about these incidents. As you're harmstrung on what you can do or how you can react until Microsoft officially acknowledges a problem. Took nearly 90mins both today and when it happened on 9th October.

reply

cyptus

16 hours ago

 |
root
 |
parent
 |
next

[–]

so true. instead of getting a fast feedback we are wasting time searching for our own issues first.

reply

hallh

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Same experience. We've recently migrated fully away from AFD due to how unreliable it is.

reply

jjp

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Whilst the status message acknowledge's the issue with Front Door (AFD), it seems as though the rest of the actions are about how to get Portal/internal services working without relying on AFD. For those of us using Front Door does that mean we're in for a long haul?

reply

progmetaldev

13 hours ago

 |
root
 |
parent
 |
next

[–]

Currently even the Front Door landing page is only partially loading.

https://azure.microsoft.com/en-us/products/frontdoor

reply

llama052

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Please migrate off of front door. It's been a failure mode since it came out historically. Anything else is better at this point

reply

everfrustrated

17 hours ago

 |
root
 |
parent
 |
next

[–]

Didn't the underlying vendor they used for Azure Front Door go bankrupt? It's probably on life support.

reply

guptadagger

9 hours ago

 |
root
 |
parent
 |
next

[–]

i understood that to be a different third party that provided a CDN and was different than afd.
https://learn.microsoft.com/en-us/azure/frontdoor/migrate-cd...

reply

8cvor6j844qw_d6

18 hours ago

 |
parent
 |
prev
 |
next

[–]

I'll be interested in the incident writeup since DNS is mentioned. It will be interesting in a way if it is similar to what happened at AWS.

reply

Insanity

18 hours ago

 |
root
 |
parent
 |
next

[–]

It's pretty unlikely. AWS published a public 'RCA'
https://aws.amazon.com/message/101925/
. A race condition in a DNS 'record allocator' causing all DNS records for DDB to be wiped out.

I'm simplifying a bit, but I don't think it's likely that Azure has a similar race condition wiping out DNS records on _one_ system than then propagates to all others. The similarity might just end at "it was DNS".

reply

parliament32

18 hours ago

 |
root
 |
parent
 |
next

[–]

That RCA was fun. A distributed system with members that don't know about each other, don't bother with leader elections, and basically all stomp all over each other updating the records. It "worked fine" until one of the members had slightly increased latency and everything cascade-failed down from there. I'm sure there was missing (internal) context but it did not sound like a well-architected system at all.

reply

nijave

12 hours ago

 |
root
 |
parent
 |
next

[–]

>slightly increased latency

They didn't provide any details on latency. It could have been delayed an hour or a day and no one noticed

reply

RajT88

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Needs STONITH

reply

kyrra

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

https://isitdns.com/

reply

cdr420

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It's always DNS

reply

tempest_

16 hours ago

 |
root
 |
parent
 |
next

[–]

It is a coin flip, heads DNS, tails BGP

reply

r_lee

15 hours ago

 |
root
 |
parent
 |
next

[–]

THIS is the real deal. Some say it's always DNS but many times it's some routing fuckup with BGP. two most cursed 3 letter acronym technologies out there

reply

chasd00

15 hours ago

 |
root
 |
parent
 |
next

[–]

when a service goes down it's DNS when an entire nation or group of nations vanish it's BGP.

reply

layer8

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

DNS has both naming and cache invalidation, so no surprise it’s among the hardest things to get right. ;)

reply

dotancohen

11 hours ago

 |
root
 |
parent
 |
next

[–]

That's three of the hardest problems in CS ))

reply

jdc0589

18 hours ago

 |
parent
 |
prev
 |
next

[–]

yea its not just the portal. microsoft.com is down too

reply

mystcb

18 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah, I am guessing it's just a placeholder till they get more info. I thought I saw somewhere that internally within Microsoft it's seen as a "Sev 1" with "all hands on deck" - Annoyingly I can't remember where I saw it, so if someone spots it before I do, please credit that person :D

Edit: Typo!

reply

verst

15 hours ago

 |
root
 |
parent
 |
next

[–]

It's a Sev 0 actually (as one would expect - this isn't a big secret). I was on the engineering bridge call earlier for a bit.
The Azure service I work on was minimally impacted (our customer facing dashboard could not load, but APIs and data layer were not impacted) but we found a workaround.

reply

chad_c

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It was here
https://news.ycombinator.com/item?id=45749054
 but that comment has been deleted.

reply

PeterCorless

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Seems all Microsoft-related domains are impacted in some way.

•https://www.xbox.com/en-USalso doesn't fully paint. Header comes up, but not the rest of the page.•https://www.minecraft.net/en-usis extremely slow, but eventually came up.

reply

daxfohl

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Downdetector says aws and gcp are down too. Might be in for a fun day.

reply

rozenmd

18 hours ago

 |
root
 |
parent
 |
next

[–]

From what I can tell, Downdetector just tracks traffic to their pages without actually checking if the site is down.

The other day during the AWS outage they "reported" OVH down too.

reply

jdc0589

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

yea I saw that, but im not sure on how accurate that is. a few large apps/companies I know to be 100% on AWS in us-east-1 are cranking along just fine.

reply

linhns

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Not sure if this is true. I just login to the console with no glitch.

reply

NetMageSCW

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

AWS was performance issues and I believe is resolved.

reply

bossyTeacher

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It sure must be embarrassing for the website of the second richest company in the world to be down.

reply

planewave

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

yes, and it seems that at least for some login.microsoftonline.com is down too, which is part of the Entra login / SSO flow.

reply

jonathanlydall

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Yet another reason to move away from Front Door.

We already had to do it for large files served from Blob Storage since they would cap out at 2MB/s when not in cache of the nearest PoP. If you’ve ever experienced slow Windows Store or Xbox downloads it’s probably the same problem.I had a support ticket open for months about this and in the end the agent said “this is to be expected and we don’t plan on doing anything about it”.We’ve moved to Cloudflare and not only is the performance great, but it costs less.Only thing I need to move off Front Door is a static website for our docs served from Blob Storage, this incident will make us do it sooner rather than later.

reply

out_sider

17 hours ago

 |
root
 |
parent
 |
next

[–]

we are considering the same but because our website uses APEX domain we would need to move all DNS resolver to cloudfront right ? Does it have as a nice "rule set builder" as azure ?

reply

jonathanlydall

17 hours ago

 |
root
 |
parent
 |
next

[–]

Unless you pay for CloudFlare’s Enterpise plan, you’re required to have them host your DNS zone, you can use a different registrar as long as you just point your NS records to Cloudflare.

Be aware that if you’re using Azure as your registrar, it’s (probably still) impossible to change your NS records to point to CloudFlare’s DNS server, at least it was for me about 6 months ago.This also makes it impossible to transfer your domain to them either, as CloudFlare’s domain transfer flow requires you set your NS records to point to them before their interface shows a transfer option.In our case we had to transfer to a different registrar, we used Namecheap.However, transferring a domain from Azure was also a nightmare. Their UI doesn’t have any kind of transfer option, I eventually found an obscure document (not on their Learn website) which had an az command which would let you get a transfer code which I could give to Namecheap.Then I had to wait over a week for the transfer timeout to occur because there is no way on Azure side that I could find to accept the transfer immediately.I found CloudFlare’s way of building rules quite easy to use, different from Front Door but I’m not doing anything more complex than some redirects and reverse proxying.I will say that Cloudflare’s UI is super fast, with Front Door I always found it painfully slow when trying to do any kind of configuration.Cloudflare also doesn’t have the problem that Front Door has where it requires a manual process every 6 months or so to renew the APEX certificate.

reply

out_sider

17 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks :). We don't use Azure as our registrar. It seems I'll have to plan for this then, we also had another issue, AFD has a hard 500ms tls handshake timeout (doesn't matter how much you put on the origin timeout settings) which means if our server was slow for some reason we would get 504 origin timeout.

reply

Figs

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

CloudFlare != CloudFront

reply

out_sider

16 hours ago

 |
root
 |
parent
 |
next

[–]

I meant cloudfare

reply

nosefrog

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Front Door is not good.

reply

NDizzle

16 hours ago

 |
parent
 |
prev
 |
next

[–]

They briefly had a statement about using Traffic Manager to work with your AFD to work around this issue, with a link to learn.microsoft.com/...traffic-manager, and the link didn't work. Due to the same issue affecting everyone right now.

They quickly updated the message to REMOVE the link. Comical at this point.

reply

Aperocky

16 hours ago

 |
root
 |
parent
 |
next

[–]

The statement is still there though on the status page though

reply

NDizzle

15 hours ago

 |
root
 |
parent
 |
next

[–]

They re-added it once the site was accessible.

reply

eddie_catflap

17 hours ago

 |
parent
 |
prev
 |
next

[–]

We saw issues before 16:00 UTC - approx 15:38

reply

ThatManulTheCat

18 hours ago

 |
parent
 |
prev
 |
next

[–]

DNS. Ofc.

reply

rconti

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Sounds like they need to move their portal to a region with more capacity for the desired instance type. /s

reply

Uehreka

18 hours ago

 |
prev
 |
next

[–]

I noticed that Starbucks mobile ordering was down and thought “welp, I guess I’ll order a bagel and coffee on Grubhub”, then GrubHub was down. My next stop was HN to find the common denominator, and y’all did not disappoint.

reply

pants2

18 hours ago

 |
parent
 |
next

[–]

Good thing HN is hosted on a couple servers in a basement. Much more reliable than cloud, it seems!

reply

dang

17 hours ago

 |
root
 |
parent
 |
next

[–]

Just don't use genetically identical hardware:

https://news.ycombinator.com/item?id=32031639https://news.ycombinator.com/item?id=32032235Edit: wow, I can't believe we hadn't puthttps://news.ycombinator.com/item?id=32031243inhttps://news.ycombinator.com/highlights. Fixed now.

reply

hinkley

14 hours ago

 |
root
 |
parent
 |
next

[–]

I’ve seen this up close twice and I’m surprised it’s only twice. Between March and September one year, 6 people on one team had to get new hard drives in their thinkpads and rebuild their systems. All from the same PO but doled out over the course of a project rampup. That was the first project where the onboarding docs were really really good, since we got a lot of practice in a short period of time.

Long before that, the first raid array anyone set up for my (teams’) usage, arrived from Sun with 2 dead drives out of 10. They RMA’d us 2 more drives and one of those was also DOA. That was a couple years after Sun stopped burning in hardware for cost savings, which maybe wasn’t that much of a savings all things considered.

reply

gogusrl

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I got burnt by this bug on freakin' Christmas Eve 2020 (
https://forum.hddguru.com/viewtopic.php?f=10&t=40766
 ). There was some data loss and a lot of lessons learned.

reply

airstrike

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I love that "Ask HN: What'd you do while HN was down?" was a thing

reply

praccu

8 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Many years ago (13?), I was around when Amazon moved SABLE from RAM to SSDs. A whole rack came from a single batch, and something like 128 disks went out at once.

I was an intern but everyone seemed very stressed.

reply

lysace

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It was on AWS at least (for a while) in 2022.

https://news.ycombinator.com/item?id=32030400

reply

jjice

17 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah looks like they're back on M5.

dang saying it's temporary:https://news.ycombinator.com/item?id=32031136$ dig news.ycombinator.com

 ; <<>> DiG 9.10.6 <<>> news.ycombinator.com
 ;; global options: +cmd
 ;; Got answer:
 ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 54819
 ;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

 ;; OPT PSEUDOSECTION:
 ; EDNS: version: 0, flags:; udp: 512
 ;; QUESTION SECTION:
 ;news.ycombinator.com. IN A

 ;; ANSWER SECTION:
 news.ycombinator.com. 1 IN A 209.216.230.207

 ;; Query time: 79 msec
 ;; SERVER: 100.100.100.100#53(100.100.100.100)
 ;; WHEN: Wed Oct 29 13:59:29 EDT 2025
 ;; MSG SIZE rcvd: 65And that IP says it's with M5 again.

reply

parliament32

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Always has been.

reply

Havoc

13 hours ago

 |
parent
 |
prev
 |
next

[–]

The sysadmin subreddit tends to beat hn on outage reports by an hour+ in my experience.

Bunch of on-call peeps over there that definitely know the instant something major goes down

reply

hypeatei

18 hours ago

 |
parent
 |
prev
 |
next

[–]

Starbucks mobile was down during the AWS outage too...

reply

SoftTalker

18 hours ago

 |
root
 |
parent
 |
next

[–]

They are multi-cloud --- vulnerable to
all
 outages!

reply

mring33621

17 hours ago

 |
root
 |
parent
 |
next

[–]

you wouldn't believe some of the crap enterprise bigco mgmt put in place for disaster recovery.

they think that they are 'eliminating a single point of failure', but in reality, they end up adding multiple, complicated points of mostly failure.

reply

andoma

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Go multi-cloud they said...

reply

Hamuko

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Gonna build my application to be multicloud so that it requires multiple cloud platforms to be online at the same time. The RAID 0 of cloud computing.

reply

sergiotapia

18 hours ago

 |
parent
 |
prev
 |
next

[–]

Wow I just left a Starbucks drivethru line because it was just not moving. I guess it was because of this.

reply

iso1631

15 hours ago

 |
root
 |
parent
 |
next

[–]

You'd think that Starbucks execs would be held accountable for the fragile system they have put in place.

But they won't be.

reply

peanut-walrus

14 hours ago

 |
root
 |
parent
 |
next

[–]

Why? Starbucks is not providing a critical service. Spending less money and resources and just accepting the risk that occasionally you won't be able to sell coffee for a few hours is a completely valid decision from both management and engineering pov.

reply

iso1631

29 minutes ago

 |
root
 |
parent
 |
next

[–]

If I were a Starbucks shareholder I wouldn't be happy that my company is throwing away revenue because of the CTO's decision to outsource accountability

Time and time again it's shown that AWS is far more expensive than other solutions, just easier for the Execs to offshore the blame.

reply

bobro

5 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Or maybe we should throw them in jail.

reply

DaSHacka

2 hours ago

 |
root
 |
parent
 |
next

[–]

I agree, but because the coffee is crap

reply

munchlax

2 hours ago

 |
root
 |
parent
 |
next

[–]

And ridiculously expensive

reply

bombcar

1 hour ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It's absolutely batshit that an in-person transaction with cash becomes
impossible
 when the computers are down.

I've seen it multiple times at various stores; only once did I see them taking cash and writing things down (probably to enter into the system later when it came back up).

reply

01284a7e

16 hours ago

 |
parent
 |
prev
 |
next

[–]

Ha, maybe rethink the I AM NOTHING BUT A HUGE CLOUD CONSUMER thing on some fundamental levels? Like food?

reply

port11

14 hours ago

 |
parent
 |
prev
 |
next

[–]

I noticed it when my Netatmo rigamajig stopped notifying me of bad indoor air quality. Lovely. Why does it need to go through the cloud if the data is right there in the home network…

reply

garbagewoman

3 hours ago

 |
parent
 |
prev
 |
next

[–]

Service culture is so hollow

reply

Theodores

15 hours ago

 |
parent
 |
prev
 |
next

[–]

My inner Nelson-from-the-Simpsons wishes I was on your team today, able to flaunt my flask of tea and homemade packed sandwiches. I would tease you by saying 'ha ha!' as your efforts to order coffee with IP packets failed.

I always go everywhere adequately prepared for beverages and food. Thanks to your comment, I have a new reason to do so. Take out coffees are actually far from guaranteed. Payment systems could go down, my bank account could be hacked or maybe the coffee shop could be randomly closed. Heck, I might even have an accident crossing the road. Anything could happen. Hence, my humble flask might not have the top beverage in it but at least it works.We all design systems with redundancy, backups and whatnot, but few of us apply this thinking to our food and drink. Maybe get a kettle for the office and a backup kettle, in case the first one fails?

reply

jeffrallen

14 hours ago

 |
parent
 |
prev
 |
next

[–]

You know you can talk to your barista and ask for a bagel, right? If you're lucky they still take cash... if you still _have_ cash. :)

reply

0_____0

8 hours ago

 |
root
 |
parent
 |
next

[–]

I was at a McDs a couple months back and I'm pretty sure you
had
 to use the kiosk to order. Some places are deprecating the cashier entirely.

reply

sherinjosephroy

18 minutes ago

 |
prev
 |
next

[–]

Yep, even massive cloud providers slip up. Reminds me that depending on “someone else’s infrastructure” still means losing access when things go sideways.

reply

foresterre

15 hours ago

 |
prev
 |
next

[–]

It still surprises me how much essential services like public transport are completely reliant on cloud providers, and don't seem to have backups in place.

Here in The Netherlands, almost all trains were first delayed significantly, and then cancelled for a few hours because of this, which had real impact because today is also the day we got to vote for the next parlement (I know some who can't get home in time before the polls close, and they left for work before they opened).

reply

conductr

15 hours ago

 |
parent
 |
next

[–]

Is voting there a one day only event? If not, I feel the solution to that particular problem is quite clear. There’s a million things that could go wrong causing you to miss something when you try to do it in a narrow time range (today after work before polls close)

If it’s a multi day event, it’s probably that way for a reason. Partially the same as the solution to above.

reply

DontBreakAlex

15 hours ago

 |
root
 |
parent
 |
next

[–]

In europe, voting typically happens in one day, where everyone physically goes to their designated voting place and puts papers in a transparent box. You can stay there and wait for the count at the end of the day if you want to. Tom Scott has a very good video about why we don't want electronic/mail voting:
https://www.youtube.com/watch?v=w3_0x6oaDmI

reply

w3ll_w3ll_w3ll

4 hours ago

 |
root
 |
parent
 |
next

[–]

In Italy we typically vote for two days, usually Sunday and Monday or Saturday and Sunday.

reply

tempestn

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Electronic voting and mail voting are very different things though.

reply

vasco

13 hours ago

 |
root
 |
parent
 |
next

[–]

They both share the fact that you don't see your vote enter a ballot box.

reply

vincnetas

58 minutes ago

 |
root
 |
parent
 |
next

[–]

With proper mail voting you have a way to verify that your mailed in vote is counted.

(AI generated explanation)
How the double-envelope system worksInner “secrecy” envelopeYou mark your ballot, fold it, and slip it into an unmarked inner envelope.
No name or identifying info is on this envelope, so your choices stay anonymous.
Outer declaration envelopeThe inner envelope goes inside a larger outer envelope that carries:
– A ballot ID/barcode unique to you.
– A signature line that must match the one on file with your election office.
In many states, a detachable privacy flap or perforated strip hides the signature until election officials open the outer envelope, keeping the ballot secret.

reply

samtp

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Well "mail in voting" in Washington state pretty much means you drop off your ballot in a drop box in your neighborhood. Which is pretty much the same thing as putting it in a ballot box.

reply

_heimdall

9 hours ago

 |
root
 |
parent
 |
next

[–]

How is that the same?

The description of voting in the Netherlands is that you can see your ballot physically go into a clear box and stay to see that exact box be opened and all ballots tallied.Dropping a ballot in a box in tour neighborhood helps ensure nothing with regards to the actually ballot count.

reply

maxdamantus

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Here in NZ when I've been to vote, there are usually a couple of party affiliates at the voting location, doing what one of the parent posts described:

> You can stay there and wait for the count at the end of the day if you want to.And if you watch the election night news, you'll see footage of multiple people counting the votes from the ballot boxes, again with various people observing to check that nothing dodgy is going on.Having everyone just put their ballots in a postbox seems like a good way remove public trust from the electoral system, because noone's standing around waiting for the postie to collect the mail, or looking at what happens in the mail truck, or the rest of the mail distribution process.I'm sure I've seen reports in the US of people burning postboxes around election time. Things like this give more excuses to treat election results as illegitimate, which I believe has been an issue over there.(Yes, we do also have advanced voting in NZ, but I think they're considered "special votes" and are counted separately .. the elections are largely determined on the day by in-person votes, with the special votes being confirmed some days later)

reply

arsome

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

One of these things is much easier to burn or otherwise tamper with.

reply

trevoragilbert

12 hours ago

 |
root
 |
parent
 |
next

[–]

You should research what’s inside the boxes in Oregon before just assuming they’re easier to tamper with.

reply

maxdamantus

12 hours ago

 |
root
 |
parent
 |
next

[–]

Doesn't look difficult:
https://www.fbi.gov/wanted/seeking-info/ballot-box-fires

(yes, that's in Oregon)

reply

bee_rider

7 hours ago

 |
root
 |
parent
 |
next

[–]

I’m not sure what’s so special in Oregon’s ballot boxes. But, tampering that is detected (don’t need much special to detect a burning box I guess!) is not a complete failure for a system. If any elections were close enough for a box to matter, they could have rerun them.

reply

belorn

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

In Sweden, mail/early votes get sent through the postal system to the official ballot box for those votes. In 2018, a local election had to be redone because the post delivered votes late. Mail delivery occasionally have packaged delayed or lost, and votes are note immune to this problem. In one case the post also gave the votes to an unauthorized person, through the votes did end up at the right place.

It is a small but distinct difference between mail/early voting and putting the votes directly into the ballot box.

reply

edoceo

6 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Is it possible to trace your own vote after? There has to be a technical solution to ensure that your own vote was counted

reply

vincnetas

57 minutes ago

 |
root
 |
parent
 |
next

[–]

yes there is. Check double envelope mail in voting mechanics.

reply

heroic

6 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

In India we have electronic voting and we get to see our vote going in the ballot box.

reply

vasco

4 hours ago

 |
root
 |
parent
 |
next

[–]

You can see electrons or what do you mean?

reply

hahajk

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I mail in to Florida and I can log in and see that they received it and it was counted. So, close to seeing it enter the box.

reply

kaashif

9 hours ago

 |
root
 |
parent
 |
next

[–]

That doesn't seem at all like the same thing as literally seeing the ballot enter the box in the presence of observers from all parties.

There's so much more you have to trust.

reply

throwaway7783

9 hours ago

 |
root
 |
parent
 |
next

[–]

Even with ballot boxes you still need to trust what happens after ballot enters the box.

reply

bee_rider

7 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It could be possible to have a system like:

If you wish, you can write a phrase on your ballot. The phrases and their corresponding vote are broadcast (on tv, internet, etc). So if you want to validate that your vote was tallied correctly, write a unique phrase. Or you could pick a random 30 digit number, collisions should be zero-probability, right?I mean, this would be annoying because people would write slurs and advertisements, and the government would have to broadcast them. But, it seems pretty robust.I’d suggest the state handle the number issuing, but then they could record who they issues which numbers to, and the winning party could go about rounding up their opposition, etc.

reply

parliament32

7 hours ago

 |
root
 |
parent
 |
next

[–]

Voting systems require that there be no way to prove that you voted a certain way, otherwise it opens the market for vote-selling.

reply

bee_rider

6 hours ago

 |
root
 |
parent
 |
next

[–]

Hmm, good point.

Googling around a bit, it sounds like there are systems that let you verify that your ballot made it, but not necessarily that it was counted correctly. (For this reason, I guess?)

reply

mulmen

3 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

In Washington you can track your ballot return status:
https://www.sos.wa.gov/elections/data-research/ballot-status...

reply

esseph

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Seeing your ballot drop in a box is no indicator the vote is actually recorded in the grand tally, or what was recorded for your vote.

reply

ceejayoz

12 hours ago

 |
root
 |
parent
 |
next

[–]

My county lets you look up if it was received. You can vote on Election Day in person if they don’t.

reply

kaashif

9 hours ago

 |
root
 |
parent
 |
next

[–]

You have to trust that whole system. Maybe you do, I don't know the details of how any of that works.

When I vote in person, I know all the officials there from various parties are just like...looking at the box for the whole day to make sure everything is counted. It's much easier to understand and trust.

reply

panarky

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

My county sends me a text message when they've counted my ballot.

reply

esseph

6 hours ago

 |
root
 |
parent
 |
next

[–]

My point is, you don't actually know that.

Sure you got a notification! That doesn't mean anything. Even with human counted ballots or electronic ballots.Following the chain of custody from vote to verification, in some way, would be nice.

reply

jampekka

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Many countries in Europe have advance voting.

reply

silversmith

14 hours ago

 |
root
 |
parent
 |
next

[–]

Off the top of my head, I can't think of an EU country that does not have some form of advance voting.

Here in Latvia the "election day" is usually (always?) on weekend, but the polling stations are open for some (and different!) part of every weekday leading up. Something like couple hours on monday morning, couple hours on tuesday evening, couple around midday wednesday, etc. In my opinion, it's a great system. You have to have a pretty convoluted schedule for at least one window not to line up for you.

reply

ndom91

14 hours ago

 |
root
 |
parent
 |
next

[–]

Germany has mail-in voting, not sure if that counts as advanced voting though

reply

generalspecific

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Ireland doesn't have it.

reply

alborzb

13 hours ago

 |
root
 |
parent
 |
next

[–]

That's not true (as somebody who had to do this last year in 2024 because I was traveling in another country for work on election day)

Here is the form to register for postal voting in the Republic of Ireland -https://www.dublincity.ie/sites/default/files/2024-01/pv4-wo...Instructions on how to submit the form / register for mail-in votes is on page 4.Hope that helps anyone else out who needs in Ireland

reply

embedding-shape

12 hours ago

 |
root
 |
parent
 |
next

[–]

I think they meant "don't have it" as in except in special circumstances, and that form says:

> You may use this form to apply for a postal vote if, due to the circumstances of your work/service or your full-time study in the State, you cannot go to your polling station on polling day.Which seems to indicate that's only for people who can't go to the polling station, otherwise you do have to go there.

reply

esperent

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I think that a lot of Ireland's voting practices come from having a small population but a huge diaspora. I imagine the percentage of people living outside Ireland what would be eligible to vote in many other countries is significant enough to effect elections, certainly if they are close.

As someone who spent the first 30 years of my life in Ireland but is now part of that diaspora, it's frustrating but I get it. I don't get to vote, but neither do thousands of plastic paddys who have very little genuine connection to Ireland.That said, I'm sure they could expand the voting window to a couple of days at least without too much issue.

reply

mrighele

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Italy has mail-in vote only for citizen residing abroad. The rest vote on the election Sunday (and Monday morning in some cases, at least in the past).

reply

wodenokoto

6 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

We do mail voting from embassies or consulates when abroad.

reply

ed_elliott_asc

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

UK is a one day affair with voting booths typically open like 6 am to 10 pm

reply

xnorswap

13 hours ago

 |
root
 |
parent
 |
next

[–]

With the option to do a postal vote, or vote-by-proxy.

reply

speakfreely

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Voting seems like one of the few problems that blockchain is actually the solution for.

reply

Sammi

11 hours ago

 |
root
 |
parent
 |
next

[–]

Nope. Blockchain has no anonymity.

reply

ehnto

6 hours ago

 |
root
 |
parent
 |
next

[–]

You don't have to attribute any name to the transaction, just a voting booth ID and the vote. The actual benefit is just that it is hard to tamper and easy to trace where tampering happened.

But I still prefer the paper vote and I usually a blockchain apathetic.

reply

johnsonelephant

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Monero demonstrates a solution (
https://en.wikipedia.org/wiki/Ring_signature
)

reply

fancyswimtime

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

wouldn't that be a feature in this case?

reply

kaibee

10 hours ago

 |
root
 |
parent
 |
next

[–]

Anonymous voting means that you can't sell your vote. Like, if I pay you $5 to vote for X, but I can't actually verify that you voted for X and not Y, then I wouldn't bother trying. Or if I'm your boss and I want you to vote for X... etc.

reply

konimex

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Not really. Your ballot should be secret, which goes against blockchain, I guess.

reply

ehnto

6 hours ago

 |
root
 |
parent
 |
next

[–]

The blockchain doesn't require your ID, just the voting station ID.

reply

klardotsh

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Washington State having full vote-by-mail (there is technically a layer of in-person voting as a fallback for those who need it for accessibility reasons or who missed the registration deadline) has spoiled me rotten, I couldn't imagine having to go back to synchronous on-site voting on a single day like I did in Illinois. Awful. Being able to fill my ballot at my leisure, at home, where I can have all the research material open, and drive it to a ballot drop box whenever is convenient in a 2-3 week window before 20:00 on election night, is a game-changer for democracy. Of course this also means that people who serve to benefit from disenfranchising voters and making it more difficult to vote, absolutely hate our system and continually attack it for one reason or another.

reply

vanviegen

14 hours ago

 |
root
 |
parent
 |
next

[–]

As a Dutchman, I have to go vote in person on a specific day. But to be honest: I really don't mind doing so. If you live in a town or city, there'll usually be multiple voting locations you can choose from within 10 minutes
walking
 distance. I've never experienced waiting times more than a couple of minutes. Opening times are pretty good, from 7:30 til 21:00. The people there are friendly. What's not to like? (Except for some of the candidates maybe, but that's a whole different story. :-))

reply

jfengel

14 hours ago

 |
root
 |
parent
 |
next

[–]

In the US, hours-long lines are routine. Not everywhere, but poorer places tend to have fewer voting machines and longer lines.

We've been closing a lot of polling places recently:https://abcnews.go.com/US/protecting-vote-1-5-election-day-p...

reply

christkv

13 hours ago

 |
root
 |
parent
 |
next

[–]

Voting machines slow down voting from what I understand

reply

vitorgrs

6 hours ago

 |
root
 |
parent
 |
next

[–]

At least in Brazil, that's not the case. You get there to vote, and it doesn't take longer than 5 minutes to leave the place.

reply

jfengel

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Not as much as hanging chads do.

reply

esseph

12 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Have not for me. I mark on a paper ballot that then gets fed into a machine to be recorded. That leaves a paper copy and a digital voting record.

reply

conductr

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

We have early voting, nobody has to wait, they choose to wait

reply

iAMkenough

13 hours ago

 |
root
 |
parent
 |
next

[–]

We're on year five of one of the two parties telling voters to not trust early voting. Their choice is because of the Fear, Uncertainty, and Doubt created by the propaganda they are fed.

Here's the President of the United States on Sunday:https://truthsocial.com/@realDonaldTrump/posts/1154418712892..."No mail-in or 'Early' Voting, Yes to Voter ID! Watch how totally dishonest the California Prop Vote is! Millions of Ballots being 'shipped.' GET SMART REPUBLICANS, BEFORE IT IS TOO LATE!!!"

reply

conductr

13 hours ago

 |
root
 |
parent
 |
next

[–]

That's all happening too, but it's honestly a different topic altogether. We have the ability to vote early. Whether you trust it or politicians are trying to undermine your trust in it, etc.... whole other can of worms

reply

jfengel

12 hours ago

 |
root
 |
parent
 |
next

[–]

Not everyone does. It varies from state to state. Red states in particular have little to no early voting.

reply

tags2k

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You have early voting, some choose not to trust the early voting system.

reply

Sleaker

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Please lookup US voting poll overflow issues that come up every election cycle. Just because you experience a well streamlined process doesn't mean that it's the norm everywhere.

reply

yellow_postit

9 hours ago

 |
root
 |
parent
 |
next

[–]

Don’t forget you can’t dare offer water or food to those stuck in lines else that’s considered tampering in many (all?) locales in the US.

Mail in voting is just better all around for a geographically diverse place as the US and I wish would be adopted by all states.

reply

wyre

8 hours ago

 |
root
 |
parent
 |
next

[–]

Rule of thumb: if Republicans are against it, it’s probably a good thing for everyone else, like mail-in voting.

So excited to see how the right-wing pedants here disagree with this.

reply

vanviegen

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Oh, I know. I'm just saying it
can
 be done properly on a single day. It is a pretty challenging and expensive logistical operation though.

reply

conductr

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

So, if you have a minor emergency, like a kidney stone and hospitalized for the day - you just miss your chance to vote in that election?

If so, I see a lot to dislike. As the point I was making is you can’t anticipate what might come up. Just because it’s worked thus far doesn’t mean it’s designed for resilience. There’s a lot of ways you could miss out in that type of situation. I seems silly to make sure everything else is redundant and fault tolerant in the name of democracy when the democratic process itself isn’t doing the same.

reply

Boltgolt

14 hours ago

 |
root
 |
parent
 |
next

[–]

If hospitalized on that specific day: Sign the back of the voting card and give your ID to a family member, they can cast your vote

reply

conductr

14 hours ago

 |
root
 |
parent
 |
next

[–]

How is that an acceptable response? Honestly. You’re in the hospital, in pain, likely having a minor surgery, and having someone cast your vote for you is going to be on your mind too? Do you have your voting card in your pocket just in case this were to play out?

That’s just ridiculous in my opinion. Makes me wonder how many well intentioned would be voters end up missing out each election cause shit happens and voting is pretty optional

reply

gowld

13 hours ago

 |
root
 |
parent
 |
next

[–]

What percent of the electorate is incapacitated on voting day?

What is the that group's deviation from the general voting population's preferences?What are the margins of the votes on those ballot questions?

reply

conductr

13 hours ago

 |
root
 |
parent
 |
next

[–]

Mild curiosity, no idea whether it would be statistically relevant but asking the question is the first step. If you knew the answer, you might want to extend the voting window even if it wouldn't effect an elections outcome it would be a quantified number of people excluded from the democratic process for simply having bad luck at the wrong time.

reply

mc32

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

If India can have voters vote and tally all the votes in one day, then so can everyone else. It’s the best way to avoid fraud and people going with whoever is ahead. I am sympathetic with emergency protocols for deadly pandemics, but for all else, in-person on a given day.

reply

sampo

13 hours ago

 |
root
 |
parent
 |
next

[–]

> If India can have voters vote and tally all the votes in one day, then so can everyone else.

In most countries, in the elections you vote or the member of parliament you want. Presidential elections, and city council elections are held separately, but are also equally simple. But in one election you cast your vote for one person, and that's it.With this kind of elections, many countries manage to hold the elections on paper ballots, count them all by hand, and publish results by midnight.But on an American ballot, you vote for, for example:- US president
 - US senator
 - US member of congress
 - state governor
 - state senator
 - state member of congress
 - several votes for several different state judge positions
 - several other state officer positions
 - several votes for several local county officers
 - local sheriff
 - local school board member
 - several yes/no votes for several proposed laws, whether they should be passed or notI don't think it would be possible to calculate all these 20 or 40 votes, if calculated by hand. That's why they use voting machines in America.https://ballotpedia.org/Official_sample_ballots,_2020

reply

konimex

10 hours ago

 |
root
 |
parent
 |
next

[–]

Say, how many voting stations are there in a typical city/county in the US?

Here in Indonesia, in a city of 2 million people there are over 7000 voting stations. While we vote for 5 ballots (President, Legislative (National, Province, and City/Regency), we still use paper ballots and count them by hand.

reply

Freedom2

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

How is it not possible? It's just additional votes, there isn't anything actually stopping counting by hand, is there? How was it counted historically without voting machines?

reply

stevenwoo

8 hours ago

 |
root
 |
parent
 |
next

[–]

It takes a lot of people (redundancy and to keep shift hours low to increase count accuracy) to accurately count by hand.
https://verifiedvoting.org/election-system/hand-counted-pape...

reply

Freedom2

6 hours ago

 |
root
 |
parent
 |
next

[–]

That makes it difficult, but the original comment said it wasn't 'possible'. I'm failing to see the impossibility still.

reply

20kleagues

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Voting in India is staggered over multiple phases over multiple days/weeks. Only the vote count happens on a single day at the end.

reply

platevoltage

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

If it's not a national holiday where the vast majority of people don't have to work, and if there aren't polling places reasonably near every voting age citizen, it's voter suppression.

reply

trenchpilgrim

5 hours ago

 |
root
 |
parent
 |
next

[–]

In particular India has a law that no one shall be made to walk more than 2km to vote. The Indian military will literally deploy a voting booth into the jungle so that a single caretaker of an old temple can vote.

reply

Mr_Minderbinder

3 hours ago

 |
parent
 |
prev
 |
next

[–]

Finance is increasingly reliant on it too, my bank moved their entire system to AWS. The amount of power being handed over to these cloud companies in exchange for “convenience” is astonishing.

reply

tuukkah

2 hours ago

 |
parent
 |
prev
 |
next

[–]

Could you provide a reference about the train disruption? I tried but couldn't find anything in English.

reply

foresterre

1 hour ago

 |
root
 |
parent
 |
next

[–]

Here is an article in English:

https://nltimes.nl/2025/10/29/ns-hit-microsoft-cloud-outage-...It should be noted that the article isn't complete: while the travel planner and ticket machines were the first to fail, trains were cancelled soon after; it took a few hours before everything restarted.Based on what the conductors said, I would speculate that the train drivers digital schedule was not operative, so they didn't know where to go next.

reply

tuukkah

37 minutes ago

 |
root
 |
parent
 |
next

[–]

Thanks! Perhaps one of the sites that track train delays can give a statistic?

This list doesn't have anything that looks relevant:https://www.rijdendetreinen.nl/en/disruptions/archive?date_b...The day does not appear as an outlier in the monthly statistics:https://www.rijdendetreinen.nl/en/statistics/2025/10I don't find a detailed statistic on the overall delays, but the per-station statistics for Amsterdam Centraal say 5% of trains were cancelled and 17% were delayed by 5 minutes or more (mostly by 10 minutes):https://www.rijdendetreinen.nl/en/train-archive/2025-10-29/a...

reply

hinkley

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Voting days should be a national holiday.

reply

tmtvl

14 hours ago

 |
root
 |
parent
 |
next

[–]

Here in Belgium voting is usually done during the weekend, although it shouldn't matter because voting is a civic duty (unless you have a good reason you have to go vote or you'll be fined), so those who work during the weekend have a valid reason to come in late or leave early.

reply

brendoelfrendo

13 hours ago

 |
root
 |
parent
 |
next

[–]

In the US, where I assume a lot of the griping comes from, election day is not a national holiday, nor is it on a weekend (in fact, by law it is defined as "the Tuesday next after the first Monday in November"), and even though it is acknowledged as an important civic duty, only about half of the states have laws on the books that require employers provide time off to vote. There are no federal laws to that effect, so it's left entirely to states to decide.

reply

hshdhdhehd

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

In Australia there are so many places to vote, it is almost popping out to get milk level if convenience. Just detour your dog walk slightly. Always at the weekend.

reply

wanderingmind

7 hours ago

 |
root
 |
parent
 |
next

[–]

From mandatory voting to preferential voting, australia seems to have figured out what this works best for democracy.

reply

Archelaos

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

In Germany it is always a Sunday.

reply

Hamuko

13 hours ago

 |
root
 |
parent
 |
next

[–]

Same in Finland. And even if you work Sundays, there's a week's worth of early voting so you can take your pick.

reply

hshdhdhehd

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

In Australia there are so many places to vote, it is almost popping out to get milk level if convenience. (At least in urbia and suburbia) Just detour your dog walk slightly. Always at the weekend.

reply

dullcrisp

11 hours ago

 |
root
 |
parent
 |
next

[–]

In the US getting milk involves driving multiple miles, finding parking, walking to the store, finding a shopping cart, finding the grocery department, navigating the aisles to the dairy section, finding the milk, waiting in line to check out, returning the cart if you’re courteous, and driving back. Could take an hour or so.

reply

johnfn

9 hours ago

 |
root
 |
parent
 |
next

[–]

Yes, or you do it on your drive back from work, and it takes 3 minutes.

reply

hshdhdhehd

9 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

No convenience stores?

reply

dullcrisp

9 hours ago

 |
root
 |
parent
 |
next

[–]

There are gas stations but I’m not sure I’d trust the milk there.

reply

sleepybrett

10 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

In washington we have a 100% mail-in voting system (for all intents and purposes). I can put my ballot back in the mail or drop at any number of drop-boxes throughout the city (less dropboxes in rural areas i'm sure). I think there are some allowances for in-person voting but I don't think they are often used.

There is a ballot tracking system as well, I can see and be notified as my ballot moves through the counting system. It's pretty cool.I actually just got back from dropping off my local elections ballot 15m ago, quick bike trip maybe a mile or so away and back.Of course, because it makes it easy for people to vote, the republicans want to do away with it. If you have to stand in line for several hours (which seems to be very normal in most cities) and potentially miss work to do it that's going to all but guarantee that working people and the less motivated will not vote.So yes in places that only do in person voting, national or state holiday.

reply

hinkley

10 hours ago

 |
root
 |
parent
 |
next

[–]

You have a mail-in voting system... for now.

reply

alt227

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Wow thats crazy! National transport infrastructure being so fragile. What a great age we live in.

reply

onionisafruit

13 hours ago

 |
root
 |
parent
 |
next

[–]

It is a great age to live in where we have transportation infrastructure beyond foot paths.

reply

dijit

9 hours ago

 |
root
 |
parent
 |
next

[–]

yeah, those are the two options. and before the cloud there was no transportation possible except via foot.

Horses were famously tamed in 2007 after AWS released S3 to the public, this is the best of times.

reply

bironran

13 hours ago

 |
parent
 |
prev
 |
next

[–]

Yet... deploy on two clouds and you'll get tax payers scream at you for "wasting money" preparing for a black swan event. Can't have both, either reliability or lower cost.

reply

bethekidyouwant

7 hours ago

 |
parent
 |
prev
 |
next

[–]

You are not getting more 9’s rolling your own

reply

bombcar

1 hour ago

 |
root
 |
parent
 |
next

[–]

You can get way more 9s if you roll your own procedures - and each step has a way of handling failure of the other steps.

Old trains had paper tickets, the locomotive was its own power source, the conductor had a flashlight, and the conductor could sell tickets for cash.And if everything else failed, the conductor would just let you ride for free.Now everything's so interconnected that any one part failing brings everything to a halt.

reply

vachina

6 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

At least I get to control when the 0.01 happens.

reply

fylo

3 hours ago

 |
root
 |
parent
 |
next

[–]

How?

reply

isbvhodnvemrwvn

3 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

No you don't, lol.

reply

stefs

13 hours ago

 |
parent
 |
prev
 |
next

[–]

i'm not sure this is an easily solvable problem. i remember reading an article arguing that your cloud provider is part of your tech stack and it's close to impossible/a huge PITA to make a non-trivial service provider-agnostic. they'd have to run their own openstack in different datacenters, which would be costly and have their own points of failure.

reply

myself248

13 hours ago

 |
root
 |
parent
 |
next

[–]

How ever did buses run before The Cloud™? What a weird world that must have been.

reply

dotancohen

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I run non trivial services on EC2, using that service as a VPS. My deploy script works just as well on provisioned Digital Ocean services and on docker containers using docker-compose.

I do need a human to provision a few servers and configure e.g. load balancing and when to spin up additional servers under load. But that is far less of a PITA than having my systems tied to a specific provider or down whenever a cloud precipitates.

reply

baby_souffle

11 hours ago

 |
root
 |
parent
 |
next

[–]

It's absolutely doable if you design for it.

The moment you choose to use S3 instead of hosting your own object store, though, you either use AWS because S3 and IAM already have you or spend more time on the care and feeding of your storage system as opposed to actually doing the thing you customers are paying you to do.It's not impossible, just complicated and difficult for any moderately complex architecture.

reply

zharknado

5 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

“precipitates” ha! Wonderfully evocative.

reply

j45

14 hours ago

 |
parent
 |
prev
 |
next

[–]

Organizations who had their own datacenters were chided for being resistant to modernizing, and now they modernized to use someone else's shared computers and they stopped working.

I really do feel the only viable future for clouds is hybrid or agnostic clouds.

reply

esseph

12 hours ago

 |
root
 |
parent
 |
next

[–]

Hybrid was always the way. Use different tools to solve different problems.

reply

barrenko

15 hours ago

 |
parent
 |
prev
 |
next

[–]

> wouldn't put China or Russia above this

reply

gowld

13 hours ago

 |
root
 |
parent
 |
next

[–]

Why would you put Microsoft above this?

reply

barrenko

12 hours ago

 |
root
 |
parent
 |
next

[–]

Nope :)

reply

platevoltage

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I wouldn't put Texas above this either.

reply

alliao

12 hours ago

 |
parent
 |
prev
 |
next

[–]

dang even zealand didn't survive! new zealand got some soul searching with this outage which took down government person ID service, it's called RealME and it can be used to file your taxes apply for passport etc

reply

tmtvl

14 hours ago

 |
parent
 |
prev
 |
next

[–]

The Flemish bus company (de Lijn) uses Azure and I couldn't activate my ticket when I came home after training a couple of hours ago. I should probably start using physical tickets again, because at least those work properly. It's just stupid that there's so much stuff being moved to digital only (often even only being accessible through an Android or iOS app, despite the parent companies of those two being utterly atrocious) when the physical alternatives are more reliable.

reply

varispeed

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Wasn't cloud sold based on a premise to prevent the very thing that is happening? Sounds like a massive fail of the whole concept.

reply

fHr

10 hours ago

 |
parent
 |
prev
 |
next

[–]

can't believe it's 2025 and some still need to go to some place to vote. I can vote since I can remember(at least 20 years) by mail for anything, we also vote multiple times a year(4-6 times), we just get 1 Month before the things to vote by mail and then mail in back votes. Hope we can soon vote online to get rid of the paper overhead.

reply

vanviegen

1 hour ago

 |
root
 |
parent
 |
next

[–]

When voting remotely, how can we be sure that your vote was not bought or coerced?

reply

qrios

7 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Is that you? The same guy with the comment "hahahhahaha"[1] on "Women dating safety app 'Tea' breached, users' IDs posted to 4chan"[2]?

[1]https://news.ycombinator.com/item?id=44689366[2]https://news.ycombinator.com/item?id=44684373

reply

bob1029

16 hours ago

 |
prev
 |
next

[–]

For some reason an Azure outage does not faze me in the same way that an AWS outage does.

I have never had much confidence in Azure as a cloud provider. The vertical integration of all the things for a Microsoft shop was initiallyverycompelling. I was ready to fight that battle. But, this fantasy was quickly ruined by poor execution on Microsoft's part. They were able to convince me to move back to AWS by simply making it difficult to provision compute resources. Their quota system & availability issues are a nightmare to deal with compared to EC2.At this point I'd rather use GCP over Azure and I have zero seconds of experience with it. The number of things Microsoft gets right in 2025 can be counted single-handedly. The things they do get right are quite good, but everything else tends to be extremely awful.

reply

xmcp123

16 hours ago

 |
parent
 |
next

[–]

Many years back was the first time I used Azure, evaluating it for a client.

I remember I at one point had expanded enough menus that it covered the entirety of the screen.Never before have I felt so lost in a cloud product.

reply

WorldMaker

16 hours ago

 |
root
 |
parent
 |
next

[–]

The "Blades" experience [0] where instead of navigating between pages it just kept opening things to the side and expanding horizontally?

Yeah, that had some fun ideas but was way more confusing than it needed to be. But also that wasquitea few years back now. The Portal ditched that experience relatively quickly. Just long enough to leave a lot of awful first impressions, but not long enough for it to be much more than a distant memory at this point, several redesigns later.[0] The name "Blades" for that came from the early years of the Xbox 360, maybe not the best UX to emulate for a complex control panel/portal.

reply

btown

15 hours ago

 |
root
 |
parent
 |
next

[–]

Azure to me has always suffered from a belief that “UI innovations can solve UX complexity if you just try hard enough.”

Like, AWS, and GCP to a lesser extent, has a principled approach where simple click-ops goals are simple. You can access the richer metadata/IAM object model at any time, but the wizards you see are dumb enough to make easy things easy.With Azure, those blades allow tremendously complex “you need to build an X Container and a Container Bucket to be able to add an X” flows to coexist on the same page. While this exposes the true complexity, and looks cool/works well for power users, it is exceedingly unintuitive. Inline documentation doesn’t solve this problem.I sometimes wonder if this is by design: like QuickBooks, there’s an entire economy of consultants who need to be Certified and thus will promote your product for their own benefit! Making the interface friendly to them and daunting to mere mortals is a feature, not a bug.But in Azure’s case it’s hard to tell how much this is intentional.

reply

xnorswap

3 hours ago

 |
root
 |
parent
 |
next

[–]

I still feel lost just trying to view my application logs.

I don't want to pay for or lock myself into, "Azure Insights".I just want to see the logging, that I know if I can remember the right buttons to click, are available.The worst place to try is "Monitoring > Logs", this is where you get faced up front with a query designer. I've never worked out how to do a simple "list by time" on that query designer, but it doesn't matter, because if you suffer through that UX, you find out that's not actually where the logs are anyway.You have to go down a different path. Don't be distracted by "Log Stream", that's not it either, it sounds useful but it's not. By default it doesn't log anything. If you do configure it to log, then it still doesn't actually log everything.What you have to actually do, and I've had to open the portal to check this, is click "Diagnose and Solve Problems" and then look for "Diagnostic tools" and then a small link to "Application Event Logs".Finally you get to your logs, although it's still a bad way to try to view logs, it's at least marginally better than the real windows event viewer, an application that feels like it hasn't been updated since NT4. ( Although some might suggest that's a good thing. )

reply

Insanity

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Not sure what to imagine with this given I didn't use Azure at the time. Is this like the Windows XP style task menu?

reply

WorldMaker

14 hours ago

 |
root
 |
parent
 |
next

[–]

Think Niri [0], but worse, embedded in a web browser tab, and without keyboard navigation.

Here's a somewhat ancient Stack Overflow screenshot I found:https://i.sstatic.net/yCseI.png(I think that's from near the transition because it has full "windowing" controls of minimize/maximize/close buttons. I recall a period with only close buttons.)All that blue space you could keep filling with more "blades" as you clicked on things until the entire page started scrolling horizontally to switch between "blades". Almost everything you could click opened in a new blade rather than in place in the existing blade. (Like having "Open in New Window" as your browser default.)It was trying to merge the needs of a configurable Dashboard and a "multi-window experience". You could save collections of blades (a bit like Niri workspaces) as named Dashboards. Overall it was somewhere between overkill and underthought.(Also someone reminded me that many "blades" still somewhat exist in the modern Portal, because, of course, Microsoft backwards compatibility. Some of the pages are just "maximized Blades" and you can accidentally unmaximize them and start horizontally scrolling into new blades.)[0]https://github.com/YaLTeR/niri

reply

csydas

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

azure likes to open new sections on the same tab / page as opposed to reloading or opening a new page / tab (overlays? modals? I'm lost on graphic terms)

depending on the resource you're accessing, you can get 5+ sections each with their own ui/ux on the same page/tab and it can be confusing to understand where you're at in your resourcesif you're having trouble visualizing it, imagine an url where each new level is a different application with its own ui/ux and purpose all on the same webpage

reply

high_priest

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Imagine OG Xbox menus, or the PS3/PSP menus.

reply

nazgulsenpai

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Count your blessings. You could have to use Azure SSO through Oracle Cloud..... ; ;

reply

foresterre

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

AWS' UI is similarly messy, and to this day. They regularly remove useful data from the UI, or change stuff like the default sort order of database snapshots from last created to initial instance created date.

I never understood why a clear and consistent UI and improved UX isn't more of a priority for the big three cloud providers. Even though you talk mostly via platform SDK's, I would consider better UI especially initially, a good way to bind new customers and pick your platform over others.I guess with their bottom line they don't need it (or cynically, you don't want to learn and invest in another cloud if you did it once).

reply

brap

15 hours ago

 |
root
 |
parent
 |
next

[–]

It’s more than just the UI itself (which is horrible), it’s the whole thing that is very hostile to new users even if they’re experienced. It’s such an incoherent mess. The UI, the product names, the entire product line itself, with seemingly overlapping or competing products… and now it’s AI this and AI that. If you don’t know exactly what you’re looking for, good luck finding it. It’s like they’re deliberately trying to make things as confusing as possible.

For some reason this applies to all AWS, GCP and Azure. Seems like the result of dozens of acquisitions.

reply

conductr

15 hours ago

 |
root
 |
parent
 |
next

[–]

I still find it much easier to just self host than learn cloud and I’ve tried a few times but it just seems overly complex for the sake of complexity. It seems they tie in all their services to jack up charges, eg. I came for S3 but now I’m paying for 5 other things just to get it working.

Any time something is that unintuitive to get started, I automatically assume that if I encounter a problem that I’ll be unable to solve it. That thought alone leads me to bounce every time.

reply

reddalo

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

100% agree. I've been working in the industry for almost 20 years, I'm a full stack developer and I manage my servers. I've tried signing up for AWS and I noped out.

AWS Is a complete mess. Everything is obscured behind other products, and they're all named in the most confusing way possible.

reply

lovich

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I found it intuitive but admittedly it felt a lot like their Xbox UI which I used a lot during my formative years

reply

jeffrallen

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Amazon: here's two buttons, some check boxes and a random popup.

MSFT : Hold my beer...

reply

issafram

4 hours ago

 |
parent
 |
prev
 |
next

[–]

I've used AWS, Azure, and recently GCP. You do NOT want to use GCP.

reply

multiplegeorges

15 hours ago

 |
parent
 |
prev
 |
next

[–]

> At this point I'd rather use GCP over Azure and I have zero seconds of experience with it.

TBH, GCP is very good! More people should use it.

reply

archon810

4 hours ago

 |
root
 |
parent
 |
next

[–]

>I've used AWS, Azure, and recently GCP. You do NOT want to use GCP.

>TBH, GCP is very good! More people should use it.These takes couldn't be further apart. Gotta love HN comments.

reply

a012

1 hour ago

 |
root
 |
parent
 |
next

[–]

GCP console is not the best but as a long term multicloud user, I can assure you that GCP is much better than Azure portal and/or Azure APIs which is fucking hell

reply

bpye

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I haven't used much of GCP, but I have had a good experience with Cloud Run and really haven't found a comparable offering from the other clouds.

reply

vrosas

10 hours ago

 |
root
 |
parent
 |
next

[–]

Cloud Run is incredible. It’s one of those things I wish more devs knew about. Even at work where we use GCP all the “smart” devs insist on GKE for their “webscale” services that get dozens of requests a second. Dozens!

reply

antonkochubey

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Isn’t ECS Fargate pretty much the same thing?

reply

nflekkhnnn

15 minutes ago

 |
root
 |
parent
 |
next

[–]

ACI is the corresponding service in our favorite cloud.

reply

macintux

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I know for some people the prospect of losing their Google Cloud access due to an automated terms of service violation on some completely unrelated service is worrisome.

https://cloud.google.com/resource-manager/docs/project-suspe...I'd hope you can create a Google Cloud account under a completely different email address, but I do as little business with Google as I can get away with, so I have no idea.

reply

kccqzy

9 hours ago

 |
root
 |
parent
 |
next

[–]

That's generally speaking a good practice anyways. My Amazon shopping account has a different email than my Amazon Web Services account. I intuited that they need to be different from the get go.

reply

major505

2 hours ago

 |
parent
 |
prev
 |
next

[–]

I like azure. I think they are more intuitive tua aws and good, and they have good prices for startups ( essentially free for a whole year )

reply

karel-3d

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Microsoft has the regulatory capture. All the European privacy and regulatory laws are good for Azure. That's why your average European government or baking app runs most likely on Azure. (or Oracle, but more likely Azure)

reply

aftbit

16 hours ago

 |
parent
 |
prev
 |
next

[–]

The problem is that in some industries, Microsoft is the only option. Many of these regulated industries are just now transitioning from the data center to the cloud, and they've barely managed to get approval for that with all of the Microsoft history in their organization. AWS or GCloud are complete non-starters.

reply

bob1029

16 hours ago

 |
root
 |
parent
 |
next

[–]

I moved a 100% MS shop to AWS circa 2015. We ran our DCs on EC2 instances just as if they were on prem. At some point we installed the AAD connector and bridged some stuff to Azure for office/mail/etc., but it was all effectively in AWS. We were selling software to banks so we had a lot of due diligence to suffer. AWS Artifact did much of the heavy lifting for us. We started with Amazon's compliance documentation and provided our own feedback on top where needed.

I feel like compliance is theentire pointof using these cloud providers. You get a huge head start. Maintaining something like PCI-DSS when you own the real estate is amuchbigger headache than if it's hosted in a provider who is already compliant up through the physical/hardware/networking layers. Getting application-layer checkboxes ticked off is trivial compared to "oops we forgot to hire an armed security team". I just took a look and there are currently 316 certifications and attestations listed under my account.https://aws.amazon.com/artifact/faq/

reply

thewebguyd

15 hours ago

 |
root
 |
parent
 |
next

[–]

I've found that lift and shifting to EC2 is also generally cheaper than the equivalent VMs on Azure.

Microsoftreallywants you to use their PaaS offerings, and so things on Azure are priced accordingly. A Microsoft shop just wanting to lift-and-shift, Azure isn't the best choice unless the org has that "nobody ever got fired for buying Microsoft" attitude.

reply

Nemo_bis

13 hours ago

 |
parent
 |
prev
 |
next

[–]

Microsoft is better at regulatory capture, so Azure has many customers in the public sector. So an Azure outage probably affects the public sector more (see example above about trains).

reply

otterdude

16 hours ago

 |
parent
 |
prev
 |
next

[–]

What Amazon, Azure, and Google are showing with their platform crashes amid layoffs, while they supports governments that are Oppressing's Citizens and Ignoring the Law, is that they do not care about anything other than the bottom line.

They think they have the market captured, but I think what their dwindling quality and ethics are really going to drive is adoption of self hosting, distributed computing frameworks. Nerds are the ones who drove adoption of these platforms, and we can eventually end if we put in the work.Seriously with container technology, and a bit more work / adoption on distributed compute systems and file storage (IPFS,FileCoin) there is a future where we dont have to use big brothers compute platform. Fuck these guys.

reply

amnesty6249

15 hours ago

 |
root
 |
parent
 |
next

[–]

These were my thoughts exactly. I may have my tinfoil hat on, but outages these close together between the largest cloud providers amid social unrest, my wonder is the government / tech companies implementing some update that adds additional spyware / blackout functionality.

I really hope this pushes the internet back to how it used to be, self hosted, privacy, anonymity. I truly hope that's where we're headed, but the masses seem to just want to stay comfortable as long as their show is on TV

reply

lazystar

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> they do not care about anything other than the bottom line.

if all companies focused on fixing each and every social issue that exists in the world, how would they make any money?

reply

WD-42

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Preach

reply

arccy

16 hours ago

 |
parent
 |
prev
 |
next

[–]

The only reason you'd notice MS was down was if Github was down....

reply

foresterre

16 hours ago

 |
root
 |
parent
 |
next

[–]

GitHub doesn't use Azure yet, but has just published their migration path to azure a few days ago.

I would link to that article, but that one does seem down ;)

reply

OptionOfT

15 hours ago

 |
root
 |
parent
 |
next

[–]

https://www.githubstatus.com/incidents/4jxdz4m769gy

> They're stating they're working with the Azure teams, so I suspect this is related.

reply

lebski88

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

At least some bits of it do. I was writing something to pull logs the other day and the redirect was to an azure bucket. It also returned a 401 with the valid temporary authed redirect in the header. I was a bit worried I'd found a massive security hole but it appears after some testing it just returned the wrong status code.

reply

abhinavk

3 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I only noticed it because VSCode's updater failed.

reply

danielovichdk

15 hours ago

 |
parent
 |
prev
 |
next

[–]

What did you do when AWS was down last week?

reply

WD-42

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Azure outages don’t faze anyone because nobody notices when it happens.

reply

redwood

16 hours ago

 |
parent
 |
prev
 |
next

[–]

I read "Microsoft shop" as "Microsoft slop". Fitting. But at least they open source wash themselves so much they're practically a charity right?

reply

Imustaskforhelp

16 hours ago

 |
prev
 |
next

[–]

Google cloud run or cloudflare workers it is.

Personally I am thinking more and more about hetzner, yes I know its not an apples to orange comparison. But its honestly so goodSomeone had created a video where they showed the underlying hardware etc., I am wondering if there is something likehttps://vpspricetracker.com/but with geek-benchmarks as well.This video was affiliated with scalahosting but still I don't think that there was too much bias of them and they showed at around 3:37 a graph comparison with priceshttps://www.youtube.com/watch?v=9dvuBH2Pc1gNow it shows how contabo has better hardware but I am pretty sure that there might be some other issues, and honestly I feel a sense of trust with hetzner I am not sure about others.Either hetzner or self hosting stuff personally or just having a very cheap vps and going to hetzner if need be but hetzner already is pretty cheap or I might use some free service that I know of are good as well.

reply

Havoc

13 hours ago

 |
parent
 |
next

[–]

Hetzner seems sound, but I doubt they play in the same reliability league as google

reply

dijit

11 hours ago

 |
root
 |
parent
 |
next

[–]

Probably not, but at least you don’t delude yourself into thinking reliability is a solved problem just because you’re paying through the nose for compute and storage.

reply

hshdhdhehd

13 hours ago

 |
parent
 |
prev
 |
next

[–]

Are you after nines? Maybe do multi provider?

reply

TiredOfLife

15 hours ago

 |
parent
 |
prev
 |
next

[–]

One of recent (4 months ago) Cloudflare outages (I think it was even workers) was caused by Google Cloud being down and Cloudflare hosting an essential service there

reply

kentonv

15 hours ago

 |
root
 |
parent
 |
next

[–]

It was Workers KV (an optional storage add-on to Workers), and we fixed it, it no longer depends on GCP:

https://blog.cloudflare.com/rearchitecting-workers-kv-for-re...

reply

Imustaskforhelp

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Hm it seemed that they hosted a critical service for cloudflare kv on google itself, but I wonder about the update.

Personally I just trust cloudflare more than google, given how their focus is on security whereas google feels googly...I have heard some good things about google cloud run and the google's interface feels the best out of AWS,Azure,GCloud but I still would just prefer cloudflare/hetzner iircAnother question: Has there ever been a list of all major cloud outages, like I am interested how many times google cloud and all cloud providers went majorly down I guess y'know? is there a website/git project that tracks this?

reply

jammo

53 minutes ago

 |
prev
 |
next

[–]

We all need to move away from these big cloud providers. Two medium size smaller providers is enough.

-Cloudflare for R2 (object storage) and CDN (Fastly+backblaze also available).
-Two VPS/Server providers with a decent reputation and mid-size (using a comparison site likehttps://serversearcher.comor look directly into people like Hetzner or latitude)
-PlanetScale or Neon for database if you don't co-locate it, though better to use someone like digital ocean, vultr or latitude who offer databases too)

reply

dspillett

22 minutes ago

 |
parent
 |
next

[–]

> We all need to move away from these big cloud providers.

But then who do we blame when things are down? If we manage our own infrastructure we have to stay late to fix it when it breaks instead of saying “sorry, Microsoft, nothing we can do” and magically our clients accepting that…

reply

blcknight

11 minutes ago

 |
parent
 |
prev
 |
next

[–]

Ah yes, let's put our multibillion dollar ecommerce site on...
checks notes
 Hetzner.

Lol

reply

Jamie452

18 hours ago

 |
prev
 |
next

[–]

Currently standing in a half closed supermarket because the tills are down and they cant take payments

reply

david422

17 hours ago

 |
parent
 |
next

[–]

IIRC, the grocery chain I worked for used to have an offline mode to move customers out the door. But it meant that when the system came back online, if the customers card was denied, the customer got free groceries.

reply

tcmart14

16 hours ago

 |
root
 |
parent
 |
next

[–]

Yea, good old store and forward. We implemented it in our PoS system. Now, we do non PCI integrations so we arn't in PCI scope, but depending on the processor, it can come with some limitations. Like, you can do store and forward, but only up to X number of transactions. I think for one integration, it's 500-ish store wide (it uses a local gateway that store and forwards to the processors gateway). The other integration we have, its 250, but store and forward on device, per device.

reply

fy20

6 hours ago

 |
root
 |
parent
 |
next

[–]

In many places it's also possibly just a left over feature from older times. I worked at a major UK supermarket in the mid-00s, and their checkout system had this feature. But it was like that because that's how it was originally built, it wasn't a 'feature' they added.

Credit card information would be recorded by the POS, synced to a mini-server in the back office (using store-and-forward to handle network issues) and then in a batch process overnight, sent to HQ where the payment was processed.It wasn't until chip-and-PIN was rolled out that they started supporting "online" (i.e. processed then and there) card transactions, and even then the old method still worked if there was a network issues or power failure (all POSes has their own UPS).The only real risk at the time was that someone tried to pay with a cancelled credit card - the bank would always honour the payment otherwise. But that was pretty uncommon back then, as you'd have to phone your bank to do it, not just press a button in an app.

reply

onionisafruit

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

What I gather from this is to always try a dead card first just in case the store is in offline mode

reply

progmetaldev

11 hours ago

 |
root
 |
parent
 |
next

[–]

They still capture the name on the card, so I would be careful about trying this, unless you can make use of a prepaid card.

reply

reaperducer

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

IIRC, the grocery chain I worked for used to have an offline mode to move customers out the door.

Chick-fil-a has this.One of the tech people there was on HN a few years ago describing their system. Credit card approval slows down the line, so the cards are automatically "approved" at the terminal, and the transaction is added to a queue.The loss from fraudulent transactions turns out to be less than the loss from customers choosing another restaurant because of the speed of the lines.

reply

ransom1538

8 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I was shopping at a mall with a visa vanilla card once. I got it as a gift and didn't know the limit. No matter what I bought the card kept going -- and I never got a balance of what was on the card. Eventually, later that day it stopped. I called customer support and asked how much was left on the balance. They told me they had no idea my balance - but everything I bought was mine.

reply

cyberax

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I remember that banks will try to honor the transactions, even if the customer's balance/credit limit is exhausted. It doesn't apply only to some gift cards.

reply

chasd00

18 hours ago

 |
parent
 |
prev
 |
next

[–]

There's a Family Dollar by my house that is down at least 2 full days per month because of bad inet connectivity. I live close enough that with a small tower on my roof i can get line of sight to theirs. I've thought about offering them a backup link off my home inet if they give me 50% of sales whenever its in use. It would be a pretty good deal for them, better some sales when their inet is down vs none.

reply

jrodom

17 hours ago

 |
root
 |
parent
 |
next

[–]

50% of sales? what do you think the gross margin is on average for each item sold?

reply

chasd00

15 hours ago

 |
root
 |
parent
 |
next

[–]

It's Family Dollar, margin has to be almost nothing and sales per day is probably < $1k. That's why I said 50% of sales and not profit.

I go there daily because it's a nice 30min round trip walk and I wfh. I go up there to get a diet coke or something else just to get out of the house. It amazes me when i see a handwritten sign on the door "closed, system is down". I've gotten to know the cashiers so I asked and it's because the internet connection goes down all the time. That store has to one of the most poorly run things i've ever seen yet it stays in business somehow.

reply

hinkley

14 hours ago

 |
root
 |
parent
 |
next

[–]

I think the point people are trying and failing to make is that asking for half of means sales is half of revenue not half of net and that you’re out of your goddamned mind if you think a store with razor thin margins would sell at a massive loss rather than just close due to connectivity problems.

Your responses imply that you think people are questioning whether you would lose money on the deal while we are instead saying you’ll get laughed out of the store, or possibly asked never to come back.

reply

gwbas1c

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

They're all run on a shoestring:

1: I doubt they're "with it" enough to put together a backup arrangement for internet.2: Their internet problems are probably due to a cheapo router, loose wire, ect.3: The employees probably like the break.

reply

progmetaldev

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Unfortunately they are largely corporate, which is how they can sell items for such a cheap price. The store manager probably has zero say in nearly anything. Even if they wanted to "break the rules," I doubt they could make use of your connection as a backup, but I've also worked for smaller companies that were able to sell internet access to individual locations like Denny's and various large hotels in the US. Being able to somehow share sales would be the difficult part, since all sales are reported back to corporate.

Good luck if you make this work for you, it would be exciting to hear about if you're able to get them to work with you.

reply

consp

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

2-3%, bit higher on perishables. Though i'd just ask lump sum payments in cash since it likely has to no go through corporate (as in, avoid the corporation).

reply

OptionOfT

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

In that case the other 50%.

reply

jiveturkey

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

it's retail. the margin is 30-50% for sure.

EDIT: their last quarterly was 36%. they lost $3.7bn in 24Q4 -- the christmas quarter. sold to PE in Q1.

reply

hinkley

14 hours ago

 |
root
 |
parent
 |
next

[–]

All my limited knowledge about retail is that losing money in Q4 means you’re dead. Are they fundamentally different than retail?

reply

ryandrake

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You'd think any SeriousBusiness would have a backup way to take customers' money. This is the one thing you always want to be able to do: accept payment. If they made it so they can't do that, they deserve the hit to their revenue. People should just walk out of the store with the goods if they're not being charged.

Why doesn't someone in the store at least have one of those manual kachunk-kachunk carbon copy card readers in the back that they can resuscitate for a few days until the technology is turned back on? Did they throw them all away?

reply

ElevenLathe

17 hours ago

 |
root
 |
parent
 |
next

[–]

The kachunk-kachunk credit card machines need raised digits on the cards, and I don't think most banks have been issuing those for years at this point. Mine have been smooth for at least 10 years.

reply

progmetaldev

11 hours ago

 |
root
 |
parent
 |
next

[–]

My card tied to my main financial institution have the raised digits, but most cards you'd sign up for online now no longer have the raised digits (and often allow you to select art to appear on the card face).

reply

rkomorn

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> kachunk-kachunk credit card machines

How aptly descriptive.

reply

xboxnolifes

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It's hit or miss. My (brand new) bank card and chase credit card are raised. But my other credit cards are flat.

reply

BenjiWiebe

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I think a lot of payment terminals have an option to record transactions offline and upload them later, but apparently it's not enabled by default - probably because it increases your risk that someone pays with a bad card.

reply

voidmain0001

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

If they used standalone merchant terminals, then those typically use the local LAN which can rollover to cellular or PoT in the event of a network outage. The store can process a card transaction with the merchant terminal and then reconcile with the end of day chit. This article from 2008 describes their PoS
https://www.retailtouchpoints.com/topics/store-operations/ca...

reply

Spooky23

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It’s family dollar. They don’t care about customer satisfaction and the cost of reliability is cost.

The stores are in the hood or middle of nowhere. The customers don’t have many options.

reply

progmetaldev

11 hours ago

 |
root
 |
parent
 |
next

[–]

These stores appear everywhere, even in areas with high income. You'd be surprised, but often people with those high incomes shop for certain products at very low rates, and that's how they keep their savings. A good example is garbage bags. Most people don't care too much about the quality of their garbage bags, unless they rip on the way to the bin.

reply

Finnucane

14 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Then they would need to get the little booklets of invalid numbers to keep by the register to check (yes, I am old).

reply

wat10000

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Many businesses don't lose revenue from short outages, it just gets shifted.

reply

BenjiWiebe

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Pretty sure it'd be a lot better deal for them to have no sales than to pay out 50% of sales on stuff with single digit margins.

reply

thisOtterBeGood

3 hours ago

 |
parent
 |
prev
 |
next

[–]

In Germany many stores still accept cash and some even only accept cash and we are ridiculed for this... Seems like one of the rare instances where this is useful :D

reply

bombcar

1 hour ago

 |
root
 |
parent
 |
next

[–]

It's sad the number of stores I've seen where they just shut down when they can't use the checkout machines; the clerks aren't allowed to do math even if they could.

Whereas the smaller, owner-run stores have more leeway; the local tiny grocery "sold" all freezer/refrigerator food for cheap/free during a power failure. The big Walmart closed and threw everything away the next day.

reply

Jamie452

14 hours ago

 |
parent
 |
prev
 |
next

[–]

Just to add - this particular supermarket wasn’t fully down, it took ages for them to press “sub total” and then pick the payment method. I suspect it was slow waiting for a request to timeout perhaps

reply

pndy

14 hours ago

 |
parent
 |
prev
 |
next

[–]

I remember last mechanical cash registers in my country in 90s and when these got replaced by early electronic ones with blue vacuum fluorescent tubes. Then everything got smaller and smaller. Now I'm pestered to "add the item to the cart" by software.

Last week I couldn't pay for flowers for grandma's grave because smartphone-sized card terminal refused to work - it stuck on charging-booting loop so I had to get cash. Tho my partner thinks she actually wanted to get cash without a receipt for herself excluding taxes

reply

SoftTalker

18 hours ago

 |
parent
 |
prev
 |
next

[–]

Mind-boggling that any retailer would not have the capability to at least run the checkout stations offline.

reply

bombcar

1 hour ago

 |
root
 |
parent
 |
next

[–]

Most retailers trust their cashiers a bit less than they trust the customers. They'd rather shut down during a power/Internet failure than give any autonomy to the worker drones.

reply

tcmart14

16 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You can, but it's all about risk mitigation. Most processors have some form of store and forward (and it can have limitations like only X number of transactions). Some even have controls to limit the amount you can store-and-forward (for instance, only charges under $50). But ultimately, it's still risk mitigation. You can store-and-forward, but you're trusting that the card/account has the funds. If it doesn't, you loose and ain't shit you can do about it. If you can't tolerate any risk, you don't turn on store and forward systems and then you can't process cards offline.

Its not the we are not capable. Its, is the business willing to assume the risk?

reply

withinboredom

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I knew an old guy in the '00s who specialized in cobal/fortran for working on tiller software. Guess he retired and they couldn't maintain it

reply

computerdork

18 hours ago

 |
root
 |
parent
 |
next

[–]

Anyone remember Bob's number?? Bob?! Oh the humanity! We're all gonna be canned!

reply

reaperducer

14 hours ago

 |
parent
 |
prev
 |
next

[–]

Currently standing in a half closed supermarket because the tills are down and they cant take payments

There's a fairly large supermarket near me that has both kinds of outages.Occasionally it can't take cards because the (fiber? cable?) internet is down, so it's cash only.Occasionally it can't take cash because the safe has its own cellular connection, and the cell tower is down.I was at Frank's Pizza in downtown Houston a few weeks ago and they were giving slices of pizza away because the POS terminal died, and nobody knew enough math to take cash. I tried to give them a $10 and told them to keep the change, but "keep the change" is an unknown phrase these days. They simply couldn't wrap their brains around it. But hey, free pizza!

reply

gmassman

17 hours ago

 |
prev
 |
next

[–]

I’ve been migrating our services off of Azure slowly for the past couple of years. The last internet facing things remaining are a static assets bucket and an analytics VM running Matomo. Working with Front Door has been an abysmal experience, and today was the push I needed to finally migrate our assets to Cloudflare.

I feel pretty justified in my previous decisions to move away from Azure. Using it feels like building on quicksand…

reply

alt227

17 hours ago

 |
parent
 |
next

[–]

All the clouds hav had major outages this year.

At this point I dont believe that any one of them is any better or reliable than the others.

reply

not_a_bot_4sho

4 hours ago

 |
parent
 |
prev
 |
next

[–]

> I feel pretty justified in my previous decisions to move away from Azure

I felt this way about AWS last week

reply

btmiller

13 hours ago

 |
parent
 |
prev
 |
next

[–]

Never let a good disaster go to waste ;)

reply

kierenj

18 hours ago

 |
prev
 |
next

[–]

Ouch, and login.microsoftonline.com too - i.e. SSO using MS accounts. We'd just rolled that out across most (all?) of our internal systems...

And microsoft.com too - that's gotta hurt

reply

planewave

17 hours ago

 |
parent
 |
next

[–]

It is interesting to see the differential across different tenants in different geographies:

- on a US tenant I am unable to access login.microsoftonline.com and the login flow stalls on any SSO authentication attempt.- on a European tenant, probably germany-west, I am able to login and access the Azure portal.

reply

parliament32

18 hours ago

 |
parent
 |
prev
 |
next

[–]

SSO and 365 are working fine for us, but admin portals for Azure/365 are down. Our workloads in Azure don't seem to be impacted.

reply

juancroldan

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Guess you have NASSO now (Not A Single Sign On)

reply

btbuildem

16 hours ago

 |
root
 |
parent
 |
next

[–]

It's Safe and Secure!

reply

ocdtrekkie

18 hours ago

 |
parent
 |
prev
 |
next

[–]

I am still stunned people choose to do this, considering major Office 365 outages are basically a weekly thing now.

reply

NetMageSCW

18 hours ago

 |
root
 |
parent
 |
next

[–]

We are very dependent on Azure and Microsoft Authentication and Microsoft 365 and haven’t had weekly or even monthly issues. I can think of maybe three issues this year.

reply

gianpaj

17 hours ago

 |
prev
 |
next

[–]

Can't download VSCode :D

Error: visual-studio-code: Download failed on Cask 'visual-studio-code' with message: Download failed:https://update.code.visualstudio.com/1.105.1/darwin-arm64/st...

reply

progmetaldev

11 hours ago

 |
parent
 |
next

[–]

I have had intermittent issues with winget today. I use UniGetUI for a front-end, and anything tied to Microsoft has failed for me. Judging by the logs, it's mostly retrieving the listing of versions (I assume similar to what 'apt-get update' does, I'm fairly new to using winget for Windows package management).

reply

robotnikman

16 hours ago

 |
parent
 |
prev
 |
next

[–]

Also cant do anything right now with the repo's we have in Azure Devops, how lovely...

reply

loopduplicate

14 hours ago

 |
parent
 |
prev
 |
next

[–]

get vscodium then

reply

agency

17 hours ago

 |
prev
 |
next

[–]

So that's why I can't check in for my Alaska Airlines flight...
https://news.microsoft.com/source/features/digital-transform...

reply

MangoCoffee

15 hours ago

 |
parent
 |
next

[–]

"BREAKING: Alaska Airlines' website, app impacted amid Microsoft Azure outage"

https://www.youtube.com/watch?v=YJVkLP57yvM

reply

Shuddown

15 hours ago

 |
parent
 |
prev
 |
next

[–]

Pretty much every single Microsoft domain I've tried to access loads for a looooong time before giving me some bare html. I wonder if someone can explain why that's happening.

reply

sodafountan

13 hours ago

 |
root
 |
parent
 |
next

[–]

I was wondering the same thing

reply

kurttheviking

17 hours ago

 |
parent
 |
prev
 |
next

[–]

I am unable to load this article...presumably for related reasons

reply

basfo

16 hours ago

 |
prev
 |
next

[–]

We’re 100% on Azure but so far there’s no impact for us.

Luckily, we moved off Azure Front Door about a year ago. We’d had three major incidents tied to Front Door and stopped treating it as a reliable CDN.They weren’t global outages, more like issues triggered by new deployments. In one case, our homepage suddenly showed a huge Microsoft banner about a “post-quantum encryption algorithm” or something along those lines.Kinda wild that a company that big can be so shaky on a CDN, which should be rock solid.

reply

Aperocky

15 hours ago

 |
parent
 |
next

[–]

Outages are one thing, but having your content polluted seems like a more serious problem? Unless you subscribed to microsoft banners somehow.

reply

basfo

15 hours ago

 |
root
 |
parent
 |
next

[–]

And it was HUGE, the microsoft logo was like 50% of the screen.

reply

qiller

14 hours ago

 |
parent
 |
prev
 |
next

[–]

We battled
https://learn.microsoft.com/en-us/answers/questions/1331370/...
 for over a year, and finally decided to move off since there was no any resolution. Unfortunately our API servers were still behind AFD so they were affected by today's stuff...

reply

zimpenfish

1 hour ago

 |
prev
 |
next

[–]

"Microsoft Azure will serve as the backbone of Asda’s digital infrastructure"[0]

Oh, that'll be why Scan & Go was down yesterday evening. I thought it was another instance of an iOS 26 update breaking their crappy code.[0]https://corporate.asda.com/newsroom/2025/22/09/asda-announce...

reply

vachina

17 hours ago

 |
prev
 |
next

[–]

microsoft.com and some subdomains (answers.microsoft.com) has no A and AAA records. They screwed up big time.

https://archive.is/Q4izZ

reply

0xbadcafebee

17 hours ago

 |
parent
 |
next

[–]

That specific subdomain has issues with propagation:
https://dnschecker.org/#A/answers.microsoft.com
 (only four resolvers return records)

The root zone and www. do not:https://dnschecker.org/#A/microsoft.com(all resolvers return records)And queryinghttps://www.microsoft.com/results in HTTP 200 on the root document, but the page elements return errors (a 504 on the .css/.js documents, a 404 on some fonts, Name Not Resolved on scripts.clarity.ms, Connection Timed Out on wcpstatic.microsoft.com and mem.gfx.ms). That many different kinds of errors is actually kind of impressive.I'm gonna say this was a networking/routing issue. The CDN stayed up, but everything else non-CDN became unroutable, and different requests traveled through different paths/services, but each eventually hit the bad network path, and that's what created all the different responses. Could also have been a bad deploy or a service stopped running and there's different things trying to access that service in different ways, leading to the weird responses... but that wouldn't explain the failed DNS propagation.

reply

Aperocky

17 hours ago

 |
parent
 |
prev
 |
next

[–]

wow, right after AWS suffered a similar thing.

I wonder if this is microsoft "learning" to "prevent" such an issue and instead triggered it..."One often meets his destiny on the path he takes to avoid it" -- Master Oogway

reply

buttscicles

54 minutes ago

 |
prev
 |
next

[–]

Interesting that everybody knows when AWS goes down but Azure needs a "Tell HN" :)

Best of luck to the teams responding to this incident.

reply

Aldipower

1 hour ago

 |
prev
 |
next

[–]

Hetzner, Netcup, OVH,
BunnyCDN,
ClouDNS,
Postmark

You name them. Other good providers you have experience with?There is no reason for an expensive cloud. Never has been, but decision makers tried to keep their pants dry.

reply

chemodax

18 hours ago

 |
prev
 |
next

[–]

For me the same. It's very confusing that status page [1] is green

[1]:https://azure.status.microsoft/en-us/status

reply

martini333

18 hours ago

 |
parent
 |
next

[–]

That status page is never red. Absolutely useless.

> There are currently no active events. UseAzure Service Healthto view other issues that may be impacting your services.Links to a page on Azure Portal which is down...

reply

endianswap

17 hours ago

 |
root
 |
parent
 |
next

[–]

It's red right now.

reply

Sharparam

17 hours ago

 |
root
 |
parent
 |
next

[–]

Only for the Azure Portal, despite Front Door also being down but showing as green on the status page.

reply

12_throw_away

16 hours ago

 |
root
 |
parent
 |
next

[–]

Heh, now it says Front Door
and "Network Infrastructure"
 are down. That second one seems bad.

reply

kylecazar

17 hours ago

 |
parent
 |
prev
 |
next

[–]

They added a message at the same time as your comment:

"We are investigating an issue with the Azure Portal where customers may be experiencing issues accessing the portal. More information will be provided shortly."

reply

ape4

18 hours ago

 |
prev
 |
next

[–]

2026: the year of your own metal in a rack

reply

0xbadcafebee

14 hours ago

 |
parent
 |
next

[–]

2027: the year of migrating from your own metal to a managed provider

2028: the year of migrating from a managed provider to the cloud2029: the year of migrating from the cloud to your own metal in a rackPeople keep thinking the solution to their problems is to do something new (that they don't fully understand).TIL it's calledNirvana Fallacy

reply

hshdhdhehd

13 hours ago

 |
root
 |
parent
 |
next

[–]

The upside of keep moving it acts as a hardener and chaos monkey. You shake out any crufty service no one knows how to build let alone deploy.

reply

t0lo

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Just experienced this with moving around multiple states and universities in the past year :) Grass really was greener in my hometown

reply

reaperducer

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

TIL it's called Nirvana Fallacy

We used to call it "The grass is always greener on the other side of the fence."

reply

Aperocky

15 hours ago

 |
parent
 |
prev
 |
next

[–]

I'd predict the year of linux desktop instead.

reply

hshdhdhehd

13 hours ago

 |
root
 |
parent
 |
next

[–]

At least YOLD is possible. Is there capacity in the world for everyone to ditch clouds.

reply

drewnick

18 hours ago

 |
parent
 |
prev
 |
next

[–]

I've been doing it since 1998 in my bedroom with a dual T1 (and on to real DCs later). While I've had some outages for sure it makes me feel better I am not that divergent in uptime in the long run vs big clouds.

reply

dylan604

17 hours ago

 |
root
 |
parent
 |
next

[–]

Are you still on a dual T1? that's gotta be expensive

reply

daveguy

17 hours ago

 |
root
 |
parent
 |
next

[–]

(and on to real DCs later) would imply their bare metal is now located in a data center.

reply

dylan604

17 hours ago

 |
root
 |
parent
 |
next

[–]

really should stop skimming the comment when i find a part to comment on <facepalm>

reply

move-on-by

16 hours ago

 |
prev
 |
next

[–]

Instead of cyber security awareness month, we should rename it to cloud availability awareness month.

reply

sedatk

16 hours ago

 |
prev
 |
next

[–]

The paradox of cloud provider crashes is that if the provider goes down and takes the whole world with it, it's actually good advertisement. Because, that means so many things rely on it, it's critically important, and has so many big customers. That might be why Amazon stock went up after AWS crash.

If Azure goes down and nobody feels it, does Azure really matter?

reply

thewebguyd

16 hours ago

 |
parent
 |
next

[–]

People feel it, but usually not general consumers like they do when AWS goes down.

If Azure goes down, it's mostly affecting internal stuff at big old enterprises. Jane in accounting might notice, but the customers don't. Contrast with AWS which runs most of the world's SaaS products.People not being able to do their jobs internally for a day tends not to make headlines like "100 popular internet services down for everyone" does.

reply

givemeethekeys

17 hours ago

 |
prev
 |
next

[–]

Surely more vibecoding will fix this problem. Time to fire more staff

reply

0000000000100

17 hours ago

 |
prev
 |
next

[–]

Yeah just took down the prod site for one of our clients since we host the front-end out of their CDN. Just got wrapped up panic hosting it somewhere else for the past hour, very quickly reminds you about the pain of cookies...

reply

alt227

17 hours ago

 |
parent
 |
next

[–]

... and DNS caching, and browser file cache, and sessions...

Moving a website quickly is never fun.

reply

DeathArrow

17 minutes ago

 |
prev
 |
next

[–]

Buy cloud because you're always safe! Until you aren't.

reply

flumpcakes

18 hours ago

 |
prev
 |
next

[–]

Pretty much all Azure services seem to be down. Their status page says it's only the portal since 16:00. It would be nice if these mega-companies could update their status page when they take down a large fraction of the Internet and thousands of services that use them.

reply

parliament32

18 hours ago

 |
parent
 |
next

[–]

All of our Azure workloads are up, but we don't use Azure Front Door. That seems to be the only impacted product, apart from the management portal.

reply

flumpcakes

17 hours ago

 |
root
 |
parent
 |
next

[–]

We're using Application Gateway for ingress, that seems to be effected.

reply

kierenj

18 hours ago

 |
parent
 |
prev
 |
next

[–]

FWIW, all of our databases, VMs, AKS clusters, services, jobs etc - are all working fine. Which services are down for you, maybe we can build a list?

reply

reknih

18 hours ago

 |
root
 |
parent
 |
next

[–]

Front Door is down for us (as Azure‘s Twitter account confirms)

reply

wbsun

13 hours ago

 |
parent
 |
prev
 |
next

[–]

Does their status page depend on something that is down already, so the page just fails static now hence no new updates?

reply

jayw_lead

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Same playbook for AWS. When they admitted that Dynamo was inaccessible, they failed to provide context that their internal services are heavily dependent on Dynamo

It's only after the fact they are transparent about the impact

reply

MangoCoffee

18 hours ago

 |
prev
 |
next

[–]

The Internet is supposed to be decentralized. The big three seem to have all the power now (Amazon, Microsoft, and Google) plus Cloudflare/Oracle.

How did we get here? Is it because of scale? Going to market in minutes by using someone else's computers instead of building out your own, like co-location or dedicated servers, like back in the day.

reply

kube-system

17 hours ago

 |
parent
 |
next

[–]

It still is very decentralized. We are discussing this via the internet right now.

reply

kbelder

16 hours ago

 |
root
 |
parent
 |
next

[–]

I need to drop AWS and start passing data through encrypted HN posts.

reply

Mr_Bees69

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Yeah, but
MyChart
 is down.

reply

chasd00

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

When AWS was down we were talking about it here, now Azure is down and we're still talking about it here. Where does HN actually live?

reply

acedTrex

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

big, if true

reply

mrinterweb

17 hours ago

 |
parent
 |
prev
 |
next

[–]

A lot of money and years of marketing the cloud as the responsible business decision led us here. Now that the cloud providers have vendor lock-in, few will leave, and customers will continue to wildly overpay for cloud services.

reply

gwbas1c

17 hours ago

 |
root
 |
parent
 |
next

[–]

Ahh, but you forget what it
used
 to be like. Sites used to go down
all the time.

Now, they go down a lot less frequently, but when they do, it's more widespread.

reply

bossyTeacher

17 hours ago

 |
root
 |
parent
 |
next

[–]

Not sure how the current situation is better. Being stranded with no way whatsoever to access most/all of your services sounds way more terrifying than regular issues limited to a couple of services at a time

reply

gwbas1c

16 hours ago

 |
root
 |
parent
 |
next

[–]

> no way whatsoever to access most/all of your services

I work on a product hosted on Azure. That's not the case. Except for front door, everything else is running fine. (Front door is a reverse proxy for static web sites.)The product itself (an iot stormwater management system) is running, but our customers just can't access the website. If they need to do something, they can go out to the sites or call us and we can "rub two sticks together" and bypass the website. (We could also bypass front door if someone twisted our arms.)Most customers only look at the website a few times a year.---That being said, our biggest point of failure is a completely different iot vendor who you probably won't hear about on Hacker News when they, or their data networks, have downtime.

reply

JoBrad

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It’s the Heisenberg cloud principal.

reply

deaux

16 hours ago

 |
parent
 |
prev
 |
next

[–]

From today [0].

> Big Tech lobbying is riding the EU’s deregulation wave by spending more, hiring more, and pushing more, according to a new report by NGO’s Corporate Europe Observatory and LobbyControl on Wednesday (29 October).> Based on data from the EU’s transparency register, the NGOs found that tech companies spend the most on lobbying of any sector, spending €151m a year on lobbying — a 33 percent increase from €113m in 2023.Gee whizz, I really do wonder how they end up having all the power![0]https://news.ycombinator.com/item?id=45744973

reply

alt227

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Thats the whole point, big players like AWS and MS can go down, but here we are still talking on the internet.

Decentralisation is winning it seems.

reply

jslaby

17 hours ago

 |
root
 |
parent
 |
next

[–]

Not everyone has moved over, but I'm sure there have been thoughts or plans to.

reply

nzach

17 hours ago

 |
parent
 |
prev
 |
next

[–]

> How did we get here?

I think the response lies in the surrounding ecosystem.If you have a company it's easier to scale your team if you use AWS (or any other established ecosystem). It's way easier to hire 10 engineers that are competent with AWS tools than it is to hire 10 engineers that are competent with the IBM tools.And from the individuals perspective it also make sense to bet on larger platforms. If you want to increase your odds of getting a new job, learning the AWS tools gives you a better ROI than learning the IBM tools.

reply

anonymars

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Efficiency (aka cost) <---> Resiliency/redundancy

Pick your point on the scale

reply

deathanatos

13 hours ago

 |
root
 |
parent
 |
next

[–]

Maybe in a perfect world, or in a free market.

But the cloud compute market is basically centralized into 2.5 companies at this point.The pointof paying companies like Azure here is that they'vein theorycentralized the knowledge and know-how of running multiple, distributed datacenters, so as toberesilient.But that we keep seeing outages encompassing more than a failure domain, then it should be fair game for engineers / customers to ask "what am I paying for, again?"Moreover, this seems to be a classic case of large barriers to entry (the huge capital costs associated with building out a datacenter) barring new entrants into the market, coupled with "nobody ever got fired for buying IBM" level thinking. Are outages like these truly factored into the napkin math that says externalizing this is worth it?

reply

codethief

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Meredith Whittaker (of Signal) addressed your question the other day:
https://mastodon.world/@Mer__edith/115445701583902092

reply

pphysch

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Consolidation is the inevitable outcome of free unregulated markets.

In our highly interconnected world, decentralization paradoxically requires a central authority to enforce decentralization by restricting M&A, cartels, etc.

reply

SoKamil

17 hours ago

 |
root
 |
parent
 |
next

[–]

Is there a theorem that models this behavior? Capital feels like a mass that attracts more mass the larger it becomes, like gravity.

reply

AndrewKemendo

17 hours ago

 |
parent
 |
prev
 |
next

[–]

A natural monopoly is a monopoly in an industry in which high infrastructure costs and other barriers to entry relative to the size of the market give the largest supplier in an industry, often the first supplier in a market, an overwhelming advantage over potential competitors. Specifically, an industry is a natural monopoly if a single firm can supply the entire market at a lower long-run average cost than if multiple firms were to operate within it. In that case, it is very probable that a company (monopoly) or a minimal number of companies (oligopoly) will form, providing all or most of the relevant products and/or services.

https://en.wikipedia.org/wiki/Natural_monopoly

reply

SecretDreams

17 hours ago

 |
parent
 |
prev
 |
next

[–]

> How did we get here?

Stonks

reply

port11

17 hours ago

 |
prev
 |
next

[–]

So much of Belgium runs on Azure… it's honestly baffling how many services are down, there's no resilience built into (even large) companies anymore.

reply

nflekkhnnn

21 minutes ago

 |
prev
 |
next

[–]

Shut the front door!

reply

kierenj

17 hours ago

 |
prev
 |
next

[–]

Sorry - my bad. I literally just connected an old XP VM to the internet to activate it.

reply

tyfon

18 hours ago

 |
prev
 |
next

[–]

Seems to be down in Norway.

Even the national digital id service is down.

reply

hexbin010

17 hours ago

 |
parent
 |
next

[–]

> Even the national digital id service is down.

Can't help but smirk as my country is ramming through "Digital ID" right now

reply

bombcar

1 hour ago

 |
root
 |
parent
 |
next

[–]

Someone somewhere thought that "national digital ID service" should absolutely rely on a cloud provider in and from another country.

What a time to be alive.

reply

Steven_Vellon

17 hours ago

 |
prev
 |
next

[–]

For us, it looks like most services are still working (eastus and eastus2). Our AKS cluster is still running and taking requests. Failures seem limited to management portal.

reply

jmspring

7 hours ago

 |
prev
 |
next

[–]

The outage was really weird. For me, parts of the portal worked, other parts didn't. I had access to a couple of resource groups, but no resources visible in those groups. Azure Devops Pipelines that needed do download from packages.microsoft.com didn't work.

The Microsoft status page mostly referenced the portal outage, but it was more than that.

reply

bombcar

1 hour ago

 |
parent
 |
next

[–]

I hate these failures because you end up with things that keep working fine because the login credentials are cached, etc; but if you restart or otherwise refresh, you're doomed.

reply

mythz

17 hours ago

 |
prev
 |
next

[–]

High availability is touted as a reason for their high prices, but I swear I read about major cloud outages far more than I experience any outages at Hetzner.

reply

prmoustache

17 hours ago

 |
parent
 |
next

[–]

I think the biggest features of the big cloud vendors is that when they are down, not only you but your customers and your competitors usually have issues at the same time so everybody just shrug and have a lazy/off day at the same time. Even on call teams reall just have to wait and stay on standby because there is very little they can do. Doing a failover can be slower than waiting for the recovery, not help at all if outage is spanned accross several region, or bring aditional risks.

And more importantly nobody lose any reputation except AWS/Azure/Google.

reply

zavec

17 hours ago

 |
root
 |
parent
 |
next

[–]

It's like back in school when there was a snow day!

reply

graemep

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Ostensible reason.

The real reason is that outages are not your fault. Its the new version of "nobody ever got fired for buying IBM" - later it became MS, and now its any big cloud provider.

reply

jmaker

17 hours ago

 |
parent
 |
prev
 |
next

[–]

For one it’s statistics - Hetzner simply runs far fewer major services than hyperscalers. And the services they run are also more affluent, with larger customer bases, so downtimes are systemically critical. Therefore it’s louder.

On the merits though, I agree, haven’t had any serious issues with Hetzner.

reply

bad_haircut72

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Same with DigitalOcean. I run one box and it hasnt gone down for like 2 years

reply

yabones

17 hours ago

 |
root
 |
parent
 |
next

[–]

DO has been shockingly reliable for me. I shut down a neglected box almost 900 days uptime the other day. In that time AWS has randomly dropped many of my boxes with no warning requiring a manual stop/start action to recover them... But everybody keeps telling me that DO isn't "as reliable" as the big three are.

reply

ipdashc

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

To be fair, in the AWS/Azure outages, I don't think any individual (already created) boxes went down, either. In AWS' case you couldn't start up
new
 EC2 instances, and presumably same for Azure (unless you bypass the management portal, I guess). And obviously services like DynamoDB and Front Door, respectively, went down. Hetzner/DO don't offer those, right? Or at least they're not very popular.

reply

robotnikman

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Same here, I run a few droplets for personal projects and never had any issues with then.

reply

bongodongobob

17 hours ago

 |
parent
 |
prev
 |
next

[–]

It's just the admin portal.

reply

12_throw_away

17 hours ago

 |
root
 |
parent
 |
next

[–]

Nope, more than the portal. For instance, I just searched for "Azure Front Door" because I hadn't heard of it before (I now know it's a CDN), and neither the product page itself [1] nor the technical docs [2] are coming up for me.

[1]https://azure.microsoft.com/en-us/products/frontdoor[2]https://learn.microsoft.com/en-us/azure/frontdoor/front-door...

reply

Foobar8568

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Plenty of sites are down and/or login not available. It's just really a mess.

reply

NDizzle

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It's absolutely not only the admin portal.

It's CDN and FrontDoor at least.

reply

bongodongobob

17 hours ago

 |
root
 |
parent
 |
next

[–]

Interesting, everything else is working just fine for us. Offices across the US.

reply

Jarwain

17 hours ago

 |
root
 |
parent
 |
next

[–]

Do you use on front door? Our VMs that don't are working fine, but our app services that do aren't.

reply

out_sider

17 hours ago

 |
root
 |
parent
 |
next

[–]

we use front door (as does miccrosoft.com) and our website was down, I was able to change the DNS records to point directly to our server and will leave it like that for a few hours until everything is green

reply

ikamm

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

The bank I work at is reporting all Power Apps applications are down.

reply

pocketman

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

It looks like it is just the 365 admin panels for us. Admittedly, we don't currently host any other services on Azure though.

reply

cbovis

18 hours ago

 |
prev
 |
next

[–]

Looks to be affecting our pipelines that rely on Playwright as they download images from Azure e.g.
https://playwright.azureedge.net/builds/chromium/1124/chromi...
 which aren't currently resolving.

reply

reid

18 hours ago

 |
prev
 |
next

[–]

This is impacting the Azure CDN at azureedge.net. DNS A records for azureedge.net tenants are taking 2-6 seconds and often return nothing.

reply

etyhhgfff

17 hours ago

 |
parent
 |
next

[–]

It's always DNS, unless it's not DNS.

reply

AdmiralAsshat

18 hours ago

 |
prev
 |
next

[–]

Some exec at Microsoft told the Azure guys to ape everything Amazon does and they took it literally.

reply

Telemakhos

17 hours ago

 |
parent
 |
next

[–]

Or, the NSA needed to upgrade their access at both.

reply

embedding-shape

17 hours ago

 |
root
 |
parent
 |
next

[–]

Do Microsoft still say "If the government has a broader voluntary national security program to gather customer data, we don't participate in it" today (which PRISM proved very false), or are they at least acknowledging they're participating in whatever NSA has deployed today?

reply

terminalshort

17 hours ago

 |
root
 |
parent
 |
next

[–]

PRISM wasn't voluntary. Also there are 3 levels here:

1. Mandatory2. "Voluntary"3. VoluntaryAnd I suspect that very little of what the NSA does falls into category 3. As Sen Chuck Schumer put it "you take on the intelligence community, they have six ways from Sunday at getting back at you"

reply

cruffle_duffle

16 hours ago

 |
root
 |
parent
 |
next

[–]

“Voluntold”

reply

jrochkind1

17 hours ago

 |
parent
 |
prev
 |
next

[–]

I was gonna say that obv AWS hacked em to even things up.

reply

dboreham

17 hours ago

 |
parent
 |
prev
 |
next

[–]

This is funny but also possibly true because: business/MBA types see these outages as a way to prove how critical some services are, leading to investors deciding to load up on the vendor's stock.

reply

alt227

17 hours ago

 |
root
 |
parent
 |
next

[–]

I may or may not have been known to temporarily take a database down in the past to make a point to management about how unreliable some old software is.

reply

aftbit

16 hours ago

 |
prev
 |
next

[–]

I still can't log into Azure Gov Cloud with

https://microsoft.com/deviceloginusSeems like they migrated the non-Gov login but not the Gov one. C'mon Microsoft, I've got a deadline in a few days.

reply

sherinjosephroy

57 minutes ago

 |
prev
 |
next

[–]

Another big cloud outage — even “enterprise” systems aren’t bulletproof. Feels like every layer depends on too much hidden glue. Makes you wonder if real redundancy even exists anymore.

reply

amaccuish

16 hours ago

 |
prev
 |
next

[–]

Seeing users having issues with the "Modern Outlook", specifically empty accounts. Switching back to the "Legacy Outlook" which functions largely without the help of the cloud fixes the issue. How ironic.

reply

mystcb

17 hours ago

 |
prev
 |
next

[–]

Updated 16:35 UTC

Azure Portal Access IssuesStarting at approximately 16:00 UTC, we began experiencing DNS issues resulting in availability degradation of some services. Customers may experience issues accessing the Azure Portal. We have taken action that is expected to address the portal access issues here shortly. We are actively investigating the underlying issue and additional mitigation actions. More information will be provided within 60 minutes or sooner.This message was last updated at 16:35 UTC on 29 October 2025----Azure Portal Access IssuesWe are investigating an issue with the Azure Portal where customers may be experiencing issues accessing the portal. More information will be provided shortly.This message was last updated at 16:18 UTC on 29 October 2025-- From the Azure status page

reply

progmetaldev

13 hours ago

 |
prev
 |
next

[–]

I was having issues a few hours ago. I'm now able to access the portal, although I get lots of errors in the browser console, and things are loading slowly. I have services in the US-East region.

I have been having issues with GitHub and the winget tool for updates throughout the day as well. I imagine things are pulling from the same locations on Azure for some of the software I needed to update (NPM dependencies, and some .NET tooling).

reply

blenderob

17 hours ago

 |
prev
 |
next

[–]

https://azure.status.microsoft/en-us/status
 says everything's fine! Any place I can read more about this outage?

reply

reid

17 hours ago

 |
parent
 |
next

[–]

You're looking at it. I couldn't find any discussion elsewhere yet...

reply

sbergot

17 hours ago

 |
parent
 |
prev
 |
next

[–]

official status pages are useless most of the time.

reply

jeffrallen

14 hours ago

 |
root
 |
parent
 |
next

[–]

I work for a cloud provider which is serious about transparency. Our customers know they are going to get the straight story from our status page.

When you find an honest vendor, cherish them. They are rare, and they work hard to earn and keep your confidence.

reply

sbergot

17 hours ago

 |
parent
 |
prev
 |
next

[–]

now there is an information about "Azure Portal Access Issues". No word about front door being down.

reply

hedayet

16 hours ago

 |
prev
 |
next

[–]

The sad thing is - $MSFT isn't even down by 1%. And IIRC, $AMZN actually went up during their previous outage.

So if we look at these companies' bottom lines, all those big wigs are actually doing something right. Sales and lobbying capacity is way more effective than reliability or good engineering (at least in the short term).

reply

locusofself

16 hours ago

 |
parent
 |
next

[–]

AMZN went up almost 4 percent between the day of the outage and the day after. Crazy market.

reply

jlarocco

15 hours ago

 |
root
 |
parent
 |
next

[–]

Because it shows how much lock-in they have.

You know nobody is migrating off of AWS or Azure because of these.

reply

navane

16 hours ago

 |
parent
 |
prev
 |
next

[–]

Look how important we are, is what these failures show

reply

marcosdumay

15 hours ago

 |
root
 |
parent
 |
next

[–]

What do you mean? That IT isn't important for Microsoft and Amazon?

That's certainly not the right conclusion.

reply

alt227

15 hours ago

 |
root
 |
parent
 |
next

[–]

I think he was implying that those companies think they are so important that it doesnt matter they are down, they wont loose any customers over it because they are too big and important.

reply

cyberax

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

So we can look forward to "accidental" cloud outages just to show their importance?

I guess the GCP is next.

reply

Arrath

15 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

"They'll learn their lesson and be rock solid after this! I better invest now!"

reply

bigstrat2003

12 hours ago

 |
parent
 |
prev
 |
next

[–]

That's a good thing. Stock prices
shouldn't
 go down because of rare incidents which don't accurately represent how successful a company is likely to be in the future.

reply

iamtheworstdev

15 hours ago

 |
parent
 |
prev
 |
next

[–]

well, at this point, 90% of the market cap of FAANGS plus Microsoft is... OMG AI LLM hype

reply

AtNightWeCode

16 hours ago

 |
parent
 |
prev
 |
next

[–]

I looked into this before and the stocks of these large corps simply does not move when outages happens. Maybe intra-day, I don't have that data, but in general no effect.

reply

delf

16 hours ago

 |
prev
 |
next

[–]

The outage impacted GitSocial minor version bump release:
https://marketplace.visualstudio.com/items?itemName=GitSocia...

There's no way to tell, and after about 30 minutes, the release process on VS Code Marketplace failed with a cryptic message: "Repository signing for extension file failed.". And there's no way to restart/resume it.

reply

vincebowdren

18 hours ago

 |
prev
 |
next

[–]

UK, and other regions too; our APAC installation in Australia is affected.

reply

vpears87

18 hours ago

 |
prev
 |
next

[–]

At least MSFT is consistent:
https://www.microsoft.com/en-us/
 is down as well

reply

CommanderData

18 hours ago

 |
parent
 |
next

[–]

Likely behind Azure Front Door.

Much of Xbox is behind that too.

reply

tartieret

17 hours ago

 |
prev
 |
next

[–]

Microsoft posted an update on X:

https://x.com/AzureSupport/status/1983569891379835372?ref_sr...

"We’re investigating an issue impacting Azure Front Door services. Customers may experience intermittent request failures or latency. Updates will be provided shortly."

reply

llama052

17 hours ago

 |
parent
 |
next

[–]

Always fun when you can't trust the main status page but have to go to some opinionated social medial website to see the actual problem.

reply

drjasonharrison

17 hours ago

 |
root
 |
parent
 |
next

[–]

https://www.cbc.ca/news/investigates/tesla-grok-mom-9.695693...

This mom’s son was asking Tesla’s Grok AI chatbot about soccer. It told him to send nude pics, she saysxAI, the company that developed Grok, responds to CBC: 'Legacy Media Lies'

reply

eeasss

14 hours ago

 |
prev
 |
next

[–]

Deglobalization in geopolitics should be followed by deglobalization in cloud providers as well. Viva la local vendors.

reply

major505

2 hours ago

 |
prev
 |
next

[–]

Somewhere, an ex microsoft engineer that where layoff during the last week, is saying to himself “thank god, this shit is not my problem anymore”

reply

udfalkso

12 hours ago

 |
prev
 |
next

[–]

OpenAI Clip python library fails because the model download is a hardcoded azure cdn url :(

reply

alt227

16 hours ago

 |
prev
 |
next

[–]

Microsoft have started putting customer status pages up on windows.net, so it must be really really bad!

For example when I try to log into our payroll provider Brightpay, it sends me here:https://bpuk1prod1environment.blob.core.windows.net/host-pro...

reply

tonymet

13 hours ago

 |
prev
 |
next

[–]

Any healthcare IT admins care to chime in? A predominantly MS industry with critical workloads.

reply

borg16

18 hours ago

 |
prev
 |
next

[–]

i guess folks in azure wanted to show some solidarity with aws brethren

(couldn't resist adding it. i acknowledge this comment adds no value to the discussion)

reply

aurumque

18 hours ago

 |
parent
 |
next

[–]

Azure goes down all the time. On Friday we had an entire regional service down all day. Two weeks ago same thing different region. You only hear about it when it's something everyone uses like the portal, because in general nobody uses Azure unless they're held hostage.

reply

Mr_Bees69

18 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah, im regretting my decision to buy an xbox now. Every once in a while, everything goes down.

reply

ApolloFortyNine

17 hours ago

 |
prev
 |
next

[–]

They admit in their update blurb azure front door is having issues but still report azure front door as having no issues on their status page.

And it's very clear from these updates that they're more focused on the portal than the product, their updates haven't even mentioned fixing it yet, just moving off of it, as if it's some third party service that's down.

reply

consp

17 hours ago

 |
parent
 |
next

[–]

> as having no issues on their status page

Unsubstantiated idea: So the support contract likely says there is a window between each reporting step and the status page is the last one and the one in the legal documents giving them several more hours before the clauses trigger.

reply

chrisgeleven

16 hours ago

 |
prev
 |
next

[–]

"Front Door" has to be the worst product name for a CDN I've ever heard of. I used to work for a CDN too.

reply

oliyoung

13 hours ago

 |
parent
 |
next

[–]

We should've never let marketing in the door honestly, all of the product names for the big three are awful.

Microsoft CDNThere, that's it. You're selling it to (hopefully) technical people

reply

joquarky

12 hours ago

 |
parent
 |
prev
 |
next

[–]

It so strongly implies a counterpart.

reply

unethical_ban

16 hours ago

 |
parent
 |
prev
 |
next

[–]

I wonder if many Germans are eager to sign up for AFD.

But seriously I thought it would be the console, not a CDN.

reply

jeffrallen

14 hours ago

 |
root
 |
parent
 |
next

[–]

Front Door (tm), with Back Door access for the FBI included free with your subscription! ;)

reply

m_fayer

17 hours ago

 |
prev
 |
next

[–]

And there goes
https://www.microsoft.com/

reply

reid

17 hours ago

 |
prev
 |
next

[–]

Portal and Azure CDN are down here in the SF Bay Area. Tenant azureedge.net DNS A queries are taking 2-6 seconds and most often return nothing. I got a couple successful A response in the last 10 minutes.

Edit: As of 9:19 AM Pacific time, I'm now getting successful A responses but they can take several seconds. The web server at that address is not responding.

reply

jacquesm

18 hours ago

 |
prev
 |
next

[–]

It is much more than azure. One of my kids needs a key for their laptop and can't reach that either. Great excuse though, 'Azure ate my homework'. What a ridiculous world we are building. Fuck MS and their account requirements for windows.

reply

ApolloFortyNine

17 hours ago

 |
prev
 |
next

[–]

Two hours after the initial outage, they have finally updated the Front Door status on their status page.

reply

elFarto

18 hours ago

 |
prev
 |
next

[–]

We saw all incoming traffic to our app drop to zero at about 15:45. I wonder how long this one will take to fix.

reply

sech8420

18 hours ago

 |
parent
 |
next

[–]

Same exact time for us as well.

reply

vs4vijay

18 hours ago

 |
prev
 |
next

[–]

Service Status:
https://status.cloud.microsoft/
 and
https://azure.status.microsoft/en-us/status

reply

ipsum2

18 hours ago

 |
parent
 |
next

[–]

Status page (first link) is down for me. Second one works

reply

charv

18 hours ago

 |
root
 |
parent
 |
next

[–]

oh the irony, the status link being down too

reply

karateka01

18 hours ago

 |
root
 |
parent
 |
next

[–]

status page being affected by the same issue is so lame

reply

millzlane

17 hours ago

 |
root
 |
parent
 |
next

[–]

It begs the question from a noob like me... Where should they host the status page? Surely it shouldn't be on the same infra that it's supposed to be monitoring. Am I correct in thinking that?

reply

aftergibson

18 hours ago

 |
parent
 |
prev
 |
next

[–]

Looks like the status page is overloaded...

reply

andhuman

18 hours ago

 |
prev
 |
next

[–]

I bet it’s DNS.

reply

andhuman

17 hours ago

 |
parent
 |
next

[–]

“ Starting at approximately 16:00 UTC, we began experiencing DNS issues resulting in availability degradation of some services. Customers may experience issues accessing the Azure Portal. We have taken action that is expected to address the portal access issues here shortly. We are actively investigating the underlying issue and additional mitigation actions. More information will be provided within 60 minutes or sooner.

This message was last updated at 16:35 UTC on 29 October 2025”

reply

LouisLazaris

17 hours ago

 |
prev
 |
next

[–]

The VS Code website is down:
https://code.visualstudio.com/

And so is Microsoft:http://www.microsoft.com/

reply

codethief

17 hours ago

 |
parent
 |
next

[–]

https://www.microsoft.com
 works for me (
with
 the www subdomain).

reply

SoftTalker

17 hours ago

 |
prev
 |
next

[–]

We're on Office 365 and so far it's still responding. At least Outlook and Teams is.

reply

jeffdn

17 hours ago

 |
parent
 |
next

[–]

They don't run on Azure!

reply

RajT88

17 hours ago

 |
root
 |
parent
 |
next

[–]

They definitely do run on Azure. Probably not 100%, but at least some footprint of those services do.

reply

rcarmo

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Are you absolutely sure?

reply

jansper39

17 hours ago

 |
root
 |
parent
 |
next

[–]

They don't, however authentication for those services relies on Entra ID which seems to be affected.

reply

rcarmo

17 hours ago

 |
root
 |
parent
 |
next

[–]

I'd say DNS/Front Door (or some carrier interconnect) is the thing affected, since I can auth just fine in a few places. (I'm at MS, but not looped into anything operational these days, so I'm checking my personal subscription).

reply

_pdp_

14 hours ago

 |
prev
 |
next

[–]

With all the recent outages considered, it is time to move off the cloud.

reply

Jarwain

17 hours ago

 |
prev
 |
next

[–]

On our end, our VMs are still working, so our gitlab instance is still up. Our services using Azure App Services are available through their provided url. However, Front Door is failing to resolve any domains that it was responsible for.

reply

irusensei

16 hours ago

 |
prev
 |
next

[–]

I was working when I saw the portal page showing only resource groups and lots of items missing. I thought it was a weird browser cache issue.

The actual stuff I was working on (App Insights, Function App) that was still open was operational.

reply

senderista

13 hours ago

 |
prev
 |
next

[–]

Even if the cloud providers have much better reliability than most on-prem infra, the failure correlation they induce negates much of the benefit.

reply

CKMo

16 hours ago

 |
prev
 |
next

[–]

Reasons to not use hyperscalers, exhibit 654

There's a lot of outages this month!

reply

hypeatei

17 hours ago

 |
prev
 |
next

[–]

All of my employers things are hosted on Azure and running just fine and didn't go down at all. Portal access has been fixed.

Doesn't seem to be too bad of an outage unless you were relying on Azure Front Door.

reply

randomsofr

17 hours ago

 |
parent
 |
next

[–]

SSO is down, Azure Portal Down and more, seems like a major outage. Already a lot of services seem to be affected: banks, airlines, consumer apps, etc.

reply

hypeatei

17 hours ago

 |
root
 |
parent
 |
next

[–]

The portal is up for me and their status page confirms they did a failover for it. Definitely not disputing that its reach is wide, but a lot of smaller setups probably aren't using Front Door.

reply

rahkiin

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Both work for me in the Netherlands

reply

a_f

17 hours ago

 |
prev
 |
next

[–]

Looks like MyGet is impacted too. Seems like they use Azure:

>What is required to be able to use MyGet? ... MyGet runs its operations from the Microsoft Azure in the West Europe region, near Amsterdam, the Netherlands.

reply

rcarmo

17 hours ago

 |
prev
 |
next

[–]

Not seeing it. I have VMs in US East and Netherlands and they're up.

reply

tgv

16 hours ago

 |
parent
 |
next

[–]

I tried to look some things up on their support pages before 1600Z, and it timed-out. The Dutch railways are also affected (they're an MS shop, IIRC).

reply

LaserToy

17 hours ago

 |
prev
 |
next

[–]

Azure portal still insists the issue is jsut with Console.

We had to bypass the Frontdoor

reply

baconbrand

18 hours ago

 |
prev
 |
next

[–]

All of our sites went down. This is my company’s busiest time of year. Hooray.

reply

tpl

15 hours ago

 |
prev
 |
next

[–]

Part of this outage involves outlook hanging and then blaming random addins. Pretty terrible practice by Microsoft to blame random vendors for their own outage.

reply

xer0x

7 hours ago

 |
prev
 |
next

[–]

Wow, they are still down 12 hours later. :/

reply

croemer

5 hours ago

 |
parent
 |
next

[–]

Not officially - status page says all healthy

reply

anon025

17 hours ago

 |
prev
 |
next

[–]

It's the DNS
https://dnschecker.org/#A/get.helm.sh
 is unreachable

reply

I_am_tiberius

17 hours ago

 |
parent
 |
next

[–]

Why are Azure App Services still working?

reply

zbowling

12 hours ago

 |
prev
 |
next

[–]

Alaska Airlines is redircting folks to their slimmed down international site and you can't check in on mobile.

reply

avgDev

18 hours ago

 |
prev
 |
next

[–]

I am having a bunch of issues. It looks like their sites and azure are both affected.

I also got weird notification in VS2022 that my license key was upgraded to Enterprise, but we did not purchase anything.

reply

Mr_Bees69

18 hours ago

 |
parent
 |
next

[–]

Might be a failsafe, if you cant get a license status, and you're aware that MS is down, just default to the highest tier.

reply

ThatManulTheCat

18 hours ago

 |
parent
 |
prev
 |
next

[–]

Free upgrade

reply

8cvor6j844qw_d6

18 hours ago

 |
prev
 |
next

[–]

Quite close to the recent AWS outage. Let me take a look if its a major one similar to AWS.

Any guess on what's causing it?In hindsight, I guess the foresight of some organizations to go multi-cloud was correct after all.

reply

jcims

18 hours ago

 |
parent
 |
next

[–]

We're multi-cloud and it really saved a few workloads last week with the AWS issue.

It's not easy though.

reply

sanskarix

4 hours ago

 |
root
 |
parent
 |
next

[–]

This is the eternal tension for early-stage builders, isn't it? Multi-cloud gives you resilience, but adds so much complexity that it can actually slow down shipping features and iterating.

I'm curious—at what point did you decide the overhead was worth it? Was it after experiencing an outage, or did you architect for it from day one?As someone launching a product soon (more on the builder/product side than infra-engineer), I keep wrestling with this. The pragmatist in me says "start simple, prove the concept, then layer in resilience." But then you see events like this week and think "what if this happens during launch?"How did you handle the operational complexity? Did you need dedicated DevOps folks, or are there patterns/tools that made it manageable for a smaller team?

reply

jcims

3 hours ago

 |
root
 |
parent
 |
next

[–]

I don't think I would recommend multi-cloud right out of the gate unless you already have a lot of experience in the space or there is a strong demand from your customers. There's a tremendous amount of overhead with security/compliance, incident management, billing, tooling, entitlements, etc. There are a number of external factors that drove our decision to do it, resiliency is just one of them. But we are a pretty big shop, spending ~$10M/mo on cloud infra and have ~100 people in the platform management department.

I would recommend focusing on multi-region within a single CSP instead (both for workloads AND your tooling), which covers the vast majority of incidents and lays some of the architectural foundation for multi-cloud down the road. Develop failover plans for each service in your architecture (eg. planned/tested runbooks to migrate to Traffic Manager in the event AFD goes down)Also choose your provider wisely. We experience 3-5x the number of service-impacting incidents on Azure that we do on AWS. I'm sure others have different experiences, but I would never personally start a company on Azure. AWS has its own issues, of course, but reliability has not been a major one (relatively speaking) over the past 10 years. Last week's incident with DynamoDB in us-east-1 had zero impact on our AWS workloads in other regions.

reply

stuff4ben

18 hours ago

 |
parent
 |
prev
 |
next

[–]

It's always freakin DNS...

reply

conroydave

18 hours ago

 |
parent
 |
prev
 |
next

[–]

cost cutting attempts

reply

iAMkenough

18 hours ago

 |
parent
 |
prev
 |
next

[–]

Trusting AI without sufficient review and oversight of changes to production.

reply

whynotminot

18 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah, these things never happened when humans were trusted without sufficient review and oversight of changes to production.

reply

shepherdjerred

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Do you have any insight or do you just dislike AI? Incidents like this happened long before AI generated code

reply

Capricorn2481

18 hours ago

 |
root
 |
parent
 |
next

[–]

I don't think it's meant to be serious. It's a comment on Microsoft laying off their staff and stuffing their Azure and Dotnet teams with AI product managers.

reply

Sharparam

18 hours ago

 |
prev
 |
next

[–]

The learning modules on
https://learn.microsoft.com/
 also seem to have a lot of issues properly loading.

reply

dlcarrier

18 hours ago

 |
prev
 |
next

[–]

Yesterday Amazon, today Microsoft. Are Google's cloud services going down tomorrow?

reply

gtowey

17 hours ago

 |
parent
 |
next

[–]

This is because Azure just copies everything AWS does. Google is a bit more innovative, they will have something else unexpected happen.

reply

dkdcio

17 hours ago

 |
root
 |
parent
 |
next

[–]

throwback to when they deleted a customer's entire account!
https://arstechnica.com/gadgets/2024/05/google-cloud-acciden...

reply

Insanity

18 hours ago

 |
parent
 |
prev
 |
next

[–]

Maybe they are and no one realized yet.. :P

That said, I don't hear about GCP outages all that often. I do think AWS might be leading in outages, but that's a gut feeling, I didn't look up numbers.

reply

luhn

17 hours ago

 |
root
 |
parent
 |
next

[–]

They had a pretty massive one earlier this year.
https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1S...

This isn't GCP's fault, but the outage ended up taking down Cloudflare too, so in total impact I think that takes the cake.

reply

xenolithis

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

fairly certain they had a significant multi region outage within the past few years. I'll try to find some details to link.

Few customers....few voices to complain as well.

reply

Mr_Bees69

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

as a victim of xbox, azure is down 'bout as often as its up

reply

m_fayer

18 hours ago

 |
parent
 |
prev
 |
next

[–]

And if they don't, we'll know who the culprit is.

reply

shishcat

18 hours ago

 |
root
 |
parent
 |
next

[–]

Who?

reply

briffle

17 hours ago

 |
parent
 |
prev
 |
next

[–]

here's hoping its Oracle's cloud instead....

reply

ycombinatornews

12 hours ago

 |
prev
 |
next

[–]

So that’s why CapitalOne is out today. Even though their (incorrect) status page says all systems operational.

reply

thimkerbell

18 hours ago

 |
prev
 |
next

[–]

Does (should, could) DownDetector also say what customer-facing services are down, when some infrastructure is unworking? Or is that the info that the malefactors are seeking?

reply

bragma

15 hours ago

 |
prev
 |
next

[–]

They suggest to use Traffic Manager to router around failing FrontDoor CDN, but DNS is failing too, making the suggestion another failure.

reply

asciii

15 hours ago

 |
parent
 |
next

[–]

Yeah they're suggesting to use CLI but then my Frontdoor deployment failed. Welp.

reply

btbuildem

16 hours ago

 |
prev
 |
next

[–]

https://login.microsoftonline.com/
 is down, so that's fun

reply

alt227

17 hours ago

 |
prev
 |
next

[–]

Cant access certain banking websites in the UK, I am assuming it because of this.

https://www.natwest.com/

reply

perks_12

16 hours ago

 |
prev
 |
next

[–]

Thank you. I was wondering what was going on at a company whose web app I need to access. I just checked with BuiltWith and it seems they are on Azure.

reply

syntaxing

17 hours ago

 |
prev
 |
next

[–]

I absolutely love the utility aspect of LLMs but part of me is curious if moving faster by using AI is going to make these sorts of failure more and more often.

reply

monkaiju

17 hours ago

 |
parent
 |
next

[–]

If true then what "utility" is there?

reply

1718627440

16 hours ago

 |
root
 |
parent
 |
next

[–]

More visibility for the general person to see how brittle software is?

reply

bronco21016

17 hours ago

 |
prev
 |
next

[–]

Unable to access the portal and any hit to SSO for other corporate accesses is also broken. Seems like there's something wrong in their Identity services.

reply

glzone1

17 hours ago

 |
prev
 |
next

[–]

Wasn't the saying "It's always DNS" floating around somewhere?

Be interesting to understand cause here. Pretty big impact on services we use

reply

mikestew

15 hours ago

 |
parent
 |
next

[–]

Could be DNS, I'm seeing SERVFAIL trying to resolve what look to be MS servers when I'm hitting (just one example) mygoodtogo.com (trying to pay a road toll bill, and failing).

reply

ThatManulTheCat

18 hours ago

 |
prev
 |
next

[–]

Azure portal currently mostly not working (UK)... Downdetector reporting various Microsoft linked services are out (Minecraft, Microsoft 365, Xbox...)

reply

jasonthorsness

10 hours ago

 |
prev
 |
next

[–]

Ahh it got me, Alaska air web site has an Azure outage banner

reply

empath75

17 hours ago

 |
prev
 |
next

[–]

Friend of mine at MSFT says it's a Sev-0 outage and they can't even get to the ticket tracking system.

reply

djeastm

17 hours ago

 |
prev
 |
next

[–]

I'm mid-deployment, but thankfully it seems to be running ok so far. Just the portal is not working so my visibility is not good.

reply

nartaczact

17 hours ago

 |
parent
 |
next

[–]

Sounds like Shrodinger's Deploy

reply

speckx

17 hours ago

 |
prev
 |
next

[–]

FYI:
https://status.cloud.microsoft/

reply

chuckadams

17 hours ago

 |
parent
 |
next

[–]

Which itself is^H^H was down. Wow.

reply

speckx

17 hours ago

 |
prev
 |
next

[–]

FYI:
https://status.cloud.microsoft/

reply

Boxersteavee

17 hours ago

 |
parent
 |
next

[–]

503 Service Unavailable

reply

martijnvds

16 hours ago

 |
prev
 |
next

[–]

This probably explains why paying for street parking in Cologne by phone/web didn't work (eternal spinner) then

reply

everfrustrated

17 hours ago

 |
prev
 |
next

[–]

GitHub runners (specifically the "larger" runner types) are all down for us. These are known to be hosted on Azure.

reply

smithkl42

16 hours ago

 |
prev
 |
next

[–]

The iron law of uptime: "The mandatory single point of failure in every possible system is configuration."

reply

tecleandor

17 hours ago

 |
prev
 |
next

[–]

LinkedIn has been acting funny for an hour or so, and some pages in the learn.microsoft.com domain have been failing for me too...

reply

ZeroConcerns

17 hours ago

 |
prev
 |
next

[–]

Oh, well, I'm
sure
 Azure will be given the same pass that AWS got here recently when they had their 12-hour outage...

reply

taeric

17 hours ago

 |
parent
 |
next

[–]

I didn't realize AWS got a pass?

reply

graemep

17 hours ago

 |
root
 |
parent
 |
next

[–]

Have repeated outages lost them customers? has it lost them any money in any way?

That is a pass.

reply

taeric

17 hours ago

 |
root
 |
parent
 |
next

[–]

Apologies, but this just reads like a low effort critique of big things.

To be clear, they should get criticism. They should be held liable for any damage they cause.But that they remain the biggest cloud offering out there isn't something you'd expect to change from a few outages that, by most all evidence, potential replacements have, as well? More, a lot of the outages potential replacements have are often more global in nature.

reply

graemep

2 hours ago

 |
root
 |
parent
 |
next

[–]

I would say you are explaining why they get a free pass so they still get one - they are bad but their main competitors are even worse!

I thought one of the major selling points of the big cloud providers was that they were more reliable than running your own stuff (by which i mean anything from a VPS to multiple data centres depending on your scale. Compared to those alternatives they seem to be less reliable in practice!The solution is to have a multi-region, or even multi-cloud setup, but then bang goes the "they do all the work for you" argument (which i doubt anyway).

reply

philipallstar

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Have people left GitHub due to the multiple post-acquisition outages? That is a pass if you don't judge it the same way.

reply

prmoustache

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Well, they have successfully locked their customers captive thanks to huge egress fees.

reply

arccy

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

customers like us are certainly looking at expanding from just multi region into instead being multi cloud...

reply

razodactyl

4 hours ago

 |
prev
 |
next

[–]

AWS, now Azure - wasn't this a plot point in Terminator where SkyNet was causing computer systems to have issues much before it finally become self-aware?

Funnily enough, AI has been training on its own data as generated by users writing AI conversations back to the internet - there's a feedback loop at play.

reply

montague27

16 hours ago

 |
prev
 |
next

[–]

Guess when/who has the next outage!

reply

baconbrand

17 hours ago

 |
prev
 |
next

[–]

Our Azure DevOps site is still functioning and our Azure hosted databases are accessible. Everything else is cooked.

reply

jimmyl02

17 hours ago

 |
prev
 |
next

[–]

pretty interesting how datadog's uptime tracker (
https://updog.ai/
) says all the sites are fully available.

if that's true then it's a sign that Azure's control / data plane separation is doing it's job! at least for now

reply

jonathanlydall

17 hours ago

 |
parent
 |
next

[–]

Our Azure hosted dotnet App Service is working fine, but our docs site served via Front Door went down. Can’t access anything through the Portal.

reply

layer8

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Maybe they need a downtime tracker. ;)

reply

glzone1

17 hours ago

 |
prev
 |
next

[–]

I remember the saying "It's always DNS". I'm old.

Kind of mindboggling it's still sometimes DNS maybe.

reply

alt227

15 hours ago

 |
parent
 |
next

[–]

That saying is just as alive today as it ever was.

https://isitdns.com/

reply

Mr_Bees69

17 hours ago

 |
prev
 |
next

[–]

MS website seems to be up but really slow. Think xbox might still be down, Bing works for some reason tho!?

reply

ksec

17 hours ago

 |
prev
 |
next

[–]

>Last week AWS, now this.

This is not the first or second time this happened, multiple Hyperscaler failed one by one.

reply

ChuckMcM

11 hours ago

 |
prev
 |
next

[–]

"On Prem" is looking better and better :-).

reply

qmr

16 hours ago

 |
prev
 |
next

[–]

Always in these large provider outages you see people who have forgotten the old ways.

reply

chemodax

17 hours ago

 |
prev
 |
next

[–]

It seems Azure FrontDoor is affected, because our private VM works fine in different regions.

reply

Shuddown

15 hours ago

 |
prev
 |
next

[–]

Github Codespaces (for the 5 people that use them) are also still down.

reply

twodave

18 hours ago

 |
prev
 |
next

[–]

Appears to be an issue in Front Door. Our back end stuff is fine but FD is bouncing everything.

reply

NDizzle

18 hours ago

 |
parent
 |
next

[–]

Yeah, I have non prod environments that don't use FD that are functioning. Routing through FD does not work. And a different app, nonprod doesn't use FD (and is working) but loads assets from the CDN (which is not working).

FD and CDN are global resources and are experiencing issues. Probably some other global resources as well.Hate to say it, but DNS is looking like it's still the undisputed champ.

reply

redwood

16 hours ago

 |
prev
 |
next

[–]

Is it Cosmos DB? If so the symmetry with AWS/Dynamo would be very eerie.

reply

whalesalad

16 hours ago

 |
prev
 |
next

[–]

Yikes,
http://schemas.xmlsoap.org/soap/encoding/
 is running on Azure and it's down. So any SOAP/WSDL api's are dead in the water.

HTTPSConnectionPool(host='schemas.xmlsoap.org', port=443): Max retries exceeded with url: /soap/encoding/ (Caused by SSLError(CertificateError("hostname 'schemas.xmlsoap.org' doesn't match '*.azureedge.net'")))A service we rely on that isn't even running on Azure is inaccessible due to this issue. For an asset that probably never changes. Wild for that to be the SPOF.160k+ results on GitHub:https://github.com/search?q=http%3A%2F%2Fschemas.xmlsoap.org...

reply

amluto

17 hours ago

 |
prev
 |
next

[–]

vscode.dev appears to be down. I think this will be my excuse to find an alternative -- I never really liked vscode.dev anyway.

(Coder is currently at the top of the experiment list. Any other suggestions?)

reply

vanviegen

18 hours ago

 |
prev
 |
next

[–]

Many (all?) LinkedIn profiles are also down for me. Luckily the frontpage still works. ;-)

Go cloud!

reply

AznHisoka

18 hours ago

 |
parent
 |
next

[–]

Luckily?

reply

macshome

18 hours ago

 |
prev
 |
next

[–]

I just tried to check the Xbox services status page and it never even loaded.

reply

chokolad

18 hours ago

 |
parent
 |
next

[–]

Majority of actual Xbox services are working fine, xbox.com itself is busted.

reply

rvz

18 hours ago

 |
prev
 |
next

[–]

Looking forward to the post mortem.

reply

internet_points

2 hours ago

 |
parent
 |
next

[–]

>
What went wrong and why?

> An inadvertent tenant configuration change within Azure Front Door (AFD) triggered a widespread service disruption affecting both Microsoft services and customer applications dependent on AFD for global content delivery. The change introduced an invalid or inconsistent configuration state that caused a significant number of AFD nodes to fail to load properly, leading to increased latencies, timeouts, and connection errors for downstream services.> As unhealthy nodes dropped out of the global pool, traffic distribution across healthy nodes became imbalanced, amplifying the impact and causing intermittent availability even for regions that were partially healthy. We immediately blocked all further configuration changes to prevent additional propagation of the faulty state and began deploying a ‘last known good’ configuration across the global fleet. Recovery required reloading configurations across a large number of nodes and rebalancing traffic gradually to avoid overload conditions as nodes returned to service. This deliberate, phased recovery was necessary to stabilize the system while restoring scale and ensuring no recurrence of the issue.> The trigger was traced to a faulty tenant configuration deployment process. Our protection mechanisms, to validate and block any erroneous deployments, failed due to a software defect which allowed the deployment to bypass safety validations. Safeguards have since been reviewed and additional validation and rollback controls have been immediately implemented to prevent similar issues in the future.So, so far they're saying it's a combination of bad config + their config-validator had a bug. Would love more details.

reply

Aldipower

1 hour ago

 |
root
 |
parent
 |
next

[–]

We have some trouble with the AFD in Germany too.

reply

vinyl7

18 hours ago

 |
prev
 |
next

[–]

Vibe coded internet keeps getting better

reply

avgDev

18 hours ago

 |
parent
 |
next

[–]

Quick find someone who can actually read documentation and code!

reply

the_af

17 hours ago

 |
parent
 |
prev
 |
next

[–]

You just paste the outage error codes back to the LLM and pray it's still working and can fix whatever went wrong!

reply

m_fayer

17 hours ago

 |
root
 |
parent
 |
next

[–]

When all the people forget to code for themselves, every LLM will code itself out of existence with that one last bug. One, after another.

reply

kryogen1c

17 hours ago

 |
prev
 |
next

[–]

downdetector reports coincident cloudflare outage. is microsoft using cloudflare for management plane, or is there common infra? data center problem somewhere, maybe fiber backbone? BGP?

reply

_oleksandr_

14 hours ago

 |
prev
 |
next

[–]

Based on the delay in resolving the issue, it appears MC attempted to rehire some of the DevOps engineers whom AI had previously replaced.

reply

jeffrallen

14 hours ago

 |
parent
 |
next

[–]

They probably hired the ones AWS laid off, causing the AWS outage.

Institutional knowledge matters. Just has to be the right institution is all.

reply

acd

13 hours ago

 |
prev
 |
next

[–]

Putting all your eggs software in one basket

reply

kryogen1c

18 hours ago

 |
prev
 |
next

[–]

downdetector reports coincident cloudflare outage. is microsoft using cloudflare for management plane, or is there common infra? data center problem somewhere, maybe fiber backbone? BGP?

reply

Mr_Bees69

18 hours ago

 |
parent
 |
next

[–]

nope, dont see any cf issues.

reply

ThatManulTheCat

18 hours ago

 |
prev
 |
next

[–]

Yudkowsky's feared Superintellignece holding Azure hostage

reply

bragma

15 hours ago

 |
prev
 |
next

[–]

They suggest to use Traffic Manager to route around failing CDNs. But DNS is not working too, making the suggestion another fail.

reply

rodolphoarruda

15 hours ago

 |
prev
 |
next

[–]

I could not access MS Clarity the entire day.

reply

somerandomness

18 hours ago

 |
prev
 |
next

[–]

yep having trouble logging into
https://entra.microsoft.com/
 as well

reply

llimos

18 hours ago

 |
prev
 |
next

[–]

Yep, down from here too (in Israel).

Services too, not just the portal.

reply

andoma

18 hours ago

 |
parent
 |
next

[–]

Can confirm

reply

I_am_tiberius

17 hours ago

 |
prev
 |
next

[–]

Shouldn't regions be completely independent?

reply

ukblewis

16 hours ago

 |
prev
 |
next

[–]

GitHub also seems to be having trouble for me

reply

howard941

17 hours ago

 |
prev
 |
next

[–]

Took out the archive.ph and .is sites too?

reply

opengrass

17 hours ago

 |
prev
 |
next

[–]

Github Actions and Codespaces degraded.

reply

nextworddev

6 hours ago

 |
prev
 |
next

[–]

Fascinating timing given the APEC summit ;)

reply

uuuubbbb

18 hours ago

 |
prev
 |
next

[–]

Intune, Azure, Entra down in Switzerland

reply

kierenj

18 hours ago

 |
prev
 |
next

[–]

microsoft.com is back -

edit: it worked once, then died again. So I guess - some resolvers, or FD servers may be working!

reply

philipallstar

17 hours ago

 |
prev
 |
next

[–]

Can't get to microsoft.com even.

reply

seinecle

14 hours ago

 |
prev
 |
next

[–]

Can't connect to Claude

reply

jacquesclouseau

16 hours ago

 |
prev
 |
next

[–]

My bet is on a bad config change.

reply

croemer

16 hours ago

 |
parent
 |
next

[–]

They already announced that.

reply

zelias

17 hours ago

 |
prev
 |
next

[–]

Anyone have betting odds on when Google will go down next? Are we looking at all 3 providers having outages in the span of 3 weeks?

reply

xuf

18 hours ago

 |
prev
 |
next

[–]

Down here too (region West Europe)

reply

rluhar

17 hours ago

 |
prev
 |
next

[–]

Looks like AWS is also impacted?

reply

zavec

17 hours ago

 |
parent
 |
next

[–]

Yeah the graph for that one looks exactly the same shape. I wonder if they were depending on some azure component somehow, or maybe there were things hosted on both and the azure failure made enough things failover to AWS that AWS couldn't cope? If that was the case I'd expect to see something similar with GCP too though.

Edit: nope looks like there's actually a spike on GCP as well

reply

estel

17 hours ago

 |
root
 |
parent
 |
next

[–]

It's possibly more likely that people mis-attribute the cause of an outage to the wrong providers when they use downdetector.

reply

zavec

17 hours ago

 |
root
 |
parent
 |
next

[–]

Definitely also a strong possibility. I wish I had paid more attention during the AWS one earlier to see what other things looked like on there at the time.

reply

journal

12 hours ago

 |
prev
 |
next

[–]

one day these outages will cause a starvation.

reply

thewisenerd

17 hours ago

 |
prev
 |
next

[–]

they recently had an incident with front door reachability, wonder if it's back.

QNBQ-5W8

reply

voidpointer2000

18 hours ago

 |
prev
 |
next

[–]

Down in Sweden Central as well (all our production systems are down)

reply

giantg2

18 hours ago

 |
prev
 |
next

[–]

Compare the comments and news coverage on this compared to the AWS outage... pretty telling.

reply

wingless_angel

17 hours ago

 |
prev
 |
next

[–]

Please sort it out, I'll be out of a job tomorrow.

reply

dlcarrier

17 hours ago

 |
prev
 |
next

[–]

We're quickly learning who's relying on a single cloud provider.

reply

Insanity

17 hours ago

 |
parent
 |
next

[–]

Multi cloud is really hard to get right at scale, and honestly not worth the effort for the majority of companies and use-case.

reply

shagie

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Like AWS or GCP?
https://downdetector.com/status/aws-amazon-web-services/
 -
https://downdetector.com/status/google-cloud/

reply

MiguelHudnandez

17 hours ago

 |
root
 |
parent
 |
next

[–]

When you look at the scale of the reports, you find they are much lower than Azure's. seeing a bunch of 24-hour sparkline type graphs next to each other can make it look like they are equally impacted, but AWS has 500 reports and Azure has 20,000. The scale is hidden by the choice of graph.

In other words, people reporting outages at AWS are probably having trouble with microsoft-run DNS services or caching proxies. It's not that the issues aren't there, it's that the internet is full of intermingled complexity. Just that amount of organic false-positives can make it look like an unrelated major service is impacted.

reply

_andrei_

15 hours ago

 |
prev
 |
next

[–]

https://www.reddit.com/r/cscareerquestions/comments/1ojbebq/...

reply

joaomoreno

18 hours ago

 |
prev
 |
next

[–]

Yup, see it as well.

reply

tonymet

14 hours ago

 |
prev
 |
next

[–]

Hello fellow boomers!

I noticed that winget is also down eg.winget upgrade fabric
 Failed in attempting to update the source: winget
 An unexpected error occurred while executing the command:
 InternetOpenUrl() failed.
 0x80072ee7 : unknown error

reply

pred8er

17 hours ago

 |
prev
 |
next

[–]

on the line with msft, they said 4 hours is what they are thinking. a workaround they are saying is to use traffic manager,

reply

widikidiw

13 hours ago

 |
prev
 |
next

[–]

main di jo777 gapernah gagal

reply

m_a_g

14 hours ago

 |
prev
 |
next

[–]

It’s not DNS

There is no way it’s DNSIt was DNS

reply

majnata

17 hours ago

 |
prev
 |
next

[–]

The Azure API is still working though.

reply

patching-trowel

17 hours ago

 |
prev
 |
next

[–]

As of now Azure Status page still shows no incident. It must be manually updated, someone has to actively decide to acknowledge an issue, and they're just... not. It undermines confidence in that status page.

reply

baconbrand

17 hours ago

 |
parent
 |
next

[–]

I have never noticed that page being updated in a timely manner.

reply

charles_f

17 hours ago

 |
parent
 |
prev
 |
next

[–]

It shows that some people have issues accessing the portal.

reply

user3939382

15 hours ago

 |
prev
 |
next

[–]

I know how to fix this but this community is too close minded and argumentative egocentric sensitive pedantic threatened angry etc to bother discussing it

reply

ycombinator_acc

15 hours ago

 |
parent
 |
next

[–]

Aww man you got me curious for a sec there.

reply

user3939382

10 hours ago

 |
root
 |
parent
 |
next

[–]

I’ll roll it out

reply

zingababba

16 hours ago

 |
prev
 |
next

[–]

This brings to mind this ->
https://thenewstack.io/github-will-prioritize-migrating-to-a...

reply

udev4096

16 hours ago

 |
prev
 |
next

[–]

Luckily, no one uses azure and it's fully expected from azure to go down all the time! Keep it up!

reply

amir734jj

16 hours ago

 |
prev
 |
next

[–]

It's DNS

reply

AtNightWeCode

16 hours ago

 |
prev
 |
next

[–]

Earnings report today. A coincidence?

I can at least login to Azure. But several MS sites are down.

reply

okokwhatever

17 hours ago

 |
prev
 |
next

[–]

This cannot be a coincidence

reply

bossyTeacher

17 hours ago

 |
prev
 |
next

[–]

I noticed issues on Azure so I went to the status page. It said everything was fine even though the Azure Portal was down. It took more than 10 minutes for that status page to update.

How can one of the richest companies in the world not offer a better service?

reply

Ylpertnodi

16 hours ago

 |
parent
 |
next

[–]

>How can one of the richest companies in the world not offer a better service?

Better service costs money.

reply

pred8er

17 hours ago

 |
prev
 |
next

[–]

looks like MS completed a failover and things are be recovering slowly

reply

NDizzle

18 hours ago

 |
prev
 |
next

[–]

My best guess at the moment is something global like the CDN is having problems affecting things everywhere. I'm able to use a legacy application we have that goes directly to resources in uswest3, but I'm not able to use our more modern application which uses APIM/CDN networks at all.

reply

rsolva

16 hours ago

 |
prev
 |
next

[–]

So that's why all of our municipality's digital services are down ... utter chaos at the political meeting I attended just now.

reply

siva7

18 hours ago

 |
prev
 |
next

[–]

auth services are down

reply

barpol

18 hours ago

 |
parent
 |
next

[–]

still down

reply

improbableinf

18 hours ago

 |
prev
 |
next

[–]

What a time to be alive!

reply

pred8er

17 hours ago

 |
prev
 |
next

[–]

things seem to be coming back up now

reply

worik

16 hours ago

 |
prev
 |
next

[–]

An important quality of the cloud is that it is always available.

Except that it is not!Interesting times...

reply

llama052

17 hours ago

 |
prev
 |
next

[–]

Just another day with microsoft. Honestly pretty tiring as something is always generally broken.

reply

zzake

17 hours ago

 |
prev
 |
next

[–]

Portal is now accessible, bypassing FDN

reply

AtNightWeCode

16 hours ago

 |
prev
 |
next

[–]

From Azure status page: "Customers can consider implementing failover strategies with Azure Traffic Manager, to fail over from Azure Front Door to your origins".

What a terrible advise.

reply

tonyhart7

16 hours ago

 |
prev
 |
next

[–]

Wtf happen with US east????

reply

bernardo786

17 hours ago

 |
prev
 |
next

[–]

now aws down again?

reply

rawgabbit

18 hours ago

 |
prev
 |
next

[–]

Meanwhile the layoffs continue
https://www.entrepreneur.com/business-news/microsoft-ceo-exp...

reply

ctoth

18 hours ago

 |
parent
 |
next

[–]

Layoffs will continue until uptime improves!

reply

onraglanroad

17 hours ago

 |
root
 |
parent
 |
next

[–]

Now that is actually funny!

reply

FeteCommuniste

17 hours ago

 |
parent
 |
prev
 |
next

[–]

> [Satya Nadella] said that the company’s future opportunity was to bring AI to all eight billion people on the planet.

But what if I don't want AI brought to me?

reply

mring33621

17 hours ago

 |
root
 |
parent
 |
next

[–]

Sounds like someone has a case of the 'Mondays'...

reply

binarymax

17 hours ago

 |
root
 |
parent
 |
next

[–]

The mondAIs

reply

bostik

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You'll have to find another planet.

Although judging by the available transports it will likely be colonized by nazis.

reply

gcanyon

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Real life Pluribus
https://en.wikipedia.org/wiki/Pluribus_(TV_series)

reply

ryandrake

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Like most technology initiative these tech CEOs dream up: You're going to get it and swallow it, whether you want it or not.

reply

the_af

17 hours ago

 |
parent
 |
prev
 |
next

[–]

I especially like how Nadella speaks of layoffs as some kind of uncontrollable natural disaster, like a hurricane, caused by no-one in particular. A kind of "God works in mysterious ways".

> “Microsoft is being recognized and rewarded at levels never seen before,” Nadella wrote. “And yet, at the same time, we’ve undergone layoffs. This is the enigma of success in an industry that has no franchise value.”

 > Nadella explained the disconnect between thriving financials and layoffs by stating that “progress isn’t linear” and that it is “sometimes dissonant, and always demanding.”I've read the whole memo and it's actually worse than those excerpts. Nadella doesn't even claim these were low performers:> These decisions are among the most difficult we have to make. They affect people we’ve worked alongside, learned from, and shared countless moments with—our colleagues, teammates, and friends.Ok, so Microsoft is thriving, these were friends and people "we've learned from", but they must go because... uh... "progress isn't linear". Well, thanks Nadella! That explains so much!

reply

18 hours ago

 |
prev
 |
next

[–]

[deleted]
almosthere

17 hours ago

 |
prev
 |
next

[–]

Reports of Azure and AWS down on the same day? Infrastructure terrorism?

reply

12_throw_away

16 hours ago

 |
parent
 |
next

[–]

> Infrastructure terrorism?

Unless that's a euphemism for "vibe coding", no.

reply

reaperducer

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Reports of Azure and AWS down on the same day? Infrastructure terrorism?

> We have confirmed that an inadvertent configuration change as the trigger event for this issue.Save the speculation for Reddit. HN is better than that.

reply

improbableinf

18 hours ago

 |
prev

[–]

According to downtector.com - both AWS and GCP are down as well. Interesting

reply

jasonjmcghee

17 hours ago

 |
parent

[–]

Don't visit this address.

reply

Consider applying for YC's Winter 2026 batch! Applications are open till Nov 10

Guidelines
 |
FAQ
 |
Lists
 |
API
 |
Security
 |
Legal
 |
Apply to YC
 |
Contact

Search:
