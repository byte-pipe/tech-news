---
title: Why I Keep Blogging With Emacs
url: https://entropicthoughts.com/why-stick-to-emacs-blog
site_name: hackernews
fetched_at: '2025-10-03T11:08:39.617839'
original_url: https://entropicthoughts.com/why-stick-to-emacs-blog
author: kqr
date: '2025-10-03'
---

Every time I look at someone’s simple static site generation setup for their
blog, I feel a pang of envy. I’m sure I could make a decent blogging engine in
2,000 lines of code, and it would be something I’d understand, be proud over,
able to extend, and willing to share with others.

Instead, I write these articles in Org mode, and use mostly the standard Org
publishing functions to export them tohtml. This issometimes brittle, but
most annoyingly, I don’t understand it. I have been asked for details on how my
publishing flow works, but the truth is I have no idea what happens when I run
theorg-publish-current-filecommand.

I could find out by tracing the evaluation of the Lisp code that runs on export,
but I won’t, because just thehtmlexporting code (ox-html.el) is 5,000
lines of complexity. The general exporting framework (ox-publish.elandox.el) is 8,000 lines. The framework depends on Org parsing code
(org-element.el) which is at least another 9,000 lines. This is over 20,000
lines of complexity I’d need to contend with.

It might seem like a no-brainer to just write that 2,000 line custom static
generator and use that instead.

Except one thing: Babel.

Any lightweight markup format (like Markdown or ReStructuredText or whatever)
allows for embedding code blocks, but Org, through Babel, canrunthat code on
export, and then display the output in the published document,even when the
output is a table or an image. It supports sessions that lets code reuse
definitions from earlier code blocks. It allows for injecting variables from the
markup into the code, and vice versa. As a bonus, Org doesn’t require a
JavaScript syntax highlighter, because it generates inline styles in the source
code.

It does this for a large number of languages, although I mainly use it with R
for drawing plots. Being able to do this is incredibly convenient, because it
makes it trivial todraft data, illustrations, and text at the same time,
adjusting both until the article coheres. Having tried it, I cannot see myself
living without it.

A simple 2,000 line blogging engine would be a fun weekend project. Mirroring
the features of Babel I use would turn it into a multi-month endeavour for
someone with limited time such as myself. Not going to happen, and I will
continue to beat myself up for overcomplicating my publishing workflow.
