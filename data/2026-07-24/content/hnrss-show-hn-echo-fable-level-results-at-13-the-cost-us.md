---
title: 'Show HN: Echo – Fable-level results at 1/3 the cost using open-weight models | Hacker News'
url: https://news.ycombinator.com/item?id=49026810
site_name: hnrss
content_file: hnrss-show-hn-echo-fable-level-results-at-13-the-cost-us
fetched_at: '2026-07-24T11:35:14.156649'
original_url: https://news.ycombinator.com/item?id=49026810
date: '2026-07-23'
description: 'Show HN: Echo – Fable-level results at 1/3 the cost using open-weight models'
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
Show HN: Echo – Fable-level results at 1/3 the cost using open-weight models
397 points
 by 
adam_rida
 
16 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
191 comments
I’ve been building Echo (
https://echo.tracerml.ai/
), an experiment in making one AI system out of a pool of open-weight models rather than choosing a single model and using it for every task.

It started with a simple experiment. I took a group of models, including GLM-5.2, Kimi K2.7 and others, and ran them on the same evaluations. Then I measured what would happen if, for each problem, you somehow knew in advance which models would be useful and how their outputs should be combined.That hypothetical system performed substantially better than any individual model in the pool. Of course, it is not something you can actually deploy because it relies on knowing which decisions were good after seeing the result. Echo is my attempt to recover some of that advantage without having that information in advance.For each request, Echo decides how much computation to allocate, which models should participate, and how their work should be combined. Some prompts may only need a relatively small amount of inference, while others benefit from multiple models working on different parts of the problem.One thing that surprised me while building it was how complementary the models are. A model that is clearly weaker overall can still be extremely useful on particular problems or as part of a combination.On my first evaluation mix, Echo consistently performed better than the best individual model in its pool. It also reached roughly the same aggregate result as Fable, which I used as one of the stronger comparison systems, at around one third of the inference cost.There are still some cases where Echo makes the wrong allocation or combination decision. I’m currently spending a lot of time understanding those failures, as well as testing whether the same approach holds up on coding and agentic tasks where measuring the quality of each decision becomes much harder.I built a chat interface (echo.tracerml.ai) and an OpenAI-compatible API (https://echo.tracerml.ai/docs/api) so the system can be tested outside the evaluation setup.Here is a short/high level video on how it works:https://www.youtube.com/watch?v=lJFJSvOdXhgI wrote up the evaluation methodology, individual model results, costs and current limitations here:https://echo.tracerml.ai/evalI would love for you to try it! Especially if you hit any weird failure cases or places where the allocation looks unintuitive.

 
help

fmx
 
2 hours ago
 
 | 
next
 
[–]

A "Message Echo" textbox that makes it 
look like
 you can get a response to a prompt without logging in, only to redirect to the sign-up page. Such a classic dark pattern - and such a sure way to get me to leave your site immediately.

I've literally taken one step on your website - the one your site design invited me to take - and immediately got tripped up. I'm not coming back.

reply

pizzao
 
57 minutes ago
 
 | 
parent
 | 
next
 
[–]

On the other hand, the creator would need to pay for those initial queries. This also invites for misues that sum up to large bill for the creator.

I dont know, it's something I can understand as someone also building AI stuff

reply

idonotknowwhy
 
20 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Then the creator should have a sign up button, not a fake chatbox.

This dark pattern is reminiscent of those online test sites in the 2000's where you spend 10 minutes filling out some quiz, then get prompted for an email address to see the results.https://chat.mistral.ai/chat<- let me chat and actually responded without signing up.MoonshotAI had this fake chat box dark pattern.So I signed up with Mistral instead.

reply

lukan
 
48 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Just don't use this dark pattern and rather be clear sign up is reqired with 10$ of free credits ad no strings attached?

reply

boesboes
 
33 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Just dont' put a fucking fake chat box there. not that hard.

reply

barapa
 
40 minutes ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Mom, the website tricked me!

reply

adam_rida
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

thanks to everyone for taking the time to try Echo and share feedback, this is precisely why i wanted to launch early.

i am going to try to address a couple of topics that came up often:- i'll keep publishing stronger evals, including more difficult coding and agentic benchmarks, to map out more precisely the differences with sota- the public eval dashboard will keep expanding and be updated (very open to more benchmark suggestions as well!)- some people found issues in the eval dashboard ui and the sign up flow, should be now all fixed in prodsome important precisions as well:- NO credit card is required to try Echo- each acount includes 10$ of free credits to try on both the API and the chaton the approach itself: the idea i'm exploring is more broader than model routing, i'm looking at how to allocate inference efficiently across open-weight models, deciding not only which models to use, but also how much computation a request deserves and how intermediate work should be combined.ensembling by itself is not new. since random forests and probably even before in statistics/classic ml we knew that bringing multiple models together can outperform individual ones. the interesting problem for Echo is how to model and leverage this without paying the full ensemble cost at each request.while there are conceptual similarities with systems like Fusion or Fugu, the architecture and optimization objective are different.thanks again for all the thoughtful feedback.

reply

user_7832
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Small feedback: the "create password" requires a symbol too, which Google's password manager by default does not use. I'm fairly sure a double-digit-level alphanumeric jumble is sufficient to be a password (or at least, Google thinks so). Great idea nonetheless!

reply

troupo
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> I'm fairly sure a double-digit-level alphanumeric jumble is sufficient to be a password

This isn't required either. Of course there's an xlcd for that:https://xkcd.com/936/Besides,--- start quote ---Using complexity requirements (that is, where staff can only use passwords that are suitably complex) is a poor defence against guessing attacks. It places an extra burden on users, many of whom will use predictable patterns (such as replacing the letter ‘o’ with a zero) to meet the required 'complexity' criteria.https://www.ncsc.gov.uk/collection/passwords/updating-your-a...--- end quote ---

reply

RugnirViking
 
10 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This. The siren song of "oh but increasing the number of characters makes brute forcing harder exponentially" is defeated in practice by the fact that everybody's password is following a few predictable patterns. You know what else increases the complexity exponentially? Longer passwords

reply

rahulroy
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It doesn't let me sign up. Throws `too many authentication attempts` error. There was only one attempt.

reply

peterlopen
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

same here

reply

cheema33
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

> Fable-level results at 1/3 the cost

I am guessing this is not targeting those of us on the heavily subsidized $200/mo plans. Sure, these plans may be temporary, but none of us really know how temporary they are. Until then, 1/3rd of the published API pricing is not very appealing.

reply

stilesja
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

I burned though my weekly fable usage last night on the $200 plan. I had $200 in promotional usage credits and was in the middle of executing a moderate sized coding plan. Ran on usage credits for about 1h 15m and burned $120 in usage credits. I was astounded to see how fast the $ usage added up. One problem was that I was using sub-agent execution so multiple agents were running simultaneously and I realized at the end that claude had "Forgotten" my directive to use cheaper models as appropriate for sub-agent tasks so I was running multiple instances of Fable at once. Still hard to imagine paying per token. $200 a month is high, $200 per night is crazy.

reply

jambalaya8
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I am too young (most of us on here are) to have lived through the paying for time on time-share machines in the 60s/70s, but this is giving me creepy memories of paying for sprintnet/telenet and tymnet... And I guess aol, compuserv, delphi. Are we really doing this computing model again?

reply

Foobar8568
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If I remember well, visual studio/ msdn used to be like 5k-10k per year... Basically any IT tool cost a shit load of money.

I have in mind 50k-100k ish for 3d studio max or was it softimage? (Well seems softimagehttps://www.awn.com/animationworld/siggraph-news-announcing-...).So... Basically we are back to this era.

reply

stkdump
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think you were able to buy VS Pro perpetual licenses for one time 500-1000 at all times. Of course they had higher tiers and a subscription model which were more expensive but in reality for most people there was little to no added value.

reply

cube00
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

>subscription model which were more expensive but in reality for most people there was little to no added value

The value was the multiple CDs of MSDN documentation and code samples which where very handy considering the slim pickings on the internet in 1995.These weren't included with an IDE perpetual license retail box.

reply

DougN7
 
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

That is really a great insight!

reply

Bombthecat
 
44 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I used fable to design a front-end, and damn! It's good! Frontend coding is dead. Design in a way also.

And it was damn cheap too! The main page cost was like 5 dollar.

reply

good8675309
 
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

I stopped using sub agents after they caused me to hit my limit to quickly. Had to create a separate account and pay for another max plan to unblock myself temporarily

reply

sunaookami
 
45 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah sub-agents are a scam and the results are always worse since you lose all context, caching, etc.

reply

hmottestad
 
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

My current 30-day Codex usage amounts to over 15,000 USD in tokens.

reply

sheepscreek
 
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

You're good.

Dude that topped Meta's tokenmaxxxing board before it was shut down used 265 billion tokens in a month. I kid you not.

reply

killingtime74
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

All enterprises users (people using them for work and not side projects) can't get the subsidized plans. I would say subsidized plans are a minority of usage?

reply

rodrodrod
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

People _can_ get subsidized plans for work: we use Claude Teams, $100/mo premium seat, which caps at 150 seats. Not enterprise tier, but fine for SMBs.

reply

lnrd
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

As long as you are fine with everything your team puts into Claude being retained by Anthropic. Afaik only enterprise API plans provide non data retention policies.

reply

nickthegreek
 
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

The subsidized userbase is large enough that cheema is right to call this out this distinction for other readers.

reply

monk_grilla
 
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

I imagine that most small to medium sized businesses are on either individual plans or Teams plans. The vast majority of firms do not need more than 150 seats, and API rates are not sustainable for most.

reply

byzantinegene
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

if this is true, the frontier labs are not able to justify their trillion dollar valuations, they are barely making anything on subsidized plans.

reply

nl
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You can bet that most people on those plans do not tokenmax.

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

I'll bet the other way: the plan is not cost effective unless you are coding, and even the most junior developer, so green they almost need mowing, are going to throw the agents into a loop.

I can not imagine some shelling out $200/month and then using that product lightly.

reply

nl
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> I can not imagine some shelling out $200/month and then using that product lightly.

The people paying for the plan are not the same people using it.Of 6 people I have data on the $200/plan only 2 regularly use more than $400 value.> I'll bet the other way: the plan is not cost effective unless you are codingThe person I've personally seen use the most tokens isn't a coder. They do the "second brain" thing and wow it uses a lot of tokens.They believe in the value, and TBH I've seen them do some pretty interesting and impressive things with it.> the most junior developer, so green they almost need mowing, are going to throw the agents into a loopI think this is also true.But loops actually hit the cache alotand most people who are calculating the value they are getting from a subscription aren't taking this into account.SemiAnalysis published a snippet of their analysis, and they believe their tokens are an effective price of $0.99/million, rather than $20/million the naive pricing calculation would give you.

reply

bensyverson
 
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

Hey, are you trying to imply that the Emperor has no clothes or something? /s

reply

byzantinegene
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I believe they will last until they IPO, and not long after that. $200/mo plans are not good for their P&L when their users using $10000 worth api credits. That's -98% margin loss per user.

reply

suby
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

People point to the equivalent API costs to show that they are getting a great deal on the subscription, 10,000 dollars worth of tokens for 200 dollars. I do wonder if it's the other way around though - are the API users simply getting ripped off? I have seen Dario say in multiple interviews that they are profitable on inference, which maybe he was only meaning to refer to API usage, but that's not the impression I got.

It's not a 98% margin loss if your users are unwilling to pay 50 times the cost that they were previously paying, and if they have other options like open source providers. The calculus isn't so simple because some portion of users would switch to API, and so it's about how many would continue using the service rather than leaving for a competitor.I'm aware they need to recoup the enormous cost of training and data centers, but on a purely inference cost level I'm not convinced that the 200 dollar plans are unprofitable.

reply

nl
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> I'm not convinced that the 200 dollar plans are unprofitable.

Especially considering not everyone is tokenmaxxing, and in most parts of the world people take leave and companies do not cut their subscriptions.I suspect they are priced to have a lifetime average price/token amount that is roughly break-even, or maybe a slight loss leader.> have seen Dario say in multiple interviews that they are profitable on inference, which maybe he was only meaning to refer to API usage, but that's not the impression I got.I think he does mean API usage. Don't forget they can (and do) adjust the number of tokens you get on each plan at any time to adjust their margins on those.That means he knows that is controllable, and it only the underlaying inference that defines the succes or otherwise of the company.

reply

kelnos
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> 
Especially considering not everyone is tokenmaxxing

Exactly. I have the Claude $100/mo plan, and use it moderately for open source hobby stuff. I still haven't dipped my toes into the Fable pool, but I always use Opus 4.8 on xhigh, and Ineverhit my limits.On the other hand, though, there have been times when I've looked at /usage for a long-running session (e.g., 7-10 days, after it's compacted a few times), and it showed I'd used ~$450 worth of tokens just for that session. So I'm clearly getting value for the money here when it comes to the subscription cost. But I still don't hit limits, so...

reply

victorbjorklund
 
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

Yea, it’s like pointing at the cost of renting all individual movies and TV-series at Netflix and concluding that Netflix subsidizes the subscription with tens of thousands of dollars.

reply

orsorna
 
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

I figured the subsidization is to entice people to give training data.

Are your thought patterns worth 9800 dollars a month?What's the RoR on analyzing those thought patterns?

reply

aroman
 
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

I simply do not believe the switching costs are high enough that they 
could
 eliminate those plans. The Chinese models will eat their lunch.

reply

davedx
 
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

No way in hell are the majority of Claude Code users burning 10k worth of credits. Many of them probably barely use it. There'll be a bell curve, and we have no idea what it looks like.

reply

lnrd
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They don't need to be the majority. One big company paying 200/300k in credits each month easily makes up for the majority of single users not doing so. I believe AI companies today make money through b2b enterprise deals and not selling to individual users, the latter is mostly a marketing expense to get people to use their product instead than the competitors one.

reply

somenameforme
 
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

Open weight models are catching up, and I see no reason to think this will change. That will largely define the economics of this industry. It seems highly improbable that there will be people spending thousands on API credits will be a thing in the future.

reply

hahahaa
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Unless you want to not get rate limited (or banned depending on how close you are sailing to the claw wind)

reply

neonstatic
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> Sure, these plans may be temporary, but none of us really know how temporary they are.

Anthropic emailed me today:Fable 5 moved to usage credits on July 20. It is still available to you, but it requires pay-as-you-go usage credits and is not included in your subscription rate limits.

reply

MertsA
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's going to be on the $20 plan. IIRC the $100 and $200 plans keep the 50% fable usage.

reply

dd8601fn
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

We got emails and UI messages informing us that Fable is now a standard part of Max plans (both sizes).

The half usage limit still applies.

reply

agar
 
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

I'm on Teams and Fable is now usage credit only.

reply

nl
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You are on a Pro plans and standard seats on Team plans: Fable 5 isn't included in your plan's usage limits.

For Premium seats it is.https://support.claude.com/en/articles/15424964-claude-fable...

reply

runtime_lens
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

I wouldn't be surprised if "the best model" becomes a niche concept over the next few years.
For most production systems the winning architecture may end up being an orchestrator that knows when to call a cheap model when to escalate to a stronger one and when to combine multiple outputs.

reply

eunos
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Isnt that the idea from gemini cli?

reply

yieldcrv
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

there are so many branches of evolution here, I also see them converging to a "best model becomes a niche concept" too

the supercycle is on device models, and one of those evolutions is models baked into chip die, and you just upgrade chipsets every few years insteadso it's the hyperscalers that will take the L in that environment

reply

subygan
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

This does not really work well, if you don't know the complexity of the problem ahead of time and ensure all future conversations go to the same model.

Else, you break the cache by doing a round robin of the same conversation across different models. Likely you'll end up paying more than what it would've cost with a cache aware system

reply

lbriner
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

You can use the Ralph Wiggum technique: 
https://ghuntley.com/ralph/

reply

hahahaa
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Cache hits should be part of the strategy.

reply

kamranjon
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

No benchmarks, no info on which models are used, ai generated video, just a signup page with nothing else.

Anyhow, this kinda reminds me of that quote about architecture: "We replaced our monolith with micro services so that every outage could be more like a murder mystery."

reply

adam_rida
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

The evaluator is public here: 
https://echo.tracerml.ai/eval/

It currently exposes 907 stored rows across seven benchmark families, with prompts, outputs, grades, and cost records. More benchmarks are coming soon.Echo does not disclose its per-request routing decision because that policy is the product. We can, however, publish some of the eligible open-weight model pool, version dates, aggregate allocation mix, and evaluation settings without exposing the request-level recipe.New video is also being made.

reply

dannyw
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Echo does not disclose its per-request routing decision because that policy is the product

My honest advice: that's going to pull away a decent amount of potential customers, even though I think your idea/concept is fantastic.For example, if we were to consider it for Canva, observerability and full transparency is critical requirement; we can't accept not knowing which model serves a request. Both for legal/contract reasons, co-ordinated capacity planning with API providers, or even just evaluating our prompts and harnesses; and debugging/tracing results that went wrong. So that renders it out of consideration; and also suggests some kind of adversarial relationship where customers aren't trusted with critical information.I definitely understand you need to keep business value, but I don't think hiding which model a request is routed to, is the right one, or at least if you want to expand to bigger potential customers / more advanced LLM deployments.

reply

lionkor
 
49 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This sounds like you want to contact sales and get a deal that includes some more NDA info? I would assume this is possible for a large enough customer.

reply

monk_grilla
 
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

> Echo does not disclose its per-request routing decision because that policy is the product

I have not had need for a router product thus far so excuse my ignorance if this is standard, but how could I possibly use and improve a product built on a router like this if I am not permitted to see which model served my request? If I got a bad answer back in my LLM-powered app, do I really have no way of knowing which model was responsible?

reply

seizethecheese
 
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

Isn't the relevant benchmark RouterBench? 
https://arxiv.org/html/2403.12031v2#S7

reply

guessmyname
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> 
No benchmarks, no info on which models are used, […]

The benchmarks are here →https://echo.tracerml.ai/eval/They are not good benchmarks but at least they exist.

reply

seizethecheese
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I've been working on a similar project and I found that it's easy to replicate Fable results if you use saturated benchmarks.

In my project, I wasted a huge amount of time trying to improve GPQA Diamond results above ~93% range. I realized my mistake when Fable dropped and made no improvement on this benchmark vs. Opus.

reply

yorwba
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I wouldn't be surprised if ≈7% of GPQA Diamond questions simply have the wrong answer in the ground truth data, so that getting such a question correct is graded as an error. Most machine-learning benchmarks are rather badly validated.

reply

seizethecheese
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yep! I found this interesting article after banging my head against a wall for a long time: 
https://epoch.ai/gradient-updates/gpqa-diamond-whats-left

reply

codekansas
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's basically trying to replicate OpenRouter, which works pretty well and has a lot of nice features to abstract away any single provider, such as failover, metering, autoswitching, etc. It's actually a really smart infrastructure abstraction.

I just wish this were solving an actual problem rather than being a fairly transparent attempt to say something approximating, "Hey VCs, OpenRouter just became a unicorn but I can basically vibe code it"Calling it "Fable-level" feels intellectually lazy / dishonest, but then again, what do you expect when there's so much money on the table.

reply

vunderba
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It feels a bit more like Fugu to me, which acts as a multi-LLM orchestrator (though I think Fugu combines open- and closed-weight models), but without being able to see the “secret sauce” behind how any of them decides the number of "plies" each model in the swarm gets, they all feel rather difficult to compare beyond the big public benchmarks...

https://github.com/SakanaAI/fugu

reply

throw10920
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Isn't Fugu the same kind of thing as NotDiamond[1] (which I believe OpenRouter uses) except not as good?

[1]https://www.notdiamond.ai/

reply

vunderba
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Honestly not sure. I think Fugu tries to leverage multiple models simultaneously where something like NotDiamond is more about picking the most optimal 
singular
 model.

This space is so crowded it feels like I see a new "model router" pop up every few weeks.

reply

seizethecheese
 
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

OpenRouter's model router for coding isn't really sophisticated. This is very different.

reply

dimitrios1
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Unrelated - but reminds me of my favorite quote by tenderlove:

"microservices turn function calls into distributed computing problems"

reply

WD-42
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

grug wonder why big brain take hardest problem, factoring system correctly, and introduce network call too

seem very confusing to grug

reply

XCSme
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I thought login-protected apps are not allowed on Show HN.

reply

j45
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's easy enough to copy and paste in a prompt, no?

Eval tests while giving general indicators might not be similar for each use case.

reply

dluan
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

So this is the dogpile.com of the askjeeves, alta vista, and lycos approach? Time is a flat circle?

reply

ljlolel
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

ensemble models always did the best at Kaggle

we did the same:https://trustedrouter.com/blog/prometheus-2-new-draco-state-...

reply

ignoramous
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You need update your blog posts.

Our whole stack is radically open source — frontend and backend alike, Apache-2.0 licensed — and so is everything behind this benchmark. That is how a benchmark number earns trust: verifiability, not hype.The repos have since been moved toBUSL-1.1:https://github.com/Lore-Hex/quill-router/commit/8155ac666ae0...

reply

glasss
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Good ideas are usually still good across time and tools

reply

onlyrealcuzzo
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Dogpile was only a good idea while Search Engines were mostly trash.

You needed to search all of them to find something decent.That's roughly analogous to today. Ignoring cost, you'd be way better off asking all the LLMs to solve a problem (like coding) where you can verify the answer.So the question is, for things like that -> can a group of models perform better than frontier models, especially at a reasonable cost?Fable is not a great value, so unless you're trying to find answers to Erdos questions, you can probably do better on cost.You can probably typically ask 3 or 4 of the top Chinese models for an answer and get a response for the same Fable question... Given that Fable isn'tthatmuch better, it's not surprising you can do better for a large subset of problems.

reply

Terretta
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> 
Dogpile was only a good idea while Search Engines were mostly trash.

Precisely.

reply

user_7832
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

LLMs fail in such bizzare, obscure methods (to the average observer) at times. Sometimes even simple questions ("who was that x person who was super famous I'm thinking of") type questions fail terribly.

The more vague and non committal and hand-wavey and subjective the field for AI to answer, the better the results (imo).

reply

rablackburn
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I daresay it's because the assistant training corpus is heavily biased towards one-shot solution answers.

Because the correct response to that query is "I have no idea -- you will need to provide more information"and LLM Agents suck at that.

reply

ai-x
 
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

There is no reason a smarter model will not build an internal smarter/efficient router itself

reply

joe_the_user
 
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

Dogpile was only a good idea while Search Engines were mostly trash.

Well, search engines are trash again. Perhaps it should come back

reply

tiffanyh
 
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

Exactly

High quality, fast & cheap (all 3 combined) - is a formula success.It’s just way easier said than done.

reply

Avicebron
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There's a reason most pros will tell you pick two of the three.

reply

hahahaa
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This is the don't use the same EC2 size for everything on your service approach.

reply

gchamonlive
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Well, you can try to make triangular wheels, but they 
are
 round for a reason

reply

ignoramous
 
13 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Mixture of Models
, perhaps? tbf to OP, the setup they're proposing has also been recently evangelized by other "ai gateway" products (like OpenRouter, JusCode, Fireworks etc), so there's likely something useful here.

reply

fmajid
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ensemble Methods:

https://en.wikipedia.org/wiki/Ensemble_learning

reply

johnvanommen
 
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

This sounds like networking.

Did OP invent an “intelligence router?”

reply

alizaki
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Indeed. What a deep cut

reply

moralestapia
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

metacrawler.com

reply

cdelsolar
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

timecube?

reply

tj800x
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

No single signin. Privacy policy allows training. No try it first without credit card. It's a good idea, but this looks premature.

reply

adam_rida
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

You are right that the privacy wording was too broad. We are fixing it now so it states explicitly that Echo does not use customer prompts, files, chats, or outputs to train or fine-tune models. We are updating the matching Terms language at the same time.

Echo also starts users with free credit and does not require a credit card to try it. The current signup flow did not make that clear enough, so we are fixing that presentation too.Thanks for calling both out.

reply

seizethecheese
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If you want to try a similar idea that you can chat with immediately (free tier uses open weight models), I'm working on this: 
http://pellmell.ai

reply

DatCodeMania
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That would open him up to lots of abuse

reply

cynicalsecurity
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I assume trying without a credit card will bankrupt him immediately.

reply

slashdave
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Replace "Show HN:" with "Advertisement:" ?

reply

Arshad-Talpur
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

The business use case of rather than going on one model choosing the best openweight model and reducing the cost seems fascinating, however the context memory, or auditability of what is happening behind would be more complicated, even within single model we have to spend tons of time to decode and understand llm behavior , add context layers and so on, having said that for GenAI executions this might be the direction. Wish you best for the project

reply

meander_water
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Seems similar to Openrouter Fusion - 
https://openrouter.ai/docs/guides/routing/routers/fusion-rou...

reply

seizethecheese
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Fusion is a totally different approach, though similar in the sense that it leverages different models.

Fusion generates many replies then synthesizes. This adds a ton of latency and cost, so it's going to be better only for cases where you're willing to wait a lot and pay a lot more.Routers (like this project) are a different thing, they can theoretically improve performance and cost at the same time without increasing latency much. I'm a bit skeptical though, since knowing which LLM is going to be better on a cost adjusted basis is hard (seehttps://artificialanalysis.ai/models/capabilities/coding?cos..., where the cost per task vs. performance is not what you expect, for example comparing Qwen 3.7 Max to GPT Sol.A project I'm working on is aimed at improving performance without added latency but from a different angle. Instead of waiting for all replies for synthesis (like OpenRouter Fusion), it streams the "best" reply immediately (using a router to pick the best model) then synthesizes with emoji reactions and optional replies from the background models. It's free to use here with no login:http://pellmell.ai

reply

springtimesun
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been trying something like this with local only models. I think I’ve tried everything that will fit in 96GB alone and in concert with each other using real project data (Rails). I haven’t found much benefit to anything other than Qwen 3.6 27b dense feeding a Claude final pass. I really thought layering was going to work like the law of large numbers, but for my workload it just hasn’t.

reply

XCSme
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

I have a spare 3090 that I want to use to off-load some tasks from Claude to a local model (probably Qwen 3.6 27b), any success with that? Is it good enough to follow some tasks, coding requirements or browser usage?

reply

stevefan1999
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

So it is a mixture of models, then each model have a mixture of experts, making it mixture of mixture of experts...why don't we just make it simple and have a central expert router made up of random forest...all we need some kind of actor system to share the gradients of the experts...and ensemble it

reply

jdthedisciple
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Grandiose claims that are hardly backed up at all.

I find that very off-turning!

reply

elnatro
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Have you taken a look at 
https://echo.tracerml.ai/eval/
? It looks promising for sure!

reply

jdthedisciple
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

None of those are SWE.

And still Fable beats it hands down 8-0 in one of them, and is atworsteven in some others.Also it doesn't make logical sense: A router can save costs, yes, but not magically be "smarter" somehow.That's like selling "free energy".

reply

sudo_cowsay
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Hi this is very cool. As a student (read: more dumb than adults), I find the eval page too loaded with words. Maybe more graphs could help?

reply

jmspring
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

So the word security or any topic related to it is mentioned and it flips to an older gen model? Fable is nearly useless now it you do anything around auth.

reply

dijit
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

I can get it to write win32 unsafe rust code.

I can't get it to review win32 unsafe rust code.Make it make sense.

reply

jmspring
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

<snark>need bigger check to guy in DC</snark>

reply

ljlolel
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

we did it with 1/10 the cost with Prometheus-1.0 and further 
https://trustedrouter.com/blog/prometheus-2-new-draco-state-...

reply

15 hours ago
 
 | 
prev
 | 
next
 
[2 more]

[deleted]
adam_rida
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

Thanks for checking the individual rows. HumanEval+ is one small code slice, not the whole basis for the launch claim. The public evaluator currently contains 907 rows across seven benchmark families, and matched SWE-bench Verified and BigCodeBench runs are the next code evidence being added.

You also found a real UI bug: the inspector should show both stored answers and currently does not in some rows. We are fixing that.On the row you reran: the page records a frozen matched run. It does not claim that Fable is incapable of solving that prompt on another run. We are adding repeated matched trials and making run count and variance explicit. Your rerun is exactly the kind of external check the row-level page is intended to make possible.The broader result remains: Echo is competitive with Fable across the evaluated task mix at materially lower measured inference cost. We are filling in the harder agentic-code evidence now rather than asking anyone to infer it from HumanEval+.

reply

Alifatisk
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

This reminds me on OpenRouters report that combining multiple different models gave comparable performance to Fable 5. I think this approach has lots of potential. Maybe OpenAi was ahead of its time with GPT-5 (it being a router to different models rather than just being one new model)

reply

seizethecheese
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

You might be interested in a project that I'm working on, which is kind of like OpenRouter Fusion, but instead of waiting for all models to synthesize, we stream the best model immediately and background the rest. The background models then reconcile with an emoji reaction and optional reply. It gets similar results to Fusion and is a lot faster! There's a free version that leverages open weight models here: 
http://pellmell.ai
.

reply

NetOpWibby
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I like that I was able to test without an account and my prompt (What's the feasibility of a NetNavi IRL, along with a PErsonal Terminal? Create a document that outlines how to make this happen.) makes me think Pellmell is gonna be a research tool I'll continue to use.

reply

hmokiguess
 
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

This is really cool, super fun!

reply

tintor
 
12 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

OpenAI's router chooses between models of different sizes, which are still trained on roughly the same data. Its purpose is to reduce infra cost for OpenAI for simpler queries. No need to pay for GPT 5.6 Sol inference for "Hello" prompt.

reply

jmaw
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I think approaches like this have potential. Only time will tell. This reminds me of the mixture of experts taken by deepseek r2 (I think it was r2, at least), but less specific models I guess.

I have often wondered how tools like GHCP choose the best model for the job when set to "auto".

reply

blobbers
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm curious if there is measurable value in diversity of thought, and if there's diminishing returns on a single models thought pattern.

For example, compute X tokens with model A, then feed those into model B, etc. to get chain of thought through a diverse set of mdoels rather than chain of thought through a heterogeneous chain.Humans seem to strongly believe echo chambers are bad. Are LLMs the same?

reply

lelanthran
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

The models are all converging, there is no diversity in any single generation.

reply

adam_rida
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

there are and this what you optimize for. ensemble learning has a long literature on this. you want models that have the most diverse pool of capabilities so they complement each other. in verifiable tasks or classification this is straightfroward but a bit tricker in open ended text gen or CoT. this is one of our core research question

reply

blobbers
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

My experience is mostly around either ensembles of weak learners that are bootstrapped to create a strong learner, or around boosted learners where you're training on residuals. With CoT you're sort of adding entropy to your answer, but you're also possibly getting a more thorough answer?

I'm curious though if these training methods are convergent or are models actually different; just like how in the stock market people think they're "diversified" but the truth is their exposure is likely much more risk correlated than one might think.In certain situations, one right answer is better than a committee discussing the problem, but in others its sometimes nice to have some alternative methods of solving something. Fun project nonetheless.My approach to using multiple models has been less about CoT but more about time to first token, and how you can use a small model to start interacting with the user while in parallel the more complex model is building a larger more complex thought. My work on this was primarily for voice backed interfaces before the voice models became quite a lot faster.

reply

thatxliner
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

How is this different from what that feature OpenRouter does?

reply

hahahaa
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

Not much probably but I'd rather my agentic system route to model choice (happy to use OpenRouter as a catalog) than something in the cloud. I.e. pi.dev routes > call this and it decides based on today's algo. In other words routing should be in my source code not yours.

reply

SubiculumCode
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Isn't the issue with the approach generally that it ends up costing more?

reply

alightsoul
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

There's so many people reimplementing Sakana fugu from its two ICLR papers but no open source version of it.

reply

yonatan8070
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm not an expert on this, but this sounds a lot like a larger-scale MoE (Mixture of Experts) type of architecture.

As I understand it, in an MoE model, you essentially have hundreds of smaller sub-models ("experts") that are good at different tasks, and for every generated token, a single "master" model chooses which ones are most relevant to participate, and you only activate them.

reply

janalsncm
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

In MoE systems the routing decision is made per-token, not per prompt or task. It’s one of ML’s many confusing naming conventions.

Even more confusingly, there are older pre-LLM MoE systems which ensemble and pool the predictions from multiple sub-components. For example in a random forest you could take the majority vote of the decision trees or the average of their numerical predictions.After that, we developed neural net architectures for predicting a single thing like whether the user will click on your ad. An MMoE is in the same family.And so now we are at massive MoE networks for LLMs which have similarities with MMoE in that the “decision” is about the very next token to predict.

reply

lukan
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

"In MoE systems the routing decision is made per-token, not per prompt or task."

Have there been experiments with doing it per task? Like, "oh this is python project, use this model" "oh this is about writing fantasy, use this"?

reply

janalsncm
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It’s a good idea. The results probably depend a lot on how close your task is to the benchmarks though.

I think OpenAI already has (had?) a feature like this called “auto” mode for thinking.

reply

alex-moon
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

I started building something like this myself (codename HFG - "Heroku for Groq") anticipating what we are indeed now seeing in ChatGPT viz. enshittification. The intention was to aim it at consumers and non-technical users who want a chatbot to help them draft reports, synthesise papers and so on. You've got a bunch of hackers in the comments going "But how can I run my own evals?" I think the answer for them is: this isn't for you.

Don't want to derail what you're trying to do with Echo in case I'm wide of the mark, but yeah even in that case, if you hadn't considered that use case for it, I reckon there will, probably inside six months, be a substantial market for non-technical users who are sick of seeing ads in a service they already pay a subscription for, and who don't care what the underlying model is - or, indeed, don't even understand the concept of an "underlying model" because they interface with AI as a product.You have already taken the HFG idea way further than I had even thought of yet, and I feel vindicated in seeing someone else do it. I wish you the very best!

reply

zhonglin
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Sounds like another token router. Not sure what is the benifit compared with codex, I used 5.6 Sol, codex already route some of the task to luna not sol.

reply

haris599
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Can you simply ensemble the outputs of all N models for each token? I'm curious how that compares to explicitly routing each token to a different model.

reply

janalsncm
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

Intuitively, your savings depend heavily on how hard the tasks are in the first place. If you have a base rate where 99% of your tasks can be routed to a cheap model, yeah, you can save a ton by not using Fable for that.

So “1/3 the cost” really depends.

reply

seizethecheese
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

Sometimes expensive models are cheaper on easier tasks because they use fewer tokens, too.

reply

janalsncm
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah apparently Opus and Sonnet are like that.

reply

seizethecheese
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yep! There are a lot of models like this: 
https://artificialanalysis.ai/models/capabilities/coding?cos...

reply

indiantinker
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I have been using this : 
https://magnitude.dev/
 for a while now. Is it something similar you are doing? I would love to have something that would connect to my codex, Claude, and opencode subscription rather than having to make a new subscription.

reply

Art9681
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

The "ensemble of models" is nothing new. It's just that it's not really a moat that can be monetized. In the end you're always paying for something. You can engineer an elaborate harness with multiple models but it is not going to particularly solve a novel problem that the frontier models can with the same level of efficiency. You're saving money and paying with time. You're going to pay with something one way or another no matter what.

The frontier providers aren't dumb. They charge what they charge because they know this. If you think Fable is too expensive then the type of problems you are solving don't demand that level of capability.If you are working on something cutting edge, something truly novel, the cost of frontier AI is well worth its price.With all that being said. No one is going to complain if we can get the same capability at a lower cost. And I mean true parity. Not trading space for time.

reply

qainsights
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Can't sign up: `too many authentication attempts`

reply

adam_rida
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

looking at it now

reply

raver1975
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

I can't sign up: too many authentication attempts

reply

adam_rida
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

looking at it now

reply

jacobgold
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

> 
Fable-level results at 1/3 the cost using open-weight models

But we get ~$2500/mo worth of Fable credits for $200/mo on Anthropic pan? I'm still confused why people (who don't have to use API billing) are chasing open weight models based on cost.

reply

teruakohatu
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Because that is a short term solution, it won’t be offered forever. Large organisations have to purchase credits at $/tokens. Eventually everyone else will too.

reply

sscaryterry
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is what OpenAI and Anthropic are trying to make everyone believe. Most accountants will flinch at this (they already are).

The $200 odd plans are already out of reach of many, many people.The attrition of customers if they were to get rid of these subscriptions plans would be untenable.

reply

recursivegirth
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think you are looking at it incorrectly. No business is buying individual accounts, because if they do, they open themselves up to considerable risk.

The $200 plans are priced so that the power-users use them and then advocate about how great the product is. If you're buying a $200 plan, you're not doing it because of the price point but rather because of the amount of work it is doing for you.

reply

trollbridge
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Lots of businesses are buying and using these plans. Basically every small business I interact with.

reply

anonzzzies
 
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

All companies we interact with have 200 plans.

reply

combyn8tor
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You may want to consider the incomes of developers outside the US, students, unemployed. $200/month is a lot to a lot of people.

reply

gruez
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The point still stands. The chinese labs don't have super discounted plans, so if the price per task benchmarks[1] are correct, and we apply the discount, you'll actually be paying more by using cheaper chinese models and this technique.

https://artificialanalysis.ai/agents/coding-agents#artificia...

reply

combyn8tor
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The point doesn't stand, and this comment appears to be spam.

reply

dbbk
 
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

They can still write code.

reply

eikenberry
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I think most people assume the subsidized plans will go away or get more limited eventually. They are basically a loss leader and a marketing cost that is very flexible and easy to change w/o directly impacting their primary customers.

reply

dberg
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

doesnt exist for enterprise plans

reply

recursivegirth
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[6 more]

[flagged]
dang
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> 
The good ole American way.

Could you please stop posting unsubstantive comments and flamebait? You've unfortunately been doing it repeatedly. It's not what this site is for, and destroys what it is for.If you wouldn't mind reviewinghttps://news.ycombinator.com/newsguidelines.htmland taking the intended spirit of the site more to heart, we'd be grateful.

reply

drnick1
 
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

> When they are successful at making those illegal/inaccessible

This would be like trying to outlaw Linux or peer-to-peer file sharing. It's technically possible to write and pass a law, but it's basically impossible to enforce it.

reply

switchbak
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Enough to make it a non-started at the organizations that pay their bills. Everyone else isn't big enough to matter.

reply

trollbridge
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Going to be an interesting world where big enterprises have to spend 100X the cost for the same value of AI as startups and small businesses.

reply

recursivegirth
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think they call that inflation :).

reply

bbstats
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

M-o-MoE

reply

zuzululu
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

1/3rd of fable ? not interested

reply

islambaraka
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

What signals does Echo use to decide which models should participate before it has seen their outputs?

reply

fneddy
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

That’s basically the same idea IBM advertises with Bob?

reply

seizethecheese
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

This looks different, it's not a main agent delegating to subagents, it's a router.

reply

wizche
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

how does this differs from OpenRouter fusion?

reply

cawingcrow
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

how does this differs from Sakana Fugu?

reply

bnjemian
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

I don’t find the recent spate of blog posts and systems delegating and combining LLMs to get better performance particularly interesting. Especially given that anyone who’s taken an ML 101 course has learned about ensemble methods.

While an LLM isn’t what you’d traditionally consider a weak learner, the theorems on learning systems clearly point to them being so in this context. The feigned surprise at combining them to yield better results seems disingenuous.Even so, the work to predict which models are best suited for which task, how to delegate, and how to combine their outputsisinteresting, especially if you’re placing a cost minimization objective on it. That said, this isn’t too far off from what many AI labs are already doing.

reply

abernard1
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

The entirety of "agents" and tool calls is a process of combining LLMs to get better results. Is it the same LLM in many cases? Yes. But it doesn't have to be.

It's the natural move that happened after people realized you couldn't throw away half a century of AI research.Most of these focus on costs. But it is simply the case that the one-shot output did not scale for harder problems on workflows.

reply

codekansas
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Fable-level, yea, but can it run gstack?

reply

ninjahawk1
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

I’m very confused on what this is, my initial thought was “oh nice, open source router.”

I go to the website…and it’s a sign up. I expected a repo. Otherwise how do I use it? As a SaaS? Yeah right.Oh well I guess at least the benchmarks are good…I find the benchmarks and many are either not present or are not what the title claims.My main question is how this has so many updoots from HN, probably the passerby not looking closer for sure.I mean no offense and I really do wish you best on this, but it seems like what we used to call back in the day, vaporware.

reply

fgoose180
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

enjoying how people are re-discovering ensemble methods.

reply

cantalopes
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

By the way, is it just me or opus 4.8 is much better at some programming tasks than fable? I've been really disappointed lately, i stopped using it evem though it's "premium on my subscription"

reply

meowface
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

It's just you. Fable 5 is consistently better than Opus 4.8 at literally every single level, for me. (I always use both at xhigh, for reference.) I could go down a laundry list of various issues I have with Opus that I don't have with Fable. For me, Opus 4.8 < GPT-5.6 Sol < Fable 5.

Plus Fable is way less annoying to talk to than Opus 4.8. Opus 4.8's writing style is absolutely insufferable. Fable has some of the same quirks but it's way less bad.

reply

anonzzzies
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

We see no difference between opus 4.8 and fable except that fable is slower. So +1 for not just GP. We use neither interactive, just via our own tooling so the ‘talk to’ doesn’t apply and we use it 24/7. We currently run 25% of tasks on both fable and opus and the rest only opus. The 25% are being code reviewed side by side and we do detect when fable switches to opus for ‘security concerns’ nonsense. Opus generally finishes sooner, results are similar quality.

reply

purplecats
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

but u wouldnt get caching savings

reply

seizethecheese
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

You definitely still would, but you need to pay the full input cost twice, so the equation really depends on how much first message vs repeat message matter.

reply

retinaros
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ttl 1 hour maybe. 5min? Never

reply

jambalaya8
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Might want to rethink the name to avoid an Amazon issue.

reply

maxdo
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

such a scam, there is only one fable-like model, that somewhat behind, it cost half, not 3x. so from here you can stop reading.

reply

seizethecheese
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

They're obviously not claiming this is a new model that is fable-like at 1/3. It's a router that saves money by only using Fable when necessary. I don't think you should be calling someone's post a "scam" without doing a minimum of research. (I'm not associated with the company, but very interested in this.)

reply

j45
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

If you copy Perplexity, they let you have the first few rounds of chat for free to get you going before asking to sign up.

reply

ototot
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Is this yet another Sakana Fugu / OpenRouter Fusion?

reply

kachnuv_ocasek
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

Looks like it but with open-weights only.

reply

hmokiguess
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

"Backed by YCombinator"

https://www.ycombinator.com/companies?query=tracermlI don't see it?

reply

zachdotai
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

Not all YC companies have launched publicly yet but I am a current YC founder and I can confirm they exist in the internal directory.

reply

dang
 
9 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You're right to be skeptical; I saw a totally fake case of this just yesterday.

But in the present case, they're just a startup in the current batch.

reply

Consider applying for YC's Fall 2026 batch! 
Applications
 are open till July 27.

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