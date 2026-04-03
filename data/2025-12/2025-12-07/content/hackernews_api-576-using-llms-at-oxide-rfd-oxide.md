---
title: 576 - Using LLMs at Oxide / RFD / Oxide
url: https://rfd.shared.oxide.computer/rfd/0576
site_name: hackernews_api
fetched_at: '2025-12-07T19:06:24.130934'
original_url: https://rfd.shared.oxide.computer/rfd/0576
author: steveklabnik
date: '2025-12-07'
description: Using LLMs at Oxide
tags:
- hackernews
- trending
---

discussion
RFD

576

# RFD576Using LLMs at Oxide

This RFD can be accessed by the following groups:
[
public
]
State
discussion
RFD
576
Authors
Bryan Cantrill

Updated

Large language models (LLMs) are an indisputable breakthrough of the last five
years, potentially profoundly changing the way that we work. As with any
extraordinarily powerful tool, LLM use has both promise and peril — and that
they are so general-purpose leaves real questions about how and when they
should be used. The landscape is shifting so rapidly that static prescription
is unlikely — but that LLMs are evolving so quickly also gives urgency to the
question:how should LLMs be used at Oxide?

## Values in LLM usage

As is our wont, it’s helpful to look at LLM use through the lens of our values,
several of which come to mind, listed here in priority order:

* Responsibility: In terms of LLM use at Oxide, our lodestar is our sense of
responsibility. However powerful they may be, LLMs are but a tool, ultimately
acting at the behest of a human. Oxide employees bear responsibility for the
artifacts we create, whatever automation we might employ to create them. That
is, human judgement remains firmly in the loop: even if or as an LLM is
generating an artifact that we will use (writing, test cases, documentation,
code, etc.), their output is the responsibility of the human using them.
* Rigor: LLMs are double-edged with respect to rigor. On the one hand,
wielded carefully, they can help us sharpen our own thinking by pointing out
holes in our own reasoning or otherwise providing thought-provoking
suggestions. On the other, if used recklessly or thoughtlessly, they can have
the opposite effect, replacing crisp thinking with generated flotsam. LLMs are
useful in as much as they promote and reinforce our rigor.
* Empathy: Be we readers or writers, there are humans on the other end of our
language use. As we use LLMs, we must keep in mind our empathy for that human,
be they the one who is consuming our writing, or the one who has written what
we are reading.
* Teamwork: We are working together on a shared endeavor, and we must be sure
that our LLM use does not undermine our sense of teamwork. Specifically, we
must be careful to not use LLMs in such a way as to undermine the trust that we
have in one another. This isn’t as simple as disclosure of usage: and in
fact, volunteering that an LLM has been used to generate work product is to
implicitly distance oneself from the responsibility for the content — and
serves as to erode the trust that is essential for teamwork.
* Urgency: Urgency seems natural with a tool that can seemingly do so much
knowledge work so quickly, but with respect to LLM use, too many organizations
have seemingly enshrined urgency over all else. These organizations treat LLMs
as an opportunity to increase pace over all else, seemingly without regard for
setting direction. Urgency is certainly important, and LLMs absolutely afford
an opportunity to do work more quickly — but that pace must not come at the
expense of our responsibility, rigor, empathy and teamwork.

## Uses of LLMs

LLM use varies widely, and the ramifications of those uses vary
accordingly; it’s worth taking apart several of the (many) uses for LLMs.

### LLMs as readers

LLMs are superlative at reading comprehension, able to process and meaningfully
comprehend documents effectively instantly. This can be extraordinarily
powerful for summarizing documents — or of answering more specific questions
of a large document like a datasheet or specification. (Ironically, LLMs are
especially good at evaluating documents to assess the degree that an LLM
assisted their creation!)

While use of LLMs to assist comprehension has little downside, it does come
with an important caveat: when uploading a document to a hosted LLM (ChatGPT,
Claude, Gemini, etc.), there must be assurance ofdata privacy— and
specifically, assurance that the model will not use the document to train
future iterations of itself. Note that this may be opt-out (that is, by
default, a model may reserve the right to train on uploaded documents), but can
generally be controlled via preferences — albeit occasionally via euphemism.
(OpenAI shamelessly calls this checked-by-default setting "Improve the model
for everyone", making anyone who doesn’t wish the model to train on their data
feel as if they suffer from a kind of reactionary avarice.)

A final cautionary note: using LLMs to assist comprehension should not
substitute for actually reading a document where such reading is socially
expected. More concretely: while LLMs can be a useful tool to assist in the
evaluating of candidate materials per[rfd3], their use should be restricted
to be as a tool, not as a substitute for human eyes (and brain!).

### LLMs as editors

LLMs can be excellent editors. Engaging an LLM late in the creative process
(that is, with a document already written and broadly polished), allows for
LLMs to provide helpful feedback on structure, phrasing, etc. — all without
danger of losing one’s own voice. A cautionary note here: LLMs are infamous
pleasers — and you may find that the breathless praise from an LLM is in fact
more sycophancy than analysis. This becomes more perilous the earlier one uses
an LLM in the writing process: the less polish a document already has, the
more likely it is that an LLM will steer to something wholly different — at
once praising your groundbreaking genius while offering to rewrite it for you.

