---
title: 'Show HN: Will my flight have Starlink? | Hacker News'
url: https://news.ycombinator.com/item?id=47428650
site_name: hnrss
content_file: hnrss-show-hn-will-my-flight-have-starlink-hacker-news
fetched_at: '2026-03-19T11:17:49.263524'
original_url: https://news.ycombinator.com/item?id=47428650
date: '2026-03-18'
description: 'Show HN: Will my flight have Starlink?'
tags:
- hackernews
- hnrss
---

Hacker News
new
 | 
past
 | 
comments
 | 
ask
 | 
show
 | 
jobs
 | 
submit
login
Show HN: Will my flight have Starlink?
227 points
 by 
bblcla
 
17 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
297 comments
Hey HN, If you’ve been lucky enough to be on a flight with Starlink, you understand the hype. It actually works!

However, its availability on flights is patchy and hard to predict. So we built a database of all airlines that have rolled out Starlink (beyond just a trial), and a flight search tool to predict it. Plug in a flight number and date, and we'll estimate the likelihood of Starlink on-board based on aircraft type and tail number.If you don’t have any trips coming up, you can also look up specific routes to see what flights offer Starlink. You can find it here:https://stardrift.ai/starlink.-I wanted to add a few notes on how this works too. There are three things we check, in order, when we answer a query:- Does this airline have Starlink?- Does this aircraft body have Starlink?- Doesthis specific aircrafthave Starlink?Only a few airlines at all have Starlink right now: United, Hawaiian, Alaskan, Air France, Qatar, JSX, and a handful of others. So if an aircraft is operated by any other airline, we can issue a blanket no immediately.Then, we check the actual body that's flying on the plane. Airlines usually publish equipment assignments in advance, and they're also rolling out Starlink body-by-body. So we know, for instance, that all JSX E145s have Starlink and that none of Air France's A320s have Starlink. (You can see a summary of our data athttps://stardrift.ai/starlink/fleet-summary, though the live logic has a few rules not encoded there.)If there's a complete match at the body type level, we can confidently tell you your flight will have Starlink. However, in most cases, the airline has only rolled out apartialupgrade to that aircraft type. In that case, we need to drill down a little more and figure out exactlywhichplane is flying on your route.We can do this by looking up the 'tail number' (think of it as a license plate for the plane).Unfortunately, the tail number is usually only assigned a few days before a flight. So, before that, the best we can do is calculate the probability that your plane will be assigned an aircraft with Starlink enabled.To do this, we had to build a mapping of aircraft tails to Starlink status. Here, I have to thank online airline enthusiasts who maintain meticulous spreadsheets and forum threads to track this data! As I understand it,theyusually get this data from airline staff who are enthusiastic about Starlink rollouts, so it's a reliable, frequently updated source. Most ofourwork was finding each source, normalizing their formats, building a reliable & responsible system to pull them in, and then tying them together with our other data sources.Basically, it's a data normalization problem! I used to work on financial data systems and I was surprised how similar this problem was.-Starlink itself is also a pretty cool technology. I also wrote a blog post (https://stardrift.ai/blog/why-is-starlink-so-good) on why it's so much better than all the other aircraft wifi options out there. At a high level, it's only possible because rocket launches are so cheap nowadays, which is incredibly cool.The performance is great, so it's well worth planning your flights around it where possible. Right now, your best bet in the US is on United regional flights and JSX/Hawaiian. Internationally, Qatar is the best option (though obviously not right now), with Air France a distance second. This will change throughout the year as more airlines roll it out though, and we'll keep our database updated!

 
help

devin
 
13 hours ago
 
 | 
next
 
[–]

I've written it elsewhere, but: it is such a shame that the United States saw fit to run electricity _everywhere_, no matter how rural your location, but instead of do the same for rural internet we had to wait for... a private company to launch a global network of satellites. Yes, this post is about internet access while traveling 500mph, which is a different problem, but it is so messed up that people fall over themselves about Starlink for rural connectivity when it is an incredibly complex and expensive technology with huge ongoing costs that could have been solved once and for all by simply running some wires.

reply

modeless
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

You have it exactly backwards. It is far less complex and expensive and resource intensive to build Starlink than to run a new copper or fiber line with associated telecom equipment on both sides to every rural residence in the US, let alone worldwide. Yes, despite the large cost of launching satellites. And it's especially good that we don't have to force everyone to subsidize inefficient monopoly utilities with our tax dollars to get everyone connected. Plus the benefit of mobility is enormous and shouldn't be ignored.

As solar and batteries become cheaper, eventually we can transition to most rural residences being entirely off the grid and self sufficient. This will also be cheaper and less resource intensive than maintaining the electric grid in those rural areas, let alone building it in the first place, and we can all stop paying hidden subsidies for those users.

reply

andrewharvey
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

this.

Except it's no longer only in rural areas, grid connected utilities are now costing more than being off grid in the cities too. Starlink residential 100 Mbps is cheaper ($69/mo AUD) (ignoring hardware and setup costs) than 50 Mbps fixed line internet ($80/mo AUD). Depending on location, home solar + batteries will usually work out cheaper than being on the grid within the battery warranty period too.

reply

rob74
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The question that comes up then is: how much traffic can Starlink handle until it gets saturated? I'm not sure it can handle even a significant percentage of the users that currently use wired connectivity. And if they see that demand for their services starts overwhelming supply, they will definitely raise the prices...

reply

JonChesterfield
 
35 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

_Lots_ of traffic. It's going to end up being the global Internet backbone.

reply

Affric
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Grid prices are going to start coming down in some of the most expensive parts of Australia due to SAPS, home generation and storage, and microgrids.

I wouldn’t rule out the grid just yet.

reply

markdown
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If you find Starlink cheap they just haven't gotten around to the bait and switch in your locality. It'll come.

reply

raw_anon_1111
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Where are you? In the suburbs of Atlanta I paid $80 for AT&T Fiber 1Gbps u/d.

reply

gnabgib
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If they're paying Australian Dollars.. probably not Atlanta

reply

Nursie
 
52 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This is because Australia has high internet prices. Partly because it's 
huge
, but partly because the NBN got stuffed-up by the Liberals because they didn't believe the country should be investing in what they called at the time "a glorified video delivery service", so put the tech back a decade, and the country ended up paying more for a worse rollout.

Your comparison point is also a bit weird to me. If I want a decent speed, my choices are fixed wireless NBN at ~250Mbit (400 in theory, 250 in practice), or Starlink at ~200Mbit, and they cost around the same.If I were just a few km closer to the city I could get 500Mbit fibre for ~$90 a month.So while it's definitely not out of the range of other plans, I wouldn't say it's definitively cheaper. And I wonder if the recent price drops are down to people not wanting to have much to do with Elon Musk any more. I know it's worth a few bucks a month to me not to be a customer of his.

reply

UltraSane
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Man, I pay $50USD/month for 1Gbps up down in Wisconsin.

reply

310260
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

As far as electric goes, that's a nice thought but the reality is prices will not go down in such a scenario. I'd rather my bill go to subsidizing rural areas than to pure profit. Nevermind there are benefits helpful to rural areas that grid service can provide versus solar+battery.

reply

sandworm101
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Maybe today, but internet over radio cannot defeat physics. There is only so much bandwidth, so much space in the RF spectrum for data. But landline internet is effectively limitless. You can always lay a second, or twentieth, fiber run. A 10cm bundle of fibers can carry more bandwidth than the entire starlink network many times over, with much lower running costs.

The most effective in rural areas is generally a combination. Fiber to a central location and wifi radio out to customers. I am monitoring a property on the west coast connected via such a setup. The last relay is actually solar powered atop an island.

reply

jojobas
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Starlink recently hit 10k satellites. I'd hazard a guess that's not anywhere near enough getting everyone in the US, let alone worldwide, online.

reply

theParadox42
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

While having more satellites sure does help serve more people, there’s a second issue which arises when trying to serve high density areas, where you run into bandwidth limitations. The solution there is not more satellites but either bigger satellites (which can make smaller beams) or more FCC allowance on the spectrum.

reply

modeless
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Not everyone. But it's enough for rural areas, which are the most expensive and least practical to serve with wires.

reply

sunshinekitty
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The HN groupthink is to hate on anything Elon adjacent, satellite internet included.

reply

razingeden
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

hopefully that include his business partners , airlines in this case.

reply

platevoltage
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's not groupthink to believe that the guy sucks and is a threat to humanity. He constantly fights against the type of programs that could have possibly given us satellite internet, the same way we all get to enjoy GPS.

reply

SV_BubbleTime
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> It's not groupthink to believe that the guy sucks and is a threat to humanity.

Wow, that’s a wild misstatement; that is exactly groupthink nonsense.You (people) loved him before he went in for Trump.

reply

heavyset_go
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> 
You (people) loved him before he went in for Trump.

The inflection point for the public was Musk calling the cave diver, who helped orchestrate the rescue of a dozen trapped kids, a "pedo guy" and then doubling down on it, again, twice in front of his audience of millions.The inflection point for anyone in tech with two eyes and a brain was Musk insisting his companies produce products that do more than they are, still to this day, capable of.First was around 2018, the latter was ~2016, although anyone who was familiar with machine learning knew models were not as capable as Musk was insisting they were, and that the hyperloop was a scam.

reply

odo1242
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Before he went in for Trump he created an obviously fake, insanely expensive system that could never work in practice (Hyperloop) just to slow down California rail projects

reply

tdeck
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Before he went in for Trump he was running a factory with an alarmingly high injury rate, where employees were regularly called the N-word, and union busting. People who liked him then weren't paying attention at all.

reply

tombert
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

For what it's worth, I hated him well before he had anything to do with Trump. Most concretely when he called the cave diver a pedo for not wanting to use his stupid submarine, but I remember thinking that the Hyperloop thing he was proposing was pretty stupid too.

Oh, and when he lied about taking Tesla private so he could quickly boost the price of the stock. That sucks too. He's always sucked.

reply

iknowstuff
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

People in the United States can choose to live in very rural and sparsely populated areas, far more remote than most OECD countries.

It’s not clear to me that we should necessarily massively subsidize their choice to live in the sticks these days. Starlink and 5G are great for this, as is solar energy and batteries.We already subsidize sprawl’s expensive-per-person infrastructure with tax revenue from dense cities. As a country we need to make a decision about which choices we want to encourage and discourage.

reply

TulliusCicero
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Some people will be really mad about this comment, but it's absolutely correct.

Broadly speaking, very rural living is generally a lifestyle choice. Yes, not everyone can afford to live in big cities, but there are typically small towns in the general vicinity of rural areas that are quite affordable.Of course, there are exceptions where you truly need the space, like if you're a farmer, but that's not most people in rural areas.Edit: to be clear, I don't think it's fundamentally wrong or anything for people to choose the rural lifestyle, I just don't think we should be heavily subsidizing it.

reply

wooger
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Being a farmer is also a lifestyle choice.

reply

devin
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Buddy, many of the people who are being served by Starlink are by no means "very" rural at all. If you get into "lives in a shack in the mountains", then sure I agree, but a HUGE number of people are barely outside of an immediate service area and have no access for one dumb reason or another. This is a demonstration of the failure of our country to do simple, pragmatic things that would benefit our citizens' lives. The "fix" was for some private company to launch things into orbit. It's an expensive fix to a simple problem.

reply

shagie
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

My parents have Starlink. They live in an area surrounded by dairy farms. It's half a mile between mailboxes. The nearest town is 7 miles away (though only 3 as the crow flies - lots of hills between here and there).

None of the neighbors have cable TV. You've got to either go into town or t'wards the highway 7 miles the other direction).Three years ago, the utility ran natural gas that far out. Prior to that, it was propane tanks (for the past 50 years) for heat in the winter.The state capital is 30 miles away... so its notthatfar away from civilization (this isn't Montana or the north woods of the upper midwest).When nano-cells came out for cellphones my father and I were the first in line at the store (that was 2010 if I recall correctly). It let the house be able to use a cell phone in the yard - before that it was the landline (and it was DSL for the nano-cell backhaul).In 2020 when school was remote, their grandkids were there. Prior to Starlink my father got a Firewalla (for network load balancing) and got a second DSL link (it was barely qualifying as high speed internet) so that it could support two zoom calls simultaneously (don't stream music or watch YouTube while the kids are on Zoom School).5G cell coverage sounds great... but those hills I mentioned earlier? Youcanget cell phone coverage at the house without the nano-cell... if you get a ladder out and climb up to the top of the roof.So yes, to support the person I'm replying to - there are alotof people who are 30 minutes outside of a city of appreciable size and are without wired high speed internet.Inhttps://broadbandmap.fcc.gov/location-summary/fixed?version=...the area that they live in has 0% for 100 Mbps for the majority of the northwest part of the county.

reply

grahamburger
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Looks like they may be getting fiber from Bertram Communications soon:

https://maps.psc.wi.gov/portal/apps/experiencebuilder/experi...That or Starlink may be getting a wad of cash just to keep serving them, courtesy of this administration's NTIA.

reply

shagie
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The area south of Highway 19 in Dane County to north of Highway 39 in Green county is still rather bare of awards.

reply

TulliusCicero
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Generally speaking, private companies want to make money by getting customers. Obviously there can be edge cases, but if there's profit to be made by hooking people up, they'll want to do it, and if private companies 
don't
 want to get more customers, you have to ask yourself some hard questions about why.

I think we both know what's usually happening: people in an area who, as a whole, are ruralenoughand poorenoughthat the economics don't really pen out well. And I'm sure said corporations would be happy for the local government to pay the cost of running those lines out -- if that's not happening, ask yourself why those local governments don't want to pay for it either.Now if you want to say, "well I don't care if it scales badly, the federal government should just subsidize it until it works", that's your prerogative. But another option would be to encourage zoning and similar rules that impact how people live to change towards better scaling of infrastructure and services, so that spending on these kinds of things is more sustainable and fair.

reply

sysguest
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

this

people here don't understand how large USA is -- connecting every corner with copper/fiber, with all the intermediary networking devices means tax money...

reply

devin
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, it does mean tax money. Stop corporate welfare and bump the corporate tax rate back to a reasonable value.

reply

nradov
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

A better option would be to eliminate corporate income tax entirely, and raise taxes on the highest income employees and investors to make the change revenue neutral. Corporations waste a lot of resources on financial engineering to minimize tax liability, and that's a pure deadweight loss for the economy as a whole.

reply

Tempest1981
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Savvy executives can also keep their income near 0 by borrowing against their stock holdings.

reply

nradov
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

So what. They pay interest on that loan, and those interest payments eventually flow to the employees and investors of the lender. Who can be taxed.

reply

heavyset_go
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

We paid $900 million in taxes to subsidize rural access to Starlink in one year lol

We also paid $42 billion in taxes for ISPs to roll out broadband access in a 2021 bill, and it hasn't connected a single person to the internetBefore that, we paid $400 billion to ISPs to do the same thing with the same results

reply

sysguest
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

wtf was this a upfront lump-sum money?

well even if I was the ISP, I'd just take the money and make the job "take forever"

reply

hattmall
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes, but we've already done it, twice, and the benefits were quite significant.

reply

dboreham
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Generally agree. I live in a location that had (still has?) PSTN service, electricity, and natural gas services, but never got any kind of broadband besides the network I paid for and deployed myself, and subsequently of course StarLink.
I think the issue isn't so much that people are demanding internet service in
random places, more they're expecting internet service in the places you get all the other regular services.

reply

edgyquant
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I don’t think we should subsidize internet, but your framing here rubs me the wrong way. People in these rural areas usually live among family and have lived there for generations, reducing this to a choice feels very elitist. People aren’t “choosing” to not pack up their entire lives and move to a city or town.

reply

platevoltage
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

We shouldn't subsidize internet, it should be provided. The internet is necessary to participate in modern society, and to only provide it to people who can afford it is what's actually elitist.

reply

iknowstuff
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Last we checked we pay for water too. It’s abundant. It still makes sense to have a price on it because it’s a resource like anything else.

In the same way, we pay for the internet. Free wifi exists if you can’t afford service.Rather than elitist, it’s just… not communist.

reply

strbean
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I think this is very short-sighted, on the order of "Why should we subsidize package / letter delivery to people in the sticks?"

The economic benefit of making those people available as consumers, lowering barriers to their engagement in markets, is enormous and certainly pays for itself.

reply

wooger
 
56 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Dubious when you consider how few people this is.

reply

TulliusCicero
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> "Why should we subsidize package / letter delivery to people in the sticks?"

Good point, it doesn't make much sense to do that either.> The economic benefit of making those people available as consumers, lowering barriers to their engagement in markets, is enormous and certainly pays for itself.Or, we could zone areas to encourage people to live in towns where it's feasible for both corporations and the government to provide infrastructure and services at a reasonable cost.

reply

strbean
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Or, we could zone areas to encourage people to live in towns where it's feasible for both corporations and the government to provide infrastructure and services at a reasonable cost.

This is assuming there isn't a good reason why we might want some percentage of the population to be rural. To have farms and ranches, for example.

reply

TulliusCicero
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Sure, if we restrict the subsidy to farmers and others where we need them to live in rural areas, that's fine.

reply

strbean
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But not the educators teaching the farmer's kids, or the doctors and nurses treating their wounds? What about the clerks at the grocery store serving those farmers? The liquor store?

Trying to create an elaborate regulatory regime to decide who is justified to live in a rural area is absurd and a waste of money. Especially considering that most people living in rural areas are either employed in a necessary industry that needs to be rural, or work in professional or service industries either directly supporting said rural industry (e.g. tractor repair) or indirectly supporting it's workforce.Furthermore, the marginal cost of providing broadband to all those "slightly-less-necessarily-rural" people is minuscule. Skipping every other house doesn't save you much when the majority of the cost is building infra to get broadband to the town/road in the first place.

reply

iknowstuff
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Farmers and ranches don’t need any more incentive to live there on top of the boatload of money they make selling their produce

reply

throw__away7391
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The situation with the electric grid is pretty crazy. The cost to supply power to houses in sparsely populated communities is orders of magnitude higher than urban apartments. Not just the power infrastructure itself but all sorts of little ongoing things like maintenance visits, as well as losses from transmission and distribution. I worked on smart grid systems and getting apartment buildings online was a piece of cake, with one simple connection handling multiple buildings with hundreds of meters, meanwhile suburban homes required much more expensive equipment that was more difficult for technicians to install and serviced only a handful of homes. Everyone talks about this as if these were humble shacks out in the boonies but the bulk of these service points are suburban McMansions built on cheap land at the margins of the cities. Broadly speaking this results is poorer ratepayers significantly subsidizing services for wealthier ones.

reply

jasonwatkinspdx
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Unironically: go move to Somalia if that's the government you want.

The rest of us understand that's utter stupidity, natural monopolies exist, and capitalism needs guard rails.

reply

TulliusCicero
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I'm a social democrat, I'm fine with subsidies in general, I just want them to be applied intelligently. Spending a lot of money to subsidize someone's lifestyle that's intentionally inefficient isn't smart.

I'm all for helping the poor, but we should do it in a way that gets us a lot of bang for the buck.

reply

wooger
 
53 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They're not 'the poor' though. If you own a $20 million of land why is everyone rich and poor in the city paying a dollar to fund your faster internet?

reply

jasonwatkinspdx
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Having grown up in rural Kansas and now being an urban tech worker, I think you have a derogatory and ignorant view on people who live rurally.

reply

raw_anon_1111
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes all of the farmers should move to the cities.

reply

renewiltord
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

No, it is not at all certain that it pays for itself. What evidence do you have for that assertion?

reply

poulsbohemian
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

>It’s not clear to me that we should necessarily massively subsidize their choice to live in the sticks these days.

Last year I had a chance to talk to Gregg Coburn, author of Homelessness is a Housing Problem. We agreed that remote work and improved public transportation were therealsolutions to many of our housing problems, allowing greater distribution of population back into more rural areas. This is an area where rural broadband investment could make a difference. Likewise, when we talk about American competitiveness in manufacturing et al, that isn't going to happen in our cities, but rather in more rural areas.

reply

hombre_fatal
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Decentralizing population seems at odds with goals like better public transport and infrastructure.

reply

mikkupikku
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You think cities exist for the sake of buses, and not the other way around?

reply

pbh101
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Who said those two were the ultimate goals to work towards?

reply

performative
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

other
 than introducing public policy to encourage building more housing, i assume?

reply

poulsbohemian
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The problem is that in places like Seattle and the Bay Area, there are hard geographic limits to construction, even if you turn them into endless high-rises. Having watched the WA state legislature go through several years of attempts to fix housing by throwing random policy ideas into the void, I'm not convinced any of it matters nearly as much as a) more money in the state housing trust to help people with down payments and b) a robust economy so more people have more money that they can apply toward housing.

So, sure, yes, by all means do things like pass residential-in-repurposed commercial changes, ADUs, greater density in transit-oriented neighborhoods - do all the things. But, getting more peopleableto move to parts of the state (in my case, Yakima, the Tri-Cities, Spokane, etc) where there are houses just sitting around relative to King / Pierce / Snohomish... that's just as viable a solution and solves a whole bunch of other water / energy / land use / political / social type problems.

reply

derektank
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

>The problem is that in places like Seattle and the Bay Area, there are hard geographic limits to construction, even if you turn them into endless high-rises

Over three quarters of all residential land in Seattle is zoned single family and the population density of the city is less than a third that of NYC. The geography is not the hard constraint in this city.

reply

nradov
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Subsidizing down payments doesn't do anything to improve housing availability or affordability in the long run. It just artificially inflates real estate values and acts as a wealth transfer from taxpayers to property owners.

reply

hombre_fatal
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You offer cities with aggressive anti-development regulations, like max height restrictions, and then suggest things would be the same if they instead had endless high-rises?

Sounds like you've found an infinite-value hack: let developers build infinite housing yet prices stay the same.How many of those "random policy ideas into the void" were to lift regulations to allow people to build housing? Which sounds a hell of a lot simpler than figuring out how to make everyone wealthier without proportional increases in market prices.

reply

scubbo
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

People can't afford to live in cities? Well, they should simply choose to live elsewhere.

People choose to live outside cities, but want access to basic utilities of modern life? Well, fuck 'em.

reply

vineyardmike
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Many of the aspects of life "outside the city" are subsidized by the city. It's affordable because of this, and the cities are extra unaffordable as a result.

There are many small towns who will never generate the tax revenue to cover their $50M highway off-ramp and associated infrastructure. The thread was about internet, which has also been subsidized. We subside oil so driving long distances is cheaper. We subsidize food production. Electricity and water distribution is subsidized by urban customers. Even health care is subsidized.If rural people actually had to pay market-rate for these resources, it wouldn't be cheaper than the city.

reply

gib444
 
48 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

So if 10 million people from rural towns moved to their nearest cities, the cities would become cheaper?

What would drop in price exactly?

reply

TulliusCicero
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Small towns exist, and ones far away from major metro areas are usually quite affordable.

Small towns are or can be made to be efficient in terms of basic infrastructure/services, whereas truly rural areas where everyone is very spread out, it's somewhere between difficult and impossible to do that.

reply

kbar13
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

that’s a bit pendantic, there exists such a thing as suburbs. even some rural communities are perfectly reasonable in terms of municipal infrastructure. but we are specifically talking about houses that are miles and miles from the next house that is then miles and miles away etc

reply

TulliusCicero
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Even in "rural regions", there are typically some small towns where infrastructure could be provided to them decently efficiently. It's when every single house is a good distance away from their neighbors that things like running fiber cabling become grossly inefficient.

reply

aaaaaaabbbbbb
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Ah yes, one step outside of New York City, and I'm immediately in the boondocks.

reply

galleywest200
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Moving is incredibly expensive. First+Last month rent up-front, plus a deposit equal to one month rent up-front. That could total around $10,000 up-front costs if you are targeting a major city.

Conversely, having quality utilities in smaller communities could incentivize the building up of those areas and they would become less rural.

reply

nailer
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

lol I paid 17K for NYC - two months rent, extra month for being foreign, 2K since they removed blinds since they showed me the apartment and everyone in NYC could see into my house.

reply

hdgvhicv
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If you’re on the electric grid why can’t you be on a fibre grid.

reply

sysguest
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

well for electric grid, you only need "local" connections -- eg. just your town and the generator...

reply

raw_anon_1111
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Who needs all of the damn farmers anyway?

reply

platevoltage
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The corporations buying up all of the land formerly owned by these bankrupt farmers probably do.

reply

jjmarr
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Countries subsidize rural living because it enforces their control over the frontier.

The United States is difficult to invade because of the oceans surrounding it and the many people with guns in the interior that'll take shots at armies.If you put everyone in a few cities on the coast, the USA becomes easier to invade.

reply

pibaker
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No country capable of landing a single troop on the lower 48 is scared of undisciplined men with AR-15s.

In fact I am not sure if any country can get a troop transport near the US coast without being nuked to the ground first.

reply

jjmarr
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In the 1930s and 1940s, Mexico wanted to invade Texas and reverse the Mexican American war.

reply

pibaker
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I can't find any source suggesting this was actually a thing in the 30s and 40s. All I can find is the Zimmerman telegram from a hundred years ago which the Mexicans weren't exactly enthusiastic about.

In any case, I doubt there is any realistic threat of a Mexican invasion beyond fantasizing from political fringes.

reply

GMoromisato
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I don't think the math works.

There are 23 million rural homes in the US and about 3 million miles of rural public roads. Let's say you wired just the public rural roads (ignore going from the road to the house).It costs $30,000 per mile to put up aerial wiring. $60,000 per mile underground. So we're already at $90 billion for wired poles and $180 billion for underground. And that's just for the wires--we're not including any of the switches and routers for actual internet.By comparison, the Starlink system cost about an order of magnitude less ($10 billion).

reply

Tempest1981
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Doesn't Starlink have some annual upkeep costs? Maybe $1-2 billion per year to replace aging satellites?

reply

panick21_
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, but Starlink needs to exist for military, planes, boats and other essential very rural services as well. So the upkeep should pay for itself.

And of course Starlink has to be for the whole planet, so just comparing it to the US would be a false analysis.Of course you also need to upkeep the physical infrastructure. Specially if you don't put all those lines underground.But one would need to do some more real work to compare. I would also say that a real program for urban fiber makes a lot of sense in more places. But I would love to see somebody take a shot at this, what would be the best if you started from 0 today?

reply

devin
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I appreciate you actually taking a moment to think through the cost, but I think we could start with some pragmatism and look to run wires to people who are within a reasonable range of existing systems, of which there are many.

Clearly not every public road needs wiring. Then, consider that you could run wired connections to wireless access points to increase high speed wireless coverage. 1 wire to light up dozens of homes in areas which currently have no service beyond DSL.

reply

bogdan
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Would 5G towers be a better alternative?

reply

protocolture
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

>I've written it elsewhere, but: it is such a shame that the United States saw fit to run electricity _everywhere_, no matter how rural your location, but instead of do the same for rural internet we had to wait for... a private company to launch a global network of satellites.

