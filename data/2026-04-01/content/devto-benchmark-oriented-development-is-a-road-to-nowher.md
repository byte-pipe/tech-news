---
title: Benchmark oriented development is a road to nowhere - DEV Community
url: https://dev.to/dmtrkovalenko/benchmark-oriented-development-is-a-road-to-nowhere-1518
site_name: devto
content_file: devto-benchmark-oriented-development-is-a-road-to-nowher
fetched_at: '2026-04-01T19:28:07.533329'
original_url: https://dev.to/dmtrkovalenko/benchmark-oriented-development-is-a-road-to-nowhere-1518
author: Dmitriy Kovalenko
date: '2026-03-25'
description: Cursor just released this article and a ton of people started worshiping Cursor like they just made a... Tagged with cursor, ai, programming.
tags: '#cursor, #ai, #programming'
---

Cursor just released thisarticleand a ton of people started worshiping Cursor like they just made a revolution in file search. They showed a beautiful graph saying that they are 1,300x faster than ripgrep, showing one specific query on the chromium codebase. You know, I happen to work a lot lately on the file search project of minehttps://github.com/dmtrKovalenko/fff.nvimand I have a feeling that this is all one large manipulation a lot of people blindly believed.

We cannot say for sure because as always they do not open source the code and do not let you repeat the experiment, which makes this whole discussion absolutely useless, but I'll try to be constructive.

Here are my claims

## 1. The data is closed

I like to say myself that ripgrep is not the fastest code search especially on macos, but I specifically asked my colleague to give me his M2 macbook air and I spent quite some time experimenting but I never got the ripgrep on the same repo with the same query longer executing longer than 9 seconds, while usuallyit takes around 6 seconds when the cache is warmed up.

The main problem of all of those closed benchmarks and weird marketing articles that you can not verify anything yourself. You have neither the data nor the instrument to reproduce the success. You know, there is a reason why every research paper has to describe the experiment - so other people can reproduce it.

But let's try to figure out what they did

## 2. Indexing the code locally

As they mentioned in their blog, indexing is a very old technique and trigram search was first mentioned 80 years ago. So how did Cursor come up with such a beautiful solution only in 2026? Is everyone around dumb and never did anything like this before? No, actually all the theory in the blog post they made (only the one that makes sense) comes from this paperhttps://swtch.com/~rsc/regexp/regexp4.htmlthat was behind the Google Code Search project.

So why didn't any of the editors before come up with the solution of using indexes? This is my main question to the Cursor team. Why didn't you mention that indexing the same repo on the same machine takes >3 minutes.

And it takes 1GB of space which tbh is not that much for 487,592 searchable non-binary files. Your implementation very likely takes MORE TIME but is likely more space efficient (maybe 2-4 times? we never know cause this is all just words)

So dear Cursor marketers, why didn't you consider this chart to be added to your blog post? Yes I'm using the infinite super power of marketing bar charts against you:

You know the biggest problem is not indexing the file, the biggest issue is maintaining the index, and this is the primary reason why every editor like VSCode is not using something like this. Inverted trigram indexes are actually a complicated thing. And you made it even more complicated. If we take ONLY the ASCII typeable characters subset you will have about 700k unique trigrams listed in the chromium codebase

### A bit about the n-gram indexing

Tri-gram or bi-gram is just a unique pairs or trios of bytes within a string. Either the document or the query.

The trigram index is going to look like this in memory, there is a bunch of ways you can optimize it like using bitfields instead of arrays to reduce the space but the amount of data is massive.

(the amount of rows would be equal to every unique 3 characters in your codebase)

┌─────────┬───────────┐
│ trigram │ file_idx │
├─────────┼───────────┤
│ " M" │ [1, 2, 3] │
│ " MA" │ [1, 2] │
│ "MAX" │ [1, 2] │
│ "AX_" │ [1, 2] │
│ "X_F" │ [1] │
│ "_FI" │ [1, 3] │
│ "FIL" │ [1, 3] │
│ "ILE" │ [1, 3] │
│ "LE_" │ [1, 3] │
│ "E_S" │ [1, 3] │
│ "_SI" │ [1, 3] │
│ "SIZ" │ [1, 3] │
│ "IZE" │ [1, 3] │
│ "ZE " │ [1, 3] │
└─────────┴───────────┘