### LLMs as writers

While LLMs are adept at reading and can be terrific at editing, their writing
is much more mixed. At best, writing from LLMs is hackneyed and cliché-ridden;
at worst, it brims with tells that reveal that the prose is in fact
automatically generated.

What’s so bad about this? First, to those who can recognize an LLM’s reveals
(an expanding demographic!), it’s just embarrassing — it’s as if the writer is
walking around with theirintellectual
fly open. But there are deeper problems: LLM-generated writing undermines
the authenticity of not just one’s writing but of the thinking behind it as
well. If the prose is automatically generated, might the ideas be too? The
reader can’t be sure — and increasingly, the hallmarks of LLM generation cause
readers to turn off (or worse).

Finally, LLM-generated prose undermines a social contract of sorts: absent
LLMs, it is presumed that of the reader and the writer, it is the writer that
has undertaken the greater intellectual exertion. (That is, it is more work to
write than to read!) For the reader, this is important: should they struggle
with an idea, they can reasonably assume that the writer themselves understands
it — and it is the least a reader can do to labor to make sense of it.

If, however, prose is LLM-generated, this social contract becomes ripped up:
a reader cannot assume that the writer understands their ideas because they
might not so much have read the product of the LLM that they tasked to write it.
If one is lucky, these are LLM hallucinations: obviously wrong and quickly
discarded. If one is unlucky, however, it will be a kind of LLM-induced
cognitive dissonance: a puzzle in which pieces don’t fit because there is in
fact no puzzle at all. This can leave a reader frustrated: why should they
spend more time reading prose than the writer spent writing it?

This can be navigated, of course, but it is truly perilous: our writing
is an important vessel for building trust — and that trust can be quickly
eroded if we are not speaking with our own voice. For us at Oxide, there
is a more mechanical reason to be jaundiced about using LLMs to write:
because our hiring process very much selects for writers, we know that
everyone at Oxidecanwrite — and we have the luxury of demanding of
ourselves the kind of writing that we know that we are all capable of.

So our guideline is to generally not use LLMs to write, but this shouldn’t
be thought of as an absolute — and it doesn’t mean that an LLM can’t be
used as part of the writing process. Just please: consider your
responsibility to yourself, to your own ideas — and to the reader.

### LLMs as code reviewers

As with reading comprehension and editing, LLMs can make for good code
reviewers. But they can also make nonsense suggestions or otherwise miss
larger issues. LLMs should be used for review (and can be very helpful when
targeted to look for a particular kind of issue), but that review should not
be accepted as a human substitute.

### LLMs as debuggers

LLMs can be surprisingly helpful debugging problems, but perhaps only because
our expectations for them would be so low. While LLMs shouldn’t be relied upon
(clearly?) to debug a problem, they can serve as a kind of animatronicrubber duck, helping to
inspire the next questions to ask. (And they can be surprising: LLMs have been
known to debug I2C issues from the screenshot of a scope capture!) When
debugging a vexing problem one has little to lose by using an LLM — but
perhaps also little to gain.

### LLMs as programmers

LLMs are amazingly good at writing code — so much so that there is borderline
mass hysteria about LLMs entirely eliminating software engineering as a craft.
As with using an LLM to write prose, there is obvious peril here! Unlike
prose, however (which really should be handed in a polished form to an LLM to
maximize the LLM’s efficacy), LLMs can be quite effective writing codede
novo. This is especially valuable for code that is experimental or auxiliary
or otherwise throwaway. The closer code is to the system that we ship, the
greater care needs to be shown when using LLMs. Even with something that seems
natural for LLM contribution (e.g., writing tests), one should still be
careful: it’s easy for LLMs to spiral into nonsense on even simple tasks.
Still, they can be extraordinarily useful — and can help to provide an entire
spectrum of utility in writing software; they shouldn’t be dismissed out of
hand.

Wherever LLM-generated code is used, it becomes the responsibility of the
engineer. As part of this process of taking responsibility,self-reviewbecomes essential: LLM-generated code should not be reviewed by others if the
responsible engineer has not themselves reviewed it. Moreover, once in the
loop of peer review, generation should more or less be removed: if code review
comments are addressed by wholesale re-generation, iterative review becomes
impossible.

In short, where LLMs are used to generate code, responsibility, rigor, empathy
and teamwork must remain top of mind.

## Mechanics

Mechanical details of using LLMs — along with many specific tips and links — can be
found in the (internal)LLMs at Oxidedocument.

## Determinations

Broadly speaking, LLM use is encouraged at Oxide, but that use must
always be consistent with our deeply-held sense of responsibility:
our responsibility to our product, our responsibility to our customers — and our responsibility to one another.

## External References

* [rfd3] Oxide Computer Company. RFD 3 Oxide Hiring Process.https://rfd.shared.oxide.computer/rfd/0003.
* Values in LLM usage
* Uses of LLMs
* LLMs as readers
* LLMs as editors
* LLMs as writers
* LLMs as code reviewers
* LLMs as debuggers
* LLMs as programmers
* Mechanics
* Determinations
* External References

### Table of Contents
