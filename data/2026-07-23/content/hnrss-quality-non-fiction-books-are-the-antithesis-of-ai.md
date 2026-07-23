---
title: Quality non-fiction books are the antithesis of AI slop
url: https://resobscura.substack.com/p/quality-non-fiction-books-are-the
site_name: hnrss
content_file: hnrss-quality-non-fiction-books-are-the-antithesis-of-ai
fetched_at: '2026-07-23T18:58:40.762831'
original_url: https://resobscura.substack.com/p/quality-non-fiction-books-are-the
author: Benjamin Breen
date: '2026-07-22'
description: '...so I vibe-coded a tool for finding more of them'
tags:
- hackernews
- hnrss
---

# Quality non-fiction books are the antithesis of AI slop

### ...so I vibe-coded a tool for finding more of them

Benjamin Breen
Jul 22, 2026
40
12
10
Share

My first year of college, I had a work-study job which ended up being one of the most sneakily important intellectual experiences of my life. I was a lowly library shelver, assigned to the shelves labelled A through F section in the Library of Congress filing system: mostly works on religion, philosophy, sociology, and history. I saysneakilyimportant because at first glance, shelving books in a library is super boring. What it amounts to, physically, is reading the label on a book, then placing it on the shelf where it belongs, repeated around a thousand times per shift.

To avoid the tedium, I decided that I would also flip to a random page of every book I shelved and read a random sentence from it. Usually, I would stop there — running aground on some passage by a Hungarian classical music critic or a long-dead statistician of Bolivia’s agricultural development or any number of other things that failed to catch my interest. But other times — like when I came across a book aboutHellenistic mystery cults, orThe Education of Henry Adams,orAre Clothes Modern?— I would become so absorbed that I’d make my way through several pages before reluctantly depositing the book back where it belonged.

And then, very often, I’d do the same with the books on either side of the one I’d liked.

GR 830, v through w: the vampire/werewolf section of Columbia’s Butler Library. 

In retrospect, I learned more at this job than in any formal class I’ve ever taken, because it was a filtered form of auto-didacticism. The Library of Congress classification system — and the expert staff of an academic research library — had already sorted and filtered these texts. Not to mention the selection mechanism of the fact that that they had beenchecked out: had, in other words, found a lasting readership. Thus I was not seeing a truly haphazard sampling of books, but a targeted, organized, yet still interestingly randomized sampling ofgoodbooks.

Today, undergraduate students will invariably search on Google when asked to find a source, and the results aresomuchworsethan the old method of going to, say, the GR 830 shelf of a research library (basically, “books that the Ghostbusters would read”) and just looking around.

But honestly, even research libraries are not what they used to be. I am 41, and I feel like I’ve lived through the peak, and now the decline, of what libraries can be (I still love them, of course — in fact I’m currently writing this in the genealogy section of the Santa Cruz Public Library). The browsable open stacks of old are being replaced by Learning Labs and Digital Innovation Hubs and seating areas devoted mostly to socializing and snacking, and increasingly, the delightful, weird old books that I had the opportunity to browse as an undergrad are heading to dumpsters, replaced by e-editions.

But one thing that has remained consistently good throughout my life is the books themselves — non-fiction books, I mean. Even now, as readership of non-fiction declines amid competition from AI chatbots and podcasts, I feel like we are living through a golden age of the form that rarely gets recognized as such.

### The Book Prize Index

Which is why I set aside some time this summer to create — or, rather, induce Claude Code to create — a free platform for searching in the long tail of high-quality non-fiction books. Quality is difficult to define, but it’s been my experience that books that win or achieve the short-list of the major non-fiction prizes are almost always noticeably good, so that was the litmus test I used. To get started, I counted up all the major non-fiction prizes in the English language. Then I had Claude and GPT-5.6 gather the lists of finalists and winners from various online sources (mostly Wikipedia) and arrange it into a searchable, sortable list.

You can visit ithere.

(And before you wonder, yes this is actually free. I am paying for the hosting and the API costs entirely because I just want people to find and read more good non-fiction books.)

Though youcouldconsider a paid subscription if you want to support this kind of thing:

Subscribe

There is really nothing “AI” about this aside from the tool that collected the data and coded it,1and, crucially,semantic search, which for me is the most appealing of all current AI tools precisely because it offers a straightforward improvement for a workflow and habit that researchers already have: it makes text search work better.

So for instance, you can search simple phrases like “modern France” or “social history” or the like, but you can also search things like “classic biographies that are surprisingly weird,” and an embedding model pulls from the 6,500 or so titles to surface some:

I am planning on reading 
Edith Wharton
, which doesn’t 
sound 
all that weird, but having read Lewis’s eclectic and brilliant biography of the James family, I think it’s a fair guess that it is. 

Sometimes the “choices” that the search makes are a bit baffling, but that is precisely why I like it: the idea is to recapture some of that feeling of a random walk through a well-tended garden that made my library shelving job so rewarding.

“Books for dads who like Pavement”
“David Attenborough, but in book form”

I find it tends to be best for finding “books like.” For instance I found Stefan Zweig’s memoir of pre-war Vienna,The World of Yesterday,to be deeply moving (even before I learned that he committed suicide, in Brazil in 1942, immediately after completing it). A search for a books like it using semantic search in the corpus immediately yields some titles that seem promising but which I’d never heard of before:

Once I had gathered all this book-related data, it became a fun experiment to make somedata visualizationswith it, including fun oddities like this display of roughly 5,000 books from the corpus arranged by color (it would be interesting to plot this by decade, to see whether the samegraying effect we see in carsover the past few decades is active in book covers, too).

Link
.

More useful, perhaps (since I’ve never seen this plotted anywhere else), isthis chartand accompanyingrankingwhich allows you to explore which imprints and publishers have fared best when it comes to non-fiction book awards over the past century.

### Against the algorithmic filter

And this, in turn, got me thinking about the past and future of nonfiction as a cultural force. For instance, here is a chart of all the non-fiction book prizes which I sampled for this project. I was surprised to learn that even the august, renowned Pulitzer Prize for nonfiction was actually relatively recently instituted, beginning in 1962.

Throughout the 70s, 80s and 90s, the number of prizes increases, until we reach a peak in 2014, and then, in 2020, the beginning of whatmaybe a slow decline:

And yet, maybe not. What most struck me as I began using my own tool to find new books to read was howconsistentlygoodthe long tail of non-fiction from the past few decades is. You can pick a book more or less at random from this list and end up with something extraordinary and original — not because it’s a hidden gem or forgotten, since obviously these books areonthe list by virtue of having been celebrated and praised. But a book that won enormous praise in newspapers and among literary intelligentsia or scholars in the early 1990s, say — like, for instance, David Levering Lewis’sacute biography of W.E.B. Du Bois, which I’m currently reading — is not exactly the sort of thing that Amazon is likely to recommend, as it’s out of print and currently at 1 million+ in the sales rankings.

Yet there it is on the list, ranked near the top ten of all books because it won no less than four major prizes when it was published back in 1993. And I can personally attest that you can buy it used for ~$4 and it’s really good.

Link

While writing this post, I got interested in the bigger question of when the golden age of non-fiction began and why. I suspect it has much to do with the rise of those old-school open stack research libraries, whose origins I wrote about here:

## The open-stack library: a futuristic technology from the 18th century

Benjamin Breen
·
November 8, 2023

“Where are all the books?” I asked the campus bookstore clerk earlier this year, as I was gearing up to teach in person for the first time since the COVID-19 shutdowns and my paternity leave.

Read full story

It’s true that the basic blueprint of these institutions is an 18th and 19th century development — but the post-war era radically transformed the ways that libraries and archives produced new knowledge, for a range of reasons that I will dig into more in a future post. It seems to me that a surprising number of them are related to technological and social change:

• The jet plane allowed writers and researchers to travel to multiple continents to research books — the sort of opportunity previously available only to the ultra-wealthy.

• The erosion of restrictions around class, race, and gender made formerly elite spaces like rare book libraries more widely accessible, and the same process also opened up new questions and research leads (for instance, it is striking how rarely biographers before ~1965 or so dug into the sexuality of their subjects).

• Proto-digital and early digital technologies like the Library of Congress classification system and the related MARC (machine-readable cataloguing) standard, developed in the late 1960s, made it much easier to sort and classify books. Crucially, they also made it easier to fact check sources and create high quality endnotes.

• The advent of broadcast news, oddball TV interview shows (Dick Cavett!), and the book-to-Hollywood pipeline created new incentives for authors and new platforms for making their work visible.

• Word processors and early computers? I’m still unsure whether these appreciably altered the quality of non-fiction writing, but I think it’s possible. Certainly (moving into the 2000s) Wikipedia and Google Books/Hathi Trust have been enormously helpful for me and others in my generation.

My own entirely subjective opinion, based on a whole lot of skimming in a whole lot of library books, is that non-fiction writing quality noticeably improved across the whole twentieth century and probably reached a peak around the 1980s to early 2000s. Whether it is now declining is, again, a topic for another post — though I’d be curious to hear whatyouthink, dear reader, both about this question and about the Book Prize Index.

Subscribe

Share

## Weekly links

•The making of the Jurassic Park computers.

• “Mill’s life has as much to teach here as his arguments. When he suffered that early breakdown, in 1826, it was because he lost faith in the pursuit of utilitarianism, his family creed. But he had no one he felt he could talk to about his crisis. His recovery, he said, came in part from reading Wordsworth. It came, too, from rejecting the psychological picture in which his father had raised him, a form of associationism that treated the mind as a mechanism for managing pleasure and pain, just as his father’s utilitarian ethics treated morality as a matter of maximizing the surplus of pleasure over pain. As he wrote inOn Liberty, human nature is ‘not a machine to be built after a model,’ but a living thing that must ‘grow and develop itself on all sides.’” —Kwame Anthony Appiah on AI and John Stuart Mill, whoseAutobiographyis one of the books that caught my attention in the open stacks.

• Mercifully, Pangram rates the Appiah essay as 100% human written… one can never tell these days. But apparently youcantell, sort of, on Substack — as I was preparing this post, I noticed thisnewly-added feature:

I have been skeptical in the past about software that claims to be able to detect AI writing, but I have to say, Pangram feels different. I’ve tested it and it’s dismayingly effective — dismaying because, as I wrote abouthere, alotof the writing people seem to like online these days is coming up as 100% AI. I’m glad Substack added this feature and I hope it pops up elsewhere, e.g., it would be interesting to see it automatically applied to the output of major news websites and magazines.

Leave a comment

Share

1

I had fun making theearly modern style colophon.

40
12
10
Share
Previous