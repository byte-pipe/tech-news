---
title: Surveillance vendors caught abusing access to telcos to track people's phone locations, researchers say | TechCrunch
url: https://techcrunch.com/2026/04/23/surveillance-vendors-caught-abusing-access-to-telcos-to-track-peoples-phone-locations-researchers-say/
site_name: hackernews_api
content_file: hackernews_api-surveillance-vendors-caught-abusing-access-to-telc
fetched_at: '2026-04-23T20:05:54.548274'
original_url: https://techcrunch.com/2026/04/23/surveillance-vendors-caught-abusing-access-to-telcos-to-track-peoples-phone-locations-researchers-say/
author: Lorenzo Franceschi-Bicchierai
date: '2026-04-23'
published_date: '2026-04-23T12:01:00+00:00'
description: The Citizen Lab found two separate surveillance vendors abusing the backbone of cellular networks to spy on several victims across the world.
tags:
- hackernews
- trending
---

Security researchers have uncovered two separate spying campaigns that are abusing well-known weaknesses in the global telecoms infrastructure to track people’s locations. The researchers say these two campaigns are likely a small snapshot of what they believe to be widespread exploitation of surveillance vendors seeking access to global phone networks.

On Thursday, the Citizen Lab, a digital rights organization with more than a decade of experience exposing surveillance abuses,published a new reportdetailing the two newly identified campaigns. The surveillance vendors behind them, which Citizen Lab did not name, operated as “ghost” companies that pretended to be legitimate cellular providers and would piggyback their access to those networks to look up the location data of their targets.

The new findings reveal continued exploitation of known flaws in the technologies that underpin the global phone networks.

One of them is the insecurity of Signaling System 7, or SS7, a set of protocols for 2G and 3G networks that for years has been the backbone of how cellular networks connect to each other and route subscribers’ calls and text messages around the world. Researchers and expertshave long warnedthat governments and surveillance tech makers can exploit vulnerabilities in SS7 to geolocate individuals’ cell phones, as SS7 does not require authentication nor encryption, leaving the door open for rogue operators to abuse it.

The newer protocol, Diameter, designed for newer 4G and 5G communications, is supposed to replace SS7 and includes the security features that were lacking in its predecessor. But as the Citizen Lab highlights in this report, there are still ways to exploit Diameter, as cell providers do not always implement the new protections. In some cases, attackers can still fall back to exploiting the older SS7 protocol.

The two spy campaigns have at least one thing in common: Both abused access to three specific telecom providers that repeatedly acted “as the surveillance entry and transit points within the telecommunications ecosystem.” This access gave the surveillance vendors and their government customers behind the campaigns the ability to “hide behind their infrastructure,” as the researchers explained.

According to the report, the first one is Israeli operator 019Mobile, which researchers said was used in several surveillance attempts. British provider Tango Networks U.K. was also used for surveillance activity over several years, the researchers say.

 

Techcrunch event

### Meet your next investor or portfolio startup at Disrupt

#### Your next round. Your next hire. Your next breakout opportunity. Find it at TechCrunch Disrupt 2026, where 10,000+ founders, investors, and tech leaders gather for three days of 250+ tactical sessions, powerful introductions, and market-defining innovation. Register now to save up to $410.

### Meet your next investor or portfolio startup at Disrupt

#### Your next round. Your next hire. Your next breakout opportunity. Find it at TechCrunch Disrupt 2026, where 10,000+ founders, investors, and tech leaders gather for three days of 250+ tactical sessions, powerful introductions, and market-defining innovation. Register now to save up to $410.

San Francisco, CA

|

October 13-15, 2026

REGISTER NOW

The third cell phone provider is Airtel Jersey, an operator on the Channel Island of Jersey now owned by Sure, a company whose networks have beenlinked to prior surveillance campaigns.

Sure CEO Alistair Beak told TechCrunch that the company “does not lease access to signalling directly or knowingly to organisations for the purposes of locating or tracking individuals, or for intercepting communications content.”

“Sure acknowledges that digital services can be misused, which is why we take a number of steps to mitigate this risk. Sure has implemented several protective measures to prevent the misuse of signalling services, including monitoring and blocking inappropriate signalling,” read Beak’s statement. “Any evidence or valid complaint relating to the misuse of Sure’s network results in the service being immediately suspended and, where malicious or inappropriate activity is confirmed following investigation, permanently terminated.”

Tango Networks and 019Mobile did not respond to TechCrunch’s request for comment.

Gil Nagar, the head of IT and security and 019Mobile,sent a letterto Citizen Lab. Nagar said that the company “cannot confirm” that the alleged 019Mobile infrastructure, identified by Citizen Lab as being used by the surveillance vendors, belongs to the company.

## Researchers say ‘high-profile’ people targeted

According to the Citizen Lab, the first surveillance vendor facilitated spying campaigns spanning several years against different targets all over the world, and using the infrastructure of several different cell phone providers. This led researchers to conclude that different government customers of the surveillance vendor were behind the various campaigns.

“The evidence shows a deliberate and well-funded operation with deep integration into the mobile signaling ecosystem,” the researchers wrote.

Gary Miller, one of the researchers who investigated these attacks, told TechCrunch that some clues point to an “Israeli-based commercial geo-intelligence provider with specialized telecom capabilities,” but did not name the surveillance provider. Several Israeli companies are known to offer similar services, such as Circles (later acquired by spyware maker NSO Group), Cognyte, and Rayzone.

#### Contact UsDo you have more information about surveillance vendors that exploit cellphone networks? From a non-work device, you can contact Lorenzo Franceschi-Bicchierai securely on Signal at +1 917 257 1382, or via Telegram and Keybase @lorenzofb, oremail.

According to the Citizen Lab, the first campaign relied on trying to abuse flaws in SS7, and then switching to exploiting Diameter if those attempts failed.

The second spy campaign used different methods. In this case, the other surveillance vendor behind it — which Citizen Lab is not naming either — relied on sending a special type of SMS message to one specific “high-profile” target, as the researchers explained.

These are text-based messages designed to communicate directly with the target’s SIM card, without showing any trace of them to the user. Under normal circumstances, these messages are used by cell phone providers to send innocuous commands to their subscribers’ SIM cards used for keeping a device connected to their network. But the surveillance vendor instead sent commands that essentially turned the target’s phone into a location tracking device, according to the researchers. This type of attack was dubbedSIMjackerby mobile cybersecurity company Enea in 2019.

“I’ve observed thousands of these attacks through the years, so I would say it’s a fairly common exploit that’s difficult to detect,” said Miller. “However, these attacks appear to be geographically targeted, indicating that actors employing SIMjacker-style attacks likely know the countries and networks most vulnerable to them.”

Miller made it clear that these two campaigns are just the tip of the iceberg. “We only focused on two surveillance campaigns in a universe of millions of attacks across the globe,” he said.

Updated to include 019Mobile’s responses sent to Citizen Lab.

Topics

cybersecurity
, 
Diameter
, 
Israel
, 
location tracking
, 
privacy
, 
Security
, 
SS7
, 
surveillance
 

When you purchase through links in our articles,we may earn a small commission. This doesn’t affect our editorial independence.

			Lorenzo Franceschi-Bicchierai	

Senior Reporter, Cybersecurity

Lorenzo Franceschi-Bicchierai is a Senior Writer at TechCrunch, where he covers hacking, cybersecurity, surveillance, and privacy.

You can contact or verify outreach from Lorenzo by emailinglorenzo@techcrunch.com, via encrypted message at +1 917 257 1382 on Signal, and @lorenzofb on Keybase/Telegram.

 

View Bio