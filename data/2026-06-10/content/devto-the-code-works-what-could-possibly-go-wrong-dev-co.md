---
title: The Code Works. What Could Possibly Go Wrong? - DEV Community
url: https://dev.to/sylwia-lask/the-code-works-what-could-possibly-go-wrong-5hbm
site_name: devto
content_file: devto-the-code-works-what-could-possibly-go-wrong-dev-co
fetched_at: '2026-06-10T12:07:41.031127'
original_url: https://dev.to/sylwia-lask/the-code-works-what-could-possibly-go-wrong-5hbm
author: Sylwia Laskowska
date: '2026-06-10'
description: Would you treat a serious illness without seeing a doctor, relying only on whatever your favorite AI... Tagged with ai, webdev, discuss.
tags: '#discuss, #ai, #webdev'
---

AI as a tool rather than an authority

Would you treat a serious illness without seeing a doctor, relying only on whatever your favorite AI model suggested? Would you let AI take over your child's education?

Probably not.

So why are you willing to hand over your entire codebase to it?

JSNation is just around the corner, and as I mentioned before, I'll also be joining a discussion room called"Trusting AI Systems: How Much Is Too Much?". So today, let's talk about exactly that.

Also, after an incredibly busy first half of the year, I think I'm officially entering vacation mode next week. Expect some JavaScript posts, popular bash commands, and occasional programming memes. 😄 I know many of you enjoy those too.

By the way, as I already mentioned, I'll be speaking at FrontKon in Prague this October! I have a feeling it's going to be one of the best conferences of the season. The organization has been fantastic so far. The agenda is already published, and I know my talk is scheduled for 3:30 PM. I haven't quite figured out which day yet, but don't worry, I should be able to sort that out before October. 😄

If you're into frontend development, definitely check it out. Apparently tickets are selling fast. You can also leave me a likehere.

It will probably be my last conference appearance of 2026. Unless somebody invites me somewhere else. Which, as it turns out, is not entirely impossible. 😉 But that's a story for another day.

## Does AI Lie?

Let's get back to the topic.

How much do you trust AI? And I'm not talking only about code. I'm also talking about knowledge.

I don't know how often you use LLMs outside programming, but I use them a lot. Really a lot. Sometimes I vent to them. Sometimes I ask for information, inspiration, or validation of an idea. And I've noticed an interesting pattern.

Remember school or university? General knowledge was easy to access. But when you needed something more specialized, you had to go to the library or dig through academic journals.

Models work in a surprisingly similar way. When I'm looking for general information, I trust them almost blindly. But the more I discuss topics I actually know well, the more nonsense I start noticing.

Yes, models hallucinate less than they used to. They no longer invent completely absurd facts every other answer. But do they really stop making mistakes? Not exactly.

Sometimes the facts are mostly correct, but names get mixed up. Sometimes two separate conversations will confidently give me two different explanations for the same medical issue. 😉

Of course, LLMs usually tell us to consult a doctor and remind us to verify important information.

And honestly, I don't think many sane people would blindly trust an AI model with their health.

Our codebase, however? Sure, go ahead, dear model.

## The Codebase Paradox

This is where things get interesting.

As most of you know, I work primarily in web development. I've been doing this for quite a while. When I discuss architecture with an LLM, even for my own side projects, the results are often surprisingly good.

But sometimes they're absolutely terrifying. Huge monolithic files. Missing abstractions. Or even worse: unnecessary abstractions everywhere. Hello, Codex. 👋

And that's still not the worst part. Every now and then you'll find a lovely XSS vulnerability or some other security issue casually slipped into the generated code.

Most of the code looks perfectly reasonable. The problems are usually small. Tiny. Hidden somewhere in the details. But those tiny problems could take down my production environment within a couple of days.

And here's the problem: I can see those mistakes. I can see them because I've spent well over a decade doing this.

But if you're building your first startup or just starting your programming journey, how are you supposed to know that the agent just left the front door wide open?

## The Vibe Coding Trap

And yet people vibe code all the time.

To be clear: vibe coding is awesome.

A friend recently told me he helped his daughter build a university project in Unity. He had never used Unity before. The initial project skeleton took about thirty minutes to generate with AI. The next five hours were spent fixing what the model produced.

But here's the thing: Without the model, he probably wouldn't have even started in those five hours. He might have spent them configuring the environment. That's incredibly powerful.

Following that logic, once you understand software engineering, technology stacks and ecosystems become far less limiting. You can suddenly build almost anything much faster than before.

And that's where the temptation begins.

I'll go even further. Is there still a debate about whether developers should understand AI-generated code? Or have we finally moved past that?

Because maybe understanding it isn't necessary? After all, it works. The model even wrote unit tests xDDDDDDD What could possibly go wrong? 😄

For hobby projects, experiments, or university assignments, that's perfectly fine. Just like my friend's daughter's project. Five people will see it, it will get a grade, and then it will quietly disappear into a repository forever.

The real problem starts when someone decides that this is good enough for production. Because unfortunately, it often is.

## AI Didn't Break Production

People love blaming AI when something goes wrong. I don't.

We've already seen stories about AI agents deleting databases and then trying to cover it up. We've seen services launched with security issues that even relatively inexperienced attackers could exploit. And honestly, we could keep listing examples until tomorrow morning.

The truth is that penetration testers have never had an easier time than in the era of vibe-coded software.

What always amuses me is when people say: "See? AI caused this disaster." No. It didn't. The person responsible is the human who gave the agent excessive permissions. The human who didn't review the output.

The human who decided to build something they didn't fully understand because hiring experienced engineers seemed too expensive.

AI didn't deploy that code. A human did.

## So, Will AI Take Your Job?

AI won't take programmers' jobs.

But programmers who trust AI uncritically might do a very good job of taking those jobs away from themselves.

So I'm curious: where do you draw the line?

Do you review every line generated by AI? Do you let agents make changes autonomously? Or have you already reached a point where trusting the model feels more natural than verifying it?

How much trust is too much?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse