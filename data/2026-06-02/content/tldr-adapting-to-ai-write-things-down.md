---
title: 'Adapting to AI: Write Things Down'
url: https://blog.colinbreck.com/adapting-to-ai-write-things-down/
site_name: tldr
content_file: tldr-adapting-to-ai-write-things-down
fetched_at: '2026-06-02T06:00:41.161890'
original_url: https://blog.colinbreck.com/adapting-to-ai-write-things-down/
date: '2026-06-02'
published_date: '2026-05-31T15:40:33.000Z'
description: If things are not written down, there is no way for a language model to operate on this knowledge.
tags:
- tldr
---

I have written a series of essays on how the software industry is adapting to AI. The first essay reflected onproductivity, the second essay was aboutcode review, and the third essay looked at AI through the lens ofsoftware engineering. In this essay, I will explore the organizational effectiveness of written communication.

## A Culture of Writing

The AI tools currently used for software engineering rely on language models—probabilistic models that largely operate on text. If things are not written down, there is no way for a language model to operate on this knowledge.[1]Organizations that have a strong writing culture will take advantage of AI more effectively than organizations that don’t have the discipline to codify work in writing.[2]

Amazon famously discouraged presentations in favor of six-page narrative documents that encourage more rigorous thinking and argumentation. More than most companies, Amazon relies on writing to develop and communicate ideas, and they view this as a competitive advantage:

So now we’re all on the same page, we’ve all read the memo, and now we can have a really elevated discussion. And this is so much better from having a slideshow presentation, a PowerPoint presentation of some kind, where that has so many difficulties. But one of the problems is PowerPoint is really designed to persuade. It’s kind of a sales tool. And internally, the last thing you want to do is sell. Again, you’re truth seeking. You’re trying to find truth. And the other problem with PowerPoint is it’s easy for the author and hard for the audience. And a memo is the opposite. It’s hard to write a six-page memo. A good six-page memo might take two weeks to write. You have to write it, you have to rewrite it, you have to edit it, you have to talk to people about it. They have to poke holes in it for you. You write it again, it might take two weeks. So the author, it’s really a very difficult job, but for the audience it’s much better.—Jeff Bezos,Lex Fridman's Podcast[3]

Oxide Computer company is another organization with a writing culture, capturing all important decisions in Requests for Discussion (RFD), many of which they havemade available publicly. For companies like Amazon and Oxide, writing well is thinking well.

Jim Gray, the Turing Award winner, was known for his writing. He believed the greatest value was not in the ideas, but in the first person who took the time to write them down and share with others so the ideas could grow:

One of the things that my research advisor Mike Harrison taught me to do is to write things down. So whenever I would go on a trip, I would write a trip report; and whenever I’d talk to people and we had an idea, I would write a memo about our discussion, to document it. One consequence of this is that I wrote lots of papers and went to lots of conferences.—Jim Gray,Jim Gray Speaks Out

Any organization that has emphasized effective written communication likely feels vindicated by the effectiveness of large language models in combination with that writing. As someone who enjoys writing long-form essays and embraces written communication at work, I am certainly welcoming this shift. Writing things down takes a lot of investment, but I notice when I take the time to write something down, and do it well, the investment amplifies when I end up referring back to it or sharing it repeatedly over time. Now I can also share those documents and amplify that value with agents.[4]

## Not a Culture of Summary

The culture of writing I’m talking about is not AI summary but canonical writing from primary sources. This type of writing compounds in value over time, whether it be a design document, product documentation, the report on a production incident, a document on team values or process, or an email memo from an executive.[5]Documents capturing the reasoning behind technology choices, architectural decisions, and team culture make it clear which decisions were intentional and which ones were accidental. Writing that is not canonical pollutes the context.[6]

I worry we read too much summary...I suspect careful thinkers do not gain a mastery of mystery, or attention to detail, by scrolling Reddit or listening to current event podcasts or asking “AI” to summarize anything. Instead I imagine they spend their time with primary sources, correspondence, stories, engaging with their own senses in one way or another, or some other form of exploring the world in detail...The opposite of summary is attention to detail.—Simon Sarris,Resist Summary

While large language models operate on text, they are also wildly efficient at generating text. The text is wonderfully formatted and it is gives the sense of being detailed, accurate, and authoritative, but without ever cutting through the details or getting to the point. It is exhausting to read. It is now common to see people who did not have strong written communication skills, or a focus on writing, creating detailed summaries, documents, and presentations from other sources using AI. Summaries of work done are like reading a detailed commit history. People who value writing and collaboration are now overloaded with decision-making noise trying to handle all this seemingly persuasive writing. What I need are higher-level strategic summaries of what was accomplished, what the value is, and where we need to go next, not an AI summary of the details. Two things AI still needs our help with: deciding what to build and evaluating how good it is.

## Using AI For Writing

When I write, at work, or on this blog, I use AI as a tool. It is wonderful for research, excellent at enumerating pros and cons, and it is ruthless for finding subtle typos that the human eye will easily anticipate away. But I try and avoid using it for doing the writing itself, especially for summarizing when I want to produce original or canonical writing. I want to be intentional about the details and how they fit together into the whole.

When I read a book, I really feel that if I can hear the author's voice ringing in my head—complete with weird accents and peculiarities of their speaking patterns—then I feel like something has succeeded.—Bjarne Stroustrup,Meet the Authors

I believe organizations that have a culture of writing—real writing about ideas, from primary sources—will outperform those that do not.[7]

1. Meetings can be transcribed. For some meetings, the value in them will be diminished if they are not transcribed. For others, it will likely be refreshing to just have a conversation and not worry about capturing it and leverage it with AI.↩︎
2. Cynically, with AI being incredibly good at analyzing a huge corpus of text, the most political operators in an organization may avoid writing things down, preferring to communicate in meetings, one-on-one interactions, or hallway conversations, or avoid communication altogether. When nothing they said is written down, it is harder to hold them accountable.↩︎
3. Read the bookWorking Backwards: Insights, Stories, and Secrets from Inside Amazonfor more on the development of the writing culture at Amazon.↩︎
4. Something I like to do is take notes when I meet with someone, especially organizational leaders. I write them up and then send them to the person I met with to review. There is something very powerful about writing down someone else’s views on culture, engineering, product management, execution, people management, and so on, having them review it to ensure they agree with your transcription, and then sharing it with others. It multiplies their value, and it multiplies your value in the process.↩︎
5. An email memo from an executive is a particularly valuable form of writing. These memos can provide crisp and clear direction and live on for years in establishing and maintaining culture.↩︎
6. An example I saw recently: the conclusion of a report on data loss was that it was related to throttling. The reason AI concluded this was there were log messages about throttling captured in a ticket, but these messages were only logged for visibility, and the rate limits were not actually enforced. One AI drew erroneous conclusions and published them in a ticket. Another AI built on these erroneous conclusions and made a convincing report.↩︎
7. The picture at the top of this essay is a note a bartender wrote me once that says, "The stories untold are written in stone" in English, Dutch, and Morse code. It seemed fitting for this essay.↩︎