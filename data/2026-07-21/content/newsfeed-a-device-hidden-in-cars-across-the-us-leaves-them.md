---
title: A Device Hidden in Cars Across the US Leaves Them Vulnerable to Hacking and Paralysis. Patch It Now | WIRED
url: https://www.wired.com/story/a-device-hidden-in-cars-across-the-us-leaves-them-vulnerable-to-hacking-and-paralysis-patch-it-now/
site_name: newsfeed
content_file: newsfeed-a-device-hidden-in-cars-across-the-us-leaves-them
fetched_at: '2026-07-21T11:37:33.337357'
original_url: https://www.wired.com/story/a-device-hidden-in-cars-across-the-us-leaves-them-vulnerable-to-hacking-and-paralysis-patch-it-now/
author: Andy Greenberg
date: '2026-07-21'
published_date: '2026-07-21T10:00:00.000Z'
description: Dealerships installed alarms in millions of vehicles—and left them in even if the buyer didn’t want them. Now researchers warn they can be hacked to unlock, track, and disable cars.
tags:
- wired
- security
- security / cyberattacks and hacks
- security
---

Save Story
Save this story
Save Story
Save this story

As modern carshave evolved intomulti-ton computers on wheels, drivers are beginning to learn they need to install security updates for their vehicles' code, just as they would for aphoneorlaptop. Yet not even the most tech-savvy car owners would expect they'd need to install a patch for an insecure third-party component they never installed or requested—and likely aren't even aware of—that's been wired into some of the most sensitive systems of their vehicle, leaving it vulnerable to stealthy hacking, tracking, and even roadside paralysis.

That's the disturbing discovery of a team of security researchers at UC San Diego, who found that a model of aftermarket car alarm known as the KARR Security System, installed in more than 2 million vehicles across the US by their estimate, can let any hacker within Bluetooth range send radio commands to silently unlock the car at will, turn off its alarm, honk the car's horn or flash its lights, or even disable its ignition and leave a driver stranded.

The KARR alarm devices are typically installed by car dealers, not manufacturers or owners, and used as a measure to prevent auto theft from dealer lots. Yet when the cars are sold, the alarms typically aren't removed, even if the buyer declines to pay for it as an additional feature. That means car owners across the US have a hackable device under their hood whose code they'll need to update to protect their vehicle—but one that, in many cases, they never purchased and have no idea is there.

The KARR Security System has been wired into the critical systems of more than 2 million vehicles by UCSD's estimate, all of which need the patch to protect them from hacking techniques that can track, unlock, and paralyze cars.

Photograph: Courtesy of David Baillot/University of California San Diego

"This is a system added to cars by dealers, and unfortunately it has a severe vulnerability that allows anyone to gain access to any of these cars," says Aaron Schulman, the UCSD computer science professor who led the research. “It's designed to make cars more secure, but ultimately it's created a vulnerability that needs to be patched immediately across millions vehicles. We're trying to get the word out that you need to check your car for this device and manually patch it now.”

The company that sells the KARR Security System, Acrisure Protection Group, today rolled out a firmware update for the vulnerable Bluetooth model of its aftermarket KARR alarm to fix the security issues UCSD uncovered. Car owners who already have the KARR Security smartphone app installed should receive an alert about the firmware update, the UCSD team says. Those who don’t have it installed will need to download the KARR Security System smartphone app (Android,iOS), connect it to their vehicle's KARR alarm, then tap “customer service” and “firmware update.”

Given that at least half of car owners who have the KARR device installed didn't ask for it to be in their vehicles, according to UCSD's estimate, you can check if your car has the device by looking for a KARR sticker on your car's driver-side window—or in some cases a sticker reading, “SWDS” for SouthWest Dealer Services, a subsidiary of Acrisure Protection Group—as well as a small button with a blinking light attached to the underside of your car's dashboard. Car owners in Southern California are most likely to have the device installed due to its popularity among car dealers in the region, but the UCSD researchers warn that they've found the devices installed in vehicles across the US and even in other countries.

That difficulty of getting word out to affected drivers, combined with the significant risk that the vulnerability could be used for theft, makes the KARR's security flaw “probably the worst” car hacking threat ever discovered, says Stefan Savage, another UCSD computer science professor who didn't work on the KARR alarm findings but did co-lead the first team to hack a car's steering and brakes in 2010 and 2011. “It affects a large number of vehicles, the manufacturer of your car can't fix it, and you don't even know you have the problem,” says Savage. “It provides all the elements a car thief would want, but you have none of the advantages we normally have in terms of defending it, because you're disconnected from the supply chain that put it there.”

## Carjacking, Sabotage, and “Mayhem”

When WIRED reached out to Acrisure Protection Group about the KARR security flaw, a spokesperson responded in a statement: “The vulnerability described in [UCSD's] research is highly complex and presents a low risk to customers under real-world conditions. Nevertheless, we responded promptly and developed a firmware update to address the issue.”

The company added that it will be alerting car owners to its patch via the KARR Security app, the KARR Security website, and via “dealer communications." It didn't share more about how it will reach car owners who aren't aware that they have the device installed, including owners of affected vehicles that may have even been resold to drivers who can't be reached by dealerships.

Despite Acrisure Protection Group's claim to have patched the flaw “promptly," it actually took close to 18 months to push out its patch. The UCSD researchers told the company about the vulnerability in January of last year, but the company didn't offer a fix until just weeks ahead of UCSD's planned presentations about its findings at the Defcon hacker conference and the Usenix security conference next month.

Acrisure's claim that the vulnerability represents a “low risk” under “real-world conditions" also merits some skepticism. In a series of demos for WIRED, all captured in the video above, the researchers showed that they could use their own Android app to send Bluetooth commands to vulnerable vehicles with KARR installed to carry out a wide array of potentially disruptive or dangerous hacking. The demo exploits can, with the tap of a button, unlock a car at a stop light to enable theft or carjacking, instantly paralyze a parked car to prevent it from starting, or even—with a “mayhem” button they built into the app—hack a group of cars to simultaneously and repeatedly trigger their horns and lights, as the researchers demonstrated for WIRED in a UCSD parking lot.

The UCSD team’s proof of concept app offers a menu of hacking options that the KARR vulnerability makes possible …

Screenshot Courtesy of Yibo Wei

… as well as a list of nearby cars whose Bluetooth signals show they have the vulnerable KARR device installed.

Screenshot Courtesy of Yibo Wei

The KARR Security System's vulnerabilities do not, fortunately, allow a hacker to start a car's ignition. But the UCSD researchers showed how a locksmith tool commonly available for resale online can, once a car thief is inside the vehicle, be plugged into a car's dash to create a working key within a few minutes and drive it away. Car thieves using that device would typically have to break a window or use car-door opening tools, potentially setting off a car alarm. But combined with the KARR vulnerability, they can stealthily get into the vehicle to carry out that theft technique.

The security flaw that makes all of those sabotage and intrusion tricks possible, the UCSD team found, is a single authentication key shared across all KARR devices. The UCSD researchers also spotted that key in the code of the KARR smartphone app, which customers who pay for the alarm can use to control it. With that key and a homemade app they created by reverse engineering the KARR app's code, they found they could spoof radio commands that would be accepted by any nearby Bluetooth-enabled KARR device.

The KARR device's insecurity is compounded by the fact that, even when a car buyer declines to pay for it as an add-on, it stays in the vehicle and continues to both beacon out and accept Bluetooth signals whenever the car is on, and also for as long as 10 minutes after the car is turned off. Though the KARR device is in a "deactivated" state for those drivers, the researchers found they could activate it with a radio command and then immediately carry out their menu of hacking techniques.

That activation does trigger a quick beep from the car's horn and a flicker of its lights, the only sign a car owner might have that someone has put their car into a hackable state. For the hundreds of thousands of KARR customers who did pay a dealer to enable the alarm system, they would receive no such warning.

## Highways of Hackable Cars

A UCSD researcher, Nishant Bhaskar, first became aware of the KARR devices in 2018, while doing analysis of radio-enabled “skimmer” devices designed to steal credit card information from gas station point-of-sale terminals. He began to pick up Bluetooth signals from mysterious devices at the gas stations, and then soon realized that he was seeing the same radio signals on the highway from vehicles of all makes and models. That's when he began to search online for the text-based prefixes of those Bluetooth signals and saw in a Federal Communications Commission database that they came from the KARR alarm device.

Only years later, when then graduate researcher Jerry Yu was looking for a summer project in 2024, did Schulman suggest he take a look at the security of the KARR device whose signals Bhaskar had spotted. Yu quickly found the KARR app's universal authentication key, a glaring security flaw. “Once we reverse-engineered their application, we quickly realized after understanding their internal authentication protocol that it was so simple that we could extract it and re-implement it as our own application, which we did," Yu says. That app could, they discovered, unlock “every single car they've ever put this in.”

To get a count of how many vulnerable KARR devices are out there, UCSD researcher Yibo Wei used the open-source radio information database WiGLE, which crowdsources radio signals that contributors pick up with antennas all over the US and the world. He estimated as a result of those scans and extrapolating from the serial numbers of the devices that more than 2 million of the Bluetooth-enabled KARR devices have been deployed.

The UCSD researchers’ estimates of the locations of vulnerable cars across the US, based in part on radio signals collection crowdsourced in the WiGLE database.

Courtesy of UCSD Research Team

Those WiGLE results are, however, more than just a measurement tool. They also potentially allow a hacker to track the historical locations of vulnerable cars based on their KARR device's Bluetooth signature and find places where the vehicle is frequently parked—a disturbingly easy scouting mechanism for finding opportunities to hack them for theft or sabotage.

In the UCSD team’s own scanning, they also found KARR-enabled vehicles virtually everywhere they looked. At one point, the researchers took me for a short drive around the outskirts of the university's campus while using their app on a normal Android phone to scan for cars with beaconing KARR devices. They found 97 vehicles with the alarms in just 20 minutes.

Schulman and his team now feel a responsibility to warn every one of those drivers about the hidden, hackable gadget in the guts of their vehicle. "When you install something by default at a dealer in every car that's sold, the pervasiveness of that vulnerability is going to be unimaginable," he says. “This is why we need to publicize this and get it out there, because the only way this will eventually get solved is if we get everyone on board and to fix it themselves.”

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:Inside WIRED’s newsroom with Katie Drummond
* Trumpmocked Zuckerberg and Bezosby showing off fawning texts
* Big Story:I found Jesusat a drone show
* Apple is making your olderiPhone run faster and stay alive longer
* WIRED event:PepsiCo’s once-in-a-generation transformation
Andy Greenberg
 is a senior writer for WIRED covering hacking, cybersecurity, and surveillance. He’s the author of the books 
Tracers in the Dark: The Global Hunt for the Crime Lords of Cryptocurrency
 and 
Sandworm: A New Era of Cyberwar and the Hunt for the Kremlin's Most Dangerous Hackers
. His books ... 
Read More
Senior Writer
* X
Topics
security
cybersecurity
cars
hacks
Bluetooth
hacking
vulnerabilities
Claude Helped a Hacker Find a Way to Issue Tickets to Almost Every US Music Festival
A researcher found that using Anthropic’s Claude Opus 4.7, he could break into the website of Front Gate—used by every festival from Lollapalooza to Bonnaroo—and freely issue any ticket he chose.
Andy Greenberg
AI Found a Root Bug in Linux That Everyone Missed for 15 Years
Plus: The Pentagon is training amateurs to become part of its hacker army, a Flock license plate reader error led to cops surrounding a car reviewer, and more.
Dell Cameron
Apple’s Hide My Email Service Fails to Hide Your Email
Plus: Alleged Scattered Spider hacking member extradited, dozens of license plate reader errors, and Indian officials are concerned about WhatsApp’s username rollout.
Matt Burgess
A Fatal Tesla Crash in Texas Sets Up a Legal Showdown
Did Full Self-Driving (Supervised), Tesla’s driver assistance feature, play a role in a woman’s death?
Aarian Marshall
Truckloads of Tesla Batteries Keep Getting Stolen Before They Even Leave the Factory
Nine major suspected cargo thefts happened at Tesla’s Nevada battery factory in January alone, according to sheriff’s records obtained by WIRED.
Paresh Dave
Top Surfshark Promo Codes for July 2026
Save up to 87% with a Surfshark coupon code, 3 months of VPN free today, and more from WIRED.
Scott Gilbertson
When the Law Kills Your Electric Car Dealership
Dealers who invested in Polestar won’t be able to sell in the US next year after the federal government denied an authorization that would have allowed the company to avoid a Chinese tech ban.
Aarian Marshall
The ACLU Is Arming Lawyers to Expose State Surveillance Secrets
A new toolkit for attorneys in Massachusetts targets the technologies police use—and conceal—to build criminal cases, from facial recognition to AI-written police reports.
Dell Cameron
Usernames Are Coming to WhatsApp Soon. Here's How to Reserve Yours
Even if you only use WhatsApp sometimes, you might want to snag your username now to stop giving out your phone number.
Reece Rogers
You Can Now Sound the Alarm on AI Behaving Badly
Are you worried your AI chatbot is trying to build a bomb or leak personal information about you? There’s a website for that.
Will Knight
World Cup Scams Are Getting Harder to Spot
From fake tickets to cloned websites, AI is magnifying World Cup scams. Can fans distinguish between what’s real and what’s not?
Jumana Naim
The Army Is Burning Through Its AI Tokens
Members of the Army received an email informing them that they were rapidly depleting their AI tokens, and needed to limit use.
Vittoria Elliott