---
title: No, Google Did Not Unilaterally Decide to Kill XSLT – Eric’s Archived Thoughts
url: https://meyerweb.com/eric/thoughts/2025/08/22/no-google-did-not-unilaterally-decide-to-kill-xslt/
site_name: lobsters
fetched_at: '2025-08-23T23:07:54.116860'
original_url: https://meyerweb.com/eric/thoughts/2025/08/22/no-google-did-not-unilaterally-decide-to-kill-xslt/
date: '2025-08-23'
tags: web
---

It’s uncommon, but not unheard of, for a GitHub issue to spark an uproar.  That happened over the past month or so as the WHATWG (Web Hypertext Application Technology Working Group, which I still say should have called themselves a Task Force instead) issue “Should we remove XSLT from the web platform?” was opened, debated, and eventually locked once the comment thread started spiraling into personal attacks.  Other discussions have since opened, such asa counterproposal to update XSLT in the web platform, thankfully with (thus far) much less heat.

If you’re new to the term, XSLT (Extensible Stylesheet Language Transformations) is an XML language that lets you transform one document tree structure into another.  If you’ve ever heard of people styling their RSS and/or Atom feeds to look nice in the browser, they were using some amount of XSLT to turn the RSS/Atom into HTML, which they could then CSS into prettiness.

This is not the only use case for XSLT, not by a long shot, but it does illustrate the sort of thing XSLT is good for.  So why remove it, and who got this flame train rolling in the first place?

Before I start, I want to note that in this post, I won’t be commenting on whether or not XSLT support should be dropped from browsers or not.  I’m also not going to be systematically addressing the various reactions I’ve seen to all this.  I have my own biases around this — some of them in direct conflict with each other! — but my focus here will be on what’s happened so far and what might lie ahead.

Also,Brianand Italked with Liam Quinabout all this, if you’d rather hear a conversation than read a blog post.

As a very quick background, various people have proposed removing XSLT support from browsers a few times over the quarter-century-plus since support first landed.  It was discussed in both the early and mid-2010s, for example.  At this point, browsers all more or less supportXSLT 1.0, whereas the latest version of XSLT is3.0.  I believe they all do so with C++ code, which is therefore not memory-safe, that is baked into the code base rather than supported via some kind of plugged-in library, like Firefox usingPDF.jsto support PDFs in the browser.

Anyway, back on August 1st, Mason Freed of Google openedissue #11523on WHATWG’s HTML repository, asking if XSLT should be removed from browsers and giving a condensed set of reasons why it might be a good idea.  He also included a WASM-based polyfill he’d written to provide XSLT support, should browsers remove it, and opened “Investigate deprecation and removal of XSLT” in the Chromium bug tracker.

“So it’s already been decided and we just have to bend over and take the changes our Googlish overlords have decreed!” many people shouted.  It’s not hard to see where they got that impression, given some of the things Google has done over the years, but that’snotwhat’s happening here.  Not at this point.  I’d like to set some records straight, as an outside observer of both Google and the issue itself.

First of all, while Mason was the one to open the issue, this was done because the idea was raised in a periodic WHATNOT meeting (call), where someone at Mozilla was actually the one to bring it up, after it had come up in various conversations over the previous few months.  After Mason opened the issue, members of the Mozilla and WebKit teams expressed (tentative, mostly) support for the idea of exploring this removal.  Basically,noneof the vendors are particularly keen on keeping native XSLT support in their codebases, particularly aftersecurity flaws were foundin XSLT implementations.

This isn’t the first time they’ve all agreed it might be nice to slim their codebases down a little by removing something that doesn’t get a lot of use (relatively speaking), and it won’t be the last.  I bet they’ve all talked at some point about how nice it would be to removeBMPsupport.

Mason mentioned that they didn’t have resources to put toward updating their XSLT code, and got widely derided for it. “Google has trillions of dollars!” people hooted.Googlehas trillions of dollars.  The Chrome team very much does not.  They probably get, at best, a tiny fraction of one percent of those dollars.  Whether Google should give the Chrome team more money is essentially irrelevant, because that’s not in the Chrome team’s control.  They have what they have, in terms of head count and time, and have to decide how those entirely finite resources are best spent.

(I will once again invoke my late-1900s formulation ofHanlon’s Razor:Never attribute to malice that which can be more adequately explained by resource constraints.)

Second of all, the issue was opened to start a discussion and gather feedback as the first stage of a multi-step process, one that could easily run for years.  Google, as I assume is true for other browser makers, has a pretty comprehensive method for working out whether removing a given feature is tenable or not.Brianand Italked with Rick Byers about ita while back, and I was impressed by both how many thingshavebeen removed, and what they do to make sure they’re removing the right things.

Here’s one (by no means the only!) way they could go about this:

1. Set up a switch that allows XSLT to be disabled.
2. In the next release of Chrome, use the switch to disable XSLT in one percent of all Chrome downloads.
3. See if any bug reports come in about it.  If so, investigate further and adjust as necessary if the problems are not actually about XSLT.
4. If not, up the percentage of XSLT-disabled downloads a little bit at a time over a number of releases.  If no bugs are reported as the percentage of XSLT-disabled users trends toward 100%, then prepare to remove it entirely.
5. If, on the other hand, it becomes clear that removing XSLT will be a widely breaking change  —  where “widely” can still mean a very tiny portion of their total user base — then XSLT can be re-enabled for all users as soon as possible, and the discussion taken back up with this new information in hand.

Again, that is just one of several approaches Google could take, and it’s a lot simpler than what they would most likely actually do, but it’s roughly what they default to, as I understand it.  The process is slow and deliberate, building up a picture of actual use and user experience.

Third of all, opening a bug that includes a pull request of code changes isn’t a declaration of countdown to merge, it’s a way of making crystal clear (to those who can read the codebase) exactly what the proposal would entail.  It’s basically a requirement for the process of making a decision to start, because it sets the exact parameters of what’s being decided on.

That said, as a result of all this, I now strongly believe that every proposed-removal issue should point to the process and where the issue stands in it. (And write down the process if it hasn’t been already.) This isn’t for the issue’s intended audience, which was other people within WHATWG who are familiar with the usual process and each other, but for cases of context escape, like happened here.  If a removal discussion is going to be held in public, then it should assume the general public will see it and provide enough context for the general public to understand the actual nature of the discussion.  In the absence of that context, the nature of the discussion will be assumed, and every assumption will be different.

There is one thing that we should all keep in mind, which is that “remove from the web platform” really means “remove from browsers”.  Even if this proposal goes through, XSLT could still be used server-side.  You could use libraries that support XSLT versions more recent than 1.0, even!  Thus, XML could still be turned into HTML, just not in the client via native support, though JS or WASM polyfills, or even add-on extensions, would still be an option.  Is that good or bad?  Like everything else in our field, the answer is “it depends”.

Just in case your eyes glazed over and you quickly skimmed to see if there was a TL;DR, here it is:

The discussion was opened by a Google employee in response to interest from multiple browser vendors in removing built-in XSLT, following a process that is opaque to most outsiders.  It’s a first step in a multi-step evaluation process that can take years to complete, and whose outcome is not predetermined.  Tempers flared and the initial discussion was locked; the conversation continues elsewhere.  There are good reasons to drop native XSLT support in browsers, and also good reasons to keep or update it, but XSLT is not itself at risk.

 
* No, Google Did Not Unilaterally Decide to Kill XSLTwas published onFriday, August 22nd, 2025.
* It was assigned to theBrowsers,Commentary, andXSLTcategories.
* There has beenone reply.

### One Comment

1. The only question I have is: if there’s a PDF.js-style polyfill which is included with browsers, why does “the web platform” need to change at all? Shouldn’t the public interface remain the same?The way I see it, this would be strictly better for everyone. People who need it can still use it, and with the improved security of the JS sandbox.

Name

E-mail(required but not displayed)

URI(optional)

Meyerweb dot com reserves the right to edit or remove any comment, especially when abusive or irrelevant to the topic at hand.

HTMLallowed:<a href="" title=""> <abbr title=""> <acronym title=""> <b> <blockquote cite=""> <cite> <code> <em> <i> <q cite=""> <s> <strong> <pre class=""> <kbd>

Your Comment
(
Markdown
 supported)

if you’re satisfied with it.

#### Comment Preview

Δ
