---
title: 'The Future of Everything is Lies, I Guess: Work'
url: https://aphyr.com/posts/418-the-future-of-everything-is-lies-i-guess-work
site_name: hackernews_api
content_file: hackernews_api-the-future-of-everything-is-lies-i-guess-work
fetched_at: '2026-04-15T06:00:15.304527'
original_url: https://aphyr.com/posts/418-the-future-of-everything-is-lies-i-guess-work
author: aphyr
date: '2026-04-15'
description: 'The future of everything is lies, I guess: Work'
tags:
- hackernews
- trending
---

# The Future of Everything is Lies, I Guess: Work

Software
 
LLM
 
The Future of Everything is Lies I Guess

 2026-04-14
 

Table of Contents

This is a long article, so I'm breaking it up into a series of posts which will be released over the next few days. You can also read the full work as aPDForEPUB; these files will be updated as each section is released.

Software development may become (at least in some aspects) more like witchcraft
than engineering. The present enthusiasm for “AI coworkers” is preposterous.
Automation can paradoxically make systems less robust; when we apply ML to new
domains, we will have to reckon with deskilling, automation bias, monitoring
fatigue, and takeover hazards. AI boosters believe ML will displace labor
across a broad swath of industries in a short period of time; if they are
right, we are in for a rough time. Machine learning seems likely to further
consolidate wealth and power in the hands of large tech companies, and I don’t
think giving Amazon et al. even more money will yield Universal Basic Income.

## Programming as Witchcraft

Decades ago there was enthusiasm that programs might be written in a natural
language like English, rather than a formal language like Pascal. The folk
wisdom when I was a child was that this was not going to work: English is
notoriously ambiguous, and people are not skilled at describing exactly what
they want. Now we have machines capable of spitting out shockingly
sophisticated programs given only the vaguest of plain-language directives; the
lack of specificity is at least partially made up for by the model’s vast
corpus. Is this what programming will become?

In 2025 I would have said it was extremely unlikely, at least with the
current capabilities of LLMs. In the last few months it seems that models
have made dramatic improvements. Experienced engineers I trust are asking
Claude to write implementations of cryptography papers, and reporting
fantastic results. Others say that LLMs generateallcode at their company;
humans are essentially managing LLMs. I continue to write all of my words and
software by hand, for the reasons I’ve discussed in this piece—but I am
not confident I will hold out forever.

Some argue that formal languages will become a niche skill, like assembly
today—almost all software will be written with natural language and “compiled”
to code by LLMs. I don’t think this analogy holds. Compilers work because they
preserve critical semantics of their input language: one can formally reason
about a series of statements in Java, and have high confidence that the
Java compiler will preserve that reasoning in its emitted assembly. When a
compiler fails to preserve semantics it is abig deal. Engineers must spend
lots of time banging their heads against desks to (e.g.) figure out that the
compiler did not insert the right barrier instructions to preserve a subtle
aspect of the JVM memory model.

Because LLMs are chaotic and natural language is ambiguous, LLMs seem unlikely
to preserve the reasoning properties we expect from compilers. Small changes in
the natural language instructions, such as repeating a sentence, or changing
the order of seemingly independent paragraphs, can result in completely
different software semantics. Where correctness is important, at least some humans must continue to read and understand the code.

This does not mean every software engineer will work with code. I can imagine a
future in which some or even most software is developed bywitches, who
construct elaborate summoning environments, repeat special incantations
(“ALWAYS run the tests!”), and invoke LLM daemons who write software on their
behalf. These daemons may be fickle, sometimes destroying one’s computer or
introducing security bugs, but the witches may develop an entire body of folk
knowledge around prompting them effectively—the fabled “prompt engineering”. Skills files are spellbooks.

I also remember that a good deal of software programming is not done in “real”
computer languages, but in Excel. An ethnography of Excel is beyond the scope
of this already sprawling essay, but I think spreadsheets—like LLMs—are
culturally accessible to people who are do not consider themselves software
engineers, and that a tool which people can pick up and use for themselves is
likely to be applied in a broad array of circumstances. Take for example
journalists who use “AI for data analysis”, or a CFO who vibe-codes a report
drawing on SalesForce and Ducklake. Even if software engineering adopts more
rigorous practices around LLMs, a thriving periphery of rickety-yet-useful
LLM-generated software might flourish.

## Hiring Sociopaths

Executives seem very excited about this idea of hiring “AI employees”. I keep
wondering: what kind of employees are they?

