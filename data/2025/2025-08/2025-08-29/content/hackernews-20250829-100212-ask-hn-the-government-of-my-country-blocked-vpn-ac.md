---
title: 'Ask HN: The government of my country blocked VPN access. What should I use? | Hacker News'
url: https://news.ycombinator.com/item?id=45054260
site_name: hackernews
fetched_at: '2025-08-29T10:02:12.594823'
original_url: https://news.ycombinator.com/item?id=45054260
author: rickybule
date: '2025-08-29'
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
Ask HN: The government of my country blocked VPN access. What should I use?
643 points
 by
rickybule

7 hours ago

 |
hide
 |
past
 |
favorite
 |
377 comments
Indonesia is currently in chaos. Earlier today, the government blocked access to Twitter & Discord knowing news spread mainly through those channels. Usually we can use Cloudflare's WARP to avoid it, but just today they blocked the access as well. What alternative should we use?

_verandaguy

5 hours ago

 |
next

[–]

Hello! I've got experience working on censorship circumvention for a major VPN provider (in the early 2020s).

- First things first, you have to get your hands on actual VPN software and configs. Many providers who are aware of VPN censorship and cater to these locales distribute their VPNs through hard-to-block channels and in obfuscated packages. S3 is a popular option but by no means the only one, and some VPN providers partner with local orgs who can figure out the safest and most efficient ways to distribute a VPN package in countries at risk of censorship or undergoing censorship.- Once you've got the software, you should try to use it with an obfuscation layer.Obfs4proxy is a popular tool here, and relies on a pre-shared key to make traffic look like nothing special. IIRC it also hides the VPN handshake. This isn't a perfectly secure model, but it's good enough to defeat most DPI setups.Another option is Shapeshifter, from Operator (https://github.com/OperatorFoundation). Or, in general, anything that uses pluggable transports. While it's a niche technology, it's quite useful in your case.In both cases, the VPN provider must provide support for these protocols.- The toughest step long term is not getting caught using a VPN. By its nature, long-term statistical analysis will often reveal a VPN connection regardless of obfuscation and masking (and this approach can be cheaper to support than DPI by a state actor). I don't know the situation on the ground in Indonesia, so I won't speculate about what the best way to avoid this would be, long-term.I will endorse Mullvad as a trustworthy and technically competent VPN provider in this niche (n.b., I do not work for them, nor have I worked for them; they were a competitor to my employer and we always respected their approach to the space).

reply

teeray

3 hours ago

 |
parent
 |
next

[–]

> First things first, you have to get your hands on actual VPN software and configs.

It would be nice if one of the big shortwave operators could datacast these packages to the world as a public service.

reply

ianburrell

30 minutes ago

 |
root
 |
parent
 |
next

[–]

There isn't enough bandwidth in HF to transmit data. Digital HF audio is 20 kHz wide so maybe 50kbps. The entire HF band is only 3-30 MHz.

reply

mfiro

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

The problem is the countries, which censor Internet and block VPNs, also jam shortwave radio signals.

reply

DrAwdeOccarim

28 minutes ago

 |
root
 |
parent
 |
next

[–]

I’m not sure that’s super feasible any longer with the advent of cheap SDRs. Over-the-horizon HF broadcast can be heard with a simple speaker wire antenna inside your house. If anyone is interested in trying to deploy such an idea, I’d love to participate as an avid ham.

reply

SahAssar

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

Could I ask for a source on that and how common it is?

Seems like it was used way back in the cold war (and even then not blocked/jammed) and I'd guess that current authoritarian regimes would perhaps not bother considering how few could use it.

reply

bragr

9 minutes ago

 |
root
 |
parent
 |
next

[–]

Source: trust me bro, but you can find HF jamming pretty easily on Internet connected SDRs, especially near "sensitive" countries.

reply

asimovfan

38 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

if it became a widespread practice, wouldnt even the countries that yet dont do it probably start doing it?

reply

downrightmike

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

https://github.com/StreisandEffect/streisand

reply

NamTaf

1 hour ago

 |
root
 |
parent
 |
next

[–]

Streisand is extremely out of date and wouldn’t last long in China, but I don’t know how sophisticated Indonesia’s firewall is

reply

ivanstepanovftw

2 hours ago

 |
parent
 |
prev
 |
next

[–]

This is no 'nothing special' with Obfs4proxy. DPI sees it as random byte stream, thus your government can decide to block unknown protocols. Instead, you should trick DPI into thinking it sees HTTPS. Unless your government decides to block HTTPS.

reply

conradev

0 minutes ago

 |
root
 |
parent
 |
next

[–]

WebRTC is another great option:
https://snowflake.torproject.org

It's used for a lot of legitimate traffic as well, so a bit harder to block

reply

rafram

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

> your government can decide to block unknown protocols

Has any government ever done that? Seems like it would just breakeverything(because the world is full of devices that use custom protocols!) at great computational expense.

reply

commandersaki

42 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

The only VPN technology I see that blends as HTTPS is MASQUE IP Proxying, and the only implementation I know that does this is iCloud Private Relay. It is also trivial to block because blocking 443/udp doesn't really affect accessing the Internet.

reply

artdigital

32 minutes ago

 |
root
 |
parent
 |
next

[–]

Cloudflare WARP (1.1.1.1 tunnel or Zero Trust) run by default on MASQUE

reply

azalemeth

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Thank you very much for a detailed answer. Might I rudely ask -- as you're knowledgeable in this space, what do you think of Mullvad's DAITA, which specifically aims to defeat traffic analysis by moving to a more pulsed constant bandwidth model?

reply

_verandaguy

4 hours ago

 |
root
 |
parent
 |
next

[–]

DAITA was introduced after my time in the industry, but this isn't a new idea (though as far as I know, it's the first time this kind of thing's been commercialized).

It's clever. It tries to defeat attacks against one of the tougher parts of VPN connections to reliably obfuscate, and the effort's commendable, but I'll stop short of saying it's a good solution for one big reason: with VPNs and censorship circumvention, the data often speaks for itself.A VPN provider working in this space will often have aggregate (and obviously anonymized, if they're working in good faith) stats about success rates and failure classes encountered from clients connecting to their nodes. Where I worked, we didn't publish this information. I'm not sure where Mullvad stands on this right now.In any case -- some VPN providers deploying new technology like this will partner with the research community (because there's a small, but passionate formal research community in this space!) and publish papers, studies, and other digests of their findings. Keep an eye out for this sort of stuff. UMD's Breakerspace in the US in particular had some extremely clever people working on this stuff when I was involved in the industry.

reply

paxcoder

3 hours ago

 |
root
 |
parent
 |
next

[–]

Have you heard about Safing's "SPN"? Could you comment on that?

reply

zelphirkalt

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

If you are on a limited data plan, beware, DAITA produces a lot of traffic.

reply

mulchpower

2 hours ago

 |
parent
 |
prev
 |
next

[–]

There are some techniques like fragmented TLS and reordered packets that work in some cases. Also using vanilla HTTPS transport is a good start for many places. URnetwork is an open source, decentralized option that does all of these out of the box. You can get it on the major stores or F-Droid.

reply

77pt77

2 hours ago

 |
parent
 |
prev
 |
next

[–]

Obfs4proxy and Shapeshifter are an absolute PITA to install.

