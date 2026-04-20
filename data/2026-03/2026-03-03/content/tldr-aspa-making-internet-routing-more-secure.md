---
title: 'ASPA: making Internet routing more secure'
url: https://blog.cloudflare.com/aspa-secure-internet/
site_name: tldr
content_file: tldr-aspa-making-internet-routing-more-secure
fetched_at: '2026-03-03T06:01:07.392876'
original_url: https://blog.cloudflare.com/aspa-secure-internet/
date: '2026-03-03'
published_date: 2026-02-27T14:00+08:00
description: ASPA is the cryptographic upgrade for BGP that helps prevent route leaks by verifying the path network traffic takes. New features in Cloudflare Radar make tracking its adoption easy.
tags:
- tldr
---

# ASPA: making Internet routing more secure

2026-02-27

* Mingwei Zhang
* Bryton Herdes
9 min read

Internet traffic relies on theBorder Gateway Protocol (BGP)to find its way between networks. However, this traffic can sometimes be misdirected due to configuration errors or malicious actions. When traffic is routed through networks it was not intended to pass through, it is known as aroute leak. We havewritten on our blogmultiple timesaboutBGP route leaksand the impact they have on Internet routing, and a few times we have even alluded to a future of path verification in BGP.

While the network community has made significant progress in verifying the final destination of Internet traffic, securing the actual path it takes to get there remains a key challenge for maintaining a reliable Internet. To address this, the industry is adopting a new cryptographic standard calledASPA (Autonomous System Provider Authorization), which is designed to validate the entire path of network traffic and prevent route leaks.

To help the community track the rollout of this standard, Cloudflare Radar has introduced a new ASPA deployment monitoring feature. This view allows users to observe ASPA adoption trends over time across the fiveRegional Internet Registries (RIRs), and view ASPA records and changes over time at theAutonomous System (AS)level.

## What is ASPA?

To understand how ASPA works, it is helpful to look at how the Internet currently secures traffic destinations.

Today, networks use a secure infrastructure system calledRPKI (Resource Public Key Infrastructure), which has seensignificant deployment growthover the past few years. Within RPKI, networks publish specific cryptographic records called ROAs (Route Origin Authorizations). A ROA acts as a verifiable digital ID card, confirming that an Autonomous System (AS) is officially authorized to announce specific IP addresses. This addresses the "origin hijacks" issue, where one network attempts to impersonate another.

ASPA (Autonomous System Provider Authorization)builds directly on this foundation. While a ROA verifies thedestination, an ASPA record verifies thejourney.

When data travels across the Internet, it keeps a running log of every network it passes through. In BGP, this log is known as theAS_PATH(Autonomous System Path). ASPA provides networks with a way to officially publish a list of their authorized upstream providers within the RPKI system. This allows any receiving network to look at theAS_PATH, check the associated ASPA records, and verify that the traffic only traveled through an approved chain of networks.

A ROA helps ensure the traffic arrives at the correct destination, ASPA ensures the traffic takes an intended, authorized route to get there. Let’s take a look at how path evaluation actually works in practice.

## Route leak detection with ASPA

How does ASPA know if a route is adetour? It relies on the hierarchy of the Internet.

In a healthy Internet routing topology (e.g.“valley-free” routing), traffic generally follows a specific path: it travels "up" from a customer to a large provider (like a major ISP), optionally crosses over to another big provider, and then flows "down" to the destination. You can visualize this as a “mountain” shape:

1. The Up-Ramp:Traffic starts at a Customer and travels "up" through larger and larger Providers (ISPs), where ISPs pay other ISPs to transit traffic for them.
2. The Apex:It reaches the top tier of the Internet backbone and may cross a single peering link.

The Down-Ramp:It travels "down" through providers to reach the destination Customer.

A visualization of "valley-free" routing. Routes propagate up to a provider, optionally across one peering link, and down to a customer.

In this model, a route leak is like a valley, or dip. One type of such leak happens when traffic goes down to a customer and then unexpectedly tries to go backupto another provider.

This "down-and-up" movement is undesirable as customers aren't intended nor equipped to transit traffic between two larger network providers.

#### How ASPA validation works

ASPA gives network operators a cryptographic way to declare theirauthorized providers,enabling receiving networks to verify that an AS path follows this expected structure.

ASPA validates AS paths by checking the “chain of relationships” from both ends of the routes propagation:

* Checking the Up-Ramp:The check starts at the origin and moves forward. At every hop, it asks:"Did this network authorize the next network as a Provider?"It keeps going until the chain stops.
* Checking the Down-Ramp:It does the same thing from the destination of a BGP update, moving backward.

If the "Up" path and the "Down" path overlap or meet at the top, the route isValid. The mountain shape is intact.

However, if the two valid pathsdo not meet, i.e. there is a gap in the middle where authorization is missing or invalid, ASPA reports such paths as problematic. That gap represents the "valley" or the leak.

#### Validation process example

Let’s look at a scenario where a network (AS65539) receives a bad route from a customer (AS65538).

The customer (AS65538) is trying to send traffic received from one provider (AS65537) "up" to another provider (AS65538), acting like a bridge between providers. This is aclassic route leak. Now let’s walk the ASPA validation process.

1. We check theUp-Ramp: The original source (AS65536) authorizes its provider. (Check passes).
2. We check theDown-Ramp: We start from the destination and look back. We see the customer (AS65538).
3. The Mismatch:The up-ramp ends at AS65537, while the down-ramp ends at 65538. The two ramps do not connect.

Because the "Up" path and "Down" path fail to connect, the system flags this as ASPAInvalid. ASPA is required to do this path validation, as without signed ASPA objects in RPKI, we cannot find which networks are authorized to advertise which prefixes to whom. By signing a list of provider networks for each AS, we know which networks should be able to propagate prefixes laterally or upstream.

### ASPA against forged-origin hijacks

ASPA can serve as an effective defense againstforged-origin hijacks, where an attacker bypasses Route Origin Validation (ROV) by pretending and advertising a BGP path to a real origin prefix. Although the origin AS remains correct, the relationship between the hijacker and the victim is fabricated.

ASPA exposes this deception by allowing the victim network to cryptographically declare its actual authorized providers; because the hijacker is not on that authorized list, the path is rejected as invalid, effectively preventing the malicious redirection.

ASPA cannot fully protect against forged-origin hijacks, however. There is still at least one case where not even ASPA validation can fully prevent this type of attack on a network. An example of a forged-origin hijack that ASPA cannot account for is when a provider forges a path advertisementto their customer.

Essentially, a provider could “fake” a peering link with another AS to attract traffic from a customer with a short AS_PATH length, even when no such peering link exists. ASPA does not prevent this path forgery by the provider, because ASPA only works off of provider information and knows nothing specific about peering relationships.

So while ASPA can be an effective means of rejecting forged-origin hijack routes, there are still some rare cases where it will be ineffective, and those are worth noting.

## Creating ASPA objects: just a few clicks away

Creating an ASPA object for your network (or Autonomous System) is now a simple process in registries likeRIPEandARIN. All you need is your AS number and the AS numbers of the providers you purchase Internet transit service from. These are the authorized upstream networks you trust to announce your IP addresses to the wider Internet. In the opposite direction, these are also the networks you authorize to send you a full routing table, which acts as the complete map of how to reach the rest of the Internet.

We’d like to show you just how easy creating an ASPA object is with a quick example.

Say we need to create the ASPA object for AS203898, an AS we use for our Cloudflare London office Internet. At the time of writing we have three Internet providers for the office: AS8220, AS2860, and AS1273. This means we will create an ASPA object for AS203898 with those three provider members in a list.

First, we log into the RIPERPKI dashboardand navigate to theASPAsection:

Then, we click on “Create ASPA” for the object we want to create an ASPA object for. From there, we just fill in the providers for that AS.

It’s as simple as that. After just a short period of waiting, we can query the global RPKI ecosystem and find our ASPA object for AS203898 with the providers we defined.

It’s a similar story withARIN, the only otherRegional Internet Registries (RIRs)that currently supports the creation of ASPA objects. Log in toARIN online,then navigate to Routing Security, and click “Manage RPKI”.

From there, you’ll be able to click on “Create ASPA”. In this example, we will create an object for another one of our ASNs, AS400095.

And that’s it – now we have created our ASPA object for AS40095 with provider AS0.

The “AS0” provider entry is special when used, and means the AS owner attests there arenovalid upstream providers for their network. By definition this means every transit-free Tier-1 network should eventually sign an ASPA with only “AS0” in their object, if they truly only have peer and customer relationships.

## New ASPA features in Cloudflare Radar

We have added a new ASPA deployment monitoring feature toCloudflare Radar. The new ASPA deployment view allows users to examine the growth of ASPA adoption over time, with the ability to visualize trends across the fiveRegional Internet Registries(RIRs) based on AS registration.

We have also integrated ASPA data directly into the country/region and ASN routing pages. Users can now track how different locations are progressing in securing their infrastructure, based on the associated ASPA records from the customer ASNs registered locally.

There are also new features when you zoom into a particular Autonomous System (AS), for exampleAS203898.

We can see whether a network’s observed BGP upstream providers are ASPA authorized, their full list of providers in their ASPA object, and the timeline of ASPA changes that involve their AS.

## The road to better routing security

With ASPA finally becoming a reality, we have our cryptographic upgrade for Internet path validation. However, those who have been around since the start of RPKI for route origin validation knowthis will be a long roadto actually providing significant value on the Internet. Changes are needed to RPKI Relaying Party (RP) packages, signer implementations, RTR (RPKI-to-Router protocol) software, and BGP implementations to actually use ASPA objects and validate paths with them.

In addition to ASPA adoption, operators should also configure BGP roles as described withinRFC9234. The BGP roles configured on BGP sessions will help future ASPA implementations on routersdecide which algorithm to apply:upstreamordownstream. In other words, BGP roles give us the power as operators to directly tie our intended BGP relationships with another AS to sessions with those neighbors. Check with your routing vendors and make sure they supportRFC9234 BGP roles and OTC(Only-to-Customer) attribute implementation.

To get the most out of ASPA, we encourage everyone to create their ASPA objects for their AS.Creating and maintaining these ASPA objects requires careful attention. In the future, as networks use these records to actively block invalid paths, omitting a legitimate provider could cause traffic to be dropped. However, managing this risk is no different from how networks already handle Route Origin Authorizations (ROAs) today. ASPA is the necessary cryptographic upgrade for Internet path validation, and we’re happy it’s here!

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


Security Week
BGP
RPKI
Routing
Routing Security
Radar
