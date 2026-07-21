---
title: Human mathematicians are being outcounterexampled | Xena
url: https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/
site_name: hackernews_api
content_file: hackernews_api-human-mathematicians-are-being-outcounterexampled
fetched_at: '2026-07-21T11:37:23.805453'
original_url: https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/
author: artninja1988
date: '2026-07-20'
published_date: '2026-07-20T09:53:22+00:00'
description: It's been an interesting few weeks for counterexamples. This post is basically my perspective of what has been going on in the world of formalization, AI tools and, in particular, counterexamples. Unit distance Two months ago today (20th May 2026), ChatGPT disproved Erdős' Unit Distance conjecture in discrete geometry. This is now old news but…
tags:
- hackernews
- trending
---

## Human mathematicians are being outcounterexampled

Posted on
 
July 20, 2026
 
by
 
xenaproject
 

It’s been an interesting few weeks for counterexamples. This post is basically my perspective of what has been going on in the world of formalization, AI tools and, in particular, counterexamples.

## Unit distance

Two months ago today (20th May 2026), ChatGPT disproved Erdős’ Unit Distance conjecture in discrete geometry. This is now old news but I had to start somewhere. Theannouncementwas accompanied with testimonies by human mathematicians, many of whom I knew and a few of whom I trusted, saying that they believed the argument (they had been given early access to it and had checked it). The basic structure of the proof is that a profound theorem in number theory due to Golod and Shafarevich from the 1960s could be used to construct a counterexample to the conjecture.

It is now 9 years since I had a mid-life crisis, realised I no longer trusted many human mathematicians when it comes to technical details, discovered Lean, and started to argue that interactive theorem provers should play an important role in the future of mathematics. So of course my first question was “is the counterexample formalized in Lean”. The answer was “no”.

But under a week later (26th May 2026), I got an email from Fields Medallist Mike Freedman. Mike is now the Chief Science Officer forLogical Intelligence, a company cofounded by Turing Award winner and “godfather of AI” Yan LeCun. Mike informed me that their system had autoformalized the entire ChatGPT-generated paper in Lean and could I take a look. I looked, and my post-doc Thomas Browning looked too. And indeed this was what Logical Intelligence had done: they had formalized precisely the statement that the profound theorem of number theory implied the Erdős counterexample. Breakthrough LLM-generated mathematics being formalized in real time. Interesting data point.

Of course there is an elephant in the room here though, the profound theorem of number theory which takes 100+ pages to prove (it needs huge chunks of global class field theory, a theory developed at the beginning of the 20th century and for which there are still no short proofs; it is proving difficult to compress). In 2025 I had run aClay Summer Schoolwith Richard Hill on the formalization of class field theory, and one year later we have nearly done the local case (it is the current PhD project of my student Edison Xie); the global case remained open, and indeed in 2025 formalizing global class field theory seemed like a fantasy.

One month later, on June 26th 2026, my perception of what was possible again changed. Boris Alexeevannounced on the Lean Zulipthat he had steered ChatGPT to a complete formalization of the Erdős counterexample, assuming nothing beyond the axioms of mathematics. Boris works at OpenAI and had used their new model Sol to do the autoformalization. Boris made the code public and it did not take long for me to realise that somewhere within all this AI-generated (and sometimes horrible, although sometimes decent) code was indeed a proof of some really hard theorems in global class field theory. Also of interest to me was that Sol had generated 1.2 million lines of Lean code in the three weeks that it had worked on the project. Lean’s fantastic (declaration of conflict of interest: I am a maintainer) mathematics librarymathlibis only 2.3 million lines of code, and took nine years to write. Perhaps it was at this point that the penny really dropped for me — large AI-generated developments of mathematics are inevitable. One cannot trust AI-generated code so I ran it in a sandbox on my machine (malicious Lean code can run arbitrary commands on your computer — Lean is a programming language, after all). Indeed, it was proving nontrivial theorems about the cohomology of number fields. Wow.

## Group schemes of order n

A week after Boris’ revelation, in early July, I was thinking hard about how to run myFormalizing Fermat workshop. This workshop was sponsored byLogos Research, who, like Logical Intelligence (and Harmonic and Axiom AI and Moonshot AI and…) have a tool which can autoformalize mathematics — translating it from human language into Lean — building on mathlib. Logos told me that they were only going to allow 5 people at a time to use their system during the workshop, and there were 25 attendees, so I told all attendees that I would buy them a Claude Max subscription for a month, so they had something to experiment with when it wasn’t their turn for Logos’ tool. The workshop was 6th to 10th July, and the Claude Max subscription would give attendees access to Claude Fable, at least until Tuesday 7th, when it was being switched off. When OpenAI got wind of what I was doing, they also offered all attendees free ChatGPT Pro access for a month; this was a big deal because ChatGPT Sol was coming out on the 9th. So basically all attendees would have access to Sol and Fable for 4 out of the 5 days of the workshop, and Logos’ tool for the entire week. In fact Fable access was not removed on the 7th so we were in even better shape.

I was not sure how good Logos’ tool was going to be, but I wanted a development of the theory of finite flat group schemes in Lean for my ongoing proof of Fermat’s Last Theorem, so I put uploaded some classic papers in the area to Fable and ChatGPT, and got them together to write down an exposition of the theory in natural language. I passed this pdf document over to Logos the day before the workshop, and on the first day of the workshop they said that one of the claims in the pdf was false and they had found an explicit counterexample. Another counterexample! I took a look and indeed the LLM-generated pdf was simply wrong at some point when describing a standard construction; false alarm. I had missed this myself though when reading through the pdf. Interesting how AI had again found a counterexample. I fixed the pdf. I thought it was interesting that the AI didn’t just say “I don’t quite follow this argument”, it instead said “here is a proof that this argument is simply wrong”, a much more powerful statement.

With the development of the theory of finite flat group schemes back on track, I could relax back into the FLT workshop. On Tuesday 7th July I sat oppositeAkhil Mathewat lunch; Akhil is a professor of mathematics at UChicago and he was an attendee who had been experimenting with the tools available. We talked about potential questions which AI could work on, and Akhil raised the old question of Grothendieck about whether every finite free group scheme of order n was killed by n. Deligne had proved the result in the commutative case, and Grothendieck had proved it when the base was reduced; Rene Schoof had proved it in more cases, and there had even beena paperby Emiliano Torti published last year, proving it in even more generality. I said that I thought that this was a fabulous thing to get AI thinking about.

The day after the workshop finished, on Saturday 11th July, I got a DM from Akhil telling me that Sol had found a counterexample. He sent me a 12 page pdf. I immediately replied saying that I was not reading AI-generated informal mathematics and could he please formalize the entire thing in Lean. Four hours later he replied again, saying that Fable had autoformalized the entire thing. I scanned over the 1076-line Lean file, checking that the code did not delete all the files on my hard drive (Lean is a programming language, so it can do this). Convinced that it was only theorems, I then compiled it on my laptop and it took me under 5 minutes in total to check that (a) thestatementof the claimed theorem used only concepts in mathlib (and thus things likeHopfAlgebracan be trusted to mean what mathematicians think of as Hopf algebras) (b) the statement of the claimed theorem was that there was a counterexample and (c) the proof compiled. At this point I knew that we had a counterexample — a group scheme of order 4 which was not killed by 4. I suggested to Akhil that he make a PR to mathlib with the counterexample — whichhe did. I would have also suggested to him that he draft a press release saying that a machine had solved a 60-year-old question of Grothendieck in algebraic geometry, but somehow by this point I was almost becoming immune to all of this. It wasn’t clear to me that the media would even be able to distinguish between “machine resolves question due to Erdős” and “machine resolves question due to Grothendieck” even though I personally found the latter far more interesting. Of course the Grothendieck counterexample was far far easier than the Erdős one (a thousand lines, not a million), all I’m saying is that it’s an area of mathematics that I personally find more interesting. I pointed out to Akhil that machines seemed to be getting very good at finding counterexamples and suggested that he try the Hodge conjecture next.

## Modularity lifting theorems

I think it’s worth stepping back at this point and surveying what the attitudes of human experts to these sorts of things are. On Tuesday (14th July) I went to work at Imperial and the Grothendieck counterexample was the talk of lunch. A member of the faculty (who I won’t name) said to me that the fact that the counterexample was so easy to find just indicated that humans had not spent enough time thinking about the problem, implying that a 60-year-old question of Grothendieck was not actually that interesting to work on. I didn’t tell him that at some point earlier in my career I had spent a week working hard on the problem. In my mind my colleague is just going through the five stages of grief; right now they seem to be in the denial phase.

After lunch I met with my PhD student Andrew Yang, who had been working on formalizing a modularity lifting theorem in Lean, something which is crucial to my FLT work. Andrew had come to the Logos FLT workshop and now had access to both Sol and Fable. He told me that using these tools he had written 250K lines of Lean code which basically completely finished the project in what was I guess a 2 week period.

A few days earlier I had got an email from a professor in the maths department here at Imperial, expressing surprise that some of our graduate students were paying $200 per month to access models such as Sol and Fable. He said that he thought that these people were crazy. I did not immediately respond. But after meeting with Andrew I emailed the professor back and told him that in my opinion, any PhD student who wasnotpaying $200 per month to access these tools was crazy. In fact during the workshop I learnt from Harvard PhD student Bryan Wang that Harvard were already giving free Fable access to all PhD students, post-docs and faculty at Harvard.

## The Jacobian Conjecture

But back to Akhil. I am not sure if he took my idea to disprove the Hodge conjecture seriously. But it looks like he had deeply understood that, with these extraordinary new AI tools, counterexamples might be low-hanging fruit right now. He had discussed with Levent Alpöge the idea of finding more counterexamples in algebraic geometry, and 12 hours ago Leventposted on Xthat Fable had found a counterexample to theJacobian Conjecture. This is a big deal — this is a famous question in algebraic geometry which had been open for 100 years and which many people had thought about. It was apparently solved during the 2026 World Cup Final.

I woke up today to a DM from Akhil saying “shall I make another PR?” but this time he was too late — Paul Lezeau had already formalized the counterexample manually and hadmade a PRto DeepMind’sFormal Conjectures repo. Mathlib does not contain a large list of conjectures in mathematics, but DeepMind’s repo does. The importance of formalization of conjectures by humans is that if humans are agreed that a Lean statement does faithfully capture the idea behind a conjecture, then checking that (possibly AI-generated) Lean code does comprise a proof or disproof of the conjecture is a triviality. Congratulations to Levent, thanks to Akhil for suggesting the problem to him, and thanks to DeepMind for already having formalized the statement and thus making formal verification of the counterexample a triviality.

The Jacobian conjecture is resolved! Wow! The next step in that work is for humans to understand exactly what is going on with the example. For the true value of work like this is to give humans better understanding of mathematics. Indeed Akhil has been working on trying to understand the Grothendieck counterexample in a way which is far deeper than “here is a random presentation of a random ring and a random calculation which shows that something doesn’t work”. What we need next is the insight which can be drawn from these extraordinary examples.

What a time to be alive.

### Share this:

* Share on X (Opens in new window)X
* Share on Facebook (Opens in new window)Facebook
Like
 
Loading...

### Related

 

 

## About xenaproject

							The Xena Project aims to get mathematics undergraduates (at Imperial College and beyond) trained in the art of formalising mathematics on a computer. Why? Because I have this feeling that digitising mathematics will be really important one day.							

									View all posts by xenaproject 
→
 

							This entry was posted in 
Algebraic Geometry
, 
Fermat's Last Theorem
, 
Machine Learning
, 
Research formalisation
 and tagged 
AI
, 
Artificial Intelligence
, 
counterexample
, 
counterexamples
, 
Grothendieck
, 
group scheme
, 
Jacobian Conjecture
, 
lean
, 
math
, 
mathematics
, 
philosophy
, 
science
, 
technology
. Bookmark the 
permalink
.													

### 10 Responses toHuman mathematicians are being outcounterexampled

1. yssays:July 20, 2026 at 3:55 pmDear Kevin,Thanks for this article. You write that you are “not reading AI-generated informal mathematics” but also that “the next step in that work is for humans to understand exactly what is going on with the example.” How do we do this without reading the informal AI output? We are surely not going through a thousand-line Lean file?LikeLikeReply* David Jaosays:July 20, 2026 at 8:05 pmI actually find it easier to go through the formal output than the informal output. With the formal output, there is no danger of imagining things or misinterpreting the argument. Most reasonable Lean developments are organized into logical progressions of lemmas, and most of the lemmas might even be obvious to someone well versed in the field (who can also read Lean, of course), leaving only a small amount of actual argumentation to read.LikeLikeReply
* Tanay Wakharesays:July 21, 2026 at 3:13 amParsing through so much LLM and Lean output is exactly the bottleneck I think is coming this year. We’re going to be dealing with two huge issues going forwardsAn overload of LLM generated proofs (which are error prone, as noted in the post)A need to check Lean code (much of which will be written by LLMs)For newcomers to Lean especially, the bigger risk imo is formalizing something different that what they thought they were formalizing.Both of these are fundamentally a UI/UX problem about how human mathematicians will deal with information overload and it’s exactly what we’re addressing athttps://mathvision.ai/🙂 Check it out for free if you’re interested.LikeLikeReply
* An overload of LLM generated proofs (which are error prone, as noted in the post)
* A need to check Lean code (much of which will be written by LLMs)
2. jeanabousamrasays:July 20, 2026 at 5:24 pm“A few days earlier I had got an email from a professor in the maths department here at Imperial, expressing surprise that some of our graduate students were paying $200 per month to access models such as Sol and Fable. He said that he thought that these people were crazy. I did not immediately respond. But after meeting with Andrew I emailed the professor back and told him that in my opinion, any PhD student who wasnotpaying $200 per month to access these tools was crazy.”With due respect, I find this comment disgusting. Among other problems, this money will be used for the gigantic V-sign to future generations that is building lots of extra gas power plants to supply new data centers. I won’t judge people for doing it any more than for eating red meat, and especially not in such a toughly competitive academic system, but if you think it’s crazynotto give 10% of your salary to unethical companies if it might hurt your career, then we are fundamentally not operating on the same set of values.LikeLiked by2 peopleReply* Yemon Choisays:July 20, 2026 at 7:50 pmWith the caveat that the internet and years of social media encourage us to make kneejerk responses, my instinct is to concur with JAS’s comment/reply. Aside from views one may (or may not) have about the companies building and selling these tools, the sentiment that Kevin candidly admits to is not a mentality that I want to see encouraged among those doing a PhD.LikeLikeReplyalpacadeliciously52e6be6b27says:July 20, 2026 at 8:02 pmThere are possibly political or social welfare reasons why one should resist the AI takeover of mathematics. But, from a strict utilitarian standpoint, these tools make you much more than 10% more productive, and are well worth the cost.I worry about the social implications of handing over a large portion of our resources to AI companies, and the equity and access concerns for people from countries where $200 is a lot of money. Also, there is evidence that AI companies are subsidizing the present cost of subscription access and that the true cost is much higher than what we pay.But, for now, if you’re a graduate student at Harvard or Imperial, the economic argument is persuasively in favor of spending the money to subscribe to AI.LikeLike
* alpacadeliciously52e6be6b27says:July 20, 2026 at 8:02 pmThere are possibly political or social welfare reasons why one should resist the AI takeover of mathematics. But, from a strict utilitarian standpoint, these tools make you much more than 10% more productive, and are well worth the cost.I worry about the social implications of handing over a large portion of our resources to AI companies, and the equity and access concerns for people from countries where $200 is a lot of money. Also, there is evidence that AI companies are subsidizing the present cost of subscription access and that the true cost is much higher than what we pay.But, for now, if you’re a graduate student at Harvard or Imperial, the economic argument is persuasively in favor of spending the money to subscribe to AI.LikeLike
* kenhchansays:July 20, 2026 at 7:57 pmyou should inform your opinion on actual numbers, data centers use a small fraction of electricity and water compared to, say agriculture. so if you’re the kind of person who judges people for eating red meat, you need to dish out that judgement proportionally for AI users.i’ve given the exact same advice to graduate students months ago, pay for the best models, especially now that they are still affordable. contribute to proving the use case (at this point, is there even any doubt?), and get your department / advisor to pay for the models going forward.LikeLikeReply
3. Anonsays:July 20, 2026 at 5:55 pmidk if this is satisfactory but here’s how GPT interpreted the Jacobian example. Take P1xP2->P3 (Union of divisors on P1 say), remove ramification locus and remove a hyperplane of P3 which is tangent to a point of the map P1->P3 (tripling the divisor) but not osculating (multiplicity exactly two). Then the preimage is A3 by direct computation.LikeLikeReply
4. Yemon Choisays:July 20, 2026 at 7:55 pmOn a more constructive note than my previous comment/post: in the hope that some people who follow this blog as part of their interest in/commitment to formalization are also interested in understanding algebraic geometry, I want to give a signal boost tohttps://sbseminar.wordpress.com/2026/07/20/the-new-counterexample-to-the-jacobian-conjecture/so that some maths discussion takes place there.LikeLikeReply
5. Madeleine Birchfieldsays:July 21, 2026 at 12:09 amA pretty important set of philosophical questions: what is the point of mathematics and the role of mathematicians when the task of formally proving conjectures has been outsourced to a team consisting of a large language model and a proof assistant? What’s the point of mathematical rigour when mathematicians no longer have to develop and write proofs out by hand?I feel like whatever remains of the formalist viewpoint of mathematics has been largely disproven by developments in the past few years in artificial intelligence and proof assistants: clearly there are still activities for mathematicians in an era where large language models are the ones writing formal proofs in a proof assistant.LikeLikeReply

### Leave a commentCancel reply

Δ