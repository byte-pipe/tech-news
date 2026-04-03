---
title: Building the Chinese Room - by SE Gyges
url: https://www.verysane.ai/p/building-the-chinese-room
site_name: tldr
content_file: tldr-building-the-chinese-room-by-se-gyges
fetched_at: '2026-02-14T19:11:06.774772'
original_url: https://www.verysane.ai/p/building-the-chinese-room
author: SE Gyges
date: '2026-02-14'
description: Suppose also that after a while I get so good at following the instructions for manipulating the Chinese symbols and the programmers get so good at writing the programs that from the external point of view—that is, from the point of view of somebody outside the room in which I am locked—my answers to the questions are absolutely indistinguishable from those of native Chinese speakers.
tags:
- tldr
---

# Building the Chinese Room

SE Gyges
Feb 12, 2026
9
2
2
Share

Suppose also that after a while I get so good at following the instructions for manipulating the Chinese symbols and the programmers get so good at writing the programs that from the external point of view—that is, from the point of view of somebody outside the room in which I am locked—my answers to the questions are absolutely indistinguishable from those of native Chinese speakers. Nobody just looking at my answers can tell that I don’t speak a word of Chinese. [...] But in the Chinese case, unlike the English case, I produce the answers by manipulating uninterpreted formal symbols. As far as the Chinese is concerned, I simply behave like a computer; I perform computational operations on formally specified elements. For the purposes of the Chinese, I am simply an instantiation of the computer program.

[...]

Now the claims made by strong AI are that the programmed computer understands the stories and that the program in some sense explains human understanding. [...]

John Searle, “Minds, Brains and Programs”, 1980

I confess that I find Searle’s writing style somewhat difficult. I ask to be forgiven for restating his argument in a much simpler form, which I find easier:

1) Computers simply follow written rules, which we call scripts or programs.

2) A person could also follow written rules.

3) If a person were following very good rules, they might seem to understand a language they did not know.

4) Therefore, if a computer, by following rules, seems to understand a language (or, indeed, anything), this does not mean that they actually understand that language.

Simple enough! This all happens in a room, into which written Chinese is passed, and out of which written Chinese emerges. This is the Chinese room, and it is, of course, a most marvelous room. We will try to work out how to make one. There are other arguments about Searle’s room with greater depth and sophistication; my contribution is only that I prefer to be very simple, and so I will restrict myself to how you would actually construct it. I will, nevertheless, try to be light on math.

Starting out, we can assume that the messages passed into and out of the room are no longer than 100 characters for simplicity. Chinese is rather more efficient per character than English, so 100 characters is enough for a good paragraph. We will not have a long term memory if we do it this way, but it is a good place to start. We can assume that we only use the 20,000 most common characters, which keeps the numbers mostly tidy.

The simplest rule is to simply look up the correct answer in a big book, which would traditionally be called a “lookup table”. As long as every input has exactly one correct output, you can simply look it up. This will be extremely inefficient, but sometimes you want to see if you can solve something inefficiently before you try to find a better way to solve it.

There are about 10430possible sequences here, which is a one with 430 zeroes after it. There are about 1080atoms in the universe, so we will need to take apart quite a few universes to make our book, and our book will also take up quite a few universes of space, too.

Just in case we do end up with 10350spare universes to make a book out of, we should consider how long it will take to look something up. Unfortunately, putting the book in sorted order does not really help us: on average we have to travel halfway across it to reach the correct answer, and if we are moving at the speed of light this will still take so long that our universe will have ended by the time we have the answer. This would be very sad.

What we need is not a faster search but a smaller book. Here we arrive at something genuinely interesting, because to make the book smaller, we must notice something about Chinese: that very little of it is ever random.

The lookup table treats every possible string of characters as equally likely. But language is not like that. Most possible messages are gibberish that no one would ever write, and the correct response is “什麼？”, or “What?”. Meaningful Chinese messages is a much smaller set of things than all possible messages, and more importantly, it has structure. This structure can be exploited.

To compress our table, we must write rules that capture the patterns. Instead of storing the response to every possible input, we write instructions like: “If the message asks a question about a person, and the person was previously mentioned in the conversation, then...” But notice what has happened. To write these rules, we have had to encode facts about Chinese, such as which words refer to people, and which do not, and when to use each kind. We did not set out to put understanding into the room. We set out to make the book smaller. But the only way to make the book smaller was to put understanding into the book. If we insisted that this was not understanding but merely a very detailed description, we would have some difficulty saying what the difference was.

For compelling mathematical reasons1, we cannot know for certain how large such a book, in order to describe Chinese perfectly, would have to be. It is hypothetically possible that it could be made quite small, but if it could be, it seems surprising that nobody has made such a book yet. Even if we only accept meaningful paragraphs of Chinese, there are rather many of them, and to be truly indistinguishable from a native speaker, we have to allow that they can be rather long and complex, instead of the 100 characters at a time we started with. In fact, as the possible output becomes longer, we will need to be able to write into books as well as read them, because no matter how complex our rules are, the only rule for dealing with being asked for information you were told earlier is to have that information on hand.

Our operator will be working very hard, so we should improve our design to make his life less difficult. We ought to split the instructions into more than one book, so that he does not have to flip back and forth when checking on things, but can leave his page open and simply open another book. These books ought to be organized in some way. For ordinary books, we organize them by subject, author, and so on, but in this case, we only need to know when to check a given book for what we need. This, too, can be a rule in the book: “if you are discussing your second grade teacher, and someone has mentioned orchards, go to volume 410”.

At last, this begins to sound like it might actually work. But now our poor operator can only read one book at once, even though he can leave his previous book open. If he has to look up more than one thing, he must do them one at a time, which will certainly be very slow. So let us make sure we have more than one operator. They cannot all be in exactly the same place at a time. We might arrange them in layers, and connect them so that each operator receives messages from several others and sends messages onward to several more. We might arrange them in three dimensions, to let them communicate as densely as possible. You might put wrinkles in their layers, so that you could use space as efficiently as possible while varying how many connections each had, and to which others.

In short: If you want your system of Chinese rooms and operators to be anything like efficient enough to work, it will look a lot like a brain.

This is the counterargument: You cannot actually construct Searle’s Chinese Room in anything like the form he describes. If you try to design it to be efficient enough to actually work, it no longer looks at all like a “room”, really. That you can build such a room, and, implicitly, that it would look something like the description, is Searle’s third premise in my restatement. Since this is false, the argument is false.

Searle’s argument hinges on a sleight of hand: the room is described in a quite ordinary way, and everyone knows by intuition that a single person following some written rules for a language they do not know cannot accomplish very much, and especially not in any reasonable amount of time.

We are asked to assume that this arrangement produces good Chinese, which certainly cannot be true because Chinese is much too complex for that, and from this he proves the argument. You are asked to suspend the intuition that tells you the room would not work, and then indulge the intuition that tells you that the room does not have understanding. In truth, the room would neither work, nor have understanding; the argument seems good because it is good at persuading you to abandon the one intuition but not the other, even though they are, in reality, directly connected.

Logicians like to say that from an absurdity anything follows. Searle asks you to assume the room works, as though this were a harmless simplification, but it is not: it is the entire question being begged. The room must be simple enough that it obviously does not understand Chinese, and complex enough that it produces good Chinese, and these cannot both be true. The assumption that they can is the absurdity, and from it Searle derives his conclusion.

My objection is really just a way of detailing one Searle covers in some detail:

1. The Systems Reply (Berkeley). “While it is true that the individual person who is locked in the room does not understand the story, the fact is that he is merely part of a whole system, and the system does understand the story. The person has a large ledger in front of him in which are written the rules, he has a lot of scratch paper and pencils for doing calculations, he has ‘data banks’ of sets of Chinese symbols. Now, understanding is not being ascribed to the mere individual; rather it is being ascribed to this whole system of which he is a part.”

I think this is correct: As described, the system as a whole, the room with the rules and the person in it, does and must understand Chinese. Conversely, any definition of “understand” which excludes the room seems to be meaningless, in that you could never tell if something or someone did or did not understand anything, past that point. All that remains is to insist that understanding requires being made of the right kind of stuff, which is not really an argument about understanding at all.

The trick is just that it seems ridiculous to say that the room understands anything, and the reason it seems ridiculous is that the room is obviously and intuitively much too simple to do so.

1

The Kolmogorov complexity of something is the length of the shortest possible way of writing it down. For example, “one googol” is a one followed by a hundred zeroes, and has, at most, relatively low Kolmogorov complexity because you can write it as “one googol” or 10^100. It is impossible, in general, to compute the Kolmogorov complexity of a string, or, equivalently, to be sure that you have found the shortest possible way of writing it down. This follows basically the same reasoning as the halting problem and Godel’s Theorem.

9
2
2
Share
