---
title: Apple's A12 and A13 Chips Facing New Unpatchable Exploit - MacRumors
url: https://www.macrumors.com/2026/06/18/a12-and-a13-chips-facing-exploit/
site_name: tldr
content_file: tldr-apples-a12-and-a13-chips-facing-new-unpatchable-ex
fetched_at: '2026-06-27T19:33:22.605984'
original_url: https://www.macrumors.com/2026/06/18/a12-and-a13-chips-facing-exploit/
date: '2026-06-27'
description: Security research firm Paradigm Shift today published details of a new BootROM vulnerability affecting Apple's A12 and A13 chips, along with a working proof-of-concept exploit named "usbliter8". The BootROM, or SecureROM, is the first code an iPhone runs when it powers on. Because it is baked directly into the chip at manufacture, any vulnerability found there cannot be fixed with a software update, meaning affected devices will remain vulnerable for the rest of their lives.
tags:
- tldr
---

# Apple's A12 and A13 Chips Facing New Unpatchable Exploit

Thursday June 18, 2026 9:17 am PDT
 by 
Hartley Charlton

Security research firm Paradigm Shift todaypublisheddetails of a new BootROM vulnerability affecting Apple's A12 and A13 chips, along with a working proof-of-concept exploit named "usbliter8."

The BootROM, or SecureROM, is the first code an iPhone runs when it powers on. Because it is baked directly into the chip at manufacture, any vulnerability found there cannot be fixed with a software update, meaning affected devices will remain vulnerable for the rest of their lives.

The last publicly known BootROM exploit of this kind was"checkm8," released in 2019which affected devices from the iPhone 4S through to the iPhone X. usbliter8 now extends that history to the next generation of chips, covering the iPhone XS through to the iPhone 11 series.

The exploit works by taking advantage of a bug in the USB controller built into Apple's chips. When an iPhone receives USB data during startup, the controller uses a memory buffer to store incoming packets. Paradigm Shift found that by sending a specific sequence of unusually small packets, they could manipulate an internal hardware pointer in a way that causes it to walk backwards through memory, allowing data to be written to locations it should never reach. The researchers say this appears to be a bug in the USB controller hardware itself, not in Apple's software.

The A11 chip, used in the iPhone X, is not affected because its USB driver manually resets the pointer after each packet. A14 and later chips are also safe, as they configure a memory protection feature correctly at the BootROM level. The A12 and A13 sit in a vulnerable middle ground between the two.

On A12 devices, gaining code execution is relatively straightforward. On A13 devices, things are considerably harder because Apple introduced a security feature called Pointer Authentication Codes (PAC), which detects and blocks certain types of memory tampering. Paradigm Shift says working around PAC on the A13 required a lengthy multi-step process before the researchers could finally take control of the processor.

Once in control, the exploit installs a custom handler that survives a device restart and adds two capabilities: temporarily lowering the device's security settings, and booting unsigned software without any verification checks. It also injects the traditional "PWND" string into the iPhone's USB serial number as a signal that the device has been compromised, a convention that carries over fromcheckm8 and earlier exploits.

Paradigm Shift notes that while usbliter8 does not affect the Secure Enclave directly, a BootROM compromise of this kind opens up wider avenues for attacking it. The firm says it reported its findings to Apple Product Security before publication and worked with Apple on coordinated disclosure. The full proof-of-concept code has been published alongside the write-up atps.tc.

Tag: 
Apple Security
Related Forum: 
iPhone
[ 
82 comments
 ]

Get weekly top MacRumors stories in your inbox.

Leave this field empty

## Popular Stories

### Apple Just Increased Prices on MacBooks, iPads, and More

Thursday June 25, 2026 5:44 am PDT by 
Hartley Charlton
Apple today dramatically increased device prices across multiple product lines.Subscribe to the MacRumors YouTube channel for more videos. After temporarily taking it down earlier today, Apple's online store is back up with a series of product price increases. The changes are as follows:HomePod mini: $129, up from $99 (+$30)HomePod: $349, up from $299 (+$50)Apple TV: $199, up from...

### Apple Explains Why It Raised Prices on 14 Products Today

Thursday June 25, 2026 10:42 am PDT by 
Joe Rossignol
Apple today raised prices on many of its products, including all Macs and iPads, as well as the Apple TV, HomePod, HomePod mini, and Vision Pro. We shared a list of the price increases, which range from $30 for the HomePod mini to up to $1,300 for the Mac Studio. iPhone, Apple Watch, and AirPods prices have not changed, at least for now.In a statement shared with MacRumors, Apple said it...

### M5 Ultra Mac Studio Could Launch in 2026 With Up to 768GB of RAM

Thursday June 25, 2026 2:30 pm PDT by 
Juli Clover
Despite price increases across the Mac line, Apple is still planning to release a new Mac Studio as soon as this year, reports Bloomberg.Apple plans to introduce a new M5 Ultra chip as the final option in the M5 family before it transitions to the M6, M7, M7 Pro, and M7 Max. The M5 Ultra will come in a new version of the Mac Studio, which hasn't been updated since March 2025.The Mac...

## Top Rated Comments

Shin-Ra
1 week ago
Here is the complete list of Apple devices powered by the A12, A12X, A12Z, and A13 chips, ordered chronologically by their release date:
A12 Bionic Devices
 [wiki ('https://en.wikipedia.org/wiki/Apple_A12')]
* 
iPhone XS
: September 21, 2018
* 
iPhone XS Max
: September 21, 2018
* 
iPhone XR
: October 26, 2018
* 
iPad Air (3rd generation)
: March 18, 2019
* 
iPad mini (5th generation)
: March 18, 2019
* 
iPad (8th generation)
: September 18, 2020
* 
Apple TV 4K (2nd generation) 
(no external USB/Lightning access): May 21, 2021
A12X Bionic Devices
 [wiki ('https://en.wikipedia.org/wiki/Apple_A12X')]
* 
iPad Pro 11-inch (1st generation)
: November 7, 2018
* 
iPad Pro 12.9-inch (3rd generation)
: November 7, 2018
A12Z Bionic Devices
 [wiki ('https://en.wikipedia.org/wiki/Apple_A12X')]
* 
iPad Pro 11-inch (2nd generation)
: March 25, 2020
* 
iPad Pro 12.9-inch (4th generation)
: March 25, 2020
* 
Developer Transition Kit (Mac mini prototype)
: June 22, 2020
A13 Bionic Devices
 [wiki ('https://en.wikipedia.org/wiki/Apple_A13')]
* 
iPhone 11
: September 20, 2019
* 
iPhone 11 Pro
: September 20, 2019
* 
iPhone 11 Pro Max
: September 20, 2019
* 
iPhone SE (2nd generation)
: April 24, 2020
* 
iPad (9th generation)
: September 24, 2021
* 
Apple Studio Display
: March 18, 2022
Score:
 50 Votes (
Like
 | 
Disagree
)
J
JoForumBlueGold
1 week ago
Me with a 14 pro and M2 iPad Pro thinking I'm just fine...then realizing "Oh no, my 2022 Studio Display!"
Score:
 34 Votes (
Like
 | 
Disagree
)
vegetassj4
1 week ago
Whew, lucky I'm still rocking this bad boy
Score:
 29 Votes (
Like
 | 
Disagree
)
Jseeker
1 week ago
it would be helpful if the article listed effected devices.
Score:
 28 Votes (
Like
 | 
Disagree
)
Westside guy
1 week ago
If the jailbreaking community was still active, this could've ended up being very useful. I miss those days...
Score:
 26 Votes (
Like
 | 
Disagree
)
L
Loi84
1 week ago
Are the current Neo...
Did you read the post?
...and future generations of Mac run by phone chip be affected?
Ask AI - maybe it's going to hallucinate a response for you.
Score:
 17 Votes (
Like
 | 
Disagree
)
Read All Comments