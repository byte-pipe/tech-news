---
title: Technical Writing Advice - DEV Community
url: https://dev.to/pauljlucas/technical-writing-advice-28a6
site_name: devto
content_file: devto-technical-writing-advice-dev-community
fetched_at: '2026-06-25T11:56:05.853564'
original_url: https://dev.to/pauljlucas/technical-writing-advice-28a6
author: Paul J. Lucas
date: '2026-06-18'
description: Some advice for writing technical material. Tagged with documentation, technical, writing.
tags: '#documentation, #technical, #writing'
---

Documentation as a system interface

## Introduction

I’ve occasionally thought about writing about how to write (and hownotto write) technical material. Recently, someone e-mailed me asking for advice about doing just that. So this article is a collection of my previous thoughts about this as well as a distillation of how I replied to that e-mail.

Any kind of writing, like many other human endeavors, is a combination oftalentandskill. For talent, you’ve either got it or you don’t; whereas skill can be learned, improved, and mastered. It’s generally difficult even to explain talent because it’s largely unconscious. I can’t tell youhowthe amorphous ideas in my head get converted to words on a page or screen — it just happens; however, I can tell you some things to do (andnotdo).

There are many kinds of technical material. I’ve mostly written articles, journal papers, Unix-style manual pages, API documentation, and a couple of books, so my advice is relevant only for those.

I largely consider the following advice to beobvious, so I don’t think itshouldbe necessary; but I’ve seen lots ofbadtechnical writing, so I guess the advice is apparently necessary after all.

The advice can be distilled into the following points. Your writing should be:

* Different.
* Well-formatted.
* Right.
* Precise.
* Complete.
* Consistent.

Also note that this advice is from the perspective of doing yourowntechnical writing, i.e., writing about whatyouwant to write about. If you’re a technical writer by trade, then your day job is writing about what other people want you to write about. You’re also most likely constrained by an in-house style guide. My advice isn’t for you.

## Different

Before actually writing anything, you should first determine whether what you want to write about is worth writing at all. Does the world really need yet another introduction to basic data types likeintandcharin C?

However, if you’re going to goreallydeep into or show some obscure thing about or a creative use of a topic, i.e., somethingdifferent, then by all means go ahead.

## Formatting

To me, it should beobviousthat what you write should be well-formatted — yet I’ve seen so many examples of badly formatted writing. When badly formatted, reading becomes visually jarring and a chore to slog through. I don’t even understand how anyone can publish anything that’s badly formatted. Don’t they look at it and think, “This looks terrible!”? (I suspect there’s a gene for having an aesthetic sense and some people don’t have it.)

In contrast, in well-formatted writing, the formatting just fades into the background so that you don’t even notice it and reading becomes easy.

For technical writing involving code, the code should be in a different typeface, generallymonospaced, and typicallyCourier.

“Typeface” is the correct term. Atypefaceis a style of letters and symbols; afontis a typeface in a particular size (e.g., 10 point) and style (e.g., bold). Courier, Helvetica, and Times Roman are typefaces; Helvetica 10 Bold is a font.

I blame Apple for everyone’s mis-use offontto meantypeface. Originally, theLisausedType Stylefor the name of what is now theFontmenu in most GUI applications. But then for some reason, theMacchanged the menu name toFontand the mis-use ensued.

If what you write is badly formatted, the rest pretty much doesn’t matter since nobody is going to want to read it anyway.

Some things that form part of my (and others’) styles include:

* Use inline or footnotes for incidental information or to cite sources. (Alternatively, you can use brackets like [42] or [Lucas, 1992] to cite sources with a References section.)
* Use parentheses for clarifying information or an aside that isn’t big enough to warrant either an inline or footnote.
* Use italics for one of emphasis, for the first occurrence of an important term, or the title of another work.
* Use quotes for one of literal text, a definition, a colloquial term, or a metaphor.

For example that illustrates most of the above, here’s an excerpt fromWhy Learn C, §1.1, p. 3:

C program source files conventionally end with a “.c” extension, so, assuming this program is in a filehello.c, it must becompiled(converted from source code into an executable) with aC compiler. On most Unix systems, the C compiler is named “cc” (short for “C compiler”).

## Be Right

It should also beobviousthat what you write should be right — yet I’ve seen so many examples of what someone has written is flat outwrong. Even if you think you know something well, double check before you write about it.

## Be Precise

While I think all writing should be precise, technical writing especially needs to be precise. Some examples:

* Parameters and arguments are different things.
* If something must be true, then use “must.” (See alsoRFC 2119.)
* Use “only if” whenever possible.

For an example of “only if,” consider:

The standard library functionisprintreturns true if a character is “printable,” that is one of a space, a punctuation symbol, a letter, or a digit.

The problem with just using “if” is that it incorrectly leaves open the possibility thatisprintreturns true in other cases as well. Replacing “if” with “only if” correctly eliminates that possibility. As a rule of thumb, any time you use “if” in a sentence, try replacing it with “only if”: if the sentence still sounds right and is more correct, then use “only if.”

## Be Complete

Don’t write something that’s either only partly true or mostly true. The situation you want to avoid is a reader reading something you’ve written and thinking that’sallthere is to the topic.

Yes, I understand that you may not want to wade deep into the weeds in an introduction for a topic. If that’s the case, at least mention that there’s more to a topic that you’ll get to later or can safely be ignored for now. For example,Why Learn C, §1.5, p. 14, contains the sentence:

Before continuing the tour, we need to digress on computer memory. It’s basically a (very long) sequence of bytes, each having a unique integer address.

While that’s true, it’s onlymostlytrue; but then it’s followed by the inline note:

■ This is an oversimplification due to both register and cache memory, but those can be safely ignored for now. □

## Be Consistent

Be consistent about word choices and term use. For example, if you use “error code,” don’t later write “status code.” Readers may wonder if they’re the same thing.

## A Note on AI

Don’t use AI to do the majority (or all) of your writing, certainly don’t copy & paste verbatim from it. Sometimes I use AI like a thesaurus to suggest alternate words or terms, but that’s pretty much it for me.

If you’re writing but not fluent in a language that is not your native language, you can be forgiven for using AI a bit more, e.g., copying something you’ve written into an AI and asking it for advice. Still, don’t copy its suggestions verbatim: edit them to fit into the rest of your writing style.

## Things to Not Do

Here’s a non-exhaustive list of things that, when I see them, don’t give me confidence that the rest of what I’m about to read will be worth my time.

* Unless you’re writing a personal account of something or giving a personal opinion, don’t write in first-person (“I ...”).
* Don’t include gratuitous images. Include images only that illustrate what you’re trying to explain. Gratuitous images are distracting. Even worse are animated images. You don’t want what you write to look gaudy.

For titles:

* Don’t use numbers of things (unless there’s some importance to the numbers).
* Don’t use hyperbole.
* Don’t use click-bait wording.

It makes your writing sound juvenile. Here’s an actual bad example I recently found online:

7 Coding Patterns I Stole From Senior Engineers

Who cares if it’s seven? Or five? Or ten? “Stole?” It’s calledlearning from— presumably from open source that’s, well, open and free to learn and copy from. Better:

Coding Patterns Used by Senior Engineers

Or something like that.

## Conclusion

To adapt a some advice one of my mentors gave to me once: do you want people to remember your writing for the way it looked or for what it said?

If you want to be taken seriously, then write as if you were submitting your writing to a prestigious journal or publisher. Some day, you might want to.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.
 Some comments have been hidden by the post's author -find out more

For further actions, you may consider blocking this person and/orreporting abuse