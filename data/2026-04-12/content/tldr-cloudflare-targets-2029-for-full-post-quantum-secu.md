---
title: Cloudflare targets 2029 for full post-quantum security
url: https://blog.cloudflare.com/post-quantum-roadmap/
site_name: tldr
content_file: tldr-cloudflare-targets-2029-for-full-post-quantum-secu
fetched_at: '2026-04-12T19:39:37.813605'
original_url: https://blog.cloudflare.com/post-quantum-roadmap/
date: '2026-04-12'
published_date: 2026-04-07T22:00+01:00
description: Recent advances in quantum hardware and software have accelerated the timeline on which quantum attack might happen. Cloudflare is responding by moving our target for full post-quantum security to 2029.
tags:
- tldr
---

# Cloudflare targets 2029 for full post-quantum security

2026-04-07

* Bas Westerbaan
8 min read

Cloudflare is accelerating its post-quantum roadmap. We now target2029to be fully post-quantum (PQ) secure including, crucially, post-quantum authentication.

At Cloudflare, we believe in making the Internet private and secure by default. We started by offeringfree universal SSL certificatesin 2014, began preparing ourpost-quantum migrationin 2019, and enabled post-quantum encryption forall websitesand APIs in 2022, mitigating harvest-now/decrypt-later attacks. While we’re excited by the fact that over65% of human trafficto Cloudflare is post-quantum encrypted, our work is not done until authentication is also upgraded. Credible new research and rapid industry developments suggest that the deadline to migrate is much sooner than expected. This is a challenge that any organization must treat with urgency, which is why we’re expediting our own internal Q-Day readiness timeline.

What happened? Last week, Googleannouncedthey had drastically improved upon the quantum algorithm to break elliptic curve cryptography, which is widely used to secure the Internet. They did not reveal the algorithm, but instead provided azero-knowledge proofthat they have one.

This is not even the biggest breakthrough. That same day, Oratomicpublisheda resource estimate for breaking RSA-2048 and P-256 on a neutral atom computer. For P-256, it only requires a shockingly low 10,000 qubits. Google’s motivation behind their recent announcement to also pursueneutral atomsalongside superconducting quantum computers becomes clear now. Although Oratomic explains their basic approach, they still leave out crucial detailson purpose.

These independent advances prompted Google to accelerate their post-quantum migration timeline to2029. What’s more, in their announcement andother talks, Google has placed a priority on quantum-secure authentication over mitigating harvest-now/decrypt-later attacks. As we discuss next, this priority indicates that Google is concerned about Q-Day coming as soon as 2030. Following the announcements, IBM Quantum Safe’s CTO is more pessimistic and can’t rule out quantum “moonshot attacks” on high value targetsas early as 2029.

The quantum threat is well known: Q-Day is the day that sufficiently capable quantum computers can break essential cryptography used to protect data and access across systems today.Cryptographically relevant quantum computers (CRQCs) don’t exist yet, but many labs across the world are pursuing different approaches to building one. Until recently, progress on CRQCs has been mostly public, but there is no reason to expect that will continue. Indeed, there is ample reason to expect that progress will leave the public eye. As quantum computer scientist Scott Aaronsonwarnedat the end of 2025:

[A]t some point, the people doing detailed estimates of how many physical qubits and gates it’ll take to break actually deployed cryptosystems using Shor’s algorithm are going to stop publishing those estimates, if for no other reason than the risk of giving too much information to adversaries. Indeed, for all we know, that point may have been passed already.

That point has now passed indeed.

## Why now: independent progress on three fronts

We’d like to spend some words on why it’s difficult to predict progress on quantum computing. Sudden “quantum” leaps in understanding, like the one we witnessed last week, can occur even if everything happens in the public eye. Simply put, breaking cryptography with a quantum computer requires engineering on three independent fronts: quantum hardware, error correction, and quantum software. Progress on each front compounds progress on the others.

