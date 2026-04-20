---
title: 'Tell HN: Anthropic no longer allowing Claude Code subscriptions to use OpenClaw | Hacker News'
url: https://news.ycombinator.com/item?id=47633396
site_name: hnrss
content_file: hnrss-tell-hn-anthropic-no-longer-allowing-claude-code-s
fetched_at: '2026-04-04T11:11:51.106013'
original_url: https://news.ycombinator.com/item?id=47633396
date: '2026-04-03'
description: 'Tell HN: Anthropic no longer allowing Claude Code subscriptions to use OpenClaw'
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
Tell HN: Anthropic no longer allowing Claude Code subscriptions to use OpenClaw
747 points
 by
firloop

12 hours ago

 |
hide
 |
past
 |
favorite
 |
588 comments
Received the following email from Anthropic:

Hi,Starting April 4 at 12pm PT / 8pm BST, you’ll no longer be able to use your Claude subscription limits for third-party harnesses including OpenClaw. You can still use them with your Claude account, but they will require extra usage, a pay-as-you-go option billed separately from your subscription.Your subscription still covers all Claude products, including Claude Code and Claude Cowork. To keep using third-party harnesses with your Claude login, turn on extra usage for your account. This will be enforced April 4 starting with OpenClaw, but this policy applies to all third-party harnesses and will be rolled out to more shortly (read more).To make the transition easier, we’re offering a one-time credit for extra usage equal to your monthly subscription price. Redeem your credit by April 17. We’re also introducing discounts when you pre-purchase bundles of extra usage (up to 30%).We’ve been working to manage demand across the board, but these tools put an outsized strain on our systems. Capacity is a resource we manage carefully and we need to prioritize our customers using our core products. You will receive another email from us tomorrow where you’ll have the ability to refund your subscription if you prefer.

 
help

jesse_dot_id

11 hours ago

 |
next

[–]

There seem to be a ton of people who don't understand how subscription services work. Every single one of them oversells their capacity. The power users that use the services a lot are subsidized by those who don't use it as much, which tends to be the vast majority of the user base. OpenClaw is an autonomous power user. The growing adoption of this walking attack surface was either going to A) cause the cost of Claude to go up or B) get banned to protect the price of the service for actual users.

reply

goosejuice

10 hours ago

 |
parent
 |
next

[–]

What you're saying is conceptually true for subscription services in general, but thats not why they are making this change. There's a 5 hour limit and a weekly limit. Those are hard token limits. Everyone on a plan pays for the max set of tokens in that plan. The limits manage capacity. The solution to that isn't a change of ToS, it's adjusting the limits.

In other words this is about Anthropic subsidizing their own tools to keep people on their platform. OpenClaw is just a good cover story for that. You can maximize plans just as easily w/ /loop. I do it all the time on max 20x. The agent consuming those tokens is irrelevant.For what it's worth I don't use OpenClaw and don't intend to, but I do use claude -p all the time.

reply

jmalicki

10 hours ago

 |
root
 |
parent
 |
next

[–]

You aren't paying to be using that limit all of the time.

You are paying to be using that limit some of the time. There are 5 hour windows when you are sleeping and can't use it. There are weekend limits.Theoretically you can max out every 5 hour window, but they lose money on that.It's structured so users can have bursts of unlimited usage, and spend ~15% of the theoretical max cap, and that's still cheaper than a subscription for that user.An OpenClaw user can use 6, 7, 8 times what a human subscriber is using.

reply

teekert

5 hours ago

 |
root
 |
parent
 |
next

[–]

I've met people that fill a box of sushi to take home at the end of their “all you can eat” session because “they paid for it”. Shrug.

reply

KeplerBoy

5 hours ago

 |
root
 |
parent
 |
next

[–]

Yes and the staff will tell them to stop that or charge them extra for it.

reply

teekert

4 hours ago

 |
root
 |
parent
 |
next

[–]

Yes and they will hide their sushi-grabbing because somewhere deep inside they know it's not part of the deal, while at the same time still strongly feeling that they have indeed paid for it.

Ah, to be human!

reply

abustamam

3 hours ago

 |
root
 |
parent
 |
next

[–]

I'd argue they hide their takeaway because of what GP comment said — not because of anything innate, but because a staff member will not let them.

I grew up in an Asian household of six. We definitely took food home at AYCE places. My parents definitely knew it wasn't OK, but they felt like they were gaming the system (like a dubious life hack of sorts) and saving money, so they were actually quite proud of it, bragging to friends how much they were able to get.To be human indeed!

reply

ohhman11

3 minutes ago

 |
root
 |
parent
 |
next

[–]

I assume it's not unusual for thieves to brag about their scores.
jhrmnn

4 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

The cooperative and competitive sides of our soul fighting it out in a single situation

reply

Alexzoofficial

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

Really

reply

daynthelife

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

> Theoretically you can max out every 5 hour window, but they lose money on that.

No, there is a weekly limit as well. Maxing out a single 5h window uses ~10% of the weekly limit

reply

MaxikCZ

5 hours ago

 |
root
 |
parent
 |
next

[–]

I fill my week limit in a few days :(

reply

KellyCriterion

3 hours ago

 |
root
 |
parent
 |
next

[–]

Do you do process XLS or similar data?
Ive seen using any other files than code files eats much more faster

reply

lherron

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

I think maybe you are not familiar with what /loop and the Claude cron tools do.

https://code.claude.com/docs/en/scheduled-tasks

reply

gregjw

6 hours ago

 |
root
 |
parent
 |
next

[–]

I need a hypothetical use case for things like this, I don't get how so many people have so much desire for use of features like this.

reply

goosejuice

4 hours ago

 |
root
 |
parent
 |
next

[–]

https://martinfowler.com/articles/harness-engineering.html
 it's being talked about everywhere.

If you manage developers or product folk, do you allow them to work when you're not looking over their shoulder? All developers can be managers/team leads now. You plan, you delegate, you review.You're welcome to not do this, surely that's appropriate in quite a few areas of work, but many of us are because we can get more work done than if we we're micromanaging every line of code change. For startups, where a bit of quality can suffer in favor of finding market fit, this is huge.

reply

vasco

4 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Every morning it summarizes a bunch of stuff for me, suggests me PRs to review, emails to reply to, freshly cloned any new repos, pulled all others, presents me with the suggested approaches to my PRs of that day, and gives me a list of my slack mentions that look more urgent.

This is just the morning ones, and saves shitloads of time of clicking around from tool to tool, freeing up time for the thinking and deciding.

reply

vichle

25 minutes ago

 |
root
 |
parent
 |
next

[–]

Wow, you should probably ask it to write a script for 90+% of that instead . Sounds like a huge waste of electricity.

reply

tomjen3

2 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Deduplicating/validating/processing incoming bug reports?

reply

kay_o

2 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> Theoretically you can max out every 5 hour window, but they lose money on that.

This typically results in a ban for TOS violations after a few windows in a row on a claude subscription

reply

sdoering

1 hour ago

 |
root
 |
parent
 |
next

[–]

I have maxed out my 5 hour limits and my weekly limits fairly regularly, when I did a bunch of editing work on long form writing next to having CC run a few coding tasks over the xmas holidys - I only slept a few hours at night an timed those roughly (by chance) with my limits.

I neither got a warning or a ban or anything - and that was with the double token amount during those days.So I don't see human usage being something they ban for TOS violation, like you describe. But as always YMMV.

reply

kay_o

47 minutes ago

 |
root
 |
parent
 |
next

[–]

Was this on a new (few months) or significantly older account?

reply

goosejuice

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

> Theoretically you can max out every 5 hour window, but they lose money on that.

Then it's not priced correctly. As I said, you can do all of this without OpenClaw.. claude code ships with everything you need to maximize the limits.

reply

Yokohiii

9 hours ago

 |
root
 |
parent
 |
next

[–]

It is priced incorrectly, but that is intentional. You can't create a tiered paid plan for the whole world that fits everyone. You can't create nuanced extra plans to satisfy all the outliers. It's an bet to keep the customers and still having a good margin.
Think of ecom, returns are a big struggle for any large company because they are unpredictable and subject to abuse, shipping fees are just an sophisticated guess to cover that cost. Not a subscription, same mechanics.
The only thing here to criticize is, if it's a good thing to make everything a subscription and disguise the real cost.

reply

fluoridation

8 hours ago

 |
root
 |
parent
 |
next

[–]

>You can't create a tiered paid plan for the whole world that fits everyone.

I mean, you can. Electricity is already sold that way. Subscribers with uncharacteristic usage spikes don't get blackouts, they get a slightly larger bill, and perhaps get moved up a tier.

reply

Yokohiii

8 hours ago

 |
root
 |
parent
 |
next

[–]

Very valid. My comment was fixated around the fact that big tech has the addiction to have subscriptions for everything. It's common that you provide generic subscription plans for the masses and supply "call us" custom plans for the specific (usually corporate) needs. If anthropic doesn't provide that or vibe coders are too cheap to do that, then those are issues, but the subscription models are itself valid. It is certainly misleading to a degree, but we've stopped complaining about this a while ago.

reply

fluoridation

8 hours ago

 |
root
 |
parent
 |
next

[–]

It's pretty stupid because as others in this thread have pointed out it's already not a flat plan. Even from their side it makes zero sense to bill things this way rather than based on usage. It's not like a VPS where your VM shares the hardware, which consumes electricity more or less regardless of what you use the machine for.

reply

Yokohiii

7 hours ago

 |
root
 |
parent
 |
next

[–]

Those yottabytes of VRAM are also consuming electricity constantly.

reply

fluoridation

7 hours ago

 |
root
 |
parent
 |
next

[–]

The difference being that an LLM request is not an operating system. Since they're compartmentalized and ephemeral, you can very easily distribute requests among your available hardware so that you can switch off machines during periods of low activity.

reply

jmalicki

7 hours ago

 |
root
 |
parent
 |
next

[–]

Your capital costs for buying those machines don't go away.

reply

fluoridation

7 hours ago

 |
root
 |
parent
 |
next

[–]

That's a problem that already exists in power generation and delivery, and it's already been solved. Bills are sums of fixed terms and variable terms.

reply

Yokohiii

5 hours ago

 |
root
 |
parent
 |
next

[–]

Custom payment schemes are late stage profit generation. It requires hoards of salespeople or an AI that can actually do math.

It's just how hyperscaling works. You are not wrong, but in the wrong timeline.

reply

fluoridation

5 hours ago

 |
root
 |
parent
 |
next

[–]

I'm not talking about custom, negotiated service contracts, I'm talking about simply charging people for what they use.

reply

anonzzzies

4 hours ago

 |
root
 |
parent
 |
next

[–]

But that would be using (a special Claude code version) of the API; as it stands now, I have tried the current api for fun and I hit $200 well within an hour. So if they would charge for real use, no one would use it as there are competitors who have less harsh limits with tier plans still. If all go away then I will be running open models on vast.ai or so as those are now viable (been testing with glm 5 and it's great for coding). So tier subscriptions cannot go away as it will end those companies fast.

reply

brookst

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

No, it is priced correctly.

Just because outliers can be money-losing doesn’t mean you should raise the price for everyone.

reply

goosejuice

9 hours ago

 |
root
 |
parent
 |
next

[–]

> Just because outliers can be money-losing doesn’t mean you should raise the price for everyone.

If they are losing money then it's not priced correctly. That's what I responded to.Yes, subscriptions work as you say. Plenty of people under utilize subscriptions from prime, to credit cards, to netflix. But if they lost money overall, they too would raise prices. Because that's how economics works. Shortage of capacity, high demand, raise prices until equilibrium.There's other knobs beyond ToS. They just didn't choose those options.

reply

crote

1 hour ago

 |
root
 |
parent
 |
next

[–]

> If they are losing money then it's not priced correctly.

Just a few years ago this was the standard business model for startups: attract VC money, offer plans at a loss, capture a huge market, boil the frog with incremental price increases to become profitable.Companies like Uber wouldn't have been anywherenearas successful if they had been forced to make a profit from day one.

reply

jmalicki

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

Yes, they chose the knob of ToS, because that was the way to price it correctly.

reply

goosejuice

8 hours ago

 |
root
 |
parent
 |
next

[–]

The market will determine if it was the correct choice. I don't think it's an obviously bad choice on their part.

reply

dimmke

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

I feel like Anthropic is going down a bad path here with billing things this way. Especially as local LLM continues to develop so fast.

I downgraded from my $200 a month plan to my $20 plan and hit limits constantly. I try to use the API access I purchased separately, and it doesn't work with Claude Code (something about the 1 million context requiring extra usage) so I have to use it Continue. Then I get instantly rate limited when it's trying to read 1-2 files.It just sucks. This whole landscape is still emerging, but if this is what it's likenow, pre enshittification, when these companies have shitloads of money - it's going to be so much worse when they start to tighten the screws.Right now my own incentive is to stop being dependent on Claude for as much as I can as quickly as I can.

reply

harrall

9 hours ago

 |
root
 |
parent
 |
next

[–]

This is how free drink refills, airplane tickets, Internet service, unlimited data plans, insurance, flat rate shipping, monthly transit passes, Netflix, Apple Music, gym memberships, museum memberships, car wash plans, amusement park passes, all you can eat buffets, news subscriptions, and many more work.

Either you get a flat rate fee based on certain allowed usage patterns or everyone has to be billed à la carte.

reply

dimmke

9 hours ago

 |
root
 |
parent
 |
next

[–]

This is a different case - those all have limitations based on human behavior (it's not necessary or possible to constantly be washing your car the entire month when you pay for unlimited washes) - that doesn't exist here. The types of plans available should reflect that reality. If gyms faced a situation where people would go and spend 18 hours working out every day for a month, they would probably change how they billed things.

Your comparisons are all also "unlimited" situations to Claude's very much limited situation. You can't buy a plan for Claude that is marketed as being unlimited. They're already selling people metered usage. They're just also adding restrictions on top of that.

reply

coldtea

8 hours ago

 |
root
 |
parent
 |
next

[–]

They sell metered usage while having the implied expectation that most wont use it fully. Power users and users of stuff like OpenClaw don't match that idea.

So they further restricted the metered caps, which were only offered to NOT be reached by that many.Simple as that.

reply

dimmke

8 hours ago

 |
root
 |
parent
 |
next

[–]

>Power users and users of stuff like OpenClaw don't match that idea.

Then they should figure out how to structure an offering that accommodates this type of usage not just blanket ban it

reply

satvikpendem

8 hours ago

 |
root
 |
parent
 |
next

[–]

Why "should" they? There's no reason they would especially when their competitor now owns OpenClaw.

reply

aleph_minus_one

51 minutes ago

 |
root
 |
parent
 |
next

[–]

>
Why "should" they?

Because it is clear that there is a market demand for it.

reply

dimmke

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

Because a big part of Anthropic's story is that they build based on how people actually use AI. Power users aren't just annoying edge cases, they're signal. Throttling them and calling it done is inconsistent with that.

reply

lelanthran

3 hours ago

 |
root
 |
parent
 |
next

[–]

> Power users aren't just annoying edge cases, they're signal.

You got that right; in this case they are signalling that AI token providers are not going to be able to run at a profit anytime soon.Not sure if that helps or hurts your argument, though.

reply

2000UltraDeluxe

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

> Power users aren't just annoying edge cases, they're signal.

Not all power users. Some re-invent the wheel and/or do things inefficiently, and in most cases there's no business incentive to adapt the service to fit the usage patterns of those users, or of other users that deviate from the norm in regards to resource usage.

reply

satvikpendem

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

Sorry to tell you but generally any company's "story" is all marketing and PR, if it interferes with their making money, which it does in this case, that company will not hesitate to leave it behind.

reply

bergheim

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

Oh the billion bollar vc backed pre ipo companys story was this? Omg and they somehow are not delivering up to your standards? Damn they better get their act together lest people like you will whine on twitter about them losing their way

reply

lelanthran

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

> Then they should figure out how to structure an offering that accommodates this type of usage

They did, didn't they? You can pay the non-plan rate.> not just blanket ban itThey didn't do that. The email specifically tells you how to use Openclaw with Anthropic. There is no "blanket ban".

reply

guiambros

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

They did: just use the metered API.

reply

what

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

They did figure out how to structure an offering that accommodates that type of usage: pay for your tokens.

reply

jyrkesh

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

"Unlimited" has always been a lie. There is no free lunch. There are always limits.

I've had to unwind "unlimited" within startups that oversold. I've been bit by ISPs, storage providers, music streamers, fuckin _Ubers_, now AI subscription services, that all dealt in "unlimited". None of them delivered in the long run.I'd be mad at Anthropic if it weren't for the fact that my experience now can see this sort of thing from a mile away. There are a lot folks, even on HN, that haven't been around for as long. I understand the outrage. I've been there. But these computers cost money to run, and companies don't operate at a loss in the fullness of time.Once you know that unlimited trends towards limited, the real question is whether we're equipped as a society to deal with the fact that the capital-L Labor input to the economic equation is about to be replaced with a Capital input for which only a handful of companies have a non-zero value.

reply

chrismorgan

1 hour ago

 |
root
 |
parent
 |
next

[–]

On your 1.5Mbps link, you could theoretically download 500GB per month. A huge amount, but I believe it was often genuinely allowed, because their uplinks could cope with it. Unlimited could genuinely be unlimited.

But now you might get things like “unlimited” 1Gbps… which reverts to 10Mbps (1% speed) or worse after 3.6TB (eight hours). And so your new theoretical maximum is about 6.8TB per month rather than 330TB.

reply

fluoridation

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

>If gyms faced a situation where people would go and spend 18 hours working out every day for a month, they would probably change how they billed things.

Not the best example. The upkeep cost of a gym is pretty flat regardless of how much people use the facilities. Two people can't use a single machine at the same time make it wear out twice as fast. The price of memberships is not correlated to usage, it'sinverselycorrelated to the number of memberships sold.

reply

harvey9

2 hours ago

 |
root
 |
parent
 |
next

[–]

Two people can't use a machine at the same time is the issue. If you have 50 machines and 200 customers all of whom want to be in the gym 18 hours per day that's quickly going to lead to cancelled subscriptions. Now you need more space and machines or some other way to balance things.

reply

dimmke

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

>Two people can't use a single machine at the same time make it wear out twice as fast

The machine doesn't care about the number of people using it. If it's constantly being used, it will wear out faster. You are conflating "we price based on expected under-utilization" with "costs don't scale with usage." Those are different things.The inverse correlation you talk about isn't relevant here - People buy gym memberships intending to go, feel good about the intention, and then don't follow through. The business model is built on that gap. That's pretty specific to fitness and a handful of similar industries where aspiration drives purchase.Anthropic doesn't sell based on a "golly gee I hope people dont use this" gap - they sell compute. Different business.

reply

fmbb

4 hours ago

 |
root
 |
parent
 |
next

[–]

> Anthropic doesn't sell based on a "golly gee I hope people dont use this" gap - they sell compute. Different business.

There is nothing anywhere hinting at that.They don’t sell compute. They sell a subscription for LLM token budgets that they hope people don’t use because the compute is vastly more expensive than what they charge or what users are ever willing to pay.Especially with enterprise subscription plans the idea is for customers to never utilize anywhere close to their limits.

reply

fluoridation

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

>If it's constantly being used, it will wear out faster.

Yeah, but there's an absolute limit to that, beyond which the cost doesn't keep increasing. Beyond that point, the QoS goes down (queues).>You are conflating "we price based on expected under-utilization" with "costs don't scale with usage."I'm not conflating anything, I'm responding to what you said:>If gyms faced a situation where people would go and spend 18 hours working out every day for a month, they would probably change how they billed things.Why would a gym need to change how they bill things if all their customers were aiming for maximal utilization, when their costs would barely see any change? I doubt your typical gym operates on razor-thin margins.

reply

dimmke

7 hours ago

 |
root
 |
parent
 |
next

[–]

Gym costs absolutely scale with usage. Equipment wears faster under heavier use. Cleaning and maintenance staff hours scale with how much the facility is used. Consumables like towels, soap, and chalk go faster. HVAC runs harder. The reason gyms can offer flat-rate pricing is that they bet on under-utilization, not that costs are flat.

Setting that aside, even if we accept your argument that gym costs barely scale with usage, then that makes gyms a bad comparison case for Anthropic, whose costs directly scale with usage. You can't use the gym model to defend Anthropic's pricing decisions if the two cost structures are nothing alike.I'm arguing that both gyms and Anthropic have usage costs that scale with usage, but gym business model assumes a large margin of under-utilization and there's a hard cap to "power user" - I think both of those extremes don't apply to Anthropic's situation. Under-utilizers aren't paying for AI they have a free tier. There's also a natural ceiling on how much any one person can use a gym. There's no equivalent constraint on API usage.

reply

krisoft

4 hours ago

 |
root
 |
parent
 |
next

[–]

> The reason gyms can offer flat-rate pricing is that they bet on under-utilization, not that costs are flat.

Yes. In fact i remember hearing about a gym which offered a flat-rate pricing model but explicitly excluded certain professions from partaking in it. I remember the deal was excluding police, bouncers, models, actors and air stewardesses. They had a separate more costly tier for these people. (And I think i heard about it from the indignation the deal has caused online.)

reply

TeMPOraL

2 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

>
Under-utilizers aren't paying for AI they have a free tier.

Sure they do. Free tiers suck. I may not always need to use AI, but when I need it, I don't want to immediately get hit by stupidly low quotas and rate limits, or get anything but SOTA models.

reply

fluoridation

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

>You can't use the gym model to defend Anthropic's pricing decisions if the two cost structures are nothing alike.

Am I? I think you read something into my comments that I didn't write.

reply

TeMPOraL

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

à la carte is honest; overprovisioning just slows progress by preventing demand from creating pressure to innovate proper solutions.

reply

taneq

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

The commons? Tragic.

reply

lelanthran

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

> I feel like Anthropic is going down a bad path here with billing things this way.

What do you expect them to do? You are looking at a business currently running at a loss, and complaining about their billingeven thoughthis is not a price-rise?Unrelated, is it still possible to use $10k/m worth of tokens on their $200/plan?

reply

alwillis

2 hours ago

 |
root
 |
parent
 |
next

[–]

They seem to know what they’re doing. Anthropic entered 2025 with a run rate of $1 billion; the run rate for March 2026 is estimated at $19 billion.

Internal projections show the company reaching cash-flow break-even in 2028, after stopping cash burn in 2027.They’ve already implemented several of the features that put OpenClaw on the map.

reply

lelanthran

2 hours ago

 |
root
 |
parent
 |
next

[–]

> Anthropic entered 2025 with a run rate of $1 billion; the run rate for March 2026 is estimated at $19 billion.

I don't know what that means in this context.> Internal projections show the company reaching cash-flow break-even in 2028, after stopping cash burn in 2027.What does that have to do with them implementing restrictions on their plans because they arecurrentlyrunning at a loss?Okay, lets say their internal projections[1] are accurate: were those before or after Openclaw released? Maybe their projections were made on the assumption that people would stop using $10k/m worth of tokens on a $200/m plan? Or that those users doing that will only be doing code? Or that the plan users won't be running requests at a rate of 5/minute, every minute of every hour of every day?--------------------------------[1] Where did you find those projections? I'm skeptical, at their current prices and current plans, that a break-even at any point in the future is possible unless they shut off or severely scale down training. Running at a per-unit loss means that the more you sell, the larger your loss - increasing your sales increases your loss.

reply

crote

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

If you can do less for the same price, that is in effect a price increase.

reply

username44

4 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You can use the API with CC, you just need to log out and log in, selecting API usage.

reply

boppo1

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

>Especially as local LLM continues to develop so fast.

I'm sorry is there anything even close to sonnet, much less opus, that can be run on a 4080? Or 64gb of ram, even slowly?

reply

satvikpendem

8 hours ago

 |
root
 |
parent
 |
next

[–]

Qwen 3.5, Gemma 4

reply

Alexzoofficial

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

Use qwen 4.6 plas

reply

manmal

4 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Tell me you are not using Anthropic without telling me. Bursts of unlimited usage was never the case. And I bet their infrastructure doesn’t like bursts as much as more spread out activity.

reply

j45

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

Efficient token use will be the new code/vim golf.

Whether it's human token use, or future OpenClaws

reply

xtracto

9 hours ago

 |
root
 |
parent
 |
next

[–]

I've mention before that we should have a look at Telegraph/telegram speak. There was a HUGE industry in word efficiency at that time. There are hundreds of books.

I even think an LLM trained to communicate using telegram style might even be faster and way cheaper.

reply

djfergus

6 hours ago

 |
root
 |
parent
 |
next

[–]

Reminds me of the terminus agent/harness on the terminal-bench coding benchmark - they just send send keystrokes to a tmux session. They score pretty well.

https://www.tbench.ai/news/terminus

reply

quietsegfault

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

Why use many word when few do trick?

reply

mannicken

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

> I've mention before that we should have a look at Telegraph/telegram speak.

.- -. -.. / .. --..-- / ..-. --- .-. / --- -. . --..-- / .-- . .-.. -.-. --- -- . / --- ..- .-. / -. . .-- / - . .-.. . --. .-. .- -- -....- -... .- ... . -.. / --- ...- . .-. .-.. --- .-. -.. ...

reply

reilly3000

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

It’s the new cloud cost vector, where cutting 2K from context on a busy service saves $xxxxx.

Terse.

reply

KellyCriterion

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

Like "Token Usage Consulting" companies popping up now? :-D

reply

xvector

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

No org doing real work cares about token use costs.

This mainly just affects hobbyists.

reply

KeplerBoy

4 hours ago

 |
root
 |
parent
 |
next

[–]

Token use cost can easily get as large as dev salaries. Even real businesses care about that.

reply

jen20

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

> You aren't paying to be using that limit all of the time.

The erosion of the norm of things doing what they advertise rather than being weasel-worded BS is particularly unfortunate, and leads to claims like this.

reply

mech422

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

you can write automated MCP tools that run within claude code, and could theoretically generate as high a load as any other automated/3rd party agent. You can also do loops that burn tokens incredibly fast. This is allowed with no caveats (I use MCP's basically to test what I'd like to try with the API...) So this explanation just seems a lil hollow.

reply

PlasmaPower

8 hours ago

 |
root
 |
parent
 |
next

[–]

Yes, but very few people are actually doing that compared to OpenClaw. If everyone else was doing that, they'd be cracking down on it too.

reply

alwa

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

When you can’t enforce everything at once, you go where the most acute problems are. I imagine when your MCP avenue of abuse catches on—like this other category of harnesses did—to such a scale as to become a problem impacting us folk trying to go about our business… when that’s where the problems shift, I imagine (and hope) Anthropic will crack down on that vector too. To keep the service usable for us ordinary meatbags.

I’m glad they give us the leeway to experiment, and I’m also glad they weed the garden from time to time. To switch metaphors, I’m deeply frustrated when my very modest, commuter-grade use gets run off the figurative highway by figurative hot-rodders. It’s been extra-529y this week, and it’s about time they reined it in a little.You’re always welcome to pay-as-you-go for as many tokens as you’d like to burn on their infrastructure… or to compute against any of the wide array of ever-improving open models on commodity compute providers…

reply

mech422

6 hours ago

 |
root
 |
parent
 |
next

[–]

>>when your MCP avenue of abuse catches on

Thats an interesting way of phrasing it - so is there a way to use the quota that's not 'abuse'? MCP/claude code seems to be want they want you to use it - are loops or ralph abuse as well ?

reply

Leynos

5 hours ago

 |
root
 |
parent
 |
next

[–]

It's not difficult at all to burn through your weekly limit just writing code.

reply

fyrecean

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

While you can write an automated tool to consume all their tokens, I strongly suspect most users, like myself, are not doing that. So even if Anthropic loses money on a power user, they profit overall and keep public sentiment high by not alienating users with restrictions. It's an optimization problem of making a profit off the average used while staying low enough to attract customers, even if that means some users cost more than they pay.

More users spinning up OpenClaw means that balance starts to shift towards more users maxing their tokens, thus the average increases, so I think their explanation makes sense still.

reply

mech422

7 hours ago

 |
root
 |
parent
 |
next

[–]

>>So even if Anthropic loses money on a power user, they profit overall and keep public sentiment high by not alienating users with restrictions

So they profit overall if I use all my tokens either way? Again, I understand usage limits - I just don't understand why some usage is 'good' and some 'bad' if I'm using the same either way.>>More users spinning up OpenClawI'm pretty sure that's a small percentage of overall users, and probably skewed towards the very people that would be recommending/implementing you model for work/businesses. Seems like that would be the group you are encouraging/cultivating ?

reply

closewith

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

My company has several MCPs that our very token intensive, but it seems that with Claude Code, usage is throttled even before hitting limits. I don't have any proof, but often when using intensive MCPs, Claude Code will just stall for 10+ minutes.

I wonder if anyone else has experienced this?

reply

mvdtnz

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

Anthropic is much more concerned about what people are ACTUALLY doing than what they could, in theory, be doing.

reply

stavros

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

How can an OpenClaw user use 6 times what a human subscriber is using when I'm four hours into the week and 15% of my weekly limit is already used up, just by coding? OpenClaw can't use 600% of my weekly limits.

reply

Kim_Bruning

16 minutes ago

 |
root
 |
parent
 |
next

[–]

Not sure what tier you're on.

Basically; spin up in the morning eats a lot of tokens because the cache is cold. This has actually gottenworsenow that Opus supports a 1Mt context.So: compact before closing up for the night (reduces the size of the cache that needs to be spun up); and the default cache life is 5 minutes, so keep a heartbeat running when you step away from the keyboard to keep the cache warm.Also, things like web-research eat context like crazy. Keep those separate, and ask for an md report with the key findings to feed into your main.This is not exhaustive list and it's potentially subtly wrong sometimes. But it's a good band-aid.https://news.ycombinator.com/item?id=47616297Know what's funny? Openclaw might actually burn less tokens than a naive claude code user; if configured correctly. %-/

reply

stavros

10 minutes ago

 |
root
 |
parent
 |
next

[–]

I'm on the $100 tier, but I don't use OpenClaw. My point is it can't use more than 100% of my limit, so "6-8x more" is only possible if you use 15% of your subscription normally.

reply

Kim_Bruning

7 minutes ago

 |
root
 |
parent
 |
next

[–]

Right. I was editing to add more info. Possibly you already know the usage tricks I list above. The world is still very messy and not much is documented properly.

And I'm skeptical of the 6x-8x claim myself. They'd have to explain that in more detail.

stavros

4 minutes ago

 |
root
 |
parent
 |
next

[–]

Oh actually the cache trick is neat, I hadn't considered it, thanks!
coldtea

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

>
How can an OpenClaw user use 6 times what a human subscriber is using when I'm four hours into the week and 15% of my weekly limit is already used up, just by coding?

Perhaps because your Claude agent usage is not representative of the average user, and closer to the average OpenClaw user levels...

reply

mikkupikku

2 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Man, I run 3-5 sessions an evening for 5-6 hours, and longer on weekends and feel like I'm barely using what I paid for. I've only hit five hour limits a small number of times. Genuinely baffled when I hear people blow through tokens apparently several times faster than me. Are you going out of your way to design complex subagent workflows or something? I just let claude code use subagents when it wants to but don't give it any extra direction to use them.

reply

echelon

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

Without data, this is just a bunk excuse to defend the walled garden practices.

With data, it's an engineering target.They could just 429 badly behaved clients.

reply

stavros

9 hours ago

 |
root
 |
parent
 |
next

[–]

They already 429 everyone! That's the crazy thing. They already have strict limits that we all keep hitting regularly.

reply

philistine

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

You guys are arguing on the reality of a subscription, but Anthropic still resides in the coocoo make-up world of growth at all costs backed up by unfathomable investments. They're not acting rationally by trying to present a good product with reasonable backend fundamentals. They're just trying to maintain the money loss to what they have set aside for the quarter. OpenClaw was not planned for, and thus must be fought.

reply

Nevermark

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

> Everyone on a plan pays for the max set of tokens in that plan.

From Anthropic's perspective, everyone pays to be in bins with a given max.And to everyone's benefit, there is a wide distribution of actual use. Most people pay for the convenience of knowing they have a max if they need it, not so they always use it.So Anthropic does something nice, and drops the price for everyone. They kick back some of the (actual/potential) savings to their customers.But if everyone automates the use of all their tokens Anthropic must either raise prices for everyone (which is terribly unfair for most users, who are not banging the ceiling every single time), or separate the continuous ceiling thumpers into another bin.That's economics. Service/cost assumptions change, something has to give.And of the two choices, they chose the one that is fair to everyone. As apposed to the one that is unfair (in different directions) to everyone.

reply

goosejuice

7 hours ago

 |
root
 |
parent
 |
next

[–]

Yes, mostly what I'm saying, but forgetting the important part:

From the email:
> but these tools put an outsized strain on our systems. Capacity is a resource we manage carefully and we need to prioritize our customers using our core productsOpenClaw doesn't put an outsized strain on their systems any more than Anthropics own tools. They just happen to have more demand than they can serve and they benefit more when people to use their own tools. They just aren't saying that explicitly.It has nothing to do with fairness or being nice.

reply

aenis

6 hours ago

 |
root
 |
parent
 |
next

[–]

If this was a gym subscription, it would be an equivalent of some people going to the gym, and some people sending their android to the gym every day, for the whole day, and using as much equipment as the gym policy allows.

reply

goosejuice

6 hours ago

 |
root
 |
parent
 |
next

[–]

It would be like some people sending the gym's competitor's android to the gym instead of the android the gym provides. Said gym also doesn't have enough equipment for everyone's gym appointed android despite being more expensive. Said gym doesn't want to admit this, nor does it want to raise prices on an already more expensive subscription. Said gym doesn't want competitor's android to gain marketshare. Said gym blames competitor's android for using up gym equipment despite gym's own android being capable of using as much equipment.

reply

chii

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

> using as much equipment as the gym policy allows.

which said customer paid for. And now they want to back out of it because it turns out they thought users wouldn't do that.I say they ought to be punished by consumer competition laws - they need to uphold the terms of the subscription as understood by the customer at the time of the sign up.

reply

chii

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

> there is a wide distribution of actual use

except when people start using openclaw, and the distribution narrows (to that of a power user).I hate companies that try to oversell capacity but hides it in the expected usage distribution. Same goes for internet bandwidth from ISP (or download limit - rarer these days, but exists).Or airplane seats. Or electricity.

reply

Nevermark

1 hour ago

 |
root
 |
parent
 |
next

[–]

> I hate companies that try to oversell capacity but hides it in the expected usage distribution.

Except they charge you less because of the distribution. Competition for customers doesn't evaporate.

reply

hombre_fatal

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

The trade-off is that if you set your usage limits so that you can handle the case where everyone is saturating their limit at all times, then (1) the usage limits would be too small and (2) you're optimizing for a usage pattern that doesn't exist and (3) you're severely underprovisioning, which is worse for everyone.

Instead, you can prioritize people "earnestly" bursting to the usage limits, like the users who are actually sitting at their computer using the service over someone's server saturating the limit 24/7.The goal is to have different tiers for manual users vs automated/programmatic tools. Not just Anthropic, this is how we design systems in general.

reply

goosejuice

9 hours ago

 |
root
 |
parent
 |
next

[–]

Well earnest here just means using Claude code directly or the Claude app. Both that just happen to support using tokens while you sleep!

reply

hombre_fatal

7 hours ago

 |
root
 |
parent
 |
next

[–]

Defining earnest (placeholder word btw) is the hard part of the trade-off, though.

When your least automated, most interactive users are competing for capacity with fully-automated tools, let's say, you're forced to define some sort of periphery between these groups.OpenClaw is a self-directed, automated loop that sits on a server. It's wowing its owner by shitposting on moltbook and doing any number of crazy stories you can find online that amount to "omg I can't believe my self-directed claude loop spent all day doing this crazy thing haha."On the other end of the spectrum is someone using Claude.app's interface.And then in the middle, you can imagine "claude -p" inside a CI tool that was still invoked downstream of a user's action. Still quite different from the claude loop.

reply

goosejuice

7 hours ago

 |
root
 |
parent
 |
next

[–]

Claude code has /loop. Claude app has scheduled tasks. The leaked source has a proactive mode.

I'm sorry but this framing just doesnt make sense.

reply

gbear605

7 hours ago

 |
root
 |
parent
 |
next

[–]

Even with those tools, the usage of Claude Code with all of them turned on is going to trend much lower than OpenClaw usage. Everyone that I've seen with OpenClaw will intentionally waste tokens just to make sure they hit the cap, even if they're doing useless stuff with it. And it can be going 24/7, every minute constantly, while the intended purpose with scheduled tasks is to use them at a set rate but not nearly constantly.

reply

goosejuice

7 hours ago

 |
root
 |
parent
 |
next

[–]

Definitely. They will see less usage. That's good for them because they have infra scaling issues that they don't care to admit explicitly. Their competitor will also get less telemetry (if they enable it). It's a win win.

reply

mech422

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

This is what I've been wondering about for a while now. I have the 20x plan as well, which I thought would allow me to try some API coding - but you get zero API usage.

As you said, I would imagine where the token usage comes from is irrelevant - you are generating the same load whether you do it from claude code or some other agent. So it seems like the rules are more to do with encouraging claude code usage, rather then claude model usage.

reply

goosejuice

7 hours ago

 |
root
 |
parent
 |
next

[–]

Claude code is still getting used by these agents. They banned the mimicry awhile ago and said claude -p was fine.

OpenClaw just happens to also get telemetry, of probably higher value, out of the same tokens. It also happens to be owned by their competitor.edit: I'm wrong OpenClaw surprisingly doesn't collect telemetry. Good for them.

reply

CubsFan1060

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

I don’t really follow what you’re saying. You mention the 5 hour limit. Is your expectation that they have enough capacity so that everyone can hit their 5 hour limit all the time? Or you are proposing that’s how they limit capacity for a subscription?

Do you have an example of how this is how they have advertised or sold the plan? I don’t recall ever seeing any advertisement that their plan is simply pre paying for tokens.

reply

dgellow

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

You’re missing something. I’m pretty sure it’s not only about the cost. Anthropic literally doesn’t have enough compute. They have to balance the load between enterprise customers and end users with subscription. If you consider they don’t have infinite compute (ie at their scale there is a limit to how much is available in a given region) and something is causing subscription users to increase usage significantly they do have to find a way to balance.

At least that’s my read. I don’t believe it is nefarious

reply

priyanshujain

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

Exactly your point. Anthropic is subsidizing their own tools to keep people on their platform. What's wrong with that?

Tokens and these agents(Claude Code/cowork/claude.ai) are separate from model tokens, and they want to discount for their own product usage.The subscription they sell is a package of these products, not tokens. They never sell token subscriptions, so why do we need to relate tokens with the subscription? Fundamentally, they never meant to sell token usage in that subscription, similar to any other SaaS company trying to sell API usage.

reply

goosejuice

6 hours ago

 |
root
 |
parent
 |
next

[–]

> What's wrong with that?

Nothing beyond fumbling the PR around it.

reply

risyachka

12 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

yes and then still subsidise subscriptions by an order of magnitude

its obvious they will tighten everything and raise prices for years to come

reply

felipeerias

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

If they bundled together these two radically different usage patterns, either the service would become more expensive or the limits would become a lot tighter, in both cases making Claude Code far less attractive to professional users.

reply

Farmalono

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

OpenClaw is a mass project and doing something in the background 24/7.

I haven't even heard of claude -p before your comment.OpenClaw is for sure not just a good cover story. Or its the cover face of the issue of automated tool workflows.I don't think they are bothered too much about other frontends who do the same as claude code.

reply

RIMR

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

You are still misunderstanding.

If you max out your token limits, you are costing Anthropic more than you are paying them. They only expect a small percentage of their users to do this, but OpenClaw changed the dynamic.Anthropic knows that they will lose more users by lowering limits than they will by blocking OpenClaw, because OpenClaw users will overwhelmingly switch to API pricing, while chatbot users will leave for competitors with higher limits.They are a business. They hope to become profitable. This was the correct move.

reply

brookst

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

> The agent consuming those tokens is irrelevant.

This is so wrong.The subscription is to Claude (the app, Claude code, etc) not the API.Anthropic subsidizes Claude code because they collect a ton of super useful telemetry and logs so they can improve… Claude code.Wanting to pay for a subscription to Claude and treat it like an API discount is like going to an all you can eat buffet and asking them to bring unlimited quantities of raw ingredients to you so you can cook at home. Ok, not a perfect analogy, but you get the idea.

reply

goosejuice

9 hours ago

 |
root
 |
parent
 |
next

[–]

> Anthropic subsidizes Claude code because they collect a ton of super useful telemetry and logs so they can improve… Claude code.

You just paraphrased my argument

reply

guelo

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

How many tokens does the $20/month buy me? I want to know what those hard token limits are but they refuse to tell me. I'm pretty sure they've reduced those limits the last week but they won't admit it. It feels like a scammy pricing model.

reply

goosejuice

5 hours ago

 |
root
 |
parent
 |
next

[–]

I agree, I think consumers appreciate transparency.

reply

fabbbbb

5 hours ago

 |
root
 |
parent
 |
next

[–]

To some degree sure, is it about the number tokens you can max out?

I’m pretty happy knowing that it supports my development workflow for a week. Recent features like the Code Desktop built in browser, Cowork with Claude in Chrome and remote control matter to me way more than the number of tokens. But that’s me.Depends on their targeted ICP also, which they are free to define. Is it those users maxing out tokens for the buck? I have the feeling there’s even better alternatives on the market right now.

reply

goosejuice

4 hours ago

 |
root
 |
parent
 |
next

[–]

> I’m pretty happy knowing that it supports my development workflow for a week

For many it doesn't. It's opaque, it changes, and they bury the news in fucking twitter.https://x.com/trq212/status/2037254607001559305There's a lot to love about Anthropic. But man do they suck at PR.

reply

PunchyHamster

1 hour ago

 |
root
 |
parent
 |
next

[–]

Oh no, man fell in love with corporation

reply

paulddraper

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

Exactly.

Subscriptions are crazy subsidized.So you can’t use OpenClaw, OpenCode, etc. because they take you outside their applications/lock in and their ability to easily monetize in the future.

reply

muyuu

9 hours ago

 |
parent
 |
prev
 |
next

[–]

It's one thing to pay $5 or $20 per month, which although it's a substantial difference, people pay that much for the convenience of having stuff ready and available - and it's a completely different thing to pay $200 per month. People don't pay that much for occasional usage and many/most people will organise themselves to use all or most of their weekly allowance when the expense is in that ballpark.

If Anthropic miscalculated the amount of tokens, or simply pushed too hard to capture market share, that is a costly mistake because people in this market are very sensitive to price hikes.They have to be honest about what they can offer for $200. Sure, people don't max their subscriptions but when they're large they make the best of it, or they will likely cancel it.
The typical subscription works well below capacity because it's cheap enough that the optionality may be worth it. $200 is not the typical subscription.

reply

rovr138

9 hours ago

 |
root
 |
parent
 |
next

[–]

>They have to be honest about what they can offer for $200

Their expectation must have been a human using the service at a human capacity.This is different from an automated agent orchestrating a ton of different agents at the same time doing a lot of things.Thereisa difference.

reply

muyuu

9 hours ago

 |
root
 |
parent
 |
next

[–]

You are correct, but you don't need openclaw to batch your work. People will figure out ways to use their tokens at that fixed price.

Sure there is a difference. It's like when most mobile companies wouldn't allow tethering because then people would actually use the service.You can try to stop that, but people will price in those inconveniences. They will simply learn that the fee pays for much less than the token limit and that the company is enforcing some unwritten limits by adding extra limitations to usage.We will see it play out.

reply

dimmke

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

If people are finding new ways to use AI, they should change how they bill. Banning third party harnesses is bad for a lot of reasons - it looks like they're trying to force people to use their software. Strategically it might make sense - gives them a tiny moat if their models ever slip - but it discourages the breakneck pace of innovation and the long term effect is that their customers (largely highly skilled with computers and building software) will look to decouple themselves. Claude is good but it's not so far better than anything else that they can pull shit like this and people will just deal with it.

They already have the regular subscription plans (Pro, Max) and a separate billing process for direct API usage. They could absolutely introduce another type of plan optimized toward this kind of usage or just accept that it's a dumb pipe that is being paid for and having these random arbitrary limitations is just making things more confusing and a bad plan for the future.

reply

systoll

1 hour ago

 |
root
 |
parent
 |
next

[–]

They have subscription plans for their software, and a seperate billing process for the API. There's nothing to change. 'Accepting that it's a dumb pipe' would just mean removing the Pro & Max plans as options.

Clawdbot was clearly against the Consumer Terms of Use the whole time, they’ve just started actively detecting and blocking it.> Except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it, [it is forbidden] to access the Services through automated or non-human means, whether through a bot, script, or otherwise.

reply

gbear605

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

They already have the way that you're supposed to bill for usages like this, the API usage. The purpose of the subscription plan is strictly for the cases where you are using few enough tokens on average that it's not a money pit for them.

reply

what

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

They don’t need to change how they bill. Your subscription is for Claude app/code. Otherwise you pay per token. It’s always been this way.

reply

dimmke

7 hours ago

 |
root
 |
parent
 |
next

[–]

Claude Code is a subscription tier explicitly designed for agentic, automated, heavy usage. So the 'subscriptions are for human use, API is for automation' line is already blurry by their own offerings.

If the actual concern is use pattern, enforce that directly. What we have instead is metered usage + behavioral restrictions + product fragmentation across three separate offerings.That's not a clean billing philosophy, it's layers of control stacked on top of each other with no coherent logic tying them together.If subscriptions are for humans and API is for automation, fine. But then don't meter the human product arbitrarily and don't sell a subscription tier for automation while also restricting automation. Pick a lane.

reply

tomnipotent

5 hours ago

 |
root
 |
parent
 |
next

[–]

> Claude Code is a subscription tier explicitly designed for agentic, automated, heavy usage

Except it's not. It's a desktop, web, mobile, and CLI subscription product built on top of a usage-based API with a generous token allowance bundled with it. That generous allowance comes with the restriction that those tokens can only be spent through Claude product surfaces. Why would Anthropic offer their API at a loss and subsidize the profits and growth of other businesses?

reply

bitwize

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

Start paying by the token if you want to use these tools. Simple as.

reply

toraway

6 hours ago

 |
root
 |
parent
 |
next

[–]

Even better: switch to Codex
plus
 get better rate limits. I’m not a captive audience as much Anthropic would like to believe otherwise.

reply

lifeformed

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

The whole industry is about robots telling robots what to do, why wouldn't they have expected automation?

reply

jen729w

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

> They have to be honest about what they can offer for $200.

Isn't that exactly what they just did?

reply

muyuu

4 hours ago

 |
root
 |
parent
 |
next

[–]

not really, no

being honest would be to just adjust the limits rather than adding piecewise limitationsbut of course with honesty comes that people can actually gauge your product accurately and they may not want that

reply

KingMob

3 hours ago

 |
root
 |
parent
 |
next

[–]

But the limits apply to all users. I doubt non-OpenClaw users want to pay $XX more to subsidize OpenClaw users.

reply

muyuu

2 hours ago

 |
root
 |
parent
 |
next

[–]

it amounts to service limit obfuscation, and their market are very clued about that

nobody wants them to add fineprint every time users find effective ways to actually use the service to its advertised limits, it only benefits those who want to be milked for recurring revenue for sporadic usage while paying handsomely for the privilege

reply

bottlepalm

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

Anthropic didn't miscalculate anything. They calculated what they could charge/subsidize for humans, not automatons. Banning OpenClaw brings usage levels under control.

If you had to pay for APIs yourself foranyprovider then you'd know that SOTA tokens are not cheap, and Claude Code for $100 is almost a too good to be true bargain for what you can get out of it.

reply

kamma4434

4 hours ago

 |
parent
 |
prev
 |
next

[–]

My impression is that at the moment the value you get out of Claude is simply incredible.

As a senior engineer, you get an assistant that never gets tired and can do quite a lot on its own. For me, it’s been an eye-opening experience. I used to have a collaborator called M that had a good general culture, but was not too smart. The calculation going into my mind every time I ask Claude for something is: how much would that cost, in terms of time and effort, to get M to do that? M was a resource that costed many thousand dollars per month, plus the time I spent correcting and directing, while Claude is actually smarter and does what it is asked with a degree of autonomy and common sense that M could never dream of.The flipside of the coin is obvious: Anthropic will find a way to claw back - no pun intended - some of this value by raising the cost of subscription. They would be crazy not to.

reply

lukewarm707

3 hours ago

 |
root
 |
parent
 |
next

[–]

value is high but what about the competitors?

is claude that good? the last time i tried claude it was sonnet 4.5. it was ok, not worth the api money clearly. but i only use api tokens for llms.

reply

port11

41 minutes ago

 |
root
 |
parent
 |
next

[–]

If you look at SWE, Claude models aren’t that special. Other benchmarks come up with different results.

But… anecdotally, Claude is justthatgood. Gemini needs a lot of hand-holding, and it will still tell you it’s done when it achieved half the work. Or say, “this test isn’t passing, I’ll just delete it”. Every now and then I get tired of it and give the same task to Sonnet 4.6; 5 minutes later I’m done. Bug fixed, UI properly working, React hooks not being conditionally rendered, theme variables used properly. It’s wonderful.I’m not sure about large agentic work or deep thinking, but I’m mostly automating away the drudgery of dealing with React Native. I still want to do the deeper work myself, but even there Opus is usually a really good sparing partner.

reply

PostOnce

9 hours ago

 |
parent
 |
prev
 |
next

[–]

The entire point of AI is for it to do shit autonomously?

The whole point is that the users can have it doing shit for them instead of them having to babysit the computer.The fact that users still have to sit there and argue with it erodes their value proposition. The proposition you can pay fewer salaries.

reply

ozim

9 hours ago

 |
root
 |
parent
 |
next

[–]

I would argue that „doing shit” should be done by dummy automations. AI should be used to help build that automations or step in when dummy automation breaks.

For now too many people will use AI for stuff that deterministic stupid code would be much more efficient.

reply

nemomarx

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

They could probably offer enough tokens for that but it would be at a higher price than the sub, I think. You could still pay fewer salaries at 3k a year or per token enterprise prices or whatever.

reply

manmal

4 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

They want you to do your shit through their own desktop apps.

reply

Alexzoofficial

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

Yes

reply

JasonHEIN

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Err, yeah, you should neither do any web scraping without respecting robots.txt, nor use ad blockers when using Google. When working with a business, never use Google Docs without paying them. Nah, that's not how the world works and at least not in the software industry.

reply

cowlby

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I just discovered Pi Coding Agent and found that it's lean System Prompt + a tuned CLAUDE.md brought back a lot of the intelligence that Opus seemed to lose over the last month.

Sucks to be pushed back to Claude Code with opaque system behavior and inconsistency. I bet many would rather pay more for stability than less for gambling on the model intelligence.

reply

chatmasta

10 hours ago

 |
root
 |
parent
 |
next

[–]

We use Pi at work (where we pay per token) and I’d love to use it personally too. From what I’ve read, nobody has been banned for using Pi yet… I wonder if Anthropic minds this much as long as it’s still human usage, or if they’re mostly focused on stamping out the autonomous harnesses. Unfortunately Pi is also what OpenClaw uses so it could easily get swept up in the enforcement attention.

Or maybe I’ll just get a Codex subscription instead. OpenAI has semi-officially blessed usage of third party harnesses, right?

reply

nerdix

9 hours ago

 |
root
 |
parent
 |
next

[–]

It appears that OpenAI has blessed third party harnesses. I know they officially support OpenCode and they have this on their developer portal:

"Developers should code in the tools they prefer, whether that's Codex, OpenCode, Cline, pi, OpenClaw, or something else, and this program supports that work."https://developers.openai.com/community/codex-for-ossObviously, the context is that OpenAI is telling open source developers who are using free subscriptions/tokens from the Codex for Open Source program that they can use any harness they want. But it would be strange for that to not extend to paying subscribers.

reply

mirashii

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

They have, but they also just announced this week that for business and enterprise plans, they’re switching from quotas for codex to token use based pricing, and I would expect that to eventually propagate to all their plans for all the same reasons.

reply

chatmasta

9 hours ago

 |
root
 |
parent
 |
next

[–]

I’d be surprised if that propagated to personal subscription plans, simply because it would put them at a huge competitive disadvantage against Anthropic, which they’ve already signaled they care about by saying they allow third-party harnesses. But I wouldn’t be surprised if they required third-party harnesses to use per-token billing, since that’d put them on par with Anthropic.

reply

jen20

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

You can still use it with an OpenAI subscription (for now at least), and the models aren't substantially worse.

reply

j45

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

I wonder if there's a way to bring some of what Pi Coding Agent has to claude code itself.

It seems that installing claude code directly from npm shields from some of the current issues.

reply

blueblisters

4 hours ago

 |
parent
 |
prev
 |
next

[–]

> Every single one of them oversells their capacity

Indeed. And this model breaks in several cases that overlaps with the current AI business model:- marginal cost of incremental usage is too high (Movie Pass)- adverse selection (all you can eat monthly steak subscriptions)- demand is synchronized (WeWork)

reply

PunchyHamster

1 hour ago

 |
parent
 |
prev
 |
next

[–]

No, people want transparency. If it was "x tokens per time interval, then you pay extra", the problem wouldn't exist.

reply

peterkelly

3 hours ago

 |
parent
 |
prev
 |
next

[–]

> Every single one of them oversells their capacity

That sounds like their problem, not ours

reply

Tzk

3 hours ago

 |
root
 |
parent
 |
next

[–]

In theory yes, but the overselling does also keep the price low (at least a bit), but also boosts revenue. So when power users use the service too much, the seller will either raise prices, cut features or ban some usage patterns.

You can vote with your wallet though. So don’t throw money at them or just deal with it. Plain and simple.

reply

raincole

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

It's not your problem anymore once you switch from Claude :)

reply

HotHotLava

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

Well, yes, it is. That's why you're seeing them take proactive steps to address the problem, like this new policy.

reply

seqizz

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

Doesn't look like it

reply

chunpaiyang

7 hours ago

 |
parent
 |
prev
 |
next

[–]

Good point. I agree with that.
The key point is that heavy users benefit from this model while light users are basically subsidizing them.
But it's a distribution when everyone shifts toward heavy usage, prices inevitably go up.
The $17/mo pro price is already set to compete with other providers. Raising it would lose customers. Other tiers are also carefully priced to match competitors.
So the only move left is to prevent the whole distribution from drifting toward heavier usage. That's exatly what this ban does.

reply

bombcar

9 hours ago

 |
parent
 |
prev
 |
next

[–]

> Every single one of them oversells their capacity

This is (almost) universally true offlat ratesubscriptions; but there are usage-billed ones, too (and even those often have an aspect of subsidies).A great example of the shakeup is when dial-up went from "connect, do the thing, disconnect" to "leave the computer online all the time" - they had to change the billing model because it wasn't built for continuous connections.

reply

mh-

9 hours ago

 |
root
 |
parent
 |
next

[–]

That's a good analogy. Maybe soon we'll see Claude Code CDs with 700 free hours.

reply

wouldbecouldbe

3 hours ago

 |
parent
 |
prev
 |
next

[–]

well that largely depends, lots of saas are running 90% operating profit margins

reply

subarctic

6 hours ago

 |
parent
 |
prev
 |
next

[–]

I'm pretty sure in this case it's anthropic doing the subsidizing because the api and extra usage rates are extremely expensive compared to the usage you get for the lowest subscription level. I pay $28 CAD per month and I'm pretty sure I'd burn through that in a day or two, and I'm not really a power user, I'm just using it to write code like it says on the tin. I seriously doubt there's a large portion of subscribers with low enough monthly usage that they'd save money by switching to the API.

reply

scotty79

1 hour ago

 |
parent
 |
prev
 |
next

[–]

So basically their move is an admission that they can't scale up their capacity accordingly to shifting demand while keeping the current pricing.

Customers have their own value calculations. If they can't use Claude for autonomous agent at reasonable price they will move to providers that are cheaper and more flexible. Autonomous agent adds way more utility than a marginally better LLM (assuming that's even true).

reply

Gregaros

8 hours ago

 |
parent
 |
prev
 |
next

[–]

Still very interesting timing to ban third party harnesses, given the proximity to the Claude Code leak …

reply

manmal

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Come on, someone on a Max account has a reason why they are paying $200. I bet many are at least often near the weekly limit, or they‘ll downgrade. If anything, OpenClaw usage is more spread out instead of ingesting whole codebases during office hours.

The Anthropic subs are likely priced at marginal cost (Amp‘s CEO recently said that in a podcast). It just doesn’t serve Anthropic to be operating as the service layer for OpenClaw.

reply

ph4rsikal

4 hours ago

 |
parent
 |
prev
 |
next

[–]

So it's like Sliceline from Silicon Valley (the show)

reply

nightski

10 hours ago

 |
parent
 |
prev
 |
next

[–]

It's fine, their moat is thin. Frontier models as a service isn't really in the best interest of anyone anyways. Only a matter of time.

reply

asgraham

10 hours ago

 |
root
 |
parent
 |
next

[–]

Are you arguing that eventually a competitor will emerge that does support OpenClaw with a subscription model? Wouldn’t that just be more expensive for the exact same reason Anthropic is banning it?

reply

tekacs

10 hours ago

 |
root
 |
parent
 |
next

[–]

OpenAI have literally gone out of their way to explicitly support this sort of thing. As they did with OpenCode.

Honestly, this just looks like what Dylan of SemiAnalysis suggested on Dwarkesh – that they've massively under-provisioned capacity / under-spent on infrastructure.That would honestly be a comforting answer if true, because I would gladly take 'we can't afford to do this right now' over 'we are self-preferencing, and the FTC should really take a look at us, even if we're technically not a monopoly right now, since we're the only strongly-instruction-following model in town and we clearly know it'.

reply

verdverm

10 hours ago

 |
root
 |
parent
 |
next

[–]

OpenAi is burning cash to stay relevant aiui, i.e. they will keep subsidizing

You can use these tools with most providers today, just no subscription plan. If you have enough spend, you can likely get bulk deals

reply

gjsman-1000

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

> we are self-preferencing, and the FTC should really take a look at us, even if we're technically not a monopoly right now

Tell me you have zero clue what a monopoly is or what the law is, without telling me.Monopoly law relies on broad categories, not narrow ones. You can’t call Microsoft a monopoly because they are the only company that makes Windows. You can’t call Amazon a monopoly because they are the only company that makes AmazonBasics. You can’t call Anthropic a monopoly because their product is 20% better for your use case, otherwise by definition no company has any incentive to do a good job at anything.

reply

code_duck

10 hours ago

 |
root
 |
parent
 |
next

[–]

Somehow this was coming up a few years ago where people kept saying that Apple could face antitrust because they were the only company who made iOS and controlled the App Store. Given that android exists, and has roughly equal market share, that didn’t make much sense to me, but I kept seeing it being discussed.

reply

satvikpendem

8 hours ago

 |
root
 |
parent
 |
next

[–]

And Apple did lose that case now so they were correct; sometimes, one can be a monopolist in the market they created.

reply

satvikpendem

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

Well, Apple did recently lose as they're the monopolist in their walled garden for app distribution.

reply

bsder

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

> Tell me you have zero clue what a monopoly is or what the law is, without telling me.

Monopoly law is subject to reinterpretation over time and anybody who has studied the history of it knows this. The only people argue for "strict" interpretations of current monopoly law are those who currently benefit from the status quo.> Monopoly law relies on broad categories, not narrow ones.And this is currently a gigantic problem. Because of relying on broad categories to define "monopoly", every single supply chain has been allowed to collapse into a small handful of suppliers who have no downstream capacity thanks to Always Late Inventory(tm). This prevents businesses from mounting effective competition since their upstream suppliers have no ability to support such activities thanks to over-optimization.To be effective on the modern incarnation of businesses, monopoly law needs to bust every single consolidatednarrowvertical over and over and over until they have enough downstream capacity to support competition again.

reply

tekacs

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

Oh, give me a break. I know the law around this incredibly well. Reasonable people can disagree about whether the law is appropriate. The whole point of laws is that they should match intent – and as for '20%': "tell me you don't understand how a small quantitative gap can result in a step change in capability."

reply

gjsman-1000

10 hours ago

 |
root
 |
parent
 |
next

[–]

> Oh, give me a break. I know the law around this incredibly well.

Then don’t make BS up like implying Anthropic is a monopolist for the crime of competence.> tell me you don't understand how a small quantitative gap can result in a step change in capabilityThe law does not give a darn about this. Being a good competitive option does not make you a league of your own. If I invent a new flavor of shake, the Emerald Slide, am I a monopolist in shakes because I’m the only one selling Emerald Slides? If you go and then start a local business reselling shakes and I’m your only supplier, am I a monopolist then? Absolutely not.

reply

tekacs

10 hours ago

 |
root
 |
parent
 |
next

[–]

You do realize that I called out in my post they are absolutely not a monopoly by the law, right? I know all-too-well what the definition is.

We have a similar situation in mobile where Apple may not be considered a monopoly, but people have walked around for a decade with a supercomputer in their pocket that is wildly underused.Things have gotten faster; things are different than they were decades ago when a lot of this was devised.The reality of the matter is that some of us just want to see innovation actually happen apace, and not see 5, 10, or 30 years of slowdown while we litigate whether or not such a company is holding all the cards, while everyone is collectively waiting at the spigot for a company to get its shit together because we're not allowed to fix the situation.For what it's worth, I'm hopeful that the other model providers will catch up and put us in a situation where this conversation is irrelevant.What I'm afraid of is a situation where we see continued divergence, and we end up with another Apple situation.

reply

nandomrumber

10 hours ago

 |
root
 |
parent
 |
next

[–]

You’re welcome to start
OpenSpigot
 yourself, and see how investors feel about you giving away your technical / IP / market advantage on launch day.

reply

gjsman-1000

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

> “we are self-preferencing, and the FTC should really take a look at us, even if we're technically not a monopoly right now”

That is not calling out that they are “absolutely not a monopoly by the law” in any way, shape, or form. You’re framing it as though they aren’t by a technicality, when they aren’t anywhere near discussion by even the most extreme of legal theories. You won’t find Lina Khan or Margarethe Vestager, both ousted for going too far, complaining about Anthropic.> “We have a similar situation in mobile where Apple may not be considered a monopoly, but people have walked around for a decade with a supercomputer in their pocket that is wildly underused.”In that we can’t run a Torrent client to download illegally redistributed media 99% of the time? Otherwise, in what way, are they underused? For the degrees of public addiction, a more underutilized phone would be a social benefit.

reply

tekacs

10 hours ago

 |
root
 |
parent
 |
next

[–]

Let me back up what you're saying. They absolutely are not a monopoly today by any definition, by any stretch, in any conceivable way.

I'm looking forward. Things are moving very quickly. As I said above, I'm afraid of us diverging into another Apple situation in the future. If I suggest that they should be looked at and thought about, it's not for today, it's for tomorrow. If divergence continues. Because as with everything in AI, it might hit us a lot faster than people expect. Hell, given their approach to morality, I suspect that Anthropic folks have already thought deeply about these sorts of concerns. That's why it's actually a lot more in character for them to be doing this not due to self-preferencing, but due to unaffordability, which - if you look at my first post - is what I said seems to be happening.Suffice to say that I have a graveyard of things that I think phones could have been, where unfortunately we've ended up with these - as you say - addicting consumerist messes.Gonna stop here so I don't flood the thread. We're getting very off topic.

reply

jfim

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

Some of the Chinese labs with cheaper per token costs do support it, like say minimax:
https://agent.minimax.io/max-claw

I haven't tried it to see if it's any good but it's $20/mo.

reply

msh

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

Kimi seems to support this with their 39 usd a month plan.

reply

techgnosis

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

Doesn't OpenAI allow this today?

reply

mil22

10 hours ago

 |
root
 |
parent
 |
next

[–]

It's a good way to win market share and build goodwill, but one has to wonder whether this class of usage is marginally profitable for them (or anyone) and how sustainable their lenient policies will be for them long term.

reply

raincole

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

You mean whether
another
 competitor will emerge? Right now we have OpenAI.

reply

rvz

10 hours ago

 |
root
 |
parent
 |
next

[–]

The real threat that Anthropic sees as
real
 competitors in the long term, are the AI labs building open weight models, especially the AI labs in China.

reply

verdverm

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

I agree, eventually the open models will be good enough and we can pay for our own infra and cut out the middle man. Also, the smaller frontier are nearly as good today and I expect the mega models will be used primarily for distillation

reply

nl

7 hours ago

 |
prev
 |
next

[–]

I suspect people are misdiagnosing the root cause of why Anthropic is doing this a bit.

I don't think this is particularly about the financial impact of people using OpenClaw - they can adjust the amount of tokens in a subscription quite easily.I think the root cause is that Anthropic is capacity constrained so is having to make choices about the customers they want to serve and have chosen people who use Claude Code above other segments.We know Anthropic weren't as aggressive as OpenAI through 2025 in signing huge capacity deals with the hyperscalers and instead signed smaller deals with more neo-clouds, and we know some of the neo-clouds have had trouble delivering capacity as quickly as they promised.We also know Claude Code usage is growing very fast - almost certainly faster since December 2025 than Anthropic predicted 12 months ago when they were doing 12-month capacity planning.We know Anthropic has suffered from brown-outs in Claude availability.Put this all together and a reasonable hypothesis is that Anthropic is choosing which customers to service rather than raising prices.

reply

wigglewoggle

7 hours ago

 |
parent
 |
next

[–]

I'm at large company and pretty much everyone has settled on opus or sonnet 4.6. We would absolutely not allow something like OpenClaw on our network so your point kinda fits here where, if capacity is constrained, then by setting focus away from OpenClaw you're essentially prioritising the enterprise clients.
Just spitballing of course

reply

nl

7 hours ago

 |
root
 |
parent
 |
next

[–]

Yes exactly.

I doubt they actuallywantto do this.They clearly see having a wide set of paying customers as valuable (otherwise they'd just raise prices) but if you are stuck having to make hard choice then I can see the attraction of this approach.

reply

manmal

4 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> not allow something like OpenClaw on our network

And where’s the difference between the Claude Desktop app and OpenClaw at this point? Anthropic have been hard at work porting the most important features. You can easily shoot yourself in the foot with both now.

reply

stingraycharles

1 hour ago

 |
root
 |
parent
 |
next

[–]

Claude Desktop is an Anthropic product, Openclaw is not (their founder works for OpenAI even).

Anthropic wants you to use their subscription only for Anthropic products.I don’t think the difference is that difficult to see.

reply

manmal

24 minutes ago

 |
root
 |
parent
 |
next

[–]

Both teams ship at breakneck speed and both randomly regress. I don't see such a big difference. Claude now uses Claude by default to judge whether a tool call is sane or not. At least OC is transparent about the insanity of running bash commands unchecked.

reply

croes

24 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I guess parents point how dangerous OpenClaw is and that Claude Code is now similarly dangerous

reply

theshrike79

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

We have a legal contract with Anthropic

OpenClaw and OpenCode are open source projects with zero warranty and nobody to sue if they have a npm Trojan in them

reply

lelanthran

1 hour ago

 |
root
 |
parent
 |
next

[–]

> OpenClaw and OpenCode are open source projects with zero warranty and nobody to sue if they have a npm Trojan in them

When has any technology company been sued for pushing accidental malware in their updates?The reality is that you haveneverhad anyone to sue.

reply

ahtihn

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

So you don’t use any other open source software at all then?

The risk with OpenClaw et al isn't that the software itself is compromised. The risk is that what itdoesis fundamentally insecure and Claude Code isn't any better

reply

stingraycharles

1 hour ago

 |
root
 |
parent
 |
next

[–]

That’s not the issue, the issue is that people are using their subscriptions (intended only for use with Anthropic products) with non-Anthropic products and this is simply Anthropic enforcing their ToS.

reply

Alifatisk

1 hour ago

 |
prev
 |
next

[–]

Skimming through the comments, it feels like I am reading the same message over and over. I agree with some comments that are pointing out the issue with Anthropics capacity constraints and when Subscription vs Api is appropriate.

I would like to point out something else. I have Z.ai subscription and they have a dashboard on my usage.When trying out Openclaw a while ago, I noted something worrying. Its constantly consuming tokens, every single hour during the day, it consumed tokens. I could see over a period of 30 days, token usage would climb and climb and climb and then shrink to bottom again, as if Openclaw did a context window compaction.Note, this usage was happening even though I wasn’t using it. It were always running and doing something in the background.I believe its their Heartbeat.md mechanism. By default it’s set to run every half an hour. I changed it to twice a day, that was enough to me.I can imagine if thousands of users where connecting their Openclaw instance with default config to Claude with the latest and greatest Opus model, that must’ve felt a bit.

reply

g-mork

11 hours ago

 |
prev
 |
next

[–]

My answer to this is simply rolling back to the pro plan for interactive usage in the coming month, and forcefully cutting myself over to one of the alternative Chinese models to just get over the hump and normalise API pricing at a sensible rate with sensible semantics.

Dealing with Claude going into stupid mode 15 times a day, constant HTTP errors, etc. just isn't really worth it for all it does. I can't see myself justifying $200/mo. on any replacement tool either, the output just doesn't warrant it.I think we all jumped on the AI mothership with our eyes closed and it's time to dial some nuance back into things. Most of the time I'm just using Opus as a bulk code autocomplete that really doesn't take much smarts comparatively speaking. But when I do lean on it for actual fiddly bug fixing or ideation, I'm regularly left disappointed and working by hand anyway. I'd prefer to set my expectations (and willingness to pay) a little lower just to get a consistent slightly dumb agent rather than an overpriced one that continually lets me down. I don't think that's a problem fixed by trying to swap in another heavily marketed cure-all like Gemini or Codex, it's solved by adjusting expectations.In terms of pricing, $200 buys an absolute ton of GLM or Minimax, so much that I'd doubt my own usage is going to get anywhere close to $200 going by ccusage output. Minimax generating a single output stream at its max throughput 24/7 only comes to about $90/mo.

reply

Syntaf

6 hours ago

 |
parent
 |
next

[–]

I put in probably thousands of Claude session hours a month, aggregated across work + personal.

I must be missing something or supremely lucky because I feel like I’ve never hit these “stupid” moments.If I do, it’s probably because I forgot to switch off of haiku for some tiny side thing I was doing before going back to planning.

reply

g-mork

1 hour ago

 |
root
 |
parent
 |
next

[–]

It's possible that it's simply paranoia, but moments where Opus starts acting like Haiku seem to correlate with periods of higher latency and HTTP errors. Don't like reporting this because it's so hand-wavy and conspiratorial, but it's difficult not to think they're internally using extraordinary measures of some sort to manage capacity.

But even when Opus is running healthy, it still doesn't address the underlying issue that these models can only do so much. I have had Opus build out a bunch of apps but I'm still finding my time absorbed as soon as it comes to anything genuinely exceeding "CRUD level difficulty". Ask it to fix a subtle visual alignment issue, make a small change to a completely novel algorithm, or just fix a tiny bug without having to watch for "Oh, this means I should rewrite module <X>" is something that simply isn't possible while still being able to stand over the work.It's not to say I don't get a massive benefit from these tools, I just think it's possible to be asking too much of them, and that's maybe the real problem to solve.

reply

hakanderyal

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

Similar usage here. But I encountered this moments, and I chalk it up to the random nature of LLMs. Back in Sonnet 3.5 days, it would happen every other day. I even build an 'you are absolutely right' tracker back then to measure it. Opus 4.6, maybe once or twice a month.

reply

SkyPuncher

11 hours ago

 |
parent
 |
prev
 |
next

[–]

I literally hit my 5 hour window limit in 1.5 hours every single day now.

2 weeks ago, I had only hit my limit a single time and that was when I had multiple agents doing codebase audits.

reply

perfmode

2 hours ago

 |
root
 |
parent
 |
next

[–]

Are you monitoring the size of your context windows? As they grow, so does the cost of every operation performed in that state.

reply

Aurornis

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

Anthropic had a special extra usage promotion going on during non-peak hours that ended recently.

They didn’t do a great job of explaining it. I wonder how many people got used to the 2X limits and now think Anthropic has done something bad by going back to normal

reply

stavros

9 hours ago

 |
root
 |
parent
 |
next

[–]

They also reduced the peak time limits, so it's not just the promotion.

reply

SkyPuncher

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

Naw, it's not that. This is business-day usage for all of it.

reply

greenavocado

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

Irrelevant. I had at least ten times more usage then at any time

reply

paulddraper

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

Could it also have anything to do with Anthropic being deliberately opaque about usage in general?

reply

estimator7292

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

They've been running a "double credits" promo for several weeks, which expired on the first of this month.

reply

Razengan

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

I've been using Codex extensively, 5.4 at "Extra High" and yet to hit a limit. The $20 plan

reply

scotty79

1 hour ago

 |
root
 |
parent
 |
next

[–]

It very much depends on the workloads. If you inspect existing code (that somebody else wrote over the years) usage runs out quickly. If you are building your own greenfield stuff the sky is the limit.

reply

bethekind

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I think my next steps are:
1) try out openai $20/month. I've heard they're much more generous.
2) try out open router free models. I don't need geniuses, so long as I can see the thinking (something that Claude code obfuscates by default) I should be good. I've heard good things about the CLIO harness and want to try openrouter+clio

reply

Flere-Imsaho

3 hours ago

 |
root
 |
parent
 |
next

[–]

I'm taking a bet on local models to do the non genius work. Gemma 4 (released yesterday) has been designed to run on laptops / edge devices....and so far is running pretty well for me.

reply

neal_jones

1 hour ago

 |
root
 |
parent
 |
next

[–]

How’s Gemma 4 been?

reply

renewiltord

56 minutes ago

 |
root
 |
parent
 |
next

[–]

Edge models are good for their purpose but putting them in agentic flow with current ollama quants on a Mac Mini I see high tool use error rate and output hallucination.

For JSON to text formatting it works well on a one-round basis. So I think you should realistically have an evaluation ready to go so you can use it on these models. I currently judge them myself but people often use a smart LLM as judge.Today writing eval harness with Claude is 5 min job. Do it yourself so you can explore as quants on Gemma get better.

reply

beering

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

Word on the street is that Opus is much much larger of a model than GPT-5.4 and that’s why the rate limits on Codex are so much more generous. But I guess you could also just switch to Sonnet or Haiku in Claude Code?

reply

merlindru

2 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

i tried out gpt 5.4 xhigh and it did meaningfully worse with the same prompt as opus 4.6. like, obvious mistakes

reply

admiralrohan

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

Openrouter free models have 50 requests per day limit + data collection. As per their doc.

reply

nodja

8 hours ago

 |
root
 |
parent
 |
next

[–]

You can charge $10 on the account and get unlimited requests. I abused this last week with the nemotron super to test out some stuff and made probably over 10000 requests over a couple of days and didn't get blocked or anything, expect 5xx errors and slowdowns tho.

reply

danpalmer

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Please don't use grossly offensive terms in this forum. That sort of language is not welcome here.

reply

g-mork

10 hours ago

 |
root
 |
parent
 |
next

[–]

Oops, fixed

reply

klohto

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

Since when are you a moderator?

reply

imp0cat

1 hour ago

 |
root
 |
parent
 |
next

[–]

Since when are you a meta-moderator? ;)

reply

zdragnar

11 hours ago

 |
parent
 |
prev
 |
next

[–]

> I think we all jumped on the AI mothership with our eyes closed

Oh no, there's plenty of us willing to say we told you so.What's more interesting to me is what it's going to look like if big companies start removing "AI usage" from their performance metrics and cease compelling us to use it. More than anything else, that's been the dumbest thing to happen with this whole craze.

reply

colechristensen

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Every service is being sold at a deep discount chasing market share, but it's not lasting forever.

reply

g-mork

10 hours ago

 |
root
 |
parent
 |
next

[–]

Speaking only personally of course, I'm completely over the chat idiom in almost every way. Where is all this future demand coming from? By the time Android lands a God mode ultimate voice assistant it's pretty much guaranteed I will be well beyond the point where I'd want to use it. The whole thing is starting to remind me of 3G video calling where the networks thought it'd change everything, and by the end of it with all the infrastructure in place, the average user has made something like 0.001 3G-native video calls over the lifetime of their usage.

Would really love some path forward where the AI parts only poke out as single fields in traditional user interfaces and we can forget this whole episode

reply

colechristensen

10 hours ago

 |
root
 |
parent
 |
next

[–]

I don't understand this perspective. I can't imaging a point where I won't want to ask "what's the weather like?" "please turn off the lights" "what is the airspeed of an unladen swallow?" likewise chatting through directing it to build something or solve a problem, voice or typing will each have their place.

