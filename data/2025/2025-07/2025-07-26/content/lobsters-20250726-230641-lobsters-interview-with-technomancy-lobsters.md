---
title: Lobsters Interview with Technomancy | Lobsters
url: https://lobste.rs/s/terwiu/lobsters_interview_with_technomancy
site_name: lobsters
fetched_at: '2025-07-26T23:06:41.413995'
original_url: https://lobste.rs/s/terwiu/lobsters_interview_with_technomancy
date: '2025-07-26'
description: ☶
tags: interview, person
---

1. 132Lobsters Interview with Technomancy☶interviewpersonauthored byveqq25 hours ago(hidden by 4 users)

I am resurrectingLobsters interviews. Although the interview becoming the next interviewer is a really cool conceit, it didn’t pan out for longevity.

This is the result of one and a half hours talking totechnomancy. (Icefoxandhwayneare next.)

Past interviews started off with introducing yourself, what do you do for work etc. But you’re not so interested in your work-work.

I started programming as a kid, but fell off the wagon for a while. In college, I got back into it, and around graduation, around 2004, got really into Ruby, at its inflection point. I didn’t exactly get tired of it, but my eye caught something shinier with Clojure and functional programming, which was really in around 2008-9. Like, everyone saw Moore’s law tapering off and thought of functional programming as the solution, the way forward. Now, I’m still doing that professionally but I got disillusioned with…

You once mentioned it wasn’t meant for hobby projects, everything added’s for corporate use

Yeah, I guess to take a step even further back, I got really interested in the free software movement, kind of idealistic in this idea that you could make the world a better place with software! And open
source, because I felt like that was the same thing. The idea was by picking the right
license you can write software that makes the world better, which doesn’t actually make any
sense because like, what is the software doing? Without more analysis, people think they’re like being altruistic, developing open source and it ends up just being free labor for companies to exploit. So I got disillusioned with the JVM in terms of that. Like, if I’m going to get paid for it, it’s fine.

But it’s really good at solving problems companies have, not humans. So I wanted to change how I was going to spend my free time. From there, I got really into Lua, playing around, making games with my kids, using love2D, for 3-4 years. But then I found this compiler Fennel that applied what I learned in Clojure to Lua. I eventually took over the project and been running it since since then. That’s where most of my headspace is right now.

Was what took you away from Ruby similar to what pulled you from Clojure?

No, with Lua, I wanted to deliberately step back from the corporate world, which didn’t play into leaving Ruby before. But there are some similarities. I got into both when they were hitting their inflection points. You reallyhad to be therein 2004 with Ruby or 2008 with Clojure. No one would do it because they thought it was good for their career, but because you just really wanted to learn more and expand your horizons. It was like the reason I came didn’t apply anymore, this is mature, I’ve learned a lot from this, but I don’t feel like I’m learning anymore.

You mentioned the Moore’s loss stopping, slowing down. Maybe 5 or 8years after, I personally noticed it, which pushed me in the other direction ofwait, all these functional things like map, we’re wasting all these cycles. Maybe we shouldn’t be doing that.

It’s an interesting tension, right? The zeitgeist was like, if Moore’s law’s slowing down
it wasn’t that computer’s wouldn’t be more capable, but where would the capability come from? Going wide, adding more cores, scaling out instead of up, right? Until that point, in the the 90s and early 2000s, it was like, boom, boom, boom,
our clock speeds were just going higher and higher. That’s what stopped.

Now, we were doing largely server side programs, so each server was going to have more cores and you’d throw in more
servers. Erlang got a big boost in popularity. Relatively, for the niche nerds. But we thoughtthis is the future. If you make it easier to spread out across multiple processes, you’re not going to not hit this problem. You’re not going
to run into a wall. That resonated a lot with people and kicked off interest in algorithms that are easy to paralyze, which you get for free with immutable data. So functional programming
became a lot more appealing, but as you mentioned, there’s also overhead.
If you can override a value in place, that’s faster than than making a
a functional update. There’s a place where that overhead won’t make sense, especially in the context of a single core, running on a more constrained hardware, maybe on mobile or on your laptop, you’re not going to want to just
throw more cores at it in the same way.

So it actually fits with the human vs. business related software.

