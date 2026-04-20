---
title: 'C++26 is done! — Trip report: March 2026 ISO C++ standards meeting (London Croydon, UK) – Sutter’s Mill'
url: https://herbsutter.com/2026/03/29/c26-is-done-trip-report-march-2026-iso-c-standards-meeting-london-croydon-uk/
site_name: hnrss
content_file: hnrss-c26-is-done-trip-report-march-2026-iso-c-standards
fetched_at: '2026-03-30T11:26:06.469335'
original_url: https://herbsutter.com/2026/03/29/c26-is-done-trip-report-march-2026-iso-c-standards-meeting-london-croydon-uk/
date: '2026-03-29'
published_date: '2026-03-29T16:24:16+00:00'
description: 'News flash: C++26 is done! 🎉 On Saturday, the ISO C++ committee completed technical work on C++26 in (partly) sunny London Croydon, UK. We resolved the remaining international comments on the C++26 draft, and are now producing the final document to be sent out for its international approval ballot (Draft International Standard, or DIS) and…'
tags:
- hackernews
- hnrss
---

Herb Sutter


C++


2026-03-29
2026-03-29


8 Minutes


News flash: C++26 is done!🎉

On Saturday, the ISO C++ committee completed technical work on C++26 in (partly) sunny London Croydon, UK. We resolved the remaining international comments on the C++26 draft, and are now producing the final document to be sent out for its international approval ballot (Draft International Standard, or DIS) and final editorial work, to be published in the near future by ISO.

This meeting was hosted byPhil NashofShaved Yaks, and theStandard C++ Foundation. Our hosts arranged for high-quality facilities for our six-day meeting from Monday through Saturday. We had about 210 attendees, about 130 in-person and 80 remote via Zoom, formally representing 24 nations. At each meeting we regularly have new guest attendees who have never attended before, and this time there were 24 new guest attendees, mostly in-person, in addition to new attendees who are official national body representatives. To all of them, once again welcome!

The committeecurrently has 23 active subgroups, nine of which met in 6 parallel tracks throughout the week. Some groups ran all week, and others ran for a few days or a part of a day, depending on their workloads. We had three technical evening sessions on C++ compiler/library implementations, memory safety, and quantities/units. You can find a brief summary of ISO procedureshere.

## C++26 is complete: The most compelling release since C++11

Per ourpublished C++26 schedule, this was our final meeting to finish technical work on C++26. No features were added or removed; we just handled fit-and-finish issues and primarily focused on finishing addressing the 411 national body comments we received in the summer’s international comment ballot (Committee Draft, or CD).

If you’re wondering “what are the Big Reasons why should I care about C++26?” then the best place to start is with the C++26 Fab Four Features…

### (1) Reflection, reflection, reflection

Reflection is by far the biggest upgrade for C++ development that we’ve shipped since the invention of templates. For details, seemy June 2025 trip reportandmy September 2025 CppCon keynote:“Reflection: C++’s decade-defining rocket engine.”From the talk abstract:

“In June 2025, C++ crossed a Rubicon: it handed us the keys to its own machinery. For the first time, C++ can describe itself—and generate more. The first compile-time reflection features in draft C++26 mark the most transformative turning point in our language’s history by giving us the most powerful new engine for expressing efficient abstractions that C++ has ever had, and we’ll need the next decade to discover what this rocket can do.”

### (2) Less UB for more memory safety: C++ code is more memory safe just by recompiling as C++26

C++26 has important memory safety improvements that you get just by recompiling your existing C++ code with no changes. The improvements come in two major ways.

No more undefined behavior (UB) for reading uninitialized local variables.This whole category of potential vulnerabilities disappears in C++26, just by recompiling your code as C++26. For more details, seemy March 2025 trip report.

The hardened standard library provides initial cross-platform library security guarantees, including bounds safety for dozens of the most widely used bounded operations on common standard types, including vector, span, string, string_view, and more. For details, seemy February 2025 trip reportand run (don’t walk) to read the November 2025 ACM Queue article“Practical Security in Production: Hardening the C++ Standard Library at Massive Scale”to learn how this is already deployed across Apple platforms and Google services, hundreds of millions of lines of code, with on average 0.3% (a fraction of 1%) performance overhead. From the paper:

“The final tally after the rollout was remarkable. Across hundreds of millions of lines of C++ at Google, only five services opted out entirely because of reliability or performance concerns. Work is ongoing to eliminate the need for these few remaining exceptions, with the goal of reaching universal adoption.

Even more telling, the fine-grained API [to opt out] for unsafe access was used in just seven distinct places, all of which were surgical changes made by the security team to reclaim performance in code that was correct but difficult for the compiler to analyze. This widespread adoption stands as the strongest possible testament to the practicality of the hardening checks in real-world production environments.”

This is no just-on-paper design. At Google alone, it has already fixed over 1,000 bugs, is projected to prevent 1,000 to 2,000 bugs a year, and has reduced the segfault rate across the production fleet by 30%.

And, now, it is standardized for everyone in C++26. Thank you, Apple and Google and all the standard library implementers!

### (3) Contracts for functional safety: pre, post, contract_assert

In C++26, we also have language contracts: preconditions and postconditions on function declarations and a language-supported assertion statement, all of which are infinitely better than C’s assert macro.

Note that some smart and respected ISO C++ committee experts have sustained technical concerns about contracts. For my summary of the contracts feature and all the major repeated concerns (with my opinions about them, which could be wrong!), seemy CppCon 2025 contracts talk. In February 2025 when we took the plenary poll to adopt contracts in the C++26 working draft (“merge it to trunk”), the vote was:

100 in favor, 14 opposed, and 12 abstaining

Since then, the concerns have all been deeply rediscussed for the last three meetings thanks to thoughtful and high-quality technical papers; all of those papers have continued to be fully heard, often for multiple days and at many telecons between meetings. At our previous meeting in November 2025, we did fix a couple of contracts specification bugs thanks to this feedback! Yesterday, when we took the plenary poll to finalize and ship the C++26 standard, the vote was non-unanimous primarily because of the sustained concerns about contracts:

114 in favor, 12 opposed, and 3 abstaining

The unusually low number of abstentions shows that virtually all our experts now feel sure about their technical opinions, either for or against contracts. After extensive scrutiny, the committee’s opinion is clear: The ISO C++ committee still wants contracts, and so contracts have stayed in C++26.

### (4) std::execution (aka “Sender/Receiver”)

std::executionis what I call “C++’s async model”: It provides a unified framework to express and control concurrency and parallelism. For details, seemy July 2024 trip report. It also happens to have some important safety properties because it makes it easier to write programs that usestructured(rigorously lifetime-nested) concurrency and parallelism to be data-race-free by construction. That’s a big deal.

I do want to write a warning though: This feature is great (my company has already been using it in production) but it’s currently harder to adopt than most C++ features because it lacks great documentation and is missing some “fingers-and-toes” libraries. For now, do expect great results from std::execution, but also expect to spend some initial time on learning with the help of a friend who already knows it well, and to write a few helper adapter libraries to integrate std::execution with your existing async code.

## C++26 adoption will be fast

There are two reasons I expect C++26 to be adopted in industry very quickly compared with C++17, C++20, and C++23.

First, user demand for this feature set is extraordinarily high. C++11 was our last “big and impactful” release that was chock full of features that the vast majority of C++ developers would use daily (auto, range-for, lambdas, smart pointers, move semantics, threads, mutexes, …). Since then, our followup triennial standards have also had some ‘big’ features like parallel STL, concepts, coroutines, and modules, but the reality is that those weren’t as massively impactful for all C++ developers as C++11’s features were, or as C++26’s marquee features of reflection and safety hardening will be now. So even if your company has been slow to enable the C++20 switch, I think you’ll find they’ll be much faster to enable C++26. There’s just so much more high-demand value that makes it an exciting and exceptionally useful release for everyone who uses C++.

Second, conforming compiler and standard library implementations are coming quickly. Throughout the development of C++26, at any given point both GCC and Clang had already implemented two-thirds of C++26 features. Today, GCC already has reflection and contracts merged in trunk, awaiting release.

## Work on C++29, especially on more memory safety and profiles

At this meeting we also adopted the schedule for C++29, which will be another three-year release cycle. To no one’s surprise, a major focus of the discussion about C++29-timeframe material was aboutfurther increasing memory safety.

This week, the main language evolution subgroup (EWG) reviewed updates on several ongoing proposals in the area of further type/memory-safety improvements for C++29, including: to pursue proposals to further reduce undefined behavior to be seen again in EWG for possible inclusion in C++29; and to pursue further development of safety profile papers in the safety and security subgroup (SG23) to then be brought to EWG targeting C++29. SG23 specifically worked onBjarne Stroustrup’s P3984 type safety profileusing the proposed general profiles framework by Gabriel Dos Reis.

Besides those sessions, type and memory safety was extensively discussed in two additional large-attendance sessions: an evening session on Wednesday night attended by the majority of the committee, and in an EWG memory safety dedicated session all Friday afternoon attended by about 90 experts. In particular, I want to thank Oliver Hunt of Apple for presenting the practical experience reportP4158R0, “Subsetting and restricting C++ for memory safety,”reporting how WebKit hardened over 4 million lines of code using a subset-of-superset approach (like Stroustrup’s Profiles) and showing how that has already made a profound difference in the security of C++ code in WebKit at scale. Here are a few highlights from the introduction slide (emphasisadded):

“Adopted ~4MLoC of code(i.e. w/o comments, tests, external libs, etc)

Closes multiple classes of vulnerabilities,current policies would have prevented majority of historical exploits

Found (andprevented exploitability) of new and existing bugs”

C++29 is already set to build even more on the safety improvements already in C++26, and I for one welcome our new era of safer-by-default-and-still-zero-overhead-efficient-C++ overlords. C++26 is the first step into a fundamentally new era: This isn’t our grandparents’ wild-west UB-filled anything-goes C++ anymore. But even as C++ moves to being more memory-safe by default, it’s staying true to C++’s enduring core of the zero-overhead principle… you don’t pay for what you don’t use, and even when some safety is so cheap that we can turn it on by default in the language you will always have a way to opt out when you need to get the last ounce of performance in that hot path or inner loop.

We did other work, including other things related to functional safety: EWG reviewed additional plans for applying contract checks in the language and standard library. The numerics subgroup (SG6) and library incubation subgroup (SG18) progressedP3045R7, “Quantities and units library”byMateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña, Chip Hogg, Nicolas Holthaus, Roth Michaels and Vincent Reverdyto the main library evolution subgroup (LEWG), and we had an evening session on the topic for the whole committee on Thursday evening. I encourage reading section 7.1 “Safety concerns” in the paper, including how technology like that in this paper could have improved Black Sabbath’s 1983 tour (which was hilariously lampooned in, of course,This Is Spinal Tap).

## What’s next

Our next two meetings will be inBrno, Czechia in Juneand inBúzios, Rio de Janeiro, Brazil in November. At those two meetings we will start work on adding features into the new C++29 working draft.

## Wrapping up

Thank you again to the about 210 experts who attended on-site and on-line at this week’s meeting, and the many more who participate in standardization through their national bodies!

But we’re not slowing down… we’ll continue to have subgroup Zoom meetings, and then in less than three months from now we’ll be meeting again in Czechia and online to start adding features to C++29, with many subgroup telecons already scheduled between now and then. Thank you again to everyone reading this for your interest and support for C++ and its standardization.

* Tagged
* C++
* c26
* contracts
* reflection
* safety
* security
* stdexecution




## Published byHerb Sutter

Herb Sutter is an author and speaker, a technical fellow at Citadel Securities, and serves as chair of the Standard C++ Foundation and chair emeritus of the ISO C++ standards committee.View all posts by Herb Sutter

Published

2026-03-29
2026-03-29
