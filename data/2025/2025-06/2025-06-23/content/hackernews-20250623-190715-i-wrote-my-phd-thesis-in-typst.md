---
title: I wrote my PhD Thesis in Typst
url: https://fransskarman.com/phd_thesis_in_typst.html
site_name: hackernews
fetched_at: '2025-06-23T19:07:15.401073'
original_url: https://fransskarman.com/phd_thesis_in_typst.html
author: todsacerdoti
date: '2025-06-23'
---

## I wrote my PhD Thesis in Typst

I recently submitted myPhD thesis, and while waiting for the physical copies to get printed I thought I'd write about something you (hopefully) wouldn't notice when reading it. I wrote it in Typst, not LaTeX. In this post I will talk a bit about what went well and what didn't.

Typst (https://typst.app/) is a modern take on a typesetting language that I think has a real shot at dethroning LaTeX. I would describe the language as a mix of markdown and dynamically typed Rust, which may sound weird but is a really nice fit. Day-to-day document writing being markdown-like is very comfortable (certainly much nicer than littering your writing with\). The scripting language is powerful, well thought out, and makes it very easy to jump between code and typesetting. For example

Produces

This isbold text. The sum of [1, 2, 5, 8] is16

In the rest of this post, I will talk about some of the things I liked and disliked about Typst while writing the thesis.

### The good

#### Compile times

The thing that pushed me over the edge to try Typst for my thesis was a friend telling me his LaTeX thesis took 90 seconds to compile towards the end. I am far too easily distracted to tolerate 90 second compile times when I'm making small changes. The Typst compiler isfast, on small-medium sized documents it compiles fast enough to do live writing in the PDF preview. As my thesis grew beyond 150 pages, compile times dropped a bit. Clean builds take about 15 seconds, but it also does incremental compilation so forcontentchanges, it is still nearly instant, for local layout changes it takes a second or two. Even for large global template changes,  10 seconds is a whole lot better than 90 seconds, and I am confident that being able to iterate on layout and style 9 times faster produced a nicer looking result in the end.

#### The language

The Typst language is amazingly well thought out. Markdown syntax is nicer than Tex syntax for general writing, but what really shines is the scripting language. My biggest complaint with LaTeX as a language is thatnothingis consistent. Every package defines their own little utilities for even basic things likeif-statements. It feels like you don't learn LaTeX, you learn each package individually. Typst on the other hand is a well-designed dynamically typed language. Being Rust inspired and me being a Rust user meant that it barely feels like I had to learn the language at all, I can just assume that I'm writing Rust. That's not true as you get into more advanced things of course, but it feels like IknowTypst in a way that I don't think is possible with LaTeX.

This isn't just philosophical, being able to script Typst is extremely useful. For example, a central part of my thesis is that there are a lot of hardware description languages out there, and I wanted to come up with a way to categorize them. Over a few years, I have collected them all with some metadata in a toml file (https://gitlab.com/TheZoq2/list_of_hdls/). Since Typst can parse toml, I could simply use that data to generate a figure to put the languages into my taxonomy:

Sure, it would be possible to do this in many other ways, but having it self-contained in the document is nice, and at this point Typst is one of my favourite scripting languages, so using it here is a no-brainer and something I did for pretty much all my data processing.

A modern language of course also comes with modern tools, a compiler with dependency management, a working language server protocol integration for editors etc. All that makes it even nicer to work with.

#### Layout Tweaks

A few times I have tried to understand latex templates, and every time it has ended in frustration. I believe it took me longer to remove a header from our university presentation template than it did for me to write a new presentation template in Typst. Again, this comes down to the language being well-thought-out and consistent. This was also hugely advantageous when tweaking my thesis template the way I want it. Naturally, this is something of a double-edged sword, had I used LaTeX I would not have had to make a template in the first place, but at the same time, modifying anything in that template would have been much more difficult. This way I ended up with everything right where I wanted it without the frustration of figuring out how to get the results I wanted.

#### Syntax Highlighting

My thesis has a lot of code in it, and Ihatereading code without good syntax highlighting. LaTeX's syntax highlighting systems leave a lot to be desired, but Typst's certainly does not. It does have built in support for textmate grammars, the same system used by sublime text for syntax highlighting, but for various reasons I decided not to use them. Instead, I just used Typst'sshowrules with regex. For example,

will syntax highlight Spade conditionals. My syntax highlighting definitions¹ are… more more complicated but produce results that I am very happy with. At some point, I even ended up parsing a subset of Spade in Typst with a recursive descent parser because I really wanted to highlight named arguments. Was that a good way to spend my time? Debatable, but it certainly was not something I would have dreamt of doing in LaTeX.

1:
https://gitlab.com/TheZoq2/typst-common/-/blob/main/highlight.typ

#### The error messages

LaTeX error messages are awful. Typst isgenerallymuch better with errors thatpointto the right place, gives accurate information about what is wrong, and doesn't fill the terminal with garbage. No more "Missing $ inserted!".

### The bad

#### Bibliography Management

Typst's bibliography management leaves some things to be desired when writing a whole thesis. The first roadblock I encountered was that you can only have one bibliography section and file per document. One per document is a deal breaker because I need one for the introduction, and one per included paper. My masterbibfile makes heavy use of Bibtex variables which are included from other sources, this does not work in Typst. I ended up solving it with a Makefile that merges my files into one before going to Typst, but that's not ideal ²

The multi-bibliography problem was worse, but luckilyhttps://typst.app/universe/package/alexandriacame along as I was working to save the day. It requires a little bit of work per bibliography so I would absolutely have preferred an automated system where I just do#bibliography(...)and would insert all the citations I've used since last time, but Alexandria did the job.

Then there is thestyleof the bibliography… At first glance, it looks fine but when you have an advisor that is very picky about bibliography styles, things start to go wrong. For example, paper titles should be written in sentence case with quotes around them, for example:

[1] F. Skarman and O. Gustafsson, “Spade: An expression-based HDL with pipelines,” inProc. Workshop Open-Source Des. Automat., Apr. 2023.

But in the Bibtex file it is very common for the titles to appear in their original title case form (Spade: An Expression-Based HDL With Pipelines). By default, Typst does not seem to do this conversion, but it can be turned on with a custom.cslfile. However, then it will not do it quite right. "Expression-Based" turns into "expression-Based" for example. In the end, I did the conversion to sentence case manually.

The system is also kind of strange about what information it includes in references. For example, the@TechReportclass in Bibtex has aninstitutefield. This does not get included, but changing it topublisher(which AFAIK is not a standard field in Bibtex) makes it work.

I also found out that book titles should not be written with quotes, but with italics. I set a rule to match onbookin my CSL field but it did not have an effect on@Book, only on@InCollection. In general, the bibliography management is death by a thousand papercuts, and a lot of them are caused by a very opaque translation from Bibtex fields to CSL…

2: In retrospect I wonder if I could not have loaded the files and merged them inside Typst 🤔 to avoid the Makefile

#### The error messages

Wait, didn't I say that the error messages are good before? I did,but they are only good in simple cases. For example, with the Alexandria library, a bibliography that fails to compile only says "failed to parse bibliography" and does not give further errors. Errors in stateful show rules also do not give any breadcrumbs back to where the error was triggered which makes them hard to track down. In general, I would like to see a longer traceback for errors to avoid having feel like I'm writing latex again by binary searching recent changes.

My thesis also has the dreadedLayout did not converge in 5 attemptswarning which is pretty much impossible to debug currently. In my case, things turn out fine, but it is a bit sketchy. I believe this is being worked on.

### The "It's complicated"

LaTeX is everywhere. My early papers were of course written in latex and I had to convert them to Typst. This was surprisingly easy with Pandoc which did 95% of the work with me just having to do a bit of final cleanup. Unfortunately, I also wrote a few new papers for the thesis that will be submitted later, and that's a more complicated situation since journals demand LaTeX code. My workflow so far has been to write the initial version of papers in Typst, submit the PDF as generated by Typst, then for the final version submit a converted version.

For conversion, I don't believe pandoc works (or doesn't work the way I want it) so I had wrote my own tool ³. It lets me do 90% of the content and layout in Typst, use Typst for generating figures and code snippets, and then I can insert style tweaks with inline LaTeX. The Typst compiler being open source was of huge help here as I just hook into that. I will talk more about that tool in a future post once one of my papers compiled using it is made public

