---
title: 'Tell HN: Cloudflare silently injects its analytics when you switch nameservers | Hacker News'
url: https://news.ycombinator.com/item?id=49322107
site_name: hnrss
content_file: hnrss-tell-hn-cloudflare-silently-injects-its-analytics
fetched_at: '2026-08-17T11:22:24.451714'
original_url: https://news.ycombinator.com/item?id=49322107
date: '2026-08-16'
description: 'Tell HN: Cloudflare silently injects its analytics when you switch nameservers'
tags:
- hackernews
- hnrss
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
Tell HN: Cloudflare silently injects its analytics when you switch nameservers
531 points
 by 
stagas
 
17 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
152 comments
A few hours ago I switched my nameservers to Cloudflare in order to enable R2 bucket serving through my own subdomain, and I found out that it silently had injected a JS analytics snippet in my HTML-only JS-free site textlog.cc — I had to go to the Analytics dashboard, Add the site to the analytics and 
then
 disable the snippet. I find this approach entirely invasive, you should opt-in to features like that not have to opt-out. Just a warning out there to folks who might not be aware of this.
 
help

okzgn
 
14 hours ago
 
 | 
next
 
[–]

An alternative: <meta http-equiv="Content-Security-Policy" content="script-src 'self' 
https://only-scripts-allowed-from-here.com
">

This makes the client only load self-hosted scripts, or scripts only from the specified origins, among the other directives CSP allows (e.g. restricting styles, images, frames, etc.):https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP

reply

1vuio0pswjnm7
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

If Cloudflare (CF) has r/w access to the response body, which CF does have by default, then CF can easily modify or remove that <meta> tag. The risk is not abated

The risk of third parties injecting scripts, etc., e.g., analytics, advertising, etc., into response bodies (web pages) is usually cited as a rationale for using HTTPS^1CF somehow avoids the usual objections. CF is a MiTM but few people object1. For example, a data collection, surveillance and advertising services company that operates a www search engine and releases a web browser may not want an ISP to inject scripts, etc., e.g., analytics, ads, etc., into web pages as it might compete with the company's business. As a defense against such ISPs and other third parties that are potential competitors for data collection/surveillance/advertising services, it might favor HTTPS sites in its www search engine results, promote HTTPS at conferences discussing its web browser, etc.

reply

1vuio0pswjnm7
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

FWIW, I operate own DNS (including own custom root.zone) and I MiTM own TLS traffic with a localhost forward proxy. With this setup I get r/w access to response bodies, I add a CSP as an HTTP response header, and a long list of other traffic manipulation. There is no tracking, ads, telemetry, etc. Nothing leaves the computer unless I allow it. Operating DNS plus forward proxy gives me lots of control

Letting Cloudflare (CF) operate DNS and direct traffic through its proxies gives CF controlIt's interesting to see how they use it under market pressures

reply

zmgsabst
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is a tangent, but your setup sounds interesting to me — would you share more about how to configure such for myself?

reply

1vuio0pswjnm7
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Many years ago I started to describe how it works in an HN comment and some reply complained about the idea of terminating TLS, i.e., decrypting, and then re-encrypting. Obviously this sacrifices something, e.g, speed, in order to gain _control_

But this is what Cloudflare does and no one seems to mindLarge companies also do this to protect their LANsI'm not running a CDN, only a small home LAN. I'm only procesing a small amount of traffic on a personal computer. This setup is fast enough for me, it's not slow at allThe basic configuration is generally:1. Configure DNS to point to the local proxy listening address #1, a local address, e.g., using a wildcard in a zone file2. Configure the proxy to terminate TLS, "do stuff", and then forward to proxy UNIX socket path #2 or proxy listening address #23. After doing the stuff, the proxy then sends the traffic over the internetThe "do stuff" part is personal. It depends on what one wants to do. There are seemingly endless possibilitiesIt's not likely the constantly changing configurations I use would be suitable for others. It's all based on personal preferences and usage habitsI rarely use a graphical browser, for exampleI don't make piecemeal remote DNS queries like most www users. (IME, most A RR's stay the same over long periods.) I get bulk DNS data periodicallly from a variety of sources and load it into the proxy's memory. When I make an HTTP request there is either no DNS lookup because I'm using the IP address of the proxy or there is a single, local DNS lookup which returns the address of the proxy. There is no access to remote DNSWhen I first decided to start inspecting own TLS traffic by terminating and re-encrypting, I initially tested the idea using socatAfter I saw that it worked, I started using other software like haproxyI never expected this approach would work well enough but many years have gone by and I'm still using it. The configurations I use are much longer and more complicated than any sample I have ever seen on the wwwIt's funny that Cloudflare is decrypting and re-encryting _other peoples'_ traffic, and this is thought to be AOK, but aside from large companies few people seem interested in doing this with their _own_ traffic on their _own_ computers on their _own_ networksIt can be useful, IMHO

reply

phrotoma
 
0 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Just out of curiosity, which proxy do you use?
dwedge
 
18 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This sounds like exactly the kind of thing I'd waste a weekend setting up but what do you actually do with the decrypted traffic? What do you inject? I know you said it's personal but maybe some basic ideas.

Do you find any websites or services that fail because of cert pinning or similar? Why do you restrict dns caching to periodic intervals, just for external privacy?In terms of the speed I doubt the time to decrypt and encrypt tls is noticeable in modern times, especially given how slow websites have become. It's not like a load balanced website behind cloudflare isn't already doing this 3 times

reply

mlrtime
 
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

How much speed are you actually sacrificing? I'd assume modern hardware can decrypt/encrypt TLS very fast.

Side note: I remember working for a company in early 2000's that had Sparc III 1U servers we had to buy crypto accelerators to do this until I had to convince them to use dell/linux.

reply

okzgn
 
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

Thanks for the background context, very interesting and realistic. Yes, of course it also has read/write access, though I always make sure there’s no interference of that kind. It has only happened to me once, where a binary I hosted on Pages didn't work when downloaded with wget (though that happened several years ago).

reply

pcmaffey
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Also can add "Cache-Control: no-transform" header, which prevents modifying the payload.

reply

hahn-kev
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Does it prevent it? Or just request it? There's no way to enforce that is there?

reply

chrisweekly
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

CF owns it all, coming and going (request handling and response writing), thus can choose how/whether to interpret, ignore, modify or append any headers.

reply

robin_reala
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

script-src 'none' is a more secure solution.

reply

leinwand
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

You are right that Cloudflare enabled these analytics by default for our free plans in Septemeber of last year.

We built Real User Measurement (RUM) into our free plans because it gives site owners actionable performance data they would not otherwise have. It is on by default for free sites fr the reasons we wrote about in the blog post below. It is easy to disable if you don't want it on. All of our paid plans are opt-in only.This also gives free plans access to our Observatory product at no cost. Observatory is a performance-monitoring tool inside the Cloudflare dashboard that combines real user data with simulated lab tests to help you measure and improve your website speed.Blog post:https://blog.cloudflare.com/the-rum-diaries-enabling-web-ana...

reply

oefrha
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Wow, this is ridiculous. Sites that have been running on Cloudflare for a decade+ silently got the treatment. Why the hell was there never a big banner telling me about this? I frequently log into the console.

I get it that by being on the free plan (well I do pay for Registrar), I'm the product, but I also converted employers to paying customers of yours based on goodwill. This just destroyed about all of that, among other things. If I haven't given a damn about "powerful, in-depth monitoring solution that helps you debug and optimize applications" in over a decade, I certainly won't suddenly be "excited" about it when you sneakily inject it.

reply

justsomehnguy
 
59 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You can contract your comment to "I'm the product" and nothing would actually change.

reply

mlrtime
 
34 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You get something for free, they announce it and you complain about not having a bigger announcement?

If they had the banner and you missed it [or someone else] they would complain about the banner not being big enough.

reply

oefrha
 
21 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> they announce it

Forgive me for not subscribing to their blog? That's not how you announce changes to customers.Using a Level 7 CDN is based on trust. This is not a trustworthy action, period.

reply

tredre3
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If RUM is such a good thing, why is it opt-in for paid users? Why push this gracious gift only onto free users?

reply

socalgal2
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Just guessing.

* Cloudflare is giving you a "free" service - they'd like something in return. Seems reasonable to me* Paid customers are usually business that have different needs, on average, than free customers

reply

tacitusarc
 
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

I have broadly good feelings about Cloudflare but this warrants a response.

reply

anon7000
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Because paying business customers are a lot more sensitive to this type of change rolling out. They are particular about how they want their shit hosted. Which is totally fair. People on the free tier probably a lot more interested in free benefits and care less about a little change in their hosting.

reply

cryptonym
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Cloudflare needs the data. Useful to validate the impact of changes, build marketing content... Using the free tier for this is fair, they let you opt out, they give you a dashboard.

If someone is mad, maybe they should pay or use a different architecture.

reply

whilenot-dev
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> this is fair, they let you opt out, they give you a dashboard

So they give you something else you didn't ask for and therefor it's "fair"? I think it's pretty dubious to extend services with such data collecting features without informing affected users first, and making it clear how to opt-out before its deployment. A blog post won't do, no.

reply

cryptonym
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You are not paying and it's a business. They need to get something from this deal and they'll maximize it: marketing, data, upselling...

Collecting RUM and giving you the opportunity to turn it off is not that bad for a free service.Makes me wonder if their stuff is GDPR-compliant without consent. If not, then ok, maybe that's bad to turn it on by default.

reply

hinata08
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Makes me wonder if their stuff is GDPR-compliant without consent.

GDPR service providers and partners do not have to consent. Consent is for the users.Services providers have to tell you when they collect your data, and they will most likely fail to do that if they don't even know their partner injects code.*So you're liable if you host on cloudflare.*Now, they somehow avoid this :>when enabling Web Analytics, you can choose to drop requests from European and UK visitors if you so desire (listed here specifically), meaning we will not collect any RUM metrics from traffic that passes through our European and UK data centers. The version of Web Analytics that will be enabled by default excludes data from EU visitors (this can be changed in the dashboard if you want).By default, it is only enabled for visitors from out of the EU, like so many services that respect your privacy and your concerns are their first priority

reply

whilenot-dev
 
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

Even on free tiers there are 
Terms of Use
 you'll need to agree to as a user of their services. Like I said, it's dubious to alter a service and collect data without informing the user first, free tier or not.

There's a reason I got emails fromLinkedInregarding its new AI training purposes, and they made it clear how to opt-out and provided a deadline. I'm on a free tier there as well. So I'd question the legality of this even before any discussions about GDPR enter the picture.

reply

cryptonym
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They are not collecting and using your personal data. To me (IANAL), it looks really different from LinkedIn.

GDPR is about legality and covers the LinkedIn case you mention.

reply

whilenot-dev
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> They are not collecting and using your personal data.

Do you see how GDPR doesn't apply, then? ...you're contradicting yourself.I'd still question the legality of the data collection by altering the offered service without properly informing the affected users. Whether GDPR applies doesn't matter, and whether it's a free tier service doesn't matter either. You're a consumer ofCloudflare, so any consumer rights apply.

reply

cryptonym
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

GDPR very much applies.

As a website owner, you are responsible towards your users for data collection (your architectural choices, your responsibility). This was my concern on GDPR.Sibling comment says data collection is disabled in EU.

reply

whilenot-dev
 
4 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Cool, so you went from

> Cloudflare needs the data. [...] If someone is mad, maybe they should pay or use a different architecture.To "they would violate GDPR".Are you ok with that behavior then? And are you basing your ethical decision solely on the current legislation?

Kevcmk
 
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

Shill

reply

cryptonym
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm not a Cloudflare customer and don't intend to actually use their services. To be transparent I got a free account for few experiments. I'm not working for them in any way.

When it's free you know you are being used, collecting data is the game.

reply

hecturchi
 
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

Because if something is free, you are the product.

reply

schubidubiduba
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Not sure what is more appalling. Silently injecting javascript tracking, or writing a marketing-speech response like this without any substance at all

reply

Scaled
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

While bad, this is far from the first problematic cloudflare behavior. They host a lot of sites with illegal content and refuse to action abuse reports. I support legal free speech, but any business who knowingly serves blatant pirate websites really shouldn't be trusted to behave ethically.

reply

stagas
 
15 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That’s cool, make sure I see it however on the onboarding screens. Big green switches (Proxy, Web Analytics) that I have to scroll through to get to the Ok so I can turn them off there.

reply

deaux
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> It is on by default for free sites fr the reasons we wrote about in the blog post below.

Nowhere in the blog post does it give the reasons why it's A. on by default for free sites B. off by default for paid sites.

reply

Puts
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What an amazing display of double speak. The only thing I didn't get is how is the DOW doing?

Btw I remember another time you tried to manipulate the DOM of peoples websites. It lead to Cloudbleed.

reply

dchest
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> measure and improve your website speed

inserts 31KB JavaScript into tiny HTML pages.

reply

jwr
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> "gives site owners actionable performance data they would not otherwise have"

As I understand, the next step will be to inject ads, to give CloudFlare actionable monetization strategies they would not otherwise have.

reply

sunaookami
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Is this even GDPR-compliant?

reply

hinata08
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Rather than count unique IP addresses (requiring storing state about each visitor), we simply count page views that originate from a distinct referral or navigation event, avoiding the need to store information that might be considered personal data.

They don't store IP addresses (but other referral ids that identify users in a different way) ; and they exclude EU visitors by default.You do your opinion

reply

sunaookami
 
8 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Just saw that in the dashboard: "Enable globally", "Exclude EU". Kinda funny (in a bad way)

reply

corford
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

If you're using free hosting and allowing that provider to mitm your origin's traffic, it seems a little naive to assume they wont eventually submit to temptation and start doing something like this.

reply

dchest
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Indeed, 
https://blog.cloudflare.com/the-rum-diaries-enabling-web-ana...

reply

altairprime
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Perhaps it drowned in newslop when announced?

The RUM Diaries: Enabling Web Analytics by Default(2 points, 11 months ago):https://news.ycombinator.com/item?id=45291323(1 point, 11 months ago):https://news.ycombinator.com/item?id=45339321

reply

cromka
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I noticed that there's very little non-AI stuff of value that gets to the front page nowadays

reply

kazinator
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

If you're only using Cloudfare for DNS, but HTTPS connections go directly to your server, how does it inject HTML?

You must be allowing Cloudfare to terminate your HTTPS connections; i.e. using them for actual proxying.

reply

tick_tock_tick
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

The OP doesn't understand what they are configuring they have Cloudflare setup as a proxy.

reply

hackernud3s
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

The orange cloud icon in dns settings, in other words, but that's opt-out too. So yeah - double opt-out I guess.

reply

____tom____
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I have no idea what 'the orange cloud icon' means, as I'm not a CloudFlare used.

But DNS/Name servers do not see HTML traffic, as the above poster mentioned, so it's not obvious how this change would matter.Is it that they are serving their HTML via CloudFlare, and cloudflare is making changing in its serving of their html?

reply

supermdguy
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Cloudflare sets up a reverse proxy as part of their core offering, so by default they can MITM your proxy. The “orange cloud” by a DNS record means it points to their proxy instead of your server.

reply

vickychijwani
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

What a shame. I wasn’t expecting these dark patterns from Cloudflare at all.

reply

hackernud3s
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's how you get DDOS protection / edge delivery, so it's not a dark pattern. I imagine it's the main reason why people would DNS through them in the first place.

reply

vickychijwani
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

An “orange cloud” with no other indication to represent a feature that is enabled-by-default (with implicitly enabled analytics) sounds like quite the dark pattern. The UI makes the DNS record seem to point to A (your entry) but actually points to B (Cloudflare). This isn’t an oversight, it’s an attempt to obfuscate.

Even if the choice to enable it by default makes sense for Cloudflare’s userbase, the implications are hidden and non-obvious.

reply

furyofantares
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's essentially the entire reason to use Cloudflare.

As sibling mentions it is indeed labeled and not just some icon. People just refer to the orange cloud UI for it for convenience and because it makes it easy to spot whether you have it on or not.But regarding the icon, the icon is their company logo, it really is the primary feature. It's also not like you have to go find it in settings to turn it off after adding DNS record, it's part of the form when you add the record (default on, yes), and it's prominent when viewing the record.

reply

mjmas
 
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

The options are actually labelled as 'Proxied' or 'DNS Only', so that is actually quite clear.

reply

kazinator
 
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

I would say that Cloudfare having customers who don't know exactly what they are getting (into) is actually a Cloudfare problem they should take responsibility for.

reply

alt227
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I would say its up to the user to research what they are using.

reply

EtienneK
 
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

That’s not a dark pattern. That’s one of the core reasons to use Cloudflare.

reply

6031769
 
0 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

And of course by extension it is also one of the core reasons not to use Cloudflare.
userbinator
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

This reminds me of the old free hosts that would inject their own scripts/ads on pages hosted by them, but their implementation would do it only after detecting the closing HTML tag (either </body> or </html>, can't remember) and the various tricks to get around it, including omitting the tag (browsers don't care), rAnDoM case tags (some were hardcoding lower or upper and comparing case-sensitively), and messing with the content type and relying on the browser to detect correctly since it didn't inject into other types (not sure how the current browsers will handle that).

reply

Terr_
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

I'm getting flashbacks to Proxomitron, a localhost proxy in the HTTP days when it was also much harder/impossible to make browser plugins.

reply

outlines
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Are you using CF as a proxy or only for DNS? I ask because I just went to check my domains on the dashboard (some purchased a few years ago, one purchased just a couple days ago), and none of them have Web Analytics enabled.

I have all my domains set to DNS only, so no CF proxy. Wondering if that is why?

reply

stagas
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

I just went and switched them to DNS only, they were on Proxy by default, that also should have been opt-in. Maybe I missed the option while switching the nameservers because I did it in a hurry but still.

reply

cortesoft
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I agree it is a bit confusing, but it makes sense if you think about the expected default use case, which is enabling the cloudflare CDN for customers. They expect people to be using their CDN.

I use them for my registrar, because they offer domains at cost and you can’t beat that. But yes, they make it an extra step to use them without using the CDN.Once you figure it out, it is fairly straightforward, though, and you can’t beat the price.

reply

Ayesh
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If a registrar requires you to use their own nameservers, then they are no longer comparable to other registries.

reply

prophesi
 
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

With the supply chain attacks happening in the JS ecosystem, this reminds me to advise against using CDN's.

reply

TiredOfLife
 
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

> that also should have been opt-in.

The proxy is like 99% of why people use Cloudflare

reply

stagas
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

A simple screen when I did the switch that requires explicitly ‘Enable Proxy’ or ‘skip for now’ would have been enough. Also for ‘Enable Analytics’. None of these existed, or not very obvious otherwise I’d seen them.

reply

TiredOfLife
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In the DNS screen there is literally a column "proxy status" with the only color besides black and white being the orange of proxy enabled

reply

neop1x
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

You are using MITM proxy as a service. In addition to analyzing all traffic and blocking legitimate users with captchas, they can inject stuff in there, too.

reply

anon5739483
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Unsuspecting reader: if you think this comment is interesting please search "deCloudflare" and "crimeflare" on the Internet. The repo is abandoned but it's still regularly taken down whenever it's uploaded. Cloudflare is literally the GFW of the world, is involved in a lot of suspicious activities and a huge danger to future of the open web. The company started as an intelligence honeypot service originally got funded by DHS in '08. You can DYOR on how things moved on from there.

This one hasn't been taken out yet:https://gitlab.lain.la/dCF/deCloudflare/-/blob/master/readme...The taken down versions of the repo usually link here:https://en.wikipedia.org/wiki/Wikipedia:Uphill_battles

reply

purpleidea
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Yikes! I see this too:

<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js/v4513226..." integrity="sha512-ZE9pZaUXND66v380QUtch/5sE9tPFh2zg45pR2PB0CVkCtOREv2AJKkSidISWkysEuQ0EH8faUU5du78bx87UQ==" data-cf-beacon='{"version":"2024.11.0","token":"c0859b51a7804ab5a9cc8e9e2b2c4cde","r":1}' crossorigin="anonymous"></script>

reply

kevincox
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Yup, I explicitly had all anaytics turned off. But had a few sites using Cloudflare for caching. Now I'm checking and seeing this on all of them. This is gross and unacceptable. "Caching" does not mean "modifying my site".

reply

zx8080
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

MITM attack, that's what it is. Why is this not in the news? Ah, no one cares.

reply

zeafoamrun
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It takes a lot of trust to let a CDN be able to terminate TLS traffic for you and this doesn't exactly give the warm fuzzies.

reply

reaperducer
 
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

Why is this not in the news?

Good point. There should be a place where hackers can get this kind of news. Some kind of Hacker News place.

reply

chrisweekly
 
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

Adding a RUM beacon for observability / performance metrics capture, as an opt-out feature for free plans (opt-in for paid plans), is not exactly nefarious. Hopefully/presumably there was some communication before the change was rolled out.

reply

matherial
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No. I was on a free plan for years and found out by accident. It's interesting that you set "nefarious" as the bar. I'd simply call it "sleazy".

reply

stackghost
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm not seeing this on my site (if you want to check: 
https://stackgho.st
), are you using their `strict` http settings? I.e. is your server terminating TLS or is theirs?

edit: perhaps it's only for sites added after that policy came into effect

reply

Animats
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

> injected a JS analytics snippet in my HTML-only JS-free site textlog.cc

Cloudflareinjected hostile codeinto a site they are not even hosting? 
If it's HTTPS, how do they even do that?Does it violate the "exceeds authorized access" provision in the Computer Fraud and Abuse Act?

reply

bawolff
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

The most likely answer is the person accidentally enabled the cloudflare reverse proxy without understanding what they were doing.

It seems incredibly unlikely cloudflare does this when just DNS hosting, if for no other reason then that this would break so many things.

reply

MrJohz
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

When you set up CNAME and certain other records in Cloudflare DNS, it defaults to (and heavily discourages you to disable) "proxied" records, which I believe means that the record points to a Cloudflare-owned host which then acts as a reverse proxy to whatever value you'd set. So from the console it looks like you've set the CNAME to a certain value, but in practice it'll be set to a different thing and transparently forward everything via Cloudflare. This is probably where the analytics get inserted, alongside a bunch of other Cloudflare features.

You can disable this, at which point the record will be set as a normal DNS record.I can see the advantage of Cloudflare's proxy systems, but I wish they'd be clearer about when they're being used and not pretend that this is some DNS feature or that records have been set to one thing when they've actually been set to something else. If nothing else, it makes debugging DNS issues a lot more confusing, particularly if you're not a DNS expert.

reply

bawolff
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

On the other hand. Proxying websites (for ddos protection, cdn, etc) is their primary product. Its what they are known for.

I think a better question is: why would you be using cloudflare, if you didn't want that?

reply

fragmede
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There's still a naive expectation that the proxy isn't going to inject invisible content on your site that hits when you realize you were being naive.

reply

gruez
 
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

>I can see the advantage of Cloudflare's proxy systems, but I wish they'd be clearer about when they're being used and not pretend that this is some DNS feature or that records have been set to one thing when they've actually been set to something else. If nothing else, it makes debugging DNS issues a lot more confusing, particularly if you're not a DNS expert.

You could say the same about the reverse, ie. people set up their site on cloudflare, thought it was "protected", but really it's dns only and their servers are wide open. It's even worse if they migrated from another provider that was providing ddos protection.

reply

Aeolun
 
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

> It seems incredibly unlikely cloudflare does this when just DNS hosting

Not to mention impossible when ‘just’ DNS hosting. Though I suppose they could secretly replace the stated IP with one of their own anyway and then still proxy the content.

reply

kazinator
 
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

If this is HTTPS, how would Cloudfare have the certificate for your domain so that browsers don't warn about a mismatch?

Or is it that when you sign over DNS to a provider, they can take over your cert? They can "ass-cert" their own? :)

reply

bawolff
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, the person who controls the DNS controls the certificate.

What a certificate is supposed to verify is that traffic is going to the right place. If you designate cloudflare as the rightful host of your website then they can get a certificate.This isn't an edge case though. This is cloudflare's primary product. It is why users use them.

reply

threecheese
 
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

As far as I know they terminate all TLS; it’s one of the tradeoffs using them.

reply

muvlon
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They have a product called Magic Transit that offers DDoS protection and such for plain IP traffic, where Cloudflare does not terminate TLS. Pricing is not public but starts in the five-digit USD per month range according to people I talk to.

This may tell you something about how keen Cloudflare are to handle traffic they themselves cannot decrypt.

reply

bawolff
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Magic Transit uses BGP magic to work. That only makes sense at scale - i believe you have to have your own ASN for it to work.

Realistically its a totally different product, and 5 digit price is probably cheap relative to competitors in that space.

reply

stagas
 
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

I can’t recall if there was a setting to enable reverse proxy, if there was it was On by default since I didn’t expect to have reverse proxy enabled as well. But you can also rp without injecting a script. That’s overdoing it.

reply

eaf7e281
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If the cloud symbol is orange, it's enabled. I believe they'll even warn you if you disable it, a lot of people enable it unintentionally.

reply

dboreham
 
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

I don't know what happened in this situation but beware that CF and similar providers are not true DNS hosting providers. They do DNS, but only so their CDN stuff works, and to lock their customers from using whatever DNS hosting they want. Various things that one might reasonably want to do with your DNS zone are not possible with their product. So use it only because you need to do so in conjunction with their core services.

reply

Touchnow
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

TLS terminates at Cloudflare, not at your origin. When a record is proxied (the orange cloud), CF holds the certificate the browser validates against and opens a separate connection to your server, so it sees plaintext on both sides and can rewrite the HTML on the way out. Same mechanism that makes the WAF and caching work, so it isn't specific to the analytics feature.

Worth checking which of your records are actually proxied. DNS-only ones (grey cloud) pass straight through and can't be touched.

reply

windexh8er
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Isn't this well known when using CF as a proxy? Not sure how they would provide traffic / DDoS telemetry otherwise.

reply

JoshTriplett
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

They're serving the HTML, they have every ability to track individual web requests without 
modifying the content they're serving
.

reply

sscaryterry
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

100% But this does not give you any 
useful
 personal data :)

reply

JoshTriplett
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Or data for the increasingly invasive Cloudflare captcha.

reply

celsoazevedo
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Yes, they add the js if "web analytics" is enabled. I believe I had to manually enable it on my old sites though. Maybe it's enabled by default when adding new domains?

reply

stagas
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

No, I hadn’t enabled for any site. I had to enable first to turn it off.

reply

nilram
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Maybe send it to them as a bug. Seems more like a mistake than malevolence.

reply

PlotCitizen
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They have a blog post about it so they know what they're doing.

reply

stragies
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Is there an entry in filter-lists used by ublock and other client-side content blockers for `
https://static.cloudflareinsights.com/beacon.min.js/
`?

reply

ValentineC
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Took me a minute to realise this isn't 1.1.1.1 (which Cloudflare also runs), but their original website DNS hosting service.

reply

sparsesignal
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I noticed the same thing with email-decode.min.js on my site. It turns out it's the "Email Address Obfuscation" feature, which I didn't expect to be on by default.

reply

jjcm
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Thank you for this. I indeed had it up on mine. Cloudflare has switched defaults a couple times now, which honestly is wild to me.

reply

the4anoni
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Thank you so much for info about this. Does anyone has list of known "traps" like that on Cloudflare? I only want to use them for proxying my IPv6 website, SSL, and nothing else.

reply

hinata08
 
2 hours ago
 
 | 
parent
 | 
next
 
[–]

Cloudflare used to effectively allow you to block users coming from Tor or proxies, forcing them to chose between not visiting your site or disabling their privacy features. (when Akamai was able to still allow legitimate users)

They do a much better job these days, at least

reply

PlotCitizen
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

There are countless objections to many of the things the Cloudflare is doing. If you only need it for a small number of things perhaps it may be worthwhile to look if at whether there are alternatives to CF for those use cases.

reply

endre
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

you wanted the cloudflare, you got the cloudflare.

reply

BorisMelnik
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

yep, last website I did was JS free 100% except that pesky cloudflare script

reply

minraws
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Is there an opt-out mechanism at least? CF is burning goodwill in months it built over the last decade.

reply

eXpl0it3r
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

If you navigate to the domain itself, then to Analytics > Web Analytics there's a Quick Action for the RUM Settings.

reply

busymom0
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes there is. I have it disabled on mine:

https://limereader.com/

reply

jwr
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Here we go. First, get everyone on the internet to use a free service (nameservers and CDN caching, which BTW is mostly unnecessary for pretty much everyone out there). Then, inject analytics, to "give site owners actionable performance data they would not otherwise have". Then, inject ads.

In the meantime, also implement "bot protection" and get everyone on the internet to outsource the decision on who can access their website. With no appeal.I'm increasingly worried about Cloudflare.

reply

jesterson
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

What else would you expect from Cloudflare?

It this point in time it is somewhere between GoDaddy and RyanAir in dark pattern usage

reply

Symbiote
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

It's not necessary to use Cloudflare hosted DNS to use R2 with a custom subdomain.

Make a CNAME record the same way you would for a CDN subdomain.(I am not yet running this in production, YMMV.)

reply

hackernud3s
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Then you don't get edge cache though, right? And maybe some other features?

reply

johneth
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The benefit of not being MITM'd by Cloudflare is probably worth it in many cases.

reply

moktonar
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Surprise! The man in the middle man-in-the-middles!
This is only the beginning, when you’ll get used to this they’ll do worse and worse, enshittification, remember?

reply

_def
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

If I wouldn't know it better I'd sometimes think some of the big tech shops are just fronts for centralizing the net.

reply

Bender
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don't know what would give anyone that idea. [1]

[1] -https://www.youtube.com/watch?v=a3Xxi0b9trY

reply

LoganDark
 
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

Cloudflare is doing this already. Once they had enough monopoly power, they started a program to block all bots that don't undergo invasive KYC procedures. Eventually, they might become a KYC broker for regular browser users too. The free internet is over.

reply

nephihaha
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Cloudflare will be linked into personal ID soon.

reply

sssilver
 
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

#savetheinternet

reply

cryo32
 
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

That's exactly what they are.

And they can fuck off.

reply

CommanderData
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Personally not sure what the concern is unless you only use Cloudflare for DNS only.

They see everything that passes through their proxy, and if they wanted to perform analysis on a site they're interested in I really wouldn't be surprised if there's a clause in the ToS that allows them to do it.

reply

monitorion
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

We use Cloudflare tunnels for connecting distributed workers to central infrastructure. Haven't seen this on tunnel traffic, but good to know it happens on nameserver-managed sites. Another reason to audit what your CDN injects — same applies to checking your security headers regularly.

reply

pudgywalsh
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

You left out the part about how you use them as a reverse proxy, which is decoupled from DNS. One is coincidental; the other required.

If they can inject script, they can also snoop on all your cleartext traffic without you knowing....

reply

stagas
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Oh gosh I didn’t enable anything like that also. I just wanted the nameservers in order to serve the bucket under my subdomain. What else is there I wonder?

reply

temp0826
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The main reason anyone chooses cloudflare is for their CDN (which I suppose is a "reverse proxy"...not a way I'd refer to it but technically yes that's essentially what it's doing). If you don't need the CDN or any of the other fancy features there are plenty of straight DNS providers out there (and often provided by the registar these days).

reply

stagas
 
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

Ok to turn this off you go Domains → Overview → your.site → DNS → Records → then Edit each entry to DNS Only (gray cloud). MITM gone now (I hope).

reply

kazinator
 
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

OK, how can Cloudfare edit your HTML without it passing through your server?

If the browser connects directly to your web server, how can there be Cloudfare's analytics stuff?Check what IP address you are connecting to when you load textlog.cc. Is that an address that you control? If it's not an address that you control, where is it getting your page, and is that not called proxying?

reply

johntash
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Indeed. I have several domains using cf for dns only and they don't/can't inject anything into those sites.

reply

sebastiennight
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

"can't" is incorrect. As your name server, they can decide to turn the reverse proxy/caching at any point in the future, write an obscure blog post about how this is the best solution for all (a post that gets 2 comments on HN due to other news that week), and you'd only find out about it 11 months later in a thread like this one.

reply

camel_gopher
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Why would they snoop your traffic?

Ah, because they can.

reply

p0w3n3d
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Spies. Spies everywhere

reply

sitzkrieg
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

cloudflare is malware, what did you expect?

reply

fragmede
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

No it's not. You don't have to like them, but malware is "any program or file built to damage, disrupt, or secretly gain access to a computer, phone, or network". Cloudflare is many things, some good, some bad, but they don't secretly gain access to your system, you have to choose to install it, so it's not malware.

reply

hinata08
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

>they don't secretly gain access to your system

They are only "enabling Web Analytics by default" "by providing a powerful, in-depth monitoring solution that helps you debug and optimize applications" when users do not come from the EUCloudflare is doing a great job most of the time, but I feel like this feature was speed run through approvals and could use more discussions

reply

PlotCitizen
 
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

You choose to install it on your website if you own a website, but if you're surfing the world wide web, then a lot of the places you visit are increasingly being gatekept/hidden behind Cloudflare pages meant to "challenge" you if you take anti-fingerprinting measures.

Presumably these include any measures which would counter their operating model of tracking users on the web, under the excuse of stopping bots.

reply

csomar
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

To add to your experience: It was also very hard, for me, to find the setting that disables this JavaScript.

reply

denkmoon
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Maybe don't use CF if you don't want someone fucking with what you're serving. It's their entire raison detre.

reply

sebastiennight
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

A public service reminder to anyone setting up their domains that there are many alternatives to Cloudflare, like EG Bunny.net (I am not affiliated, just a happy customer) and that by using one of these other DNS providers, you

- play your small part in keeping the Internet open- delay or avoid entirely the enshittification that is 100% foreseeable when buying the "free" services of a quasi-monopoly vendor.If you're not an enterprise customer, alternate providers will also give you every single feature you could ever need and more, and fewer surprises like the OP's.

reply

mbravorus
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

if you aren't paying, you aren't buying

reply

deadbabe
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Why do people care? This is hardly anything malicious.

reply

eXpl0it3r
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Hardly anything malicious ... yet and even that's debatable.

Yes, when you proxy anything through Cloudflare (CF) you give up on having your contents encrypted as CF terminates the TLS endpoints, but going from this to changing the content of the served site and injecting JavaScript is quite a big step and likely not what a lot of people would want nor expect. Your JavaScript-free site becomes a site that ships JavaScript without you knowing or having done anything.Additionally, this introduces additional tracking of users, which a lot of people don't want.And finally, there's the slippery slope. Today it's RUM, tomorrow it's ads or something else? Once CF starts modifying the user's content, what's stopping them from doing it more and more?

reply

yogorenapan
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Noticed this the other day as well. Sketchy as fuck. I didn't have analytics enabled. I had to go and enable to get access to the option to turn this off

reply

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