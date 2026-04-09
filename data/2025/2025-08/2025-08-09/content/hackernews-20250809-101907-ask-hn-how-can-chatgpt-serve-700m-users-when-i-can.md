---
title: 'Ask HN: How can ChatGPT serve 700M users when I can''t run one GPT-4 locally? | Hacker News'
url: https://news.ycombinator.com/item?id=44840728
site_name: hackernews
fetched_at: '2025-08-09T10:19:07.703679'
original_url: https://news.ycombinator.com/item?id=44840728
author: superasn
date: '2025-08-09'
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
Ask HN: How can ChatGPT serve 700M users when I can't run one GPT-4 locally?
235 points
 by
superasn

4 hours ago

 |
hide
 |
past
 |
favorite
 |
162 comments
Sam said yesterday that chatgpt handles ~700M weekly users. Meanwhile, I can't even run a single GPT-4-class model locally without insane VRAM or painfully slow speeds.

Sure, they have huge GPU clusters, but there must be more going on - model optimizations, sharding, custom hardware, clever load balancing, etc.What engineering tricks make this possible at such massive scale while keeping latency low?Curious to hear insights from people who've built large-scale ML systems.

canyon289

4 hours ago

 |
next

[–]

I work at Google on these systems everyday (caveat this is my own words not my employers)). So I simultaneously can tell you that its smart people really thinking about every facet of the problem, and I can't tell you much more than that.

However I can share this written by my colleagues! You'll find great explanations about accelerator architectures and the considerations made to make things fast.https://jax-ml.github.io/scaling-book/In particular your questions are around inference which is the focus of this chapterhttps://jax-ml.github.io/scaling-book/inference/Edit:
Another great resource to look at is the unsloth guides. These folks are incredibly good at getting deep into various models and finding optimizations, and they're very good at writing it up. Here's the Gemma 3n guide, and you'll find others as well.https://docs.unsloth.ai/basics/gemma-3n-how-to-run-and-fine-...

reply

KaiserPro

2 hours ago

 |
parent
 |
next

[–]

Same explanation but with less mysticism:

Inference is (mostly) stateless. So unlike training where you need to have memory coherence over something like 100kmachinesand somehow avoid the certainty of machine failure, you just need to route mostly small amounts of data to a bunch of big machines.I don't know what the specs of their inference machines are, but where I worked the machines research used were all 8gpu monsters. so long as your model fitted in (combined) vram, you could job was a goodun.To scale the secret ingredient was industrial amounts of cash. Sure we had DGXs (fun fact, nvidia sent literal gold plated DGX machines) but they wernt dense, and were very expensive.Most large companies have robust RPC, and orchestration, which means the hard part isn't routing the message, its making the model fit in the boxes you have. (thats not my area of expertise though)

reply

blibble

1 hour ago

 |
parent
 |
prev
 |
next

[–]

> So I simultaneously can tell you that its smart people really thinking about every facet of the problem, and I can't tell you much more than that.

"we do 1970s mainframe style timesharing"there, that was easy

reply

tough

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Doesn't google have TPU's that makes inference of their own models much more profitable than say having to rent out NVDIA cards?

Doesn't OpenAI depend mostly on its relationship/partnership with Microsoft to get GPUs to inference on?Thanks for the links, interesting book!

reply

ActorNightly

4 hours ago

 |
root
 |
parent
 |
next

[–]

Yes. Google is probably gonna win the LLM game tbh. They had a massive head start with TPUs which are very energy efficient compared to Nvidia Cards.

reply

baxtr

2 hours ago

 |
root
 |
parent
 |
next

[–]

The only one who can stop Google is Google.

They’ll definitely have the best model, but there is a chance they will f*up the product / integration into their products.

reply

scarface_74

2 hours ago

 |
root
 |
parent
 |
next

[–]

It would take talent for them to mess up hosting businesses who want to use their TPUs on GCP.

But then again even there, their reputation for abandoning products, lack of customer service, condescension when it came to large enterprises’ “legacy tech” lets Microsoft who is king of hand holding big enterprise and even AWS run rough shod over them.When I was at AWS ProServe, we didn’t even bother coming up with talking points when competing with GCP except to point out how they abandon services. Was it partially FUD? Probably. But it worked.

reply

serf

1 hour ago

 |
root
 |
parent
 |
next

[–]

>It would take talent for them to mess up hosting businesses who want to use their TPUs on GCP.

there are few groups as talented at losing a head start as google.

reply

JoshuaDavid

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

Google employees collectively have a lot of talent.

reply

davedx

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

But they’re ASICs so any big architecture changes will be painful for them right?

reply

edoceo

30 minutes ago

 |
root
 |
parent
 |
next

[–]

I'd think no. They have the hardware and software experience, likely have next and next-next plans in place already. The big hurdle is money, which G has a bunch of.

reply

stogot

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

Hasn’t the Inferentia chip been around long enough to make the same argument? AWS and Google probably have the same order of magnitude of their own custom chips

reply

fakedang

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

Yeah honestly. They could just try selling solutions and SLAs combining their TPU hardware with on-prem SOTA models and practically dominate enterprise. From what I understand, that's GCP's gameplay too for most regulated enterprise clients.

reply

ActorNightly

2 hours ago

 |
root
 |
parent
 |
next

[–]

Googles bread and butter is advertising, so they have a huge interest in keeping things in house. Data is more valuable to them than money from hardware sales.

Even then, I think that their primary use case is going to be consumer grade good AI on phones. I dunno why Gemma QAT model fly so low on the radar, but you can basically get full scale Llamma 3 like performance from a single 3090 now, at home.

reply

klik99

1 hour ago

 |
root
 |
parent
 |
next

[–]

It’s my understanding that google makes bulk of ad money from search ads - sure they harvest a ton of data but it isn’t as valuable to them as you’d think. I suspect they know that could change so they’re hoovering up as much as they can to hedge their bets. Meta on the other hand is all about targeted ads.

reply

fakedang

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

https://www.cnbc.com/2025/04/09/google-will-let-companies-ru...

Google has already started the process of letting companies self-host Gemini, even on NVidia Blackwell GPUs.Although imho, they really should bundle it with their TPUs as a turnkey solution for those clients who haven't invested in large scale infra like DCs yet.

reply

canyon289

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

Im a research person building models so I can't answer your questions well (save for one part)

That is, as a research person using our GPUs and TPUs I see first hand how choices from the high level python level, through Jax, down to the TPU architecture all work together to make training and inference efficient. You can see a bit of that in the gif on the front page of the book.https://jax-ml.github.io/scaling-book/I also see how sometimes bad choices by me can make things inefficient. Luckily for me if my code/models are running slow I can ping colleagues who are able to debug at both a depth and speed that is quite incredible.And because were on HN I want to preemptively call out my positive bias for Google! It's a privilege to be able to see all this technology first hand, work with great people, and do my best to ship this at scale across the globe.

reply

catigula

40 minutes ago

 |
parent
 |
prev
 |
next

[–]

A lot of really smart people working on problems that don't even really need to be solved is an interesting aspect of market allocation.

reply

YossarianFrPrez

30 minutes ago

 |
root
 |
parent
 |
next

[–]

Can you explain what you mean about 'not needing to be solved'? There are versions of that kind of critique that would seem, at least on the surface, to better apply to finance or flash trading.

I ask because scaling an system that a substantially chunk of the population finds incredibly useful, including for the more efficient production of public goods (scientific research, for example) does seem like a problem that a) needs to be solved from a business point of view, and b) should be solved from a civic-minded point of view.

reply

abletonlive

23 minutes ago

 |
root
 |
parent
 |
next

[–]

They won’t be honest and explain it to you but I will. Takes like the one you’re responding to are from loathsome pessimistic anti-llm people that are so far detached from reality they can just confidently assert things that have no bearing on truth or evidence. It’s a coping mechanism and it’s basically a prolific mental illness at this point

reply

catigula

27 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

People are starving to death and the world's brightest engineers are under NDA trying to figure out how to scale clusters of tik tok and ad slop.

No solution is proposed here but the truth is on its face comic.

reply

hattmall

17 minutes ago

 |
root
 |
parent
 |
next

[–]

The only solution to those people starving to death is to kill the people that benefit from them starving to death. It's a solved problem, the solution isn't palatable. No one is starving to death because of a lack of engineering prowess.

reply

catigula

10 minutes ago

 |
root
 |
parent
 |
next

[–]

Figuring out how to align misaligned incentives is an engineering problem. Obviously I disavow what you said, I reject all forms of advocacy of violence.

reply

vermilingua

32 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Well, we all thought advertising was the worst thing to come out of the tech industry, someone had to prove us wrong!

reply

virgil_disgr4ce

19 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> working on problems that don't even really need to be solved

Very, very few problems _need_ to be solved. Feeding yourself is a problem that needs to be solved in order for you to continue living. People solve problems for different reasons. If you don't think LLMs are valuable, you can just say that.

reply

catigula

9 minutes ago

 |
root
 |
parent
 |
next

[–]

The notion that simply pretending to not understand that I was making a value judgment about worth is an argument is tiring.

reply

jackhalford

2 hours ago

 |
parent
 |
prev
 |
next

[–]

Why does the unsloth guide for gemma 3n say:

> llama.cpp an other inference engines auto add a <bos> - DO NOT add TWO <bos> tokens! You should ignore the <bos> when prompting the model!That makes the want to try exactly that? Weird

reply

ignoramous

2 hours ago

 |
parent
 |
prev
 |
next

[–]

>
Another great resource to look at is the unsloth guides.

And folks at LMSys:https://lmsys.org/blog/Large Model Systems (LMSYS Corp.) is a 501(c)(3) non-profit focused on incubating open-source projects and research. Our mission is to make large AI models accessible to everyone by co-developing open models, datasets, systems, and evaluation tools. We conduct cutting-edge machine learning research, develop open-source software, train large language models for broad accessibility, and build distributed systems to optimize their training and inference.

reply

airhangerf15

4 hours ago

 |
prev
 |
next

[–]

An H100 is a $20k USD card and has 80GB of vRAM. Imagine a 2U rack server with $100k of these cards in it. Now imagine an entire rack of these things, plus all the other components (CPUs, RAM, passive cooling or water cooling) and you're talking $1 million per rack, not including the costs to run them or the engineers needed to maintain them. Even the "cheaper"

I don't think people realize the size of these compute units.When the AI bubble pops is when you're likely to be able to realistically run good local models. I imagine some of these $100k servers going for $3k on eBay in 10 years, and a lot of electricians being asked to install new 240v connectors in makeshift server rooms or garages.

reply

semi-extrinsic

3 hours ago

 |
parent
 |
next

[–]

What do you mean 10 years?

You can pick up a DGX-1 on Ebay right now for less than $10k. 256 GB vRAM (HBM2 nonetheless), NVLink capability, 512 GB RAM, 40 CPU cores, 8 TB SSD, 100 Gbit HBAs. Equivalent non-Nvidia branded machines are around $6k.They are heavy, noisy like you would not believe, and a single one just about maxes out a 16A 240V circuit. Which also means it produces 13 000 BTU/hr of waste heat.

reply

kj4ips

2 hours ago

 |
root
 |
parent
 |
next

[–]

Fair warning: the BMCs on those suck so bad, and the firmware bundles are painful, since you need a working nvidia-specific container runtime to apply them, which you might not be able to get up and running because of a firmware bug causing almost all the ram to be presented as nonvolatile.

reply

ksherlock

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

It's not waste heat if you only run it in the winter.

reply

hdgvhicv

1 hour ago

 |
root
 |
parent
 |
next

[–]

Opt if you ignore that both gas furnaces and heat pumps are more efficient than resistive loads.

reply

tgma

1 hour ago

 |
root
 |
parent
 |
next

[–]

Heat pump sure, but how is gas furnace more efficient than resistive load inside the house? Do you mean more
economical
 rather than more efficient (due to gas being much cheaper/unit of energy)?

reply

meatmanek

1 hour ago

 |
root
 |
parent
 |
next

[–]

Depends where your electricity comes from. If you're burning fossil fuels to make electricity, that's only about 40% efficient, so you need to burn 2.5x as much fuel to get the same amount of heat into the house.

reply

Tade0

27 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I'm in the market for an oven right now and 230V/16A is the voltage/current the one I'll probably be getting operates under.

At 90°C you can do sous vide, so basically use that waste heat entirely.For such temperatures you'd need a CO2 heat pump, which is still expensive. I don't know about gas, as I don't even have a line to my place.

reply

_zoltan_

0 minutes ago

 |
root
 |
parent
 |
next

[–]

90C for sous vide??? You're going to kill any meal at 90.
eulgro

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

> 13 000 BTU/hr

In sane units: 3.8 kW

reply

andy99

2 hours ago

 |
root
 |
parent
 |
next

[–]

You mean 1.083 tons of refrigeration

reply

Skunkleton

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

> In sane units: 3.8 kW

5.1 Horsepower

reply

_kb

3 minutes ago

 |
root
 |
parent
 |
next

[–]

3.8850 poncelet

reply

ta12653421

27 minutes ago

 |
root
 |
parent
 |
prev
 |
next

[–]

But ... can it run Crysis?

:D

reply

quickthrowman

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

You’ll need (2) 240V 20A 2P breakers, one for the server and one for the 1-ton mini-split to remove the heat ;)

reply

Dylan16807

2 hours ago

 |
root
 |
parent
 |
next

[–]

Matching AC would only need 1/4 the power, right? If you don't already have a method to remove heat.

reply

quickthrowman

2 hours ago

 |
root
 |
parent
 |
next

[–]

Cooling BTUs already take the coefficient of performance of the vapor-compression cycle into account. 4w of heat removed for each 1w of input power is around the max COP for an air cooled condenser, but adding an evaporative cooling tower can raise that up to ~7.

I just looked at a spec sheet for a 230V single-phase 12k BTU mini-split and the minimum circuit ampacity was 3A for the air handler and 12A for the condenser, add those together for 15A, divide by .8 is 18.75A, next size up is 20A. Minimum circuit ampacity is a formula that is (roughly) the sum of the full load amps of the motor(s) inside the piece of equipment times 1.25 to determine the conductor size required to power the equipment.So the condensing unit likely draws ~9.5-10A max and the air handler around ~2.4A, and both will have variable speed motors that would probably only need about half of that to remove 12k BTU of heat, so ~5-6A or thereabouts should do it, which is around 1/3rd of the 16A server, or a COP of 3.

reply

Dylan16807

2 hours ago

 |
root
 |
parent
 |
next

[–]

Well I don't know why that unit wants so many amps. The first 12k BTU window unit I looked at on amazon uses 12A at 115V.

reply

kelnos

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

Well, get a heat pump with a good COP of 3 or more, and you won't need
quite
 as much power ;)

reply

Scoundreller

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

Just air freight them from 60 degrees North to 60 degrees South and vice verse every 6 months.

reply

CamperBob2

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

Are you talking about the guy in Temecula running two different auctions with some of the same photos (356878140643 and 357146508609, both showing a missing heat sink?) Interesting, but seems sketchy.

How useful is this Tesla-era hardware on current workloads? If you tried to run the full DeepSeek R1 model on it at (say) 4-bit quantization, any idea what kind of TTFT and TPS figures might be expected?

reply

oceanplexian

40 minutes ago

 |
root
 |
parent
 |
next

[–]

I can’t speak to the Tesla stuff but I run an Epyc 7713 with a single 3090 and creatively splitting the model between GPU/8 channels of DDR4 I can do about 9 tokens per second on a q4 quant.

reply

CamperBob2

33 minutes ago

 |
root
 |
parent
 |
next

[–]

Impressive. Is that a distillation, or the real thing?

reply

invaliduser

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Even is the AI bubble does not pops, your prediction about those servers being available on ebay in 10 years will likely be true, because some datacenters will simply upgrade their hardware and resell their old ones to third parties.

reply

potatolicious

2 hours ago

 |
root
 |
parent
 |
next

[–]

Would anybody buy the hardware though?

Sure, datacenters will get rid of the hardware - but only because it's no longer commercially profitable run them, presumably because compute demands have eclipsed their abilities.It's kind of like buying a used GeForce 980Ti in 2025. Would anyone buy them and run them besides out of nostalgia or curiosity? Just the power draw makes them uneconomical to run.Much more likely every single H100 that exists today becomes e-waste in a few years. If you have need for H100-level compute you'd be able to buy it in the form of new hardware for way less money and consuming way less power.For example if you actually wanted 980Ti-level compute in a desktop today you can just buy a RTX5050, which is ~50% faster, consumes half the power, and can be had for $250 brand new. Oh, and is well-supported by modern software stacks.

reply

CBarkleyU

2 hours ago

 |
root
 |
parent
 |
next

[–]

Off topic, but I bought my (still in active use) 980ti literally 9 years ago for that price. I know, I know, inflation and stuff, but I really expected more than 50% bang for my buck after 9 whole years…

reply

belter

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

Except their insane electricity demands will still be the same, meaning nobody will buy them. You have plenty of SPARC servers on Ebay.

reply

cicloid

3 hours ago

 |
root
 |
parent
 |
next

[–]

There is also a community of users known for not making sane financial decisions and keeping older technologies working in their basements.

reply

dijit

2 hours ago

 |
root
 |
parent
 |
next

[–]

But we are few, and fewer still who will go for high power consumption devices with esoteric cooling requirements that generate a lot of noise.

reply

mattmanser

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

Someone's take on AI was that we're collectively investing billions in data centers that will be utterly worthless in 10 years.

Unlike the investments in railways or telephone cables or roads or any other sort of architecture, this investment has a very short lifespan.Their point was that whatever your take on AI, the present investment in data centres is a ridiculous waste and will always end up as a huge net loss compared to most other investments our societies could spend it on.Maybe we'll invent AGI and he'll be proven wrong as they'll pay back themselves many times over, but I suspect they'll ultimately be proved right and it'll all end up as land fill.

reply

toast0

2 hours ago

 |
root
 |
parent
 |
next

[–]

The servers may well be worthless (or at least worth a lot less), but that's pretty much true for a long time. Not many people want to run on 10 year old servers (although I pay $30/month for a dedicated server that's dual Xeon L5640 or something like that, which is about 15 years old).

The servers will be replaced, the networking equipment will be replaced. The building will still be useful, the fiber that was pulled to internet exchanges/etc will still be useful, the wiring to the electric utility will still be useful (although I've certainly heard stories of datacenters where much of the floor space is unusable, because power density of racks has increased and the power distribution is maxed out)

reply

bespokedevelopr

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

If it is all a waste and a bubble, I wonder what the long term impact will be of the infrastructure upgrades around these dcs. A lot of new HV wires and substations are being built out. Cities are expanding around clusters of dcs. Are they setting themselves up for a new rust belt?

reply

abeyer

1 hour ago

 |
root
 |
parent
 |
next

[–]

Or early provisioning for massively expanded electric transit and EV charging infrastructure, perhaps.

reply

jonplackett

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

They probably are right, but a counter argument could be how people thought going to the moon was pointless and insanely expensive, but the technology to put stuff in space and have GPS and comms satellites probably paid that back 100x

reply

vl

1 hour ago

 |
root
 |
parent
 |
next

[–]

Reality is that we don’t know how much of a trope this statement is.

I think we would get all this technology without going to the moon or Space Shuttle program. GPS, for example, was developed for military applications initially.

reply

DaiPlusPlus

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

I don’t mean to invalidate your point (about genuine value arising from innovations originating from the Apollo program), but GPS and comms satellites (and heck, the Internet) are all products of nuclear weapons programs rather than civilian space exploration programs (ditto the Space Shuttle, and I could go on…).

reply

dortlick

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

Sure, but what about the collective investment in smartphones, digital cameras, laptops, even cars. Not much modern technology is useful and practical after 10 years, let alone 20. AI is probably moving a little faster than normal, but technology depreciation is not limited to AI.

reply

mensetmanusman

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

Utterly? Moores law per power requirement is dead, lower power units can run electric heating for small towns!

reply

torginus

2 hours ago

 |
parent
 |
prev
 |
next

[–]

My personal sneaking suspicion is that publicly offered models are using way less compute than thought. In modern mixture of experts models, you can do top-k sampling, where only some experts are evaluated, meaning even SOTA models aren't using much more compute than a 70-80b non-MoE model.

reply

ActorNightly

3 hours ago

 |
parent
 |
prev
 |
next

[–]

To piggyback on this, at enterprise level in modern age, the question is really not about "how are we going to serve all these users", it comes down to the fact that investors believe that eventually they will see a return on investment, and then pay whatever is needed to get the infra.

Even if you didn't have optimizations involved in terms of job scheduling, they would just build as many warehouses as necessary filled with as many racks as necessary to serve the required user base.

reply

eitally

1 hour ago

 |
parent
 |
prev
 |
next

[–]

What I wonder is what this means for Coreweave, Lambda and the rest, who are essentially just renting out fleets of racks like this. Does it ultimately result in acquisition by a larger player? Severe loss of demand? Can they even sell enough to cover the capex costs?

reply

adw

1 hour ago

 |
root
 |
parent
 |
next

[–]

These are also depreciating assets.

reply

torginus

2 hours ago

 |
parent
 |
prev
 |
next

[–]

I wonder if it's feasible to hook up NAND flash with a high bandwidth link necessary for inference.

Each of these NAND chips hundreds of dies of flash stacked inside, and they are hooked up to the same data line, so just 1 of them can talk at the same time, and they still achieve >1GB/s bandwidth. If you could hook them up in parallel, you could have 100s of GBs of bandwidth per chip.

reply

potatolicious

2 hours ago

 |
root
 |
parent
 |
next

[–]

NAND is very, very slow relative to RAM, so you'd pay a huge performance penalty there. But maybe more importantly my impression is that memory contents mutate pretty heavily during inference (you're not just storing the fixed weights), so I'd be pretty concerned about NAND wear. Mutating a single bit on a NAND chip a million times over just results in a large pile of dead NAND chips.

reply

torginus

2 hours ago

 |
root
 |
parent
 |
next

[–]

No it's not slow - a single NAND chip in SSDs offers >1GB of bandwidth - inside the chip there are 100+ wafers actually holding the data, but in SSDs only one of them is active when reading/writing.

You could probably make special NAND chips where all of them can be active at the same time, which means you could get 100GB+ bandwidth out of a single chip.This would be useless for data storage scenarios, but very useful when you have huge amounts of static data you need to read quickly.

reply

neko_ranger

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Four H100 in a 2U rack didn't sound impressive, but that is accurate:

>A typical 1U or 2U server can accommodate 2-4 H100 PCIe GPUs, depending on the chassis design.>In a 42U rack with 20x 2U servers (allowing space for switches and PDU), you could fit approximately 40-80 H100 PCIe GPUs.

reply

michaelt

3 hours ago

 |
root
 |
parent
 |
next

[–]

Why stop at 80 H100s for a mere 6.4 terabytes of GPU memory?

Supermicro will sell you a full rack loaded with servers [1] providing 13.4 TB of GPU memory.And with 132kW of power output, you can heat an olympic-sized swimming pool by 1°C every day with that rack alone. That's almost as much power consumption as 10 mid-sized cars cruising at 50 mph.[1]https://www.supermicro.com/en/products/system/gpu/48u/srs-gb...

reply

handfuloflight

51 minutes ago

 |
root
 |
parent
 |
next

[–]

What about
https://www.cerebras.ai/system
?

reply

jzymbaluk

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

And the big hyperscaler cloud providers are building city-block sized data centers stuffed to the gills with these racks as far as the eye can see

reply

dboreham

35 minutes ago

 |
parent
 |
prev
 |
next

[–]

They'll be in landfill in 10 years.

reply

scarface_74

2 hours ago

 |
parent
 |
prev
 |
next

[–]

This isn’t like how Google was able to buy up dark fiber cheaply and use it.

From what I understand, this hardware has a high failure rate over the long term especially because of the heat they generate.

reply

piyh

4 hours ago

 |
prev
 |
next

[–]

You have thousands of dollars, they have tens of billions. $1,000 vs $10,000,000,000. They have 7 more zeros than you, which is one less zero than the scale difference in users: 1 user (you) vs 700,000,000 users (openai). They managed to squeak out at least one or two zeros worth of efficiency at scale vs what you're doing.

Also, you CAN run local models that are as good as GPT 4 was on launch on a macbook with 24 gigs of ram.https://artificialanalysis.ai/?models=gpt-oss-20b%2Cgemma-3-...

reply

cornholio

3 hours ago

 |
parent
 |
next

[–]

You can knock off a zero or two just by time shifting the 700 million distinct users across a day/week and account for the mere minutes of compute time they will actually use in each interaction. So they might no see peaks higher than 10 million active inference session at the same time.

Conversely, you can't do the same thing as a self hosted user, you can't really bank your idle compute for a week and consume it all in a single serving, hence the much more expensive local hardware to reach the peak generation rate you need.

reply

0cf8612b2e1e

3 hours ago

 |
root
 |
parent
 |
next

[–]

During times of high utilization, how do they handle more requests than they have hardware? Is the software granular enough that they can round robin the hardware per token generated? UserA token, then UserB, then UserC, back to UserA? Or is it more likely that everyone goes into a big FIFO processing the entire request before switching to the next user?

I assume the former has massive overhead, but maybe it is worthwhile to keep responsiveness up for everyone.

reply

cornholio

2 hours ago

 |
root
 |
parent
 |
next

[–]

Inference is essentially a very complex matrix algorithm run repeatedly on itself, each time the input matrix (context window) is shifted and the new generated tokens appended to the end. So, it's easy to multiplex all active sessions over limited hardware, a typical server can hold hundreds of thousands of active contexts in the main system ram, each less than 500KB and ferry them to the GPU nearly instantaneously as required.

reply

the8472

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

During peaks they can kick out background jobs like model training or API users doing batch jobs.

reply

abathologist

2 hours ago

 |
prev
 |
next

[–]

One clever ingredient in OpenAI's secret sauce is billions of dollars of losses. About $5 billion dollars lost in 2024.
https://www.cnbc.com/2024/09/27/openai-sees-5-billion-loss-t...

reply

93po

30 minutes ago

 |
parent
 |
next

[–]

they would be break-even if all they did was serve existing models and got rid of everything related to R&D

reply

fergal_reid

4 hours ago

 |
prev
 |
next

[–]

I think the most direct answer is that at scale, inference can be batched, so that processing many queries together in a parallel batch is more efficient than interactively dedicating a single GPU per user (like your home setup).

If you want a survey of intermediate level engineering tricks, this post we wrote on the Fin AI blog might be interesting. (There's probably a level of proprietary techniques OpenAI etc have again beyond these):https://fin.ai/research/think-fast-reasoning-at-3ms-a-token/

reply

jp57

2 hours ago

 |
prev
 |
next

[–]

700M weekly users doesn't say much about how much load they have.

I think the thing to remember is that the majority of chatGPT users, even those who use it every day, are idle 99.9% of the time. Even someone who has it actively processing for an hour a day, seven days a week, is idle 96% of the time. On top of that, many are using less-intensive models. The fact that they chose to mention weekly users implies that there is a significant tail of their user distribution who don't even use it once a day.So your question factors into a few of easier-but-still-not-trivial problems:- Making individual hosts that can fit their models in memory and run them at acceptable toks/sec.- Making enough of them to handle the combined demand, as measured in peak aggregate toks/sec.- Multiplexing all the requests onto the hosts efficiently.Of course there are nuances, but honestly, from a high level last problem does not seem so different from running a search engine. All the state is in the chat transcript, so I don't think there any particular reason reason that successive interactions on the same chat need be handled by the same server. They could just be load-balanced to whatever server is free.We don't know, for example, when the chat says "Thinking..." whether the model is running or if it's just queued waiting for a free server.

reply

ritz_labringue

2 hours ago

 |
prev
 |
next

[–]

The short answer is "batch size". These days, LLMs are what we call "Mixture of Experts", meaning they only activate a small subset of their weights at a time.
This makes them a lot more efficient to run at high batch size.

If you try to run GPT4 at home, you'll still need enough VRAM to load the entire model, which means you'll need several H100s (each one costs like $40k). But you will be under-utilizing those cards by a huge amount for personal use.It's a bit like saying "How come Apple can make iphones for billions of people but I can't even build a single one in my garage"

reply

arjvik

24 minutes ago

 |
parent
 |
next

[–]

Essentially, inference is well-amortized across the many users.

reply

robotnikman

2 hours ago

 |
parent
 |
prev
 |
next

[–]

I wonder then if its possible to load the unused parts into main memory, while the more used parts into VRAM

reply

cududa

34 minutes ago

 |
parent
 |
prev
 |
next

[–]

Great metaphor

reply

kazinator

23 minutes ago

 |
prev
 |
next

[–]

One trick is that multiple prompts are combined into a batch that is subject to the token prediction simultaneously.

I've had Google Gemini start talking to be in the context of someone else's chat, unrelated to mine.ME: Does POSIX have any API for creating a filesystem object (such as a file) with a predetermined inode number supplied by the caller?AI: <reformats my question into LaTeX syntax, out of the blue>\documentclass{article}
 \usepackage{amsmath}
 \usepackage{amsfonts}
 \usepackage{amssymb}
 \begin{document}
 \section*{Does POSIX have any API for creating a filesystem object with a predetermined inode number supplied by the caller?}
 \textbf{No, POSIX does not provide a standard API for creating a filesystem object (like a file or directory) with a caller-specified inode number.}

 \subsection*{Inode Allocation in POSIX Filesystems}
 [... SNIP]ME: Why are you spewing LaTeX syntax at me?AI: You are absolutely right! My apologies. That was a mistake on my part. I got carried away with the instruction to use LaTeX for mathematical and scientific notations and incorrectly applied it to the entire response. [... SNIP]There was no such instruction. I've never chatted with any AI about LaTeX. it leaked from the tokens of someone else's chat.

reply

roadside_picnic

4 hours ago

 |
prev
 |
next

[–]

I'm sure there are countless tricks, but one that can implemented at home, and I know plays a major part in Cerebras' performance is: speculative decoding.

Speculative decoding uses a smaller draft model to generate tokens with much less compute and memory required. Then the main model will accept those tokens based on the probabilityitwould have generated them. In practice this case easily result in a 3x speedup in inference.Another trick for structured outputs that I know of is "fast forwarding" where you can skip tokens if you know they are going to be the only acceptable outputs. For example, you know that when generating JSON you need to start with `{ "<first key>": ` etc. This can also lead to a ~3x speedup in when responding in JSON.

reply

tough

4 hours ago

 |
parent
 |
next

[–]

gpt-oss-120b can be used with gpt-oss-20b as speculative drafting on LM Studio

I'm not sure it improved the speed much

reply

roadside_picnic

3 hours ago

 |
root
 |
parent
 |
next

[–]

To measure the performance gains on a local machine (or even standard cloud GPU setup), since you can't run this in parallel with the same efficiency you could in a high-ed data center, you need to compare the number of calls made to each model.

In my experiences I'd seen the calls to the target model reduced to a third of what they would have been without using a draft model.You'll still get some gains on a local model, but they won't be near what they could be theoretically if everything is properly tuned for performance.It also depends on the type of task. I was working with pretty structured data with lots of easy to predict tokens.

reply

vrm

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

a 6:1 parameter ratio is too small for specdec to have that much of an effect. You'd really want to see 10:1 or even more for this to start to matter

reply

wisty

29 minutes ago

 |
prev
 |
next

[–]

They can have a very even load if they use their nodes for training when the customer use is low, so that massively helps. If they have 3x as much hardware as they need to serve peak demand (even with throttling) this will cost a lot, unless they have a another use for lots of GPU.

I probably underestimate overheads here but anyway ...Let's assume a $20k expert node can produce 500 tokens per second (15,000 per year). $5k a year for the machine per year. $5k overheads. 5 experts per token (so $50k to produce 15,000 megatokens with a
100% throughput). Say they charge up to $10 per million tokens ... yeah it's tight but I can see how it's doable.Say they cost $100 per user per year. If it's $10 per million tokens (depends on the model) then they are budgeting 10 million tokens per user. That's like 100 books per year. The answer is that users probably don't use as much as the api would cost.The real question is, how does it cost $10 per megatoken?500 tokens per second per node is like 15,000 megatokens per year. So a 500 token node can bring in $150,000 per node.Call it 5 live experts and a router. That's maybe $20k per expert per year. If it's a kilowatt power supply per expert, and $0.1 per kW power that's $1000 for power. The hardware is good for 4 years so $5k for that. Toss in overheads, and it's maybe $10k costs.So at full capacity they can make $5 off $10 revenue. With uneven loads they make nothing, unless they have some optimisation and very good load balancing (if they can double the tokens per second then they make a decent profit).

reply

ryao

2 hours ago

 |
prev
 |
next

[–]

At the heart of inference is matrix-vector multiplication. If you have many of these operations to do and only the vector part differs (which is the case when you have multiple queries), you can do matrix-matrix multiplication by stuffing the vectors into a matrix. Computing hardware is able to run the equivalent of dozens of matrix-vector multiplication operations in the same time it takes to do 1 matrix-matrix multiplication operation. This is called batching. That is the main trick.

A second trick is to implement something called speculative decoding. Inference has two phases. One is prompt processing and another is token generation. They actually work the same way using what is called a forward pass, except prompt processing can do them in parallel by switching from matrix-vector to matrix-matrix multiplication and dumping the prompt’s tokens into each forward pass in parallel. Each forward pass will create a new token, but it can be discarded unless it is from the last forward pass, as that will be the first new token generated as part of token generation. Now, you put that token into the next forward pass to get the token after it, and so on. It would be nice if all of the forward passes could be done in parallel, but you do not know the future, so you ordinarily cannot. However, if you make a draft model that is a very fast model runs in a fraction of the time and guesses the next token correctly most of the time, then you can sequentially run the forward pass for that instead N times. Now, you can take the N tokens and put it into the prompt processing routine that did N forward passes in parallel. Instead of discarding all tokens except the last one like in prompt processing, we will compare them to the input tokens. All tokens up to and including the first token that differ, that come out of the parallel forward pass are valid tokens for the output of the main model. This is guaranteed to always produce at least 1 valid token since in the worse case the first token does not match, but the output for the first token will be equal to the output of running the forward pass without having done speculative decoding. You can get a 2x to 4x performance increase from this if done right.Now, I do not work on any of this professionally, but I am willing to guess that beyond these techniques, they have groups of machines handling queries of similar length in parallel (since doing a batch where 1 query is much longer than the others is inefficient) and some sort of dynamic load balancing so that machines do not get stuck with a query size that is not actively being utilized.

reply

afr0ck

50 minutes ago

 |
prev
 |
next

[–]

Inference runs like a stateless web server. If you have 50K or 100K machines, each with a tons of GPUs (usually 8 GPUs per node), then you end up with a massive GPU infrastructure that can run hundreds of thousands, if not millions, of inference instances. They use something like Kubernetes on top for scheduling, scaling and spinning up instances as needed.

For storage, they also have massive amount of hard disks and SSD behind planet scale object file systems (like AWS's S3 or Tectonic at Meta or MinIO in prem) all connected by massive amount of switches and routers of varying capacity.So in the end, it's just the good old Cloud, but also with GPUs.Btw, OpenAI's infrastructure is provided and managed by Microsoft Azure.And, yes, all of this requires billions of dollars to build and operate.

reply

simne

3 hours ago

 |
prev
 |
next

[–]

It is not just engineering. There are also huge, very huge, investments into infrastructure.

As already answered, AI companies use extremely expensive setups (servers with professional cards) in large numbers and all these things concentrated in big datcenters with powerful networking and huge power consumption.Imagine - last time, so huge investments (~1.2% of GDP, and unknown if investments will grow or not) was into telecom infrastructure - mostly wired telephones, but also cable TV and later added Internet and cell communications and clouds (in some countries wired phones just don't cover whole country and they jumped directly into wireless communications).Larger investments was into railroads - ~6% of GDP (and I'm also not sure, some people said, AI will surpass them as share of possible for AI tasks constantly grow).So to conclude, just now AI boom looks like main consumer of telecom (Internet) and cloud infrastructure. If you've seen old mainframes in datacenters, and extremely thick core network cables (with hundreds wires or fibers in just one cable), and huge satellite dishes, you could imagine, what I'm talking about.And yes, I'm not sure, will this boom end like dot-coms (Y2K), or such huge usage of resources will sustain. Why it is not obvious, because for telecoms (internet) also was unknown, if people will use phones and other p2p communications for leisure as now, or will leave phones just for work. Even worse, if AI agents become ordinary things, possible scenario, number of AI agents will surpass number of people.

reply

Szpadel

4 hours ago

 |
prev
 |
next

[–]

AFAIK main trick is batching, GPU can do same work on batch of data, you can work on many requests at the same time more efficiently.

batching requests increase latency to first token, so it's tradeoff and MoE makes it more tricky because they are not equally used.there was somewhere great article explaining deepseek efficiency that explained it in great detail (basically latency - throughput tradeoff)

reply

threatripper

2 hours ago

 |
parent
 |
next

[–]

Your model keeps the weights on slow memory and needs to touch all of them to make 1 token for you. By batching you make 64 tokens for 64 users in one go. And they use dozens of GPUs in parallel to make 1024 tokens in the time your system makes 1 token. So even though the big system costs more, it is much more efficient when being used by many users in parallel. Also, by using many fast GPUs in series to process parts of the neural net, it produces output much faster for each user compared to your local system. You can't beat that.

reply

mquander

4 hours ago

 |
prev
 |
next

[–]

I'm pretty much an AI layperson but my basic understanding of how LLMs usually run on my or your box is:

1. You load all the weights of the model into GPU VRAM, plus the context.2. You construct a data structure called the "KV cache" representing the context, and it hopefully stays in the GPU cache.3. For each token in the response, for each layer of the model, you read the weights of that layer out of VRAM and use them plus the KV cache to compute the inputs to the next layer. After all the layers you output a new token and update the KV cache with it.Furthermore, my understanding is that the bottleneck of this process is usually in step 3 where you read the weights of the layer from VRAM.As a result, this process is very parallelizable if you have lots of different people doing independent queries at the same time, because you can have all their contexts in cache at once, and then process them through each layer at the same time, reading the weights from VRAM only once.So once you got the VRAM it's much more efficient for you to serve lots of people's different queries than for you to be one guy doing one query at a time.

reply

nbardy

43 minutes ago

 |
prev
 |
next

[–]

The serving infrastructure becomes very efficient when serving requests in parallel.

Look at VLLM. It's the top open source version of this.But the idea is you can service 5000 or so people in parallel.You get about 1.5-2x slowdown on per token speed per user, but you get 2000x-3000x throughput on the server.The main insight is that memory bandwidth is the main bottleneck so if you batch requests and use a clever KV cache along with the batching you can drastically increase parallel throughput.

reply

rythie

3 hours ago

 |
prev
 |
next

[–]

First off I’d say you can run models locally at good speed, llama3.1:8b runs fine a MacBook Air M2 with 16GB RAM and much better on a Nvidia RTX3050 which are fairly affordable.

For OpenAI, I’d assume that a GPU is dedicated to your task from the point you press enter to the point it finishes writing. I would think most of the 700 million barely use ChatGPT and a small proportion use it a lot and likely would need to pay due to the limits. Most of the time you have the website/app open I’d think you are either reading what it has written, writing something or it’s just open in the background, so ChatGPT isn’t doing anything in that time. If we assume 20 queries a week taking 25 seconds each. That’s 8.33 minutes a week. That would mean a single GPU could serve up to 1209 users, meaning for 700 million users you’d need at least 578,703 GPUs. Sam Altman has said OpenAI is due to have over a million GPUs by the end of year.I’ve found that the inference speed on newer GPUs is barely faster than older ones (perhaps it’s memory speed limited?). They could be using older clusters of V100, A100 or even H100 GPUs for inference if they can get the model to fit or multiple GPUs if it doesn’t fit. A100s were available in 40GB and 80GB versions.I would think they use a queuing system to allocate your message to a GPU. Slurm is widely used in HPC compute clusters, so might use that, though likely they have rolled their own system for inference.

reply

atty

3 hours ago

 |
parent
 |
next

[–]

The idea that a GPU is dedicated to a single inference task is just generally incorrect. Inputs are batched, and it’s not a single GPU handling a single request, it’s a handful of GPUs in various parallelism schemes processing a batch of requests at once. There’s a latency vs throughput trade off that operators make. The larger that batch size the greater the latency, but it improves overall cluster throughput.

reply

storus

43 minutes ago

 |
prev
 |
next

[–]

I'd start by watching these lectures:

https://ut.philkr.net/advances_in_deeplearning/Especially the "Advanced Training" section to get some idea of tricks that are used these days.

reply

valbaca

1 hour ago

 |
prev
 |
next

[–]

How can Google serve 3B users when I can't do one internet search locally? [2001]

reply

mattnewton

2 hours ago

 |
prev
 |
next

[–]

Lots of good answers that mention the big things (money, scale, and expertise). But one thing I haven’t seen mentioned yet is that the transformer math is probably against your use case. Batch compute on beefy hardware is currently more efficient than computing small sequences for a single user at a time, since these models tend to be memory bound and not compute bound. They have the users that makes the beefy hardware make sense, enough people are querying around the same time to make some batching possible.

reply

minimaxir

4 hours ago

 |
prev
 |
next

[–]

> Sure, they have huge GPU clusters

That's a really, really big "sure."Almost every trick to run a LLM at OpenAI's scale is a trade secret and may not be easily understood by mere mortals anyways (e.g. bare-metal CUDA optimizations)

reply

handfuloflight

2 minutes ago

 |
parent
 |
next

[–]

Trade secrets also exist to hide faults and blemishes.

reply

v5v3

4 hours ago

 |
parent
 |
prev
 |
next

[–]

Trade secret?

With all the staff poaching the trade secrets may have now leaked?

reply

minimaxir

1 hour ago

 |
root
 |
parent
 |
next

[–]

That's half the reason tech companies poach.

reply

dan-robertson

2 hours ago

 |
prev
 |
next

[–]

I think it’s some combination of:

- the models are not too big for the cards. Specifically, they know the cards they have and they modify the topology of the model to fit their hardware well- lots of optimisations. Eg the most trivial implementation of transformer-with-attention inference is going to be quadratic in the size of your output but actual implementations are not quadratic. Then there are lots of small things: tracing the specific model running on the specific gpu, optimising kernels, etc- more costs are amortized. Your hardware is relatively expensive because it is mostly sitting idle. AI company hardware gets much more utilization and therefore can be relatively more expensive hardware, where customers are mostly paying for energy.

reply

nmca

3 hours ago

 |
prev
 |
next

[–]

Isn’t the answer to the question just classic economies of scale?

You can’t run GPT4 for yourself because the fixed costs are high. But the variable costs are low, so OAI can serve a shit ton.Or equivalently the smallest available unit of “serving a gpt4” is more gpt4 than one person needs.I think all the inference optimisation answers are plain wrong for the actual question asked?

reply

nmca

3 hours ago

 |
parent
 |
next

[–]

It’s the same principle as:

https://www.tripadvisor.com/Restaurant_Review-g60763-d477541...

reply

kj4ips

2 hours ago

 |
prev
 |
next

[–]

TL;DR: It's massively easier to run a few models really fast than it is to run many different models acceptably.

They probably are using some interesting hardware, but there's a strange economy of scale when serving lots of requests for a small number of models. Regardless of if you are running single GPU, clustered GPU, FPGAs, or ASICs, there is a cost with initializing the model that dwarfs the cost of inferring on it by many orders of magnitude.If you build a workstation with enough accelerator-accessible memory to have "good" performance on a larger model, but only use it with typical user access patterns, that hardware will be sitting idle the vast majority of the time. If you switch between models for different situations, that incurs a load penalty, which might evict other models, which you might have to load in again.However, if you build an inference farm, you likely have only a few models you are working with (possibly with some dynamic weight shifting[1]) and there are already some number of ready instances of each, so that load cost is only incurred when scaling a given model up or down.I've had the pleasure to work with some folks around provisioning an FPGA+ASIC based appliance, and it can produce mind-boggling amounts of tokens/sec, but it takes 30m+ to load a model.[1] there was a neat paper at SC a few years ago about that, but I can't find it now

reply

gundmc

4 hours ago

 |
prev
 |
next

[–]

Well, their huge GPU clusters have "insane VRAM". Once you can actually load the model without offloading, inference isn't all that computationally expensive for the most part.

reply

jl6

3 hours ago

 |
prev
 |
next

[–]

If the explanation really is, as many comments here suggest, that prompts can be run in parallel in batches at low marginal additional cost, then that feels like bad news for the democratization and/or local running of LLMs. If it’s only cost-effective to run a model for ~thousands of people at the same time, it’s never going to be cost-effective to run on your own.

reply

simonw

3 hours ago

 |
parent
 |
next

[–]

Sure, but that's how most of human society works already.

It's more cost effective to farm eggs from a hundred thousand chickens than it is for individuals to have chickens in their yard.You CAN run a GPT-class model on your own machine right now, for several thousand dollars of machine... but you can get massively better results if you spend those thousands of dollars on API credits over the next five years or so.Some people will choose to do that. I have backyard chickens, they're really fun! Most expensive eggs I've ever seen in my life.

reply

hdgvhicv

1 hour ago

 |
root
 |
parent
 |
next

[–]

50 years ago general computers were also time shared. Then the pendulum swing to desktop, then back to central.

I for one look forward to another 10 years of progress - or less - putting current models running on a laptop. I don’t trust any big company with my data

reply

sixo

44 minutes ago

 |
parent
 |
prev
 |
next

[–]

That determines the cost effectiveness to make it worth it to train one of these models in the first place. Using someone else's weights, you can afford to predict quite inefficiently.

reply

ijk

2 hours ago

 |
parent
 |
prev
 |
next

[–]

Well, you can also batch your own queries. Not much use for a chatbot but for an agentic system or offline batch processing it becomes more reasonable.

Consider a system were running a dozen queries at once is only marginally more expensive than running one query. What would you build?

reply

HPsquared

2 hours ago

 |
prev
 |
next

[–]

You also can't run a Google search. Some systems are just large!

reply

davepeck

2 hours ago

 |
prev
 |
next

[–]

Baseten serves models as a service, at scale. There’s quite a lot of interesting engineering both for inference and infrastructure perf. This is a pretty good deep dive into the tricks they employ:
https://www.baseten.co/resources/guide/the-baseten-inference...

reply

highfrequency

3 hours ago

 |
prev
 |
next

[–]

Multi-tenancy likely explains the bulk of it. $10k vs. $10b gives them six orders of magnitude more GPU resources, but they have 9 orders of magnitude more users. The average user is probably only running an active ChatGPT query for a few minutes per day, which covers the remaining 3 orders of magnitude.

reply

ilaksh

4 hours ago

 |
prev
 |
next

[–]

You and your engineering team might be able to figure it out and purchase enough equipment also if you had received billions of dollars. And billions and billions. And more billions and billions and billions. Then additional billions, and more billions and billions and even more billions and billions of dollars. They have had 11 rounds of funding totaling around $60 billion.

reply

aziis98

3 hours ago

 |
prev
 |
next

[–]

I think this article can be interesting:

https://www.seangoedecke.com/inference-batching-and-deepseek...Here is an example of what happens> The only way to do fast inference here is to pipeline those layers by having one GPU handle the first ten layers, another handle the next ten, and so on. Otherwise you just won’t be able to fit all the weights in a single GPU’s memory, so you’ll spend a ton of time swapping weights in and out of memory and it’ll end up being really slow. During inference, each token (typically in a “micro batch” of a few tens of tokens each) passes sequentially through that pipeline of GPUs

reply

ionwake

55 minutes ago

 |
prev
 |
next

[–]

I think they just have a philosophers stone that they plug their ethernet cable into

reply

handfuloflight

13 minutes ago

 |
parent
 |
next

[–]

And to think they'll let me use (some of it) for mere pennies!

reply

guluarte

2 hours ago

 |
prev
 |
next

[–]

Simple answer: they are throwing billions of dollars at infrastructure (GPU) and losing money with every user.

reply

teamonkey

1 hour ago

 |
parent
 |
next

[–]

You’re not losing money if money flows in faster than it flows out

reply

suspended_state

4 hours ago

 |
prev
 |
next

[–]

Look for positron.ai talks about their tech, they discuss their approach to scaling LLM workloads with their dedicated hardware. It may not be what is done by OpenAI or other vendors, but you'll get an idea of the underlying problems.

reply

nestorD

3 hours ago

 |
prev
 |
next

[–]

The first step is to acquire hardware fast enough to run one query quickly (and yes, for some model size you are looking at sharding the model and distributed runs). The next one is to batch request, improving GPU use significantly.

Take a look at vLLM for an open source solution that is pretty close to the state of the art as far as handling many user queries:https://docs.vllm.ai/en/stable/

reply

randomNumber7

2 hours ago

 |
prev
 |
next

[–]

Once you have enough GPUs to have your whole model available in GPU RAM you can do inference pretty fast.

As soon as you have enough users you can let your GPUs burn with a high load constantly, while your home solution would idle most of the time and therefore be way too expensive compared to the value.

reply

fancyfredbot

4 hours ago

 |
prev
 |
next

[–]

Have you looked at what happens to tokens per second when you increase batch size? The cost of serving 128 queries at once is not 128x the cost of serving one query.

reply

zerd

4 hours ago

 |
parent
 |
next

[–]

This. the main trick, outside of just bigger hardware, is smart batching. E.g. if one user asks why the sky is blue, the other asks what to make for dinner, both queries go though the same transformer layers, same model weights so they can be answered concurrently for very little extra GPU time. There's also ways to continuously batch requests together so they don't have to be issued at the same time.

reply

valbaca

2 hours ago

 |
prev
 |
next

[–]

How does a billion dollar company scale in a way that a single person cannot?

reply

legitster

4 hours ago

 |
prev
 |
next

[–]

Complete guess, but my hunch is that it's in the sharding. When they break apart your input into its components, they send it off to hardware that is optimized to solve for that piece. On that hardware they have insane VRAM and it's already cached in a way that optimizes that sort of problem.

reply

vlovich123

1 hour ago

 |
prev
 |
next

[–]

1. They have many machines to split the load over
2. MoE architecture that lets them shard experts across different machines - 1 machine handles generating 1 token of context before the entire thing is shipped off to the next expert for the next token. This reduces bandwidth requirements by 1/N as well as the amount of VRAM needed on any single machine
3. They batch tokens from multiple users to further reduce memory bandwidth (eg they compute the math for some given weights on multiple users). This reduces bandwidth requirements significantly as well.

So basically the main tricks are batching (only relevant when you have > 1 query to process) and MoE sharding.

reply

yard2010

4 hours ago

 |
prev
 |
next

[–]

The marginal value of money is low. So it's not linear. They can buy orders of magnitude more GPUs than you can buy.

reply

7speter

48 minutes ago

 |
prev
 |
next

[–]

Elsewhere in the thread, someone talked about how h100’s each have 80GB of vram and cost 20000 dollars.

The largest chatgpt models are maybe 1-1.5tb in size and all of that needs to load into pooled vram. That sounds daunting, but a company like open ai has countless machines that have enough of these datacenter grade gpus with gobs of vram pooled together to run their big models.Inference is also pretty cheap, especially when a model can comfortably fit in a pool of vram. Its not that the pool of gpus spool up each time someone sends a request, but whats more likely is that there’s a queue to f requests from someone like chatgpts 700 million users, and the multiple (I have no idea how many) pools of vram keep the models in their memory to chew through that nearly perpetual queue of requests.

reply

an0malous

2 hours ago

 |
prev
 |
next

[–]

They have more than 700mX your computing budget?

reply

whimsicalism

2 hours ago

 |
prev
 |
next

[–]

batching & spread of users over time will get you there already

reply

worik

1 hour ago

 |
prev
 |
next

[–]

I do not have a technical answer, but I have the feeling that the concept of "loss leaders" is useful

IMO outfits like OpenAI are burning metric shit tonnes of cash serving these models. It pails in comparison to the mega shit tonnes of cash used to train the models.They hope to gain market share before they start charging customers what it costs.

reply

boombapoom

55 minutes ago

 |
prev
 |
next

[–]

redis

reply

GaggiX

4 hours ago

 |
prev
 |
next

[–]

Huge batches to find the perfect balance between compute and memory banthwidth, quantized models, speculative decoding or similar techniques, MoE models, routing of requests on smaller models if required, batch processing to fill the GPUs when demand is lower (or electricity is cheaper).

reply

lihaciudaniel

2 hours ago

 |
prev
 |
next

[–]

Azure servers

reply

tekno45

2 hours ago

 |
prev
 |
next

[–]

Money. Don't let them lie to you. just look at nvidia.

They are throwing money at this problem hoping you throw more money back.

reply

moralestapia

4 hours ago

 |
prev
 |
next

[–]

Because they spend billions per year on that.

reply

kirito1337

3 hours ago

 |
prev
 |
next

[–]

Data centers, and use of client hardware, those 700M clients' hardware are being partially used as clusters.

reply

anon291

1 hour ago

 |
prev
 |
next

[–]

At the end of the day, the answer is... specialized hardware. No matter what you do on your local system, you don't have the interconnects necessary. Yes, they have special software, but the software would not work locally. NVIDIA sells entire solutions and specialized interconnects for this purpose. They are well out of the reach of the standard consumer.

But software wise, they shard, load balance, and batch. ChatGPT gets 1000s (or something like that) of requests every second. Those are batched and submitted to one GPU. Generating text for 1000 answers is often the same speed as generating for just 1 due to how memory works on these systems.

reply

vFunct

4 hours ago

 |
prev
 |
next

[–]

They also don’t need one system per user. Think of how often you use their system over the week, maybe one hour total? You can shove 100+ people into sharing one system at that rate… so already you’re down to only needing 7 million systems.

reply

maurycyz

3 hours ago

 |
prev
 |
next

[–]

By setting billions of VC money on fire:
https://en.wikipedia.org/wiki/OpenAI

No, really. They just have entire datacenters filled with high end GPUs.

reply

SpaceManNabs

4 hours ago

 |
prev
 |
next

[–]

not affiliated with them and i might be a little out of date but here are my guesses

1. prompt caching2. some RAG to save resources3. of course lots model optimizations and CUDA optimizations4. lots of throttling5. offloading parts of the answer that are better served by other approaches (if asked to add numbers, do a system call to a calculator instead of using LLM)6. a lot of shardingOne thing you should ask is: What does it mean to handle a request with chatgpt? It might not be what you think it is.source: random workshops over the past year.

reply

bigyabai

4 hours ago

 |
prev
 |
next

[–]

https://en.wikipedia.org/wiki/Autoscaling

reply

midzer

4 hours ago

 |
prev
 |
next

[–]

Finally, some1 with the important questions!

Hint: it's a money thing.

reply

roman_soldier

3 hours ago

 |
prev
 |
next

[–]

They rewrote it in Rust/Zig the one you have is written in Ruby. :-p

reply

cloudking

4 hours ago

 |
prev
 |
next

[–]

They are hosted on Microsoft Azure cloud infrastructure and Microsoft owns 49%

They are also partnering with rivals like Google for additional capacityhttps://www.reuters.com/business/retail-consumer/openai-taps...

reply

lihaciudaniel

2 hours ago

 |
parent
 |
next

[–]

In fact logout gpt I found it hosted on azure

reply

captainmuon

4 hours ago

 |
prev

[–]

I work at a university data center, although not on LLMs. We host state of the art models for a large number of users. As far as I understand, there is no secret sauce. We just have a big GPU cluster with a batch system, where we spin up jobs to run certain models. The tricky part for us is to have the various models available on demand with no waiting time.

But I also have to say 700M weekly users could mean 100M daily or 70k a minute (low ball estimate with no returning users...) is a lot, but achievable at startup scale. I don't have out current numbers but we are several orders of magnitude smaller of course :-)The big difference to home use is the amount of VRAM. Large VRAM GPUs such as H100 are gated being support contracts and cost 20k. Theoretically you could buy a Mac Pro with a ton of RAM as an individual if you wanted to run auch models yourself.

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
