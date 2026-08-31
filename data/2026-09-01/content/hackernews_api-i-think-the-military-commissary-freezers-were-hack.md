---
title: I Think the Military Commissary Freezers Were Hacked
url: https://signalandsilence.substack.com/p/i-think-someone-hacked-the-commissary
site_name: hackernews_api
content_file: hackernews_api-i-think-the-military-commissary-freezers-were-hack
fetched_at: '2026-09-01T09:50:27.504140'
original_url: https://signalandsilence.substack.com/p/i-think-someone-hacked-the-commissary
author: M. Elizabeth
date: '2026-08-31'
description: The frozen pizza aisle has become the national security risk du jour
tags:
- hackernews
- trending
---

# I Think The Military Commissary’s Freezers Were Hacked

### The frozen pizza aisle has become the national security risk du jour

M. Elizabeth
Aug 28, 2026
22
5
5
Share

Originally published: Aug. 28, 2026 at 1:18 p.m. PT.

Last Updated: Aug. 29, 7:27 PT

Since publication, Stars and Stripes, Military Times/Navy Times, and multiple others have independently reported on the multi-base refrigeration failures, with the Pentagon now acknowledging a “possible refrigeration disruption” at numerous DeCA commissaries.

Near-simultaneous refrigeration failures or significant issues impacting at least six military installations have now been confirmed through official sources during the last few days, with additional independent confirmation of multiple other incidents.

Self-aware enough to know this sounds insane, but I need you to stick with me.

#### I think there is a nonzero chance someone has hacked the commissary freezers.

Not one freezer, not one grocery store, not just ANY grocery store, either.

The refrigeration systems at military commissaries (tax-free grocery stores for military personnel and their families located on bases across the country) appear to be under some type of siege; either their own aging fleet of equipment is deciding to seppuku in perfect harmony, or by something (or someone) more nefarious.

Where to even begin?

# It started with doomscrolling, obviously.

Flipping through my normal rotation of social media, I started seeing scattered posts lamenting the commissary suddenly losing their entire refrigerated & frozen sections.

All cold food spoiled, or removed from shelves.

Unfortunate and wasteful,I thought, but inconsequential to me personally. I don’t shop there, I have no stake in the availability of my frozen favs, plus the commissary is not exactly known for smoothly functioning operations, thus, moving on.

But then I saw another post, and another… with a chorus of comments

huh, how odd, the same thing is happening here.

What are the chances!

The pattern caught my attention, and what followed was a deep dive into military social-media chatter, commercial refrigeration, defense procurement contracts, and network security refreshers in an attempt to resurrect the rudimentary cybersecurity knowledge my degrees required.

‘Twas never my strongest subject.When would Ieverneed to use this, I distinctly remember thinking. (Freezers didn’t have networks, in the olden days)

# Introducing our starting lineup.

At the time of initial publication, I identified 14 commissary refrigeration/freezer outage reports attributed to the following military installations across 11 states on August 26–27. Subsequent additions denoted by asterisk, Reports later determined to be unsupported/unrelated remain struck through for transparency.

* Fort Huachuca (Confirmed)
* F.E. Warren AFB (Confirmed)
* Fort Irwin (Confirmed)
* Columbus AFB (Confirmed)
* Naval Station Newport (ConfirmedAug. 26;RestoredAug. 29)
* *Travis AFB (Confirmed)
* NAS Lemoore (Independently Confirmed; Restored Aug. 28 per Commissary employee)
* *Port Hueneme (Independently Confirmed)
* Little Rock AFB
* Dyess AFB (Independently Confirmed; Restored Aug. 29 per Commissary employee)
* Holloman AFB
* Robins AFB
* McConnell AFB
* Cannon AFB
* Fort Meade(Removed; operating normally per local as of Aug. 28)
* Camp Lejeune(Removed: official outage notice initially identified as current was actually from 2025)

To be very clear:I do not have evidence that the Defense Commissary Agency was hacked.

Whatdoesexist is evidence that something odd is happening, plus a whole lotta explanations for how a cyber incident of this magnitude is technologically possible, and that there may bemuchlarger implications than a dearth of cold veggies.

## First Up: Fort Huachuca

Unfamiliar to me prior, and I say that intending no offense to you (lovely, I'm sure) Fort Huachucans; the Cochise County, Arizona base has captured my attention today.

On August 27th, the official U.S. Army Fort Huachuca Facebook accountannouncedthat an overnight equipment failure causedALL of the commissary’s freezers to enter defrost mode, spoiling everything inside.

This wasn’t a case of simply a power flickering and ice cream melting, because someone commentedjustthat. Fort Huachuca responded from its verified account:

“the power didn’t go out”

Another questioned whether all of the food was really “spoiled” if the freezers had simply stopped working.

The installation clarified that, no, the freezers hadn’t just shut off. They had entereddefrost mode, which heated the food.

That is a very different problem and I’m fully invested at this point. Buried in the largely useless comments, I unearthed what felt like a gem:

“I was told that it was a network issue.”

Unverified Facebook comment; included because it prompted the RMCS question, not as evidence of a cause

This commenter claimed thatHuachuca’s cold-storage equipment had been replaced relatively recently, and that refrigeration and HVAC were remotely controlled through DeCA.

That is a random Facebook comment, from an unverified individual. It is not evidence that this was a network problem. But naturally, I absolutely had to know whether the second part was evenpossible.

Unfortunately for my productivity, it is.

# Meet DeCA

I learned that commissaries (of which there are ~235 worldwide) aren’t actually independently operated by whatever military installation or base they happen to sit on.

They’re run by the Defense Commissary Agency (DeCA), an agency seated within the Department of Defense.

DeCA, as expected, has a whole refrigeration-control infrastructure.

In March 2026, DeCA issued procurement documents seeking support for“Facilities Maintenance, Call Center Support, and Remote Monitoring Control System (RMCS) Management.”

It covers approximately182 DeCA locations, encompassing all 14 on my original list.

That alone doesn’t mean anything, however. They’re DeCA stores… of course they’re in a DeCA facilities document.

What matters is what the systemactuallydoes.

### Guess what controls the defrost?

With some cursory control+F digging through DeCA’s titillatingrefrigeration engineering specifications, bingo.

“Defrost shall be controlled through the RMCS”

Which brings us back to Fort Huachuca.

Every freezer entered defrost mode.

The installation itself says the power didn’t fail, and that defrost actually heated the food.

DeCA’s own engineering documentation saysdefrost is controlled through its refrigeration monitoring/control system.

## And these systems aren’t necessarily isolated inside the stores.

AnotherDeCA refrigeration contractdescribesRefrigeration Monitoring and Control Systems (RMCS)located at individual commissaries whose refrigeration and HVAC alarms aremonitored remotely24/7.

Per the contract, the contractor was required to maintain a“master control system for all of the RMCS”somewhere in the continental United States.

Important caveat, because this is where it’s really easy to jump ahead (spoken by a professional jump-aheader): this doesnotmean someone at DeCA headquarters can remotely hit a proverbial DEFROST EVERY COMMISSARY button. It establishes centralized monitoring infrastructure.

Exactly how much remote control exists, where current master systems are hosted, and whether affected stores share equipment remains unclear.Publicly available information is limited here, and it’s not exactly a hotly discussed topic, as you can reasonably imagine.

But we can establish networked control at individual commissaries independently.

The contractor that allegedly built the newer commissary atRobins AFB, one of the installations with reported problems, describes the building as havingRSMS controls managing all of the store’s refrigeration and HVAC systems.

Again: centralized refrigeration control is not suspicious. It’s (apparently) how modern supermarkets work.

What it does is change the options for what a “freezer failure” can mean.

## Then, theotherreports started getting weird

AtHolloman AFB, someone posted the printed notice hastily taped to the blocked off, empty refrigerated section of their commissary:

Source: 
@AFamnncosnco
 on Facebook

A printed note by Holloman AFB Commissary Management reads:

“Due to an unexpected refrigeration system failure, all chilled and frozen merchandise is temporarily unavailable for purchase until further notice.”

The person submitting the photographs said they’d experienced power outages there before, but this event took outall of the refrigeration systems.

The sign and empty cases are considerably harder to argue with.

Fort Irwinpublicly acknowledged its refrigeration problem as well, with similar DIY signage and bare shelving visible.

Naval Station Newportalso officially announced restricted commissary sales due to refrigeration-system issues, however they opted to go with a (dated?) picture of fully stocked shelves. I appreciate the variety.

Then there’sDyess AFB, where another poster supplied a photograph taken that morning showing an entire commissary meat case emptied and closed off after someone reported that the Dyess commissary refrigeration was down.

Robins customers reported produce and meat being covered and unavailable.

Little Rockgets stranger.

A local community page reported that the commissary’s refrigerated systems went down at approximately 2 a.m., affecting chilled, refrigerated and frozen merchandise.

Then an anonymous submission to a large Air Force community page claimed:

“I overheard employees discussing that the system was hacked last night”

Do I know that those employees actually said that?

Nope.

Do I know whether the employees would know the cause even if they did?

Also no.

Columbus AFBissued an official notice acknowledging freezer and chillers experienced an outage.

The official DeCA page forTravis AFBposted an August 26noticestating that “refrigeration issues” had made some frozen and chilled items unavailable and temporarily affected Click2Go operations.

Moving south,F.E. Warren AFBacknowledged a malfunction as well.

In addition to the official statement, I found an anonymous submission to a popular military social media page from someone claiming to work at the F.E. Warren commissary. They wrote that its freezers, and apparently those at 14 other bases, “quit working or reversed to heating.”

Source: 
@AFamnncosnco 
on Facebook

The commenter claimed one deli freezer registered 180 degrees and another 160.

I have no idea what those numbers mean. Case temperature? Defrost heater? I am emphaticallynotreporting that food reached 180°F, but the “14 other bases” part stuck out.

Because once I started counting, I got the same number.

## Here’s where the timing becomes important:

OnAugust 9, 2026, industrial cybersecurity researchers at Claroty’s Team82 published anarticletitled“Freeze the Controller, Defrost the Food: Uncovering Vulnerabilities in Danfoss Refrigeration Controllers.”

Yes, that is the actual title.

The researchers examined theDanfoss AK-SM 800A, a supervisory controller used to centrally manage commercial refrigeration systems. And what did they find?

Vulnerabilities capable of allowingserious unauthorized access.

Before anyone screenshots that paragraph and runs away with it:

I havenotestablished that Fort Huachuca uses a Danfoss AK-SM 800A.

Ihave, however, found a searchable copy of aDeCA equipment inventory listidentifying a Danfoss AK-SM880 refrigeration monitoring/control system at NAF El Centro - notably, not one of the commissaries on my affected list.

So, Danfoss AK-SM technology exists within the DeCA environment.

Interesting, but not attribution.

## It gets better. Or worse?

Claroty published a second refrigerationinvestigationon thesameday, this time, about something called theCopeland XWEB Prosupervisory controller ($5,509+ shipping, in case you’re in the market; fair warning, this isn’t exactly a glowing sales pitch).

They found23 vulnerabilities, 21 rated ‘high severity’, and ultimately demonstrated the part I actually care about: After compromising the supervisory controller, they could physically manipulate the refrigeration equipment.

Copeland itself already issued asecurity bulletinacknowledging vulnerabilities and explicitly advising customersnever to expose the control system or its web interface to the broader internet.

So:Can someone actually hack a commercial refrigeration controller and make it do things?

Yes.

## Does that meanthiswas a cyberattack?

No. Too early to call it that.

And this is where I am currently stuck.

A common software or configuration problem, update-gone-wrong, a communications failure, or some boring DeCA-wide maintenance issue could explain it too.

A bunch of unrelated aging refrigeration systems deciding to off themselves during August is also not exactly unimaginable. DeCA’s own March procurement specifically identifiedaging infrastructureas something it is trying to manage. If you’ve ever shopped at a commissary, you can attest to the fact that the facilities are not what I would calltop of the lineboutique shopping experiences.

There are also historical examples of commissary refrigeration outages. Refrigeration equipment does, in fact, break.

But the thing I can’t get past isFort Huachuca’s failure mode.

Not:the freezer compressor died.

Not:the power went out.

Not even:the refrigeration system stopped cooling.

Every freezer went into active defrost.

The function that did it, per DeCA’s own engineering documents, is controlled through the RMCS.

This is not proof of a cyberattack, but it is quite a series of coincidences.

There is still no public evidence that the affected stores share the same RMCS vendor, controller, firmware, contractor, or network.

# The IoT of it all

This is where we have to talk about the Internet of Things (IoT), because if I had to think about how the internet works inside a grocery-store freezer today, you do too.

We’ve spent years connectingeverythingto networks because, obviously, being able to monitor and control stuff remotely is convenient. We’ve seen Wall-E.

Your printer, camera, washing machine, smart ring, toothbrush, car, andsomany more create the IoT. In-store refrigeration systems are, apparently, also things that we have connected to computers. How progressive.

The con? Every time we make an object network accessible, we create a potential way to exploit it.

Remember thatCopeland experimentfrom back yonder? Once Claroty compromised the supervisory controller, they could remotely set the compressors, cooling fans, or defrost cycle, heating or cooling what’s inside.

That is the important part.

The computer doesn’t have to “hack” the freezer in some sci-fi sense. The computer issupposedto tell the freezer what to do.

Claroty’s separateDanfoss investigationfound security bypass and remote vulnerabilities in another commercial refrigeration controller, plusthousands of its management interfaces exposed to the public internet.

Again,none of this is proven to be connected to DeCA.

### It does, however, explain whysomeone hacked the military’s freezersis an objectively less stupid sentence than I initially thought.

I seem to have picked anexceptionallytimely week to become concerned about industrial controllers.

On August 19, only eight days before Ft. Huachuca announced its freezer failure, the NSA and its partnerswarnedthat cyber actors are currently conducting“targeted reconnaissance and capability development” against U.S.-based industrial controllers. Targets include energy, water, manufacturing, food production and commercial facilities.

Their concern is also physical: successful exploitation could causeequipment damage, downtime, potential harm to health and life, as well as disruption of industrial processes.

Different equipment. No demonstrated connection to DeCA.

But suddenly, my concern about computers making physical equipment, ya know,dothings feels exceptionally timely.

# Why does this matter beyond spoiled groceries?

This is where my silly little freezer saga collides withactualnational security.

The2026 National Defense Strategyidentifies cyber capabilities among the growing direct threats to the American homeland.

In June, the Department of Energywarnedthat nation-state adversaries are activelypre-positioning inside U.S. critical-infrastructure networks, while other actors increasingly target the OT/industrial-control systems that make physical equipmentdo things.

Obviously, losing frozen meals is not the same as losing the power grid.

But network-connected software controlling physical infrastructure?

Same security problem, considerably lower stakes.

# Why yes, the foreign-state actor possibility crossed my mind, now that you ask!

There is a possibility my security-trained brain can’t tune out when thinking about what the purpose of an incident like this could be.

### Ifthis were a cyberattack,why mess with freezers?

Well,we already know one answer is in the playbook:Reconnaissance and pre-positioning.

A2024 Joint Cybersecurity Advisoryfrom CISA, NSA, FBI and international partners concludedwith high confidencethat Chinese-sponsored ‘Volt Typhoon’ hackers were positioning themselves inside U.S. critical infrastructure networks.

Why?

To enable future disruption.

The agencies confirmed compromises across communications, energy, transportation and water systems. The hackers gained access, and then conducted extensive reconnaissance to understand victim networks. In some instances, theymaintained access for at least five years.

That sounds considerably less theoretical.

I am absolutely not sayingChina hacked the commissaries.

But if this ultimately proves to be a cyber incident rather than a mundane hardware failure, the national-security question wouldn’t just bewho wants to ruin frozen pizzas?

It would bewhether the refrigeration failures had anything to do with access to a mundane piece of network-connected infrastructure operated by a DoD agency, and if so, what the purpose of that access was.

A freezer is relatively low-stakes. Access controls, utilities, HVAC, water systems? Not so much. Different systems, obviously, but the same broader security problem: physical infrastructure sitting behind network-connected controls.

Speculative, but not an entirely hypothetical threat.

## And then the FBI seized a Chinese hacking platform

Because the timing of this all wasn’t already odd enough: On August 26, the DOJ and FBIannouncedthe seizure of infrastructure belonging to a PRC state-sponsored hacking group, QTFY.

TheNSA advisoryreleased alongside it is perhaps even more interesting.

QTFY’s QScan wasn’t merely infecting IoT devices. NSA describes it as areconnaissance and exploitation platform used to find vulnerabilities in networks, while QTFY used compromised IoT devices themselves to disguise subsequent hacking activity.

The group has targeted theDefense Industrial Base, and DOJ says targets included NASA, DOE, the Federal Reserve, DOJ and the U.S. Senate, alongside power companies and defense contractors.

Its customers? China’s Ministry of State Security and PLA, among others.

Again:zero evidence connects QTFY to DeCA.

Buttwo days ago, on August 26th, the NSA was quite literally warning about a PRC state-sponsored group using IoT devices and vulnerability-scanning tools to target military-adjacent and critical infrastructure networks.

So, forgive me for continuing to have questions about the freezers.

# Onto the fun part: Action Items

I decided to exercise my God and country-given right and ask for the boring paperwork, which I’m sure will be produced to me in a timely and reasonable fashion.

/s, of course

I’ve put together requests to DeCA for the Fort Huachuca refrigeration work order, RMCS alarm/event records, maintenance findings, and whatever root-cause determination exists.

I’m also requesting records concerning whether DeCA identified a common technical problem affecting multiple commissaries during August - including network, controller, software/configuration, or cybersecurity incidents.

Most importantly, I want the equipment inventory. DeCA maintains remarkably detailed equipment records, and ideally I can get my paws on the RMCS/controller manufacturer and model forevery commissary, not merely those on my list.

Because then, this becomes testable.

If affected commissaries disproportionately share a controller, firmware iteration, contractor, or recent change? That becomes quite interesting.

If 90% of DeCA uses the same controller, finding it at affected stores tells us basically nothing.

And, if the maintenance logs come backrelay failed/compressor died/lost refrigerant/blown fuseacross unrelated stores, my little theory dies an appropriately boring death and I begin my apology tour.

Sorry in advance (just in case).

# Bottom Line

For right now,“DeCA was hacked”is not a substantive enough argument to make, however I'd be lying if I said it wasn’t still my hunch.

Publicly, I'm not one for frivolous claims. So I'll take off my tin hat for you, dear reader, and stick to whatissupported:

At least six military installations across the country have now officially acknowledged refrigeration/freezer failures or significant refrigeration issues during the same general period, with additional incidents reported elsewhere. At least one involvedeveryfreezer entering a defrost state while power remained on; DeCA engineering specifications state that defrost is controlled through the RMCS. A cybersecurity incident remains a plausible hypothesis, but there is not yet enough evidence to support that fact.

So, that was today’s deep dive. This is perhaps the longest my brain has idled on refrigeration-related topics. Unfortunately, I need the government to answer my FOIA request in order to free myself from The Pointed Questions That Persist, as I call them… and we all know how quickly that goes.

As I stood in front of my own freezer while making dinner, I caught myself pondering the network security risks of those ridiculousfridgeswith the integrated wifi-enabled touchscreens.

Every day, I draw closer to becoming a luddite.

Chat soon,

M. Elizabeth

### Material Updates:

##### August 29:

* AFort IrwinFacebookpostsays DeCA and Ft. Irwin techs are still working to repair the commissary’s refrigerators and freezers, describing the issue as part of a “situation that has impacted grocery stores across the country.” It is unclear whether the installation is referring specifically to commissaries, or grocery stores more broadly based on wording.
* APort Huenemeshopper confirmed to mephotosshowing empty cases were taken Aug. 27, while a commissary employee confirmed by phone that the store’s refrigeration remains offline without a known restoration date.
* ADyess AFBcommissary employee confirmed by phone refrigerators were working and stocked, but being monitored closely.

##### Aug. 28, 2026:

* I’ve submitted 3 FOIA requests to DeCA seeking Fort Huachuca’s RMCS event/alarm logs, work orders and root-cause findings; records concerning any common cause among the recent refrigeration failures; and DeCA’s existing inventory of RMCS/refrigeration-controller equipment across commissary locations.
* Updated to include DeCA’s Aug. 26 notice confirming refrigeration issues affecting frozen and chilled inventory at Travis AFB Commissary. The confirmed count is nowsixinstallations.
* Fort Meade remains unverified. A source who visited the commissary Aug. 28 found the commissary operating normally; I have not independently confirmed the earlier reported outage.
* DeCA’s Camp Lejeune page now reports a “service outage of several freezer units” and says the commissary is working with DeCA Headquarters to bring the units back online, however this notice appears to be on a dated, duplicated DeCA site (old,new). Removed from count, confirmed total remains at six.DeCA MCB Camp Lejeune commissarypage, accessed Aug. 28, 2026.
* I received an (unverified) tip that Port Hueneme’s refrigeration is also disrupted. No official confirmation discovered.
* Fort Irwin’s Facebookpoststates “Working diligently to troubleshoot and resolve the refrigeration issues…no estimated time for completion”
* The Pentagon has now acknowledged a broader problem, tellingMilitary Timesthat DoD is aware of a “possible refrigeration disruption at some Defense Commissary Agency commissaries.” Officials have not disclosed the cause or whether the incidents are connected
* Earlier reporting:Stars and Stripes(attributes this investigation)
* Earlier in the year, DeCA signed incumbent maintenance contractors were retained for the majority of Commissary location through 2026 because of their store-specific knowledge of historical maintenance, repairs and replacements…knowledge that may reasonably also reside with sub/local contractors partners working under those prime contractors.
* Stars and Stripesspoke with Aldevra, a DeCA refrigeration vendor, which said it received no service calls related to the outages, and that the refrigerators it supplies to DeCA aren’t network-connected themselves, though separate remote-monitoring systems can be added (as suspected). This reinforces a connectivity theory and reduces likelihood of a large-scale physical hardware malfunction.
* An anonymous inbox sent to @AFamnncosncoalleges a refrigeration incident atVance AFB (Unconfirmed). No public statement by official sources available at this time.
* ANAS Lemoorecommissary employee confirmed by phone that its refrigeration system returned to normal operation today (Aug. 28).

Further Reporting:

* Stars and Stripes
* NavyTimes
22
5
5
Share