---
title: The Best C++ Library · mcyoung
url: https://mcyoung.xyz/2025/07/14/best/#fnref:terrible-people
site_name: lobsters
fetched_at: '2025-07-15T23:05:52.331000'
original_url: https://mcyoung.xyz/2025/07/14/best/#fnref:terrible-people
date: '2025-07-15'
tags: c++
---

2025-07-14 • 4003 words • 44 minutes

•

#c++
 •
#language-design
 •
#metaprogramming



# The Best C++ Library





It’s no secret that my taste in programming languages is very weird for a programming languageenthusiastprofessional. Several of mylastfewpostsare about Go, broadly regarded as the programming language equivalent of eating plain oatmeal for breakfast.



To make up for that, I’m going to write about the programming language equivalent of diluting your morning coffee withEverclear. I am, of course, talking about C++.



If you’ve ever had the misfortune of doing C++ professionally, you’ll know that the C++ standard library is really bad. Where to begin?



Well, the associative containers are terrible. Due to bone-headed API decisions,std::unordered_mapMUST be a closed-addressing, array-of-linked-lists map, not a Swisstable, despite closed-addressing being an outdated technology.std::map, which is not what you usually want,mustbe a red-black tree. It can’t be a b-tree, like every sensible language provides for the ordered map.



std::optionalis a massive pain in the ass to use, and is full of footguns, likeoperator*.std::variantis also really annoying to use.std::filesystemis full of sharp edges. And where are the APIs for signals?



Everything is extremely wordy.std::hardware_destructive_interference_sizecould have been calledstd::cache_line.std::span::subspancould have usedopeartor[]. The standard algorithms are super wordy, because they deal with iterator pairs. Oh my god, iterator pairs. They addedstd::ranges, which do not measure up to Rust’sIteratorat all!



I’m so mad about all this! The people in charge of C++ clearly, actively hate their users!1They want C++ to be as hard and unpleasant as possible to use. Many brilliant people that I am lucky to consider friends and colleagues, including Titus Winters, JeanHeyd Meneide, Matt Fowles-Kulukundis, and Andy Soffer, have tried and mostly failed2to improve the language.



This is much to say that I believe C++ in its current form is unfixable. But that’s only due to the small-mindedness of a small cabal based out of Redmond. What if we could do whatever we wanted? What if we used C++’s incredible library-building language features to build a brand-new language?



For the last year-or-so I’ve been playing with a wild idea: what would C++ look like if we did it over again? Starting from an empty C++20 file with no access to the standard library, what can we build in its place?



## Starting Over



Titus started Abseil while at Google, whose namespace,absl, is sometimes said to stand for “a better standard library”3. To me, Abseil is important because it was an attempt to work with the existing standard library and make it better, while retaining a high level of implementation quality that a C++ shop’s home-grown utility library won’t have, and a uniformity of vision thatBoostis too all-over-the-place to achieve.



Rather than trying to coexist with the standard library, I want to surpass it. As a form of performance art, I want to discover what the standard library would look like if we designed ittoday, in 2025.



In this sense, I want to build something that isn’t justbetter. It should be the C++ standard library from the best possible world. It is the best possible library. This is why my library’s namespace isbest.



In general, I am trying not to directly copy either what C++, or Abseil, or Rust, or Go did. However, each of them has really interesting ideas, and the best library probably lies in some middle-ground somewhere.



The rest of this post will be about what I have achieved withbestso far, and where I want to take it. You can look at the codehere.



### Building a Foundation



We’re throwing out everything, and that includes<type_traits>. This is a header which shows its age: alias templates were’t added until C++14, and variable templates were added in C++17. As a result, many things that really aught to be concepts have names likebest::is_same_v. All of these now have concept equivalents in<concepts>.



I have opted to try to classify type traits into separate headers to make them easier to find. They all live under//best/meta/traits, and they form the leaves of the dependency graph.



For example,arrays.hcontains all of the array traits, such asbest::is_array,best::un_array(to remove an array extent), andbest::as_array, which applies an extent to a type T, such thatbest::as_array<T, 0>is not an error.



types.hcontains very low-level metaprogramming helpers, such as:


* best::idandbest::val, the identity traits for type- and value-kinded traits.
* best::same<...>, which returns whether an entirepackof types is all equal.
* best::lie, our version ofstd::declval.
* best::select, ourstd::conditional_t.
* best::abridge, a “symbol compression” mechanism for shortening the names of otherwise huge symbols.


funcs.hprovidesbest::tame, which removes the qualifiers from anabominable function type.quals.hprovidesbest::qualifies_to, necessary for determining if a type is “more const” than another.empty.hprovides a standard empty type that interoperates cleanly withvoid.



On top of the type traits is the metaprogramming library//best/meta, which includes generalized constructibility traits ininit.h(e.g., to check that you can, in fact, initialize aT&from aT&&, for example).tlist.hprovides a very general type-level heterogenous list abstraction; a parameter pack as-a-type.



The other part of “the foundation” is//best/base, which mostly provides access to intrinsics, portability helpers, macros, and “tag types” such as our versions ofstd::in_place. For example,macro.hprovidesBEST_STRINGIFY(),port.hprovidesBEST_HAS_INCLUDE(), andhint.hprovidesbest::unreachable().



guard.hprovides our version of the Rust?operator, which is not an expression because statement expressions are broken in Clang.



Finally, within//best/containerwe findbest::object, a special type for turning any C++ type into an object (i.e., a type that you can form a reference to). This is useful for manipulating any type generically, without tripping over the assign-through semantics of references. For example,best::object<T&>is essentially a pointer.



### “ADT” Containers



On top of this foundation we build the basic algebraic data types ofbest:best::rowandbest::choice, which replacestd::tupleandstd::variant.



best::row<A, B, C>is a heterogenous collection of values, stored inside ofbest::objects. This means thatbest::row<int&>has natural rebinding, rather than assign-through, semantics.



Accessing elements is done withat():my_row.at<0>()returns a reference to the first element. Getting the first element is so common that you can also usemy_row.first(). Usingmy_row.object<0>()will return a reference to abest::objectinstead, which can be used for rebinding references. For example:


int

x

=

0
,

y

=

0
;

best
::
row
<
int
&>

a
{
x
};

a
.
at
<
0
>
()

=

42
;

// Writes to x.

a
.
object
<
0
>
()

=

y
;

// Rebinds a.0 to y.

a
.
at
<
0
>
()

=

2
*
x
;

// Writes to y.
C++


There is alsosecond()andlast(), for the other two most common elements to access.



best::rowis named so in reference to database rows: it provides many operations for slicing and dicing thatstd::tupledoes not.



For example, in addition to extracting single elements, it’s also possible to access contiguous subsequences, usingbest::bounds:a.at<best::bounds{.start = 1, .end = 10}>()! There are also a plethora of mutation operations:


* a + bconcatenates tuples, copying or moving as appropriate (a + BEST_MOVE(b)will move out of the elements ofb, for example).
* a.push(x)returns a copy ofawithxappended, whilea.insert<n>(x)does the same at an arbitrary index.
* a.update<n>(x)replacesthenth element withx, potentially of a different type.
* a.remove<n>()deletes thenth element, whilea.erase<...>()deletes a contiguous range.
* a.splice<best::bounds{...}>(...)splices a row into another row, offering a general replace/delete operation that all of the above operations are implemented in terms of.
* gather()andscatter()are even more general, allowing for non-contiguous indexing.


Meanwhile,std::applyis a method now:a.apply(f)callsfwitha’s elements as its arguments.a.each(f)is similar, but instead expands tonunary calls off, one with each element.



Andof course,best::rowsupports structured bindings.



Meanwhile,best::choice<A, B, C>contains precisely one value from various types. There is an underlyingbest::pun<A, B, C>type that implements a variadic untagged union that works around many of C++’s bugs relating to unions with members of non-trivial type.



The most common way to operate on a choice is tomatchon it:


best
::
choice
<
int
,

*
int
,

void
>

z

=

42
;

int

result

=

z
.
match
(


[](
int

x
)

{

return

x
;

},


[](
int
*

x
)

{

return

*
x
;

},


[]

{

return

0
;

}

);
C++


Which case gets called here is chosen by overload resolution, allowing us to write a default case as[](auto&&) { ... }.



Which variant is currently selected can be checked withz.which(), while specific variants can be accessed withz.at(), just like abest::row, except that it returns abest::option<T&>.



best::choiceis what all of the other sum types, likebest::optionandbest::result, are built out of. All of the clever layout optimizations live here.



Speaking ofbest::option<T>, that’s our option type. It’s close in spirit to whatOption<T>is in Rust.besthas a generic niche mechanism that user types can opt into, allowingbest::option<T&>to be the same size as a pointer, usingnullptrfor thebest::nonevariant.



best::optionprovides the usual transformation operations:map,then,filter. Emptiness can be checked withis_empty()orhas_value(). You can even pass a predicate tohas_value()to check the value with, if it’s present:x.has_value([](auto& x) { return x == 42; }).



The value can be accessed usingoperator*andoperator->, likestd::optional; however, this operation is checked, instead of causing UB if the option is empty.value_or()can be used to unwrap with a default; the default can be any number of arguments, which are used to construct the default, or even a callback. For example:


best
::
option
<
Foo
>

x
;

// Pass arguments to the constructor.

do_something
(
x
.
value_or
(
args
,

to
,

foo
));

// Execute arbitrary logic if the value is missing.

do_something
(
x
.
value_or
([]

{


return

Foo
(...);

}))
C++


best::option<void>also Just Works (in fact,best::option<T>is abest::choice<void, T>internally), allowing for truly generic manipulation of optional results.



best::result<T, E>is, unsurprisingly, the analogue of Rust’sResult<T, E>. Because it’s abest::choiceinternally,best::result<void, E>works as you might expect, and is a common return value for I/O operations.



It’s very similar tobest::option, including offeringoperator->for accessing the “ok” variant. This enables succinct idioms:


if

(
auto

r

=

fallible
())

{


r
->
do_something
();

}

else

{


best
::
println
(
"{}"
,

*
r
.
err
());

}
C++


r.ok()andr.err()returnbest::options containing references to the ok and error variants, depending on which is actually present; meanwhile, abest::optioncan be converted into abest::resultusingok_or()orerr_or(), just like in Rust.



best::results are constructed usingbest::okandbest::err. For example:


best
::
result
<
Foo
,

Error
>

r

=

best
::
ok
(
args
,

to
,

foo
);
C++


These internally usebest::args, a wrapper overbest::rowthat represents a “delayed initialization” that can be stored in a value. It will implicitly convert into any type that can be constructed from its elements. For example:


Foo

foo

=

best
::
args
(
args
,

to
,

foo
);

// Calls Foo::Foo(args, to, foo).
C++


Also, every one of the above types is a structural type, meaning it can be used for non-type template parameters!



### Memory and Pointers



Of course, all of these ADTs need to be built on top of pointer operations, which is where//best/memorycomes in.best::ptr<T>is a generalized pointer type that provides many of the same operations as Rust’s raw pointers, including offsetting, copying, and indexing. Like Rust pointers,best::ptr<T>can be a fat pointer, i.e., it can carry additional metadata on top of the pointer. For example,best::ptr<int[]>remembers the size of the array.



Providing metadata for abest::ptris done through a member alias calledBestPtrMetadata. This alias should be private, whichbestis given access to by befriendingbest::access. Types with custom metadata will usually not be directly constructible (because they are of variable size), and must be manipulated exclusively through types likebest::ptr.



Specifying custom metadata allows specifying what the pointer dereferences to. For example,best::ptr<int[]>dereferences to abest::span<int>, meaning that all the span operations are accessible throughoperator->: for example,my_array_ptr->first().



Most of this may seem a bit over-complicated, since ordinary C++ raw pointers and references are fine for most uses. However,best::ptris the foundation upon whichbest::box<T>is built on.best::box<T>is a replacement forstd::unique_ptr<T>that fixes its const correctness and adds RustBox-like helpers.best::box<T[]>also works, but unlikestd::unique_ptr<T[]>, it remembers its size, just likebest::ptr<T[]>.



best::boxis parameterized by its allocator, which must satisfybest::allocator, a much less insane API than whatstd::allocatoroffers.best::mallocis a singleton allocator representing the system allocator.



best::span<T>, mentioned before, is the contiguous memory abstraction, replacingstd::span. Likestd::span,best::span<T, n>is a fixed-length span ofnelements. Unlikestd::span, the second parameter is abest::option<size_t>, not asize_tthat uses-1as a sentinel.



best::span<T>tries to approximate the API ofRust slices, providing indexing, slicing, splicing, search, sort, and more. Naturally, it’s also iterable, both forwards and backwards, and provides splitting iterators, just like Rust.



Slicing and indexing is always bounds-checked. Indexing can be done withsize_tvalues, while slicing uses abest::bounds:


best
::
span
<
int
>

xs

=

...;

auto

x

=

xs
[
5
];

auto

ys

=

xs
[{.
start

=

1
,

.
end

=

6
}];
C++


best::boundsis a generic mechanism for specifying slicing bounds, similar to Rust’srange types. You can specify the start and end (exclusive), likex..yin Rust. You can also specify an inclusive end using.inclusive_end = 5, equivalent to Rust’sx..=y. And you can specify a count, like C++’s slicing operations prefer:{.start = 1, .count = 5}.best::boundsitself provides all of the necessary helpers for performing bounds checks and crashing with a nice error message.best::boundsis also iterable, as we’ll see shortly.



best::layoutis a copy of Rust’sLayouttype, providing similar helpers for performing C++-specific size and address calculations.



### Iterators



C++ iterator pairs suck. C++ ranges suck.bestprovides a new paradigm for iteration that is essentially just RustIteratorshammered into a C++ shape. This library lives in//best/iter.



To define an iterator, you define aniterator implementation type, which must define a member function namednext()that returns abest::option:


class

my_iter_impl

final

{


public:


best
::
option
<
int
>

next
();

};
C++


This type is an implementation detail; the actual iterator type isbest::iter<my_iter_impl>.best::iterprovides all kinds of helpers, just likeIterator, for adapting the iterator or consuming items out of it.



Iterators can override the behavior of some of these adaptors to be more efficient, such as for makingcount()constant-time rather than linear. Iterators can also offer extra methods if they define the member aliasBestIterArrow; for example, the iterators forbest::spanhave a->rest()method for returning the part of the slice that has not been yielded bynext()yet.



One of the most important extension points issize_hint(), analogous toIterator::size_hint(), for right-sizing containers that the iterator is converted to, such as abest::vec.



And of course,best::iterprovidesbegin/endso that it can be used in a C++ range-for loop, just like C++20 ranges do.best::int_range<I>4, whichbest::boundsis an instantiation of, is also an iterator, and can be used much like Rust ranges would:


for

(
auto

i

:

best
::
int_range
<
int
>
{.
start

=

1
,

.
count

=

200
})

{


// ...

}
C++


best::int_rangewill carefully handle all of the awkward corner cases around overflow, such asbest::int_range<uint8_t>{.end_inclusive = 255}.



### Heap Containers



Iterators brings us to the most complex container type that’s checked in right now,best::vec. Not only can you customize its allocator type, but you can customize its small vector optimization type.



Inlibc++,std::strings of at most 23 bytes are storedinline, meaning that the strings’s own storage, rather than heap storage, is used to hold them.best::vecgeneralizes this, by allowing any trivially copyable type to be inlined. Thus, abest::vec<int>will hold at most fiveints inline, on 64-bit targets.



best::vecmostly copies the APIs ofstd::vectorand Rust’sVec. Indexing and slicing works the same as withbest::span, and all of thebest::spanoperations can be accessed through->, allowing for things likemy_vec->sort(...).



I have an active (failing) PR which addsbest::table<K, V>, a general hash table implementation that can be used as either a map or a set. Internally it’s backed by a Swisstable5implementation. Its API resembles neitherstd::unordered_map,absl::flat_hash_map, or Rust’sHashMap. Instead, everything is done through a general entry API, similar to that of Rust, but optimized for clarity and minimizing hash lookups. I want to get it merged soonish.



Beyondbest::table, I plan to addat leastthe following containers:


* best::tree, a btree map/set with a similar API.
* best::heap, a simple min-heap implementation.
* best::lru, abest::tablewith a linked list running through it for in-order iteration and oldest-member eviction.
* best::ring, a ring buffer likeVecDeque.
* best::trie, a port of mytwiecrate.


Possible other ideas:Russ’s sparse array, splay trees, something like Java’sEnumMap, bitset types, and so on.



### Text Handling



best’s string handling is intended to resemble Rust’s as much as possible; it lives within//best/text.best::runeis the Unicode scalar type, which is such that it isalwayswithin the valid range for a Unicode scalar, but including the unpaired surrogates. It offers a number of relatively simple character operations, but I plan to extend it to all kinds of character classes in the future.



best::stris our replacement forbest::string_view, close to Rust’sstr: a sequence of valid UTF-8 bytes, with all kinds of string manipulation operations, such as rune search, splitting, indexing, and so on.



best::runeandbest::struse compiler extensions to ensure that when constructed from literals, they’re constructed fromvalidliterals. This means that the following won’t compile!


best
::
str

invalid

=

"
\xFF
"
;
C++


best::stris abest::spanunder the hood, which can be accessed and manipulated the same way as the underlying&[u8]to&stris.



best::strbufis ourstd::stringequivalent. There isn’t very much to say about it, because it works just like you’d expect, and provides a RustString-like API.



Where this library really shines is that everything is parametrized over encodings.best::stris actually abest::text<best::utf8>;best::str16is thenbest::text<best::utf16>. You can write your own text encodings, too, so long as they are relatively tame and you provide rune encode/decode for them.best::encodingis the concept



best::textis always validly encoded; however, sometimes, that’s not possible. For this reason we havebest::pretext, which is “presumed validly encoded”; its operations can fail or produce replacement characters if invalid code units are found. There is nobest::pretextbuf; instead, you would generally use something like abest::vec<uint8_t>instead.



Unlike C++, the fact that abest::textbufis abest::vecunder the hood is part of the public interface, allowing for cheap conversions and, of course, we getbest::vec’s small vector optimization for free.



bestprovides the following encodings out of the box:best::utf8,best::utf16,best::utf32,best::wtf8,best::ascii, andbest::latin1.



### Formatting



//best/text:formatprovides a Rustformat!()-style text formatting library. It’s as easy as:


auto

str

=

best
::
format
(
"my number: 0x{:08x}"
,

n
);
C++


Through the power of compiler extensions andconstexpr, the format is actually checked at compile time!



The available formats are the same as Rust’s, including the{}vs{:?}distinction. But it’s actually way more flexible. You can use any ASCII letter, and types can provide multiple custom formatting schemes using letters. By convention,x,X,b, andoall mean numeric bases.qwill quote strings, runes, and other text objects;pwill print pointer addresses.



The special format{:!}“forwards from above”; when used in a formatting implementation, it uses the format specifier the caller used. This is useful for causing formats to be “passed through”, such as when printing lists orbest::option.



Any type can be made formattable by providing a friend template ADL extension (FTADLE) calledBestFmt. This is analogous to implementing a trait likefmt::Debugin Rust, however, all formatting operations use the same function; this is similar tofmt.Formatterin Go.



Thebest::formattertype, which gets passed intoBestFmt, is similar to Rust’sFormatter. Beyond being a sink, it also exposes information on the specifier for the formatting operation viacurrent_spec(), and helpers for printing indented lists and blocks.



BestFmtQueryis a related FTADLE that is called to determine what the valid format specifiers for this type are. This allows the format validator to reject formats that a type does not support, such as formatting abest::strwith{:x}.



best::formatreturns (or appends to) abest::strbuf;best::printlnandbest::eprintlncan be used to write to stdout and stderr.



### Reflection



Within the metaprogramming library,//best/meta:reflectoffers a basic form of reflection. It’s not C++26 reflection, because that’s wholely overkill. Instead, it provides a method for introspecting the members of structs and enums.



For example, suppose that we want to have a default way of formatting arbitraryaggregatestructs. The code for doing this is actually devilishly simple:


void

BestFmt
(
auto
&

fmt
,

const

best
::
is_reflected_struct

auto
&

value
)

{


// Reflect the type of the struct.


auto

refl

=

best
::
reflect
<
decltype
(
value
)
>
;


// Start formatting a "record" (key-value pairs).


auto

rec

=

fmt
.
record
(
refl
.
name
());


// For each field in the struct...


refl
.
each
([
&
](
auto

field
)

{


// Add a field to the formatting record...


rec
.
field
(


field
.
name
(),

// ...whose name is the field...


value
->*
field
,

// ...and with the appropriate value.


);


});

}
C++


best::reflectprovides access to the fields (or enum variants) of a user-defined type that opts itself in by providing theBestReflectFTADLE, which tells the reflection framework what the fields are. The simplest version of this FTADLE looks like this:


friend

constexpr

auto

BestReflect
(
auto
&

mirror
,

MyStruct
*
)

{


return

mirror
.
infer
();

}
C++


best::mirroris essentially a “reflection builder” that offers fine-grained control over what reflection actually shows of a struct. This allows for hiding fields, or attachingtagsto specific fields, which generic functions can then introspect usingbest::reflected_field::tags().



The functions onbest::reflected_typeallow iterating over and searching for specific fields (or enum variants); thesebest::reflected_fields provide metadata about a field (such as its name) and allow accessing it, with the same syntax as a pointer-to-member:value->*field.



Explaining the full breadth (and implementation tricks) ofbest::reflectwould be a post of its own, so I’ll leave it at that.



### Unit Tests and Apps



bestprovides a unit testing framework under//best/test, like any good standard library should. To define a test, you define a special kind of global variable:


best
::
test

MyTest

=

[](
best
::
test
&

t
)

{


// Test code.

};
C++


This is very similar to a Go unit test, which defines a function that starts withTestand takes a*testing.Tas its argument. Thebest::test&value offers test assertions and test failures. Through the power of looking at debuginfo, we can extract the nameMyTestfrom the binary, and use that as the name of the test directly.



That’s right, this is a C++ test framework withno macros at all!



Meanwhile, at//best/cliwe can find a robust CLI parsing library, in the spirit of#[derive(clap::Parser)]and other similar Rust libraries. The way it works is you first define a reflectable struct, whose fields correspond to CLI flags. A very basic example of this can be found intest.h, since test binaries define their own flags:


struct

test
::
flags

final

{


best
::
vec
<
best
::
strbuf
>

skip
;


best
::
vec
<
best
::
strbuf
>

filters
;


constexpr

friend

auto

BestReflect
(
auto
&

m
,

flags
*
)

{


return

m
.
infer
()


.
with
(
best
::
cli
::
app
{.
about

=

"a best unit test binary"
})


.
with
(
&
flags
::
skip
,


best
::
cli
::
flag
{


.
arg

=

"FILTER"
,


.
help

=

"Skip tests whose names contain FILTER"
,


})


.
with
(
&
flags
::
filters
,


best
::
cli
::
positional
{


.
name

=

"FILTERS"
,


.
help

=

"Include only tests whose names contain FILTER"
,


});


}

};
C++


Usingbest::mirror::with, we can apply tags to the individual fields that describe how they should be parsed and displayed as CLI flags. A more complicated, full-featured example can be found attoy_flags.h, which exercises most of the CLI parser’s features.



best::parse_flags<MyFlags>(...)can be used to parse a particular flag struct from program inputs, independent of the actualargvof the program. Abest::clicontains the actual parser metadata, but this is not generally user-accessible; it is constructed automatically using reflection.



Streamlining top-level app execution can be done usingbest::app, which fully replaces themain()function. Defining an app is very similar to defining a test:


best
::
app

MyApp

=

[](
MyFlags
&

flags
)

{


// Do something cool!

};
C++


This will automatically record the program inputs, run the flag parser forMyFlags(printing--helpand existing, when requested), and then call the body of the lambda.



The lambda can either returnvoid, anint(as an exit code) or even abest::result, like Rust.best::appis also where theargvof the program can be requested by other parts of the program.



## What’s Next?



There’s still a lot of stuff I want to add tobest. There’s no synchronization primitives, neither atomics nor locks or channels. There’s no I/O; I have a work-in-progress PR to addbest::pathandbest::file. I’d like to write my own math library,best::rc(reference-counting), and portable SIMD. There’s also some other OS APIs I want to build, such as signals and subprocesses. I want to add a robust PRNG, time APIs, networking, and stack symbolization.



Building the best C++ library is a lot of work, not the least because C++ is a very tricky language and writing exhaustive tests is tedious. But it manages to make C++ fun for me again!



I would love to see contributions some day. I don’t expect anyone to actually use this, but to me, it proves C++ could be so much better.



1. They are alsoterrible people.↩
2. I will grant that JeanHeyd has made significant process where many people believed was impossible. He appears to have the indomitable willpower of a shōnen protagonist.↩
3. I have heard an apocryphal story that the namespace was going to beabcorabcl, because it was “Alphabet’s library”. This name was ultimately shot down by the office of the CEO, or so the legend goes.↩
4. This may get renamed tobest::intervalor evenbest::rangeWe’ll see!↩
5. The fourth time I’ve written one in my career, lmao. I also wrote aC implementationat one point. My friend Matt has anexcellent introductionto the Swisstable data structure.↩





## Related Posts










2025-07-14

•

4003

words

•

44

minutes


•

#c++

•

#language-design

•

#metaprogramming



# TheBestC++Library





It’snosecretthatmytasteinprogramminglanguagesisveryweirdforaprogramminglanguageenthusiastprofessional.SeveralofmylastfewpostsareaboutGo,broadlyregardedastheprogramminglanguageequivalentofeatingplainoatmealforbreakfast.



Tomakeupforthat,I’mgoingtowriteabouttheprogramminglanguageequivalentofdilutingyourmorningcoffeewithEverclear.Iam,ofcourse,talkingaboutC++.



Ifyou’veeverhadthemisfortuneofdoingC++professionally,you’llknowthattheC++standardlibraryisreallybad.Wheretobegin?



Well,theassociativecontainersareterrible.Duetobone-headedAPIdecisions,std::unordered_mapMUSTbeaclosed-addressing,array-of-linked-listsmap,notaSwisstable,despiteclosed-addressingbeinganoutdatedtechnology.std::map,whichisnotwhatyouusuallywant,mustbeared-blacktree.Itcan’tbeab-tree,likeeverysensiblelanguageprovidesfortheorderedmap.



std::optionalisamassivepainintheasstouse,andisfulloffootguns,likeoperator*.std::variantisalsoreallyannoyingtouse.std::filesystemisfullofsharpedges.AndwherearetheAPIsforsignals?



Everythingisextremelywordy.std::hardware_destructive_interference_sizecouldhavebeencalledstd::cache_line.std::span::subspancouldhaveusedopeartor[].Thestandardalgorithmsaresuperwordy,becausetheydealwithiteratorpairs.Ohmygod,iteratorpairs.Theyaddedstd::ranges,whichdonotmeasureuptoRust’sIteratoratall!



I’msomadaboutallthis!ThepeopleinchargeofC++clearly,activelyhatetheirusers!1TheywantC++tobeashardandunpleasantaspossibletouse.ManybrilliantpeoplethatIamluckytoconsiderfriendsandcolleagues,includingTitusWinters,JeanHeydMeneide,MattFowles-Kulukundis,andAndySoffer,havetriedandmostlyfailed2toimprovethelanguage.



ThisismuchtosaythatIbelieveC++initscurrentformisunfixable.Butthat’sonlyduetothesmall-mindednessofasmallcabalbasedoutofRedmond.Whatifwecoulddowhateverwewanted?WhatifweusedC++’sincrediblelibrary-buildinglanguagefeaturestobuildabrand-newlanguage?



Forthelastyear-or-soI’vebeenplayingwithawildidea:whatwouldC++looklikeifwediditoveragain?StartingfromanemptyC++20filewithnoaccesstothestandardlibrary,whatcanwebuildinitsplace?



## StartingOver



TitusstartedAbseilwhileatGoogle,whosenamespace,absl,issometimessaidtostandfor“abetterstandardlibrary”3.Tome,Abseilisimportantbecauseitwasanattempttoworkwiththeexistingstandardlibraryandmakeitbetter,whileretainingahighlevelofimplementationqualitythataC++shop’shome-grownutilitylibrarywon’thave,andauniformityofvisionthatBoostistooall-over-the-placetoachieve.



Ratherthantryingtocoexistwiththestandardlibrary,Iwanttosurpassit.Asaformofperformanceart,Iwanttodiscoverwhatthestandardlibrarywouldlooklikeifwedesignedittoday,in2025.



Inthissense,Iwanttobuildsomethingthatisn’tjustbetter.ItshouldbetheC++standardlibraryfromthebestpossibleworld.Itisthebestpossiblelibrary.Thisiswhymylibrary’snamespaceisbest.



Ingeneral,IamtryingnottodirectlycopyeitherwhatC++,orAbseil,orRust,orGodid.However,eachofthemhasreallyinterestingideas,andthebestlibraryprobablyliesinsomemiddle-groundsomewhere.



TherestofthispostwillbeaboutwhatIhaveachievedwithbestsofar,andwhereIwanttotakeit.Youcanlookatthecodehere.



### BuildingaFoundation



We’rethrowingouteverything,andthatincludes.Thisisaheaderwhichshowsitsage:aliastemplateswere’taddeduntilC++14,andvariabletemplateswereaddedinC++17.Asaresult,manythingsthatreallyaughttobeconceptshavenameslikebest::is_same_v.Allofthesenowhaveconceptequivalentsin.



Ihaveoptedtotrytoclassifytypetraitsintoseparateheaderstomakethemeasiertofind.Theyallliveunder//best/meta/traits,andtheyformtheleavesofthedependencygraph.



Forexample,arrays.hcontainsallofthearraytraits,suchasbest::is_array,best::un_array(toremoveanarrayextent),andbest::as_array,whichappliesanextenttoatypeT,suchthatbest::as_array0>isnotanerror.



types.hcontainsverylow-levelmetaprogramminghelpers,suchas:


* best::idandbest::val,theidentitytraitsfortype-andvalue-kindedtraits.
* best::same<...>,whichreturnswhetheranentirepackoftypesisallequal.
* best::lie,ourversionofstd::declval.
* best::select,ourstd::conditional_t.
* best::abridge,a“symbolcompression”mechanismforshorteningthenamesofotherwisehugesymbols.


funcs.hprovidesbest::tame,whichremovesthequalifiersfromanabominablefunctiontype.quals.hprovidesbest::qualifies_to,necessaryfordeterminingifatypeis“moreconst”thananother.empty.hprovidesastandardemptytypethatinteroperatescleanlywithvoid.



Ontopofthetypetraitsisthemetaprogramminglibrary//best/meta,whichincludesgeneralizedconstructibilitytraitsininit.h(e.g.,tocheckthatyoucan,infact,initializeaT&fromaT&&,forexample).tlist.hprovidesaverygeneraltype-levelheterogenouslistabstraction;aparameterpackas-a-type.



Theotherpartof“thefoundation”is//best/base,whichmostlyprovidesaccesstointrinsics,portabilityhelpers,macros,and“tagtypes”suchasourversionsofstd::in_place.Forexample,macro.hprovidesBEST_STRINGIFY(),port.hprovidesBEST_HAS_INCLUDE(),andhint.hprovidesbest::unreachable().



guard.hprovidesourversionoftheRust?operator,whichisnotanexpressionbecausestatementexpressionsarebrokeninClang.



Finally,within//best/containerwefindbest::object,aspecialtypeforturninganyC++typeintoanobject(i.e.,atypethatyoucanformareferenceto).Thisisusefulformanipulatinganytypegenerically,withouttrippingovertheassign-throughsemanticsofreferences.Forexample,best::objectisessentiallyapointer.



### “ADT”Containers



Ontopofthisfoundationwebuildthebasicalgebraicdatatypesofbest:best::rowandbest::choice,whichreplacestd::tupleandstd::variant.



best::rowB,C>isaheterogenouscollectionofvalues,storedinsideofbest::objects.Thismeansthatbest::rowhasnaturalrebinding,ratherthanassign-through,semantics.



Accessingelementsisdonewithat():my_row.at<0>()returnsareferencetothefirstelement.Gettingthefirstelementissocommonthatyoucanalsousemy_row.first().Usingmy_row.object<0>()willreturnareferencetoabest::objectinstead,whichcanbeusedforrebindingreferences.Forexample:



int

x

=

0
,

y

=

0
;

best
::
row
<
int
&>

a
{
x
};

a
.
at
<
0
>
()

=

42
;

//

Writes

to

x.

a
.
object
<
0
>
()

=

y
;

//

Rebinds

a.0

to

y.

a
.
at
<
0
>
()

=

2
*
x
;

//

Writes

to

y.
C++



Thereisalsosecond()andlast(),fortheothertwomostcommonelementstoaccess.



best::rowisnamedsoinreferencetodatabaserows:itprovidesmanyoperationsforslicinganddicingthatstd::tupledoesnot.



Forexample,inadditiontoextractingsingleelements,it’salsopossibletoaccesscontiguoussubsequences,usingbest::bounds:a.at=1,.end=10}>()!Therearealsoaplethoraofmutationoperations:


* a+bconcatenatestuples,copyingormovingasappropriate(a+BEST_MOVE(b)willmoveoutoftheelementsofb,forexample).
* a.push(x)returnsacopyofawithxappended,whilea.insert(x)doesthesameatanarbitraryindex.
* a.update(x)replacesthenthelementwithx,potentiallyofadifferenttype.
* a.remove()deletesthenthelement,whilea.erase<...>()deletesacontiguousrange.
* a.splice(...)splicesarowintoanotherrow,offeringageneralreplace/deleteoperationthatalloftheaboveoperationsareimplementedintermsof.
* gather()andscatter()areevenmoregeneral,allowingfornon-contiguousindexing.


Meanwhile,std::applyisamethodnow:a.apply(f)callsfwitha’selementsasitsarguments.a.each(f)issimilar,butinsteadexpandstonunarycallsoff,onewitheachelement.



Andofcourse,best::rowsupportsstructuredbindings.



Meanwhile,best::choiceB,C>containspreciselyonevaluefromvarioustypes.Thereisanunderlyingbest::punB,C>typethatimplementsavariadicuntaggedunionthatworksaroundmanyofC++’sbugsrelatingtounionswithmembersofnon-trivialtype.



Themostcommonwaytooperateonachoiceistomatchonit:



best
::
choice
<
int
,

*
int
,

void
>

z

=

42
;

int

result

=

z
.
match
(


[](
int

x
)

{

return

x
;

},


[](
int
*

x
)

{

return

*
x
;

},


[]

{

return

0
;

}

);
C++



Whichcasegetscalledhereischosenbyoverloadresolution,allowingustowriteadefaultcaseas[](auto&&){...}.



Whichvariantiscurrentlyselectedcanbecheckedwithz.which(),whilespecificvariantscanbeaccessedwithz.at(),justlikeabest::row,exceptthatitreturnsabest::option.



best::choiceiswhatalloftheothersumtypes,likebest::optionandbest::result,arebuiltoutof.Allofthecleverlayoutoptimizationslivehere.



Speakingofbest::option,that’souroptiontype.It’scloseinspirittowhatOptionisinRust.besthasagenericnichemechanismthatusertypescanoptinto,allowingbest::optiontobethesamesizeasapointer,usingnullptrforthebest::nonevariant.



best::optionprovidestheusualtransformationoperations:map,then,filter.Emptinesscanbecheckedwithis_empty()orhas_value().Youcanevenpassapredicatetohas_value()tocheckthevaluewith,ifit’spresent:x.has_value([](auto&x){returnx==42;}).



Thevaluecanbeaccessedusingoperator*andoperator->,likestd::optional;however,thisoperationischecked,insteadofcausingUBiftheoptionisempty.value_or()canbeusedtounwrapwithadefault;thedefaultcanbeanynumberofarguments,whichareusedtoconstructthedefault,orevenacallback.Forexample:



best
::
option
<
Foo
>

x
;

//

Pass

arguments

to

the

constructor.

do_something
(
x
.
value_or
(
args
,

to
,

foo
));

//

Execute

arbitrary

logic

if

the

value

is

missing.

do_something
(
x
.
value_or
([]

{


return

Foo
(...);

}))
C++



best::optionalsoJustWorks(infact,best::optionisabest::choiceT>internally),allowingfortrulygenericmanipulationofoptionalresults.



best::resultE>is,unsurprisingly,theanalogueofRust’sResultE>.Becauseit’sabest::choiceinternally,best::resultE>worksasyoumightexpect,andisacommonreturnvalueforI/Ooperations.



It’sverysimilartobest::option,includingofferingoperator->foraccessingthe“ok”variant.Thisenablessuccinctidioms:



if

(
auto

r

=

fallible
())

{


r
->
do_something
();

}

else

{


best
::
println
(
"{}"
,

*
r
.
err
());

}
C++



r.ok()andr.err()returnbest::optionscontainingreferencestotheokanderrorvariants,dependingonwhichisactuallypresent;meanwhile,abest::optioncanbeconvertedintoabest::resultusingok_or()orerr_or(),justlikeinRust.



best::resultsareconstructedusingbest::okandbest::err.Forexample:



best
::
result
<
Foo
,

Error
>

r

=

best
::
ok
(
args
,

to
,

foo
);
C++



Theseinternallyusebest::args,awrapperoverbest::rowthatrepresentsa“delayedinitialization”thatcanbestoredinavalue.Itwillimplicitlyconvertintoanytypethatcanbeconstructedfromitselements.Forexample:



Foo

foo

=

best
::
args
(
args
,

to
,

foo
);

//

Calls

Foo::Foo(args,

to,

foo).
C++



Also,everyoneoftheabovetypesisastructuraltype,meaningitcanbeusedfornon-typetemplateparameters!



### MemoryandPointers



Ofcourse,alloftheseADTsneedtobebuiltontopofpointeroperations,whichiswhere//best/memorycomesin.best::ptrisageneralizedpointertypethatprovidesmanyofthesameoperationsasRust’srawpointers,includingoffsetting,copying,andindexing.LikeRustpointers,best::ptrcanbeafatpointer,i.e.,itcancarryadditionalmetadataontopofthepointer.Forexample,best::ptrremembersthesizeofthearray.



Providingmetadataforabest::ptrisdonethroughamemberaliascalledBestPtrMetadata.Thisaliasshouldbeprivate,whichbestisgivenaccesstobybefriendingbest::access.Typeswithcustommetadatawillusuallynotbedirectlyconstructible(becausetheyareofvariablesize),andmustbemanipulatedexclusivelythroughtypeslikebest::ptr.



Specifyingcustommetadataallowsspecifyingwhatthepointerdereferencesto.Forexample,best::ptrdereferencestoabest::span,meaningthatallthespanoperationsareaccessiblethroughoperator->:forexample,my_array_ptr->first().



Mostofthismayseemabitover-complicated,sinceordinaryC++rawpointersandreferencesarefineformostuses.However,best::ptristhefoundationuponwhichbest::boxisbuilton.best::boxisareplacementforstd::unique_ptrthatfixesitsconstcorrectnessandaddsRustBox-likehelpers.best::boxalsoworks,butunlikestd::unique_ptr,itremembersitssize,justlikebest::ptr.



best::boxisparameterizedbyitsallocator,whichmustsatisfybest::allocator,amuchlessinsaneAPIthanwhatstd::allocatoroffers.best::mallocisasingletonallocatorrepresentingthesystemallocator.



best::span,mentionedbefore,isthecontiguousmemoryabstraction,replacingstd::span.Likestd::span,best::spann>isafixed-lengthspanofnelements.Unlikestd::span,thesecondparameterisabest::option,notasize_tthatuses-1asasentinel.



best::spantriestoapproximatetheAPIofRustslices,providingindexing,slicing,splicing,search,sort,andmore.Naturally,it’salsoiterable,bothforwardsandbackwards,andprovidessplittingiterators,justlikeRust.



Slicingandindexingisalwaysbounds-checked.Indexingcanbedonewithsize_tvalues,whileslicingusesabest::bounds:



best
::
span
<
int
>

xs

=

...;

auto

x

=

xs
[
5
];

auto

ys

=

xs
[{.
start

=

1
,

.
end

=

6
}];
C++



best::boundsisagenericmechanismforspecifyingslicingbounds,similartoRust’srangetypes.Youcanspecifythestartandend(exclusive),likex..yinRust.Youcanalsospecifyaninclusiveendusing.inclusive_end=5,equivalenttoRust’sx..=y.Andyoucanspecifyacount,likeC++’sslicingoperationsprefer:{.start=1,.count=5}.best::boundsitselfprovidesallofthenecessaryhelpersforperformingboundschecksandcrashingwithaniceerrormessage.best::boundsisalsoiterable,aswe’llseeshortly.



best::layoutisacopyofRust’sLayouttype,providingsimilarhelpersforperformingC++-specificsizeandaddresscalculations.



### Iterators



C++iteratorpairssuck.C++rangessuck.bestprovidesanewparadigmforiterationthatisessentiallyjustRustIteratorshammeredintoaC++shape.Thislibrarylivesin//best/iter.



Todefineaniterator,youdefineaniteratorimplementationtype,whichmustdefineamemberfunctionnamednext()thatreturnsabest::option:



class

my_iter_impl

final

{


public:


best
::
option
<
int
>

next
();

};
C++



Thistypeisanimplementationdetail;theactualiteratortypeisbest::iter.best::iterprovidesallkindsofhelpers,justlikeIterator,foradaptingtheiteratororconsumingitemsoutofit.



Iteratorscanoverridethebehaviorofsomeoftheseadaptorstobemoreefficient,suchasformakingcount()constant-timeratherthanlinear.IteratorscanalsoofferextramethodsiftheydefinethememberaliasBestIterArrow;forexample,theiteratorsforbest::spanhavea->rest()methodforreturningthepartoftheslicethathasnotbeenyieldedbynext()yet.



Oneofthemostimportantextensionpointsissize_hint(),analogoustoIterator::size_hint(),forright-sizingcontainersthattheiteratorisconvertedto,suchasabest::vec.



Andofcourse,best::iterprovidesbegin/endsothatitcanbeusedinaC++range-forloop,justlikeC++20rangesdo.best::int_range4,whichbest::boundsisaninstantiationof,isalsoaniterator,andcanbeusedmuchlikeRustrangeswould:



for

(
auto

i

:

best
::
int_range
<
int
>
{.
start

=

1
,

.
count

=

200
})

{


//

...

}
C++



best::int_rangewillcarefullyhandlealloftheawkwardcornercasesaroundoverflow,suchasbest::int_range{.end_inclusive=255}.



### HeapContainers



Iteratorsbringsustothemostcomplexcontainertypethat’scheckedinrightnow,best::vec.Notonlycanyoucustomizeitsallocatortype,butyoucancustomizeitssmallvectoroptimizationtype.



Inlibc++,std::stringsofatmost23bytesarestoredinline,meaningthatthestrings’sownstorage,ratherthanheapstorage,isusedtoholdthem.best::vecgeneralizesthis,byallowinganytriviallycopyabletypetobeinlined.Thus,abest::vecwillholdatmostfiveintsinline,on64-bittargets.



best::vecmostlycopiestheAPIsofstd::vectorandRust’sVec.Indexingandslicingworksthesameaswithbest::span,andallofthebest::spanoperationscanbeaccessedthrough->,allowingforthingslikemy_vec->sort(...).



Ihaveanactive(failing)PRwhichaddsbest::tableV>,ageneralhashtableimplementationthatcanbeusedaseitheramaporaset.Internallyit’sbackedbyaSwisstable5implementation.ItsAPIresemblesneitherstd::unordered_map,absl::flat_hash_map,orRust’sHashMap.Instead,everythingisdonethroughageneralentryAPI,similartothatofRust,butoptimizedforclarityandminimizinghashlookups.Iwanttogetitmergedsoonish.



Beyondbest::table,Iplantoaddatleastthefollowingcontainers:


* best::tree,abtreemap/setwithasimilarAPI.
* best::heap,asimplemin-heapimplementation.
* best::lru,abest::tablewithalinkedlistrunningthroughitforin-orderiterationandoldest-membereviction.
* best::ring,aringbufferlikeVecDeque.
* best::trie,aportofmytwiecrate.


Possibleotherideas:Russ’ssparsearray,splaytrees,somethinglikeJava’sEnumMap,bitsettypes,andsoon.



### TextHandling



best’sstringhandlingisintendedtoresembleRust’sasmuchaspossible;itliveswithin//best/text.best::runeistheUnicodescalartype,whichissuchthatitisalwayswithinthevalidrangeforaUnicodescalar,butincludingtheunpairedsurrogates.Itoffersanumberofrelativelysimplecharacteroperations,butIplantoextendittoallkindsofcharacterclassesinthefuture.



best::strisourreplacementforbest::string_view,closetoRust’sstr:asequenceofvalidUTF-8bytes,withallkindsofstringmanipulationoperations,suchasrunesearch,splitting,indexing,andsoon.



best::runeandbest::strusecompilerextensionstoensurethatwhenconstructedfromliterals,they’reconstructedfromvalidliterals.Thismeansthatthefollowingwon’tcompile!



best
::
str

invalid

=

"
\xFF
"
;
C++



best::strisabest::spanunderthehood,whichcanbeaccessedandmanipulatedthesamewayastheunderlying&[u8]to&stris.



best::strbufisourstd::stringequivalent.Thereisn’tverymuchtosayaboutit,becauseitworksjustlikeyou’dexpect,andprovidesaRustString-likeAPI.



Wherethislibraryreallyshinesisthateverythingisparametrizedoverencodings.best::strisactuallyabest::text;best::str16isthenbest::text.Youcanwriteyourowntextencodings,too,solongastheyarerelativelytameandyouprovideruneencode/decodeforthem.best::encodingistheconcept



best::textisalwaysvalidlyencoded;however,sometimes,that’snotpossible.Forthisreasonwehavebest::pretext,whichis“presumedvalidlyencoded”;itsoperationscanfailorproducereplacementcharactersifinvalidcodeunitsarefound.Thereisnobest::pretextbuf;instead,youwouldgenerallyusesomethinglikeabest::vecinstead.



UnlikeC++,thefactthatabest::textbufisabest::vecunderthehoodispartofthepublicinterface,allowingforcheapconversionsand,ofcourse,wegetbest::vec’ssmallvectoroptimizationforfree.



bestprovidesthefollowingencodingsoutofthebox:best::utf8,best::utf16,best::utf32,best::wtf8,best::ascii,andbest::latin1.



### Formatting



//best/text:formatprovidesaRustformat!()-styletextformattinglibrary.It’saseasyas:



auto

str

=

best
::
format
(
"my

number:

0x{:08x}"
,

n
);
C++



Throughthepowerofcompilerextensionsandconstexpr,theformatisactuallycheckedatcompiletime!



TheavailableformatsarethesameasRust’s,includingthe{}vs{:?}distinction.Butit’sactuallywaymoreflexible.YoucanuseanyASCIIletter,andtypescanprovidemultiplecustomformattingschemesusingletters.Byconvention,x,X,b,andoallmeannumericbases.qwillquotestrings,runes,andothertextobjects;pwillprintpointeraddresses.



Thespecialformat{:!}“forwardsfromabove”;whenusedinaformattingimplementation,itusestheformatspecifierthecallerused.Thisisusefulforcausingformatstobe“passedthrough”,suchaswhenprintinglistsorbest::option.



AnytypecanbemadeformattablebyprovidingafriendtemplateADLextension(FTADLE)calledBestFmt.Thisisanalogoustoimplementingatraitlikefmt::DebuginRust,however,allformattingoperationsusethesamefunction;thisissimilartofmt.FormatterinGo.



Thebest::formattertype,whichgetspassedintoBestFmt,issimilartoRust’sFormatter.Beyondbeingasink,italsoexposesinformationonthespecifierfortheformattingoperationviacurrent_spec(),andhelpersforprintingindentedlistsandblocks.



BestFmtQueryisarelatedFTADLEthatiscalledtodeterminewhatthevalidformatspecifiersforthistypeare.Thisallowstheformatvalidatortorejectformatsthatatypedoesnotsupport,suchasformattingabest::strwith{:x}.



best::formatreturns(orappendsto)abest::strbuf;best::printlnandbest::eprintlncanbeusedtowritetostdoutandstderr.



### Reflection



Withinthemetaprogramminglibrary,//best/meta:reflectoffersabasicformofreflection.It’snotC++26reflection,becausethat’swholelyoverkill.Instead,itprovidesamethodforintrospectingthemembersofstructsandenums.



Forexample,supposethatwewanttohaveadefaultwayofformattingarbitraryaggregatestructs.Thecodefordoingthisisactuallydevilishlysimple:



void

BestFmt
(
auto
&

fmt
,

const

best
::
is_reflected_struct

auto
&

value
)

{


//

Reflect

the

type

of

the

struct.


auto

refl

=

best
::
reflect
<
decltype
(
value
)
>
;


//

Start

formatting

a

"record"

(key-value

pairs).


auto

rec

=

fmt
.
record
(
refl
.
name
());


//

For

each

field

in

the

struct...


refl
.
each
([
&
](
auto

field
)

{


//

Add

a

field

to

the

formatting

record...


rec
.
field
(


field
.
name
(),

//

...whose

name

is

the

field...


value
->*
field
,

//

...and

with

the

appropriate

value.


);


});

}
C++



best::reflectprovidesaccesstothefields(orenumvariants)ofauser-definedtypethatoptsitselfinbyprovidingtheBestReflectFTADLE,whichtellsthereflectionframeworkwhatthefieldsare.ThesimplestversionofthisFTADLElookslikethis:



friend

constexpr

auto

BestReflect
(
auto
&

mirror
,

MyStruct
*
)

{


return

mirror
.
infer
();

}
C++



best::mirrorisessentiallya“reflectionbuilder”thatoffersfine-grainedcontroloverwhatreflectionactuallyshowsofastruct.Thisallowsforhidingfields,orattachingtagstospecificfields,whichgenericfunctionscanthenintrospectusingbest::reflected_field::tags().



Thefunctionsonbest::reflected_typeallowiteratingoverandsearchingforspecificfields(orenumvariants);thesebest::reflected_fieldsprovidemetadataaboutafield(suchasitsname)andallowaccessingit,withthesamesyntaxasapointer-to-member:value->*field.



Explainingthefullbreadth(andimplementationtricks)ofbest::reflectwouldbeapostofitsown,soI’llleaveitatthat.



### UnitTestsandApps



bestprovidesaunittestingframeworkunder//best/test,likeanygoodstandardlibraryshould.Todefineatest,youdefineaspecialkindofglobalvariable:



best
::
test

MyTest

=

[](
best
::
test
&

t
)

{


//

Test

code.

};
C++



ThisisverysimilartoaGounittest,whichdefinesafunctionthatstartswithTestandtakesa*testing.Tasitsargument.Thebest::test&valueofferstestassertionsandtestfailures.Throughthepoweroflookingatdebuginfo,wecanextractthenameMyTestfromthebinary,andusethatasthenameofthetestdirectly.



That’sright,thisisaC++testframeworkwithnomacrosatall!



Meanwhile,at//best/cliwecanfindarobustCLIparsinglibrary,inthespiritof#[derive(clap::Parser)]andothersimilarRustlibraries.Thewayitworksisyoufirstdefineareflectablestruct,whosefieldscorrespondtoCLIflags.Averybasicexampleofthiscanbefoundintest.h,sincetestbinariesdefinetheirownflags:



struct

test
::
flags

final

{


best
::
vec
<
best
::
strbuf
>

skip
;


best
::
vec
<
best
::
strbuf
>

filters
;


constexpr

friend

auto

BestReflect
(
auto
&

m
,

flags
*
)

{


return

m
.
infer
()


.
with
(
best
::
cli
::
app
{.
about

=

"a

best

unit

test

binary"
})


.
with
(
&
flags
::
skip
,


best
::
cli
::
flag
{


.
arg

=

"FILTER"
,


.
help

=

"Skip

tests

whose

names

contain

FILTER"
,


})


.
with
(
&
flags
::
filters
,


best
::
cli
::
positional
{


.
name

=

"FILTERS"
,


.
help

=

"Include

only

tests

whose

names

contain

FILTER"
,


});


}

};
C++



Usingbest::mirror::with,wecanapplytagstotheindividualfieldsthatdescribehowtheyshouldbeparsedanddisplayedasCLIflags.Amorecomplicated,full-featuredexamplecanbefoundattoy_flags.h,whichexercisesmostoftheCLIparser’sfeatures.



best::parse_flags(...)canbeusedtoparseaparticularflagstructfromprograminputs,independentoftheactualargvoftheprogram.Abest::clicontainstheactualparsermetadata,butthisisnotgenerallyuser-accessible;itisconstructedautomaticallyusingreflection.



Streamliningtop-levelappexecutioncanbedoneusingbest::app,whichfullyreplacesthemain()function.Defininganappisverysimilartodefiningatest:



best
::
app

MyApp

=

[](
MyFlags
&

flags
)

{


//

Do

something

cool!

};
C++



Thiswillautomaticallyrecordtheprograminputs,runtheflagparserforMyFlags(printing--helpandexisting,whenrequested),andthencallthebodyofthelambda.



Thelambdacaneitherreturnvoid,anint(asanexitcode)orevenabest::result,likeRust.best::appisalsowheretheargvoftheprogramcanberequestedbyotherpartsoftheprogram.



## What’sNext?



There’sstillalotofstuffIwanttoaddtobest.There’snosynchronizationprimitives,neitheratomicsnorlocksorchannels.There’snoI/O;Ihaveawork-in-progressPRtoaddbest::pathandbest::file.I’dliketowritemyownmathlibrary,best::rc(reference-counting),andportableSIMD.There’salsosomeotherOSAPIsIwanttobuild,suchassignalsandsubprocesses.IwanttoaddarobustPRNG,timeAPIs,networking,andstacksymbolization.



BuildingthebestC++libraryisalotofwork,nottheleastbecauseC++isaverytrickylanguageandwritingexhaustivetestsistedious.ButitmanagestomakeC++funformeagain!



Iwouldlovetoseecontributionssomeday.Idon’texpectanyonetoactuallyusethis,buttome,itprovesC++couldbesomuchbetter.



1. Theyarealsoterriblepeople.↩
2. IwillgrantthatJeanHeydhasmadesignificantprocesswheremanypeoplebelievedwasimpossible.Heappearstohavetheindomitablewillpowerofashōnenprotagonist.↩
3. Ihaveheardanapocryphalstorythatthenamespacewasgoingtobeabcorabcl,becauseitwas“Alphabet’slibrary”.ThisnamewasultimatelyshotdownbytheofficeoftheCEO,orsothelegendgoes.↩
4. Thismaygetrenamedtobest::intervalorevenbest::rangeWe’llsee!↩
5. ThefourthtimeI’vewrittenoneinmycareer,lmao.IalsowroteaCimplementationatonepoint.MyfriendMatthasanexcellentintroductiontotheSwisstabledatastructure.↩





## RelatedPosts
