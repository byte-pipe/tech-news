---
title: 'Project Xanadu: Even More Hindsight · Gwern.net'
url: https://gwern.net/xanadu
site_name: hnrss
content_file: hnrss-project-xanadu-even-more-hindsight-gwernnet
fetched_at: '2026-09-04T14:48:05.083675'
original_url: https://gwern.net/xanadu
author: Gwern
date: '2026-09-04'
description: 'Retrospective on Project Xanadu’s success and failure: a lack of design iteration, meaningful use-cases, or practicality stopped a valuable vision from maturing into something useful. (And contrasted with my approach.)'
tags:
- hackernews
- hnrss
---

Skip to main content

Warning:JavaScript Disabled!

For support of keywebsite features(link annotation popups/popovers & transclusions, collapsible sections, backlinks, tablesorting, image zooming,sidenotesetc.), you must enable JavaScript.

JS,design,meta

Retrospective on Project Xanadu’s success and failure: a lack of design iteration, meaningful use-cases, or practicality stopped a valuable vision from maturing into something useful. (And contrasted with my approach.)

2025-05-05

finished

certainty
: 
possible

importance
: 
4

bibliography

 

In December 2024 during a visit to San Francisco, I was lucky enough to be invited at the last minute to a party that could only have happened there: a celebration of the 50thanniversary ofhypermediavisionaryTed Nelson’s197452yamanifesto,Computer Lib/Dream Machines, extolling the vision ofProject Xanaduhypertext. I’ve contributed to English Wikipedia for 20 years now, and I’ve been working on Gwern.net on and off for 15 years now, so I could not possibly miss an entire party of people with strong opinions on hypertext.

Our host, James, had arranged for a surprisingly extensive collection of Nelson memorabilia: not just copies of that book (far larger and more impressive in person than I had realized, similar to a Compact OED in requiring a magnifying glass, also provided), or Nelson’s199729yabookThe Future of Information, but also copies of hisSwarthmore Collegemimeographmagazines, and most impressive of all—several vintage computers running copies of various Xanadu implementations.

Ted Nelson was still alive at age 87, but unfortunately could not attend. Fortunately, one of the attendees was one of the former Xanadu programmers from theAutodeskera (c.1988–5199333ya), and we could listen to some of his stories.

They were a reminder of how, while we romanticize earlier eras of computing, the hardware constraints were really quite severe, and made productive development difficult. I think some disappointments in past software systems become more comprehensible when we remember how much time and ingenuity is spent working around the limitations—eg.McIlroy 1982is justifiably proud of themonthsof clever algorithm design & optimization he did to get a useful spellchecker to fit in RAM in under 1MB that today we would write in a few lines of JavaScript (and done by anLLM).

For example, he described how they prototyped Xanadu inSmalltalk(which made sense, as a highly-productive, pleasant language/OS whose object-oriented model matches hypermedia beautifully), but then had to cross-compile it toC++and compile that… which took about aweekto compile. Not a minute, or an hour, or even a day, but a week. (And I thought that Gwern.net’s multi-hour compile-times were bad for my development speed!) He also had to waste a lot of time dealing with C++ silliness and compile issues.1

Getting this to run at all for the PCs we saw was a challenge, and one reason for the party.

I had, I must admit, sometimes wondered how the Xanadu years at Autodesk could have so little to show for multiple fulltime man-years, when implementing the various client-sidetransclusionor popup features on Gwern.net were typically a few days of work forSaid Achmiz. But hearing some war stories from the horse’s mouth helped put things in proper perspective, and remind me just how incredibly compute-impoverished people were at that time. (Perhaps worse than the CPU was thestorage: I take for granted being able to host any PDF orPostScriptor HTML file I need, but a meaningful fraction of my hosted documents exceed thetotalhard drive space of a mid-range199036yaPC, which might have a 50 MB hard drive. Meanwhile, the Markdown source files of the Gwern.net essays are themselves ~40MB, the annotations twice that, and the final site is 221,438 MB!)

The college magazines were a surprise and entertaining to leaf through: young Ted already liked to write, quite a lot, and dispense his advice. Someone mentioned that Nelson had dreamed of being a Hollywood director and regretted that he went into technology instead; I thought that made sense and explained some things about his auteur approach to software development (like his insistence he is“not a programmer”, 50 years later) or use of film-editing metaphors like“edit decision lists”.

I also had never sat down to readComputer Lib/Dream Machinesproperly, and leafed through a few pages. It was interesting to see such alargebook, in multiple columns to get as much in as possible: Nelson can’t assume the reader knows anything about computers and has to start from scratch to explain the basic concepts like bytes or files. (You really would need the magnifying glass if you were older.)

The later (and much more obscure) bookFuture of Informationwas also interesting for an unusual structure of chapters, where you could read in multiple orders, with a central summary chapter.

Yuxi Liupoints out that Xanadu resembles another famous long-running boil-the-ocean project with close connections to databases & AI with a charismatic leader who never changed his mind, averse to open-source, and which showed similar signs of ‘pathological science’:Douglas Lenat’s Cyc. And thinking about it and re-reading Xanadu materials, I agree.

I briefly poked at the Xanadu PCs, impressed that they were running at all, but I and most of the party-goers bounced off them. The UI was too alien. We really needed to see James demo them, or something like that: hypertext systems do not lend themselves to immediate exploration, especially when they are running in OSes on computers no one there has used in 25 years, if ever.

But I didn’t need to use them much to look at the screen displaying the stereotypical Project Xanadu demo, the opening of theBook of Genesiswith its famous lines zig-zagging off to the right to denote transclusions or commentary on passages, and have a sudden realization:

“Oh my god—It’s completely unreadable.”

The lines were confusing clutter, especially as they crisscrossed (a perennial problem in sidenotes layout, made far worse by the outlines). None of the ‘sidenotes’ were readable because thescreen was so small. Even as you simply scrolled, for many possible positions, due to the lines you were unable to read anything! How could a document UI where often, you could read nothing, have ever seemed like a good idea?2The UI was just terrible—it could never have worked. Even on a large screen like my 4k monitor, I wouldn’t want that.

And then I thought about the choice of text, and I realized that the UI wasn’t the real problem; and the problem, for all these many decades, wasn’t the team either.

The whole concept of side-by-side range transclusions is a solution in search of a problem.

The range-specific transclusion & commentary made sense for the Book of Genesis, where there are detailed commentaries on every line, and much Biblical criticism sorting out how it’s redacted from multiple contradictory texts (like the famously self-contradictingmultiple stories of creation), but as I thought to myself about how “hey, we can dosidenotesand range transcludes/commentaries with bidirectionalbacklinkson Gwern.net too, and wedodo it in my”Suzanne Delage” short story analysis!”3, I suddenly realized: we can, but we mostly don’t, because no one really needs to do that. This is especially true if we look at Ted Nelson’s“Examples of Parallel Documents”: textual criticism again (the Bible,Hamlet,“Rashomon”vs the movieRashomon), the stretched example of theVirginia Declaration of Rightsinfluencing theUnited States Bill of Rights, and then very dubious examples—lists of saints, telephone phone-calls inside an organization, andcomedy TV episodes…?

Hardly any text in the world actuallyneedsto befisked, or have specific lines or paragraphs transcluded; hardly anyone is doingTalmudic commentary, nested layer upon layer. Most real instances of citations are citations to the target as a whole. And even with those, we wouldn’t want to see 99% of them, and we wouldn’t know how to organize the good 1% anyway because they may each have a different purpose. (Just look at online comments sometime: do we sort them by date, by popularity or some sort of karma or‘page rank’, by length, by whether the page author responded directly to them…?)

In retrospect, I think it’s telling that in neitherLib/DreamnorFuturedid I see any instances of ‘transclusion’ on paper. Nelsoncouldhave used any amount of side-by-side layout or range-transclusion in his books, because software is no obstacle: he was laying them out by hand, and could draw or illustrate or copy anything he wanted in any arrangement. But he didn’t, because… it’s just not that useful for books. Not even his. (You don’t need transclusions when you can just cite an earlier passage.)

Note that even in film, where it is trivial to put two sources of footage side by side, and have one ‘comment on’ the other, this is rarely done; instead of relying on horizontal or vertical juxtaposition, film uses the third dimension of time, developing a rich vocabulary ofcuttingand other tricks for doingtransitions, which do the same thing (to an extent we can’t realize until we watch films created before ones likeBattleship Potemkin). Spatial juxtaposition is used in various circumstances, but is nowhere near a default. Only in rare circumstances is it conventional to do anything like apicture-in-picturelayout. A major niche is live broadcasts where it’s infeasible to shoot from multiple angles & edit coherently; in doing a live interview, it is conventional to have two talking heads simultaneous, but then when edited for later, when time permits, it is often turned into a cut-by-cut sequence. Similarly, a streamer, for example, cannot easily ‘cut’ because they are busy doing the actual stream, do not have a large number of film sources to cut between, do not have skilled staff who can be tied up doing, but if they were making a ‘greatest hits’, they might rearrange or zoom in. (I would bet that when Hololive streamers perform at the big annual concert,involving tens of millions of dollars, they do not adopt streaming-like side-by-side formatting, but go for more typical concert cinematography, just like theMiku ExpoVocaloidconcerts.) Notably, where budgets for live broadcasts areveryhigh and quality is a top priority, such asNBA gamesor NFL orMet HD opera broadcasts, and one can have a large number of cameras as well as a ‘director’ and multiple staff, they typically donotsettle for any kind of static picture-in-picture or side-by-side arrangement; instead, they choose to cut a single feed rapidly between different cameras, which lets them ‘follow the action’, order cameramen to move around in advance to make a new angle on the fly, and try to create a meaningful rhythm based on their assessment of the game flow.

And that’s why we didn’t bother adding that specific transclusion capability to Gwern.net until around 2023, motivated by my literary analysis of a short story. I don’t need it,English Wikipediadoesn’t need it,Redditdoesn’t need it, Twitter doesn’t need it, ~100% of personal blogs do not need it… It’s just not that useful—unless you are doing literary criticism or commentary on a text, which describes ~0% of theWorld Wide Web(in 2025or198937ya). All those lines look cool and futuristic, but the moment I think about how I would use them in an actual Gwern.net essay and how it would look to read, I start to get a headache.

The famous Project Xanadu UI/UX is a “science fiction interface”, like the 3D gesture interfaces in theMinority Reportmovieor the virtual reality ofSnow Crash: everyone looks at them and is dazzled and wowed by how cool theylook, except they are a terrible idea which would be a misery touseand give you“gorilla arm”. You try out a prototype or mockup, and almost as soon as you start using them, you realize that no, this isn’t workable and you have to throw it out completely.

This reminded me of the Hollywood director comment: you could say that Project Xanadu is a Hollywood director’s idea of what a World Wide Web should be. You can only believe in it if you never try to actuallyuseit for any real project. If Ted Nelson had been less charismatic, and less compelling a writer, or had less faith in his own vision, this would have been clearer sooner. Since it was not, likeDouglas Engelbart, Nelson enjoys (if that is the word) the honor of being a living embodiment ofCunningham’s Law: becoming one of those historic figures whose importance was that they weresowrong onsuchan important topic they helped popularize that they inspired others to become right.

In fact, that also explains something about Xanadu that had always puzzled me, its emphasis oncopyright. It’s hard to think of any part of the modern world more pernicious and opposed to a useful hypertext system than our current maximalist copyright law, but the Xanadu17 principlesspend more time trying to make the Web safe for copyright holders than they do on such minor things as “transclusion”—it needs to supportmicropaymentsat arbitrary levels of transclusion, needs to have default licenses, eschewNet Neutrality, allow permissionless transclusion of arbitrary resources, etc.:

The 17 Xanadu Principles (Wikipedia version)

1. Every Xanadu server is uniquely and securely identified.
2. Every Xanadu server can be operated independently or in a network.
3. Every user is uniquely and securely identified.
4. Every user can search, retrieve, create, and store documents.
5. Every document can consist of any number of parts each of which may be of any data type.
6. Every document can contain links of any type including virtual copies (“transclusions”) to any other document in the system accessible to its owner.
7. Links are visible and can be followed from all endpoints.
8. Permission to link to a document is explicitly granted by the act of publication.
9. Every document can contain a royalty mechanism at any desired degree of granularity to ensure payment on any portion accessed, including virtual copies (“transclusions”) of all or part of the document.
10. Every document is uniquely and securely identified.
11. Every document can have secure access controls.
12. Every document can be rapidly searched, stored and retrieved without user knowledge of where it is physically stored.
13. Every document is automatically moved to physical storage appropriate to its frequency of access from any given location.
14. Every document is automatically stored redundantly to maintain availability even in case of a disaster.
15. Every Xanadu service provider can charge their users at any rate they choose for the storage, retrieval, and publishing of documents.
16. Every transaction is secure and auditable only by the parties to that transaction.
17. The Xanadu client-server communication protocol is an openly published standard.Third-party software development and integration is encouraged.

I’d always wondered how anyone could believe any of this was either possible or desirable:of coursecopyright holders would refuse to comply with any of this, and would reject any Xanadu with horror and loathing, as it blows up countless business models and IP regimes and deals, and would be bogged down instantly withtragedy of the anticommons, holdouts, prima donnas,controlling copyright owners, etc. But of course, if you saw yourself as really a Hollywood director at heart, you would have strong feelings about the sanctity of copyright, you would be fiercely opposed to following the logic of transclusion to free software/open source(despite the last Xanadu principle, Nelson apparentlyhas never believed in FLOSSand insisted on NDAs), and you would believe in a kind ofsemanticwebwhere you expect… anything to work, really.

As opposed to the reality of what happens when you get 8 billion people online and make much of the world run off the Internet: a nightmarish dark forest where everything that can go wrong will go wrong arbitrarily many times a day;every single invariant you believed inturns out to be broken somewhere in the world4; and every nice feature—liketrackbackbidirectional links—will be ruthlessly abused by spammers, fools & knaves, nation-state actors, emergent bugs or hackers…

Most of those principles make sense only if you don’t ever try it in the real world, where you will discover that many of them are not just of questionable value, or would be fiercely opposed by many entities, but outright illegal. (One of the systems that most embodied the principles of robust decentralized storage of files, which moved them closer to users requesting them for efficiency, was…Freenet, which immediately became notorious for child pornography.)

So, to me, Project Xanadu is a case-study in why designersmustmock-up and prototype their designs before too much is invested in them. Xanadu wasn’t the victim of“Worse is Better”; it was just a solution in search of a problem.5(Something similar seems to be true ofArbital: it had one real user, Eliezer Yudkowsky, who had envisioned it, but struggled to communicate the vision or create a clear prototype and set of use-cases, mocked up as necessary; and like Xanadu, it was a square peg of what ought to have been a long-term non-profit FLOSS effort shoved into the round hole of a software startup company.)

Where were the Xanadu demos and use-cases laid out on paper with some scissors and glue, if need be?6Why are they always just a wildly unrepresentative use-case like “The Book of Genesis”? If you sat down and tried to turn some ordinary technical documentation or the nearest magazine laying near you into a bunch of range-transclusions… how well would it work? How much can, or should be, some text with transclusions spliced in between? (Even in this pageaboutXanadu, there’s thus far only one point where I need to present a large block transcluded from elsewhere, thelist of Xanadu principlescopied from Wikipedia—which is covered by a popup link already, and trivial to inline.)

I think if you did this, the answer rapidly becomes, “yes, I need hyperlinks, those are dead-useful; I need to be able to link arbitrary media types like images, audio, video, or specific pages in a book; I need links which don’t linkrot; Ineed a scripting language(which Xanadu is silent about), but… I don’t really need most of these other things. If I were making some sort of distributed collaborative editor like Google Docs, then Imayneed something likeCRDTsor Xanadu’s similar”enfilades”, but I don’t need that in my published writing!”

And for me, when I started working on Gwern.net, almost every feature was driven by a use-case I had (mostly because I am lazy); even with Said Achmiz, our approach has been to wait for several use-cases, and then implement it while enabling them all. (Invariably, as Gwern.net has become so large and complex, we discover edge-cases and have to revise the design, and for many changes,abandon them.)

For hypertext, I ask myself, “what do I need that a basic blog-like HTML page or an English Wikipedia page does not provide?”, and the answer is: “I don’t need to transclude just a bunch of random paragraphs from a URL.7I don’t need a bunch of tiny atomic 1-sentence long pages nested in a Table of Contents longer than the actual contents, likeGNU Infoencourages you to write. What I need is some sort ofsummary or abstract. I need a reader to be able to browse as fast and friction-free as possible, and quickly skim references or trace interesting citations. I need something like…Lupin’s Wikipedia popups, which allow you to navigate WP with just the most casual mouse navigation, but on steroids.”8

I would say the flaw of Xanadu’s UI was treating transclusion as ‘horizontal’ and side-by-side and assuming that all reading/writing must be done at the lowest raw level of text (motivating the ‘tumblers’ etc.), when it should have been ‘vertical’ with popups, and ‘zooming in’ and ‘zooming out’ at different levels of abstraction (link-icon → title → abstract → section etc.) of the text (which motivates an entirely different set of concerns—being able to specify arbitrary ranges becomes much less important, especially as any key ranges can just be hoisted into a higher level).

Once you have popups offering seamless navigation, you are in effect using transclusion everywhere—just inside the popups. And once you have gone all-in on the idea of offering abstracts for everything, it’s natural to generalize it: if you have two versions of a URL, one ‘small’ (the abstract) and one ‘large’ (the whole URL), why not have a ‘medium’ as well?

There is no natural stopping point here, so you can simply embrace aoutliner-style hierarchical view of“semantic zoom”.9This leads to many elegant Gwern.net UI/UX design patterns, like: the disclosure/collapses to allow in-place zooming of everything from sections to sentences in paragraphs, or thetag-directories(which rely heavily on transcludingabstractsin place of the link as a whole to create ‘annotated bibliographies’), or the backlinks which improve so much over the backlinks of a Xanadu or English Wikipedia by doing a ‘reverse’ transclusion to show the transclude/link context in theotherpages, etc. And thelocal archive systemmeans that not only do links not break, you can ‘preview’ many URLs by popping up & transcluding the cleaned local archive version.

1. I had a little trouble understanding the point of this, but apparently this really is what happened. This was presumably the same C++ codebase that was ultimately released aspseudo-open-source in August 1999.Don Hopkins(who was very intoearly hypertext systems likeNeWSandHyperTIES) says: “They originally wrote Xanadu in Smalltalk, then implemented a Smalltalk to C++ compiler, and finally they released the machine generated output of that compiler, which was unreadable and practically useless. It completely missed the point and purpose of ‘open source software’.”and“Sheez. You don’t actually believe anybody will be able to do anything useful with all that source code, do you? Take a look at the code. It’s mostly uncommented glue gluing glue to glue. Nothing reusable there.”↩︎
2. Contrast this to the Gwern.net UI: pretty much no matter where you are or what you have done, you can still see a lot of useful text with a good “data-ink ratio”. You can even successfully browse the site on anApple Watch!↩︎
3. Since we can transclude or pop up any anchor, any range can be transcluded simply by defining a<span>/</div>wrapper. So for “Suzanne Delage”, I simply wrap each story passage in a named span-wrapper and link to that. (And these backlinks are displayed inside the story section too, so one can see what parts of the story are referenced in the rest of the analysis.) I do not need to specify anexactbyte-range in the original Markdown source… which is good because those ranges kept changing as I added to or edited the passages.This illustrates that a problem with Nelson’s insistence on byte-ranges—perhaps stemming fromhis old metaphorof splicing together specified frames from reels of film—is that it ignores semantics.I do not want to ‘transclude bytes 123–456’ of a HTML file; I want to transclude a specific, meaningful element XYZ, which mayhappento be stored at bytes 123–456 right now but will change length, be moved around within or across pages, be rewritten arbitrarily, have markup inserted or removed… While frames of film may have been effectively ‘semantically immutable’ when Nelson was learning about film editing back in the 1960s (because once the film is shot on analogue film, it is effectively fixed), text isnot; regardless of whether you track the full edit history, soon there may simply not be any ‘range’ which corresponds to a range previously specified by an author. (Even thetext fragmentstakes what you might call a‘content-addressable’perspective: trying to store a few phrases or keywords to locate the nearest part of a web page which is hopefully the intended content.)So you have to rely on having access to the entire edit-history of everything so you can transclude from the old versions, which is the camel’s nose; and if you want to do that, you can just host your own copy!↩︎
4. Even something as simple as “how do you handle different text encodings, since not everything will beUTF-8?” apparentlydoesn’t have a straightforward answerin Project Xanadu.↩︎
5. In worse-is-better, the ‘worse’ systems ultimately do wind up solving thesameproblems as the original better design did, just in a worse way (requiring far more R&D, to result in solutions with more arbitrary limitations, papercuts, needless complexity etc.).↩︎
6. Or as Hopkins charged in199927ya: “Has Xanadu been used to document its own source code? How does it compare to, say, the browsable cross-referenced Mozilla source code? Or Knuth’s classicLiterate Programmingwork withTeX?”↩︎
7. Even when I need to quote some specific parts, I tend to need to quote a few different parts, and ideally they would be modified, like adding missing hyperlinks or commentary, which would require building my own version to transclude, so why bother with the original?↩︎
8. While Lupin’s Tool dates to ~2005, as far as I can tell, Gwern.net’s popups and transclusions were more or less possible almost from the beginning of JavaScript-poweredDHTML~1997.You would perhaps not have been able to do fully-recursive popups, depending on how restricted things like<script>were in terms of loading new JS-encoded data—at least not without gross hacks like never closing the HTTP connection so the client can fake requests for arbitrary data, or usingiframesinstead, or perhaps,Java appletsas a crutch—but you would definitely have been able to straightforwardly implement thefirst few generations of our popups.(David Carter-Todin199927yastates that“This[‘transpublishing’]can be done with cleverly simple use of JavaScript and is much less intrusive, eg. The JavaScript just writes HTML. It’s invisible to the end user. I know I’ve said this before, but the first time I did this with theExciteaffiliate program, I was astounded by how easy it was.”) A JS-free version was proposedin 1996.↩︎
9. I think one of the reasons outliner approaches have not caught on for hypertext in general is that while useful, they wind upfoisting too much work on the author. I am willing to do this work in part to explore website design, but the idea that many websites should be like English Wikipedia or Gwern.net is crazy. However, LLMs open up many new design opportunities forautomatically summarizing/expandingto build a full hierarchy while the human author writes just what is necessary, which I think can resurrect many old ‘tools for thought’ ideas and finally make them usable.↩︎

Error:JavaScript disabled.

Backlinks, similar links, and the bibliography require JS enabled to load.

# Bibliography

 

[Bibliography of links/references used in page]

 

[ Send Anonymous Feedback ]

[Quote Of The Day]

[Site Of The Day]

[Annotation Of The Day]

 

​