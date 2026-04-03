---
title: I used o3 to profile myself from my saved Pocket links | noperator
url: https://noperator.dev/posts/o3-pocket-profile/
site_name: hackernews_api
fetched_at: '2025-07-09T01:05:39.767417'
original_url: https://noperator.dev/posts/o3-pocket-profile/
date: '2025-07-07'
published_date: '2025-07-07T00:00:00+00:00'
description: 'Welp, Pocket shuts down tomorrow despite our pleas for it to stay. While migrating1 all of my saved articles, I noticed that I’ve got almost 900 saved articles spanning nearly 7 years. That’s a goldmine of stuff-I-like data! Some quick analysis using xsv2: 𝄢 unzip pocket.zip && xsv headers part_000000.csv 1 title 2 url 3 time_added 4 tags 5 status 𝄢 xsv sample 1 part_000000.csv | xsv flatten title The Uncertain Future of American Libraries url https://mek.'
tags:
- hackernews
- trending
---

Welp, Pocketshuts down tomorrowdespite ourpleasfor it to stay. While migrating1all of my saved articles, I noticed that I’ve got almost 900 saved articles spanning nearly 7 years. That’s a goldmine of stuff-I-like data! Some quick analysis using xsv2:

𝄢 unzip pocket.zip && xsv headers part_000000.csv

1 title

2 url

3 time_added

4 tags

5 status

𝄢 xsv sample 1 part_000000.csv | xsv flatten

title The Uncertain Future of American Libraries

url https://mek.fyi/posts/the-uncertain-future-of-american-libraries

time_added 1678243022

tags

status unread

𝄢 xsv count part_000000.csv

878

𝄢 xsv select time_added part_000000.csv |

 xsv stats | xsv select min,max | xsv flatten |

 while read header value; do

 echo -n "$header "

 date -I -d "@$value"

 done

min 2018-07-12

max 2025-06-26

### Experiment#

Recalling Simon Willison’s recentgeoguessing challengefor o3, I considered, “What might o3 be able to tell me about myself, simply based on a list of URLs I’ve chosen to save?” I opened a temporary chat with o3 (doesn’t use ChatGPT’s memory feature) and prompted:

I’m going to share a list of articles that I’ve saved to Pocket, a read-it-later app. I want you to use that information to “profile” me. Tell me everything about myself that you can possibly infer from this data set. Here’s an example of possible dimensions of that profile, but feel free to include other things that you can infer: age, sex, geographic location, education level, industry/field of work, job level/seniority, income bracket, political orientation, risk tolerance, learning style, information diet, relationship status, parental status and kids’ ages, health concerns, major life transitions, seasonal patterns in interests, etc.

### Results#

o3’s response in full3:

Thought for 13 seconds

* The user has shared a broad range of article preferences, which could actually give me some good insight into their demographic and interests. Technical articles related to software, AI, cybersecurity, and finance suggest strong analytical and professional interests. The content about family life, homeschooling, and Catholic practices points to someone who’s likely a parent, possibly with a strong focus on family values. It makes sense to assume they might be male, based on the profiles aggregating to this, but I’m not completely sure yet. I’ll keep this in mind!
* I’m pulling together some details! The user’s mix of technical articles and Catholic family topics suggests they could either be a father interested in homemaking or a female parent with a tech background. Their location seems to be coastal VA, based on property listings, and their age looks to be around 30-40. With a career in software engineering, likely at a senior level, their income probably exceeds 150k. They seem to have a self-directed learning style and a moderate to high risk tolerance in investments. They’re likely married with multiple young kids.

Below is a “best-guess” portrait distilled from the themes, sources, and timing of the articles you save. None of these inferences is certain, but together they form a coherent narrative.

Core demographics

Dimension

Likely inference

Key signals

Age

Mid-30s to early-40s

Staff-level career content, FIRE math, parenting toddlers

Sex

Male

Strong focus on engineering / hacking culture + “dad”-oriented parenting pieces

Location

Coastal VA

Repeated local property links and local-news saves

Education

BS/MS in Computer Science or similar

Deep dive security/AI papers, Unix history, academic PDFs

Industry & Role

Senior/staff software engineer – specializing in security & infra

PortSwigger, fuzzing, exploit-dev, “Ways Staff Engineers Get Stuck”, Honeycomb career ladders

Income bracket

~$150-220 k household

Salary-band posts, six-figure FIRE calcs, high-earner tax strategies

Relationship & family

Married, 3-4 young kids (incl. at least one toddler)

Twin-mom sleep articles, Catholic “family table”, homeschooling & microschools pieces

Mindset & preferences

Dimension

Inference

Rationale

Politics

Fiscally conservative / civil-libertarian with traditionalist social leanings

Bogleheads & MMM frugality + Catholic/First Things pieces, EFF privacy, skepticism of Big Tech censorship

Risk tolerance

Career:
 high (security research, side projects)
Financial:
 moderate (indexing, 4 % rule, self-sufficiency)

Mix of daring technical reading and ultra-conservative portfolio design

Learning style

Self-directed, text-heavy, long-form + auditory

Uses Pocket/RSS, collects PDFs, long podcasts & conference talks at 1×

Information diet

60 % deep-tech, 20 % personal finance/FIRE, 10 % parenting/homemaking, 10 % faith & culture

Counts of saved links across themes

Major life arc

Phase shift
: from pure IC hacker → technical leadership & family-centric life, aiming for FI

Saves on management paths, burnout, early-retirement reflections

Seasonal spikes

Late Dec–Jan: career-planning & goal-setting; May–Aug: homeschooling, beach/sea-level, property; Sep–Oct: security-conference binge (DEF CON, Black Hat)

Timestamp clusters in list

Subtler clues

* Faith:Regular saves from Catholic & conservative Christian sites suggest active practice.
* Privacy/Self-hosting streak:Mail-in-a-box, “thrown in the towel on self-hosted email” links → you experiment, then pragmatically revert.
* Maker tendencies:Woodworking workbench plans, PVC-pipe acoustics, E-ink DIY frames — you like hands-on projects that complement screen work.
* Health:Zone-2 training, sleep hacks, Huberman podcasts — pragmatic bio-optimization, not fad-chasing.
* Writing impulse:Many “write more”, “blogging for the hell of it”, “personal branding” saves hint you intend to publish more of your own thinking.

Quick “user manual” for you

* Motivators:Autonomy, mastery, frugality, family time, living your faith.
* Blind spots:Can slip into infinite-research mode (huge unread queue); be mindful of analysis-paralysis.
* Best mediums:Long-form articles + podcasts during commutes/chores; interactive docs for code.
* Big goals on deck:Finish FIRE plan, ship a public-facing security tool, formalize homeschool curriculum, and blog consistently.

Take what resonates and discard the rest—but if it feels eerily accurate, that’s because your bookmarks tell quite a story.

### Reaction#

Yeah, pretty accurate. Perhaps even eerily so. Upon first reading, I was surprised when it nailed age range, location, family size, etc.—details that I didn’t expect to be represented in a data set that I thought mostly consisted of Hacker News posts. Shows you how much can be inferred by a simple trail of “likes.”

Worth noting that o3 tended to perform better (i.e., the response felt more accurate) when I copypasted the CSV data directly into the prompt body. Sending the CSV as a file attachment caused o3 to get too fixated on using Python to sample and analyze the CSV data rather than simply “taking it all in,” and in my experience yielded a less compelling narrative at the end.

### Implications#

Is there a lesson here? We already know that advertising companies profile us based on expressed interests, but up until recently it felt like only Google or Facebook had access to analysis capabilities strong enough to draw meaningful conclusions from disparate data points. I’d agree with Simon that the more interesting takeaway is “the fact that this technology is openly available to almost anyone.”

Case in point: I’ll be using this profile to power apersonal content recommendation system.

1. I’ve moved over toWallabag, and also took the opportunity to switch from Inoreader toFreshRSS. Happy with both. Self-hosting these services is much easier now in 2025 compared to my last self-hosting initiative years ago;Caddyhas been a huge part of that.↩︎
2. xsvhas been hands-down my favorite way to quickly explore CSV data. Looks like it’s no longer maintained as of 2 months ago, but it feels pretty feature-complete.↩︎
3. I mean, mostly intact. Did you really expect me to leave in the part about “dandruff remedies”?↩︎
