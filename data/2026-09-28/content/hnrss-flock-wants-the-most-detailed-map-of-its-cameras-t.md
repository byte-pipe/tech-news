---
title: Flock Wants the Most Detailed Map of Its Cameras Taken Down
url: https://theintercept.com/2026/09/24/how-many-flock-devices-in-united-states-300000/
site_name: hnrss
content_file: hnrss-flock-wants-the-most-detailed-map-of-its-cameras-t
fetched_at: '2026-09-28T23:42:15.183238'
original_url: https://theintercept.com/2026/09/24/how-many-flock-devices-in-united-states-300000/
author: Nikita Mazurov
date: '2026-09-28'
published_date: '2026-09-24T23:21:24+00:00'
description: A new map shows Flock has more cameras in the U.S. than was previously known. The company wants the map taken down.
tags:
- hackernews
- hnrss
---

A Flock camera, photographed in Tucson, Ariz., on Sept. 23, 2026.

Photo: Nikita Mazurov/The Intercept

Amid mounting concernsabout its sprawling surveillance camera network, Flock Security told the press this summer that it operatesmore than 120,000cameras nationwide.

But a new map published Wednesday by a cybersecurity researcher reveals Flock’s nationwide reach is even bigger. Based on location coordinates from Flock’s own database, the map shows more than 170,000 cameras, plus more than 130,000 accompanying gadgets that play a part in the company’s expansive American surveillance network.

Joshua Michael’sFlock Surveillance Maphighlights the locations of what he says are 300,000 Flock surveillance devices spread across the country. His findings — which were cited in Wednesday’s Senate Subcommittee on Crime and Counterterrorismhearingon Flock — differ from existing maps of Flock’s automated license plate readers in scope and methodology.

“These cameras form a nationwide surveillance network that tracks where everyone drives.”

Unlike crowd-sourced projects such asDeFlock, which are built on locations submitted by users, the Flock Surveillance Map relies on location data culled from a snapshot, archived by Michael in December 2025, of Flock’s own records. In addition to cameras, it maps supplemental devices — including 27,000 acoustic detection devices, as well as networking equipment that integrates third-party cameras — to illustrate the scale of Flock’s surveillance web.

“These cameras form a nationwide surveillance network that tracks where everyone drives,” Michael told The Intercept, “so foreign nations don’t need to send spies to harm our country. They can simply watch where our soldiers, federal agents, and politicians go.”

## Most ReadDoorDash Spent $1.4 Million Trying to Stop Mamdani From Becoming Mayor. Now We Know Why.Meghnad Bose, Macy Hanzlik-BarendThe Backlash to “NAZA” Shows How Little Israeli Citizenship Really MeansSéamus MalekafzaliThe “Satanic Panic” Made Her a True-Crime Obsession. The Truth Is More Haunting.Liliana Segura

The Intercept visited six random Arizona locations on Michael’s map; each location had a Flock camera present at the indicated coordinates.

The Flock Surveillance Map also color-codes each Flock device according to its model — showing, for instance, whether the device is a Flock camera, known as a Falcon, or an accompanying processing unit known as a Picard. (Flock did not immediately respond to a request for comment.)

The accompanyingsearchable dataset tablealso lists each camera’s individual name, as outlined in Flock’s database, which typically includes a street address and sometimes other identifying characteristics. A camera with the name “FBI Pilot Camera,” for example, is shown to be located at the J. Edgar Hoover Building — the FBI headquarters in Washington.

 

## Related

### Cops Are Using Flock to Spy on People for the Crime of Standing Around

 

The map illustrates Flock’s national spread, but also its clustering in certain areas. For example, 860 Flock devices appear to be concentrated just outside Chicago O’Hare International Airport, at the Rosemont Public Safety Department, which provides police, fire, and emergency medical services in the Chicago suburb.

Numerous Flock cameras appear to be installed inside detention centers. A camera titled “C-F-23 FOXTROT MALE HOLDING 2/SHOWERS” appears at the coordinates of the Silverdale Detention Center in Chattanooga, Tennessee.

## We’re independent of corporate interests — and powered by members. Join us.Become a member## Join Our NewsletterThank You For Joining!Original reporting. Fearless journalism. Delivered to you.Will you take the next step to support our independent journalism by becoming a member of The Intercept?I'm inBecome a memberBy signing up, I agree to receive emails from The Intercept and to thePrivacy PolicyandTerms of Use.## Join Our Newsletter## Original reporting. Fearless journalism. Delivered to you.I'm in

In November 2025,Michael discovered a novel way to identify the location of Flock’s devices. Trawling the company’s website, he realized that Flock’s servers were publicly leaking data in the form of an access token that could be acquired without needing to log in. With that token, Michael said he could query ArcGIS, a third-party geographic information system platform used by Flock, to retrieve the locations of Flock devices.

Michael told The Intercept he promptly contacted Flock and described his findings. As Michael wrote in his initial email to Flock on November 13, 2025: “all testing was strictly non-intrusive, limited to open unauthenticated endpoints, and did not involve bypassing authentication, modifying data, or invoking any billable ArcGIS or Google operations.” Michael said he didn’t receive a reply, so he followed up with Flock the next day, and a third time several days later.

After his third attempt to inform Flock of the discovered vulnerability, Michael received a reply from a Flock that said, “Thank you for the findings. We are internally triaging them and will reach back out with next steps soon.”

 

## Related

### License Plate Surveillance, Courtesy of Your Homeowners Association

 

Michael said he never heard back about it from Flock.

In December 2025, Michael downloaded the Flock device location data, and in January wrote an in-depth technicalblog postabout what he had found. After Michael’s post, it appears that Flock fixed the vulnerability.

Despite being alerted of Michael’s findings in November 2025, Flock published its ownblog postthe following January saying it hadn’t had any data breaches. “Flock has never been hacked, and there has not been a leak of Flock information,” the company claimed. “Flock Safety’s cloud platform has never experienced a data breach.”

The Atlanta-based startup has faced mounting criticism for its practices and lack of transparency in recent months. An American Civil Liberties Unionreportfound “a pattern of Flock regularly misleading or even lying about its business practices, safety record, commitment to privacy, and efforts to protect vulnerable populations.”

Michael told The Intercept that Flock’s recent claims about its data security record don’t reflect reality. Flock has publicly claimed multiple times that the company has never experienced a data breach, “and this was after I pulled their database of devices.”

“That leaves two possibilities,” he said. “Either they knew and chose not to disclose it for fear of bad press, or they didn’t know I exfiltrated the data at all. The first is a transparency failure. The second is a detection failure with national security implications.”

On Thursday, Michael was notified that Doppel, which describes itself as an “AI-native social engineering defense platfom,” filed a trademark infringement complaint regarding his site, claiming to be working on Flock’s behalf. Doppel says that the site is using the trademark “FLOCK SAFETY” without authorization, which “may cause customer confusion / harm.” Doppel requested the site be taken down.

When he posted the Flock Surveillance Map, Michael included a pop-up disclaimer saying that the site is “not affiliated with or endorsed by Flock.”

 Share 

IT’S EVEN WORSE THAN WE THOUGHT.

What we’re seeing right now from Donald Trump is a full-on authoritarian takeover of the U.S. government.

This is not hyperbole.

Court orders are being ignored. MAGA loyalists have been put in charge of the military and federal law enforcement agencies. The Department of Government Efficiency has stripped Congress of its power of the purse. News outlets that challenge Trump have been banished or put under investigation.

Yet far too many are still covering Trump’s assault on democracy like politics as usual, with flattering headlines describing Trump as “unconventional,” “testing the boundaries,” and “aggressively flexing power.”

The Intercept has long covered authoritarian governments, billionaire oligarchs, and backsliding democracies around the world. We understand the challenge we face in Trump and the vital importance of press freedom in defending democracy.

## We’re independent of corporate interests. Will you help us?

 $15 

 $25 

 $50 

 $100 

 $5 

 $8 

 $10 

 $15 

 One Time 

 Monthly 

 Donate 

IT’S BEEN A DEVASTATINGyear for journalism — the worst in modern U.S. history.

We have a president with utter contempt for truth aggressively using the government’s full powers to dismantle the free press. Corporate news outlets have cowered, becoming accessories in Trump’s project to create a post-truth America. Right-wing billionaires have pounced, buying up media organizations and rebuilding the information environment to their liking.

In this most perilous moment for democracy, The Intercept is fighting back. But to do so effectively, we need to grow.

That’s where you come in. Will you help us expand our reporting capacity in time to hit the ground running in 2026?

## We’re independent of corporate interests. Will you help us?

 $15 

 $25 

 $50 

 $100 

 $5 

 $8 

 $10 

 $15 

 One Time 

 Monthly 

 Donate 

I’M BEN MUESSIG,The Intercept’s editor-in-chief. It’s been a devastating year for journalism — the worst in modern U.S. history.

We have a president with utter contempt for truth aggressively using the government’s full powers to dismantle the free press. Corporate news outlets have cowered, becoming accessories in Trump’s project to create a post-truth America. Right-wing billionaires have pounced, buying up media organizations and rebuilding the information environment to their liking.

In this most perilous moment for democracy, The Intercept is fighting back. But to do so effectively, we need to grow.

That’s where you come in. Will you help us expand our reporting capacity in time to hit the ground running in 2026?

## We’re independent of corporate interests. Will you help us?

 $15 

 $25 

 $50 

 $100 

 $5 

 $8 

 $10 

 $15 

 One Time 

 Monthly 

 Donate 

## Contact the author:

 Nikita Mazurov 

## Latest Stories

 

Targeting Iran

### Iran Has Wounded and Killed More Americans Since the End of Operation Epic Fury

Nick Turse

- 
5:45 pm

The Trump administration’s attempt to rebrand its faltering forever war hasn’t slowed the mounting toll of U.S. casualties.

 

### AI Almost Started a U.S.–China War — and No One Seems to Care

Sam Biddle

- 
12:54 pm

The tech world is too busy dreaming up imaginary doomsday scenarios to focus on a very real one that flared up between nuclear powers.

 

### The “Satanic Panic” Made Her a True-Crime Obsession. The Truth Is More Haunting.

Liliana Segura

- 
Sep. 27

After 30 years on death row, Christa Pike faces execution for a grisly murder she committed at 18.

 Join The Conversation