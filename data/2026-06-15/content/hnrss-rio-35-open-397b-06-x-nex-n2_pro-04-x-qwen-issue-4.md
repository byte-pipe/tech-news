---
title: 'Rio-3.5-Open-397B ≈ 0.6 x Nex-N2_pro + 0.4 x Qwen · Issue #4 · nex-agi/Nex-N2 · GitHub'
url: https://github.com/nex-agi/Nex-N2/issues/4
site_name: hnrss
content_file: hnrss-rio-35-open-397b-06-x-nex-n2_pro-04-x-qwen-issue-4
fetched_at: '2026-06-15T06:00:35.555368'
original_url: https://github.com/nex-agi/Nex-N2/issues/4
date: '2026-06-14'
description: prefeitura-rio/Rio-3.5-Open-397B is presented as an original 397B model trained by IplanRIO. It is not. Its weights are a direct element-wise merge of our model, Nex, with the official Qwen3.5-397B-A17B base — about 0.6 Nex / 0.4 Qwen — ...
tags:
- hackernews
- hnrss
---

nex-agi

 

/

Nex-N2

Public

* NotificationsYou must be signed in to change notification settings
* Fork12
* Star170

# Rio-3.5-Open-397B ≈ 0.6 x Nex-N2_pro + 0.4 x Qwen#4

Open
Open
Rio-3.5-Open-397B ≈ 0.6 x Nex-N2_pro + 0.4 x Qwen
#4

## Description

00INDEX
opened 
on 
Jun 14, 2026
Issue body actions

prefeitura-rio/Rio-3.5-Open-397Bis presented as an original 397B model trained byIplanRIO. It is not. Its weights are adirect element-wise merge of our model, Nex, with the officialQwen3.5-397B-A17Bbase— about0.6 Nex / 0.4 Qwen— and we findno evidence of any training of their own.We can show thistwo completely independent ways:

1. With Rio's hard-coded "You are Rio" system prompt removed, its own deployed model identifies itself as "Nex, from Nex-AGI" 79% of the time — and as "Rio" 0% of the time.It even recites our organization's bespoke backstory word-for-word.
2. Every weight tensor in Rio is, to thousands of standard deviations, the same 0.6/0.4 blend of Nex and Qwen— across all 60 layers and every component of the network. Other finetunes cannot be explained as interpolations.

Below is the evidence. Judge for yourself.

Reactions are currently unavailable

## Metadata

## Metadata