And video calling did take off, plenty of people use facetime and almost everybody working in an office uses some form of video calls. Criticizing the early attempts at getting video calling working because they hadn't taken off yet (I remember them being advertised on "video phones" with 56k modems), of course someone was going to have the idea and implement before it was quite reasonable.

reply

neonstatic

9 hours ago

 |
root
 |
parent
 |
next

[–]

> I can't imaging a point where I won't want to ask "what's the weather like?" "please turn off the lights"

To help with understanding that perspective, I cannot imagine a scenario where I would ask a device connected to the internet to turn off the lights. I literally never wanted this. A physical switch is a 100% non negotiable for me. I feel the same way about non-mechanical car doors.Perhaps due to that outlook I was always puzzled about the entire idea of an "assistant". It's interesting for me to see, that there are people out there who actually want that "assistant".

reply

Barbing

4 hours ago

 |
root
 |
parent
 |
next

[–]

The switch is a necessity.

Ever end up cooking or something when the phone/doorbell rings and you want to pause the music? Have your hands full and wanted to open a door? Hear the weather and then the news as you brew coffee or put your shoes on (without interaction with a bright screen)?You should save some money and keep some privacy doing it your way :)

reply

wat10000

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

You don't watch Iron Man and want a JARVIS? Current systems are pretty far away from that, but that's the overall draw.

reply

neonstatic

6 hours ago

 |
root
 |
parent
 |
next

[–]

I don't watch superhero stuff. But even with a more classical example of Space Odyssey 2001 - a talking computer has never been something I found even remotely interesting. It took me months to give LLMs a serious try due to this.

reply

codybontecou

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Are you using the Chinese models through their individual services or via an intermediary layer?

reply

rhodysurf

9 hours ago

 |
parent
 |
prev
 |
next

[–]

This is what I did, downgraded to pro and pay for opencode zen for the open models. I like the combo of the two

reply

Aurornis

10 hours ago

 |
parent
 |
prev
 |
next

[–]

> I think we all jumped on the AI mothership with our eyes closed and it's time to dial some nuance back into things.

I’m kind of confused by these takes from HN readers. I could see LinkedIn bros getting reality checked when they finally discover that LLMs aren’t magic, but I’m confused about how a developer could go all-in on AI and not immediately realize the limitations of the output.

reply

krupan

3 hours ago

 |
root
 |
parent
 |
next

[–]

It has indeed been baffling. Ad I dig deeper into what developers are doing with AI, it's basically like what I did customizing and tweaking emacs when I was younger (and fine, I'll admit I still do it sometimes). They are having so much fun playing with these new tools that they aren't really noticing how little the new tools are actually helping them

reply

Flere-Imsaho

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

> immediately realize the limitations of the output.

I'm "all-in" on AI code generation. I very much realise their limitations, it's like any tool really. I do think they're magic, you just need to learn how to weld the power.

reply

firloop

11 hours ago

 |
prev
 |
next

[–]

This is slightly different from what OpenCode was banned from doing; they were a separate harness grabbing a user’s Claude Code session and pretending to be Claude Code.

OpenClaw was still using Claude Code as the harness (via claude -p)[0]. I understand why Anthropic is doing this (and they’ve made it clear that building products around claude -p is disallowed) but I fear Conductor will be next.[0]: See “Option B: Claude CLI as the message provider” herehttps://docs.openclaw.ai/providers/anthropic#option-b-claude...

reply

userbinator

10 hours ago

 |
parent
 |
next

[–]

and they’ve made it clear that building products around claude -p is disallowed

Imagine not being able to connect services together or compose building-blocks to do what you want. This is absolute insanity that runs counter to decades of computing progress and interoperability (including Unix philosophy); and I'm saying this as someone who doesn't even care for using AI.

reply

4b11b4

10 hours ago

 |
root
 |
parent
 |
next

[–]

But you can still integrate this (claude -p) into your local workflows when you basically want to pipe pipe stuff to Claude for inference

reply

Aperocky

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

it's trivial to use tmux. But it does feels like openclaw is used (and increasingly developed) by people who never heard of it.

reply

colechristensen

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

You absolutely can, just pay for their API usage. The subscriptions are deeply discounted if you use your full quota compared to the API.

reply

mccoyb

10 hours ago

 |
root
 |
parent
 |
next

[–]

It is confusing for a company to sell you the subscription service, say "Claude Code is covered", ship Claude Code with `claude -p`, and then say "oh right, actually, not _all of Claude Code_, don't try and use it as a executable ... sorry, right, the subscription only works as long as you're looking at that juicy little Claude Code logo in the TUI"

The disrespect Anthropic has for their user base is constant and palpable.

reply

the_other

3 hours ago

 |
root
 |
parent
 |
next

[–]

You could think about it this way:

All AI prices will rise soon - probably shortly after the IPOs. The new prices will be eyewatering compared with today’s. This bulling change is lengthening the time until Anthropic have to raise the subscription prices, so those of us who’re not doing 24hr claw stuff can continue to use the tools the way we’ve gotten used to.

reply

colechristensen

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

This strikes me the same way the people in college who would print 497 empty pages at the end of the semester for the quota "they'd paid for" or that one guy who made lemonade at restaurants with the free lemon wedges and sugar packets. "Contempt for users" is silly. Adjusting terms to handle users who use things as not intended isn't contempt.

reply

mccoyb

9 hours ago

 |
root
 |
parent
 |
next

[–]

Contempt for users is not silly when the CEO of said company has repeatedly claimed they will replace SWEs "end-to-end" by next year.

I'm not sure what to say. You're either listening to the actions of these companies, or you're not in a place where you feel the need to be concerned be their actions.I'm in a place where I'm concerned by their actions, and the impact that their claims and behavior have on the working environment around me.

reply

serial_dev

5 hours ago

 |
root
 |
parent
 |
next

[–]

Did he say they will replace SWEs, or maybe something more nuanced, that code will be written by AI tools?

Honest question from my end, I try to not read every AI related news that keeps telling me “it’s over, good luck feeding your family in 9-12 months”.

reply

colechristensen

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

At no point in the last 10,000 years of human civilization has there not been a developing technology that threatened to forever reshape and displace a class of labor.

Or are you also upset about the modern plight of the telephone operator, farrier, or coal miner?

reply

mccoyb

9 hours ago

 |
root
 |
parent
 |
next

[–]

I see -- and AI is just like all technologies that came before it ...

It is nota class of labor... it is all digital labor. Do you or do you not understand this?It is digital knowledge itself, and then all communication labor, and then allphysicallabor with robotics.Is this clear to you?

reply

NewsaHackO

8 hours ago

 |
root
 |
parent
 |
next

[–]

Are SWE's the only digital labor job?

reply

colechristensen

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

And? Hyperbolic fear of change always exists and there's always been more work.

Marx' whole idea of Communism was predicted on the fact that he assumed industrialization would lead to a post-scarcity society requiring virtually no work and a overhaul of how everything was owned and produced. Boy was he wrong.

reply

xvector

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

Oh nooo, labor might be automated and we might see advancement that makes the Industrial Revolution look small! Oh, the humanity! Please someone, stop progressing humanity, I need to cling to my sticks!

reply

zmmmmm

9 hours ago

 |
parent
 |
prev
 |
next

[–]

> building products around claude -p

But OpenClaw is not a product. It's just a pile of open source code that the user happens to choose to run. It's the user electing to use the functionality provided to them in the manner they want to. There's nothing fundamental to distinguish the user from running claude -p inside OpenClaw from them running it inside their own script.I've mostly defended Anthropic's position on people using the session ids or hidden OAuth tokens etc. But this is directly externally exposed functionality and they are telling the user certain types of uses are banned arbitrarily because they interfere with Anthropic's business.This really harms the concept of it as a platform - how can I build anything on Claude if Anthropic can turn around and say they don't like it and ban me arbitrarily.

reply

beering

9 hours ago

 |
root
 |
parent
 |
next

[–]

Claude Code is not a platform and you’re not meant to be building on it. Netflix is also not a platform and you shouldn’t be running code (open source or not) to mass download Netflix movies either.

reply

zmmmmm

9 hours ago

 |
root
 |
parent
 |
next

[–]

It's a reasonable comment, and I should be clear, I don't expect it to be a platform. But I do expect to be able to use its advertised features for any reasonable purpose they can support.

Where it leaves me is is sort of like the DoD - nobody should use Claude for anything. Because Anthropic has set as principle here that if they don't like what you do, they will interfere with your usage. There is no principle to guide you on what they might not like and therefore ban next. So you can't do anything you want to be able to rely on. If you need to rely on it, don't use Claude Code.And to be clear, I'm not arguing at all against using their API per-token billed services.

reply

mccoyb

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

https://code.claude.com/docs/en/overview#what-you-can-do

Try this one:https://code.claude.com/docs/en/overview#run-agent-teams-and...Or perhaps:https://code.claude.com/docs/en/overview#pipe-script-and-aut...You know what they say about looking and quacking.

reply

nextaccountic

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

Is using claude -p supposed to be dangerous? Could someone be confused as openclaw or other things?

If yes, why do Anthropic provide this cli flag?

reply

freedomben

11 hours ago

 |
parent
 |
prev
 |
next

[–]

Ah thank you, this is very helpful distinction to know.

When they shut down open code, I thought it was a lame move and was critical of them, but I could understand at least where they're coming from. With this though, it's ridiculous. Claude core tools are still being used in this case. Shelling out to it to use it there's no different than a normal user would do themselves.If this continues, I'll be taking my $200 subscription over to open AI.

reply

sunsunsunsun

10 hours ago

 |
root
 |
parent
 |
next

[–]

Im still using opencode with claude pro so im confused.

reply

stavros

10 hours ago

 |
root
 |
parent
 |
next

[–]

You're using it with a PAYG API key, not a subscription.

reply

xvector

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

No a normal user is not shelling out to Claude Code 24/7, but OpenClaw certainly is.

OpenAI will soon do the same thing, don't be delusional.

reply

sethherr

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I’m also terrified of this.

When this happens I will have to look at other providers and downgrade my subscription. Conductor is just too powerful to give up. It’s the whole reason why I’m on a max plan.

reply

loveparade

11 hours ago

 |
parent
 |
prev
 |
next

[–]

I assume this means we can no longer use Claude code sessions in editors like zed because it also wraps claude cli via ACP?

reply

upcoming-sesame

3 hours ago

 |
root
 |
parent
 |
next

[–]

ACP was a good idea but I feel it has not lived up to its potential.

reply

andai

11 hours ago

 |
parent
 |
prev
 |
next

[–]

Why are they doing that? Opus is the only good way to run Claw. Do they regret making it cheaper or what?

Also what's the point of Claude -p if not integration with 3rd party code? (They have a whole agents SDK which does the same thing.. but I think that one requires per token pricing.) I guess they regret supporting subscription auth on the -p flag

reply

happyopossum

9 hours ago

 |
root
 |
parent
 |
next

[–]

> Opus is the only good way to run Claw

that's a ridiculous position to take - gemini and others work just great with claw...

reply

andai

3 hours ago

 |
root
 |
parent
 |
next

[–]

Well, it might have been cargo culting but that was the consensus in the OC community a while ago.

reply

randall

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

exactly. They probably have unsustainable margins on accident.

reply

adastra22

8 hours ago

 |
parent
 |
prev
 |
next

[–]

Has there been an actual change to their ToS? As of the last change which I saw reach HN, a week or so ago, `claude -p` was still in compliance with the Claude Code ToS. Has that language changed?

reply

wild_egg

11 hours ago

 |
parent
 |
prev
 |
next

[–]

I keep hearing OpenClaw runs on pi?

EDIT: confused by downvotes. In this thread people are saying it runs on top of `claude -p` and others saying it's on pi.The `claude -p` option is allowed perhttps://x.com/i/status/2040207998807908432so I really don't understand how they're enforcing this.

reply

nc

1 hour ago

 |
root
 |
parent
 |
next

[–]

It runs on pi, not claude -p

reply

kzahel

1 hour ago

 |
root
 |
parent
 |
next

[–]

That's my understanding too, though i haven't checked it. running claude -p would be horribly inefficient.
I would not be surprised if openclaw added some compatibility layer to brute force prompts through claude -p as a workaround. This isn't the first time that openclaw was "banned" from claude subscriptions.

reply

juanre

18 minutes ago

 |
prev
 |
next

[–]

I am genuinely curious about OpenClaw's continuing allure. I understood it way back then, when Claude Cowork did not have channels and scheduled tasks. But now? Has Claude not become a sane replacement for OpenClaw? I can see that it's fun to play with OpenClaw and non-SOTA providers, but why would anyone run OpenClaw on a Claude Code subscription?

reply

armanj

7 hours ago

 |
prev
 |
next

[–]

People in the comments are, in my opinion, overcomplicating this and making it more philosophical than it needs to be. The reason for their decision is dead simple: there aren’t enough GPUs, so they have to cut access somewhere, and they’re starting with claw.

It’s really that straightforward. If tomorrow they decide GPUs are better allocated to enterprise use, they could start removing the $20 plan just as quickly overnight, the same way they did tonight.

reply

password4321

11 hours ago

 |
prev
 |
next

[–]

GitHub Copilot supports Anthropic models with any client but they have a monthly usage cap after which it is pay-per-prompt.

https://news.ycombinator.com/item?id=46936105Billing can be bypassed using a combo of subagents with an agent definition>"Even without hacks, Copilot is still a cheap way to use Claude models"20260116https://github.blog/changelog/2026-01-16-github-copilot-now-...https://github.com/features/copilot/plans$40/month for 1500 requests; $0.04/request after thathttps://docs.github.com/en/copilot/concepts/billing/copilot-...Opus uses 3x requests

reply

briHass

8 hours ago

 |
parent
 |
next

[–]

GHCP also has magical rate limits that hit users that slam multi-agent workflows or other crazy request burners.

Mind you, I think GHCP is a great service at an excellent price, but the hardcore vibe coders complain about the rate limits that I've never personally experienced using the CLI.

reply

59nadir

4 hours ago

 |
root
 |
parent
 |
next

[–]

That's weird, because every time I see someone even talking positively about Claude Code they always seem to mention they're hitting their 5 hour limits in 2-3 hours all the time, they're hitting their overall limits all the time, and so on.

Meanwhile I can't even seem to spend my $20 Cursor Composer 2 tokens using their agent. I've been doing useless shit just to see how much usage I can cram in there and it'd probably take 10 hours of vibecoding like a loser every day to hit the limits at this point.With that said I'm not going to pay for something that doesn't allow me to use whatever I want to use (in terms of harness, etc.), so both Anthropic (who were already disqualified because of their ridiculous limits) and Cursor is out (AFAIK you can't an agent other than their `agent` binary without some ridiculous hack like proxying all of the calls through `agent`.I can't imagine all of the providers pretending their agents are real value going forward, but even if they do there's still stuff like OpenRouter which doesn't give a shit, may as well use something like that.

reply

sunaookami

2 hours ago

 |
parent
 |
prev
 |
next

[–]

Don't jinx it!

reply

hooch

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Last time I looked Copilot's context window for Anthropic models was something like 150,000 tokens only.

reply

2001zhaozhao

11 hours ago

 |
prev
 |
next

[–]

There are going to be a lot of tools coming soon that are "agent-agnostic", i.e. can run on CLIs including Claude Code. I am personally experimenting with using a combo of MCP + custom UI layer to provide custom tools with bespoke UX and thus turn Claude Code (or any other CLI agent for that matter) into whatever I want. I wonder how they'll deal with that.

For a good existing example developed by a known company, check Cline Kanban:https://cline.bot/kanbanThey don't have the MCP-bundling idea that I'm experimenting with, however.

reply

pxc

10 hours ago

 |
parent
 |
next

[–]

Some editor integrations are a bit like this already, where during use you don't actually touch the built-in TUI even for prompting or viewing the output and approving permissions requests.

I imagine how they treat these things will be contextual and maybe inconsistent. There aren't really hard lines between what they probably want editors that integrate with them to do and generic tools that try to sit a layer above the vendors' agent TUIs.

reply

ChildOfChaos

55 minutes ago

 |
prev
 |
next

[–]

I’m feel like the decent AI models are going to become out of reach for normal people soon enough.

Even the $20 subscription is ridiculously limited and they keep adding more and more limits. The $200 a month sub is insane and only going to get worse and yet still limited

reply

noritaka88

10 hours ago

 |
prev
 |
next

[–]

This feels less like a pricing issue and more like a structural mismatch.

Subscriptions assume “human usage” — bursty, limited, mostly interactive. Agent systems are closer to autonomous infrastructure load running continuously.OpenClaw is a good example of this. Once agents operate freely, they don’t behave like users — they behave like infrastructure.That’s why this kind of restriction isn’t too surprising.Long term, it seems likely this pushes things toward:
- API-first usage
- or local / open modelsrather than agents sitting on top of subscription-based UIs.

reply

Fogest

7 hours ago

 |
parent
 |
next

[–]

I am pretty sure Claude Code limits were being hit so fast recently because there was an increasing amount of OpenClaw style usage on the subscription. From tweets from the people in charge it sounded like they were having more usage than they expected which was causing them to have to be more aggressive on the rate limits. They said they were working to address it soon. I have a feeling this is what they were working on changing. I bet OpenClaw was the reason for the rate limiting being so bad lately.

I'm hoping with this change we see the rate limits start to not be as rough.

reply

dnw

9 hours ago

 |
prev
 |
next

[–]

To give credit where it is due: Boris actually submitted a few PRs this week to OpenClaw to increase prompt cache hits. You can see them here:

https://github.com/openclaw/openclaw/pullsq=is%3Apr+author%3...

I think the usage patterns of a lot of harnesses are pushing against their planned capacity. I would say they can certainly explain themselves a lot better.

reply

admiralrohan

8 hours ago

 |
parent
 |
next

[–]

Link is broken.

reply

cormorant

8 hours ago

 |
root
 |
parent
 |
next

[–]

missing a ? character.
https://github.com/openclaw/openclaw/pulls?q=is%3Apr+author%...

reply

nvalis

1 hour ago

 |
root
 |
parent
 |
next

[–]

I can't see any results any more.

reply

dnw

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

Thank you!

reply

Multiplayer

11 hours ago

 |
prev
 |
next

[–]

Big Giant Million Dollar Question: Where does having Openclaw using Claude Code via ACP fall? It's using the Claude Code harness, not the model directly.

If you are not aware, ACP creates a persistent session for steering rather than using the models directly.

reply

nextaccountic

4 hours ago

 |
parent
 |
next

[–]

The Zed ACP client for example is still controlled by the human prompt, and they will probably not be banned

reply

Aperocky

8 hours ago

 |
parent
 |
prev
 |
next

[–]

I have no idea what ACP offers that are superior to a tmux session. With tmux, you can attach to it at any time, send keys at any time, and capture pane without bothering any running process inside.

And you don't have to get anyone's permission to use tmux.

reply

bontaq

11 hours ago

 |
parent
 |
prev
 |
next

[–]

This is my big question too. It seems by intent it's to kill it, including ACP, but I don't know.

reply

alasano

12 hours ago

 |
prev
 |
next

[–]

"these tools put an outsized strain on our systems"

AKA when you fully use the capacity you paid for, that's too much!

reply

danpalmer

10 hours ago

 |
parent
 |
next

[–]

You don't pay for capacity, you pay for an interface. Paying for capacity is what API keys are for.

Similarly, on a home internet connection you might pay for a given size of pipe, but most residential ISPs don't allow running publicly accessible servers on your connection because you'll typically use way more of the bandwidth.

reply

GandalfHN

5 hours ago

 |
root
 |
parent
 |
next

[–]

That analogy fails.
Anthropic sold a Claude Code subscription, then blocked OpenClaw and narrowed the practical use case after the sale, which reads more like an airline overbooking and then claiming you bought a seat, not a flight.

API and subscription are different products, sure.
The vendor still sets the line between flat-rate access and rate limits, and that line looks slippery once your usage leaves the preferred path.

reply

imtringued

18 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

This is probably one of the worst analogies you could have brought up in this context.

The business model of an ISP involves fixed capital investments into infrastructure with constant opex and very little variable costs.The marginal cost of sending a gigabyte is basically zero. The limited resource here is bandwidth and ISPs split their tiers based on bandwidth.The problem is that some users may consume the local bandwidth that is shared with other users. More bandwidth requires more investment into infrastructure. This means that bandwidth in itself doesn't produce costs for the ISP either, it is the maximum bandwidth capacity that costs money.Hence, oversubscription is a viable business as long as neighbors aren't impacted by power users.This doesn't apply to LLMs. Token economics has the same economics as steel. There is high capex to get started, but the real killer is the variable cost per unit of steel.You can't sell steel on a oversubscribed subscription model. It's nonsensical.If the subscription is more expensive than buying what you need, nobody is going to pay for the subscription unless they consume all of it.Hence the subscription must contain a subsidy to make it competitive.However, the people who consume the full subscription are still there and each token they request adds up on your electricity bill.Ergo, the subscription must be more expensive than the API, but with a smart billing limit that removes the cognitive burden of using your service with pay as you go billing.

reply

alasano

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

If that same internet provider has caps on how much bandwidth I can use every 5 hours and total on a weekly basis, then yes, I pay for capacity.

That argument would have been valid when the 5 hours blocks were unlimited in the beginning.

reply

Jimmc414

9 hours ago

 |
parent
 |
prev
 |
next

[–]

I’m not sure why people expect Anthropic to subsidize tokens through Open Claw when it’s specifically forbidden in the ToS.

reply

topherhunt

1 hour ago

 |
root
 |
parent
 |
next

[–]

^ This. I get that We Are On The Internet And People Will Be Wrong Sometimes -- but I'm really confused by the amount of people insisting that a subscription is just a slosh bucket of token capacity to be used however they feel like using it; are these people who genuinely misunderstand how subscriptions work or what Anthropic's terms were, and genuinely weren't aware that 3rd-party harnesses violate them? The vibe I get is more "how dare you constrain me from doing whatever I want", angry rebellious teenager vibe, willful oversimplifications of the situation... it doesn't feel particularly honest or reality-seeking.

reply

cortesoft

6 hours ago

 |
parent
 |
prev
 |
next

[–]

Except no, you aren't paying the full capacity of using all of your limits every time. The subscription cost is less than it would take to actually pay for the capacity of the limits. That is how these sorts of subscriptions work.

You can pay for the capacity, using the per token price.

reply

infecto

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Meh this argument does not hold up. If you don’t like it pay for the API. We all know these services are priced for human use, as in your not using it 24/7.

reply

onchainintel

19 minutes ago

 |
prev
 |
next

[–]

Read this earlier as well. A lot of OpemClaw jockets are going to wake up to some very unfriendly news! That said, spot on points re: subscription services biz model.

reply

Wowfunhappy

7 hours ago

 |
prev
 |
next

[–]

Claude is a UNIX command line tool with an SDK. Yes there's an interactive mode, but it can be invoked as a normal utility too, and piped to other tools and so on.

In that context, I don't understand the difference between a "third party harness" and a shell script.How are they even detecting OpenClaw?

reply

jatora

7 hours ago

 |
parent
 |
next

[–]

Im wondering this too. If I have my own local platform similar in nature to openclaw, and am leveraging claude -p through my subscription, is this now against ToS? Or is this just a ban specific to certain services? In which case they're saying 'use -p until you scale and then we'll hammer you'. Either way what a pita.

reply

anhldbk

3 hours ago

 |
parent
 |
prev
 |
next

[–]

I guess Anthropic will scrutinize big open source projects for that purpose. The direct official integrations will be removed.

reply

mohsen1

5 hours ago

 |
parent
 |
prev
 |
next

[–]

They have terms to not allow `claude -p` used like that. However, people can hide this with the leaked source code. What a funny cat-and-mouse game!

reply

ramon156

4 hours ago

 |
prev
 |
next

[–]

May I suggest trying Z.ai coding plan? I've had a good experience, and its 1/3rd of the price.

When I do use AI, I already have a solid plan of what I need. Sometimes I ask it to look something up. I never do both in one prompt.GLM 5.1 can do both, and its way way cheaper. I also don't hit my limit that fast (Plus I get to use it in OpenCode).

reply

Alifatisk

1 hour ago

 |
parent
 |
next

[–]

Now is also a good time because they have a discount offer this month for using GLM-5-Turbo. During off-peak hours, only 1x multiplier will be deducted (otherwise it is 2x). I’m am on the Lite plan and have never maxed my usage quota (their Christmas deal offered 3 month for 7$).

reply

breisa

1 hour ago

 |
parent
 |
prev
 |
next

[–]

They also do not allow non-coding usage of their coding plan in their ToS.

reply

upcoming-sesame

3 hours ago

 |
parent
 |
prev
 |
next

[–]

which plan do you suggest ? 80$/m ?

reply

karlpoppery

4 hours ago

 |
prev
 |
next

[–]

Is any code that auto launches Claude Code considered a "harness"?

I'm hoping that they won't bother you unless you specifically max out the subscription limits every time

reply

dabeeeenster

1 hour ago

 |
parent
 |
next

[–]

I don't see where they are going to draw the line. If I run 4 sessions in tmux, all connected to claude code, is that OK?

reply

datahack

10 hours ago

 |
prev
 |
next

[–]

Ok. Someone explain to me why they would f themselves this hard with software engineers when they are absolutely winning. This just seems like a bad move.

Is it infrastructure? Are they unable to control costs?Everyone else is spending like money is water to try to get adoption. Claude has it and is dialing back utility so that its most passionate users will probably leave.I don’t understand this move.

reply

vitaflo

10 hours ago

 |
parent
 |
next

[–]

Openclaw users are a small percentage of their user base but take up a lot of their compute. Given the cost is subsidized it’s not surprising they would target it. Getting these users to leave is probably the point. These aren’t profitable users.

reply

w10-1

10 hours ago

 |
parent
 |
prev
 |
next

[–]

"Adoption" like 2000's internet companies losing money on every sale to get market share?

For SaaS, use the SaaS API. For product, use the product.They subsidize the product with "don't care how much" pricing so they have users to build out features without users worrying about cost. If it's not actual users using the product, then features will be built in OpenClaw instead of Claude.The earlier they draw this line, the better.However, announcing it the day before it is effective is a huge unforced error, even if it were just a consequence of the TOS. They gain nothing by making people scramble.Also better to announce at the same new ways to support plugging in to Claude Code - something to encourage integration/cooperation. No fences unless the field inside is flowering.

reply

beering

9 hours ago

 |
parent
 |
prev
 |
next

[–]

They have so much mindshare right now that they can’t lose, and the number of users that use opencode and would be affected is miniscule—-on the level of complaining about your online bank not supporting Konqueror.

reply

ffsm8

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Honestly I suspect they're just getting ready to release a new feature for autonomous usage. I mean it was one of the leaked feature toggles. If I'm right it'll likely mean we'll get an announcement within the next 2 weeks for "long running prompts/agents"

reply

_pdp_

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I mean, it is easy to understand once you realise that there is no spoon.

Despite their power, frontier models are threatened by open-source equivalents. If AGI is not on the horizon and model performance is likely not going to be enough of a differentiator to keep the momentum going, the only other way is to go horizontal - enterprise solutions, proprietary coding agent harnesses, market capture, etc.If AGI is in sight, none of these short-term games really matter. You just need to race ahead.

