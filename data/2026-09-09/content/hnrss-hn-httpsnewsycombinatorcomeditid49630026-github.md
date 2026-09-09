---
title: 'HN: https://news.ycombinator.com/edit?id=49630026 · GitHub'
url: https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3
site_name: hnrss
content_file: hnrss-hn-httpsnewsycombinatorcomeditid49630026-github
fetched_at: '2026-09-09T21:31:01.946898'
original_url: https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3
date: '2026-09-09'
description: 'HN: https://news.ycombinator.com/edit?id=49630026. GitHub Gist: instantly share code, notes, and snippets.'
tags:
- hackernews
- hnrss
---

Instantly share code, notes, and snippets.

# wsxiaoys/reasoning-prefill-1-1.mdSecret

 Last active
 
September 9, 2026 19:28

 

Show Gist options

 

* Download ZIP

 

 

* Star3(3)You must be signed in to star a gist
* Fork0(0)You must be signed in to fork a gist

* Embed# Select an optionEmbedEmbed this gist in your website.ShareCopy sharable link for this gist.Clone via HTTPSClone using the web URL.## No results foundLearn more about clone URLsClone this repository at &lt;script src=&quot;https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3.js&quot;&gt;&lt;/script&gt;
* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.
* Save wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3 to your computer and use it in GitHub Desktop.

 

Embed

# Select an option

 

* EmbedEmbed this gist in your website.
* ShareCopy sharable link for this gist.
* Clone via HTTPSClone using the web URL.

## No results found

 

 
 
Learn more about clone URLs

 

 

 Clone this repository at &lt;script src=&quot;https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3.js&quot;&gt;&lt;/script&gt;

 

 

Save wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3 to your computer and use it in GitHub Desktop.

Download ZIP

 HN: 
https://news.ycombinator.com/edit?id=49630026

 

Raw

 reasoning-prefill-1-1.md
 

# Reasoning prefills on a few open models, v1.1

A follow-up toReasoning prefills on a few open modelsandStolen Thoughts

This v1.1 reruns the reasoning-prefill experiment with GPT-5.5 Pro as the teacher.

For each problem, I generated two responses from each target model:

1. an ordinary, unprefilled response; and
2. a response starting with the first 1% of GPT-5.5 Pro's reasoning, inserted into the target model's reasoning channel.

The visible answer remained freely generated. I then measured how much of the teacher's visible answer appeared in the first 100 tokens of the target model's answer. As in the previous post, each score is the mean of unigram, bigram, and trigram source recall. Deltas are absolute percentage-point changes.

## All problems

The evaluation contains 45 problems: 15 STEM, 15 non-STEM, and 15 synthetic puzzles.

Model

n

Unprefilled

GPT-5.5 Pro reasoning prefill

Delta

DeepSeek V4 Flash

45

27.30%

26.13%

−1.17 pp

Inkling

45

19.99%

20.45%

+0.46 pp

Kimi K3

45

31.11%

35.65%

+4.54 pp

Qwen3.8 A95B

45

16.79%

34.97%

+18.18 pp

## Qwen by category

Category

n

Unprefilled

GPT-5.5 Pro reasoning prefill

Delta

STEM

15

19.26%

46.24%

+26.99 pp

Non-STEM

15

20.62%

33.42%

+12.80 pp

Puzzle

15

10.49%

25.23%

+14.75 pp

All

45

16.79%

34.97%

+18.18 pp

## Discussion

Qwen barely moved toward Opus 4.8 in the earlier experiment, but moved by +18.18 points toward GPT-5.5 Pro here, including a large effect on the private synthetic puzzles. The data suggest that Qwen may have learned from GPT-5.5 Pro, or from a closely related GPT model, rather than from Opus.

Kimi K3 has the highest overlap with GPT-5.5 Pro both without and with the prefill (31.11% and 35.65%), although the prefill adds only +4.54 points.

Sign up for free

to join this conversation on GitHub
.
 Already have an account?
 
Sign in to comment