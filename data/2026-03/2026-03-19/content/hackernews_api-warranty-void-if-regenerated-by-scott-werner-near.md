---
title: Warranty Void If Regenerated - by Scott Werner - Near Zero
url: https://nearzero.software/p/warranty-void-if-regenerated
site_name: hackernews_api
content_file: hackernews_api-warranty-void-if-regenerated-by-scott-werner-near
fetched_at: '2026-03-19T11:17:39.745155'
original_url: https://nearzero.software/p/warranty-void-if-regenerated
author: Scott Werner
date: '2026-03-18'
description: Tom Hartmann had not planned to become a Software Mechanic.
tags:
- hackernews
- trending
---

# Warranty Void If Regenerated

Scott Werner
Mar 17, 2026
40
5
5
Share

Tom Hartmann had not planned to become a Software Mechanic. But then, nobody who was a Software Mechanic had planned to become one, because the job hadn’t existed seven years ago, and the people doing it had all been something else first.

This was true of most professions in the post-transition economy, and it had been true of most professions after containerization, and after electrification, and after the printing press, and probably after the invention of bronze. The first blacksmiths had not grown up dreaming of blacksmithery. They had been people who were good at hitting things with other things and who noticed, at some point, that metal responded interestingly to being hit. The first Software Mechanics were people who were good at diagnosing the gap between what technology was supposed to do and what it actually did. A skill that, before the transition, had been called “IT support” and had been compensated accordingly, which is to say: badly.

Tom had been an agricultural equipment technician, which meant he’d fixed tractors, combines, GPS guidance systems, and the increasingly complex control software that made modern farming possible. He’d worked for a John Deere dealership in Marshfield for eleven years. Then the transition happened, and the dealership’s software repair business evaporated; the machines still needed repair, but the software on the machines stopped being something you repaired. You regenerated it. You typed what you wanted, it appeared, and if it broke, you typed it again, which is to say: the concept of “broken software” had been replaced by the concept of “an inadequate specification,” which was the same problem wearing a different hat but which required an entirely different person to fix it.

The hardware still needed fixing. Engines, hydraulics, electrical systems, and so on. These remained stubbornly physical. But the software layer, which had been an increasingly large portion of Tom’s work, had been replaced by a churn of generated tools that his clients produced themselves, configured themselves, and broke in ways that were entirely new.

So Tom had adapted. He’d taken the certification course (eight weeks online, practical exam at a regional testing center) and hung a new shingle. HARTMANN SOFTWARE MECHANICS, it read, below the original sign that still said HARTMANN EQUIPMENT REPAIR, because he still fixed the physical stuff too, and because in a farming community nobody cared about the distinction between software and hardware.

This was, in miniature, the death of a distinction that had organized the entire technology industry for fifty years. “Hardware” and “software” had been separate disciplines, separate companies, separate career paths, separate worldviews. Hardware people understood atoms. Software people understood bits. The transition had collapsed the distinction, because when software was generated from plain-language specifications, the relevant expertise was no longer “software”, it was whatever domain the software was for. A Software Mechanic in a farming community needed to understand farming. A Software Mechanic in a medical practice needed to understand medicine. The tool had changed. The domain had not. People who understood the domain and could also diagnose specification problems were the most valuable people in any industry, and most of them, like Tom, had arrived at the job sideways from something else.

His shop was in a corrugated steel building on Highway 29, between a feed store and a Laundromat. It had a waiting area with four plastic chairs and a coffee machine that Tom had specified himself and which made coffee that was, by consensus of his clients, exactly adequate and no better. He’d tried to improve the spec three times. Each time, the regenerated firmware made the coffee subtly worse in a different way. He’d eventually concluded that coffee machine specs existed at the exact intersection of fluid dynamics, thermal management, and taste (three domains where natural language was particularly poor at capturing the relevant distinctions) and had stopped trying. He had, however, found a use for it: when new clients came in insisting that the software they’d generated was “basically fine” and “just needs a little tweak,” he would gesture at the coffee machine and say, “I’ve been trying to get that thing to make decent coffee for two years. You think your sixty-parameter irrigation optimizer is going to be simpler?” This was usually effective. People understood coffee.

It was a typical day in October, and the morning’s appointments were typical.

The first client was Margaret Brennan, who farmed 340 acres of cabbage and sweet corn in the county and who had, six months ago, generated a custom harvest-timing tool that integrated soil moisture data, weather forecasts, market prices, and satellite imagery to recommend optimal harvest windows.

The tool had worked beautifully through the summer. It had saved her, by her estimate, about $40,000 in better timing decisions. Then, last week, it had recommended harvesting a 60-acre cabbage field four days before the heads were ready, and the resulting early harvest had cost her roughly $25,000 in undersized product.

Margaret was not happy.

“It just said harvest,” she told Tom. She was sitting in one of the plastic chairs, holding a cup of the adequate coffee. “Same as always. Green light, harvest window open, confidence 94%. So we harvested. And the heads were this big.” She held her thumb and forefinger about three inches apart. “Two more days and they’d have been perfect. Four days and they’d have been good. But it saidnow.”

Tom pulled up the tool’s specification on his diagnostic display. This was always the first step: read the spec, not the code. The code was generated, opaque, and (critically) not the artifact that the client had actually written. The spec was what the client had intended. The code was what the machine had interpreted. The gap between them was where the problem lived.

Margaret’s spec was better than average, which was not saying much. It was about 1,200 words long. It described the data sources (soil sensors, weather API, market feed, satellite), the decision logic (”recommend harvest when expected quality-adjusted revenue is maximized across a 14-day forward window”), and the output format (green/yellow/red with a confidence percentage).

The average specification written by a non-technical person was, in Tom’s experience, about as precise as the average recipe written by someone who had never cooked for anyone other than themselves. It contained all the right ingredients in approximately the right proportions but omitted crucial details that the writer took for granted because they were obvious to them and invisible to anyone else. “Season to taste” is a perfectly useful instruction for someone who knows what the dish is supposed to taste like. For a machine that has no taste buds, it is meaningless. Specifications written by farmers tended to be heavy on domain knowledge (”maximize quality-adjusted revenue”) and light on the kind of procedural specificity that prevented the machine from doing something unexpected with that knowledge. This wasn’t stupidity. It was the natural result of asking domain experts to communicate with machines through a medium (natural language) that was never designed for the purpose.

The problem, Tom suspected, was in the phrase “quality-adjusted revenue.” He asked Margaret what she meant by it.

“You know, the price per pound times the yield, adjusted for quality. Grade A cabbage gets a premium. Undersized gets a discount. I want to harvest when the total revenue is highest.”

“And how does the tool know what counts as Grade A?”

Margaret paused. “I mean... it knows. It has the data. The satellite imagery shows the head size.”

“It shows canopy coverage,” Tom said. “Not head size. Not directly. It infers head size from canopy coverage, weather data, and growing-degree-day models. And those models were retrained last month when the weather service updated their historical data set.”

He showed her. The model update (a routine recalibration by the weather data provider) had shifted the growing-degree-day calculations by a small amount, roughly 3% in this temperature range. This had caused the tool’s head-size inference to overestimate maturity by about two days. The tool thought the cabbage was ready. The cabbage disagreed.

“But I didn’t change anything,” Margaret said.

“You didn’t. The weather service didn’t change anything that affectedthem. They updated their historical records, which made their models more accurate for weather prediction, which is what they’re for. But your tool was using those models for something they weren’t designed for, crop maturity estimation, and the update that made weather prediction better made your harvest timing worse.”

Margaret stared at him. “So my cabbage got worse because the weather got more accurate?”

“Your cabbage got worse because your specification doesn’t account for upstream model changes. It says ‘use weather data.’ It doesn’t say ‘alert me when the underlying weather models are recalibrated, because my crop maturity inferences are sensitive to the specific calibration.’ That’s a detail the AI has no way of knowing matters unless you tell it.”

This was Tom’s most common diagnosis. Roughly 60% of the cases he saw were some variation of “an external data source changed in a way the specification didn’t anticipate.” The tool worked perfectly until the world shifted underneath it. The spec described a static relationship between inputs and outputs, but the inputs were alive (feeds from other systems that were themselves being updated, recalibrated, and regenerated constantly). Tom had started calling this “the ground moved” problem, because it was like building a house on a foundation that periodically shifted a few inches to the left. The house was fine. The foundation was fine. The relationship between them was what broke. A tractor did not spontaneously change its engine calibration because John Deere updated a database somewhere; physical tools degraded predictably, through wear and corrosion and fatigue, and you could see the degradation coming. Software tools degraded through upstream changes, model drift, and specification ambiguities that only became apparent when a rare condition was met, and you couldn’t see any of it coming until it had already cost you $25,000 in undersized cabbage.

Margaret looked at the spec on his display, then at the cabbage loss figures on her tablet, then at the adequate coffee in her hand.

“Can you fix it?”

“I can make it more resilient. We add a monitoring clause to the spec. Any time an upstream data source version changes, the tool flags it and suspends recommendations until you or I verify that the new version doesn’t affect your inferences. It’ll mean more maintenance. You’ll get maybe two or three flags a month. But you won’t get another surprise harvest.”

“How much?”

“For the spec revision, an hour of my time. For the ongoing monitoring... that’s really a pit crew conversation, Margaret. You’ve got enough tools now that you need someone checking them regularly, not just when they break.”

Margaret made a face. The pit crew conversation. Tom had it with clients about twice a week. The transition from “fix it when it breaks” to “have someone watching it all the time” was a hard sell for farmers, who were accustomed to buying a tool, using it until it wore out, and buying another one. The idea that software needed continuous tending because the world around it moved was counterintuitive to people whose other tools stayed reliably what they were.

“I’ll think about the pit crew thing,” Margaret said, which Tom had learned was farmer for “no.”

He revised the spec, regenerated the tool, ran it against Margaret’s historical data to verify it would have flagged the weather service update, and sent her on her way. Forty-five minutes, door to door. He billed her $180, which was less than 1% of what the failure had cost her, and which she would pay without complaint while continuing to resist the $400-a-month pit crew service that would have caught the problem before it happened.

This was the mechanic’s paradox: the cheaper you were relative to the cost of failure, the more your clients needed you; and the more they needed you, the more they resisted the implication that they’d need you again.

The same paradox existed in human medicine. People who would spend $50,000 on elective surgery without blinking would balk at a $200 annual wellness check. The fix was always cheaper than the failure, the prevention was always cheaper than the fix, and somehow the money always flowed toward the crisis rather than away from it. Tom had concluded that this was not a problem of economics but of psychology: paying for maintenance meant admitting vulnerability, while paying for repair meant responding to an emergency, and humans found emergencies much more motivating than vulnerabilities. This was probably an evolutionary adaptation. A gazelle that responded to the lion in front of it survived. A gazelle that worried about the lion that might show up next Tuesday got distracted and was eaten by the lion in front of it. Unfortunately, software maintenance was a next-Tuesday problem in a world that was very good at producing lions.

The second client was more complicated.

Ethan Novak was twenty-six, a third-generation dairy farmer, and the most prolific generator of custom software in the county, which was saying something in a region where even the most change-resistant operations had adopted at least a handful of generated tools. Tom had been tracking this informally; Ethan had generated at least forty tools in the past year, covering everything from feed optimization to herd health monitoring to milk pricing to manure management to a weather-adjusted grazing rotation system that was, Tom had to admit, genuinely clever.

The problem was that Ethan’s tools talked to each other. Or rather, they were supposed to talk to each other, and mostly did, but the connections between them were specified ad hoc, tool by tool, with no overall architecture and no one managing the interactions. Ethan’s operation was, from a systems perspective, a plate of spaghetti (which was, incidentally, the technical term; the profession had borrowed it from an earlier era of programming and nobody had bothered to find a more dignified metaphor, possibly because none existed). Dozens of independently generated tools sharing data through a tangle of integrations that nobody had designed and nobody fully understood.

Ethan had come in because his milk pricing tool had started outputting prices that were about 8% below market, and his contracts were auto-negotiating based on those prices, and by the time he’d noticed, he’d locked in three months of underpriced milk.

Tom looked at the pricing tool. The spec was fine. The market data feed was fine. The pricing logic was fine.

“When did this start?” he asked.

“About ten days ago, maybe? I don’t check it every day. It was always right before.”

Ten days ago. Tom checked the change logs on Ethan’s other tools. Ten days ago, Ethan had regenerated his feed optimization tool after tweaking the spec to account for a new silage blend. The regenerated feed tool had changed the format of its output data — a minor structural change, the kind that happens when code is regenerated from a revised spec, because the generator optimizes the entire output structure, not just the changed parts.

The milk pricing tool consumed the feed tool’s output as one of its cost inputs. The format change hadn’t broken the connection — the data still flowed — but it had caused the pricing tool to misparse one field, reading a per-head cost as a per-hundredweight cost, which made the feed expenses look much higher than they were, which made the margin calculations come out lower, which made the recommended prices drop.

“You changed your feed tool,” Tom said.

“Yeah, I updated the silage ratios. What does that have to do with milk prices?”

“Everything.”

He showed Ethan the chain: feed tool regenerated → output format shifted → pricing tool misparsed → margins calculated wrong → prices dropped → contracts auto-negotiated at below-market rates. Five links, each one individually innocuous, collectively costing Ethan roughly $14,000.

Ethan looked ill.

“This is the spaghetti problem,” Tom said, not unkindly. “You’ve got forty tools. They share data. When you regenerate one, you can’t predict what happens downstream, because the connections aren’t specified... they’re just... there. They grew organically. Nobody designed the system. You designed forty individual tools and they grew into a system on their own.”

“So what do I do?”

Tom had two answers to this question, and he gave both.

The short-term answer was a spec revision on the pricing tool that pinned the expected input format, so that if an upstream tool changed its output structure, the pricing tool would throw an error instead of silently misparsing. This was a band-aid. It would preventthisfailure from recurring but would do nothing about the thirty-nine other tools and the hundreds of connections between them.

The long-term answer was the one Ethan didn’t want to hear.

“You need a choreographer,” Tom said.

Ethan’s face did the thing that faces did when Tom told young farmers they needed a choreographer. It was a complex expression that combined the resentment of being told you can’t handle your own systems with the dawning realization that you actually can’t handle your own systems, seasoned with the very practical concern of what a choreographer cost.

“A Software Choreographer would map your entire tool ecosystem, specify the interfaces between them, build a conformance layer so that when any tool regenerates, the interfaces are verified before the new version goes live. It’s the difference between forty tools and a system.”

“How much does that cost?”

Tom told him. Ethan’s face did another thing.

The economics of software choreography were counterintuitive to people who had internalized the premise that software was free. The tools were free (or nearly so). Generating a new tool cost essentially nothing. But managing the relationships between tools (the integration layer, the data contracts, the behavioral expectations) was expensive, because it required a human who understood the entire system and could anticipate how a change in one part would propagate through the rest. This was, Tom reflected, the containerization parallel in miniature. Shipping containers were cheap. Organizing container logistics (the ports, the cranes, the rail connections, the tracking systems, the customs protocols) was where all the value and all the jobs were. The container was the easy part. The system was the hard part. Ethan had built forty containers. He hadn’t built a port.

“I can give you a name,” Tom said. “Megan Callahan. She does choreography for about a dozen operations in the area. She’s good. She’ll be honest about what you need and what you don’t.”

Ethan took the name. He paid for the band-aid fix. He left looking like a man who had just learned that the free thing was going to cost him quite a lot of money, which was, Tom thought, one of the defining experiences of the post-transition economy. Through the shop window, Tom watched him sit in his truck for a long moment before starting the engine, the choreographer’s number glowing on his phone screen.

Lunch was a sandwich from the deli on Main Street, eaten at his workbench while he reviewed the afternoon’s queue. Two routine checkups (clients on his quarterly inspection plan, which was as close to a pit crew arrangement as most of his older clients would tolerate), one new client consultation, and a house call.

The house call was for Carol Lindgren, who was seventy-one and ran a small organic operation (45 acres of mixed vegetables, a farm stand on County Road K, and a fierce opposition to any technology more complex than a drip irrigation timer, which she considered the last acceptable innovation in agriculture). She had called this morning and said, with the particular tone of someone delivering information they found personally distressing, that her grandson had “put some software on the irrigation.”

Tom ate his sandwich and thought about Carol Lindgren’s irrigation.

He knew her operation well. It was simple by modern standards: soil moisture sensors wired to a control system that opened and closed drip valves on a schedule. The schedule was manual. Carol set it herself, based on forty years of experience, the weather forecast, and what she described as “looking at the dirt.” Her yields were good. Not optimized, but good. She didn’t want optimized. She wanted to grow vegetables the way she understood how to grow them, with tools she could see and touch and turn off with a physical switch.

Her grandson, Tom guessed, had generated an optimization layer. This happened constantly — a younger family member, with good intentions and an AI tool, would generate a system that automated some part of an older relative’s workflow, and the older relative would call Tom to either verify it or remove it, depending on their temperament.

Carol’s temperament was clear: she wanted it gone. But Tom had learned that “take it off” was rarely the whole story. Usually, underneath the resistance, there was a real question:Is what my grandson built actually better? And if it is, what does that mean about the way I’ve been doing things for forty years?

This was the emotional core of Tom’s job, and it was the part that no certification course taught. A Software Mechanic in a farming community needed to understand pride, tradition, generational tension, and the particular kind of grief that comes from discovering that a machine can do something you spent decades learning to do, and can do it a little better. The question was always the same, whether the client was a seventy-one-year-old vegetable farmer or a cardiologist or a teacher: Am I still the one doing this? Tom had learned that the honest response was not “you’re still the expert” (patronizing) or “the machine is better, adapt” (brutal) but something more like: the machine handles one dimension very well, and you handle all the others, and the work is the combination.

The afternoon checkups were uneventful, which was the ideal state for a checkup and which Tom appreciated more than his clients probably realized. One client’s soil analysis tool had a minor calibration drift; the sensor data was being processed by a module that had been regenerated three weeks ago, and the new version handled decimal precision differently, rounding soil pH to one decimal place instead of two. The difference between pH 6.3 and pH 6.34 was, for most purposes, irrelevant. For this client’s blueberries, which were exquisitely sensitive to soil acidity, it mattered. Tom adjusted the spec to require two-decimal precision and regenerated. Five minutes.

The other checkup was clean. Tom noted this with the quiet satisfaction of a mechanic whose client’s engine is running well. The absence of a problem was, in its way, the best outcome.

Then he drove to Carol Lindgren’s farm.

The farm was beautiful in the way that well-tended small farms are beautiful. Rows of late-season kale and chard. A greenhouse with winter starts. The farm stand, closed for the day, with a hand-painted sign that said LINDGREN FARMS and below it, in smaller letters, SINCE 1987.

Carol met him at the irrigation control shed, which was a ten-by-ten wooden structure that housed the valve manifold, the pump controls, and (now) a small gray box that Tom recognized as a standard home automation hub, repurposed.

“Tyler put that in last weekend,” Carol said, pointing at the box with the expression people reserve for wasps’ nests and unexpected tax bills. “He said it would save me water.”

“Does it?”

“I don’t know. That’s why you’re here.”

Tom examined the setup. Tyler (the grandson) had done a reasonable job, physically. The hub was connected to Carol’s existing soil moisture sensors and to the valve controllers. The specification was on the hub’s management interface, and Tom read it.

It was short. About 400 words. Tyler had specified a system that read the soil moisture sensors, checked the weather forecast, and adjusted the irrigation schedule to deliver water only when the soil moisture dropped below a target threshold, accounting for expected rainfall. The target threshold was set at 60% field capacity, which was a standard recommendation for mixed vegetables.

The generated system was working. The valves were opening and closing on a schedule that differed from Carol’s manual schedule resulting in less water overall by being more precisely timed. The soil moisture data showed that the system was maintaining the target level more consistently than Carol’s manual approach.

It was, objectively, better.

Tom looked at the rows of kale. They looked the same as they always looked. Healthy. Green. Carol’s.

“Well?” Carol said.

Here was the thing about being a mechanic in a community. The technical answer was clear: Tyler’s system was using about 15% less water while maintaining more consistent soil moisture, which would likely improve yields slightly and reduce water costs. The system was well-specified for what it was, had no safety issues, and was doing exactly what Tyler intended.

But Tom was not in the business of delivering technical answers to human questions. Carol was not asking whether the system worked. She was asking whether she was still the farmer.

“The system is using about 15% less water and keeping the moisture more consistent,” Tom said. “For what it does, maintaining a target soil moisture level, it’s doing a good job.”

“But?”

Tom liked Carol. He respected people who heard the “but” before he said it.

“But it’s maintaining a single number. Sixty percent field capacity, everywhere, all the time. Your manual schedule isn’t doing that. Your manual schedule is... messier. You give the kale more water than the chard. You give the south rows less than the north. You adjust for things that aren’t in the sensor data... how the plants look, what you grew there last year, that spot near the greenhouse that drains weird.”

Carol nodded. “The spot near the greenhouse has clay underneath. Water pools.”

“Right. Tyler’s spec doesn’t know that. His spec says ‘maintain 60% field capacity based on sensor readings.’ The sensor in that spot reads low because the clay holds water below the sensor depth. So the system over-irrigates it.”

“I’ve been under-watering that spot on purpose for thirty years.”

“I know. Your manual schedule encodes thirty years of knowledge about this specific piece of land. Tyler’s spec encodes a general principle about vegetable irrigation. The general principle is correct. Your specific knowledge is also correct. They’re in conflict in about four places.”

This was, Tom had come to understand, the core tension of the entire post-transition economy expressed in forty-five acres of vegetables. The AI systems were very good at general principles. They could optimize for a target, account for measurable variables, and respond to data faster than any human. What they couldn’t do was encode the kind of knowledge that accumulates over decades of physical presence in a specific place — the clay underneath the greenhouse, the deer path that compacted the soil in the northeast corner, the way the prevailing west wind dried the far rows faster than the ones sheltered by the tree line. This knowledge was in Carol’s head, not in any database, and it was precisely the kind of knowledge that natural-language specifications were worst at capturing, because it was embodied, contextual, and often inarticulable. Carol didn’t know that she under-watered the clay spot. She just did it. Her hands knew. The AI’s spec couldn’t capture what Carol’s hands knew, because Carol couldn’t put it into words, and words were the only thing the AI understood.

“So what do I do?” Carol asked.

Tom gave her three options, which was his standard approach for situations where the technical answer and the human answer diverged.

The first was simple: take the system out entirely. Go back to manual. Carol’s way worked. It had worked for decades. There was no shame in it. The second was more involved: keep the system but add Carol’s knowledge. Tom would sit with her and translate her specific knowledge into specification language (the clay spot, the drainage pattern, the crop-specific preferences, all of it), and the system would become a hybrid of Tyler’s optimization logic and Carol’s thirty years of site-specific knowledge. This was the best technical outcome but would take several hours and would need updating whenever Carol learned something new about her land, which was more often than people realized, because land kept teaching you things if you paid attention. The third option was the one Tom suspected she’d choose: use the system as a baseline and let Carol override it. The system would run Tyler’s optimization, but Carol would have a physical override switch (a real switch, mounted on the wall, that she could flip to take manual control whenever she wanted). The system would log when she overrode it and why, and over time, those overrides would become data that could be fed back into the spec, gradually incorporating her knowledge.

