---
title: I'm Getting Into Mesh Networks... (Meshtastic, MeshCore, and Reticulum)
url: https://www.jonaharagon.com/posts/im-getting-into-mesh-networks-meshtastic-meshcore-and-reticulum/
site_name: hnrss
content_file: hnrss-im-getting-into-mesh-networks-meshtastic-meshcore
fetched_at: '2026-05-28T12:11:55.447724'
original_url: https://www.jonaharagon.com/posts/im-getting-into-mesh-networks-meshtastic-meshcore-and-reticulum/
date: '2026-05-27'
published_date: '2026-01-26T20:47:58.000Z'
description: I'm Getting into Mesh Networks (Meshtastic, MeshCore, and Reticulum)
tags:
- hackernews
- hnrss
---

I love networking, a lot. So much so that I've run my ownISPsince 2024, complete with its own ASN, IPv4/6 address space, fiber optics, etc.

However, do this and you quickly realize how reliant youstillremain on central service providers. The internetisa mesh, but the real players on that mesh are few, far between, and easy to coerce intocensorshipand other bad things. Even after ascending to the lofty realms of direct BGP peering myself, my access to those resources is locked behind yearly fees from ARIN.Ownershipof the "real estate" of the internet, IP addresses, no longer exists.

The tragedy of modern computing is that the local compute we own in our offices, on our laps, or in the palm of our hands is massively, massively powerful, but Big Tech companies actively refuse to take advantage of that fact. Why are you, I, and our neighbors largely relegated to consuming access from big players when the computers we have are capable of so much more?

Mesh networking, sending packets of data through manydirectlyinterconnected peers instead of through central datacenters, promises to free us from our reliance on central service providers, and it's something I've been really excited about lately.

Of course, there is good reason for how the internet is currently designed. High bandwidth connectionsarecostly, and for some applications lowering latency as much as possible is very important, which realistically requires continent- and ocean-spanning fiber optics with as few middle-men as possible.

This doesn't mean we need to putallour eggs in this basket though. While bandwidth-intensive services like Netflix or latency-sensitive services like gaming are not likely to come to mesh networks anytime soon, there are a vast number of applications whichareperfectly suited to mesh networking:

Messaging, social networking, and general information sharing are very practical uses for mesh networking where access, censorship resistance, andresiliencyare increasingly critical for many people around the world.

For applications like this, we don'tneedto trench fiber connections through the ground to get everyone connected. In the modern mesh networking space, much of the innovation is happening in theLoRaradio space.

LoRa radios uselicense-free, sub-gigahertz radio bands that are available for public use in nearly all countries around the world. Compared to the license-free 2.4 GHz or 5 GHz radio you'd recognize from Wi-Fi (but is also used by many other technologies), LoRa operates at much lower power and, importantly and simultaneously, at much longer range.

Mesh networking over the airwaves presents a very unique opportunity for our societies. We could build a resilient, peer-to-peer network thatcoexistswith the internet, enabling connectivity in currently underserved regions and increasing our personal sovereignty online by maintaining a functional backup to the internet for our most critical needs.

It's also just a freeing feeling to be able to send a message to someone else relying only on devices that you and people in your network own outright, instead of renting the capability to do so from your local ISP or Elon Musk's Starlink.

## Meshtastic

The obvious frontrunner in the mesh networking space isMeshtastic, mostly because they were the first in the consumer LoRa mesh space, or at the very least the first to do it pretty well.

It's easy to see why Meshtastic has quite a bit of popularity: it's a real product designed with a specific use-case in mind (mobile messaging and device tracking, primarily), not a technical project just trying to build a network and hoping the use-case comes later.

This is very appealing for most people who just want something they can buy and use out of the box, like a set of walkie-talkies from Wal-Mart. Unfortunately, much like those cheap walkie-talkies in comparison to more serious technology like amateur radio, Meshtastic's core design holds the platform back from achieving its full potential.

Meshtastic's first-mover advantage is pretty hard to overcome, especially when it already works reasonably well for small, private groups like hikers or event-goers.

For a very large and public mesh, however, it's become clear to most people that Meshtastic by design is a fairly untenable solution. Some public mesh groups have increased the bandwidth available to Meshtastic by giving up some range, but it's a stop-gap solution that doesn't fix the problems Meshtastic has in this environment at the end of the day.

💡
To be perfectly upfront with you, this post will be glossing over many Meshtastic and MeshCore features, because I feel they are both non-serious solutions compared to Reticulum for reasons I will explain later on in this post. I can almost guarantee I have been running Meshtastic and MeshCore for longer and with more infrastructure than you, and in fact I still do, despite not really believing in their long-term success, so... Any omissions or "lack of problem solving" in this post are not due to a lack of knowledge, but simply because 
fully
 detailing the many problems they have is outside the scope of this article.

I think most people who are serious about public mesh networking have moved on to researching other solutions, or will have to soon.

## MeshCore

MeshCore is one of these potential solutions some public mesh groups have begun switching to.

While Meshtastic's original design essentially floods the network with every message being sent, hoping it eventually reaches the correct destination, MeshCore has an actual routing system that can send messages only through a path of specific devices on the mesh that include the sender and recipient.

This results in a monumental reduction in radio transmissions, the advantages of which can't be understated. It makes the network less congested and more reliable, and for people who are mainly interested inmessagingas opposed to sharing sensor/location data that Meshtastic remains well-suited for, it's no surprise that many larger groups have begun to shift to MeshCore.

Unfortunately, MeshCore is not a true mesh in the way public mesh enthusiasts would probably like it to be. At a very high level, devices in MeshCore are broken up into two categories:companionsandrepeaters.

Companion devices would be what most people use to send and receive messages, while repeaters are the devices which actually mesh with each other and extend the overall network's range. What this means is that a companion always has to be in range of a repeater to access the network, companions never relay messages between themselves on behalf of other companions.

There are advantages to this approach. MeshCore allows messages to traverse up to 64 hops away, which is an enormous real-world scale when LoRa repeaters can be many miles apart in ideal conditions. Even in the best possible case, Meshtastic's default 3-hop limit (albeit configurable up to 7) places a real limit on how far messages can spread.

It's very true that anyone can participate in MeshCore as a repeater, so all the tools to build your own mesh are certainly there. It's just that it requires some additional planning, coordination, and centralization that I don't view as totally necessary.

Thebiggerproblem I have with MeshCore is that many parts of it areproprietary. While the underlying protocol and the firmware for some radios is open source, all of the official MeshCore clients are proprietary, and even have features paywalled.

Proprietary software is simplynotdisaster-ready, and that goes doubly so for software reliant on central payment processors.

I amnotthe type of person who needs to use open-source software 100% of the time by any means (although it'd be nice), but theonlypoint in my mind of having an off-grid mesh network in the first place is total freedom and control, so in this particular case I simply cannot ever support a closed-source solution.

Efforts are already being made to create unofficialopen source clients for MeshCore. I won't discount this fact, but at the end of the day most people in the MeshCore ecosystem will be in theofficial, proprietary ecosystem, and I don't think MeshCore has enough advantages, users, or reliability to warrant adopting at this very early stage of mesh networking.

We have a unique opportunity as enthusiasts to adopt thebestmesh networking solution we can, before the "network effect" truly sets in and locks people in place to a particular platform. I think we can do better than Meshtastic and MeshCore.

## Problems

Unfortunately, both Meshtastic and MeshCore are highly limited, and don't scale well. Meshtasticbarelycan scale to a regional mesh in ideal scenarios, and while MeshCore fares better here, it's still unlikely to scale to the size of many larger regions, much less countries orplanets.

The thing is, Meshtastic and MeshCore are both moreapplicationsthan they areprotocols. They enable simple instant messaging communication over LoRa, but they don't give much thought to mesh networking applications beyond what their client apps officially support.

They're geared towards communicating with a small, local group, and any public meshes on these networks are really exceptions rather than the standard use-case.

Another problem is that Meshtastic and MeshCore both rely on LoRa pretty muchexclusively.

LoRa isverycool for building ad-hoc, low-bandwidth mesh networks, and it's a blessing that we have it available in most countries as an unlicensed option we can operate on without a ham radio license, and with modern digital technologies like encryption that are mostly forbidden on amateur radio.

It's hardly the perfect solution for many scenarios though, and it is quite slow.

In a perfect world, the mesh networking/routing software would be completely independent of the physical network that connects all these devices together.

For example, I want to be able to build cheap, local LoRa networks in neighborhoods and other regional communities, and interconnect them with more powerful point-to-point microwave connections, or even fiber or the internet.

Meshtastic (and I believe MeshCore via some unofficial "gateways") have some hacky methods of interconnecting different meshes with MQTT, but the experience is quite poor and it's clear that this type of connectivity is not a first-class experience on the network. Especially on Meshtastic, bridging to the internet with MQTT can degrade the network so much that it becomes impractical to use among any more than a handful of people.

Itshouldbe possible to build a mesh routing solution that intelligently routes packets between nodes over many different types of connections, completely seamlessly so that the experience of using the mesh never changes based on your specific interface.

Luckily for us, this has already been done!

## Reticulum

Reticulum is extremely cool.

It's a networking stack that intelligently provides strongly-encrypted routing over a wide variety of physical networks, including LoRa. Like MeshCore, it has automatic routing over paths on the network, but unlike MeshCore, those paths can traverse not only over LoRa but over any supportedinterface.

Additionally, like Meshtastic, Reticulum essentially works out of the box with devices operating on the same local network. Connect two devices on the same LoRa frequency and you have a functional mesh right away, with no advanced networking skills or dedicated repeaters required.

This makes Reticulum very well suitedbothfor small, private networks like Meshtastic, and for very large networks that MeshCore tends to work better with, likely going beyond MeshCore's capabilities with promises of planetary-level scalability.

## Good reading so far?

I write about data privacy, digital rights, and cybersecurity. I also make videos on YouTube. If you like any of this stuff, I'd love to let you know next time I post something 💙

Subscribe

 Email sent! Check your inbox to complete your signup.
 

No spam. Unsubscribe anytime.

The best part is that you can easily start small with Reticulum and everything will work perfectly fine, but once a member of your small network interconnects with a different Reticulum network simultaneously, the networks can seamlessly combine, enabling complete interoperability without the need to fiddle with settings or all agree on some common radio protocol as in Meshtastic-land.

You can mix-and-match Reticulum connections over LoRa radio, your local LAN network, point-to-point Wi-Fi or microwave connections, the internet, Tor or I2P, and even over networks like packet radio for the ham enthusiasts out there.

## Many Networks

Essentially, Reticulum can theoretically support any network you can interact with via TCP, UDP, or just a simple serial interface. It takes the bandwidth of all the networks you connect to into account when determining the best paths for messages to traverse, optimizing both for distance and to use the resources of each physical network efficiently.

Heterogeneous connectivityis Reticulum's bread and butter, basically. The project'sdocumentationprobably says it best:

In conventional networking, mixing different transport mediums typically requires gateways, translation layers, and careful configuration. A WiFi network doesn’t natively interoperate with a packet radio network without additional infrastructure, and you can’t just download a car over a serial port, or send an encrypted message in a QR code. Reticulum treats heterogeneity as a core premise. The protocol is designed to seamlessly mix mediums with vastly different characteristics [...]
For network designers, this means you are free to use whatever mediums are available, affordable, or appropriate for your situation. You might use LoRa for wide-area low-bandwidth coverage, WiFi for local high-capacity links, I2P for anonymous Internet connectivity, and Ethernet for infrastructure backhauls, all within the same network. Reticulum handles the translation and coordination automatically.

While I don't think homegrown mesh networks should be reliant on the internet or I2P in the long run, I think first-class support for connectivity over TCP and other internet protocols is still asignificantadvantage for people striving to build local, public mesh networks.

## Interconnected Local Meshes

Distinct local groups being able to interconnect is a huge boon for content availability on the network, and the beauty is that all these network links in Reticulum automatically become redundant as more connections are made.

A local mesh in Minneapolis could interconnect with a local mesh in Chicago over the internet, for example, but perhaps in the future some dedicated network operators arealsoable to establish a direct connection via microwave or LoRa between those cities. Connections may normally continue to traverse the internet at higher speeds, but in the event of an outage those alternate/ad-hoc paths can take over seamlessly, because they're all just paths on the same, single Reticulum network.

In the worst case scenario, a local Reticulum mesh lacking any connections to other Reticulum networks is going to fall back to only regional content availability, which is still themostthat you'll realistically get from Meshtastic and MeshCore.

Perhaps just as importantly, Reticulum enables connectivityacross borders.LoRa has a bit of a problem, which is that it operates on different frequencies in different jurisdictions. While LoRa operates on 915 MHz at up to 1 watt of power in the United States, it runs at 868 MHz (or 433 MHz) at much lower power levels in much of Europe, or 923 MHz in Asia, etc.

This means that a Meshtastic or MeshCore network in Asia will never natively connect to one in Europe. Again this could be worked around with "hacky" bridge solutions like MQTT, but Reticulum wouldnativelyinterconnect two different LoRa networks seamlessly as long as one common gateway point could be found: For example, an 868 MHz radio in one country connected to a 923 MHz radio in another via some other means like a fiber link, or a 2.4 GHz microwave connection, or the internet, or even packet radio. As long as some connectivity point (or multiple) can be found, then Reticulum routing between different physical networks would work seamlessly without any central servers required.

This is all possible without any sort of central coordination, which is the most important part of building a truly decentralized network. Network operators are free to create segments of the network in any way they see fit, and if/when those segments become connected, Reticulum handles the convergence of those networks automatically.

Reticulum's address space is global, and every node has a unique address guaranteed by the encryption Reticulum uses. There's no potential for different Reticulum networks to have overlapping addresses, and no need for a central authority to hand out addresses in the fashion that IANA/ARIN/RIPE/etc. hand out IP addresses on the traditional internet.

## Reticulum Applications

Although building the networkwellgives Reticulum a distinct advantage over Meshtastic and MeshCore, it is not enough to just build a network alone.

The developer of Reticulum realized this, of course, and built a number of applications that work on Reticulum seamlessly:NomadNetis one of the most popular, providing messaging, file sharing, and text-based browsing in a terminal app (which has mouse support too, thankfully).

Using a terminal won't appeal to many people though, so you can also useSideband, a GUI app for Android and PC, orMeshchatto communicate, as well as manyother apps which use Reticulum.

Fortunately, many of these communications apps work with each other, so you can choose between them at will. While you can really build essentially any app or protocol on top of Reticulum, many of the messengers standardize on a handful ofhomemade protocols: LXMF, LXST, and RRC.

While understanding what these protocols mean is not particularly important for people just looking to use the network, the important thing to know is that Reticulum already has an ecosystem of apps that connect with each other generally using the same underlying protocols, and provide similar functionality to Meshtastic's and MeshCore's apps for messaging and other functions.

## Reticulum's Biggest Problem

Unfortunately, despite being what I'd consider perhaps the perfect public mesh networking platform, Reticulum has a big drawback holding it back from supplanting public MeshCore and Meshtastic networks today, and it's not the apps or anything to do with the software.

Reticulum's main problem is that it does not have dedicated firmware for LoRa radios in the same way Meshtastic and MeshCore do.

Installing Meshtastic on a cheap device like aHeltec V3creates a full,standaloneMeshtastic node capable of sending & receiving messages, and relaying data throughout the network.

With Reticulum you can use the same cheap hardware with firmware called RNode to make LoRa connections. However, Reticulum's RNode firmware functions basically as a LoRamodemfor a connected computer, not as a standalone mesh node itself.

RNode is completely unintelligent, requiring a connection to a computer running Reticulum to send and receive messages and to route messages to other nodes on the Reticulum network.

For most people who would simply be using the network, this is not actually a problem. Even with Meshtastic, it is very rare for most people to try andcommunicateusing only a standalone device (one exception being the LILYGO T-Deck).

Instead, people commonly connect their Meshtastic-enabled LoRa radios to their phones or their computers, all of which are very capable devices which could easily run Reticulum while connected to RNode if people wanted to switch.

Where thisdoespresent a real problem to Reticulum is where it comes toinfrastructure.

In the world of Meshtastic and MeshCore, many people are running remote and often solar-powered nodes on high hilltops or buildings to selflessly increase the capacity of the network.

When it comes to Reticulum, these remote nodes would not only need a LoRa radio running RNode, but a full computer running Reticulum to enable the mesh capabilities. This computer could be as simple as a Raspberry Pi Zero, but even that level of additional priceand added power consumptionmakes this setup fairly untenable for many unattended installations, especially solar-powered ones.

Progressisbeing made on this front. In particular, a port calledmicroReticulumfor ESP32 and better devices is continually being developed. I really hope it succeeds, because the ability for current Meshtastic and MeshCore operators to switch to Reticulum routing with no additional hardware necessary could instantly, radically boost the adoption of a much more capable public mesh network like Reticulum in many communities.

## What's Next

There's work to be done here, but at the end of the day Reticulum is the only solution that promises to let people create local networks, large and small,andinterconnect those networks organically into a seamless, global mesh.

It's a killer feature that I think many people intuitivelywantfrom Meshtastic and MeshCore, but that those networks will never actually be able to provide.

I see a lot of advantages to all three of these apps. Meshtastic is really slick for a group of hikers who just want to text and share GPS easily instead of using voice walkie-talkies. MeshCore has some compelling features for local/neighborhood messaging, perhaps off-grid messaging at a large event like DEF CON.

If that's your use-case, then cool, but I am begging people with grander ambitions in the mesh networking space to focus on the most practical solution to the problem here.

There are many groups creating a region-wide or larger public Meshtastic network, when it is simply the wrong solution to the problem at hand, and this should be self-evident to anyone who's tried to use Meshtastic in this scenario.

I think many people get swept up in "collecting nodes" on Meshtastic and the thrill of seeing as many "connected" devices as they possibly can, but at least in my local area I see little consideration to how well-connected and functional the network actually is. When you look beyond being simplyawareof nodes in your local area, and actually try tointeractwith those nodes, failed messages and communication issues are common.

Reticulum offers not just a messenger app or a way to share GPS & other sensor data, but a full-fledged alternative to the internet itself. This enables critical applications that would not be possible on Meshtastic and MeshCore.

For example, I canshare access to any Kiwix file, including the entirety of Wikipedia, to anyone on Reticulum, which would make quick information sharing a breeze in a disaster scenario.

All of this is why I'm settling on Reticulum for what I want to build and see in the world. If other people are interested, I'll share more details about what I'm actually working on building myself here, and other mesh topics.

And certainly if you're in Northeast Minneapolis, get in touch. God only knows how critical tools like this could quickly become around here, and it's better to prepare today than be forced to learn all of this tomorrow 🙂

## Liked this article?

I post other things every once in a while too! I write about data privacy, digital rights, and cybersecurity. I also make videos on YouTube. If that's your jazz, I'll let you know next time I publish something 🤍

Subscribe

 Email sent! Check your inbox to complete your signup.
 

No spam. Unsubscribe anytime.