Actually whats crazy is that you guys had private and public power run everywhere, and those companies had private and public fibre companies run fibre through those power lead ins almost everywhere that's practical. A feat thats honestly not been achieved anywhere else that I have seen. Lots of people in other countries stomp around wondering why private fibre doesnt just materialise in their house, when they have no access to national public utilities. The answer was local utilities. But there's not even an ounce of appreciation for it outside of the ISP space.

reply

miki123211
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Internet still has a "moral vice" label associated with it that I don't think electricity ever had.

In the popular person's imagination, electricity is the revolutionary technology that enables cheap and safe lighting, as well as instant access to information (through radio). The telephone is the revolutionary technology that lets you call a doctor in an emergency or negotiate crop prices. The internet is the revolutionary technology that lets you go on dating sites and stare at pretty girls on HotOrNot, talk to fellow netizens on discussion forums, and waste hours playing Mmorpgs. It's "that weird technology that the young people use for God knows what." It's for entertainment, not serious business use, except if your business is in providing the entertainment.Of course none of it is true, especially these days as so much non-tech-adjacent business is happening over the internet (and especially internet-enabled smartphones).

reply

fy20
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Are there any countries that have actually done an exhaustive job of this? I'm from the UK, and I'd say they are pretty good, my parents live in a 300 person village, and they can get 50ish mbit internet through wires. But "rural" in the UK is very different from "rural" in some parts of the US. And this was done by a private company (although it was based on infrastructure built by the government).

reply

DaedalusII
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

its literally cheaper to create a low earth orbit satellite constellation than deal with bureaucracy

reply

tgma
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Let me guess, it would be a 512kbit/sec service.

reply

jasonwatkinspdx
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

The only way rural America got landline service was by the government forcing it. The market had no solution.

reply

raw_anon_1111
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Blame rural America who continuously votes for politicians who oppose it.

reply

moduspol
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Eh, I think we'll look back on this in 10-20 years and conclude that wireless transmission was always going to make more sense than running millions of miles of wires. Especially so for rural access.

reply

scottyah
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Wired will definitely be the rich, elite way to go.

reply

BurningFrog
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Satellite internet can get several orders of magnitudes more capacity.

reply

platevoltage
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Municipal internet is something the ISPs lobby against like there is no tomorrow. It is a shame, but that's how the US government works.

reply

gowld
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Why is wire better than terrestrial wireless? Isn't terrestrial wireless how most of Africa caught up to more earlier-developed regions in telecom?

reply

stevenhuang
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Your understanding of the history and economics of it all is very confused.

> simply running wiresLol. Yes let's just ignore the most expensive and complicated part of the whole endeavor.

reply

Hansenq
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Ben Thompson interviewed UA's CEO on Starlink a few months ago.

Scott said: "It took time to negotiate, because we wanted to own the consumer data, and at the beginning, Starlink did, so that was hard, and then, the other thing was I wanted to let my big competitors in the United States finish their deals with other providers and get locked in so that we would — eventually, everyone’s going to have Starlink."Brilliant. Just brilliant. Ensured that UA would be first (of the 3 major US carriers) to Starlink and that everyone else had to wait until their existing agreements multi-year expired before switching. UA's best CEO in decades!https://stratechery.com/2026/an-interview-with-united-ceo-sc...

reply

Nicholas_C
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

I'm surprised he would admit that publicly on a podcast.

reply

vl
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

After deal is done it becomes rational to describe how good it is in comparison to completion to promote it.

reply

moduspol
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's also possible that it's a post-facto rationalization that only seems prescient in hindsight.

reply

inemesitaffia
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

People like to brag

reply

moomoo11
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

He's signal maxxing so he gets a bigger bonus.

reply

gpt5
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

One nice thing about Starlink is that they force the airlines to offer it for free. I’m not sure why SpaceX is doing this, but it was surprising enough to me that my international WiFi was not only fast, but completely free that I researched it.

reply

jfoster
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

I think this approach gets the whole industry to adopt it.

Consider the opposite approach. If they let airlines charge any amount for it, the airlines that installed it would make it expensive. No one would use it. Other airlines would feel no pressure to offer it.By making it free, it gets used, and eventually depended upon. SpaceX are making free wifi the expectation from consumers on flights.

reply

stingraycharles
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Correct, I’ve had Starlink in several long haul flights over the past 6 months and it’s already becoming an expectation, ie makes the flights without it noticeably worse. I’m not sure whether everyone gets it for free, though, it was my understanding that it’s complementary for business class but a paid add on for economy. But once you have it, it’s fast and stable.

reply

SoKamil
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> I’m not sure why SpaceX is doing this

One word: marketing.

reply

nativeit
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

A few more words: they’re struggling to find a niche where their ungodly expensive product makes more sense than the readily available alternatives. In this case, fair play it’s objectively better.

reply

htx80nerd
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

>A few more words: they’re struggling to find a niche where their ungodly expensive product makes more sense than the readily available alternatives

pretty obvious you never worked for an ISP and forgot about all the `middle of nowhere` customers who have no high speed internet.even for me, in houston texas, we cant get fiber to the home and were stuck with AT&T DSL which was like $60 per month and ungodly slow. Also my GF and I both work from home and she does massive file uploads.had xfinity not been available starlink would be an easy choice. ive tried 5g hotspots and they are not super reliable.

reply

overfeed
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In all fairness, it was a qualified statement: "
readily available
 alternatives". That immediately disqualifies customers stuck in the boonies, or a few hundred feet away from service coverage.

reply

Wyverald
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Just noting that the phrasing "readily available alternatives" by itself is slightly ambiguous: it could be read as subsetting ("the alternatives that are readily available") or just attributive ("the alternatives, which are readily available").

reply

mattmaroon
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

He has readily available alternatives, but they suck.

There are other, far worse forms of satellite Internet, so everybody has a readily available alternative. That makes it not a qualifying statement at all.

reply

nativeit
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I apologize for the initial ambiguous snippy comment.

I'm an I.T. consultant in N. Carolina, and I've worked in very rural areas setting up connectivity for farms. Indeed, I have recommended StarLink on at least two occasions, albeit in concert with 4G/5G cellular (bad weather remains a problem). StarLink sounds great for airlines, RV's, boats, base camps, disaster relief--but those are almost all examples where affordability aren't usually high priorities, and I'm not sure if it's significantly better than upgrading geostationary satellite tech.I do firmly believe that StarLink is, at best, a flawed solution to the largely solvable problem in the context of rural broadband access. We very recently had federal programs and funding to advance cable/fiber rural broadband services, but it was so weighed down with bureaucratic cruft that basically nothing got done. I dunno if that specific provision of Biden's infrastructure bill remains law, but I'm pretty sure it ceased being a priority after the last election (not for nothing, StarLink had plenty to gain by those federal programs dying, although I have no direct knowledge that Musk, DOGE, et al made any direct moves to stop it--I think it was mainly the shite implementation/execution by the Biden administration).So "readily available" in the sense of "we could do it at any time, and it would be a helluva lot cheaper and more durable than continuously launching hundreds of satellites into LEO". Poor choice of words on my part, and even still I'm sure there's still plenty to disagree with there.

reply

kdkdkrjrj
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

To be fair: this is an america regulatory capture problem.

reply

nradov
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Regulatory capture is only a secondary reason why many parts of the USA still lack cheap, reliable broadband Internet access. It turns out that running fiber everywhere is expensive, and in some areas the potential customer base doesn't justify the cost.

reply

rconti
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It doesn't justify the cost when they can just rip you off, charging the same amount for a fraction of the bandwidth.. unless and until there's competition.

Funny how quickly my internet options went from expensive cable internet, to 1 gig symmetric fiber for $90, to 10 gig symmetric fiber for $50. And now, magically, Xfinity has 1Gbps+ service for $50 as well.

reply

ghaff
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I most certainly don’t have 1 Gps+ service for $50 though in practice my circa 50-100 Mps service for about twice that works fine does for me from Xfinity. I care a lot more about reliability.

reply

parineum
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> It doesn't justify the cost when they can just rip you off, charging the same amount for a fraction of the bandwidth...

You can start a company right now and lay fiber in these places and start your own telecom.You probably don't have the money for that but, if you put together a solid business plan, a bank would give you a loan.You may not have the experience or expertise to do that, but there are plenty of people who do.Why hasn't that happened yet? It turns out that laying down miles of fiber for a handful of customers isn't profitable.Google dod it in a few places that were low hanging fruit. Places that had telephone poles where they could get relatively easy access to them.There are certainly places where access to those poles is more difficult than it should be but most places are hampered by either being too remote to justify the cost of burying lines to a few customers (rural areas) or the digging is too expensive to many customers (suburban areas) because they'd be digging up streets.

reply

rconti
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Profitable vs unprofitable is not black and white. No doubt there are some places where it's simply not profitable to run the fiber today.

However, there are a TON of places where the business strategy you outline is a great idea, and would be profitable...... until the incumbents lower their outrageous prices in the face of the competition, and bam, now your business model is no longer profitable.

reply

nativeit
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

We do a lot of things that require subsidizing, very much including the things commonly found in/around a lot of the rural farms where these services would target. If broadband internet access is a fundamental need for contemporary communication--much like the postal service, telegraph, and telephones were--then historically we do what's necessary to provide them.

reply

nradov
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Sure, subsidies are potentially an option to increase broadband availability. But that's not really a regulatory capture issue.

reply

FireBeyond
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yeah, a primary reason would include "spineless legislators who allowed carriers to say "We'd need tens of billions of subsidies to even consider doing this", and then when given that money to do so, just... largely didn't. And kept cruising without consequence (and with the money).

reply

tayo42
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You couldn't get cable internet in Houston?

reply

mediaman
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's not that expensive. The Starlink Mini is around $200, and service is $50/mo for 100gb.

I've been somewhat skeptical of the addressable market (doesn't fiber + cell tower network offer good enough coverage?) but I know so many people who have put it on their RV, their boat, or are using it rurally that I've started changing my mind. And the service really is better than cell phone networks, which are far too patchy to provide reliable service at decent speed.And you can put it on standby mode for $5/mo, so you're not even really locked into $50/mo if you're occasionally doing travel where you want to stay connected.And in places like Africa, they've had to tightly rate limit new customers because demand is so high.

reply

mattmaroon
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah, as an RVer, I can tell you that you would probably be surprised by how much of the country does not have readily available cell service. And even if it does, they might not have it on your network.

I was paying more to have SIM cards for all of the big three, and getting much less out of it

reply

sangel21
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Australia we just turned 3G off now there are large black spots everywhere for hours.

Some trades now use them in there cars, they can use it for mobile service/internet nearly anywhere

reply

infinitewars
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

RV is a great use case but a tiny market. For fixed broadband the others are cheaper most everywhere in the U.S. 
that people actually live
.

reply

panick21_
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The markets are additive. The great thing about Starlink is that it is GLOBAL. Meaning if you want to offer it for ships and planes (where there are no alternatives) you might as well also offer it to RV. And to rural people. And to the military. And you can do so in every country on the whole planet at the same time.

Having a few 1000s of sats to cover the whole planet is crazy efficient.

reply

uyzstvqs
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Residential prices:

100 Mbps down / 15-35 Mbps up, unlimited data, includes hardware rental: €29/month in Europe, $39/month in the US.200 Mbps down / 15-35 Mbps up, unlimited data, includes hardware rental: €49/month in Europe, $69/month in the US.400+ Mbps down / 20-40 Mbps up (QoS higher priority), unlimited data, includes hardware rental: €69/month in Europe, $109/month in the US.A good high-speed fiber connection is obviously better quality and value; but if you don't have one, then Starlink is absolutely the most competitive option you're going to get.

reply

dadoum
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I don't have a lot of data points, but in metropolitan France at least I think you would always be better off with either a fiber or a 5G subscription, because it will be cheaper for more throughput, and because fiber is very widespread.

In Germany I think you are still better off with a cable subscription which also seems to be widespread in my experience and is cheaper than Starlink even if it's not as good as French deals (I only take in account offers without a contract for fairness, but if you don't mind you may be able to get even cheaper offers).

reply

lurkingllama
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

In the (relatively) rural area that I live in, the only ISP options available were something like $75/mo for 10mbsp speeds. Starlink was an incredible blessing when it became available. Legitimately feels like magic in comparison to the existing options we had.

reply

lxgr
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> their ungodly expensive product

Do you have any idea how much other satellite operators charge per megabyte or Mbit/s?

reply

victorbjorklund
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Their competitors isn’t other satellite in most cases. It’s fiber, 5G and so on.

reply

sangel21
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's cheaper then fibre here in Australia. Especially rural.

reply

victorbjorklund
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Wow that sucks that Starlink is cheaper than Fiber at the same speed.

reply

nostromo
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Starlink isn't expensive by those standards either.

reply

victorbjorklund
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Probably depends where. It is for sure more expensive than fiber with the same speed where I live.

reply

infinitewars
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Starlink's main goal isn't consumer internet, it's being the backbone for Golden Dome

https://en.wikipedia.org/wiki/Golden_Dome_(missile_defense_s...

reply

DarmokJalad1701
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Of course that's terrifying...

Why would you be "terrified" of space-based ballistic missile defense? Seems a lot better than ground-based interceptors that have a not-great rate of interception.

reply

infinitewars
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

For trillions of dollars, Golden Dome is unlikely to be effective at interception, but it destabilizes MAD and can be used as a global prompt strike offense weapon.

So, worth it?

reply

panick21_
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Man this dumb conspiracy again ...

reply

mattmaroon
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

They have several niches where the alternatives are more expensive and worse. Half the RVers in any park have it now. RVing teaches you how much of the country is not covered by cell signal. Boats.

Another one I know first hand: food trucks. I do several events a year where cell signals get overwhelmed and cease to function, but I still have to process my credit cards. I’d say a solid 25% of food trucks are running these now.

reply

wat10000
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

$39/month for 100Mbps in the middle of nowhere is spectacularly cheap.

reply

inemesitaffia
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Starlink costs around the same as business mobile Internet.

Or see T-Mobile away

reply

bs7280
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

United gives you free access only if you are a mileageplus member I think?

Regardless, having free high speed internet on a flight will motivate me as a consumer every time.

reply

theultdev
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Joining United MileagePlus is completely free, you just sign up.

About the same work as filling out a hotel wifi login.

reply

kevincox
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Completely free as in you don't have to give them money.

But you need to give personal information which also has value.

reply

schmookeeg
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

More personal information than you provide them to purchase the ticket to use the free starlink?

reply

tjoff
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Regardless one of the conditions surely is giving them permissions to sell this to starlink as and everyone else. So whether the information is the same is probably irrelevant, how they are using it is.

reply

kevincox
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Probably, because you are now associating your internet browsing with your personal information. (I don't know if they have the sophistication to actually do this, but it is very possible.)

reply

theultdev
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The people concerned with that hypothetical can use a VPN.

At most they could see domains, ip addresses, timestamps, and http-only sites (are there any left?)But the person sitting next to you can see everything.

reply

LoganDark
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> But the person sitting next to you can see everything.

Privacy filters are a thing.

reply

raw_anon_1111
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You realize you have to give them the same informaron to even step foot on the plane?

reply

altacc
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Free (for now). Introducing or raising costs for a previously free or cheap service is normal practice for start ups.

reply

raw_anon_1111
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Delta has had free high speed satellite internet for years. I’m going to start flying Southwest more this year but they also advertise free internet. I don’t know how fast it is.

reply

ddoolin
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Really ironic given that they pulled the rug on general aviation usage.

reply

briandw
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It’s too difficult to distinguish between a terminal in small GA aircraft and something with destructive payload. Commercial aircraft are few and controllable.

reply

bpodgursky
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Nobody wants their brand associated with price gouging and half-broken in-flight credit card payment portals, and Starlink is better enough than any alternative that they can play hardball with airlines.

reply

oceanplexian
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Delta is still stubbornly refusing to adopt Starlink.

I've got status with them and have started booking with other airlines b/c it doesn't matter how nice the seats are if you can't get any work done. Most airline revenue comes from business flights, I don't think they realize how important this is to their customer base.

reply

ghaff
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Airplanes are one of the places I feel happily disconnected from being online. Never used in-flight WiFi even when my company would have paid for it.

reply

scottyah
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's probably what the UA CEO was talking about, trying to get competitors to sign contracts with other providers. Viasat was hot stuff for a long time, wouldn't be surprised if there's a noncompete preventing the change.

reply

raw_anon_1111
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Delta has had high speed internet for years on their flights. I’m Platinum Medallion

reply

thinkling
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Delta uses Viasat and has been rolling out free wi-fi on more and more of their planes. Is it not usable?

reply

lxgr
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It’s pretty good, but the latency is inherently high since Viasat is in GEO.

reply

spullara
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

~600ms ping times vs ~40ms on Starlink

reply

inemesitaffia
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Starlink failed it's Delta Demo.

The article is online.

reply

supertrope
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It could just be the ESPN/gym membership/AAA business model. $ from every single passenger is more revenue than $$ from just those who click buy.

reply

light_hue_1
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> Nobody wants their brand associated with price gouging and half-broken in-flight credit card payment portals

The airlines have no problem with this. T-mobile has no problem with it either.

reply

unsupp0rted
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Nobody had a problem with flip phones that play snake or Blackberry physical keyboards until the iPhone was demonstrated, and then nobody could conceive of ever going back (except in niche cases, e.g. journalists loved those keyboards)

reply

SR2Z
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

T-Mobile also offers free Wifi on airplanes.

reply

raw_anon_1111
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Only if the airplane uses much slower ground based Gogo (?). I use it every now and then when taking the 45 minute flight from ATL to my parents home in South GA

reply

sangel21
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Most of the airlines I have been on charge per megabyte. Having internet for the whole trip is a huge value add for the airline.

reply

nelox
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

And show ads for it on the inflight entertainment

reply

technothrasher
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The built in entertainment systems are so full of ads, that I much prefer the planes with no seat back screens. I've always already got my own devices which I use to entertain myself, whether the airline is providing advertainment or not.

reply

mh-
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

And no one interrupts the movie I fell asleep watching on my iPad in order to push a credit card application at max PA volume.

reply

mandeepj
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> One nice thing about Starlink is that they force the airlines to offer it for free

There are many ways to circumvent that, even while claiming to offer it for free.

reply

kotaKat
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

On the flip side, the "private" aviation customer is 100% forced into the pricey plans privately with (physical) speed enforcement on the terminals.

There's even twotiersof aviation speed limting: 300MPH ($250/mo) and 450MPH ($1000/mo). They know who they're targeting at both speed points (the guy flying for fun in a prop VS the guy in a Gulfstream that wants to Get There Now).https://starlink.com/support/article/9839230e-dc08-21e6-a94d...

reply

ryandrake
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

What sucks is that normal "for fun" prop pilots 
used to
 be able to use the basic $50 roaming plan, and then Starlink pulled the rug out from under them by taking it away, instead offering the new plan 5X the cost with 1/5 the bandwidth limit. Total scumbags. Even your hated local cable company doesn't have the balls to 5X your monthly bill suddenly out of the blue.

reply

tonymet
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

give the customers the complete experience and they will subscribe.

IF carriers were allowed to charge, they would piecemeal or handicap the service, and passengers would leave with a bad impression.

reply

p0w3n3d
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

For God's sake you can take 2-4 hours of not working, right? Just sit and relax, or take an audiobook with you! Or watch a cringy show from 90s. You don't have obligations of sharing #airplane #boeing #starlink #momwithbaby[kl]ickingmyseat every 5 minutes or so

reply

apitman
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've only had it once, but inflight Starlink is a game changer. I was able to play a ranked AoE2 game over the Pacific Ocean.

reply

TulliusCicero
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

That sounds somewhat unpleasant even if the connection itself is fine. How much space did you have for a mouse?

reply

batshit_beaver
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

He didn't say he won.

reply

apitman
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This

reply

LightBug1
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Did they even enjoy it though beyond the novelty!?

reply

darknavi
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Everyone wins when you can wololo with others on the internet at 30,000ft.

reply

apitman
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It depends on the airline, but sometimes I can put my laptop in weird positions that aren't half bad. The main technique is fully opening the screen, balancing the laptop on its lower edge, and using a Bluetooth mouse and keyboard. Has the added benefit of putting the screen closer to eye level.

reply

scottyah
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Hah, reminds me of learning to play Quake Live on my macbook trackpad. It was hard to go back to a mouse.

reply

sva_
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I guess not everyone flies economy (I do though, and not out of choice.)

reply

apitman
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I thought this was an AoE2 eco joke for a second

reply

throwaway132448
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

No internet on flights is one of my favourite features.

reply

fdghrtbrt
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Right. I don't know what I find more disturbing: that people are this addicted, or that they don't care. Either way, I'm with you.

reply

AndroTux
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

So let’s get rid of internet on the highway and in trains, too. Because it’s pretty much exactly the same thing. One just happens to be airborne.

reply

fdghrtbrt
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> So let’s get rid of internet on the highway and in trains, too. Because it’s pretty much exactly the same thing. One just happens to be airborne.

Ok? You sound like you're trying to make a point. Make a point.

reply

peab
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

his point is that it's useful, and there's nothing special about planes that make it important for them not to have internet, compared to any other mode of transportation. If you want to get away from the internet, you could have a dedicated space for that.

Also, nobody forces you to use the internet on a plane...

reply

fdghrtbrt
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, but why is he responding to me? I didn't say there was something special about planes and I didn't say someone was forcing me to use internet.

reply

pibaker
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> get rid of internet on the highway

Does not sound too bad once you have seen the number of drivers scrolling their phones while driving lately.

reply

raw_anon_1111
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Its cellphone based and has the same issues you would have just using your cellphone.

reply

deathanatos
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

… or maybe I have 6 hours to kill?

Would you look at someone reading a book and be like "it's so disturbing that people are this addicted"? Is something Internet connected really that different?(That said these days I'm thrilled if there ispoweron a flight.)

reply

fdghrtbrt
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It IS different. Because scrolling is effortless, reading a book takes effort.

Do you understand?

reply

bogdan
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

When am I allowed to relax boss?

reply

panick21_
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Maybe you don't know this, but there is much more on the internet then social media ...

reply

jryle70
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I suppose you'd approve if I read book on the internet? What if I'd be working?

reply

fdghrtbrt
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You don't need my approval. Someone was asking how I view these things, and I was explaining: reading a book is effort, scrolling facebook is effortless.

Now, keeping in mind that you don't need my approval: do you have any questions?

reply

bogdan
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Are you on the spectrum by any chance?

reply

fdghrtbrt
 
29 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, but I understand why you ask. I just refuse to engage with certain figures of speech because that would legitimize them. Don't say "would you approve if" if that's not what you mean. Say "what is your opinion on" or "what's your view on" or "how do you think about" or "how does that compare to" because that's what you actually mean. I'm not on the spectrum, but I think that when it comes to many things, language included, simpler is better. As simple as possible, but not simpler.

reply

rjh29
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

For normal people the presence of wifi on airplanes is not a problem; they can simply not use it. It's not a threat to them.

I use the internet more than I'd like, and I agree that the lack of wifi (on a long international flight) can be a really nice experience.

reply

rayiner
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I tried Starlink on a United flight the other day (short hop from Hilton Head to DC) and it was amazing.

reply

ValentineC
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

As someone who's 
really
 not a fan of fElon (he made Twitter steal my OG username), it's nice to see people misuse the Starlink term, and I hope it would eventually be genericised [1]. ;)

The proper term should be Low Earth Orbit (LEO) satellites, and there are other providers like Amazon [2] and Panasonic Avionics [3] that I hope other airlines would do business with.[1]https://en.wikipedia.org/wiki/Generic_trademark[2]https://leo.amazon.com/[3]https://www.panasonic.aero/blog/blog-post/what-is-low-earth-...

reply

neilsharma425
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Neat problem to work on. The tail number lookup is the hard part and it sounds like you solved it the right way, by finding the people who actually track this obsessively rather than trying to scrape it yourself.

Two questions: how stale does the tail assignment data get in practice, and do you have a way to detect when an enthusiast spreadsheet goes unmaintained? And what happens to your probability estimate when an airline swaps aircraft last minute, which seems to happen pretty often on regional routes?

reply

bblcla
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Great questions!

> how stale does the tail assignment data get in practice, and do you have a way to detect when an enthusiast spreadsheet goes unmaintained?These are updated almost every day so far, so they seem very up-to-date. Internally we track all changes/removals, so I'm not that worried about spreadsheets being abandoned yet. It's a good thought though.> And what happens to your probability estimate when an airline swaps aircraft last minute, which seems to happen pretty often on regional routes?Honestly our estimate right now is pretty crude. At the scale we're at right now it works, but I think you're right that we could make this more accurate by tracking equipment swaps & really drilling into the details of which aircraft get assigned to which routes.

reply

gadders
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I wish my bloody commuter train into London had Starlink. Even when the onboard wifi works you are limited to 100mb of traffic.

I get a better 5g signal on the Jubilee line than I do on an overground train.

reply

sva_
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

Just swap mac address if you have to use such a wifi. Or set up Xray[0] with the captive portal as domain if you have a VPS and are so inclined. Can also use this on locked down airplane wifi.

0.https://github.com/XTLS/Xray-core

reply

romarinhooo
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

can always macgyver your own antenna like this guy in Brazil 
https://tecnoblog.net/noticias/passageiro-causa-polemica-ao-...

reply

whalesalad
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Just get a good 5G plan? On the ground in a busy metropolis like London, I can't imagine why or how you would need to consider using satellite communication for connectivity. Then again the last time I was in London the cellular service was by and large pretty bad.

reply

davnicwil
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

yeah, 5g doesn't work on trains very well once just a little bit out of zone 2/3. Actually to be honest any connectivity at all is patchy.

reply

aeronaut80
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

The globe doesn't pan to some routes - perhaps ones that cross the international date line? - for example 
https://stardrift.ai/starlink/search?origin=AKL&dest=LAX&dep...

reply

Hansenq
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I've definitely thought about substituting a nonstop flight for a 1-stop flight on UA regional jets just to get Starlink on the entire route. The annoying this is I live by a UA hub and UA doesn't fly regional planes between UA hubs.

So the best I've been able to do is a regional flight to a UA hub near me, and then a non-regional flight back to my home airport. Which is honestly probably not worth it. And it's definitely not worth doing a two-stop trip so I'm really excited for them to roll it out on their mainline jets!

reply

bblcla
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

> The annoying this is I live by a UA hub and UA doesn't fly regional planes between UA hubs.

Oh I actually didn't know this! Do you know why?

reply

SR2Z
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Regional planes are for direct routes to smaller airports, but hub-to-hub flights can be filled up and easily justify larger airplanes.

reply

HorizonXP
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

This is awesome! I just came back from Cancun with my family, and I was on a WestJet flight. I was taken aback by a) free Wifi and b) how fast it was to support everyone streaming YouTube even. Your tracker let me figure out that it was a WestJet flight; now I know that I have to seek out these flights from now on.

reply

rootusrootus
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Well, hells bells, next week I'm actually going to be flying on an Alaska Airlines E175. That's quite rare for me, I can't remember the last time I've flown on one of their small planes. And it looks like 
all
 of their E175s have Starlink. Sweet! I may have to try it out, even if paying for WiFi on a short flight is generally a waste of money.

Edit: ooh, it's free! Because I have their credit card.

reply

bblcla
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

> And it looks like all of their E175s have Starlink

Not quite sorry, we only track the frames thatdohave Starlink. But if you check back a few days beforehand you can see if yours matches!

reply

rootusrootus
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Took me a second to parse that. It says 28 of 28 E175s have Starlink, but what I am hearing you say is that Alaska has more than 28 E175s.

Indeed, wikipedia says their fleet includes 47 E175s. Consider my hopes dashed :(. Oh well, I don't usually bother with wifi on flights that are only a few hours anyway, but free Starlink speed wifi would be fun!Feature request: Put a disclaimer on the fleet page that the tracking is limited. Or pull enough data to say "28 airframes of 47 are starlink capable" which is what I think most people will be looking to know in the fleet info.

reply

bblcla
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Feature request: Put a disclaimer on the fleet page that the tracking is limited. Or pull enough data to say "28 airframes of 47 are starlink capable" which is what I think most people will be looking to know in the fleet info.

Oh, this one is very doable and makes sense! We track this internally anyway so it's just a matter of surfacing it on the fleet information.

reply

torcete
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

People are so rude with their phones that I fear that starlink becomes popular in all flights.

reply

peab
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

United recently started announcing at the beginning of flights that using your phone with sound on the speaker is prohibited, as a new official policy.

reply

raw_anon_1111
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Talking on your phone has always been prohibited while in flight. Having high speed internet on a plane is not new.

reply

seneca
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I share your concern. Airlines seem to be anticipating this. There was a recent publicized incident of American Airlines removing a woman from a flight for playing audio over her phone speakers. United has similar policies. As I understand it, both are saying they will ban passengers over it.

reply

freelancedata
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

This matches what I've seen in the data. The correlation between niche specificity and close rate is much stronger than most people expect — generalists trying to compete on price lose even when they win.

reply

andrewcamel
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Big fan. One feature idea/request - a map showing coverage with 0-100% by route (red/yellow/green lines). I’m just curious to see where I should think to look for / expect starlink options. Probing into a few upcoming trips showed basically no coverage.

reply

bblcla
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Oh that's a cool idea! We wanted to do a variant of this, will add it to the list. The tricky part for us is getting a canonical list of 
all
 flights + body types on it.

reply

andrewcamel
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I’d imagine you could seed it more easily by focusing on top 50 routes by passenger count in domestic USA. Then go from flight schedules for top airlines into tail numbers into body types etc.

reply

whalesalad
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Would not having starlink on the flight influence your decision to take the trip

reply

martin_
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I built something similar[0] a while back, Stardrift looks 100x better - nice work!

[0] unitedstarlinktracker.com

reply

bblcla
 
4 hours ago
 
 | 
parent
 | 
next
 
[–]

hey! I saw this and liked it a lot! It’s impressive how you pull in all the routes per tail - we considered doing it but were worried it would be too expensive. Definitely opens up cool options though.

reply

raw_anon_1111
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Starlink is good I’m sure. But it isn’t the be all end all of high speed internet on planes. Delta doesn’t use Starlink and most of its planes have fast satellite internet except the A900s used for short hops.

reply

6thbit
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Why does it work on the plane?
are the constant handoffs between satellites not enough to break connections or cause extremely high packet loss for it to suck?

is there a speed at which it would break?

reply

disconcision
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

speed of plane is about 3% speed of satellite so i wouldn't expect handoffs to be much more frequent than with stationary receivers?

reply

6thbit
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I see, stationary receiver already has to deal with this and plane speed doesn’t add much to the equation cause satellites already go brr.

Honestly that wasn’t intuitive in my head but makes a lot of sense, thanks!

reply

Bombthecat
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

My trip from USA to Amsterdam doesn't have starlink, at all. Not a single plane. No matter the company.

So sad

reply

aeblyve
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

This is awesome! In the past I would use the promise of starlink or other LEO internet as a tiebreaker for booking flights and was disappointed a few times (as clearly not all of the airframes for an airline have the capability)

reply

userbinator
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Why the .ai domain? Are you using AI in your data pipeline somehow?

reply

nomilk
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

It would be great to make this data into a browser extension that overlays the info when using Google Flights

reply

dvno42
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

United has this on some flights. It's no cost but they force you watch ads in the captive portal. I'd rather pay the $8 and be left in peace, every time.

reply

theultdev
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Just an ad one time when you login? That seems fine.

I've never paid for hotel wifi and never will, but I don't mind an ad on the captive portal.

reply

HPsquared
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Looking forward to Starlink on UK trains. I frequently have to go basically without internet for a couple of hours.

reply

bspammer
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

I’ve been frustrated by this for years, you just know that if there was a mobile data deadzone on a motorway they’d fix it immediately.

Meanwhile on the train 30 miles from London, nothing.

reply

tombot
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Here’s a hack, get yourself a cheap eSIM data only plan from an alternative UK network (VOXI, Talkmobile etc) if you main network doesn’t have connectivity; they will!

reply

Doohickey-d
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There's even eSIMs specifically marketed as being a "backup" esim, with coverage on _all_ UK networks.

At least on my android, you could set the second esim as a "backup" that it would switch to for data if the main one lost connection (it took a few seconds, so it wasn't an "always connected" experience, probably because the phone wants to save power)Lots of options if you search for "esim UK all networks".

reply

FireBeyond
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I used to be a first responder with a Firstnet setup (not just the plan discount, but the actual black SIM card) that could roam AT&T to Verizon to TMO as needed, so was as close to universal connectivity as feasible. Though (probably relatedly) it was always 1-2 generations behind (many areas were still ATT LTE, maybe 5GE, when they were rolling out 5G).

And the clusterfuck when I tried to transition my account back to normal, where an $8 balance that wasn't reconciled triggered the suspension of my AT&T whole family account, but when I tried to pay, no-one in FirstNet support or AT&T could tell me how much to pay or where or my account number (and this is in the store), until a poor store and a poor phone CSR spent THREE HOURS getting it resolved. "I am literally trying to give you the money to take care of this." "We don't know where to have you pay that money to fix this."I was an early adopter, but FML.

reply

rjh29
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Or if your main sim is an eSIM, there seem to be 500GB/month business sims for effectively £2 a month online. You can't port your existing mobile phone number over, but it's fine for data.

I was introduced to it by another HN poster:https://www.hotukdeals.com/deals/three-500gb-preloaded-5g-da...

reply

caycep
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

looking back at the history of starlink, when was it decided to pursue this project at SpaceX? Was it always the natural evolution, i.e. cheap launches = more communications sats? Or was there a specific communications engineer/person that brought it up to Elon or Gwynne?

reply

phonon
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

SpaceX originally partnered with 
https://en.wikipedia.org/wiki/Greg_Wyler
 and 
https://en.wikipedia.org/wiki/Eutelsat_OneWeb
 in 2014, then they eventually went their separate ways.

https://x.com/greg_wyler/status/1116101020675977218

reply

inemesitaffia
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

https://en.wikipedia.org/wiki/Surrey_Satellite_Technology

You can clearly see the tech had an older history at SpaceX pre acquisition2004I believe they also signed up a teledesic exec Larry Williams around the same time

reply

bblcla
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm not actually sure myself, but I was really surprised to learn how profitable it is. SpaceX made $15b of revenue last year and $8b of profit. Starlink was 60-80% of that!

It turns out the demand for really good internet everywhere ishuge.

reply

infinitewars
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Absolutely false.

There were article claiming "$8b profit" but relabeling EBITDA as profit. EBITDA only tells you that Starlink makes money on a satellite once it is already in space and connected to a user. It deletes the cost of building the satellite, launching the satellite, the user equipment manufacturing, and just about all other substantial expenses. Not to mention payments servicing all their debt and Starship development.The fact a Starlink satellite only has a < 5 year lifetime and ~2 starlink sats burn up in the atmosphereevery single dayis entirely left out as well.They have never been profitable in any real sense. But that's okay, because their real goal is backed by Uncle Sam:https://wikipedia.org/wiki/Golden_Dome_(missile_defense_syst...

reply

infinitewars
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Starlink is based on the strategic defense initiative (SDI). Both reusable rockets (DC-X) and large satellite constellations (Brilliant Pebbles) were SDI inventions.

SpaceX was in fact founded with the architect of SDI:https://en.wikipedia.org/wiki/Michael_D._Griffinwho went from the CIA to become head of NASA and funded the early SpaceX (10x from what Musk himself put in!)Now in 2026, SpaceX is the frontrunner for the Golden Dome, which is an SDI reboot.The company was always about Wars not Mars.

reply

caycep
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

ah good to know....it seems this history is kinda scrubbed from at least a quick Google search of the company's history.

I do remember DC-X, mostly as when I was a kid, that program coincided with when the web became popular, and I remember (hopefully somewhat accurately) downloaded jpeg/gif files from NASA publicity releases of that rocket over my 2400 bps modem

reply

infinitewars
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Elon was downloading those same images with you ;)

reply

DarmokJalad1701
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> The company was always about Wars not Mars.

Such a cynical take! StarlinkmadeGolden Dome possible. It is easy to make up conspiracies post-hoc while forgetting that they were ridiculed when they announced it and the "experts" opined that it is impossible to do.> SpaceX was in fact founded with the architect of SDIThis is highly unfounded speculation. Griffin went to work for "In-Q-Tel" after SpaceX was already founded (as said in the link you cited). There is no evidence I could find that they ever invested in SpaceX.The existence of cheap launch and cheap satellites allowed the (at the time new) Space Force to pivot from large, expensive monolithic satellites to a "proliferated architecture" (https://en.wikipedia.org/wiki/Space_Development_Agency#Launc...) at a much lower cost.

reply

infinitewars
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It wasn't In-Q-Tel directly...

https://scheerpost.com/2025/02/11/the-pentagon-is-recruiting...https://web.archive.org/web/20241213051851/https://historyco...

reply

DarmokJalad1701
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yea .. so new that I have only worked in the industry for 5+ years now. Your link doesn't support anything you said.

What passage in that interview says anything about "In‑Q‑Tel invested in SpaceX" or "CIA funded SpaceX"?That interview is a NASA oral history of Mike Griffin’s career. It mentions his time at In‑Q‑Tel and later NASA, but it never says In‑Q‑Tel or the CIA funded SpaceX. You’re conflating "this guy once ran a CIA‑linked VC" with "he personally funneled CIA money into SpaceX," which simply isn't true. SpaceX’s early funding is well‑documented as Musk’s own money plus later NASA contracts as a customer, not a CIA equity round.SpaceX (and Kistler Aerospace, Orbital Sciences etc.) was awarded contracts for commercial transportation to the ISS [1]. NASA’s role was as an anchor customer and partner under a publicly described program to get cargo (and later crew) to ISS via commercial providers. NASA’s commercial cargo program and SpaceX’s contracts are not secret. They were openly competed and publicly announced. That's the opposite of clandestine CIA startup funding.DoD launch money for SpaceX (EELV/NSSL contracts, etc.) came much later, after Falcon 9 was flying and competing with ULA, and those are again launch service contracts, not "investment".> Trump admin took this link down off NASA's website but it's archived just before the transitionThat interview wasn't mysteriously "scrubbed". The website got updated and you found an old link that wasn't working anymore [2][3]. Not a conspiracy, just garden variety link rot.[1]https://en.wikipedia.org/wiki/Commercial_Orbital_Transportat...[2]https://www.nasa.gov/wp-content/uploads/2024/11/griffinmd-1-...[3]https://www.nasa.gov/history/history-publications-and-resour...

reply

infinitewars
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You just created the straw man argument about the CIA directly funding SpaceX. Not that simple. Read the articles.

reply

DarmokJalad1701
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> SpaceX was in fact founded with the architect of SDI

> Griffin who went from the CIA to become head of NASA and funded the early SpaceX (10x from what Musk himself put in!)Strawman eh? You pretty much claimed that Griffin funded SpaceX, and not just that, that he invested 10x as much as Musk.Now you go around editing your comments. Lol.It is not a strawman to say that what you said is non even nearly close to reality.

reply

Singlaw
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Damn that's so cool I just checked it and it works dayum how far we have come guys

reply

hughes
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I would love to see this integrated into Flighty.

reply

elAhmo
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

It would probably be locked behind a paid upgrade. Shame that so many features are locked behind a subscription model, and super annoying that they try to force the subscription 
every single time
 you open the app, sometimes more than once.

reply

SilentEditor
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

This is incredibly interesting, will follow.

reply

ellyagg
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Thank you for your service. Hopefully something like this can put pressure on airlines to understand how hostile their internet services are and that it matters.

Last year I flew roundtrip to the Philippines on Philippines Airlines. Each way they claimed they had internet and each time, they sent an email reneging the day before the flight.The same thing happened when my sister-in-law flew with them a couple months earlier.These are long flights during which I expected to be able to work. Just so infuriating.

reply

bblcla
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

That's frustrating. It's possible their link was down for some reason - airline maintenance issues happen all the time. :(

reply

LightBug1
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

Planes and underground trains are/were focus sanctuaries ...

reply

munk-a
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I had access to it on a long-haul AirFrance flight. While I avoid doom-scrolling in my daily life because there's better stuff to do... on a long haul flight it's a surprisingly good way to pass time intermittently. I still just watched pre-downloaded dropout for 80% of the flight but when I was too tired to appreciate it I'd turn my brain off and watch a bit of that wonderful doom-scroll slop.

The fact that it's powered by starlink is disappointing due purely to Elon Musk's involvement - but this is one of the better use cases for satellite internet technology. I'm not going to go out of my way to book with airlines that use the service though.

reply

elonisaass
 
16 hours ago
 
 | 
prev
 | 
next
 
[6 more]

[flagged]
carodgers
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Lots of examples of anti-Elon pols giving nazi salutes and no one cares. People are done pretending that your concerns are genuine. Move on.

reply

gambiting
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

>> People are done pretending that your concerns are genuine

I am absolutely not, and I refuse to spend any money on anything even remotely connected to Elon thanks to his actions. His nazi salutes go far beyond anything even vaguely acceptable in a public figure like him, as someone who lost family in the holocaust I don't find this "funny" or "a mistake" as some people put it. The other day someone was trying to convince me that it was some kind of heartfelt "from the heart" gesture - I've never seen someone so delusional.Feel free to stick fingers in your ears and cover your eyes and pretend that people don't care about this or that this wasn't a nazi salute - but Musk is exactly who he is, nothing more nothing less.

reply

elonisaass
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[2 more]

[flagged]
weirdmantis69
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Because your concern is not real. It wasn't a nazi salute period. You are seeing things. Get your eyes checked.

reply

drcongo
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

The fact that you're getting downvoted is a great example of why America is in the state it's in. Personally this tool looks like a useful way of booking a flight without financially funding the rise of fascism.

reply

weirdmantis69
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[2 more]

[flagged]
gambiting
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Who is Mamdani? You've got mayors somewhere doing nazi salutes? Where is that?

reply

accesspatchh
 
10 hours ago
 
 | 
prev
 | 
next
 
[2 more]

[flagged]
rogerrogerr
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

> Don't post generated comments or AI-edited comments. HN is for conversation between humans.

reply

adrithmetiqa
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Does anyone else appreciate the final space where we can be disconnected. I do, for one

reply

sva_
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

I love disconnecting while hiking in the forest/mountaineering or such. But being stuck in an economy seat for 8 hours as an 188cm guy while being in a low air pressure environment just isn't the place for me. I'll gladly take the distraction.

reply

umanwizard
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You can be disconnected wherever you want, with a bit of self control.

reply

halapro
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Always a catch.

reply

throwaway132448
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This misses the point. What’s nice is not that it’s just me, but that it’s everyone.

reply

lxgr
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Host a “phones off” party, go to a sauna, go for a hike with friends with self control etc., but please don’t hold me hostage (connectivity wise) in a cramped metal tube for your sense of nostalgia.

Planes are just about the least pleasant space to experience involuntary offline-ness. (That said, people scrolling reels with the speaker on (or the display at brightness levels making me consider sunscreen) should immediately go on the no-fly list.)

reply

throwaway132448
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Nobody is holding you hostage. Sounds like you need the timeout more than anyone.

And the assumption that this view was drawn from nostalgia is completely invalid.

reply

lxgr
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> What’s nice is not that it’s just me, but that it’s everyone.

This made it sound like you enjoymebeing offline, and that seems pretty selfish (as long as I don't annoy you somehow with my Internet connection, and on that, see my original comment).I'm a big fan of offline gatherings (ideally in nature, which is pretty much the opposite of economy class on many dimensions), but I think this should be a choice.

reply

throwaway132448
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I do enjoy you being offline. There’s nothing selfish about having different preferences to you. Selfish would be forcing those preferences on you. That you assumed one was the other is a good reason to reflect.

reply

rendang
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Consider paying a visit to one of these if you want to immerse yourself in the world of ideas and disengage from screens:

https://labri.org/My ~4 weeks were some of the most memorable of my life

reply

aeblyve
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Not really, personally... time waits for no one.

reply

throwaway132448
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

And now you’ll have one less opportunity not to waste your finite time on the internet.

reply

kleiba
 
15 hours ago
 
 | 
prev
 
[–]

Even when flying intercontinental for many hours, I usually just pull a Puddy on flights and do nothing. I have my laptop with me, of course, but I usually leave it just in the overhead compartment.

I don't even watch movies or read.

reply

Guidelines
 | 
FAQ
 | 
Lists
 | 
API
 | 
Security
 | 
Legal
 | 
Apply to YC
 | 
Contact

Search: