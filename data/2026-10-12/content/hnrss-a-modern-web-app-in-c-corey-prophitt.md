---
title: A modern web app in c | Corey Prophitt
url: https://prophitt.me/writing/a-modern-web-app-in-c
site_name: hnrss
content_file: hnrss-a-modern-web-app-in-c-corey-prophitt
fetched_at: '2026-10-12T20:08:26.765006'
original_url: https://prophitt.me/writing/a-modern-web-app-in-c
date: '2026-10-12'
description: 'A modern web app written in c and served the old way: CGI, SQLite and a single binary. No frameworks, no containers and no regrets.'
tags:
- hackernews
- hnrss
---

## ## INTRO

If you wanted a dynamic website in 1994, you wrote a C program, dropped it in a cgi-bin directory, and let Apache fork it per request. Thirty-two years later, I shipped a commercial web product using fundamentally the same technology.

Everything aboutmarketyour.gamesis modern. It's a web product with user accounts, a search dashboard for content creators, folders for organizing them, payments via Stripe and transactional emails via Postmark. It follows progressive enhancement and doesn't require any JavaScript.

Everything is modern except the way it was made and how it is served. Here are my thoughts on writing a real product in C and serving it via CGI in 2026.

## ## TLDR

CGI's decline was justified in 2004 but doesn't hold up in 2026.

You can write a modern web application in C. I shipped one. One binary, a SQLite file, three dependencies and the entire thing fits in your head.

## ## HOW IT WAS DONE

The stack isBCHS: OpenBSD, C, httpd, and SQLite.

There's no framework. You write a C program that reads CGI environment variables and responds.

There's no templating language. You write C that outputs the HTML directly.

There's no separate database server. You open the database file through SQLite's C API.

There's no container. You build a statically linked binary and drop it in a folder.

Every request spawns a fresh process. Deploying a new version is replacing one file. That means no server restart and no downtime. New requests simply pick up the new binary.

OpenBSD ships with sane defaults and gives you the tools to actually secure a C program like pledge and unveil. Httpd serves from a chroot by default, so your CGI binary runs sandboxed to its own corner of the filesystem.

I lean on three additional libraries:

libcurl handles all outbound requests to Stripe and Postmark.

libsodium handles random identifier generation, password hashing and the HMAC verification for Stripe webhooks.

libcjson handles JSON parsing for Stripe and Postmark.

Only two of those are actual build dependencies: libcurl and libsodium.

libcjson is a single C file and has no external dependencies.SQLite ships an official amalgamation (single C file) build.

Both are vendored and built as part of the project.

The result is a build with almost no moving parts. A clean build takes a few seconds and rebuilds complete in less than half a second.

Instead of serving static assets the traditional way, I route all traffic from httpd to the CGI binary. Every asset is compiled into the executable and served from memory.

## ## WHAT I LIKED

### Fundamentals over frameworks.

CGI isn't a framework to learn. The 1.1 specification was published in 2004 and hasn't changed since.

There's no API to internalize. The entire interface is a handful of fundamental HTTP concepts:

Request headers.Request methods.Query strings.Body data.

If you understand HTTP, you already understand CGI.

It's language and platform agnostic. You learn it once and the knowledge is good forever.

### Clear separation of concerns.

A modern web application typically puts a web server like nginx in front and reverse-proxies to an application server written in another language like Ruby, Python, Go, or Rust. That always felt a bit strange to me: you essentially have two web servers, and one of them is also responsible for your business logic.

CGI gives you a single web server that calls your business logic directly. It's clear who does what.

It makes debugging simpler, too. Your application is an ordinary program you can run from a shell: pipe it a request, watch stderr, step through it with gdb.

In a sense, CGI resembles serverless architecture: a supervisor invokes your code per request, hands it a bag of environment variables, and collects the result. CGI is serverless, minus the vendor (and surprise bills).

### Minimal supply chain risk.

With the rise of autonomous agents and weekly attacks on package repositories, it feels reassuring to have very few dependencies.

Most modern tech stacks come with a package manager and an ecosystem to go along with it. It's convenient, but the dependency graph balloons. One or two direct dependencies can pull in hundreds of indirect ones, each maintained by somebody you've never heard of, with publish credentials protected by a password reused since 2015.

My supply chain is a C compiler and three libraries. Compromising it would require compromising libcurl... a project the entire internet watches, not a package with eleven weekly downloads and an owner who left in 2019.

### Simple tooling.

I'm a minimalist at heart. I use classic Vim with zero plugins. That means no LSP, no autocomplete, no code formatters, and no AI.

Complex tech stacks demand complex tooling: they demand a language server to wade through the layers of abstraction. But this stack is simple enough a plain editor is all you need. The entire application is a directory of C files and a Makefile.

Open a file, read it, and you know what it does.

### Great tooling is within reach.

When you do want tooling, it's not far. Sanitizers, valgrind, gdb, ctags, cscope... these are mature (well, geriatric) tools that have been refined for decades and they're a package install away on any system that can compile C.

The maturity goes further than the tools themselves: integration is built into many editors. Vim ships with native support for ctags, cscope and has a graphical gdb frontend (see :h Termdebug).

### Writing HTML and CSS in C isn't too bad.

I was hesitant to write the entire frontend in C, but it wasn't nearly as painful as I imagined.

All too many times have I:

Fought vim to highlight Go's html/template syntax.Fought helix to detect Go templates without breaking html detection.Fought rustrover to recognize jinja templates for a project using askama.

Using C means there's no second language for your editor to half-detect, no mixed-syntax where highlighting falls apart, no plugin dance to get the two languages to cooperate.

It was refreshing to just write C. It isn't pretty, but neither is Tailwind.

### SQLite is a breath of fresh air.

I've always defaulted to Postgres for web applications. It's a great database, but it comes with some operational burden. There's a server process to babysit and frequent releases to upgrade to.

SQLite has none of that. There's no process, no configuration, no dependencies. Your application opens the database file directly. The operational burden is minimal.

## ## WHAT I WOULD CHANGE

CGI is an interface between a web server and your application. There's no framework or library. This means you get very little out of the box.

You need to write your own utilities to handle things like:

Cookie parsing and creation.Query parameter parsing and validation.Form data parsing and validation.Escaping input for display.

I rolled my own in a single header file (cgi.h), but I'm not convinced that was the right solution. Libraries likekcgiexist, but adopting one means buying into its API and security model.

I'd like to see a set of shared utilities that developers can drop in (like the stb libraries).

Maybe I'll publish cgi.h as a start.

## ## CONCLUSION

CGI is old, but it's not forgotten.

Most of the reasons we abandoned it in the early 2000s don't hold up today. Process forking isn't nearly as expensive as it was; modern kernels optimize it heavily.

And if the cost of forking ever became an issue, FastCGI is a simple enough upgrade.

Writing a modern web application in C is more than feasible—marketyour.gamesis a commercial product running on a single binary using a serving model that was officially standardized in 2004.

It has fewer moving parts than anything I've shipped before. I'll be reaching for this stack again.