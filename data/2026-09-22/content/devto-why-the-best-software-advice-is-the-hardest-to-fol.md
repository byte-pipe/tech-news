---
title: Why the Best Software Advice Is the Hardest to Follow - DEV Community
url: https://dev.to/remojansen/why-the-best-software-advice-is-the-hardest-to-follow-4kg8
site_name: devto
content_file: devto-why-the-best-software-advice-is-the-hardest-to-fol
fetched_at: '2026-09-22T21:49:18.126807'
original_url: https://dev.to/remojansen/why-the-best-software-advice-is-the-hardest-to-follow-4kg8
author: Remo H. Jansen
date: '2026-09-22'
description: Not all software advice is created equal. Some advice is practical. It tells you exactly what to... Tagged with software, career, learning, discuss.
tags: '#discuss, #software, #career, #learning'
---

Not all software advice is created equal. Some advice is practical. It tells you exactly what to do:

* Write small functions.
* Keep functions focused.
* Use constants instead of magic numbers.
* Give variables meaningful names.
* Keep your classes small.

This kind of advice is useful because it is easy to understand, easy to teach, and easy to verify. You can look at a piece of code and ask:Is this function too large? Is this a magic number? Is this constant named correctly?

There is usually a relatively clear answer. And because this advice is so easy to follow, it tends to spread. Teams put it into coding standards. Linters enforce it. Code reviews check it. Developers learn it early in their careers. But there is another kind of advice. It is much harder to follow. And, in my experience, it is often much more valuable.

## Two kinds of advice

I think about software advice as belonging roughly to two categories. The first ispractical advice. It is close to black and white:

Do this.Don't do that.

The second isjudgment-based advice.

It doesn't give you a recipe. Instead, it gives you a principle that you have to interpret depending on the situation. It might even contradict another principle you have learned. This kind of advice is closer to a balance between two opposing forces. There isn't always a universally correct answer. And that's what makes it difficult.

## Practical advice is easy to scale

Take a piece of advice like:

Write small functions.

That's generally useful advice. A junior developer can understand it. A senior developer can teach it. A code reviewer can point at a 200-line function and say, "This should probably be split up."

The same is true for advice such as:

Don't use magic numbers.

Or:

Use meaningful names.

Or:

Keep your classes focused.

These are great pieces of advice because they reduce the number of decisions you need to make.

You don't need years of experience to understand what they mean. You can learn them from a book, apply them tomorrow, and see an immediate improvement. This is one of the reasons books likeClean Codebecame so influential. A large part of the advice is actionable.

You can take a principle and immediately translate it into something you do while writing code. And that's valuable. But there is a danger. We can start confusingfollowing good practiceswithbecoming a good engineer.

## When advice stops being black and white

Consider a different piece of advice:

The wrong abstraction is more costly than duplication.

This sounds simple, but try turning it into a rule. Should I duplicate this code? Sometimes yes. Sometimes no.

How much duplication is acceptable?

How similar do two pieces of code need to be before they should be abstracted? What if they look similar today but are likely to evolve differently?

What if the abstraction makes the current code more complicated but might save us from duplication later? There is no simple checklist that answers these questions. You need judgment. And judgment comes from experience. You have to have seen abstractions that worked well. You also have to have seen abstractions that turned into monsters.

You need to experience the cost of changing an abstraction that was designed too early. You need to see duplication that was completely harmless. And you need to see duplication eventually become a maintenance nightmare. Only then does the advice start to become useful at a deeper level. It stops being a rule and becomes away of thinking.

## Experience changes the meaning of advice

This is something I find fascinating about software engineering. You can hear exactly the same advice at different stages of your career and understand something completely different each time. Early in your career, someone tells you: "Don't repeat yourself".

You learn DRY. So you start looking for duplication everywhere. Two pieces of code look similar? Abstract them. A few parameters are repeated? Create a common object. Several classes have similar behavior? Create a base class. You are following the advice. Then, years later, you encounter another principle:

Prefer duplication over the wrong abstraction.

And suddenly DRY doesn't look so simple anymore. You realize that duplication isn't necessarily the problem.

Sometimes duplication is the price you pay for keeping two concepts independent. Sometimes an abstraction creates more coupling than the duplication ever would have. Sometimes the best thing you can do is repeat yourself and wait until the domain tells you what the abstraction should actually be.

The advice didn't change.Your ability to interpret it changed.That's what experience gives you.

## From rules to intuition

There is a point in your career where you accumulate enough examples that you start recognizing patterns before you can fully articulate them. You look at an abstraction and something feels wrong. You can't immediately explain it. You might say:

"I don't think we should abstract this yet."

Why? Maybe you've seen this exact situation before. Maybe you've experienced how these abstractions evolve. Maybe you recognize that two things that currently look identical are likely to change for completely different reasons.

This is where intuition starts becoming important. Intuition in software engineering isn't magic. It isn't a replacement for thinking. It is often the result of accumulated experience.

You've seen enough situations, failures, trade-offs, and consequences that your brain starts recognizing patterns automatically. The problem is that intuition is much harder to teach than a rule. I can teach you "Use small functions." in five minutes.

I can't give you five minutes of advice that will make you understandwhena function is too large,whyit is too large, andwhen splitting it would actually make the code worse. That requires experience.

## The uncomfortable part of judgment-based advice

There is another reason this kind of advice is difficult. Sometimes two pieces of good advice conflict. You might hear:

Keep things simple.

And:

Don't duplicate code.

And:

Avoid premature abstraction.

And:

Encapsulate things that change.

All of these can be good advice. But what happens when following one makes it harder to follow another?

There is no compiler warning for this. There is no linter that can tell you which principle should win. You have to make a decision. And that decision depends on context.

This is why experienced engineers can sometimes disagree about a piece of code while both having perfectly reasonable arguments. The disagreement isn't necessarily because one person knows the rules and the other doesn't.

It may be because they're making different judgments about the future, the domain, the cost of change, or the risks involved. That's the gray area of software engineering.

## Scrum is another interesting example

I think the same distinction can be seen outside of code. Consider Scrum and the Agile Manifesto. Scrum gives you something concrete. Roles, Events, Artifacts and Rules.

A team can learn Scrum and start implementing it relatively quickly. That makes it attractive to organizations. There is something reassuring about being able to say:

"We are doing Scrum."

There is a framework. There are defined practices. There are ceremonies you can schedule. There are artifacts you can create. There are things you can point to and say, "We're doing it."

The Agile Manifesto is different. It gives you four values and twelve principles, but it doesn't give you a complete operating manual for running a software organization.

It tells you things like valuing individuals and interactions over processes and tools, and responding to change over following a plan. Those statements require interpretation. They require judgment.

For example, valuing individuals and interactions over processes doesn't mean processes are useless. Responding to change doesn't mean planning is useless.

The interesting question is not:

"Which one do I follow?"

The interesting question is:

"How do I apply these principles in this particular situation?"

And that is much harder. You can implement Scrum without necessarily developing the judgment behind Agile.

You can have all the ceremonies, all the boards, all the roles, and all the terminology and still miss the underlying principles.

That's the difference betweenfollowing a frameworkandunderstanding the principles behind it.

## Why the easy advice wins

There is a natural reason practical advice dominates.

* It is measurable.
* It is teachable.
* It is reviewable.
* It is scalable.

A company can create a coding standard that says:

Functions should be small.

It is much harder to create a standard that says:

Use your accumulated experience and judgment to determine the appropriate level of abstraction for the current domain and its likely future changes.

The first can become a rule. The second requires a person who knows what they're doing. Organizations naturally prefer things that can be turned into rules. And this isn't necessarily bad. Practical advice is extremely useful. The problem starts when we believe that collecting enough practical rules will eventually give us good judgment.

It doesn't work that way. Knowing more rules doesn't automatically make you better at making trade-offs. At some point, you need to develop the ability to decidewhich rule matters in this situation.

## The hardest advice may be the most valuable

This is why I think some of the most valuable software advice is also the hardest to follow.

It doesn't tell you exactly what to do.

It makes you think. It gives you a lens through which you can look at a problem. It might even force you to balance two competing ideas. And initially, that can be frustrating. We want software engineering to have recipes.

* Tell me the right architecture.
* Tell me when to abstract.
* Tell me how big a function should be.
* Tell me exactly when to introduce a design pattern.
* Tell me the correct process for building software.

But software is built in contexts.

* Different teams.
* Different domains.
* Different constraints.
* Different people.
* Different levels of uncertainty.

The more experience you gain, the more you realize that many of the most important engineering decisions don't have a universally correct answer. They require judgment. And judgment is difficult becauseyou have to own the decision. There is no checklist to hide behind.

## Maybe that's the real progression

Perhaps becoming a better software engineer isn't about replacing bad rules with better rules. Maybe it's about gradually moving from rules toward principles.

From:

"I was told to do this."

to:

"I understand why this is usually useful."

and eventually to:

"I understand the trade-off, and I can decide whether it applies here."

That's a much harder skill to develop. But once you develop it, practical advice becomes even more useful. You don't stop using the rules. You understand them better. You know when to follow them. You know when two rules conflict. And, perhaps most importantly, you know whennotto follow them. That is where experience turns advice into wisdom.

## What do you think?

I'm curious about your experience.What is the most pointless practical software advice you've encountered in your career?And on the other side:What is the most valuable piece of judgment-based advice you've learned?The kind of advice that didn't give you a rule to follow, but changed the way you think about software engineering.

I'd love to hear your examples in the comments.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse