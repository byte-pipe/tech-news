---
title: The Real Token Economy Is Not About Spending Less. It Is About Thinking Smaller. - DEV Community
url: https://dev.to/marcosomma/the-real-token-economy-is-not-about-spending-less-it-is-about-thinking-smaller-3j3e
site_name: devto
content_file: devto-the-real-token-economy-is-not-about-spending-less
fetched_at: '2026-04-28T12:26:18.009172'
original_url: https://dev.to/marcosomma/the-real-token-economy-is-not-about-spending-less-it-is-about-thinking-smaller-3j3e
author: marcosomma
date: '2026-04-26'
description: I saw a video today that made me laugh, then made me a bit worried. It was one of those jokes that... Tagged with ai, agents, programming, productivity.
tags: '#ai, #agents, #programming, #productivity'
---

Easier debugging with cognitive pipelines

I saw a video today that made me laugh, then made me a bit worried.

It was one of those jokes that is not really a joke because you can already see some company doing it six months from now. A manager was basically complaining because an employee was not spending enough AI tokens. Not enough tokens. As if tokens were steps on a fitness tracker.

"You only burned 2,000 tokens today, Susan. Are you even working?"

It sounds absurd, but we are not that far from it. Companies are already starting to measure AI adoption through number of prompts, number of tool calls, input tokens, output tokens, cost per user, cost per team, cost per workflow. And to be clear, I do not think this is automatically wrong. Measuring token usage makes sense. Tokens are cost. Tokens are latency. Tokens are context. They are also a trace of how people and systems are using AI.

The problem starts when we confuse the metric with the objective. We did this with hours worked. We did this with tickets closed. We did this with meetings attended. We did this with leads, where 1,000 unqualified leads looked better than 10 serious conversations because the spreadsheet was having a great day and nobody wanted to ruin the mood with reality.

Now we risk doing the same with tokens.

More tokens does not mean better work. Fewer tokens does not mean smarter work. The interesting signal is not the raw number. The interesting signal is the relationship between what you put into the model, what you ask it to do, and what comes out. That is where I think the real token economy starts. Not as a cost saving obsession, but as an architectural signal.

## Tokens are not just money

The first way people talk about tokens is cost, and that is understandable. If you use hosted LLM APIs, tokens map quite directly to money. Input tokens cost something. Output tokens cost something. Larger models cost more. Long contexts cost more. Retries cost more. Bad prompts cost more. Bad architecture costs a lot more, but usually in a way that arrives later and looks like a reliability problem.

So the first instinct is to optimize token consumption. Compress prompts. Summarize context. Pick cheaper models. Cache responses. Reduce unnecessary output. All of that is useful, but I think it is only the shallow layer of the problem.

The more interesting question is not "how many tokens did this task consume?" The more interesting question is "what cognitive operation did those tokens represent?"

Because input tokens and output tokens are not the same thing. Input tokens usually buy context. They are the material you ask the model to look at. Output tokens usually buy generation, explanation, structure, synthesis, or action. If I send 10,000 input tokens to a model and get back 10 output tokens, that could be terrible. It could also be exactly right.

If the task is to read a long error log and return whether the failure is caused by authentication, a tiny output may be valid. If the task is to classify a product review as positive, neutral, or negative, a small answer is not a failure. It is the point. If the task is to route a bug report to the correct engineering queue, I do not need a novel. I need the right route.

So no, high input and low output is not automatically bad. But it is a signal. And I think that signal deserves a lot more attention than it currently gets.

## Balance does not mean symmetry

When I talk about token balance, I do not mean that input tokens and output tokens should be equal. That would be a very silly metric, and we already have enough silly metrics trying to cosplay as management science.

By balance, I mean the relationship between the size of the input, the size of the output, and the value of the decision produced. A large input with a tiny output usually means the model is doing some kind of compression, classification, extraction, routing, filtering, moderation, scoring, validation, or decision making. A small input with a large output usually means the model is doing generation, expansion, explanation, drafting, or ideation. A large input with a large output usually means synthesis, transformation, summarization, comparison, or multi-step reasoning. A small input with a small output is usually a narrow atomic task.

None of these patterns are good or bad by themselves. They tell you something about the shape of the work. And sometimes the shape of the work is screaming.

Imagine you send a giant prompt containing a full meeting transcript, a product description, usage logs, a bug report, five examples, a JSON schema, tone guidelines, safety instructions, and a final line saying "be concise" because apparently we enjoy irony. Then you ask the model to return this:

{

 
"priority"
:
 
"high"

}

Enter fullscreen mode

Exit fullscreen mode

Maybe that is fine. Maybe the classification really required all of that context. But maybe you just built a cognitive washing machine to clean one spoon.

The point is not that the token ratio is wrong. The point is that the ratio invites questions. Did the task need all of that context? Could the context have been retrieved more narrowly? Could the classification have been separated from the extraction? Could a smaller model do part of the work? Could a deterministic rule do part of it? Could the final output be validated separately instead of trusting one giant model call?

That is where token metrics become useful. Not as a scoreboard. As a diagnostic tool.

## The real problem is overloaded cognition

A lot of AI workflows are not expensive because the model is expensive. They are expensive because the task design is confused. We ask one model call to do too many things at once, then we act surprised when the model behaves like a very intelligent intern who received eight contradictory Jira tickets in one message.

Read this long input. Understand the domain. Extract twenty fields. Normalize them. Infer missing values. Respect the schema. Apply business rules. Avoid hallucinations. Explain your decision. Be concise. Be deterministic. Also, please do it in one call because we saw a demo once and now we think architecture is a prompt template.

This is where things become fragile. One big prompt. One big model. One fragile JSON output. One retry loop when it fails. One annoyed engineer staring at a malformed comma at 1:12 AM wondering why they studied data structures.

The problem is not only cost. The problem is that the reasoning surface is too large. Every additional instruction increases the model's degrees of freedom. Every unrelated piece of context adds noise. Every extra output field increases the chance of format drift. Every hidden dependency between fields makes validation harder. And when the output fails, you often do not know why.

Was the context too long? Was the instruction ambiguous? Was the schema too complex? Was the task logically overloaded? Was the model too weak? Was the model too creative? Was Mercury in retrograde? At some point, debugging a giant prompt starts to feel like debugging a dream.

This is why I think the unit of optimization should not be the prompt. The unit of optimization should be the cognitive task.

## Think smaller, not just cheaper

When people hear "token economy", they often think about saving money. I think that is incomplete. The better version is this: design AI workflows so each model call has the smallest reasonable cognitive surface.

Not the smallest prompt. Not the cheapest model. The smallest cognitive surface.

A task has a cognitive surface when it asks the model to consider a certain amount of context, make a certain type of judgment, and produce a certain kind of output. A wide cognitive surface is something like this: read a conversation, infer the user's emotional state, detect all action items, classify the sales opportunity, extract objections, score urgency, summarize the call, generate a follow-up email, and return a perfect JSON object with 28 fields.

That is not one task. That is a small village.

A narrower cognitive task is different. Given this segment of a product feedback thread, identify whether the user mentions pricing as a blocker. Return true or false. Or extract only the next meeting date from this text and return null if absent. Or given these three already extracted signals, choose the priority level from low, medium, or high.

Those tasks have narrower inputs and narrower outputs. They are easier to validate. They are easier to retry. They can often run on smaller models. Some can be replaced by deterministic code. Most importantly, they reduce ambiguity.

This is the part that matters. The best token optimization is not always compression. Sometimes the best token optimization is decomposition.

## The 20 field JSON problem

Let us take a simple example. You have a large input document and you need a structured output with 20 values. The obvious modern AI approach is to send the full document to a model and ask it to extract everything in one JSON object. Add a schema, add "do not hallucinate", add "use null when unknown", maybe add three examples, and hope the model behaves.

Sometimes this works. Sometimes it works very well in the demo. Then production arrives, wearing boots.

The model misses a field. It invents a value. It mixes two fields. It returns invalid JSON. It follows the schema but puts the wrong value in the right place, which is worse because it looks correct. It explains itself inside a field because apparently JSON needed feelings.

So you add more instructions. Then stricter schema language. Then validation. Then retry. Then a stronger model. Then a more expensive model. Then someone says, "Maybe we should fine-tune it." And now your simple extraction pipeline has become a small national infrastructure project.

A different approach is to ask a boring but useful question: are these 20 values actually one cognitive task?

Maybe not. Maybe five fields are direct extraction. Maybe three require classification. Maybe four depend on dates. Maybe two require numerical normalization. Maybe six are only relevant if a previous condition is true. In that case, one big prompt is not simpler. It is only hiding the complexity inside the model call.

You may get a better system by clustering the fields by semantic dependency. For example, direct identifiers can be one batch. Dates and temporal constraints can be another. Risk indicators can be another. Obligations and responsible parties can be another. The final normalized summary can be built only after the previous signals exist.

Each batch can have a smaller prompt, a smaller schema, and a narrower validation rule. Some batches may not need an LLM. Some can use regex, parsers, lookup tables, embeddings, or deterministic checks. Some can use a small local model. Only the genuinely difficult parts need the expensive model.

This is where the cost savings come from, but cost is only one part of the win. You also get better observability. If the final output is wrong, you can inspect which subtask failed. You can measure field-level accuracy. You can retry only the failing part. You can swap models for one stage without touching the rest. You can cache intermediate outputs. You can add deterministic validation at the boundary.

That is a real token economy. Not "use fewer tokens". Spend tokens where cognition is actually needed.

## Smaller prompts reduce variance

I want to be careful with the word deterministic. LLMs are not truly deterministic systems in the classical engineering sense, even when you reduce temperature and constrain output. They are probabilistic systems. But workflow design can make their behavior more stable, more reproducible, and more controllable.

Smaller prompts with narrower objectives usually reduce the degrees of freedom of the model. If the model has one job, a small output space, and a strict schema, there are fewer ways to fail. If the model has twenty jobs, a large input, competing instructions, implicit dependencies, and a complex schema, you should not be surprised when it occasionally decides to express itself like a haunted spreadsheet.

This is why task decomposition can improve consistency. Not because small calls magically make the model deterministic, but because small calls make the system around the model easier to control. The output space is narrower. The validation is simpler. The retry logic is cheaper. The failure modes are easier to classify. The model choice becomes more flexible. The prompts become easier to test.

And the orchestration becomes explicit.

That last point matters a lot. When everything happens inside one prompt, the process is invisible. When you split the work into stages, the process becomes inspectable. This is the difference between hoping the model thinks correctly and designing a system where each step can be observed.

## Where OrKa fits into this

This is one of the reasons I have been buildingOrKa, an orchestration framework for AI agents and reasoning workflows. The point of OrKa is not "use more agents because agents are cool". Honestly, if adding agents makes your system less understandable, congratulations, you have invented distributed confusion.

The point is different. Make cognitive work explicit. Define the flow. Split reasoning into smaller units. Route tasks. Log execution. Validate outputs. Keep memory and context under control. Make the system inspectable instead of praying over a large prompt.

In this view, an LLM is not the application. It is one component inside a system. Sometimes the LLM extracts. Sometimes it classifies. Sometimes it rewrites. Sometimes it evaluates. Sometimes it should not be called at all. The orchestration layer decides how work moves between these pieces.

That is where token economy becomes architecture. You are no longer asking only how to reduce a prompt by 20 percent. You are asking which cognitive step actually needs this context.

That question changes everything. Maybe the first model call only needs the user message. Maybe the second needs the relevant log snippet. Maybe the third needs only three extracted fields. Maybe the final formatter needs no model at all. If you send the full context to every step, you are not designing an AI system. You are photocopying the universe and asking a model to find the invoice number.

It may work. It is not a strategy.

## Token metrics should trigger questions

So how should teams use token metrics? Not as productivity surveillance. Not as a way to shame people for using too many or too few tokens. Not as a leaderboard where the person with the most prompts wins some cursed office trophy.

Token metrics should trigger engineering questions.

When input tokens are very high and output tokens are very low, ask whether the task is intentionally compressive or accidentally overloaded. When output tokens are very high, ask whether the model is generating useful structure or just producing expensive fog. When the same context is repeatedly sent across multiple calls, ask whether retrieval, caching, or state passing could reduce duplication. When a large model is used for simple extraction, ask whether a smaller model or deterministic rule would work. When retries consume a lot of tokens, ask whether the schema, validation, or task boundaries are wrong.

This does not mean splitting tasks is automatically better. If you send the same 10,000 token input twenty times to extract twenty fields, you may have made the system more expensive and slower. You have not built architecture. You have built a very complicated way to duplicate context.

The win comes when decomposition is paired with context narrowing. Extract the relevant segment once. Reuse intermediate state. Cluster fields that share dependencies. Route only the necessary context. Validate locally. Use smaller models where possible. Stop calling the model when code can do the job.

This is not anti-LLM. It is pro-system.

## A simple mental model

Here is the mental model I keep coming back to. Input tokens are attention budget. Output tokens are commitment surface.

The more input you provide, the more the model has to attend to. The more output you request, the more opportunities the model has to drift. A workflow becomes more stable when the attention budget and the commitment surface are aligned with the actual cognitive task.

If the model needs to classify one thing, do not ask it to also summarize, extract, explain, normalize, and format a complex object. If the model needs to generate a long answer, do not overload it with irrelevant context that only increases noise. If the model needs to extract structured fields, do not assume all fields belong in the same call. If the model needs to make a decision, make the decision boundary explicit.

The goal is not minimal tokens. The goal is minimal unnecessary cognition.

That distinction is important. Some tasks deserve many tokens. A long research synthesis may need a lot of context. A technical incident summary may need careful source retention. A product comparison may need long input and long output. A multi-document comparison may be legitimately expensive.

The problem is not spending tokens. The problem is spending tokens without knowing what they are buying.

## This is also a model selection problem

Once you split cognitive tasks, model selection becomes much more interesting. In a one-prompt architecture, you usually choose the strongest model you can afford because the task is messy. The model has to handle everything. It has to read long context, reason, extract, format, validate, and recover from ambiguity.

But if you split the workflow, you can choose models per cognitive step. A small model can do simple classification. A local model can extract obvious fields. A deterministic parser can normalize dates. A rules engine can validate constraints. A stronger model can handle the genuinely ambiguous reasoning.

This is where the economics change. Not because you begged the prompt to be shorter, but because you changed the shape of the work. The expensive model becomes a specialist instead of a landfill.

And yes, I know "landfill" sounds harsh. But many AI systems today are exactly that. They throw all context into one place and hope the biggest model will recycle it into something useful. This works surprisingly often, which is the dangerous part. It works enough to ship a demo. It fails enough to punish you in production.

## Token economy as observability

A mature AI system should not only log the final response. It should log the token shape of the workflow.

Which step consumed the most input? Which step produced the most output? Which step retried the most? Which step had the most schema failures? Which step required the strongest model? Which step could be cached? Which step could be replaced by code? Which step actually improved the final decision?

This is not accounting. This is observability.

You are not only tracking spend. You are tracking cognitive pressure inside the system. A sudden increase in input tokens may mean your retrieval is bringing too much context. A sudden increase in output tokens may mean the model started explaining instead of structuring. A high retry cost may mean your schema is too complex or your prompt is ambiguous. A high token cost on a low-value decision may mean the workflow needs decomposition. A low token cost with poor quality may mean you compressed away necessary context.

Again, the metric is not the answer. The metric is the signal. The engineer still needs judgment, which is very inconvenient. We were promised automation and somehow we still need thinking. Rude.

## The wrong future

The wrong future is easy to imagine. Teams get AI dashboards. Managers see token usage per employee. People are encouraged to "use AI more". Token consumption becomes proof of adoption. Employees learn to generate more prompts because the dashboard rewards activity. Everyone looks productive, costs go up, and quality does not.

Then leadership announces an AI efficiency initiative. Now everyone must reduce token usage. People use smaller prompts. Quality drops. Nobody knows why. Another dashboard is created. A consultant appears. The circle of life continues.

This is what happens when the metric becomes the goal. Token usage by itself tells you almost nothing about quality. A great engineer may use fewer tokens because they decomposed the problem properly. Another great engineer may use more tokens because the task genuinely required context. A bad workflow may use few tokens and produce garbage. A good workflow may use many tokens and produce a high-value decision.

So measuring tokens is not wrong. Judging work by raw token volume is wrong.

## The better future

The better future is more boring, which is usually a good sign in engineering. Teams treat token metrics as workflow diagnostics. They look at input-output patterns. They identify overloaded prompts. They split tasks where it makes sense. They route context more carefully. They use smaller models for smaller cognitive jobs. They validate structured outputs separately. They measure retries, drift, and failure modes.

They do not ask "how much AI did you use?" They ask "where did the AI actually add decision value?"

That is the mindset shift. Tokens are not just a bill. Tokens are a trace of cognitive architecture. They show where a system is bloated. They show where context is duplicated. They show where outputs are too ambitious. They show where models are being used as glue because nobody wanted to design the pipeline. And yes, sometimes they show that the expensive model was actually justified.

That is fine. The goal is not to make everything cheap. The goal is to make the system honest.

## Final thought

I think the next stage of AI engineering will not be about who writes the cleverest prompt. It will be about who designs the clearest cognitive pipeline.

The prompt is not the unit of architecture. The cognitive task is.

Token balance matters because it gives us a way to inspect that task. Not perfectly. Not automatically. Not as a KPI to punish or reward people. But as a signal that says: maybe this workflow is overloaded, maybe this context is too broad, maybe this output is trying to do too much, maybe this model is stronger than necessary, maybe this task should be split, maybe this step should not use an LLM at all.

That is where the real token economy lives. Not in spending fewer tokens, but in spending attention where attention is needed.

If we do that well, the benefits go beyond cost. Lower latency. Smaller models. Cleaner validation. Less format drift. More stable outputs. More inspectable workflows. Systems that are closer to engineering and less close to whispering wishes into a very expensive autocomplete machine.

Which, to be fair, is still fun.

But maybe not the future we should build production systems on.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse