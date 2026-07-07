---
title: A Hacker's Arrest Reveals Microsoft Can Track Users Via a Windows Device ID | PCMag
url: https://www.pcmag.com/news/a-hackers-arrest-reveals-microsoft-can-track-users-via-a-windows-device
site_name: hackernews_api
content_file: hackernews_api-a-hackers-arrest-reveals-microsoft-can-track-users
fetched_at: '2026-07-08T01:53:47.334269'
original_url: https://www.pcmag.com/news/a-hackers-arrest-reveals-microsoft-can-track-users-via-a-windows-device
author: ifh-hn
date: '2026-07-07'
published_date: '2026-07-06T16:58:47+00:00'
description: The FBI used a Microsoft device identifier, dubbed GDID, to link a teenager to a hack attributed to Scattered Spider, raising privacy red flags about Windows' surveillance capabilities.
tags:
- hackernews
- trending
---

(Photo by Drew Angerer/Getty Images)
 

The arrest of a teenage hacker has revealed that Microsoft can track a Windows PC and its online activity through a “Global Device ID" that seems to have no easy opt-out, sparking fears about potential surveillance.

Last week, the US announced it hadextradited19-year-old Peter Stokes from Europe for allegedly being a member of the notorious hacking groupScattered Spider.But the case stands out because Microsoft played a key role in linking Stokes to the suspected hacking crimes, according to an unsealed criminal complaint.

(Credit: DOJ)

Stokes allegedly hacked an unnamed luxury jewelry retailer in May 2025 while using aVPN. The39-pagecriminal complaint shows the FBI used Microsoft records to discover that his IP address was associated with a Microsoft device identifier known as Global Device ID (GDID).

You May Also Like

“According to a Microsoft representative, a Global Device Identifier in the Windows ecosystem is a persistent, device-level identifier designed to uniquely identify an installation of a Windows operating system on a device, either a physical device (e.g., a mobile phone or laptop) or virtual machine, across certain Microsoft services and scenarios," the complaint explains.

The global device ID isn’t exactly surprising, given that it's standard practice to assign a unique ID to each account or device so a tech provider can recognize and distinguish between them. But the complaint reveals Microsoft can associate the GDID with third-party services and the timing as well, giving Redmond a way to theoretically track a user’s online activity. In other words, Redmond might be able to track the online activity of your Windows PC without third-party browser cookies.

(Credit: DOJ)

Stokes was discovered exploiting a web development tool called ngrok to bypass the jewelry retailer's network defenses. The complaint says Microsoft had records showing that on May 12, 2025, at 19:21 UTC, the GDID associated with Stokes’ computer “accessed, among other ngrok pages, 'https://dashboard[.]ngrok.com/signup,' the ngrok page to set up an ngrok account.”

The document adds that Microsoft records also showed the GDID accessing “multiple sites” from servers at Tzulo, aweb hosting provider, to help pull off the hack.

The GDID for Stokes' PC was allegedly 6755467234350028. (Credit: DOJ)

Hence, the fact that federal investigators used the Microsoft identifier to nab a suspected hacker is raising concerns that it could be abused for other surveillance purposes. “Microsoft Windows is surveillance software,” cybersecurity expert Matthew Hickey alleged in atweet.

The device ID is mentioned briefly onthis support page, but Microsoft hasn't otherwise commented on it publicly. According to the criminal complaint, a Windows user can reset the GDID on their own, although it's not easy. “A GDID remains consistent across Windows operating system updates on a device, but a reinstall of Windows, either on the same device or on a different device, will be tied to a new unique GDID,” the court document says. In a footnote, it adds, “Thus, one Microsoft user could have multiple GDIDs.”

### Recommended by Our Editors

Ring Cancels Deal With Flock Safety Amid Surveillance Concerns

X Wants FTC to Get Rid of Privacy Order Imposed on Twitter, and You Can Weigh In

Windows 11's Start Menu Is Getting Better...But These 3 Launchers Still Run Circles Around It

Still, we suspect it wouldn’t be hard for Microsoft to tie a newly set GDID to the old one, since the company could look at other identifiers, such as a Microsoft account login or an IP address, and match them. In response to the surveillance potential, some users have already beenexploringways to contain and scrub the GDID identifier.

Meanwhile, cybersecurity researcher Costin Raiu is questioning whether other tech companies have the same surveillance capabilities, given the use of unique identifiers.

"I would also ask: how much of this is happening on Apple devices? Is it on the same scale? Is it happening at an even higher level — do they tie it to the hardware, so that even if you reinstall, it doesn’t matter, because it’s hardware-based?" he said in the Three Buddy Problempodcast. "Very likely it’s not unique to Microsoft. And probably, if you want to be fully anonymous, you may at some point have to use Linux, FreeBSD, whatever, for your development environments, and tunnel everything throughproxies, Tor, VPNs, and such."

## About Our Expert

Michael Kan

Principal Reporter

 

 

 

Experience

I've been a journalist for over 15 years. I got my start as a schools and cities reporter in Kansas City and joined PCMag in 2017, where I cover satellite internet services, cybersecurity, PC hardware, and more. I'm currently based in San Francisco, but previously spent over five years in China, covering the country's technology sector.

Since 2020, I've covered the launch and explosive growth of SpaceX's Starlink satellite internet service, writing 600+ stories on availability and feature launches, but also the regulatory battles over the expansion of satellite constellations, fights with rival providers like AST SpaceMobile and Amazon, and the effort to expand into satellite-based mobile service. I've combed through FCC filings for the latest news and driven to remote corners of California to test Starlink's cellular service.

I also cover cyber threats, from ransomware gangs to the emergence of AI-based malware. In 2024 and 2025,the FTC forced Avastto pay consumers $16.5 million for secretly harvesting and selling their personal information to third-party clients, as revealed in my jointinvestigationwith Motherboard.

I also cover the PC graphics card market. Pandemic-era shortagesled me to camp outin front of a Best Buy to get an RTX 3000. I'm now following how the AI-driven memory shortage is impacting the entire consumer electronics market. I'm always eager to learn more, so please jump in the comments with feedback and send me tips.

Areas of Expertise

* Networking
* Security
* Graphics Cards
* Processors
* AI
* SpaceX
* Nvidia
* AMD

Latest By Michael Kan

* Starlink 'Gen 3' to Span 100K Satellites, for Gigabit Broadband But Also AI
* Waymo Robotaxis Face Blame for San Francisco's July 4th Traffic Chaos
* Wisconsin Residents Sue Microsoft Over Noisy, 'Nightmare' Data Center
* Microsoft Splits With 4 Xbox Game Studios, Will Lay Off 3,200 Employees
* Google: This Proxy Service Is Using TV Streaming Devices to Host Cybercrime
* More from Michael Kan

 Read Full Bio
 

### Weekend Project

 

 

Never Miss a Beat: This Echo Trick Lets You Play Music Throughout Your Home

 By
 
Lance Whitney

Wait! Instead of Throwing Away That Old PC, Try One of These 20 Fun Projects

 By
 
Eric Griffith

Admit It, Your Screen Time Is Out of Control. My Top 4 Digital Detox Tips Can Help

 By
 
Jill Duffy

7 Fun AI Experiments to Try With Google Labs (And Most Are Free)

 By
 
Lance Whitney

Psst! You Can Remove Your Personal Info From Google Search. Here's How

 By
 
Eric Griffith

Have an Old Smartphone? 10 Clever Ways to Reuse It

 By
 
Jason Cohen

Your Laptop Needs Some TLC. How to Clean Your Computer Without Damaging It

 By
 
Charles Jefferies

Stop Paying for VPNs: I Built My Own in Hours With a Raspberry Pi 5

 By
 
Justyn Newman

All 
Weekend Project
 Stories 

### Further Reading

 

 

Backblaze: Backup May Be a 'Declining' Business, But We're Not Backing Away

 By
 
Rob Pegoraro

This Week in Cybersecurity: Signal Drama, Meta Backlash, and a Million Exposed Passports

 By
 
Alan Henry

Google: This Proxy Service Is Using TV Streaming Devices to Host Cybercrime

 By
 
Michael Kan

Apple's Hide My Email Feature Reportedly Leaks Your Actual Email IDs

 By
 
Jibin Joseph

Congressman Admits He Got Hacked, Warns That Signal 'Is Not Secure'

 By
 
Michael Kan

Supreme Court: Fourth Amendment Protects Your Phone's Location History

 By
 
Rob Pegoraro

Meta to Scrap 'Off-Facebook Activity' Feature That Curbed Web Tracking

 By
 
Rob Pegoraro

Polymarket to Refund Users After Hackers Drained Their Crypto Wallets

 By
 
Jibin Joseph