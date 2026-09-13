---
title: Stabilizing Rust's never type [LWN.net]
url: https://lwn.net/SubscriberLink/1091015/d9e48318ed242b41/
site_name: hnrss
content_file: hnrss-stabilizing-rusts-never-type-lwnnet
fetched_at: '2026-09-13T14:50:18.210135'
original_url: https://lwn.net/SubscriberLink/1091015/d9e48318ed242b41/
date: '2026-09-09'
description: Stabilizing Rust's Never Type
tags:
- hackernews
- hnrss
---

### Welcome to LWN.netThe following subscription-only content has been made available to you 
by an LWN subscriber. Thousands of subscribers depend on LWN for the 
best news from the Linux and free software communities. If you enjoy this 
article, please considersubscribing to LWN. Thank you
for visiting LWN.net!ByDaroc AldenSeptember 8, 2026A function's return type is supposed to indicate the kind of data that it
produces. 
Rust's "never" type, which isdenoted by an exclamation mark("!"), is the type the language uses to mark
a function that never returns and other places where a value can never occur. For
a long time, the never type was used internally by the compiler, but was
considered an unstable feature. OnAugust 24, after more than two years of work,
Rust-compiler-contributor "waffle" finally managed to stabilize the type. It
took so long, in part, because it involved a small breaking
change to previous Rust editions, which the compiler maintainers needed to
ensure did not impact much real code.(Note: Rust also uses exclamation marks to indicate calls to macros. The way the
syntax is constructed, a place where it is valid to use the never type is not a
valid place to put a macro invocation and vice versa.)#### Why a never type?There are two reasons that Rust has a never type, one practical and one
philosophical. The practical reason is that it allows for more efficient generic
code. For example, consider theFromStrtrait in the standard library, which is used for types that
can be instantiated from a string:trait FromStr: Sized {
 type Err;
 fn from_str(s: &str) -> Result<Self, Self::Err>;
 }FromStr::from_str()either returns a converted result, or a custom
error type. For example, attempting to convert "foo" into an integer will return
aParseIntError. But some types have an infallible conversion. For
example, it is always possible to convert a string into aByteString. That implementation ofFromStrcould setErrto be the never type. Then the compiler would know that the
error branch of the returnedResultis never present, and could
optimize out all of the code that touches it or checks for it.impl FromStr for ByteString {
 type Err = !;
 fn from_str(s: &str) -> Result<Self, !> { ... }
 // Keeps the same generic interface,
 // but generates code equivalent to:
 // fn from_str(s: &str) -> Self { ... }
 }The philosophical reason involves correct type inference. In Rust, constructs
such asifstatements andwhileloops are expressions; their results can be
assigned to a variable. The compiler needs a type to infer for the result of an
infinite loop, if the programmer writes one. That shouldn't come up often in
real code, but it turns out to simplify type inference to be able to treat that
case uniformly, rather than adding special rules to handle it.In particular, the never type has a useful property for simplifying code: it
automatically coerces to any other type. This sounds strange, but it is
safe, since the never type represents the "result" of a computation that will
never produce a value. So, anywhere that the code claims to have a value of the
never type, the compiler knows that it can't possiblyreachthat code, and therefore it's safe to ignore it. This is a form of
type-system-driven dead-code elimination.For both of these reasons, Rust programmers have wanted to be able to use the
never type in stable versions of the language. Making that happen
required resolving a particularly thorny corner case.#### Never fallbackBecause of the way that conversions from the never type to other types are
implemented, the compiler can sometimes end up in a situation where it cannot
naively infer the concrete type of an expression. Consider this example, which
defines an anonymous function (using||, which is like
Python or LISP'slambda) that never returns, and then calls it in a way
that expects a concrete error type (using the?operator):let function_that_never_returns = || { loop {} };
 function_that_never_returns()?;That infinite loop is given a type of!which is then implicitly
converted to whatever the function is supposed to return. But since the function
is defined locally and not given an explicit type, the compiler does not have
sufficient information to say what that type is.
The problem could be fixed by giving the function an explicit return type:let function_that_never_returns = || -> Foo { loop {} };Since such an annotation would only be required in cases where the function
cannot return anything, however, it would
be a bit pointless to require the programmer to assign a fictitious type to it.
So, the compiler includes a special rule: if, after all other type inference has
been done, there is still an ambiguous type that cannot be determined, just assume
that it should be the designated fallback type. Prior to the 2024editionof Rust, that fallback type was()(the unit type, which has
exactly one possible value). In the 2024 edition, the fallback type was changed
to!itself, essentially canceling out the implicit conversion. In the
compiler internals, the never type still gets converted to an unknown type and
then falls back, but from the programmer's perspective the behavior is identical
to having the never type only undergo implicit conversion when required for the
types to make sense.That change of behavior was, technically, a breaking change. Type inference for
some code could change, which could in turn cause compilation errors. That is
the purpose of Rust's edition system: allow breaking changes in the front-end
design of the language without breaking older code or requiring the whole
ecosystem to update at once. In this case, however, there were reasons to want
the new behavior backported to old editions.#### Never infallibleFor many years, the standard library has had anInfallibletype to work
around the unstable nature of the never type. It served the same semantic
purpose as the never type, but did not have any special compiler support.
Therefore, code using it would be technically correct but suboptimal (such as
having an extra layer of tags in an enumeration or emitting dead code), because
the optimizer would not always be able to remove references toInfallible. It was planned that, when the never type was
eventually stabilized,Infalliblewould become a type alias for!and all that old code would silently become more efficient. However,
people pointed out a handful of ways that redefiningInfalliblehad accidentally been made into a breaking change. Since!has implicit conversions, changing the definition ofInfalliblecould result in existing code needing additional type
specifiers in order to type check.Luckily, changing the definition ofInfallibleand changing the default
fallback type, while both breaking changes, nearly cancel out. Any code that refers to the
standard library'sInfallibletype by name would continue to work; it
is only places where type inference is implicitly expected to produceInfalliblethat pose a risk of breaking existing code. With Rust's lack
of implicit conversions in most cases, that will most often come up in places
where the never type used to be implicitly converted toInfallible. IfInfallibleis made to be a type alias of the never type, then those
places may experience never-type fallback, which would, in turn, change the
inferred type and cause a compilation error if the never fallback type were not
updated at the same time.With both changes occurring simultaneously, the Rust maintainers believed that
almost all existing Rust code would continue to compile — but "almost all" is
not a reassuring qualifier when dealing with backward-incompatible
changes. The Rust community does have a solution to this in the form ofcrater, which can download and compile all publicly available Rust
libraries fromcrates.ioin search of code that is broken by a compiler change.#### Never say neverWaffle ran crater in April andfoundthat, while there were 3,300 crates negatively impacted by the change,
only seven were fully broken, with the rest broken by depending on old
versions of libraries that had since been fixed. In the latter case, the problem
would theoretically be fixable by releasing backported fixes for a handful of
core libraries.
This is not an accident; Rust has been emitting a warning whenever
code triggers never-type fallback in a way that will break with the new change
since 2024, so most libraries had plenty of time to update of their own
initiative. The most common remaining error observed bycrateris code
that calls a generic function without enough type information for the compiler
to pick a specific return type. Consider this function:fn foo<T: Default>() -> Result<T, Error> { ... }It returns either a value of some caller-chosen typeTthat must
implement theDefaulttrait, or an error. If
it is called without specifying a value forT, however, then type
fallback can kick in:// No type specified.
 foo()?;Previously, this would have made the compiler assume thatTshould be(), which implementsDefault, and so the code compiles. After
this change (and on the 2024 edition), the compiler assumes thatTshould be!, which doesn't implementDefault, and therefore
causes a compilation error. The fix is to explicitly specify the type thatfoo()should return, either in the call or by pattern-matching
assignment.foo::<()>()?;
 // or
 () = foo()?;Even though it's not a complicated change, the Rust maintainers were not willing
to break 3,300 crates. Waffle wasaskedto work with the maintainers
of common libraries to backport simple changes like the above (making a newpatch version, which many Rust build environments will pick up automatically),
in order to
reduce the number of libraries depending on broken dependencies. Several library
authors werewillingto make the backports, but some refused on the grounds that those
old versions were past their end of life. Those maintainers pointed out that
users could stay on an older version of Rust or update to the maintained version
of the library. Even so, the successful backports
addressed 1,553 of the failing crates.After fixinga
handful of related problemsto reduce the number of broken crates even
further, the Rust maintainers eventually agreed that
even though there would still be some broken code it was worth making the change
to simplify the language. So, starting in Rust 1.99, the never type will be
stable andInfalliblewill be a type alias for the never type. Users
who find that this breaks their code have a few options:Stay on Rust version 1.98.Update their dependencies to supported versions that include a fix for the
problem.Add a patch to explicitly specify the return types of affected function calls.On the one hand, this is
a breaking change, and people may see code that had remained stable
and working suddenly fail to compile. That could be seen as a violation of
Rust's commitment
to backward compatibility. On the other hand, the problem is
relatively rare, there are multiple simple ways to fix it, it has been warned
about for years, and it has always been part of the plan for the language.
Additionally, the
Rust maintainers worked directly with the community to find and
address the breakage, even going so far as to help backport fixes to long-dead
versions of popular libraries. So, the whole process could also be seen as an
affirmation of Rust's commitment to backward compatibility.In the
future, people learning the language will hopefully find the never type just a
little less special.
Either way, most users of Rust will probably not be affected at all, but never
say "never".to post comments### One more thing to doPosted Sep 8, 2026 16:57 UTC (Tue)
 bymss(subscriber, #138799)
 [Link] (5 responses)That's great.It would be even better if Rust folks finally stabilizedCET supportin their compiler since currently even a tiny bit of Rust code in an application (or one of the libraries it loads) is enough to cause the entire application to lose CET protection.### One more thing to doPosted Sep 9, 2026 8:19 UTC (Wed)
 bycyperpunks(subscriber, #39406)
 [Link]Fedora has done a very nice job here and the rust stack in upcoming Fedora 45 will use cf-protection by default:https://fedoraproject.org/wiki/Changes/ShadowStack### One more thing to doPosted Sep 9, 2026 11:48 UTC (Wed)
 byralfj(subscriber, #172874)
 [Link] (3 responses)What does this comment have to do with the never type? Nothing at all I think. Seems entirely off-topic here, unless for some reason you think that "everything related to Rust" is on-topic in every article about any part of Rust.### One more thing to doPosted Sep 9, 2026 11:54 UTC (Wed)
 bymss(subscriber, #138799)
 [Link] (2 responses)This article is about stabilizing a Rust feature so discussion about stabilizing other Rust features is on-topic.### One more thing to doPosted Sep 9, 2026 12:55 UTC (Wed)
 byralfj(subscriber, #172874)
 [Link] (1 responses)If the features are entirely unrelated then no, it is not.### One more thing to doPosted Sep 9, 2026 13:10 UTC (Wed)
 bypatrick_g(subscriber, #44470)
 [Link]For my part, I wasn't aware of this issue regarding CET protection and Rust, so I'm glad the subject was raised.### Why this code is actually a regression.Posted Sep 8, 2026 17:04 UTC (Tue)
 bymatthias(subscriber, #94967)
 [Link] (1 responses)// No type specified.
foo()?;I really wondered, why this code was a regression. And without the question mark, it would have always been an error, as the compiler would not be able to infer a type. However the question mark is syntactic sugar formatch foo() {
 Ok(v) => v
 Err(e) => return e.into()
}Here, the compiler can infer a type. The error branch has the type!which is changed toInfallible. As both branches need to have the same type, the compiler tries to find a type that is compatible with both branches. In most code, this would simply be the type of the Ok branch. But in this special case, the Ok branch has unspecified generic typeT. And this is where the fallback type comes into play. In rust editions prior to 2024, this was the unit type(), which implementsDefault. So there is no problem. Since Edition 2024 and with rust 1.99 also for all older editions, this fallback will become!, which does not implementDefaultand we get a compile error.This seems to be the only possibility of triggering a regression. We need to have two branches, where one is divergent (has type!) and the other has an unspecified generic type that cannot be inferred by other means and where it makes a difference whether we infer()or!. Seems to be quite a corner case.### Why this code is actually a regression.Posted Sep 13, 2026 9:30 UTC (Sun)
 bykoflerdavid(subscriber, #176408)
 [Link]That's correct, and if I read the article correctly rustc should have for a long time already raised a warning for such code.### It's not a violation of promise!Posted Sep 8, 2026 19:15 UTC (Tue)
 bykhim(subscriber, #9252)
 [Link]Just readthe blog post from 2014: “We reserve the right to fix compiler bugs, patch safety holes, and change type inference in ways that may occasionally require new type annotations”. Read the last part.### Infallible is not as bad as it soundsPosted Sep 9, 2026 7:58 UTC (Wed)
 byNYKevin(subscriber, #129325)
 [Link]> For many years, the standard library has had an Infallible type to work around the unstable nature of the never type. It served the same semantic purpose as the never type, but did not have any special compiler support. Therefore, code using it would be technically correct but suboptimal (such as having an extra layer of tags in an enumeration or emitting dead code), because the optimizer would not always be able to remove references to Infallible.Infallible is (was) defined as an empty enum, and Rust knows very well that empty enums cannot be instantiated. For example, you can legally write something like the following:let Ok(s) = String::FromStr("hello world!");Note the complete lack of an Err case. This works even without the never type stabilization, because Rust knows the Err() case can't really exist. If this is known early enough for the above code to type-check successfully, then it obviously should also be known at trans (which is much later in the compilation process).The real problem with Infallible is mostly that it has a silly name and does not auto-coerce at all. The latter can be worked around by writing match(x) {} where x is (or contains) an Infallible. The match statement does not require arms because (again) Rust knows that there are no possible values to match against, and does not require any match arms. This expression will coerce into an arbitrary type. But that's more unwieldy than using !, which auto-coerces and doesn't require this workaround.### Void is surprisingly useful.Posted Sep 9, 2026 9:56 UTC (Wed)
 bydcoutts(subscriber, #5387)
 [Link] (24 responses)Haskell has had aVoidtype in the standard library for over 10 years and it is surprisingly useful.I guess Haskell borrowed the namevoidfrom C/C++.In Haskell we represent it as a data type with no constructors, which is similar to Rust's empty enumeration.data Void

-- | Since 'Void' values logically don't exist, this witnesses the
-- logical reasoning tool of \"ex falso quodlibet\".
--
absurd :: Void -> a
absurd a = case a of {}Note the cute empty pattern matchof {}, showing to the compiler that there are no cases. This empty pattern match trick is also useful in other contexts to show that certain cases are impossible (and thus don't need to be handled).There isn't special compiler support forVoidand it is not inserted as a last resort. In Haskell, functions that (very obviously) loop can be inferred to have a polymorphic result type, for example:foo n = foo (n+1)This will be inferred to have typefoo :: forall a b. Num a => a -> bThere's no special case in the language or type system here, this is just the most general type and thus the inferred type.Notice the result is a universally quantified type: for any b. This can be instantiated at a call site at any type. The article describes this as coercion, but in a type system with polymorphism it's better understood as instantiating a polymorphic type variable for another (possibly concrete) type.### Void is surprisingly useful.Posted Sep 9, 2026 11:47 UTC (Wed)
 byralfj(subscriber, #172874)
 [Link] (23 responses)Note that Haskell'sVoidand C'svoidare very different types. If we map them both to Rust, Haskell'sVoidis like!(the empty type) and C'svoidis like()(the unit type). The fact that C'svoidis often described as a "type with no values" is extremely misleading and confusing: C'svoidhas exactly one value, and because there is only one value you don't have to spell it out and it encodes 0 bits of information. In Rust if a function has return type()you also don't need to spell out its return value, but you can if you want -- the syntax for the only value of the unit type is()as well."void" sounds like it should be an empty type, so IMO it is very unfortunate that C picked this term.### Void is surprisingly useful.Posted Sep 9, 2026 12:50 UTC (Wed)
 bytux3(subscriber, #101245)
 [Link] (15 responses)Also note that C's rules around void are too irregular to make it work as a unit type. You can't declare a void variable. It's not really an empty type or a unit type, it's a secret third thing.In C++ this forces templates to special-case void. There was a proposal to make void more regular, but that wasn't going to happen without breakage, so C++ added std::monostate instead, which is actually intended as a unit type.### Void is surprisingly useful.Posted Sep 9, 2026 12:54 UTC (Wed)
 byralfj(subscriber, #172874)
 [Link] (14 responses)I would say `void` is a poorly supported accidental unit type in C. ;)### Void is surprisingly useful.Posted Sep 9, 2026 13:42 UTC (Wed)
 byiabervon(subscriber, #722)
 [Link] (13 responses)I think it's not really a type at all; it's a keyword used in places in type declarations where an optional type parameter isn't used. While "int *" is "pointer to int", "void *" isn't "pointer to void", it's just "pointer". "int (*)(int)" is "function that takes int and returns int", but "void (*)(int)" is "function that takes int and calling it is a statement rather than an expression", and "int (*)(void)" is "function that returns int". Subsequent language design research showed that optional type parameters are a bad idea, and you can make your parameterized types uniform by including some types that the compiler optimizes (like having "function that returns a value you must discard" instead), but that's not how C was designed, so void ends up with all the weirdness that you get if you try to have a value that embodies the effects of not using something optional.### Void is surprisingly useful.Posted Sep 9, 2026 14:52 UTC (Wed)
 byalx.manpages(subscriber, #145117)
 [Link] (3 responses)"void (*)(int)" is "function that takes int and calling it is a statement rather than an expression"void functions still produce expressions. This can be seen in the comma operator:void f(void);

42, f(), 42;exit() returns void, but it's still usable as an expression. You just can't assign it to something, because variables of typevoidare not allowed. But that doesn't make them statements.### Void is surprisingly useful.Posted Sep 9, 2026 16:17 UTC (Wed)
 byNYKevin(subscriber, #129325)
 [Link]I think a better way of expressing it might be "void must be discarded."(I was going to say "void can't be an rvalue," but your example is indeed an rvalue!)### Void is surprisingly useful.Posted Sep 13, 2026 9:35 UTC (Sun)
 bykoflerdavid(subscriber, #176408)
 [Link] (1 responses)Thanks for showing this, I didn't know this compiles.### Void is surprisingly useful.Posted Sep 13, 2026 11:31 UTC (Sun)
 byalx.manpages(subscriber, #145117)
 [Link]Another --more interesting-- example is with the ternary operator:#define assert(e) ((e) ? (void)0 : abort())### Void is surprisingly useful.Posted Sep 9, 2026 14:55 UTC (Wed)
 byalx.manpages(subscriber, #145117)
 [Link] (8 responses)> Subsequent language design research showed that optional type parameters are a bad idea,I'm not sure I understand this. Would you mind rephrasing? Or maybe (or also) showing examples?> and you can make your parameterized types uniform by including some types that the compiler optimizes (like having "function that returns a value you must discard" instead), but that's not how C was designed, so void ends up with all the weirdness that you get if you try to have a value that embodies the effects of not using something optional.### Void is surprisingly useful.Posted Sep 9, 2026 16:40 UTC (Wed)
 byNYKevin(subscriber, #129325)
 [Link] (7 responses)The problem with optional type parameters, in generic code (which is the only kind of code that has "type parameters" of any kind, optional or not), is combinatorial blowup. For each optional type parameter, we must write twice as many implementations. This might be worth it, if we could accomplish something special with optional type parameters that is otherwise impossible. But it turns out that the overwhelming majority of cases look like one of the following:* A user-supplied callback function might be void, so we need not propagate its return value.* The user might only want to use part of our container (e.g. using a hash table as a hash set), so we need not store the rest.* A user-supplied function might be infallible, so we need not handle errors.In other words, the vast majority of cases just look like deleting some code that we don't need. So you don't really need optional type parameters, you just need types that tell the compiler to delete some code. That gives us () and !:* () ("unit") means roughly "don't emit code to store or pass along values of this type." It's a type whose only value is always constant-folded out of existence. It's good for cases where we want the code to do basically the same thing, except without storing a value.* ! ("never") means roughly "don't emit code in any scope where a value of this type is observed to exist." It's a type with no values, so you don't need any code to handle it. It's good for cases where we want some branch(es) to disappear entirely, e.g. for removing error handling or otherwise forcing compile-time evaluation of something.! has the additional behavior of making some pattern matches infallible. If we have a Result<V, !>, it may be infallibly pattern-matched against Ok(v) because Rust knows the Err() case can't exist. This doesn't work with Result<V, ()>, because that means "there is an error case, but no error information is provided" (similar to Option<V>).### Void is surprisingly useful.Posted Sep 9, 2026 17:05 UTC (Wed)
 byiabervon(subscriber, #722)
 [Link]Yeah, that's what I meant. And C started out thinking of types as "how do I interpret the bits in memory or registers" which doesn't encourage having () or ! as types, so void is kind of all of these plus an unsafe Any depending on where you used it instead of a regular type, for one of those use cases.### Void is surprisingly useful.Posted Sep 9, 2026 21:15 UTC (Wed)
 byalx.manpages(subscriber, #145117)
 [Link] (5 responses)The problem with optional type parameters, in generic code (which is the only kind of code that has "type parameters" of any kind, optional or not), is combinatorial blowup. For each optional type parameter, we must write twice as many implementations.Not necessarily. Here's some generic code with a single implementation:#define rvalue(lv) ((void)0, (lv))
#define typeof_typename(T) typeof(*(typeof(T) *){_Generic(0, T: NULL, default: NULL)})
#define mallocarray(...) reallocarray(NULL, __VA_ARGS__)
#define malloc_T(n, T) rvalue((typeof_typename(T) *){mallocarray(n, sizeof(T))})malloc_T() is implemented internally through void* (through reallocarray(3)), but exposes a type-generic API. We could say reallocarray(3) is unsafe, but the exposed API of malloc_T() is safe. And we didn't need an exponential number of implementations. But it can certainly be used with hundreds of types.int *p = malloc_T(42, int);
long *q = malloc_T(6, long);
struct foo *r = malloc_T(7, struct foo);Am I misunderstanding something?### Void is surprisingly useful.Posted Sep 10, 2026 0:19 UTC (Thu)
 byNYKevin(subscriber, #129325)
 [Link] (4 responses)An "optional type parameter" is a type parameter that you can leave out at the callsite. In your example, that would mean an API that lets you write malloc_T(37, void) or some other syntax instead of "void", such as malloc_T(37). But you can't do that with your example, because sizeof(void) is nonsense. So your example has a mandatory type parameter, not an optional type parameter.### Void is surprisingly useful.Posted Sep 10, 2026 9:52 UTC (Thu)
 byalx.manpages(subscriber, #145117)
 [Link] (3 responses)Indeed, this API lets you write malloc_T(42, void). It's not allowed in the ISO C dialect, because sizeof(void) is not valid there. But in GNU C, sizeof(void)==1, and thus this is perfectly allowed.alx@devuan:~/tmp$ cat malloc.c 
#include <stdlib.h>

#define rvalue(lv) ((void)0, (lv))
#define typeof_typename(T) typeof(*(typeof(T) *){_Generic(0, T: NULL, default: NULL)})
#define mallocarray(...) reallocarray(NULL, __VA_ARGS__)
#define malloc_T(n, T) rvalue((typeof_typename(T) *){mallocarray(n, sizeof(T))})

int
main(void)
{
	void *p = malloc_T(42, void);

	/*
	 * The memory in 'p' doesn't have an effective type yet at this
	 * point. This is useful for example for creating a memory pool
	 * from which to use memory later.
	 */

	int *i = p;
	*i = 7;

	/*
	 * The first byte of the pool now has an effective type of
	 * 'int'. The rest remains without effective type.
	 */

	free(p);
}$ gcc -Wall -Wextra malloc.c 
$### Void is surprisingly useful.Posted Sep 10, 2026 9:53 UTC (Thu)
 byalx.manpages(subscriber, #145117)
 [Link]/*
	 * The first byte of the pool now has an effective type of
	 * 'int'. The rest remains without effective type.
	 */Oh, well, I meant the first 4 bytes, of course. :)### Void is surprisingly useful.Posted Sep 11, 2026 22:29 UTC (Fri)
 byNYKevin(subscriber, #129325)
 [Link] (1 responses)Not sure I would characterize that as an "optional" type parameter. I would maybe call it "GNU C decided to make void act more like a real type, and less like the absence of a type." Anyway, if you're going to give examples in GNU C, you should specify. ISO is the standard dialect (GCC's out-of-the-box behavior notwithstanding).Of course, there has to be some allowance for special cases where you don't need multiple implementations, because you could always write a function that does not actually use its type parameter. But my point is that in the general case, where you may want to write arbitrary code, you do face a combinatorial explosion. There might happen to be a few special cases where it's not strictly necessary... but Rust in particular is not a fan of this sort of thing.In Rust (unlike C++), generic definitions have to be valid for all possible choices of parameters, not just for the particular invocation(s) that happen to appear in your project. This is essential for backwards compatibility. If someone calls into your function in version 1.0 with a given set of generic parameters, then that same set of parameters ought to work in version 1.1 (assuming you follow semver or something like semver). Rust upholds that guarantee without forcing you to test all possible (or all "reasonable") combinations of parameters manually, because it does type checking before the generics are monomorphized. By the time parameters are actually substituted, we already know that the resulting code will compile. And you know that you're backwards compatible as long as you didn't change the signature (which includes information about which types are "allowed" to be used as type parameters).So now you can see the issue: If we want to allow for "optional" type parameters in Rust, we need to fit them into the type checking scheme. At that point, it is a lot easier to say "OK, we're promoting these empty values to full types and giving them completely regular type-level semantics" than it is to say "OK, we're going to litter the generic type logic with dozens of special cases scattered all over the place just in case a type parameter turns out to be empty."### Void is surprisingly useful.Posted Sep 11, 2026 23:25 UTC (Fri)
 byalx.manpages(subscriber, #145117)
 [Link]> Anyway, if you're going to give examples in GNU C, you should specify. ISO is the standard dialect (GCC's out-of-the-box behavior notwithstanding).I say it now. ISO C is like speaking standard Latin: nobody does it, and nobody ever did (except maybe a few Romans, during a few years, and maybe neither). It's good as a guideline on which to base dialects, not as an actual dialect meant to be directly useful. Very few programs (none that are non-trivial?) are strictly conforming to ISO C (and even less to ISO C90).> But my point is that in the general case, where you may want to write arbitrary code, you do face a combinatorial explosion. There might happen to be a few special cases where it's not strictly necessary...I write a lot of type-generic code using GNU C23, and only have a few places where I've had to duplicate code; they are the special case, IME. We're working to improve the language in ways that those special cases may not be needed in the future.> but Rust in particular is not a fan of this sort of thing.I don't write any Rust, but this seems consistent with what I've heard, and with the little Rust I've read: it tends to be more verbose than C.### Regular voidPosted Sep 10, 2026 9:57 UTC (Thu)
 bytialaramex(subscriber, #21167)
 [Link] (6 responses)In C++ this idea that their void should be a unit type often comes up as "Regular void" to distinguish this from the present status that void is irregular because it is treated as "incomplete" in their language whereas a pointer to void is an actual type.Here's an example of a "Regular void" proposal for C++https://open-std.org/JTC1/SC22/WG21/docs/papers/2016/p014...But while "regular void" is superficially attractive, it can't really work in C or C++ and that proposal illustrates some of the difficulty and I'm sure responses when it was presented get into some others.Basically C has a crap type system and C++ mostly makes things worse rather than better, a "regular void" might be a reasonable patch in a good type system, but in C++ it just substitutes one set of crazy edge cases for a different set of crazy edge cases.### Regular voidPosted Sep 10, 2026 10:24 UTC (Thu)
 byralfj(subscriber, #172874)
 [Link] (4 responses)Fixing such an early mistake in a language with a huge installed base is indeed hard. Rust made the right call with()(ourvoidequivalent) from the start, but we made!not-a-type initially and it took us 10 years and I don't even remember how many attempts to fix that...### Regular voidPosted Sep 10, 2026 11:05 UTC (Thu)
 bytialaramex(subscriber, #21167)
 [Link] (3 responses)I used to have a lot more sympathy for the "It's hard to fix" people before I saw how hard WG21 worked to shoot down Epochs (an attempt to give C++ a feature like Rust's editions, after seeing it work just once in 2018 Edition) and Sean's "Safe C++" work and read JeanHeyd's lengthy battle to land #embed in C at WG14These are not people who tried hard to improve the language but were foiled by how difficult it was to deliver because the language is very old, they're people who didn't want to change and found every excuse possible for why everything must remain exactly as it is. Computer Science is a young discipline, and I'm an old man, but this sort of thing is how we get that saying "Science advances one funeral at a time".### Regular voidPosted Sep 11, 2026 17:49 UTC (Fri)
 bywahern(subscriber, #37304)
 [Link] (2 responses)Well, #embed has already had to undergo revision shortly after standardization in C23:https://www.open-std.org/jtc1/sc22/wg14/www/docs/n3912.htmEven the simplest features can be tricky.Granted, the headaches come from C wanting to support some degree of source-level compatibility with C++, as well as having many implementations, including multiple *major* implementations. These are headaches languages like Rust don't have to deal with. An implementation quirk in Rust can just become the de facto standard, or supported as hack through backward compatibility features. But when you have multiple implementations that diverge, there's no tidy way to fix that mess.### Regular voidPosted Sep 11, 2026 18:58 UTC (Fri)
 bymb(subscriber, #50428)
 [Link] (1 responses)>wanting to support some degree of source-level compatibility with C++Not having an FFI between C++ and C is a major problem.Having it would free C++ from many of the compatibility problems.It is fixable by introducing it in a new standard version.But there does not seem to be willingness to do it - I presume - as it would complicate programs that mix C and C++ willy-nilly### Regular voidPosted Sep 11, 2026 22:51 UTC (Fri)
 bywahern(subscriber, #37304)
 [Link]Almost certainly will never happen. My impression is the committee avoids name mangling like the plague. And name mangling aside, I assume there's a host of other thorny issues regarding parameter passing (e.g. references, implicit this, etc) that nobody wants to tackle. Is there any prior art? I don't remember GCC or clang having any extensions to help calling into non-extern-C C++.### Regular voidPosted Sep 11, 2026 22:04 UTC (Fri)
 bymagfr(subscriber, #16052)
 [Link]When I read this I thought it looked more like the proposed bottom type ofP3549R0.### nice writeupPosted Sep 10, 2026 8:49 UTC (Thu)
 byzuki(subscriber, #41808)
 [Link]The topic is complicated and this explanation was very pleasant to read.### Never traitsPosted Sep 11, 2026 4:16 UTC (Fri)
 bytsavola(subscriber, #37605)
 [Link] (5 responses)After this change (and on the 2024 edition), the compiler assumes that T should be !, which doesn't implement Default, and therefore causes a compilation error.Couldn't ! just be assumed to implement any and all traits?### Never traitsPosted Sep 11, 2026 5:39 UTC (Fri)
 bymicka(subscriber, #38720)
 [Link] (3 responses)For Default, you need to provide one value, and you can’t do that for !.### Never traitsPosted Sep 11, 2026 5:50 UTC (Fri)
 bytsavola(subscriber, #37605)
 [Link] (2 responses)Yes, but with ! that code path is never reached. The compiler could say that it can, because it never has to.### Never traitsPosted Sep 11, 2026 6:57 UTC (Fri)
 bytaladar(subscriber, #68407)
 [Link] (1 responses)But that is not how traits work in Rust. What you suggest would be true if all traits just had their types appear in parameter position in the methods they implement but traits like Default have them appear only in return type position where you absolutely have to come up with a value if someone calls <! as Default>::default()### Never traitsPosted Sep 11, 2026 7:17 UTC (Fri)
 bytsavola(subscriber, #37605)
 [Link]Okay, I see.### Never traitsPosted Sep 12, 2026 7:52 UTC (Sat)
 byNYKevin(subscriber, #129325)
 [Link]Sort of, but not exactly. I believe this confusion arises from conflating traits with types.Instances of ! can be coerced into arbitrary types. So if you're coming from another language, it might seem intuitive to assume that this means ! should implement all traits. But it is important to remember that traits are not types.If types are nouns, traits are adjectives. Or to put it another way, a trait specifies a family or category of types, not a type in its own right. This differs significantly from interfaces in languages that support them (Go, Java, etc.), where you can simply treat an interface as if it is a type for all purposes (except for calling the nonexistent constructor). You can turn a trait into a type by prefixing it with the keywords dyn or impl, but those are not the same as the trait itself, and have important differences in their semantics:* dyn Trait is only compatible with some traits. It is also dynamically sized and must exist behind a pointer, in a language with manual memory management and no GC. Either of those restrictions in isolation would be far too annoying for dyn Trait to be the type-level equivalent of Trait (but early Rust did try to make this work). This also implies the use of a vtable for dynamic dispatch (hence the name "dyn"), and the incompatibility stems from methods that do things like passing Self by value, not having a receiver at all, having type parameters, etc. (none of which can be dynamically dispatched in Rust).* impl Trait is compatible with all traits, but it's a form of generics. Generics must be tied to some function or other context that tells the compiler how they should be monomorphized. So you can't treat it as a general-purpose type-level equivalent of Trait, because in non-generic contexts, this would make no sense. In a generic context, impl Trait should be read as "some type which implements Trait, but I'm not going to tell you what type it is."The Default trait, in particular, is the Rust equivalent of what C++ calls "having a default constructor." It is not a type, nor does it have a type-level equivalent in most languages.