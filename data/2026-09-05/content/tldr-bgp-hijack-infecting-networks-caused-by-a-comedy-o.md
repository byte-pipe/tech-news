---
title: BGP hijack infecting networks caused by a comedy of errors that’s not funny at all - Ars Technica
url: https://arstechnica.com/security/2026/09/well-executed-bgp-attack-uses-hijacked-ips-to-infect-real-networks/
site_name: tldr
content_file: tldr-bgp-hijack-infecting-networks-caused-by-a-comedy-o
fetched_at: '2026-09-05T20:58:11.916473'
original_url: https://arstechnica.com/security/2026/09/well-executed-bgp-attack-uses-hijacked-ips-to-infect-real-networks/
date: '2026-09-05'
published_date: '2026-09-02T11:00:43+00:00'
description: What can we learn from a BGP hijacking that poisoned production software? Plenty.
tags:
- tldr
---

Text
 settings

Hackers carried out a supply chain attack that installed malware on networks using an unusual technique: hijacking a chunk of Internet space where cloud management software used by hosting providers, data centers, and other large infrastructure companies is updated.

In a well-coordinated operation, the unknown attackers exploited weaknesses in the routing security setup of hosting provider Hetzner Online and the process for attaining valid TLS certificates. The lapses allowed the attackers to successfully perform a BGP (Border Gateway Protocol) hijacking to obtain control over IP addresses assigned to Softaculous. The company, based in the United Arab Emirates, is the maker of a platform for installing and managing Web software and is the developer of Virtualizor, a management platform for virtualized environments.

Softaculous used the IPs to issue updates and host a client and billing site. With control over the hijacked space, the attacker was now using the addresses to push malware masquerading as updates to unsuspecting users.

## Silly, preventable mistakes

Lax configuration of routing security in Softaculous’ hosting provider, Hetzner Online, was the major contributor to the hack. A large number of other errors contributed to the success of the attack. Most notably, Softaculous failed to follow one of the most common safety steps in software development, which is to validate software updates using code signing.

“During the incident window, a Virtualizor installation whose traffic was diverted could have received a malicious update package from the attacker’s server,” Softaculouswarned Monday. “Our product update clients did not yet cryptographically verify update packages, so a modified package would not have been rejected on that basis. We believe only a small number of servers were actually affected, but we cannot produce a definitive list, so please treat every Virtualizor server as in scope for the checks below.”

A loose configuration by Hetzner Online allowed hijackers to intermittently misdirect traffic over two spans in a 33-hour window. Hetzner Online reclaimed the address space 12 hours after the hijacking started by announcing the correct path. Then Hetzner Online stopped announcing the path, and the attacker executed the same hijack a second time. This time, it took Hetzner almost 10 hours to react. During that time, the hijack was active.

Like Hetzner Online, both Softaculous and Zet.net, the transit peer downstream from Hetzner Online, failed to properly monitor their systems and, as a result, didn’t catch the hijacking until it had been ongoing on and off for 22 hours. There are also questions about another host provider, Nexon Host, whose infrastructure somehow facilitated the malicious announcement.

Ben Cartwright-Cox, a BGP expert and creator of the BGP Tools suite, called the lapses “silly, preventable mistakes.” Softaculous, Hetzner, and Zet.net didn’t immediately respond to emailed questions.

## A brief history of BGP

BGP attacks target the underpinnings that make the Internet a unified, worldwide network. The Internet is splintered into many ASes (autonomous systems). Each AS is an independent network assigned a portion of the 3.7 billion publicly available addresses under the IPv4 protocol. BGP acts as the glue that binds all these ASes together and allows each one to connect to any other.

To allow an address assigned to an AS in, say, Germany to reach IPs in North America, an AS must “announce” the route a given IP range should follow. These routing announcements are declarations made as entries on a global routing table used by all ASes and the hosting providers serving them. In the Internet’s early days, BGP ran on trust. Providers simply assumed announcements were valid and made in good faith.

Over the years, attackers repeatedly abused this trust by making announcements for IPs they had no valid right to control. Attackers—with ties to bothnation-statesandfinancially motivatedgroups—capitalized on the lax system to, in some cases, route petabytes’ worth of sensitive data through networks they controlled.

Eventually, Internet architects developed a series of measures to prevent such hijacking. The most prominent of these is RPKI (Resource Public Key Infrastructure) ROV (Route Origin Validation). RPKI ROV uses cryptographic records called Route Origin Authorizations (ROAs) to assert the proper origin and prefix mask length of routes in BGP. ASes that deploy RPKI ROV will reject routes that don’t match the information contained in ROAs, preventing hijacks from spreading throughout the Internet.

## How it went down

