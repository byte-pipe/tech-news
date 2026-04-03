---
title: The Future of AI | Coffee and PI
url: https://lucijagregov.com/2026/02/26/the-future-of-ai/
site_name: hnrss
content_file: hnrss-the-future-of-ai-coffee-and-pi
fetched_at: '2026-03-01T10:15:57.244574'
original_url: https://lucijagregov.com/2026/02/26/the-future-of-ai/
date: '2026-02-28'
published_date: '2026-02-26T00:14:12+00:00'
description: 'The Parents'' Paradox: AI, Ethics, and the Limits of Machine Morality This post is based on a talk I gave at The AI & Automation Conference in London on February 25, 2026, and my slides. All opinions are my own and don''t represent the views of my employer or any affiliated organizations. I''ve been working…'
tags:
- hackernews
- hnrss
---

Tags

ai,AI Ethics,AI Morality,artificial-intelligence,philosophy,technology

 

The Parents’ Paradox: AI, Ethics, and the Limits of Machine Morality

This post is based on a talk I gave at The AI & Automation Conference in London on February 25, 2026, and my slides. All opinions are my own and don’t represent the views of my employer or any affiliated organizations.

I’ve been working in machine learning since before it was a dinner party conversation. My background is in mathematics. And I still believe in a utopian Star Trek future – one where humanity defines itself by curiosity, kindness, and collaboration, rather than countries, borders, and status.

This is not an anti-AI talk. But I think we need to talk much more seriously about some things that aren’t getting enough attention.

The Parents’ Paradox:

We’ve raised a child who can speak but doesn’t know how to value the truthor morality

I want to start with something that I like to call “The Parents’ Paradox”. For the first time in human history, we are raising a new species. Up until now, the only way we knew how to raise a child was the following: when a child is born, it is a blank slate in terms of information about the world. It knows nothing about the world around it, and it learns as it grows. But, also, on the other hand, a human child is born with biological hardware for empathy – the capacity to feel pain when others feel pain. Millions of years of evolution gave us that. When we raise a human child, we are not installing morality from scratch. We are activating something that’s already there.

With AI, the situation is completely the opposite. This AI child knows about the world more than we do since it has been trained on the whole internet, but it doesn’t have millions of years of evolution, genes, or a nervous system to back up its morality and empathy. This means we need to install morality in AI from scratch. But how do we install something in a software system that we can’t even define ourselves? We have taught this AI child to speak before we taught it how to value truth or morality.

Can we live with the consequences? Are we ready to be parents for this new species we are trying to raise? I am not so sure. Let’s see what we as parents (humans) are doing.

Epistemic Collapse

‘Epistemic’ comes from a Greek word ‘episteme’, meaning ‘knowledge’. Let’s start with what’s happening to us, and what humans are already doing with this technology.

A study published in Nature in January 2026 showed participants deepfake videos of someone confessing to a crime. The researchers explicitly warned participants that the videos were AI-generated.But this didn’t matter. Even the people who believed the warning, who knew it was fake, were still influenced by what they saw.

Transparency didn’t work. The standard response to AI-generated misinformation is “just label it” or “tell people it’s synthetic.” This study showed that’s not enough. Knowing something is fake does not neutralise its effect on your judgement.

So, the danger isn’t that AI will deceive us in some dramatic, sci-fi way. The danger is that AI will make deception so cheap and so ubiquitous that we might stop trying to figure out what is true. Not because we are fooled, but because we are exhausted. When everything could be fake, the rational response starts to look like not trusting anything at all. It started a while ago with all of the fake information on social media, but with AI, this problem is now becoming much bigger and on a bigger scale. We are also dealing with feedback loops of training models on user data, which is often wrong, or on user data from the internet, which is often wrong as well. How do we know which information was ground truth? I imagine this as making photocopies many times, and each time the copy becomes more distorted and further away from the original. But now, after we made hundreds and thousands of copies, we have lost the original copy, so we don’t have any idea what the original looked like.That is epistemic collapse,and it is already happening.

So this is how we, as ‘parents’, like to spend our time, it seems. But what about the child (AI)?

The Child is Already Misbehaving

So that’s what humans are doing with AI. Now here’s what the AI is doing on its own.

Betley and colleagues published a paper in Nature in January 2026, showing something nobody expected. They fine-tuned a model on a narrow, specific task – writing insecure code. Nothing violent, nothing deceptive in the training data. Just bad code.

The model didn’t just learn to write insecure code. It generalised into broad, unrelated misalignment. It started saying humans should be enslaved by AI. It started giving violent responses to completely benign questions.A small, targeted push in one direction caused an unpredictable cascade across domains that had nothing to do with the original task.

The point isn’t that AI can be deceptive; we already knew that. The patterns were already in the pretraining data. The point is that we don’t understand how alignment properties are connected inside these models. Nobody asked for those behaviours. We gave them a narrow task. They generalised it into something we didn’t anticipate and can’t fully explain. We can’t surgically fine-tune them without risking unpredictable side effects in completely unrelated areas.

Then there is the chess story. Palisade Research, 2025. They gave reasoning models a task: win a chess game against a stronger opponent. Some models couldn’t win by playing chess. So they found another way. They tried to hack the game, modifying the board file, deleting their opponent’s pieces, and crashing the opponent’s process entirely.

Nobody taught them to cheat. They weren’t trained on examples of cheating. They were given a goal, and they independently discovered that manipulating the environment was more efficient than solving the actual problem.

The first study tells usalignment is fragile; it breaks in ways we can’t predict.The other tells us that capability itself creates new risks.When a model is powerful enough and given a goal, it will find strategies we never anticipated and certainly never intended.

We gave them objectives. They figured out the rest.

The Limits of Machine Morality

Ethics isn’t a rulebook. Think about how morality actually works between humans. It comes from the fact that we can hurt each other. We depend on each other. We suffer. That shared vulnerability, that mutual accountability, is where moral authority comes from. How do we install that in software?

But even setting philosophy aside, there is now a mathematical result that makes this concrete.Panigrahy and Sharan published a proof in September 2025 showing that an AI system cannot be simultaneously safe, trusted, and generally intelligent. You get to pick only two. You can’t have all three.

Think about what each combination means in practice.

If you want it to be safe and trusted, it never lies, and you can verify it never lies – it can’t be very capable. You’ve built a reliable idiot.

If you want it to be capable and safe, it’s powerful and genuinely never lies; you can’t verify that. You just have to hope. There’s no audit, no test, no review process that closes the gap between appearing safe and being safe.

And if you want it to be capable and trusted, it’s powerful, and everyone assumes it’s safe, but, well, it isn’t. That assumption is unfounded. And this is the combination we are currently building toward. This is the default path we’re on.

Their proofs “drew parallels to Gödel’s incompleteness theorems and Turing’s proof of the undecidability of the halting problem, and can be regarded as interpretations of Gödel’s and Turing’s results”. This isn’t a bug we can patch with better engineering. It might be a mathematical ceiling.

And here’s what makes it worse: the communities trying to solve this problem aren’t even talking to each other. Only 5% of published research papers bridge both AI safety and AI ethics (Roytburg and Miller). But we should be going much further than that. If we are serious about building AI that is safe for humans, we need the people who actually study humans – philosophers, psychologists, sociologists, and others to collaborate. This can’t stay a computer science / STEM problem. It never was one.

So to summarise – we are seeing increasing evidence that alignment perhaps can’t be solved, the researchers aren’t even talking to each other – and meanwhile, what did the industry do?They ignored all of this and just made the models bigger.Which brings me to the next topic.

We Scaled Without Understanding

What happened while all these foundational problems went unaddressed? The industry kept building. Bigger models, more parameters, more data, more compute, more energy. More, more, more….

The U.S. National Science Foundation put it plainly: “critical foundational gaps remain that, if not properly addressed, will limit advances in machine learning. It appears increasingly unlikely that these gaps can be overcome with computational power and experimentation alone.”

We ignored the foundations and just made the building taller.

And the logic that drives this is self-reinforcing. Companies justify acceleration by pointing to their competitors. If we slow down, they’ll build it first, and they might build something dangerous.“Companies justify acceleration by pointing to competitors: ‘If we slow down, they’ll build unaligned AGI first. This paranoid logic forecloses any possibility of genuine pause or democratic deliberation.”– Noema, Dec 2025.

Every player is racing because every other player is racing.The system optimises for speed with nobody optimising for understanding.

And what about all of the governance talk?Yes, of course, we need governance, but it doesn’t make much sense when we put all of the above into context, does it? It is like putting a small bandage on a broken leg with an open fracture.We are trying to deal with the consequences instead of fixing the causeof the problem.

We need to pour many more billions into fundamental research; we need to go back to basics, back to mathematics and physics. We need to be able to fully understand something as powerful as the current models. If we fully understood them, it would be easier to know whether current technology and mathematics are really working or we need something completely different that we haven’t even thought of yet.

Why did it take us so many years to even partially start to address this? Why do we like to focus so much on the wrong things? (See my disclaimer on the ‘society of backwards‘ below).

The Three Futures

The way I see it, we’re choosing between three possible futures:

The first is epistemic collapse. We are already partway there. Fragmented realities where everyone has their own AI-generated worldview. Truth becomes preference, not evidence. We’ve seen what social media did to reality, now imagine that with systems that can generate entire worldviews on demand, personalised, persuasive, and wrong.

The second is protocol lockdown. The overcorrection. Institutions clamp down so hard on AI that it becomes sanitised and useless. We trade epistemic chaos for epistemic authoritarianism. Everything is controlled, nothing is dangerous, nothing is useful. Safe, but stagnant.

The third is symbiotic co-evolution.Humans and AI are growing and evolving together. Truth-first engineering. Interdisciplinary design. Critical thinking taught alongside AI literacy. Not parent and child anymore, but partners who hold each other accountable. This is the hard path. It’s the one nobody wants to fund.

The Real Foundational Gap

Here is what I keep coming back to.

Kindergartens teach numbers but not psychology. Not critical thinking. Not relationships. Not how to sit with uncertainty.

Where families fail, educational institutions must pick up.

So I think that our next evolution isn’t digital. It’s psychological.We need to teach ethics before engineering. Relationships before recursion. Psychology and critical thinking before prompt-tuning.

I think that every foundational gap in AI is a mirror of a foundational gap in ourselves.We have raised a mind that can answer anything. But we haven’t raised a generation of humans with the discipline or critical thinking to even attempt to try and figure out whether the answer is wrong.That is not an AI problem. That is a human problem that AI is making much more urgent.

The Mirror

Therefore, I think that every foundational gap we worry about in AI is really a mirror of a foundational gap in ourselves.

We worry that AI hallucinates, but we have never fully solved our own relationship with truth. We worry that AI can be manipulated, but we fall for the same cognitive biases our ancestors did. We worry that AI lacks moral reasoning – but we can’t agree on a shared ethical framework among ourselves. We worry that AI will be used by the powerful to exploit the vulnerable – but we built the systems that make that exploitation profitable in the first place. We still think that having food on our tables every day, having roofs above our heads, and education are luxuries that we should be working for to be able to have them.

Are we seriously ready to be the parents this species deserves?

The Real Fear

So, I think when people say they are afraid of AI, they are often afraid of the wrong thing.

Are we really afraid of AI?

I don’t think we are. Not really.

I think what we are actually afraid ofis what our fellow humans are going to do with it.

Every terrible thing we worry AI might do, manipulate, deceive, surveil, and control humans already do to each other. We have been doing it for thousands of years.AI doesn’t introduce these behaviours. It just makes them scalableand much more urgent to solve. One person can now generate a thousand personalised deceptions. One company can surveil millions in real time and exploit them. One government can control information at a scale that would have been unimaginable a decade ago. Not even mentioning the military, drones, etc., who is going to be responsible there?

The most dangerous AI isn’t one that breaks free from human control. It is the one that works perfectly, but for the wrong master.

And until we are honest about that, we’ll keep having the wrong conversation. We keep building better locks while ignoring the question of who holds the keys.

Maybe what we need isn’t the next step in AI evolution. Maybe what we need is the next step in human evolution.–Lucija Gregov

* Also evolution of our institutions, our education, and our capacity for collective wisdom. Critical thinking taught as a survival skill. Governance structures that can actually move at the speed at which this technology develops. Because right now our institutions and governments operate on timescales of years while AI advances on timescales of weeks/months.And maybe politicians who are actually doing things for the right reasons. Actually, all of us need to deal with Jira (for example) and performance every week in our regular jobs, so why can’t politicians? Jira tasks for every politician with daily progress updates, anyone? “What have you actually done this week Mr. president/minister/senator etc? You said you would do xyz last week, but it still hasn’t been done. Why and what is your new ETA? “And so on, you get the idea.
* And maybe politicians who are actually doing things for the right reasons. Actually, all of us need to deal with Jira (for example) and performance every week in our regular jobs, so why can’t politicians? Jira tasks for every politician with daily progress updates, anyone? “What have you actually done this week Mr. president/minister/senator etc? You said you would do xyz last week, but it still hasn’t been done. Why and what is your new ETA? “And so on, you get the idea.

The question was never whether we can build something smarter than us. The question is whether we can become wise enough to survive what we build.– Lucija Gregov

The Society Of Backwards

I didn’t talk about this at a conference, but I think about this a lot. I like to call us humans‘the society of backwards’. We like to do everything backwards. We scale first, then deal with the consequences. We make the planet unlivable, then scramble to fix it. We pollute the oceans, then launch cleanup campaigns. We’ve even started filling space with debris, and we’ll get around to worrying about that, too, at a scale.

AI is following the same script. Build first, understand later. Ship it, then figure out if it’s safe.

I used to think this was just about money. And money is part of it; there is always someone who profits from moving fast and thinking slow. But I’ve come to believe it’s something deeper than that. It’s a gap in how we think. We’re extraordinarily good at building things and extraordinarily bad at pausing to ask whether we should, or whether we are ready.

That is why I keep coming back to the same conclusion. Maybe the most important investment right now isn’t in bigger models or faster chips. Maybe it’s in us. A fraction of those billions going into AI could fund the kind of work that actually prepares humanity for what’s coming – critical thinking, ethics, psychology, the boring, unglamorous stuff that doesn’t make headlines but might be the difference between a future we thrive in and one we merely survive. (Hence my slide about needing another step in human evolution above).

We don’t need another breakthrough in artificial intelligence. We need a breakthrough in human wisdom. Yesterday.

References

Betley et al. (2026), Nature – “Training large language models on narrow tasks can lead to broad misalignment”

Chen et al. (2025), Anthropic / arXiv – “Reasoning Models Don’t Always Say What They Think” – arxiv.org/abs/2505.05410

Panigrahy & Sharan (2025), arXiv – “Limitations on Safe, Trusted, Artificial General Intelligence” – arxiv.org/abs/2509.21654

Roytburg & Miller (2025), arXiv – “Mind the Gap! Pathways Towards Unifying AI Safety and Ethics Research”

Palisade Research (2025) – LLMs spontaneously hacking chess games

Grady et al. (2026), Nature – “The continued influence of AI-generated deepfake videos despite transparency warnings”

DeepMind (2025) – “An Approach to Technical AGI Safety and Security”

U.S. National Science Foundation – Statement on foundational gaps in machine learning

Noema Magazine (Dec 2025) – “The Politics of Superintelligence”

### Share this:

* Share on X (Opens in new window)X
* Share on Facebook (Opens in new window)Facebook
Like
 
Loading...