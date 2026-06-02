---
title: AI costs how much? GitHub Copilot users react to new usage-based pricing system. - Ars Technica
url: https://arstechnica.com/ai/2026/06/ai-costs-how-much-github-copilot-users-react-to-new-usage-based-pricing-system/
site_name: newsfeed
content_file: newsfeed-ai-costs-how-much-github-copilot-users-react-to-ne
fetched_at: '2026-06-02T12:21:46.509133'
original_url: https://arstechnica.com/ai/2026/06/ai-costs-how-much-github-copilot-users-react-to-new-usage-based-pricing-system/
date: '2026-06-01'
published_date: '2026-06-01T22:18:09+00:00'
description: Some report burning through their whole monthly "AI credit" allotment in a single day.
tags:
- ars-technica
- ai
- copilot
- github
---

Text
 settings

In April, GitHubannouncedthat it was moving subscribers from request-based billing to a usage-based model for its AI-powered Copilot service. As that new pricing model goes into effect today, many GitHub Copilot users are reporting some extreme sticker shock as they realize just how quickly their previous “normal” usage is burning through their newly limited monthly allotment of AI credits.

Across social media and forums,many Copilot usersaresharing personal statisticsshowing howjust a few hoursofAI usagecan nowaccount for a large chunkof their new monthly subscription caps. For some users, it reportedlytook less than a daytouse upa month’s usage quota.

That’s a big change from previous months, when GitHub Copilot subscribers were allocated a certain number of “requests” and “premium requests” based on their payment tier. GitHub said that the old system meant that “a quick chat question and a multi-hour autonomous coding session [could] cost the user the same amount,” forcing Copilot itself to “absorb much of the escalating inference cost behind that usage.” Indeed, some Copilot users have beensharing estimatesfromGitHub’s own toolshowing that their previous monthly usage wouldrack up bills in the thousands of dollarsunder the new pricing plan.

 Cost estimates like this show just how much GitHub was subsidizing power users’ Copilot habit in the past months.
 

 Credit:
 
twhoff / Reddit

 Cost estimates like this show just how much GitHub was subsidizing power users’ Copilot habit in the past months.

 

 Credit:

 

 
 twhoff / Reddit

 

Under GitHub’snew usage-based pricing system, paid Copilot subscriptions instead grant users a certain number of AI “credits” each month, with one credit corresponding to $0.01 of usage. Subscribers also get bonus credits depending on their subscription level: the $10/month Pro plan includes 1,500 credits ($15 worth); the $39 Pro+ plan includes 7,000 credits ($70 worth); and the $100/month Copilot Max plan includes 20,000 credits ($200 worth).

The precise number of Copilot credits used by a given prompt is determined by the number of input and output tokens used and the rates charged by the underlying large language model. That means pricing is highly dependent not just on the type of request but on the specific model that a user chooses. One million output tokens from OpenAI’s GPT-5.4 nano wouldrun just $1.25 on GitHub Copilot, but that same level of output would run $30 on the frontier GPT-5.5 model (Copilot users who rely on “Auto” mode to pick the most appropriate available model for any request should be extremely careful, as some users report it canswitch to expensive models for extremely simple queries).

## How much for that prompt in the window?

Spot testing by Ars Technica found that re-runningour simple “build aMinesweepergame” promptthrough Claude Haiku 4.5 via Copilot used about 94 credits (you can view the results here). That’s a pretty decent rate for a relatively simple toy project. But it’s also easy to see how those kinds of costs could balloon quickly for requests involving major changes or reviews on complex codebases.

You can see that kind of ballooning cost in reports of a single complex promptburning through 171 Copilot credits, or anotherspending 700 creditson “a few prompts,” or a couple of Copilot-led commitsusing up 5,000 credits. Other Copilot users expressed surprise at just how many credits could be spent on even simple Copilot requests, froma reported 15 creditsfor a simple “run-of-the-mill query” tospending 100 creditsin “generating a small plan.”

“Even though I was super cautious on the first day, trying it out with a limited number of uses, it still consumed 840 credits,” one userwroteof testing Claude Sonnet 4.6 through Copilot today. “I haven’t even done any really complex work yet,” another user complained afterreportedusage representing 21 percent of their monthly Pro Copilot subscription’s credit allotment in a single day. “I have a feeling I’ll be going somewhere else pretty soon.”

 Using all 8,000 of your org’s monthly AI credits in a single day is… probably not sustainable.
 

 Credit:
 
gxjo / X

 Using all 8,000 of your org’s monthly AI credits in a single day is… probably not sustainable.

 

 Credit:

 

 
 gxjo / X

 

Amid the pricing change, plenty of GitHub Copilot users are predictably and publicly threatening to cancel their subscriptions or looking for other AI coding options. But others say they have been able to adjust to the new world of usage-based pricing. Coder Henri Kinnunenwritesthat they only burned 161 credits in a “productive day” of using GPT 5.3-Codex through Copilot, thanks to limiting themselves to “very focused and deliberate changes with AI.” Over on Bluesky, coder Neil Hewittwisely notedthat continuing a three-day-old chat session on Copilot probably isn’t as wise now, since it means sending “the entire chat history as context every time… hey, input tokens use credits… it’s not rocket science.”

While some Copilot users are jumping ship for other services with more generous usage limits, that kind of subsidized customer acquisition may soon give way to Copilot-style usage-based pricing across the industry. If that happens, LLMs that are more efficient with their tokens may win the economic battle; on Reddit, one user isalready discussinghow they’ve integrated Deepseek into their GitHub VSCode environment at a cost of only “about 7 cents for 15 million tokens.” While you might say “you get what you pay for,” some AI users are now contemplating a world where they also have to pay for what they get.

 Kyle Orland
 

Senior Gaming Editor

 Kyle Orland
 

Senior Gaming Editor

 Kyle Orland has been the Senior Gaming Editor at Ars Technica since 2012, writing primarily about the business, tech, and culture behind video games. He has journalism and computer science degrees from University of Maryland. He once 
wrote a whole book about 
Minesweeper
.
 

1. 1.AI costs how much? GitHub Copilot users react to new usage-based pricing system.
2. 2.An OpenAI model solved a famous math problem that stumped humans for 80 years
3. 3.Fed up with vibe coders, dev sneaks data-nuking prompt injection into their code
4. 4.New Trump vaccine order based on "no credible scientific evidence," doctors say
5. 5.Nvidia RTX Spark comes to Windows PCs with Arm CPU, RTX GPU, and unified memory

Customize