Yeah. You you want to pay more attention to efficiency. If you’re if you’re a startup with all this investor money,
and the community in the late 2000s had all this investor money sloshing around, you can solve your problem by throwing
more cores at it. I think ironically, the wave of interest in functional
programming didn’t end up… Maybe I’m extrapolating here, but even imperative languages, you’re going to run in a
similar way. You’re going to run a bunch of processes behind a load balancer and the point of
synchronization is going to be the database anyway. So using a
functional language isn’t necessarily going to make it easier for you to go wide on that.
If you’re tied to a request response cycle, then your load balancer is going to do
the job for you. And everything’s web based, so you’re almost always tied to a request
response cycle.

There are exceptions. If you want to keep one socket open for an extended period of time, which Erlang handles more gracefully, that is really hard to do with a load balancer. But when you’re dealing with everything going over HTTP, it’s not really the silver bullet we expected.

What’s your workspace and computing environment like? We’ve talked about this onIRC, about decks and keyboards.

My main machine is what I call aThinkPad fanfic, takes a chassis of a ThinkPad from like 2009. This hacker collective
in Shenzhen redesigned the motherboard with a more modern CPU and architecture, which fits right into that.
The screen’s a little dim, but everything else is great, the replaceable battery, old school ThinkPad keyboard.

But the majority of the time I’m using the keyboard I designed myselfthe Atreuswith 42 in the original, 44 keys now, with each side angled to match where your hands are. But really portable because I,
I love going out all the time, at least a couple times a week to coffee shops or when weather’s nicer, a park or something. I got the original Ergo Docs and I loved it. At home, it felt so good, but then pulling it out with all the wires at the coffee shops…

In my office, I have an older ThinkPad with two portrait display monitors and a big old Kensington track ball, almost a billiard ball size. I like that a lot. But I prefer keyboard shortcuts. I use Emacs. And then there’re surfing keys in the browser extension I use to highlight links so I can visit the links with the keyboard. That’s pretty nice.

Do you have your Emacs config online somewhere?

Yeah,all my dot filesare together. Emacs and everything else. Yeah. But

I use Emacs as my window manager usingexWMso every program running in Xorg is shown as if it was an Emacs buffer. So your regular Emacs screen splits instead of having text files inside of them. There’s Firefox, your terminal, whatever else.

Did Emacs come before closure or vice versa?

I started with Emacs in in university. I had just learned Dvorak and was like, now Vim or Emacs? In Vim, HKJL are all lined up for QWERTY and… forget it. So Emacs and Elisp.

When I started thinking about functional languages,
a lot of people were talking about Haskell and Erlang, butI liked this Lisp thing.

Did you have any favorite courses or such? Like in some corners,
people love to obsess over SICP.

My CS program wasn’t really great. I learned more from all the hacking I did to get Linux working on a laptop in 2003 than in classes. But recently I’ve been working through this book called Elements of Computing Systems,nand2tetris, with my kids, in upper high school. I was trying to stay ahead of them, but it’s summer. There’s no way I can do that. But I like how every step is built on the previous step; you can’t use anything until you’ve derived it from first principles. And how far can that approach get you? It turns out pretty far!

Did you discover Lua games through programming with your kids or making games for, with them? When you first had kids, did you think oh I love programming and need to share it?

Yeah. I think it’s normal to want to share what you’re interested in, with the kids and especially if they show interest and get on board. And games are just such a great way to learn, in general. It’s easy to get people and kids’ attention with games. And they’re curioushow did they do that? Let’s take a look.So we first started inScratch, a drag and drop programming environment which is great for younger kids.
You don’t have to know how to type but it still lets you do step by step algorithms etc. And more importantly, if it doesn’t work the way expected, it teaches you how to debug that and how to break the problem apart and try to find e.g. where you didn’t quite cover all the bases or whatever.

One of the coolest things about scratch is that when you publish something, anyone else can view source, how was it made, and then more importantly remix, like make a copy you can edit yourself and change, to, you know, make the characters move faster or see what happens when the shots are fired at a different angle. Experimenting is amazing when you’re trying to explore the world of how software works. I wish everything would work like that. It’s really empowering.

One of my more recent projects isfedibot.clubwhere you can you can create these scripts that get tied into social media bots, to run either on a schedule or in response to replies and your script and do whatever.
And this is really, really fun, just as kind of a toy to mess around with social media, but also great fit for
Lua because Lua makes it really easy to sandbox code and limit what you have access to,
to make sure one person can’t write a script that will take the whole system down.

Then on top of that, I was able to add this same remix ability. So when you see one of these bots, maybe they’ll
have a link in their bio to the source. You go to their source code, log in and boom, you test it, change it, do something a little different! I really admired Scratch and its model of view source. View source is so important for learning how to program, how a technique is done. You shouldn’t have to go search on GitHub then clone it, it should be right there, on your fingertips. Being able to read it isn’t really enough because there’re limits to how reading code without executing it.

(Later insert, today on IRC, he said:)

Using emacs is praxis because it gives people a view into how computing should be; view-source on every command, immediately rewrite things to work the way you want.

I feel we don’t understand this very well from a scientific perspective. Why is this
true? For most things, you can just read a book and understand it. But reading a piece of code,
interacting with it, running, modifying it, those are so different! In terms of how you experience them and how it affects your understanding of the problem.

There’s a really great paper on this calledProgramming as Theory Building. It doesn’t even try to explain why, which is kind of funny. But it goes and talks about the implications of when you understanding. When you have a piece of code, what you really have, what’s really valuable is not the code, but the the knowledge in heads of the people developing it. That’s what you’re building. The code is almost a side effect of that. Once you have the theory about how the system works, the code itself is not that big of a deal. A lot people don’t understand that about working on a team and building programs.

How do you actually approach modeling? Like, you have a problem. What do you do with it?

So with Fennel, I’m doing language design. And one most important skills for language design is just having enough imagination to try to think of all the ways how five years from now, we could be looking back on this, wishing if only we had known better and not done this. If you have an idea, what are the ways you’ll potentially regret it? It’s really hard and I think it can only come from experience.

Everyone’s really leaning into language server protocol nowadays, right? You have this kind of
standardized tooling, which enables certain analysis on on your project, when you made a mistake immediately instead of having to wait.
I was a skeptic. but I’ve been won over. But it’s very difficult to do this safely. In Clojure, if you want to run the language server on a program or a file, you don’t want to compile the program because in Clojure compiling it runs it, which isn’t uncommon in dynamic languages. Obviously, the problem’s that you don’t know if you trust the code. And how do you know if you
should trust the code? By opening it up in your editor and reading it! But opening it up runs it? A chicken and egg problem. A lot of language servers just don’t care and run it anyway, which is really bad. I thought Clojure would too, because it’s so dynamic, but they built out a completely separate static analysis tool in the language server that does the job of the compiler, redundantly, safely, because it won’t to try to expand the macros. That’s great, the right choice with Clojure.

But it sucks to not expand your macros. Sometimes the macro will introduce a new local variable and you… don’t see where it comes from, it looks like an error. So what can we learn from this experience? How can we run macros in a safe way? Well, why should a macro be able to write to disk, to open a network connection? That doesn’t make any sense. No one writes macros with legitimate reasons to open a network connection.

I totally do. I love to use macros to prepare the environments, download data and compile with those.

Yeah, there are legitimate use cases to read from disc, but to write to disk, to send… Even if you do allow writes, never outside the project directory! But it’s too late for Clojure, hundreds of thousands have been written. But Fennel didn’t have a macro system yet. Okay, so macros are like functions; they take and produce ASTs. There’s no reason to be able to do output anything else. So we made our macro system work that way, so the Fennel language server doesn’t have the problem Clojure’s has, even though there’s a a tiny amount of comparative effort in this system. It’s smaller, with less resources, but capable of more because we learned from the situation.

The commitment to backwards compatibility is hard. Sometimes you have to stick with these decisions you don’t like. And how can you avoid that, really learn from your own mistakes or learn from someone else’s mistakes? I like defaulting to saying no until you’ve really got the chance to think it all the way through. We can do what we’re confident now and extend later, but you can’t go the other way and sometimes people are too fast.

Outside of language design, the most general design principle a really thoughtful coworker had one trick: “Take it apart!” Like, this thing is causing you trouble, but it’s really two things. Think about how to untangle them and reason about them separately. It sounds like such generic advice, but it’s a really good lens to approach problems with.

Is there a special Clojure word for that?

Rich calls it “decomplecting.” He has a talkSimple Made Easybut it wasn’t until I saw it in action through my coworker’s work that I truly appreciate what it means. Taking it apart’s the one trick for 90% of design problems.

How do you choose what problem to actually work on? Out of so many problems, so much information, fun things…

Let me just take a step back. We’ve had the rise in the past 10,
15 years of hosted languages, right? Clojure lives on the JVM. It’s not Java.
It uses the Java virtual machine, it compiles to Java bytecode, uses Java libraries.
You piggyback on this existing ecosystem, get a bunch of stuff for free. Clojure was one of, but not the first one to do it. I thinkColdFusionwas the first I heard of. But with Clojure, I could see how compelling that that approach was. And today you have
Elixir, TypeScript,Gleam,Reasonand F-sharp. It’s really hard to build a language, to build a runtime, to build a library ecosystem, profilers, debuggers… If you can narrow down the work in front of you, without inventing the wheel everywhere, it’s amazing what you can accomplish. I love that about Fennel!

But usually, when you have a hosted language, you have the VM completely in the other language, then the compiler converts from hosted into host language, then the runtime… In Clojure, when you define a function, it’s not just a Java method, it depends, extends this, uses some Clojure interface for callables… Data structures come with the host… And for Clojure, that’s the right choice for what it’s trying to accomplish.

But Fennel just has the compiler. When you compile a Fennel function, you get a Lua function, nothing more, nothing less. Sharing runtime semantics exactly with your host language really reduces the scope of what you have to do. If it’s not a transformation you can do compile-time, we just say sorry. “What if Fennel had immutable data structures?” That’s never going to happen; it’s just a compiler. But we can point you to so and so library which provides them at run time.

Now, I have a conceptual space of features. For example, pattern matching, one of my favorites, what does it actually mean? I think it’s 2 orthogonal features: destructuring, pulling your data apart declaratively and binding local variables to it. That’s one axis. But destructuring can’t decide which path to take. So you have conditionals, and when you put them together you have pattern matching.

(Later insert: Peter van Roy’sparadigm diagramis interesting. What others are there, exploring these concept spaces?)

So if some new feature is made up of things already there, you’re not adding much burden to learning, being effective in it, even to the implementation. But if you add pattern matching to a language without destructuring, there’s a lot more to chew on. But if you already have destructuring, adding this little thing lets it make decisions for you, cool! So what’s the conceptual footprint of so and so feature? What space does it take up? If destructuring and conditionals are already allocated in the learner’s mind, pattern matching is free! Fennel’s list comprehensions are similar: If you already have loops and data structures, you’re just combining them. A loop can give you a sequential or associative data structure. We first added the sequential DS, which you use all the time. Then we wondered about adding one for key value DS as well, the operation’s not as common, so it’s not worth spending limited space in our conceptual tool box.

How did you first discover Fennel? Were you already like facing issues due to Lua’s design, looking for
alternatives?

In my home directory, I have thegripe file. A friend in IRC gave me the idea. You just collect all the problems, complaints you have. How could the programs I use on a regular basis be better? Sometimes you see something can added or improved and you can delete this line from the gripe file. I love it. For example, SSH wouldn’t let you specify a directory for your config files. But a few years later, I went back and saw they had! So I deleted it from the gripe file, which is a really cool feeling. I recommend you keep a gripes file.

For Lua, if you typo the name of a variable, you can it’s local, but it ends up being a global and set or read it by accident. This makes sense, if you really want your scripts to be short and accessible, but I don’t think it’s the right choice because you can only catch it on runtime. You can use the LSP, linters but… Shouldn’t that just be in the language? So that goes in my gripe file. There are statements, not just expressions, another gripe! Lack of destructuring? Lack of pattern matching? Sure, Lua’s a small language, they had to draw the line somewhere, but it bugs me.

I began to look for alternatives and thought you could fix most of them with a Lisp! So I looked for Lisps on the Lua runtime, foud a few Schemes, an early, impressive Clojurescript prototype, but it wasn’t self hosted, depending on JVM stuff (to work on one runtime, requiring another 100 times bigger doesn’t feel great). I found a few one offs, but many likeUrnweren’t just syntactic transformations but included full standard libraries, which is cool, but I wanted something tiny, just a compiler.

So I foundFennel, a project Calvin Rose spent like a week on, then put to the side to work on another language from scratch, with his own virtual machine and everything. I think he was just more interested in how build a VM, how to solve tricky performance problems, whereas Lua’s already existed, but I wanted to explore the space around the language. So, Fennel was like a thousand lines of code and the core I wanted was visible. Excited, I started sending patches and asking him to clarify how it worked. I think he was really surprised that I was interested, really helpful and receptive! But he was more interested in this other language, DST at the time, renamedJanet.

How’d that “handover” go? Some guy falls in love with some weekend side project and now people write games in it! How do you react to that?

I think he saw it as a warm up. He had some ideas and wanted to sketch them out, starting with an easier problem, just this compiler; now he’s working on what he really wants to do with a bytecode engine, I love that for him. But it’s like playing on hard mode, doing it all from scratch. But we don’t have as much flexibility in Fennel, to e.g. add immutable data structures, but we’re making the most of our niche.

How do you see the basic requirements and expectations of tooling changing? The hosted language helps with some of that already, but e.g. you madeLeinigen, a build system for Clojure, while now Janet has JPM just built in. Most new languages appear with these kinds of things already, otherwise, people won’t touch them.

There’re different different categories of tooling, with runtime stuff like a profiler, in Fennel and Clojure you can use the profiles meant for Lua and Java. They work fine, though maybe you’ll see problems with source mapping? So another big win for hosted languages. But then you have things like LSP, where we have to do it ourselves. But we used a cheat code by making macros sandbox and we made that work a lot easier for us where you can just use the compiler instead of duplicating it like Clojure’s. But you’re hinting at this idea of libraries, the whole ecosystem. Fennel itself doesn’t have a solution for pulling in libraries
and dependencies. Before, when working in Clojure that was one of the first things I did, because going into the JVM,
you see these deep dependency trees and the dependencies are even binary artifacts, right? But in other languages, you can just drop the source in and it’s less important to have a dependency manager that can
pull the versions you need. In Fennel, it’s viable to just drop the repositories you want and be done. But there are a few places that doesn’t work very well, like when you have libraries which depend on C code, where your make file has to invoke their make file and… But the Fennel programs I write rarely have more than a dozen (even transitive) dependencies and the majority are just one file! It just hasn’t felt like enough to build a whole manager around! But C code is also complicated, not uniform, so you can’t do a one size fits all solution. Now, someone is working ondeps.fnlbut I haven’t tried it myself.

I’m curious about pedagogy. You came to Lua to make things with your kids. You’re doing nand2tetris now with them. Fennel, Lua, games echo that writing basic in the 80s so many people did. But now with this with LLMs, we’re “pulling up the ladder”. How do I phrase this?

Yeah, I love Fennel as a place to start learning because it’s so simple. You can learn the whole thing in a few days with a programming background. But as a fresh learner, it’s also a better place to start with fewer concepts, it fits in your head, so I love that. I don’t know what to say about AI though.

You mentioned the Fediverse before.

I mentioned picking projects with human impact and that’s the perfect example, digital independence, breaking the silos, giving people agency over their data etc. a way to allow people to take control of their own destiny with how they communicate. It’s inspiring seeing projects like Mastadon, but thenGoToSocial,Pleroma,Akkoma, the ecosystem is really taking off. The Free Software Foundation, GNU project have these ideals but miss the opportunity to make impacts, too focused on licensing… While megacorps are treating their users quite badly, while using software on free licenses, which don’t make much of a difference. But the Fediverse shows another way. You really can build software which impacts people in a direct way! I’ve been working with GoToSocial to improve their documentation, test new features, but mostly I’m just a user. I’m really impressed with how easy it is to run and operate. It takes like 15 minutes to set up your own server and it just runs. I did Debian packaging for it too, so you can just doaptif you addmy repo.

Talking about empowering users, it’s really easy to take for granted the way package managers put this wealth of incredible software at your fingertips, just one command and boom! But my packaging won’t be upstreamed in Debian any time soon; I break a ton of rules because of versioning etc. It’s a very non-compliant package, but better than nothing.

Why do you think ActivityPub got adoption where XMPP didn’t?

Just being in the right place at the right time? Mastodon was the poster child for ActivityPub
and plain as day, you could see new signup spikes to Mastodon instances every time e.g.
Twitter did something stupid. Just being there and not screwing up while others kept dropping the ball so hard, helps.
Even before Musk, so many bad decisions, whether or not we’re kicking the Nazis off or whatever, almost comical. And they were just ready to take on these dissatisfied users.

With XMPP, you hadembrace, extend, extinguishsituation where, Google went in with a big investment on XMPP, Facebook let you connect with XMPP… Then one day,oh, we’re not doing that anymore. So suddenly you couldn’t talk to your friends, the whole reason you were there. I think we were a little naive to think Google showing up and investing was a good thing.

I strongly empathize with your packaging woes. I tried to help a project with it but failed, burned out.

I helped with the packaging of Fennel too. It was like night and day because we have one
dependency and one or two files, a man page and an executable. But as soon as you start pulling in these complex dependencies, multiple Go or C libraries, you have to be an expert in Debian packaging to
to pull that off. Even with Fennel, we stubbed our toe and it took like six months of back and forth.