reply

verdverm

10 hours ago

 |
parent
 |
prev
 |
next

[–]

They have plenty of high paying users that will soak up what the claws are consuming in capacity. They are thinking about those customers and delivering them a better experience

reply

tzury

5 hours ago

 |
prev
 |
next

[–]

Boris Cherny on this

https://x.com/bcherny/status/2040206440556826908?s=20

reply

kh_hk

4 hours ago

 |
prev
 |
next

[–]

The same reason I would not use a proprietary text editor applies to harnesses. It's enough of a constraint to use a proprietary service, for me the line is at the tooling. Sunk cost and all it's things.

reply

figmert

9 hours ago

 |
prev
 |
next

[–]

Can they actually realistically do this? Nothing technical can stop a client from masquerading as another, and with the right level of dedication, this wouldn't be very hard to do. And since they're mostly targeting power users, seems like they're barking up the wrong tree. Have I missed something?

reply

varenc

8 hours ago

 |
parent
 |
next

[–]

Realistically, they can likely prevent the majority of this sort of use. You're right that's it's impossible to prevent 100%, but they can likely stop most of it. Particularly because each user is linked with an account which has an extra high cost to the user if penalized. Abuse prevention is harder when you permit anonymous users. (Like OAI's battle against people turning the free logged out chatgpt.com into an API)

reply

fcanesin

1 hour ago

 |
prev
 |
next

[–]

Anthropic is a great showing for startup founders how if you have a great product people will buy it, even if they dislike your pricing, your marketing and the CEO opinions.

Real PMF sells itself. The risk is of course the competition catching up, I bet switching costs are very low on this setup.

reply

nfw2

9 hours ago

 |
prev
 |
next

[–]

I don't understand exactly what is being banned. I have a vibe coded context manager + chat thread UI that I use to manage multiple claude code cli sessions simultaneous. Is this allowed? If not how would this get identified vs other cli usage? How is this different than openclaw?

reply

Aperocky

8 hours ago

 |
parent
 |
next

[–]

openclaw is too easy to set up and way too messy and context heavy, they don't have to catch you they just have to catch the guy on the market giving out free modified V8 F150s while Anthropic are selling gas subscriptions in town.

reply

wolttam

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Check into the CC source leaks, they're doing some relatively sophisticated attestation

reply

luxuryballs

8 hours ago

 |
parent
 |
prev
 |
next

[–]

it’s not banned it will just charge to extra usage instead of going towards the sub when using setup token, you can allocate money to extra usage or make an anthropic api key and use that

reply

djhope99

10 hours ago

 |
prev
 |
next

[–]

Personally I appreciate the clarity and technical enforcement vs banning accounts.

I switched OpenClaw to MiniMax 2.7. This combined with Claude over telegram does enough for me.OpenClaw used to burn through all my Claude usage anyway.

reply

upcoming-sesame

2 hours ago

 |
parent
 |
next

[–]

how do you use Claude over telegram ?

reply

zephyreon

11 hours ago

 |
prev
 |
next

[–]

Yah well I'll be downgrading my subscription to the $20/month plan for the light chats I have with AI outside of using custom harnesses and will figure out a better provider for the agentic tooling.

reply

luxuryballs

8 hours ago

 |
parent
 |
next

[–]

couldn’t you just do that and put the other $80 towards extra usage and OpenClaw can use that?

reply

steveharing1

1 hour ago

 |
prev
 |
next

[–]

It seems like they are suffering from compute problems bcs they are not only allowing OpenClaw but also limiting the chats

reply

aimadetools

2 hours ago

 |
prev
 |
next

[–]

This is why I'm wary of vendor lock-in with these subscription models. It feels like bait and switch once they have your payment info.

reply

topherhunt

2 hours ago

 |
parent
 |
next

[–]

I don't get it - in what way is this bait-and-switch? Anthropic's terms have made it amply clear that your claude subscription can only be used with Anthropic-provided tools, not with 3rd-party harnesses. I imagine anyone who uses OpenClaw is AI-savvy enough to be aware of that, and happily flouted those terms anyway. If anything Anthropic seems overly accommodating here by giving all flouters a month of free credit, rather than simply saying "sorry yall but we're gonna start enforcing that thing our TOS has said from the start".

The premise of the subscription isn't "giant bucket of ultra-cheap tokens that you can use however you want", it's "giant bucket of ultra-cheap tokens that you can use with OUR tools, within reasonable limits". Even if their TOS didn't prohibit OpenClaw-oids, I wouldn't consider this bait-and-switch, I'd consider it a reasonable and needed move.

reply

gos9

9 hours ago

 |
prev
 |
next

[–]

I don’t understand why they’re catching any flak here lol if you want to use the frontier model more then pay for it?

Graceful handling from Anthropic

reply

hnburnsy

4 hours ago

 |
parent
 |
next

[–]

>Graceful handling from Anthropic

Less than 24 hours notice and on a holiday weekend

reply

luxuryballs

8 hours ago

 |
parent
 |
prev
 |
next

[–]

exactly! they actually chose the better approach rather than just locking us out

reply

hgoel

6 hours ago

 |
prev
 |
next

[–]

This seems like a reasonable move even putting aside the reasoning about breaking the assumptions that make a subscription model cheaper than a pay-per-use model.

Why would they actively subsidize the ticking timebomb? When OpenClaw has an especially large security incident, Anthropic will probably be affected just for the association.Like, right alongside this post on the front page, we have a post about a relatively serious privilege escalation vulnerability in OpenClaw.

reply

ph4te

6 hours ago

 |
parent
 |
next

[–]

As a CC power user, an OpenClaw, and ZeroClaw user, I am completely fine with this. My CC usage has suffered lately, and however cool and fun the Claws are, I use Claude Desktop probably more than OpenClaw and it works just fine, and has a lot of integrations. I would rather have Anthropic continue to support its own products working well, and have all of these things move to another service, or pay Anthropic for their use.

reply

sunaookami

1 hour ago

 |
prev
 |
next

[–]

It's the tragedy of the commons where OpenClaw users abuse the system and everyone has to suffer.

reply

ugiox

59 minutes ago

 |
prev
 |
next

[–]

Literally :rofl: here. About all the people panicking that they suddenly can’t work anymore. Come on, how did you work and develop three years ago without AI? If you can’t program or understand code without an LLM you should maybe switch careers and not call yourself engineers. In the meantime, I have never touched Claude, Copilot, or what not, and continue to write my low level code used in real engineering and manufacturing plants as well as science labs. And since most/all of this isn’t really working through/with AI (as some colleagues in the field have tried and miserably failed) I can increase my rates and have started to charge a good amount more from clients. As they can’t find people anymore that are willing to understand the problems and deliver working code. The people are busy trying to get AI work in the my field instead of doing the real work that is asked. Literally :rofl: on how AI makes me more money without having to use and touch it. If this continues as it does, I might be able to retire soon (40s) and go back to study physics as I did and maybe engage in some theoretical physics PHD (self financed).

reply

causal

10 hours ago

 |
prev
 |
next

[–]

Their whole business model seems built around selling you limits that you will never be able to utilize: limit you to tools that will never run long.

Claude Code seems designed to terminate quickly- mine always finds excuses to declare victory prematurely given a task that should take hours.

reply

Seattle3503

11 hours ago

 |
prev
 |
next

[–]

Am I still allowed to invoke cc in a bash script, or is that out too? Interactive sessions only.

reply

Larrikin

4 hours ago

 |
prev
 |
next

[–]

Some of the vigorous defending of Claude changing the deal, makes me wonder if Open Claw is banned because they have their own version they are working on deploying.

reply

arewethereyeta

11 hours ago

 |
prev
 |
next

[–]

Marketing geniuses. They had 2 options here:

1. Make a better product/alternative to Openclaw and start eating their userbase. They hold the advantage because the ones "using their servers too much" are already their clients so they could reach out and keep trying to convert. Openclaw literally brought them customers at the door.2. Do everyone royally and get them off their platform - with a strong feeling of dislike or hatred towards Anthropic.Let's see how 2 goes for them. This is not the space to be treating your clients this way.

reply

infecto

9 hours ago

 |
parent
 |
next

[–]

Such a small minority of the customers they want use openclaw and in aggregate a lot of compute use is coming from the total group. Better to stop customers you don’t want. This has zero impact on top line revenue

reply

mrbungie

11 hours ago

 |
parent
 |
prev
 |
next

[–]

From you can tell from they long-term strategy they are not marketing geniuses, but rather they try to signal are "moral geniuses". That's the game they are playing, I don't really know if it is going to work or not.

reply

airstrike

10 hours ago

 |
root
 |
parent
 |
next

[–]

marketing geniuses was never a real alternative if inference is heavily subsidized, because open models scale in performance just as well, albeit 12-18 months late

reply

subscribed

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Well, I don't use openclaw and I don't think it would be fair if everyone had to pay more to subscribe them.

Why hatred btw? They're not even banning accounts left and right like Google?

reply

krater23

44 minutes ago

 |
parent
 |
prev
 |
next

[–]

Not the software is the product, you know? The tokens are the product. Selling cheap subscriptions to power users costs them money. That are the customers you don't want, so why hesitate to get rid of them when they don't want to pay more?

reply

dboreham

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I'm fine with it. I don't want my subscription subsidizing the claw people.

reply

a10c

9 hours ago

 |
root
 |
parent
 |
next

[–]

How about the people that don't use OpenClaw, but alternative agent harnesses that are vastly better than Claude Code?

reply

bsder

9 hours ago

 |
root
 |
parent
 |
next

[–]

> alternative agent harnesses that are vastly better than Claude Code?

Okay,thatgot my attention. What harnesses are those?

reply

a10c

7 hours ago

 |
root
 |
parent
 |
next

[–]

pi-coding-agent (
https://shittycodingagent.ai/
) is what I use and is particularly popular due to its simplicity and minimal system prompt.

reply

arewethereyeta

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

Cursor - I'm sure I can find more.

reply

arewethereyeta

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

I think you value yourself too much over other people. What does it even mean "claw people"?

reply

nojito

10 hours ago

 |
parent
 |
prev
 |
next

[–]

>Make a better product/alternative to Openclaw and start eating their userbase.

There's a good chance they do not have the infrastructure to do that.

reply

luxuryballs

8 hours ago

 |
parent
 |
prev
 |
next

[–]

but are they really doing that? I mean it says you can keep using OpenClaw you just have to allocate money to the extra usage or an api token, I have no plan on not using it because Opus makes the claw so smart, I’ll just put more money towards the extra usage rather than the beefier sub

reply

loveparade

11 hours ago

 |
prev
 |
next

[–]

That's why I am using Codex. I slightly prefer Claude in terms of code quality, but it's close, but not being able to use my subscription with other CLIs and apps ruins Claude for me.

reply

freedomben

11 hours ago

 |
parent
 |
next

[–]

Indeed, this is the outcome they are going to create. It seems like their goal is to get people using their core tools, and they want that bad enough to subsidize it for some users. The net effect on users like me however, will be the exact opposite. I'll be switching to a different tool.

reply

loveparade

11 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah and it doesn't help that the claude CLI itself IMO isn't that great. It feels a bit like a sloppy vibe coded app. So they are forcing me to use an inferior product.

reply

SkyPuncher

11 hours ago

 |
prev
 |
next

[–]

Just give me a subscription tier where I’m not being blocked out every afternoon.

Im hitting rate limits within 1:45 during afternoons.I can’t justify extra usage since it’s a variable cost, but I can justify a higher subscription tier.

reply

bitpush

11 hours ago

 |
parent
 |
next

[–]

even higher than $200? gosh, what are you doing to hit limits every day?

reply

muyuu

10 hours ago

 |
root
 |
parent
 |
next

[–]

For me it's surprising that they expected anything other than heavy utilisation at that price point. People don't subscribe at those prices and forget about it.

reply

TillE

9 hours ago

 |
root
 |
parent
 |
next

[–]

All these companies are offering quite generous subscription plans if you compare to API pricing.

There's gotta be a limit; nobody can afford to have tons of users who are losing them money every month.

reply

muyuu

9 hours ago

 |
root
 |
parent
 |
next

[–]

Perhaps. So let them come clean about what they can offer. At that price, people are going to make the best of their subscription whatever it is that's on offer.

Time to compete on value with the Chinese.

reply

SkyPuncher

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

Professional software development. I literally have 2 to 5 terminals running all day.

reply

krater23

39 minutes ago

 |
root
 |
parent
 |
next

[–]

Sorry guy, this has nothing to do with professional software development :D

reply

rvz

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

Consulting fees from Claude & Ralph.

reply

sarchertech

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Based on the way subscriptions work for every other business, if you’re hitting the limits, you are not profitable for them.

My guess is a plan with double the limits would need to be 5-10x as expensive.

reply

SkyPuncher

8 hours ago

 |
root
 |
parent
 |
next

[–]

This is only an issue between 12pm and ~4pm ET. If I work at any other time of day, I never hit my usage limit.

reply

arjie

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Extra usage seems like the right thing for you. It's pre-paid so if you only ever fill in $100 more per-month it works as a higher subscription tier.

reply

charcircuit

11 hours ago

 |
parent
 |
prev
 |
next

[–]

You can set the monthly extra usage cap to $1000 or something to cap how much it can cost per month.

https://support.claude.com/en/articles/12429409-manage-extra...

reply

SkyPuncher

10 hours ago

 |
root
 |
parent
 |
next

[–]

That's a had sell to a finance team.

reply

bleepblap

10 hours ago

 |
root
 |
parent
 |
next

[–]

Sounds backwards -- your company is getting the benefits of your increased productivity and doesn't want to pay for it. Im not sure that's Anthropics problem?

It's like I was a graphic designer and my finance company said "photoshop is too expensive". I wouldn't be mad at Adobe for it

reply

CubsFan1060

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

It seems like you have an impossible ask? Why not 4 subscriptions to last you 5 hours?

reply

charcircuit

8 hours ago

 |
root
 |
parent
 |
next

[–]

You are not allowed to use multiple accounts to bypass the rate limit. You can only use different accounts for different uses like a work account and then a personal account. You can't rotate through 5 for personal use.

reply

groby_b

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

Then maybe it's not worth using Claude Code that much.

reply

iberator

3 hours ago

 |
parent
 |
prev
 |
next

[–]

Maybe start actually working and PROGRAMMING instead of simply cheating and ruining the job market at the same time?

Usage of such tools should be forbidden in companies - its cheating and using code you didn't even wrote. thsts literally a crime

reply

lherron

6 hours ago

 |
prev
 |
next

[–]

Reality is Ant can supply X tokens and they see demand for 10*X tokens. So they’ll charge whatever the top 10% of users are willing to pay, and slowly degrade the value of the subscriptions until everyone has moved to another supplier or migrated to the 10% price point. The draconian ToS that they sometimes enforce is their mechanism to degrade subscription value over time. Expect agent-sdk to be next on the chopping block, moving from oauth supported to api only. When they switch it they will rightly point out the docs never explicitly said it was allowed.

reply

bob1029

8 hours ago

 |
prev
 |
next

[–]

$200 is a lot of money per month. I just bought this much in OAI API credits and I expect them to last me until August or so.

If you started plugging tools into GPT5.4 you may soon discover that you don't need anything beyond a single conversation loop with some light nesting. A lot of the openclaw approach seems to be about error handling, retry, resilience and perspectives on LLM tool use from 4+ months ago. All of these ideas are nice, but it's a hell of a lot easier to just be right the first time if all you need is a source file updated or an email written. You can get done in 100 tokens what others can't seem to get done in millions of tokens. As we become more efficient, the economic urgency around token smuggling begins to dissipate.

reply

smallerfish

8 hours ago

 |
prev
 |
next

[–]

> for third-party harnesses

What's the exact definition of third-party harnesses? They have an Agent SDK in Claude Code that can be used. Are they trying to say that only Anthropic products can use pro/max plans?

reply

Multiplayer

8 hours ago

 |
parent
 |
next

[–]

Great question. I've read that the agent sdk is ok as long as it's not for external use - meaning you aren't selling access to it. Unclear now though!

reply

NewsaHackO

7 hours ago

 |
parent
 |
prev
 |
next

[–]

When another program is doing direct tool calling instead of delegating it to Claude.

reply

christopher8827

11 hours ago

 |
prev
 |
next

[–]

This is why people are switching over to Codex

reply

minimaxir

11 hours ago

 |
parent
 |
next

[–]

Codex
just
 ended their double-usage offer and OpenAI just had an exec shakeup, so it'll be interesting to see how Codex reacts, or if people have usage issues with Codex.

reply

lmedinas

11 hours ago

 |
root
 |
parent
 |
next

[–]

OpenAI mentioned already that it's ok to use Codex with Openclaw.

reply

minimaxir

11 hours ago

 |
root
 |
parent
 |
next

[–]

Months ago. Things in the AI world change quickly.

reply

xtracto

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

So the VC gravy is drying. We should see the enshitification of LLM providers in the rest of 2026 and 2027. The bubble has to burst at some point.

reply

zephyreon

9 hours ago

 |
prev
 |
next

[–]

This is the classic car wash subscription scheme. You sign up a bunch of people for $40 a month to wash their car. Most people only go to wash their car once or twice a month (or even less), which offsets those few folks that do it three times a week or more.

The problem Anthropic is running into is that OpenClaw made it easy for everyone to become one of those folks that washes their car three times a week or more.I’m sure they were losing money on subscriptions in general but now they are really losing money. Shutting off OpenClaw specifically probably helps stem some of the bleeding.

reply

eternaut

4 hours ago

 |
prev
 |
next

[–]

Anthropic might underestimate how many users got a subscription because of openclaw and the likes. I did; $100 max subscription. Not renewing it. GLM and minimax are viable alternatives for a fraction of the cost.

reply

_pdp_

11 hours ago

 |
prev
 |
next

[–]

The solution as usual is open source.

For example...We recently moved a very expensive sonnet 4.6 agent to step-3.5-flash and it works surprising well. Obviously step-3.5-flash is nowhere near the raw performance of sonnet but step works perfectly fine for this case.Another personal observation is that we are most likely going to see a lot of micro coding agent architectures everywhere. We have several such cases. GPT and Claude are not needed if you focus the agent to work on specific parts of the code. I wrote something about this here:https://chatbotkit.com/reflections/the-rise-of-micro-coding-...

reply

stavros

11 hours ago

 |
parent
 |
next

[–]

> The solution as usual is open source.

> Obviously step-3.5-flash is nowhere near the raw performance of sonnetI feel like these two statements conflict with each other.

reply

happyopossum

11 hours ago

 |
root
 |
parent
 |
next

[–]

Those two statements completely check out about a lot of open source projects/products tho... macOS upsetting you today? The solution is linux!

reply

snarkyturtle

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Google releasing Gemma 4 yesterday was prescient. Toying around with Zed + Gemma 4 on my laptop is 95% as good as using a cloud provider.

reply

nothinkjustai

11 hours ago

 |
parent
 |
prev
 |
next

[–]

Yeah this is similar to my approach, although with slightly more powerful models. I’m just not having a good time letting the sota models loose on a code base to implement entire features. Spending too much time cleaning up the mess. It’s my fault, I needed to guide it more, but it would take the same amount of time to use a faster model to generate smaller chunks and also cost less. And I’m not even doing anything particularly complex!

inb4 skill issue I could probably beat you coding by hand with you using Claude code

reply

8note

11 hours ago

 |
prev
 |
next

[–]

> We’ve been working to manage demand across the board, but these tools put an outsized strain on our systems. Capacity is a resource we manage carefully and we need to prioritize our customers using our core products.

but couldn't i use this in off times only?

reply

throwaway911282

6 hours ago

 |
prev
 |
next

[–]

Just use codex. A company that has not released any open weights models and goes after banning accounts and suing companies is not really the kind of company I want to give my money too. And gpt5.4 is the best model out there. Some people overthink on personality but I just want good code.

reply

Reebz

6 hours ago

 |
parent
 |
next

[–]

Just use opus. A company that has not rejected agreements with a “Department of War” and sanctions reasoning models to enable mass citizen surveillance and autonomous weapons deployment with no human intervention is not really the kind of company I want to give my money too. And opus4.6 is the best model out there. Some people overthink on personality but I just want good code.

reply

mogili1

11 hours ago

 |
prev
 |
next

[–]

What about when you use Claude agent SDK on your laptop?

Extra usage is very sneaky you don't get any notice that you are using extra usage and could end up with unnecessary costs in case you would have preferred to wait an hour or so.

reply

scottcha

10 hours ago

 |
parent
 |
next

[–]

I think there was a clarification posted on Reddit that said Claude Agents SDK didn't apply for now.

reply

gnabgib

10 hours ago

 |
prev
 |
next

[–]

Discussion (655 points, 1 month ago, 793 comments)
https://news.ycombinator.com/item?id=47069299

reply

jklm

9 hours ago

 |
prev
 |
next

[–]

