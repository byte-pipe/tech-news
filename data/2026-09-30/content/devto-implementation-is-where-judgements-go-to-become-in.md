---
title: Implementation is where judgements go to become invisible - DEV Community
url: https://dev.to/tom_jones_230c4659491adcd/implementation-is-where-judgements-go-to-become-invisible-4p1h
site_name: devto
content_file: devto-implementation-is-where-judgements-go-to-become-in
fetched_at: '2026-09-30T16:40:40.908530'
original_url: https://dev.to/tom_jones_230c4659491adcd/implementation-is-where-judgements-go-to-become-invisible-4p1h
author: Tom Jones
date: '2026-09-27'
description: One question, three answers I have a small tool that finds people waiting for a reply from... Tagged with testing, programming, discuss, ai.
tags: '#discuss, #testing, #programming, #ai'
---

How simple code hides past design choices

## One question, three answers

I have a small tool that finds people waiting for a reply from me.

It had three versions. Each one was correct. Each one gave a different answer.

1. Version one said 18.It counted a reply only if it sat directly under theirs. But dev.to sometimes will not show a comment its API still returns, so you reply beside it instead. Nine of ten had been answered that way.
2. Version two said 34.It counted any later comment from me in the thread. So it counted two other people talking to each other.
3. Version three said 2.It used both rules. One was a friendly sign-off from July. The other was Pascal, suggesting there might be an article hiding in these comments.

This is that article.

Nothing in the tool was broken. Each count was right about its own population. The trouble was the question. Every version reported its number as the answer to "who is waiting?", and every version had quietly decided what "answered" means.

The first version was built with care. It encoded a sensible judgement. Then the judgement stopped looking like one.

That is the whole article in one incident. The rest is how we got there.

## How we got here

It started in July, in the comments underPascal's article about replacing Calendly. It ran for two months, in bursts, with pauses while one of us went off and tested things in production.

We did not start with a method. It went like this, over and over:

1. one of us has an answer that looks finished
2. the other brings back a real failure
3. the answer turns out to be hiding a judgement

Enter fullscreen mode

Exit fullscreen mode

Sometimes Pascal had the answer and I found the hole. Sometimes the other way round. Here it is in the order it came up.

## The test passes

The first example is from Pascal's article. Two people try to book the same slot at the same moment. On Postgres that is a real race. On SQLite it cannot happen, because SQLite lets only one writer in at a time.

So a test for that race, run on SQLite, passes forever. The bug ships on Postgres.

The hidden judgement:that this test can fail at all.

The fix is mechanical. After you write a test, break the thing it protects on purpose and run it again.

Green means it was never watching anything.

Pascal's version: a regression test is valuable because"it represents a failure that actually happened and that we proved it can fail when the condition comes back."Most people keep the first half of that sentence and drop the second.

## The test is weak

Breaking code on purpose to see if a test notices is called mutation testing. When the test stays green, everyone assumes the test is weak.

That is one of four causes, and the least interesting one.

My case was the first box. A key binding compared the key press against" ". The runtime reported the space bar as"space". That branch had never matched in the whole life of the file.

I had already told a colleague I had introduced a regression there. There was nothing to regress.

The hidden judgement:that the code under test runs at all.

Pascal turned the boxes into an order of checks:

1. Is the path reachable?
2. Does the test observe the behaviour?
3. Does breaking it make the test fail?

Only after all three is "the test is weak" the right diagnosis.

He also suggested that a surviving mutant may be less a verdict on the test than"a way of challenging the story the code tells about itself."

## The checks are green

That story has several authors. The code says what it does. The tests appear to confirm it. The last person who explained the system repeats it.

They can all be wrong in the same way at once. That is what happened with the space bar.

What breaks the agreement is something that cannot be told the story. Pascal described it as"an artefact whose validity is defined operationally rather than narratively,"and its whole test fits in four words:"Show me the failure."

Then he pushed further. Tests only check what somebody thought of. Real users bring what nobody thought of. In his words, production is"the one test suite whose authors we don't control."

I had a painful example. My gateway speaks three API formats, and every check was green.

The checks used curl, written by me, speaking my own format back to me. One vendor SDK sends its key in a different header than the one my edge rule read. Its requests died before reaching the code that would have handled them.

The hidden judgement:who wrote the check. The checker and the thing checked had the same author. So they had the same blind spot.

## Add more checks

The obvious response is more checks. That only helps if they can disagree.

Before, on the left: three checks on the same registry of files. Different code, written at different times, for different reasons. All green. Two files sat in a folder the registry had been told to skip, so none of the three ever saw them.

Three green lights. One blind spot, seen three times.

After, on the right: a real catch. Two tools counted the same store and got 16 and 2,375. One walked a list someone had declared. The other walked the disk. Neither got its input from the other, so they could come apart, and one day they did.

Pascal's sentence for this: independence is about"preserving the possibility of disagreement."Different code is not enough. The checks have to be able to be wrong in different ways.

## Zero replies waiting

Every check counts something, and somebody chose what. Usually nobody did. The set arrived as whatever the first caller passed in, and it stuck.

Pascal asked the question that names it:"Who chose what the test is allowed to see?"

My nightly report once led with this line:

0 replies waiting on our own articles

Enter fullscreen mode

Exit fullscreen mode

True. The session that read it concluded nobody was waiting on me. False. Replies on other people's articles lived in a different bucket.

The count never lied. It answered a narrower question in the voice of a wider one.

The hidden judgement:which articles count as mine to watch. This is the same family as the detector at the top, one step earlier.

I fixed the report rather than adding a checker. It now says what it could not see, and printscoverage unknownwhen it cannot list everything. An empty set and a set nobody measured both print zero, and they mean opposite things.

