---
title: XML is a Cheap DSL
url: https://unplannedobsolescence.com/blog/xml-cheap-dsl/
site_name: hackernews_api
content_file: hackernews_api-xml-is-a-cheap-dsl
fetched_at: '2026-03-15T06:00:14.867783'
original_url: https://unplannedobsolescence.com/blog/xml-cheap-dsl/
author: y1n0
date: '2026-03-14'
description: Lessons about XML from the open source IRS Tax Withholding Estimator.
tags:
- hackernews
- trending
---

XML is a Cheap DSL

# XML is a Cheap DSL

March 13, 2026

Yesterday, the IRSannounced the releaseof the project I’ve been engineering leading since this summer, its newTax Withholding Estimator(TWE).
Taxpayers enter in their income, expected deductions, and other relevant info to estimate what they’ll owe in taxes at the end of the year, and adjust the withholdings on their paycheck.
It’s free, open source, and, in a major first for the IRS,open for public contributions.

TWE is full of exciting learnings about the field of public sector software. Being me, I’m going to start by writing about by far the driest one: XML.

(I am writing this in my personal capacity, based on the open source release, not in my position as a federal employee.)

XML is widely considered clunky at best, obsolete at worst.
It evokes memories of SOAP configs and J2EE (it’s fine, even good, if those acronyms don’t mean anything to you).
My experience with the Tax Withholding Estimator, however, has taught me that XML absolutely has a place in modern software development, and it should be considered a leading option for any cross-platform declarative specification.

## The Fact Graph

TWE is a static site generated fromtwoXML configurations.
The first of these configs is the Fact Dictionary, our representation of the US Tax Code; the second will be the subject of a later blog post.

We use the Fact Graph, a logic engine, to calculate the taxpayer’s tax obligations (and their withholdings) based on the facts defined in the Fact Dictionary.
The Fact Graph was originally built forIRS Direct Fileand now we use it for TWE.
I’m going to introduce you to the Fact Graph the way that I was introduced to it: byfireexample.

Put aside any preconceptions you might have about XML for a moment and ask yourself what this fact describes, and how well it describes it.

<
Fact
 path
="
/totalOwed
">

 <
Derived
>

 <
Subtract
>

 <
Minuend
>

 <
Dependency
 path
="
/totalTax
"/>

 </
Minuend
>

 <
Subtrahends
>

 <
Dependency
 path
="
/totalPayments
"/>

 </
Subtrahends
>

 </
Subtract
>

 </
Derived
>

</
Fact
>

This fact describes a/totalOwedfact that’s derived by subtracting/totalPaymentsfrom/totalTax.
In tax terms, this fact describes the amount you will need to pay the IRS at the end of the year.
That amount, “total owed,” is the difference between the total taxes due for your income (“total tax”) and the amount you’ve already paid (“total payments”).

My initial reaction to this was that it’s quite verbose, but also reasonably clear.
That’s more or less how I still feel.

You only need to look at a few of these to intuit the structure.
Take the refundable credits calculation, for example.
A refundable credit is a tax credit that can lead to a negative tax balance—if you qualify for more refundable credits than you owe in taxes, the government just gives you some money.
TWE calculates the total value of refundable credits by adding up the values of the Earned Income Credit, the Child Tax Credit (CTC), American Opportunity Credit, the refundable portion of the Adoption Credit, and some other stuff from the Schedule 3.

<
Fact
 path
="
/totalRefundableCredits
">

 <
Description
>

 Form 1040 Line 32. Schedule 3 Line 15 + EITC,ACTC, AOTC,

 refundable portion of Adoption

 </
Description
>

 <
Derived
>

 <
Add
>

 <
Dependency
 path
="
/earnedIncomeCredit
"/>

 <
Dependency
 path
="
/additionalCtc
"/>

 <
Dependency
 path
="
/americanOpportunityCredit
"/>

 <
Dependency
 path
="
/adoptionCreditRefundable
"/>

 <
Dependency
 path
="
/schedule3OtherPaymentsAndRefundableCreditsTotal
"/>

 </
Add
>

 </
Derived
>

</
Fact
>

By contrast, non-refundable tax credits can bring your tax burden down to zero, but won’t ever make it negative.
TWE models that by subtracting non-refundable credits from the tentative tax burden while making sure it can’t go below zero,
using the<GreaterOf>operator.

<
Fact
 path
="
/tentativeTaxNetNonRefundableCredits
">

 <
Description
>

 Total tentative tax after applying non-refundable credits, but before

 applying refundable credits.

 </
Description
>

 <
Derived
>

 <
GreaterOf
>

 <
Dollar
>0</
Dollar
>

 <
Subtract
>

 <
Minuend
>

 <
Dependency
 path
="
/totalTentativeTax
"/>

 </
Minuend
>

 <
Subtrahends
>

 <
Dependency
 path
="
/totalNonRefundableCredits
"/>

 </
Subtrahends
>

 </
Subtract
>

 </
GreaterOf
>

 </
Derived
>

</
Fact
>

While admittedlyveryverbose, the nesting is straightforward to follow.
The tax after non-refundable credits is derived by saying “give me the greater of these two numbers: zero, or the difference between tentative tax and the non-refundable credits.”

Finally, what about inputs?
Obviously we need places for the taxpayer to provide information, so that we can calculate all the other values.

<
Fact
 path
="
/totalEstimatedTaxesPaid
">

 <
Writable
>

 <
Dollar
/>

 </
Writable
>

</
Fact
>

Okay, so instead of<Derived>we use<Writable>.
Because the value is… writable.
Fair enough.
The<Dollar/>denotes what type of value this fact takes.
True-or-false questions use<Boolean/>, like this one that records whether the taxpayer is 65 or older.

<
Fact
 path
="
/primaryFilerAge65OrOlder
">

 <
Writable
>

 <
Boolean
/>

 </
Writable
>

</
Fact
>

There are some (much) longer facts, but these are a fair representation of what the median fact looks like.
Facts depend on other facts, sometimes derived and sometimes writable, and they all add up to some final tax numbers at the end.
But why encode math this way when it seems far clunkier than traditional notation?

## Tax logic needs a declarative specification

Countless mainstream programming languages would instead let you write this calculation in a notation that looks more like normal math.
Take this JavaScript example, which looks like elementary algebra:

const
 totalOwed = totalTax - totalPayments

That seems better!
It’s far more concise, easier to read, and doesn’t make you explicitly label the “minuend” and “subtrahend.”

Let’s add in the definitions fortotalTaxandtotalPayments.

const
 totalTax = tentativeTaxNetNonRefundableCredits + totalOtherTaxes

const
 totalPayments = totalEstimatedTaxesPaid +

 totalTaxesPaidOnSocialSecurityIncome +

 totalRefundableCredits

const
 totalOwed = totalTax - totalPayments

Still not too bad.
Total tax is calculated by adding the tax after non-refundable credits (discussed earlier) to whatever’s in “other taxes.”
Total payments is the sum of estimated taxes you’ve already paid, taxes you’ve paid on social security, and any refundable credits.

The problem with the JavaScript representation is that it’simperative.
It describes actions you take in a sequence, and once the sequence is done, the intermediate steps are lost.
The issues with this get more obvious when you go another level deeper, adding the definitions of all the values thattotalTaxandtotalPaymentsdepend on.

// Total tax calculation

const
 totalOtherTaxes = selfEmploymentTax + additionalMedicareTax + netInvestmentIncomeTax

const
 tentativeTaxNetNonRefundableCredits = Math.
max
(totalTentativeTax - totalNonRefundableCredits,
 0
)

const
 totalTax = tentativeTaxNetNonRefundableCredits + totalOtherTaxes

// Total payments calculation

const
 totalEstimatedTaxesPaid =
 getInput
()

const
 totalTaxesPaidOnSocialSecurityIncome = socialSecuritySources

 .
map
(
source
 =>
 source.totalTaxesPaid)

 .
reduce
((
acc
,
 val
)
 =>
 {
 return
 acc+val },
 0
)

const
 totalRefundableCredits = earnedIncomeCredit +

 additionalCtc +

 americanOpportunityCredit +

 adoptionCreditRefundable +

 schedule3OtherPaymentsAndRefundableCreditsTotal

const
 totalPayments = totalEstimatedTaxesPaid +

 totalTaxesPaidOnSocialSecurityIncome +

 totalRefundableCredits

// Total owed

const
 totalOwed = totalTax - totalPayments

We are quickly arriving at a situation that has a lot of subtle problems.

One problem is the execution order.
The hypotheticalgetInput()function solicits an answer from the taxpayer, which has to happen before the program can continue.
Calculations that don’t depend on knowing “total estimated taxes” are still held up waiting for the user;
calculations thatdodepend on knowing that value had better be specified after it.

Or, take a close look at how we add up all the social security income:

const
 totalTaxesPaidOnSocialSecurityIncome = socialSecuritySources

 .
map
(
source
 =>
 source.totalTaxesPaid)

 .
reduce
((
acc
,
 val
)
 =>
 {
 return
 acc+val },
 0
)

All of a sudden we are really in the weeds with JavaScript.
These are not complicated code concepts—map and reduce are both in the standard library and basic functional paradigms are widespread these days—but they are not tax math concepts.
Instead, they are implementation details.

Compare it to the Fact representation of that same value.

<
Fact
 path
="
/totalTaxesPaidOnSocialSecurityIncome
">

 <
Derived
>

 <
CollectionSum
>

 <
Dependency
 path
="
/socialSecuritySources/*/totalFederalTaxesPaid
"/>

 </
CollectionSum
>

 </
Derived
>

</
Fact
>

This isn’t perfect—the*that represents each social security source is a little hacky—but the meaning is much clearer.
What are the total taxes paid on social security income?
The sum of the taxes paid oneachsocial security income.
How do you add all the items in a collection?
With<CollectionSum>.

Plus, it reads like all the other facts; needing to add up all items in a collection didn’t suddenly kick us into a new conceptual realm.

The philosophical difference between these two is that, unlike JavaScript, which isimperative, the Fact Dictionary isdeclarative.
It doesn’t describe exactly what steps the computer will take or in what order;
it describes a bunch of named calculations and how they depend on each other.
The engine decides automatically how to execute that calculation.

Besides being (relatively) friendlier to read, the most important benefit of a declarative tax model is that you can ask the program how it calculated something.
Per the Fact Graph’s original author,Chris Given:

The Fact Graph provides us with a means of proving that none of the unasked questions would have changed the bottom line of your tax return and that you’re getting every tax benefit to which you’re entitled.

Suppose you get a value fortotalOwedthat doesn’t seem right.
You can’t ask the JavaScript version “how did you arrive at that number?” because those intermediate values have already been discarded.
Imperative programs are generally debugged by adding log statements or stepping through with a debugger, pausing to check each value.
This works fine when the number of intermediate values is small;
it does not scale at all for the US Tax Code, where the final value is calculated based on hundreds upon hundreds of calculations of intermediate values.

With a declarative graph representation, we get auditability and introspection for free, for every single calculation.

Intuit, the company behind TurboTax, came to the same conclusion, and publisheda whitepaper about their “Tax Knowledge Graph”in 2020.
Their implementation is not open source, however (or least I can’t find it).
TheIRS Fact Graphis open source and public domain, so it can be studied, shared, and extended by the public.

## XML is much better at this than JSON

If we accept the need for a declarative data representation of the tax code, what should it be?

In many of the places where people used to encounter XML, such network data transfer and configuration files, it has been replaced by JSON.
I find JSON to be a reasonably good wire format and a painful configuration format, but in neither case would I rather be using XML (although it’s a close call on the latter).

The Fact Dictionary is different.
It’s not a pile of settings or key-value pairs.
It’s a custom language that models a unique and complex problem space.
In programming we call this a domain-specific language, or DSL for short.

As an exercise, I tried to come up with a plausible JSON representation of the/tentativeTaxNetNonRefundableCreditsfact from earlier.

{

 "description"
: "
Total tentative tax after applying non-refundable credits, but before applying refundable credits.
",

 "definition"
: {

 "type"
: "
Expression
",

 "kind"
: "
GreaterOf
",

 "children"
: [

 {

 "type"
: "
Value
",

 "kind"
: "
Dollar
",

 "value"
:
 0

 },

 {

 "type"
: "
Expression
",

 "kind"
: "
Subtract
",

 "minuend"
: {

 "type"
: "
Dependency
",

 "path"
: "
/totalTentativeTax
"

 },

 "subtrahend"
: {

 "type"
: "
Dependency
",

 "path"
: "
/totalNonRefundableCredits
"

 }

 }

 ]

 }

}

This is not a terribly complicated fact, but it’s immediately apparent that JSON does not handle arbitrary nested expressions well.
The only complex data structureavailable in JSONis an object, so every child object has to declare what kind of object it is.
Contrast that with XML, where the “kind” of the object is embedded in its delimiters.

<
Fact
 path
="
/tentativeTaxNetNonRefundableCredits
">

 <
Description
>

 Total tentative tax after applying non-refundable credits, but before

 applying refundable credits.

 </
Description
>

 <
Derived
>

 <
GreaterOf
>

 <
Dollar
>0</
Dollar
>

 <
Subtract
>

 <
Minuend
>

 <
Dependency
 path
="
/totalTentativeTax
"/>

 </
Minuend
>

 <
Subtrahends
>

 <
Dependency
 path
="
/totalNonRefundableCredits
"/>

 </
Subtrahends
>

 </
Subtract
>

 </
GreaterOf
>

 </
Derived
>

</
Fact
>

I think this XML representation could be improved, but even in its current form, it is clearly better than JSON.
(It’s also, amusingly, a couple lines shorter.)
Attributes and named children give you just enough expressive power to make choices about what your language should or should not emphasize.
Not being tied to specific set of data types makes it reasonable to define your own, such as a distinction between “dollars” and “integers.”

A lot of minor frustrations we’ve all internalized as inevitable with JSON are actually JSON-specific.
XML has comments, for instance.
That’s nice.
It also has sane whitespace and newline handling, which is important when your descriptions are often long.
For text that has any length or shape to it, XML is far more pleasant to read and edit by hand than JSON.

There are still verbosity gains to be had, particularly with switch statements (omitted here out of respect for page length).
I’d certainly remove the explicit “minuend” and “subtrahend,” for starters.

<
Fact
 path
="
/tentativeTaxNetNonRefundableCredits
">

 <
Description
>

 Total tentative tax after applying non-refundable credits, but before

 applying refundable credits.

 </
Description
>

 <
Derived
>

 <
GreaterOf
>

 <
Dollar
>0</
Dollar
>

 <
Subtract
>

 <
Dependency
 path
="
/totalTentativeTax
"/>

 <
Dependency
 path
="
/totalNonRefundableCredits
"/>

 </
Subtract
>

 </
GreaterOf
>

 </
Derived
>

</
Fact
>

I believe that the original team didn’t do this because they didn’t want the order of the children to have semantic consequence.
I get it, but orderisguaranteed in XML and I think the additional nesting and words do more harm then good.

What about YAML?Chris Given again:

whatever you do, don’t try to express the logic of the Internal Revenue Code as YAML

## XML is cheap and universal

Finally, there’s a good case to made that you could build this DSL with s-expressions.
In a lot of ways, this is nicest syntax to read and edit.

(Fact

 (Path "
/tentativeTaxNetNonRefundableCredits
")

 (Description "
Total tentative tax after applying non-refundable

 credits, but before applying refundable credits.
")

 (Derived

 (GreaterOf

 (Dollar 
0
)

 (Subtract

 (Minuend (Dependency "
/totalTentativeTax
"))

 (Subtrahends (Dependency "
/totalNonRefundableCredits
"))))))

HackerNews userok123456 asks: “Why would I want to use this over Prolog/Datalog?”I’m a Prolog fan!
This is also possible.

fact
(

 path(
"/tentativeTaxNetNonRefundableCredits"
),

 description(
"Total tentative tax after applying non-refundable credits, but before applying refundable credits."
),

 derived(

 greaterOf(

 dollar(
0
),

 subtract(

 minued(dependency(
"/totalTentativeTax"
)),

 subtrahends(dependency(
"/totalNonRefundableCredits"
))))))

My friend Deniz couldn’t help but rewrite it inKDL, a cool thing I had to look up.

fact
 /
tentativeTaxNetNonRefundableCredits
 {

 description
 """

 Total tentative tax after applying non-refundable credits, but before

 applying refundable credits.

 """

 derived
 {

 greater-of
 {

 dollar
 0

 subtract
 {

 dependency
 /
totalTentativeTax

 dependency
 /
totalNonRefundableCredits

 }

 }

 }

}

At least to my eye, all of these feel more pleasant than the XML version.
When I started working on the Fact Graph, I strongly considered proposing a transition to s-expressions.
I even half-jokingly included it in a draft design document.
The process of actually building on top of the Fact Graph, however, taught me something very important about the value of XML.

Using XML gives you a parser and a universal tooling ecosystem for free.

Take Prolog for instance.
You can relate XML to Prolog terms witha single predicate.
If I want to explore Fact Dictionaries in Prolog—or even make a whole alternative implementation of the Fact Graph—I basically get the Prolog representation out of the box.

S-expressions work great in Lisp and Prolog terms work great in Prolog.
XML can be transformed, more or less natively, into anything.
That makes it a great canonical, cross-platform data format.

XML is rivaled only by JSON in the maturity and availability of its tooling.
At one point I had the idea that it would be helpful to fuzzy search for Fact definitions by path.
I’d like to just type “overtime” and see all the facts related to overtime.
Regular searches of the codebase were cluttered with references and dependencies.

This was possible entirely with shell commands I already had on my computer.

cat facts.xml | xpath -q -e '//Fact/@path' | grep -o '/[^"]*' | fzf

This usesXPathto query all the fact paths,grepto clean up the output, andfzfto interactively search the results.
I solved my problem with a trivial bash one-liner.
I kept going and said: not only do I want to search the paths, I’d likeselectingone of the paths to show me the definition.

Easy. Just take the result of the first command, which is a path attribute, and use it in a second XPath query.

path=$(cat facts.xml | xpath -q -e '//Fact/@path' | grep -o '/[^"]*' | fzf)

cat facts.xml | xpath -q -e "//Fact[@path=\"$path\"]" | format

I got a little carried awaybuilding this outinto a “$0 Dispatch Pattern” script of the kinddescribed by Andy Chu.
(Andy is a blogging icon, by the way.)
I also added dependency search—not only can you query the definition of a fact, but you can goupthe dependency chain by asking what facts depend on it.

Try it yourself by cloningthe repoand running./scripts/fgs.sh(you needfzfinstalled).
The error handling is janky but it’s pretty solid for 60 lines of bash I wrote in an afternoon.
I use it almost daily.

I’m not sure how many people used my script, but multiple other team members put together similarly quick, powerful debugging tools that became part of everyone’s workflow.
All of these tools relied on being able to trivially parse the XML representation and work with it in the language that best suited the problem they were trying to solve, without touching the Fact Graph’s actual implementation in Scala.

The lesson I took from this is that a universal data representation is worth its weight in gold.
There are exactly two options in this category.
In most cases you should choose JSON.
If you need a DSL though, XML is by far the cheapest one, and the cost-efficiency of building on it will empower your team to spend their innovation budget elsewhere.

Thanks toChris GivenandDeniz Akşimşekfor their feedback on a draft of this blog.

# Notes

* I had never heard of XPath before 2023, when Denizfigured out an XPath querythat mademy first htmx PRpossible.
* Another reason to use XML is that humans who aren’t programmers can read it. They usually don’t like it, but, if you did a good-enough job designing the schema, they can read it in a pinch. Do them a favor and build an alternative view, though. Because you’re using XML, this is pretty easy.
* It’s probably just because I’ve started to use it—buy a Jeep Grand Cherokee and suddenly the roadways seem full of them—but lately I have noticed an uptick in XML interest.
FellowSpring ’24 RecurserJake Low recently wrotea tool calledgrexwhich turns XML documents into a flat, line-oriented representation.
Martijn Faassen has been working ona modern XPath and XSLT engine in Rust.
* I’m not sure it’s fair to call JSON “lobotomized” but I thoughtthis articlewas largely correct about the problems XML can solve. The binary format is especially interesting to me.