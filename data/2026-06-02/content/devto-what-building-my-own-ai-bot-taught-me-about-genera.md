---
title: What Building My Own AI Bot Taught Me About Generative AI - DEV Community
url: https://dev.to/dannwaneri/what-building-my-own-ai-bot-taught-me-about-generative-ai-57il
site_name: devto
content_file: devto-what-building-my-own-ai-bot-taught-me-about-genera
fetched_at: '2026-06-02T20:05:23.527103'
original_url: https://dev.to/dannwaneri/what-building-my-own-ai-bot-taught-me-about-generative-ai-57il
author: Daniel Nwaneri
date: '2026-05-27'
description: I built a bot trained on my own X bookmarks and likes. Around 50,000 of them, accumulated over years... Tagged with ai, webdev, rag, llm.
tags: '#ai, #webdev, #rag, #llm'
---

Intelligence as high-quality retrieval

I built a bot trained on my own X bookmarks and likes. Around 50,000 of them, accumulated over years of lurking, arguing, and clicking the save button on things that made me stop scrolling.

The technical part isn't complicated in principle. You pull your export, embed the text, build a RAG pipeline, add a style prompt derived from your own writing patterns, and you get something that responds to prompts by retrieving your most relevant saved content and riffing from there. I called it Bookmark Brain, which is either clever or embarrassing — I haven't decided.

What I didn't expect was how much it would clarify my thinking about what generative AI actually is.

The bot works too well. That's the problem.

When I ask it about API design opinions or takes on the current AI hype cycle, it returns something that sounds like me — specific, slightly annoyed, grounded in a particular set of concerns — better than most general-purpose LLMs do when I prompt them with "write in my voice." The difference isn't the model. It's the retrieval layer. The model in both cases is doing the same approximate thing. What changes is what it retrieves before it starts generating.

That realization landed harder than I expected: a significant chunk of what we call AI "intelligence" is retrieval. The system finds related content, mixes it with the query, and produces output shaped by that specific neighborhood of the embedding space. It's not thinking. It's not understanding. It's doing something closer to extremely sophisticated autocomplete with a memory. The illusion of reasoning comes from the quality of what was retrieved, not from inference happening in any deep sense.

The uncomfortable follow-on: I started noticing the same thing in myself. A lot of what I'd been calling original thinking was my brain doing something structurally similar — retrieving from a curated internal dataset of influences, combining them in ways that felt novel, outputting with enough fluency to pass as insight. The bot didn't make me feel smarter. It made me suspicious of my own cognition.

My bot sounds coherent because my bookmarks are coherent. I've spent years curating a specific worldview — skeptical of tech hype, interested in systems and incentives, irritated by vague abstraction. That worldview is baked into the dataset. Retrieval finds it. The model outputs it in grammatical sentences. The whole thing looks like intelligence from the outside.

Then the Granta thing happened.

If you missed it: Granta, the literary magazine, ran a piece flagged by AI detectors. Turns out the writing was human — and older than the detectors themselves. Pre-2022, written before the tools they were being assessed with even existed.

The writer, understandably, was furious. The editorial response was clumsy. What struck me was the confidence behind the process — the idea that a detector score constitutes evidence of anything meaningful.

It doesn't. AI detectors are probabilistic classifiers trained on distributional differences between human and AI writing. Dense, formal, or unusual prose trips them constantly. Academic writing, translated text, anything with a compressed or structured style — all of these get flagged. The detector isn't reading. It's pattern-matching statistical features. And those features shift as models improve, as writing styles evolve, as the gap between the training distribution and current reality widens.

Watching publications, employers, and universities lean on these tools as if they're reliable is the same energy as relying on a polygraph. The tool isn't detecting deception. It's detecting nervousness, or formality, or the wrong register for the context. The conclusion isn't what the tool thinks it is.

What the Granta situation made concrete for me: we have a collective problem with mistaking a signal for the thing the signal supposedly measures. Perplexity score is not authenticity. Semantic similarity is not understanding. And this is the same confusion that inflates most AI capability claims.

Here's the irony I live with every day.

I use AI heavily. I build with it, write with it, prototype faster because of it. I'm not performing skepticism while secretly relying on it — I'm actually relying on it, out in the open, and also genuinely skeptical of what it's doing and why the claims around it are so often overconfident.

Yes, I'm part of the problem. I know that. But I built Bookmark Brain precisely because I wanted to understand what the problem actually is — not at the level of takes and op-eds, but at the level of retrieval logs and embedding distances and why a particular output came out the way it did. The people most confident about AI — evangelists and critics alike — are usually the ones who haven't built anything with it. They're responding to the outputs. I wanted to see the pipes.

My bot makes this concrete in a specific way. Because I can see exactly what it's doing — retrieve, compose, style-match — I can no longer pretend the underlying process is mysterious. It isn't. It's a very good pattern engine. And the patterns it's good at are the ones humans have already made enough times to constitute a retrievable signal.

The things it can't do are equally clear. It can't tell me something genuinely new. It can't resolve contradictions in my bookmarks; it just retrieves whichever side of an argument is more semantically proximate to my query. It has no persistent sense of what I care about most — that's in the embedding weights and the retrieval ranking, not in anything like a value structure. If I've saved content across five years on Nigerian economic policy, it can retrieve that content. It cannot tell me what I should think about a new development that doesn't yet exist in those embeddings.

That's not a criticism. It's just an accurate description of what the tool is. The criticism is when people — including, honestly, past me — talk about these systems as if they're operating at a different level entirely.

Most people initially misunderstand generative AI the same way. They see the output and map it to human cognition because that's the only reference frame available. The output sounds like thinking. Therefore it is thinking. The logic is understandable and wrong.

What's actually happening is closer to: the system has compressed a large representation of existing human expression, retrieves the most contextually relevant parts, and generates a continuation that's statistically consistent with that neighborhood. That's not nothing. In fact it's remarkable. But it's not reasoning. It's not understanding. And it absolutely is not reliable in domains where the training distribution doesn't match the actual problem.

Building Bookmark Brain made this concrete rather than abstract. I could watch the retrieval logs. I could see what it was pulling. I could trace why a particular response came out the way it did. That transparency — available only because I built it — is exactly what's missing when people interact with closed systems and anthropomorphize the outputs.

The piece of this I'm still sitting with is about curation.

My bot is useful because I curated carefully for years. The quality of the output is downstream of the quality of the input — not the model, not the prompt engineering, the input. 50,000 bookmarks that reflect a consistent set of concerns, an identifiable worldview, real opinions.

If I'd bookmarked everything uncritically, the bot would be incoherent. Garbage in, garbage out, but at scale and with a convincing fluency that would make the garbage harder to spot.

That's the thing about generative AI broadly: it doesn't make bad data good. It makes it fluent. And fluency is exactly the property that makes it hard for people — including detectors, including reviewers, including people who should know better — to evaluate what's actually in front of them.

I built a tool that sounds like me. It works because of what I put into it, not because of anything the model does that's particularly special. The model is a compositor. The dataset is the author.

That's the most clarifying thing I've learned. It's what almost every discussion about these systems gets wrong.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (17 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse