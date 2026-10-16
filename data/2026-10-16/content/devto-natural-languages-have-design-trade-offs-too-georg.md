---
title: 'Natural Languages Have Design Trade-offs Too: Georgian Is Dynamically Typed, English Is Statically Typed - DEV Community'
url: https://dev.to/georgekobaidze/natural-languages-have-design-trade-offs-too-georgian-is-dynamically-typed-english-is-statically-emi
site_name: devto
content_file: devto-natural-languages-have-design-trade-offs-too-georg
fetched_at: '2026-10-16T15:12:16.475188'
original_url: https://dev.to/georgekobaidze/natural-languages-have-design-trade-offs-too-georgian-is-dynamically-typed-english-is-statically-emi
author: Giorgi Kobaidze
date: '2026-10-15'
description: 'Table of Contents How This Started Feature #1: Articles (or the Lack of Them) The... Tagged with programming, writing, design, languages.'
tags: '#programming, #writing, #design, #languages'
---

Compares human grammar quirks to coding paradigms

## Table of Contents

* How This Started
* Feature #1: Articles (or the Lack of Them)The UpsideThe Downside
* The Upside
* The Downside
* Feature #2: GenderEnglish: He, She, and ItItalian: Two Genders, Every NounGerman: Three GendersGeorgian: Zero GendersThe Upside of GenderThe Downside of GenderThe Downside of Having No Gender
* English: He, She, and It
* Italian: Two Genders, Every Noun
* German: Three Genders
* Georgian: Zero Genders
* The Upside of Gender
* The Downside of Gender
* The Downside of Having No Gender
* Complexity Doesn't Disappear, It Moves
* Sounds Familiar, Developers?Articles vs.varGender vs. Typing
* Articles vs.var
* Gender vs. Typing
* Languages That Evolve (and Ones That Mostly Don't)
* Every Language Is a Trade-Off
* Tell Me About Your Language

## How This Started

I've been doing a little research on how good AI models are with uncommon, niche languages. And Georgian, my native language, is my main test subject. Check out the article for more details:

Kaggle Benchmarking Challenge Submission

 Giorgi Kobaidze
 

 Giorgi Kobaidze
 

Giorgi Kobaidze

 Follow
 

Oct 11

## Georgian Language Benchmark: Two Biggest AI Labs Clash in a Language That Doesn't Play by Anyone's Rules

#
devchallenge

#
kagglechallenge

#
ai

#
machinelearning

69
 reactions

Picked as gem

Picked as gem by you

Comments

 34
 comments

 20 min read
 

While comparing outputs, I kept noticing that the hardest parts weren't vocabulary. They were structure: things Georgian simply doesn't encode that English requires, and the other way around.

And because I'm a developer, my brain immediately filed these under one label:language features. Some features make life easier, some make it harder, and almost all of them are trade-offs.

I'll compare English and Georgian, since those are the only two languages I know (for now, German is in progress). I love both of them, and both are beautiful in their own way. But they couldn't be more different. Georgian has its own alphabet, Mkhedruli, with 33 letters and no uppercase or lowercase in everyday writing. Yes, my native language is case-insensitive by design. We don't really need casing at all.

Let's look at two features.

## Feature #1: Articles (or the Lack of Them)

English marks whether a noun isdefinite(a specific thing the listener already knows about) orindefinite(something new or non-specific). That's the whole job oftheversusa/an.

I sawabus leavingthestation.Thebus wasawhite MCI 102-DL3 with silver rims andaGreyhound badge on it.

Georgian has no articles at all. Structurally, the same sentence looks like this:

I saw bus leaving station. Bus was white 1999 MCI 102-DL3 with silver rims and Greyhound badge on it.

In actual Georgian:

დავინახე, როგორ გადიოდა ავტობუსი სადგურიდან. ავტობუსი იყო თეთრი MCI 102-DL3, ვერცხლისფერი დისკებით და Greyhound-ის ემბლემით.

No articles. None. Zero. Null. Undefined.The listener figures out definiteness from context: what was mentioned before, word order, and the situation itself. The first "bus" is obviously new information, the second one is obviously the same bus.

That doesn't mean Georgian is helpless when it needs precision. It just reaches for other tools on demand:

* Demonstratives likeეს(this) andის(that) make something definite:

this/that bus

* In casual speech,ერთი(one) often works like an indefinite article:

ერთი კაცი შემხვდა ("I met a (certain) man")

### The Upside

It's simpler. Fewer words to say and write, and nothing to choose. You never have to stop and think about which article goes where, which is famously one of the hardest parts of English for people whose native languages don't have articles.

### The Downside

It's not explicit, and implicit things occasionally become ambiguous. Rarely, but it happens. If someone tells you:

Take bus

Do they meanabus, any bus, orthebus that's standing right in front of you? In real life, the speaker resolves it with intonation, a gesture, or by saying:

Takethisbus

But that doesn't always happen.

And here's where it connects back to my AI research: when a model translates Georgian into English, it has toinsertinformation that wasn't in the source. Every "a" and "the" in the output is a guess. Usually a good one, but still a guess.

## Feature #2: Gender

From what I've observed, languages are absolutely obsessed with sorting things by gender. But there are actually two different things going on, and it's worth separating them:

* Natural gender: pronouns reflect the actual gender of a person. That's English.
* Grammatical gender:everynoun belongs to a class, including spoons, tables, and the moon. That's Italian, German, and many others.

### English: He, She, and It

English hashe/him/his,she/her/hers, andit/its. That's as far as it goes, and it mostly follows reality: people get he or she, a table is "it". (Except ships, which are sometimes "she" for reasons sailors would have to explain.)

### Italian: Two Genders, Every Noun

Italian has masculine and feminine, and every noun has to pick one. There are patterns (nouns ending in-oare usually masculine,-ausually feminine), and then the exceptions show up:

* la mano(hand) is feminine, despite ending in-o
* il problema(problem) is masculine, despite ending in-a
* il sole(sun) is masculine,la luna(moon) is feminine

Logic behind it? Nobody knows. Well, at least I don't. You just memorize them.

### German: Three Genders

Think that's complex? German has three: masculine (der), feminine (die), and neuter (das). Look at your dinner table:

* der Löffel: the spoon is masculine
* die Gabel: the fork is feminine
* das Messer: the knife is neuter

Three pieces of cutlery, three genders. It gets better:das Mädchen(the girl) isneuter, because the diminutive suffix-chenalways makes a word neuter. Grammar beats biology. And the sun and moon?die Sonneis feminine andder Mondis masculine, the exact opposite of Italian. If gender were logical, the two languages would at least agree on the sky.

I recently started learning German, and honestly, der/die/das is the hardest part for me. The standard advice is to never learn a noun without its article, and now I understand why.

### Georgian: Zero Genders

When I was a kid and started learning other languages, this was the weirdest thing of all. Why on earth are words divided by gender? That was absolute nonsense to me. Because in Georgian, there's no gender. None. Zero. Not even for people.

The same pronoun covers he, she, and it:ის(he/she/it),მას(him/her/it, as an object),მისი(his/her/its). The only distinction Georgian makes is between people and things, withვინ(who) versusრა(what). Which is natural. Nobody asks:

Who is that truck?

### The Upside of Gender

It carries information.

My boss is really lovely, she told me I'm doing a great job during the meeting.

One pronoun, and you already know your boss is a woman.

It helps you track references.This is the advantage people rarely mention. In German:

Die Gabel liegt neben dem Löffel.Sieist schmutzig.

Siecan only be the fork, because the fork is feminine and the spoon isn't. In English, the same sentence is ambiguous:

The fork is next to the spoon.Itis dirty.

In Georgian, it's equally ambiguous. Grammatical gender works like a checksum: redundant information that helps the listener connect the right pronoun to the right noun.

### The Downside of Gender

What if you don't know?

Tell your boss to give you some vacation days, he or she should be concerned that you're working so much.

Now you have to say both, and it gets clunky fast.

English's escape hatch issingular "they":

When a developer joins the meeting, ask them to show you where the repository is.

One developer, plural pronoun. My first instinct was that this is technically incorrect, but it turns out English speakers have been doing it since the 14th century, and writers like Shakespeare and Jane Austen used it. Even better: English has done this exact trick before.Youwas originallyplural only; the singular wasthou. Over time, "you" took over the singular too, and nobody today thinks "you are" is a grammar bug. Singular "they" is the same migration, still in progress.

The memorization tax.For people, gender carries meaning. For spoons and forks, it carries none, yet Italian and German learners still have to memorize it for every single noun.

### The Downside of Having No Gender

Georgian's simplicity has a price too. If youwantto express gender, you have to say it explicitly: man or woman, gentleman or lady. "My friend" (მეგობარი) tells you nothing about who that friend is.

And once again, this is a real problem for AI. Translating ის into English forces a choice between "he" and "she" that the original sentence never made. Machine translation systems have historically filled that gap with stereotypes: the doctor becomes "he", the nurse becomes "she". Those assumptions are never good.

## Complexity Doesn't Disappear, It Moves

Before anyone concludes that Georgian is "easy mode", it isn't. Far from it, it's so complex, sometimes even native speakers struggle to speak or write grammatically correct, It just stores its complexity somewhere else, mostly in verbs.

A single Georgian verb can encode both the subject and the object.მიყვარხარmeans "I love you". One word, three ideas. Verbs change form across groups of tenses, and even thecase of the subjectchanges depending on the tense. Georgian dropped articles and gender, then poured all that saved effort into verbs that do an enormous amount of work.

There's a principle in software for exactly this:Tesler's law, or the law of conservation of complexity. Complexity can't be removed, only moved. Languages, it seems, follow it too.

## Sounds Familiar, Developers?

All of this reminded me of programming languages, because they face the exact same trade-offs.

### Articles vs.var

Georgian's missing articles map almost perfectly onto type inference in C#:

Bus
 
bus
 
=
 
new
 
Bus
(
"MCI 102-DL3"
);
 
// explicit: "the bus"

var
 
bus
 
=
 
new
 
Bus
(
"MCI 102-DL3"
);
 
// implied, but obvious from context

var
 
next
 
=
 
dispatcher
.
Next
();
 
// ...is that a Bus? A Route? "take bus"

Enter fullscreen mode

Exit fullscreen mode

The compiler always knows whatnextis. The human reading the code might not. That's why many teams have a style rule along the lines of "usevaronly when the type is obvious from the right-hand side". It's the Georgian rule exactly: implicit is great when the context makes it obvious, and when it doesn't, you say "thisbus" or write the type out.

C# even went in the other direction with target-typednew, where the left side carries the information and the right side drops it:

Bus
 
bus
 
=
 
new
(
"MCI 102-DL3"
);

Enter fullscreen mode

Exit fullscreen mode

Same idea, different side of the sentence.

### Gender vs. Typing

German grammatical gender behaves a lot like static typing. Every noun carries a tag, and everything around it (the article, the adjective endings) has to agree with that tag. It's ceremony, and sometimes it feels like noise, but mismatches get caught and references are easier to track.

Georgian pronouns are closer to dynamic typing.ისcan hold anything: a person, a truck, an idea. Less ceremony, more flexibility, and meaning gets resolved at "runtime" from context.

C# won't let you mix types without saying so:

int
 
distance
 
=
 
5
;

string
 
label
 
=
 
"2"
;

var
 
total
 
=
 
distance
 
-
 
label
;

// error CS0019: Operator '-' cannot be applied to operands of type 'int' and 'string'

Enter fullscreen mode

Exit fullscreen mode

JavaScript will happily guess what you meant:

"
5
"
 
-
 
2
 
// 3

"
5
"
 
+
 
2
 
// "52"

[]
 
+
 
[]
 
// ""

Enter fullscreen mode

Exit fullscreen mode

(To be precise, static vs. dynamic and strong vs. weak are two different axes. Python is dynamic but strongly typed:"5" + 2raises aTypeError. JavaScript is dynamicandweakly typed, which is how you get"52".)

And the arbitrary part of German gender? Imagine a language that forces you to annotate every variable with a type, where the type names were assigned by rolling dice centuries ago, and nobody is allowed to refactor. That's der Löffel, die Gabel, and das Messer.

## Languages That Evolve (and Ones That Mostly Don't)

Here's where natural languages and programming languages really differ.

Programming languages learn from each other constantly. C# is a great example. It added generics, then lambdas and LINQ (borrowed from the functional programming world), pattern matching inspired by F# and the ML family, records, and nullable reference types to fight what Tony Hoare called his "billion-dollar mistake". And it doesn't only borrow, it lends:async/await, introduced in C# 5, was later adopted by JavaScript, Python, Rust, and many others.

Natural languages mostly borrowwords. English tookbeef,pork, andmuttonfrom French after the Norman conquest, while the living animals stayedcow,pig, andsheep. Georgian borrowedკომპიუტერი(computer) andტელეფონი(telephone) like nearly every other language on Earth. Sometimes a borrowed word wins so completely that people forget the original word in their own language ever existed.

The structure, on the other hand, usually stays put.Usually.Natural languages do refactor, just very slowly:

* Old English had three grammatical genders, just like German. By the Middle English period, they were gone. English deprecated a feature that German still ships today.
* Thouwas deprecated, andyouabsorbed its job, which is exactly the precedent for singular "they".

The difference is the release process. There's no changelog and no migration guide, a breaking change takes a few centuries to roll out, and every speaker is a maintainer.

## Every Language Is a Trade-Off

No matter what design you come up with, there will always be trade-offs. Articles buy precision and cost effort. Gender buys information and reference tracking, and costs memorization. Dropping both buys simplicity and costs explicitness, then the complexity sneaks back in through the verbs.

Every language is beautiful in its own right, and the same goes for programming languages. Learning a new one, spoken or compiled, is the best way to discover assumptions you didn't even know you had. Georgian taught me that a language can live perfectly well without "a/an/the" and "she/he". C# taught me whyvarneeds a style guide. And German is currently teaching me how insanely hard it is.

As for AI: the places where languages disagree on what to encode are exactly the places where models have to guess. Which is precisely why I'm benchmarking them in Georgian.

## Tell Me About Your Language

Now it's your turn. What languages do you speak, and how do they handle these features? Do they have articles? Grammatical gender? Is your native language "statically" or "dynamically" typed? Tell me in the comments. I'd love to see which languages follow the same patterns and which break all the rules.

Enjoyed this write-up? Let's stay connected!

I share more software engineering insights, projects, and experiments across these platforms:

* 💼Connect with me on LinkedIn
* 💻Explore my projects on GitHub
* 📱Follow me on X
* 🎥Watch my videos on YouTube
* 💬Let's Chat on Discord

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (24 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse