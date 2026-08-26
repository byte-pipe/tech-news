---
title: Keep AI Out of Your (Obsidian) Vault
url: https://www.ssp.sh/brain/using-obsidian-with-ai/
site_name: hnrss
content_file: hnrss-keep-ai-out-of-your-obsidian-vault
fetched_at: '2026-08-26T21:39:43.156722'
original_url: https://www.ssp.sh/brain/using-obsidian-with-ai/
author: Simon Späti
date: '2026-08-26'
published_date: '2026-04-24T00:00:00Z'
description: Everyone is using Obsidian for AI, or wants to use it to become more productive. But I think it's a dead end.
tags:
- hackernews
- hnrss
---

# Keep AI Out of Your (Obsidian) Vault

Last updatedUpdated:Aug 26, 2026bySimon Späti·CreatedCreated:Apr 24, 2026·8 min readrecently updatedRecent changesAug 26today+160/−84wordsAug 62 weeks ago+4/−0wordsJul 303 weeks ago+32/−32wordsJun 93 months ago+9/−0wordsJun 13 months ago+85/−179wordsMay 293 months ago+12/−0wordsMay 273 months ago+201/−9wordsMay 183 months ago+32/−15wordsMay 114 months ago+13/−0wordsApr 304 months ago+1084/−1057wordsApr 274 months agopublished· 1792 words

Everyone is usingObsidianforAI, or wants to use it to become moreproductive. But I thinkit’s a dead end.

The reasons are clear: Obsidian notes are open on your local disk in an open format,Markdown, and accessible to everyone, including your AI agents. This makes it as great and easy an integration as possible. But should you actually use AI with your notes? And if so, what are the use cases or ways you should interact with it?

First of all, if you useVibe Code Agentswith Obsidian, use theObsidian CLI. It will be much faster to return your files, search, or act, grepping through the files.

Second, I’m a strong proponent of avoiding adding lots of AI-generated summaries[^1] or other on-the-fly-generated text to my vault. The reason is simple: over time, I don’t know anymore whether the content was written by me or by an AI, and my own, much more valuable thoughts get diminished by “AI Slop”.

1. Also, when searching for something, you need to fight through the noise of generated stuff. If you only have your own writing, it’s all valuable, or at least there’s a reason why you noted it down. There was aconviction,idea, or something that moved you.
2. Yes, it’s good in certain areas, and mostly on-the-spot summaries seem great, but every time I come back to them, I find them very average. It doesn’t help me, as it didn’t highlight the things I would, and I need to reread anyway.
3. What I do sometimes withObsidian Webclipper, if I create a new note, is summarize it in one sentence or a few. I clearly mark it as AI-generated and even put it in a quote, so it’s clear to me, and to anyone in 5 years, that it wasn’t mine. If I have added my own thoughts and writing, I will just remove the generated paragraphs (not my words).

But, use it for advanced research, like finding related notes. I think this might be the best use case. But don’t use it for tagging or organization, because eventually all your relations and connections won’t count for anything, since they aren’t made by you. The power lies in thedeliberately created graph of notes, your very ownSecond Brain.

My Obsidian Vault with Smart Lookup and related notes with Smart Connections andlocal graph| Also check outVim Motions for Writersto see my writing workflow and how I write

I personally don’t use it like that yet, but I might one day with a powerful local model, since I have lots of sensitive notes I don’t want to upload anywhere. Plus, it takes away thethinking partofMy Obsidian Note-Taking Workflow. I don’t want toreplace my human thinkingyet. But I use a mathematical or local model withObsidian Smart Connections, or theGraph Analysisplugin.

I’m pretty sure that if yougo all in with using AIto generate your notes, you will end up with less clarity and fewer insights. You might start fresh very soon, as you won’t get value from it, and stop maintaining or adding ideas.

[^1] To be clear, I mean long summaries, no harm in a 1-2 sentence intro in a note.

Long AI Summarization is usually just noise

Kepanosays, too: “A summary of a PDF is noise. An insight I had from reading the PDF is signal”.Tweet. Read moreOther Opinionsby Jason Fried, Paul Graham, Ted Gioia, Mitchell Hashimoto, and many more.

## #Search is an Organizational Question

I think if you have an urge to do something, do it in a separate vault, or just use a database, e.g.DuckDB, and do all the fun stuff with AI as I did forsearch and clustering. But don’t mix your precious notes andZettelkastenfor it. Not yet, at least, but probably never.

I have 25'979 files totaling 3.5 GB, all in a single vault, and I find everything in split seconds (using theOmnisearchplugin). Search ispretty much an organizational question; e.g., I useZettelkasten, and some refer toMemexas its digital version.

But if you need more advanced features, you can just add theObsidian Smart Connectionsplugin and get vector and similarity search, etc., out of the box.

### #Your Notes Will Be Your Prompts Tomorrow

Remember, your notes will beprompts orlibraries for AI tomorrow, but not if you generate them.

#### #Cultivating Knowledge

Also on the notion ofcultivating knowledge for AI systems, I’d say I’m more interested in cultivating for myself, long-term 🙂.

I imagine if humans do not have their own knowledge bases, everyone will have the same (average) notes based on AI models, not 100% of course, but there is no conviction, no decisions made,just all equally similar.

This is another reason we also need human-curated knowledge on a large scale. AI models will retrain on this data, better than on synthetic, fake data, IMO, though we need to find an economic model that also works for the creator of these insights and knowledge.

## #Whose Knowledge System is It?

UsingClaude Code(or another agent) to generate your system and make connections, like, is notyoursystem. If you want a tool for retrieval, yes, sure, but I have a second brain and a knowledge system where my thinking happens. I make the connections because I had an idea, or something told me to do so.

Great video on this with more of the same thinking I have atObsidian vs Claude — Why I’m Not Worried About AI Killing Note-Taking Apps. He says elegantly that a second brain is a system; the connections and writing parts are not inefficient; it’s the process of thinking and learning.

Claude is just a tool, like Obsidian, but asFile Over App, by the CEO of Obsidian, goes, it’s not about the app anyway, it’s about the files, your thoughts, your insights. So if it’s someone else’s, heck, even generated, it’s not why I use the second brain. Can be useful, too, sure, but not as much as my new ideas, the thinking I get from my knowledge system.Touch some grass, they say.

## #Examples

Some examples that identify this phenomenon quite well, or help us understand and think through it better.

### #It’s Hard to Finish an Idea that is not Yours

While I use Claude a lot for my Omarchy plugins and Linux optimization/failure detection, I don’t use it for writing and note-taking, especially for coming up with unique ideas and driving them home by writing them through to the end.

It’s sohard to finish an idea that is not yoursand is just suggested by AI.

### #Andrej Karpathy’s LLM Knowledge

Andrej KarpathyLLM Knowledge Auto Research, which is another good example of hownotto do it (IMO), especially if you like tolearn. Sure, it’s fun and helpful, but it will lose its appeal and value over time. It’s like this Reddit quote says it well:

I definitely agree that the ‘Karpathy LLM Wiki’ mediated knowledge base everyone is excited about isnot a useful way to actually learnor manage your learned and curated data for the reasons written. If instead you do just want anautomated research summaryof some knowledge - sure why not, butit’s not particularly interestingand I really don’t get the excitement about it.Reddit

Some great discussionin this threadon this topic.

#### #Does not Scale, or Will Die Very soon

Automating the links and connections like this won’t sustain for YOUR second brain, for your ideas and notes - you are skipping the thinking, and IMO, the insights. Most of my ideas come from linking and seeing the links I made myself, sometimes years back.

A good example of what not to do for your own vault.Tweet

For sure interesting to see what comes out, but I wouldn’t recommend it for your “second brain” where you develop your thinking and YOUR ideas.

If you want the above brain, which is not yours, you should useWikipedia. Wikipedia graphs and wikilinks give you great insights, as the automated AI ones (probably more), but made by human collaborators. But if you want to create your own knowledge base, I’d do it manually. Thepayoff comes over the year, itcompounds.

### #PARA Method: Dedicated Folder

ThePARAmethod byTiago Forteis super convenient - and you could create an AI folder in resources and put all generated notes there and hide that from search or through other mechanisms. This way, you could still have AI-generated insights or notes that you can link, if helpful, to your original notes.

### #Voice to Text

AI withVoice to Textcan be another approach to use with Obsidian, which makes sense when you are in a car or so.

But because of my talking much more compared to when I write, and to AI or translator service not understanding all my words, it’s much more work for me than just typing it out. Plus, I usually skip the thinking, though sometimes talking it through can add to the process.

## #Slowing Down: Have More Impact Long-term?

SeeSlowing Down.

## #Creativity by Its Very Nature is Forward-looking

Creativity is Forward Looking

## #Further Reads

* Second Brain Assistant with Obsidian (NoteGPT)
* Building an Obsidian RAG with DuckDB and MotherDuck
* Don’t use AI for everything, you stop thinking-learning AI Use
* How To Think Better in the Age of AI (From the Stoics)
* Use less AI
* Everything Ive published came out of one Obsidian vault

Origin:Libymehdio,ObsidianReferences:Writing is Thinking!,

Data Engineering & Second Brain Newsletter

This note is part of my Second Brain, a 650+ public notes on data engineering, life, and more. I send a digest of new notes, blog posts, and book chapters, and general updates by email. Subscribe below if you'd like to get the next one.

### Interactive Graph