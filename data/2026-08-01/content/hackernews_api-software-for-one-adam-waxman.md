---
title: Software for One - Adam Waxman
url: https://www.ajwaxman.com/writing/software-for-one
site_name: hackernews_api
content_file: hackernews_api-software-for-one-adam-waxman
fetched_at: '2026-08-01T19:28:12.312376'
original_url: https://www.ajwaxman.com/writing/software-for-one
author: awaxman11
date: '2026-07-29'
published_date: '2026-07-28T00:00:00'
description: Robin Sloan wished for a HyperCard that could build a family app in a day. That world showed up.
tags:
- hackernews
- trending
---

In 2020, Robin Sloan wrote aboutBoopSnoop, a messaging app he built for his family. Four people downloaded it. He considered this a resounding success. His point was simple: an app can be a home-cooked meal. You don't need scale. You don't need users. You cook for the people you love.

The app took him a week to build, half of it lost to code-signing purgatory. He wrote: "In a better world, I would have built this in a day, using some kind of modern, flexible HyperCard for iOS."

## The time is now

Six years later, the essay resurfaced on X whenThariq wrotethat "personal software was a bit early in 2020 but in 2026, it really can be as personal as a home cooked meal, or a handwritten letter."

Lee Robinsonwrote about the same shift. AI has made "personal computing" actuallypersonal. He and his wife built a baby tracker because they didn't need "user profiles, badges, subscription tiers, or any other extra features."

## My smoothie knows my mileage

I spent the past six months building way too much personalized software:

* Asleep appthat runs our sleep consultant's plan
* Afitness appthat sizes my smoothie to that morning's run
* Amarathon planbuilt from my races, not my age
* A"Duolingo for jazz"that quizzes me on chord voicings from my piano lessons
* Amedical records toolthat flagged gaps before a specialist visit

Our sleep consultant's plan arrived as a PDF full of conditional logic: wake windows, nap caps, what to do when a nap fails. Turning it into an app took a week of evenings. Now my wife, our nanny, and I share one live schedule that re-plans itself when a nap runs short.

The sleep app in action

My fitness app is built around my goals and connects data sources in a way no single app can. It knows my weekly run schedule, courtesy of the marathon app below, so it adjusts my daily calorie targets based on that morning's run distance and intensity. It tells me how many extra carbs and protein to eat before and after long runs, and reminds me to carb load the night before. It knows my smoothie recipe, eight ingredients I weigh out every morning, and sizes each portion to that day's training.

The fitness app in action

My running app skips the plan templates and derives everything from my Strava history and race results, including heart rate zones computed from races I ran instead of a formula involving my age.

The running app in action

Sloan's sovereignty point holds up too. "There will be no sudden redesign, no flood of ads, no pivot to chase a userbase inscrutable to us." My wife's favorite feature in the sleep app will be there as long as she wants it.

## My stack

I'm been using the same stack for a couple years now and continue to love it. It lets me build fast and gives me full control over implementation details.

* Framework:Next.jsonVercel
* Frontend:Tailwindandshadcn/ui
* Auth:Better Auth
* Database:Postgres onNeonwithDrizzle ORM
* Email:Resend
* Jobs:GitHub Actions
* AI:Claude Code,Vercel AI SDK,custom skills
* Terminal:Warp
* Analytics:Umami

There are plenty of other great ways to do this, including less technical tools likeClaude Artifacts,Replit, andLovablethat can get you a working app without touching a terminal.

## Cost

The whole thing costs me about $160/mo: $100 for Claude Code Max, $10 in Anthropic API usage, $20 for Vercel, and $30 for Neon.

That's probably more than I'd pay for subscriptions to all these apps combined. But the bulk of the cost is my Claude subscription, which I'd keep regardless. Most of the Neon and API costs come from my slightly larger projects,nycjazz.guideandClaude Code Daily, not the personal apps. Before I upgraded from Claude Pro to Max it was under $100/mo.

Most of these services have generous free tiers, so if you're running one or two apps you could likely keep it to a $20/mo agentic coding subscription and ~$5-10/mo in model API usage.

## Learnings

1. The cost to build dropped off a cliff.The sleep app took a week of evenings. The fitness app took a weekend. The jazz quiz took a single evening after the kids went to bed. A year or two ago I wouldn't have considered building any of these: too slow to build, even harder to maintain. Imagination is now the limiting factor.
2. Maintenance is surprisingly easy.At least so far. Sloan's essay has a running gag in its yearly updates: "I have added one (1) feature, at my mother's request." In 2020 that made sense, because each change cost him a fight with Xcode. I've found fixing bugs, adding new features and dependency bumps to be easier than ever. 9/10 times a feedback screenshot shared with Claude gets the job done.
3. Aggregate data, add an LLM.The cost drop doesn't just mean more apps, it means apps can be far more personal. Most of mine follow the same shape: pull data from multiple sources, combine it in one place, and use an LLM to generate insights from the full picture. My fitness app combines nutrition, sleep, weight, and training data that lives in four separate apps, then uses that context to make recommendations none of them could alone. I think this pattern will spread to professional tools too.
4. Ephemeral is fine.We used the sleep app for about four months. Our son sleeps through the night now, so we retired it. If the app had taken me months to build, that might sting. Because it took a week, I'm just glad it worked when we needed it.
5. AI floods big markets and unlocks small ones.Yes, AI producesendless derivative apps. But the same tools also let me build apps for my household that no company would bother making. Beyond my household, I builtnycjazz.guidefor NYC jazz fans andclaudecodedaily.comfor Claude Code developers, audiences too small for a business but worth serving.
6. Good APIs matter more than ever.I switched from Cronometer to FatSecret because FatSecret had a better API. My fitness app pulls from Strava, Oura, Withings, and FatSecret, and the quality of each integration depends on how well the API is designed. As more people build personal software, users will expect their apps to have APIs and MCPs worth connecting to.
7. Building is the point, not just the result.These apps solve real problems for me and the people I care about: how well our son sleeps, my health, my running. That part is rewarding. But I also spend my evenings after the kids are asleep building these instead of watching Netflix or scrolling X. It's my preferred source of entertainment now.
8. It's not just fun. It's addictive.Agentic coding has slot machine mechanics. You're one prompt away from the next feature or unlock, so you keep pulling. The irony isn't lost on me: I've ruined more than a few nights of sleep building apps to improve my health.

## Looking ahead

My approach is still too technical for most people. You need to be comfortable with a terminal, a database, and deployment pipelines. But I don't think that lasts. Sam Altmanposted recentlyabout sending ChatGPT a single message from his phone: plan a trip for nine friends, build a site to coordinate, draft the invite email. It worked. The prompt was one paragraph long.

If that's where the tools are heading, building personal software won't require a developer's stack for much longer. I kept building these apps because no app in the App Store knows my smoothie recipe, my race history, or my sleep consultant's rules. I think that frustration is common. Once the barrier drops far enough, a lot of people will build their own.

And once you use an app that actually knows your context, the generic version feels broken. I wouldn't be surprised if truly personalized becomes the new baseline consumer expectation.

Sloan wished for "some kind of modern, flexible HyperCard for iOS." He got something stranger: you describe what you want in plain English, and an agent builds it. His better world has arrived.