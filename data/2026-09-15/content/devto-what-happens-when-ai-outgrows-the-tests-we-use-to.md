---
title: What Happens When AI Outgrows the Tests We Use to Measure It? - DEV Community
url: https://dev.to/hemapriya_kanagala/what-happens-when-ai-outgrows-the-tests-we-use-to-measure-it-30al
site_name: devto
content_file: devto-what-happens-when-ai-outgrows-the-tests-we-use-to
fetched_at: '2026-09-15T15:27:49.293613'
original_url: https://dev.to/hemapriya_kanagala/what-happens-when-ai-outgrows-the-tests-we-use-to-measure-it-30al
author: Hemapriya Kanagala
date: '2026-09-14'
description: TL;DR GPT-6 Astra has started another familiar AI conversation. The model is more capable, Jensen... Tagged with discuss, ai, programming, chatgpt.
tags: '#discuss, #ai, #programming, #chatgpt'
---

Comments warn of inflated benchmark scores

TL;DR

GPT-6 Astra has started another familiar AI conversation. The model is more capable, Jensen Huang said on X that"AGI has arrived,"and social feeds quickly moved between excitement, curiosity, and fear about what comes next.

I understand why the reactions are strong. AI is changing quickly, and some of the things these models can do now would have sounded surprising not long ago. But I have also noticed how quickly"AI is becoming much more capable"can turn into"developers will not be needed"or"CSE is finished."That feels like a much bigger conclusion.

For me, Astra raises another question that is easier to miss:

How do we actually know an AI model is getting better?

We usually look at benchmarks, and they are useful. But benchmarks can age too. Some become saturated, some use proxies for capabilities that are difficult to measure directly, ground truth can be complicated, and evaluation methods can change. A benchmark score also does not automatically tell us how useful a model will be for our own work.

Astra's system card gives several examples of this, including older evaluations becoming saturated or being considered for retirement, newer evaluations using more realistic or experimental data, and evaluation methods changing over time.

That matters for developers too. If AI makes writing code cheaper and faster, software engineering does not suddenly disappear. Requirements, architecture, system design, security, verification, tradeoffs, maintenance, and deciding what should actually be built still matter.

AI will change the work. I think that part is pretty clear.

The more useful question is what we do with that change, and whether we are measuring AI well enough to understand what is actually happening.

## Table of Contents

* Another AI launch, and the conversation gets loud very quickly
* A benchmark gives us a number. What does the number really tell us?
* Every benchmark has a lifespan
* 92% according to what?
* The number can change because the test changed
* One answer is starting to tell us less
* So what should we look at when we see a benchmark?
* What does all of this mean for developers?
* We can take AI seriously without making every headline the final answer
* The models are changing. Our way of looking at them has to change too.
* I Would Love to Hear From You
* References
* 🤝 Let's Stay Connected

## Another AI launch, and the conversation gets loud very quickly

Whenever a major AI model arrives, there seems to be a familiar sequence. The model launches, people try it, benchmark results appear, comparisons start, and then the bigger questions arrive.

With Astra, NVIDIA CEO Jensen Huang also said on X that"AGI has arrived"while congratulating OpenAI on the launch.

As you would expect, people started interpreting that statement in very different ways. Some saw it as a major milestone, some questioned whether Astra actually meets their definition of AGI, and others immediately started thinking about what this could mean for jobs and software development.

From what I have been seeing in my own feed, there is also a lot of fear around where developers fit into all of this.

I am not saying fear is wrong. There are real risks with increasingly capable AI, and I think those risks deserve serious attention.

But I think there is a big difference between saying"this technology is changing quickly"and saying"developers are no longer needed"or"there is no need for CSE anymore."

That feels like a much bigger conclusion to draw from a capability improvement.

Software development will change. There is very little doubt about that. But when producing code becomes easier, other parts of the work can become more important too.

Understanding the problem, designing the system, making architecture decisions, working through requirements, thinking about security and reliability, verifying what was produced, understanding tradeoffs, and knowing when an AI-generated solution is simply the wrong solution are all still part of building software.

None of those become less important just because writing the code becomes faster.

So while everyone is asking how capable the new model is, I started wondering about something slightly different:

How are we actually measuring that capability?

## A benchmark gives us a number. What does the number really tell us?

There is something very convenient about benchmarks. You see Model A at 82% and Model B at 88%, and it suddenly feels like we have a clear answer about which one is better.

And honestly, benchmarks are useful. Without them, comparing AI systems would be much harder. Having a common test gives us a starting point, and that is valuable.

The part that is easy to forget is that a benchmark is ameasurement tool. It gives us evidence about a model's capability, but it is not the capability itself.

Think about a thermometer. It tells you the temperature, but the thermometer is not the temperature. In the same way, a benchmark can tell us something about what a model can do, but it cannot capture everything the model is capable of doing in the real world.

And this becomes more important as models improve, because the test itself can eventually become less informative.

A benchmark that once showed a clear difference between models might eventually have almost every strong model scoring near the top. At that point, the number is still a number, but it may not tell us as much as it used to.

## Every benchmark has a lifespan

One of the things I found interesting in Astra's system card is how openly it talks about evaluations changing over time. Some earlier evaluations have become relatively saturated, some are being considered for retirement, and newer evaluations are being introduced because the older ones may no longer give enough signal.

That actually makes a lot of sense. Imagine a test where the strongest models are now scoring 97%, 98%, and 98%. Those are obviously impressive results, but if most capable models are already close to the ceiling, how much are we really learning from that one percentage point?

The benchmark may not have become bad. It may have simply reached the point where it is no longer good at showing the differences we care about.

In a way, that means the benchmark did its job. It helped us see progress when the models were still further away from the ceiling, and now the models have moved far enough that we need a different way to separate them.

So when I see an evaluation being retired or replaced, I do not necessarily see that as a failure of the benchmark. Sometimes it is actually a sign that the technology has moved forward.

The models moved, so the test needs to move too.

And I think that idea is going to matter more and more as AI systems keep getting better.

## 92% according to what?

This is probably my favorite question to ask when I see a benchmark score.

92% according to what?

For some tasks, the answer is easy. A math problem has a known answer. A programming problem can be checked with tests. A factual question can often be compared against a trusted source.

But things get more complicated when we are evaluating scientific reasoning, biological predictions, or longer tasks where there may not be one obvious correct answer.

That is whereground truthcomes in. In simple terms, ground truth is the answer or evidence we treat as the correct reference when we evaluate a model. Depending on the problem, it might come from experts, experimental data, a simulation, or some other trusted source.

And sometimes we cannot directly measure the capability we care about, so we use aproxy. A proxy is something we can measure that is expected to tell us something about a harder-to-measure capability.

Astra's system card gives an example from biology. One of its evaluations looks atAAV capsid packaging prediction. AAV stands for adeno-associated virus, and a capsid is the protein shell around a virus. In this evaluation, the model is asked to predict how well different capsids may perform in packaging. The result is being used as a proxy for certain broader biological design capabilities.

Using a proxy is not automatically a problem. In many areas, it is simply a practical way to measure something that would otherwise be very difficult or expensive to test directly.

But there is an important difference between saying"the model got better at this prediction"and saying"the model got better at the real-world capability this prediction represents."

Those two things can be connected without being exactly the same.

The system card also discusses a related issue withBPNet, a model used to make biological predictions. If the predictions from the original system contain errors or assumptions, using those predictions as the test's reference can create a strange situation where a future AI system might become better at reproducing those patterns without necessarily becoming better at the underlying biological task we actually care about.

That is a subtle measurement problem, but it is an important one.

The score can be real, the improvement can be real, and we can still have questions about what that improvement actually represents.

This is also why Astra's newer biological evaluations usingunpublished experimental dataandwet-lab-validated evidenceare interesting. Wet-lab validation basically means the results have been checked through actual laboratory experiments rather than relying only on a computational prediction. That gives the evaluation a closer connection to the real-world behavior it is trying to measure.

So when I see a benchmark saying 92%, I am still interested in the number.

I just want to know what is behind it.

92% according to what?

## The number can change because the test changed

There is another part that can easily get lost when we look at benchmark charts:the test itself can change.

A benchmark score does not appear on its own. There is a dataset behind it, instructions for the model, a way of grading the answer, a scoring method, and sometimes specific tools or model settings. If any of those things change, the meaning of the final number can change too.

Astra's system card points this out directly. Policies, graders, datasets, evaluations, and other measurement details can evolve over time, which means older results should generally not be treated as directly comparable to newer ones without looking at what changed.

So when we see something like:

Model A: 90%Model B: 95%

the five-point difference might be meaningful. But before using it to make a big claim about one model being much better than another, it is worth checking whether both numbers came from the same kind of evaluation setup.

There is even a smaller detail that can affect some results:the length of the answer.

In some open-ended evaluations, a longer answer can have more opportunities to satisfy the different things a grader is looking for. That means a model could potentially score better simply because it said more, even when a shorter answer might have been more useful to a person. Astra's system card discusses this issue and reports length-adjusted scores for some evaluations to account for it.

It may sound like a small technical detail, but these are exactly the kinds of details that matter when we are trying to understand what a benchmark score is really telling us.

The number is important.

But the way we arrived at the number matters too.

## One answer is starting to tell us less

There is also a change happening in how we actually use AI. We are not only asking a question and waiting for an answer anymore. AI systems can work through multi-step tasks, use tools, interact with software, deal with incomplete instructions, and adjust when the requirements change.

Astra's launch material talks about this kind of behavior too. It describes the model handling ambiguity better, asking focused questions when an answer could change the outcome, and continuing with other work while waiting for a response. When the decision is more consequential, it can wait for the user's input instead of simply guessing.

That kind of behavior is difficult to capture with one isolated question.

If I am asking an AI system to help with a 30-minute workflow, I probably care about much more than whether it got one answer right. Did it understand what I was actually trying to do? Did it make reasonable decisions along the way? Did it handle a requirement that changed halfway through? If something went wrong, could it recover? And at the end, did the result actually work?

The Astra system card also includes more realistic workplace-style evaluations involving computer and browser tasks, ambiguous instructions, and complex permissions.

That feels closer to how many of us experience AI now.

A model can be excellent at answering individual questions and still struggle when it has to carry a task from beginning to end. The opposite can also happen. A system may not look extraordinary on one isolated benchmark but perform surprisingly well when given the tools and context it needs.

That is why I think the evaluation question is slowly changing too.

Instead of only asking"Did the model get the answer right?", we may also need to ask"How well did it handle the whole task?"

And that is a much harder thing to measure.

## So what should we look at when we see a benchmark?

I do not think we need to become experts in evaluation methodology every time a new model launches. But there are a few questions that can make a benchmark score much easier to understand.

### 1. What is actually being measured?

Is the benchmark measuring the capability we care about, or is it using aproxy, something that is expected to tell us about that capability?

### 2. Is the benchmark still difficult?

If most strong models are already close to the top score, the benchmark may have becomesaturated, meaning it is no longer giving us much room to see meaningful differences between models.

### 3. Where does the ground truth come from?

What are we treating as the correct answer? Is it a fixed answer, expert judgment, another model, a simulation, or real-world evidence?

### 4. Did the evaluation change?

Did the dataset, grader, scoring method, prompts, tools, or model setup change? Even small changes can affect how we should interpret the final number.

### 5. Does the result transfer to the work I actually care about?

This one is especially useful if you are a developer. A model can perform extremely well on a general coding benchmark and still not be the best model for your actual codebase, team, or workflow.

For that, your own small evaluation can be surprisingly useful.

Take 20 or 30 real tasks from your workflow and try the models on them. Then look at the things that actually matter to you. Did the code work? Did the model understand the requirements? How did it handle changes? How much did you have to correct? Could it recover when something went wrong? How long did it take, and what did it cost?

You do not need to throw away the big benchmark scores. They can still give you a useful general picture.

Your own tasks simply add another piece of evidence, and sometimes that is the piece that matters most.

## What does all of this mean for developers?

This is where the benchmark discussion connects back to something I have been seeing a lot around Astra:"AI will replace developers."

I can understand why people are asking that question. If a model can write code, understand a codebase, use tools, work through a task, and handle changes along the way, it is reasonable to wonder what software development will look like a few years from now.

I do expect the work to change. Some things will become much faster, some tasks may need less human effort, and there will probably be skills that become less important as the tools improve. At the same time, other skills can become more important.

If producing code becomes much easier, for example, the difficult part may move toward understandingwhat should actually be built and how it should be built.

What are the real requirements? What constraints do we have? How should the system be designed? Will the architecture hold when the system grows? Is the solution secure and reliable? How do we verify what the AI produced? What happens when the requirements change six months from now? And does the whole thing actually solve the user's problem?

These questions do not disappear because an AI can produce hundreds of lines of code quickly.

In some cases, they may become even more important because producing several possible implementations becomes easier. Someone still has to understand the options and decide which one makes sense for the situation.

That is why the idea that"CSE is no longer needed"feels too extreme to me. Computer science and software engineering have always been about more than writing code. Code is one part of building software, not the entire process.

There will definitely be changes, and some of those changes may be significant. But I would rather watch how the work actually evolves than decide too early that the whole field is going away.

Maybe the more useful question for developers is not"Will AI replace me?", but"As AI takes over more of the work, what should I become better at?"

## We can take AI seriously without making every headline the final answer

I do not want to dismiss the concerns around AI. There are genuine questions around safety, misuse, security, reliability, employment, and how much autonomy we should give these systems. Those are not small questions, and they deserve serious attention as the technology becomes more capable.

At the same time, I do not think every capability improvement needs to turn into a prediction about the end of a profession. When I see that AI can write code, I see a technology that is changing software development. I do not think the only possible conclusion is that developers are finished.

The same goes for increasingly complex AI systems. Instead of jumping straight to whether humans will be needed, I find it more useful to ask which parts of the work we can trust AI with, where we still need people involved, and what kind of oversight makes sense.

And when I see a benchmark score go up, I want to understand what is behind that number too. What was tested? How was it tested? Is the benchmark still giving us a useful signal? Does that improvement show up in the kind of work people actually do?

For me, that makes the conversation more interesting. We can be excited about what these models are doing and still question the claims around them. We can take the risks seriously without assuming the most extreme outcome, and we can recognize real progress without treating every new headline as the final answer.

There is probably a lot we still do not know about where all of this is going.

And that is okay. We are watching it change in real time.

## The models are changing. Our way of looking at them has to change too.

That is probably what I keep coming back to with Astra. The model is becoming more capable, but at the same time, measuring that capability is getting more complicated. Benchmarks can saturate, proxies have limits, ground truth is not always simple, and evaluation methods have to keep evolving too.

Maybe our questions need to evolve along with them.

Instead of only asking"Will AI replace developers?", we can ask"Which parts of development are changing, and what skills are becoming more valuable?"

Instead of"Is CSE dead?", we can ask"What does computer science look like when producing code becomes much easier?"

And instead of only asking"Is AGI here?", we can ask"What capabilities are we actually talking about, how are we measuring them, and what evidence do we have?"

We are going to keep seeing stronger models, impressive demos, and very strong opinions around them. Some predictions will probably turn out to be right, some will go too far, and some things will surprise all of us.

That is part of watching a technology change this quickly.

For me, the useful thing is to stay curious, look at the evidence, take the risks seriously, and also pay attention to what is actually changing in the work we do.

Because after all the benchmarks, headlines, and predictions, maybe the question worth asking is simply:

"What changed, how do we know, and what does that mean for the work we care about?"

And then:

"Okay. This is what the technology can do now. What should we build with it?"

## I Would Love to Hear From You

We are all watching the same AI developments, but we do not always see them in the same way.

Maybe you think the current progress is being underestimated. Maybe you think some of the excitement or fear is going too far. Or maybe you are already seeing changes in your own development work that I have not noticed.

I would love to hear your perspective.

What do you think?

If you have a different way of looking at AI benchmarks, model evaluations, or where software development is heading, share it in the comments. We all come from different experiences, and I think that is where these conversations become much more interesting.

## References

* OpenAI GPT-6 Astra System Card
* OpenAI GPT-6 Astra launch announcement
* Jensen Huang's post on X about AGI

These are the main references behind the benchmark, evaluation, and capability points discussed in the article.

## 🤝 Let's Stay Connected

Place

Find me here

GitHub

building things → 
hemapriya-kanagala

LinkedIn

resources & updates → 
hemapriya-kanagala

X

random dev thoughts → 
@KanagalaHema

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (26 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse