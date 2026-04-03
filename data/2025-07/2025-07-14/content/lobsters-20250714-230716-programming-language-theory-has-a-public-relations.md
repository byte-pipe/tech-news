---
title: Programming Language Theory has a public relations problem | One Happy Fellow - blog
url: https://happyfellow.bearblog.dev/programming-language-theory-has-a-public-relations-problem/
site_name: lobsters
fetched_at: '2025-07-14T23:07:16.681547'
original_url: https://happyfellow.bearblog.dev/programming-language-theory-has-a-public-relations-problem/
date: '2025-07-14'
description: Programming Language Theory (PLT) is one of my favourite areas of computer science yet I feel it's one of the most misunderstood by outsiders. It's full ...
tags: plt
---

# Programming Language Theory has a public relations problem

13 Jul, 2025

Programming Language Theory (PLT) is one of my favourite areas of computer science yet I feel it's one of the most misunderstood by outsiders.

It's full of beautiful constructions and great ideas at the intersection of pure theory and practical applications. And yet outside of the PLT community, it's considered cryptic, hard, useless, not practical. The problems are similar to the public perception of pure maths ("why would I learn it?", "does it have any practical applications?") but somehow even worse.

How did it happen?

## Problem 1: Theory vs applications

PLT can be done and appreciated as a pure maths subject, just like a beautiful construction proving an intricate topological theorem, or a stunning painting. It's an art. To fully appreciate it, you need some education.

A purely theoretical work is sometimes presented as having "practical applications". Sometimes the authors mean "it can be used to prove other theorems and the other 8 people interested in this topic might find it practically useful for that purpose". At other times, it's an overstated hope for potential future applications.

Imagine an experienced software engineer who got interested in PLT and wants to learn more. Someone told them that they should start with reading "The Lambda Calculus. Its Syntax and Semantics" by Barendregt. They go and struggle through unfamiliar notation, fighting to extract a drop of insight relevant to their experience. Finally, they understood the Church-Rosser theorem.

"What's Church-Rosser theorem good for?", software engineer asks. Oh, you see, it haspractical applications, you just don't know enough to see it yet.

The engineer disappeared. His time was better spent learning a new Javascript framework - at least there he could see practical benefits.

## Problem 2: Standing on the toes of the giants

Even simple-sounding theorems require heavy machinery. And that machinery is still being built, even though we started in the 30s.

How is that different from any other branch of mathematics? Well, if you take a look at undergraduate or graduate mathematics curriculum, you'll see that most subjects connect to one another. The build up on one another. Or there are celebrated "bridge" theorems, providing a way to translate results from one branch of mathematics to another.

Not so much in PLT. Each development, each proof starts close to starting from scratch. You won't find many authors reusing someone else's lemmas and theorems. Even definitions aren't agreed upon. So each paper can feel like starting from scratch.

Don't get me wrong, PLT researchers read each other's papers and do influence each other's work. But this influence happens at the level of techniques and approaches rather than formal reuse. Instead of building theorem-upon-theorem like in other mathematical fields, PLT researchers tend to adapt and modify each other's proof methods for their own ground-up constructions.

## Problem 3: Abstraction creep

I mentioned that each paper, each problem might require a separate setup, with its own definitions, lemmas and theorems. Wouldn't it be nice if we could package common proof techniques as ready-made theorems and reuse them across many proofs?

It definitely would be nice but the price to pay is a very high level of abstraction. Think of it as a codebase which uses complicated architectural patterns, lots of indirection, many layers. Not in the spaghetti code kind of way, it's all necessary and used well - but there's a steep learning curve.

Just like with that codebase, where implementing each single piece of functionality from scratch would beso much easierwithout using so many abstractions, it's also the case for proofs using abstract methods. They are powerful but you lose intuitive clarity and make it harder for new people to jump in.

## Problem 4: It's just hard

PLT is very hard. Minor changes to a language might break properties you rely on, language features don't compose nicely. The design space is vast, exploring each corner is expensive (how many production-grade compilers are there in the world?) and we've only had so much time.

On the other hand, PLT is about very concrete objects: programming languages. I can experiment with them, I can write interpreters, create my own toy language. Many people do! Why not learn some theory as well? How hard can it be?

It's an unpleasant surprise.

## Solutions?

I can't dictate what people should and shouldn't do. But I'm well within my right to write down a wish-list:

* Be honest and tell people that big part of motivation for PLT work is its inherent beauty and immediate applicability in software engineering scenarios is not the goal.
* Create introductory materials for software engineers interested in PLT. It doesn't need to be comprehensive but it should provide motivation for why the theory exists, why it can be useful and why it is hard.
* Keep your theorems and proofs as simple as possible. I know the incentives in academia and asking everyone to write their papers with novices in mind won't happen but this is my wish-list and I can wish whatever I want.

## A prayer

May I have the strength of will and clarity of mind to bring the beauty of PLT to more people through my hard work. May readers understand my intentions, forgive my sarcasm and enjoy the writing.

55
