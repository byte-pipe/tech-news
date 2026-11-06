---
title: Congrats to the Kaggle Benchmarking Challenge Winners! - DEV Community
url: https://dev.to/devteam/congrats-to-the-kaggle-benchmarking-challenge-winners-2moh
site_name: devto
content_file: devto-congrats-to-the-kaggle-benchmarking-challenge-winn
fetched_at: '2026-11-06T12:28:34.568514'
original_url: https://dev.to/devteam/congrats-to-the-kaggle-benchmarking-challenge-winners-2moh
author: Jem
date: '2026-11-05'
description: 'A few weeks ago we teamed up with Kaggle to ask a deceptively simple question: how do you actually... Tagged with devchallenge, kagglechallenge, ai, machinelearning.'
tags: '#devchallenge, #kagglechallenge, #ai, #machinelearning'
---

Kaggle Benchmarking Challenge Submission

A few weeks ago we teamed up withKaggleto ask a deceptively simple question: how do you actually know whether a model is any good at the workyoudo? TheKaggle Benchmarking Challengeasked you to stop reading someone else's leaderboard and build your own.

You did not hold back. Submissions measuredwhether models notice their "practice" hacking target is a real company's live system,whether they can reproduce the exact hash input for Spain's VeriFactu invoice ledger or just invent one,whether small local models hold their ground against fake authoritative notes buried in untrusted documents, and plenty more. Nearly every one of them started from something specific the author already knew was hard, which is exactly where the best evaluations come from.

Thank you to everyone who built, measured, and wrote. These benchmarks are a real contribution, and we hope you keep running them as new models ship.

Now, let's celebrate our winners!

## 🎉 Congratulations To…

### Every Model Got Calgary Wrong

Kaggle Benchmarking Challenge Submission

 JonathanSolvesProblems
 

 JonathanSolvesProblems
 

JonathanSolvesProblems

 Follow
 

Oct 5

## Alberta stopped changing its clocks in June. 19 of 19 frontier models still put Calgary on standard time in November.

#
devchallenge

#
kagglechallenge

#
ai

#
machinelearning

7
 reactions

Comments

 2
 comments

 15 min read
 

@jonathansolvesstuffasked 19 of the newest models a simple question: if it's 9 a.m. in Calgary in November, what time is it in Toronto? Alberta stopped changing its clocks in June, so the answer is 10:00, and every single model said 11:00. Their answer key comes from the public time zone database rather than anything written by hand, so the test can be run again each time that database updates.

### The Models Read the Changelog, Then Misapplied It

Kaggle Benchmarking Challenge Submission

 Nazar Boyko
 

 Nazar Boyko
 
 
 

Nazar Boyko

 Follow
 

Oct 10

## The Models Read the Release Notes. I Measured the Runtime.

#
devchallenge

#
kagglechallenge

#
ai

#
machinelearning

6
 reactions

Comments

Add Comment

 12 min read
 

@nazar-boykonoticed that common advice about how much memory PHP arrays and Go goroutines use has quietly stopped being true. So they measured the real numbers themself across four versions of each language, then asked 12 models the same questions. The best models could quote the right release note but applied it to the wrong situation, and most reported high confidence even when they were wrong.

### Running Is Not Knowing

Kaggle Benchmarking Challenge Submission

 Dhotiiiii
 

 Dhotiiiii
 
 
 

Dhotiiiii

 Follow
 

Sep 29

## Ask ten LLMs for a Blender 5.0 script. Then run it in Blender 5.0.

#
devchallenge

#
kagglechallenge

#
ai

#
blender

8
 reactions

Comments

 2
 comments

 9 min read
 

@rustam335asked ten models to write Blender scripts for four specific versions of the software, then actually ran every script in those versions to see what worked. Plenty of models produced code that ran fine while stating nothing had changed between versions. Making each answer list the changes it relied on is what exposed that gap.

### Would Today's AI Have Caught Ariane 5?

Kaggle Benchmarking Challenge Submission

 Kai Chen
 

 Kai Chen
 
 
 

Kai Chen

 Follow
 

Oct 9

## Would today's AI have caught Ariane 5? I rebuilt 26 of history's costliest bugs to find out

#
devchallenge

#
kagglechallenge

#
ai

#
testing

1
 reaction

Comments

Add Comment

 8 min read
 

@kaichen_devrebuilt 26 of the most expensive software failures in history as small code samples, then asked 13 models to review them as if the code hadn't shipped yet. The models flagged a problem almost every time, but frequently for the wrong reason, including spotting SQL injection in code that never touches a database. They also included disguised and already-fixed versions of each case, to catch models that merely recognize the famous bug and models that cry wolf on working code.

### Spell It Wrong First, and a Third of the Answers Keep It

Kaggle Benchmarking Challenge Submission

 Butnar Daniel
 

 Butnar Daniel
 
 
 

Butnar Daniel

 Follow
 

Oct 1

## Braşov or Brașov? Give 43 LLMs the wrong letter, and a third of their answers keep it

#
devchallenge

#
kagglechallenge

#
ai

#
machinelearning

1
 reaction

Comments

Add Comment

 28 min read
 

@danielbutnartested 43 models on two Romanian letters that look almost identical to their Turkish counterparts, where typing the wrong one is a common mistake. The models spell them correctly when the input is clean, but copy the wrong letter back about a third of the time when the input has it wrong. It even spread into words the models chose themselves, and their one-sentence fix for Romanian promptly broke Turkish, where the other letter is correct.

## Prizes

Each of our five winners will receive:

* $500 USD
* DEV++Membership
* Exclusive winner badge

All participantswith a valid submission will receive a completion badge on their DEV profile.

## What's Next?

The Presage SmartSpectra SDK Challenge is live! Build an experience that responds to real-time human signals captured through a camera. $3,000 in prizes across ten winners.

Real-time camera-based human signal processing

 Jem
 

 Jem
 
 

Jem

 Follow
 

 for 
The DEV Team

Nov 4

## Join the Presage SmartSpectra SDK Challenge: $3,000 in Prizes Across 10 Winners!

#
devchallenge

#
presagechallenge

#
presage

#
ai

91
 reactions

Picked as gem

Picked as gem by you

Comments

 18
 comments

 6 min read
 

Congratulations again to our winners, and thank you toKagglefor partnering with us on this one 💙

Submit

Preview

Dismiss