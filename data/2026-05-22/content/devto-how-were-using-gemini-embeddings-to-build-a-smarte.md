---
title: How we're using Gemini Embeddings to build a smarter, community-driven feed on DEV - DEV Community
url: https://dev.to/devteam/how-were-using-gemini-embeddings-to-build-a-smarter-community-driven-feed-on-dev-1b9f
site_name: devto
content_file: devto-how-were-using-gemini-embeddings-to-build-a-smarte
fetched_at: '2026-05-22T19:34:50.809391'
original_url: https://dev.to/devteam/how-were-using-gemini-embeddings-to-build-a-smarter-community-driven-feed-on-dev-1b9f
author: Ben Halpern
date: '2026-05-22'
description: Big improvements incoming 👋 Finding the right balance for a feed algorithm is historically really... Tagged with gemini, ai, googlecloud, postgres.
tags: '#gemini, #ai, #googlecloud, #postgres'
---

Big improvements incoming 👋

Finding the right balance for a feed algorithm is historically really hard. If you optimize purely for clicks and comments, you end up with a clickbait echo chamber. But if you just sort by recency, it's a firehose where great discussions disappear in hours.

We've wrestled with this tension at DEV for a long time. We want a feed that feels alive, but actually surfaces high-quality, intellectually stimulating stuff.

So, we're trying something new. We are combining standard community signals—like who you follow and what you react to—withGemini Embeddings 2andpgvector.

Here is a look under the hood at how we are putting this together.

## 1. Keeping things flexible and auditable

Instead of duct-taping API calls all over the codebase, we built a flexible foundation using wrapper classes, mostly centered aroundAi::BaseandAi::Embedding.

When a service needs the API, it just passeswrapper: selfto the client. This letsAi::Baselook at the calling object, grab its class name, and check itsVERSION.

Ai
::
Base
.
new
(
wrapper: 
self
)

Enter fullscreen mode

Exit fullscreen mode

This pattern gives us a really clean audit trail via ourAiAuditmodel. Every single time we generate a vector or analyze a trend, we automatically log the model used, the caller's class, payloads, latency, and token counts.

It makes debugging and tracking costs so much easier, without muddying up our core business logic.

## 2. A more personalized feed

Our main feed is powered byFeedConfig. It compiles custom SQL to score and rank articles for you.

Historically, this was all hardcoded math based on things like tags and whether you follow the author. Now, we've introduced a semantic feedback loop.

As you interact with the platform, we compile a dynamicinterest_embeddingthat represents what you actually care about. We use thepgvectorextension in PostgreSQL to inject your interests directly into the SQL query:

(

 
CASE

 
WHEN
 
articles
.
semantic_embedding
 
IS
 
NOT
 
NULL

 
AND
 
articles
.
published_at
 
>=
 
:
published_since

 
THEN
 
(
1
 
-
 
(
articles
.
semantic_embedding
 
<=>
 
:
interest_embedding
))
 
*
 
:
semantic_similarity_weight

 
ELSE
 
0

 
END

)

Enter fullscreen mode

Exit fullscreen mode

By using1 - (embedding <=> user_interest), we get a cosine similarity score. We scale that up and mix it in with standard social signals (like who you follow), post quality, and time decay.

This means a highly relevant post can rise to the top of your feed, but so can a globally trending post from a community member you love. It’s all about balance.

## 3. What the heck is an embedding anyway? (And why v2 matters)

If you're new to the concept, an embedding is basically taking a piece of content—like an article text—and turning it into a long string of numbers (a vector). These numbers map the content into a "semantic space." If two posts are talking about the exact same conceptual ideas, their numbers will look very similar mathematically, even if they use completely different wording.

We've upgraded this pipeline to use Google's newly releasedGemini Embeddings 2model.

A standard text embedding model only looks at words. But Gemini Embeddings 2 compiles into massive 3,072-dimensional vectors and maps everything into a single, unified semantic space.

### Future-proofing for a multi-modal DEV

The coolest part about moving to Embeddings 2 is that it isn't just restricted to text. It natively accepts multimodal inputs—meaning text, code, images, audio, and video.

Right now, we're using it to analyze written DEV posts. But because the underlying math maps everything into the exact same vector space, we are completely future-proofing our infrastructure. As the DEV platform evolves, we can easily feed images, podcast audio, or video posts into the exact same database architecture[.

A user'sinterest_embeddingwill be able to effortlessly surface an open-source video tutorial or a technical podcast episode based entirely on conceptual relevance, without us needing to rewrite our feed logic from scratch.

## 4. Catching nuanced trends 📈

Tags are great for high-level sorting, but they miss the highly specific, timely conversations. If Ruby 3.4 drops, a#rubytag search won't distinguish between a "Hello World" tutorial and a deep debate about the new parser.

To fix this, we are in the process of building a clustering service powered byTrendDetector.

Every 6 hours, a background job runs a Leader Clustering algorithm in pure Ruby:

* Quality first:We only look at recent articles scoring at least 15 points above our homepage minimum.
* Clustering:We measure the cosine distance between articles. If a post is close enough (0.15or less) to an existing cluster, it joins it. If not, it starts a new one.
* Labeling:Once a cluster hits 10 or more articles, we ask the Gemini API to label the trend and summarize the core debate.

We store all of this inTrendMembership, which lets us sort articles in the UI based on how close they are to the core topic.

All of this can be tracked via our open source codebase Forem:

## forem/forem

### For empowering community 🌱

# Forem 🌱

For Empowering Community

Welcome to theForemcodebase, the platform that powersdev.to. We are so excited to have you. With your help, we can
build out Forem’s usability, scalability, and stability to better serve our
communities.

## What is Forem?

Forem is open source software for building communities. Communities for your
peers, customers, fanbases, families, friends, and any other time and space
where people need to come together to be part of a collectiveSee our announcement postfor a high-level overview of what Forem is.

dev.to(or just DEV) is hosted by Forem. It is a community of
software developers who write articles, take part in discussions, and build
their professional profiles. We value supportive and constructive dialogue in
the pursuit of great code and career growth for all members. The ecosystem spans
from beginner to advanced developers, and all are welcome to find their place…

View on GitHub

## 5. Putting the community first ❤️

Human curation, both from the broader community and our editorial perspective, is still the backbone of the system.

We are using Gemini Embeddings to amplify what the community is already doing. It’s about mixing the raw utility of vector search with the human spirit of developer-voted scores and relationships.

We want DEV to be the best place on the internet to share code and talk about software. We think this is a big step in that direction.

What do you think? Let me know in the comments.

Happy coding!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse