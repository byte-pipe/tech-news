---
title: AI can rewrite open source code—but can it rewrite the license, too? - Ars Technica
url: https://arstechnica.com/ai/2026/03/ai-can-rewrite-open-source-code-but-can-it-rewrite-the-license-too/
site_name: newsfeed
content_file: newsfeed-ai-can-rewrite-open-source-codebut-can-it-rewrite
fetched_at: '2026-03-11T13:13:05.662696'
original_url: https://arstechnica.com/ai/2026/03/ai-can-rewrite-open-source-code-but-can-it-rewrite-the-license-too/
date: '2026-03-10'
published_date: '2026-03-10T19:36:05+00:00'
description: Is it clean "reverse engineering" or just an LLM-filtered "derivative work"?
tags:
- ars-technica
- ai
- chardet
- claude code
---

Text
 settings

Computer engineers and programmers havelong relied on reverse engineeringas a way to copy the functionality of a computer program without copying that program’s copyright-protected code directly. Now, AI coding tools are raising new issues with how that “clean room” rewrite process plays out both legally, ethically, and practically.

Those issues came to the forefront last week with the release of a new version ofchardet, a popular open source python library for automatically detecting character encoding. The repository was originally written by coder Mark Pilgrimin 2006and released underan LGPL licensethat placed strict limits on how it could be reused and redistributed.

Dan Blanchard took over maintenance of the repository in 2012 but waded into some controversy with the release ofversion 7.0 of chardetlast week. Blanchard described that overhaul as “a ground-up, MIT-licensed rewrite” of the entire library built with the help of Claude Code to be “much faster and more accurate” than what came before.

Speaking to The Register, Blanchard said that he has long wanted to get chardet added to the Python standard library but that he didn’t have the time to fix problems with “its license, its speed, and its accuracy” that were getting in the way of that goal. With the help of Claude Code, though, Blanchard said he was able to overhaul the library “in roughly five days” and get a 48x performance boost to boot.

Not everyone has been happy with that outcome, though. A poster using the name Mark Pilgrimsurfaced on GitHubto argue that this new version amounts to an illegitimate relicensing of Pilgrim’s original code under a more permissive MIT license (which, among other things, allows for its use in closed-source projects). As a modification of his original LGPL-licensed code, Pilgrim argues this new version of chardet must also maintain the same LGPL license.

“Their claim that it is a ‘complete rewrite’ is irrelevant, since they had ample exposure to the originally licensed code (i.e., this is not a ‘clean room’ implementation),” Pilgrim wrote. “Adding a fancy code generator into the mix does not somehow grant them any additional rights. I respectfully insist that they revert the project to its original license.”

## Whose code is it, anyway?

Inhis own response to Pilgrim, Blanchard admits that he has had “extensive exposure to the original codebase,” meaning he didn’t have the traditional “strict separation” usually used for “clean room” reverse engineering. But that tradition was set up for human coders as a way “to ensure the resulting code is not a derivative work of the original,” Blanchard argues.

In this case, Blanchard said that the new AI-generated code is “qualitatively different” from what came before it and “is structurally independent of the old code.” As evidence, he citesJPlagsimilarity statistics showing that a maximum of 1.29 percent of any chardet version 7.0.0 file is structurally similar to the corresponding file in version 6.0.0. Comparing version 5.2.0 to version 6.0.0, on the other hand, finds up to 80 percent similarity in some corresponding files.

“No file in the 7.0.0 codebase structurally resembles any file from any prior release,” Blanchard writes. “This is not a case of ‘rewrote most of it but carried some files forward.’ Nothing was carried forward.”

 Blanchard says starting with a “wipe it clean” commit and a fresh repository was key in crafting fresh, non-derivative code from the AI.
 

 Credit:
 
Dan Blanchard / Github

 Blanchard says starting with a “wipe it clean” commit and a fresh repository was key in crafting fresh, non-derivative code from the AI.

 

 Credit:

 

 
 Dan Blanchard / Github

 

Blanchard says he was able to accomplish this “AI clean room” process by firstspecifying an architecture in a design documentand writing out some requirements to Claude Code. After that, Blanchard “started in an empty repository with no access to the old source tree and explicitly instructed Claude not to base anything on LGPL/GPL-licensed code.”

There are a few complicating factors to this straightforward story, though. For one, Claudeexplicitly relied on some metadata files from previous versions of chardet, raising direct questions about whether this version is actually “derivative.”

For another, Claude’s models are trained onreams of data pulled from the public Internet, which means it’s overwhelmingly likely that Claude has ingested the open source code of previous chardet versions in its training. Whether that prior “knowledge” means that Claude’s creation is a “derivative” of Pilgrim’s work is an open question, even if the new code is structurally different from the old.

And then there’s the remaining human factor. While the code for this new version was generated by Claude, Blanchard said he “reviewed, tested, and iterated on every piece of the result using Claude. … I did not write the code by hand, but I was deeply involved in designing, reviewing, and iterating on every aspect of it.” Having someone with intimate knowledge of earlier chardet code take such a heavy hand in reviewing the new code could also have an impact on whether this version can be considered a wholly new project.

## Brave new world

All of these issues have predictably led to a huge debate over legalities of chardet version 7.0.0 across the open source community. “There is nothing ‘clean’ about a Large Language Model which has ingested the code it is being asked to reimplement,” Free Software Foundation Executive Director Zoë Kooymantold The Register.

But others think the“Ship of Theseus”-stylearguments that can often emerge in code licensing dust-ups don’t apply as much here. “If you throw away all code and start from scratch, even if the end result behaves the same, it’s a new ship,” Open source developer Armin Ronacher saidin a blog post analyzing the situation.

 The legal status of AI-generated code is still largely unsettled.
 

 Credit:
 Getty Images
 

 The legal status of AI-generated code is still largely unsettled.

 

 Credit:

 
 Getty Images

 

Old code licenses aside, using AI to create new code from whole cloth could also create its own legal complications going forward. Courts have already said that AIcan’t be the author on a patentorthe copyright holder on a piece of artbut have yet to rule on what that means for the licensing of software created in whole or in part by AI. The issues surrounding potential “tainting” of an open source license with this kind of generated code canget remarkably complex remarkably quickly.

Whatever the outcome here, the practical impact of being able to use AI to quickly rewrite and relicense many open source projects—without nearly as much effort on the part of human programmers—is likely to have huge knock-on effects throughout the community.

“Now the process of rewriting is so simple to do, and many people are disturbed by this,” Italian coder Salvatore “antirez” Sanfilippowrote on his blog. “There is a more fundamental truth here: the nature of software changed; the reimplementations under different licenses are just an instance of how such nature was transformed forever. Instead of combating each manifestation of automatic programming, I believe it is better to build a new mental model and adapt.”

Others put the sea change in more alarming terms. “I’m breaking the glass and pulling the fire alarm!”open source evangelist Bruce PerenstoldThe Register. “The entire economics of software development are dead, gone, over, kaput! … We have been there before, for example when the printing press happened and resulted in copyright law, when the scientific method proliferated and suddenly there was a logical structure for the accumulation of knowledge. I think this one is just as large.”

 Kyle Orland
 

Senior Gaming Editor

 Kyle Orland
 

Senior Gaming Editor

 Kyle Orland has been the Senior Gaming Editor at Ars Technica since 2012, writing primarily about the business, tech, and culture behind video games. He has journalism and computer science degrees from University of Maryland. He once 
wrote a whole book about 
Minesweeper
.
 

1. 1.After falling far behind the rest of industry, Blue Origin creates new stock option plan
2. 2.After outages, Amazon to make senior engineers sign off on AI-assisted changes
3. 3.“It doesn't feel safe”—Many international game developers plan to skip GDC in US
4. 4.US blindsides states with surprise settlement in Live Nation/Ticketmaster trial
5. 5.Apple MacBook Neo review: Can a Mac get by with an iPhone’s processor inside?

Customize