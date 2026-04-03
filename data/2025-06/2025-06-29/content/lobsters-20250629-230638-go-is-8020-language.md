---
title: Go is 80/20 language
url: https://blog.kowalczyk.info/article/d-2025-06-26/go-is-8020-language.html
site_name: lobsters
fetched_at: '2025-06-29T23:06:38.164677'
original_url: https://blog.kowalczyk.info/article/d-2025-06-26/go-is-8020-language.html
date: '2025-06-29'
tags: go
---

Home

Go is 80/20 language

2025-06-26 Thu

edit

Go is the most hated programming language. Compared to other languages, it provides 80% of utility with 20% of complexity. The hate comes from people who want 81% of utility, or 85% or 97%.

As Rob Pike said, no one denies that 87% provides more utility than 80%. The problem is that additional 7% of utility requires 36% more work.

Here are some examples.

Someone complained on HN that
struct tags
 are a not as powerful as annotations or macros. I
explained
 that this is
80
⁄
20
 design.

Go’s
testing support
 in standard library is a couple hundred lines of code, didn’t change much over the years and yet it provides all the basic testing features you might need. It doesn’t provide all the convenience features you might think of. That’s what Java’s jUnit library does, at a cost of tens of thousands lines of code and years of never-ending development. Go is
80
⁄
20
 design.

Goroutines
 are
80
⁄
20
 design for concurrency compared to async in C# or Rust. Not as many features and knobs but only a fraction of complexity (for users and implementors).

When Go launched it didn’t have user defined generics but the built-in types that needed it were
generic: arrays/slices, maps, channels
. That
80
⁄
20
 design served Go well for over a decade.

Most languages can’t resist driving towards 100% design at 400% the cost. C#, Swift, Rust - they all seem on a never-ending treadmill of adding features. Even JavaScript, which started as a
70
⁄
15
 language has been captured by people whose job became adding more features to JavaScript.

If
80
⁄
20
 is good, wouldn’t
70
⁄
15
 be even better? No, it wouldn’t. Go has shown that you can have a popular language without enums. I don’t think you could have a popular language without structs. There’s a line below which the language is just not useful enough.

Finally, what does “work” mean?

There’s
work by the users
 of the language. Every additional feature of the language requires the programmer to learn about it. It’s more work than it seems. If you make functions as first class concepts, the work is not just learning the syntax and functionality. You need to learn new patterns of coding, like functions that return functions. You need to learn about currying, passing functions as arguments. You need to learn not only
how
 but also
when
: when you should use that powerful functionality and when you shouldn’t.

You can’t skip that complexity. Even if you decide to not learn how to use functions as first class concepts, your co-worker might and you have to be able to understand his code. Or a useful library uses it or a tutorial talks about it.

That’s why 80+% languages need coding guidelines. Google
has one for C++
 because hundreds of programmers couldn’t effectively work on shared C++ codebase if there was no restriction on what features any individual programmer could use. Google’s C++ style guide exists to lower C++ from 95% language to 90% language.

The other
work is by implementors
 of the language. Swift is a cautionary tale here. Despite over 10 years of development by very smart people with practically unlimited budget, on a project that is a priority for Apple, Swift compiler is still slow, crashy and is not meaningfully cross platform.

They designed a language that they cannot implement properly. In contrast: Go, a much simpler but still very capable language, was fast, cross platform and robust from version 1.0.

## activity

* tweaked the design of this blog
* yesterday I did a lot of changes toEdnato support folding of blocks, persisting that across sessions. I also refactored loading process. That means I might have broken things so today is testing those changes and if no major problems detected, deploying a new version

daily thoughts

go

 Jun 26 2025



 try my software


Edna


 note taking app for developers and power users



 optimized for speed



 cross between Obsidian and Notational Velocity


SumatraPDF

small, fast,
 free PDF / ePub / comic book reader for Windows

Feedback about page:

Feedback:Optional: your email if you want me to get back to you:

Send FeedbackCancel

Home

•

Software

•

Writings

•

Contact Me
