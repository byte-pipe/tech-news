---
title: TruffleRuby
url: https://chrisseaton.com/truffleruby/
site_name: hackernews_api
content_file: hackernews_api-truffleruby
fetched_at: '2026-04-01T19:28:06.758749'
original_url: https://chrisseaton.com/truffleruby/
author: tosh
date: '2026-03-28'
description: TruffleRuby
tags:
- hackernews
- trending
---

TruffleRuby started asmyinternship project atOracle
Labsin early 2013. It is an implementation of theRubyprogramming language on the JVM, using theGraal dynamic compiler and the Truffle AST interpreter
framework. TruffleRuby can achieve
peak performance well beyond that possible in JRuby at the same time as being a
significantly simpler system. In early 2014 it was open sourced and integrated
intoJRubyfor incubation, then in 2017 it became its
own project, and now it is part ofGraalVM. It was
the subject of myPhD, and since 2019Shopifyhas sponsored development.

This page links to the literature and code related to the project. Note that any
views expressed are my own and not those of Oracle.

Finalist, Ruby Prize, 2016

# Blog Posts and Articles

* Stamping Out Overflow Checks in Ruby. Can you remove overflow checks on integer arithmetic in Ruby?
* The Future Shape of Ruby Objects. How does TruffleRuby represent objects and could MRI do the same?
* Seeing Escape Analysis Working. Can we see escape analysis working in practice?
* Understanding Basic Truffle Graphs. How can you make sense of Graal graphs from Truffle?
* Context on STM in Ruby. What is STM and how does it apply to Ruby?
* Seeing Register Allocation Working in Java. Can se we the theory of register allocation working in practice?
* Understanding Basic Graal Graphs. How can you make sense of Graal graphs?
* Understanding Programs Using Graphs. What can we learn about a program using graphs?
* Low Overhead Polling For Ruby. How can Ruby check for interruptions without a branch?
* Top 10 Things To Do With GraalVM. What does GraalVM actually do?
* Ruby Objects as C Structs and Vice Versa. How you can use Ruby objects as if they were C structs and C structs as if they were Ruby objects.
* Understanding How Graal Works. A Java JIT Compiler Written in Java.
* Flip-Flops — the 1-in-10-million operator. Do people actually use flip-flops?
* Deoptimizing Ruby. What deoptimization means for Ruby and how JRuby+Truffle implements and applies it.
* Very High Performance C Extensions For JRuby+Truffle. How JRuby+Truffle supports C extensions.
* Optimising Small Data Structures in JRuby+Truffle. Specialised optimisations for small arrays and hashes.
* Pushing Pixels with JRuby+Truffle. Running real-world Ruby gems.
* Tracing With Zero Overhead in JRuby+Truffle. How JRuby+Truffle implementsset_trace_funcwith zero overhead, and how we use the same technique to implement debugging.
* How Method Dispatch Works in JRuby/Truffle. How method calls work all the way from AST down to machine code.
* A Truffle/Graal High Performance Backend for JRuby. Blog post announcing the open sourcing.

# Research Papers and Thesis

* B. Daloze, A. Tal, S. Marr, H. Mössenböck, E. Petrank.Parallelization of Dynamic Languages: Synchronizing Built-in Collections. In Proceedings of the Conference on Object-Oriented Programming, Systems, Languages, and Applications (OOPSLA), 2018.PDF
* J. Kreindl, M. Rigger, and H. Mössenböck.Debugging Native Extensions of Dynamic Languages. In Proceedings of 15th International Conference on Managed Languages & Runtimes (ManLang), 2018.PDF
* K. Menard, C. Seaton, and B. Daloze.Specializing Ropes for Ruby. In Proceedings of 15th International Conference on Managed Languages & Runtimes (ManLang), 2018.PDF
* M. Van De Vanter, C. Seaton, M. Haupt, C. Humer, and T. Würthinger.Fast, Flexible, Polyglot Instrumentation Support for Debuggers and other Tools. In The Art, Science, and Engineering of Programming, Vol. 2, No. 3, 2018.PDF
* M. Grimmer, R. Schatz, C. Seaton, T. Würthinger, M. Luján.Cross-Language Interoperability in a Multi-Language Runtime. In ACM Transactions on Programming Languages and Systems (TOPLAS), Vol. 40, No. 2, 2018.PDF
* T. Würthinger, C. Wimmer, C. Humer, A. Wöss, L. Stadler, C. Seaton, G. Duboscq, D. Simon, M. Grimmer.Practical Partial Evaluation for High-Performance Dynamic Language Runtimes. In Proceedings of the Conference on Programming Language Design and Implementation (PLDI), 2017.PDF
* B. Daloze, S. Marr, D. Bonetta, H. Mössenböck.Efficient and Thread-Safe Objects for Dynamically-Typed Languages. In Proceedings of the ACM International Conference on Object Oriented Programming Systems Languages and Applications (OOPSLA), 2016.PDF
* C. Seaton.AST Specialisation and Partial Evaluation for Easy High-Performance Metaprogramming. In Proceedings of the 1st Workshop on Meta-Programming Techniques and Reflection (META), 2016.PDF,Slides
* C. Seaton.Specialising Dynamic Techniques for Implementing the Ruby Programming Language. PhD thesis, University of Manchester, 2015.Abstract,PDF
* M. Grimmer, C. Seaton, R. Schatz, T. Würthinger, H. Mössenböck.High-Performance Cross-Language Interoperability in a Multi-Language Runtime. In Proceedings of 11th Dynamic Languages Symposium (DLS), 2015.PDF
* F. Niephaus, M. Springer, T. Felgentreff, T. Pape, R. Hirschfeld.Call-target-specific Method Arguments. In Proceedings of the 10th Implementation, Compilation, Optimization of Object-Oriented Languages, Programs and Systems Workshop (ICOOOLPS), 2015.PDF
* B. Daloze, C. Seaton, D. Bonetta, H. Mössenböck.Techniques and Applications for Guest-Language Safepoints. In Proceedings of the 10th Implementation, Compilation, Optimization of Object-Oriented Languages, Programs and Systems Workshop (ICOOOLPS), 2015.PDF
* S. Marr, C. Seaton, S. Ducasse.Zero-Overhead Metaprogramming: Reflection and Metaobject Protocols Fast and without Compromises. In Proceedings of the 36th Conference on Programming Language Design and Implementation (PLDI), 2015.PDF
* M. Grimmer, C. Seaton, T. Würthinger, H. Mössenböck.Dynamically Composing Languages in a Modular Way: Supporting C Extensions for Dynamic Languages. In Proceedings of the 14th International Conference on Modularity, 2015.PDF,
* A. Wöß, C. Wirth, D. Bonetta, C. Seaton, C. Humer, and H. Mössenböck.An object storage model for the Truffle language implementation framework. In Proceedings of the International Conference on Principles and Practices of Programming on the Java Platform (PPPJ), 2014.PDF
* C. Seaton, M. L. Van De Vanter, and M. Haupt.Debugging at full speed. In Proceedings of the 8th Workshop on Dynamic Languages and Applications (DYLA), 2014.PDF,Code

# Videos of Talks and Slide Decks

* Chris Seaton.Ruby’s Core Gem. RubyConf. 2022.Slides.
* Chris Seaton.Ruby’s Call-Site Behaviour - An Advertisement for Sophie Kaleba’s Research. Lightning Talk, RubyConf Mini. 2022.Slides.
* Maple Ong and Chris Seaton.Call-Target Agnostic Keyword Arguments. At the Graal Workshop 2022.Videoandslides.
* Stefan Marr, Octave Larose, Sophie Kaleba, and Chris Seaton.Truffle Interpreter Performance without the Holy Graal. At the Graal Workshop 2022.Slides.
* Chris Seaton.A History of Compiling Ruby. At RubyConf 2021.Videoandwebsite.
* Chris Seaton. Understanding JIT Optimisations By Decompilation. At QCon Plus Online 2021.
* Chris Seaton.The Importance of Optimising Little Languages. At VMM 2021.Video.
* Chris Seaton.The Future Shape of Ruby Objects. Keynote at RubyKaigi 2021.Videoandblog post.
* Chris Seaton.Understanding Graal IR. At VMIL 2020.Video.
* Chris Seaton.Visualizing Graal. At Science, Art, Voodoo: Using and Developing The Graal Compiler 2020.Slidesandvideo.
* Chris Seaton.The TruffleRuby Compilation Pipeline. At Wroclove.rb 2019.Slidesandvideo.
* Chris Seaton.Graal: where it’s from and where it’s going, keynote. At the Graal Workshop 2019.Slides.
* Chris Seaton.Ten Things To Do With GraalVM. At Oracle Code One 2018.Slides.
* Eric Sedlar and Chris Seaton.Run Programs Faster with GraalVM. At Oracle Code Boston 2018.Video.
* Chris Seaton.Understanding How Graal Works - a Java JIT Compiler Written in Java. At JokerConf 2017.Slides,videoandblog post.
* Chris Seaton.Polyglot From the Very Old to the Very New(keynote). At PolyConf 2017.Slidesandvideo.
* Chris Seaton.Turning the JVM into a Polyglot VM with Graal. At Oracle Code London 2017.Slidesandvideo.
* Chris Seaton.Ruby’s C Extension Problem and How We’re Fixing It. At RubyConf 2016.Slidesandvideo.
* Chris Seaton.Faster Ruby and JavaScript with GraalVM. At JavaOne 2016.Slides.
* Chris Seaton.Using LLVM and Sulong for Language C Extensions. At the LLVM Cauldron 2016.Slidesandvideo.
* Chris Seaton.JRuby+Truffle: Why it’s important to optimise the tricky parts. Virtual Machines Summer School (VMSS) 2016.Slidesandvideo.
* Chris Seaton.Guilt Free Ruby on the JVM. At JavaOne 2015.Slides.
* Chris Seaton and Benoit Daloze.A Tour Through a New Ruby Implementation. At FOSDEM 2015.Slides.
* Chris Seaton.Deoptimizing Ruby. At RubyConf 2014.Video,slidesandblog post.
* Chris Seaton.Implementing Ruby Using Truffle and Graal. At the European Conference on Object Oriented Programming (ECOOP) Summer School. 2014.Slides.
* Christian Wimmer and Chris Seaton.One VM to Rule Them All. At the JVM Language Summit. 2013.Videoandslides.
* Charles Nutter.Beyond JVMtalk at Sydney in December 2013 made some references to this work in the context of JRuby. Also avideoof a talk with earlier details at Baruco 2013.

# Source Code

* TruffleRuby code
* Graal and Truffle code