Enter fullscreen mode

Exit fullscreen mode

The problem is that to keep it fast it absolutely has to use a flat allocated array of all the files somewhere to keep the lookup table fast. This brings 2 problems

a) you have to know and store the list of all the files in the file systemb) you have to update both file list and index every time something has changed

The blog post mentions that they use "layers" to keep the sync up-to-date. It is a smart move but the blog post never mentions ANYTHING about the way they do the layering. And this is actually the most important part because if they were able to figure out how to quickly and efficiently handle the "file deleted at index N" problem without hitting conflicts or growing another 1GB file next to the original index, this is actually something worth discussing. And they simply omitting it?!

Where do they do the updates? Do they use a persistent file watcher? Where index is stored, how much time do they spend on traversing the tree? What is going to happen when a user wants to search innode_modules? We don't know because they specifically omit this part entirely.

we control the state of the index by basing it off a commit in the underlying Git repository. User and agent changes are stored as a layer on top of it.

So you are saying that every single commit a user makes, you will spend 3 minutes indexing? Great job, but in fact they just do the indexing in the background, effectively falling back to regex search in the meantime. Because reindexing is a non-atomic operation that requires a lock.

This is the essential problem of indexing that IS NOT solved. You do the marketing like you solved this problem or it is not imporant while in fact this is exactly what is important.

My project uses in-memory indexing that looks pretty similar to what they describe and I'll tell you later how we bypass this exact limitation in fff.

## 3. n-gram indexing and its cost

So I actually read the blog post a few times because I am genuinely interested in how they do this and this is the only paragraph that actually describes something. Everything else is pure water. But the funniest part of this paragraph is that to me it looks like a complete LLM hallucination. In short: they are building an inverted index of the trigrams but adding a bloom filter to the next byte.

The way n-gram inverted index works is very simple

Here is the first suspicious part making me think they didn't really understand the point of trigrams

By having a mask that contains the characters following each trigram, our inverted index can be constructed using trigram keys, but we can query it using quadgrams! This already scopes down the potential documents much more than a simple trigram index could.

So I actually ran the n-gram indexing for the chromium project. And here is what I found for the exact "MAX_FILE_SIZE" query over the same indexed code using trigram and bi-gram search.

┌─────────────────┬───────────────────┬────────────────────┬───────┬───────┐
│ Query │ Bigram candidates │ Trigram candidates │ Bi % │ Tri % │
├─────────────────┼───────────────────┼────────────────────┼───────┼───────┤
│ MAX_FILE_SIZE │ 13,241 │ 727 │ 3.0% │ 0.2% │
├─────────────────┼───────────────────┼────────────────────┼───────┼───────┤
│ mutex_lock │ 13,934 │ 279 │ 3.2% │ 0.1% │
├─────────────────┼───────────────────┼────────────────────┼───────┼───────┤
│ return │ 179,617 │ 140,367 │ 40.8% │ 31.9% │
├─────────────────┼───────────────────┼────────────────────┼───────┼───────┤
│ #include │ 127,705 │ 125,227 │ 29.0% │ 28.5% │
├─────────────────┼───────────────────┼────────────────────┼───────┼───────┤
│ TODO │ 191,186 │ 32,865 │ 43.4% │ 7.5% │
├─────────────────┼───────────────────┼────────────────────┼───────┼───────┤
│ struct file │ 92,419 │ 22,337 │ 21.0% │ 5.1% │
├─────────────────┼───────────────────┼────────────────────┼───────┼───────┤
│ phylink_ethtool │ 3,069 │ 2 │ 0.7% │ 0.0% │
└─────────────────┴───────────────────┴────────────────────┴───────┴───────┘

Enter fullscreen mode

Exit fullscreen mode

There is absolutely no reason to read the article further because for the exact query they showed, the trigram index actually returns <1k candidates, and there is absolutely no reason to optimize it even further. Unless of course you run your LLM in a loop asking to come up with a better approach (LLMs love to put bloom filters everywhere, just saying)

For any normal sized repository (e.g. 20k lines) quadgram indexing would essentially be equal to the exact search (every query will result in 1-2 candidates). This is simply an overkill even for a chromium 500k files repo.

But on top of adding an additional bloom filter imitating quadgrams, they decided to prefilter by frequency and hash every single trigram (there are 779,889 distinct trigrams in chromium), effectively making indexing way slower simply to reduce 727 candidates to 300. There are a ton of questions about how this works that we will never get answers to because this is a private proprietary thing. I have no idea why we are even discussing this.

In addition to that, with their idea of dynamic n-grams + a bloom filter, they now have the problem of storing the data because there is no primitive that can fit those as a key in the address space (and no, this is not because they support full Unicode indexing), so they have to hash every single key to simply store the index on the file system.

## 4. Ultimate performance problem

I once said that FFF is the fastest file search on the planet. While it was true, I never thought that this was the killer feature. Once in a while I get tweets like "fff feels slow in the 200GB Android root repo". I usually ignore those because I actually work with a former Android core dev now and I asked them how they do Android development and they told me that NO ONE EVER opens the Android root. The same thing happens with chromium, it literally mixes Android, iOS, web, V8, and other subprojects.

The indexing itself is a complicated operation which doesn't actually give any performance benefit onrealrepositories but anyway takes time to build and store. Without index fff is able to search the Linux kernel for a very rare string in under 6ms (the average repo you're gonna work with is way less than 100k files) which is absolutely fine, and under 1ms with the very simple index we have:

### Index optimized for the actual users

for large repositories FFF is actually doing a very similar approach to what is described, and I originally thought they just stole my code (seems like not really 😭). We use the inverted bigram index approach but only over the most useful and rare ones. There is absolutely 0 reason to even index bigrams like "th" because the word "the" will exist in the absolute majority of files.

This is not what I even call a feature, but an optimization because n-gram indexing never works on the real Unicode files (because once you have many languages you will need to pick up the actual trigrams that exist in the words rather than all the combinations, and this simply doesn't work with source code files).

Here is how fff in-memory bi-gram prefiltering works:

If we take the 95 printable ASCII characters and lowercase them we get 69 distinct values (a-z, 0-9, punctuation, space). 69² = 4,761 possible unique bigram pairs - that's it. No banning, no frequency cutoffs. We index ALL of them because the key space is naturally bounded and tiny compared to trigrams (69³ = 328,509 keys). During the indexing phase we do the same reading of all the files to:

a) populate the virtual memory mapped cacheb) read the file content and extract bigrams for the inverted index

Because bigram extraction is just splitting bytes by 2 and lowercasing, modern CPUs chew through it because it is easy SIMD problem. Indexing the whole chromium repository takes around 2 seconds to list files and 7 seconds for the bigram index which runs completely asynchronously:

2026-03-24T19:43:11.331524Z INFO fff_search::file_picker: crates/fff-core/src/file_picker.rs:1115 Bigram index built in 7.59s - 4761 columns (3481 sparse, 1280 dense) for 487592 files

This is faster than gathering git status for those files using libgit2! The prefilter index is stored as a compressed immutable inverted index with a hybrid column storage - each bigram gets either a dense bitset or a sparse posting list, whichever is smaller.

Here's the full layout:

LOOKUP TABLE (178 KB fixed)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Maps every possible bigram key (u16) to its column index.
44,587 entries × 4 bytes. Most map to NO_COLUMN (bigram never seen).

┌──────────┬──────────┬──────────┬──────────┬───┬──────────┐
│ key 0 │ key 1 │ key 2 │ key 3 │...│ key 65535│
│ col: ── │ col: ── │ col: 0 │ col: ── │ │ col: ── │
└──────────┴──────────┴────┬─────┴──────────┴───┴──────────┘
 │
 ▼
COLUMNS (4,761 for chromium — one per unique lowercased ASCII bigram)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Each column stores "which files contain this bigram" in one of two formats:

BITSET (1,280 columns — common bigrams like "ma", "in", "re")
┌──────────────────────────────────────────────────────────────────────┐
│ One bit per file. For 487k files → 7,610 u64 words → ~60 KB/col │
│ │
│ Column for bigram "fi": │
│ ┌──────────────────┬──────────────────┬──────────────────┬─────┐ │
│ │ word 0 │ word 1 │ word 2 │ ... │ │
│ │ files 0–63 │ files 64–127 │ files 128–191 │ │ │
│ │ 0b..00101001 │ 0b..10000100 │ 0b..00000011 │ │ │
│ │ ↑ ↑ ↑ │ ↑ ↑ │ ↑ ↑ │ │ │
│ │ 0 3 5 │ 66 71 │128 129 │ │ │
│ └──────────────────┴──────────────────┴──────────────────┴─────┘ │
│ Query: result &= column (word-by-word AND, SIMD-friendly) │
└──────────────────────────────────────────────────────────────────────┘

Enter fullscreen mode

Exit fullscreen mode

And this is how the filtering process looks like. I do not have time and resources to build and interactive visualization but I think this is actually more clear:

QUERY: grep "MAX_FILE_SIZE"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Extract bigrams: "ma","ax","x_","_f","fi","il","le","e_","_s","si","iz","ze"
2. Look up each in the table → get column indices
3. AND all columns together:

 result = 1111...1111 (start: all files are candidates)
 result &= col["ma"] → ████░░░░████░░██░░░░... (files with "ma")
 result &= col["ax"] → ██░░░░░░░██░░░██░░░░... (intersect with "ax")
 result &= col["x_"] → █░░░░░░░░░█░░░█░░░░░... (getting smaller)
 ... ↓ after all 12 bigrams:
 result = 13,241 bits set out of 487,592 → 97% of files eliminated

OVERLAY (live updates without reindexing)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
The base index is immutable. File changes go to a delta layer:

Enter fullscreen mode

Exit fullscreen mode

The crossover point between sparse and dense is elegant: whenpopcount × 4 bytes ≥ ⌈file_count/64⌉ × 8 bytes, the column switches from a posting list to a bitset. This happens at ~3.1% file occupancy. For chromium that means a bigram appearing in 15,000+ files gets a dense bitset, while rarer bigrams use compact posting lists. We store all 4,761 distinct case-insensitive ASCII bigrams - not losing anything on the prefiltering step.

Because fff is originally built with a background fs watcher in mind and an immutable file tree index, this is extremely easy for us to update the index every time a file is updated or deleted, though it might take ~10 seconds if the whole scan is invalidated. Here are real measurements on actual codebases (Apple M4 Max, all times measured from scan complete to index ready):

┌─────────────────┬─────────┬────────────┬──────────────────────┬──────────┬──────────┐
│ Repository │ Files │ Indexing │ Cols (sparse/dense) │ Memory │ B/file │
├─────────────────┼─────────┼────────────┼──────────────────────┼──────────┼──────────┤
│ whisper.cpp │ 1,150 │ 0.10s │ 4,320 (2,534/1,786) │ 747 KB │ 665 │
│ ffmpeg │ 9,834 │ 0.31s │ 4,672 (3,078/1,594) │ 2.9 MB │ 309 │
│ rust-skia │ 12,502 │ 0.41s │ 4,542 (3,081/1,461) │ 3.5 MB │ 294 │
│ <Your B2B SAAS> │ 21,462 │ 0.52s │ 4,314 (2,823/1,491) │ 3.7 MB │ 269 │
│ linux kernel │ 98,462 │ 1.94s │ 4,489 (3,202/1,287) │ 23.7 MB │ 287 │
│ chromium │ 487,592 │ 7.87s │ 4,761 (3,481/1,280) │ 113.1 MB │ 243 │
└─────────────────┴─────────┴────────────┴──────────────────────┴──────────┴──────────┘

Enter fullscreen mode

Exit fullscreen mode

Okay and here is the real comparison, where you can literally see that the value coming from persistent indexing is visible only on the VERY LARGE repositories.

┌───────────────────────┬──────────────────┬──────────────────────┬──────────────────────┬──────────────────────┐
│ Repository │ Tool │ Time to Index │ Index Size │ Time to Query │
├───────────────────────┼──────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│ whisper.cpp (1,150) │ Cursor* │ ~14 s* │ ~2 MB* │ ? │
│ │ zoekt │ 10s │ 4MB │ ~3 ms │
│ │ fff │ 0.10 s (async) │ 747 KB │ ~1 ms │
│ │ ripgrep │ - (no index) │ - (no index) │ ~15 ms │
├───────────────────────┼──────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│ ffmpeg (9,834) │ Cursor* │ ~45 s* │ ~20 MB* │ ? │
│ │ zoekt │ 28s │ 43MB │ ~1 ms │
│ │ fff │ 0.31 s (async) │ 2.9 MB │ ~1 ms │
│ │ ripgrep │ - (no index) │ - (no index) │ ~120 ms │
├───────────────────────┼──────────────────┼──────────────────────┼──────────────────────┼──────────────────────┤
│ chromium (487,592) │ Cursor* │ ~4 min* │ ~1 GB* │ ? │
│ │ zoekt │ 2 min │ 1.4GB │ ~3 ms │
│ │ fff │ 7.87 s (async) │ 113.1 MB │ 118 ms │
│ │ ripgrep │ - (no index) │ - (no index) │ ~6 s │
└───────────────────────┴──────────────────┴──────────────────────┴──────────────────────┴──────────────────────┘
* Cursor values are estimates - code is not open source, measurements cannot be reproduced

Enter fullscreen mode

Exit fullscreen mode

The question is: do you want to wait 3 minutes and burn 1GB of disk for a 35x improvement on the one repo nobody opens as a whole? Or do you want instant results on every real repository you actually work on?

Yes fff is 10 times slower than the "ephemeral code they showed" while effectively having no persistent index stored, and is still 34x faster than ripgrep (because ripgrep didn't take 16 seconds to find the files, it takes 6, let's be honest) but on the real repositories every query runs in sub-ms

and here is why even this doesn't really matter

## 5. I heard you are an AI agentic company, right?

All I want to say is that the main problem of file search is not the speed, it's accuracy.

It's like typing speed, I can type 200 words per minute with a 99% typo rate.

The main problem of file search that I am trying to solve is the way we suggest files for the user / AI agent. Yes I recently released fff-mcp that is replacing built-in file commands and actually delivers +10% of speed to your clanker run. Though it's not because of the search itself, it's because of the reduced round trips of the agent.

Let's try to do a search on chromium for actual code. You can literally see that LLMs LOVE to stack all kinds of guards to reduce the amount of incoming files on their own, similar to what is happening to the

Here is a beautiful example of 2 sessions, one with Claude's default tools and the one with fff

The one with fff mcp that is 3x less time and 4x less cost (lmao I should've used this in the announcement)

Most of the queries immediately look like "v8/ " which is parsed by the fff query parsing and does very fast SIMD-optimized prefiltering in the paths 4ns + bigram index 8ns, having the file search only touch 458 files on the real query generated by the agent. This query returned results in under 2ms

And the biggest value is NOT THE RAW SPEED of a file search, it's the reduced amount of round trips because fff has built-in fuzzy code matching that is pretty slow (it's impossible to prefilter) but it does show suggestions for your LLM, significantly reducing round trips. This is where the actual optimization for the coding agents is, and you folks are missing that.

In addition to that, fff knows about git status of every file, how often it's modified, it classifies which lines are definitions (function names, classes, variables) to suggest them first, keeps track of frecency and sorts the files by all kinds of heuristics (which is very slow) to prevent the user, whether a human or AI agent, from repeating the search which is exactly where the time waste is.

And it can still finish the prefiltering index on a 500k file codebase faster than an LLM will generate the first tool call.

Cheers.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
