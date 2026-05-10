---
title: Replacing a 3 GB SQLite database with a 10 MB FST (finite state transducer) binaryAndrew Quinn's TILs
url: https://til.andrew-quinn.me/posts/replacing-a-3-gb-sqlite-database-with-a-7-mb-fst-finite-state-trandsucer-binary/
site_name: hackernews_api
content_file: hackernews_api-replacing-a-3-gb-sqlite-database-with-a-10-mb-fst
fetched_at: '2026-05-11T06:03:41.418950'
original_url: https://til.andrew-quinn.me/posts/replacing-a-3-gb-sqlite-database-with-a-7-mb-fst-finite-state-trandsucer-binary/
date: '2026-05-10'
published_date: '2026-05-10T00:00:00+00:00'
description: 'Note for numberphiles: all numbers have been rounded to their first significant digit, because I’m a fan of Rob Eastaway’s “zequals” method of getting to the point when it comes to estimation. It’s much more valuable to walk away with the heuristic “some dude got a 300x memory reduction by swapping out a database he hacked together for a tiny, static, specialized data structure that does exactly what he needs it to and no more.”'
tags:
- hackernews
- trending
---

Add me on X / Twitter
!
You can cite this post as a reason if you're shy.

Note fornumberphiles:
all numbers have been rounded to their first significant
digit, because I’m a fan of Rob Eastaway’s“zequals” methodof getting to the point when it comes to estimation. It’s much
more valuable to walk away with the heuristic “some dude got
a 300x memory reduction by swapping out a database he hacked
together for a tiny, static, specialized data structure that
does exactly what he needs it to and no more.”

I found myself with an increasingly rare opportunity to work
this weekend onTaskusanakirja,
also often calledtsk,
a Finnish-English dictionary with incremental search-as-you-type.1Fundamentally this problem reduces down toprefix search,
and the canonical solution for prefix search with autocomplete
is to implementa trie.

And this worked wonderfully for the first implementation
oftsk, which was in Go (and which I have written aboutelsewhereandelsewhereandelsewhere).
With a few basic optimizations.
To prevent matching on some single-digit percentage of the
mid-six-figures number of words we were baking into the
binary (it’s been a design goal from the start to ship the
entire program asone.exe,one.app, oronestatically linked binary), we set some limit of e.g. only the
first 50 or 100 matches or so and then just memoized all
of the 1-, 2-, and 3-character combinations, after which
I’ve never noticed a perceptible delay in the
program again after a year of heavy personal use. We could
just about squeeze a trie with some basic optimizations
like that into ~60 MB of space.

But Finnish is a heavilyagglutinativelanguage. It’s not
impossible for a single base word in the language to have
over one hundred possible endings, when all combinations
are considered. And the combinations are not regular!2The
extremely regularized orthography of the Finnish languagealsomeans no fibbing when it comes to what speakersactuallysay on the page, and that means that base words
stretch and shift and transmute in acoustically-pleasing
ways as you layer on endings, which makes perfect senseafteryou’ve spent a couple years already immersed in
the language. When you’re a beginner, and you see a
sentence like e.g. “Opiskelijassammekin on leijonan sydän”,
there is one word you are disproportionately likely to
get stuck on. Part of what this tool attempts to do is
help the student figure out how tocleavethe word at
the right edges by embedding all that information as well.

The trie fell down at that point. I could keep ~400,000
items in the trie sipping ~50 MB of RAM.
The same trick does not scale to 40-60 million. Not if you want
it all to run on the old laptop of a college kid from Jakarta.
Frustrated and running out of time, I threw up my hands and
said “We’ll ship the inflections in a separate
SQLite database with FTS (Full Text Search) and
let them search on that if they’re so desperate,” whichworked— still without perceptible delay — but it required
a one time 3 gigabyte download. Not ideal!

That was where the story stopped about 9 months ago. This
weekend, with 9 more months of intense full time software
engineering under my belt, I boldly asked:Had I considered rewriting it in Rust?3

It turns out there is avery, verysmart guy namedBurntSushi aka Andrew Gallant,
infamous forripgrep, a really really fast grep—
a tool so ubiquitously usefulI put it years ago in my “Holy Trinity” of modern shell commands—
whoalsofaced a similar problem
at some point in the past, and wrote a post calledIndex 1,600,000,000 Keys with Automata and Rust.
(Warning: long, extremely interesting.)
The opening spoils it:

It turns out that finite state machines are useful for things other than expressing computation. Finite state machines can also be used to compactly represent ordered sets or maps of strings that can be [prefix, fuzzy, suffix] searched very quickly.

Well, I thought, this seems promising. Let’s write
a minimal Rust program to strip the data out of that
3 GB database and compact it down into one of these
FST thingies.4I mean, it was always obvious that was
a hack, but it was the best hack I could manage with
the time and energy at the time. How small could we
get it?

Ten _mega_bytes.A 300x reduction in space.
Even in the world offstcrateusers,
this particular application — mapping conjugations
and declensions of a highly agglutinative language
back to their source definitions — was extremely
well suited to the domain. Unlike tries, FSTs compressbothprefixesandsuffixes, and in a language like
Finnish, there are a very small handful of popular
suffixes which get repeated extremely often in
the dictionary corpus. The data load is static
at runtime, which gets aroundfst’s greatest
weakness.

I do wish to point out, of course, that the whole
reason it was possible to experiment cheaply and come
across this serendipity was because 9 months ago,
faced with the choice to either do the bad easy thing
or the good nothing, I chose to do the bad easy thing.5The SQLite database worked! Iunderstoodhow it worked, behind the scenes with its B-trees and itsFull Text Search extension. I think I even used that same
FTS extension to power certain lesser used features that
arenotin the alphas oftsk v2.0.0at the time being
and are likely to be dropped entirely if it means compromising
this now salivatory memory footprint.

Because the Pro version ofv2is shaping up to be about 20 megabytes, all batteries
included, which is 3 times less than the free version ofv1ever was. We’ll see what makes it past the cutting room in
time.

1. tskstarted life as a TUI Go program — and in fact evolved out of an earlierfzfprototype calledfinstem, seethe highest-ROI program I’ve written so far. The “pocket dictionary” framing (taskusanakirjaliterally means “pocket dictionary” in Finnish) was always load-bearing: if it doesn’t fit on the kind of dusty laptop someone might inherit from an uncle, it isn’t apocketdictionary, it’s an old Oxford that happens to compile.↩︎
2. Linguists call the deformations triggered by suffixesconsonant gradationandvowel harmony, and Finnish wields both at once. Takekatu(“street”), whose genitive is notkatunbutkadun— thetsoftens todbecause the syllable closed. Multiply that across 15 cases, then 2 plurals, then 6 possessive suffixes, then some indetermintate amount of possible clitics, and you can see why a naïve trie capitulates. It simply has no way to share the cost of thethousandsof words that all end in-ssa-mme-kin(“in- our [X]-, as well”).↩︎
3. “Rewrite It In Rust” is enough of a meme that there is an entire genre of blog posts pushing back on it. One honest version of the meme is something like: If your problem is in the intersection of “needs to be fast”, “needs to be portable”, and “the existing tooling has gnarly memory ergonomics”, Rust might put you in clover.↩︎
4. The trick that makes FSTs so much more compact than tries on natural-language data issuffix sharing: a trie shares prefixes (sokadunandkaduilleshare their first three nodes) but stores every distinct suffix path independently, while aminimal acyclic deterministic finite-state automatonmerges any two subtrees that are structurally identical. For a corpus where 100,000 words all end in the same dozen inflectional patterns, this is a license to print memory.↩︎
5. This is a recurring shape to my notes here that I keep bumping into qua“it’s okay to solve a problem twice”. One could say in the first quarter-century of my life, that while I was always fascinated by programming, I could never overcome the guilt of not really knowing whether the tool I am building right now isn’t already superceded by some much better implementation someone else has already written 30 or 40 years ago; I could write a TSV-aware search and replace, or I could find out aboutawkand solve that entire class of problems in one fell swoop, for example. My central conceit is thatthis is a trap. Youneedto reinvent a couple of wheels to get to the edge of what we know about wheel-making, not a thousand wheels, and not zero; probably four or five is sufficient in most domains, maybe closer to twenty or thirty in the most epistemically rigorous and developed fields like mathematics or computer science. Each wheel you reinvent, and every driected question you ask along the way, will propel you faster to the true frontier than that same amount of time spend in idle study, or even five times that amount. This is at heart aCaplanian view: “If schools teach few job skills, transfer of learning is mostly wishful thinking, and the effect of education on intelligence is largely hollow, how on earth do human beings get good at their jobs? The same way you get to Carnegie Hall:practice.” Or if you prefer exhortations,Do Ten Times as Muchis my favorite unpleasant advice that works.↩︎