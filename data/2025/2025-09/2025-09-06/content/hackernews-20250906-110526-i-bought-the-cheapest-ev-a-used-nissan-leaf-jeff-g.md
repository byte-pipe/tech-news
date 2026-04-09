---
title: I bought the cheapest EV (a used Nissan Leaf) | Jeff Geerling
url: https://www.jeffgeerling.com/blog/2025/i-bought-cheapest-ev-used-nissan-leaf
site_name: hackernews
fetched_at: '2025-09-06T11:05:26.224028'
original_url: https://www.jeffgeerling.com/blog/2025/i-bought-cheapest-ev-used-nissan-leaf
author: calcifer
date: '2025-09-06'
---

# I bought the cheapest EV (a used Nissan Leaf)

I bought a used 2023 Nissan Leaf in 2025, my first 'new' car in 15 years. The above photo was taken by the dealership; apparently their social media team likes to post photos of all purchasers.

I test drove a Tesla in 2012, and quickly realized my mistake. No gasoline-powered car (outside of supercars, maybe? Never drove one of those) could match the feel of pressing the throttle on an electric.

I started out with a used minivan, which I drove into the ground. Then I bought a used Olds that I drove into the ground. Then I bought a used Camry that I bought before we had kids, when I had a 16 mile commute.

Fast forward about 15 years, and I found myself with a very short commute, only driving a few miles a day, and a family minivan we use for nearly all the 'driving around the kids' stuff.

So I wanted a smaller car (get back a foot or so of garage space...) that was also more efficient.

## Video and GitHub EV Project

If you don't like reading blog posts (why are you here?), I also posted a video going over most of this, with a little more color, on my YouTube channel:

Also, this blog post is also the centerpiece of my new GitHub projectgeerlingguy/electric-car, where I detail all the steps on my nascent EV journey.

## Equipment and Add-ons

Before I go further, I thought I'd mention some of the things I've added to my Leaf to make the EV experience a little nicer (some links are Amazon affiliate links. I earn for qualifying referrals):

* Grizzl-E Level 2 Chargerfor the garage (seeIssue #5)
* Lectron L1 J1772 EV chargerfor a more portable charger, when I just need to top off the car for a few hours
* J1772 Wall mount for cable and plug- I was going to 3D print one, but figured the metal product would hold up better in a garage in the midwest
* NACS to J1772AC L1/L2 charging adapter
* CCS1 to CHAdeMOL3 DC Fast charge adapter (seeIssue #9)
* CarlinKit 5.0 Wireless CarPlay/Android Auto adapterbecause the Leaf only supports wired CarPlay by default
* VIOFO A119 Mini Dashcamwith aDongar wiring harness adapter(seeIssue #3)

## Monitoring the Battery

If you're considering a used Leaf, or if you have a Leaf already, it's a good idea to keep tabs on the battery health, especially since the meter on your dash is painfully basic in how much data it provides.

Individual cell charge, 'State of Health' of the overall battery, and much more are available through the car's OBD-II port.

Soon after I bought my Leaf, I ordered aLeLink 2($35) and bought theLeafSpy ProApp for my iPhone ($20).

I plugged the LeLink 2 into the OBD-II diagnostics port under the steering column, and fired up LeafSpy Pro. It gives me some helpful metrics like:

* SOH: State of Health
* Hx: Conductance

SeeIssue #8: Document battery healthfor all my notes monitoring my own Leaf's battery. But bottom line, my battery showed a 93.16% 'SoH' (State of Health), meaning it still has most of its capacity.

I've been reading up on various forums about managing the Leaf's battery, and am trying to do some things to extend the battery's life as long as possible:

* Limiting the number of QCs (Quick Charges / DC Fast Charge), as this heats up the uncooled Leaf battery, degrading it slightly each time, especially on hotter days
* Keeping the charge between 50-80% when manageable
* Charging up to 100% at least once a month, and letting it 'top off' to rebalance the pack for at least a few hours afterwards
* Not driving like a maniac, despite having more torque in this car than I've ever had in any of my previous cars

## Why buy electric?

I overanalyze most things, so had been researching this purchase for about a decade now.

With EVs there are tradeoffs. Even in my situation, only driving a car a few miles a day, Idotake my car on one or two regional road trips every year.

Having the ability to hop in at 6 am and be in Chicago or KC by late morning is nice. Having to plan a long break somewhere halfway to charge is not.

But if I only take that trip once a year, I can either (a) rent a gas car that gets me there a little more quickly, and ensures I don't have to find a spot in the destination city to do a full charge before the return trip. Or (b) plan for an extra X hours total during the trip to ensure I have padding for charging.

Charging infrastructure's improving in the US (and in many parts of the world), but it's nowhere near as ubiquitous as gas stations.

Hopefully this improves over time, but for now, I plan on using the electric car for local travel, likely only going more than 100 miles or so in a day once or twice a year.

## Why buy Leaf?

Price.

That's mostly it. And I drove a Nissan Sentra rental on a recent trip, and realized Nissan isn't half bad. They seem to not require an Internet connection for their cars, they offer basic lane following and adaptive cruise control, they have CarPlay/Android Auto...

The Leaf ticks all the little 'convenience' checkboxes, but is also not 'extravagant'.

And the later model years also aren't "look at me I drive an EV" ugly (though they're not amazing-looking, either).

But I drove a minivan, an olds, and a Camry, so obviously I'm function > form when it comes to my car!

Because of the smaller battery (and up until 2026, a battery with no active cooling), combined with the use of a DC fast charging connector (CHAdeMO) that's going out of style in the US, used Nissan Leafs are pricedconsiderablylower than competitors.

Well, all except maybe Teslas around a year or two older right now. But Teslas don't have native CarPlay. And I'm not a fan of how Tesla is trying to turn the car into some kind of appliance, RoboTaxi, self-driving thing, versus it being a transportation vehicle that I can do what I want with.

No judgement on Tesla owners, the used Tesla market was enticing at the time I bought the Leaf.

I also looked a lot at the Hyundai Ioniq and Kona; both were just alittlebit too large for my liking, but they could've worked. The problem was used models in good condition were a lot more expensive than I was willing to pay.

So back to the Leaf: Nissan's probably not thebestright now when it comes to EVs and features, but they're certainly thecheapest. And 'good enough' is fine by me.

She's got it where it counts, kid.

## Gripes about my Leaf

There are a few things that baffle me about the Leaf, some that have been frustrating from the first test drive; others that are more subtle:

* There is no 'play/pause' button.Anywhere. At least not on the steering wheel or the display area. You have to go into the music section on the entertainment display,thenpress the software play/pause button. That's dumb. I've resorted to just turning Audio on/off using the volume knob, which accomplishes the same goal but is not always ideal.
* Going into 'Neutral' is an exercise in frustration.I thought you just put your foot on the brake and move the shifter knob to the left. But you have to do it with the right timing, I think.
* There's no way to open the tailgate short of pressing the release button.At least as far as I'm aware. There's no button in the cabin or key fob to unlatch it. The manual says the other way to open it is with a screwdriver, from inside the car, pushing on the latch (lol).I'm not alone here. At least there's a button on the remote to open the charge port.

## The joy of electric

I don't care about engine noise. I appreciate it, though. My brother had a 1992 Forumula Firebird. And I nearly owned it after he moved away, instead of my Olds! (But I'm a boring-car person, so I think I was happier with the Olds).

The nice things about electric vehicles that swayed me in their favor, in descending order:

* One pedal drivingSeriously, why doesn't every EV have this mode? It makes driving one feel SO much better than any gas car, in terms of connection between driver and car movement.
* Sprightly torque: Outside of exotic tiny gas cars, you're not going to get the same zip even a cheap EV like a Leaf gives you—smash the accelerator in non-Eco mode and any passenger will giggle, every time.
* Blissful quiet: Though some cars have annoying noises (Nissan calls this VSP, or "Vehicle Sound for Pedestirians") they play at low speeds.
* Lower maintenance requirements: I hate every time I have to jack up my car and change the brakes, or take it in for oil/fluid changes. EVs (usually) require less maintenance, besides maybe tires.
* Conveniences: Like running climate control to cool down/heat up the car prior to hopping in, even while it's in the garage! Or plugging it in to charge at home, and not having to stop by a gas station.
* Long-term economics: ingeneral, charging with electricity, at least here in St. Louis, is cheaper than filling up with gas, on a dollar-per-mile basis.

## The pain of electric

All that said, I knew going into this there would be some pain. Maybe in 10 or 20 years these things will get solved, but off the top of my head:

* Price: The Leaf (especially used, right now) is the cheapest, but it is by no meanscheap. It takes a few years to break even with a similarly-specced gas car. But buying a gas car, you have a lot more options on the low-low end.
* Range Anxiety: Yes, it's overblown, but no, it's not non-existent. The day Iboughtmy used EV, the dealership (which doesn't sell many EVs, even new) didn't have a 'Level 3' DC fast charger—and they had only charged it to about 16%. Letting it top off at L2 while I was dealing with finance, we got to 23%. I wasn't quite sure I'd make it home off the lot! Luckily I did, with 12 miles of range remaining. Road tripping or day trips require more planning when driving an EV.
* Lack of standards: For 'L3' DC Fast Charging, the Leaf has a CHAdeMO port. Teslas and many newer EVs have NACS. Then there's CCS1 and CCS2. And charging stations are run by multiple vendors with multiple apps and payment methods. It's not like gas stations, like with Shell, BP, Buckee's, etc. where you just drive up, stick the gas nozzle in your tank, and squeeze. Even adapters can be complicated and annoying, and many EV charging stations only support one or two standards—and some may only haveoneCHAdeMO plug, and that plug may have been ripped off the unit to be scrapped by a copper thief!
* Lack of standards, part 2: For L1/L2 charging, some cars use J1772, some use NACS... and then wall charging units are all over the board with supporting 6, 12, or 16 Amps for L1 (they shouldn't do 16 on a 15A circuit but it seems like some do!), or various different amperages for L2. Some of these units require apps to configure them, others have dip switches, and yet others are not configurable, and don't list their exact specs in an easy-to-find location. Usually forum posts from users whobuythe chargers offer more information than product manufacturers' own websites!
* Being an EV: For some reason, most EVs look like... EVs. I honestly was holding out hope Tesla would just make a Corolla, but an EV version. All the cheap EVs like the Bolt, i3, Leaf, etc. just look... sorta ugly. Subjective, sure, but at least my Olds looked kinda sleek. Even if it was an Olds. EVs stand out, and that I don't enjoy. I want an EV that looks like a Camry. Just blend in and don't stand out.
* Cables and chargers: The Leaf has slightly less trunk space than my slightly-larger Camry. I didn't realize how big L1/L2 charge cables are. Even L1-only cables (which charge at a very anemic pace, like 10 miles / hour of charge) are fairly thick, bulky affairs. About 1/10 of my trunk is devoted to my charging cable. And on a road trip, I will likely carry myNACS to J1772andCCS1 to CHAdeMOadapters. And the latter adapter includes itsownbattery (that has to be charged) and firmware (that might need to be updated)!

## The Price I Paid

I was reminded in aHacker News discussion about this postthat I didn't mention the price I paid for the Leaf.

For the 2023 Nissan Leaf SV Plus, with about 36,000 miles and a 94% SoH battery, I paid $17k minus an extra $2k added to my Camry's trade-in value. It's eligible for the$4k used vehicle EV tax rebateat the end of the year (for which I qualify).

It was out the door at $15,000, and at the end of the tax year I'll have paid $11k for the car, effectively.

I tacked on the price of the CHAdeMO adapter mentally to the price I offered, since I knew I'd want it for the one or two regional road trips I take per year.

## Further Reading

Be sure to check theIssuesin my GitHub project for more of my EV adventures.

I don't plan on becoming an EV advocate by any means.

The Leaf is the perfect option for me, but I wouldn't recommend an EV for most car owners yet, especially considering the price disparity and infrastructure requirements that exclude large swaths of the population!

## Further reading

* Home Assistant and CarPlay with the Pi Touch Display 2
* Build log: Macintosh PowerBook 3400c
* Project Mini Rack - compact and portable homelabs

nissan

leaf

electric

cars

ev

video

youtube

* Add new comment


## Comments

I have a much older Leaf (2015) with much less range (allegedly 80, possibly more like 50). The worst moment of range anxiety is when the car jumps from claiming you have 12 miles left, to admitting it has no idea and you'd better do something about it. Happened to me only once on the way back from the airport, but it was awful. I tell everyone to get an L2 charger before they get an EV.

But I love my Leaf. It's fun to drive, and the price still makes me happy.

* Reply

Congrats on the Leaf! I've had two (a first gen, and a second gen) and now have a Mach-E.

I loved those Leafs, but I hated Nissan. My second Leaf (purchased new) had a bad battery pack. It took me a long time to realize it but while the pack behaved normally from ~100% to ~60%, it would drop from ~50% to ~15% over the course of a few miles. I didn't realize because most of my use was very local, so I only discovered this on my first 100-mile road trip. It very nearly stranded me in the mountains outside Portland.

It took me ~9 months, numerous trips to multiple dealers, and eventually threatening them with a lemon law lawsuit to get them to fix the issue. I presented them with videos (https://youtu.be/b3z2BWc63LI), a multi-page PDF showing the voltage levels of all the cells, and identified the single cell that had a bad voltage dip. They refused to do anything until I hired a lawyer.

The eventual fix took them about 15 minutes and resolved the problem completely. Getting to that point wasted many, many, many hours. So frustrating.

* Reply

Most of your listed pain points are related to your specific choice in EV. The Leaf has less range, a more temperamental battery, uses a long-deprecated charging standard, and has fewer quality of life improvements than modern EVs. They are cheap for a reason...

I agree on the charging infrastructure and cost of entry. Those are absolutely barriers that most people won't be able to overcome. Juggling multiple apps, dealing with multiple charging standards and speeds, and just having to plan your route around charging stops is likely a bridge too far for most people. Europe had the right idea by just choosing a national standard that everyone had to follow. The last remaining caveat is towing, where a hybrid makes significantly more sense until energy density increases substantially.

I have a '22 Volvo XC40 Recharge that I use to make an annual trip from Kansas City to the Wisconsin Northwoods. Many vehicles on the market (some of them cheaper) would be more ideal for this trip. The vehicle has a midrange charging speed and is on the lower end of range at only 200 miles or so. For this trip, we typically end up stopping about 6 times for a duration of 20-45 minutes each. For a top-performing EV, you'd probably do the same trip with 4 stops for 15-30 minutes each. Just enough time to get out, stretch your legs, use the bathroom, and hit the road again. The car even plans the route and charging stops for us with the built-in Google Maps. The experience is still not quite ready for "main-stream" use, but it's pretty close.

* Reply

This is very much from the perspective of a used car buyer and thats cool. I look around and see people buying/leasing $30k+ new gas cars and wonder what compels them to buy gas propulsion. If you are spending 30k+ there are a lot of great options in the new ev market. Granted new EV prices are a big unknown for next month, but right now you can pull off the lot in a 2025 Chevy Equinox EV for about $30k OTD. The used market is going to be very interesting in two to three years. Will my Blazer EV be worthless because prices came down so much and battery tech went so far or will it hold its value well given that it seems like most new cars are 30k+. Doesn't matter either way to me because I love it and hope to drive it until there is nothing left of it. If you can charge at home or at work, I cant imagine wanting to stop at a gas station. Enjoy those Es.

* Reply

The new car market is just out of my price range. I'm weird and old school I guess, but I don't want to lease a car, I'd much prefer to purchase it outright, but if you do that, car dealership finance departments get all snippy with you, so I do the loan at whatever the going rate is (I think this one was 6%? my last one was 3%) and pay it off over a few months instead of the 36 month term.

I hate that so many markets are pushing towards people never owning the thing they're 'buying' (and understand that leasing + purchasing can still make more financial sense, I'm just allergic to that model of ownership!).

* Reply

Snippy finance departments. Love it.

Bought our last 2 cars with cash. Drove both dealers crazy. I still don't know why they required me to unlock my credit history so they could do a credit bureau check when I was giving them a personal check for the whole $ 40k or so.

Car buying is just a brutal experience.

* Reply

Probably to check your check won't bounce.

Meanwhile here in Europe, you can do a SEPA Instant Transfer and 10 seconds later the whole price shows up on the dealership's online banking.

* Reply

I just upgraded my EV recently. I purchased a Tesla Model 3 Performance in 2019, and drove it for nearly 6 years on trips long and short. Range anxiety was my own personal problem for about 6 months until I got used to the slightly different behavior patterns. Electricity in my area was exceptionally cheap and my L1 charger on a 15A circuit (12A limit) was more than enough to handle daily work driving. Took quite a few interstate trips and never had a problem charging anywhere. Car was a fairly expensive, but a great car overall, until Elon made it difficult to justify, so we traded it in for a Hyundai Ioniq 5 (800V bat) with NACS. Between the Tesla trade in value and a few thousand in cash, the new car loan was $20K, which was actually pretty damnn good. For the L1 chargers with a 16A setting, at least the Tesla mobile charger has plug adapter options and can use 20A 120V circuits, of which my new house actually has several. I actually had a Tesla L2 wall charger that I couldn't install in the apartment we previously lived in, but now that I have the Ioniq 5 I ended up installing it and it works fantastically. It's a Gen2 without wifi or any of the extra crap, and limiting it to 32A@240v gives me enough power to charge fully overnight while not requiring a huge load on my panel. Car came with 2 plug adapters (no batteries) and we've used them at a couple of different hotels with L2 guest chargers, but we use Superchargers on longer trips if needed. Honestly, the wife and I never see going back to gas. There's just no reason. We'll be putting in solar and home battery storage eventually, so we'll pay a bit more for a bit more energy independence. We did like the Volkswagen ID Buzz van in concept, but they wanted an extremely high price for them and the range sucks. They were actually pretty huge in person, which was kind of nice and had more space than my old Caravan had.

* Reply

I bought a 2022 Polestar 2 at the end of July, replacing a car I'd purchased new in 2002. The Polestar was half the price it'd been when it was new and only had 16,000 miles on it. I'm absolutely loving the electric car experience here in Seattle, and I took a road trip of 500 miles each way to my sister's home in Idaho as a test last week. The Volvo / Polestar NACS power adapter cost close to $300 after taxes but was absolutely worth it to open up more fast charging opportunities during a road trip.

The built in Google maps experience will suggest charging locations if you set a destination that is farther away than your current charge will take you. When I stopped at her home with 20% charge left it asked if I wanted it to find a nearby charging location. (I didn't because she had a power receptacle I could fully charge overnight.)

* Reply

RE "...Not driving like a maniac, despite having more torque in this car ...."

I've always thought , the acceleration of electric cars should be limited. to conserve the battery and conserve battery charge.

* Reply

Most of them do have some sort of drive mode where you can set it to an "eco" state. This slows the pedal response and makes it slightly more difficult to get the fast acceleration. Jamming on the accelerator makes it go fast if you need it to get out of the way or whatever, so that's nice.

* Reply

When war* broke out in Ukraine's, quite a few bought an old leaf and swapped the battery with a newer versions battey pack. They bought them because diesel and gas deliveries were severely disrupted and expensive. Eventually this stopped, because of the electrid grid destruction and c.e. fuel was ok again.

* Reply

We bought a used Hyundai Ioniq Electric 38kWh. I had to replace the small 12V battery (~150 dollars) as soon we got the car. A few months later, a light came up and it was to do with the cooling of the main battery: apparently the original fluid goes bad and clogs the cooling circuit (didn't cost anything, still under warranty and I believe Hyundai is fixing this for free anyway).

Other than this, we've only had to change tires, which seem to last more or less than before. Driving in eco mode removes some of that initial power and probably helps. The breaks will probably be changed in the next check next year.

I've managed to do a 170 miles trip in summer with a full battery and some AC. In winter, it would probably be ~140 miles or so with heating. I do 80-100 miles a day. Charge it over night on a slow 5kW charger, it's done when I'm ready to leave in the morning.

We looked at the Leaf, but on top of the issue with the port (CCS2 is the standard here), the lack of battery cooling worried me as I have no idea how the previous owner was using the car. The 2021 Ioniq Electric doesn't have these issues and so the choice then was between the 28 or 38 kWh battery. The smaller one charges much faster, which can be useful in longer trips, but I wanted to charge less and in 99% of times, the extra range is useful as I don't always start with 100%.

Everything got easier with time. I already have an idea of what 10% of battery can do (the car prediction is often wrong). Apps like ABetterRoutePlanner can help you plan long trips, charging stops, etc, if needed and I have 2 apps to check chargers around me if needed for long trips.

Coming from a diesel car, there was an adaptation period. For example, waiting for 100% during a trip makes no sense. Use 80% as your "full" and the last 20% as a extra can of fuel, which should only be filled if you have the time to do so (eg: charging while you're eating, over night, etc) or absolutely need the range. The panic when I had 20% and the car would tell me to charge it... lol. I also started taking advantage of EV chargers, especially slow ones, to park for free (as I was charging) while going to do something. Last month we went on a one day road trip, arrived there with 40%, parked somewhere where it slowly charged to 100% while we explored the place. I lost no time charging the car.

I'm not going back to ICE cars, unless absolutely needed.

* Reply

To get into Neutral you just hold it to the left without going up or down (while pressing the brake). It takes a second or two of holding so that it doesn't accidentally put it into neutral while you're shifting to reverse or drive, but that's all you need to do.

* Reply

Great article!(on the 2022 Leaf at least) take the plate off the left side in the trunk, and you can fit the whole Nissan L1/L2 charger up in there. The Lectron brick looks to be about the same size...

* Reply

Yes; I have the flat tire repair kit, and an AC NACS to J1772 adapter in there right now. Trying to figure out a way to securely store a couple other things in that bit, in a way they don't rattle around.

* Reply

Dear sir just off topic, but you sincerely reply faster than my ignorant professor does.

* Reply

As someone who has an older Leaf (2015) and living a fairly temperate location, the heated steering wheel & heated seats are for energy efficient heating in colder climates. It's relatively expensive (energy-wise) to resistance heat air to warm the cabin & this reduces range a measurable amount. Switching on the seat heating (ours has front and rear heated seats) and the steering wheel reduces the range a lot less while providing those warm feels. If you don't need that though it could be mystifying.

* Reply
