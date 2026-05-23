---
title: On the <dl> | Ben Myers
url: https://benmyers.dev/blog/on-the-dl/
site_name: hackernews_api
content_file: hackernews_api-on-the-dl-ben-myers
fetched_at: '2026-05-23T19:29:56.950480'
original_url: https://benmyers.dev/blog/on-the-dl/
author: Ben Myers
date: '2026-05-23'
published_date: '2021-08-06'
description: The semantics you didn’t know you needed.
tags:
- hackernews
- trending
---

## Introduction

The<dl>, ordescription list, element is underrated.

It’s used to represent alist of name–value pairs. This is a commonUIpattern that, at the same time, isincrediblyversatile. For instance, you’ve probably seen these layouts out in the wild…

Each of these examples shows a list (or lists!) of name–value pairs. You might have also seen lists of name–value pairs to describe lodging amenities, or to list out individual charges in your monthly rent, or in glossaries of technical terms. Each of these is a candidate to be represented with the<dl>element.

So what does that look like?

## The Anatomy of a Description List

I’ve been saying “<dl>,” when really, I’m talking about three separate elements:<dl>,<dt>, and<dd>.

We start with our<dl>. This is thedescription list,[note 1]akin to using a<ul>for an unordered list or an<ol>for an ordered list.

Copy code

<
dl
>

</
dl
>

Fancy.

Next up, we want to add a name–value pair. We’ll use a<dt>, short fordescription term, for the name, and we’ll use a<dd>, short fordescription detail, for the value.[note 2]

Copy code

<
dl
>

	
<
dt
>
Title
</
dt
>

	
<
dd
>
Designing with Web Standards
</
dd
>

</
dl
>

To add another name–value pair to our list, we add another<dt>and<dd>:

Copy code

<
dl
>

	
<
dt
>
Title
</
dt
>

	
<
dd
>
Designing with Web Standards
</
dd
>

	
<
dt
>
Publisher
</
dt
>

	
<
dd
>
New Riders Pub; 3rd edition (October 19, 2009)
</
dd
>

</
dl
>

But wait — what if I have a term that has multiple values? For instance, what if this book has multiple authors?

That’s fine! One<dt>can have multiple<dd>s:

Copy code

<
dl
>

	
<
dt
>
Title
</
dt
>

	
<
dd
>
Designing with Web Standards
</
dd
>

	
<
dt
>
Author
</
dt
>

	
<
dd
>
Jeffrey Zeldman
</
dd
>

	
<
dd
>
Ethan Marcotte
</
dd
>

	
<
dt
>
Publisher
</
dt
>

	
<
dd
>
New Riders Pub; 3rd edition (October 19, 2009)
</
dd
>

</
dl
>

There’s one last piece of the description list anatomy to look at for most basic use cases: what if I want to wrap a<dt>and its<dd>(s) for styling reasons?

In this case, the specs allow you to wrap a<dt>and its<dd>(s) in a<div>:

Copy code

<
dl
>

	
<
div
>

		
<
dt
>
Title
</
dt
>

		
<
dd
>
Designing with Web Standards
</
dd
>

	
</
div
>

	
<
div
>

		
<
dt
>
Author
</
dt
>

		
<
dd
>
Jeffrey Zeldman
</
dd
>

		
<
dd
>
Ethan Marcotte
</
dd
>

	
</
div
>

	
<
div
>

		
<
dt
>
Publisher
</
dt
>

		
<
dd
>
New Riders Pub; 3rd edition (October 19, 2009)
</
dd
>

	
</
div
>

</
dl
>

A wrapper<div>like this is theonlyelement that can wrap those<dt>/<dd>groups.

And that’s it! That’s the anatomy of the description list,HTML's semantic way to mark up a list of name–value groups!

## Why Do We Need Semantics For This Anyways?

Before we learned about the<dl>,<dt>, and<dd>elements, my team used to use nested<div>s for this pattern all the time. It looked a lot like:

Copy code

<
div
 
class
=
"
book-details
"
>

	
<
div
 
class
=
"
book-details--item
"
>

		
<
div
 
class
=
"
book-details--label
"
>

			Title

		
</
div
>

		
<
div
 
class
=
"
book-details--value
"
>

			Designing with Web Standards

		
</
div
>

	
</
div
>

	
<
div
 
class
=
"
book-details--item
"
>

		
<
div
 
class
=
"
book-details--label
"
>

			Author

		
</
div
>

		
<
div
 
class
=
"
book-details--value
"
>

			Jeffrey Zeldman

		
</
div
>

		
<
div
 
class
=
"
book-details--value
"
>

			Ethan Marcotte

		
</
div
>

	
</
div
>

	
<
div
 
class
=
"
book-details--item
"
>

		
<
div
 
class
=
"
book-details--label
"
>

			Publisher

		
</
div
>

		
<
div
 
class
=
"
book-details--value
"
>

			New Riders Pub; 3rd edition (October 19, 2009)

		
</
div
>

	
</
div
>

</
div
>

This has all the information about the book, right? Why do weneedsemantics for a list of name–value groups in the first place if something like a series of nested<div>s could get the job done?

When determining whether a semantic element might be appropriate for a given pattern, I find it helpful to ask,“What benefits —even theoretical— could we get if computers could recognize this pattern?”In this case, what lift could we get if browsers could somehow recognize a list of name–value groups?

Answers to that question will be varied. I tend to spend a lot of time advocating for web accessibility, so my first thought tends to be how screenreaders could interpret the pattern. Off the top of my head, I can think of a couple of benefits screenreader users could get from their screenreaders recognizing this pattern:

1. The screenreader could tell the user how many name–value groups are in the list.
2. The screenreader could tell the user how far into the list they are.
3. The screenreader could treat the list as one block that the user could skip over if they’re uninterested in it.

All of these could make the list more usable than a series of nested<div>s, which would treat each name and value in the list as nothing more than a standalone text node.

If you can come up with a couple of even theoretical lifts from the user’s device recognizing a pattern, then there’s a good chance that the pattern is a strong candidate for having some associated semantics.

For what it’s worth, these screenreader experiencesaren’thypothetical — they’re benefits that screenreader users really get from using<dl>in most browser/screenreader combinations. Admittedly, however, support for the<dl>element is not yet universal. You may decide that screenreaders’ fallback experience — treating the list as standalone text nodes — isn’t sufficient for your use case, and instead opt for something like a<ul>until support improves.

## Okay, Okay, One Last Example!

My favorite example, the one thatreallytakes the cake for me, isDungeons & Dragonsstatblocks, which are really “Oops! All Name–Value Pairs!”

No, really: just how many candidates for<dl>s do you see in this statblock alone?

I countedfivepossible description lists, personally. Here’s how I chose to mark this up:

Copy code

<
div
>

	
<
h1
>
Kobold
</
h1
>

	
<
small
>
Small humanoid (kobold), lawful evil
</
small
>

	
<
dl
>

		
<
div
>

			
<
dt
>
Armor Class
</
dt
>

			
<
dd
>
12
</
dd
>

		
</
div
>

		
<
div
>

			
<
dt
>
Hit Points
</
dt
>

			
<
dd
>
5 (2d6 - 2)
</
dd
>

		
</
div
>

		
<
div
>

			
<
dt
>
Speed
</
dt
>

			
<
dd
>
30 ft.
</
dd
>

		
</
div
>

	
</
dl
>

	
<
dl
 
aria-label
=
"
Ability Scores
"
>

		
<
div
>

			
<
dt
>
STR
</
dt
>

			
<
dd
>
7 (-2)
</
dd
>

		
</
div
>

		
<
div
>

			
<
dt
>
DEX
</
dt
>

			
<
dd
>
15 (+2)
</
dd
>

		
</
div
>

		
<
div
>

			
<
dt
>
CON
</
dt
>

			
<
dd
>
9 (-1)
</
dd
>

		
</
div
>

		
<
div
>

			
<
dt
>
INT
</
dt
>

			
<
dd
>
8 (-1)
</
dd
>

		
</
div
>

		
<
div
>

			
<
dt
>
WIS
</
dt
>

			
<
dd
>
7 (-2)
</
dd
>

		
</
div
>

		
<
div
>

			
<
dt
>
CHA
</
dt
>

			
<
dd
>
8 (–1)
</
dd
>

		
</
div
>

	
</
dl
>

	
<
dl
 
aria-label
=
"
Proficiencies
"
>

		
<
div
>

			
<
dt
>
Senses
</
dt
>

			
<
dd
>
Darkvision 60 ft.
</
dd
>

			
<
dd
>
Passive Perception 8
</
dd
>

		
</
div
>

		
<
div
>

			
<
dt
>
Languages
</
dt
>

			
<
dd
>
Common
</
dd
>

			
<
dd
>
Draconic
</
dd
>

		
</
div
>

		
<
div
>

			
<
dt
>
Challenge
</
dt
>

			
<
dd
>
1/8 (25 XP)
</
dd
>

		
</
div
>

	
</
dl
>

	
<
dl
 
aria-label
=
"
Traits
"
>

		
<
div
>

			
<
dt
>
Sunlight Sensitivity
</
dt
>

			
<
dd
>

				While in sunlight, the kobold has disadvantage

				on attack rolls, as well as on Wisdom (Perception)

				checks that rely on sight.

			
</
dd
>

		
</
div
>

		
<
div
>

			
<
dt
>
Pack Tactics
</
dt
>

			
<
dd
>

				The kobold has advantage on an attack roll against

				a creature if at least one of the kobold's allies

				is within 5 ft. of the creature and the ally

				isn't incapacitated.

			
</
dd
>

		
</
div
>

	
</
dl
>

	
<
h2
 
id
=
"
actions
"
>
Actions
</
h2
>

	
<
dl
 
aria-labelledby
=
"
actions
"
>

		
<
div
>

			
<
dt
>
Dagger
</
dt
>

			
<
dd
>

				
<
i
>
Melee Weapon Attack:
</
i
>
 +4 to hit, reach 5 ft.,

				one target. 
<
i
>
Hit:
</
i
>
 (1d4 + 2) piercing damage.

			
</
dd
>

		
</
div
>

		
<
div
>

			
<
dt
>
Sling
</
dt
>

			
<
dd
>

				
<
i
>
Ranged Weapon Attack:
</
i
>
 +4 to hit, reach 30/120 ft.,

				one target. 
<
i
>
Hit
</
i
>
: (1d4 + 2) bludgeoning damage.

			
</
dd
>

		
</
div
>

	
</
dl
>

</
div
>

This is just one way you could have opted to mark up that statblock.

I love this as a demonstration because it really goes to show just how versatile the description list pattern can really be — the lists of ability scores (STR,DEX, and so forth) and attacks both look very different, and yet, the description list pattern can span them all.

## Takeaways

Lists of name–value pairs (or, in some cases, name–value groups) are a common pattern across the web, in part due to their versatility.HTMLlets us mark up these lists with a combination of three elements:

* The<dl>, ordescription list, element,which wraps the entire list of name–value pairs
* The<dt>, ordescription term, element,which represents a name in our name–value pairs
* The<dd>, ordescription detail, element,which represents a value in our name–value pairs

Ascribing semantics to patterns such as these gives our users’ devices the information they need to curate useful, usable experiences — oftentimes in ways that we as developers may not expect.

To learn more about description lists and what’s allowed or not allowed, I recommendtheMDNdocs on the<dl>, orgoing directly to the specs!

## Footnotes

1. Prior toHTML5, this was called adefinition list. This is because the<dl>was originally only intended to represent glossaries of terms and their definitions. |Back to [1]
2. Previously known as thedefinition termanddefinition detailelements respectively. |Back to [2]