Get your own VPS server (VPS in EU/US with 2GB of ram, 40GB of disk space and TBs/month of traffic go for $10 a year, it's that cheap). Never get anything in the UK and even USA is weird. I'd stick with EU.Install your software (wireguard + obsfuscation or even tailscale with your own DERP server)Another simpler alternative is just `ssh -D port` and use it as a SOCKS server. It's usually not blocked but very obvious.

reply

mrb

1 hour ago

 |
root
 |
parent
 |
next

[–]

In my experience, in China as of 2016, "ssh -D" vasn't reliable at all, I wrote more details at
https://blog.zorinaq.com/my-experience-with-the-great-firewa...
 (see "idea 1")

reply

jquery

34 minutes ago

 |
root
 |
parent
 |
next

[–]

I just spent 3 months in China this summer. The GFW has become much more sophisticated than I remember. I found only one method that reliably worked. That was to use Holafly (an international eSIM provider) and use its built-in VPN. China largely doesn’t care if foreigners get around the GFW, I guess.

Another method that usually worked was ProtonVPN with protocol set to Wireguard. Not sure why this worked, it’s definitely a lot more detectable than other methods I tried. But as long as I rotated which US server I used every few days, this worked fine.No luck with shadowsocks, ProtonVPN “stealth” mode, Outline+Digital Ocean, or even Jump / Remote Desktop. Jump worked the longest at several hours before it became unbearably slow, I’m still not sure if I was actually throttled or my home computer started misbehaving.I didn’t get around to setting up a pure TLS proxy, or proxying traffic through a domain that serves “legitimate” traffic, so no idea if that still works.

reply

extraduder_ire

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

Where are you finding a VPS in the EU for $10/year? Any I've seen are about 5-6 times that much.

reply

danielhep

25 minutes ago

 |
root
 |
parent
 |
next

[–]

Check LowEndTalk and LowEndBox

reply

dannyobrien

22 minutes ago

 |
root
 |
parent
 |
next

[–]

https://lowendtalk.com/

Can recommend. Always a little crazy, always insanely cheap. If it doesn't work out, you can just switch to another provider.

reply

myshoemouth

3 hours ago

 |
parent
 |
prev
 |
next

[–]

I'm curious. How does a state actor do actual DPI without pushing certs to end user devices?

reply

teraflop

3 hours ago

 |
root
 |
parent
 |
next

[–]

The "inspection" part of DPI isn't limited to encrypted payloads. It's straightforward enough to look at application-level protocol headers and identify e.g. a Wireguard or OpenVPN or SSH connection, even if you can't decrypt the payload. That could be used as sufficient grounds to either block the traffic or punish the user.

reply

mrbluecoat

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

Network fingerprinting, like
https://github.com/FoxIO-LLC/ja4

reply

oasisbob

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

DPI refers to a broad class of products which attempt to find signals and categorize traffic according to a ruleset, either to block it or throttle the speeds, etc.

While access to plaintext is useful, it's not required for other rules which are eg looking at the timing and frequency of packets.

reply

dev_l1x_be

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

Because you are leaking information left and right with TCP / DNS and all these basic protocols that powering the internet today. When these were designed people were happy that it worked at all and nobody really tought that it should be state actor proof. Except maybe DJB.
https://www.curvecp.org/

reply

trod1234

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

There are a couple of ways.

The main one is called an Eclipse Attack in cyber circles, and it can be done at any entity operating at the ASN layer so long as they can position themselves to relay your traffic.The adversary can invisibly (to victim PoV) modify traffic if they have a cooperating rootPKI cert (anywhere in the ecosystem) that isn't the originating content provider, so long as they recognize the network signature (connection handshake); solely by terminating encryption early.Without a cert, you can still listen in with traffic analysis, the fetched traffic that's already been encrypted with their key (bit for bit), as known plaintext the math quickly reduces. SNI and a few other artifacts referencing the resources/sites are not part of the encrypted payload.Its more commonly known in a crypto context, but that kind of attack can happen anywhere. It even works against TOR. One of the first instances (afaik) was disclosed by Princeton researches in 2015, under the Raptor paper.

reply

unethical_ban

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

Patterns of data transmission (network behavioral analysis, I just made that term up), analyzing IP and ports, inspecting SSL handshakes for destination site. In short, metadata.

reply

exe34

4 hours ago

 |
parent
 |
prev
 |
next

[–]

I wonder if it can be embedded in a video stream, like a video of a lava lamp that you always have open, but the lsb of ever byte is meaningful.

reply

_verandaguy

4 hours ago

 |
root
 |
parent
 |
next

[–]

That's an interesting idea, and probably something you might be able to achieve with a tool like h26forge.

It's also probably more useful to just have a connection be fully dedicated to a VPN, and have the traffic volume over time mimic what you'd see in a video, rather than embedding it in a video -- thanks to letsencrypt, much of the web's served over TLS these days (asterisks for countries like KZ and TM which force the use of a state-sponsored CA), so going to great lengths to embed your VPN in a video isn't really practical.

reply

hsbauauvhabzb

4 hours ago

 |
parent
 |
prev
 |
next

[–]

I’m curious about what makes it difficult to block a vpn provider long term. You said getting the software is difficult, but can a country not block known vpn ingress points?

reply

_verandaguy

4 hours ago

 |
root
 |
parent
 |
next

[–]

A country can and absolutely will block known VPN ingress points. There are two tricks that we can use to circumvent this:

- Host on a piece of infrastructure that's so big that you can't effectively block it without causing a major internet outage (think: S3, Cloudflare R2, etc). Bonus points if you can leverage something like ECH (ex-ESNI) to make it harder to identify a single bucket or subdomain.- Keep spawning new domains and subdomains to distribute your binaries.There are complications with both approaches. Some countries block ECH outright. Some have no problem shutting the internet down wholesale for a little bit. The domain-hopping approach presents challenges w/r/t establishing trust (though not insurmountable ones, much of the time).These are thing that have to be judged and balanced on a case-by-case basis, and having partners on the ground in these places really helps reduce risk to users trying to connect from these places, but then you have to be very careful talking to then since they couldthemselvesget in trouble for trying to organize a VPN distribution network with you. It's layers on layers, and at some point it helps to just have someone on the team with a background in working with people in vulnerable sectors and someone else from a global affairs and policy background to try and keep things as safe as they can be for people living under these regimes.

reply

shawa_a_a

4 hours ago

 |
root
 |
parent
 |
next

[–]

I've heard of domain fronting, where you host something on a subdomain of a large provider like Azure or Amazon. Is this what you're talking about when you say

> - Host on a piece of infrastructure that's so big that you can't effectively block it without causing a major internet outage (think: S3, Cloudflare R2, etc).How can one bounce VPN traffic through S3? Or are you just talking about hosting client software, ingress IP address lists, etc?

reply

_verandaguy

4 hours ago

 |
root
 |
parent
 |
next

[–]

That's generally for distribution, but yeah, it's a form of domain fronting.

There are some more niche techniques that are _really_ cool but haven't gained widespread adoption, too, like refractive routing. The logistics of getting that working are particularly challenging since you need a willing partner who'll undermine some of their trustworthiness with some actors to support (what is, normally, to them) your project.

reply

jart

12 minutes ago

 |
root
 |
parent
 |
next

[–]

If I understand correctly, refractive routing basically just gets big trustworthy cloud providers to host the VPNs so that third world governments can't block them without blocking the cloud too. It's an unfortunate solution since tech platforms are international entities that should be neutral. When America asks them to take sides and prevent other countries from implementing their desired policies, America is spending the political capital and trust that tech companies worked hard to earn. It's also really foolish of those countries to just block things outright. They could probably achieve their policy goals simply by slowing down access to VPN endpoints.

reply

incrediblesulk

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

I thought a lot of the domain-fronting approaches have largely been closed from policy changes at major CDNs (e.g.
https://techcommunity.microsoft.com/blog/azurenetworkingblog...
) . Or is it still possible through other approaches?

reply

hsbauauvhabzb

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

Sorry I’m referring to WireGuard/ovpn server IPs, not the binaries/configs used to setup a client. Unless you’re talking about fronting for both, but I imagine it is not economical to run a commercial -scale privacy vpn via a cloud provider.

reply

btown

4 hours ago

 |
parent
 |
prev
 |
next

[–]

This makes me wonder: are there "cloud drive virtual sneakernet" systems that will communicate e.g. by a client uploading URL request(s) as documents via OneDrive/SharePoint/Google Drive/Baidu etc., a server reacting to this via webhook and uploading (say) a PDF version of the rendered site, then allowing the client to download that PDF? You effectively use the CDN of that service as a (very slow) proxy.

Of course,https://xkcd.com/538/applies in full force, and I don't have any background in the space to make this a recommendation!

reply

cluckindan

2 hours ago

 |
root
 |
parent
 |
next

[–]

How about IPv6 over S3?

https://xeiaso.net/blog/anything-message-queue/

reply

jack_pp

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

It doesn't apply imo as OP is probably not a high value target of the govt, he just wants to bypass his govt restrictions and I doubt the situation is so bad that the govt will send people physically to deal with people circumventing the block.

Your solution could technically work over any kind of open connection / data transfer protocol that isn't blocked by the provider but it would be an absolute pain to browse the web that way and there are probably better solutions out there.

reply

joshryandavis

3 hours ago

 |
prev
 |
next

[–]

I lived in China for a while and there were several waves of VPN blocks. Also very few VPN services even try to actively support VPN-blocking nations anymore. Any commercial offering will be blocked eventually.

What I settled on for decent reliability and speeds was a free-tier EC2 hosted in an international region. I then setup a SOCKS5 server and connected my devices to it. You mentioned Cloudflare so whatever their VM service is might also work.It's very low profile as it's just your traffic and the state can't easily differentiate your host from the millions of others in that cloud region.LPT for surviving the unfree internet: GitHub won't be blocked and you'll find all the resources and downloads you need for this method and others posted by Chinese engineers.Edit: If you're worried about being too identifiable because of your static IP, well it's just a computer, you can use a VPN on there too if you want to!

reply

redleader55

2 hours ago

 |
parent
 |
next

[–]

The VM instance is good for setting up a VPN tunnel, but it's not good in terms of bandwidth if it's hosted in. Because of DPI capacity, China has a very limited amount of "real internet" bandwidth. A more capable setup is to have one VM on each side of the firewall on an hosting service with peering between inside and outside - Aliyun (Alibaba Cloud) is an example. The "inside" VM could be just "socat UDP4-RECVFROM:<port>,fork UDP4-SENDTO:<remote>:<port>" or something done using netfilter.

Like others commented in this thread, having an obfuscator is a good idea to ensure the traffic is not dropped by DPI.When the inevitable ban comes and your VPN stops working, rotate the IP of the external VPN and update the firewall/socat config to reflect it. Usually, the internal VM's IP doesn't need to be updated.

reply

77pt77

2 hours ago

 |
root
 |
parent
 |
next

[–]

How easy is it to get a VPS in China.

Could HK work?

reply

redleader55

2 hours ago

 |
root
 |
parent
 |
next

[–]

HK "outside" the firewall, for now. It's where you would place the outside VM.

reply

wulfstan

2 hours ago

 |
parent
 |
prev
 |
next

[–]

When I worked in China (not for long periods but frequently enough that the Great Firewall became an irritant) I hosted an OpenVPN server on port 443 and/or port 22 of a server I owned. That worked sufficiently well most of the time.

reply

ykl

2 hours ago

 |
root
 |
parent
 |
next

[–]

This doesn't work anymore; the GFW no longer detects VPN connections by port but instead by performing deep packet inspection to characterize the type of traffic going over every connection. Using this technique in combination with some advanced ML systems, they're able to detect any encrypted VPN connection and cut it off; it's basically not possible to run any kind of outbound VPN connection (even to private servers) from inside of China anymore, and it's usually not even possible to _tunnel_ a VPN connection through some other protocol because the GFW now detects that too.

Stepping back and looking at it from a purely technical perspective, it's actually insanely impressive.Here's a USENIX paper from a few years ago on how it is done:https://gfw.report/publications/usenixsecurity23/en/

reply

rglynn

5 minutes ago

 |
root
 |
parent
 |
next

[–]

So there's a disconnect between what you're saying and what others and myself have experienced in China even recently. You appear to be saying that it's not possible to use a VPN to bypass the GFW, but I apologise if I have misunderstood.

The comments have multiple examples of people successfully bypassing the firewall. I personally just used Mullvad with wireguard + obfuscation (possibly also DAITA) and it just worked. No issues whatsoever.

reply

eqvinox

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

This is what IPsec TFS is for [
https://datatracker.ietf.org/doc/rfc9347/
]

>the focus in this document is to enhance IP Traffic Flow Security (IP-TFS) by adding Traffic Flow Confidentiality (TFC) to encrypted IP-encapsulated traffic. TFC is provided by obscuring the size and frequency of IP traffic using a fixed-size, constant-send-rate IPsec tunnel(If they block a constant rate stream, that'll hit a whole ton of audio/video streaming setups)

reply

kimixa

12 minutes ago

 |
root
 |
parent
 |
next

[–]

So they'll just block any constant rate stream that isn't containing AV data or a whilelisted streaming service.

reply

tracker1

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

Assuming they don't MITM SSH, you should still be able to use something like wireguard over an SSH tunnel. At least I would think.. it's all SSH traffic as far as any DPI listener is concerned, you'd of course need to ensure the connection signature through another vector though.

reply

IshKebab

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

> it's basically not possible to run any kind of outbound VPN connection (even to private servers) from inside of China anymore.

Really? Because the paper you linked says they don't block any TLS connections so you can just run a VPN over TLS:> TLS connections start with a TLS Client Hello message, and the first three bytes of this message cause the GFW to exempt the connection from blocking.

reply

ykl

28 minutes ago

 |
root
 |
parent
 |
next

[–]

Give it a try if you want; it doesn't work. For TLS traffic they track what the connection looks like over time; a TLS connection for normal web traffic versus a VPN connection tunneling through TLS apparently look different enough that they can detect and cut it off.

reply

wulfstan

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

That is impressive. Beyond bonkers, but impressive.

reply

77pt77

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

> it's basically not possible to run any kind of output VPN connection (even to private servers) from inside of China anymore.

What if you run your own HTTPS server that look semi-legitimate and just encapsulate it in that traffic?Can they still detect it?What about a VPS in HK? Is this even doable?

reply

tossit444

28 minutes ago

 |
root
 |
parent
 |
next

[–]

v2ray and similar servers do exactly that, and I would assume they're still working as they're actively developed.

reply

77pt77

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

Which is ridiculous because OpenVPN is trivial to identify, even when over TCP since it's different from "regular" HTTPS/SSL traffic.

Why they chose this I have no idea.You can even port share.443 -> Web server for HTTPS traffic
443 -> OpenVPN for OpenVPN trafficStill trivial to identify and not uncommon for even public WiFi to do so.Since I changed to tailscale+headscale with my own derp server all these issues have disappeared (for now).

reply

bekicot

2 hours ago

 |
parent
 |
prev
 |
next

[–]

GitHub was briefly blocked a couple of years ago in Indonesia. SSH was also blocked briefly by one of the largest mobile providers.

reply

rd07

1 hour ago

 |
prev
 |
next

[–]

I live in Indonesia, and I don't find any recent news that mention X (formerly Twittwr) and or Discord being blocked by the government. The only relevant news from a quick Google search I can find is about the government threatened to block X due to pornography content in 2024.
You can even check for yourself if a domain is blocked by visiting
https://trustpositif.komdigi.go.id/
.

Also for your unability to access the VPN, as far as my experience goes, in the past some providers do block access to VPN. But, I am not experiencing that for at least the last 5 years.So, maybe you can try changing your internet provider and see if you can connect to VPN?

reply

reisse

5 hours ago

 |
prev
 |
next

[–]

You've come to a wrong place to ask. Most people here (judging by recommendations of own VPN instances, Tor, Tailscale/other Wireguard-based VPNs, and Mullvad) don't have any experience with censorship circumvention.

Just look for any VPNs that are advertised specifically for China, Russia, or Iran. These are the cutting edge tech, they may not be so privacy-friendly as Mullvad, but they will certainly work.

reply

tomaskafka

4 hours ago

 |
parent
 |
next

[–]

> Just look for any VPNs that are advertised specifically for China, Russia, or Iran.

If I was working for a secret service for these countries, I would set up many "VPNs that are advertised specifically for x" as honeypots to gather data about any dissidents.

reply

dmantis

4 hours ago

 |
root
 |
parent
 |
next

[–]

It doesn't matter, he should look into the open source protocols that these services use. He doesn't have to use them.

VLESS / v2ray works in Russia, as far as I know.

reply

spinagon

4 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah, I'm using v2less on rented VPS, it's been workin for almost 2 years already (Russia)

reply

khaki54

4 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Just run second VPN inside the honeypotted VPN

reply

refulgentis

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

Mr. Kafka, suspicion is healthy. However, abstraction provides no way forward when faced with practicalities instead of theory. Creates a Kafka-esque situation - anything suitable is by definition unsuitable. Better to focus on practical technical advice.

reply

sebastiennight

2 hours ago

 |
root
 |
parent
 |
next

[–]

I think you might want to read about the Anom phone [0], supposedly encrypting messages for drug dealers to avoid law enforcement, which was actually sold by... the FBI.

[0]:https://www.inc.com/jennifer-conrad/the-fbi-created-its-own-...

reply

refulgentis

52 minutes ago

 |
root
 |
parent
 |
next

[–]

Sir Night: may I ask, what should it mean to me that
some
 businesses are fronts?

I hope I do not present the presence of a dullard unfamiliar with this.

reply

s1mplicissimus

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

I don't see parent abstracting. They are simply pointing out a very real risk, which you don't provide any counter points to. Instead you seem to dismiss their point based on a strawman

reply

cogman10

3 hours ago

 |
parent
 |
prev
 |
next

[–]

IMO, the safest route for an individual with tech competency is to setup a small instance server in the cloud outside your country and use ssh port forwarding and a proxy to get at information you want.

For an example of a proxy servicehttps://www.digitalocean.com/community/tutorials/how-to-set-...That will give you a hard to snoop proxy service that should completely circumvent a government blockaid (they likely aren't going to be watching or blocking ssh traffic).

reply

asqueella

2 hours ago

 |
root
 |
parent
 |
next

[–]

Advanced enough censors (who have DPI) do block or slow down ssh, e.g.:
https://serverfault.com/questions/1122015/ssh-blockedfor-for...

reply

kragen

5 hours ago

 |
parent
 |
prev
 |
next

[–]

VPNs that are advertised are for-profit products, which means:

1. They are in most cases run by national spy agencies.2. They will at leastappearto work,i.e., they will provide you with access to websites that are blocked by the country you are in. Depending on which country's spies run the system, they mayactuallywork in the sense of hiding your traffic fromthatcountry's spies, or they may mark you as a specific target and save all your traffic for later analysis.My inclination is to prefer free (open-source) software that isn't controlled by a company which can use that control against its users.

reply

reisse

4 hours ago

 |
root
 |
parent
 |
next

[–]

Well, you have to host your free open-source VPN software somewhere. And then, (N. B.: technical and usability stuff aside, I'm talking only about privacy bits here) everything boils down to two equally nightmarish options.

First, you use well-known cloud or dedicated hoster. All your traffic is now tied to the single IP address of that hoster. It may be linked to you by visiting two different sites from the same IP address. Furthermore, this hoster is legally required to do anything with your VPN machine on demand of corresponding state actors (this is not a speculative scenario; i. e. Linode literally silently MitMed one of their customers on German request). Going ever further, residential and company IPs have quite different rules when it comes to law enforcement. Seeding Linux ISOs from your residential IP will be overlooked almost everywhere (sorry, Germany again), but seeding Linux ISOs from AWS can easily be a criminal offense.Second, you use some shady abuse-proof hosting company, which keeps no logs (or at least says that) and accepts payments in XMR. Now you're logging in to your bank account from an IP address that is used to seedbox pirate content or something even more illegal, and you still don't know if anyone meddles with your VPN instance looking for crypto wallet keys in your traffic.VPN services have a lot of "good" customers for a small amount of IP addresses, so even if they have some "bad" actors, their IPs as a whole remain "good enough". And, as the number of customers is big, each IP cannot be reliably tied to a specific customer without access logs.

reply

kragen

4 hours ago

 |
root
 |
parent
 |
next

[–]

Tor is a third option, at least as one layer, and seeding Linux ISOs is not, to my knowledge, a criminal offense in any jurisdiction, not even in China. I don't know where you got that idea.

reply

close04

3 hours ago

 |
root
 |
parent
 |
next

[–]

I read that as a euphemism for piracy.

reply

kragen

2 hours ago

 |
root
 |
parent
 |
next

[–]

Pirating Linux ISOs is legal, though.

reply

Gander5739

53 minutes ago

 |
root
 |
parent
 |
next

[–]

Piracy is by definitin illegal, no?

reply

some_random

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

Do you have any evidence for either of these claims?

reply

jack_pp

3 hours ago

 |
root
 |
parent
 |
next

[–]

From gemini.. (edited for brevity)

Kape Technologies Owns: ExpressVPN, CyberGhost, Private Internet Access, Zenmate> is there any suspicion that Kape Technologies is influenced or has ties to the Mossad?Yes, there is significant suspicion and public discussion about Kape Technologies having ties to former Israeli intelligence personnel. While a direct operational link to Mossad has not been proven, the concerns stem from the company's history, its key figures, and their backgrounds....Kape Technologies is owned by Israeli billionaire Teddy Sagi. While Sagi himself does not have a documented intelligence background, his business history, which includes a conviction for insider trading in the 1990s, has been a point of concern for some privacy advocates. The consolidation of several major VPN providers under his ownership has raised questions about the potential for centralized data access.----Sure there isn't directproofbut there wasn't any proof the CIA was driving drug trade while it was happening. Proof materializes when the dust settles on such matters.

reply

Daishiman

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

It is absolutely self-evident that VPNs are considered high-value targets and that all spy agencies invest a chunk of resources to go after high-value targets.

reply

gnfargbl

4 hours ago

 |
root
 |
parent
 |
next

[–]

I would invite you to read again the two claims made, and consider whether your statement actually addresses the veracity of either.

To be a little trite: we all agree that chickens like grain, but it does not follow that a majority of grain producers are secretly controlled by a cabal of poultry.

reply

tiahura

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

For 99% of use cases - piracy and porn, does that matter?

reply

jacobgkau

4 hours ago

 |
root
 |
parent
 |
next

[–]

This thread's not about that 99% use case.

reply

Hizonner

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Hmm. People who recommend widely used approaches, and well-known, well-established providers, "don't have any experience with cenorship circumvention".

So the solution is no-name providers using random ad-hoc hackery, chosen according to a criterion more or less custom designed to lead you into watering hole attacks.Right.

reply

raincole

44 minutes ago

 |
root
 |
parent
 |
next

[–]

It's very sad that every sane and informed comment (like reisse's) has to meet this kind of snarky comment whose only purpose is being snarky on HN.

Perhaps you should stop and think about why people living in countries where governmentsactuallycensor a lot hardly use these "well-established providers" to circumvent censorship. Tip: it's not because they're stupid.

reply

adamfisk

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

@reisse is 100% right. Most people outside of heavily censored regions have no clue what technology is actually used in those countries. The well-known, well-established providers don't actually work in censored regions because:

1) The problem is very difficult and requires a lot of engineering resources
2) It's very hard to make money in these countries for many reasons, including sanctions or the government restricting payments (Alipay, WeChatPay, etc)The immediate response would be: "If the problem is so difficult, how can it be solved if not be well-known, well-established providers?"The answer is simple: the crowdsourcing power of open source combined with billions of people with a huge incentive to get around government blocking.

reply

Hizonner

38 minutes ago

 |
root
 |
parent
 |
next

[–]

> It's very hard to make money in these countries for many reasons

Tor and I2P, for example, don't actually make money anywhere. Which is not to say that they work for any of the users in all of these places, or for all of the users in any of these places.> The answer is simple: the crowdsourcing power of open source combined with billions of people with a huge incentive to get around government blocking.The actual answer is that (a) they're using so many different weird approaches that the censors and/or secret police can't easily keep up with the whack-a-mole, and (b) they're relying on folklore and survivorship bias to tell them what "works", without really knowing when or how it might fail, or even whether it'salready failing.Oh, and most of them are playing for the limited stakes of being blocked, rather than for the larger stakes of being arrested. Or at least they think they are.Maybe that's "solving" it, maybe not.

reply

reisse

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

None of the things I listed are "widely used approaches, and well-known, well-established providers" in the parts of the world where it does matter.

Yeah, maybe V* and derivatives are random ad-hoc hackery, but they also arethewell-known standard now.

reply

Hizonner

3 hours ago

 |
root
 |
parent
 |
next

[–]

> Yeah, maybe V* and derivatives are random ad-hoc hackery, but they also are the well-known standard now.

A lot of people use Telegram and think it's private, too.What about the part about choosing your VPN provider in the waymost likelyto get you an untrustworthy one who's afteryou personally?

reply

Nextgrid

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Furthermore, you can always run another VPN on top of that if you don’t trust the outer one with the actual plaintext traffic.

reply

05

2 hours ago

 |
root
 |
parent
 |
next

[–]

Not on mobile - iOS doesn't support nested VPNs, and neither does stock Android.

reply

arewethereyeta

3 hours ago

 |
parent
 |
prev
 |
next

[–]

Actually I do, we sell a lot of proxy types designed specifically to circumvent such filters. Trojan works great for our Iran and China users:
https://www.anonymous-proxies.net/products/residential-troja...

reply

yogorenapan

5 hours ago

 |
parent
 |
prev
 |
next

[–]

You can always do v2ray -> Mullvad in a docker container routed with gluetun for censorship avoidance and privacy

reply

genericuser256

3 hours ago

 |
parent
 |
prev
 |
next

[–]

I would recommend Psiphon [1,2] most (all?) of their code is open source and their main goal is to get around censorship blocks. They do have some crypto side projects but the main product is very solid.

[1]https://psiphon.ca/[2]https://github.com/Psiphon-Inc

reply

ailun

3 hours ago

 |
parent
 |
prev
 |
next

[–]

Mullvad worked okay in China in June for me. I imagine it will be better in Indonesia with their less sophisticated blocking.

reply

77pt77

2 hours ago

 |
root
 |
parent
 |
next

[–]

This makes no sense.

On the one hand they do DPI with ML.On the other hand a major player is open!Something is not right here...

reply

riehwvfbk

5 hours ago

 |
parent
 |
prev
 |
next

[–]

OP: look into VLESS (and similar). And read up on ntc.party (through Google translate). There are certain VPN providers that offer the protocol.

reply

yogorenapan

5 hours ago

 |
root
 |
parent
 |
next

[–]

I think REALITY is the newer protocol. I remember VLESS being somewhat more detectable

reply

taminka

4 hours ago

 |
root
 |
parent
 |
next

[–]

nah, vless is the protocol, reality is a newer obfuscation method that works over vless

edit: op, protonvpn has a free tier that works in russia, so likely works everywhere, or if you're comfortable with buying a vps, sshing into it and running some commands, look up x-ray, and use on of their gui panels

reply

esosac

4 hours ago

 |
parent
 |
prev
 |
next

[–]

what's wrong with those solutions?

reply

leshenka

2 hours ago

 |
root
 |
parent
 |
next

[–]

Wrong threat model. Solutions like mullvad/proton focus on privacy not breaking the blockade. They have well known entry points and therefore easily blocked. You can play cat and mouse game switching servers faster than censorship agency blocks them (e.g. Telegram vs Roskomnadzor circa 2018 [1]) but that gets expensive and not really focus of these companies.

What you need is open protocols and hundreds of thousands of small servers only known to their owners and their family/friends1:https://archive.is/sxiha

reply

hinkley

5 hours ago

 |
parent
 |
prev
 |
next

[–]

I have a little, maybe enough to be dangerous. SSH won’t be sufficient to avoid all traffic analysis. Everyone can see how much traffic and the pattern of that traffic, which can leak info about the sort of things you’re doing.

If you’re worried about ending up on a list, using things that look like VPNs while the VPNs are locked down is likely to do so.Also… your neighbors in Myanmar didn’t do a lockdown during the genocide and things got pretty fucking dire as a result. People have taken different lessons from this. I’m not sure what the right answer is, and which is the greater evil. Deplatforming and arresting people for inciting riots and hate speech is probably the best you can do to maintain life and liberty for the most people.

reply

logicchains

3 hours ago

 |
root
 |
parent
 |
next

[–]

>Also… your neighbors in Myanmar didn’t do a lockdown during the genocide and things got pretty fucking dire as a result

The genocide in Myanmar was incited _by_ the government there; giving it more power to censor it's citizens' communications would have done absolutely nothing to help the people being genocided. Genocides don't just suddenly happen; the vast majority of genocide over the past century (including Indonesian genocides against ethnically Chinese Indonesians) had the support of the state.

reply

hinkley

1 hour ago

 |
root
 |
parent
 |
next

[–]

This has been simmering for a very long time. The first I heard of it was violence that broke out after the defacement of a Buddhist temple statue. That would have been almost 20 years ago. Buddhists murdering people tends to lead one to ask a lot of questions.

At that time I think the government was hands off, let it happen rather than tried to stop it.Regardless of who was behind the violence, the whole region has thought about what to do in such situations and they aren’t the same answers the West would choose.

reply

wat10000

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Mullvad worked OK in China for me recently. Sometimes I'd have to try a few different endpoints before it worked. Something built specifically to work in those places would probably be better, but it wasn't too much trouble. Not necessarily a recommendation, just sharing one data point.

reply

Liftyee

5 hours ago

 |
root
 |
parent
 |
next

[–]

I remember always needing obfuscation enabled in Mullvad, but it would work in the end (as you said, after trying a few endpoints).

reply

more_corn

3 hours ago

 |
parent
 |
prev
 |
next

[–]

^ this comment is right on. The cutting edge of VPN circumvention is the one marketed to people in China. Last I poked at this there were a lot of options.

reply

johnisgood

3 hours ago

 |
root
 |
parent
 |
next

[–]

Can I have a list of these options?

reply

degamad

59 minutes ago

 |
root
 |
parent
 |
next

[–]

Despite its silly name, the reddit forum r/dumbclub is probably the place to start, they are focused on GFW-related discussions.

https://old.reddit.com/r/dumbclub/

reply

girvo

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

v2/Vless

reply

mrtesthah

5 hours ago

 |
parent
 |
prev
 |
next

[–]

https://www.reddit.com/r/dumbclub/

reply

NamTaf

30 minutes ago

 |
prev
 |
next

[–]

I work often in China. I somehow haven’t had my WireGuard VPN back to my own home server blocked, yet. It’s pointed to a domain that also hosts some HTTPS web services so that might help.

Prior to this, pre-Covid I used to use shadowsocks hosted on a DO droplet. Shadowsocks with obfs, or a newer equivalent (v2ray w/ vmess or vless protocol) and obfs (reality seems to be the current hotness) will probably work within Indonesia given their blocking will be way less sophisticated than China. The difference here is that it’s a proxy, not a VPN, but it makes it a lot easier to obfuscate its true nature than a VPN which stands out because obfuscation isn’t in its design.Hosting on big public VPSs can be double edged. On one hand, blocking DO or AWS is huge collateral. On the other, it’s an obvious VPN endpoint and can help identify the type of traffic as something to block.If you have access to reddit, r/dumbclub (believe it or not) has some relatively current info but it’s pretty poor signal to noise. Scratch around there for some leads though.Note that this stuff is all brittle as hell to set up and I usually have a nightmarish time duct-taping it all together. That’s why I’m overjoyed my WireGuard tunnel has worked whenever I’ve visited for a year now.One other left-field option, depending on your cost appetite, is a roaming SIM. Roaming by design tunnels all data back to your own ISP before routing out so even in China roaming SIMs aren’t blocked. It’s a very handy backup if you need a clear link to ssh into a box to set up the above, for example.

reply

nomilk

6 hours ago

 |
prev
 |
next

[–]

Australia and UK might soon go down this path.

Something quite depressing is if we (HN crowd) find workarounds, most regular folks won't have the budget/expertise to do so, so citizen journalism will have been successfully muted by government / big media.

reply

GlacierFox

5 hours ago

 |
parent
 |
next

[–]

I would have laughed in your face if you wrote this comment merely 6 months ago. Now I'm just depressed. (UK)

reply

isaacremuant

3 hours ago

 |
root
 |
parent
 |
next

[–]

Don't worry. You'll call us conspiracy theories once you get used to the new goalposts and we warn you about the next thing.

How about instead of being depressed you start being vocal and defiant?

reply

GlacierFox

33 minutes ago

 |
root
 |
parent
 |
next

[–]

You know what, I think I've become lethargic after all the backwards garbage going on in my country attacking my way of life on all fronts - from rampant crime to government censorship.
Your comment just gave me a kick up the ass. I'm gonna try and get some local stuff going in opposition to this lunacy.

reply

jll29

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

When ES leaked his info to the Guardian people, they could still (2013) use the Guardian's US base to publish, protected by the US' stronger freedom of speech laws. Now, in 2025, if the same were to happen again, I'm not sure that would work quite the same way, with Trump aggressively taking American citizens' rights away.

Maybe The Guardian should open a branch in Sealand...

reply

SlowTao

2 hours ago

 |
root
 |
parent
 |
next

[–]

It was David Graeber that said we should be wary of places like The Guardian. They are a wolf in sheeps clothing. Used a lot of the more liberal momentum of the early 2010s combined with promoting some of the more left leaning writters to gain a fair bit of clout. But underneath, they will conform to the power structures if it comes down to survival. Alas, they nay not be a Sealand edition although that would be neat.

reply

SlowTao

2 hours ago

 |
parent
 |
prev
 |
next

[–]

In oz personally and yes, I warned folks of this a few years back, especially in the 12 months or so. Every time I was met with a fair bit of push back.

They would argue back on technical merits, I was talking political, a politics doesn't give a damn about the tech. We have slowly been going down this path for a while now.“The laws of mathematics are very commendable, but the only law that applies in Australia is the law of Australia,” - PM Malcolm Turnbull in 2017.

reply

dijit

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Don't worry, you shouldn't underestimate the capability of society.

I grew up in a pretty deprived area of the UK, and we all knew "a guy" who could get you access to free cable, or shim your electric line to bypass the meter, or get you pirated CD's and VHS' and whatever.There will always be "that guy down the pub" selling raspberry pi's with some deranged outdated firmware that runs a proxy for everything in the house or whatever. To be honest with you, I might end up being that guy for a bunch of people once I'm laid off from tech like the rest. :)

reply

int_19h

4 hours ago

 |
root
 |
parent
 |
next

[–]

Normally I would agree with you, but the ability to pull this kind of thing off hinges on there being enough shadows that the Eye doesn't look at for prolonged periods of time. And the overall trajectory of technological advance lately is such that those shadows are rapidly shrinking. First it was the street cameras (and UK is already one of the most enthusiastic adopters in the world). And now comes AI which can automatically sift through all the mined data, performing sentiment analysis etc. I feel that the time will come pretty soon when "a guy" will need to be so adept at concealing the tracks in order to avoid detection that most people wouldn't have access to one.

reply

dijit

4 hours ago

 |
root
 |
parent
 |
next

[–]

I wouldn’t worry about it.

They can barely handle wolf-whistlers let alone pedophile rape gangs consisting of the lowest IQ dregs of our society.I know it’s only painfully stupid people who think the law is stupid, but dodgy Dave down the way tends to fly under the radar. Otherwise there wouldn’t be so many of them.

reply

alisonatwork

1 hour ago

 |
root
 |
parent
 |
next

[–]

One of the problems with authoritarianism is that even though most dodgy Daves will be fine because the political apparatus doesn't have the time or energy to arrest everyone for everything, they retain the ability to arrest anyone for anything.

The moment your dodgy Dave offends your local cadre, even for reasons entirely other than being dodgy, they'll throw the book at him. And because there is now unpredictability around who will be arrested and for what reason, it acts as a chilling effect for everyone who values some degree of stability in their lives. So the arc of dodgy Daves bends toward compliance.

reply

nomilk

1 hour ago

 |
root
 |
parent
 |
next

[–]

Very well explained

reply

ljsprague

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

It's not that they couldn't handle the rape gangs; it's that they turned a blind eye towards them.

reply

isaacremuant

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

The eye doesn't care as long as you're not politically efficient in opposing their narratives or power.

Authoritarianism in the UK doesn't correlate with crime. The economy does.The point of these things is not really to help citizens. "there's no money for that" like there's no money for healthcare or education (although there is for bombings in foreign countries). The point is protecting power from any threat that could mount against it.

reply

SlowTao

2 hours ago

 |
root
 |
parent
 |
next

[–]

I think both sides of this are fair. Power is interested in stability of itself, to keeps its back to the wall so that nobody can sneak up on it. But also political power has teamed up with corporate power/determination to create a far more nasty beast.

Seeing companies like Palantir (and many lesser known ones) buddy up to everyone that wants it, its a clear statement on how they want to monitor and control the populace.Long term I don't think it can be done, but the pain mid term can be vast.

reply

primitivesuave

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

I suppose that for this case, an underground black market of VPN providers might emerge - average individuals setting up VPN software on a cloud service provider, and then selling monthly access to people. Aside from the obvious danger of getting ripped off (someone might put you on a slow shared VPN with many other people, or shut down the server at any time), there is also the possibility of someone monitoring all your Internet activity.

reply

nomilk

2 hours ago

 |
root
 |
parent
 |
next

[–]

I'd default assume black market VPNs
will
 monitor internet activity since it's both easy and profitable

reply

jama211

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

That absolutely sounds like a world I should be worried about, where our only choices are dodgy ones

reply

Ray20

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

Don't worry, you shouldn't underestimate the capability of society.

You should be worried. Don't underestimate the capabilities of the government bureaucrats. That "guys down the pub" will quickly disappear once they start getting jail time for their activities.

reply

doix

4 hours ago

 |
root
 |
parent
 |
next

[–]

I think you really overestimate the capability of the UK to enforce laws. Yes, they can write them and yes they can fine large corporations, that's basically it.

They cannot enforce laws against such "petty" crimes, the reason society mostly functions in the UK is because most people don't try to break the law.Pretty sure the local punters would kick the cops out if they came for one of their own, especially if he got them their porn back.

reply

wiredpancake

37 minutes ago

 |
root
 |
parent
 |
next

[–]

What do you mean? They already arrest thousands of people a year for posting (or even retweeting) things online in the UK.

What makes you think, if the Gov was to implement some sophisticated DPI firewall that blocks a million different things, they won't come after the people who circumvent it? They already enforce petty crimes. I could report you for causing me anxiety and you would have a copper show up at your door.

reply

Ray20

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

It's not just about UK abilities to enforce laws, but also about other factors. The described activities are extremely unattractive as criminal: small market, small margin, the need for planning, preparation and qualification.

There is no need for special efforts to enforce the law. Put a few people in jail - and everyone else will quickly find safer and more legal ways to spend their time. No one will do something like that unless they are confident of their impunity.

reply

mikestorrent

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

Yes, it's also dystopian to pin one's future on such hopes. People need to stick it to the government and demand their freedoms. Far too many things are being forced on us in the West that go against fundamental values that have been established for centuries.

Somehow, things that could be unifying protests where the working class of every political stripe are able to overlook their differences and push back against government never seem to happen. It is always polarized so that it's only ever one side at a time, and the other side is against them. How does that work?

reply

nemomarx

4 hours ago

 |
root
 |
parent
 |
next

[–]

Reflex. People's opinion on a subject changes if you tell them which political group supports it, sometimes even if they get asked twice in a row. Tribal identity determines ideology more than the other way around for a lot of people.

So as soon as Labour comes out for something, Cons are inclined to be against it and so on. The only way to have neutral protests is if no one visibly backs them and they don't become associated with a side, but then how do they get support and organization?

reply

isaacremuant

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

> People need to stick it to the government and demand their freedoms.

It will only work if they admit that they supported this and all forms of totalitarianism during COVID. You can't fall for that and then be surprised when the world keeps going down that obvious path.

reply

multjoy

2 hours ago

 |
root
 |
parent
 |
next

[–]

In matters of public health, you cannot trust the public to do the right thing.

The problem with covid is that we weren't totalitarian enough. Regulations you could drive a coach & horses through and no way to enforce is a sop.The first lock down needed to be a proper 'papers, please' affair. When we get a properly lethal pandemic, we're fucked. Hopefully Laurence Fox and Piers Corbyn will catch it quickly and expire in a painful and televised way, it's the only hope of people complying with actual quarantine measures.

reply

hdgvhicv

5 hours ago

 |
parent
 |
prev
 |
next

[–]

90% of “citizen journalism” is nothing of the sort. Just like “citizen science” researching vaccines.

reply

nomilk

5 hours ago

 |
root
 |
parent
 |
next

[–]

> 90% of “citizen journalism” is (trash)

You're right. Butcompared to what?I guess99%of mainstream "journalism" is irrelevant and/or inaccurate, hence citizen journalism is a 10x improvement in accuracy and relevancy! Not 10% better, 900% better! This makes ahugedifference to our society as a whole and in our daily lives!But this misses the most important point which is that the user should have the right to choose for themselves what they say and read. Making citizen journalism unduly burdensome deprives everyone of that choice.

reply

RansomStark

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

Preach comrade!

Those citizen journalists with their primary sources, disgusting.Thats nothing but propaganda.Remember it doesnt matter what the video shows, it only matters who showed it to you.

reply

p_j_w

2 hours ago

 |
root
 |
parent
 |
next

[–]

> Remember it doesnt matter what the video shows, it only matters who showed it to you.

Both matter.

reply

Barrin92

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

>Remember it doesnt matter what the video shows, it only matters who showed it to you

In an age of mass media (where there's a video for anything) or now one step further synthetic media knowing who makes something is much more important than the content, given that what's being shown can be created on demand. Propaganda in the modern world is taking something that actually happened, and then framing it as an authentic piece of information found "on the street", twisting its context."what's in the video" is now largely pointless, and anyone who isn't gullible will obviously always focus on where the promoter of any material wants to direct the audiences attention to, or what they want to deflect from.

reply

anigbrowl

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

You really think someone would do that? Just go on the internet and tell lies?

reply

logicchains

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

Citizen journalism avoids the main weakness of a centralised system: it's incredible suspectible to capture. A prime example of this is the mass opposition around the world to Israel's genocide in Gaza. Israel committed such genocides prior to the event of social media, such as the Nakba, but it was rarely reported on, due to media ownership being concentrated in the hands of a few pro-Zionist individuals.

reply

JustExAWS

5 hours ago

 |
parent
 |
prev
 |
next

[–]

I am just waiting for red states in the US to try this too since their current laws requiring ID verification for porn sites aren’t effective.

reply

curiousgal

4 hours ago

 |
root
 |
parent
 |
next

[–]

> red states

Well you'd be surprised to find out that this stupid policy (and many more) have been brought forward by Labour (Left).

reply

mikestorrent

4 hours ago

 |
root
 |
parent
 |
next

[–]

At this point, anyone who has been watching politics for a few decades understands that the left/right dichotomy is primarily one designed to keep the majority of people within a certain set of bounds. We see it revealed when politicians and ideologies that should be in opposition to one another still cooperate on the same strategies, like this one.

The goal right now is to make online anonymity impossible. Adult content is the wedge issue being used to make defending it unpalatable for any elected official, but nobody actually has it as a goal to prevent teenagers from looking at porn - if they did, they would be using more direct and efficient strategies. No, it's very clear that anonymous online commentary is hurting politicians and they are striking back against it.

reply

int_19h

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

It has been my impression that in UK, both parties are strongly authoritarian, with the sole difference being what kinds of speech and expression, precisely, they want to police.

reply

cherryteastain

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

Labour supported it but it was proposed and passed by Parliament in 2023 during the Tory government

reply

nomilk

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

Both the major Australian parties (Liberal and Labor) seem as spineless as each other.

They're being pushed by media conglomerates News Corp and Nine Entertainment [0] to crush competition (social media apps). With the soon-to-be-introduced 'internet licence' (euphemism: 'age verification'), and it's working. If they ban VPN's, it will make social media apps even more burdensome to access and use.[0] News Corp and Nine Entertainment together own 90% of Australian print media, and are hugely influential in radio, digital and paid and free-to-air TV. They have alotto gain by removing access to social media apps, where many (especially young) people get their information now days.

reply

SlowTao

2 hours ago

 |
root
 |
parent
 |
next

[–]

How long until they produce an generative AI version of Burt Newton to do new episodes of 20 to 1 based on some social media slop?

Yep, not a great time line here.

reply

SlowTao

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

Yep, here in Australia the social media age restriction was pushed through by both sides. Two sides of the same coin.

reply

Humorist2290

6 hours ago

 |
prev
 |
next

[–]

- Tor. Pros: Reasonably user friendly and easy to get online, strong anonymity, free. Cons: a common target for censorship, not very fast, exit nodes are basically universally distrusted by websites.

- Tailscale with Mullvad exit nodes. Pros: little setup but not more than installing and configuring a program, faster than Got, very versatile. Cons: deep packet inspection can probably identify your traffic is using Mullvad, costs some money.- Your own VPSs with Wireguard/Tailscale. Pros: max control, you control how fast you want it, you can share with people you care about (and are willing to support). Cons: the admin effort isn't huge but requires some skill, cost is flexible but probably 20-30$ per month minimum in hosting.

reply

codethief

5 hours ago

 |
parent
 |
next

[–]

> - Tailscale with Mullvad exit nodes

Tailscale is completely unnecessary here, unless OP can't connect to Mullvad.net in the first place to sign up. But if the Indonesian government blocks Mullvad nodes, they'll be out of luck either way.> - Your own VPSs with Wireguard/TailscaleKeep in mind that from the POV of any websites you visit, you will be easily identifiable due to your static IP.My suggestion would be to rent a VPS outside Indonesia, set up Mullvad or Tor on the VPS and route all traffic through that VPS (and thereby through Mullvad/Tor). The fastest way to set up the latter across devices is probably to use the VPS as Tailscale exit node.

reply

jkaplowitz

4 hours ago

 |
root
 |
parent
 |
next

[–]

Tailscale + Mullvad does have a privacy advantage over either one by itself: the party that could potentially spy on the VPN traffic (Mullvad) doesn’t know whose traffic it is beyond that it’s a Tailscale customer. Any government who wanted to trace specific traffic back to OP would need to get the cooperation of both Mullvad and Tailscale, which is a lot less likely than even the quite unlikely event of getting Mullvad to cooperate.

reply

zargon

6 hours ago

 |
parent
 |
prev
 |
next

[–]

> 20-30$ per month minimum in hosting

Typo? Wireguard-capable VPSes are available for $20-$30 per year. (https://vpspricetracker.com/is a good site for finding them.)

reply

Humorist2290

6 hours ago

 |
root
 |
parent
 |
next

[–]

I mean multiple VPSs for redundancy. Contabo is maybe the cheapest I've seen and it's like 3$ mtl for the smallest?

reply

Humorist2290

6 hours ago

 |
parent
 |
prev
 |
next

[–]

And using another VPN like NordVPN or ProtonVPN is probably in the same category as Mullvad, but worth being cautious. If it's free, you are the product. If you pay, you're still sending your traffic to a publicly (usually) known server of a VPN. That metadata alone in some jurisdictions can still put you in danger.

Stay safe

reply

weinzierl

5 hours ago

 |
parent
 |
prev
 |
next

[–]

This is good overview, I just wanted to add that a VPS IP is not a residential IP. You will encounter roadblocks when you try to access services if you appear to be coming from a VPS. Not that I had a better solution, just to clarify what you can expect.

reply

vaylian

6 hours ago

 |
parent
 |
prev
 |
next

[–]

Tor also has anti-censorship mechanisms (snowflakes, ...). Depending on how aggressive the blocking is, Tor might be the most effective solution.

reply

akho

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Wireguard is not censorship-resistant, and most VPN-averse countries block cross-border Wireguard. Why reply a practical question in an area in which you have no experience?

reply

LeoPanthera

3 hours ago

 |
root
 |
parent
 |
next

[–]

Is it possible to identify wireguard traffic that isn't on a common port?

reply

akho

3 hours ago

 |
root
 |
parent
 |
next

[–]

Yes. Fixed packet headers, predictable packet sizes. I don't know what "a common port" means in relation to wg.

reply

ItsHarper

2 hours ago

 |
root
 |
parent
 |
next

[–]

51820 is the one they use in the docs, that's probably the most common one.

reply

kube-system

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

They mean UDP port 51820

reply

akho

2 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah. Tailscale uses 41641, and you can generally use whatever. I don't think there's any consensus, or majority.

reply

more_corn

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

Because Indonesia is new to the game and might still be catching up. They’re probably playing whackamole with the most common public VPN providers and might not be doing deep packet inspection yet. I worked with someone getting traffic out of Hong Kong a year ago and there was a lot trial and error figuring out what was blocked and what was not. Wireguard was one that worked.

reply

akho

3 hours ago

 |
root
 |
parent
 |
next

[–]

They recommend Tailscale in particular. Tailscale control plane and DERPs (which are functionally required on mobile) will be among the first to go.

Outline (shadowsocks-based) and amnezia (obfuscated wg and xray) both offer few-click install on your own VPS, which is easier than setting up headscale or static wg infrastructure, and will last you longer.Also, you did not answer my "why" question. I'm not sure what question you were answering.

reply

msgodel

6 hours ago

 |
parent
 |
prev
 |
next

[–]

IMO most people should have a VPS even if you don't need it for tunneling. Living without having a place to just leave services/files is very hard and often "free" services will hold your data hostage to manipulate your behavior which is annoying on a good day.

reply

nisegami

6 hours ago

 |
parent
 |
prev
 |
next

[–]

Minimums for a VPS should be closer to $5-10 a month, no?

reply

Humorist2290

6 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah they can be cheap, but I would definitely recommend having at least 3 for redundancy. If one get shut down or it's IP blacklisted you still hopefully have a backup line to create a replacement.

reply

shellwizard

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

No, unless you pay month to month. If you wait till BF you can find some really good deals on sites like lowendspirit

reply

rickybule

6 hours ago

 |
parent
 |
prev
 |
next

[–]

Thank you so much for this. It is very helpful.

reply

dingi

5 hours ago

 |
parent
 |
prev
 |
next

[–]

> cost is flexible but probably 20-30$ per month minimum in hosting.

$4/month VPS from DigitalOcean is more than enough to handle a few users as per my experience. I have a Wireguard setup like this for more than a year. Didn't notice any issues.

reply

cm2187

6 hours ago

 |
parent
 |
prev
 |
next

[–]

or simply RDP into a windows VPS.

reply

nine_k

4 hours ago

 |
prev
 |
next

[–]

XRay / XTLS-Reality / VLESS work rather fine, and is said to be very hard to detect, even in China.

I followed [1] to set up my own proxy, which works pretty fine. More config examples may be helpful, e.g. [2].[1]:https://cscot.pages.dev/2023/03/02/Xray-REALITY-tutorial/[2]:https://github.com/XTLS/Xray-examples/blob/main/VLESS-TCP-XT...

reply

zeropointsh

3 hours ago

 |
parent
 |
next

[–]

The great thing about China's Great Firewall is that really good options to circumvent censorship have been around for a while. Was waiting for someone to bring up XRay! Alternatively, here is a great write up of using V2Ray[1]. May be worth OP looking into, as a blogger I found noted[2] is an alternative to a VPN, and may work.
[1]:
https://www.v2ray.com/en/

[2]:
https://sequentialread.com/v2ray-caddy-to-access-the-interne...

reply

gck1

1 hour ago

 |
parent
 |
prev
 |
next

[–]

Also sing-box [1]. I don't use it for its primary use case of censorship circumvention, but rather for some highly complex routing configurations it supports.

My use case consists of passing some apps on my Android through interface A (e.g. banking apps through my 5G modem), some apps through US residential proxy (for US banks that don't like me visiting from abroad), and all the rest through VPN. And no root required!It's wild that GFW triggered creation of this and nothing like it existed / exists.[1]:https://github.com/SagerNet/sing-box

reply

taminka

2 hours ago

 |
parent
 |
prev
 |
next

[–]

im curious, isn't ALL of your traffic appearing to be to just one website the most obvious giveaway?

reply

akho

1 hour ago

 |
root
 |
parent
 |
next

[–]

*ray clients typically allow configuration of routing. So you can send only blocked stuff through the tunnel; or, in reverse, send some known-working stuff (e. g. local domain) direct. Also works as adblock.

reply

doix

6 hours ago

 |
prev
 |
next

[–]

I'm currently traveling in Uzbekistan and am surprised that wireguard as a protocol is just blocked. I use wireguard with my own server, because usually governments just block well known VPN providers and a small individual server is fine.

It's the first time I've encountered where the entire protocol is just blocked. Worth checking what is blocked and how before deciding which VPN provider to use.

reply

bryanlarsen

6 hours ago

 |
parent
 |
next

[–]

We've had success using wireguard over wstunnel in places where wireguard is blocked.

https://github.com/erebe/wstunnel

reply

vehemenz

3 hours ago

 |
root
 |
parent
 |
next

[–]

This looks great, thanks.

reply

bryanlarsen

2 hours ago

 |
root
 |
parent
 |
next

[–]

I should have mentioned that our use case isn't avoiding government firewalls, it's transiting through broken network environments.

reply

VTimofeenko

5 hours ago

 |
parent
 |
prev
 |
next

[–]

WireGuard by itself has a pretty noticeable network pattern and I don't think they make obfuscating it a goal.

There are some solutions that mimic the traffic and, say, route it through 443/TCP.

reply

daveidol

6 hours ago

 |
parent
 |
prev
 |
next

[–]

Wow, kinda crazy to think about a government blocking a protocol that just simply lets two computers talk securely over a tunnel.

reply

mikestorrent

4 hours ago

 |
root
 |
parent
 |
next

[–]

Well, think about it - almost every other interaction you can have with an individual in another country is mediated by government. Physical interaction? You need to get through a border and customs. Phone call? Going through their exchanges, could be blocked, easy to spy on with wiretaps. Letter mail? Many cases historically of all letters being opened before being forwarded along.

We lived through the golden age of the Internet where anyone was allowed to open a raw socket connection to anyone else, anywhere. That age is fading, now, and time may come where even sending an email to someone in Russia or China will be fraught with difficulty. Certainly encryption will be blocked.We're going to need steganographic tech that uses AI-hallucinated content as a carrier, or something.

reply

roscas

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

That is how you know they haven't got a clue on what they're doing.

reply

Flere-Imsaho

4 hours ago

 |
parent
 |
prev
 |
next

[–]

> surprised that wireguard as a protocol is just blocked.

Honestly this is the route I'm sure the UK will decide upon in the not too distant future.The job of us hackers is going to become even more important...

reply

atmosx

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Cloak + wireguard should work fine on the server side. The problem is that I didn't find any clients for Android and I doubt there are clients for iOs that can (a) open a cloak tunnel and then (b) allow wireguard to connect to localhost...

reply

akho

1 hour ago

 |
root
 |
parent
 |
next

[–]

AmneziaWG is obfuscated, wireguard-based, and has clients for whatever.

reply

wereHamster

4 hours ago

 |
parent
 |
prev
 |
next

[–]

A year ago I was traveling through Uzbekistan while also partly working remotely. IKEv2 VPN was blocked but thankfully I was able to switch to SSL VPN which worked fine. I didn't expect that, everything else (people, culture) in the country seemed quite open.

reply

aabdelhafez

6 hours ago

 |
parent
 |
prev
 |
next

[–]

Same in Egypt.

reply

dmantis

4 hours ago

 |
parent
 |
prev
 |
next

[–]

XRay protocol based VPN worked for me in Uzbekistan when I were travelling there.

Wireguard is indeed blocked.

reply

akho

1 hour ago

 |
root
 |
parent
 |
next

[–]

xray is a proxy. They may have needed an actual VPN.

reply

sintezcs

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Same in Russia

reply

slt2021

4 hours ago

 |
parent
 |
prev
 |
next

[–]

how can they detect it is wireguard, I thought the traffic is encrypted?

how does it differ from regular TLS 1.3 traffic?

reply

dmantis

4 hours ago

 |
root
 |
parent
 |
next

[–]

It's UDP, not TCP (like TLS) and has a distinguishable handshake. Wireguard is not designed as a censorship prevention tool, it's purely a networking solution.

The tunnel itself is encrypted, but the tunnel creation and existence is not obfuscated.

reply

jszymborski

7 hours ago

 |
prev
 |
next

[–]

Mastodon is not easy for regimes to completely block, and most instances won't block you for using Tor. Mastodon saw a huge migration from Brazil when X was blocked there.

https://joinmastodon.org/

reply

barbazoo

5 hours ago

 |
parent
 |
next

[–]

Wouldn't it be easy to block the individual servers, e.g.
https://mastodon.social
?

reply

evulhotdog

5 hours ago

 |
root
 |
parent
 |
next

[–]

There are many instances of Mastodon, and due to its federated nature, you can use any of them to access it, and even host your own.

reply

Ray20

4 hours ago

 |
root
 |
parent
 |
next

[–]

What's stopping them from just blocking them all and continuing to block new ones?

reply

evulhotdog

4 hours ago

 |
root
 |
parent
 |
next

[–]

Nothing is stopping them, but like most things in blocking free speech, it’s a game of cat and mouse.

reply

mayneack

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

The long tail is very long

reply

kragen

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

Sure, but if you have an account on a different server, you can still see things posted on mastodon.social if you have followed someone there.

reply

int_19h

4 hours ago

 |
parent
 |
prev
 |
next

[–]

It would be easy to block on protocol level. Countries that block VPNs usually progress to that level pretty fast once they discover that simple IP blocks don't work.

reply

jszymborski

3 hours ago

 |
root
 |
parent
 |
next

[–]

The traffic looks like any other web page.

reply

int_19h

3 hours ago

 |
root
 |
parent
 |
next

[–]

I doubt that is the case once you do statistical analysis of it.

Advanced VPN tunneling protocols, for example, have to take a lot of special measures to conceal their nature from China's and Russia's deep packet inspecting firewalls.

reply

nneonneo

1 hour ago

 |
prev
 |
next

[–]

An expensive but functional option is to enable roaming on a foreign eSIM. Getting an eSIM is relatively easy. Roaming mobile traffic is routed from the country in which the SIM is from, not the country that you're in, meaning that an eSIM from e.g. an American carrier will not be subject to the censorship in your country.

I've used this on multiple trips to China over the past decade (including a trip last year). You can find carriers that will charge very low (or even no) roaming rates.

reply

gck1

29 minutes ago

 |
parent
 |
next

[–]

Data-only eSIMs (e.g. ones you get from Airalo and apps like that) are not going to cut it though. You need a "full" eSIM that gives you a real number and even then, it's not a guarantee that your traffic will be routed via the country eSIM is from. Tello does route (or rather, exit) via US for example, but it's 2¢/MB.

Chinese forums / blogs have a lot of information about this stuff. I usually ask ChatGPT to translate "Researchtopic re: some form of circumventionand give me forum posts and blog posts about it" to Chinese, then paste that into DeepSeek with search enabled and just let Chrome translate the responses. Does a really good job. At least better than what I can manage with Baidu.

reply

jauntywundrkind

6 hours ago

 |
prev
 |
next

[–]

Nations severing peoples connections to the world is awful. I'm so sorry for the chaos in general, and the state doing awful things both.

Go onhttps://lowendbox.comand get a cheap cheap cheap VPS. Use ssh SOCKS proxy in your browser to send web traffic through it.Very unfancy, a 30+ year old solution, but uses such primitive internet basics that it will almost certainly never fail. Builtin to everything but Windows (which afaik doesn't have an ssh client built-in).Tailscale is also super fantastic.

reply

int_19h

4 hours ago

 |
parent
 |
next

[–]

> uses such primitive internet basics that it will almost certainly never fail.

It already fails in China and Russia. Simply tunneling HTTP through SSH is too easy to detect with DPI.> Windows (which afaik doesn't have an ssh client built-in)It has had both SSH client and SSH server built-in since Win10.

reply

sertsa

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Windows has had both ssh client/server for years

reply

throwawayffffas

50 minutes ago

 |
prev
 |
next

[–]

You can also setup your own, get a VM in the free world and setup an open VPN server.
https://www.digitalocean.com/community/tutorials/how-to-set-...

reply

jszymborski

7 hours ago

 |
prev
 |
next

[–]

Folks who are looking to bypass censorship, and those who live in countries where their internet connection is not currently censored who would like to help, can look to
https://snowflake.torproject.org/

reply

dongcarl

6 hours ago

 |
prev
 |
next

[–]

Give Obscura a try, we get around internet restrictions by using QUIC as transport, which looks like HTTP/3 and doesn't suffer from TCP-over-TCP meltdown:
https://obscura.net/

Technical details:https://obscura.net/blog/bootstrapping-trust/Let us know what you think!Disclaimer: I'm the creator of Obscura.

reply

McNulty2

5 hours ago

 |
parent
 |
next

[–]

If they're blocking other protocols then likely they're blocking quic also.

reply

dongcarl

5 hours ago

 |
root
 |
parent
 |
next

[–]

Very possible, though many of our users are saying that in network environments where WireGuard is blocked they were able to use Obscura.

reply

tmpfs

4 hours ago

 |
root
 |
parent
 |
next

[–]

Hey, I went to take a look at Obscura and I like the ideas but I can't find the source code.

You are making some bold claims but without the source I can't verify those claims.Any plans to open-source it?

reply

dongcarl

4 hours ago

 |
root
 |
parent
 |
next

[–]

We should link it in more places, apologies!

Here it is:https://github.com/Sovereign-Engineering/obscuravpn-client

reply

neurostimulant

51 minutes ago

 |
prev
 |
next

[–]

Probably just an unfortunate timing. Cloudflare is going down in this region [1] at the same time with the protests and unrest caused by the news of a motorcycle taxi driver who got run over by a swat car during a protest [2].

Such coincidence might seems like the government trying to do some damage control by restricting internet access, but I hope that's not what happen here. At the moment, cloudflare status for Jakarta is still "rerouted".[1]https://www.cloudflarestatus.com/incidents/1chpg2514kq8[2]https://www.youtube.com/watch?v=-jONV0mb9nw

reply

VortexLain

4 hours ago

 |
prev
 |
next

[–]

The most effective solution is to use X-ray/V2ray with VLESS, or VMESS, or Trojan as a protocol.

Another obfuscated solution is AmneziaIf you are not ready to set up your own VPN server and need any kind of connection right now, try Psiphon, but it's a proprietary centralized service and it's not the best solution.

reply

Arubis

5 hours ago

 |
prev
 |
next

[–]

If you can still get SSH access and can establish an account with a VPS provider with endpoints outside your country of origin,
https://github.com/StreisandEffect/streisand
 is a little long in the tooth but may still be viable.

reply

kccqzy

5 hours ago

 |
parent
 |
next

[–]

Tunneling via SSH (ssh -D) is super easy to detect. The government doesn't need any sophisticated analysis to tell SSH connections for tunneling from SSH connections where a human is typing into a terminal.

Countries like China have blocked SSH-based tunneling for years.It can also block sessions based on packet sizes: a typical web browsing session involves a short HTTP request and a long HTTP response, during which the receiving end sends TCP ACKs; but if the traffic traffic mimics the above except these "ACKs" are a few dozen bytes larger than a real ACK, it knows you are tunneling over a different protocol. This is how it detects the vast majority of VPNs.

reply

mnw21cam

4 hours ago

 |
root
 |
parent
 |
next

[–]

One alternative would be to set up a VPS, run VNC on it, run your browser on that to access the various web sites, and connect over an SSH tunnel to the VNC instance. Then it actually is an interactive ssh session.

reply

galaxy_gas

3 hours ago

 |
root
 |
parent
 |
next

[–]

Anything more then small text bandwidth use is also detected . Not about interactivity instead this case

reply

bsimpson

5 hours ago

 |
parent
 |
prev
 |
next

[–]

15 years ago, I was using EC2 at work, and realized it was surprisingly easy to SSH into it in a way where all my traffic went through EC2. I could watch local Netflix when traveling. It was a de facto VPN.

Details are not at the top of my mind these years later, but you can probably rig something up yourself that looks like regular web dev shit and not a known commercial VPN. I think there was a preference in Firefox or something.

reply

mikestorrent

4 hours ago

 |
root
 |
parent
 |
next

[–]

The issue these days is that all of the EC2 IP ranges are well known, and are usually not very high-reputation IPs, so a lot of services will block them, or at least aggressively require CAPTCHAs to prevent botting.

Source: used to work for a shady SEO company that searched Google 6,000,000 times a day on a huge farm of IPs from every provider we could find

reply

hinkley

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

I watched a season of Doctor Who that way back when the BBC were being precious about it. But Digital Ocean, so $5.

reply

yogorenapan

6 hours ago

 |
prev
 |
next

[–]

WireGuard should still work. Tons of different providers. I trust Mullvad but ProtonVPN has a free tier. If they start blocking WireGuard, check out v2ray and xray-core. If those get blocked... that means somehow they're restricting all HTTPS traffic going out of the country

reply

lifeisstillgood

1 hour ago

 |
prev
 |
next

[–]

I’m not sure this is the right conversation right now, but is this thread heading towards “how do we make totalitarian governments become liberal democracies?”

It’s a nice technical question on how to run a VPN but the ultimate goal is not the best technical solution but the ability to avoid detection by the state. And that’s not a technical problem but an opsec oneIf someone is participating in online discussions (discord and twitter) to spread local news - then it’s hard to know who is who, and who to trust - and that’s kind of the why Arab spring did not spring “hey wear a red carnation and meet me by the corner” can become a death sentenceThe answer to opsec is avoid all digital comms - but at this point you are seriously into “regieme change”, or just as Eastern Europe did, keep your heads down for forty years and hope those who leave you economically behind will half bankrupt them selves bringing you back.I think in the end, a thriving middle class with a sufficient amount of land reform, wealth taxes which can over a generation push for liberalisation sounds a good idea.Our job in the very lucky liberal
West is to keep what our forefathers won, and then push it further to show why our values are worth the sacrifice in copying

reply

ryan-ca

19 minutes ago

 |
prev
 |
next

[–]

I recommend using tor over snowflake relays to connect. It is meant to be censorship proof.

reply

RajT88

2 hours ago

 |
prev
 |
next

[–]

Somewhat dated read here:

https://www.reddit.com/r/Tailscale/comments/16zfag4/travelin...Some good ideas, though. There seems to be OSS alternatives for TailScale control servers which would make it harder to block - I'd go that route. The top recommendation boils down to, "Set up several different methods, and one will always work".

reply

drake99

6 hours ago

 |
prev
 |
next

[–]

In this scenario, Chinese have very rich experience.
you need to use the advance proxy tool like clash ,v2ray, shadowsocks etc.

reply

mezyt

4 hours ago

 |
parent
 |
next

[–]

shadowsocks was the winner of the state of the art I had to do at work. It address the "long-term statistical analysis will often reveal a VPN connection regardless of obfuscation and masking (and this approach can be cheaper to support than DPI by a stat)" comment.

reply

rthnbgrredf

7 hours ago

 |
prev
 |
next

[–]

In case known VPN providers are blocked you can pick a small VPS from a hoster like Hetzner and setup your own VPN.

reply

o999

4 hours ago

 |
prev
 |
next

[–]

AmneziaWG client worked just fine with normal Wireguard servers in Egypt where official Wireguard clients doesn't, WGTunnel app on android support both protocols.

https://github.com/amnezia-vpn/amneziawg-gohttps://github.com/wgtunnel/wgtunnel

reply

WarOnPrivacy

6 hours ago

 |
prev
 |
next

[–]

I'm reading posts that indicate (at least some of) the blocking is at the DNS level.

https://old-reddit-com.translate.goog/r/WkwkwkLand/comments/...Cloudflare sayssome issueaffecting Jakarta has been resolved. They aren't saying what the issue was.https://www.cloudflarestatus.com/incidents/1chpg2514kq8

reply

rickybule

6 hours ago

 |
parent
 |
next

[–]

What I'm worried most are that most people are not even aware of what is DNS and how to change it.

I can't imagine those who are caught in the chaos with only their phone and unable to access information that could help them to be safe.

reply

jhanschoo

5 hours ago

 |
root
 |
parent
 |
next

[–]

Generally speaking, the general population that wants to use blocked services will develop enough technical know-how to circumvent it. The biggest risk is that there are bad actors giving malicious advice and to such learners, looking to defraud or otherwise exploit them.

reply

qwezxcrty

3 hours ago

 |
prev
 |
next

[–]

Chinese have developed a significant amount of sophisticated tools countering internet censorship. V2ray as far as I recall is the state-of-the-art.

To use them, one need to first rent a (virtual) server somewhere from a foreign cloud provider as long as the payment does not pose a problem. The first step sometimes proves difficult for people in China, but hopefully Indonesia is not at that stage yet. What follows is relatively easy as there are many tutorials for the deployment like:https://guide.v2fly.org/en_US/

reply

mrbluecoat

3 hours ago

 |
parent
 |
next

[–]

Agreed, the best tools for circumventing The Great Firewall of China are from Chinese developers.
https://github.com/txthinking/brook
 comes to mind..

reply

teekert

4 hours ago

 |
prev
 |
next

[–]

What is going on if you don’t mind my asking? Our local news does not mention anything. Nor does ddging help? Any sources?

reply

nograpes

4 hours ago

 |
parent
 |
next

[–]

Massive protests have occurred due to obvious government corruption. In particular the housing allowance for a month for a parliamentarian is now ten times the minimum wage for a month.

https://www.theguardian.com/world/2025/aug/26/indonesia-prot...Sorry I don't have a better freely accessible source, maybe someone with more knowledge can fill it in.

reply

jacobgkau

3 hours ago

 |
root
 |
parent
 |
next

[–]

> the housing allowance for a month for a parliamentarian is now ten times the minimum wage for a month.

I'm almost positive that everyone in the US Congress is making at least ten times the minimum wage in this country. The "housing allowance" being referred to is separate from their normal salary in Indonesia, but still, interesting to imagine how much more seriously people there would take that disparity than in many other countries.This caught my attention more:> Indonesia passed a law in March allowing for the military to assume more civilian posts, while this month the government announced 100 new military battalions that will be trained in agriculture and animal husbandry. In July the government said the military would also start manufacturing pharmaceuticals.They're replacing civilian industry with military, apparently not out of any emergency requirement but just to benefit the military with jobs (and the government with control over those sectors) at the expense of civilian jobs.

reply

ToValueFunfetti

1 hour ago

 |
root
 |
parent
 |
next

[–]

The ratio between Indonesian parliamentary income and the median Indonesian income is ~18x, while the ratio in the US is ~4x. As someone who wants US congressional income to be substantially higher, it's hard for me to be upset at that on its own. There are plenty of other variables at play, though, and a direct comparison of these ones might not be getting at the issue.

reply

Lu2025

5 minutes ago

 |
prev
 |
next

[–]

Starlink?

reply

herodoturtle

6 hours ago

 |
prev
 |
next

[–]

On a related note, does anyone have insight into *why* the Indonesian government is doing this?

reply

rickybule

6 hours ago

 |
parent
 |
next

[–]

there is a major protest currently happening due to the legislative body representative just giving themselves a monthly domicile stipend of ~$3300 on top of their salaries (yes, multiple), while the average people earned ~$330 monthly. the information about the protest are not broadcasted on local TVs, so the only spread of information is through social media. i guess since a lot of people went around it using VPN, the gov decided to block it too.

reply

jofer

4 hours ago

 |
parent
 |
prev
 |
next

[–]

If it helps, here's some recent coverage:

https://www.theguardian.com/world/2025/aug/26/indonesia-prot...

reply

teekert

4 hours ago

 |
root
 |
parent
 |
next

[–]

“Some demonstrators on Monday were seen on television footage carrying a flag from the Japanese manga series One Piece, which has become a symbol of protest against government policies in the country.”

reply

TheChaplain

6 hours ago

 |
parent
 |
prev
 |
next

[–]

The official word is to counter gambling. Lately the government is not really popular after some decisions that could be interpreted as authoritative, and as citizens have spoken out about it online, causing more voices to join and protests erupting..

So well, my guess is they're trying to control it.

reply

geephroh

6 hours ago

 |
parent
 |
prev
 |
next

[–]

https://tech.yahoo.com/social-media/articles/indonesia-urges...

reply

whyleyc

6 hours ago

 |
prev
 |
next

[–]

I'd recommend using Outline - it's a one click setup that lets you provision your own VPN on a cloud provider (or your own hardware).

Since you get to pick where the hardware is located and it is just you (or you and a small group of friends & family) using the VPN, blocking is more difficult.If you don't want the hassle of using your own hardware you can rent a Digital Ocean droplet for <$5 per month.https://getoutline.org/

reply

lucasban

4 hours ago

 |
parent
 |
next

[–]

I’ve set this up for friends in fairly heavily censored countries before, it has been working well so far, but as others have said, this is a cat and mouse game

reply

mlhpdx

1 hour ago

 |
prev
 |
next

[–]

A question related to the question, for which I apologize:

It seems to me that using WireGuard (UDP) in conjunction with something like Raptor Forward Error Correction would be somewhat difficult to block. A client could send to and receive from a wide array of endpoints without ever establishing a session and communicate privately and reliably, is that correct?

reply

gudzpoz

3 hours ago

 |
prev
 |
next

[–]

As someone based in China, it's a bit surprising that techniques used by Chinese people get very few mentions here, while I do think they are quite effective against access blocking, especially after coevolving with GFW for the past decade. While I do hope blocking in Indonesia won't get to GFW level, I will leave this here in case it helps.

I found this article [0] summarizing the history of censorship and anti-censorship measures in China, and I think it might be of help to you if the national censorship ever gets worse. As is shown in the article, access blocking in China can be categorized into several kinds: (sorted by severity)1. DNS poisoning by intercepting DNS traffic. This can be easily mitigated by using a DOT/DOH DNS resolver.2. Keyword-based HTTP traffic resetting. You are safe as long as you use HTTPS.3. IP blocking/unencrypted SNI header checking. This will require the use of a VPN/proxy.4. VPN blocking by recognizing traffic signatures. (VPNs with identifiable signatures include OpenVPN and WireGuard (and Tor and SSH forwards if you count those as VPNs), or basically any VPN that was designed without obfuscation in mind.) This really levels up the blocking: if the government don't block VPN access, then maybe any VPN provider will do; but if they do, you will have a harder time finding providers and configuring things.5. Many other ways to detect and block obfuscated proxy traffic. It is the worse (that I'm aware of), but it will also cost the government a lot to pull off, so you probably don't need to worry about this. But if you do, maybe check out V2Ray, XRay, Trojan, Hysteria, NaiveProxy and many other obfuscated proxies.But anyways, bypassing techniques always coevolve with the blocking measures. And many suggestions here by non-Indonesian (including mine!) might not be of help. My personal suggestion is to find a local tech community and see what techniques they are using, which could suit you better.[0]https://danglingpointer.fun/posts/GFWHistory

reply

mxie-ca

3 hours ago

 |
parent
 |
next

[–]

Thanks for the link!

Is there any good DoT/DoH DNS resolver that works well in China? I know I can build one myself, but forwarding all DNS requests to my home server in NA slows down all connections...

reply

swe_dima

4 hours ago

 |
prev
 |
next

[–]

Personally, I like Amnezia VPN, it has some ways to work around blocks:
https://amnezia.org/en

You can very easily self-host it, their installer automatically works on major cloud platforms.

Though if Indonesia has blocked VPNs only now, possibly they only block major providers and don't try to detect the VPN protocol itself, which would make self-hosting any VPN possible.

reply

throwawayffffas

54 minutes ago

 |
prev
 |
next

[–]

Maybe TOR?
https://www.torproject.org/

reply

jasonlingx

48 minutes ago

 |
prev
 |
next

[–]

An alternative is using an eSIM with an “internet breakout” via another country.

Esimdb is a good place to start.

reply

gwbas1c

4 hours ago

 |
prev
 |
next

[–]

Just curious: Anyone know if things like Starlink are viable?

reply

akho

1 hour ago

 |
parent
 |
next

[–]

Starlink, by policy, connects you through a ground station in the same country. They wouldn't be allowed to operate otherwise.

reply

ultim8k

41 minutes ago

 |
root
 |
parent
 |
next

[–]

Why? Can someone block the sky? (I have 0 satellite knowledge)

reply

egberts1

31 minutes ago

 |
prev
 |
next

[–]

Buy a VSP elsewhere and run Wireguard over IPSec

reply

Beijinger

2 hours ago

 |
prev
 |
next

[–]

Use Astrill - if you can afford. You could try AirVPN, much cheaper, but if Astrill does not work, probably no VPN will.

https://expatcircle.com/cms/privacy/vpn-services/

Why is Indonesia in chaos?

reply

rufus_foreman

58 minutes ago

 |
parent
 |
next

[–]

>> Why is Indonesia in chaos?

I was wondering that too, looks likehttps://en.wikipedia.org/wiki/2025_Indonesian_protests.

reply

ryzvonusef

4 hours ago

 |
prev
 |
next

[–]

I live in Pakistan and two years back we had this exact same problem, (election interference) and frankly, you just try to scrape through solutions, but without an answerable government, there is little you can do.

We tried things like Proton VPN and Windscribe VPN, as well as enabling MT proxy on Telegram, but soon govts find it easier to just mass ban internet access.Use Netblocks.org to analyse the level of internet blockage and try to react accordingly.

reply

andrewinardeer

1 hour ago

 |
prev
 |
next

[–]

Weird. I'm in Indonesia and can access VPNs, X and Discord.

reply

ies7

1 hour ago

 |
parent
 |
next

[–]

I just wake up in Jakarta and there is nothing wrong with X or Discord

reply

thewanderer1983

3 hours ago

 |
prev
 |
next

[–]

Go here.
https://github.com/net4people/bbs/issues

Very helpful community.

reply

ACCount37

5 hours ago

 |
prev
 |
next

[–]

AmneziaWG is a decent option for censorship resistance, and it can be installed as a container on your own server.

reply

o999

4 hours ago

 |
parent
 |
next

[–]

AmneziaWG clients works just fine with normal Wireguard servers by the way.

reply

jinnko

4 hours ago

 |
prev
 |
next

[–]

AmneziaVPN has censorship circumvention options and makes it easy to set up a self hosted instance of that's what you prefer, or use their hosted service.

https://amnezia.org/

reply

arewethereyeta

3 hours ago

 |
prev
 |
next

[–]

Give Trojan proxy a try. It's supposed to go unnoticed since it works on the https port 443. Something like:
https://www.anonymous-proxies.net/products/residential-troja...
 If you get it with a residential IP is even better. Works great in Iran and China and i suspect will wotk great for you too

reply

Aachen

7 hours ago

 |
prev
 |
next

[–]

Aren't there local (online or print) newspapers to get news from, as an alternative to Discord? Hope I'm not asking a dumb question

reply

alluro2

6 hours ago

 |
parent
 |
next

[–]

In countries where it comes to government blocking/censoring internet traffic, traditional media is cleared of all dissent and fully controlled long before. Last stages of that are happening in my country, Serbia, currently.

reply

Aachen

6 hours ago

 |
root
 |
parent
 |
next

[–]

Right, that makes sense. Did some looking up and nonfree press seems to be indeed the case for Indonesia:
https://rsf.org/en/country/indonesia

It's a mixed bag apparently, free press is technically legal since 1998 but selective prosecution and harassment of those actually uncovering issues (mainly becomes clear in the last section, "Safety")Tried looking up Serbia next on that website but got a cloudflare block. I'm a robot now...

reply

wafflemaker

6 hours ago

 |
parent
 |
prev
 |
next

[–]

It's not a dumb question at all. Level on hn really got down lately if you're getting downvoted.

Think about it Aachen. If the government has enough power to censor internet traffic, that what was the first thing it censored? Which media is traditionally known for being censored or just speaking propaganda? That's the classical newspapers. It's not uncommon in authoritarian countries for editors to need state to sign off on the day's paper. And if not that, articles are signed and publishers are known. They will auto-censor to avoid problems. Just like creators on YouTube don't comment on this one country's treatment of civilians to avoid problems.

reply

database64128

4 hours ago

 |
prev
 |
next

[–]

You could use something like
https://github.com/database64128/swgp-go
 to obfuscate WireGuard traffic.

Using full-blown VPNs under such environments has the disadvantage of affecting your use of domestic web services. You might want to try something likehttps://github.com/database64128/shadowsocks-go, which allows you to route traffic based on domain and IP geolocation rules.

reply

thinkingtoilet

3 hours ago

 |
prev
 |
next

[–]

Please consider the potential consequences of circumventing the ban. Do what you do, but above all stay safe!

reply

breve

1 hour ago

 |
prev
 |
next

[–]

You should use people power to work to make Indonesia a more open, democratic society.

Yes, it's hard work. Yes, it will take a long time. Yes, you personally may not get very far with your efforts.But if Indonesians don't take responsibility for and work to improve Indonesia then the rest of it doesn't matter.

reply

protocolture

1 hour ago

 |
parent
 |
next

[–]

Part of that is knowing whats happening inside the country, of which they were previously using tools like discord, which have now been blocked. So the first step to using people power to make Indonesia a more open, democratic society would be to find a way to tunnel out to get and share that information. To that end the OP has created this Ask HN thread.

reply

breve

1 hour ago

 |
root
 |
parent
 |
next

[–]

Nope. The outside doesn't matter. The problem is on the inside. External websites will never fix the internal problem.

There are no technical solutions to what is fundamentally a problem of political culture.

reply

degamad

40 minutes ago

 |
root
 |
parent
 |
next

[–]

How do you propose they coordinate the political activities when they can't use external communications sites/tools, and internal sites are actively monitored by an authoritarian government?

Step 1 is establishing a secure means of communication.

reply

mulchpower

2 hours ago

 |
prev
 |
next

[–]

URnetwork works where many don't
http://ur.io
 . It used a grab bag of techniques, open source

reply

acuozzo

7 hours ago

 |
prev
 |
next

[–]

Grab a VPS and use SOCKS5 tunneling via SSH.

reply

Joel_Mckay

6 hours ago

 |
parent
 |
next

[–]

SSH is often targeted by deep packet inspection and protocol binding filters.

i.e. One is better off tunneling overhttps://www.praise-the-glorious-leader.google.com.facebook.c...include SSH traffic protocol auto-swapping on your server (i.e. no way to tell the apparent web page differs between clients), as some corporate networks are infamously invasive. People can do this all day long, and they do... =3

reply

bitwize

6 hours ago

 |
root
 |
parent
 |
next

[–]

lolwut

At least it isn't goatse...

reply

Joel_Mckay

6 hours ago

 |
root
 |
parent
 |
next

[–]

It is not a real URI... lol

The point was to include something clowns can't filter without incurring collateral costs, and wrapping the ssh protocol in standard web traffic. =3

reply

chrisweekly

5 hours ago

 |
root
 |
parent
 |
next

[–]

tangent: what is the significance of the "=3" you sign your messages with?

reply

Joel_Mckay

5 hours ago

 |
root
 |
parent
 |
next

[–]

Don't worry about it... =3

reply

ddtaylor

5 hours ago

 |
prev
 |
next

[–]

Your first option until you get settled is to use an SSH reverse proxy:

ssh -D 9999 user@my.serverThen configure your browser to use local port 9999 for your SOCKS5 proxy.This gets you a temporarily usable system and if you can tunnel this way successfully installing some WireGuard or OpenVPN stuff will likely work.EDIT: Thanks it's -D not -R

reply

hdgvhicv

4 hours ago

 |
parent
 |
next

[–]

It’s -D, -R is for forwarding specific ports.

reply

ddtaylor

4 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks I have updated my comment as well.

Sorry for the brain rot!

reply

Jigsy

6 hours ago

 |
prev
 |
next

[–]

I was wondering something like this but in a different capacity.

What with certain countries (they know who they are) and their hatred for encryption, it got me wondering how people would communicate securely if - for example - Signal/WhatsApp/etc. pulled out and the country wound up disconnecting the submarine cables to "keep $MORAL_PANIC_OF_THE_DAY safe."How would people communicate securely and privately in a domestic situation like that?

reply

RansomStark

5 hours ago

 |
parent
 |
next

[–]

In person or not at all.

At that point you've essentially lost.You either hope another country sees value in spreading you some democracy, or you rise up and hope others join you.Or not and you accept the protection the state is graciously providing to you.

reply

Jigsy

5 hours ago

 |
root
 |
parent
 |
next

[–]

SneakerNet or bust, eh? That sucks.

reply

wsintra2022

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Encrypted hand written notes tied to pigeons

reply

mhitza

5 hours ago

 |
prev
 |
next

[–]

Use the Tor browser window in Brave. It's nowhere near as anonymous as the Tor browser, but the built in ad blocking makes browsing via Tor usable. And that's what you and your compatriots are interested in.

Prepare to fill in Cloudflare captchas all day, but that's what it takes to have a bit of privacy nowadays.

reply

jay-418

2 hours ago

 |
prev
 |
next

[–]

Censorship circumvention tools specialize in this, and are extensively used in China, Iran, and Russia. I work on Lantern, and we're not seeing any significant interruptions to connections in Indonesia at the moment.

https://lantern.io/download

Hope it helps!

reply

nromiun

4 hours ago

 |
prev
 |
next

[–]

Usually when countries block websites they don't block major cloud providers, like AWS and Google Cloud. Because most websites are hosted on them. So you can get a cheap VPS from AWS or GCP (always free VM is available) and host OpenVPN on it.

reply

fruitworks

3 hours ago

 |
prev
 |
next

[–]

Try looking into tor bridges.

You could also buy a VPS and use SSH tunneling to access a tor daemon running on a VPS. Host some sort of web service on the VPS so it looks inconspicuous

reply

rurban

5 hours ago

 |
prev
 |
next

[–]

In this case the blockage will probably just be up for a few days, until the protests calmed down.

Other than that: tor

reply

puffybuf

3 hours ago

 |
prev
 |
next

[–]

I like mullvad. You can buy a prepaid card off amazon. I figured out how to setup wireguard on various unixes Mac/linux/openbsd

reply

anikom15

35 minutes ago

 |
prev
 |
next

[–]

Move

reply

vander_elst

5 hours ago

 |
prev
 |
next

[–]

Set up a VM on AWS/azure/gcp/... in the desired cell, install a VPN server and done. Once you have automation in place it takes ~2 minutes to start, you can run it on demand so you can pay per minute.

reply

liveoneggs

5 hours ago

 |
prev
 |
next

[–]

All the various proxy solutions offered are good (although the simplest ones - like squid - haven't been mentioned yet). You can also use a remote desktop or even just ssh -Y me@remote-server "firefox"

reply

seany

39 minutes ago

 |
prev
 |
next

[–]

Shadowsocks used to be the thing that _really_ worked in CN. Not sure what's current there.

AWS ap-southeast-3 should still be up, and isn't in a different partition like CN, govcloud, iso etc. So a VM there and a vpc peer in the US should get you around a lot of stuff.

reply

wiredpancake

10 minutes ago

 |
parent
 |
next

[–]

Shadowsocks isn't a viable method in 2025 it seems. Not by itself apparently.
Shadowsocks generates high-entropy noise via packet analysis, which typically is easy to spot out as it looks irregular.

reply

defulmere

7 hours ago

 |
prev
 |
next

[–]

SOCKS proxy over SSH?

reply

pmlnr

6 hours ago

 |
parent
 |
next

[–]

Android doesn't come with system wide socks proxy support, and i couldn't find an open source app for it either. Is anyone aware of one?

Nonetheless this is a surprisingly simple and bullet proof solution: SSH, that's not vpn boss, i need it for work.

reply

kevindamm

5 hours ago

 |
root
 |
parent
 |
next

[–]

Outline is an open source shadowsocks client, and you provision your own server to act as the proxy. You can use it against any Shadowsocks server you want, and the protocol makes it look like regular https traffic.

https://github.com/Jigsaw-Code/outline-appsAndroid & iOS & Linux & Mac & Windowstheir server installer will help set up a proxy for users that aren't familiar with shadowsocks, too

reply

newlisp

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

For web browsing, Firefox lets you configure socks on android.

reply

oleksandr_l5

1 hour ago

 |
prev
 |
next

[–]

SSTP or other HTTPS like VPN

reply

leishman

4 hours ago

 |
prev
 |
next

[–]

I'd recommend Obscura because it uses Wireguard over QUIC and it pretty good at avoiding these blocks. It's also open source.

reply

teaga

4 hours ago

 |
prev
 |
next

[–]

Launch an EC2 instance in the US region (Ubuntu, open ports 22 and 1194), then connect via SSH and run the OpenVPN install script. Generate the .ovpn profile with the script and download it to your local machine. Finally, import the file into the OpenVPN client and connect to route traffic through the US server.

reply

wiredpancake

9 minutes ago

 |
parent
 |
next

[–]

Doesn't work in China, this is a method for last decades censorship.

reply

lidder86

1 hour ago

 |
prev
 |
next

[–]

surfshark works also Im on MTM no issues! Same with Biznet

reply

Gud

3 hours ago

 |
prev
 |
next

[–]

Try a ssh socks5 proxy to a cheap vps.

It worked well for me in UAE when other solutions didn’t

reply

yannick

3 hours ago

 |
prev
 |
next

[–]

does this include bali? curious as that would impact the large international population.

reply

SirMaster

6 hours ago

 |
prev
 |
next

[–]

Remote desktop (RDP/AnyDesk/etc) into a VM hosted somewhere else?

reply

bitbasher

5 hours ago

 |
prev
 |
next

[–]

Make your own VPN using a VPS and something like openvpn.

Not every website will allow it, but it should get you access to more than you have now.

reply

afh1

4 hours ago

 |
prev
 |
next

[–]

Depending on the circumstances, maybe ditch the landline local ISP for a satellite connection with a foreign ISP?

reply

jwong_

5 hours ago

 |
prev
 |
next

[–]

A proxy service like shadow socks works. There are thousands of providers for $X/month for a decent amount of traffic

reply

pshirshov

3 hours ago

 |
prev
 |
next

[–]

You should use a jet. Actually that's a Russian joke.

reply

sturza

7 hours ago

 |
prev
 |
next

[–]

Mullvad

reply

reisse

5 hours ago

 |
parent
 |
next

[–]

Mullvad doesn't really have any modern censorship circumvention options.

reply

octo888

5 hours ago

 |
root
 |
parent
 |
next

[–]

Genuine question is Shadowsocks outdated? Because it supports it

reply

dboreham

1 hour ago

 |
prev
 |
next

[–]

The closest I've come to this is on an airplane where almost everything was blocked. SSTP to a server I spun up worked well.

reply

princevegeta89

5 hours ago

 |
prev
 |
next

[–]

OP, you can rent a VPS from a reputable and cheap provider within the NA region - OVH, Vultr, Linode etc. are decent. Also check out lowendtalk.com

Then, setup Tailscale on the server. You can VPN into it and essentially browse the internet as someone from NA.

reply

teekert

4 hours ago

 |
parent
 |
next

[–]

From some of the comments here I get why you are downvoted. But tbh I would also have gone that route. So are we just inexperienced? I read here indeed that wireguard is very easily blocked. It was at the company I worked for but then I just set port 23 (who uses ftp anyways??). And it worked. But why is this still bad then?

Obviously I have 0 real experience with this.

reply

princevegeta89

3 hours ago

 |
root
 |
parent
 |
next

[–]

Well, I mean, Tailscale is pretty easy overall. When client apps get blocked, you can literally hook up your router into Tailscale if needed, or you can run a headless version of Tailscale on your home server or the very machine you are on.

It should also be possible to use a tunnel to get around the blocking of WireGuard, for example.You can then use it as an exit node if needed. It should work in theory, I have never tried this though. I just speak as a very frequent user of Tailscale with a bunch of nodes that are geographically located in different cities around me.

reply

teekert

2 hours ago

 |
root
 |
parent
 |
next

[–]

Sure, I know and use it too. But I saw you being downvoted so I responded to that. I think, reading the rest of the thread, your response (as mine would be) does not work as signals 0 experience with actually oppressing regimes. Not?

reply

tonymet

3 hours ago

 |
prev
 |
next

[–]

try Bright Data / luminati and the traffic is http to the proxy as well.

reply

cabirum

2 hours ago

 |
prev
 |
next

[–]

sshuttle.
Tunnel your connections inside ssh.

reply

yupyupyups

5 hours ago

 |
prev
 |
next

[–]

Residential VPNs, but try to find ones that are ran ethically.

reply

yegor

2 hours ago

 |
prev
 |
next

[–]

Full disclosure, I run a commercial VPN service (Windscribe).

There are 2 paths you can take here:1. Roll your own VPN server on a VPS at a less common cloud provider and use it. If you're tech savvy and know what you're doing, you can get this going in <1hr. Be mindful of the downsides of being the sole user of your custom VPN server you pay for: cloud providers log all TCP flows and traffic correlation is trivial. You do something "bad", your gov subpoenas the provider who hands over your personal info. If you used fake info, your TCP flows are still there, which means your ISP's IP is logged, and deanonymizing you after that is a piece of cake (no court order needed in many countries).2. Get a paid commercial VPN service that values your privacy, has a diverse network of endpoints and protocols. Do not use any random free VPN apps from the Play/App stores, as they're either Chinese honeypots (https://www.bitdefender.com/en-us/blog/hotforsecurity/china-...) or total scams (https://www.tomsguide.com/computing/vpns/this-shady-vpn-has-...).Do not go with a VPN service that is "mainstream" (advertised by a Youtuber) or one that has an affiliate program. Doing/having both of these things essentially requires a provider to resort so dishonest billing practices where your subscription renews at 2-5x of the original price. This is because VPNs that advertise or run affiliate programs don't make a profit on the initial purchase for that amazing deal thats 27 months with 4 months free or whatever the random numbers are, they pay all of this to an affiliate, sometimes more. Since commercial VPNs are not charities, they need ROI and that comes only when someone rebills. Since many people cancel their subscriptions immediately after purchase (to avoid the thing that follows) the rebill price is usually significantly more than the initial "amazing deal". This is why both Nord and Express have multiple class action lawsuits for dishonest billing practices - they have to do it, to get their bag (back). It's a race to the bottom of who can offer the most $ to affiliates, and shaft their customers as the inevitable result.Billing quirks aside, a VPN you choose should offer multiple VPN protocols, and obfuscation techniques. There is no 1 magic protocol that just works everywhere, as every country does censorship differently, using different tools.- Some do basic DNS filtering, in which case you don't need a VPN at all, just use an encrypted DNS protocol like DOH, from any provider (Cloudflare, Google, Control D[I also run this company], NextDNS, Adguard DNS)- Then there is SNI filtering, where changing your DNS provider won't have any effect and you will have to use a VPN or a secure proxy (HTTPS forward proxy, or something fancier like shadowsocks or v2ray).- Finally there is full protocol aware DPI that can be implemented with various degrees of aggressiveness that will perform all kinds of unholy traffic inspection on all TCP and UDP flows, for some or all IP subnets.For this last type, having a variety of protocols and endpoints you can connect to is what's gonna define your chance of success to bypass restrictions. Beyond variety of protocols, some VPN providers (like Windscribe, and Mullvad) will mess with packets in order to bypass DPI engines, which works with variable degree of success and is very region/ISP specific. You can learn about some of these concepts in this very handy project:https://github.com/ValdikSS/GoodbyeDPI(we borrow some concepts from here, and have a few of our own).Soooo... what are good VPNs that don't do shady stuff, keeps your privacy in mind, have a reasonably sized server footprint and have features that go beyond basic traffic proxying? There is IVPN, Mullvad, and maybe even Windscribe. All are audited, have open source clients and in case of Windscribe, also court proven to keep no logs (ask me about that 1 time I got criminally charged in Greece for actions of a Windscribe user).If you have any questions, I'd be happy to answer them.

reply

king_of_shit

1 hour ago

 |
parent
 |
next

[–]

TIL

reply

asdefghyk

4 hours ago

 |
prev
 |
next

[–]

shortwave radios would enable you to still get news of major events - not 2 way though

reply

farceSpherule

3 hours ago

 |
prev
 |
next

[–]

If you are a journalist or other, contact Team Cymru.

reply

jongjong

18 minutes ago

 |
prev
 |
next

[–]

Easy, you can just create any generic Linux Amazon EC2 instance (or just about any cloud provider of your choice) and use it as a SOCKS5 proxy via SSH tunnel with -D flag... Then set one of your browsers (e.g. Firefox) to connect via that proxy.

Indistinguishable from any other server on the internet.

reply

ddbb33

5 hours ago

 |
prev
 |
next

[–]

Psiphon works

reply

reactordev

7 hours ago

 |
prev
 |
next

[–]

localtunnel.me, some node in the cloud, tunnel…

reply

darkhorn

4 hours ago

 |
prev
 |
next

[–]

People in Turkey use
https://github.com/ValdikSS/GoodbyeDPI
 together with DNS over HTTPS (DoH).

reply

TimCTRL

5 hours ago

 |
prev
 |
next

[–]

I can relate to this because my country has an election soon and I'm sure we wont have internet for 3 - 5 days then.

reply

pbiggar

5 hours ago

 |
prev
 |
next

[–]

There's a new VPN that you might try, built by Boycat.

https://www.boycat.io/vpnDon't know if it will help in this situation as it's designed to be a VPN not controlled by Israel, but it might be worth a try.

reply

moralestapia

2 hours ago

 |
prev
 |
next

[–]

Can you SSH outside the country?

If so, then you have a VPN.

reply

diggan

7 hours ago

 |
prev
 |
next

[–]

Tor should be pretty good even for environments where they crack down on VPNs, although it can be a bit slow, at least it works.

reply

immibis

7 hours ago

 |
parent
 |
next

[–]

Then you will be blocked by Twitter and Discord, which is the same thing.

reply

diggan

6 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah, sucks, but really should find better places for people to gather regardless, if you're in that sort of environment.

reply

redserk

5 hours ago

 |
root
 |
parent
 |
next

[–]

How is this practical advice in a thread where someone mentions that the clampdown happened without notice?

The "shoulda done..." advice isn't useful in the slightest, and I'd argue is malicious with how often it's done simply to satiate a poster's ego.

reply

jedisct1

6 hours ago

 |
prev
 |
next

[–]

Get a cheap VPS anywhere, and use DSVPN
https://github.com/jedisct1/dsvpn

Uses TCP and works pretty much anywhere.

reply

ivape

3 hours ago

 |
prev
 |
next

[–]

SSH tunnel on cheap VPS, a couple.

reply

ok123456

5 hours ago

 |
prev
 |
next

[–]

ssh -D 48323 -p 61423 my-vps.big-company.com

reply

zhengiszen

3 hours ago

 |
prev
 |
next

[–]

Use an ethical one

https://www.boycat.io/vpn

reply

more_corn

3 hours ago

 |
prev
 |
next

[–]

You could rent a cheapo instance at a cloud provider and tunnel https over ssh.

That’s basically undetectable. Long lived ssh connection? Totally normal. Lots of throughput? Also normal. Bursts throughput? Same.Not sure how to do this on mobile.Tailscale might be an option too (they have a free account for individuals and an exit node out of country nearly bypasses your problem) It uses wireguard which might not be blocked and which comes with some plausible deniability. It’s a secure network overlay not a VPN. It just connects my machines, honest officer.

reply

theyknowitsxmas

4 hours ago

 |
prev
 |
next

[–]

OVH VPS-1 and your own configuration.

reply

trhway

4 hours ago

 |
prev
 |
next

[–]

HTTPS to you own proxy on a foreign VPS.

reply

ck2

5 hours ago

 |
prev
 |
next

[–]

Just please be safe and necessarily paranoid

One way they tend to "solve" workarounds is making examples of people

reply

TZubiri

5 hours ago

 |
prev
 |
next

[–]

https://www.youtube.com/watch?v=lbOtyWTRZ_g

reply

whalesalad

5 hours ago

 |
prev
 |
next

[–]

SSH SOCKS proxy if you have an SSH host somewhere that is not Indonesia.

reply

guluarte

5 hours ago

 |
prev
 |
next

[–]

SSH tunneling on port 80 could work since it's rarely blocked, rent a cheap vps.

reply

throwpoaster

4 hours ago

 |
prev
 |
next

[–]

Emigration.

reply

jeffbee

4 hours ago

 |
prev
 |
next

[–]

Use an Actual Private Network? Radio links that you control. Peer with someone who owns a Starlink terminal. Rent instances in GCP's Jakarta datacenter.

reply

jasonjayr

4 hours ago

 |
parent
 |
next

[–]

https://en.wikipedia.org/wiki/AMSAT-OSCAR_7#Use_by_Polish_an...
 <-- "Radio links you control", and is hard to block/detect.

reply

lemper

7 hours ago

 |
prev
 |
next

[–]

megavpn, should be around a dollar a month for 5 devices.

reply

Joel_Mckay

6 hours ago

 |
prev
 |
next

[–]

There are many options, but avoiding the legal consequences may be a grey area:

https://www.stunnel.org/index.htmlhttps://github.com/yarrick/iodinehttps://infocondb.org/con/black-hat/black-hat-usa-2010/psudp.....and many many more, as networks see reduced throughput as an error to naturally route around. =3

reply

weregiraffe

4 hours ago

 |
prev
 |
next

[–]

You should use another government.

reply

scotty79

6 hours ago

 |
prev
 |
next

[–]

Maybe you could buy VPS in another country and set up VPN server yourself?

reply

roscas

6 hours ago

 |
prev

[–]

Blocking Twitter is a good start, now Facebook, Instagram, Whatsup and TikTok.

This is a good start but more should be blocked. Then force ISP to block ads.Not just for Indonesia but all countries. But we still have a lot more to do to fix the web.

reply

platevoltage

4 hours ago

 |
parent
 |
next

[–]

I can't stand most of these things you want blocked but this is bonkers.

reply

mr90210

6 hours ago

 |
parent
 |
prev

[–]

The issue with that is where do they draw the line. Next thing you know each country becomes North Korea.

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
