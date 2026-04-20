---
title: Claude mixes up who said what, and that's not OK
url: https://dwyer.co.za/static/claude-mixes-up-who-said-what-and-thats-not-ok.html
site_name: hackernews_api
content_file: hackernews_api-claude-mixes-up-who-said-what-and-thats-not-ok
fetched_at: '2026-04-10T06:00:18.810236'
original_url: https://dwyer.co.za/static/claude-mixes-up-who-said-what-and-thats-not-ok.html
author: sixhobbits
date: '2026-04-09'
description: Claude sometimes sends messages to itself and then thinks those messages come from the user. This is categorically distinct from hallucinations or missing permissions.
tags:
- hackernews
- trending
---

## The bug

Claude sometimes sends messages to itself and then thinks those messages came from the user. This is the worst bug I’ve seen from an LLM provider, but people always misunderstand what’s happening and blame LLMs, hallucinations, or lack of permission boundaries. Those are related issues, but this ‘who said what’ bug is categorically distinct.

I wrote about this in detail inThe worst bug I’ve seen so far in Claude Code, where I showed two examples of Claude giving itself instructions and then believing those instructions came from me.

Claude told itself my typos were intentional and deployed anyway, then insisted I was the one who said it.

## It’s not just me

Here’sa Reddit threadwhere Claude said “Tear down the H100 too”, and then claimed that the user had given that instruction.

From r/Anthropic — Claude gives itself a destructive instruction and blames the user.

## “You shouldn’t give it that much access”

Comments onmy previous postwere things like “It should help you use more discipline in your DevOps.” And on the Reddit thread, many in the class of “don’t give it nearly this much access to a production environment, especially if there’s data you want to keep.”

This isn’t the point. Yes, of course AI has risks and can behave unpredictably, but after using it for months you get a ‘feel’ for what kind of mistakes it makes, when to watch it more closely, when to give it more permissions or a longer leash.

This class of bug seems to be in the harness, not in the model itself. It’s somehow labelling internal reasoning messages as coming from the user, which is why the model is so confident that “No, you said that.”

Before, I thought it was a temporary thing — I saw it a few times in a single day, and then not again for months. But either they have a regression or it was a coincidence and it just pops up every so often, and people only notice when it gives itself permission to do something bad.

## Update

This article reached #1 onHacker News, and it seems that this is definitely a widespread issue. Here’s another super clear example shared bynathell(full transcript).

From nathell — Claude asks itself “Shall I commit this progress?” and treats it as user approval.

Several people questioned whether this is actually a harness bug like I assumed, as people have reported similar issues using other interfaces and models, including chatgpt.com. One pattern does seem to be that it happens in the so-called “Dumb Zone” once a conversation starts approaching the limits of the context window.
