---
title: Logo Programming Language
url: https://el.media.mit.edu/logo-foundation/what_is_logo/logo_programming.html
site_name: hnrss
content_file: hnrss-logo-programming-language
fetched_at: '2026-09-11T21:35:49.783796'
original_url: https://el.media.mit.edu/logo-foundation/what_is_logo/logo_programming.html
date: '2026-09-09'
tags:
- hackernews
- hnrss
---

# Logo Programming

 

The Logo Programming Language, a dialect of Lisp, was designed
 as a tool for learning. Its features - interactivity,
 modularity, extensibility, flexibility of data types - follow
 from this goal.

 

### Interactivity

Although there are some versions of Logo that compile, it is
 generally implemented as an interpreted language. The
 interactivity of this approach provides the user with immediate
 feedback on individual instructions, thus aiding in the
 debugging and learning process. Error messages are descriptive.
 For example

fowad

I don't know how to fowad

(The wordfowadis not a primitive - one of Logo's
 built in words - nor a procedure that you've defined.)

 

forward

Not enough inputs to forward

(Now that you've spelled it correctly, Logo knows the wordforward,
 but can't run your instruction becauseforwardrequires
 additional information.

forward 100

(Logo is happy. There's no error message. The turtle moves
 forward 100 steps.)

 

### Modularity and Extensibility

Logo programs are usually collections of small procedures.
 Generally, procedures are defined by writing them in a text
 editor. The special wordtois followed by the name of
 the procedure. Subsequent lines form the procedure definition.
 The wordendsignals that you're finished.

In ourturtle graphicsexample
 we defined a procedure to draw a square

to squarerepeat 4 [forward 50 right 90]end

and used it as a subprocedure of another procedure

to flowerrepeat 36 [right 10 square]end

Similarly,flowercould be a building block of
 something larger

to gardenrepeat 25 [set-random-position flower]end

No,set-random-positionis not a primitive, butrandomis and so issetposition(orsetposorsetxy).
 Or you could writeset-random-positionusingforwardandrightwithrandom.

Once a Logo procedure is defined it works like the Logo
 primitives. In fact, when you look at Logo programs there's no
 way of knowing which words are primitives and which are
 user-defined unless you know that particular Logo
 implementation. In ourlanguagesample we used the procedurepickto randomly select an
 item from a list, for example in the procedure who.

to whooutput pick [Sandy Dale Dana Chris]end

In some versions of Logopickis a primitive while in
 others you have to write it yourself.Whowould look and
 work the same way in either case.

Logo allows you to build up complex projects in small steps.
 Programming in Logo is done by adding to its vocabulary,
 teaching it new words in terms of words it already knows. In
 this way it's similar to the way people learn spoken language.

 

### Flexibility

Logo works with words and lists. A Logo word is a string of
 characters. A Logo list is an ordered collection of words and or
 lists. Numbers are words, but they're special because you can do
 things like arithmetic with them.

Many programming languages are pretty strict about wanting to
 know exactly what kind of data you claim to be using. This makes
 things easier for the computer, but harder for the programmer.
 Before adding a couple of numbers you might have to specify
 whether they are integers or real numbers. The computer needs to
 know such things. But most people don't think about this so Logo
 takes care of it for you. When asked to do arithmetic Logo just
 does it.

print 3 + 47

print 3 / 4.75

If you are unfamiliar with Logo but work in other programming
 languages, the following sequence may surprise you:

print word "apple "sauceapplesauce

print word "3 "434

print 12 + word "3 "446

Here's a recursive procedure that computes factorials:

 

to factorial :numberif :number = 1 [output 1]output :number * factorial :number - 1end

print factorial 36

print factorial 5120

Here's a procedure to reverse a list of words:

to reverse :stuffifelse equal? count :stuff 1[output first :stuff][output sentence reverse butfirst :stuff first :stuff]end

print reverse [apples and pears]pears and apples

You might also want to take a look at Brian Harvey's
 interestingLogo sample.

 

### Enhancements

The features just illustrated are common to all versions of
 Logo. Some Logo implementations include enhanced language
 features.

There was an object-oriented Logo called Object Logo for the
 Macintosh.

MicroWorlds Logo includes multi-tasking so that several
 independent processes may be run simultaneously. The same
 capability is in the software for Control Lab, a LEGO Logo
 product. An even more massively parallel Logo is StarLogo.

In a traditional Logo the command to the turtle

repeat 9999 [forward 1 right 1]

would take a while to execute. The instruction

repeat 9999 [forward 1 right 1] print "HELLO

would cause the wordHELLOto appear after the turtle
 was done moving.

In MicroWorlds Logo typing

launch [repeat 9999 [forward 1 right 1]] print
 "HELLO

would start the turtle going. The wordHELLOwould
 appear as soon as the first process is launched. Or

forever [forward 1 right 1] print "HELLO

would initiate a process that would continue until you stopped
 it. Again, the wordHELLOwould appear as soon as the
 turtle process is initiated.

 

### Find Out More

To find out more about the Logo programming language look at
 Brian Harvey's three-volume epicComputer
 Science Logo Styleand Michael Friendly'sAdvanced
 Logo.

If you do not have Logo and want to get started, you might
 want look at ourLogo
 software page. Or, you can just downloadUCBLogo,MSWLogo,FMSLogo,StarLogo
 TNG, orStarLogo
 Novaright now.


 A Hindi translation of this article 
is available here
. 

A Ukrainian translation of this articleis available here.A Serbo-Croatian translation of this articleis available here