---
title: Why XML Tags Are so Fundamental to Claude
url: https://glthr.com/XML-fundamental-to-Claude
site_name: hnrss
content_file: hnrss-why-xml-tags-are-so-fundamental-to-claude
fetched_at: '2026-03-02T08:25:32.524007'
original_url: https://glthr.com/XML-fundamental-to-Claude
date: '2026-03-01'
published_date: '2026-03-01T14:51:45.997Z'
description: (This is the fourth installment in my series on delimiters in languages). The tour de force of Claude is to have made XML tags first-class citizens. This assertion may seem provocative, but I believe
tags:
- hackernews
- hnrss
---

## Command Palette

Search for a command to run...

G

Guillaume Lethuillier

(This is the fourth installment in my series ondelimiters in languages).

The tour de force of Claude is to have made XML tags first-class citizens. This assertion may seem provocative, but I believe there is something fundamental at play here.

The Claude API Docs provide practicalprompting best practices, designed for developers by outlining specific instructions and clear formatting rules. They presenta contrast between Claude’s modern approach and the reiterated suggestion of using traditional XML tags:

This is not a minor tip: users report thatstructuring prompts with XML can be a transformative experience: “Here’s the simple trick. Instead of just asking Claude stuff like normal, you put your request in special [XML] tags. . . . That’s literally it. And the results are so much better.”

And not only does Claude use XML tags in prompts, but its training specifically incorporates them as key elements: “Anthropic heavily uses XML tags in their prompts.” In other words, XML tags have not only a special place at inference level but also during training.

This is, admittedly, a subjective reading, but I believethe repurposing of XML, a technology dating back to 1998, may represent a core aspect of what makes Claude distinctive: it turns Claude into something closer to a genuine language interpreter.

My own research (as a hobbyist) has led me to postulate the existence of a universal principle underlying all languages, whether human or artificial. I have observedthis principleat work in diverse contexts:programming languages, bacterial DNA sequences,Homeric verses, and now, seemingly, with Claude. This principle centers onthe necessity for any language (regardless of its form) to possess a mechanism for signaling the transition from first-order to second-order expressions. I contend that such a mechanism is fundamentally required for information transfer between any two entities; without it, meaningful communication becomes virtually impossible.

These transitions are typically indicated by markers or delimiters. In contemporary English, quotation marks serve this purpose. They delineate the shift from direct statement to reported speech, metaphor, or quoted material. These markers operate in pairs: one initiates the transition from first-order to second-order expression, while the other signals a return to the original level of discourse. Furthermore, this nesting can be deeply embedded; we can move from ordernto ordern+1, then ton+2, and so on, creating complex layers of meaning.

To illustrate how these distinctions play out in practice, consider an observation froman AWS prompt engineering course. It serves as a concrete demonstration of how crucial clear delimiters are for ensuring Claude accurately interprets and executes complex prompts:

“Here, Claude thinks ‘Yo Claude’ is part of the email it’s supposed to rewrite!” is a remarkably revealing statement. “Yo Claude” is a first-order expression (the user interacting with Claude), the content of the email is a second-order expression (the email the user will address to someone else). And they use XML tags because they need to delimit, they need to enclose the higher-order expression, like we do, in English, when we quote someone using quotation marks (like at the beginning of this paragraph); like Homer did when making heroes talk using formulaic delimiters in Ancient Greek; like bacterial DNA does to store recognition sequences.

In truth, it does not matter that these tags are XML. Other models use ad hoc delimiters (as explained ina previous article; example:<|begin_of_text|>and<|end_of_text|>) and Claude could have done the same. What matters is what these tags represent.What makes Claude special is that its creators made it “aware” of the concept of delimiters, which, at least this is my view, is so crucial to the effective processing and communication of information.And it is precisely this capacity that makes Claude so effective at interpreting layered meaning.

#
llm
#
languages
#
claudeai

## More from this blog

Jan 3, 2026
·
12 min read

Subscribe to the newsletter

Get new posts delivered to your inbox.

Subscribe
Dec 26, 2025
·
7 min read
Sep 20, 2025
·
10 min read
Aug 5, 2025
·
4 min read

glthr.com | Guillaume Lethuillier's blog

19posts published
