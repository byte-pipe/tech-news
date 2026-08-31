---
title: ATM Flaws Reveal Key Weaknesses in the Software Supply Chain | WIRED
url: https://www.wired.com/story/atm-flaws-reveal-key-weaknesses-in-the-software-supply-chain/
site_name: newsfeed
content_file: newsfeed-atm-flaws-reveal-key-weaknesses-in-the-software-su
fetched_at: '2026-08-31T23:09:08.811967'
original_url: https://www.wired.com/story/atm-flaws-reveal-key-weaknesses-in-the-software-supply-chain/
author: Lily Hay Newman
date: '2026-08-31'
published_date: '2026-08-31T10:00:00.000Z'
description: A security researcher discovered nine vulnerabilities impacting ATM encryption and authentication software. But the problems extend far beyond your local cash machine.
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

For the pastfive years, security researcher Matt Burch has immersed himself in the esoteric and high-stakes world of ATM security, in which small software flaws can sometimesexpose cold, hard cash. As Burch has bored deeper into the computers powering these digital lock boxes—and continued to find vulnerabilities in key digital security systems—he has started working to raise the alarm, not just about overlooked ATM flaws, but about how that same software used in other industries can introduce weaknesses in an array of critical systems.

At theBlack HatandDefconsecurity conferences in Las Vegas this month, Burch presented findings about ninevulnerabilitiesthat have been fixed in disk encryption and pre-boot authentication software called CryptoPro Secure Disk. The flaws could have been exploited to bypass CryptoPro's integrity checks and gain full access to encrypted devices.

Made by the German software firm CryptWare, CryptoPro is marketed to ATM makers and is used in some ATMs, including as part of Diebold Nixdorf's Vynamic Security Suite. But CryptoPro is also sold as a security solution for other embedded-device makers, as well as big organizations using Microsoft Windows, underscoring the supply chain challenge of addressing bugs when software is widely implemented in numerous industries.

“ATMs are what brought me down this path, but I think there may be an even higher impact of these findings beyond that,” Burch says. “From the perspective of ATMs and the financial network, there are a lot of layers, and I think as a result of that, things just get implemented a certain way and then there’s limited technical insight—bugs can get overlooked or they don’t get addressed.”

CryptWare managing director Uwe Saame tells WIRED that the company patched the nine bugs in two phases with CryptoPro version 7.7.2 in early November and 7.7.3 in early December. He adds that there are hundreds of CryptoPro customers across critical industries including “automotive, banking, government agencies, manufacturing, research, finance, and healthcare. There are also extensive installations in the ATM sector.”

Burch says the company was prompt and collaborative throughout his disclosure process and he validated that the patches actually fix the vulnerabilities he found.

While CryptoPro does not publicly release update notes, Saame says that the company has maintenance agreements with all customers and notifies them in advance about any security findings as well as the company's timeline for resolving them. “As a rule, the new version is already available to our customers before its official publication,” he says.

Diebold Nixdorf spokesperson Michael Jacobsen tells WIRED in a statement that only two of the nine vulnerabilities are relevant to Diebold Nixdorf's Vynamic Security Hard Disk Encryption, the system where the ATM maker uses CryptoPro software. Jacobsen says that Diebold Nixdorf issued fixes related to those two bugs in December, but that they could not have been exploited on their own to compromise a Diebold Nixdorf ATM.

In ATMs, embedded devices, and enterprise security more broadly, the challenge of the software supply chain comes from all of the steps to actually apply fixes in the world. As in this case, a developer has to release a patch, then companies that implement the product in their own software need to develop a tailored fix, and then customers need to actually hear about and install that patch—which can be difficult for systems that are running in the field or can't easily be paused and updated.

Speaking generally about this challenge, Jacobsen, the Diebold Nixdorf spokesperson, says that “when a security issue is identified, Diebold Nixdorf assesses the impact, identifies affected products and configurations, and develops any needed updates through our product security and engineering processes. We then notify impacted customers and provide updates through standard software distribution channels, including the Global Security Portal where applicable. For deployed ATMs, updates are coordinated with each customer based on their operating model, service agreements, and change-management processes.”

Security researchers have warned for decades about the danger of relying on “security through obscurity” by trying to hide software from view or keep it locked away. And, as a result of this work, internet-of-things manufacturers and those in critical industries like the financial sector and medical device manufacturing have made some progress on transparency and promoting patch adoption. But Burch points out that as AI systemsmake it easier to evaluate software and find vulnerabilities—even for researchers or attackers who don't have granular expertise in a given area—it is more pressing than ever to shed light on niche security products.

“AI really blows away the obscurity model,” Burch says. “You don’t need to fully understand how something works anymore to move forward and potentially have a big impact.”

Updated 8/31/2026 at 8 am EDT: Added additional details from CryptoWorks.

## Comments

Back to top
Join the discussion

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:Maxwell Zeff's dispatchon the business of AI
* Whynormal peoplearen’t using AI agents
* Big Story:How data centersbroke American politics
* Hackers stalked me byhijacking a cheap pink plastic watch
* Special edition:The WIRED guide to expanding your mind
Lily Hay Newman
 is a senior writer at WIRED focused on information security, digital privacy, and hacking. She previously worked as a technology reporter at Slate, and was the staff writer for Future Tense, a publication and partnership between Slate, the New America Foundation, and Arizona State University. Her work ... 
Read More
Senior Writer
* X
Topics
security
cybersecurity
vulnerabilities
hacking
software
black hat
DefCon
Top Tempo Promo Codes: Get up to 60% Off Healthy Meals in September 2026
Upgrade your meal prep with these Tempo discount codes and offers. Save on high-protein, ready-to-heat meals delivered to your door.
Matthew Korfhage
George Santos Just Got Hit With Kalshi’s First-Ever Lifetime Ban
The former US representative was also fined more than $71,000 for allegedly attempting to manipulate the prediction market.
Kate Knibbs
From Salmonella Eggs to Diarrhea Lettuce, Why This Has Been a Sick Hot American Summer
While Trump administration cuts have contributed to the epidemic of foodborne illnesses this summer, there are also deeper issues that make the American food supply chain susceptible to parasites and bacteria outbreaks.
Kate Taylor
You Know Who Really Hates AI? Insurance Claims Adjusters
Of the Glassdoor reviews from claims adjusters that mentioned AI, a staggering 98 percent were negative. “AI is just a tool,” one person tells WIRED. “It should never be given the keys.”
Kate Taylor
ATM Flaws Reveal Key Weaknesses in the Software Supply Chain
A security researcher discovered nine vulnerabilities impacting ATM encryption and authentication software. But the problems extend far beyond your local cash machine.
Lily Hay Newman
Google Maps Now Shows ‘Lake America’ Instead of Lake Ontario
After Donald Trump’s executive order demanding the name change, Google is the first major online map provider to flip the switch.
Paresh Dave
The Best Mesh Wi-Fi Systems for Networking Nirvana
Forget about patchy internet connections and dead spots in the house. These WIRED-tested, multi-room mesh Wi-Fi systems will keep your whole house online.
Simon Hill
Why the Hottest New Wearables Want to Be Ignored
Burnt out on wrist buzzes and notification overload? A new crop of minimalist wearables promises to collect your health data without demanding your attention.
Andrew Williams
How to Escape Group Chat Hell
Young adults are in more group chats than ever—sometimes more than 20 at a time. Here’s how to tame the chat madness.
Reece Rogers
Scientists Create the Littlest Big Bang to Study the Universe's Origins
The discovery redefines how large atoms need to be to produce the extreme state of matter found in the early universe.
Jorge Garay
NASA’s Nancy Grace Roman Space Telescope Has a Hidden Technological Leap
Astronomers will test equipment that, if it’s successful, will one day be crucial for discovering Earthlike planets.
Meghan Bartels
The Cybersecurity Apocalypse Is Coming in ‘Months,’ AI Giants Warn
Plus: Hackers target over 100 US water systems, ICE puts in an order for robot dogs, and you’ll never guess what “MrChildPorn” was arrested for.
Maddy Varner