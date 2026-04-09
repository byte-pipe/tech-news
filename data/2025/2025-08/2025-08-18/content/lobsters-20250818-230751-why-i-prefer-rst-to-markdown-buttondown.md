---
title: Why I prefer rST to markdown • Buttondown
url: https://buttondown.com/hillelwayne/archive/why-i-prefer-rst-to-markdown/
site_name: lobsters
fetched_at: '2025-08-18T23:07:51.073478'
original_url: https://buttondown.com/hillelwayne/archive/why-i-prefer-rst-to-markdown/
date: '2025-08-18'
description: I will never stop dying on this hill
tags: practices
---

July 31, 2024




# Why I prefer rST to markdown

## I will never stop dying on this hill

I just published a new version ofLogic for Programmers! v0.2 has epub support, content on constraint solving and formal specification, and more! Get ithere.

This is my second book written withSphinx, after the newLearn TLA+. Sphinx uses a peculiar markup calledreStructured Text(rST), which has a steeper learning curve than markdown. I only switched to itafterwriting a couple of books in markdown and deciding I needed something better. So I want to talk about why rst was that something.1

## Why rst is better

The most important difference between rst and markdown is that markdown is a lightweight representation of html, while rst is a midweight representation of an abstract documentation tree.

It's easiest to see this with a comparison. Here's how to make an image in markdown:

![
alttext
](
example.jpg
)

Technically, you don't even need a parser for this. You just need a regex to transform it into<img alt="alttext" src="example.jpg"/>. Most modern markdown enginesdoparse this into an intermediate representation, but theessenceof markdown is that it's a lightweight html notation.

Now here's how to make an image in rst:

..

image
::
 example.jpg

:alt:
 alttext

.. image::defines the image "directive". When Sphinx reads it, it looks up the registered handler for the directive, findsImageDirective, invokesImageDirective.run, which returns animage_node, which is an object with analtfield containing "alttext". Once Sphinx's processed all nodes, it passes the whole doctree to the HTML Writer, which looks up the rendering function forimage_node, which tells it to output an<image>tag.

Whew that's a mouthful. And for all that implementation complexity, we get… an interface that has 3x the boilerplate as markdown.

On the other hand, the markdown image is hardcoded as a special case in the parser, while the rst image is not. It was added in the exact same way as every other directive in rst: register a handler for the directive, have the handler output a specific kind of node, and then register a renderer for that node for each builder you want.

This means you can extend Sphinx with new text objects! Say you that instead of an<image>, you want a<figure>with a<figcaption>. In basic markdown you have to manually insert the html, with Sphinx you can just register a newfiguredirective. You can even make yourFigureDirectivesubclassImageDirectiveand have it do most of the heavy lifting.

The second benefit is more subtle: you can transform the doctree before rendering it. This is how Sphinx handles cross-referencing: if I put afooanchor in one document and:ref:`image <foo>`in another, Sphinx will insert the right URL during postprocessing. The transformation code is also first-class with the rest of the build process: I can configure a transform to only apply when I'm outputting html, have it trigger in a certain stage of building, or even remove a builtin transform I don't want to run.

Now, most people may not need this kind of power! Markdown is ubiquitous because it's lightweight and portable, and rst is anything but. ButIneed that power.

### One use case

Logic for Programmersis a math-adjacent book, and all good math books need exercises for the reader. It's easier to write an exercise if I can put it and the solution right next to each other in the document. But for readers, I want the solutions to show up in the back of the book. I also want to link the two together, and since I might want to eventually print the book, the pdfs should also include page references. Plus they need to be rendered in different ways for latex (pdf) output and epub output. Overall lots of moving parts.

To handle this I wrote my own exercise extension.

.. in chapter.rst

..

exercise
::
 Fizzbuzz

:name:
 ex-fizzbuzz

 An exercise

..

solution
::
 ex-fizzbuzz

 A solution

.. in answers.rst

..

solutionlist
::

How these nodes are processed depends on my compilation target. I like to debug in HTML, so for HTML it just renders the exercise and solution inline.

When generating epub and latex, though, things works a little differently. After generating the whole doctree, I run a transform that moves every solution node from its original location to undersolutionlist. Then it attaches a reference node to every exercise, linking it to thenewsolution location, and vice versa. So it starts like this (using Sphinx's "pseudoxml" format):

--

chapter.rst

<exercise_node

ids=
"ex-fizzbuzz"
>


<title>


Fizzbuzz


<paragraph>


An

exercise

<solution_node

ids=
"ex-fizzbuzz-sol"
>


<paragraph>


A

solution

--

answers.rst

<solutionlist_node>

And it becomes this:

--

chapter.rst

<exercise_node

ids=
"ex-fizzbuzz"
>


<title>


Fizzbuzz


<paragraph>


An

exercise


<exsol_ref_node

refuri=
"/path/to/answers#ex-fizzbuzz-sol"
>


Solution

--

answers.rst

<solutionlist_node>


<solution_node

ids=
"ex-fizzbuzz-sol"
>


<paragraph>


A

solution


<exsol_ref_node

refuri=
"/path/to/chapter#ex-fizzbuzz"
>


(back)

The Latex builder renders this by wrapping each exercise and solution in ananswers environment, while the epub builder renders the solution as apopup footnote.2Making this work:



It's a complex dance of operations, but it works enormously well. It even helps with creating a "free sample" subset of the book: the back of the free sample only includes the solutions from the included subset, not the whole book!

### "But I hate the syntax"

When I gush about rST to other programmers, this is the objection I hear the most: it's ugly.

To which I say, are you really going to avoid using a good tool just because it makes you puke? Because looking at it makes your stomach churn? Because it offends every fiber of your being?

...Okay yeah that's actually a pretty good reason not to use it. I can't get into lisps for the same reason. I'm not going to begrudge anybody who avoids a tool because it's ugly.

Maybe you'd findasciidocmore aesthetically pleasing? OrMyST? OrTypst? OrPollen? Or evenpandoc-extended markdown? There are lots of solid document builders out there! My point isn't that sphinx/rst is exceptionallygoodfor largescale documentation, it's that simple markdown is exceptionallybad. It doesn't have a uniform extension syntax or native support for pre-render transforms.

This is why a lot of markdown-based documentation generators kind of hack on their own preprocessing step to support new use-cases, which works for the most part (unless you're trying to do something really crazy). But they have to work around the markdown, not in it, which limits how powerful they can be. It also means that most programmer tooling can't understand it well. There's LSP and treesitter for markdown and rst but not for gitbook-markdown or md-markdown or leanpub-markdown.3

But if you find a builder that uses markdown and satisfies your needs, more power to you! I just want to expose people to the idea that doc builders can be a lot more powerful than they might otherwise expect.

### No newsletter next week

I'll be in Hong Kong.

## Update 2024-07-31

Okay since this is blowing up online I'm going to throw in a quick explanation ofLogic for Programmersfor all of the non-regulars here. I'm working on a book about how formal logic is useful in day-to-day software engineering. It starts with a basic rundown of the math and then goes into eight different applications, such as property testing, database constraints, and decision tables. It's still in the alpha stages but already 20k words and has a lot of useful content. You can find ithere. Reader feedback highly appreciated!

1. rst is actually independent of Sphinx, but everybody I know who writes rst writes itbecausethey're using Sphinx, so I'll use the two interchangeably. Also typing rST is annoying so I'm typing rst.↩
2. This is why I attachexsol_ref_nodesand not defaultreference_nodes. Sphinx's epub translator uses an attribute passlist I need to workaround in post-rendering.↩
3. This is also one place where rst's ugly syntax works in its favor. I've got a treesitter query that changes the body of todo directives andonlytodo directives, which is only possible because the rst syntax tree is much richer than the markdown syntax tree.↩

If you're reading this on the web, you can subscribehere. Updates are once a week. My main website ishere.

My new book,Logic for Programmers, is now in early access! Get ithere.



Don't miss what's next. Subscribe to Computer Things:




Subscribe



Start the conversation:




 Comment and Subscribe
