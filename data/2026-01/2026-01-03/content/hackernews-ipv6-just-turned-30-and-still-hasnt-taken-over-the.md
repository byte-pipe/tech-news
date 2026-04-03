---
title: IPv6 just turned 30 and still hasn’t taken over the world • The Register
url: https://www.theregister.com/2025/12/31/ipv6_at_30/
site_name: hackernews
fetched_at: '2026-01-03T11:06:34.759449'
original_url: https://www.theregister.com/2025/12/31/ipv6_at_30/
author: Brajeshwar
date: '2026-01-03'
---

#### Networks

# IPv6 just turned 30 and still hasn’t taken over the world, but don't call it a failure



## The world has passed it by in many ways, yet it remains relevant

FeatureIn the early 1990s, internetworking wonks realized the world was not many years away from running out of Internet Protocol version 4 (IPv4) addresses, the numbers needed to identify any device connected to the public internet. Noting booming interest in the internet, the internet community went looking for ways to avoid an IP address shortage that many feared would harm technology adoption and therefore the global economy.

A possible fix arrived in December 1995 in the form ofRFC 1883, the first definition of IPv6, the planned successor to IPv4.

The most important change from IPv4 to IPv6 was moving from 32-bit to 128-bit addresses, a decision that increased the available pool of IP addresses from around 4.3 billion to over 340 undecillion – a 39-digit number. IPv6 was therefore thought to have future-proofed the internet, because nobody could imagine humanity would ever need more than a handful of undecillion IP addresses, never mind the entire range available under IPv6.

As billions of devices and people came online, first using PCs and then wielding smartphones, conventional wisdom assumed that network operators would move to IPv6 rather than persist with IPv4.

Yet according to data fromGoogle,the Asia Pacific Network Information Center (APNIC), andCloudflare, less than half of all netizens use IPv6 today.

To understand why, know that IPv6 also suggested other, rather modest, changes to the way networks operate.

"IPv6 was an extremely conservative protocol that changed as little as possible," APNIC chief scientist Geoff Huston toldThe Register. "It was a classic case of mis-design by committee."

And that notional committee made one more critical choice: IPv6 was not backward-compatible with IPv4, meaning users had to choose one or the other – or decide to run both in parallel.

For many, the decision of which protocol to use was easy because IPv6 didn't add features that represented major improvements.

"One big surprise to me was how few features went into IPv6 in the end, aside from the massive expansion of address space," said Bruce Davie, a veteran computer scientist recently honored with alifetime achievement awardby the Association for Computing Machinery's Special Interest Group on Data Communications, which lauded him for "fundamental contributions in networking systems through design, standardization, and commercialization of network protocols and systems."

Davie said many of the security, plug-and-play, and quality of service features that didn't make it into IPv6 were eventually implemented in IPv4, further reducing the incentive to adopt the new protocol. "Given the small amount of new functionality in v6, it's not so surprising that deployment has been a 30 year struggle," he said.

Another innovation that meant IPv6 made less sense was network address translation (NAT), which allows many devices to share a single public IPv4 address. NAT meant IPv4 network operators could connect thousands of devices with a single IP address, meaning their existing IP addresses became more useful.

"These solutions were relatively easy to deploy, aligned with existing expertise, and avoided large-scale infrastructure changes," said Alvaro Vives, manager of the learning and development team at RIPE NCC, the regional internet registry for 76 nations across Europe, the Middle East, and Central Asia.

Because NAT stalled IPv6 adoption, vendors didn't rally behind the new protocol.

"Migration costs, complexity, and training requirements remain high, while short-term ROI is low," Gartner distinguished VP analyst Andrew Lerner toldThe Register. "Performance parity across applications and devices is inconsistent, and some organizations even disable IPv6 for better performance. Lack of dual-stack support in legacy infrastructure is another barrier," he added.

### A misunderstood protocol

While IPv6 didn't take off as expected, it's not fair to say it failed.

"IPv6 wasn't about turning IPv4 off, but about ensuring the internet could continue to grow without breaking," said John Curran, president and CEO of the American Registry for Internet Numbers (ARIN).

"In fact, IPv4's continued viability is largely because IPv6 absorbed that growth pressure elsewhere – particularly in mobile, broadband, and cloud environments," he added. "In that sense, IPv6 succeeded where it was needed most, and must be regarded as a success."

RIPE NCC's Alvaro Vives agrees. "What IPv6 got right was its long-term design," he toldThe Register. "It provides a vast address space that allows networks to be planned more simply and consistently. This has enabled innovation, from large mobile networks to the Internet of Things and advanced routing techniques such as Segment Routing over IPv6."

* Unofficial IETF draft calls for grant of five nonillion IPv6 addresses to ham radio operators
* IETF Draft suggests making IPv6 standard on DNS resolvers - partly to destroy IPv4
* China's IPv6 adoption takes a decent leap forward, especially on fixed networks
* Asia reaches 50 percent IPv6 capability and leads the world in user numbers

Gartner's Lerner thinks the time has come for organizations to develop detailed IPv6 migration plans.

"Validate application compatibility, and ensure new infrastructure supports IPv6," he advised. "Pilot deployments and lab testing with DNS64/NAT64 are recommended. Over time, IPv6 adoption will accelerate as private IPv4 space depletes and cloud providers introduce pricing models that favor IPv6."

APNIC's Huston, however, thinks that IPv6 has become less relevant to the wider internet.

"I would argue that we actually found a far better outcome along the way," he toldThe Register. "NATS forced us to think about network architectures in an entirely different way."

That new way is encapsulated in a new technology called Quick UDP Internet Connections (QUIC), that doesn't require client devices to always have access to a public IP address.

"We are proving to ourselves that clients don't need permanent assignment of IP address, which makes the client side of network far cheaper, more flexible, and scalable," he said.

Huston thinks IPv6 has also become less relevant to servers.

"These days the Domain Name Service (DNS) is the service selector, not the IP address," Huston toldThe Register. "The entire security framework of today's Internet is name based and the world of authentication and channel encryption is based on service names, not IP addresses."

"So folk use IPv6 these days based on cost: If the cost of obtaining more IPv4 addresses to fuel bigger NATs is too high, then they deploy IPv6. Not because it's better, but if they are confident that they can work around IPv6's weaknesses then in a largely name based world there is no real issue in using one addressing protocol or another as the transport underlay."

But there are plenty of organizations that still see a need for IPv6.Huawei sought 2.56 decillion IPv6 addressesand Starlink appears to have acquired150 sextillion, which is helping topush more countriespast 50 percent IPv6 adoption. ®



Get our

Tech Resources

Share

#### More about

* IPv4
* IPv6
* Network

More like these

×

### More about

* IPv4
* IPv6
* Network

### Narrower topics

* Black Hole
* Broadband
* Broadcom
* Cellular network
* Dynamic Host Configuration Protocol
* Email
* Ericsson
* Ethernet
* Firewall
* IETF
* InfiniBand
* Network interface card
* Network switch
* Radio Access Network
* Router
* SmartNIC
* Software-defined network
* Streaming video
* Submarine cable
* Systems Approach
* VPN
* World Wide Web

### Broader topics

* Internet

#### More about

Share

#### More about

* IPv4
* IPv6
* Network

More like these

×

### More about

* IPv4
* IPv6
* Network

### Narrower topics

* Black Hole
* Broadband
* Broadcom
* Cellular network
* Dynamic Host Configuration Protocol
* Email
* Ericsson
* Ethernet
* Firewall
* IETF
* InfiniBand
* Network interface card
* Network switch
* Radio Access Network
* Router
* SmartNIC
* Software-defined network
* Streaming video
* Submarine cable
* Systems Approach
* VPN
* World Wide Web

### Broader topics

* Internet

#### TIP US OFF

Send us news
