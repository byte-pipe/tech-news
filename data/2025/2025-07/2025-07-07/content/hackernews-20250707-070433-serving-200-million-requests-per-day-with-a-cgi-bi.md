---
title: Serving 200 million requests per day with a cgi-bin
url: https://simonwillison.net/2025/Jul/5/cgi-bin-performance/
site_name: hackernews
fetched_at: '2025-07-07T07:04:33.924943'
original_url: https://simonwillison.net/2025/Jul/5/cgi-bin-performance/
author: Simon Willison
date: '2025-07-07'
---

# Simon Willison’s Weblog

Subscribe

Serving 200 million requests per day with a cgi-bin(via) Jake Gold tests how well 90s-era CGI works today, using a Go + SQLite CGI program running on a 16-thread AMD 3700X.

Using CGI on modest hardware, it’s possible to serve 2400+ requests per second or 200M+ requests per day.

I got my start in web development with CGI back in the late 1990s - I was a huge fan ofNewsPro, which was effectively a weblog system before anyone knew what a weblog was.

CGI works by starting, executing and terminating a process for every incoming request. The nascent web community quickly learned that this was a bad idea, and invented technologies like PHP andFastCGIto help avoid that extra overhead and keep code resident in-memory instead.

This lesson ended up baked into my brain, and I spent the next twenty years convinced that you shouldneverexecute a full process as part of serving a web page.

Of course, computers in those two decades got alotfaster. I finally overcame that twenty-year core belief in 2020, whenI built datasette-ripgrep, a Datasette plugin that shells out to the lightning fastripgrepCLI tool (written in Rust) to execute searches. It worked great!

As waspointed out on Hacker News, part of CGI's problem back then was that we were writing web scripts in languages like Perl, Python and Java which had not been designed for lightning fast startup speeds. Using Go and Rust today helps make CGI-style requests a whole lot more effective.

Jake notes that CGI-style request handling is actually a great way to take advantage of multiple CPU cores:

These days, we have servers with 384 CPU threads. Even a small VM can have 16 CPUs. The CPUs and memory are much faster as well.

Most importantly, CGI programs, because they run as separate processes, are excellent at taking advantage of many CPUs!

Maybe we should start coding web applications like it's 1998, albeit with Go and Rust!

To clarify, I don't think most people should do this. I just think it's interesting that it's not as bad an idea as it was ~25 years ago.

Posted
5th July 2025
 at 11:28 pm

## Recent articles

* Phoenix.new is Fly's entry into the prompt-driven app development space- 23rd June 2025
* Trying out the new Gemini 2.5 model family- 17th June 2025
* The lethal trifecta for AI agents: private data, untrusted content, and external communication- 16th June 2025



 cgi

13

 go

41

 performance

91

 sqlite

299

### Monthly briefing

Sponsor me for$10/monthand get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

 Sponsor & subscribe








* Colophon
* ©
* 2002
* 2003
* 2004
* 2005
* 2006
* 2007
* 2008
* 2009
* 2010
* 2011
* 2012
* 2013
* 2014
* 2015
* 2016
* 2017
* 2018
* 2019
* 2020
* 2021
* 2022
* 2023
* 2024
* 2025
