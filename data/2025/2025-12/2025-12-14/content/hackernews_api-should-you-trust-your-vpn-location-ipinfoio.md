---
title: Should You Trust Your VPN Location? | IPinfo.io
url: https://ipinfo.io/blog/vpn-location-mismatch-report
site_name: hackernews_api
fetched_at: '2025-12-14T11:06:38.017596'
original_url: https://ipinfo.io/blog/vpn-location-mismatch-report
author: mmaia
date: '2025-12-13'
description: 17 out of 20 popular VPNs exit traffic from different countries than they claim. Dig into what that means and why it matters in our VPN report.
tags:
- hackernews
- trending
---

* IP Data Fundamentals
* IP Data Accuracy
* Solving Business Challenges
* Getting Started
* Optimizing and Scaling
* Community and Thought Leadership
* Company News and Updates
6 days ago

by

Ben Dowling

—
10
 min read

# Should You Trust Your VPN Location?

In a large-scale analysis of 20 popular VPNs, IPinfo found that 17 of those VPNs exit traffic fromdifferent countries than they claim. Some claim 100+ countries, but many of them point to the same handful of physical data centers in the US or Europe.

That means the majority of VPN providers we analyzed don’t route your traffic via the countries they claim to, and they claim many more countries than they actually support.

Analyzing over150,000 exit IPsacross137 possible exit countries,and comparing what providers claim to what IPinfo measures, shows that:

* 17 in 20 providershad traffic exiting in a different country.
* 38 countrieswere “virtual-only” in our dataset (claimed by at least one provider, but never observed as the actual traffic exit country for any provider we tested).
* We were only able to verify all provider announced locations for3 providersout of the 20.
* Across ~150,000 VPN exit IPs tested, ProbeNet, our internet measurement platform, detected roughly8,000 caseswhere widely-used IP datasets placed the server in the wrong country — sometimes thousands of kilometers off.

This report walks through what we saw across VPN and IP data providers, provides a closer look at two particularly interesting countries, explores why measurement-based IP data matters if you care where your traffic really goes, and shares how we ran the investigation.

## Which VPNs Matched Reality (And Which Didn’t)

Here is the overlap between the number of listed countries each VPN provider claims to offer versus the countries with real VPN traffic that we measured — lower percentages indicate providers whose claimed lists best match our data:

Provider

Claimed Countries

% Virtual or Unmeasurable

IPVanish

108

61

CyberGhost

100

57

ExpressVPN

105

57

NordVPN

126

53

Private Internet Access

91

52

ProtonVPN

110

51

FastVPN

112

49

X-VPN

89

43

Surfshark

100

41

BelkaVPN

63

41

ZoogVPN

76

34

VyprVPN

63

27

FastestVPN

47

26

TrustZone

39

18

PrivateVPN

62

13

TunnelBear

47

9

VeePN

84

6

IVPN

41

0

Mullvad

50

0

Windscribe

70

0

It's important to note that we used the most commonly and widely supported technologies in this research, to make comparison between providers as fair as possible while giving us significant data to analyze, so this will not be the full coverage for each provider.

These are some of the most visible names in the market. They also tend to have very long country lists on their websites. Notably, three well-known providers had zero mismatches across all the countries we tested: Mullvad, IVPN, and Windscribe.

Country mismatches doesn’t automatically mean some providers offer “bad VPNs,” but it does mean that if you’re choosing a VPN because it claims “100+ countries,” you should know that a significant share of those flags may be labels, or virtual locations.

## What “Virtual Locations” Really Mean

When a VPN lets you connect to, for example, “Bahamas” or “Somalia,” that doesn’t always mean traffic routes through there. In many cases, it’s somewhere entirely different, like Miami or London, but presented as if traffic is in the country you picked.

This setup is known as a virtual location:

* The VPN app shows “Country X” (e.g. Bahamas).
* The IP registry data also says “Country X” — because the provider self-declared it that way.
* But the network measurements (latency and routing) show the traffic actually exits in “Country Y” — often thousands of kilometers away.

The problem? Without active network measurement, most IP datasets will rely on what the IP’s owner told the internet registry or published in WHOIS/geofeeds: a self-reported country tag. If that record is wrong or outdated, the mistake spreads everywhere. That’s where IPinfo’s ProbeNet comes in: by running live RTT tests from 1,200+ points of presence worldwide, we anchor each IP to its real-world location, not just its declared one.

Across the dataset, we found97 countrieswhere at least one VPN brand only ever appeared as virtual or unmeasurable in our data. In other words, for a noticeable slice of the world map, some “locations” in VPNs never show up as true exits in our measurements.

We also found38 countrieswhere every mention behaved this way: at least one VPN claimed them, butnoneever produced a stable, measurable exit in that country in our sample.

You can think of these 38 as the “unmeasurable” countries in this study – places that exist in server lists, config files, and IP geofeeds, but never once appeared as the actual exit country in our measurements. They’re not randomly scattered – they cluster in specific parts of the map. By region, that includes:

This doesn’t prove there is zero VPN infrastructure in those countries globally. It does show that, across the providers and locations we measured, the dominant pattern is to serve those locations from elsewhere. Here are three of the most interesting examples of how this looks at the IP level.

## Case Studies: Two Countries That Only Exist on the Map

To make this concrete, let’s look at three countries where every provider in our dataset turned out to be virtual:Bahamas, andSomalia.

### Bahamas: All-Inclusive, Hosted in the US

In our measurements, five providers offered locations labeled as “Bahamas”: NordVPN, ExpressVPN, Private Internet Access, FastVPN, and IPVanish.

For all of them, measured traffic was in the United States, usually with sub-millisecond RTT to US probes.

Provider

Claimed as

Measured exit country

RTT to nearest ProbeNet vantage point in (evidence)

Example exit IP

NordVPN

🇧🇸

Bahamas

🇺🇸United States

0.27 ms from Miami, United States

45.95.160.61

ExpressVPN

🇧🇸

Bahamas

🇺🇸United States

0.15 ms from Miami, United States

64.64.117.18

Private Internet Access

🇧🇸

Bahamas

🇺🇸United States

0.42 ms from New York, United States

95.181.238.101

FastVPN

🇧🇸

Bahamas

🇺🇸United States

0.42 ms from Miami, United States

108.171.106.198

IPVanish

🇧🇸

Bahamas

🇺🇸United States

0.37 ms from Miami, United States

108.171.106.207

### Somalia: Mogadishu, via France and the UK

Somalia appears in our sample for only two providers: NordVPN and ProtonVPN.

Both label Mogadishu explicitly in their naming, but these RTTs are exactly what you’d expect for traffic in Western Europe, and completely inconsistent with traffic in East Africa. Both providers go out of their way in the labels (e.g. “SO, Mogadishu”), but the actual traffic is in Nice and London, not Somalia.

Provider

Claimed as

Measured exit country

RTT to nearest probe (evidence)

Example exit IP

NordVPN

🇸🇴

Somalia

🇫🇷France

0.33 ms from Nice, France

212.32.91.11

ProtonVPN

🇸🇴

Somalia

🇬🇧United Kingdom

0.37 ms from London, UK

74.118.126.204

## When Legacy IP Providers Agree With the Wrong VPN Locations

So far, we’ve talked about VPN claims versus our measurements. But other IP data providers don’t run active RTT tests. They rely on self-declared IP data sources, and often assume that if an IP is tagged as “Country X,” it must actually be there.

In these cases, the IP legacy datasets typically “follow” the VPN provider’s story: if the VPN markets the endpoint as Country X, the legacy IP dataset also places it in Country X.

To quantify that, we looked at 736 VPN exits where ProbeNet’s measured country disagreed with one or more widely used legacy IP datasets.

We then compared the country IPinfo's ProbeNet measured (backed by RTT and routing) with the country reported by these other IP datasets and computed the distance between them. The gaps are large:

### How Far Off Were the Other IP Datasets?

Distance between legacy IP databases and IPinfo country

Share of disagreement cases

> 1,000 km

83%

> 2,000 km

63%

> 5,000 km

28%

> 8,000 km

12%

The median error between ProbeNet and the legacy datasets was roughly 3,100 km.On the ProbeNet side, we have strong latency evidence that our measured country is the right one:

* The median minimum RTTto a probe in the measured country was0.27 ms.
* About90%of these locations had asub-millisecondRTT from at least one probe.

That’s what you expect when traffic is genuinely in that country, not thousands of kilometers away.

### An IP Example You Can Test Yourself

This behavior is much more tangible if you can see it on a single IP.

Here'sone VPN exit IPwhere ProbeNet places the server in the United Kingdom, backed by sub-millisecond RTT from local probes, while other widely used legacy IP datasets place the same IP in Mauritius, 9,691 kilometers away.

🇬🇧 United Kingdom vs 🇲🇺 Mauritius (ProtonVPN)

If you want to check this yourself, you can plug it into a public measurement tool likehttps://ping.sx/and run pings or traceroutes from different regions. Tools like this one provide a clear visual for where latency is lowest.

ProbeNet uses the same basic idea, but at a different scale: we maintain a network of 1,200+ points of presence (PoPs) around the world, so we can usually get even closer to the real physical location than public tools with smaller networks.

If you’d like to play with more real IPs (not necessarily VPNs) where ProbeNet and IPinfo get the country right and other datasets don’t, you can find a fuller set of examples on our IP geolocationaccuracy page.

## Why This Happens and How It Impacts Trust

It’s worth separating technical reasons from trust issues. There are technical reasons to use virtual or hubbed infrastructure:

* Risk & regulation.Hosting in certain countries can expose both the provider and users to local surveillance or seizure.
* Infrastructure quality.Some regions simply don’t have the same density of reliable data centers or high-capacity internet links, so running servers there is harder and riskier.
* Performance & cost.Serving “Bahamas” from Miami or “Cambodia” from Singapore can be cheaper, faster, and easier to maintain.

From this perspective, a virtual location can be a reasonable compromise: you get a regional IP and content unblocking without the downsides of hosting in a fragile environment.

### Where It Becomes a Trust Problem

Three things change the picture:

* Lack of disclosure.Marking something clearly as “Virtual Bahamas (US-based)” is transparent. Listing “Bahamas” alongside “Germany” without any hint that one is virtual and the other is physical blurs the line between marketing and reality.
* Scale of the mismatch.It’s one thing to have a few virtual locations in hard-to-host places. It’s another when dozens of countries exist only as labels across your entire footprint, or when more than half of your tested locations are actually somewhere else.
* Downstream reliance.Journalists, activists, and NGOs may pick locations based on safety assumptions. Fraud systems, compliance workflows, and geo-restricted services may treat “Somalia” vs “France” as a meaningful difference. If both the VPN UI and the IP data say “Somalia” while the traffic is physically in France, everyone is making decisions on a false premise.

That last point leads directly into the IP data problem that we are focused on solving.

## So How Much Should You Trust Your VPN?

If you’re a VPN user, here are some practical takeaways from this work:

* Treat “100+ countries” as a marketing number, not a guarantee.In our sample, 97 countries existed only as claims, not reality, across 17 providers.
* Check how your provider talks about locations.Do they clearly label “virtual” servers? Document where they’re actually hosted? Or do they quietly mix virtual and physical locations in one long list?
* If you rely on IP data professionally, ask where it comes from.A static “99.x% accurate worldwide” claim doesn’t tell you how an IP data provider handles fast-moving, high-stakes environments like VPN infrastructure.

Ultimately, this isn’t an argument against VPNs, or even against virtual locations. It’s an argument for honesty and evidence. If a VPN provider wants you to trust that map of flags, they should be willing, and able, to show that it matches the real network underneath.

## How IPinfo Approaches IP Data Differently

Most legacy IP data providers rely on regional internet registry (RIR) allocation data and heuristics around routing and address blocks. These providers will often accept self-declared data like customer feedback, corrections, and geofeeds, without a clear way to verify them.

IPinfo takes a measurement-first approach:

1. Proprietary ProbeNet with 1,200+ points of presenceWe maintain an internet measurement platform of PoPs in locations around the world.
2. Active measurementsFor each visible IP on the internet, including both IPv4 and IPv6 addresses, we measure RTT from multiple probes.
3. Evidence-based geolocationWe combine these measurements with IPinfo’s other signals to assign a country (and more granular location) that’s grounded in how the internet actually behaves.

This measurement-first approach is unique in the IP data space. Once we realized how much inaccuracy came from self-declared data, we started investing heavily in research and building ProbeNet to use active measurements at scale. Our goal is to make IP data as evidence-based as possible, verifying with observation on how the internet actually behaves.

## Our Methodology for This Report

We approached this VPN investigation the way a skeptical but well-equipped user would: start from the VPNs’ own claims, then test them.

### Step 1: Collecting What Providers Say

For each of the20 VPN providers, we pulled together three kinds of data:

* Marketing promises:The “servers in X countries” claims and country lists from their websites. When a country was clearly listed there, we treated it as the locations they actively promote.
* Configurations and locations lists:Configurations from different protocols like OpenVPN or WireGuard were collected along with location information available on provider command-line tools, mobile applications, or APIs.
* Unique provider–location entries:We ended up with over 6,000,000 data points and a list of provider + location combinations we could actually try to connect to with multiple IPs each.

### Step 2: Observing Where the Traffic Really Goes

Next, we used IPinfo infrastructure and ProbeNet to dial into those locations and watch what actually happens:

* We connected to each VPN “location” and captured the exit IP addresses.
* For each exit IP address, we used IPinfo + ProbeNet’s active measurements to determine a measured country, plus:The nearest ProbeNet vantage point (e.g., US, Brazil, France)The round-trip time (RTT) from that probe (often under 1 ms), which is a strong hint about physical proximity
* The nearest ProbeNet vantage point (e.g., US, Brazil, France)
* The round-trip time (RTT) from that probe (often under 1 ms), which is a strong hint about physical proximity

Now we had two views for each location:

* Expected/Claimed country: What the VPN claims in its UI/configs/website
* Measured country: Where IPinfo + ProbeNet actually see the exit IP

### Step 3: Comparing Claims vs Reality

For each location where a country was clearly specified, we asked a very simple question: Does the expected country match the measured country?

If yes, we counted it as a match. If not, it became a mismatch: a location where the app says one country, but the traffic exits somewhere else.

### Acknowledgements, Limitations, and Constrains

We deliberately used a very narrow definition of “mismatch.” For a location to be counted, two things had to be true: the provider had to clearly claim a specific country (on their website, in their app, or in configs), and we had direct active measurements from ProbeNet for the exit IPs behind that location.

We ignored any locations where the marketing was ambiguous, where we hadn’t measured the exit directly, or where we only had weaker hints like hostname strings, registry data, or third-party IP databases. Those signals can be useful and true, but we wanted our numbers to be as hard-to-argue-with as possible.

The result is that the mismatch rates we show here are conservative. With a looser methodology that also leaned on those additional hints, the numbers would almost certainly be higher, not lower.

#### Share this article

#### About the author

Ben Dowling

Ben founded IPinfo in 2013 with the goal of providing reliable, easily accessible IP address data. As IPinfo co-CEO, he is committed to constantly improving that data and how customers can use it.

### Get Unlimited Access to IPinfo Lite

Start using accurate IP data for cybersecurity, compliance, and personalization—no limits, no cost.

Sign up for free

#### Recent articles

* Why VPN Infrastructure Location Impacts Risk Scoring
* Should You Trust Your VPN Location?
* Exploring LLM-Based Approaches for Improving IP Geolocation Accuracy
* See You at Black Hat Europe: We’re Bringing New VPN Insights
* Fraud-as-a-Service in the AI Age: Why Defenses Depend on Data Accuracy

#### Share this article
