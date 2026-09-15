---
title: The Slow and Quiet Cognitive Atrophy of a Modern Software Engineer - DEV Community
url: https://dev.to/codingwithjiro/the-slow-and-quiet-cognitive-atrophy-of-a-modern-software-engineer-3lbh
site_name: devto
content_file: devto-the-slow-and-quiet-cognitive-atrophy-of-a-modern-s
fetched_at: '2026-09-15T21:56:17.896583'
original_url: https://dev.to/codingwithjiro/the-slow-and-quiet-cognitive-atrophy-of-a-modern-software-engineer-3lbh
author: Elmar Chavez
date: '2026-09-15'
description: Over the past couple of months, I've read a lot of articles about the consequences of AI dependency... Tagged with software, ai, programming, productivity.
tags: '#software, #ai, #programming, #productivity'
---

The danger of skipping your own Step 1

Over the past couple of months, I've read a lot of articles about the consequences of AI dependency and one prominent finding iscognitive atrophy. In other words, it's about suffering from gradual skill decay because of over-reliance on AI.

Most of the realizations involvenot solving the problem directly. Software engineers instinctively ask AI what to do first instead of thinking of a solution themselves. This means skipping the crucial process ofthinking. This is primarily why I chose the banner above:The Blind Leading the Blind (1568)byPieter Bruegel the Elder.

It depicts a row of blind men being led by also a blind man until they eventually stumble and fall. The artwork painted centuries ago still mirrors what's happening in today's world. The only difference is,we are deliberately making ourselves blind

## Prompt > Accept > Repeat

Notice there's no review step. That's the problem. You may think this workflow is fine. You may say"It's just a small change, nothing to be worried about really", until you repeat the process over and over again and these"small changes"eventually accumulate. Stretch it out over the long term and you'll slowly realize you can't"code"anymore without AI.

We are intentionally not looking at the generated code anymore.

AI-generated code is clean and deceiving at the same time. The UI looks good and the test (which it also generated) passes. It's like everything in the codebase is made out of rainbows and sunshine. No wonder engineers are just accepting changes and then moving on.But we are more than that.

Skill decay isn't unique to this industry. Any skill not used regularly will eventually deteriorate. It's always easier todictatewhat to do until youdo the task yourself. Oftentimes, dictating something isn't the same as actually implementing the task.

Executing the task yourself forces your brain to think. You'll find the right edge cases. You'll think more about the UX. You'll think about which tests make sense. You'll find which code matters more. That's the beauty of doing it yourself and using AI as a complement for repetitive tasks. It's a completely different story when we outsource all of the thinking to AI.

Sure you could argue that human-written code isn't perfect. The majority of us are notgifted programmers. Our code often hashuman errors. But that's the main reason why it's already valuable.

There is a human attached to it.

Someone already owns the decision. Someone is already accountable. Someone already has the context. When there's a mistake, that someone already has the foundation and they are not starting from zero. They built the code in the first place, they could fix it too. Struggling, making wrong assumptions, and eventually finding the right solution are the crucial steps for making genuine understanding. The next time they'll encounter the same problem, they have a pretty good chance of solving it alone this time resulting in better efficiency.

Use AI to learn and let it intentionally expose your gaps. Question and scrutinize it. Challenge and verify it at the same time. That's a much healthier way of using AI without surrendering the thinking process itself. But if you are going to delegate all the work to it, you might as well declare yourself as atab-pressing robotfor AI.

## Blind Trust Creates A Domino Effect

When unreviewed AI generated code is pushed for a PR review, the domino starts to fall. The junior trusts the AI, the senior trusts the junior, and eventually the code reaches production. This doesn't only cause cognitive atrophy, it also creates a false sense of trust.

How did we allow ourselves to get to this point?

Speed was never the best measure of quality code. A codebase is fragile. It always was. One wrong implementation can cause a multitude of errors.

AI lays down perfectly convincing code. The author sees it and gets trapped in the illusion that it works without actually understanding it. Context is already lost the moment this new code is pushed. You are betting on it to work from the start instead of deliberately increasing the chances for success byactually looking at it.

Instead of the senior asking whether this is a good change, they might first wonder whether the junior actually understands what they sent (or if they even read the code at all).

Who even likes reading 1000+ lines of slop?

Reading AI-generated code iscontagiousto the point that the reviewer might as well be lazy too and accept the changes without reviewing them.

It is human nature after all. If too much change is introduced at once, quality checking isn't uniformly implemented. It tempts the reviewer to skip through the entire change, skim the important parts, or worse, rely on AI review agents on top of it. This adds even more uncertainty.

AI is good but only when used as acomplement, not as asubstitute. It is a tool to be used correctly and responsibly. You can't force everyone to use this workflow, but you can always start with yourself. Read before sending, understand the PR, push with intention.

The point is to make your PR"ready for review". It doesn't have to be perfect. The most important thing is thatit is yours, and you can defend it in a snap when the reviewer asks about it. You can explain the ins and outs of your code and ultimately answer the question"Why?".