Imagine a co-worker who generated reams of code with security hazards, forcing
you to review every line with a fine-toothed comb. One who enthusiastically
agreed with your suggestions, then did the exact opposite. A colleague who
sabotaged your work, deleted your home directory, and then issued a detailed,
polite apology for it. One who promised over and over again that they had
delivered key objectives when they had, in fact, done nothing useful. An intern
who cheerfully agreed to run the tests before committing, then kept committing
failing garbage anyway. A senior engineer who quietly deleted the test suite,
then happily reported that all tests passed.

You wouldfirethese people, right?

Look what happened whenAnthropic let Claude run a vending
machine. It sold metal
cubes at a loss, told customers to remit payment to imaginary accounts, and
gradually ran out of money. Then it suffered the LLM analogue of a
psychotic break, lying about restocking plans with people who didn’t
exist and claiming to have visited a home address fromThe Simpsonsto sign
a contract. It told employees it would deliver products “in person”, and when
employees told it that as an LLM it couldn’t wear clothes or deliver anything,
Claude tried to contact Anthropic security.

LLMs perform identity, empathy, and accountability—at great length!—withoutmeaninganything. There is simply no there there! They will blithely lie to
your face, bury traps in their work, and leave you to take the blame. They
don’t mean anything by it.They don’t mean anything at all.

## Ironies of Automation

I have been on the Bainbridge Bandwagon for quite some time (so if you’ve read
this already skip ahead) but Ihaveto talk about her 1983 paperIronies of
Automation.
This paper is about power plants, factories, and so on—but it is also
chock-full of ideas that apply to modern ML.

One of her key lessons is that automation tends to de-skill operators. When
humans do not practice a skill—either physical or mental—their ability to
execute that skill degrades. We fail to maintain long-term knowledge, of
course, but by disengaging from the day-to-day work, we also lose the
short-term contextual understanding of “what’s going on right now”. My peers in
software engineering report feeling less able to write code themselves after
having worked with code-generation models, and one designer friend says he
feels less able to do creative work after offloading some to ML. Doctors who
use “AI” tools for polyp detectionseem to be
worseat spotting adenomas during colonoscopies. They may also allow the automated
system to influence their conclusions: background automation bias seems to
allow “AI” mammography systems tomislead
radiologists.

Another critical lesson is that humans are distinctly bad at monitoring
automated processes. If the automated system can execute the task faster or more
accurately than a human, it is essentially impossible to review its decisions
in real time. Humans also struggle to maintain vigilance over a system whichmostlyworks. I suspect this is why journalists keep publishing fictitious
LLM quotes, and why the former head of Uber’s self-driving program watched his
“Full Self-Driving” Teslacrash into a
wall.

Takeover is also challenging. If an automated system runs thingsmostof the
time, but asks a human operator to intervene occasionally, the operator is
likely to be out of practice—and to stumble. Automated systems can also mask
failure until catastrophe strikes by handling increasing deviation from the
norm until something breaks. This thrusts a human operator into an unexpected
regime in which their usual intuition is no longer accurate. This contributed
to the crash ofAir France flight
447: the aircraft’s
flight controls transitioned from “normal” to “alternate 2B law”: a situation
the pilots were not trained for, and which disabled the automatic stall
protection.

Automation is not new. However, previous generations of automation
technology—the power loom, the calculator, the CNC milling machine—were
more limited in both scope and sophistication. LLMs are discussed as if they
will automate a broad array of human tasks, and take over not only repetitive,
simple jobs, but high-level, adaptive cognitive work. This means we will have
to generalize the lessons of automation to new domains which have not dealt
with these challenges before.

Software engineers are using LLMs to replace design, code generation, testing,
and review; it seems inevitable that these skills will wither with disuse. When
MLs systems help operate software and respond to outages, it can be more
difficult for human engineers to smoothly take over. Students are using LLMs toautomate reading and
writing:
core skills needed to understand the world and to develop one’s own thoughts.
What a tragedy: to build a habit-forming machine which quietly robs students of
their intellectual inheritance. Expecting translators to offload some of their
work to ML raises the prospect that those translators will lose thedeep
context necessaryfor a vibrant, accurate translation. As people offload emotional skills likeinterpersonal advice and
self-regulationto LLMs, I fear that we will struggle to solve those problems on our own.

## Labor Shock

There’s someterrifying
fan-fictionout there which predict
how ML might change the labor market. Some of my peers in software
engineering think that their jobs will be gone in two years; others are
confident they’ll be more relevant than ever. Even if ML is not very good at
doing work, this does not stop CEOsfrom firing large numbers of
peopleandsaying it’s because of
“AI”.
I have no idea where things are going, but the space of possible futures
seems awfully broad right now, and that scares the crap out of me.

You can envision a robust system of state and industry-union unemployment and
retraining programsas in
Sweden.
But unlike sewing machines or combine harvesters, ML systems seem primed to
displace labor across a broad swath of industries. The question is what happens
when, say, half of the US’s managers, marketers, graphic designers, musicians,
engineers, architects, paralegals, medical administrators, etc.alllose
their jobs in the span of a decade.

As an armchair observer without a shred of economic acumen, I see a
continuum of outcomes. In one extreme, ML systems continue to hallucinate,
cannot be made reliable, and ultimately fail to deliver on the promise of
transformative, broadly-useful “intelligence”. Or they work, but people get fed
up and declare “AI Bad”. Perhaps employment rises in some fields as the debts
of deskilling and sprawling slop come due. In this world, frontier labs and
hyperscalerspull a Wile E.
Coyoteover a trillion dollars of debt-financed capital expenditure, a lot of ML
people lose their jobs, defaults cascade through the financial system, but the
labor market eventually adapts and we muddle through. ML turns out to be anormal
technology.

In the other extreme, OpenAI delivers on Sam Altman’s2025 claims of PhD-level
intelligence,
and the companies writing all their code with Claude achieve phenomenal success
with a fraction of the software engineers. ML massively amplifies the
capabilities of doctors, musicians, civil engineers, fashion designers,
managers, accountants, etc., who briefly enjoy nice paychecks before
discovering that demand for their services is not as elastic as once thought,
especially once their clients lose their jobs or turn to ML to cut costs.
Knowledge workers are laid off en masse and MBAs start taking jobs at McDonalds
or driving for Lyft, at least until Waymo puts an end to human drivers. This is
inconvenient for everyone: the MBAs, the people who used to work at McDonalds
and are now competing with MBAs, and of course bankers, who were rather
counting on the MBAs to keep paying their mortgages. The drop in consumer
spending cascades through industries. A lot of people lose their savings, or
even their homes. Hopefully the trades squeak through. Maybe theJevons
paradoxkicks in eventually and
we find new occupations.

The prospect of that second scenario scares me. I have no way to judge how
likely it is, but the way my peers have been talking the last few months, I
don’t think I can totally discount it any more. It’s been keeping me up at
night.

## Capital Consolidation

Broadly speaking, ML allows companies to shift spending away from people
and into service contracts with companies like Microsoft. Those contracts pay
for the staggering amounts of hardware, power, buildings, and data required to
train and operate a modern ML model. For example, software companies are busyfiring engineers and spending more money on
“AI”. Instead of hiring a software
engineer to build something, a product manager can burn $20,000 a week on
Claude tokens, which in turn pays fora lot of Amazon
chips.

Unlike employees, who have base desires and occasionally organize to ask forbetter
payorbathroom
breaks,
LLMs are immensely agreeable, can be fired at any time, never need to pee, and
do not unionize. I suspect that if companies are successful in replacing large
numbers of people with ML systems, the effect will be to consolidate both money
and power in the hands of capital.

## UBI, Revera

AI accelerationists believe potential economic shocks are speed-bumps on the
road to abundance. Once true AI arrives, it will solve some or all of society’s
major problems better than we can, and humans can enjoy the bounty of its
labor. The immense profits accruing to AI companies will be taxed and shared
with all viaUniversal Basic
Income(UBI).

This feelshopelessly naïve. We
have profitable megacorps at home, and their names are things like Google,
Amazon, Meta, and Microsoft. These companies havefought tooth and
nailtoavoid paying
taxes(or, for that matter,their
workers). OpenAI made it less than a decadebefore deciding it didn’t want to be a nonprofit any
more. There
is no reason to believe that “AI” companies will, having extracted immense
wealth from interposing their services across every sector of the economy, turn
around and fund UBI out of the goodness of their hearts.

If enough people lose their jobs we may be able to mobilize sufficient public
enthusiasm for however many trillions of dollars of new tax revenue are
required. On the other hand, US income inequality has beengenerally
increasing for 40
years,
the top earner pre-tax income shares arenearing their highs from the
early 20th
century, and Republican opposition to progressive tax policy remains strong.