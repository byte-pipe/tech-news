---
title: An opinionated (and mainly correct) guide to naming
url: https://adamtornhill.substack.com/p/an-opinionated-and-mainly-correct
site_name: tldr
content_file: tldr-an-opinionated-and-mainly-correct-guide-to-naming
fetched_at: '2026-06-28T18:00:34.322227'
original_url: https://adamtornhill.substack.com/p/an-opinionated-and-mainly-correct
author: Adam Tornhill
date: '2026-06-28'
description: Naming in software goes way beyond any aesthetics. Good naming minimizes reconstruction work. Here is the style and habits that I've picked up.
tags:
- tldr
---

AI-Readable Code

# An opinionated (and mainly correct) guide to naming

### Naming in software goes way beyond any aesthetics. Good naming minimizes reconstruction work. Here is the style and habits that I've picked up.

Adam Tornhill
Jun 23, 2026
10
3
Share

Today we’re taking on thesecond hardest problemin computer science: naming.

Each time we write code, we face a multitude of micro-decisions. How do we label functions, classes, variables, etc. to get the most out of the code as a communication medium? That is, communication that sharpens our thoughts in the moment, as well as code that supports our future selves and any agent trying to make sense of what’s already there.

As such, naming in software goes way beyond any aesthetics. Good naming minimizes reconstruction work. For both humans and machines.

In this article, I share the style and habits that I’ve picked up. It’s a style that evolved over the years, and shaped by viewing software through the lens of cognitive psychology to support the way we think, reason, and solve problems.

## Why naming matters

Names are cognitive compression mechanisms. Design elements with strong names stretch the amount of information you can hold in your head at once.

Further, when reading unfamiliar code, we try to infer the purpose by building up mental representations. This process is largely driven by the names of classes and functions. The stronger the names, the easier the process.

And this translates into time savings, too. For example: clearer identifier names cut debugging times by19% alone.

AI-assisted development benefits too. Arecent studyinvestigated the structural elements that contribute to LLM code understanding. Improving identifier names consistently yielded the largest returns.

## Optimize function names for calling context

Most naming advice focuses on the declaration site. However, we read call sites far more often than declarations.

Consequently, we should communicate context via names. Let the names combine to build sentences in the calling context:

notify_all(registered_clients, about=the_new_version)

Turning our function calls into sentences has cognitive reasoning benefits: that one sentence servesas a chunk. It becomes an abstraction that allows us to squeeze much more information into our cognitive working memory. That way, reasoning improves.

## Derive names via wishful thinking

Now, let me share a trick that has helped me get this naming right over the years: the beauty ofWishful Thinking. Wishful Thinking in this context is a design tool that I learned about from the uber-classicStructure and Interpretation of Computer Programs. The idea is to write code as if the abstraction already existed. Pretend. Then, once the ideal sentence has taken shape, you go ahead and implement those functions. Naming comes first.

The reward is code that reads close to natural language without becoming verbose. That helps bridging the gap between the problem we’re trying to solve and the solution we express.

Subscribe

## Let domain types liberate your parameter names

A function name is incomplete without its arguments. Yet too much code misses that opportunity.

A common reason for that is the code smellprimitive obsession: representing domain concepts using primitive types. Consider:

public ActionResult ListRss(int languageId) {
...
}
public ActionResult NewsItem(int newsItemId) {
...

While anRSSfeed and aNewsitem are clearly separate domain concepts, the code models both as raw integers. Besides weakening the type system, that code also fails to clarify context and intent. What roles does the news item play? Was it clicked by a reader, or selected to feature on a front page?

Introducing proper domain types lets us solve both problems. When the types capture the domain, they also liberate the variable names. Those names can now be repurposed to communicate context:

public ActionResult ListRss(Language preferredRssFeedLanguage) {
...
}
public ActionResult NewsItem(NewsItem clickedArticle) {
...
}

The types tell us what the arguments are. That frees the parameter names to tell uswhythey’re there.

## Scope determines length

We get told that we should let our variables explain exactly what they do. This naturally leads to longer names. However, like all programming “rules”, the soundness of that advice depends on context. Names don’t carry meaning in isolation. They expand on their surrounding context.

So, variable naming should reflect scope. The smaller the scope, the shorter the variable name. (and vice versa).

As an example, consider the following:

for i, article in enumerate(front_page_articles):
 publish(article)

Animight be perfectly fine in that short, tight loop or in a lambda function. The whole block serves as one logical element, one chunk.

It also follows from the same principle that a one letter name is detrimental in a larger scope such as an instance variable or, shudder, a public API. There you really want to spell it out since the context cannot communicate the purpose of anivariable.

## Naming conventions that detract

At this point, it’s time to look at whatnotto do.

### Drop the I

Every now and then I travel outside my functional programming circle, and have to code in an object-oriented language. My object-oriented code follows the same style as presented here. This causes me to break one of the common “best” practices: the I-prefix added to interface names.

That is, I’d create aChatConnectioninterface rather than anIChatConnection.

The fact that something is an interface is probably the least interesting aspect about that abstraction. I’d even argue that it’s a leaky name. Any user that gets hold of a reference to an instance of that type shouldn’t have to carehowit’s implemented. Is it a concrete class? An abstract one? Or really an interface? Who cares? I don’t. So drop that cognitive distractor, the I-prefix.

### Get rid of the getters

...and the setters.

We’ve probably all seen plenty of code along the lines ofgetCustomer(id), orsetCustomerName(name).

Those prefixes,getandset, rarely add value. Rather, they detract by leading us down the dangerous path of asking rather than telling. (See theTell, don’t Ask principle). The names are procedural in their nature, and attract such code:

customer = get_customer(customer_id)
set_customer_status(customer, SUSPENDED)

The preceding logic is better modelled as:

suspend(a_customer)

And even if we stick to query-like functions, pure renaming makes the code read better:

buyer = customer_for(customer_id)

Disagree? Well, I said it’s an opinionated guide. There’s also a psychology lesson here, so let me throw in themere-exposure principle. The mere-exposure principle says that repeated exposure tends to increase our preference for something. We like what we’re familiar with.

My advice is to continuously question our practices. Are they based on familiarity or reason?

### Avoid the dumpster

One of the most common naming issues I tend to see are generic placeholder names likeUtils,Misc, orHelper.

Names aren’t just passive labels. Just like the getters and setters, these names influence future behavior and perspective. A vague and imprecise name — likeUtils— will attract code of those same qualities.

Each time we feel tempted to create a utility class, it’s an admission that we’re prepared to give up on our design. Resist the temptation, and iterate once more. Somewhere, there’s a domain concept looking to get out and get a proper name.

A vague and imprecise name attracts code of those same qualities.

## Good names reduce reconstruction work

This article reflects stuff I’ve learned over my three decades in software. The goal has always been to let the code communicate as effectively as possible.

That way, we guide future code readers, whether they are fellow humans or, increasingly common, coding agents. Both benefit from explicit intent and rich context. So, give your naming the focus it deserves.

Code for Humans and Machines is a reader-supported publication. To support my work, consider becoming a free or paid subscriber.

Subscribe
10
3
Share