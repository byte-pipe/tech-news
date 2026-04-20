---
title: Clawshier OpenClaw Skill - DEV Community
url: https://dev.to/fdocr/clawshier-openclaw-skill-l1n
site_name: devto
content_file: devto-clawshier-openclaw-skill-dev-community
fetched_at: '2026-04-09T19:39:27.291552'
original_url: https://dev.to/fdocr/clawshier-openclaw-skill-l1n
author: Fernando
date: '2026-04-08'
description: I've been meaning to take a stab at this idea of automating a process to take a picture of any... Tagged with ai, openclaw, opensource, openai.
tags: '#ai, #openclaw, #opensource, #openai'
---

Honest 60% success rate for receipt extraction

I've been meaning to take a stab at this idea of automating a process totake a picture of any receipt and log it to an expenses spreadsheet. Clawshier is the OpenClaw skill that came as a result. It'sopen source on GitHubandavailable in ClawHub.

## Is it any good?

Far from perfect but a fun project. Image recognition is currently the weakest link. It currently supports two providers: OpenAI (default) and Ollama.

OpenAI sometimes refuses to process the image but I simply retry after a minute and that's it. I'd say60% of the time, it works every time. Quality of extraction is quite good for establishment name, expense category recognition, totals and taxes. Thermal receipt pictures with poor lighting can be very tricky, on top of cryptic text/acronyms in them. I traced the image recognition step to take between 5 and 12 seconds which is good.

For Ollama I triedllama3.2-vision:11bdue to my available memory (fits in my 16GB RAM), but sadly was unusable. Infinite loops (extracting one line thousands of times), hallucinations and taking too long to process. 5 minute timeouts sometimes worked but essentially a coin toss whether it would extract "something" or simply hang/crash.

I ran benchmarks and I had to downsize the image to 512px to consistently avoid those timeouts, but that degraded the image too much for it to be usable. Perhaps thellama3.2-vision:90bwould perform better... Wish I had a Ryzen Strix Halo with that juicy RAM.

## What does it look like?

Send your bot a picture of any receipt. There's currently an issue with dates because receipts I deal with sometimes have DD-MM and MM-DD dates so image extraction sometimes mixes them up. The current workaround is to specify the date, but it's likely not an issue if you only deal with MM-DD-YYYY dates.

Then the spreadsheets are updated with the new expense record. A few different sheets are created/updated automatically with each pipeline execution:

* SummaryAggregated totals and charts
* Aggregated totals and charts
* Invoice Archive BreakdownBreakdown of each invoiceCurrently very flaky data from image recognition since these are the individual line items that are tricky to read/decode even for humans
* Breakdown of each invoice
* Currently very flaky data from image recognition since these are the individual line items that are tricky to read/decode even for humans
* Monthly expense sheetExpenses aggregated in their corresponding MM-YY date sheet
* Expenses aggregated in their corresponding MM-YY date sheet

## Conclusions

Now I'm the guy taking a picture of his receipts everywhere I go. Not a huge fan of sending these to OpenAI and would wish I could do more of this using local models, but it might help me track my "small expenses" which I struggle to keep a close eye on.

Also worth noting I'm not a huge fan of the DX for OpenClaw skills either, it was painful at times... I hope it's not a "skill issue" 🥁

In terms of usage I'm expecting a couple dollars worth of OpenAI credits per month, we'll see how it goes. Again local models would be able to reduce this substantially since image recognition takes up the bulk of the processing.

There's plenty of ways this could be improved (i.e. PaddleOCR/Tesserect which would also avoid sending my pics to Sam). If Clawshier sounds interesting to you take a peek at theGitHub repo. Pura Vida!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
