---
title: Shae Erisson's blog - Tools built on tree-sitter's concrete syntax trees
url: |
  https://www.scannedinavian.com/tools-built-on-tree-sitters-concrete-syntax-trees.html
site_name: lobsters
fetched_at: |
  2025-06-01T23:46:30.372817
original_url: |
  https://www.scannedinavian.com/tools-built-on-tree-sitters-concrete-syntax-trees.html
date: 2025-06-01
tags: compilers, editors, practices
---



# Tools built on tree-sitter's concrete syntax trees

    Posted on 2025-05-31


# What is this all about?

Lots of surprisingly powerful tools have been built on top of tree sitter, and I just found out about them!

I thought weâd need real AST tools, which tree sitter doesnât have. I was wrong, thereâs so much awesome!

If youâre not interested in the background, or you already know it, skip down to the tools section!

# Refactoring and abstract syntax trees

Decades ago I got excited about refactoring browsers and read all the research.
A refactoring browser parses your source code to anabstract syntax tree, modifies that structured representation, and then unparses back to source code.
I figured all languages would have these amazingly powerful tools by 2010, but it hasnât happened.

(Also, I canât find any good descriptions of the power of a refactoring browser on the internet, so that goes into my list of blog post ideas.)

# concrete syntax trees?

Microsoft came up with this cool idea, thelanguage server protocol. The idea is that each programming language can build their own tools for interactive use, and use a single API to hook them into any editor. LSP isok, I guess.

Github came up withtree sitter, a parser generator. In my view itâs another editor agnostic slice of the interactive software development experience, but for incremental parsing of source code.

At first I was excited, maybe tree sitter would be a good base for editor agnostic refactoring tools?

I foundthis issue, which says roughly âno, you cannot make a refactoring browser with tree-sitterâ.

Turns out, you can get pretty close though!

# COOL TOOLS

## difftastic

Honestly,difftasticis just better than any diff program that does not use a syntax tree. The linked image doesnât do it justice if you havenât spent much time puzzling over a git diff. Install it now!

If you use emacs and magit like I do, I recommend thedifftastic.ellibrary.

After I linked difftastic, one of my friends immediately used difftastic to find a stealthy bug, five stars!

## combobulate for emacs

What if you want to navigate (and edit) your program via the parsed source code? Trycombobulate! Like most of these tools, the description doesnât do it justice, you have to try it!

Since it uses all the same emacs key bindings, my navigation was instantly improved.
Iâm still wrapping my head around the large amount of editing functionality, but being able to smoothly reorder definitions in a file is immediately useful to me.

## cursorless for voice navigation

I know two people who damaged their arms from too much code, and theyâve switched to usingcursorlessso they can fluently (voice pun?) navigate source code.

This yet another case where the description might not sound impressive, but after watching one friend use cursorless, Iâm considering using this myself.

## mergiraf

So you tried difftastic and it was AMAZING, right?

Wouldnât you like that same functionality to simplify complicated merges in git?

You wantmergiraf! I havenât started using this yet, but if itâs the same power increase I got from difftastic, itâs gonna be great!

## more links

I ended up asking on mastodon if there were more cool tools in this area and got a list:

## What about languages that donât exist yet?

From what Iâve seen, all the above tools focus cool tricks with existing languages.

I heard frombugarelathatTopiaryuses tree sitter to make language formatters like rust-fmt or gofmt, but for your own custom language. (In this case, bugarela is the lead dev onQuint, an updated take on TLA+)

## What did I miss?

If you know of a cool tree sitter related tool that I didnât mention, or especially if you know of research papers comparing the expressive power of ASTs and CSTs, I want to hear about it!
