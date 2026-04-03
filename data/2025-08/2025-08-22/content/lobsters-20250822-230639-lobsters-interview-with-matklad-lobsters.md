---
title: Lobsters Interview with Matklad | Lobsters
url: https://lobste.rs/s/ntruuu/lobsters_interview_with_matklad
site_name: lobsters
fetched_at: '2025-08-22T23:06:39.361736'
original_url: https://lobste.rs/s/ntruuu/lobsters_interview_with_matklad
date: '2025-08-22'
description: ☶
tags: person
---

1. 69Lobsters Interview with Matklad☶personauthored byveqq9 hours ago

I am targeting a fortnightly cadence, going forward.@susamand@zdsmithwill be next. I spoke with@matkladfor a few hours, resulting in this feast! Thank you to him and my proof readers!

Hi Matt!

My name is not in fact Matt.

Oh.

But I’m lax about my name. Anything unambiguous works! My name is too common where every 2nd guy has it!

What’s your computing environment like?

I worked at least half of my professional career on Rust tooling, so I care. But our tooling is so much worse than it could be that I don’t try to optimize it all that much. My journey went from Emacs to IntelliJ (working at JetBrains onIntellij-Rust), which at the time had unparalled capabilities to actually understand and edit your code as a statically typed language instead of just UTF-8 codepoints. It’s been a decade since that time when I was using IntelliJ, but I don’t think anyone is actually any closer to what IntelliJ was capable of doing a decade ago.

To give a simple example, while experimenting with vibe coding, it wrote stupid code where if a condition doesn’t hold we do this, otherwise we do that. Of course, you could just flip the branches to remove negation. My time with IntelliJ gave me the reflex to place my cursor on theifand do a code action to flip it. But even such a basic feature doesn’t work for TypeScript. You don’t even have to understand the language’s semantics to a deep level; it’s purely a syntax transformation.

Many programmers dream of working on a farm or living in the woods, but when I retire, I’ll just be coding Java in Intellij all day, because that was good and nothing else is really there.

I did not see that coming, I love it! What do you think keeps our tooling from getting there?

The most important part’s history. What the world looks like today’s determined by how it looked a year ago. It’s all supercontigent. Nobody really tried to make this work outside of JetBrains. In 2005, Martin Fowler wrotePost-Intellijand said they’d been talking about Smalltalk IDEs forever but finally had something next-level, which let you extract methods etc. The world forked at that point. People in the JetBrains ecosystem (IntelliJ and ReSharper) took it for granted, because it just worked. But no one else was doing it, because it’s a non-trivial problem. If you get IntelliJ-envy with C++, you’d think your compiler knows everything and ask it to parse and mark things but actually compilers are quite different. There were few successes outside of JetBrains, who weren’t interested in an open protocol until Microsoft came out with LSP. This was obvious, but no one’d cared yet. It wasn’t common for a language to have good tooling yet.

But we’re still behind the quality JetBrains was doing, because the last 20% requires a lot of effort and thoughtful language design. Now, tooling-friendliness was accidental with Java because it’s simple. But Go was explicitly designed to be tooling-friendly and has some of the best IDE support. But Rust has many features which make it hard to implement an IDE. A lof of effort goes into fighting the language semantics instead of implementing features. Earlier, before we expected great tooling by default, ecosystems couldn’t coordinate the concentrated effort necessary. With LSP and higher expectations, I expect everything to be good in a decade, but maybe we’ll abandon that static-type driven approach for LLMs.

What about editors for languages without types?

JS with TypeScript, Python, Ruby etc. now have types. If you have a language without ypes, maybe you should think about retrofitting them in. Add them for good tooling support the way TypeScript did instead of Python’s vague Platonic reasons. But at the same time, I’m very curious about this different branch of IDEs around image-based programming. I wish a huge fan of Smalltalk or Lisp Machines would write a blog post destroying IntelliJ, explaining how they were doing those things in the 80s! I’m not qualified to talk, but I think you could actually solve problems relying on language dynamics. Smalltalk had thisRefactoring Browser. If you want to rename a method, you need to update all call sites, which they did at runtime. So you didn’t rename the method but saidwhen you call this method, actually call me and make a list. So if you run your test suite, it discovers all the call sites dynamically which you update in the image. Obviously it works, but I’m skeptical about scale. It reminds me of REPL debates too. Lispers love their REPLs but it always felt like worse tests to me. Do you manually redo all those checks in the REPL again? REPL seems good for exploring, but not ensuring things remain correct. But why write tests to check if your variables’ names are correct when you could have a static type system? I believe doing it statically is strictly better (especially as the code base grows), but I’m not a zealot.

