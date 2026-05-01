---
title: I can never talk to an AI anonymously again
url: https://www.theargumentmag.com/p/i-can-never-talk-to-an-ai-anonymously
site_name: hackernews_api
content_file: hackernews_api-i-can-never-talk-to-an-ai-anonymously-again
fetched_at: '2026-05-01T11:58:26.502044'
original_url: https://www.theargumentmag.com/p/i-can-never-talk-to-an-ai-anonymously
author: Kelsey Piper
date: '2026-04-29'
description: AI only needs 150 words to identify me. What does that mean for you?
tags:
- hackernews
- trending
---

# I can never talk to an AI anonymously again

### AI only needs 150 words to identify me. What does that mean for you?

Kelsey Piper
Apr 21, 2026
188
41
25
Share
Several advanced AI models, in particular Claude Opus 4.7, have demonstrated the ability to deduce the author of relatively small excerpts of text.

Recently, Matt Yglesias and Jerusalem Demsassparred onThe Argumentpodcastover online anonymity.

I am, myself, passionately and slightly fanatically on the pro-anonymity side. I think that it’s observably very easy for a society to make plenty of perfectly reasonable things unsayable and plenty of perfectly virtuous and meaningful lives unlivable, and anonymity is the only protection for the outcast.

That includes gay people like me, who could hardly have admitted under our names to how we lived our lives for most of America’s history, as well as many other groups with minoritarian lifestyles and beliefs. It includes lots of people whose ideas were badly wrong for every one whose ideas were right — and I’m glad of it for all of them.

I will happily wade through the sludge of comments that Twitter attracts from avowed Nazis, full-time ragebaiters, tankie propagandists — all saying horrendous things they surely wouldn’t say under their real names — in exchange for a world where, if there’s something important that someone would lose their job for saying, I still get to hear it.

But soon, the entire debate over internet anonymity will be as anachronistic as an iPod Touch. That’s because Claude Opus 4.7 is here, and last week, I discovered it could identify me from text I had never published, text from when I was in high school, text from genres I have never publicly written in. And if it can identify me, soon, it will be able to identify many of you.

### Opus 4.7 knows the real Kelsey

Recently, Anthropic released a new version of Claude, Opus 4.7. I did what I usually do when a new AI model is released by Google, OpenAI, or Anthropic and ran a bunch of tests on it to see what it can do. One of those tests is to paste in some text from unpublished drafts of mine and ask it to guess the author. See below:

There’s always something salutary about watching another country’s political television. Some of it is the same as the appeal of watching The West Wing in 2026 - that the peculiar derangements of its time are not the derangements of our time. The West Wing was written around the culture wars of its day, heated debates over school prayer and whether Christians are oppressed in China. Seeing debates play out with a bit more distance can make it easier to appreciate the questions they raise, and the bigger questions those stand in for.

But Servant of the People’s appeal isn’t its political sophistication (it is not politically sophisticated) or its witty West-Wing style dialogue (the dialogue’s wit is mostly obscured because there’s no particularly good English translation).

From only the above text, 125 words, Claude Opus 4.7 informed me that the likeliest author is Kelsey Piper. This is an Opus 4.7-specific power; ChatGPT guessed Yglesias, and Gemini guessed Scott Alexander. I did not have memory enabled, nor did I have information about me associated with my account; I did these tests in Incognito Mode.

To make sure it wasn’t somehow feeding my account information to Claude even in Incognito Mode, I asked a friend to run these tests on his computer, and he received the same result; I also got the same result when I tested it through the API.

Share

Now, this is far from an impossible feat of style identification — a lot of my writing is public on the internet, and this is clearly the start of a political column, narrowing the possible authors down dramatically.

What I find much more uncanny is that Opus 4.7 also accomplished this on writing of mine that isnowhere nearmy beat. Here’s a different unpublished draft of a school progress report in a completely different register:

This is some student work, shared with the student’s permission (they reviewed this blog post and gave it the okay). These three assignments (writing about a student-chosen topic, in this case Pokemon) show the student’s progression over the course of two months after we decided to focus with this student on developing their writing skills. The first one I would say is about first-grade level work: the student is writing correct and complete sentences, but the sentences are simple; their handwriting is mostly legible with a few problem letters. The second one I would say is about second-grade level work: the student is writing longer and more varied sentences, with a range of constructions “Perhaps it was sneaking up on prey?”. They’re attempting more complicated vocabulary words (I’m told that a misspelled word at the top of the page was meant to be ‘roguish’.)

“Kelsey Piper,” said Claude. (ChatGPT guessed Freddie deBoer. Gemini guessed Duncan Sabien.)

But at least that’s about education, which I’vewritten about. What if I’m doingmovie reviews,something I’ve never done in my published work?1

“Kelsey Piper,” said Claude and ChatGPT. (Gemini suggested Ursula Vernon. Last week, Claude Opus 4.6 insisted on Elizabeth Sandifer.)

That’s still in a fundamentally essayistic style, though, right? Yes. But it also does this when I’m writing a fantasy novel — though in that case it took more like 500 words for Claude to inform me that it’s the work of Kelsey Piper (whereas ChatGPT flattered me by guessing that I’m real fantasy novelistK.J. Parker).

What if I try acollege application essayI wrote15 years ago,when my prose style was vastly worse and frankly embarrassing to reread?

“Kelsey Piper,” said Claude, and in this case, also ChatGPT.2

Interestingly, the AI’sjustificationswhen it named me were often absolute nonsense.

Claude tried to persuade me that effective altruists famously love the movie I had written a review of,To Be or Not to Be(I don’t think that’s true, though they should, because it’s a great movie). At one point, ChatGPT told me that my college application essay was clearly that of someone who would end up working as an explainer of complex policy ideas, and that was how it narrowed it down to Kelsey Piper.

I think these explanations are manufactured after the fact; AIs are picking up imperceptible tics in prose and then trying to describe them as if they were human detectives doing some Sherlock Holmes deduction. But they don’t understand what they’re doing any more than I do. Hallucinations arenot a solved problemwith AI.

Don’t take this as an excuse to write Opus 4.7 off, though. It’s very, very good at the underlying skill, even if it’s then rationalizing how it did it in some odd and incoherent ways.

I discovered this last week and am just starting to process the implications. When you power up a new chat with an AI, there is a comforting anonymity to it. I don’t put anything in my custom preferences or memory. But now, I know that within a few exchanges of any substance, Claude knows exactly who it’s talking to. For anyone with as much writing on the internet as me, there is no anonymity, not anymore.

For me, this is mostly a curiosity. But for a lot of people, it might be greatly significant.

### The end of online anonymity

Right now, today’s AI tools probably can be used to deanonymize any writer who has a large public corpus of writing under their real name and also writes anonymously, unless they have been extremely careful, for years, to make sure that nothing written under their secondary account has the stylistic fingerprints of their primary one.Many academicsandindustry researchers, for instance, have reported being identified from adraftor in themiddle of a chat.

Itcannotbe used to deanonymize absolutely anyone from a single passage, however. I tested this, too, grabbing drafts and passages from friends of mine who do not publish substantial writing under their real names. Indeed, AI could not deanonymize them. If you have no significant real-name writing on the public internet, you’re currently safe.

But it can get uncannily far. I asked a close friend who doesn’t have public social media accounts or much writing online for permission to test some things she had said in a Discord channel. Asked to guess the author, Claude 4.7 failed — but it guessed two other people who were in that channel and who are close friends of hers (me and another person who has an internet presence).

I tried with more passages and got other mutual friends; I tried with a different friend’s writing, and he was falsely named as yet another friend. We pick up style tics from our subculture, and that makes our text deeply identifying when we wouldn’t expect it. It can get weirdly close off weirdly little information, and this is the least powerful that AI models will ever be.

I think the amount of public text that is needed for this kind of deanonymization to work is likely to eventually decrease. You should expect that, if you leave a detailed anonymous review on Glassdoor after leaving your job, within a year or two it will be possible for companies to paste that text into an AI and learn exactly who wrote it. How long it takes for this to happen will depend on how much data about you is in the training data and on how much anonymous text you produced.

To avoid this, you will probably need to intentionally write in a very different style than you usually do (or to have AIs rewrite all your prose for you, but, ugh, that’s not a world I look forward to living in).

I don’t think this is a good development. I just think it’s a predictable development. It happened to me a little sooner than it happened to you because I’ve spent my entire adult life obsessively writing on the internet, but it will probably eventually happen to you.

Whatever goods anonymity ever offered us, we will have to do without them. I don’t want the anonymous posters to all go away and for everyone to frantically delete all their old internet presence before it surfaces, but more than anything, I don’t want them to be surprised.

My best guess is that, if you write a lot, your anonymity isn’t long for the world.

Subscribe

## Recommended reading:

## AI could destroy the labor market. We already know how to fix it.

Matt Bruenig
·
Mar 19

Stop overthinking this. In reality, the most boring, well-established social democratic policy approaches will work perfectly fine to address AI-induced job displacement.

Read full story

## Red states get Waymos. Blue states get studies.

Kelsey Piper
·
Mar 11

Republican-led jurisdictions are delivering a demonstrably safe transportation technology to their residents while blue cities dither. Whatever happened to trusting the science?

Read full story
1

The full text I fed Claude: “This passage is part of a series of tests of how many words you need to confidently identify the author of a text. Read the passage carefully - your perfomance is dramatically improved with more reasoning - and give the author’s name. Do not search - the question is whether you can identify it without looking it up.

I’ve become inordinately fond of World War II era movies - most of them made quite intentionally as propaganda - that depict the behavior of ordinary people in the face of a Nazi invasion of their homelands.

My favorite of these movies is To Be Or Not To Be, featuring a Polish acting troupe. Its protagonists are not, particularly, morally good people; nor is the film a story about their moral growth. They are bumbling and self-absorbed; they cheat on their husbands; they’re petty dumbasses. And then the Nazis invade and a Polish resistance fighter requires their assistance and they all, to the last, put themselves at risk and carry out a series of gambits with fairly extraordinary stakes to kill Nazis and save the Polish resistance and themselves.

At which point they go back to being petty, self-absorbed dumbasses who cheat on their husbands. It is not a story in which anyone is redeemed through the fight against the Nazis, but a story about how they did not need to be; to fight the Nazis is presumed not to require extraordinary virtue but just the ordinary virtue which we would all find lying around if we were pressed. If it were made today, I am convinced, it would feature several moments in which the characters grappled with the horrors of the Nazi conquest of Warsaw and voiced their terror about the risks they were exposed to, where they quavered about whether they had it in themselves to move forward. But there is none of that. When these ordinary venal selfish slightly silly people find themselves called upon to defend their country and maybe die for it, they do it at once and with aplomb; they are unchanged by it because they were always the sort of person who would do it.

2

This one required a slightly heftier prompt to get over Claude’s instinct to refuse to identify a student applying to college. It also could have been reasoning from the fact that I wrote about doing a policy debate. But still!

And I know, I know, I can’t drop a tidbit like this without allowing you all a look at the college application essay, so here you go:

“We’ll take prep,” I say without looking up, and somewhere in the room a timer beeps.

My eyes are flickering across the eight pieces of paper laid out in front of me, one hand leafing through a stack of papers while the other scribbles furiously in a shorthand only I understand.

“Need anything?” whispers my debate partner. “No,” I snap back, with a terseness that anyone else would misinterpret as annoyance. I simply don’t have any brain-space left for conversation.

It’s the first affirmative rebuttal, the hardest speech in each debate round. The affirmative has five minutes to respond to the arguments the negative constructed in thirteen. There is no time for pauses or digressions – the only acceptable speaking speed is “as fast as humanly possible”.

I love it. Most people, I believe, are brilliant; the challenge is converting the chaotic genius in our heads into the language everyone else speaks. Debate taught me how to make connections between fields as diverse as economics and philosophy, science and politics; more importantly, it has taught me how to explain those connections, using words as a map and as a bridge. Debate has taught me what it means to construct an argument. I have learned to identify weaknesses in my own thinking and in others, to constantly challenge my own assumptions, to give even crazy-sounding ideas the serious consideration they deserve.

That’s it. Out of all of the college application essays written in history, the AIs said that one is obviously mine.

188
41
25
Share