The attack began a few minutes before 9 PM UTC on Friday, when a small chunk of Softaculous IP space entered the global routing table. This new IP prefix, designated as 162.55.80.0/24, was announced along the path: AS6204 (Zet.net), AS62390 (Nexon Host), and AS24940 (Hetzner Online).

This IP range, containing 256 addresses, hosted Softaculous’ software-update endpoint and its client and billing site. The space was a more specific chunk of the much bigger 162.55.0.0/16 space that was usually originated by AS24940. According to apostby BGP expert Doug Madory, the announcement likely originated with NexonHost (AS62390), possibly through a compromise of its infrastructure or a customer who exploited gaps in its security.

Protocols such as RPKI prevent large operators from routing addresses made through fraud or error, but the routing lapses and the failure to properly monitor traffic allowed the hijack to pulse on and off for much of the weekend. Madory, who is head of Internet analysis at Infoblox, continued:

The hijack also included an AS path with a forged origin. Because the attacker appended 24940 as the rightmost ASN in the path, it was considered RPKI-valid for two reasons: the ROA required the origin to be AS24940 but also because it allowed the prefix length to be anywhere between 24 and 16. As a result, this route was RPKI-valid and would not be at risk of being dropped by ASes that reject RPKI-invalid routes.

Both Cartwright-Cox and Madory said Hetzner configured these settings in a way that allowed the hijacking to fly under the radar provided by these security measures.

IP ranges are measured in blocks, with the size of them designated by a slash followed by a number. Somewhat counterintuitively, the larger the number at the end, the smaller the block is. That’s becausethe systemis based on the 32 bits forming the basis of the IPv4 standard. A /24 block designates 2(32-24), or 256 addresses. A /16 block designates 2(32-16), or 65,536 IPs.

Hetzner Online configured a parameter in RPKI that allowed sub-prefixes as small as /24 to be considered valid. Combined with the fact that the hijacked route contained an AS path forged to match the origin in the ROA, the attacker’s new route with a smaller prefix was able to bypass RPKI protections.

“Because there was no existing route for 162.55.80.0/24 to compete against, it propagated as far as other route filtering mechanisms would allow,” Madory wrote. “And because it was a more-specific route, any traffic destined for this IP range would prefer it over the legitimate route (162.55.0.0/16) due to routers’ preference for longest-prefix-match.”

Cartwright-Cox succinctly described the lapse as: “Hetzner allowed more precise IP ranges (/24 when it should have been /16) to be announced, allowing the hijacker to impersonate them and automatically win on routing decisions.”

## Bypassing TLS certificate validation

The smaller IP range also made it possible for the attackers to bypass industry-wide measures for validating TLS certificate requests. Typically, the requesting party must demonstrate that it has control of the domain over a geographically dispersed set of end points.Let’s Encrypt, the certificate authority that issued the certificates used in the hijacking, requires a quorum of them to return a positive result before a certificate is issued.

By targeting the smaller /24 range, the hijack spread globally, “causing the validation perspectives (and all other traffic) to reach the attacker’s server instead of the legitimate domain operator,” Let’s Encrypt said in an email. It also said thatCertification Authority Authorization(CAA) account binding, which limits acceptable issuers and validation methods, “would have made this significantly more difficult for the attacker.”

It remains unclear how many Virtualizor users received the malicious update or what the malware did once installed. Softaculous is urging all its users to check their systems for signs of compromise.

The incident is one of the few times a BGP hijacking has been known to be used to spread malware. One event occurred in 2015 when the mercenary hacker collective Hacking Teamused oneagainst a target it had been contracted to infect. Anotherhappened in 2022when attackers hijacked IP addresses belonging to Amazon. The attackers used the IP addresses to host a smart contract that drained about $235,000 in bitcoin from people trying to visit the Celer Bridge cryptocurrency exchange.

Thankfully, BGP hijackings are becoming less common with the widespread adoption of RPKI. This weekend’s event demonstrates that it only takes one mistake for these protections to go off the rails.

 Dan Goodin
 

Senior Security Editor

 Dan Goodin
 

Senior Security Editor

 Dan Goodin is Senior Security Editor at Ars Technica, where he oversees coverage of malware, computer espionage, botnets, hardware hacking, encryption, and passwords. In his spare time, he enjoys gardening, cooking, and following the independent music scene. Dan is based in San Francisco. Follow him at 
here
 on Mastodon and 
here
 on Bluesky. Contact him on Signal at DanArs.82.
 

1. 1.OpenAI agents discussed ways to escape their sandbox on public wiki
2. 2.I rented a car, and within hours, my driver's license was for sale
3. 3.After 8 years, Europe's BepiColombo mission is on final approach to Mercury
4. 4.Meet the 2026 Ig Nobel Prize winners
5. 5.Pentagon rescinds new testosterone screening policy without explanation

Customize