The main reason I find myself using Opus is because it's a better communicator. (Yes, I know it's better in some areas like frontend vs. others but this is not significant enough for my purposes.)

So this change has actually forced a reckoning of sorts. Maybe the best option is to outsource the thinking to another model, and then send it back to Opus to package up.Ironically this is how the non-agent works too to an extent.

reply

ramoz

11 hours ago

 |
prev
 |
next

[–]

Super confusing email. Not sure why I received. Am i to assume my account was flagged? I only use my subscription for Claude Code.

UPDATE:reply on x
Thariq
@trq212
only flagged accounts, but you can still claim the credit

reply

mh-

11 hours ago

 |
parent
 |
next

[–]

Any idea what caused your account to be flagged, then?

reply

ramoz

10 hours ago

 |
root
 |
parent
 |
next

[–]

I mustve tried openclaw with it. Though ive been running it on codex primarily since I was serious about setting it up.

reply

dboreham

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I got the email and I've only ever run the legit claude client.

reply

siliconc0w

7 hours ago

 |
prev
 |
next

[–]

As the demand for GPUs grows and supply cannot match it, the GPUs are going towards the enterprise and it'll be the haves vs the have-nots.

Instead of not driving to work to save fuel, frugal companies are going to have their engineers work on weekends to save tokens.

reply

benbojangles

7 hours ago

 |
prev
 |
next

[–]

Anthropic are a smart clever research based bunch of people, they probably realised that openclaw is a mess, full of vibe coding get rich quick people, nothing particularly interesting to observe, and don't want to mix this data with the data they have already from real coders.

reply

paulcole

7 hours ago

 |
parent
 |
next

[–]

“What I’m doing is real coding. What you’re doing is a mess full of vibe coding.”

reply

jatora

7 hours ago

 |
root
 |
parent
 |
next

[–]

I do enjoy these gatekeepers getting sideswept, their comments being little raindrops in a hurricane. It's a vile mindset.

reply

merlindru

2 hours ago

 |
prev
 |
next

[–]

I still haven't got this email, anyone else?

reply

evbogue

10 hours ago

 |
prev
 |
next

[–]

How does Anthropic detect that a person is using OpenClaw vs using Claude Code?

Forgive me if someone asked this already and I can't find it in the comments.

reply

kristopolous

10 hours ago

 |
parent
 |
next

[–]

It's probably just the header.

headers['X-Title']You can change thatThe other simple method is to only accept certain system promptsI've been meaning to do some dumb little proxy system where all your i/o can pass through any specified system such as a web page, harness, whatever...Essentially a local model toolcalls to an "Oracle" which is just something like a wrapper around Claude code or anything you've figured out how to scrape and then you talk to the small model that mostly uses the Oracle and.... There you go.There's certainly i/o shuffling and latency but given model speeds and throughput it'll be relatively very smallNow people probably careDoesn't mean I know how to market it, I'll certainly fail at that, but at least I can build it

reply

stavros

9 hours ago

 |
parent
 |
prev
 |
next

[–]

The bun executable attests the code by sending a signature along. I'm not sure what why we can't simply clone that signature, though.

reply

password4321

10 hours ago

 |
parent
 |
prev
 |
next

[–]

Continuous requests at a constant rate for days with interruptions?

reply

TheDong

9 hours ago

 |
root
 |
parent
 |
next

[–]

That's just a ralph loop:
https://ghuntley.com/ralph/

I can do that now with claude code and a "while true" bash loop.Or with the built-in "/schedule" in claude code to set an agent to run say once every few minutes.

reply

rane

3 hours ago

 |
prev
 |
next

[–]

Why doesn't OpenAI introduce $100/mo plan? Surely many would switch in a heartbeat

reply

krupan

3 hours ago

 |
parent
 |
next

[–]

Maybe because they don't want to lose money even faster than Anthropic is?

reply

rane

1 hour ago

 |
root
 |
parent
 |
next

[–]

Is that also why they allow to use their subscriptions in OpenClaw and 3rd party harnesses?

reply

skyberrys

11 hours ago

 |
prev
 |
next

[–]

Is this going to nuke all bring your own API 3rd party tools? I've been casually using fewshell
https://github.com/few-sh/fewshell
 with my Claude api key, I really hope it's going to keep working. I've just finally managed to turn myself into a reasonable devops team with it.

reply

minimaxir

11 hours ago

 |
parent
 |
next

[–]

This does not affect anyone who uses an API key.

reply

skyberrys

10 hours ago

 |
root
 |
parent
 |
next

[–]

Oh thank you! I'm using these tools but occasionally I feel like a medieval horse rider trying to drive a sedan. Glad to know, I haven't used OpenClaw, I prefer the meat computer for autonomous compute.

reply

anon0834

10 hours ago

 |
root
 |
parent
 |
next

[–]

All these people that complain were not paying for an API key

reply

sanex

8 hours ago

 |
prev
 |
next

[–]

Claude usage limits are insane. I love their models but had to cancel my personal plan because I would burn through my weekly limits in 2 days. I use them for work but I spend like $30-50 __per day__. Not something I'd pay for myself.

reply

krater23

35 minutes ago

 |
parent
 |
next

[–]

You don't make $50 per day? From where you are?

reply

crawshaw

9 hours ago

 |
prev
 |
next

[–]

Based on this and recent product releases, Anthropic seems keen on building a closed ecosystem around their excellent model. That is their business choice, I suspect it will work well. But I cannot say I am particularly excited to have my entire development stack owned by one company.

reply

xtracto

9 hours ago

 |
parent
 |
next

[–]

As a non-American, I love what Chinese companies are doing. The progress they are showing and the fact they are sharing the weights of the models is great. I can't wait for the day when companies that "have no moat" like A. , Cursor or even OpenAI are left with a bunch of float matrices and hardware.

I understand people from the US will have an anti-Chinese reaction, but for us in the "third world" that can use both techs, the openess is always good.

reply

luxuryballs

8 hours ago

 |
parent
 |
prev
 |
next

[–]

they could have locked OpenClaw out but instead they took the time to adjust the way it works so people can still use it

reply

kelnos

8 hours ago

 |
prev
 |
next

[–]

I guess they're only sending this to people who use tools like OpenClaw. I don't, and haven't gotten an email. And I guess also won't get the free extra usage credit offer. Ah well.

reply

dvt

4 hours ago

 |
prev
 |
next

[–]

Running locally or privately (in the cloud) is the future. Anthropic/OAI will need to recoup (astronomical) training costs and I'm not going to be their bailout plan, especially considering training was done on torrented & copyrighted data anyway.

Public model inference quality is almost at SOTA levels, why would anyone pay these VC-subsidized companies even a cent? For a shitty chat interface? Give me a break.

reply

hombre_fatal

10 hours ago

 |
prev
 |
next

[–]

If OpenClaw is just "claude -p", then how do they know when you're using OpenClaw?

reply

JSR_FDED

10 hours ago

 |
parent
 |
next

[–]

They look for pincer marks

reply

hombre_fatal

7 hours ago

 |
root
 |
parent
 |
next

[–]

It's a pair of ragged claws.

reply

dgellow

3 hours ago

 |
prev
 |
next

[–]

Makes sense, yes. That’s definitely not sustainable

reply

eagleinparadise

12 hours ago

 |
prev
 |
next

[–]

Anthropic measures your usage based on token consumption

We are paying for a certain amount of token consumptionWhy then, is this an outsized strain on your system Anthropic?It's like buying gasoline from Shell, and then Shell's terms of services forcing you to use that gas in a Hummer that does 5 MPG, while everyone else wants to drive any other vehicle.

reply

SpicyLemonZest

11 hours ago

 |
parent
 |
next

[–]

If you're on a subscription plan, you're paying for a certain amount of
maximum
 token consumption. Mass market consumers generally prefer this model to one where they're billed for actual usage. But making it work requires statistical estimates of how much people will consume, which often requires excluding third party tools that circumvent those estimates.

To use your analogy, if Shell sold you a subscription to fill up your Hummer up to 30 times a month, they wouldn't let you use that subscription to fill gas cans with a GMC logo taped to the side. They couldn't, without overcharging the people who just want to average out their cost of driving.

reply

fc417fc802

10 hours ago

 |
root
 |
parent
 |
next

[–]

I think that just as with ISPs people become irate when they feel there's been a bait-and-switch. Had they very loudly advertised the subscription as limited to their harness up front with a note about maximum token use people presumably wouldn't feel cheated. Whereas they seem to be pulling a "pray I don't alter it further" for the second time now.

You don't get to sell a subscription described primarily as being for some quantity of X and then change the terms every time people find creative ways to use the stream of X they believe themselves to have purchased from you. People thought they were purchasing in bulk.

reply

bitpush

11 hours ago

 |
parent
 |
prev
 |
next

[–]

I feel icky replying in favor of a for-profit entity, but here goes ..

> We are paying for a certain amount of token consumptionI dont think you are. The specific arrangement you have is you pay for a subscription to be used with Claude Code. It isnt access to tokens, so you can do whatever you please.---An analogy would be a refillable cup for a soda at a restuarnt. They will allow you to refill how many ever times you want, but only using the store provided cup - and you cant bring your own 2L hydroflask or whatever. You're paying not just for the liquid, but for the entire setup.

reply

stavros

11 hours ago

 |
root
 |
parent
 |
next

[–]

The analogy is bad. Anthropic does not let you "refill however many times you want", they have limits. That's what "limits" in your account is.

It would be like the restaurant saying "you can buy the 2-liter soda pack" and then getting all uppity when you bring your own 2L hydroflask in.

reply

charcircuit

11 hours ago

 |
parent
 |
prev
 |
next

[–]

You are making the false assumption that all token consumption costs the same when it doesn't. Yes in the limit the price to serve the model and generate a response is O(tokens), but when tokens is smaller it can be cheaper to generate a new token than when tokens is bigger. If other harnesses prompt with more tokens than Claude Code it can be more expensive to serve.

reply

stavros

11 hours ago

 |
root
 |
parent
 |
next

[–]

They have limits. I don't care how expensive it is to serve, I'm paying them for a given amount of tokens (a limit which THEY SET) and they want to
also
 dictate where I spend those tokens.

reply

charcircuit

11 hours ago

 |
root
 |
parent
 |
next

[–]

>I'm paying them for a given amount of tokens

The plans do not say how many tokens you get. People are paying for access. Higher plans get more usage. The marketing and support material of the plans only use the word "usage" and never "tokens."

reply

verdverm

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

Those are subsidized tokens because you are also using their product.

They have a per-token payment option where you can use any tool you like

reply

Robdel12

10 hours ago

 |
prev
 |
next

[–]

I believe the capacity about 30%. They did just spend the entire last month of feature releases in Clade Code replacing "claw" features.

So, to me its a "we built it into our world use ours"Edit: FWIW I am an avid hater of all claw things, they're security nightmare.

reply

janalsncm

10 hours ago

 |
prev
 |
next

[–]

I got fed up with Claude code limits and have been using a combination of qwen3-coder, gemma4, and qwen3-vl locally. Gets me 90% of the way there and CC is still around for now if I need it.

Btw even at insane markups $200/mo means GPUs break even pretty fast.

reply

thegagne

8 hours ago

 |
parent
 |
next

[–]

Which harness and how which GPU?

reply

janalsncm

2 hours ago

 |
root
 |
parent
 |
next

[–]

Opencode + 4090

reply

p_stuart82

8 hours ago

 |
parent
 |
prev
 |
next

[–]

the hardware ROI is insane right now tbh. a $200/mo sub is literally paying off a second gpu in less than a year.

reply

computerex

9 hours ago

 |
prev
 |
next

[–]

Claude is a great model. But anthropic’s user hostile practices have forced me to terminate my sub with them. Right now I am all in on GitHub copilot and that’s primarily how I get my opus tokens.

reply

jerieljan

8 hours ago

 |
prev
 |
next

[–]

I always thought this was the case since they declared war against Opencode and its users.

The lines drawn by their consumer vs commercial TOS was clear and I never subscribed because of it.

reply

OptionOfT

9 hours ago

 |
prev
 |
next

[–]

Given the sheer amount of logging that happens in Claude Code based on the leak, I'm not surprised. This isn't about load, this is merely about cost.

Claude Code is subsidized because of data collection.

reply

Ifkaluva

7 hours ago

 |
prev
 |
next

[–]

I think this is why the LLM era will not produce as much automation as people think.

We have had the ability to automate browser activities for a long time—but, online service providers don’t want to be behind a layer of automation, which is why captchas were invented.Automating things on the Internet has never been a technology obstacle, it has been a social one.I don’t see how anything has changed!In fact I recently received an updated ToS from eBay saying I am not allowed to use an AI agent to buy stuff on their site. Just a matter of time until others follow suit!Edit: I misunderstood what was happening. Thanks to the comment below for clarifying.

reply

isubkhankulov

7 hours ago

 |
parent
 |
next

[–]

While I agree with you, thats not what this announcement is about. Anthropic wants to disallow programmatic use of their subscription plans for business reasons as a way to manage demand. They’re having outages, at least weekly, since March.

reply

Ifkaluva

6 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks for the clarification! I added an edit to my comment.

reply

stingraycharles

6 hours ago

 |
prev
 |
next

[–]

OpenClaw also had the ability to run entirely within Claude Code instead of using the oauth token. Would that still be allowed?

reply

yalogin

9 hours ago

 |
prev
 |
next

[–]

Oh that is the crux of it, I was wondering why they are leading with the free credit in their email and what the catch is. I guess for someone that doesn’t use openclaw it doesn’t matter.

reply

rohansood15

9 hours ago

 |
prev
 |
next

[–]

This email gives out the endgame - eventually, Claude subscription would be ~30% cheaper than API costs.

Our engineering team averages 1.5k per dev per month on credit costs, without busting Max limits today.

reply

bglusman

7 hours ago

 |
prev
 |
next

[–]

For anyone interested, I’m cleaning up a project I’ve been working on that is a router for arbitrary agents derivative of/forked from ZeroClaw… part of what it does is let you switch between different agents on WhatsApp/Signal/Matrix etc via !switch commands, so that part isn’t an agent itself but just wants to own your channels so you can have any number of agents talking to the same handful of channels without contention.

I do also bundle a default agent with it, also forked from ZeroClaw, with a goal of being more or less prompt injection proof and hopefully able to centralize some configuration and permissions for most or all of the agents it manages, though that part is very rough sketch/plan at the moment I’d love feedback and help on from anyone interested…. Two projects, clash and nono caught my eye in this space, I think both leverage Linux landgrant but I may also use landrun for similar control of other processes like openclaw that it may manage for the user, still figuring out how and where to fit all the pieces together and what’s pragmatic/what’s overkill/what overlaps or duplicates across various strategies and tools. Right now there’s real bash wrappers that evaluate starlark policies, hoping to fully validate better end to end but if you’re interested a few others users testing, validating and/or contributing Claude tokens to the project could be invaluable at this stage. Plan to open source ASAP, maybe tonight or tomorrow if there’s interest and I have time to finish cleanup and rename (I was calling it PolyClaw but that confuses with some weird polymarket Claude skill, so now the router is going to be ZeroClawed and the agent will stay NonZeroClaw in homage to ZeroClaw who it’s forked from… we may also integrate the new Claw Code port which is also rust, just for good measure/as a native coding agent in addition to the native claw agent )Anyway the main reason I mention is it already has a working ACP integration for any code agent, and working now on using Claude codes native channel integration to make it appear as a full fledged channel of its own, as it now more or less does already to OpenClaw, for anyone wanting to gradually migrate away from their existing OpenClaw installation using this, towards Claude or some other agent. Email me or respond here if interested, or I’ll try and post link here once it’s fully public/open source

reply

yoyohello13

5 hours ago

 |
prev
 |
next

[–]

You can basically do what open claw does with native Claude code features now anyway.

reply

RIMR

1 hour ago

 |
prev
 |
next

[–]

I didn't even realize you could connect a standard subscription to OpenClaw in the first place. It seems like you would run into limits rather quickly, which would degrade the experience quite badly.

Anthropic's current business model is to sell access to their tools to subscribers at a loss. Users maxing out their $200/month plan can realistically cost Anthropic $500-600 in actual compute costs.Anthropic is okay with this right now because they want to amass as many users as they can, and eventually hope that GPUs will increase in power and efficiency, and their LLMs will become more efficient as well. They can eventually profit off of their current pricing, or with modest price increases, if that comes to fruition.But letting OpenClaw wake up every 30 minutes and start sending requests is a surefire way to max out your weekly limits, and that certainly isn't something Anthropic planned for.

reply

whateveracct

7 hours ago

 |
prev
 |
next

[–]

Go pay for the API. It's not complicated.

reply

dev0p

4 hours ago

 |
prev
 |
next

[–]

Just in time for my subscription to expire. Goodbye!

reply

chrisjj

12 hours ago

 |
prev
 |
next

[–]

And so it begins...

reply

mememememememo

11 hours ago

 |
parent
 |
next

[–]

Drug dealer got them hooked, now time to charge by the ounce.

reply

buremba

10 hours ago

 |
prev
 |
next

[–]

I get why they block OpenClaw and it makes sense but I wonder if they can actually detect OpenClaw calling Claude Code CLI using something like acpx.

It's simply identical to how people use Claude Code locally.

reply

jeffpersonified

9 hours ago

 |
prev
 |
next

[–]

Less than 24hr notice on a Friday: either Anthropic is dropping S tier next week or they massively fumbled over the past 2 months in self owns and outages.

reply

mikkupikku

2 hours ago

 |
prev
 |
next

[–]

I had an idea to use `claude -p` to break apart books and annotate all dialogue with estimated speaker meta-data. The tips displaying in interactive claude sessions keep seeming to advocate for such experimentation with claude -p, but despite this I have deliberately held back because after reading the TOS (weeks ago) I couldn't clearly make out where the line is meant to be. The existence of `claude -p` is confusing to me.

reply

davesque

7 hours ago

 |
prev
 |
next

[–]

I'm honestly completely in favor of this. Anthropic obviously budgets their capacity based on projected
human
 usage patterns coming through their native app suite (Claude Cowork, Claude Code, etc.). They should not be expected to shoulder the burden of community tools like OpenClaw that are effectively designed to strategically max out usage windows on the plan. That has clearly caused issues with uptime in the past couple of months and I've gotten pretty fed up with the degraded service quality while I'm just trying to use Claude Code as it's intended to be used. I'm happy to see they're doing something about this. Seems like a totally fair move to me. I'd rather that Claude Code functions well when I'm using it according to its design.

reply

lrvick

10 hours ago

 |
prev
 |
next

[–]

They also forced OpenCode to remove support as well. Thankfully there is always self hosting and a shit ton of competitors that let you use whatever local software you want.

reply

snthpy

4 hours ago

 |
prev
 |
next

[–]

I thought this had already been the case for a while?

reply

mediagato

7 hours ago

 |
prev
 |
next

[–]

We built an open-source orchestrator that routes across providers with direct API keys. If you're looking for alternatives to subscription-locked tools:
https://modelreins.com

reply

pikdum

11 hours ago

 |
prev
 |
next

[–]

Does this mean I can't use `claude -p` in bash scripts now?

reply

techgnosis

10 hours ago

 |
parent
 |
next

[–]

I doubt it means that. How would they ever know? Honest question..

reply

martinald

10 hours ago

 |
root
 |
parent
 |
next

[–]

if (process.argv.includes('-p')) and then setting a different http header?

reply

raincole

11 hours ago

 |
prev
 |
next

[–]

So is Codex the only SOTA that welcomes third-party harness?

reply

wyre

10 hours ago

 |
parent
 |
next

[–]

Any model besides Claude. AFAIK anthropics the only corp to say no to other harnesses.

reply

benn67

11 hours ago

 |
prev
 |
next

[–]

Haha, I almost expected this.

Say goodbye to my 600$/ month Anthropic.

reply

minimaxir

11 hours ago

 |
parent
 |
next

[–]

The people who have enough Opus usage such that they were using multiple Max accounts are the exact users Anthropic want to kick out.

reply

operatingthetan

10 hours ago

 |
parent
 |
prev
 |
next

[–]

So you were using API tokens already, this doesn’t affect you. Why are you quitting in protest?

reply

stavros

10 hours ago

 |
root
 |
parent
 |
next

[–]

Three Max subscriptions.

reply

operatingthetan

10 hours ago

 |
root
 |
parent
 |
next

[–]

So they were breaking the TOS anyway

reply

stavros

10 hours ago

 |
root
 |
parent
 |
next

[–]

The ToS says you can't have more than one sub?

reply

Zopieux

10 hours ago

 |
parent
 |
prev
 |
next

[–]

There's no way in hell this amount of tokens is reasonable for anything or worth it

reply

benn67

10 hours ago

 |
root
 |
parent
 |
next

[–]

I have 2 max 20x subscriptions. So not API tokens.

I do a lotta stuff don’t need to get into it here.

reply

techgnosis

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

You have a tiny imagination

reply

cbg0

4 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

You have no idea how much slop people push out on daily basis.

reply

renewiltord

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Three Claude Max subs maxed out? I think that's exactly what they
do
 want to say goodbye to. This might be the most unregretted "unregretted attrition" they have.

reply

NewsaHackO

8 hours ago

 |
root
 |
parent
 |
next

[–]

The worst thing is that someone with three Max accounts is definitely not going to leave due to this. They already clearly have a dependence on Claude.

reply

Animats

10 hours ago

 |
prev
 |
next

[–]

Oh, it's a billing thing. Not fear that Claude coupled to something that can actually
do
 things is dangerous.

reply

HellsMaddy

11 hours ago

 |
prev
 |
next

[–]

I received it too. I wonder if they sent this to all pro/max subscribers or only those who they’ve flagged as having used a third party harness.

reply

windexh8er

11 hours ago

 |
parent
 |
next

[–]

I have a few accounts but have been avoiding OpenCode with my Pro/Max accounts because I had heard some were being banned. Have only been using Anthropic models through OpenRouter, but it ends up being cost prohibitive for anything reasonably complex. But, I haven't received emails in either account around the change. Anthropic probably figures that it's less ideal to draw attention to it if a user isn't using it in that way. Personally I'm not a fan of what they're doing and will likely drop them and go out of my way to find a different option and move away from their lock-in strategy. They're really no different than OpenAI at this point (for the worst).

reply

mh-

11 hours ago

 |
parent
 |
prev
 |
next

[–]

FWIW: I did
not
 receive it, and have never used my subscription outside of first party Claude tools. I was, however, able to claim the extra usage credit.

Interestingly, it looks like I haven't received a non-receipt email from them since August 2025.

reply

FireBeyond

11 hours ago

 |
root
 |
parent
 |
next

[–]

How/where were you able to do that?

reply

mh-

11 hours ago

 |
root
 |
parent
 |
next

[–]

Top of
https://claude.ai/settings/usage

edit: see Boris' tweet about ithttps://x.com/bcherny/status/2040206443094446558

reply

burnte

11 hours ago

 |
parent
 |
prev
 |
next

[–]

I'm a pro subscriber and didn't get this so I wager its accounts they detect because i only use it in the browser and haven't seen this.

reply

zem

11 hours ago

 |
prev
 |
next

[–]

I wonder if this also applies to tools that interact with the claude code tui through tmux's capabilities.

reply

jonwinstanley

10 hours ago

 |
prev
 |
next

[–]

What are people doing with OpenClaw? Are there any places that try to log best uses and new ideas?

reply

tiarafawn

5 hours ago

 |
prev
 |
next

[–]

Could the real reason for this be more centered around generation and control of new training data?

I suspect the same for the forced high AI usage quotas for developers at MS etc.
We've had multiple generations of models trained on all of the code that's available and there are diminishing returns on how much that data can do for training now. Newly published publicly available data is also made up of a significant portion of slop.The best way to get fresh training data from real human brains might be to have real humans use your first party tools where you control all of the telemetry.

reply

Lihh27

9 hours ago

 |
prev
 |
next

[–]

This is exactly why building daily workflows on top of proprietary API wrappers is a ticking time bomb. The moment your tooling becomes an outsized strain, they just flip the switch on you.

reply

Sinidir

10 hours ago

 |
prev
 |
next

[–]

Does anyone know. How would that relate to simply wrapping claude code as a subprocess?

reply

0xbadcafebee

7 hours ago

 |
prev
 |
next

[–]

If you spend $200/month on Anthropic, that's $2400/year. Buy a fast GPU or Strix Halo machine, do the AI locally, after a year you're saving money.

reply

cbg0

4 hours ago

 |
parent
 |
next

[–]

The open models are still far behind GPT 5.4 and Claude if you're using them for building software.

reply

Kim_Bruning

4 hours ago

 |
root
 |
parent
 |
next

[–]

About a year behind , TBQH. Newer Mixture-of-Experts models are comparable to a slightly older Claude Sonnet; if you don't mind the (lack of) speed. Some benchmarks say they're competitive with the frontier models
right now
 for certain tasks.

I'm not sure how much I trust those benchmarks; I have a feeling everyone is playing up to them in some way. Still, if you're willing to accept the latency, they're definitely usable.Of course everyone has realized this, so the hardware you need to run them is a little bit on the expensive side right this minute.CPU manufacturers are working on improvements so that you can more practically run models on regular CPU+RAM (it's already possible with llama.cpp, just even slower).

reply

TheDong

7 hours ago

 |
parent
 |
prev
 |
next

[–]

If you want to run better models, you need one of the more expensive GPUs, like an H100 or such ($40k). I don't think any of the smaller models are remotely comparable to anthropic.

The GPU also takes around $500-$1000 in electricity, and even then you won't be able to run a model of as good quality as anthropic.It's also hard to justify since who knows how quickly it will be outdated, like maybe soon you'll need a blackwell chip (like a $100k PC, check out the NVIDIA DGX Station) to run a decent model.... It'll take a lot more than a year to pay back a model capable of running openclaw with any sort of reasonable performance.Or can you report that you've had good luck with a Strix Halo or local GPU for less than $40k up-front costs?

reply

logicallee

2 hours ago

 |
prev
 |
next

[–]

Has anyone gotten Google's open offline model Gemma 4 (released yesterday) working with OpenClaw? It didn't work for me as an agent with OpenClaw.

reply

davidkunz

2 hours ago

 |
prev
 |
next

[–]

We need Net Neutrality for LLMs.

reply

anizan

9 hours ago

 |
prev
 |
next

[–]

Using Xiaomi’s mimo pro on openrouter via hermes agent

reply

eternaut

7 hours ago

 |
prev
 |
next

[–]

someone else _not_ having the “Claim” button on the banner at the top of the Usage page?

reply

eternaut

4 hours ago

 |
parent
 |
next

[–]

Ok, it showed up eventually

reply

dackdel

6 hours ago

 |
prev
 |
next

[–]

cant wait till they implement turboquant and make ai cheaper again

reply

randall

11 hours ago

 |
prev
 |
next

[–]

Does anyone have a link to the "read more"?

reply

supliminal

11 hours ago

 |
prev
 |
next

[–]

Since the OpenClaw creator is posting on HN I’d like to hear some commentary from him directly.

reply

seamossfet

10 hours ago

 |
prev
 |
next

[–]

Honestly, this is a good thing. OpenClaw as a concept was rather silly to run such a heavy model for. If you want something like OpenClaw to work you really need to figure out how to do it with an economical model.

reply

cat-turner

11 hours ago

 |
prev
 |
next

[–]

Doesn't this unfairly impact startups? Why not instead allow issuance of API keys with usage caps? It seems like a money grab.

reply

jasonlotito

11 hours ago

 |
parent
 |
next

[–]

> you’ll no longer be able to use your Claude subscription limits for third-party harnesses including OpenClaw. You can still use them with your Claude account, but they will require extra usage, a pay-as-you-go option billed separately from your subscription.

How is what you are asking for different from what they are saying?

reply

raverbashing

5 hours ago

 |
prev
 |
next

[–]

It looks like the chickens came to roost much earlier than expected, including the fall in RAM prices

reply

yieldcrv

10 hours ago

 |
prev
 |
next

[–]

I like how the best way to protest this is by doing what everyone should have been doing to begin with: running a great open source model on rented hardware

reply

saltyoldman

11 hours ago

 |
prev
 |
next

[–]

Is anyone even getting anything out of a $20/mo sub for Anthropic?

I'm doing a side-by-side with GPT-5.4 for $20/mo and Sonnet for $20/mo and I can tell you that all my 5 hour tokens are eaten in 30 minutes with Claude. I still haven't used my tokens for OpenAI.Code quality seems fine on both. Building an app in Go

reply

freedomben

11 hours ago

 |
parent
 |
next

[–]

Yeah, the $20 Claude plan is almost worthless. Unless you're just using it to write scripts and not working in a real world application code base, it just runs out way too fast to get much done.

I think using it to write small documentation or small scripts would be a good use case for it, but serious development work you Hit the usage limits way too fast.

reply

girvo

10 hours ago

 |
parent
 |
prev
 |
next

[–]

I used to, but not anymore. Now I can somehow burn my _entire_ limit with a single prompt, maybe two. It's ridiculous, I've changed nothing about how I do things.

Only thing now is that the cheaper (worse) chinese model coding plans have huge limits, so I lean on those now. Requires a lot more hand-holding though.

reply

warmonger

9 hours ago

 |
parent
 |
prev
 |
next

[–]

Yes, 20/mo is worth the price for me. Just don't run Opus by default for everything

reply

Traubenfuchs

11 hours ago

 |
prev
 |
next

[–]

You can cancel your subscription, there are like 5 competitors you can pick instead and anthropic offers an API plan where you can find out how many tokens circus tools like claws really consume compared to coding tasks.

reply

kjuulh

11 hours ago

 |
prev
 |
next

[–]

Anthropic should calm down, I get that they're trying to either build a moat, or simply curb what is essentially subsidized tokens. It is technically true that when you've got a claude code subscription you pay for the product with its terms, and those terms doesn't include you grabbing the token and using it for another application. They're also trying to build a competitor to openclaw so it makes sense they're trying to crush it. But it feels like such a feeble moat, that it looks silly. Claude Code is nice, but it is not
that
 nice.

reply

beanjuiceII

10 hours ago

 |
prev
 |
next

[–]

i think i'll no longer be giving my money to anthropic

reply

winterrx

11 hours ago

 |
prev
 |
next

[–]

So now what happens to startups and ADE's orientated around Claude like Conductor.. no more Claude for them I guess back to Codex!

reply

jasonlotito

11 hours ago

 |
parent
 |
next

[–]

Nothing. They aren't using third party harnesses, which is the issue here as spelled out in the post.

> you’ll no longer be able to use your Claude subscription limits for third-party harnesses including OpenClaw.My understanding is that Conductor and others aren't using it.

reply

jsunderland323

9 hours ago

 |
root
 |
parent
 |
next

[–]

I'm not sure. The docs on claude -p are sort of ambiguous on third party usage

reply

mccoyb

10 hours ago

 |
prev
 |
next

[–]

Why not use datacenter of geniuses to increase capacity? Grug confused.

reply

Razengan

7 hours ago

 |
prev
 |
next

[–]

AI disallowing use by AI :|

reply

desireco42

7 hours ago

 |
prev
 |
next

[–]

They are running out of things to ban...

reply

andrewstuart

9 hours ago

 |
prev
 |
next

[–]

Big mistake.

Claude innovation will come from being open, not closed.

reply

zer00eyz

9 hours ago

 |
prev
 |
next

[–]

"We dont crash ever" -- the social network.

If you haven't been paying attention anthropic burned a lot of their developer good will in the last 2 weeks, with some combination of bugs and rate limits.But the writing is on the wall about how bad things are behind the scenes. The circa 2002 sentiment filter regex in their own tool should have been a major clue about where things stand.The question every one should be asking at this point is this: is there an economic model that makes AI viable. The "bitter lesson" here is in AI's history: expert systems were amazing, but they could not be maintained at cost.The next race is the scaling problem, and google with their memory savings paper has given a strong signal what the next 2 years of research are going to be focused on: scaling.

reply

cute_boi

9 hours ago

 |
prev
 |
next

[–]

Idk why people are complaining when they know subscription are currently heavily subsidized. If they don't like they can always choose alternative service.

reply

stavros

11 hours ago

 |
prev
 |
next

[–]

Looks like I'm going to be switching to OpenAI. I know the whole "well those are the terms" Stockholm syndrome argument, but no, those weren't the terms when I signed up. If one of the parties decided to unilaterally change terms in any other everyday situation, nobody would think it was acceptable, but we've become so resigned to corporations having enough money to make the law suit them that we think it's moral behavior.

No, Anthropic, just because you added a clause that says "we can change these terms whenever" doesn't make it right. I'm paying you a set amount of money a month for a set amount of tokens (that's what limits are), and I should be able to use these tokens however I want.Luckily, there are alternatives.

reply

benced

11 hours ago

 |
parent
 |
next

[–]

They changed the terms going forward so you’re changing your behavior going forward? Nobody but the psychos you’re making up would think you’re out of line here. They’re not required to offer the same product forever and you’re not required to pay forever.

reply

jakelazaroff

11 hours ago

 |
parent
 |
prev
 |
next

[–]

Anthropic changing their terms is fine. You taking your money elsewhere is also fine. What's the issue here?

reply

nrmitchi

11 hours ago

 |
parent
 |
prev
 |
next

[–]

This actually seems rather generous of them? Not only are they offering credits equal the cost you paid, but they're offering refunds if you disagree.

Anthropic not allowing Claiude Code subscriptions to be used with other projects isn't "pulling the rug out"; you paid for an API subscription to use Claude Code, and now you're using it for a different purpose and a different product.If Tesla offered $10/month charging for your Tesla, and then a bunch of people turned around and use their Tesla Charge subscription to charge all different electric vehicles, and battery packs, and also hooked up a crypto mining rig to it, would you be surprised if they said "Nope, we're cutting this off. You can only use your Tesla Charge subscription for your Tesla vehicle"?

reply

stavros

11 hours ago

 |
root
 |
parent
 |
next

[–]

Nope, I paid for an Anthropic subscription that I could use with the Agents SDK. Then they decided I shouldn't be able to use that, just because.

> If Tesla offered $10/month charging for your TeslaNo, "if Tesla offered $10/month for 100 kWh of charging", and yes, I expect to use those 100 kWh with any vehicle I want, because there's a limit on the resource I'm paying for.I can understand caps on unlimited, I can't understand caps when there are strict limits.

reply

danpalmer

10 hours ago

 |
root
 |
parent
 |
next

[–]

A more apt comparison is Telsa offering $10/m for 100kWh for your car, or pay-as-you-go for any cars, but then you setting up shop at a charger, putting up a sign saying anyone can charge on your subscription until you reach that limit.

reply

stavros

10 hours ago

 |
root
 |
parent
 |
next

[–]

Who is "anyone" here if I'm the only one charging?

reply

danpalmer

6 hours ago

 |
root
 |
parent
 |
next

[–]

Anyone is the other software you're using. You were sold a subscription for use in a specific application controlled by the service provider, that they can optimise and control as needed to maintain their business.

You are the reason these changes are happening. You may well be the reason that subscription prices go up.

reply

harha

10 hours ago

 |
parent
 |
prev
 |
next

[–]

One interesting observation I had between ChatGPT and Claude before I was familiar with openclaw came
when I asked if about the difference between ChatGPT and Claude for coding and if I can get to a setup that can use both. At that time I had both subscriptions, felt it was better to build with Claude but was frequently reaching limits.

ChatGPT found it was a great idea and that I can use Claude for planning and gave me instructions on how to best hand off the building part. Claude told me it’s a horrible idea.Claude also burns much more liberally through tokens, eg reading through entire irrelevant docs.Openclaw is great for resolving this since I much more control which work goes where and also gives a much better user experience without all the back and forth to understand what context it has (my use case is to build things from my phone while I’m in senseless meetings in my day job).Fully agree on the alternatives. In the end Claude’s experience is worse, while it still makes bad decisions if you let it. Better to get a good workflow on a less capable model.

reply

post-it

11 hours ago

 |
parent
 |
prev
 |
next

[–]

I mean that's the thing, you're paying per month. And they're changing things going forward and offering to refund the current month.

It's like if I buy a hot dog every month and they tell me they're raising the price next month, or discontinuing honey mustard. Inconvenient but they're not doing anything wrong.Especially since, given my back of the napkin math, they're giving us a pretty decent discount on the subscription plans.

reply

nekusar

9 hours ago

 |
prev
 |
next

[–]

Wellll, that rug aint gonna pull itself, now is it?

Ive been calling for local LLM as owning the means of production. I aint wrong.

reply

ChildOfChaos

49 minutes ago

 |
parent
 |
next

[–]

Not as simple as that. Everyone would happily use local, but the issue is local sucks.

reply

j45

9 hours ago

 |
prev
 |
next

[–]

Inefficient token use will have to tighten up.

reply

tinyhouse

10 hours ago

 |
prev
 |
next

[–]

I really started to like Pi. That's unfortunate that I won't be able to use it with Opus (way too expensive without a subscription). I'm optimistic that open source coding models will be able to keep up. AI is too important, we're shooting ourselves in the foot if we don't adopt open source tools and models. The more adoption the better it will become.

reply

nothinkjustai

9 hours ago

 |
parent
 |
next

[–]

The copilot plans work with pi and are stupidly cheap for what you get.

reply

rvz

12 hours ago

 |
prev
 |
next

[–]

> To make the transition easier, we’re offering a one-time credit for extra usage equal to your monthly subscription price. Redeem your credit by April 17. We’re also introducing discounts when you pre-purchase bundles of extra usage (up to 30%).

The Anthropic casino wants you to continue gambling tokens at their casino only on their machines (Claude Code) only by giving more promotional offers such as free spins, $20 bets and more free tokens at the roulette wheels and slot machines.But you cannot repurpose your subscription on other slot machines that are not owned by Anthropic and if you want it badly, they charge you more for those credits.The house (Anthropic) always wins.

reply

sidrag22

11 hours ago

 |
parent
 |
next

[–]

Plenty to hate on anthropic for right now, but Ill never understand the references to output as a slot machine.
It is massively a skill based tool, you CAN use it like a slot machine with "please make it work" style prompts. The variance is the difference, if you feed it great context and/or relevant sources to utilize, your odds of success increase dramatically.
Slot machines, it doesn't matter how much thought you put into your pull, you will have the same odds as literally any other person pulling the lever.

reply

0xy

11 hours ago

 |
parent
 |
prev
 |
next

[–]

Except you put $200 into the CC casino and you can (if you choose) extract thousands in token value.

reply

Alexzoofficial

8 hours ago

 |
prev
 |
next

[–]

Nice

reply

SevenTGK

9 hours ago

 |
prev
 |
next

[–]

mysterious anthropic win???

reply

jasonlotito

11 hours ago

 |
prev
 |
next

[–]

Yes, this was made clear a while back and should not be a surprise. (Honestly, I had to double-check the date/time to see if this was actually posted today.

You can use your Claude Code subscription with third-party tools, but you have to use the Claude Code harness. Or, you use the API. OpenClaw could use the Claude Code harness, but they don't.

reply

firloop

11 hours ago

 |
parent
 |
next

[–]

FWIW I am sympathetic to Anthropic here, but OpenClaw _is_ using the Claude Code harness (via claude -p). But yes, Anthropic has made it clear they don’t like this.

reply

jasonlotito

11 hours ago

 |
root
 |
parent
 |
next

[–]

So they changed it? Last I heard they hadn't. Where did they announce they were switching to the Claude harness? I can't find anything.

reply

firloop

11 hours ago

 |
root
 |
parent
 |
next

[–]

I received the email and I have been using “Option B”, which wraps the Claude CLI.
https://docs.openclaw.ai/providers/anthropic#option-b-claude...

reply

weird-eye-issue

10 hours ago

 |
root
 |
parent
 |
next

[–]

I have heavy usage on two accounts with option c and didn't get an email

reply

charcircuit

11 hours ago

 |
prev
 |
next

[–]

You never have been able to. It's against ToS.

reply

Alexzoofficial

8 hours ago

 |
parent
 |
next

[–]

Hmmmmm

reply

entropoem

10 hours ago

 |
prev
 |
next

[–]

Anthropic and OpenAI are the clearest examples of why, in an organization of specialists, the experts themselves should not be the CEO or the final decision-maker once the company’s challenges extend beyond just the product.

Just look at how Sam Altman has led OpenAI step by step to dominate—and choke out—Anthropic, a company founded by the group of engineers who were once part of the turmoil at OpenAI.Anthorpic's product thinking is terrible even though it is technically very good.

reply

danpalmer

10 hours ago

 |
parent
 |
next

[–]

An interesting... weird(?), take. I see Anthropic as being mostly a much more compelling option. They've avoided most negative backlash, they have a much higher percentage of paying users, plenty of enterprise contracts, etc. They avoided money pits like Sora.

OpenAI seems to mostly be chasing the consumer market, but not doing great at it.

reply

dboreham

10 hours ago

 |
root
 |
parent
 |
next

[–]

I'm a very happy Anthropic customer. They could charge me 3X the current rate and it'd still be a great deal.

reply

himata4113

1 hour ago

 |
prev

[–]

I disagree with the sentiment here. Anthropic is profiting off everything they do, subscriptions not so much, but they are definitely not losing money in a way most people claim they do. These subscriptions are not only advertisement, but also the reason why trying to load the claude user account on github errors out.

IMO, the goal here is clear: they want them to use their software, have people build an ecosystem around their software, they want to have visibility around their software.It's never about capacity or usage, they just want to have the claude ecosystem, there is a reason why they don't support AGENTS.MD or other initiatives, they want everything to be theirs and theirs alone. You can argue that 'well fair', but to me this is clear abuse of their position in the market.

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
