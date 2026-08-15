---
title: ChatGPT Already Knows Who It'll Recommend Before It Searches — Suganthan
url: https://suganthan.com/blog/chatgpt-decides-before-it-searches/
site_name: tldr
content_file: tldr-chatgpt-already-knows-who-itll-recommend-before-it
fetched_at: '2026-08-15T11:17:47.089869'
original_url: https://suganthan.com/blog/chatgpt-decides-before-it-searches/
author: Suganthan Mohanadasan
date: '2026-08-15'
published_date: '2026-08-10T00:00:00.000Z'
description: ChatGPT writes brand names into its own search query before it fetches a single page. I read the traffic across 60 conversations to work out when it happens, what being named is worth, and what actually gets you onto that list.
tags:
- tldr
---

I asked ChatGPT for the best AI note taking app. Nothing in my question named a brand.

Before it fetched anything, it wrote itself this search.

best AI note taking apps 2026 official pricing features Granola Notion AI Otter Fireflies Fathom Mem Limitless

Read the tail of that string. Granola. Notion AI. Otter. Fireflies. Fathom. Mem. Limitless. Seven products in one search.I’d named none of them, and nothing had come back from the web search yet, so no result put them there. Those names came out of the model.

Then it ran nine more searches.

site:granola.ai pricing features AI meeting notes 2026

site:otter.ai pricing AI meeting notes 2026

site:fathom.video pricing AI meeting assistant 2026

site:notion.com product AI Meeting Notes official 2026 pricing

site:fireflies.ai pricing official AI meeting notes 2026

site:mem.ai pricing AI notes official 2026

site:notebooklm.google official features pricing 2026

That’s the fan-out I wrote about in the first two parts, and now you can see what it’s made of. One search to name the shortlist, then one search per name on that shortlist, each pointed straight at that company’s own website.

So the fan-out was never a search for candidates, it was ChatGPT going down a list it already had, one name at a time.

In the first two parts I wrote that you need to survive asite:yourdomain.comprobe, because ChatGPT runs them. It only runs one on you if you were named in that first search. Miss the shortlist and your website never gets looked at, however well built it is. The decision happens before anything touches your server.

I’ve spent two months reading this traffic forpart 1andpart 2. This is the first thing I’ve found that changes what I’d tell a client to do.

Before you read any further, all of this comes off one account, so every percentage below is a direction rather than a measurement. The mechanism is a different matter. You can reproduce that on your own account in two minutes and I’ll show you how at the end.

## The four ideas behind this

Each one sets up the next.

1. ChatGPT writes its own search queries, and you can read them.
2. Those queries already contain brands nobody mentioned.
3. Being in that query is worth about 33 times more than being findable.
4. Once you’re in, a second and much harsher filter decides who gets cited.

## Idea 1. It writes its own searches, and they’re readable

When you ask a question, ChatGPT rewrites it into search queries of its own, runs them, reads what comes back, then writes an answer.

Those queries sit in the response your browser downloads, under a key currently calledsearch_queries. OpenAI renamed it fromsearch_model_queriesin early August 2026. Nothing about this is a leak. Your own browser needs that JSON to draw the page, and you can read it in DevTools on your own account in about two minutes. Recipe’s at the end.

Here’s one from a question about live chat software.

best AI live chat customer support software 2026

Intercom Fin Zendesk AI pricing official

I asked for “best ai based live chat support software”. It added the year, “official”, “pricing” and three names.

Everything below comes from reading a few hundred of these.

Start here.Open ChatGPT, ask the “best [your category]” question your buyers ask, and read the query it writes back. That one string shows you whether ChatGPT knows your brand exists, which is what AI visibility audits are sold to answer. Everything else in this article is about what to do with what you find in it.

## Idea 2. The shortlist exists before the search runs

The obvious objection to my note taking example is timing. Maybe ChatGPT searched once, saw those brands, then wrote a smarter second query. That’d make the names a result of retrieval rather than a cause.

