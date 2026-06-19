---
title: 'CS 6120: The Self-Guided Course'
url: https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/
site_name: hackernews_api
content_file: hackernews_api-cs-6120-the-self-guided-course
fetched_at: '2026-06-19T12:23:44.959979'
original_url: https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/
author: ibobev
date: '2026-06-18'
description: 'CS 6120: Advanced Compilers: The Self-Guided Online Course (2020)'
tags:
- hackernews
- trending
---

# CS 6120: Advanced Compilers: The Self-Guided Online Course

CS 6120 is a PhD-levelCornell CScourse byAdrian Sampsonon programming language implementation.
It covers universal compilers topics like intermediate representations, data flow, and “classic” optimizations as well as more research-flavored topics such as parallelization, just-in-time compilation, and garbage collection.
The work consists of reading papers and open-source hacking tasks, which useLLVMandan educational IR invented just for this class.

This page lists the curriculum for following this course at the university of your imagination, for four imagination credits (ungraded).
There’s a linear timeline of lessons interspersed with papers to read.
Each lesson has videos and written notes, and some haveimplementation tasksfor you to complete.
Tasks are all open-ended, to one degree or another, and are meant to solidify your understanding of the abstract concepts by turning them into real code.
The order represents a suggested interleaving of video-watching and paper-reading.

Some differences with the “real” CS 6120 are that you can ignore the task deadlines and you can’t participate in our discussion threads on Zulip.
Real 6120 also has an end-of-semester course project—in the self-guided version, your end-of-semester assignment is to change the world through the magic of compilers.

The instructor is a video production neophyte, so please excuse the production values, especially in the early lessons.
CS 6120 isopen source and on GitHub, so please file bugs if you find problems.

When you finish the course, please fill outthis feedback form.

# Lesson 1:Welcome & Overview

* video

* Producing Wrong Data Without Doing Anything Obviously Wrong!Todd Mytkowicz, Amer Diwan, Matthias Hauswirth, and Peter F. Sweeney. ASPLOS 2009.
* SIGPLAN Empirical Evaluation Guidelines

# Lesson 2:Representing Programs

* representing programs
* getting started with Bril

# Lesson 3:Local Analysis & Optimization

* simple dead code elimination
* local value numbering

# Lesson 4:Data Flow

* data flow
* implementation task

# Lesson 5:Global Analysis

* global analysis & optimization

* Efficient Path ProfilingThomas Ball and James R. Larus. MICRO 1996.

# Lesson 6:Static Single Assignment

* static single assignment

* Provably Correct Peephole Optimizations with AliveNuno P. Lopes, David Menendez, Santosh Nagarakatte, and John Regehr. PLDI 2015.

# Lesson 7:LLVM

* introduction to LLVM
* writing an LLVM pass

# Lesson 8:Loop Optimization

* video

# Lesson 9:Interprocedural Analysis

* video

* Type-Based Alias AnalysisAmer Diwan, Kathryn S. McKinley, and J. Eliot B. Moss.

# Lesson 10:Alias Analysis

* video

* A Unified Theory of Garbage CollectionDavid F. Bacon, Perry Cheng, and V. T. Rajan. OOPSLA 2004.
* Fast Conservative Garbage CollectionRifat Shahriyar, Stephen M. Blackburn, and Kathryn S. McKinley. OOPSLA 2014.

# Lesson 11:Memory Management

* video

* An Efficient Implementation of SELF, a Dynamically-Typed Object-Oriented Language Based on PrototypesC. Chambers, D. Ungar, and E. Lee. OOPSLA 1989.
* Trace-Based Just-in-Time Type Specialization for Dynamic LanguagesAndreas Gal, Brendan Eich, Mike Shaver, David Anderson, David Mandelin, Mohammad R. Haghighat, Blake Kaplan, Graydon Hoare, Boris Zbarsky, Jason Orendorff, Jesse Ruderman, Edwin W. Smith, Rick Reitmaier, Michael Bebenita, Mason Chang, and Michael Franz. PLDI 2009.

# Lesson 12:Dynamic Compilers

* Dynamic Compilers
* Tracing via Speculation

* Superoptimizer: A Look at the Smallest ProgramAlexia Massalin. ASPLOS 1987.
* Chlorophyll: Synthesis-Aided Compiler for Low-Power Spatial ArchitecturesPhitchaya Mangpo Phothilimthana, Tikhon Jelvis, Rohin Shah, Nishant Totla, Sarah Chasins, and Rastislav Bodik. PLDI 2014.

# Lesson 13:Concurrency & Parallelism

* video

* Threads Cannot Be Implemented as a LibraryHans-J. Boehm. PLDI 2005.
* Exploiting Superword Level Parallelism with Multimedia Instruction SetsSamuel Larsen and Saman Amarasinghe. PLDI 2000.
* A Type and Effect System for Deterministic Parallel JavaRobert L. Bocchino, Vikram S. Adve, Danny Dig, Sarita V. Adve, Stephen Heumann, Rakesh Komuravelli, Jeffrey Overbey, Patrick Simmons, Hyojin Sung, and Mohsen Vakilian. OOPSLA 2009.
* Formal Verification of a Realistic CompilerXavier Leroy. CACM in 2009.

# Lesson 14:Fast Compilers