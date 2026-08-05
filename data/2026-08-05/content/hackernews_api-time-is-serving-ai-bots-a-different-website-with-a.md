---
title: TIME Is Serving AI Bots a Different Website, With Ads Built In - Vincent Schmalbach
url: https://www.vincentschmalbach.com/time-serves-ai-bots-a-different-website/
site_name: hackernews_api
content_file: hackernews_api-time-is-serving-ai-bots-a-different-website-with-a
fetched_at: '2026-08-05T20:40:04.453954'
original_url: https://www.vincentschmalbach.com/time-serves-ai-bots-a-different-website/
author: vincent_s
date: '2026-08-05'
published_date: '2026-08-05T12:41:25+00:00'
description: TIME is now serving two different versions of its website. Humans get the magazine. AI crawlers get a stripped down markdown copy with ads baked in that no…
tags:
- hackernews
- trending
---

Currently Available:
 Need a skilled Software Developer for your next project?
 

Hire Me Today

Categories

Economics
 
LLM
 
News
 
SEO
 

# TIME Is Serving AI Bots a Different Website, With Ads Built In

August 5, 2026by Vincent Schmalbach

TIME is now serving two different versions of its website. Humans get the magazine. AI crawlers get a stripped down markdown copy with ads baked in that no person will ever see.

I fetched one ordinary TIME health article,The Morning Light Habit Sleep Experts Swear By, over and over from the same machine, changing only theUser-Agentheader each time. That header is the string every browser and bot sends to say what it is. TIME reads it and decides what to hand back.

As Chrome, I got200 OK,text/html, and 303,235 bytes. The full page, design, images, scripts. As Safari, the same 303KB. As Googlebot, also the same 303KB of HTML.

Then I asked as an assistant crawler. As ClaudeBot, I got200 OK,text/markdown, and 13,409 bytes. As PerplexityBot, byte for byte identical. As OpenAI's OAI-SearchBot, identical again. Same URL, same second, one twenty-third of the size, and a completely different format: no HTML, no layout, just clean markdown that a language model can process.

A couple of the bots did not even get that. GPTBot and ChatGPT-User, the agents OpenAI uses for training and live fetches, came back406. Blocked. But OAI-SearchBot, the one that feeds ChatGPT's search index, was waved through to the markdown. So this is not a blanket bot policy. TIME is choosing, per bot, who gets the reader-free version.

Response headers on the markdown copy:

content-type: text/markdown; charset=utf-8
cache-control: no-store
x-mobian-registry-version: 2026-07-28.v9
x-mobian-impression: 46dfff3c-fb40-41cc-85e1-8b1fa637083a
x-mobian-tokens: 3323
x-mobian-format: md

Mobian is an ad-tech vendor. The markdown page literally begins with<!-- mobian-agent-page publisher="time" -->. Thatx-mobian-impressionvalue is a fresh UUID on every single request. I fetched the same page twice and got two different IDs. Paired withcache-control: no-store, that means every time a bot reads the page, it is logged as a distinct ad impression. Andx-mobian-tokens: 3323tells you the unit being counted. Not a person, not a pageview. Tokens fed into a model.

The article itself carries no ad. The sponsored unit shows up on the list and section pages, one per page. So I fetched TIME'sBest Inventions of 2025collection as ClaudeBot. Sitting inside the markdown, where no human reader would ever encounter it, is a full Ally Bank FAQ:

> Sponsored content. Supplied in partnership with Ally.

#### Who is Ally Bank?
Ally Bank is an online-only bank launched in 2009...

#### What bank is built for life today?
Ally describes itself as the only bank built for life today...

It runs on with questions like "Which banks offer early direct deposit?" and "Can you deposit cash at Ally Bank?", each answered in Ally's own marketing language, plus aFAQPageJSON-LD block and tracking links taggedcampaign="ally-2026-q3". The business section had the same treatment for the Project Management Institute: a "Reference Facts and FAQ" table, member counts, a claim that certified project managers earn 16% more, all labeled sponsored. The human HTML of those pages contains none of it. Zero hits for "Ally Bank" or "Mobian" when I loaded them as a person.

"Who is Ally Bank?" is written like the phrasing a model emits when a user asks ChatGPT which bank to open an account with.

The ads are labeled sponsored inside the markdown, so this is not undisclosed advertising in the classic sense. What is hidden is the audience split. There is now a layer of TIME.com written entirely for machines, and the humans who read the site have no idea it exists or what is being said to the models on their behalf.

Googlebot gets the same HTML a human gets, so the search-ranking crawler sees the real page. Only the assistant crawlers get the forked version.

TIME says its bot traffic already outnumbers its human traffic on most days. That number is going to be true for a lot of publishers soon. So this is probably the first clear look at what the web starts to become when the main audience is AI models.

What I'm building

## Delegate tasks. Get software.

Give Vroni a GitHub issue, bug report, spec, or rough idea. It reads the repo, plans the change, writes code, runs checks, and works toward a review-ready pull request.

Take a look at vroni.com

## Subscribe to my newsletter

Get new posts when I publish them.

 Subscribe
 

I respect your privacy. Unsubscribe at any time.