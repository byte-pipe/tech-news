---
title: 'Thomas Wolf on X: "18 of the 20 best open models today are Mixture-of-Experts. Dense is basically over. And yet the know-how to train a good MoE still lives mostly in the heads of a handful of teams. So we spent 800k GPU hours running the experiments ourselves and wrote everything down. Super hap… / X'
url: https://x.com/thom_wolf/status/2118432475730882627
site_name: tldr
content_file: tldr-thomas-wolf-on-x-18-of-the-20-best-open-models-tod
fetched_at: '2026-11-06T12:28:41.442758'
original_url: https://x.com/thom_wolf/status/2118432475730882627
date: '2026-11-06'
published_date: '2026-11-05T19:57:15.000Z'
description: 18 of the 20 best open models today are Mixture-of-Experts. Dense is basically over. And yet the know-how to train a good MoE still lives mostly in the heads of a handful of teams. So we spent 800k GPU hours running the experiments ourselves and wrote everything down. Super happy to finally relea…
tags:
- tldr
---

## Post

Log in
Sign up

## Post

Log in
Sign up

# Thomas Wolf on X: "18 of the 20 best open models today are Mixture-of-Experts. Dense is basically over.

And yet the know-how to train a good MoE still lives mostly in the heads of a handful of teams.

So we spent 800k GPU hours running the experiments ourselves and wrote everything down. Super happy to finally release "The Ultimate MoE Training Handbook", free and open, organized around the questions training teams hit:
- how many experts, how big, shared or not?
- why is half my step spent in all-to-all, and how do I hide it?
- why is my run 25x slower with no error in the logs?
- softmax, sigmoid or sqrt(softplus) router, and why keep it in fp32?
- aux loss or DeepSeek's loss-free bias?
- upcycle a dense checkpoint or train from scratch?
- can I serve with fewer experts per token than I trained with?

⚠️ Warning: it's long (~70k words, budget a few days, sorry) but with 55 interactive figures, code you can run and numbers from our own runs.

Read it here: https://t.co/6XihlUrj92"

## Conversation

Thomas Wolf
@Thom_Wolf
18 of the 20 best open models today are Mixture-of-Experts. Dense is basically over.

And yet the know-how to train a good MoE still lives mostly in the heads of a handful of teams.

So we spent 800k GPU hours running the experiments ourselves and wrote everything down. Super happy to finally release "The Ultimate MoE Training Handbook", free and open, organized around the questions training teams hit:
- how many experts, how big, shared or not?
- why is half my step spent in all-to-all, and how do I hide it?
- why is my run 25x slower with no error in the logs?
- softmax, sigmoid or sqrt(softplus) router, and why keep it in fp32?
- aux loss or DeepSeek's loss-free bias?
- upcycle a dense checkpoint or train from scratch?
- can I serve with fewer experts per token than I trained with?

⚠️ Warning: it's long (~70k words, budget a few days, sorry) but with 55 interactive figures, code you can run and numbers from our own runs.

Read it here: 
huggingface.co/spaces/hugging…
00:00
Nouamane Tazi and 2 others
7:57 PM · Nov 5, 2026
·
56.6K
Views
56
200
1.4K
1.5K