Hardware.There are many different competing approaches. We mentioned neutral atoms and superconducting qubits, but there are also ion-trap, photonics, and moonshots like topological qubits. Complementary approaches can even becombined. Most of these approaches are pursued by several labs around the world. They all have their distinct engineering challenges and problems to solve before they can scale up. A few years ago, all of them had a long list of open challenges, and it was unclear if any of them would scale. Today most of them have made good progress. None have been demonstrated to scale yet: if they had, we wouldn’t have a couple of years left. But these approaches are much closer now, especially neutral atoms. To ignore this progress, you’d have to believe that every single approach will hit a wall.

Error correction.All quantum computers are noisy and require error-correcting codes to perform meaningful computation. This adds quite a bit of overhead, though how much depends on the architecture. More noise requires more error correction, but more interestingly, improved qubit connectivity allows for much more efficient codes. For a sense of scale: typically around a thousand physical qubits are required for one logical qubit for the superconducting quantum computers that are noisy and only have neighbor qubit connectivity. We knew “reconfigurable qubits” such as those of neutral-atom machines allow for an order of magnitude better error-correcting codes. Surprisingly, Oratomic showed the advantage is even larger: only about 3-4 physical neutral atom qubits are required per logical qubit.

Software.Lastly, the quantum algorithms to crack cryptography can be improved. This is Google’s breakthrough: they massively sped up the algorithm to crack P-256. On top of that, Oratomic showed further architecture specific optimizations for reconfigurable qubits.

The picture comes together: in 2025 neutral atoms turned out to be more scalable than expected, and now Oratomic figured out how to do much better error-correcting codes with such highly connected qubits. On top of that, breaking P-256 requires much less work. The result is that Q-Day has been pulled forward significantly from typical2035+ timelines, with neutral atoms in the lead, and other approaches not far behind.

In previous blog postswe’ve discussedhow different quantum computers compare on physical qubit count and fidelity, compared to the conservative goalpost of cracking RSA-2048 on a superconducting qubit architecture. This analysis gives us a rough idea of how much time we have, and it’s certainly better than trackingquantum factoring records, but it misses architecture-specific optimization and software improvements. What to watch for now is when the final missingcapabilitiesfor each architecture are achieved.

## It’s time to focus on authentication

Historically, the industry’s focus on post-quantum cryptography (PQC) has been based largely on PQencryption,which stops harvest-now/decrypt-later (HNDL) attacks. In an HNDL attack, an adversary harvests sensitive encrypted network traffic today and stores it until a future date when it can use a powerful quantum computer to decrypt the data. HNDL attacks are the primary threat when Q-Day is far away. That’s why our focus, thus far, has been on mitigating this risk, by adopting post-quantum encryption by default in our productssince 2022. Today, as we mentioned above,most Cloudflare productsare secure against HNDL attacks, and we’re working to upgrade the rest as we speak.

The other category of attacks is against authentication: adversaries armed with functioning quantum computers impersonate servers or forge access credentials. If Q-Day is far off, authentication is not urgent: deploying PQ certificates and signatures does not add any value, only effort.

An imminent Q-Day flips the script: data leaks are severe, but broken authentication is catastrophic. Any overlooked quantum-vulnerable remote-login key is an access point for an attacker to do as they wish, whether that’s to extort, take down, or snoop on your system. Any automatic software-update mechanism becomes aremote code executionvector. An active quantum attacker has it easy — they only need to find one trusted quantum-vulnerable key to get in.

When experts in the field of building quantum computers start patching authentication systems, we should all listen. The question is no longer "when will our encrypted data be at risk?" but "how long before an attacker walks in the front door with a quantum-forged key?"

### Prioritizing the most vulnerable systems

If quantum computers arrive in the next few years, they will be scarce and expensive. Attackers will prioritize high-value targets, like long-lived keys that unlock substantial assets or persistent access such as root certificates, API auth keys and code-signing certs. If an attacker is able to compromise one such key, they retain indefinite access until they are discovered or that key is revoked.

This suggests long-lived keys should be prioritized. That is certainly true if the quantum attack of a single key is expensive and slow, which is to be expected for the first generation of neutral atom quantum computers. That’s not the case for scalable superconducting quantum computers and later generations of neutral atom quantum computers, which could well crack keys much faster. Such fast CRQCs flip the script again, and an adversary with one might focus purely on HNDL attacks so that their attacks remain undetected. Google’s Sophie Schmiegcomparesthis scenario to Enigma’s cryptanalysis that changed the direction of World War II.

Adding support for PQ cryptography is not enough. Systems must disable support for quantum-vulnerable cryptography to be secure againstdowngrade attacks. In larger, especially federated systems such as the web, this is not feasible because not every client (browser) will support post-quantum certificates, and servers need to keep supporting these legacy clients. However, downgrade protection for HTTPS is still achievable using “PQ HSTS” and/orcertificate transparency.

Disabling quantum-vulnerable cryptography is not the last step: once done, all secrets such as passwords and access tokens previously exposed in the quantum-vulnerable system need to be rotated. Unlike post-quantum encryption, which takes one big push, migrating to post-quantum authentication has a long dependency chain — not to mention third-party validation and fraud monitoring. This will take years, not months.

It’s natural for organizations reading this to rush out and think about which internal systems they need to upgrade. But that’s not the end of the story. Q-day threatens all systems. As such, it’s important to understand the impact of a potential Q-day on third-party dependencies, both direct and indirect. Not just the third-parties you speak cryptography to, but also any third parties that are critical business dependencies like financial services and utilities.

With Q-day approaching on a shorter timeline, post-quantum authentication is top priority. Long-term keys should be upgraded first. Deep dependency chains and the fact that everyone has third-party vendors means this effort will take on the order of years, not months. Upgrading to post-quantum cryptography is not enough: to prevent downgrades, quantum-vulnerable cryptography must also be turned off.

## Cloudflare’s roadmap to full post-quantum security

Today, Cloudflare provides post-quantum encryption for the majority of our products mitigating harvest-now/decrypt-later. This is the product of work we startedover a decade agoto protect our customers and the Internet at large.

We are targeting full post-quantum security including authentication for our entire product suite by 2029. Here we’re sharing some intermediate milestones we’ve set, subject to change as our understanding of the risk and deployment challenges evolve.

## What we recommend

For businesses, we recommend making post-quantum support a requirement for any procurement. Common best practices, like keeping software updated and automating certificate issuance, are meaningful and will get you pretty far. We recommend assessing critical vendors early for what their failure to take action would mean for your business.

For regulatory agencies and governments: leading by setting early timelines has been crucial for industry-wide progress so far. We are now in a pivotal position where fragmentation in standards and effort between and within jurisdictions could put progress at risk. We recommend that governments assign and empower a lead agency to coordinate the migration on a clear timeline, stay security-focused, and promote the use of existing international standards. Governments need not panic, but can lead migration with confidence.

For Cloudflare customers, with respect to our services, you do not need to take any mitigating action. We are following the latest advancements in quantum computing closely and taking proactive steps to protect your data. As we have done in the past, we will turn on post-quantum security by default, with no switches to flip. What we don’t control is the other side: browsers, applications, and origins need to upgrade. Corporate network traffic on Cloudflare need not worry: Cloudflare One offersend-to-end protectionwhen tunnelling traffic through our post-quantum encrypted infrastructure.

Privacy and security are table stakes for the Internet. That's why every post-quantum upgrade we build will continue to be available to all customers, on every plan, atno additional cost. Making post-quantum security the default is the only way to protect the Internet at scale.

Free TLShelped encrypt the web. Free post-quantum cryptography will help secure it for what comes next.

Cloudflare's connectivity cloud protects 
entire corporate networks
, helps customers build 
Internet-scale applications efficiently
, accelerates any 
website or Internet application
, 
wards off DDoS attacks
, keeps 
hackers at bay
, and can help you on 
your journey to Zero Trust
.
Visit 
1.1.1.1
 from any device to get started with our free app that makes your Internet faster and safer.
To learn more about our mission to help build a better Internet, 
start here
. If you're looking for a new career direction, check out 
our open positions
.
 
 
Post-Quantum
Security