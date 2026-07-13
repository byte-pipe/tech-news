---
title: 'Fable 5 Vs Opus 4.8: Outcomes-Based Assessments Are A Massive Warning For Frontier AI Labs'
url: https://vinvashishta.substack.com/p/fable-5-vs-opus-48-outcomes-based
site_name: tldr
content_file: tldr-fable-5-vs-opus-48-outcomes-based-assessments-are
fetched_at: '2026-07-13T12:27:05.673225'
original_url: https://vinvashishta.substack.com/p/fable-5-vs-opus-48-outcomes-based
author: Vin Vashishta
date: '2026-07-13'
description: Dear AI labs, no one believes your benchmarks anymore.
tags:
- tldr
---

# Fable 5 Vs Opus 4.8: Outcomes-Based Assessments Are A Massive Warning For Frontier AI Labs

Vin Vashishta
Jul 09, 2026
16
1
1
Share

Dear AI labs, no one believes your benchmarks anymore. In the last month, DoorDash and Snowflake have both created their own benchmarks based on their real-world internal and customer-facing workflows. I do the same with clients, and this article leads with an example of a real-world benchmark using my business’s websites.

Fable 5 is supposed to be transcendent at coding tasks, so we gave it one. We gave Fable 5 and Opus 4.8 a template, my previous website, and an outcomes-based objective: rebuild the website to improve conversions. Outcomes-based metrics are essential for any agentic workflow, or the artifact that gets generated is measured on vibes.

## Spoiler Alert: Both Models Failed Miserably

Most companies are still measuring AI on artifact metrics, and that’s creating a false perception of their capabilities. Look at the technical artifacts Fable 5 (highroiai.com) and Opus 4.8 (datascience.vin) created, and they both seem incredibly capable. However, measure those artifacts based on the outcome of improving conversion rates over my website’s benchmark, and they both score a 0.

Both websites are functional technical artifacts, but nonfunctional business artifacts. What you’re seeing on both is the product of multiple iterations of building and improvement with some manual fixes thrown in. And neither achieves the level of functionality that the old website had.

Both sites fail for multiple reasons, but the biggest one makes it clear how large the gap between frontier model capabilities and enterprise requirements really is. Neither website was built to track any metrics that measure conversion rates. The old site did rigorous tracking to build the benchmarks we have, but at no point did Fable 5 or Opus 4.8 think to include basic tracking hooks on any page. It’s web design 101 (click a button, log an event) but only if you understand the point of a website.

## Stop Pretending AI Works Like It Has Been Sold

Obviously, neither model understands the outcome unless you specifically explain the need in terms of artifacts that must be created. Tracking and event logging are just two examples of the basic features you must specifically call out to get even the most advanced models to build them.

I had to tell it to generate other basic website elements like a site map and basic SEO metadata for each page. The webpages have 0 security built in, and Fable 5 frequently refused to find issues and even once refused to build a more secure version. It downgraded to using Opus 4.8.

Yes, there are more rigorous ways to prompt the models or provide more workflow context, but as soon as you go down that road, a model like Gemma 4 performs just as well. The more information and context I provide, the less all that advanced AI reasoning matters. My personal website (vinvashishta.com) was built by Gemma 4, all running locally on theDell Pro Precision I talk about all the time.

I provided the same context required to get the frontier models to deliver their websites, and Gemma did just as well. There were still a few manual fixes required, and it produced a website that was equally incomplete to the ones the frontier models delivered. The difference was that it cost 0 for tokens, and I could use a lot more contextual data because I had no worries about sending that data outside of my firewall.

## Hype Meets Reality In Outcomes-Based Benchmarks

The CEO of Palo Alto Networks, Nikesh Arora, went on CNBC today to say that the demand for AI is “infinite.” That might be true if frontier models did any of the things Arora claims they do. He says that we want frontier AI to do high-end research like finding cures for cancer. Yet, the pharmaceuticals business with the most advanced AI stack, Eli Lilly, intentionally avoids using frontier models for research.

Lilly ran an outcomes-based benchmark and wasn’t impressed by the results. They signed a deal with OpenAI in 2024 and have yet to expand the partnership. If frontier models worked, a company like Lilly would be sending out signals in the form of expanded partnerships and new joint ventures with frontier labs.

Instead, it has doubled down on smaller, purpose-built models trained or fine-tuned on its proprietary data for high-end research. It has acquired or partnered with smaller, domain-leading AI providers. Companies that build real things and are accountable for the value those things create are all saying the same thing. AI works. Frontier AI isn’t worth the cost.

That’s why Lilly is the last case study in myAI & Agentic Platform Monetization course. It shows you where the AI cycle is really headed. Everything is moving towards smaller, purpose-built models and information flywheels. It takes the same orchestration layer to run a frontier model or smaller model (either open source or purpose-built). So why pay the extra cost, expose your IP, and become dependent on someone else’s tech?

Arora even admits that most workloads will run on smaller, open-source models, not frontier AI. Yet he continues to repeat the AI demand is infinite claim to support the massive amounts of money being spent by frontier labs. He essentially says, “You have to spend all the money on infrastructure first, then figure out how to monetize it later. And it works every time. Except when it doesn’t.”

Is it any surprise that Arora comes from Softbank, which rode the WeWork debacle all the way down to 0? His entire interview was 5 minutes of hot air, and the person interviewing him gave 0 pushback on even the most ridiculous claims.

## The Enterprise AI Epiphany Your C-Suite Needs

Over the last 3 months, the most mature AI enterprises have looked the AI labs straight in the eye and said, “Your benchmarks are 100% vibes and 0% outcomes-based.” Palantir’s CEO went on a rant during a CNBC interview that went viral. I am not always an Alex Karp fan, buthe was my spirit animal for about 7 minutes. And I was not alone.

“This is not shade. It’s reporting.” The library was open, and Karp read the frontier AI labs like a dime novel. It was elegant savagery and the kind of tough love that might save OpenAI and Anthropic. If they listen to Arora, they will drive themselves right off a spending cliff. If they listen to Karp and their largest customers, they will rapidly pivot towards new partnerships and outcomes-based products.

In the week since Karp’s interview aired, I have gotten more client outreach saying the same thing: “Local AI strategy. Small open-source first agents. Intent-Outcomes alignment. I get it now. Thanks for putting us on the right track.” THIS NEVER HAPPENS. If you have worked as a C-level advisor, you know they don’t give credit out of the blue.

The Zeitgeist around AI has taken a turn, but it’s only really the most mature 10% of AI adopters who see it clearly. This article is something you can use to help your executive leadership and C-Suite understand the themes they may not be seeing yet. Start with 1 question that Alex Karp raised in the interview. I have frequently raised it myself because it shifts the thinking dramatically.

“If I could make you a billion dollars. Wouldn’t I say, ‘I can make you a billion dollars. I want 30%’? Why are they charging for tokens, if it’s so valuable?”

## Helping Your C-Suite See The Power Of Outcomes

That framing is an excellent summary of the outcomes-centric argument. Models are being sold on delivering business outcomes, but they don’t. Agent builder platforms from Microsoft and Google to ServiceNow and Salesforce are sold on being the application layer that will help AI to deliver outcomes. They also don’t.

If any of these companies did what they claimed, they would be migrating to outcomes-based pricing models, not consumption, subscription, or something similar. Frontier AI labs and agentic platforms can’t deliver outcomes, so they sold us tokenmaxxing. The backlash was swift.

I want you to turn your C-Suite’s attention to a different type of frontier AI lab. Begin to evangelize case studies that use JPMC, Eli Lilly, Siemens, Walmart, Tencent, BMW, and Hyundai. For these frontier AI labs, delivering models, agentic platforms, and semantic layers are as meaningless as delivering the websites I led off with. For these frontier AI labs, the technology is secondary to creating value that the business model monetizes.

Technology is critical to delivering value for these frontier AI labs, but it is not the primary outcome that they monetize. The connection to a non-AI outcome is what makes them better case studies in how to monetize AI. The sooner you can get your C-Suite to stop seeing AI as the outcome and return to the outcomes their business model is built to monetize, the sooner your AI investments will begin to deliver the value they need it to.

This is a huge opportunity for us to advance. The timing is right, and the C-Suite is ready to listen. They know what they have been doing isn’t working, which makes them receptive to new ideas. They know their jobs are on the line and investors are watching for revenue growth. CEOs are looking for clarity and need people who can deliver it.

16
1
1
Share
Previous
Next