I find that talking about programming languages is misguided because languages do not really matter. What really matters is the runtime, and dynamic languages usually have pretty impressive runtimes. For example, you could have dynamic code loading: reading programs from disk into a running program and making them part of the running image. That capability is key in plugin-heavy systems like code editors and shells. Languages with static semantics and runtimes struggle here. But you’ll want static types eventually which isn’t always easy. That’s why Java’s brilliant. Java has a very dynamic runtime but a boring and standard static type system!

Then there’re questions of iteration speed and compilation time. There’s a platonic ideal of a statically typed, static language which compiles fast, but Rust is horribly slow to compile. Zig is slow too, because you still use LLVM. They’re working on it, but I’m on ARM…

If we were redoing our entire computing infrastructure from zero, would I have space for dynamically typed languages? Maybe something gradually TypeScript where you generally have static types but could match the shape of data and dynamically walk the code. Writing a compiler in Zig, you’d have a ton of code generation usingcomptime, but in TypeScript you can specify this is a multiplication expression or a file, they’re typed. Then there’s one function with objects and keys which maps or iterates through everything conveniently. So, even in this hypothetical Matklad computing universe, I’d still want some dynamicism for cross application scripting withJanetor Lua, so that users can include their own code in your program, e.g. mods for a game. But I would only allow one gradually typed language.

I love Janet!

In that hypothetical world where Matklad has infinite time, I definitely want to write a modern take on Emacs using Janet as the core language.

Have you seenLem?

I looked at it briefly but bounced because it clamors you with Common Lisp. There’s this war between Scheme and Common Lisp, but then there’s Janet which doesn’t care and doesn’t bother with hygienic macros. It’s just arrays and tables, not even cons cells, which feels like a strict improvement to me. I’m not a fan of syntactic metaprogramming. Lispers also valorize the languages to an excessive degree. Like, every language is Turing-complete and has capabilities for abstraction, it doesn’t really matter what language you use. It’s just a tool. Janet’s more pragmatic in this sense. So knowing nothing about Scheme or Common Lisp, I feel like Janet would be an all around better tool for writing a new Emacs.

I’m not a fan of extending languages syntactically because it feels like it makes systems harder to understand. It allows for some expressivity but it’s bounded. Zig’s comptime doesn’t operate on syntax but types, which is more natural and powerful. The synctactic approach creates beautiful but inscrutablesystems.

So for my ideal Emacs, I want like JavaScript with TypeScript syntax and semantics with UTF-8 strings. A reasonably fast and small implementation would be cool too, which is where Janet comes in again. I don’t think they do JIT compilation right now, but I’ve heard they’re working on it.

Interesting, I love making DSLs. What don’t you like about that approach?

I think Lisp falls into the same kind of trap as OOP. The big idea is that you have late binding, this very dynamic, extensible, flexible system. The problem’s that it helps 10% of your system, but 90% of your code shouldn’t be extensible. This is the solution to theexpression problem. Do you want to extend a data type in terms of variance or methods? Neither! 90% of the code should be concrete types like hash maps. You don’t want the user to extend your hash maps. The problem with OOP is that it puts this extensibility front and center, so all systems become extensible in ways they shouldn’t. Extensibility is a big constraint on how you can evolve your system and is a tax on understanding things.

