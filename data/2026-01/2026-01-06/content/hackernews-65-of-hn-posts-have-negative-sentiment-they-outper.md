---
title: 65% of HN Posts Have Negative Sentiment, They Outperform - philippdubach.com
url: https://philippdubach.com/standalone/hn-sentiment/
site_name: hackernews
fetched_at: '2026-01-06T19:07:02.649640'
original_url: https://philippdubach.com/standalone/hn-sentiment/
author: Philipp D. Dubach
date: '2026-01-06'
published_date: '2026-01-06T00:00:00Z'
description: Analysis of 32,000 HN posts and 340K comments reveals negativity bias correlates with higher engagement. Data, methodology, and full paper available.
---

Posts with negative sentiment average 35.6 points onHacker News. The overall average is 28 points. That’s a 27% performance premium for negativity.This finding comes from an empirical study I’ve been running on HN attention dynamics, covering decay curves, preferential attachment, survival probability, and early-engagement prediction. The preprint isavailable on SSRN. I already had a gut feeling. Across 32,000 posts and 340,000 comments, nearly 65% register as negative. This might be a feature of my classifier being miscalibrated toward negativity; yet the pattern holds across six different models.I tested three transformer-based classifiers (DistilBERT, BERT Multi, RoBERTa) and three LLMs (Llama 3.1 8B, Mistral 3.1 24B, Gemma 3 12B). The distributions vary, but the negative skew persists across all of them (inverted scale for 2-6). The results I use in my dashboard are from DistilBERT because it runs efficiently in my Cloudflare-based pipeline.

What counts as “negative” here? Criticism of technology, skepticism toward announcements, complaints about industry practices, frustration with APIs. The usual. It’s worth noting that technical critique reads differently than personal attacks; most HN negativity is substantive rather than toxic. But, does negativity cause engagement, or does controversial content attract both negative framing and attention? Probably some of both.

I’ll publish the full code, dataset, and a dashboard for the HN archiver soon and I’m happy to send you an update:

Alternatively, you can also subscribe to theRSS feedor get updates onBluesky.
