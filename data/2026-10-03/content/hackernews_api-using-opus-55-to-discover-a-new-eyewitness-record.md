---
title: Using Opus 5.5 to discover a new eyewitness record of the dodo
url: https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness
site_name: hackernews_api
content_file: hackernews_api-using-opus-55-to-discover-a-new-eyewitness-record
fetched_at: '2026-10-03T03:06:46.181278'
original_url: https://resobscura.substack.com/p/using-opus-55-to-discover-a-new-eyewitness
author: Benjamin Breen
date: '2026-10-02'
description: Frontier models can now produce novel historical knowledge, but in a really weird way
tags:
- hackernews
- trending
---

# Using Opus 5.5 to discover a new eyewitness record of the dodo

### Frontier models can now produce novel historical knowledge, but in a really weird way

Benjamin Breen
Oct 01, 2026
21
14
3
Share

Another day, another historical cipher broken by a frontier model. Yesterday, the security researcher Carter Churchannouncedthat he had used GPT-6 Astra (working on the problem for six hours) to break a Napoleonic-era cipher that had previously resisted all decryption attempts.

Church’sposton the subject is an interesting example not just of a reproducible methodology, but also of how to vibe code an information-dense writeup that is notably different from any traditional academic aesthetic, but which actually does surface primary sources and meaningful information in a fairly deep way:

The aesthetic weirdness is just the tip of the iceberg here. What I notice most about these forays into historical sleuthing using AI (and my own attempts at same) is theepistemological weirdnessof how current frontier models now operate when given historical research tasks.

The best way to demonstrate what I mean here is by sharing the step-by-step process by which I was able to find what appears to be apreviously-unnoticed Dutch report of hunting dodosdating to 1615. The core steps were:

1. Start from an actual base of specialist knowledge to define aspecific research question(for example, I hadpreviously researchedthe history of the exotic animal trade in the seventeenth century, and am planning to write a book on animal extinctions in the early modern period which will have a dodo chapter)
2. Identify a large, freely-available, well-edited corpus of historical sources (in this case, theGLOBALISE archiveof Dutch East India Company archives, which is an amazing resource)
3. Download the sources and run them through an embedding model to allow semantic search to find passages that might help answer the research question
4. Use semantic search to surface candidate passages and then ask frontier models to read them and produce a ranked list of the best matches for human review
5. Do any of the source passages help answer the question? If so, iterate on them. If not, keep looking in new archives or with new search terms.

This is not, on its face, allthatdifferent from how I do research on my own. I tend to search around in historical databases using various search terms that pop into my head, and then scan through the results until a passage catches my interest, then I read more carefully and iterate.

The difference is that an AI agent like Opus 5.5 can spawn dozens of copies of itself to read through sources in multiple languages. If you give these agents an API key, they can also run their own embedding searches on new sources that emerge during their research, as Opus did here during the run that led it to the newly-discovered passage:

So what is that dodo passage and why does it matter?

Subscribe

## A dodo in a haystack

Few historical creatures have been more widely studied than the dodo, the large Mauritius bird that famously went extinct due to overhunting around 1681. But this is actually a large part of why findingmoreinformation about the animal turned out to be “tractable” for an AI agent: it already had a very large identified source base to draw on, and it was able to scan the scholarly literature to find out where previous archival finds relating to dodos had been made (here is Opus 5.5writing up its own process in a research dossier).

Most of what Opus 5.5 found as it searched through the millions of records in the Dutch East India Company records was already known to the many historians and scientists who have studied the history of the dodo. But one manuscript source from 1615, a ship’s log availablehere, seems not to have been noticed before.

The journal was probably written by Isbrant Cornelisz van Petten, who captained a Dutch East India Company merchant vessel calledWapen van Amsterdam. TheWapenmade landfall on the island of Mauritius in April, 1615, where the crew collected water and food to prepare for the rest of their voyage to the East Indies.

Among other things, they “caught many tortoises, dodos [dodeersen], and some geese and parrots.”

A detail from Nationaal Archief, The Hague, VOC 1.04.02, inv. 1059, fol. 141. “dodersen” (dodos) is visible at lower left here. 

Here is the Dutch transcription and English translation of the relevant passages (note that the transcription and translation are not perfect — if you work on early modern Dutch please let me know of any corrections!):

I read through the available secondary literature on the topic, like Parrish’s 2013 bookThe Dodo and the Solitaire, and other specialist articles. It genuinely looks like this is a new addition to the timeline of dodo, which previously had a gap in the 1611-16 period.

Now, as for whether this actually matters all that much: it not exactly earth-shattering. But I do think that this is a publishable result, especially when combined with another new finding from the same search, which found a probable new reference toanotherextinct bird from Mauritius, thered rail. An account from 1638, the year the Dutch first colonized the island, turns out to describe “field-hens” using the Dutch word (velthoenderen). Experts on the topic have previously identified this word as one that the Dutch used to describe red rails. But this particular reference was apparently missed because a French scholar in 1890 mistranslated the word asperdrix (partridges).

From the writeup 
here
. 

Opus 5.5 was able to go back to the original manuscript source and correct this.

For me, though, the most interestingpossiblefinding is still very much in doubt. But if it can be nailed down, it really would be quite fascinating. This is because it might help explain one of the most mysterious paintings from the 17th century: theMughal Emperor Jahangirapparently owned a living dodo. However, no one knows who gave it to him, when, or why, and Jahangir never writes anything about it in hismemoirs.

Ustad Mansur, Institute for Eastern Studies, Novo-Mikhailovsky Palace, Saint Petersburg (
Wikipedia link
)

I actuallywrote about this painting back in 2012:

Two years earlier Mansur had painted a Mauritian dodo that is still cited by biologists as the most accurate surviving representation of the bird. In other words, Jahangir wasexactlywho a canny merchant or courtier would go to if they came across a highly unusual-looking bird.

It turns out that no one really knows the exact date of this painting. Some scholars go with “circa 1625,” others with “circa 1615.” (We do know that an English merchant reported the existence of Mauritian dodos in India in 1628, but whether this included the dodo shown in the painting is unknowable).

To my great surprise, Opus 5.5 dug around in a very wide range of manuscripts to surface the following theory: Jahangir’s dodo was quite possibly the same animal that a Portuguese Jesuit described on Mauritius in 1616. The Jesuit referred to this Mauritian bird as an “ostrich.” The thing is, Mauritiushasno ostriches!

Unfortunately, the original Portuguese text of this account is now thought to be lost, but aFrench translationsurvives, and that’s what Opus is citing here:

The theory that this “ostrich” was actually a dodo is already known to experts on the topic, and the French translator glosses it as such. But it appears that the connection between this Portuguese dodo caught en route to Goa in 1616 and the dodo that ended up reaching Jahangir at some point between 1615 and 1625 has not yet been made.

Granted, the chain of transmission has not been established. But my hunch is that this may in fact be the origin of Jahangir’s dodo. This is because we happen to already have a very clear chain of transmission ofanotherexotic bird from the Portuguese based in Goa to Jahangir’s court, dating to 1612: an American turkey!

This is something I plan to dig into more. If it can be traced more reliably, I think the identification of Jahangir’s dodo would be a pretty big deal. The Mughal court dodo is possibly the most famous and scientifically important individual dodo that ever lived, because Jahangir’s brilliant court painter, Ustad Mansur, left behind the most accurate surviving depiction of it.

At minimum, I can say that this deep dive into the Dutch records has made it clear to me that frontier AI models are capable of surfacing new historical finds based on independent archival sleuthing. That’s not something I could have said months ago.

What they can’t currently do is ask the right questions or determine the significance of finds.

Subscribe

Share

## Epistemological weirdness

The main thing that contemporary AI can do for historical research is, in effect, the digital equivalent of counting sheep. Because they never get bored, they can search through enormous datasets to find new evidence for existing claims (or, potentially, disprove them).

They are worse at coming up with new ideas of their own. What seems to work best is if they are placed on the boundary between two disciplines, given a source base, and told to work methodically toward answering ahuman-generated question.

They are also notably bad at judging the historical significance of what they find.

Again and again, in my attempts to find something tractable, Opus 5.5 and GPT-6 ended up spawning up to a dozen independent agents that that drilled down into minutiae and got utterly lost in the weeds.

Sometimes, the weeds ended up being fun. For instance, one agent discovered a very entertaining and novel account of an English ship captain, Jonathan Hide, who stole valuable ebony wood plus “two sea cows” (!) from the Dutch colony in Mauritius. When a Dutch official confronted Hide and his crew, “their carpenter threatened to split my head with his axe.” The official adds:

The Captain also took about 20 land tortoises on the voyage,claiming he intended to put them ashore on St Helena, so as to breed the said tortoises there.

This is historically significant as an environmental history finding. It turns out that the animal in question, theMauritius giant tortoise,alsoended up going extinct. Whether these twenty individuals ever did end up on St. Helena, many thousands of miles away, is unknown. But we do know that Captain Hide’s ship sank near the Azores on the return voyage home.

This is a pretty great story! Early modern people transplanting crops and animals is very much in my wheelhouse, and I love the carpenter brandishing an axe at the Dutch official. I will likely use it in some of my published work at some point.

Most of the time, however, agents veered off into archives that are totally illegible to me and require very extensive specialist knowledge to fact check. For instance, this was the product of a multi-hour search into Incakhipu:

Isthat decisive? Does any of this mean anything? I genuinely have no idea. I assumeGary Urtondoes. But I don’t really want to bother someone who has dedicated his life to the study of Inca khipu with a question generated by an AI agent which spent a few hours on the same topic.

This is really the crux of the current problem in a number of fields that AI research agents stand poised to transform:how should human experts interface with these things?

I feel comfortable working with the material relating to, say, English merchants stealing giant tortoises, or Jahangir’s dodo, because this is the sort of stuff I’ve been studying for well over a decade now. But what happens when amateurs running AI research agents veer off into genuine new scholarly territory, without the knowledge or network to double check it?

This is what Carter Church gets at in the post I linked to at the top:

A patient specialist could have done this in 1970. But it would have meant weeks of a specialist’s time: period French, a steady eye for 1,300 hand-drawn signs, and the statistics, all spent on one plate in one army journal. People with those skills exist, and they have more important problems to solve. So the letter sat unread, because no one who could read it could justify the time.

I spent six hours of model time and a few evenings of my own. Tomokiyo says he’s receiving solutions faster than he can record them. I’m sure few of these are from cryptographers. A year ago that sentence probably wouldn’t have made sense.

I’d guess most “unsolved” lists, in most fields, hold more problems like this than anyone assumes. Those lists are about to get a lot shorter, and the people shortening them will increasingly be people who were simply curious.

Personally, I would be thrilled if a bunch of curious amateurs running a small army of AI agents dug into the dodo material, or into the early modern drug trade, or the history of consciousness science in the 19th century, or any number of other things I’m actively researching. But it is going to get really weird, really soon, when these things happen.

The bottleneck will soon become not research findings themselves, butthe attention of experts in niche topics.

Aguest poston mathematician Terrence Tao’s blog recently concluded: “We’re gonna need a lot more mathematicians.”

I agree, and I would add: we’re gonna need a lot more historians and humanists.

# Weekly links

• Why the Bronze Age collapsed (Works in Progress)

• Who wrote Queen Elizabeth I’s most scathing letters? (Smithsonian- this is a great example of original historical analysis based on cross-comparison between manuscript sources).

•More breakthroughs relating to the Herculaneum scrolls.

Res Obscura is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Subscribe

Leave a comment

Share

21
14
3
Share
Previous