---
title: We Should Revisit Literate Programming in the Agent Era | silly business
url: https://silly.business/blog/we-should-revisit-literate-programming-in-the-agent-era/
site_name: hackernews_api
content_file: hackernews_api-we-should-revisit-literate-programming-in-the-agen
fetched_at: '2026-03-09T11:18:10.535048'
original_url: https://silly.business/blog/we-should-revisit-literate-programming-in-the-agent-era/
author: horseradish
date: '2026-03-08'
published_date: '2026-03-07T10:07:36-08:00'
description: 'Literate programming is the idea that code should be intermingled with prose such that an uninformed reader could read a code base as a narrative, and come away with an understanding of how it works and what it does. Although I have long been intrigued by this idea, and have found uses for it in a couple1 of different cases2, I have found that in practice literate programming turns into a chore of maintaining two parallel narratives: the code itself, and the prose. This has obviously limited its adoption.'
tags:
- hackernews
- trending
---

# We Should Revisit Literate Programming in the Agent Era

07 Mar, 2026

Literate programming is the idea that code should be intermingled with prose such that an uninformed reader could read a code base as a narrative, and come away with an understanding of how it works and what it does.

Although I have long been intrigued by this idea, and have found uses for it in a couple1of different cases2, I have found that in practice literate programming turns into a chore of maintaining two parallel narratives: the code itself, and the prose. This has obviously limited its adoption.

Historically in practice literate programming is most commonly found as Jupyter notebooks in the data science community, where explanations live alongside calculations and their results in a web browser.

Frequent readers of this blog will be aware that Emacs Org Mode supports polyglot literate programming through itsorg-babelpackage, allowing execution of arbitrary languages with results captured back into the document, but this has remained a niche pattern for nerds like me.

Even for someone as enthusiastic about this pattern as I am, it becomes cumbersome to use Org as the source of truth for larger software projects, as the source code essentially becomes a compiled output, and after every edit in the Org file, the code must be re-extracted and placed into its destination ("tangled", in Org Mode parlance). Obviously this can be automated, but it's easy to get into annoying situations where you or your agent has edited the real source and it gets overwritten on the next tangle.

That said, I have had enough success with using literate programming for bookkeeping personal configuration that I have not been able to fully give up on the idea, even before the advent of LLMs.

For example: before coding agents, I had been adapting a pattern for using Org Mode for manual testing and note-taking: instead of working on the command line, I would write more commands into my editor and execute them there, editing them in place until each step was correct, and running them in-place, so that when I was done I would have a document explaining exactly the steps that were taken, without extra steps or note-taking.Combining the act of creating the note and running the test gives you the notes for free when the test is completed.

This is even more exciting now that we have coding agents. Claude and Kimi and friends all have a great grasp of Org Mode syntax; it's a forgiving markup language and they are quite good at those. All the documentation is available online and was probably in the training data, and while a big downside of Org Mode is just how much syntax there is, but that's no problem at all for a language model.

Now when I want to test a feature, I ask the clanker3to write me a runbook in Org. Then I can review it – the prose explains the model's reflection of the intent for each step, and the code blocks are interactively executable once I am done reviewing, either one at a time or the whole file like a script. The results will be stored in the document, under the code, like a Jupyter notebook.

I can edit the prose and ask the model to update the code, or edit the code and have the model reflect the meaning upon the text. Or ask the agent to change both simultaneously. The problem of maintaining the parallel systems disappears.

The agent is told to handle tangling, and the problem of extraction goes away. The agent can be instructed with an AGENTS.md file to treat the Org Mode file as the source of truth, to always explain in prose what is going on, and to tangle before execution. The agent is very good at all of these things, and it never gets tired of re-explaining something in prose after a tweak to the code.

The fundamental extra labor of literate programming, which I believe is why it is not widely practiced, is eliminated by the agent and it utilizes capabilities the large language model is best at: translation and summarization.

As a benefit, the code base can now be exported into many formats for comfortable reading. This is especially important if the primary role of engineers is shifting from writing to reading.

I don't have data to support this, but I also suspect that literate programming will improve the quality of generated code, because the prose explaining the intent of each code block will appear in context alongside the code itself.

I have not personally had the opportunity to try this pattern yet on a larger, more serious codebase. So far, I have only been using this workflow for testing and for documenting manual processes, but I am thrilled by its application there.

I also recognize that the Org format is a limiting factor, due to its tight integration with Emacs. However, I have long believed that Org should escape Emacs. I would promote something like Markdown instead, however Markdown lacks the ability to include metadata4. But as usual in my posts about Emacs, it's not Emacs's specific implementation of the idea that excites me, as in this case Org's implementation of literate programming does.

It is the idea itself that is exciting to me, not the tool.

With agents, does it become practical to have large codebases that can be read like a narrative, whose prose is kept in sync with changes to the code by tireless machines?

I think that's a compelling question.

## Footnotes

1

/emacs/

2

/blog/the-literate-self-hoster/

3

https://en.wikipedia.org/wiki/Clanker

4

Org Mode has concepts likepropertieswhich allow acting on the document programmatically from Emacs Lisp. In the past this meant I was often tempted to fumble around with Lisp for awhile to get some imagined interactive feature in my document, for which I never had time in practice. But now the LLM will happily shove some Emacs Lisp into thefile variablessection of the document with bespoke functionality for that interactive document specifically.

The lack of metadata in Markdown also means that there is nowhere to store information about codeblocks that would be extracted from a literate document. Org Mode providesheader argumentsthat can be applied to source code blocks, providing instruction to the machine about execution details like where the code should be executed, which might even be a remote machine.