---
title: How can I prevent my AI coding assistant from repeating fixed mistakes across sessions? - DEV Community
url: https://dev.to/izgorodin/how-can-i-prevent-my-ai-coding-assistant-from-repeating-fixed-mistakes-across-sessions-2kf7
site_name: devto
content_file: devto-how-can-i-prevent-my-ai-coding-assistant-from-repe
fetched_at: '2026-09-19T14:10:47.211466'
original_url: https://dev.to/izgorodin/how-can-i-prevent-my-ai-coding-assistant-from-repeating-fixed-mistakes-across-sessions-2kf7
author: Edward Izgorodin
date: '2026-09-15'
description: On Tuesday you told the assistant that the migration script must never touch the staging database. It... Tagged with ai, agents, mcp, architecture.
tags: '#ai, #agents, #mcp, #architecture'
---

Storage fails without negative feedback loops

On Tuesday you told the assistant that the migration script must never touch the staging database. It agreed, rewrote the script, and the session ended. On Thursday, in a fresh session, it wrote the same migration against staging again, and the note where you explained why was sitting right there in its memory, retrieved alongside the old approach, with nothing to say which of the two had failed. You fixed it, you explained it, and it came back. The complaint is common enough to be a search query, and it hides a mechanical question that is easier to answer than the complaint itself: when the outcome of a recall was bad, does anything in the memory layer change? Not when you write something new. When something failed.

Writing the correction down is not the fix, and it is worth being precise about why. The memory that carried the mistake is still in the store. It is still eligible. At the start of the next session it arrives in front of the model again, next to your correction, with nothing separating the two. Storing a mistake and learning from it are different operations. Storage means the mistake can be read again. Learning means something about what the system does next is different because that outcome was bad.

So I put one question to six memory systems, including the one I work on, and read each vendor's own documentation for the answer: is there a published input that takes an explicitly negative verdict on a recall, what is it attached to, and what does the vendor say it moves. No performance numbers anywhere below, mine or anyone's. A number is the output of a recipe, and I am not showing a recipe here.

## Four of the five others publish an input, which is not what I expected

One line to carry through the rest: if reporting a bad recall changes nothing about the next read, you do not have learning. You have a diary.

The first version of this sweep read one page of each vendor's documentation tree and concluded that almost nobody publishes an outcome input. That conclusion was wrong, and the reason is instructive: the pages that describe these inputs sit several clicks below the root. Re-read on each vendor's documentation host, four of the five other systems publish an input that accepts a negative verdict. What separates them is not whether the input exists. It is what the input is attached to, and whether the vendor says anything about what changes in the next read.

system

published input that takes a negative verdict

attached to

what the vendor publishes about the effect

Cognee

cognee.session.add_feedback
, feedback text plus a score from one to five

the answer to a recall, by its identifier inside a session

"To make feedback influence future retrieval, run improve() with the relevant session_ids."

Mem0

POST /v1/feedback/
, values POSITIVE, NEGATIVE and VERY_NEGATIVE

a memory result, by memory id

the endpoint exists to "Submit positive or negative feedback on memory results", and the page says nothing about ranking

Letta

PATCH /v1/steps/{step_id}/feedback
, positive or negative

an execution step

the operation modifies feedback for a step, and the page connects it to no retrieval order

Supermemory

review endpoints: approve, decline, undo

a memory the engine inferred, not one you stated

an unreviewed inferred memory "is down-weighted in search", a declined one is "Removed from search entirely"

Zep

none found on the surfaces read

Mnemoverse

memory_feedback(atom_ids, outcome)
, a float from minus one to plus one

the memories a recall returned

"This tunes future recall", and "unhelpful memories are out-ranked rather than erased"

Every quotation in that table is a contiguous substring of a page you can open, re-checked on 2026-09-12, and the page for each is named on thefull write-up, together with the queries behind the one absence claim.

## What the input is attached to is where they separate

Cognee is the clearest case. Its feedback guide records the interaction, finds the identifier of the answer you want to rate, calls add_feedback on it, and then says the sentence that matters: "To make feedback influence future retrieval, run improve() with the relevant session_ids." That is an input on the answer to a retrieval, with a published path from it back to what retrieval does next.

Mem0 publishes an input too, and the honest boundary is what its page does not say. The endpoint takes a memory identifier and one of three values; it states what it accepts, not what happens to ranking afterwards. Mem0 separately publishes a search-time bias that moves the order of results while taking no verdict at all: a per-project decay that boosts recently touched memories, off by default, and in the vendor's words, "Decay can reorder candidates but never removes them". Frequency and recency move that ranking. Whether the answer was right does not.

Letta's input exists and is attached to something else. A step is an execution object, and marking one positive or negative is useful for observability and for evaluation. It is not a report that a retrieved memory was wrong, and nothing on that page says it reorders a later read.

Supermemory's review endpoints take a verdict on a guess the engine made about a fact, not on how a recall turned out. Those are different questions, and it is worth keeping them apart: one asks whether a derived fact is true, the other asks whether what came back was useful.

Zep is the one absence claim, and its bounds go in the same sentence: on its machine-readable index and across the pages listed in its site map on the day of the sweep, nothing describes an input that takes a verdict on a recall. The closed part of the product cannot be read from outside, and this says nothing about it.

## Learning from context is not learning from outcome

Two of the five publish a stated position on how learning should work, and both put the learning in context. Supermemory says its model "extracts and dreams on the context of every user, task, and tenant". Letta's research post argues that learning belongs in token space, "updates to learned context, not weights". Both are real positions and both are about the same thing: more of what happened goes in, and the model gets a better briefing. Neither sentence takes a verdict on whether the last answer was any good.

The same Letta page names the one shipped mechanism that does learn from user feedback at scale, and puts two limits on it in the vendor's own words: Cursor's tab completion model improves the model for everyone rather than for your project, and it covers completions rather than reasoning and actions. If you have read anywhere that nobody in this field learns from outcomes, that is the counter-example, and the limits on it are the vendor's.

## The word for it, and where it appears

There is a word for the negative direction of this mechanism, and a code search for its solid spelling across the five vendor organisations returns zero files, with a control term returning files in every one of them. That zero says less than it seems to. Two of the five write the word with a hyphen on live documentation pages: Supermemory in its review documentation, and Cognee in a guide that says its search does not down-weight closed nodes, which is a sentence about what their retrieval does not do. The vocabulary is lopsided. Rerank is everywhere; the direction that means down, on the strength of a bad result, is written down twice, and one of those two times says it does not happen.

## Our row, and the limit on it

I work on Mnemoverse, so weigh this section accordingly. We publish an input for an outcome that takes a value from minus one to plus one, and minus one is the case this article is about. It is attached to the memories a recall returned, so the verdict lands on the items that were actually put in front of the model, and what it moves is the order of the next read rather than the text of the memory.

The limit is the one that applies to four of these six: the engine is closed. You can read the range and the description, and you cannot watch the ranking move. And our own published article about this input says that explicit outcome feedback is almost entirely absent from the production traffic we measured, because reporting an outcome is something the agent has to choose to do after the answer is already written, when nothing is watching. Having the input does not mean the mistake will not come back. A channel nobody calls and a channel that does not exist produce the same repeated mistake, and that is the fairest summary of where this category stands, ours included.

## The one-minute test, on whatever you already use

Find a memory your tool holds that you know is wrong. Ask a question that memory would answer, and watch the wrong item come back. Before reporting anything, ask the same question two or three more times in fresh sessions and note whether the order already moves on its own: that is your control. Then tell the tool it was wrong, in whatever way the tool allows: the endpoint, the review action, a slash command, a message in the chat, and ask the same question once more in a fresh session, so nothing left in the context window is doing the work. Read the result with care in both directions. If the wrong item still comes back first, that alone does not show the report went nowhere: its weight can fall without its rank changing when it started far ahead of the rest. If the order moved after the report and never moved in the control runs, you have a candidate for the mechanism this article is about, and the vendor's own description is the next thing to read.

## What to ask a vendor

Four questions, in this order. Is there an input that takes an outcome, not a place to write a note but a report that what you returned was wrong. What is it attached to: an answer, a memory, a step, or a stored guess, and only the first two are about a recall. What does it move, and where is that written down: the text, the weight, or the order of the next read. And who has to remember to send it. If the answer to the last one is the agent, after the work is done, when nothing is watching, read everything else with that in mind. That is our answer too.

Disclosure: I work onMnemoverse, one of the six systems above, so weigh the argument accordingly. The full comparison, with every source page and every query printed, is on our library.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (53 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse