---
title: Fixing the Portobello Police Station Clock
url: https://pointinthecloud.com/2026-04-11-211700.html
site_name: hackernews_api
content_file: hackernews_api-fixing-the-portobello-police-station-clock
fetched_at: '2026-09-23T22:02:07.881054'
original_url: https://pointinthecloud.com/2026-04-11-211700.html
author: avidly
date: '2026-09-23'
description: Fixing the Portobello Police Station Clock
tags:
- hackernews
- trending
---

Written on 11th April 2026

I got a message from a friend today which read along the lines of "I know we were going to meet in Edinburgh today, but do you fancy meeting in Portobello instead and trying to fix the clock in the old police station with me?"

I don't know about you, but clambering around the dusty nineteenth century clock tower of an abandoned police station sounds an ideal way to spend a Saturday afternoon to me, so I jumped at the chance.

The rather grandPortobello Police Stationbuilding.

This was in response to a message fromAction Porty:

"Can you help keep Portobello on time? Action Porty has recently bought the Police Station for the community, but we can't work out how to change the time on the clock tower! We wondered if there was anyone in the community with expertise that could advise us of the details for changing the time? Or who best to contact for help?"

The bit I hadn't figured out was that clocks are high up. If we were to fix the clock we would be next to it and so we would also be high up. And being high up involves heights, and steep long ladders are needed to get up high.

I suppressed my whimpers at climbing up the rather high, steep ladder into the likely spider-infested darkness and was rewarded with an explore of the attic, which lead to another set of steps which went to the clock tower itself.

Once there we were rewarded with the magnificent sight of the clock mechanism and its three clock faces:

Construction of the building apparently started in 1877 and it seems quite feasible that this was an original mechanism. Modifications had been made - electric motors powered the mechanism and a control box allowed the clock chime to be turned off overnight.

The building was built to house meeting, administration and courts for Portobello burgh council. After Portobello was absorbed into Edinburgh the building became a library, and then a police station.

The Scottish Land Fund has since enabled it to be purchased for community ownership and when I went there many volunteeers were removing the 1970s polystyrene ceiling tiles and wood-chip wallpaper to reveal the original grandeur of the building.

### Setting the clock

The first step was to figure out how to set the time. This is probably easy to someone in the know, but we weren't.

We figured that the clock is driven from the small motor, through a series of gears onto a shaft which rotates once per hour. This shaft is split into three - one for each face, and drives the minute hand directly. A gear on each clock face derives the hour hand. If we could disconnect the motor maybe we could turn the shaft directly and set the time.

Sure enough - we found a pawl on one of the gears which could be lifted out of the way. Once this was done the shaft turned easily and we could set the time. Each hand had a counterweight on the clock face and we could set the time by imagining the hand we couldn't see opposite to each counterweight.

We had a slightly stupid moment when we thought we'd got it wrong, and the clock was running backwards - only to realise we were inside the clock and so were looking at it the wrong way. Doh. We had to head down to the ground to check that the time was correct - but - phew - time was OK and not running backwards.

### Setting the chime

Figuring out the chime was more difficult. The original mechanism had been modified, and switches and a motor had been added. These led to a box containing a circuit board which definitely was not from 1877. It contained a PIC 16F628 microcontroller which had a suspected date-code of 2001. There were a number of relays, a power supply and a battery charging circuit to charge the included lead-acid battery. I assume this box would be getting on for 1/4 century old, but it still seemed to work. No idea how good the battery was; maybe this should be tested another time.

We have idea who designed and built this box; there were no obvious description markings. Is it a standard thing, or just a one-off for this clock?

A mystery unmarked circuit board, ripe for deciphering.

This box didn't have much of a user interface, other than a non-obvious button marked "advance". The only problem was that pressing it did nothing. How did this thing work? Surely you had to set the timesomehow.

A summary after more head scratching, measuring and fiddling:

TLDR:

* The box switches a mains powered motor (the blue one with the chain in the picture above) which controls the chime striker mechanism. When the motor is powered the clock strikes continuously.
* A switch on the striker tells the box how many chimes have taken place, so it knows when to stop.
* A switch on the clock shaft triggers on the hour and tells the box when it should chime.
* The box controls the clock motor. The "reset" switch appears to do nothing other than switch off the clock motor. (As I write this, I assume it also sets the 'time' back to midnight, but this is to be tested).
* The "advance" button needs to be held for a few seconds before anything happens. When it is released, the clock will chime. When pressed and released again, it will chime again for the next hour.
* Setting the time appears to be done by pressing advance until the correct hour is reached.
* The "Status" LED flashes some kind of code - long long, short short short. I assumed the number of flashes would correspond to the time but apparently not. We didn't have time to figure this out before we had to leave.
* The box has no "clock" as such in it - it just has a counter which keeps track of the hour. All timing is done from the "hour trigger" switch from the main mechanism.
* The two switches are connected via banana plugs to the box; the box has cables for the GMT/BST switch, mains input, clock motor out, chime motor out.

I had hoped we could do a "test" by letting the clock chime thirteen (or even just strike continuously), but I was up in the tower with a bunch of spoilsports who wouldn't let me. Oh well, next time when they're not around.

### Yay - It tells the time

So - we waited until 4pm and the clock had advanced and we checked outside and the time was good. Come 4pm and the bell chimed 4 times. Dongggggg. (Bells are loud when you're next to them. Oops again.) This was perfect timing - 4pm was the time we had to leave.

We decided our mission was a success. Some local residents may have decided that the chime reinstatement was not a success, so we disconnected the chime motor to disable the chime.

### Some pub-fuelled enhancements:

After a quick visit to check out the police cells we decided to head across the road to thePortobello tapfor a beer and one of their burgers to celebrate our success. Lucy the dog came to join us and she was very quick to point out how starved she was, and really a little chip would just tide her over until she got her dinner, as she had bad owners who just never fed her. She isn't a labrador really.

After our beer we thought of some "enhancements":

* Have a box with more control of the chime times in case 8am is too early for chimes to start.
* Be able to have a remote control chime for special occasions.
* Have a doorbell which chimes the clock when you ring it.
* Make it chime 13 at Halloween.
* Have some customised LED lighting to replace the fluorescent tubes. This could have a rainbow forPorty Prideor St Patricks day or Christmas colourings or something.
* More to come

### It was fun

It was a fun afternoon, and thank you for the invite. I'm looking forward to seeing what becomes of the police station now it is community owned - it has the potential to be such a fun place! Maybe I can go back and become more involved.