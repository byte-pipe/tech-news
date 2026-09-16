---
title: Small Programming Tricks · will keleher
url: https://will-keleher.com/posts/small-programming-tricks-matter/
site_name: hackernews_api
content_file: hackernews_api-small-programming-tricks-will-keleher
fetched_at: '2026-09-16T21:54:38.374193'
original_url: https://will-keleher.com/posts/small-programming-tricks-matter/
author: signa11
date: '2026-09-16'
description: A lot of effective engineering comes from the accumulation of small nuggets of knowledge.
tags:
- hackernews
- trending
---

# Small Programming Tricks

Day to day, I think a surprising amount of engineering productivity comes from small nuggets of knowledge: being aware that a language feature exists; knowing that an unexplained tcp delay is probably related to the TCP_NO_DELAY setting and Nagle’s algorithm; knowing the rightgitincantation to get out of a pickle; or knowing a trick withsedto rewrite a file.

In one sense, this is self-evident: anything you know is going to be made up of smaller pieces of knowledge.Of coursethose smaller pieces of knowledge matter.

But I think there are some nuggets of knowledge that are particularly valuable and don’t require a lot of supporting mental infrastructure. You don’t need to know any python to usepython3 -m http.serverto start a simple server in a directory, but it might still make your work marginally easier. Let me share a few examples:

* You probably know thatctrl + rallows searching your terminal’s command history, but if you installfzf, you can set it up so thatctrl + rdoes a fuzzy search. If you want even more power,atuinreplaces your shell history with a searchable SQLite database.per-directory-historylets you switch back and forth between searching for commands that have been run in a specific directory or searching all previous commands. Finally, you can configure how much history to store:stackoverflow question.
* You canSELECTwithout aFROM. This can be useful for testing out how a function in your database actually works or reminding yourself howSELECT TRUE <> NULLworks.1
* PostgresSQL and MySQL both supportexplain analyzewhich will actually run the query you’re trying to optimize and give you a ton more information about its performance.
* In regular expressions,\b, theword boundary assertion, makes it easy to look for the beginnings or ends of words.
* You can use logarithms with metrics to get a sense of the distribution of values for a field you’re interested in:constbucket=Math.floor(Math.log10(userInGroupCount))metrics.increment("my_metric", {bucket});
* Modern JS now supportsArray.flatMap,Object.entries, andPromise.withResolvers.
* In NodeJS, you can keep a connection open to an external resource by creating anhttps.Agentand then providing it to your http requests:fetch(url, {method, agent}). This can have a dramatic impact on latency.
* git log -S pattern(”git pickaxe”) can give you all commits thatadded or removeda string in a codebase. It’s amazingly useful especially with older codebases! (git log -G patternis similar, but will also show when that line was moved)
* Similar tocd -, you can usegit checkout -to check out your previous HEAD.
* You probably don’t needfind. A lot offindcommands can be replaced with globs like**/*.md. Most shells support this out of the box, but with bash, you need to turn this on withshopt -s globstar.
* In a similar vein, most folks will probably want to userg(ripgrep) rather thangrep,ack, orag.
* zsh’s advanced autocompletion features aren’t turned on by default:iftype brew &>/dev/null;thenFPATH="$(brew --prefix)/share/zsh/site-functions:${FPATH}"fiautoload -Uz compinitcompinit

You might have already known all of these things! Or you might work in a domain that makes all of these little tricks totally useless. Even if this particular set of tricks isn’t useful for you, I bet you have your own stash of tricks that you’ve accumulated over the years that makes your work easier.

At a company, I think even more knowledge tends to be this sort of small high-leverage nugget:

* To debug $PROBLEM, use $DATA_SOURCE.
* $PERSON knows a ton about $AREA and they’re happy to help if you get stuck
* There are good docs about $HARD_THING $OVER_HERE.
* When $THING happens, it means we should manually scale out.
* To do a rolling restart of a service, run $THIS_COMMAND.
* This $UTIL makes $THAT_PROBLEM easy to script.

At a previous company, I shared a trick on slack every day with the engineering team, both technical and company-specific, and folks found them pretty useful. Even if you knew 9/10 tricks, that 10th doc or technique might save you some time! And one trick per day was the right number to avoid overwhelming people with knowledge, and it could occasionally spark useful discussion. If you’re a more senior engineer at your company, you might think about doing something similar.

1. I think I first saw this technique onJulia Evan’s blog, and I think her writing often perfectly encapsulates the idea behind this post: "small bits of knowledge are powerful! and fun! and approachable!!"↩︎