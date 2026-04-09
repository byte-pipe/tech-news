---
title: 'Typst: a possible LaTeX replacement [LWN.net]'
url: https://lwn.net/Articles/1037577/
site_name: hackernews_api
fetched_at: '2025-09-28T10:10:32.209755'
original_url: https://lwn.net/Articles/1037577/
author: pykello
date: '2025-09-27'
description: 'Typst: A Possible LaTeX Replacement'
tags:
- hackernews
- trending
---

LWN
.net

News from the source






User:


Password:



 |


 |


Subscribe
 /

Log in
 /

New account

# Typst: a possible LaTeX replacement

September 17, 2025

This article was contributed by Lee Phillips

Typstis a program for document
typesetting. It is especially well-suited to technical material
incorporating elements such as mathematics, tables, and floating
figures. It produces high-quality results, comparable to the gold standard,LaTeX, with a simpler markup
system and easier customization, all while compiling documents
more quickly. Typst is free software, Apache-2.0 licensed, and is written in Rust.

#### Desire for a LaTeX replacement

LaTeX is a document typesetting system built on the foundation of Donald
Knuth'sTeX. LaTeX has become the
standard tool for the preparation of scholarly papers and books in several
fields, such as mathematics and computer science, and widely adopted in
others, such as physics. TeX and LaTeX, whichpredate
Linux, are early free softwaresuccess
stories. The quality of TeX's (and therefore LaTeX's) output rivals the
work of skilled hand typesetters for both text and mathematics.

$ sudo subscribe today

Subscribe today and elevate your LWN privileges. You’ll have
access to all of LWN’s high-quality articles as soon as they’re
published, and help support LWN in the process.Act nowand you can start with a free trial subscription.

Despite the acclaim earned by LaTeX, its community of users has been
griping about it for years, and wondering aloud whether one day a
replacement might arrive. There are several reasons for this
dissatisfaction: the LaTeX installation is huge, compilation of large
documents is not fast, and its error messages are riddles delivered by an
infuriating oracle. In addition, any nontrivial customization or alteration to the
program's behavior requires expertise in an arcane macro-expansion
language.

Along with the griping came resignation: after decades of talk about a
LaTeX replacement with nothing plausible on the horizon, and with the
recognition that LaTeX's collection of specialized packages would take
years to replace, it seemed impossible to dislodge the behemoth from its
exalted position.

#### Introducing Typst

In 2019 two German developers, Laurenz
Mädje and Martin Haug, decided to try to write a LaTeX replacement "just for fun". In 2022, Mädje wrote his
computer sciencemaster's
thesis about Typst. In March 2023, its
first pre-release beta versionwas announced; a
month later, semantic versioning was adopted with therelease of
v0.1.0.Typst is now atv.0.13.1and shows
365 contributors on itsGitHub repository.

I had been aware of this project for over a year but had not paid much
attention, assuming it to be yet another attempt to supplant LaTeX that was
doomed to fail. A rising chorus of enthusiasm among early
adopters, and the beginnings ofacceptanceof
Typst manuscripts by scholarly journals, made me curious enough
to take the young project for a spin.

Typst is available as Rust source and as a compiled binary. To install,
visit thereleases
pageand download the appropriate archive. There are options for Linux,
macOS and Windows; I used the
precompiled Linux version for my testing.

The "typst" command accepts several subcommands. Entering
"typst fonts" lists all of the usable fonts to be found in
standard locations on the machine; nonstandard font directories can be
added manually. In my case, Typst found all of my 476 fonts instantly;
the only ones omitted were some ancient PostScript Type 1 fonts used
by LaTeX. Users who have LaTeX installed will have a large collection of
OpenType and TrueType math and text fonts on their machines; Typst can
use all of these. But Typst will work fine without them, as the program has
a small collection of fonts built in (try "typst fonts
--ignore-system-fonts" to see them).

Two other subcommands to explore are
"compile", which generates the output (PDF by default, with PDF/A,
SVG, and PNG available, along with HTML under development) from a source file, and
"watch" for interactive editing. Thewatchsubcommand keeps a Typst process running that
incrementally and automatically compiles the document to PDF in response to
changes in the source. To use "typst watch" effectively, the
screen should be divided into three windows: a small terminal window to monitor
thetypstoutput for error (or success) messages, the editing
window, and an area for any PDF reader that automatically reloads the
displayed document when it changes (many, such as my favorite,Sioyek, do this). The result is a
responsive live preview, even of large documents, due to Typst's speed and
incremental compilation. For example, Frans Skarmandescribedhis experience writing his doctoral thesis in Typst, and noted
that he was able to enjoy nearly instant previews of content changes to
the book-length document.

#### How Typst improves on LaTeX

Typst output is quite close to that of LaTeX. It uses the sameline-breaking
algorithmdeveloped by Donald Knuth and Michael Plass for TeX, so it
creates nicely balanced paragraphs of regular text. Its mathematical
typesetting algorithms arebased closelyon the
TeX algorithms, and indeed mathematical rendering is nearly
indistinguishable between the two systems.

Getting started with LaTeX can be confusing for newcomers, because it comes
with several alternative "engines" reflecting the long and complex history
of the project. These are the various binaries such as "pdflatex",
"tex", "xelatex", "luatex", "lualatex",
and more, each with somewhat different capabilities. For Typst there is
only "typst".

Markup in Typst is less verbose and easier to read than in LaTeX. It
dispenses with the plethora of curly brackets and backslashes littering
LaTeX documents by adopting, for prose, syntax in the style ofMarkdown, and, for
equations, a set of conventions designed for easy input. The
fact that curly brackets and backslashes are awkward to type on German
keyboards may have provided a little extra impetus for the developers to
create an alternative markup system that doesn't require a forest of these
symbols.

When users make syntax errors in markup or programming, inevitable
even in Typst, the system presents them with another dramatic improvement
over LaTeX (and TeX): error messages using colored glyphs that
clearly point out exactly where the problem is. I've even discovered that
Typst will save me from trying to run a syntactically correct infinite
loop.

Here is a bit of Typst markup for a shopping list, with
the resulting rendering to the right:

 = Shopping List

 == Vegetables

 + Broccoli
 + Asparagus (*fresh only*)
 + Plantains (_ripe and green_)

 == Booze

 + Rum
 - White
 - Dark
 + #underline[Good] gin

The example gives a flavor of Typst's terse markup syntax. Headings are
indicated with leading=signs. Automatically numbered lists are
created by prepending+signs to items, and bulleted lists with-signs; lists can be nested. Delimiters are shown for bold text
and italics. These are shortcuts, or markup syntax sugar, for Typst
functions for transforming text. Not every function has a corresponding
shortcut; in those cases one needs to call the function explicitly, as in
the final item.

Typst input is always within one of three modes. Markup (text) mode is the
default. The#sign preceding the function call in the last line
of the example
places Typst in "code mode". The "underline()" function accepts a number of keyword arguments that affect its behavior, and one trailing argument, in square brackets, containing the text that it modifies. In the example, we've stuck with the default behavior, but if we wanted, for example, a red underline, we could use "#underline(stroke: red)[Good] gin". Following the square-bracketed text argument, Typst returns to interpreting input in text mode.

Other functions produce output directly, rather than modifying a text argument. This bit of Typst input:

 #let word = "Manhattan"
 There are #str.len(word) letters in #word.

produces the output (in typeset form) "There are 9 letters in Manhattan.". The "len()" function is part of the
"str" module, so it needs the namespace.

Let's take a look at the LaTeX equivalent for the first half of the
shopping list for comparison:

 \documentclass[12pt]{article}
 \begin{document}
 \section*{Shopping List}

 \subsection*{Vegetables}

 \begin{enumerate}
 \item Broccoli
 \item Asparagus ({\bfseries fresh only})
 \item Plantains (\emph{ripe and green})
 \end{enumerate}
 \end{document}

The first two and the last line are boilerplate that is not required in
Typst. The difference in verbosity level and ease of reading the source is
clear.

The third Typst mode, in addition to markup and code, is math mode,
delimited by dollar signs. This is also best illustrated by an example:

 $ integral_0^1 (arcsin x)^2 (dif x)/(x^2 sqrt(1-x^2)) = π ln 2 $

When this is compiled by Typst, it produces the result shown below:

Those who've used LaTeX will begin to see from this example how math in
Typst source is less verbose and easier to read than in LaTeX. Greek
letters and other Unicode symbols can be used directly, as in modern LaTeX
engines such aslualatex, which welooked at back in 2017, but with no
imports required.

The advent of the LuaTeX and LuaLaTeX projects provided users who wanted to
incorporate programming into their documents a more pleasant alternative to
the TeX macro language. As powerful as the embedded Lua system is, however,
it betrays its bolted-on status, requiring users to negotiate the interface
between Lua data structures and LaTeX or TeX internals. In Typst,
programming is thoroughly integrated into the system, with no seams between
the language used for calculation and the constructs that place characters
in the final PDF. Typst programs are invariablysimplerthan their LuaLaTeX
equivalents. All authors using Typst will make at least some simple use of
its programming language, as such basic necessities as changing fonts, or
customizations such as changing the style of section headings, are
accomplished by calling Typst functions.

The Typst language is somewhat similar to Rust, perhaps
unsurprisingly. Most Typst functions arepure: they have no side effects and
always produce the same result given the same arguments (aside from certain
functions that mutate their arguments, such asarray.push()). This
aspect reduces the probability of difficult-to-debug conflicts among
packages that plague LaTeX, and makes it easier to debug Typst documents.

Although Typst uses the same line-breaking algorithm as LaTeX, its internal
approach to overall page layout isdistinct. Some
consequences are that Typst does a better job at handling movable elements
such as floating figures, and can, for example, easily split large tables
across page breaks, something that LaTeX struggles with even with
specialized packages.

#### Typst drawbacks

Typst's page layout algorithm doesn't always permit the refinements that
LaTeX is capable of.
For example, Typst is not as good
as LaTeX at avoidingwidows
and orphans.
Another salient deficiency is Typst's relative lack of specialized packages,
compared with the vast ecosystem produced by LaTeX's decades of community
involvement. However, the relative ease of programming in Typst (and the
well-organized and extensively commented underlying Rust code) suggests
that this drawback may be remedied before a comparable number of decades
have elapsed. Indeed, there are alreadyover 800 packages available. Typst still cannot do
everything that LaTeX can, but the breadth of its package collection is
encouraging.

Almost no journals that provide LaTeX templates for submissions offer a
Typst option, so physicists and mathematicians adopting Typst will need to
find a way to convert their manuscripts. This is made easier for those who
usePandoc, as that conversion program
handles Typst.

Another drawback is the difficulty of learning Typst. Theofficial documentationis confusingly
organized, with information scattered unpredictably among "Tutorial",
"Reference", and "Guides" sections. Concepts are not always clearly
explained, and sometimes not presented in a logical order. The manual is
not keeping up with the rapid development of the program, and contains some
out-of-date information and errors. None of this is surprising considering
how quickly the project is moving, its early stage, and its
small core team. A work-in-progress called theTypst
Examples Bookhas appeared, which may be a better starting point
than the official documentation.

There are other minor deficiencies compared with LaTeX, such as the
inability to include PDF documents. Typst provides no analogue to LaTeX'sparshapecommand, which lets authors mold paragraphs to, for
example, wrap around complex illustrations. The situation is likely to
change, however, as something likeparshapeisbeing
consideredfor the future.

More serious is the possibility of breaking changes as the system evolves,
always a risk of early adoption. I suspect, however, that these will require
only minor edits to documents in most cases. Progress seems to be steady,
rational, andresponsive to
user requests.

#### Conclusion

I'm using Typst in real work right now to write a physics paper. I will
need to submit my manuscript using the journal's LaTeX template, but I'm
taking advantage of Typst to make the entry of the paper's many equations
simpler, and I'lltransformthe result to
LaTeX with Pandoc without needing any manual adjustment. The tooling is excellent, as my preferred editor,Neovim, hassupportfor theTree-sitter
incremental parserfor Markdown and Typst, which provides syntax-aware highlighting
and navigation of the source files. I use Typst's fast incremental
compilation to get live feedback as I fiddle with my math markup.

I was skeptical when I downloaded Typst to try it out, but became
enthusiastic within minutes, as I saw the first (of many) of its lovely
error messages, and remained sanguine as I saw the quality of its output. I
predict that Typst will eventually take the place of LaTeX. But even if
that never comes to pass, it is a useful tool right now.

Index entries for this article

GuestArticles
Phillips, Lee

 to post comments




### To become success storyPosted Sep 17, 2025 15:45 UTC (Wed)
 byspacefrogg(subscriber, #119608)
 [Link] (22 responses)Obviously, after providing fitness for purpose, the second property that made the TeX ecosystem a success was that its contributors understood, fought for and respected the necessity to maintain forward compatibility as much as possible.There used to be the well-founded expectation from users that a typeset document did not change when processed by a future version of the processor, style or packages. In the long-run, this made learning and dealing with the languages intricacies and idiosyncrasies worthwhile. This has faded somewhat (looking at you, siunitx) in recent years since the first-generation contributors left the scene.I hope that the Typst maintainers and contributors understand this historic lesson as well.Also, TeX is a document processor able to document itself or at least its packages. And there is a reliable ecosystem for that as well (e.g. certain pressure on contributors to provide documentation along with code for acceptance).### To become success storyPosted Sep 17, 2025 17:07 UTC (Wed)
 bywtarreau(subscriber, #51152)
 [Link] (11 responses)> the necessity to maintain forward compatibility as much as possible.Interesting because while that may be true in theory, it's precisely the opposite that made me abandon it over time. Trying to rebuild my old docs systematically resulted in cryptic errors. Looking on the net suggested that foobar.sty was replaced by somethingelse.sty which was close enough but required modifications etc. It happened to me several times to spend half a day updating a 5-year old manual to accommodate new packages. It might very well just be that some packages are less strict than the lower layers and that I hadn't been using state-of-the-art ones, but for the end user experience the problem is the same, a document you wrote doesn't build anymore spewing many errors. That happened to me with documents written between 1995 and 2000 roughly. Some packages were even related to how to deal with character encodings, which newer versions implemented more naturally but probably caused more difficulties to adapt to. I also remember some of article.sty no longer being compatible with the older one I used. I'm speaking about old memories, as it's been 20 years or so since I progressively stopped using it. It always made me sad because I loved the output quality which was super pleasant to read. Also I remember that newer versions were way simpler to install than the pre-2000 ones where you had to collect styles from everywhere and build your own packages from sources.### To become success storyPosted Sep 17, 2025 18:38 UTC (Wed)
 byballombe(subscriber, #9523)
 [Link] (4 responses)The problem is that some website push you to use the newest gimmick package that will break compatibility in two year instead of the tried and true solution. But how is it different from other software?### To become success storyPosted Sep 17, 2025 20:23 UTC (Wed)
 byNYKevin(subscriber, #129325)
 [Link] (3 responses)If you are publishing something, you don't (usually) have a choice. Your publisher will hand you a LaTeX template, probably with a big stack of arbitrary packages, and tell you to use that. But then what is the benefit of LaTeX being stable, if we're just going to depend on random unstable stuff anyway?### To become success storyPosted Sep 18, 2025 12:35 UTC (Thu)
 byaragilar(subscriber, #122569)
 [Link]My impression (from what packages I was required to use) was the journals didn't pick the unstable (or new or modern or even maintained) packages, but the oldest ones (along with old compilers)? I'm not sure that whatever system is used that the journals will support the latest (or recent) version anyway.### To become success storyPosted Sep 19, 2025 18:05 UTC (Fri)
 byanton(subscriber, #25547)
 [Link] (1 responses)Yes, you get a class file, and a template with \usepackage invocations (or they are in the class file), and if you want to produce the exact same output, then yes, you may need to keep the old packages around. But in that scenario I can just keep the resulting output (e.g., a PDF) around.If I want to revise the paper (e.g., submit a revision of a rejected paper to a different conference), the original appearance is not desired, and usually I need to produce a different format, so it does not matter much if the original class and template no longer works. What matters is that I can easily copy my text to the new template. That is mostly easy, but recently I have had to deal with templates that want all kinds of meta-data, and place standard elements such as \title and \author in a non-standard location, which makes things somewhat time-consuming. But the main part of the paper can be reused and revised, with a formatting pass at the end.Concerning longevity, I have rarely had the need to process a really old work, but just to see how well it works, I have tried a thesis from 1990, and the main text works (graphics are separate, and I would have to invest more time to find out how they were built). I also tried papers from 1992 and 1993, and they compiled fine; the paper from 1992 contains Framemaker graphics, and I no longer have a way to convert that to Postscript, but fortunately I have the Postscript output; for one picture, the placement is slightly wrong, though. The 1993 paper looks fine.Maybe the advantage with these old papers is that there were no style/class files coming from the publication venue, so I just used article (or, for the thesis, report), and not many packages, either.### To become success storyPosted Sep 20, 2025 22:11 UTC (Sat)
 byNYKevin(subscriber, #129325)
 [Link]It sounds to me as if you're arguing that stability is not required in the first place so long as the main text works. Which is fair enough, but it is also exactly the point I was trying to make. If stability does not exist in practice, then obviously it can't be a functional requirement of the software.### To become success storyPosted Sep 19, 2025 0:03 UTC (Fri)
 byjschrod(subscriber, #1646)
 [Link] (4 responses)Well, you mentioning article.sty means you complained about a major LaTeX upgrade that happened in 1994 and your problems, owing to that upgrade, appeared some 6 years later - when many other people report that they had no problems at this time, because backward compatibility was very important to us.But you still bring this up, 31 years after the upgrade - which was 5 years in the making before. From a developer point of view, this is a complaint about a development that happened 35 years ago.Are you aware that this statement is similar to "I will not use Wayland because I had to write XFree86 modline configs back then"? (Because, as you surely remember, this was even before the days of the X.org server with better autoconfiguration that now is considered obsolete.)Disclaimer: I was part of the team that introduced LaTeX 2e back in 1994. I am still connected to that work and to the people working on it, though I'm not an active developer anymore.### To become success storyPosted Sep 19, 2025 5:20 UTC (Fri)
 bywtarreau(subscriber, #51152)
 [Link] (3 responses)I get your point and am not really complaining against LaTeX, which I still love, I'm describing my annoying experience of upgrades. Sure, other programs like gcc break compatibility way more often (every release) and in more subtle ways (silently produce bad code by abusing UB).The thing is that when you don't use LaTeX often enough and each time you do it's difficult, then what remains of the experience is frustration. The frustration of not being able to reproduce a previous report that you spent a lot of time arranging, etc.When I was using it on a daily basis 30 years ago, I *loved* it. Never having to think about what the output would look like and just typing was really awesome and I haven't found anything getting close to that experience. And I'm still pleased to read papers written using it, which are instantly recognizable. I'm also a bit suspicious about tools that try to imitate it, because, as you say, it has accumulated decades of expertise in what it's doing, so users risk losing great stuff.It's very possible that forward compatibility has improved a lot since these experience, but due to these problems I got used to no longer using it. The rare times I need to write something with different fonts and sizes, I just write HTML and let the browser of the moment render it. It's a bit more painful but relies on a standard that's not going to disappear any time soon.### To become success storyPosted Sep 19, 2025 8:34 UTC (Fri)
 byanselm(subscriber, #2796)
 [Link] (2 responses)When I was using it on a daily basis 30 years ago, I *loved* it. Never having to think about what the output would look like and just typing was really awesome and I haven't found anything getting close to that experience. And I'm still pleased to read papers written using it, which are instantly recognizable. I'm also a bit suspicious about tools that try to imitate it, because, as you say, it has accumulated decades of expertise in what it's doing, so users risk losing great stuff.LaTeX is great if you're largely happy with what it does. If you need to bend it to your will to obtain a specific effect, that can easily become an exercise in frustration – fortunately now there are extension packages which will let you, e.g., control how chapter and section headings look like, which was something that in the 1990s required fairly arcane knowledge of the insides of LaTeX to change in even minor ways. Similarly, LaTeX input is reasonably straightforward towriteonce you've got the hang of it, but it is an absolute bear toparseif you want to process it with a tool that isn't LaTeX itself. TeX input, if anything, is worse.The main problem of the TeX and LaTeX ecosystem is that it is, to a large extent, based on ideas which were innovative in the 1980s, but the publishing world has continued turning in the meantime, and TeX's stability guarantee in particular, while commendable in principle, has largely prevented it from evolving along. When TeX was new, PostScript hadn't really been invented yet, PDF wasn't even on the horizon, font technology looked a lot different from what it does today, and Unicode wasn't a thing at all, but now there is no way around these developments. The solutions that Knuth and his colleagues came up with (DVI, Metafont, and so on) didn't catch on outside the TeX community, so TeX has been chasing what the rest of the world was doing in these areas, through non-standard variants such as eTeX, PDFTeX, LuaTeX, etc.It is true that it is perfectly possible, in 2025, to use LaTeX to typeset a PDF document with OpenType fonts based on UTF-8 encoded input, but this means you have to run a version of TeX that has special code extensions not necessarily found in other versions of TeX, using special LaTeX packages which may come bundled in a “batteries included” distribution such as TeXLive but are not actually part of LaTeX itself. This fragmentation tends to make life with (La)TeX more difficult. Also, nowadays people expect to be able to write a document in a single source format and render it, without source changes, in wildly different output formats such as HTML and PDF, in a way that avails itself of the specific advantages of the format in question, and TeX/LaTeX doesn't really have a straightforward and obvious answer to that requirement like Markdown, Pandoc, or Sphinx (to name but a few examples) do.I've been a TeX and LaTeX user for 40 years now but I'm looking at Typst with considerable interest.### To become success storyPosted Sep 19, 2025 12:21 UTC (Fri)
 bydskoll(subscriber, #1630)
 [Link]Also, nowadays people expect to be able to write a document in a single source format and render it, without source changes, in wildly different output formats such as HTML and PDF, in a way that avails itself of the specific advantages of the format in question, and TeX/LaTeX doesn't really have a straightforward and obvious answer to that requirement[...]I solved this problem (with a little bit of pain) for my 600-page set of manuals I mentioned earlier. I wanted PDF output as well as HTML output. There's a pretty nice program calledhtlatexthat does a creditable job of generating HTML, and then I post-processed it to (eg) replace the generated images with the original source images so figures were of higher quality. I also defined a few conditional macros that inserted links to training videos in certain spots... something you can't really do with PDF.Yes, it was a bit annoying to set up, but once I had my Makefile written, it worked beautifully.### Inclusion of PDF files has been implementedPosted Sep 27, 2025 9:26 UTC (Sat)
 byDelio(guest, #179554)
 [Link]The article mentions Typst's inability to include PDF files but this feature has been merged recently:https://github.com/typst/typst/pull/6623### To become success storyPosted Sep 27, 2025 11:59 UTC (Sat)
 bysimlo(guest, #10866)
 [Link]Seems to me, that what you need is a requirements lock file, similar to what you get with pip compile. Unfortunately, a lot of packaging systems doesn't provide that. You can't even build containers with a lock on the dependencies of the packages you install - at least not in a way I have figurer out.### About the compatibility story...Posted Sep 17, 2025 20:51 UTC (Wed)
 bywarrax(subscriber, #103205)
 [Link] (9 responses)Yes, TeX itself has been rock stable, of course, but the idea that you could just rebuild LaTeX documents years after making them hasn't been true for me. I can't remember the exact packages I used which broke, but I'm certain it wasn't anything particularly advanced. Of course it broke with inscrutable error messages, etc.I do think you're correct that backward[1] compatibility *is* important, but the LaTeX ecosystem as a whole isn't necessarily great at that... it very much depends on what packages you use.[1] Future versions being able to process old code/documents is usually referred to as 'backward' compatibility.### About the compatibility story...Posted Sep 17, 2025 21:24 UTC (Wed)
 bydskoll(subscriber, #1630)
 [Link] (4 responses)Hmm... I have three manuals I started writing 20 years ago and continued writing through 2018; they total almost 600 pages and still build perfectly fine on whatever version of LaTeX ships with Debian 13.I don't go crazy with untested or new packages, though... all of the packages I use have been around for a long time and are very stable.### About the compatibility story...Posted Sep 18, 2025 2:18 UTC (Thu)
 byCyberax(✭ supporter ✭, #52523)
 [Link] (3 responses)I have LaTeX files from university days (early 2000-s). I can't render them anymore. Ironically, MS Word documents that I wrote during that time are perfectly readable.### About the compatibility story...Posted Sep 18, 2025 9:38 UTC (Thu)
 bypaulj(subscriber, #341)
 [Link] (1 responses)Whether the MS Word documents render the same as they did before, hell whether they render the same on one PC as another, is another question though. (And the answer is "often not"). So your "perfectly" very likely has a wide margin of error.### About the compatibility story...Posted Sep 18, 2025 13:02 UTC (Thu)
 bypizza(subscriber, #46)
 [Link]> Whether the MS Word documents render the same as they did before, hell whether they render the same on one PC as another, is another question though....Even on the *same* PC, with the *same* version of Word, "rendering the same" was not guaranteed.(Back in the day, I recall that merely changing the printer driver was sufficient to cause the document to paginate differently..)### About the compatibility story...Posted Sep 18, 2025 17:12 UTC (Thu)
 byhholzgra(subscriber, #11737)
 [Link]My early 90s experience was different, I wrote my bachelors thesis with WinWord 2.0a originally, then after switching universities for my masters degree they made it clear that they would expect me to use LaTeX, so as a learning exercise I re-did the complete thesis using LaTeX (somewhere around the switch from 2.09 to 2ε).WinWord could already no longer process it properly when WinWord 6.0; the version right after 2.0a, came out.The LaTeX version worked all the way until late 1999, when due to a series of mishaps the source was lost and I was left with only the PDF result, which I still have. (Generating PDF from Word documents on the other hand was basically unheard of back in the 1990s ...)I also still have a few smaller texts I've written after the 1999 backup disaster, and these I can still process using current LaTeX versions.### About the compatibility story...Posted Sep 17, 2025 21:26 UTC (Wed)
 byiabervon(subscriber, #722)
 [Link] (2 responses)I think there was originally a model of fetching the packages you were using and storing them with the document that used them (and not continuing to update those copies); you had to go and get packages and get them again for them to change. As networking got faster, we switched to effectively having a local mirror of CTAN that you used packages from directly and updated periodically, which means that maintainers who aren't thinking about long-term backwards compatibility break old documents.### About the compatibility story...Posted Sep 18, 2025 20:54 UTC (Thu)
 bySLi(subscriber, #53131)
 [Link]Have you tried modifying those .sty files?If only the underlying language was something modern and somehow modular and encapsulated instead of a weird macro mess with not-really-scopes.Maybe I never got deep enough into it to really appreciate its cleverness (now I do appreciate that it's 50 years old), but in my experience it doesn't exactly take just "not thinking" to not break something by an unrelated change.### About the compatibility story...Posted Sep 18, 2025 20:58 UTC (Thu)
 byejr(subscriber, #51652)
 [Link]This. Unfortunately some functionality relies on external programs (e.g. eps<->X conversions). Those do bitrot.There was ConTeXt as well. I'm not sure of its status. And "worse is better" seems to have been a thing for me this week in many venues.### About the compatibility story...Posted Sep 18, 2025 20:49 UTC (Thu)
 bySLi(subscriber, #53131)
 [Link]I use LaTeX because the other options tend to suck more, but I sure hope something more solid replaces it. As of now, I understand TeX enough to wonder if it really seemed a good idea even when it was invented; but, granted, the TeX part is relatively solid, in the same way perhaps as MS-DOS is relatively solid and it's all the applications causing all the problems.I think one big problem that I've seen in my field of CS is that people have become used to the output of LaTeX to the extent that everything else looks "unprofessional" to them merely by virtue of being different, even if it fixes some real annoyance in LaTeX output.So while I still do my maths and typesetting often in LaTeX, I'm actually happy that the modern practitioners are refusing to take that route, even if it means them using Word. We shouldn't teach people to rely on stuff built on MS-DOS and Cobol either, even if the best typesetting tool remains some obscure DOS executable.### Another project with similar aimsPosted Sep 17, 2025 18:25 UTC (Wed)
 byrogerwhittaker(subscriber, #39354)
 [Link] (6 responses)It would be interesting to see a comparison by someone with knowledge of both Typst and SILE.https://sile-typesetter.org/### Another project with similar aimsPosted Sep 17, 2025 19:35 UTC (Wed)
 byspacefrogg(subscriber, #119608)
 [Link] (5 responses)One of the most obvious differences between TeX (and SILE as far as I can see) and Typst is that the latter has a proper separation between code syntax and typesetting syntax. This, for the uninitiated, is a point of constant frustration in *TeX, with macro definitions producing unwanted output. Code has lexically scoped variables, lambda expressions and much of the 21st century quality-of-life features. It would be interesting to know how SILE does in that regard.Additionally, Typst documents are closer in code style to plain TeX than LaTeX with its verbose Pascal'ish blocks.Anecdote: I had to write a letter, printed, on paper, just the other day. Had a go at using Typst and it was done in 20 minutes incl. downloading the letter package, initialising the document boilerplate and understanding what to change where. It looks like simple tasks are actually simple to do.### Another project with similar aimsPosted Sep 18, 2025 10:10 UTC (Thu)
 byepa(subscriber, #39769)
 [Link] (4 responses)So Typst is still a Turing-complete programming language? It would seem cleaner to have something less powerful, or at least define a subset without fully general macros that's good enough for 80% of documents. I think that gives a better chance of forward compatibility too: some of the unhappy experiences with LaTeX bitrot are because LaTeX packages can do anything at all, so it's hard to guarantee that a new version works the same, or to automatically convert documents from old to new.### Another project with similar aimsPosted Sep 18, 2025 12:41 UTC (Thu)
 bysmoogen(subscriber, #97)
 [Link]The first company I worked at was a browser company who thought that you could meet 80% of all document pages with something simple. What we learned was that what we thought was an 80% solution really only covered 20% of the actual document space. This seems to have been the case with many other attempts I have seen over the years. You can add a couple of items in a highly opionated method of 'this is our one true way' but you quickly find that there are conflicting 'choices' in how people visually perceive layout.. In the end you either accidentally create a turing complete language or put one in on purpose.### Another project with similar aimsPosted Sep 19, 2025 9:19 UTC (Fri)
 bytaladar(subscriber, #68407)
 [Link]I would argue it is the opposite. Every "purely declarative" or "deliberately not Turing-complete" language eventually gets turned into one anyway because otherwise you lack too much expressive power so you either have the choice of doing so deliberately from the start or doing so accidentally with bad ergonomics later.### Another project with similar aimsPosted Sep 26, 2025 19:38 UTC (Fri)
 bybluss(guest, #47454)
 [Link]Typst's embedded language is fully turing complete but that doesn't mean that it can do "anything at all" with the output document. For example something packages do in the latex world is emit raw pdf directives, which no Typst package can do (the API is just not there).### Another project with similar aimsPosted Sep 27, 2025 17:01 UTC (Sat)
 bytjbc(guest, #179557)
 [Link]This comment shows a deep misunderstanding of what Turing complete means. You are confounding that with the macro system that LaTeX provides. Typst deliberately does not and will not support macros.### Very friendly and helpful CommunityPosted Sep 18, 2025 9:21 UTC (Thu)
 byal4711(subscriber, #57932)
 [Link]At my beginning with Typst I had a punch of questions and the Peoples at the community forumhttps://forum.typst.app/was very friendly and helpful which is also a point of view, imho.### LoutPosted Sep 18, 2025 11:36 UTC (Thu)
 byceplm(subscriber, #41334)
 [Link] (2 responses)I was a big fan of Lout (http://jeffreykingston.id.au/lout/), which has very clear (fully functional) language for writing was PostScript oriented from the beginning (yes, that shows the age of the project). Unfortunately, the author was never interested in moving the program to the Unicode world we live now, and especially there were just not enough packages for it to really take off. Pity.### LoutPosted Sep 19, 2025 18:22 UTC (Fri)
 byanton(subscriber, #25547)
 [Link] (1 responses)Yes, when I read the article, I remembered Lout; a collegue advocated that in the 1990s. And already at that time it was obvious that TeX was a good typesetting engine, but a badly designed programming language, and LaTeX inherited this. Nevertheless, LaTeX has a big community behind it, and obviously Lout was unable to overcome the network effects coming from that. Will it be different for Typst or other contenders? Would it help if they built on each other rather than starting from scratch?I looked up when Lout was released, and that was in 1991 (with work starting in 1994). The most recent release is from 2023, but apparently that just made it easier to build, so it's not sure if it is still being maintained. But then, if it works, do you really need any other maintenance?### LoutPosted Sep 19, 2025 20:15 UTC (Fri)
 byceplm(subscriber, #41334)
 [Link]The word “maintained” can cover multitude of sins. Seehttps://git.sr.ht/~mcepl/lout(yes, those commit message with just version numbers is everything we have, there is no better VCS repository anywhere; `whatsnew` is woefully incomplete).### Bad feeling ...Posted Sep 18, 2025 17:02 UTC (Thu)
 byhholzgra(subscriber, #11737)
 [Link] (3 responses)I somehow have a similar bad feeling about this as I had about replacing DocBook based documentation stacks with AsciiDoc, or even worse: MarkDown derived solutions.Lower entry barrier for sure, but always having a taste of"Those who do not understand XXX have to reinvent it ... poorly"(CMake vs. Autotools rings a similar bell, although in a slightly different field)I'm afraid that once again we are forgetting about quite a few things that were already solved in the past by switching to such new solutions carrying less of a history with them ...### Bad feeling ...Posted Sep 20, 2025 3:30 UTC (Sat)
 bymathstuf(subscriber, #69389)
 [Link] (2 responses)> (CMake vs. Autotools rings a similar bell, although in a slightly different field)*sigh* Note that one of the "sparks" for CMake was Windows (as in MSVC, not MinGW-on-Cygwin or MSYS2) support. Something Autotools still does not have today.### Bad feeling ...Posted Sep 20, 2025 10:44 UTC (Sat)
 byhholzgra(subscriber, #11737)
 [Link] (1 responses)Yes, CMake solved the "build on Windows" part, something that autotools with its dependencies on a posix shell, a working m4 preprocessor, and real make (not nmake) could not solve. It also has the capability of generating for other build systems than good old Unix Make / GNU Make.That is not my issue with CMake, it is rather that it "forgot" about things like "make distcheck" and quite a few other things that autotools had solved just fine for ages. So while it supports other build systems besides good old Make, I'd say that at least on the Unixoid side Makefiles are still the predominant backend being used. And the Makefiles it generates are sub par compared to what automake generates.That's my "reinvent it ... badly" pain point with CMake.### Bad feeling ...Posted Sep 20, 2025 23:49 UTC (Sat)
 bymathstuf(subscriber, #69389)
 [Link]> That is not my issue with CMake, it is rather that it "forgot" about things like "make distcheck"I don't think `distcheck` is all that important for CMake because…the source tree *is* the tarball; there's no intermediate step which bundles everything that needs re-verified> I'd say that at least on the Unixoid side Makefiles are still the predominant backend being usedI'd be very surprised if Ninja were not the most popular generator these days. I believe Fedora has switched its default generator at this point at least? I know Visual Studio's integration prefers it.> And the Makefiles it generates are sub par compared to what automake generates.Oh, I don't think anyone is going to argue that CMake's Unix Makefiles generator is anywhere near optimal. There are a number of reasons for it. The most important is that autotools and CMake are different build *systems* even though they do share support for a common build *tool* as an output. Because CMake also supports IDEs with…rather restrictive ideas on what is possible, CMake's model for the build is quite different than autotools'. The build tool is easy to define: it is a build graph executor. Make, ninja, msbuild, just, rake, build2, boost.build, bjam, scons, tup, etc. are all "build tools" that execute a build graph. The build *system* is where things get interesting (for me). Some build tools are also build systems: build2, boost.build, scons, tup. This is the layer which defines things like "what is a target" and "how do targets relate". autotools and CMake both execute at this level and "compile" their input language to something the target build tool understands. This does not mean that build systems expose everything that the build tool supports (e.g., CMake does not allow users to write their own ninja rule statements because…what does that even mean for its other outputs). Of course, some build tool support may have additional features as long as it doesn't conflict with the overall model of the build system itself. For example, CMake's Ninja generator can drop some dependencies other generators need to support the semantics CMake guarantees if it can prove to itself that they're satisfied in other ways.Now, there are ideas to rewrite CMake's Makefiles output to be more like Ninja: one global graph without per-directory entry points and without the per-target subgraph recursive instance. This would allow the Makefiles generator to do the same pruning of unnecessary dependencies that Ninja does. But because it was following the IDE model of "the build graph is a series of targets; each target's subgraph is an independent entity", we have the non-optimal behavior of "if A links to B, B must link before anything in A starts" because that is how CMake guarantees things like generated headers in B are available when A starts compiling[1].So, in short, I think CMake tool a more general approach to build systems and its Makefiles output is suboptimal because of that. But because we now also support the Ninja generator which is, IMO, strictly better (unless one needs a job server for nested builds), restricting the scope to the Makefiles output of each is not a fair comparison.[1] The link dependency can be dropped if A's custom command dependencies are a superset of B's custom command dependencies: any header or whatever B ends up generating is already in A's graph.### Fully Tagged PDF (even for math) is in the works for LaTeXPosted Sep 19, 2025 0:28 UTC (Fri)
 byjschrod(subscriber, #1646)
 [Link] (10 responses)Readers of this article might be interested that work on LaTeX is ongoing. This is not a decades old dying project as some of the comments might make you believe - who report of problems that happened 25 years ago.Just in the last few years, a major undertaking starts to produce tangible results: LaTeX Tagged PDFhttps://latex3.github.io/tagging-project/This is bound to be incorporated into the next TeX-Live release and thus will appear in all major Linux distributions in due course.With it, one can prepare barrier free PDFs with acceptable effort - *even for math*. I don't know if any other system that provides this level of capability. This is the stuff that gets developed in established FOSS ecosystems by people who work on typesetting systems since decades.Disclaimer: I'm personally involved in the LaTeX project, though I'm not a developer any more.### Fully Tagged PDF (even for math) is in the works for LaTeXPosted Sep 19, 2025 2:46 UTC (Fri)
 byintelfx(guest, #130118)
 [Link] (6 responses)> Just in the last few years, a major undertaking starts to produce tangible results: LaTeX Tagged PDFhttps://latex3.github.io/tagging-project> This is bound to be incorporated into the next TeX-Live release and thus will appear in all major Linux distributions in due course.How does this help with UX of *writing* in LaTeX, which seems to be the major issue driving the competing developments (and specifically the subject of the article)?<...>I understand that LaTeX is something you relate to, but your response reads somewhat like this:- Project A sucks at ABC, and I'm badly tired of it, so I don't wish to use project A anymore. I'm looking forward to possible replacements.- But project A is the best at XYZ, so this proves we are better than project B!### Fully Tagged PDF (even for math) is in the works for LaTeXPosted Sep 19, 2025 9:52 UTC (Fri)
 byWol(subscriber, #4433)
 [Link]AOL.This seems to be a major blinker problem in FOSS. My brother's comments about his experience of Emacs at Uni 40 years ago are classic - when he first started he thought it was awful, impossible to use, way too complicated. Then after a year or two, once he'd mastered it, he couldn't imagine using anything else.The reason Word conquered the world (and the reason I hate it) is because it was aimed at people who COULDN'T TYPE - the managerial guys who had professional typists, the couch potatoes who didn't do much, etc etc. WordPerfect - which I took to like a duck to water because it (on the surface) mimicked a typewriter - which failed in large part due to MS's dirty tricks - couldn't compete in the battle for the minds of the people with the purse strings, even though it was a much better professional solution.FLOSS so often is such a super swiss army knife that anybody new approaching it is left thinking "but how does it fix MY problem ???". I use lilypond, and it's incredibly powerful, but the learning curve to access that power is almost impenetrable (it's driven by a variant of Lisp!).Cheers,Wol### Fully Tagged PDF (even for math) is in the works for LaTeXPosted Sep 19, 2025 10:55 UTC (Fri)
 bysmitty_one_each(subscriber, #28989)
 [Link] (4 responses)Your attention is drawn tohttps://www.overleaf.com/### Fully Tagged PDF (even for math) is in the works for LaTeXPosted Sep 19, 2025 11:21 UTC (Fri)
 byleephillips(subscriber, #100450)
 [Link] (3 responses)Any particular reason? Using Overleaf is a distinctly worse experience than using a locally installed LaTeX with your favorite editor, Git, Rsync, etc. Although not as convenient for this as Typst, LaTeX can be set up to provide a live preview (but it will lag behind “live” when your document swells, as LaTeX lacks Typst’s incremental compilation).### Fully Tagged PDF (even for math) is in the works for LaTeXPosted Sep 19, 2025 12:41 UTC (Fri)
 bysmitty_one_each(subscriber, #28989)
 [Link]In response to:> the learning curve to access that power is almost impenetrableOne of my pet cliches is: "Everything is easy, when you know how to do it."Overleaf provides a gentle introduction to LaTeX.### Fully Tagged PDF (even for math) is in the works for LaTeXPosted Sep 19, 2025 13:17 UTC (Fri)
 bypaulj(subscriber, #341)
 [Link]Lyx has very good inline live preview support for Math. It's just 'compiling' the math snippet itself (with whatever environments/packages the doc is using) so it's near instant.I'm a big fan of Lyx as a great accessible and fairly user-friendly UI for writing documents to eventually typeset with LaTeX. I've used it for my own dissertation and it made writing so much easier. It's also customisable. I ended up making a few of my own definitions for things, with their own menu entries - which was just a matter of adding some UI definition files.My father went to uni after retirement and (eventually) got a masters. He used to have endless issues with his masters dissertation in MS Word, with the format going screw and *especially* the required citations being very hard to manage and constantly getting messed up. I was constantly having to go over to him to try help him with his MS Word processing issues. In the end, I switched him over to Lyx. Showed him how to make chapters, sections and sub-sections, and insert citations. Told him just to write, and that the formatting would largely take care of itself. I helped with proofing at the end and help with inserting figures and illustrations, but it saved *both of us* a lot of hair-pulling and time.My dad generally does not get on with computers. He gets very frustrated with complex programmes, with states affecting things he can't see/understand. He became a big of fan Lyx however, for the way it just let him write and generally staying out of the way, while keeping track of all the citations and layout for him, and producing a beautiful doc at the end thanks to LaTeX.Lyx is a _great_ bit of software!### Fully Tagged PDF (even for math) is in the works for LaTeXPosted Sep 27, 2025 19:46 UTC (Sat)
 bycallegar(guest, #16148)
 [Link]Using overleaf has a unique advantage when you have a group of collaborators that use different OSs and have installed LaTeX using different approaches (e.g. one on Windows with MikTeX, another one on Linux with TeXLive, another one on Linux with distribution provided packages). It gives you a platforms that can be used as a reference: if the doc compiles fine there and it does not compile fine for a subset of the collaborators, it is easy to convince them that the issue is on their side.A pain point is that the free tier is insufficient even for the simplest document with the LuaLaTeX engine.### Fully Tagged PDF (even for math) is in the works for LaTeXPosted Sep 19, 2025 19:04 UTC (Fri)
 bynotriddle(subscriber, #130608)
 [Link] (1 responses)If Typst manages to steal mindshare from LaTeX, I doubt it'll have much to do with tagged pdf or other niche features. It'll happen because, if I forget a closing brace, pdflatex does this:This is pdfTeX, Version 3.141592653-2.6-1.40.24 (TeX Live 2022/Debian) (preloaded format=pdflatex)
 restricted \write18 enabled.
entering extended mode
(./t.latex
LaTeX2e <2022-11-01> patch level 1
L3 programming layer <2023-01-16>
(/usr/share/texlive/texmf-dist/tex/latex/base/article.cls
Document Class: article 2022/07/02 v1.4n Standard LaTeX document class
(/usr/share/texlive/texmf-dist/tex/latex/base/size12.clo))
(/usr/share/texlive/texmf-dist/tex/latex/l3backend/l3backend-pdftex.def)
(./t.aux))
Runaway argument?
{ripe and green) \end {enumerate} \end {document} \par
! File ended while scanning use of \emph .
<inserted text>
 \par
<*> t.latex

?And Typst does this:error: unclosed delimiter
 ┌─ t.typst:14:12
 │
14 │ + #underline[Good gin
 | ^In TeX's defense, it's not the worst system I've ever dealt with, and a lot of that spew can be cleaned up by just putting it behind a --verbose flag, but the biggest, hardest-to-fix problem is here:{ripe and green) \end {enumerate} \end {document} \parTypest's equivalent has a line number. It alsoactually matches what was written. Is that fixable without breaking changes to the macro system?### Fully Tagged PDF (even for math) is in the works for LaTeXPosted Sep 22, 2025 18:49 UTC (Mon)
 byjschrod(subscriber, #1646)
 [Link]You chose to use the one example of an error message that comes without a line number.In all other error messages TeX's error messages consist of two lines. The first line has the line number and all characters that are read up to the error, the second line has the characters that are still to be processed.But that is actually a bynote. You wrote> tagged pdf or other niche featuresSince journals (especial scientific journals that Lee wrote about) and other publishers increasingly demand the production of barrier free PDFs for online publication, Tagged PDF is not a niche feature, IMNSHO. Customers of mine currently pour 6-digit numbers of Euro in creation of such files. For private production it doesn't matter -- but for publication, it will soon be a must-have.### Fully Tagged PDF (even for math) is in the works for LaTeXPosted Sep 27, 2025 9:11 UTC (Sat)
 byDelio(guest, #179554)
 [Link]Tagged PDF is the focus of the next Typst release (0.14) which is due very soon.### Meander for parshapePosted Sep 19, 2025 6:06 UTC (Fri)
 byyashi(subscriber, #4289)
 [Link] (2 responses)> Typst provides no analogue to LaTeX's parshape commandMeander seems to do it:https://github.com/typst/packages/pull/3065### Meander for parshapePosted Sep 19, 2025 11:28 UTC (Fri)
 byleephillips(subscriber, #100450)
 [Link] (1 responses)Very nice! It even has real documentation.This was first released while we were still working on the article. In other words, my prediction is coming true: that packages for Typst will emerge rapidly, because it’s easy (easier) to program in.### Meander for parshapePosted Sep 19, 2025 15:27 UTC (Fri)
 byadnl(subscriber, #179418)
 [Link]I came here to suggest this as well! I'm writing a grant with meander and the developer was able to add multi-page support in <24hrs after I mentioned it, wild stuff### Bad comparisonPosted Sep 27, 2025 12:04 UTC (Sat)
 bynorbusan(guest, #10100)
 [Link] (2 responses)Typst should be compared to plain TeX. It provides the basics (and in contrast to Typst, TeX itself is stable). Typst is decades away from being able to produce things likehttps://www.tug.org/texshowcase/- and after those decades have passed, Typst will have its own pain of backward compatibility, quirks, and left-overs.As wtih coreutils, as with several other places, first of all "I'm so shiny" (thanks Moana!), but reality is different.### Bad comparisonPosted Sep 27, 2025 13:26 UTC (Sat)
 byDelio(guest, #179554)
 [Link]Typst can already do most of the things in this showcase. The exceptions I see are the music notation, and the documents that use esoteric PDF features (interactive buttons, embedded 3D object, movies) which might not be far away since the Typst pdf-writer module has recently integrated support for multimedia embeddings, but there seems to be little interest to push this further as these things are poorly supported in most PDF viewers.### Bad comparisonPosted Sep 27, 2025 16:06 UTC (Sat)
 byLonjil(guest, #152573)
 [Link]> Typst is decades away from being able to produce things likehttps://www.tug.org/texshowcase/? Almost everything on that page is basic typesetting, and most of the stuff that isn't is just about levering funny PDF features.Have you actually looked at Typst and its package ecosystem?### Italics correctionPosted Sep 27, 2025 19:59 UTC (Sat)
 bycallegar(guest, #16148)
 [Link]One thing that made me suffer when I tried Typst is the lack of proper italics correction.Images on this issue report show the problem very well:https://github.com/typst/typst/issues/1021#issuecomment-1...May seem a niche case, but it is in fact much easier to encounter it than not. And if you do, you bounce back to LaTeX, even if the problem is not really Typst fault, but the fact that in OpenType there is no provision for treating these situations and Typst bases its rendering on what the fonts provide, without the heuristics that are present in LaTeX from a time when fonts where much more basic things.Incidentally, also modern LaTeX engines have some problems with OpenType, particularly in managing line breaks with hyphenation and ligatures. Using LuaLaTeX with the "harfbuzz" renderer that is a standard in many applications and makes document compilation much faster wrt the specialized renderer that LuaLaTeX uses as a default, leads to loss of many hyphenation points: seehttps://github.com/latex3/luaotfload/wiki/Comparing-the-m...andhttps://github.com/latex3/luaotfload/issues/152#issuecomm...for more details.





Copyright © 2025, Eklektix, Inc.Comments and public postings are copyrighted by their creators.Linux is a registered trademark of Linus Torvalds