So I tested it properly. For each conversation I took the first user message and the first search query, ordered by timestamp. At that point nothing’s been fetched, so there’s no earlier result to have learned from.

In 21 of 27 conversations, that first query contained brands the user never typed.

What I asked
What ChatGPT searched for, before any results
best AI note taking app 2026
…official pricing features 
Granola Notion AI Otter Fireflies Fathom Mem Limitless
best ai based live chat support software
…2026 
Intercom Fin Zendesk
 AI pricing official
best ai based live chat software
…
Intercom Fin Zendesk AI Ada Decagon Sierra
 pricing official

Look at rows two and three. Same question, slightly different phrasing, and the list grew from three names to seven. The list stretches with how you ask instead of coming out of a fixed table.

Then I ran twelve categories that have nothing to do with each other, to check this wasn’t a software thing.

11 of 13 did the same.

Category
ChatGPT’s own first search
Language learning apps
Duolingo Babbel Busuu Pimsleur Speak LingQ review
Accounting software
official pricing Xero QuickBooks Zoho Books FreshBooks Wave Sage
Online therapy
BetterHelp Talkspace Brightside Online-Therapy.com official pricing insurance
Robot vacuums
Roborock Saros Dreame X50 Narwal Freo Z10 Eufy S1 Pro
Web hosting
Hostinger SiteGround Cloudways Kinsta
Electric SUVs
review Car and Driver Edmunds Top Gear

The robot vacuum row is the one that got me. Recalling that Roborock exists would be unremarkable. It recalledSaros,Dreame X50andEufy S1 Pro. Current model numbers, in the first query, unprompted. Whatever this knowledge is, it goes down to the product line.

The electric SUV row does something different from all the others. For accounting and therapy and hosting it named vendors and went to their pricing pages. For cars it named magazines. Car and Driver, Edmunds, Top Gear. In one category its instinct is to go to the makers, in another the reviewers.

I got excited about that and then re-ran three categories to see if any of it holds still.

Category
First run
Second run
Language learning
Duolingo Babbel Busuu Pimsleur Speak LingQ
Duolingo Babbel Busuu Pimsleur LingQ
Accounting software
Xero QuickBooks Zoho Books FreshBooks Wave Sage
site:quickbooks.intuit.com ... QuickBooks Online official
Web hosting
Hostinger SiteGround Cloudways Kinsta
benchmark WordPress ReviewSignal

Language learning barely moved. Five of six names came back the same. Accounting collapsed from six vendors to a single targeted probe at QuickBooks. Web hosting switched sides completely, dropped every vendor and went to a review site instead.

So vendors versus magazines is a tendency that can flip between runs, not a fixed property of the category. Two things survive that. The injection happened every single time, and the category with the clearest market leaders kept its names. My guess is that settled categories have stable shortlists and contested ones wobble, but three repeats isn’t enough to say that.

Don’t judge your AI visibility from one answer. Run the question five times, because the list changes between runs.

### It happens whenever ChatGPT has to supply the products

Every query up to this point had the word “best” in it, so that was the first thing I tried to break. I ran twenty-four more queries that avoided the word, across seven different shapes.

“Best” turned out to have nothing to do with it. What matters is whether ChatGPT has to come up with the products itself.

When it doesn’t search at all, none of this applies.Ask how noise cancelling works, or what a vector database is, and it answers from training with no web search. Same for open-ended moaning. “We are spending too much on customer support tooling” got no search either. Seven of my twenty-four never touched the web, so there was no shortlist to get onto.

Name the brands yourself and it takes them.“Xero or QuickBooks for a small business” went straight tosite:xero.com/uk. “Should I use HubSpot for a small agency” went tosite:hubspot.com.

Leave the candidates to it and it reaches into memory.That happened in ten of the eleven cases where I asked for a recommendation without naming anything.

What I asked
ChatGPT’s first search
what should i use to take notes in meetings
Granola official pricing meeting notes
our meeting notes are a mess and nobody writes them up
Granola official pricing AI meeting notes 2026
what do people use to clean floors automatically these days
site:global.roborock.com Saros 10R official
which crm works for a 5 person startup
site:hubspot.com pricing sales hub starter official
what is the cheapest way to host a wordpress site
site:hostinger.com/uk wordpress hosting pricing UK official
help me pick a web host for a small ecommerce site
official WooCommerce hosting pricing SiteGround GrowBig 2026

The third row is my favourite. I deliberately avoided saying “robot vacuum” and named nobody. It went to a specific Roborock model’s own website on the first search.

Row two should worry you if you sell software. That’s a complaint, not a shopping question. Somebody grumbling about their meeting notes got turned intoGranola official pricingbefore a single page was fetched.

And there’s a version of this aimed straight at your competitors. All three of my displacement queries pulled in new names. “Alternatives to zendesk” produced Help Scout, “what can i use instead of quickbooks” produced Zoho Books, and “something like duolingo but better for grammar” produced Kwiziq and Babbel. When your customer goes looking for a way out of your rival, ChatGPT nominates whoever it already knows. That could be you, and you don’t get a say in it on the day.

If ChatGPT searches for a product and you haven’t named one, it brings its own.

Do this.Run your category question five times and write down the names that appear in the query each time. The names that show up every run are your real competitive set in ChatGPT’s head. Anything that comes and goes is contested ground, which is where a push can move something. If your brand never appears in five runs, you have your answer and it isn’t a technical one.

## Idea 3. Being in the query is worth about 33 times more

I sorted every brand into two groups. Ones that appeared in a query ChatGPT wrote, and ones that were only fetched during the search without ever being named. Then I checked how often each group made it into the final answer.

Brand’s situation
How many
Mentioned in the answer
Named in ChatGPT’s own query
119
68.9%
Fetched, never named in a query
515
2.1%

About 33 times the difference.

I also found 86 cases where a brand got recommended and its website was never fetched in that conversation at all. A mention doesn’t need a crawl.

This is the uncomfortable part for my own industry. Most of what’s sold as GEO right now is retrieval work, which is the 2.1% column. The 68.9% column is decided before any of it runs.

Do this.Split your budget to match the two columns. If you’re absent from the query, the money belongs in the work that gets you written about, reviewed, compared and listed. Digital PR, category content, review-site placement, analyst coverage, showing up in the roundups your buyers read. If you’re already in the query, that spend is largely done and the technical work below is what’s left.

## Idea 4. Being in the query is the entry ticket, not the win

If it stopped there the advice would be “build brand equity” and we could all go home. A second filter runs after the query, and it’s brutal.

I built a labelled dataset from 57 conversations. Every retrieved page as a row, with whether it earned a citation as the label. 3,554 pages.

110 got cited. That’s 3.1%.

ChatGPT reads around 600 pages to write one answer and credits about 30. Almost everything gets read. The gap between being read and being credited is where the work is.

Three things separated the cited from the ignored.

Position, hard.ChatGPT groups results by domain, and where you sit in that group predicts nearly everything.

Position in the group
Cite rate
1st
5.2%
2nd
4.6%
3rd
2.4%
4th
1.7%
5th
0.6%
6th or later
0.3%

Below the top two, citation is a rounding error. Being in the retrieved set isn’t a win if you’re ninth.

Piling on pages hurts.When several pages from one domain show up in the same group, per-page conversion collapses.

Pages from your domain in the group
Cite rate
1
4.0%
2
6.2%
3 to 4
~4.3%
5
1.9%
6 or more
1.7%

Two tightly matched pages is the sweet spot. Past six you’re mostly competing with yourself. I’ve been telling clients to consolidate for a year on instinct. This is the first time I’ve watched it happen in the data.

Relevance qualifies you, it doesn’t select you.I scored the cited page against every other page retrieved for the same claim, on how well its text matched the sentence being supported. The cited page sat in the top 5% of the pool. But it was the single best match only 20% of the time, and its average overlap was well below the best available.

So claim relevance builds a shortlist and something else picks the winner. Get into the top 10% for a specific claim and you’re in the conversation. That part you control by writing. The final pick involves things I can’t see.

Do this.Take the questions your buyers ask and find every page of yours that answers the same one. That’s the bottom row of the table above, and it’s costing you. Pick the page that matches the intent most tightly, make it the answer, and fold or redirect the rest into it. Then make sure the sentence that actually answers the question sits near the top of that page in plain HTML text, with the numbers in it.

Finding those overlaps by hand across a real site is the miserable part. Cannibalisation is normally judged on keyword overlap, and that’s the wrong unit here, because ChatGPT groups by claim rather than by keyword.

This is whatKeyword Insightswas built for.

It clusters your keywords by search intent rather than by string match, so the pages fighting over one intent surface as a group even when they share no keywords.

That grouping maps closely onto what I’m watching ChatGPT do when it collapses a domain down to one cited page.

Full disclosure, it’s my company, which is also why I know it handles this specific job.

## What I’d actually do with this

The findings split AI visibility into two games that keep getting treated as one.

### Game one is being in the category vocabulary

If ChatGPT doesn’t already connect your brand to your category, it won’t name you in the query, and you’re looking at a 2% chance of a mention.

Schema won’t fix that, and neither will page speed. Anllms.txtfile has even less of a chance, because your server never gets contacted before the decision’s made.

What seems to build it is slow and unglamorous. Being written about, reviewed, compared and argued over across the open web for years, until the association exists in the training data.

That’s digital PR and category-defining content, which is awkward for everyone currently selling technical audits as an AI strategy.

### Game two is winning the citation once you’re in

That’s the 3.1%, and it’s real. One tightly matched page per intent, the claim-bearing sentence early, facts and numbers in plain HTML text, and no cluster of near-identical pages fighting each other.

Here’s the whole thing as a sequence you can run this week.

1. Read the query.Ask your category question five times and note the brands ChatGPT writes into its own search. Ten minutes.
2. Find which game you’re in.In the query every time means you’re playing game two. Never in it means game one, and no amount of page work will move you.
3. If you’re absent, go and get written about.Reviews, roundups, comparison pages, the publications your category reads. In a category like electric SUVs, where ChatGPT went to the magazines before it went to any manufacturer, that’s the only door.
4. If you’re present, check conversion not retrieval.Count how often your pages get fetched against how often they get credited. Fetched a lot and credited rarely is a page problem, not a visibility problem.
5. Fix the page, not the site.One page per intent, the answer sentence near the top, real numbers in HTML text rather than in an image or loaded by JavaScript.
6. Re-check monthly.The stability test showed the shortlist moves, and the format moves with it. In early August 2026 OpenAI renamed the key these queries sit under, and the fan-outs in my captures dropped from 12 searches per answer to 4. What was true in July won’t necessarily hold in September.

In my data one brand got fetched 66 times and never cited once. That’s not an awareness problem. The engine kept going back and kept deciding they had nothing worth quoting. Step four exists to catch that.

Steps one and four are what I builtFanoutFoxfor, because running them by hand for every answer gets old fast. It’s a free Chrome extension, everything stays in your browser, and it reads your own ChatGPT session rather than guessing from the outside. It shows you the fan-out queries verbatim, so step one is a glance instead of a DevTools session.

For step four it now has a converts column, retrieved against cited per domain, the number this article argues you should be tracking instead of retrieval counts. A domain that gets read repeatedly and never credited is the diagnosis you’re looking for, and it’s sorted right there.

## The caveats

I’d rather you trust the parts that deserve it.

The mechanism is solid. ChatGPT writing brand names into its first query is visible in a single capture and you can reproduce it yourself in two minutes. Every percentage comes from one account and a few hundred conversations, weighted towards software and AI tools because that’s what I ask about. A different query mix moves the numbers.

My first pass was entirely “best X” queries, which meant I’d have published a claim about ChatGPT while only testing one phrasing of one kind of question. The twenty-four query boundary test exists because that bothered me, and it changed the finding rather than confirming it.

Personalisation is real and it showed up in my data. My meal kit query came back withUAE,Dubaiand a local company. Travel insurance went straight to a UAE insurer’s site. I never said where I live. So these are my account’s shortlists, not ChatGPT’s.

FanoutFox has a personalisation label, so you can see if your query is affected by personalisation.

The 68.9% against 2.1% comparison uses whole conversations, so a brand learned in turn one and queried in turn two counts as pre-known. That’s why the first-query test is the headline claim instead. A 33 times gap is too big for that contamination to explain, but the clean number is the 21 of 27.

My brand matching splits “Car and Driver” into two tokens and once let “SaaS” through as a brand. On the local query it counted “Arabian Ranches” and “Dubai” as brands, which they obviously aren’t. The queries themselves are the evidence. Treat my counts as approximate and read the query strings instead.

## Check it yourself in two minutes

You don’t have to take my word for any of this, which is the whole point of reading traffic instead of guessing.

1. Open ChatGPT in Chrome, open DevTools, go to the Network tab.
2. Ask “best [your category] 2026”.
3. Filter forconversation, open the response, search forqueries.
4. Read the first query the model wrote and look for names you never typed.

If your competitors are in that list and you’re not, now you know, and it took less time than making a coffee.

That’s the manual version, and it’s fine for one check.FanoutFoxruns the same check on every answer you give it, keeps a history so you can watch a category shift over weeks, and never sends your conversations anywhere. It’s free and it’s the tool I use for all of this myself.

## What’s next

The gap in all this is that it’s one account. I’ve requested my full ChatGPT data export to run the same analysis across every conversation I’ve ever had. The follow-up that would settle it is the same category sweep on several accounts at once. If the same brands get injected for the same questions on other people’s accounts, it’s model-level knowledge. If they don’t, personalisation is doing more work than anyone thinks.

Either answer is worth having, and I’ll publish whichever one turns up. Anything that moves goes inthe ChatGPT research tracker.

Read off a logged-in ChatGPT Plus account in Dubai between 24 and 25 July 2026. 57 conversations for the citation numbers, 27 for the first-query test, twelve fresh category queries and three repeats. Structural findings are solid at this sample. Every percentage is directional.

 
 
 
 

Want to know whether ChatGPT already knows your brand?

 

If you want help applying this on your own site, my agency Snippet Digital takes on this kind of work. Send an enquiry and I will be in touch.

 
 Work with me 
 
 
 
 

Enjoying this? Get the next one in your inbox.

 

I email when I publish something new. Usually 2 to 4 emails a month. Unsubscribe anytime.

 
 
 
 
 
 
 
 
 
 
 
 
 
 

Join my list

 
 
 
 

Join 1,220+ readers.Unsubscribe anytime.

 
 
 
 
 

Share

 
 
 
 
X
 
 
 
 
LinkedIn
 
 
 
 
Facebook
 
 
 
 
Copy link
 
 
 
 
 
 
 
 

Want my posts to show up more often on Google?

 

One click and Google will surface this site in your Top Stories.

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Suganthan Mohanadasan
 

Norwegian entrepreneur with 20+ years in SEO. Co-founder of Keyword Insights and Snippet Digital. Based in Dubai.

 
 
 
 
 
 
 
 
 
 
 
 
 
 

## You might also like

 
* ChatGPT Changed How It Picks Sources While You Were Reading My Last Post14 Jul 2026geoai-seo
* How ChatGPT Actually Picks Sources (I Read the Network Traffic, Not the Outputs)24 Jun 2026geoai-seo
* How Perplexity Actually Picks Sources (I Read the Stream, Not the Answers)27 Jul 2026geoai-seo
 
 
 
 

← All posts