The next step would be another set of eyes to look over your code, add some polish, some minor (or major) fixes, or request additional refactoring. Discussing about the changes is what causes the context to benaturally transferredto team members.

If done right, people would eventually follow. If not, at least you've saved yourself fromcognitive atrophy.

## The Human Mind Needs To Be Challenged

To combat cognitive atrophy, we must find ways to challenge our minds. The data suggests that the current workflow isn't enough. We need to exercise our brains.

Personally, what I do is always solve at least one coding challenge every day, record myself doing it, and explain my thought process step by step as if I were teaching someone how to solve it. Below is my current collection of videos just talking to the camera and showing my screen.

It exposes my gaps, and I like that. Whenever I review my recordings, I could easily take note of the parts where I am struggling and parts where I find myself pausing during an explanation. Mistakes and pauses always ground me to the reality of my current skill level. But the best thing about this setup is that it gives me something tangible to improve upon while keeping my brain active and allowing it to form new connections.

I have seen clear improvements.

When I compare my very first recording to how I explain things now, I can tell that I am sharper and I now have a deeper understanding of the language and concepts I'm working with. It gives me a real comparison and personally I prefer it that way. Just like in video games, I always get motivated to grind more when I see my character's stats improve over time.

Beyond coding challenges, I also make sure to scrutinize my work by double checking best practices and methods. I find it useful to first search the internet for documentation, examples, and different approaches. After forming myown ideas, I then use AI to complement that knowledge and help me understand the subject on a deeper level.

There are also times when I caught AI suggesting deprecated methods.

This is something I wouldn't have noticed if I hadn't done my own due diligence of studying the subject beforehand. And what was AI's answer after I called it out?

"You're absolutely right!"

Yeah... that's when I realized howunreliableAI is.

It's a hit or miss. You're much more likely to miss something if you have little to no knowledge of the subject to start. I mean, they themselves are already telling us before we type our prompts.

But overall, these are some of my activities that work for me and they may be different for you. What's important is you are constantly challenging your mind just enough to keep it sharp.

Cognitive atrophy creeps in the moment you decide to outsource your thinking. You'll only realize it when you find yourselfstruggling to code the way you used to without the help of AI.

## Discipline is the Ultimate Form of Self-Respect

Yes, I will not be a hypocrite and tell everyone that I never tried using AI-generated code once. I did, and I did not like it. I opened my localhost and was greeted by multiple bugs. The bugs themselves weren't the ones that frustrated me.The mere fact that I don't know where to look is the problem.

The feeling of helplessness and the lack of ownership was overpowering.

I didn't create the code, AI did. So I continued and tried prompting again. It gave me around three to five pre-check actions that I need to verify first to solve the problem.It was exhausting.That workflow was not for me. When the bug was still not fixed, it gave me another list of pre-checks and possible fixes essentially generating another solution again and again.

You could argue that I don't have the experience yet and I don't have the correct prompt, or that I don't have the correct markdown files for describing the architecture and additional context. That's fair.

But if we're willing to go that far to have an AI code that"works", then we might as well do the code ourselves.

Fine, I'll do it myself. So I did.

It took me around 15-30 mins to debug, reiterate, study, fix, break, fix again and then create the component I needed. There were struggles, but they were the kind of struggles where I knew I was getting somewhere. The experience was like physically climbing a ladder. The struggle is tangible.

And more importantly, I knew more than I did before. My code was my own. My mistakes were my own. My solutions were my own. Finally, the understanding I gained was something that sticks.

My only enemy in this setup is my discipline.

I once read a quote about discipline:"Discipline is the ultimate form of self-respect". It stuck with me the moment I read it and I think it perfectly applies here.

In a world where generating code is easier every day, having the discipline to learn without cutting corners is asuperpower. Fundamentals are always present in every endeavor we find ourselves in. Investing in them through proper discipline implicitly earns your self-respect and eventually the respect from the engineers around you.

## Open Your Eyes

The solution is simple.

To combat cognitive atrophy, we should think for ourselves more. The more we exercise our minds, the more we can preserve the skills we've worked so hard to build.

I'm not saying we should abandon AI altogether. That would be a waste of an available resource. What I'm saying is to use AI responsibly. Use it as a tool and a complement that can elevate our thinking even further,not replace it.

AI is powerful but not to the point that it should take over every single decision involved in building software. That would be a ticket straight to cognitive atrophy. Remember, AI amplifies both the positive and the negative practices of the engineer controlling it. Like any other tool, if used improperly, the output will eventually go sideways.

At the end of the day, become part of a new generation of software engineers that still values quality. It doesn't have to be perfect and delivered fast. What's important is that you own it, you can defend it, you can fix it when something goes wrong, and ultimately, you are constantly improving in your own right.Don't let convenience become the reason to outsource your thinking.

So open your eyes.

Thank you for reading. This was longer than I expected. I decided to add this epic image from Avengers: Doomsday trailer last minute. I think it fits well with the ending. Bu-bye.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse