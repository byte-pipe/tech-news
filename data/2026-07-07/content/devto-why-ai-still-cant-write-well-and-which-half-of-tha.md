---
title: Why AI Still Can't Write Well and Which Half of That Problem Is Actually Yours - DEV Community
url: https://dev.to/dannwaneri/why-ai-still-cant-write-well-and-which-half-of-that-problem-is-actually-yours-kh4
site_name: devto
content_file: devto-why-ai-still-cant-write-well-and-which-half-of-tha
fetched_at: '2026-07-07T19:36:53.231684'
original_url: https://dev.to/dannwaneri/why-ai-still-cant-write-well-and-which-half-of-that-problem-is-actually-yours-kh4
author: Daniel Nwaneri
date: '2026-07-06'
description: I built a 36-pattern checklist to catch AI writing tells in my own drafts, calibrated against... Tagged with ai, discuss, machinelearning, writing.
tags: '#discuss, #ai, #machinelearning, #writing'
---

A 36-pattern checklist for AI writing tells

I built a 36-pattern checklist to catch AI writing tells in my own drafts, calibrated against everything I've published. So when a theory aboutwhyAI can't write well went semi-viral last week, I read it the way I read a bug report: I wanted to know if the explanation actually matched the failure I was seeing in my own tool's flagged patterns, or if it just sounded right.

One of the theories didn't match. It's wrong, and it's the kind of wrong that spreads because it sounds technical enough to not get checked.

The claim: inference-time optimizations — the tricks labs use to make models respond faster — are why creative writing sounds worse than it used to. Specifically, speculative decoding.

Quick version of what that is, because the claim only sounds plausible if you don't know this part. Instead of one big model generating a response token by token, you pair it with a small, fast "draft" model. The small model guesses several words ahead; the big model checks the guesses in parallel and keeps the ones it agrees with. It's a shortcut for speed. The claim going around is that this shortcut quietly degrades writing quality.

It doesn't.Speculative decoding is built to be lossless by design— the output distribution is mathematically identical to what the big model would've produced generating alone, word by word. There's no quality trade happening anywhere in the math. What's real is narrower: creative writing benefitslessfrom the speedup, because high-temperature prose has more genuine surprise in it, so the small model's guesses get rejected more often.One inference-benchmarking writeupput creative-fiction guess-acceptance around 50-65%, versus 75-85% for code — not a peer-reviewed number, but it lines up with how the technique works. That's a story about how much faster your writing gets served, not about how good it is.

Quantization — shrinking a model's precision to save memory — can genuinely hurt output quality. Real, separate lever. But it's not the same thing as speculative decoding, and I watched people conflate the two for a full afternoon before anyone pushed back.

The part that actually holds up isn't the part people were arguing about.

Every major model goes through a training step called RLHF — reinforcement learning from human feedback — where it gets nudged toward responses that human raters rated highly. Sounds fine until you notice what raters actually reward: responses that are pleasant to skim, hard to disagree with. Over enough training, the model doesn't just get better at avoiding bad answers. It narrows toward one "safe" register and stops producing the wider range of responses it was originally capable of. That's called mode collapse, andKirk et al. measured it directly: RLHF-trained models show meaningfully lower output diversity than the same models before that training step, across every metric in their study.

This is why the "ten drafts, then a panel of models grades and picks the best parts" trick doesn't work, and I know because I've run some version of it myself. If every draft came from a model that already narrowed toward the same safe average, grading and merging those drafts just averages the average. You don't escape mode collapse by voting inside it. You get the same failure, run twice, dressed up as rigor.

Writing has no equivalent to "the code compiles." There's no automatic checkable signal for "this is insightful," so training has nothing to push against except rater preference — and rater preference, in bulk, rewards smooth and safe over sharp and specific. That's the actual bottleneck: the training incentive itself, not the prompt, not the inference trick.

Once you name mode collapse, it's tempting to treat "AI can't write well" as one flat, unsolved problem. It isn't. It splits into two, and I write in the easier half without having fully clocked that until this week.

Nonfiction — technical writing, essays, arguments — has a nameable failure mode: conflicting optimization objectives. The traits that make a model pleasant in consumer chat (warm, hedged) are directly at odds with what good technical writing needs (precise, willing to be blunt). One reward signal, trying to serve two audiences that want different things, so the model gets pulled toward the middle of both and satisfies neither. That's a solvable engineering problem, the same way you'd split an API endpoint that's trying to serve two incompatible callers. Not fully solved, but there's already public evidence of labs shipping partial fixes aimed at exactly this (OpenAI's November 2024 GPT-4o writing updateis one example).

Fiction is a different kind of hard, and I don't think it's mine to weigh in on with any authority. A good novel gets built over years of iteration on structure and character, closer to how Pixar's story team reworks a film's plot for years before a single frame gets animated. Published novels only show the finished result. The failed drafts and the years of restructuring never got kept as training data. Even if that data existed, there's limited economic incentive to solve it yet, because "does this novel move a reader emotionally over 300 pages" isn't something you can currently measure the way you can measure "does this code pass its tests."

Update (Jul 7): a sharper version of this argument surfaced after this went up, worth naming honestly. The "no training data for the process" framing has a real hole — finished novels already exist in these training corpora by the millions, so a lack of raw text isn't the bottleneck. Models like GPT-4.5 and Llama 3.1 405B suggest pretraining alone can already produce genuinely strong long-form prose. The likelier story: post-training optimization (RLHF and shrinking parameter counts chasing efficiency) is actively degrading a capability that already existed, not filling a gap that was never there. Doesn't change the nonfiction half of this piece. Does mean the paragraph above needs a rewrite I haven't done yet.

Two different problems, wearing the same complaint. One has a name and a rough fix already shipping somewhere. The other doesn't have a dataset yet, or a business case to build one.

I only write the first kind. Tutorials, arguments built from things I've actually built and broken. That puts me on the solvable side of this line, and for most of the week I was following this argument, I didn't separate that from the harder, maybe-unsolvable half everyone was actually upset about.

"Solvable" doesn't mean "solved," though, and the fix that exists today isn't a model retrain I have access to. It's an editing pass. Which is the actual reason I builtthat 36-pattern checklistI mentioned at the start — calibrated against my own published work specifically so it can't smooth my sentences toward a generic "good writing" average. There's no average in it to smooth toward. Just my corpus. It doesn't generate the underlying argument for me. Nothing does that yet, and nothing should. What it catches is the RLHF hedge-language creeping back in after a draft is written — the sentence that trails off into a comma and an "-ing" clause instead of just ending, the vague "many people" claim that should name someone instead.

I'm not claiming AI writing is solved. I'm saying I spent a week watching smart people argue about a math claim that turned out to be checkable in about ten minutes, and the actual fix for my half of the problem was something I could run on a draft that same afternoon.

AI helped me research, structure, and edit this piece. The arguments, the examples, and the opinions are mine. So is whatever's wrong with them.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (22 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse