---
title: Data on AI-related Show HN posts
url: https://ryanfarley.co/ai-show-hn-data/
site_name: hackernews
fetched_at: '2025-07-07T10:21:07.719302'
original_url: https://ryanfarley.co/ai-show-hn-data/
author: rfarley04
date: '2025-07-07'
---

Back to home

## More than 1 in 5 Show HN posts are now AI-related, but get less than half the votes or comments._

The idea for this article didn't exist in my brain before this morning. But there I was, scrolling the New page and even more tired of all the AI-related Show HN posts than usual. I was confident that their numbers were multiplying and wanted proof. Exactly how much more AI crap is on my lawn compared to last year?

Full disclosure: I'm not a data guy. Everything below was off the top of my head. Not carefully structured or considered. I was grumpy, caffeinated, and avoiding work. I would love nothing more than for someone to show me some dumb error in my SQL queries that makes everything below meaningless.

I am NOT interested in debating the value of AI (LLMs, whatever). Mainly because I don't hate it/them nearly as much as this post suggests! I used Cursor + Claude to create the Chartjs visualizations in this article, dammit. What I hate is that a Show HN post used to represent someone's hard work or passion project. And that 100% justified the self-promotion IMO.

But since the introduction of coding chatbots, the New page has increasingly felt like an avalanche of low-effort crap. Make all of the "Chat with a PDF" nonsense you want, seriously! Just don't post it to HN.

With that out of the way, I used theHacker News BigQuery datasetand some basic SQL queries to answer a few straightforward questions.

## Is the number of Show HN posts increasing?

This is the broadest and least specific indicator of how coding chatbots have affected the frequency of Show HN posts. Coding bot make coding easy so number go up? Yes, the total number of Show HN posts looks to be trending upwards.

Here is the SQL query I ran:

SELECT
 EXTRACT(YEAR FROM DATETIME(TIMESTAMP_SECONDS(time))) AS year,
 COUNT(*) AS post_count,
 AVG(score) AS avg_score,
 AVG(descendants) AS avg_comments
FROM `bigquery-public-data.hacker_news.full`
WHERE
 type = 'story'
 AND REGEXP_CONTAINS(title, r'^Show HN:')
 AND time >= UNIX_SECONDS(TIMESTAMP(DATE_SUB(CURRENT_DATE(), INTERVAL 8 YEAR)))
 AND deleted IS NULL
GROUP BY year
ORDER BY year DESC


And here is the output as of 10am Bangkok time on July 3, 2025:

Year

# of Show HN posts

2025
12,500 (so far)

2024
17,618

2023
14,062

2022
10,076

2021
12,644

2020
16,899

2019
5,831

2018
11,130

2017
5,526

Obviously, the 2025 data only represents 50.41% of the year. If we estimate the number of Show HN posts for the rest of 2025 (12,500*.9837), the graph looks like this:

A steeper trendline, sure. But I would have expected a bigger difference between 2018 (11,130 posts) and 2023 (14,062).

What's more, 2020, likely because of COVID externalities, had more posts (16,899) than 2023 (14,062) and almost as many as 2024 (17,618).

So I guess 2024 didn't feel like enough of a deluge for me to check the numbers and 2025 did. Maybe it wasn't the double shot. Maybe it's gotten worse very recently.

## What % of Show HN posts mention AI?

At this point, I have to confront precisely what is bothering me about the perceived flood of Show HN posts. The core of the issue, to me, is that self-promotion without some sort of filtering function (i.e. having a working tool no longer infers significant labor and effort) is bad.

I am open to the idea of someone building a novel/interesting ChatGPT wrapper that required "real" work (i.e. without AI-generated code). But that's hard to judge from a Show HN post, so generalizing is the best I can do.

I am going out on a limb and assuming that Show HN posts with ' AI ', ' A.I. ', or 'GPT' in the title, as well as those with '.ai' or 'gpt' in the URL were built with less human elbow grease than those that do not include those keywords. Here is the SQL query that I used:

SELECT
 EXTRACT(YEAR FROM DATETIME(TIMESTAMP_SECONDS(time))) as year,
 COUNT(*) as ai_post_count,
 AVG(score) as avg_score,
 AVG(descendants) as avg_comments
FROM `bigquery-public-data.hacker_news.full`
WHERE
 type = 'story'
 AND REGEXP_CONTAINS(title, r'^Show HN:')
 AND (
 REGEXP_CONTAINS(UPPER(title), r'\bAI\b')
 OR REGEXP_CONTAINS(UPPER(title), r'\bA\.I\.\b')
 OR REGEXP_CONTAINS(UPPER(title), r'\bGPT\b')
 OR REGEXP_CONTAINS(LOWER(url), r'\.ai/')
 OR REGEXP_CONTAINS(LOWER(url), r'\.ai$')
 OR REGEXP_CONTAINS(UPPER(url), r'\bGPT\b')
 )
AND time >= UNIX_SECONDS(TIMESTAMP(DATE_SUB(CURRENT_DATE(), INTERVAL 8 YEAR)))
 AND deleted IS NULL
GROUP BY year
ORDER BY year DESC


I am Jack's total lack of surprise:

Mmmm it feels so good to justify one's own arguments.

Want more? Here is perhaps the best visualization of what's annoying me: a graph of [# of AI Show HN posts] / [total Show HN posts]:

This is not, as I have labeled it, a flood, deluge, or avalanche. It's an earthquake. A rupture. Quiet in 2022, five-alarm fire in 2023.

In 2018, one out of every 63 Show HN posts was AI-related. In 2025, it's shaping up to be more than one out of every 4.6. Nggghhhh.

But how does the community feel? Maybe there is a large cohort of HN users who want the AIs stomping all over their grass.

## Are Show HN posts getting fewer votes?

This question is fraught with all sorts of blind spots. I'm not aware of any public data about the number of registered users on Hacker News, which means we don't know the number of upvotes relative to total user base or monthly active users. And, there doesn't seem to be any data on downvotes.

So, if Show HN posts are getting more points on average, that could mean that they're generally more popular than before OR that they're getting more downvotes than before while still netting higher scores thanks to an influx of new, pro-AI HN accounts. Or something else entirely. The caffeine is wearing off, so I'm just going to forge ahead with incomplete data.

Points for all Show HN posts were somewhat flat until 2022, when they spiked before declining back to 2017 levels.

Show HN posts with AI/GPT in the title/URL followed a very similar path but consistently scored lower than titles that do not include AI. Except 2017, which seems to be the year the.ai TLD went commercial. Until someone pokes holes in any of this, I still look to be justified in my annoyance. Huzzah!

## Do AI Show HN posts get more comments?

Average number of comments are even more fraught with ambiguity than net total points, but what the hell:

The picture here is similar to net total points. AI-related Show HN posts get fewer comments, on average. No flamewars, basically. Both categories jumped up in 2022, and declined every year after. There are a couple of small differences compared to net total points data, though:

* Unlike points, 2017 AI Show HN posts did worse than regular posts, in terms of comments
* 2020 AI posts generated more discussion than non AI-posts
* 2022 AI posts had fewer comments than non-AI posts
* Both AI and non-AI posts in 2024/2025 seem to be consistently below 2017/2018 baseline.

Basically, AI-related posts have been consistently less chatty since ChatGPT.

## tl;dr More AI Show HN posts, fewer votes and comments

The data isn't surprising and it certainly isn't perfect. There are Show HN posts included in these counts that contain AI or GPT keywords but are actually anti-AI. The converse is likely true, however.

Should anything change? I don't know. Doesn't seem like scrapping Show HN solves much of anything. Banning or limiting AI-related promotion doesn't really get to the root of the issue IMO. At the end of the day, it's just a thing that annoys me. And having data to point to makes me feel a little less crazy. That helps, somewhat.
