---
title: Does Reddit have an astroturfing problem? What the data suggests — Peter Vijeh
url: https://www.petervijeh.com/projects/reddit-astroturf
site_name: hackernews_api
content_file: hackernews_api-does-reddit-have-an-astroturfing-problem-what-the
fetched_at: '2026-09-30T06:00:21.627381'
original_url: https://www.petervijeh.com/projects/reddit-astroturf
author: p-s-v
date: '2026-09-28'
description: In 51,129 comments from six knife subreddits, the 5% most brand-heavy accounts wrote 11.3% of the brand mentions in buying threads, against 7.9% expected by chance. For one brand it is 31% against 8%. The full Reddit histories of those accounts are 4.5 years old and spread over 66 subreddits, the same as a comparison group, so the data shows concentration and not who paid for it.
tags:
- hackernews
- trending
---

One chef's-knife brand gets 31% of its "what should I buy" mentions from 5% of the accounts, four times what chance predicts. So I pulled those accounts' full Reddit histories.

I like to cook, and cooking turned into an obsession with high-end Japanese chef's knives. When I want to buy a knife, or anything else, I type the product name into Google and add the word "reddit". A lot of people do this. Mike Riggs wrote it up in Reason in 2022 as "the Reddit hack", after Dmitri Brereton's essay on Google search made the same point: a query with "reddit" on the end returns humans instead of affiliate pages. The bet behind the habit is that a stranger in r/chefknives has no reason to lie to you about a knife.

That bet has an obvious weak point. If Reddit is where buyers go for unpaid opinions, Reddit is where a brand would want to plant paid ones. I wanted to know whether the knife subreddits I read, and scrape for New Knife Day, show any sign of that. Not a hunch about one suspicious comment, but something I could count and someone else could recount.

## Why the question is testable at all

Last year I fine-tuned a small named-entity model, GLiNER, to pull brands, models and steels out of knife comments. From "picked up a Mazaki in white #2, way better than my old Fibrox" it returns Mazaki as a brand, Fibrox as a model and white #2 as a steel. That model runs over every comment the New Knife Day scraper collects from six subreddits: r/knives, r/knifeclub, r/chefknives, r/japaneseknives, r/FixedBladeEdc and r/KnifeSteels.The write-up on that model is here.

So for every comment I already have who wrote it, which brands it names, and whether the thread it sits in is someone asking what to buy. That is enough to ask a narrow question: in the threads where a recommendation changes a purchase, who is doing the recommending?

New Knife Day is my site for knife collectors. It catalogs knives and steels and tracks which knives people on Reddit are buying and arguing about, so I have a stake in knife Reddit being worth reading.New Knife Day is at new.knife.day.

## What astroturfing would look like in the data

Nobody publishes their shill accounts, so I had to decide in advance what paid posting would leave behind. The market for it is not hidden. REDCmts sells one Reddit comment for $9.99 and 100 for $699.99, from what it calls "real, aged accounts", and shows a gallery of brand mentions it says it delivered. Soar says its accounts are "aged and manually warmed" for weeks before a single brand mention. Bazzly advertises automated replies to every post that looks like someone shopping.

REDCmts price list, September 2026. This shows the service exists and what it costs. Nothing in this article connects it, or any vendor, to any account in the knife subreddits.
Soar describes the account preparation a buyer is paying for. Same caveat as above.

Taking those sales pages as the description of the product, a paid campaign for one brand, delivered through a handful of prepared accounts, should show up as:

* A small group of accounts writing a disproportionate share of the brand mentions in "what should I buy" threads.
* Those accounts naming one brand almost every time they name any.
* Thin accounts: few comments, low scores, no real standing in the subreddit.
* Young accounts, or accounts with histories that are hidden or wiped.
* Accounts that post mostly in knife subreddits, since the knife comments are what is being paid for.
* Links to a store or an affiliate page.

Every one of those is also what a devoted fan, a maker's employee posting on their own time, or a brand's own subreddit regulars wandering into a buying thread would produce. Public Reddit data can show that recommendations are concentrated, and cannot show why. Everything below is about the first half.

## The corpus, and the refresh that changed the answer

The scraper stores each new post and its comments shortly after posting. That turned out to be the wrong moment for this question: a buying thread collects its recommendations over the following day or two, and r/knives posts had 1.5 stored comments each. A refresh pass went back to 3,607 posts older than 48 hours and refetched their comment trees, which took the corpus from 21,673 comments to 51,129. Before the refresh the test below found nothing, because about 800 buying-thread mentions were too few to tell 7.6% from the 7.1% chance gives.

Count
Posts
6,675
Comments after refresh
51,129
Authors with 10 or more comments
987
Brand mentions in buying threads, from those authors
1,471

Three definitions do the work. A buying thread is a post whose title or body matches phrases like "should I buy", "recommend", "under $" or "best knife"; it is a regular expression, not a classifier. An author's brand-heaviness is the share of their comments that name a brand, weighted toward naming the same brand each time. The 5% of the 987 authors with 10 or more comments who score highest are 49 accounts, and the rest of this article calls them the brand-loyal accounts. I score it this way because an account that keeps bringing up the same brand is the product the vendors above are selling.

The question is what share of buying-thread mentions the 49 brand-loyal accounts would write by chance, given how much everyone posts. To get that number I keep every brand mention where it is, in its thread and naming its brand, and reassign the author names at random across those mentions, like shuffling name tags. A prolific account still gets many mentions and a quiet one gets few, but which threads an account appears in no longer depends on who it is. I do this 1,000 times and record the 49 accounts' share each time. If the real share sits inside the range those 1,000 reassignments produce, they are no more concentrated in buying threads than its comment count explains. If it sits above the range, they turn up in buying threads more often than their posting volume explains. Authors are salted hashes throughout; no usernames or comment text leave the database.

## What the data supports

Here is the test in one example. Take the 1,471 brand mentions in buying threads and deal the author names back out at random, so a busy account still gets many mentions and a quiet one few. Do that 1,000 times. On average the 49 brand-loyal accounts end up with 7.9% of the mentions, and in 95 of every 100 deals their share lands between 6.3% and 10.1%.

Their real share is 11.3%. Only 2 of the 1,000 deals reached it. In counts, about one buying-thread recommendation in nine comes from these 49 accounts, where chance gives one in thirteen. That is about 50 extra recommendations out of 1,471.

How much buying advice comes from the brand-heavy 5%

How much buying advice comes from the brand-heavy 5%

Share of brand mentions in “what should I buy” threads written by the 49 brand-loyal accounts

0%

5%

10%

15%

20%

25%

30%

35%

All six subs

11.3%

n=1471

r/knives

6.7%

n=496

r/chefknives

14.9%

n=475

r/knifeclub

12.4%

n=274

r/japaneseknives

15.2%

n=132

r/FixedBladeEdc

8.5%

n=94

Brand B001

20.4%

n=147

Brand B004

26.1%

n=115

Brand B003

31.2%

n=77

Brand B002

8.1%

n=74

expected by chance: average to 95th percentile

observed, above the 95th

n = brand mentions in buying threads by authors with 10+ comments. Brands coded; chance from 1,000 random reassignments of authors.

Where the extra share lands matters more than its size. If knife Reddit as a whole were being gamed, every subreddit would sit above chance. Two do, r/chefknives and r/knifeclub. r/knives, the largest, is within half a point of chance. A paid campaign is bought by one brand, so it should also show up brand by brand, and it does. Three brands get far more of their buying advice from the brand-loyal accounts than chance gives, one large brand gets slightly less, and three get none. That is the shape a few targeted campaigns would leave, and also the shape a few loud fan bases would leave.

Buying-thread brand mentions
Share from the 49 brand-loyal accounts
Share by chance
r/chefknives
14.9%
7.7%
r/knifeclub
12.4%
7.3%
r/knives
6.7%
6.4%
r/japaneseknives
15.2%
14.3%
r/FixedBladeEdc
8.5%
8.7%
Brand B003, a chef's-knife brand
31.2%
8.0%
Brand B004
26.1%
8.2%
Brand B001, the most-mentioned brand in r/knives
20.4%
11.8%
Brand B002
8.1%
9.5%

The brands are coded because a concentration statistic is not evidence that any brand paid for anything, and the brand with the strongest signal also has a large, loud fan base.

On corpus data, the brand-loyal accounts also match two more of the predictions above. The accounts are thin: a median of 12 comments in these six subreddits, and a median score of 1, so nobody is upvoting them into prominence. They are loyal to one brand: two thirds of each account's brand mentions go to the same brand. That is three of the six predictions, all the corpus can test. Age, knife focus and store links need each account's whole Reddit history.

## Their full Reddit histories look ordinary

I took the 23 brand-loyal accounts behind the three brands with a signal and fetched everything Reddit would return for each: up to about 2,000 comments and their submissions, account creation date and karma. For comparison, 23 other 10-plus-comment authors from the same corpus, drawn at random from the same comment-count range. Eight brand-loyal histories and seven comparison histories were hidden, suspended or deleted; the rest were readable.

Full Reddit histories: brand-loyal accounts vs comparison accounts

Full Reddit histories: brand-loyal accounts vs comparison accounts

23 brand-loyal accounts behind B001, B003 and B004, against 23 regulars drawn from the same 10-to-102 comment range

Account age (years)

0 to 8y

loyal

4.5y

control

4.5y

Comments on Reddit (up to 1,000 fetched)

0 to 2000

loyal

1250

control

1700

Subreddits commented in

0 to 140

loyal

66

control

47

Comments in the 6 knife subs (%)

0 to 40%

loyal

3.2%

control

10.3%

Knife brands named, whole history

0 to 16

loyal

7

control

12

Comments with a store link (%)

0 to 4%

loyal

0.3%

control

0.2%

Dot = median, band = middle half of accounts. 15 brand-loyal and 16 control accounts with readable histories.

No feature separates the groups at p < 0.05 (Mann-Whitney). 8 brand-loyal and 7 control profiles hide their history.

A prepared paid account should be young, post mostly in the subreddits it is paid to post in, and push one brand. The brand-loyal accounts are 4.5 years old at the median, the same as the comparison accounts. Only 3% of their comments are in the six knife subs, against 10% for the comparison group, and they spread over 66 subreddits to the comparison group's 47. Across their whole history they name seven knife brands, not one. Store links are rare in both groups.

I compared about two dozen features in all. With 15 and 16 readable accounts, none of the differences is larger than splitting 31 people into two random groups would often produce, and the ones that lean anywhere lean toward the brand-loyal accounts being less knife-focused.

That is not what a warmed, single-purpose account looks like. It is what a person who is on Reddit a lot, and who has strong feelings about one knife maker, looks like. It is also what a well-run paid account would look like, which is why the vendors sell aged accounts instead of fresh ones. The eight hidden brand-loyal histories could hold the whole story and I cannot read them.

## What this method cannot catch

The Hacker News thread on the first version of this article made five points the article had not answered. They are right about most of them, and this section answers each one.The thread is here.

* Bought aged accounts. Several commenters pointed out that old accounts with long, varied histories sell for cents in bulk. The full-history comparison above cannot tell one of those from a person. "Their histories look ordinary" rules out cheap fresh accounts and nothing more.
* Moderators. The corpus only holds comments that survived moderation. A moderator who removes criticism of one brand, or approves one seller's posts, leaves no trace in it.
* Votes. Nothing here tests upvotes. A paid comment that gets bought upvotes looks the same to this method as one that earned them.
* No known shills to test against. The method has never been run on accounts known to be paid, so nobody knows how many paid accounts it misses. The way to find out is to buy a few comments into a subreddit I run and see whether the test flags them. I have not done that.
* "None of the results are significant." That is true of the account-history comparison and not of the main result. Across all 1,471 buying-thread mentions, 2 of 1,000 random deals reached the real share. The per-brand and per-subreddit rows are many tests at once, and one or two of them could be luck.

One more correction. The practical check at the end of the first version said to click through to an unfamiliar account's history. Reddit now lets any account hide its history, and many do, so that check often shows a blank page.

## Shortcomings

* The brand detector is the stock GLiNER model, not the knife-tuned one from the earlier write-up, because that repo shipped without weights. It misses some brands and over-tags some model names. No hand-labeled check of its output on this corpus exists yet.
* "Buying thread" is a regex over titles and bodies. It has not been checked against 100 hand-labeled threads either. Both checks are cheap and I have not done them; until then every percentage above is a percentage of machine labels.
* The brand-loyal group is 49 accounts and the per-brand results rest on 15 to 20 of them. One brand-model false positive in the NER could move a per-brand row.
* I tested eight brands and six subreddits, and with that many tests one or two will look unusual by luck. The overall 11.3% result is a single test and does not have that problem.
* The comparison accounts were drawn from the brand-loyal accounts' comment-count range, not paired account by account. They have a median of 23 comments in the corpus to the brand-loyal accounts' 13, which should make them look more knife-focused, not less.
* Histories are capped at what Reddit's listing returns, around 2,000 comments. For accounts over the cap, the age at first knife comment is unknown and left blank.
* Reddit's listings stop near 1,000 posts per subreddit, so the kitchen subs cover about a year and r/knives and r/knifeclub only the weeks before the refresh. This is six subreddits, not Reddit.
* New Knife Day, which I run, tracks the same brands this corpus counts. I have no relationship with any brand in the data and no way to prove that to you.

## What I take from it

Adding "reddit" to a knife search still gets you humans, mostly. For a couple of brands, a quarter to a third of the buying advice comes from accounts that mostly recommend that brand. Whether those are fans or paid, I do not know, and after reading their histories I lean toward fans and hold the lean loosely.

The practical check is the one the data endorses: when a knife recommendation comes from an account you do not recognize, click through and see whether it has ever named a different brand. In this corpus that one question separates the brand-loyal accounts from everyone else better than karma does. It fails on a hidden history, and it will not catch the paid comment from a bought aged account. I do not think anything a reader can do will.

Code, anonymized data and charts are in the public repository linked below. Usernames, comment text, account histories and the brand-code key are not published and will not be.

## At a glance

Question
Do the knife subreddits' "what should I buy" threads show the concentration paid posting would leave behind
Approach
GLiNER brand tags over 51,129 comments from six subreddits, 1,000 random reassignments of authors to estimate chance, then full Reddit histories for 23 brand-loyal accounts and 23 comparison accounts
Result
Brand-loyal accounts write 11.3% of buying-thread brand mentions against 7.9% expected; their full histories are 4.5 years old and no more knife-focused than the comparison group's
Not shown
Payment, coordination, or which brand is B003
Analysis code, anonymized data and charts (reddit-astroturf-analysis) →
The GLiNER brand-tagging write-up →
Mike Riggs, "How the Reddit Hack Makes Google Results Better", Reason, 2022 →
New Knife Day, which tracks what knife Reddit is buying →
Personal site. Views my own; not affiliated with or endorsed by my employer.