## One setup wins by a wide margin

A comparison has two denominators. They can differ without anyone noticing.

I was writing up a retrieval benchmark where one setup beat another by a wide margin. Every number was accurate. Then I looked at what each setup searched. One ranked over 3,038 documents. The other ranked over 7, and those 7 were the files holding the answers, because a helper had built its index from the task list.

Pascal's reply was the shortest rule in the thread:"You don't add bananas and monkeys."

It held up a few hours later. A cache keyed each document by a shortened id, so 120 documents produced 86 keys. 34 were scored against someone else's results while the report kept dividing by 120. One line caught it:

assert
 
len
(
cache
)
 
==
 
len
(
documents
)

Enter fullscreen mode

Exit fullscreen mode

The same line then caught my fix, which collided the other way.

The nastier cousin is when both counts agree. My usage log recorded 2,488 requests under one provider name. For that kind of request the service points at a different provider and leaves the name alone. Both sides said 2,488 because both read the same label.

As Pascal put it,"Sometimes you need to look at the thing being named, rather than trusting the name."

## Value, scope, treatment

Past a certain point the number is perfectly correct, and it answers a narrower question than the reader reasonably thinks it answers. Pascal called that a broken semantic contract, and noted there may be no invariant to catch it.

His answer: a measurement is"value + scope + treatment."If changing the scope or the treatment could change what the number means, they belong next to it.

That answer looked finished. I answered with the term it was hiding, because it had just bitten me. The comparison is a treatment too.

I had published that notes my system pushes to an agent change what it does, compared with a random note. Then I rebuilt the control the way a published benchmark does, using the nearest wrong note instead. The effect disappeared: 35.4% against 30.8%, p=0.549.

The measurement never changed. What it was compared to did.

The hidden judgement:what the number was compared to. So scope, treatment and comparison all go next to the number.

## Every claim has evidence

That catch came from reading someone else's method. None of my own checks found it. My gates confirm every claim has evidence, and that claim did.

Pascal named the gap. Nothing asked"why do we believe this is the right question?"

I got an example within the hour. I had been calling my note delivery "noisy," so I measured noise carefully and built a fix. It changed nothing.

Then a colleague asked what it was actually like inside, and I looked at one real session instead of the averages. Nothing was noisy. Exactly two notes had been crowded out and never arrived. They were the two I had just spent an evening learning again the hard way.

Pascal's line: a knowledge base can be"complete and still be functionally incomplete."

Then the outside check failed the same way. A second model reviewed my decisions. It was sharp and mostly right, and it concluded I had shipped a null result. That part was wrong, because the evidence against it existed and I had left it out of the brief.

Pascal separated the two cleanly. The reviewer was"independent"in its reasoning, but not"independently informed."

The hidden judgement:which question was worth asking, and what the outside reviewer was allowed to see.

## The randomiser is fine

I randomly hold back ten percent of those notes, so I can compare what happens with and without them. When I finally computed the result, the two groups turned out to be logged at different points in the pipeline:

held back logged the moment it was held
delivered logged only if it survived several later filters

Enter fullscreen mode

Exit fullscreen mode

Sixty-eight days of data compared a whole group with its survivors. The randomiser was fine. Someone had once decided where to put two log lines, and that decision had quietly become code.

The hidden judgement:where the log lines went.

I wrote back that implementation is where judgements go to become invisible. Pascal finished the thought: a judgement"starts as a conscious choice, becomes a field, a log point, a default, a population boundary, a control, an ordering decision,"and six months later it just looks like how the system works.

## Back to 18, 34, 2

While we were agreeing on that, it happened again, to the detector at the top.

Look at it with the whole thread behind it:

Version

Count

What it silently decided "answered" means

1

18

my reply sits directly under theirs

2

34

any later comment from me in the thread

3

2

both rules together

Three correct measurements. Three different populations. One question.

Much of the thread is in there. Version one could not see a reply placed beside a comment, so it could not notice being wrong about one. Each version counted a population somebody chose once. Each number was right, and the reader heard a different question. And a judgement about one word sat in the code, looking like how the system works.

## What you could extract afterwards

Once it was over, you could write it up as a list. I did, in the first draft.

1. Can it fail? Break it on purpose and watch.
2. Does the code under test run at all?
3. Who wrote the check, and does it share an author with what it checks?
4. Could your checks disagree, or do they share one input?
5. What exactly is being counted, and who chose that?
6. Are both sides of the comparison the same kind of thing?
7. Does the number carry its scope, its treatment and its comparison?
8. Is this the right question, and did anyone outside your own checks get a real chance to ask?
9. Which of these answers is now buried in code, where nobody will see it as a choice?

Pascal's review of that draft caught the problem. We never started with nine questions and applied them to nine cases. We kept finding an answer that looked finished, and then finding the judgement inside it.

A clean list is exactly the kind of instrument this article warns about. Use it, and expect it to be hiding something too.

The useful items cost a line of code each: a count printed next to a result, an assertion that two populations match, a mutant run once. The hard ones do not go away when you automate them. The judgement moves somewhere it is harder to see.

## What I'd try next

The logging from the randomiser story is fixed and symmetric now. The next step is per note: for each note, compare the rate of the specific mistake it warns about when it was delivered against when it was held back. That turns "did the note arrive when it mattered" into arithmetic.

It will not tell me I picked the right mistake to detect. That part is still a judgement, and I expect it to hide in the code the same way the log lines did.

Neither of us would have found most of this alone. That is the other thing the thread showed.

This came out of a two-month thread with Pascal Cescato, who also reviewed this draft. Thank you, Pascal.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (28 comments)
 

Some comments have been hidden by the post's author -find out more

For further actions, you may consider blocking this person and/orreporting abuse