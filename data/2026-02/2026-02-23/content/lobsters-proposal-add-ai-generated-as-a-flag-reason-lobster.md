---
title: 'Proposal: add "AI generated" as a flag reason | Lobsters'
url: https://lobste.rs/s/rkjpob/proposal_add_ai_generated_as_flag_reason
site_name: lobsters
content_file: lobsters-proposal-add-ai-generated-as-a-flag-reason-lobster
fetched_at: '2026-02-23T06:00:32.957900'
original_url: https://lobste.rs/s/rkjpob/proposal_add_ai_generated_as_flag_reason
date: '2026-02-23'
description: ☶
tags: meta
---

1. 240Proposal: add "AI generated" as a flag reason☶metaauthored bydanderson13 hours ago

IMO, the feed is being DoSed by LLM-authored text and vibecoded software. Anecdotally, the community's immune system is currently rejecting these in two ways: adding thevibecodingtag to anything that's been touched at all by an LLM, or flagging posts as spam.

I suggest that both these immune responses are problematic in their own way, and that giving us a way to flag specifically LLM generated content would be better.

Per the guidance on the lobsters code repo, posting this as a meta first to gauge sentiment. If this is something we'd collectively like, I would be delighted to make the implementation happen.

To define what I mean by AI generated: text or code that was substantially not authored by a human mind trying to communicate an idea, but rather by having an LLM expand a prompt into a larger artifact. There is an element of Stewart's "I know it when I see it" in this definition, buthttps://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writingis one laundry list of hallmarks of LLM output.

Speaking personally, I think flagging as spam is the correct response. Such content is a denial of service attack on our collective attention. I find it deeply frustrating to get partway into a submission before seeing the LLM signs, and realizing that I've likely already spent more time reading the slop than the author spent writing it. This type of content is no better than what was on the content farms and lazy clout farming blogs of old, LLMs have merely made it much easier to generate such content in volume.

However, flagging as spam seems to cause confusion. It seems to me that the confusion stems from people who haven't learned to recognize LLM text, and express a confusion that boils down to "this doesn't look like commercial/ad type spam, why the flags?" Having a separate flag reason that conveys "hey this is AI slop" would address this confusion. Incidentally it'd also help folks learn what LLM text looks like, which I think is an immensely important skill to pick up.

Likewise, flagging everything that's had an LLM near it asvibecodingseems to frustrate people. I personally think we'd be better off with all the vibecoding posts deleted from the site, but let me try to steelman. I think the contention is that there is interesting, high-quality stuff out there concerning the application of LLMs to software development, and that the tag should be concerned with those rather than acting as a dumping ground for anything that an LLM has touched. If this is correct, then having an explicit flag for removing low-value LLM output should benefit both the people who seek out posts taggedvibecoding, and those who hide the tag.

(I'm skipping over the whole "rename the tag" discussion, which has been rehashed several times already in recent meta posts. I think it's orthogonal to this proposal, and I don't think this proposal provides any new data for that question.)

I remember seeing post deletions in the moderation logs with the reason (paraphrased) "This is 'I vibecoded something', which is off-topic". I argue that this is a special case of the general rule I'm proposing: content whose human involvement was mostly prompting an LLM and (maybe) skimming its output is not a welcome contribution to this site. And I would like a way to explicitly call out and flag such vibed content, code or not.
