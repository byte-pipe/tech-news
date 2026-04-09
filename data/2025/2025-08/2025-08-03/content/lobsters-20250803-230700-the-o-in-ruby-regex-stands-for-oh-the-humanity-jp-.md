---
title: The /o in Ruby regex stands for “oh the humanity!” - JP Camara
url: https://jpcamara.com/2025/08/02/the-o-in-ruby-regex.html
site_name: lobsters
fetched_at: '2025-08-03T23:07:00.733479'
original_url: https://jpcamara.com/2025/08/02/the-o-in-ruby-regex.html
author: JP Camara
date: '2025-08-03'
published_date: '2025-08-02T01:16:06-04:00'
description: 'Your code using the /o modifier Source: wikipedia Hi there! Do you like Regex? Do you like performance? Do you like creating confounding bugs for yourself rooted in the mechanics of the Ruby VM itself? If you said yes to all of the above, have I got a feature for you! But first, let’s start with a story. The cliffs of insanity I was recently reviewing some code, and part of the functionality was about matching.'
tags: compilers, ruby
---

Your code using the/omodifier

Source:wikipedia

Hi there! Do you like Regex? Do you like performance? Do you like creating confounding bugs for yourself rooted in the mechanics of the Ruby VM itself?

If you said yes to all of the above, have I got a feature for you!

But first, let’s start with a story.

### The cliffs of insanity

I was recently reviewing some code, and part of the functionality was about matching. A class took an array of strings, and you could call a method to see if an input matched part of any of the strings. Stripped down, it was effectively the following code:

class Matcher
 def initialize(matchables)
 @matchables = matchables
 end

 def matches_any?(input)
 @matchables.any? { |m| m.match?(/#{input}/io) }
 end
end

Iknowthere are some of you reading this code and thinking “does this really need a regex?”, “couldn’t it just useinclude?and some downcasing?”, “does this even need to exist?”, etc, etc. I see you, I hear you, I’d probably think the same, and Ipromiseyou the specifics of this method aren’t that important.

Functionally, the code lookedokto me. I knew what/iwas (a regex incase-insensitive mode), but I didn’t recognize/o. It didn’t seem critically important to lookup yet. Tests were not exhaustive but were green, and so I went to run the code in a console:

Matcher
.
new(
[
"Ruby!"
]
)
.
matches_any?(
"ruby"
)

=>

true

Matcher
.
new(
[
"Ruby!"
]
)
.
matches_any?(
"something else"
)

=>

true

Matcher
.
new(
[
"Ruby!"
]
)
.
matches_any?(
"javascript"
)

=>

true

Well, that seemed broken. Assuming it was a bug, I looked at the code to see what was wrong. But nothing stuck out. The codeseemedok, and simple:

@matchables.any? |m| m.match?(/#{input/io) }

So I deconstructed the code and ran it directly, outside the class:

[
"Ruby!"
].
any? {
|
m
|
 m
.
match?(
/ruby/io
) }

=>

true

[
"Ruby!"
].
any? {
|
m
|
 m
.
match?(
/something else/io
) }

=>

false

Even weirder. Run directly, it ran as expected. What if I started a new console, and ran the original class in a different order?

Matcher
.
new(
[
"Ruby!"
]
)
.
matches_any?(
"something else"
)

=>

false

Matcher
.
new(
[
"Ruby!"
]
)
.
matches_any?(
"ruby"
)

=>

false

Matcher
.
new(
[
"something else"
]
)
.
matches_any?(
"Ruby!"
)

=>

true

Well, that was interesting. It seems like whatever value I sent tomatches_any?was cached for every run after that point, even forbrand new objects.

I looked through the class again. There was no weird memoization. No class-level variables. No thread locals. I was instantiating the class each time I ranmatches_any?. I was out of ideas for the predictable things that cause unpredictable results. What else was there?

### /o the humanity!

With nothing else to investigate, I finally looked up the docs for what the/oregex modifier does./ois referred to as “Interpolation mode”, which sounded pretty harmless. The Ruby docs have a succinct section on the expected behavior:https://ruby-doc.org/3.4.1/Regexp.html#class-Regexp-label-Interpolation+Mode

Modifier o means that the first time a literal regexp with interpolations is encountered, the generated Regexp object is saved and used for all future evaluations of that literal regexp

Just reading that, I still wasn’t sure I’d expect what I was seeing. It almost sounded like internally Ruby would cacheeachdifferent interpolation that comes through. As if it would maybe reuse an internal regex if the same string value was interpolated. They provide a code example that makes it a little clearer:

def letters; sleep 5; /[A-Z][a-z]/; end
words = %w[abc def xyz]
start = Time.now
words.each {|word| word.match(/\A[#{letters}]+\z/) }
Time.now - start # => 15.0174892

start = Time.now
words.each {|word| word.match(/\A[#{letters}]+\z/o) }
Time.now - start # => 5.0010866

Thelettersmethod in the first example is called three times. One time for each iteration, as expected, taking 15 seconds total.

In the second example, the code iterates three times, but thelettersmethod is calledonce, taking 5 seconds total.

Knowing that, I went back to the original code with new eyes:

class

Matcher


def

initialize
(matchables)
 @matchables
=
 matchables

end



def

matches_any?
(input)
 @matchables
.
any? {
|
m
|

 m
.
match?(

/
#{
input
}
/io

# This is run once, _ever_

 )
 }

end

end

What that meant for me is that the regular expression inside ofmatches_any?was interpolating thefirst value iteverreceives. Past that point the regexnever interpolated another value.

As it turned out, the developer had read about it as a potential regex optimization. It seemed harmless enough, so they added it. Now that I knew why I was hitting the issue, I removed the/oand everything started working properly.

But it still was not clear to mehowthis was possible. What in the world is Ruby doing internally? Let’s figure it out together.

### Inside the VM

Sometimes the only way to understand a behavior in Ruby is to drop a bit lower. Let’s disassemble the code into Ruby VM byte code, to see if it gives us any clues. I’ll use theDATAfeature to be able to put it into a script directly (you can find more aboutthat syntax here).

puts
RubyVM
::
InstructionSequence
.
compile(
DATA
.
read)
.
disassemble


__END__

class Matcher

 def initialize(matchables)

 @matchables = matchables

 end



 def matches_any?(input)

 @matchables.any? { |m| m.match?(/#{input}/io) }

 end

end

There are a bunch of other instructions you’ll see if you run that code, but we’ll focus on the instructions specific to the block in thematches_any?method:

# { |m| m.match?(/#{input/io) }

== disasm: #<ISeq:block in matches_any?@<compiled>:7 (7,21)-(7,51)>
local table (size: 1, argc: 1 [opts: 0, rest: -1, post: 0, block: -1, kw: -1@-1, kwrest: -1])
[ 1] m@0<AmbiguousArg>
0000 getlocal_WC_0 m@0 ( 7)[LiBc]
0002 once block (2 levels) in matches_any?, <is:0>
0005 opt_send_without_block <calldata!mid:match?, argc:1, ARGS_SIMPLE>
0007 leave [Br]

It describes:

* Getting local variablem
* Running the…onceinstruction?
* Callingmwithopt_send_without_blockwith a method id (mid) ofmatch?
* Thenleaveing.

All of these instructions areverycommon in the Ruby VM. All except one - theonceinstruction. I’ve never heard of that!

What isonce? It can’t exist almost solely for the purposes of this extremely strange regex modifier, can it? Surely this modifier is not built into the verybonesof Ruby?

### onceupon a time

If you are ever curious to know how Ruby VM instructions get interpreted in CRuby, there is a central file to all of it calledinsns.def. It contains all of the available YARV (Yet Another Ruby VM) instructions in a C-esque format which is compiled into an actual C file as part of building the language.

In normal program execution, without JIT optimizations applied (like YJIT, ZJIT, MJIT), you can trace how each instruction is executed by readinginsns.def. Let’s look at theoncedefinition to see what kind of dark magic is being invoked.

/* run iseq only once */
DEFINE_INSN
once
(ISEQ iseq, ISE ise)
()
(VALUE val)
{
 val = vm_once_dispatch(ec, iseq, ise);
}

In essence it’s very simple - it takes the instruction and runs it usingvm_once_dispatch.iseqis the instruction sequence, andiseis an “Inline Storage Entry”, which is a place to cache an instruction result. What doesvm_once_dispatchdo?

static
 VALUE

vm_once_dispatch
(rb_execution_context_t
*
ec, ISEQ iseq, ISE is)
{
 rb_thread_t
*
th
=
 rb_ec_thread_ptr(ec);
 rb_thread_t
*
const
 RUNNING_THREAD_ONCE_DONE
=
 (rb_thread_t
*
)(
0x1
);

 again:

if
 (is
->
once.running_thread
==
 RUNNING_THREAD_ONCE_DONE) {

return
 is
->
once.value;
 }

else

if
 (is
->
once.running_thread
==
 NULL) {
 VALUE val;
 is
->
once.running_thread
=
 th;
 val
=
 rb_ensure(vm_once_exec, (VALUE)iseq, vm_once_clear, (VALUE)is);

// ... skipped ...

 is
->
once.running_thread
=
 RUNNING_THREAD_ONCE_DONE;
/* success */


return
 val;
 }

else

if
 (is
->
once.running_thread
==
 th) {

/* recursive once */


return
 vm_once_exec((VALUE)iseq);
 }

else
 {

/* waiting for finish */

 RUBY_VM_CHECK_INTS(ec);
 rb_thread_schedule();

goto
 again;
 }
}

It’s a little daunting at first look, but broken down it’s just some simple if statements:

1. is->once.running_thread == RUNNING_THREAD_ONCE_DONEIf the instruction cache is set toRUNNING_THREAD_ONCE_DONE(a flag to identify being done vs pointing at a thread), it returns its cached value. Forever.
2. is->once.running_thread == NULLIf there is no running thread, congratulations! Your thread is the winner! You get to decide what value gets cached! Every other thread trying to run this instruction will wait until you have produced a value (by callingvm_once_exec), then use whatever value you produced. Forever.
3. is->once.running_thread == thIf there is a running thread set, and it’s the current thread, we’re in a recursiveonce(terrifying…)
4. Otherwise you are a different thread, and you have to wait. You’ll keep checking for a value immediately, or get rescheduled and check it a little later (once some other threads have been given a slice of time)

We’ve broken down the logic. Now let’s break down the implications.

1. If you use/oin your regex, the content of the regex will be evaluatedonce,ever. Even if it’s inside of an instance method. Even if it’s inside of a loop with a thousand iterations. It willneverbe evaluated again. That’s the content you’ve got for your regex. This is why the code I was reviewing was so confusing - even though it lived in an object, and was only created local to that method - itimplicitly created a constant, immutable value.

Now we can understand how the original code worked, by evaluating it relative to how the CRuby internals work. The first call we have no value set - past that point we will always use the value literally cached inside of the VM itself:

# We haven't run the code yet, so in our starting state:
# is->once.running_thread == NULL
# m.match?(/#{input}/io)
> Matcher.new(["Ruby!"]).matches_any?("something else")
# Now we've run the code once, we're done!
# is->once.running_thread == RUNNING_THREAD_ONCE_DONE
# m.match?(/something else/io)

> Matcher.new(["Ruby!"]).matches_any?("ruby")
# is->once.running_thread == RUNNING_THREAD_ONCE_DONE
# m.match?(/something else/io)

> Matcher.new(["something else"]).matches_any?("Ruby!")
# is->once.running_thread == RUNNING_THREAD_ONCE_DONE
# m.match?(/something else/io)

1. If the code has not been run yet, you’re in the starting state ofis->once.running_thread == NULL. This means two things. One is clear - the first code to run this gets to determine the value set. Two is a little less clear - it is non-deterministic what value will win!

If you’ve read any ofmy series on Ruby concurrency, you’ll know I love a good thread non-determinism example. Here we create a method containing an “interpolation mode” regex. Then we create five threads, and call the method from each thread. To introduce some context switching, we sleep for random amounts (this could also be caused by IO, or long-running code, alternatively):

def once_and_for_all(input)
 /#{input}/o
end

5.times.map do |i|
 Thread.new { sleep(rand); p once_and_for_all(i) }
end.map(&:join)

# Run it once, it prints /3/ 5 times
# Run it again, it prints /1/ 5 times
# Run it again...

In my first run, I see the regex/3/printed 5 times. Each run gave me a different result. Run this code several times and you will likely see a different value printed each time. It may repeat at times, but there will be no consistency.

Quite the behavior! This is pretty close to being aHeisenbug. Non-determinism at its finest.

1. The code has been run already, but now it’s being run again before being set asRUNNING_THREAD_ONCE_DONE:is->once.running_thread == th. This can only happen within the same thread, and it’s there to handlerecursion. It’s hard to imagine using the/oat all, let alonerecursively. If you were to do that I’d only have one question for you: “Who hurt you?”

But let’s do the damn thing. Here’s a recursive case of the/omodifier. Heaven help us.

def recursive_regex(n)
 puts "Evaluating regex for n=#{n}"
 if n > 0
 /#{recursive_regex(n - 1)}/o # This calls itself recursively
 else
 "base"
 end
end

recursive_regex(5)
# Evaluating regex for n=5
# Evaluating regex for n=4
# Evaluating regex for n=3
# Evaluating regex for n=2
# Evaluating regex for n=1
# Evaluating regex for n=0

recursive_regex(5)
# Evaluating regex for n=5

# Call it with whatever value you want, it's never running the method recursively again.
recursive_regex(500)
# Evaluating regex for n=500

I promise it hurt me more to write that than it did for you to read it.

This example does bring up an interesting point though! Our examples so far have been simple values interpolated into the regex. In this case, we’re calling a method and it is still only being evaluated once. The operation you run in the interpolation is irrelevant - whatever is interpolated will never be run again with the/omodifier.

1. If none of the other conditions are met, it means the interpolation is being evaluated by a different thread. All we can do here is wait to see what the value is.

This is the same concept as the threading example, but this is about the threads that lose the race. The most interesting part here is that it means this interpolation is guaranteed to be thread safe in CRuby (at least in the sense that other threads are locked out of it, not that you get a deterministic result). That will actually matter a little later, if you can believe it.

### Why does it exist?

I didn’t find a clear origin of this modifier. But it’s been around for 20+ years. It’s likely been around almost as long as Ruby itself. Matz, you scoundrel, you.

Shockingly, every other forum or blog post I found in relation to the/omodifier exclusively spoke about the performance benefits of it. I didn’t find any warnings at all. But mostly I found it used in a scripting context. In a single, simple script run,maybeyou’re safe. But the downside seems way worse than any potential upside. If you really need a speed boost - just cache the regex yourself?

interpolated_once
=

/
#{
ARGV
.
first
}
/

interpolated_once
.
match?(
"a string"
)
interpolated_once
.
match?(
"a string 2"
)
interpolated_once
.
match?(
"a string 3"
)

# Just as performant as /o?

The earliest reference I could find to the existence of a/omodifier in regex was in a2003 post on aPerlforum. Based on this, I’m guessing Ruby borrowed it from Perl. Even in 2003, the prevailing wisdom was already clear:

The best heuristic is: Never use/o

I agree with that 2003 Perl person. You don’t need it. You should not use it. Step away from the modifier, and no one has to get hurt.

### I’ll take youronce, and raise you…

We’re all having fun here, right? Should we take this confounding modifier, and muddy things a bit more?

Thereisactually a way to force the/omodifier to re-evaluate.

hushed whispers!

someone in the back of the room faints!

I stumbled upon it because I was testing this code in a Rails console. I found that every time I calledreload!, I was able to test my method from scratch again. Why would that be?

It’s because when youreload!, all of your code is re-evaluated by Ruby. And when it gets re-evaluated, you get new bytecode, and a new cache! Take this for instance:

def one_time(input)
 /#{input}/o
end

p one_time("hi there!")

def one_time(input)
 /#{input}/o
end

p one_time("how are you?")
# /hi there!/
# /how are you?/

Even though we used the/omodifier, we were able to re-evaluate it. That’s because we overrode ourone_timeimplementation, which gave us a newoncecache.

This matters because it means you can’t eventrulyguarantee your/oregex will only be run once. If a piece of monkey patch code gets loaded and overrides your method, you will get evenmorenon-deterministic behavior.

### The inmates are running the asylum

In a moment of pure serendipity, the day after I started writing this post I happened to read Jared Norman’sCode Reloading for Rack Apps. The article teaches you how to build the same kind of code reloading Rails has, but in a standalone Rack application. You should give it a read.

In it, he creates a class calledOnce.

This class let’s you create an object that encapsulates a bit of code and only ever lets it run once, even if it’s called across multiple threads.

-Jared Norman

class

Once


def

initialize
(
&
block)
 @block
=
 block
 @mutex
=

Mutex
.
new

end


def

call

 @mutex
&.
synchronize
do


return

unless
 @mutex


# Ignore the \, it's for a markdown issue...

 \@block
.
call

 @mutex
=

nil


end


end

end


o
=

Once
.
new
do

 puts
"I should only happen once"

end



100
.
times
.
map {
Thread
.
new { o
.
call } }
.
each(
&
:join
)

# => I should only happen once

Any thread attempting to run this code will block on the@mutex.synchronize. It runs@block.call, then at the end of thesynchronizeblock, the@mutexis set tonil. This means that after the first thread, every other thread either exits early because@mutexisnil, or never runs thesynchronizeblock at all because of the safe-nav. Makes sense!

As if I was destined to read this by some kind of trickster regex god, what did I see at the end of the article? A reimplementation of hisOnceclass using the/omodifier!

A veritable devil on Jared’s shoulder,John Hawthorngave him the idea. It would make sense that John, a Ruby internals wizard, would suggest such a thing. Then Jared, author ofAdvent of Criminally Bad Ruby Code, would actually decide to include it.

Here is their ingenious abomination.

class Once
 def initialize(&block)
 @block = block
 end

 def call
 /#{@block.call}/o # THE HORROR
 end
end

o = Once.new do
 puts "I should only happen once"
end

100.times.map { Thread.new { o.call } }.each(&:join)
# => I should only happen once

Using/o, the code examples still behave correctly and only run once despite the many threads attempting to run it.

It does, however, have a fatal flaw in comparison to the original code. Can you guess it?

Let’s demonstrate by creating multiple instances:

o1 = Once.new { puts "I should only happen once 1" }
o2 = Once.new { puts "I should only happen once 2" }
o3 = Once.new { puts "I should only happen once 3" }

100.times.map { Thread.new { o1.call } }.each(&:join)
100.times.map { Thread.new { o2.call } }.each(&:join)
100.times.map { Thread.new { o3.call } }.each(&:join)

In the original, mutex based implementation, we’d see the following:

# => I should only happen once 1
# => I should only happen once 2
# => I should only happen once 3

In the/obased implementation, we see this:

# => I should only happen once 1

Because of the instruction-level caching, we can only haveoneresult fromOnce#call,ever. A class that literally can only be run reliably asingletime. “Once”, indeed.

It’s probably more efficient than the mutex approach andmaybein some bizarro world where you truly needed a piece of code to be thread safe and lazy evaluated and as efficient up front as possible and only ever run once… maybe…

No… I cannot condone it -don’t do it!

Side note: Jared also has an excellent podcast calledDead Code, with loads of episodes with fantastic guests. I went on tospeak about concurrency - give it a listen!

### This is theEND

Earlier, I said:

What isonce? It can’t exist almost solely for the purposes of this extremely strange regex modifier, can it? Surely this modifier is not built into the verybonesof Ruby?

And the truth is,/ois not theonlyreason theonceinstruction exists. It took a little digging, but I found another piece of Ruby code that usesonce- theENDlanguage sytax. I was surprised to find thatENDexisted! I had never heard of it or used it before.

Not to be confused with theendkeyword that closes out blocks,ENDdefines a block that is run at the end of the Ruby program. For instance:

END
 { puts
"do this last please"
 }
puts
"1"

puts
"2"



# => 1

# => 2

# => do this last please

Note that if you run this code inirb, theENDblock will not run until you exit.irbis just a Ruby program, and it doesn’tENDuntilirbis exited.

If you disassemble this code, we’ll see a familiar instruction:

puts
RubyVM
::
InstructionSequence
.
compile(
DATA
.
read)
.
disassemble


__END__

END { puts "do this last please" }

puts "1"

puts "2"



# == disasm: #<ISeq:<compiled>@<compiled>:1 (1,0)-(4,8)>

# 0000 once block in <compiled>, <is:0>( 2)

So theENDblock, but not theendof a block, uses theonceinstruction, an instruction that is used twice in Ruby. An appropriately confusing close to an article about a fascinating feature I think you should never use - the/omodifier.