Carol chose the third option without hesitation. Tom had expected this. It let her keep her authority. The machine could suggest. She would decide. And the physical switch (the real, tangible, flip-it-with-your-hand switch) mattered more than any software interface could.

Tom had learned early in his career to always offer a physical control. A button. A switch. A lever. Something the client could touch. This was not a technical necessity — any override could be implemented in software. It was a psychological necessity. People who felt that a machine was making decisions for them resisted. People who felt that a machine was making suggestions that they could physically override accepted. The difference was a $4 toggle switch from the hardware store. Tom kept a box of them in his truck. He thought of them as the most important tool in his kit, because they solved the problem that no specification could: the human need to feel in control of your own land, your own work, your own life. The machines could optimize. The switch said: but I choose.

He installed the switch. He set up the logging. He showed Carol how to read the override log on her tablet, ”you can also just ignore it, and I’ll check it when I come for inspections”. He gave Tyler’s system a clean bill of health with a note about the four spots where Carol’s knowledge and the system’s logic conflicted. And he left Carol standing in her irrigation shed, one hand on the new switch and the other holding a cup of tea, looking out at her rows of kale with the expression of a woman who had been told that the machines were better and had decided, calmly and without drama, that better was not the only thing that mattered.

Tom drove back to the shop as the sun was going down over the fields. The land on either side of Highway 29 was a patchwork of operations. Some small and manual like Carol’s, some large and heavily automated, most somewhere in between. All of them, by now, running some amount of generated software. All of them, at some point, going to need a mechanic.

He had six appointments tomorrow. A cranberry grower whose pest detection tool was flagging false positives. A cattle rancher whose automated feeding system had started delivering 10% more grain than specified, for reasons that would turn out to be either a specification ambiguity or an upstream data change or, occasionally, an actual bug in the generated code that nobody could fix because nobody had written it. An organic certification collective that needed their documentation system verified for compliance. Three others he hadn’t looked at yet.

The work was steady. It would stay steady, because the tools were getting better but the specifications were not keeping pace, and the world underneath the specifications was not getting simpler. Every season brought new cultivars, new regulations, new weather patterns, new market dynamics, new data sources, new models, new integrations, new ways for the gap between intent and execution to manifest as a flooded field or an underpriced contract or an over-irrigated clay spot.

He pulled into the shop lot and parked. The sign on the building — HARTMANN SOFTWARE MECHANICS, below HARTMANN EQUIPMENT REPAIR — was lit by the security light above the door. Both signs were accurate. He fixed things. Some of the things had engines. Some of the things had specifications. All of them belonged to people who were trying to grow food in a complicated world, and all of them, sooner or later, needed someone who could see where the ground had moved.

Tom Hartmann is a certified Software Mechanic (SM-II, Agricultural Systems) operating out of Marshfield, Wisconsin. He sees an average of 6-8 clients per day. His diagnostic success rate is 94%, which is above the national average for agricultural SM practitioners. He still also fixes tractors.

Margaret Brennan’s cabbage field recovered. The next harvest was full-sized. She has not yet signed up for pit crew services, but she has started checking her tool change logs twice a week, which Tom considers progress.

Ethan Novak hired Megan Callahan to choreograph his tool ecosystem. The project took three weeks and cost him more than his truck. He has not had an integration failure since, which he attributes to Megan’s work. Megan attributes it to the fact that she also quietly deleted eleven of Ethan’s forty tools on the grounds that they were redundant, contradictory, or — in the case of a manure-analysis tool that had been generating confidently meaningless reports for four months — “not even wrong.”

Carol Lindgren uses the override switch an average of three times per week. The irrigation system is performing well. She has not told Tyler about the clay spot, because she is waiting for him to notice it himself, which she considers an important part of his education.

The coffee machine at Hartmann Software Mechanics continues to produce adequate coffee.

40
5
5
Share