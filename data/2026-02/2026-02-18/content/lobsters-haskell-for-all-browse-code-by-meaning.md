---
title: 'Haskell for all: Browse code by meaning'
url: https://haskellforall.com/2026/02/browse-code-by-meaning
site_name: lobsters
content_file: lobsters-haskell-for-all-browse-code-by-meaning
fetched_at: '2026-02-18T06:00:34.535045'
original_url: https://haskellforall.com/2026/02/browse-code-by-meaning
date: '2026-02-18'
description: Navigate a repository using topic modeling
tags: vibecoding
---

# Haskell for all

###### Monday, February 16, 2026

## Browse code by meaning

This post follows up on my previous post,Beyond agentic coding,
where I sketched several ideas for non-chat AI dev tools. In that post I
teased a prototype of one such tool, asemantic project navigator, and that
prototype is now a little more suitable for public consumption. You can find
the tool I created in myGabriella439/semantic-navigatorGitHub repository.

The semantic project navigator lets you browse any repository by meaning rather
than by directory. For example, here is what the tool looks like when run onGrace, my prompt-engineering
programming language:

I made this because I want to highlight how much better our coding tools could
be if we were to think outside of the chat box. Can you imagine trying to
gather this same information from a chat agent? It's certainlypossiblebut
going through a chat agent has a lot of downsides:

* information overload (you have to sift through prose at every step)
* clumsiness (you have to type out every inquiry and idly wait for a response)
* supportability (it's hard to reason about the agent's accuracy/completeness)

I think we can do much better than chat interfaces if we're willing to put in
the design and engineering work. We can still use large language models, but
we can build much better interfaces to them.

## Example usage

This post is more about an idea for a better interface rather than an
implementation, but in my experience people internalize some things better when
they can play with a working implementation.

TheREADMEprovides instructions for installing and running the semantic navigator tool,
but the basic usage is:

$
 export
 OPENAI_API_KEY="
$(
<
 ./path/to/openai.key
)
"

$
 semantic-navigator
 ./path/to/repository

Depending on the size of the project it will probably take between a few
seconds to a minute to produce a tree viewer. Most of this delay is due to
usinggpt-5-miniby default to label clusters becausegpt-5-minihas worse
latency1, howevergpt-5-miniis cheaper and still generally gives good
results. If you're willing to pay 7× as much to use a snappier and better model
you can do this:

$
 semantic-navigator
 --completion-model
 gpt-5.2
 ./path/to/repository

For small repositories (up to 20 files) you won't see any clusters and the tool
will just summarize the individual files:

This is a tradeoff the tool makes for ergonomic reasons: the tool avoids
subdividing clusters with 20 files or fewer.

For a medium-sized repository you'll begin to see top-level clusters:

The label for each cluster describes the files within that cluster and will
also display a file pattern if all files within the cluster begin with the same
prefix or suffix. In the above example the "Project Prelude" doesn't display a
file pattern because there is no common prefix or suffix within the cluster,
whereas the "Condition Rendering" cluster displays a file pattern of*/Condition.dhallbecause both files within the cluster share the same
suffix.

For an even larger repository you'll begin to see nested clusters:

On a somewhat modern MacBook this tool can handle up to ≈10,000 files within a
few minutes.

You can use this tool on any text documents; not just code! For example,
here's the result when running the tool on the repository for my self-hosted
blog:

In other words, this tool isn't just a code indexer or project indexer; it's a
general file indexer.

## Implementation

I tunneled pretty hard on improving the quality of the results, not because I
expect people to use this tool in anger but rather because I've been burned by a
lot of AI solutions that "demo well" but then fall apart at the seams or perform
poorly under scrutiny. I wanted to see if the approach I had in mind could
perform well on real world repositories or if it was just a curiosity.

The semantic navigator has a conceptually simple implementation:

* Embed every file in the project as a semantic vector
* Recursively cluster those semantic vectors into smaller and smaller clusters
* Label each node in this tree of nested clusters
* Display the tree of subclusters to the user

However, the devil is in the details so I'll expand upon the most interesting
design choices I made to improve the quality of the results and the user
experience.

### Clustering

I wanted this tool to be as "hands-free" and "magical" as possible, which meant
that I preferred a clustering algorithm that wouldn't require specifying the
desired number of clusters (or any other tuning parameters for that matter).

The algorithm I ended up going with wasspectral clusteringand I
won't go into a lot of detail about the algorithm except to say that it has a
few nice properties:

* the algorithm is highly "supportable"… meaning that the algorithm is based on linear algebra and not just vibes.
That's not to say that this algorithm is the best algorithm or that other
clustering algorithms wouldn't perform well, but it's easier to justify why
the algorithm works and understand how variations on the algorithm affect the
quality of the results.
* the performance is alrightIt scales just fine to about ≈10,000 files which is enough for my use case
(indexing code). If I were interested in clustering larger things then I
might revisit the choice of algorithm.
* there are tuning-free variations on this algorithmThis was a big deal to me because I wanted this to work well in inexpert
hands. I'm not a fan of tools with lots of dials and knobs.

In particular, spectral clustering has the nice property that yousort ofdon't need to decide how many clusters you want. The algorithm "suggests"
natural cluster counts so the choice of cluster count becomes less arbitrary.

For performance reasons and also ergonomic reasons you still want to cap the
cluster count because otherwise the algorithm can suggest a very large cluster
count. I found some cases where the optimal cluster count was in the
hundreds2but that's way too many clusters to present to a user all at once.
So the one somewhat arbitrary number is that every cluster can have at most
20 sub-clusters.

### Distinctive labels

Labeling clusters was also way trickier than I thought it would be going into
this. For example, you might naively think to do something like this:

* label each leaf of the tree (each individual file)
* label each cluster based on the labels for each child

… but the problem with that approach is that you end up getting very generic
names for each cluster and often you will have multiple sibling clusters with
extremely similar names, like this example from an earlier iteration of my
algorithm:

There you have a bunch of sibling clusters labeled "type errors" (which is also
the same name as their parent cluster) so the user has no idea which subcluster
to pick.

The trick is to label the siblings together instead of labeling them
independently. I present all the sibling clusters to the model and ask the
model to label them all at once. The model picks much more distinctive labels
once it understands that it is labeling each clusterin the context of other
sibling clusters.

A related thing that improved labels was to ask the model to producemoredata
("homework") than strictly needed for the label. I actually ask the model to
produce this data structure for each cluster:

class
 Label
(
BaseModel
):

 overarchingTheme
:
 str

 distinguishingFeature
:
 str

 label
:
 str

In other words, for each sibling cluster the model has to not only produce alabelbut also come up with anoverarchingThemeand adistinguishingFeaturefor that cluster. I then throw away theoverarchingThemeanddistinguishingFeatureand keep just thelabel.

My partner showed me this "homework" trick for guiding a model's reasoning
process, where the extra requested work nudges the model into the right basin
for the result we actually care about. Moreover, this works better than an
ordinary prose prompt because we have much more control over where the homework
is done. When we place theoverarchingThemeanddistinguishingFeaturehomework next to a givenlabelthe model correctly infers that the requested
homework is relevant tothat specific labeland not other labels. You can
more reliably communicate that sort of "spatial relationship" between reasoning
steps using types rather than prose.

### Label sizes

I spent way more time than I care to admit tweaking the label sizes, which were
the most important "magic constants" that influenced the quality of the results.

The "magic" sizes I came up with for labels were:

* 3 to 7 words for file labels
* exactly 2 words for cluster labels

This may sound like a trivial detail but this made a very big impact on the
quality of the results and the user experience. In particular:

* shorter labels force the model to compress informationIf you permit longer labels then the model is more likely to spit out a
laundry list of the cluster's contents and less likely to identify important
patterns and themes.
* shorter labels are also easier for the user to digestUsers need to be able to find the cluster of interest at a glance and
shorter labels are easier to visually scan

I permit longer labels for files because those are the ground truth for all the
other labels: once files are labeled the contents are never consulted again. If
file labels are misleading or missing important information then that poisons
all other derived labels.

### Path patterns

I mentioned earlier how labels include path patterns (if any) matching all files
within that cluster:

These path patterns are not just for the user's benefit; I also feed these path
patterns into the labeling algorithm!

One of my rules of thumb for prompt engineering is that anything that helps a
human helps a model, too. I originally added the path patterns for the benefit
of the user (because they're really useful hints) but then I realized: the model
would probably benefit from them, too (and it did improve labeling quite a lot).

Path patterns also have a nice emergent property: they gracefully degrade to
ordinary filesystem browsing when clusters align with the project's filesystem
hierarchy, like in this example:

Here the user can see at a glance that selecting the last cluster is
functionally the same thing as descending into thetasty/data/jsonsubdirectory.

## Conclusions

I created this tool mostly as a fairly fleshed out proof of concept but I'll
still talk about how this could be made into a more "real" thing.

For example, one obvious next step would be to turn the semantic navigator into
an IDE plugin powered by this tool. That's a no-brainer.

However, you could apply this tool outside of software development, too: there's
nothing really code-specific about how the semantic navigator works and the tool
works just fine on any directory tree containing text files.

For example, my partner and I stress-tested this tool on her giant collection
of saved memes3by first translating the memes to text (usingthe Kimi model) and then running
the semantic navigator on the text. The results were great and amusing:

… and you can see the cluster of memes highlighted in the screenshot here:

That means another promising direction for this sort of work is generalizing
the tool to work on other document types (e.g. images or PDFs), which is very
doable with modern multimodal models.

## Footnotes

1. OpenAI advertisesgpt-5-minias faster thangpt-5*models, but I see
significantly worse latency for completions requests usinggpt-5-miniwhich
matters more for this project's purposes. The completions model is only being
used to generate short labels where inference throughput does not matter that
much.↩
2. There was one repository I tested that suggested a cluster count of 600+
and the infuriating part is that the suggestion wasgood. The clusters
returned were very meaningful and well-separated, but that was still way too
many clusters to use as a starting point.↩
3. Yes, my partner has an enormous library of memes that she saved locally
to her computer. She hates losing memes to bitrot, plus storing them locally
means she can easily dig them up later. However, her meme library has gotten
large enough that she now has trouble browsing them so she was really excited
when I demo'd my semantic navigation tool to her.↩

Copyright © 2026
Gabriella Gonzalez
. This work is licensed under
CC BY-SA 4.0
