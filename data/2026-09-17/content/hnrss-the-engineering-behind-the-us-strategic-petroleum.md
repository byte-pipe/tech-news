---
title: The engineering behind the US Strategic Petroleum Reserve | John Wang
url: https://johnjwang.com/post/2026/09/15/engineering-behind-us-strategic-petroleum-reserve
site_name: hnrss
content_file: hnrss-the-engineering-behind-the-us-strategic-petroleum
fetched_at: '2026-09-17T15:27:04.099670'
original_url: https://johnjwang.com/post/2026/09/15/engineering-behind-us-strategic-petroleum-reserve
author: John Wang
date: '2026-09-15'
published_date: '2026-09-15T00:00:00Z'
description: 'One of the most fascinating things I&rsquo;ve learned about recently is the engineering behind the US Strategic Petroleum Reserve. Here are the key requirements it&rsquo;s designed to meet: Store …'
tags:
- hackernews
- hnrss
---

One of the most fascinating things I’ve learned about recently is the engineering behind the US Strategic Petroleum Reserve. Here are the key requirements it’s designed to meet:

* Store hundreds of millions of barrels of crude oil for long periods of time torespond to disruptions in petroleum supplies.
* Keep the oil secure against attacks by our adversaries. This is an especially hard challenge because petroleum has this tendency to light on fire, so a huge concentration of it is especially difficult to keep safe.
* Release oil quickly so it can reach the market during a supply disruption.
* Keep maintenance costs low and last for decades.

The actual solution, like many great engineering solutions, is incredibly elegant and simple. But before we talk about it, let’s start with how you might go about solving this:

## The naive solution: External floating roof tanks

Enbridge tank farm, Cushing, Oklahoma, April 2010. Photo: 
roy.luck
, 
CC BY 2.0
.

Looking at the requirements, the first thing most people would probably think to do is to just take what we do commercially for storing petroleum and scale it up.External floating roof tanks (EFRTs)are the common solution for storing petroleum. Most tanks are confined to about 50 feet tall and 300 feet in diameter – larger than that and you start to have engineering problems with the foundation and drainage systems. This gives a volume of $V = \pi (150 \mathrm{ft})^2(50 \mathrm{ft})$, or $3{,}532{,}500 \mathrm{ft}^3$, equivalent to about 630,000 barrels of oil.

To hold 714 million barrels of oil (the full capacity of the Strategic Petroleum Reserve), you’d need about 1,130 of these tanks. If you use the standard capacity of the largest commercial petroleum farms (e.g., in Cushing, Oklahoma), you need about 45,000 acres to store these tanks. That’s basically the size of Washington, D.C., which means you’d need to acquire a lot of land.

However, the biggest downside to using tanks is that they’re incredibly vulnerable to attack. Damage can cause spills and fires, and there’s a particular weak point at the seal between a floating roof and the tank shell.Lightning-caused fires have been documented in the seal space of open floating-roof tanks, so a deliberate ignition source (shrapnel, incendiary) could be particularly bad.

## Putting tanks underground

Next up, one might think about putting the petroleum underground. The Navy actually did this at theRed Hill Facilitynear Pearl Harbor. Built in 1943, it housed 20 enormous steel-lined concrete tanks inside excavated volcanic rock. Each tank was about 100 feet across and 250 feet tall, making it comparable in volume to a large EFRT. Altogether, the facility housed 6 million barrels of fuel. The surrounding rock provided protection from aerial attack, which was a major reason for building the facility. But this was a substantial construction project, and thousands of workers had to excavate the tunnels, install steel liners, and pour concrete. The original construction cost was$42.2 million (~$820M in 2026 dollars).

Also, groundwater protection became a major challenge. A tank released about 27,000 gallons of fuel in 2014. Separate releases in 2021 contaminated the Navy’s drinking-water system, causing the Navy to defuel andpermanently close the facility.

There’s also the question of scale. To get to 714 million barrels, you’d need roughly 119 Red Hill-sized facilities’ worth of capacity and enough space to actually put these tanks in the ground. It would be an absolutely enormous construction project that would cost hundreds of billions of dollars (which, even for the government, is extremely expensive).

## The actual solution: Salt caverns

So how did the US solve this? The crux was using salt domes at four sites in Texas and Louisiana along the Gulf of Mexico. The US created massive caverns underground in these salt domes that hold about 10 million barrels each (more than the entire Red Hill facility). The DOE currently lists 60 caverns with a combined authorized storage capacity of about714 million barrels.

A few properties make this work:

* Cylindrical caverns are excavated using water. Engineers drill into a salt dome and inject fresh water. The salt dissolves in the water, and then pumps are used to remove the resulting brine, leaving a cavern that can be used to store petroleum.
* Salt contains the oil and helps seal small fractures. The rock salt surrounding the SPR’s caverns has extremely low permeability, meaning fluids have very little ability to pass through it. It also doesn’t react with petroleum. Under enormous pressures underground, salt also slowly deforms, which helps close small fractures. The salt itself can therefore contain the oil without a steel-and-concrete tank lining the cavern.
* Oil floats on water, which means pumping water into the bottom of the cavern pushes the oil out. As fresh water is pumped into the bottom of the cavern, the oil gets displaced upwards into a delivery system.
* As a bonus, the location helps get oil to market. The Gulf Coast puts the reserve near refineries, pipelines, and marine terminals, which is particularly useful when the whole point is to deliver oil during a supply disruption.

This storage solution is relatively inexpensive. DOE’s historical capital-cost estimate is about [$3.50 per barrel](https://www.energy.gov/hgeo/opr/spr-faqs) of cavern storage capacity, compared with$15-$18for aboveground tanks. Storing the oil deep underground also helps protect it from aerial attack.

There are still tradeoffs, though. Creating caverns requires a water supply and a way to dispose of the brine. And fresh water introduced during withdrawals dissolves additional salt, gradually enlarging the caverns. That limits repeated cycling and makes cavern monitoring and maintenance quite important. The wells, pumps, and pipelines also need continued upkeep, so frequent withdrawals can degrade the infrastructure.