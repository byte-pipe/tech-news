---
title: 'Content Effort: The Google Ranking Feature Nobody Talks About'
url: https://signal.zyppy.com/p/content-effort
site_name: tldr
content_file: tldr-content-effort-the-google-ranking-feature-nobody-t
fetched_at: '2026-08-18T19:26:13.067691'
original_url: https://signal.zyppy.com/p/content-effort
author: Cyrus Shepard
date: '2026-08-18'
description: Google doesn't care about how hard you worked - it's about showing evidence of unique value
tags:
- tldr
---

# Content Effort: The Google Ranking Feature Nobody Talks About

### Effort isn't how hard you worked - Google cares about evidence of unique value

Cyrus Shepard
Aug 13, 2026
9
1
Share

👋 Subscribe free (it helps me produce research like this) and get the7-Step AI Citation Checklistwith tips + tactics on how to win more SEO/AI visibility.

Subscribe

When I worked asa Google Quality Rater, we were required to evaluate every webpage we scored oneffort, alongside originality, talent/skill, and accuracy.

What exactly is “effort”,andwhy is it so important?

Google’s definition isn’t what you think it is.

Effort ≠ work.

For the uninitiated, it may seem strange for Google to evaluate pages on subjective factors like effort and talent.How can Google possibly know how much effort you put into a page?

In truth, they don’t.

But they can very easilyestimate it—and with a high degree of accuracy—based on strict standards and theevidence visible on your page. Google can draw on thousands of human-rated documents, machine-learning trained at scale, and now AI to assess the “quality” signals of virtually any webpage you publish.

And over the past ~20 years, they’ve gottenvery, very good at it.

SEO tools typically focus on things likekeywordsandtopical relevance, but there’s a strong case that “subjective” features—such as effort—are equally, and possibly more, important in Google’s eyes.

In the age of low-effort,scaled AI contentgetting algorithmically decimated,understanding “high-effort” is increasingly relevant to brands.

Graphic by Shepard Design

Here’s how Google defines “effort” in its Quality Rater Guidelines.

Effort:Consider the extent to which a human being actively worked to create satisfying content. Effort may be direct, such as a person translating a poem from one language to another. Effort may go into designing page functionality or building systems that power a webpage, such as the creation of a page that offers machine translation as a service to users. On the other hand, the automatic creation of thousands of pages by running existing freely available content through existing translation software without any oversight, manual curation, etc., would not be considered to have effort.

The Rater Guidelines then go on to give exhaustive examples of both high and low-effort webpages.Effort is mentioned over 100 times.

Most interestingly, theGoogle API leakexposed two data points that specifically reference Effort scoring.

* contentEffort- LLM-based effort estimation for article pages
* ugcDiscussionEffortScore- UGC page quality signals.

To be fair, we don’t know how (or even if) Google uses these metrics. But it’s obvious from documentation, public statements, and data leaks that Google spends a lot of time thinking about, evaluating, and scoring content effort.

Understanding how Googleevaluateseffort can help us produce content with a better chance of ranking highly.

### SEO Nerd Section (feel free to skip)

In theGoogle API leak, bothcontentEffortandugcDiscussionEffortScoresit inside thecompressedQualitySignalsstructure, which are page-specific signals that “can be used in preliminary scoring.”

This structure contains other seemingly important fields such aslowQualityandsiteAuthority, among others.

The docs indicate thatcontentEffortis produced by an LLM, which may be separate from the quality scoring performed by Quality Raters. Finally,contentEffortis defined as afloating-point number, which indicates an actual numeric score.

Finally, it’s important to note that Google almost always mentions Effort in the same context as Originality and Talent/Skill. These concepts overlap heavily in the Quality Rater Guidelines.

## How Google Defines “Effort”

Before we understand what effort is, it’s important to know what itisn’t. Effort is not:

* Word count
* Time spent creating page
* Human-written content > AI

The key is this:effort is not how much work you actually put into a page. It’s more about theevidence of useful workthatends up on the final page.

So what kind of on-page evidence does Google look for? I’ve classified all the instructions and examples from Google’s guidance into 7 signals of “effort”.

### 1. Curation and Editing

A low-effort page is a collection of information with little human involvement. A high-effort page means a human carefully chose (curated) what information was important and organized it in a way that was useful.

Low-effort curation: A large collection of chicken recipes scraped from other sites.

High-effort curation: A collection of chicken recipes personally tested by the author, organized by popularity and taste.

### 2. Low-Quality Automation vs Added Value

Using AI (or any other form of automation) to help generate content isn’t necessarily bad. That said, when it’s done at scale to create content withlittle added valuecompared to other content, that’s a recipe for disaster.

High-effort pages typically contain at least some elements that AI or automation can’t easily replicate, such as:

* Information fromproprietary databases(e.g., product catalog)
* Humanevaluationand perspectives
* High-qualityuser-generated content
* Uniqueimagesand other media
* Authenticuser reviews

The key point here is not to punish automation, but to identify thevalue-add. High-effort pages must addvaluethat’s not easily automated.

Low-effort automation: 5,000 location pages generated from the same template with city names swapped in.

High-effort automation: Automated movie recommendation pages generated withreal user reviewsfrom an owned app, along withproprietary real-time ticket data.

### 3. Recycles Information vs Original Facts and Perspectives

Google’s move toward“non-commodity” contentrepresents one of the most significant algorithmic shifts we’ve seen in years.

To put it simply:low-effort contentuses the same facts and information that can be found elsewhere on the web. It’s the type of content most easily reproduced by anyone with access to AI, Google, and Wikipedia. Low-effort pagessummarize what others say with commonly known facts.

High-effort content, on the other hand, containsoriginal facts(gained through your own experience) anduniqueperspectives/opinions. This is also known asfirst-party information, as the value of the content comes from the creator of the webpage.

High-effort pages often containunique factsgainedthrough first-hand experience.

### Recycled Media vs High-Effort Media

Importantly,images and videocount as content too.

Recycled images and videos “borrowed” from other sites, and/or stock images and video, can be considered low-effort. This applies to images or videos that have been slightly altered.

High-effort media includesdetailed, high-quality photographyand original video. High-quality photography doesn’t gaurentee high rankings, but it does show you put the work in.

Low-effort information: A page titled “10 Best Protein Powders” describes 10 popular powders without any original research or testing.

High-effort information: A similar page titled “10 Best Protein Powders We’ve Tested” describes the user’s experience, testing methods, experiment results, opinions, and richly detailed photos of each product.

### 4. Filler content vs. Prominent Helpful Content

Here’s how Google defines “filler”:

…low-effort content that adds little value and doesn’t directly support the purpose of the page. Filler can artificially inflate content, creating a page that appears rich but lacks content website visitors find valuable.

SEOs used to (and sometimes still do) try to improve their keyword “relevance” by writing paragraphs of keyword-rich text that targetedtopical authoritybutcontained little original information.

Even worse is when this filler content sits at the top of the page in order to increase ad views or time-on-site.

High-effort content, in contrast, places the most useful, unique information prominentlywhere it can quickly solve a user’s problem.

Low-effort filler: A page titled “How to boil an egg?” begins with 600 words about the history and nutritional value of eggs.

High-effort content: A similar page titled “How To Boil An Egg Perfectly Every Time” gives important facts up-front, followed by useful supplementary information such as egg size, altitude adjustments, and yolk firmness.

### 5. Shallow Discussion vs. Quality Discussion

“Discussion” is an interesting angle for Google to evaluate because it seems Google wants to reward pages that go beyond merely presenting facts - Google wants people’sperspectiveon things.

High-effort discussion means evidence is carefully considered, and anopinion—or judgment—is rendered based on that evidence.

Interestingly, Google seems to evaluate effort differently based on the type of page, specifically if the page is User Generated Content (UGC). From the Rater Guidelines:

For pages like social media posts or forum discussions, the level of participation and depth of conversation is an important part of effort. Contributions from multiple individuals on such pages can add up to a significant amount of total human effort.

Low-effort discussion: A Reddit post titled “Anyone else allergic to butter?” gets a single reply: “Yep, me”

High-effort discussion: A page title “Best Hiking Boots for Women” describes features and experiences from wearing each boot, along within-depth perspectives and opinionswhich inform the final recommendations.

👋 Subscribe free (it helps me produce research like this) and get tips + tactics on how to win more SEO and AI visibility.

Subscribe

## How to Create High-Effort Pages: Two-Minute Audit

At the risk of repeating myself: effortis not how much work you put into content creation, but theon-page evidencethat you created satisfying, unique content.

Before creating or publishing content, perform the following checks:

1. Is the content edited and curated thoughtfully?

Is the content organized around the user’s goal, with the most valuable content easy to find?

2. Did you add something unique that doesn’t exist elsewhere?

First-party informationis critical. This can include original data, facts, observations, and even opinions and perspectives.

3. Does the content show evidence of work?

Explaining your methodology, high-quality photos, screenshots, interviews, and observationsall provide evidence that you actually have experience.

4. Does the content go beyond common facts?

If someone else could easily reproduce your content simply by researching the internet, it’s likely considered low-effort. Explaindetailsoredge casesif you need to dive deeper into a subject matter.

5. Does the content provide deep discussion?

To be clear, not every webpage requires discussion (e.g., current stock prices), but for many topics,personal perspectivesthat explore evidence and offer carefully crafted perspectives can elevate content to “high-effort.”

## Paid subscriber bonus: Content Effort Audit

I built a quick scoring system based on the effort signals covered above. You can use it to score a page from 0–100, identify any “effort” gaps, and get ideas for what to add.

It also includes 50+ examples of visible evidence of effort and playbooks for reviews, how-tos, travel, research, ecommerce, local pages, and more. You can find it inPro Templates.

9
1
Share
Previous