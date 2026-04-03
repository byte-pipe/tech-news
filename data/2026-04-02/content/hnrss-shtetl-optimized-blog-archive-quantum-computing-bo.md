---
title: Shtetl-Optimized » Blog Archive » Quantum computing bombshells that are not April Fools
url: https://scottaaronson.blog/?p=9665
site_name: hnrss
content_file: hnrss-shtetl-optimized-blog-archive-quantum-computing-bo
fetched_at: '2026-04-02T11:21:03.563074'
original_url: https://scottaaronson.blog/?p=9665
date: '2026-04-02'
published_date: '2026-04-01T21:26:47+00:00'
description: For those of you who haven't seen, there were actually two “bombshell” QC announcements this week. One, from Caltech, including friend-of-the-blog John Preskill, showed how to do quantum fault-tolerance with lower overhead than was previously known, by using high-rate codes, which could work for example in neutral-atom architectures (or possibly other architectures that allow nonlocal…
tags:
- hackernews
- hnrss
---

## Quantum computing bombshells that are not April Fools

For those of you who haven’t seen, there were actually two “bombshell” QC announcements this week. One, from Caltech, including friend-of-the-blog John Preskill,showed how to do quantum fault-tolerancewith lower overhead than was previously known, by using high-rate codes, which could work for example in neutral-atom architectures (or possibly other architectures that allow nonlocal operations, like trapped ions). The second bombshell, from Google,gave a lower-overhead implementation of Shor’s algorithmto break 256-bit elliptic curve cryptography.

Notably, out of an abudance of caution, the Google team chose to “publish” its result via a cryptographic zero-knowledge proof that their circuit exists (so, without revealing the details to attackers). This is the first time I’ve ever seen a new mathematical result actually announced that way, although I understand that there’s precedent in the 1500’s, when mathematicians would (for example) prove their ability to solve quartic equations by challenging their rivals to duels. I’m not sure how much it will actually help, as once other groups know that a smaller circuit exists, it might be only a short time until they’re able to find it as well.

Neither of these results change the basic principles of QC that we’ve known for decades, but they do change the numbers.

When you put both of them together, Bitcoin signatures for example certainly look vulnerable to quantum attack earlier than was previously known!  In particular, the Caltech group estimates that a mere 25,000 physical qubits might suffice for this, where a year ago the best estimates were in the millions. How much time will this save — maybe a year?  Subtracting, of course, off a number of years that no one knows.

In any case, these results provide an even stronger impetus for people to upgrade now to quantum-resistant cryptography.  They—meaning you, if relevant—should really get on that!

When I got an early heads-up about these results—especially the Google team’s choice to “publish” via a zero-knowledge proof—I thought of Frisch and Peierls, calculating how much U-235 was needed for a chain reaction in 1940, butnotpublishing it, even though the latest results on nuclear fission had been openly published just the year prior. Will we, in quantum computing, also soon cross that threshold? But I got strong pushback on that analogy from the cryptography and cybersecurity people who I most respect. They said: we have decades of experience with this, and the answer is that you publish. And, they said, if publishing causes people still using quantum-vulnerable systems to crap their pants … well, maybe that’s whatneedsto happen right now.

Naturally, journalists have been hounding me for comments, though it was the worst possible week, when I needed to host like four separate visitors in Austin. I hope this post helps! Please feel free to ask questions or post further details in the comments.

And now, with no time for this blog post to leaven and rise, I need to go home for my family’s Seder. Happy Passover!

 Follow

This entry was posted
												on Wednesday, April 1st, 2026 at 4:26 pm						and is filed underAnnouncements,Quantum.
						You can follow any responses to this entry through theRSS 2.0feed.

													You canleave a response, ortrackbackfrom your own site.

### 2 Responses to “Quantum computing bombshells that are not April Fools”

1. asdfSays:Comment #1April 1st, 2026 at 9:01 pmMatt Green’s comment in Quanta seemed ok to me. It’s an algorithm for a computer that’s at best years away from existing, so I’d say publish.A similar thing happened in 2017 when someone announced the existence of an attack against a conventional (non-quantum) algorithm, while holding back the details. Within a week someone else had reverse-engineered the attack:https://blog.cr.yp.to/20171105-infineon.html
2. tossrockSays:Comment #2April 1st, 2026 at 9:58 pmStill in practice as recently as the late 1600s when Hooke originally published his eponymous law for spring force – as an anagram of the latin phrase capturing the essential linear relationship, that he only decoded two years later.

### Leave a Reply

You can use rich HTML in comments! You can also use basic TeX, by enclosing it within$$ $$for displayed equations or\( \)for inline equations.

Comment Policies:After two decades of mostly-open comments, in July 2024Shtetl-Optimizedtransitioned to the following policy:All comments are treated, by default, as personal missives to me, Scott Aaronson---with no expectation either that they'll appear on the blog or that I'll reply to them.At my leisure and discretion, and in consultation with theShtetl-OptimizedCommittee of Guardians, I'll put on the blog a curated selection of comments that I judge to be particularly interesting or to move the topic forward, and I'll do my best to answer those. But it will be more like Letters to the Editor. Anyone who feels unjustly censored is welcome to the rest of the Internet.To the many who've asked me for this over the years, you're welcome!Name (required)Mail (will not be published) (required)WebsiteΔ