A big downside of this is that it generates latex with\includepdffor things like inline code. I am hoping publishers will not count those as figures and be weirded out by them…

Everyone also knows LaTeX, so if I want to use Typst in collaboration, I force everyone I want to work with to learn it. My advisor was not super pleased with that 😇

3:
https://gitlab.com/TheZoq2/typstex2/

#### Ecosystem

The Typst ecosystem is young. Being able to whip up a thesis template and doing all the tweaks to make itjust the way I want itis great. On the other hand, since I am probably the first person at my university to do it meant Ihadto whip up a template. For submitting to conferences and journals, there are Typst templates, but they are not flawless. The IEEE template only has conference variant, not a journal variant. The LLNCS template I found on git looked OK but had the wrong margins, so our paper ended up being slightly longer when converted to latex.

### Conclusion

With all this in mind, would I recommend using Typst for a PhD Thesis? If you are like me,   absolutely   probably. I like playing with programming languages, I'm easily frustrated by tools that bother me. I also much prefer a tool that I can tweak to get exactly the way I want over a tool that "just works" out of the box but where it is hard to tweak. In the end, I don't think I compromised on the quality of the document, the quick iteration probably made things look better than they would have otherwise. It certainly took some effort to work around a few issues, and some extra work setting up a template, but that wasfunwork compared to having to suffer through LaTeX's annoyances.

If you're not like me and want a system that works out of the box, Typst today probably isn't the right choice for a PhD thesis. But I would still recommend playing with Typst for smaller things but leave the big documents to LaTeX, for now.

Updated June 23 2025: Changed absolutely to probably in the conclusion and added the 'advisors perspective section below'

### The Advisors Perspective

My advisor had a somewhat different perspective on this and I think it is worth posting that here. This is essentially taken verbatim from a LinkedIn comment where we discussed it:

"The thing is that you HAD to tweak it to make things look the way they should. Not sure that is a benefit.

Would I, as a supervisor, recommend someone to use Typst if they are in a field where all manuscripts are written in LaTeX? No. The fact that Frans is clever and a good programmer helped for sure. But think twice. Thrice if you are not a good programmer. And ask Frans for the scripts he developed to move things between Typst and LaTeX.

It is simply not mature enough for most people to be used at this stage when you have to produce documents looking a particular way. Unless you are willing to spend much time on tweaking things etc. It may be mature for sure and someone will have to contribute to make it more mature for sure.

"Good" thing from a supervisor perspective is that I barely edited any text in the source at all, but had to let Frans edit the text (and format). Quite inefficient though.

Despite the disagreement on the procedure, I cannot stress enough that the end result was great though! Both technically and layoutwise."

He certainly has a point here, especially needing to be interested in working around issues and needing some programming experience to get things working perfectly. The problem of having to spend time adjusting things is in my opinion hard to quantify since it trades easy fun upfront work for frustration over other aspects of the language.