Lisps excel at building new programming languages, because they solved parsing. They give you a balanced parenthesis sequence which you can trivially parse and transform. So if you’re working with languages, it’s the perfect tool. That’s what got me interested in Janet. At TigerBeetle, we support clients for 5-6 languages and I want to build an in-process model of TigerBeetle in the host language. So if you’re writing in Python and want to run tests, you don’t have to be in the TigerBeetle binary nor embed it, you’d just have a Python module which re-implements the same logic in Python. So I’m thinking of implementing the TigerBeetle state machine in an abstract language and then compile it down to Python, JavaScript, Java etc. Lisp is perfect for this. You start your abstract language with an intermediate syntax tree (IST) implemented as s-expressions, then lower it into syntax trees for Python, Ruby, whatever but also implemented as s-expressions. Then there’s a simple function which takes this Python IST and produces a string.

Lisps are really good at manipulating trees, but you don’t want to make every problem in your codebase a problem of defining your language. There’s a limited amount of languages you can keep in your head and you only want to go that far if the payoff is really great. With OOP, if you’re building an extensible code editor like VSCode, making the interface into an object-oriented program is a good idea, it’s exactly where you want this open-world extensibility and the vocabulary of OOP really fits. But you don’t want that through your entire codebase. It’s the same with custom languages. Sometimes you can benefit from a DSL, but don’t try to turn every program into one!

Could you go more into solving the expression problem?

You can extend a data structure in terms of data variance or operations. OOP lets you add more kinds of data to the same interface, sum types let you cheaply add more operations. But most of the time you want neither, your code should be absolutely closed. Rust’s hash map is not extensible, there’s no hash map trait because no one needs it. There’s also no reason to add a custom hash map operation. This is a pattern of general cognitive biases in programming; we think hard about expressivity, allowing stuff. But extensibility always has costs and good systems design is when you can limit extensibility. Good systems are extensible, but through a specific, narrow crisp interfaces.

How do you approach modeling a problem or domain?

The top level question’s whether I am modeling a program domain or what my CPU is actually going to do? These are two very different vantage points to approach programming from. On one hand, we have mathematical modeling, where you describe your problem as a mathematical object with some operations and how it is transformed over time. Your goal there, as a programmer, is to capture fuzzy intuition about the world into rigid, executable mathematical specifications. The other vantage point is what the CPU is doing, getting the most of your CPU cores and making every instruction count. You have to think in terms of bytes, CPU cycles, latency numbers etc.

So first, determine what regime you’re functioning in; because if you don’t have performance constraints, you should be thinking about modeling the problem for a human to understand. If you care about performance, you should think about what’s efficient to execute and change your problem to map cleanly to hardware. The purpose of computers ultimately is making things fast and you totally should change your problem, what your program is doing, to make it. If modeling things, I’ll try to identify some core abstraction, some invariance etc. But there’s always interplay. Rust, in particular, is pretty great and lets you do both at the same time, to some extent.

Second, think about the program and its evolution over time. Coding is easy. You can just write a program (or even ask a GPU to write it for you) and it’s there. Evolving it over time is hard. Can you change it? Are you promising any public interfaces? If I can change it tomorrow, I don’t care what I write today because I can always improve it. You could draw on paper what the nouns, verbs, data and fundamental data transformations are, figure out how it’ll evolve. But I don’t honestly do much upfront modeling. Normally, there’s just something obvious to do next, so I’m always doing that.

How do you approach writing a blog post?

If I have a good title, I’ll just write it all up then and there! If I can’t find a good title, it just sits in the drafts forever until I forget about it. If it doesn’t get done in one sitting, it won’t get finished. So I’ll sometimes stay up all night doing it, while still in theflow. This is why I write blog posts, not books: I can finish them before I die of starvation!

How do talks go? You can’t just wing it based on the title, because you have slides prepared!

The night before the talk! Talks are harder because they’re announced, while if I never publish a blog post I was working on,no one knows. But it’s too easy to commit to talks 6 months out, because only the future Matklad will have to deal with the consequences of my decisions today. Even if he’ll hate me now, he’s committed and has to push himself! But yeah, I’m not super keen on the talks; I like reading stuff. It’s quicker and gets into my brain better. The purpose of conferences aren’t really talks, but bringing like minded people to the same room for networking, collaborating, solving a coordination problem. But most talks would be better as a blog post.

How did you end up in programming?

At school, I didn’t program at all and only did mathematics, but I wanted to do something more tangible. However, in Russia, a software engineering degree is physics, analysis, differential equations, topology etc. so I do have a mathematically inclined brain. I tried a MA to see if I’d like theoretical computer science, but several months in, I realized proving theorems about Turing machines is fun, but what keeps me up at night was hacking on a little visualization of that Turing machine in JavaScript. The tangible part brought me to programming instead of proving theorems.

Do you write much JS these days?

I have VS Code extensions where I use it and routinely use the web stack for visualizations, GUIs etc. but like 2005-style. But I know flexbox, that’s super important! Before that, layouts were a complete nightmare!

How do you learn something new?

I always try to learn the underlying idea, not the actual thing. I try to just type the API, expecting stuff to be there. If it’s not, either the library is missing a feature or I need to fix my mental model. All knowledge is super compressible, so once you understand the general idea, you should be able to derive the rest and not need to learn every detail.

You mentioned that Rust is very good at both modeling for humans and the machine, how would you put compare Zig and others?

Zig is strictly a machine level language. An example for the last question, how do you learn Zig? You learn that it’s a DSL for producing machine code. Once you understand that, you’ll know why it has inline for. Because inline for is a way to specify a DSL that you want to have a similar but different fragment of assembly to be repeated.

I’d describe Rust as better than everything else. It’s notgreat, there’s a lot of stuff that could be better. Zig’s pretty close to optimal for its goal of producing machine code. There’s little fat to the language.

I’d love for you to explain the domain models of literally every technology possible, but that’s too much to ask. So, how do computers work? I mean, I read some books, did nand2tetris etc. so I know how they worked 40 years ago, but now that IST is emulating old machines, there’s magic everywhere… How do you know what’s going on, that Zig can be a DSL to? It seems inscrutable!

That’s a good question. To be honest, I also have a vague understanding about what my CPU is actually doing. We’re programming against x86 or Arm64 instruction sets, which are just abstractions. In my computer, there’s a smaller computer transforming my x86 program into an actual program for the hardware. It’s layers all the way down. Useful to keep in mind, Andrew Kelly’s definition of what systems programming is: Programming against the underlying platform APIs. So, programming for the browser, you can program in C because it’s the systems programming language, compile it into WASM and run WASM in the browser, but are you doing systems programming because it’s C? No! You can’t do browser systems programming in WASM, because systems APIs aren’t exposed to WASM today. Systems programming in the browser is necessarily in JavaScript, because that is the underlying system API, the final level without indirection you can code against.

So we can’t say what happens in a CPU, by design, because it gives designers flexibility to change things. As I was saying before, the most important thing about a system isn’t how you model a domain, but how you upgrade it! It’s remarkable how Apple could transition from Power to x86 to Arm, because they thought it through. When you code in Zig, you can’t know what happens underneath your assembly, beneath machine code, but you have tight control of the machine code while being target-independent, without inline assembly. There’s a fundamental abstraction required to make target-independence possible. It doesn’t prioritize particular patterns. For example, there are at least 2 ways to do dynamic dispatch. C++‘s style has an object start with an object header with a pointer to the vtable. Rust’s obviously superior way uses wide pointers with a pointer to the data and a pointer to the vtable, so you can flexibly combine arbitrary data and vtables, which Go and Swift also do. C++ and Rust hardcode these approaches. Zig provides you with nothing, so you have to write your own abstraction. You could do polymorphism throughFieldParentPtr, it doesn’t matter! But it’s the curse of choice, it’s on you as a programmer to build your primitive abstractions, which isn’t what you want to do if you’re programming in the mathematical domain modeling approach to software engineering. It’s important that Zig’s a language, not just portable micro assembly, because Zig enables you to abstract over those patterns or machine code. This is the difference of metaprogramming between Lisp and Zig: In Lisp you abstract source code, the text of your program, because a macro expands to the source code. In Zig, you want to abstract over and expand to machine code, thinking about copy-pasted fragments of assembly, not fragments of source code.

Circling back to Matklad’s user space redux…

Also kernel space! The user space is the easy part. A historical issue defining our computer landscape is that modern kernels try really hard to provide the illusion of a blocking API. You write a file, which takes time then you continue when it’s done. This is smoke and mirrors, this isn’t how hardware works at all! It’s always fire and forget: Write this, here’s a region of memory, wake me up when it’s over. It’s fundamentally asynchronous. The OS provides these thread and process abstractions which make you think the API’s blocking. The horrible side effect’s that language designers get an out of jail card for async programming, they don’t have to think about it! When writing to a file, they don’t need to make sure the bytes aren’t moved during the operation while running something. No, you just bind to the POSIX API and enjoy this blocking world illusion.

But historically, hyperscalers then found the blocking APIs kind of slow, so languages retrofitted async without planning for it, with mediocre results. We don’t know how to write asynchronous code, because we allow language designers to design languages which just rely on the OS for that part of the runtime. Coroutines are implemented in the kernel, but should be in languages, so I’d start with the kernel!

A friend wanted to know what you think of Zig’s async vs. Rust’s.

The biggest difference is that Rust async actually exists so you can use it, but Zig’s async doesn’t really exist yet. But it’s absolutely brilliant that Zig makes a sharp distinction between API used to express concurrency and asynchrony and the implementation. Zig says this is the API, how you model async flows, but the actual runtime might be synchronous or multi-threaded. This is good, because there are a lot of questions about how to implement asynchrony, again because we all rely on one suboptimal implementation in the kernel. Then we have a second implementation in the user space and they fight with each other.

But another can of worms is how you actually express that something’s concurrency. We don’t have any answers yet. I am slightly hesitant that Zig goes for a library based approach where creating an asynchronous flow of execution, a future, a coroutine is like a library call, I feel this has to be built into the language. I believe asynchrony is a universal construct like aforloop. You don’thaveto write a language with aforloop, you could usegotoorwhilebut we figured outforis a pretty universal construct, which wasn’t obvious before. Dijkstra wrote his diatribe about how we should do structured programming with this theory which proves howifandforare enough to code everything withoutgoto. It took some time to realize we didn’t have to use assembly but could write in high-level languages like C! With concurrency, I feel we’re still in thisgotophase. We try to solve it with library design, futures, promises, channels, nurseries, bundles… I think we need a few keywords like semicolon, where what’s before and after can go fully parallel or something. But I’m not a language designer. My observation’s that we don’t force language designers to answer this question, which is a shame.

So I’m really happy Zig distinguishes between implementation and interface, but sad the implementation is just a library, because it’s a local optimum. I think it makes sense to come up with 5 keywords to describe it like control flow, to describe everything, but don’t ask me what those 5 keywords are.

What are those 5 keywords?

Fundamentally, you want to describe a tree shaped stack. A stack which branches. You need keywords to:

* branch in 2
* branch to n
* allow a runtime this many branches in this tree (anaccept loopsays while accept pass this coroutine for this particular client. If you just do static concurrency, you couldn’t write those things)
* synchronization (let a = async work; let b = async work; join a and b;but not a promise

I don’t think you should expose promise as a construct. We don’t have a promise for an uninitialized variable likevar x = promise; x resolve foo;to access x. We just specify stuff such that we can only access a variable once computed. I think we could do the same for concurrency, scheduling things but only using them when guaranteed to be joined. But I’m not a language designer.

What is an OS to you?Introduction to Operating System Abstractions using Plan 9taught me it’s the whole interface to use your machine, including languages. My dream OS would even handle garbage collection and the database. You have a different model.

We don’t know the answers. I don’t necessarily think we know what an operating system is. Maybe tomorrow someone writes a Lisp machine which is actually good and we spend the next 50 years gluing legacy code into it. Or a glorious world where language-level abstractions correspond to hardware where you can’t break out of your abstractions. It breaks down to the question: What is a computer? We have 2 answers. Mechanically, a computer is linear memory which is executable, a Von Neumann architecture letting you do anything you want. But we can also say it’s a graph of objects which have a specific interface, you can write, compose and send messages. We might be going there, that’s what WASM with interface types is. There’s still linear memory as pokeable bytes, but it’s really a graph of individual objects with isolated heaps. I don’t know whether it’ll be successful or not, but it could be our entire future infrastructure. My gut feeling says we should expose the lowest level hardware denominator, but it’s not really true. Virtual memory is like a poorly done capability system. I’m excited aboutCHERI. I want to channel@carlanathat CHERI is not a replacement for Rust (by compiling C++ to CHERI for memory safety), CHERI is a replacement for virtual memory. Instead of slicing your address space into process granularity and suffering like TLB flushes and what not, when you switch processes you could do a faster and simpler system slicing memory into individual objects and passing capabilities to those slices. This doesn’t feel higher-level than what we have today, because it’s just more general virtual memory.

The key idea of a computer might be the interface, what you can program against, where there’s a kernel on the other side, which can change without breaking the interface. I have no idea how it should look, what belongs above and below the kernel etc. I don’t think current systems are the best, but we’re just locked in because of history.

Hare wants to be a hundred-year language, do you think Zig has what it takes?

I don’t believe in the concept of a 100-year language. We will have to change languages in the future. We aren’t even done with Moore’s law. It seems premature to commit to absolute stability. We should be open to change. Perhaps balance and build infrastructure for 20 years and think out how we’ll decommission and replace it with something better. This is why toolability’s such a crucial thing for a language. C++ gets it right. It’s a horribly complicated language, impossible to process automatedly, so it’s impossible to replace. When people invent a better Go, they’ll automatically translate it, it’s designed for it. But C++ will always be there because of some macro with undefined behavior. The smart thing is probably what Rust does, stability without stagnation. I’m glad Hare does have thisautomated transformationfor the currently unstable language, though I think it’s more useful when it is stable and you want to upgrade it.

For Zig, I don’t care. I use Zig for one particular purpose, writing TigerBeetle. The key’s that we don’t have dependencies, so upgrading is easy. Normally, upgrading the language is hard because dependencies start using the same version, but gradually want different versions and you have to decide which baby to throw out of the window. I think Zig had the ambition to release 1.0 in 3 years. But that might be Zig’s advantage. We already have a good enough systems programming language: Rust. Zig doesn’t have to chase stability, it could redo async await 5 times until it really gets it right.

Who chose Zig at TigerBeetle?

Joran, our founder, I think. He could have chosen C, Zig, Rust and it would have been fine. I wouldn’t have made it, because I was too enamored with Rust. Previously, Joran was working on Node.js with gigabytes of dependencies and the absolute advantage of Zig at the time was missing a package manager. Unfortunately for TigerBeetle, Zig now has a package manager but our strong culture lets us ignore this and fight the temptation of dependencies.

You said you were enamored in Rust, you fell out of love?

It’s a brilliant industrial language, already in Windows and Linux! That’s mindbogglingly unbelievable. In 2016 I would have said it’s only successful if it’d enter the kernels but didn’t think it’d happen this fast. But Rust isn’t as focused on low-level programming; it bridges high and low levels. So I wouldn’t have expected HTTP web services and RPC and still don’t think it’s the best possible language for these things. It’s still the best language out of what we have today.

Your blog has a bit about mentorship etc. How didyouactually learn?

Learning is funny. When finishing university, I thought I’d be a professional programmer! A junior developer with a mentor who could explain how to write production-ready code. For the first 8 years of my career, I searched for that mentor and realized I wouldn’t find them. Mentorship is a bright idea but didn’t work for me. I had to figure everything out from first principles, from books, trying things out. You can just learn programming, it’s not rocket science. I’ve written a lot about what I learned on my blog, which is just learning and thinking from first principles. A lot of it is just “I was thinking of x and tried it out.” People often ask me to mentor them, but it’s not scalable for me.

I just try to explain: If you want to be a writer, you write. If you want to be a potter, you make pots. But actively reflect on your code,deliberate practicealthough I don’t like the concept. Solve a problem, feel pain, understand why you’re feeling pain and form a hypotheses for how to avoid pain next time. It’s important to solve toy problems. This really surprised me, because I loved building toys as a young programmer. I’d code a red black tree with Java AWT, compilers or a database. I didn’t think they had any relationship to real things, but when I started working, real projects are the same as toys, just bigger and sometimes worse! Because you can throw away and improve a toy, but you can’t always fix architectural mistakes in production systems. Trust your own reflective brain, not mentors!

What’s on your mind lately?

LLMs. They’re not ground breaking for me yet, but if the trajectory continues everything will be so different in 10 years. My own personal strategy is that I check every 6 months whether I can automate myself away yet. Otherwise, I ignore the whole field because it’s not my own comparative advantage.

Terminals suck. Interfaces are important, but terminal interfaces are really bad. Yesterday, I learned a soul-breaking fact.stderris human readable andstdoutis structured output, a beautiful system, but if you actually use a terminal, a PTY device, they aren’t actually distinct. The two streams are erased going into the same terminal! We have this beautiful system, but then we put io coreutils on top to turn our file descriptor into adhoc device and adhoc controls. Let’s say I want to display color output from Zig build. Just capturing the output won’t give me colors, which makes sense. So I may not like them, but I can use ANSI escapes for colors and do my job and properly parse and render them like HTML. But you can’t do that without the kernel, asking it to make a pseudo terminal, giving Zig build’s process half and me the other, which is horrible! The power of an interface is having multiple implementations which behave the same, which terminals violate. Escape sequences are the same, I just want colors! (Though there is aCLICOLOR_FORCEenvironmental variable, but it’s pretty horrible.) Out of band signaling and literal signaling likeSIGWINCHis horrible. Also, I’m a human!

I use computers as a human and a stream of bytes as an interface isn’t convenient. I want to love text, but text for me is a grid of characters I can move my cursor around. So I want the concept of an Emacs buffer, elevated from a special thing in 1 editor to a coprimitive of the OS or an IPC thing. I dream of an API letting you implementMagitas a separate binary which talks to arbitrary clients. Such a rich and structured interface would offer great power, while remaining 100% text. But such things take a lot of time and effort. I’m not angry enough to dedicate 5 years of my life to shaving this particular yak, so I begrudgingly useGhosttyterminal, though terminals should die. There’s a path dependency, they are good enough, so people grow to like them.

If guys were to start from scratch on TigerBeetle, would it be different or worth doing?

I don’t think so. We are very happy with what we have built. We might tweak our domain model slightly. We have concept of pending transfer, a created but not finalized transfer which might be better modeled as a transfer scheduled in the future. Instead of saying this transfer gets voided in 2 days, you’d submit the original transfer and one scheduled in the future. But because of our stable interface we solve such problems differently. It’s not worth rewriting for that.

Automatic minimization for our simulator would be good. Right now, our simulator doesn’t do minimization. It finds the bug which is 10 GB of logs or it could be a shorter issue, but maybe not. That’s no attempt to smartly minimize this. I think it would be easy to retrofit minimization and if starting from scratch, I would. Full disclosure: I wanted to learn to build such systems but hadn’t worked on big distributed systems so I starting hacking on a toy. I thought a banking application doing transfers was a good distributed system which needs consensus, which is hard to test! So I needed proper randomized testing with minimization, which is easy with Rust’sarbitrarycrate. That’s howarbtestwas born. Then I found out about TigerBeetle and got on a call to show our simulators to each other. We were working on the same thing! But my toy simulator had working minimization while TigerBeetle doesn’t! In TigerBeetle today, we don’t have bugs so we don’t need a bug minimizer. But of course it took a while to get here. I spent a lot of time debugging with 20 GB log files and needed a minimizer because grepping 20 GB was realy inefficient. But actually, I’d already written a minimizer but not a grep. So I ended up writing my own grep replacementwindowand used that to fix the bugs.

But overall, TigerBeetle is a perfect piece of software.

Is anything else perfect?

SQLite!

As far as programming languages go, Zig. It strikes its intended target as close as possible. Rust is great, better than C++ and Java but there’s.for method access or::for namespaces which aren’t great. There are 5 comment syntaxes… There’s a lot of accidental complexity in Rust while Zig’s really tight. If you removed a single primitive from the language, it’d fall apart.

Thefishshell has a perfect interface and was a major influence in how I think about building tooling without needing any configuration. I’ve been using it since ~2014, before I started doing Rust.
