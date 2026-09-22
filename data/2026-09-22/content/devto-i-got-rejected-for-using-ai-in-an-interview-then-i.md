---
title: I got rejected for using AI in an interview. Then I watched the interviewer do it. - DEV Community
url: https://dev.to/infoinlet1/i-got-rejected-for-using-ai-in-an-interview-then-i-watched-the-interviewer-do-it-31d0
site_name: devto
content_file: devto-i-got-rejected-for-using-ai-in-an-interview-then-i
fetched_at: '2026-09-22T15:25:57.987801'
original_url: https://dev.to/infoinlet1/i-got-rejected-for-using-ai-in-an-interview-then-i-watched-the-interviewer-do-it-31d0
author: Info Inlet
date: '2026-09-19'
description: I got the rejection email on a Tuesday. I've been rejected before — everyone has. This one broke... Tagged with ai, webdev, career, discuss.
tags: '#discuss, #ai, #webdev, #career'
---

Comments highlight the new era of AI hypocrisy

I got the rejection email on a Tuesday. I've been rejected before — everyone has. This one broke something.

"While your technical skills are strong, we felt your reliance on AI tools during the assessment didn't reflect the independent problem-solving we're looking for."

Rejected. For using AI.

By a man who — forty minutes earlier, on the same video call — had quietly done the exact same thing right in front of me.

Let me tell you how I know.

## It was a normal live-coding round

Screen shared, camera on, the usual. A medium problem: parse some messy input, transform it, return something structured. Nothing exotic. The kind of thing I do at my actual job every single day.

So I did it the way I do it every single day. I broke the problem down, wrote the core logic myself, and let the assistant stub the boilerplate so I could spend my attention on the edge cases. And Isaid so, out loud, on the call: "I'll let the assistant scaffold this part so I can focus on where it'll actually break."

I wasn't hiding anything. That, it turns out, was the mistake — thinking honesty was the safe choice.

## Then he went quiet

Not thinking-quiet.Uncomfortable-quiet.

I didn't clock it in the moment. You never do. You just feel a small temperature drop on the other side of the glass and tell yourself you're imagining it.

## The follow-up that gave him away

He asked a follow-up about time complexity. Then his eyes did the thing.

The flick. The half-second reading pause. The answer that came back a beat too clean, too structured, tooformattedto be something a person says off the top of their head on a Tuesday afternoon.

I'm not going to pretend I could read his screen. But I've used these tools every day for two years. I know exactly what someone reading a generated answer looks like, because I look like that too. He was reading an AI's answer while quietly marking me down for reaching for one.

## Here's what actually broke me

It wasn't the hypocrisy. Hypocrisy I can file away.

What broke me was realizing the rule was never "don't use AI."

The rule was"don't let us see you use AI."

Pretend you didn't. Perform the 2019 version of yourself. Hide the tool that everyone in the room — interviewer included — is already using. They didn't reject someone who couldn't do the work. They rejected someone who was honest abouthowhe does it. Those are not the same person, and only one of them is a problem.

## The test they thought they were running

Here's the part I've actually been chewing on, past the sting.

They believed they were testing whether I could solve the problemwithoutAI. But that's a test for a job that no longer exists. Nobody on their team ships without AI. He couldn't get through afollow-up questionwithout it.

The test that would have actually told them something is the opposite one: give me the AI, then watch whether I can tell when it's lying to me.

Because that's the only skill that survived a year of me leaning on these tools as hard as humanly possible. A month ago I ran an experiment where I let AI write100% of my codefor 30 days and refused to type a line of application logic myself. It shipped a real product. And the thing that made it shippable wasn't the AI — it was the times I looked at a clean, confident, plausible diff and saidno.

## The tell they never asked about

During that same round, before the boilerplate, I'd flagged something in the problem's framing: the write path needed to persist before it acknowledged, or a retry could double-count. It's the exact ack-before-persist bug that bit me during the 30-day run — the one where acknowledging before you save leaves a paying customer locked out with no record on a bad day.

No AI gave me that. I earned it the slow, expensive way, years before any of this. It's the thing that would have been worth an entire interview.

They didn't ask about it. They were too busy noting that I'd used autocomplete.

## The two skills we keep pricing as one

There are two different things hiding inside the word "coding," and hiring is still pricing them as one.

* Recall— the syntax, the API, the flag order, the incantation. AI has made this obsolete, and good riddance; it was never the valuable part. Testing for it in 2026 is testing for penmanship.
* Judgment— knowing what to build, what to distrust, what breaks at 2am when a real person does something strange. AI cannot hand you this. You can only earn it by doing the work AI now does for you — and you can onlydemonstrateit by catching the AI when it's wrong.

An interview that punishes you for using AI is measuring recall and calling it character. An interview worth passing hands you the AI and measures whether you can overrule it.

## Why this is the whole reason I build the way I do

I didn't quit AI over one bad interview. It still writes 100% of my code and always will — the typing was never the hard part, it just felt like it was.

But that call crystallized something I already believed about how these systems should be built. The failure in that room wasn't the AI. It was a process that couldn't tell the difference betweenusinga tool andbeing unable to judge its output— so it optimized for hiding the tool instead of testing the judgment.

That's precisely the mistake I refuse to build into an agent. I never let the thing that writes the code be the thing that blesses it. There's an author agent that produces the diff, a separate skeptic agent whose only job is torefuteit rather than admire it, and a human on the merge button who can still see the blast radius the model can't. The AI's role is never hidden and never trusted by default — it's made explicit so a human can judge it. That separation between author, skeptic, and human is the entire shape ofxenition, the agent platform we build. That interviewer and I were both using AI. The only difference worth hiring for is whether you're honest enough to admit it and sharp enough to overrule it.

Honest question for the comments:have you ever hidden the fact that you used AI in an interview — or been on the other side of the glass, marking someone down for it? I want to know how common this actually is, because I don't think I hit a rare bug. I think I hit the norm. 👇

(If this landed, a ❤️ and a 🔖 help — and tell me the moment you realized the rule was "don't get caught," not "don't use it.")

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (20 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse