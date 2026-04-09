---
title: Learning to read Arthur Whitney's C to become Smart - Needleful.net
url: https://needleful.net/blog/2024/01/arthur_whitney.html
site_name: hackernews
fetched_at: '2025-11-04T11:09:22.998849'
original_url: https://needleful.net/blog/2024/01/arthur_whitney.html
author: Devin Hastings aka needleful
date: '2025-11-04'
description: it's not working
---

* needleful dot net/
* needleful's blog/
* Learning to read Arthur Whitney's C to become Smart

Burger.

### it's not working

##### Written January 19, 2024

Arthur Whitney is an esteemed computer scientist who led the design on a few well-known pieces of software:

* The A, K, and Q programming languages
* kdb, a high-performance database built on K used in fintech
* Shakti, which is like kdb but faster, designed for trillion-row datasets.

I've never even seen a trillion numbers, much less calculated them, but kdb is apparently a standard tool on Wall Street. They probably care about money, so I'll assume kdb does its job well.
His languages take significantly after APL, which was a very popular language for similar applications before the invention of (qwerty) keyboards.

But I'm not here to talk about boring things like "using software to make incomprehensible amounts of money in finance" or "human beings and their careers", I'm here to talk about how a guy writes C code weird.
For a very simple version of the programming language K, there's apublicly available interpreterhe wrote in a few days using about 50 lines of C to show the basics of interpreter writing. This is the C (specifically the January 16, 2024 version #2):

## a.h

typedef char*s,c;s Q=(s)128;
#define _(e...) ({e;})
#define x(a,e...) _(s x=a;e)
#define $(a,b) if(a)b;else
#define i(n,e) {int $n=n;int i=0;for(;i<$n;++i){e;}}

#define Q(e) if(Q==(e))return Q;
#define Qs(e,s) if(e)return err(__func__,s);
#define Qr(e) Qs(e,"rank")
#define Qd(e) Qs(e,"domain")
#define Qz(e) Qs(e,"nyi")

#define _s(f,e,x...) s f(x){return _(e);}
#define _i(f,e) _s(f,e,c x)
#define f(f,e) _s(f,e,s x)
#define F(f,e) _s(f,e,s a,s x)

#define ax (256>x)
#define ix (c)x
#define nx x[-1]
#define xi x[i]

#define aa x(a,ax)
#define ia x(a,ix)
#define na x(a,nx)

#define oo w("oo\n")

## a.c

#include"a.h"//fF[+-!#,@] atom/vector 1byte(int/token) clang-13 -Os -oa a.c -w
#define r(n,e) _(s r=m(n);i(n,r[i]=e)r)
f(w,write(1,ax?&x:x,ax?1:strlen(x));x)F(err,w(a);w((s)58);w(x);w((s)10);Q)
_i(wi,s b[5];sprintf(b,"%d ",x);w(b);0)
f(W,Q(x)$(ax,wi(ix))i(nx,wi(xi))w(10);x)

f(srt,Qz(1)0)f(uni,Qz(1)0)F(Cut,Qz(1)0)F(Drp,Qz(1)0)_i(m,s a=malloc(1+x);*a++=x;a)
#define A(c) ((s)memchr(a,c,na)?:a+na)-a
#define g(a,v) ax?255&a:r(nx,v)
f(not,g(!ix,!xi))f(sub,g(-ix,-xi))F(At,Qr(aa)g(a[ix],a[xi]))F(_A,Qr(aa)g(A(ix),A(xi)))
f(ind,Qr(!ax)0>ix?r(-ix,-ix-1-i):r(ix,i))F(Ind,Qr(!aa)Qd(1>ia)g(ix%ia,xi%ia))
#define G(f,o) F(f,ax?aa?255&ia o ix:Ltn==f?f(sub(x),sub(a)):f(x,a):r(nx,(aa?ia:a[i])o xi))
G(Ltn,<)G(Eql,==)G(Not,!=)G(Sum,+)G(Prd,*)G(And,&)G(Or,|)
f(cat,Qr(!ax)r(1,ix))F(Cat,a=aa?cat(a):a;x=ax?cat(x):x;s r=m(na+nx);memcpy(r+na,x,nx);memcpy(r,a,na))
f(at,At(x,0))f(rev,Qr(ax)At(x,ind(255&-nx)))f(cnt,Qr(ax)nx)
F(Tak,Qr(!aa||ax)Qd(0>ia||ia>nx)At(x,ind(a)))F(Sub,Sum(a,sub(x)))F(Mtn,Ltn(x,a))f(qz,Qz(1)0)
#define v(e) ((strchr(V,e)?:V)-V)
s U[26],V=" +-*&|<>=~!@?#_^,",
(*f[])()={0,abs,sub,qz ,qz,rev,qz ,qz, qz ,not,ind,at,uni,cnt,qz ,srt,cat},
(*F[])()={0,Sum,Sub,Prd,And,Or,Ltn,Mtn,Eql,Not,Ind,At,_A ,Tak,Drp,Cut,Cat};
_i(n,10u>x-48?x-48:26u>x-97?U[x-97]:0)
f(e,s z=x;c i=*z++;!*z?n(i):v(i)?x(e(z),Q(x)f[v(i)](x)):x(e(z+1),Q(x)58==*z?U[i-97]=x:_(c f=v(*z);Qd(!f)F[f](n(i),x))))
int main(){c b[99];while(1)if(w(32),b[read(0,b,99)-1]=0,*b)58==b[1]?e(b):W(e(b));}

This is the entire interpreter, and this is apparently how he normally writes code.
Opinions on his coding style are divided, though general consensus seems to be that it's incomprehensible.
As daunting as it is, I figured I should give it a chance for a few reasons.

* As I work on larger and larger codebases, scrolling up and down to track information has become a more common annoyance. Whitney's talked about coding the way he does to avoid exactly that: he wants to keep his logic on one screen.
Perhaps learning to read code like this could give me ideas on writing my own code more compactly.
* In a Hacker News comments section, somebody asked "would you rather spend 10 days reading 100,000 lines of code, or 4 days reading 1000?", and that raises a good point.
The complexity of the code is because even a simple interpreter is pretty complex. Writing it in 500 lines wouldn't make the complexity go away, it just spreads it out.
Does writing in this more compact format feel more daunting because you're exposed to more of the complexity at once? I think so.
Does showing it all at once actually help you understand the whole thingfaster? I don't know.
* Reading code has become a more important part of my job than writing it, so I should challenge my reading skills, regardless.
* It confuses people, and that's basically the same as being smart.

So I'm going to go line by line and explain my understanding. I tried to use the notes provided in the repo only when I was stuck, which was a few times early on, but by the end I could understand it pretty well.

## A reading of a.h

typedef char*s,c;

This already shows some funky C. It definessaschar *, andcaschar, because the*attaches to the name, not the type. It's an oddity of C syntax that I've never been a fan of. Otherwise this is pretty straight forward:sis for string, andcis for character.

s Q=(s)128;

Fuck. Shit. He assigned 128 to a string namedQ. What does it mean?sischar *. Why is Q a pointer to the address 128? I thought I must have misunderstood, andswas actually a character or something, but it's clearly specified aschar *.sis for string!
I couldn't figure out the meaning, so I soon gave up and looked at the annotated code. Thechar *isunsigned long longin other versions, and they explain that the type is used for both integers and pointers. The code operates on vectors of 8-bit integers, either as ASCII or numbers, so it makes some sense to usechar *from a memory layout perspective, but I don't use pointers as integers very often.

#define _(e...) ({e;})
#define x(a,e...) _(s x=a;e)
#define $(a,b) if(a)b;else
#define i(n,e) {int $n=n;int i=0;for(;i<$n;++i){e;}}

These are all pretty straight forward, with one subtle caveat I only realized from the annotated code.
They're all macros to make common operations more compact: wrapping an expression in a block, defining a variablexand using it, conditional statements, and running an expressionntimes.

The subtle thing the annotations point out is the first macro,({e;}). The parentheses around curly brackets make this astatement expression, a non-standard C extension that allows you to treat a block of statements as a single expression, if the last statement is an expression that provides a value. In other words,int x = ({int a = func1(); int b = func2(a); a+b;});setsxto whatevera+bis. This is used everywhere in the code after this.

#define Q(e) if(Q==(e))return Q;
#define Qs(e,s) if(e)return err(__func__,s);
#define Qr(e) Qs(e,"rank")
#define Qd(e) Qs(e,"domain")
#define Qz(e) Qs(e,"nyi")

These are error macros using that mysteriousQdefined earlier.Qseems to have been used to represent errors, possibly short for "Quit". TheQr/d/zfunctions seem to be types of errors. I have no idea what "nyi" means (I figure it out later).

#define _s(f,e,x...) s f(x){return _(e);}
#define _i(f,e) _s(f,e,c x)
#define f(f,e) _s(f,e,s x)
#define F(f,e) _s(f,e,s a,s x)

These replace function declarations, and we can see that_macro being used to add an implicit return._scould be used like

_s(my_function, puts("I rock!!!"); x*5+e, s x, int e)

, which would create basically this standard C:

char *my_function(char *x, int e) {
	puts("I rock!!!");
	return x*5+e;
}

All the macros except the base_salso add implicit arguments likeaandxand you bet it's hard to tell them apart.

#define ax (256>x)

This was another one that baffled me until I looked at the annotations. Remember how I saidsvalues were either integers or pointers? 256 is the cutoff value for these integers, which the annotations callatoms, so ax means "isxan atom?"

#define ix (c)x
#define nx x[-1]
#define xi x[i]

These aren't too confusing.ixcastsxto achar.nximpliesxis some sort of fat pointer, meaning there's probably a length atx[-1], but we'll see.xijust indexesxas a normal pointer, using our implicitly definedifrom thei(...)macro.

#define aa x(a,ax)
#define ia x(a,ix)
#define na x(a,nx)

These copyax,ix, andnxrespectively to work on theavariable, which is an implicit argument in functions defined using theF(f,e)macro. You remembered thex(name, expression)macro for assigning to a locally-scopedx, right?

#define oo w("oo\n")

It printsoo. It's not used anywhere.

## a reading of a.c

I wound up not needing to refer to the annotated code at all to understand this. The C code is mostly using everything in the headers to build the interpreter.

#define r(n,e) _(s r=m(n);i(n,r[i]=e)r)

We create a vectorrfromm(n)(which is defined later (it's malloc)), fillrwith the results ofe, and return it out of the statement expression.

f(w,write(1,ax?&x:x,ax?1:strlen(x));x)

This definess w(s x), which is our print function. Ifxis an atom (ax?), we print it as a single character by getting its address (&x) and providing a length of 1. If it's a vector, we print it as a string usingstrlento calculate how long it is, so now we also know vectors must be null-terminated here.writeandstrlenare standard functions that we call without including the headers, because fuck headers. Let the linker figure it out.

F(err,w(a);w((s)58);w(x);w((s)10);Q)

Our fancy shmancy error printing function,s err(s a, s x). The confusing thing is that:and the newline are represented by their ASCII numbers 58 and 10, respectively. This just prints a message in the format{a}:{x}\nand returns our special error valueQ.

_i(wi,s b[5];sprintf(b,"%d ",x);w(b);0)

Definess wi(c x), which takesxas achar, formats it as an integer in up to5*sizeof(char*)/sizeof(char)characters (40 on 64-bit machines), and writes that.

f(W,Q(x)$(ax,wi(ix))i(nx,wi(xi))w(10);x)

Another print function,s W(s x)either writesxas an integer or a list of integers. It also refuses to print theQvector.

f(srt,Qz(1)0) f(uni,Qz(1)0) F(Cut,Qz(1)0) F(Drp,Qz(1)0)

I figured out whatnyimeans! It means "Not yet implemented", as we can see from these function definitions.

_i(m,s a=malloc(1+x);*a++=x;a)

And we find our previously-used functions m(c x), which allocates our buffer and returns a fat pointer (with the size atx[-1], hence the1+xanda++).xis the length we're allocating here, which means our vectors are limited to 255 bytes. The repo suggests upgrading capacity as an exercise to the reader, which could be fun.

#define A(c) ((s)memchr(a,c,na)?:a+na)-a

This macro finds the first occurence of the charactercin our vectoraas an index into the string (hence the-a, sincememchrreturns a pointer). If the result is null, it just returns the length of the string (a+na - a). We see another fun bit of non-standard syntax,?:, whichI had to look up.a ?: bis equivalent toa ? a : bwithout evaluatingatwice. Pretty snazzy!

#define g(a,v) ax?255&a:r(nx,v)

Strange little operation, I'll have to see it in action. Ifxis an atom, it clampsato be an atom with a simple mask (255&a), otherwise it creates a new vector the same size asxfilled with the result fromv.

f(not,g(!ix,!xi)) f(sub,g(-ix,-xi)) F(At,Qr(aa)g(a[ix],a[xi])) F(_A,Qr(aa)g(A(ix),A(xi)))

Ah, I see now.g(a, v)lets us define functions that work onbothatoms and vectors. Ifxis an atom, it returns the atom result clamped within the correct bounds. Otherwise it allocates a new vector and computes the other expression.
All the above functions work either onxas an integer (ix), or on every element ofx(xi).

* s not(s x)does boolean negation.
* s sub(s x)does arithmetic negation.
* s At(s a, s x)indexes intoa, either to get one value or to shuffle them into a new vector.ahas to be a vector.
* s _A(s a, s x)searches a vectorafor the value ofxand gives us the index, either one value or every value in the vector.

This is a lot of functionality in such a small bit of code.

f(ind,Qr(!ax)0>ix?r(-ix,-ix-1-i):r(ix,i))
F(Ind,Qr(!aa)Qd(1>ia)g(ix%ia,xi%ia))

These are some atom-only functions.

* s ind(s x)creates a vector of length|x|containing0, 1... x-1ifxis positive, otherwise it contains-x-1, -x-2... 0.
* s Ind(s a, s x)doesxmoduloa, either onxas an integer or every value of the vectorx.

Honestly, I can buy that this method of coding produces fewer bugs, once you can actually write it, since you work only on small building blocks of the logic and reuse them. Like, where could a bug forindeven be? Maybe an off-by-one in-ix-1-i, but it's hard to miss what's happening once you can see the trees through the forest.

#define G(f,o) F(f,ax?aa?255&ia o ix:Ltn==f?f(sub(x),sub(a)):f(x,a):r(nx,(aa?ia:a[i])o xi))

That's too many trees! I can't understand this many nested ternary operators at the same time because I'm not the alien fromArrival. I process things in linear time. I have to chunk this up.

F(f, ax ?
		aa ?
			255 & ia o ix
			: Ltn==f ?
				f(sub(x),sub(a))
				: f(x,a)
		: r(nx,(aa?ia:a[i])o xi))

Okay, I see. It's 3 cases from 2 conditions:xis an atom or a vector, andais an atom or a vector.

* xandaare atoms: apply some operatoroto both values and clamp to 8 bits. I also didn't realize the bitwize and (&) had a lower precedence than the operators this macro is used on, meaning it's always`C
255 & (ia o ix)`.
* xis an atom andais a vector: run this function with the arguments swapped. If the function isLtn, also negate the arguments, since less-than depends on argument order.
* xis a vector: create a new vector, either applyingaor each value ofatoxusing the operator. It assumes vectorais at least as long asx, or it'll index past the end ofa.
G(Ltn,<)G(Eql,==)G(Not,!=)G(Sum,+)G(Prd,*)G(And,&)G(Or,|)

Using our fancy new macro, we quickly define seven new functions for the vectors, where they're all element-wise applications of binary operators.

f(cat,Qr(!ax)r(1,ix)) F(Cat,a=aa?cat(a):a;x=ax?cat(x):x;s r=m(na+nx);memcpy(r+na,x,nx);memcpy(r,a,na))

I was confused by the first function, but I see now these arecatas in "concatenate". For an atom, it creates a vector of length 1 containing that atom.Catdoes the more complex work of joining two vectors together, runningcaton each value if it's an atom to get a list.

f(at,At(x,0)) f(rev,Qr(ax)At(x,ind(255&-nx))) f(cnt,Qr(ax)nx)

Some more simple functions. Lilatgets the first item ofx;revreverses the list using ourindfunction to generate the list of indeces in reverse, which is a little overkill but vectors are 256 bytes at max and memory is never freed so who cares; andcntgets the size ofx.

F(Tak,Qr(!aa||ax)Qd(0>ia||ia>nx)At(x,ind(a))) F(Sub,Sum(a,sub(x))) F(Mtn,Ltn(x,a)) f(qz,Qz(1)0)

Some more simple functions.Takreturns the firstacharacters from the vectorxas a new list;Subsubtracts;Mtnis "more than"; andqzreturns our "not yet implemented" error.

#define v(e) ((strchr(V,e)?:V)-V)

A shorthand to get the first occurence of a character from a stringV, returning an offset into the array or zero if it's not present. This seems ambiguous, since that's also the result if we match with the first character, but we'll see.

s U[26],V=" +-*&|<>=~!@?#_^,",
(*f[])()={0,abs,sub,qz ,qz,rev,qz ,qz, qz ,not,ind,at,uni,cnt,qz ,srt,cat},
(*F[])()={0,Sum,Sub,Prd,And,Or,Ltn,Mtn,Eql,Not,Ind,At,_A ,Tak,Drp,Cut,Cat};

Ah, we have seen. The first character ofVis a space, and it looks like the arrays of function pointers match up with the characters ofVto give us our functions, with space being null. However, I thinkabsis from the standard library here, since it's not defined anywhere else? That seems like a bug. It'd work for atoms, but it'd break vectors.
This also defines an array of 26 vectors, which I assume will be our variables.

_i(n, 10u>x-48? x-48 : 26u>x-97? U[x-97] : 0)

s n(c x)reads a char and returns one of several things. I'll have to consult an ASCII table.

* Ifxis between 48 and 57 (inclusive), we subtract 48 and return that. Meaning, ifxis an ASCII character representing 0-9, we subtract 48 so it's theinteger0-9, rather than the character. It's phrased strangely,10u > x-48, instead of the more obviousx>47&&58>x. Maybe it's because it's two characters shorter. Maybe Arthur wanted to show thelengthof the span of characters (10) more than the start and end, which this does once you understand it. Maybe he just thought the underflow trickery was neat.
* Ifxis between 97 and 122 (inclusive), it's a lowercase character of the alphabet in ASCII, in which case the function returns one of our variables from theUarray, mapping 'a' to 'z'.
* Otherwise, the function returns 0.

So it looks like this function is specifically to read values, either numerals or variables, all of which are one character.

f(e,s z=x;c i=*z++;!*z?n(i):v(i)?x(e(z),Q(x)f[v(i)](x)):x(e(z+1),Q(x)58==*z?U[i-97]=x:_(c f=v(*z);Qd(!f)F[f](n(i),x))))

Uh, let's spread this out a little.

f(e, s z=x; c i=*z++; !*z ? n(i)
	: v(i) ? x(e(z), Q(x) f[v(i)](x))
		: x(e(z+1), Q(x) 58==*z ? U[i-97]=x
			: _(c f=v(*z); Qd(!f) F[f](n(i),x))))

Okay, easy. It's a recursive function that checks each character of vectorx, calledi.
If we're at the end of the string, we check ifiis a value and return it.
Otherwise, we first check if it's an operator (from ourVstring). If it is, we evaluate the rest of the string, check for errors, and then apply the operation to the result from the rest of the evaluation.
If it wasn't an operation, we evaluate the rest of the string, skipping one character. If the skipped character is a colon (ASCII 58), we assign the result of the evaluation to one of the slots inU(if the characteriis not a lowercase ASCII letter, this will corrupt memory, so don't write bugs).

I'm pretty sure spaces are a syntax error in every location, and I don't see code to create array literals.
If the skipped character is an operator, we instead apply that binary operator on the evaluation result andn(i), which is either a variable or a number.
This means code is executed from right to left, with no operator precedent, which is standard for APL-type languages from what I understand.
Because this language has only single-character variable names, numbers, and operators, this is all the tokenizing, parsing, and evaluation we need.

C int main(){c b[99]; while(1) if(w(32),b[read(0,b,99)-1]=0,*b) 58==b[1] ? e(b) : W(e(b));}

And finally,main.
In an infinite loop, we read up to 99 characters from a user, and then write the evaluated result of that text.

Et voila. We have a tiny interpreter for a simple array language. It's not exactly production-ready, but it does quite a lot in its tiny footprint.

## Conclusions

I think I can say I understand this code pretty well, even more than most code I read. I don't know how much of that is because of the coding style, or because I spent eight hours writing several thousand words about fifty lines of code in a borderline-delusional fugue state brought on by drinking one small Starbucks™ Frapuccino® (Mocha® Flavored*) I bought from a gas station at 10 PM on a Thursday.

I had some fun dreams about macros with one-character names applying operations on scalars and vectors that morning (I went to sleep at 6:40 AM).

All in all, it was a fun exercise. To summarize my thoughts:

### Good ideas

* Well-considered primitives.I've read and written a lot of macro-ridden C, but this feels like a proper little language designed with composable, useful macros that removed enough repetition to make common operations, like iteration, easy to decipher. In other languages, higher-order functions and similar constructs could be used the same way.
* Fewer lines. I didn't have to scroll so much when I forgot what a macro or a function did! I have a wide screen monitor, I don't need lines limited to 10-20 characters of actual code most of the time.
If people can read English in compact paragraphs, why not code?

### Bad ideas

* Non-semantic types. I was completely baffled by thechar *being treated as an integer at first, and simply assumed I was misunderstanding the code somehow until I checked the annotated version.
In my own code, I use types as one of the core building blocks. What the dataisdefines how I use it.
For a full interpreter, this would be a custom type anyway, since right now it assumesmallocwill never give it a pointer to an address less than 256, which is probably true but not guaranteed, and also the integer 128 is reserved for invalid results, which is probably the bigger limitation.
* Code golf. I can understand the large gains to density like macros, and even the medium gains like short names, but there's a point where the code becomes significantly harder to follow for very minor gains, such as the use of ASCII codes like58instead of character literals like':', or the use of10u>x-48instead ofx>48&&58>xfor checking ifxis within a range.
And while I think more code can be put on a line, I'm not throwing out my space key just yet, epecially between function declarations.

### Ideas I'm ambivalent about

* Non-standard syntax.There's some very interesting features in this code that utilize GCC-specific extensions, likea ?: bternaries and statement expressions. I don't typically need to compile for everything on earth, so learning the tricks of one reasonably cross-platform compiler isn't a bad idea.
At the same time, even using clang, the same compiler Arthur was using, I had to includestdio.hdue to not linkingsprintfotherwise. If I wanted to build using Visual Studio I'd just have to rewrite a bunch of stuff.
Also, compiling without-wgenerates almost three compiler warnings per line of code. Those are useful sometimes, if they aren't flooded!
* Implicit arguments. Many of the density gains in this code come from using the variablesx,a, andiin nearly every context, allowing macros to use them by default and skip listing other parameters. I didn't find it to be a problem after a brief adjustment, but it's also a very small codebase.
Implicit arguments are a feature in many dynamically typed languages, and in"point-free" or "tacit" programming, but it's fallen out of style due to its difficulty to parse at first glance.
Whitney's languages all being based around tacit programming is surely an influence on his tendency to make arguments implicit.
* Short names.Beyond the very first introduction, there'd be virtually no benefit to renamingaxasvector_is_atom(x),_(...)as 'execute(...)', or most other primitives after they're introduced.
Most are small enough that you can parse what it does right away.
However, this doesn't lend any signal as towhyit does. You have to figure out what it does from context.
For code that's meant to be read by another person, there should probably be some explanation as towhya primitive does what it does, even if it has a short name. This is especially true of more complex operations, like the evaluation functione.
* Nested ternary operators. Too confusing for me to follow without parentheses, especially without whitespace.

This coding style feels most appropriate for "done" code, or code that's been worked out on paper or some other environment and is now being written down in a compact way. It's more like finalized mathematical notation than typical code.
I don't see myself being able to effectively write code like this, since I tend to quickly jot down ideas, compile and run to validate, and edit what I've done based on the results. Making a small set of good primitives and building heavily on those requires basically having solved the problem before writing a single line. Otherwise you get bad primitives that cause more confusion than help, and adjusting those primitives would involve rewriting all the code that depends on them, which is all the code.

But I think that's my key takeaway: I tend to work out problemsin the code, which can lead to messy results. I write the dumbest possible solution, and then have to try and refactor as I develop a better mental model of the problem.
What I like most about this code isn't how few characters are used, or everything fitting in one screen. I like how it seems the code was well-understoodbeforeit was written. You can't refactor a 500-line jumble of C into code like this.

The real lesson is that I'm probably too quick to jump into coding things. I could spend more time working out how I want to model a problem in a more free-form way, like writing notation on paper, before jumping into the rigid world of programming syntax.
With a clear mental model, I can then write code in terms of how I wasthinkingabout the problem, instead of thinking about the problem in terms of how I wrote the code.

## Next time

I think a fun exercise would be to extend this interpreter while maintaining its code style, to see how I fare actually working with it. The repository this came fromhas various suggested exercises, but my ideas would be adding the following:

* Swapping the bytes for float vectors
* Vectors longer than 255 values
* Multi-character numbers
* Array literals (you can do it with comma, but that runscaton every value, which isn't ideal)
* Whitespace insensitivity
* Memory management
* The unimplemented functions
* Multi-character variable names
* Multi-character operators
* Indication for syntax errors
