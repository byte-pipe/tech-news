---
title: Store tags after payloads
url: https://www.scattered-thoughts.net/writing/store-tags-after-payloads/
site_name: lobsters
fetched_at: '2025-07-14T23:07:17.014070'
original_url: https://www.scattered-thoughts.net/writing/store-tags-after-payloads/
date: '2025-07-14'
tags: plt
---

The short version of this shower thought: storing the tags for sum types after the payload rather than before can save a surprising amount of space.

The long version needs some context.

A pointer has alignmentAifptr % A == 0. Eg a pointer to address 564 has alignment 4, because564 % 4 == 0. But it does not have alignment 8 because564 % 8 == 4.

This matters because load/store instructions on cpus usually have alignment requirements. Loading a 4 byte value requires a pointer with alignment 4, and loading an 8 byte value requires a pointer with alignment 8. The penalty for using a pointer that does not satisfy the alignment requirements ranges from a mild performance penalty (on x86) to crashing the program (on most arm).

When you allocate a value on the heap or stack, the allocator has to make sure that any pointers to that value will have the correct alignment. Eg if you allocate a 32-bit integer (4 bytes) then it must be allocated at an address with alignment 4, so that any loads/stores of that value are correctly aligned.

This is more complicated when the value you are allocating is a struct:

struct
Foo
{

 a
:
u8
,

 b
:
u64
,

}

How much space should we allocate for this struct, and what alignment does it require? That depends on how the compiler choose to layout the struct.

A common choice is to loop through the fields in order. For each field, we roundup the offset to the required alignment and then add the size of the field. So:

* We start with offset 0.
* aneeds alignment 1, so it can go at offset 0, and the next available offset is 1.
* bneeds alignment 8, so we round up the offset from 1 to 8, and the next available offset is 16.
* That's all the fields, so the total size of the struct is 16 bytes.
* The alignment of the struct is the maximum alignment of its fields - in this case 8.

So we need to allocate 16 bytes at an alignment of 8.

(A complication I'm ignoring here is that some compilers will reorder struct fields to reduce the size of the struct. It's not relevant to the main point below.)

There is one more complication. Here's another struct:

struct
Bar
{

 a
:
u64
,

 b
:
u8
,

}

You might expect this struct to end up with a size of 9 and alignment of 8, and if we were just allocating one struct that would be fine.

But what if we allocate an array of 2 structs, using 9 bytes for each? The firstBarstarts at offset 0, so itsafield has alignment 8. But the secondBarstarts at offset 9, right after the firstBarends, so itsafield starts at offset 9 from the base address, which does not have alignment 9.

To solve this problem, most languages round up the size of a struct to its alignment. So the size ofBarwould be rounded up from 9 to 16.

But this can be pretty wasteful when we're nesting structs!

struct
Quux
<T> {

 a
:
 T,

 b
:
u8
,

}

Quux<u64>has size 16 and alignment 8, which means thatQuux<Quux<u64>>has size 24 and alignment 8, andQuux<Quux<Quux<u64>>>has size 32 and alignment 8. Most of that is wasted space.

Swift has a slightly better layout algorithm. It doesn't round up the size of structs, but instead does the rounding up in a separate measurement called the 'stride'. Individual struct allocations use the size, and only arrays of structs care about the stride.

With swift-style layout,Quux<u64>would have size 9, stride 16, aligment 8.Quux<Quux<u64>>would have size 10, stride 16, aligment 8.Quux<Quux<Quux<u64>>>would have size 11, stride 16, aligment 8. That saves a lot of space!

So now we can talk about sum types, like this classic:

enum
Option
<T> {


Some
<T>
,


None
,

}

The wayOption<T>is laid out in most languages is like:

struct
Option
<T> {

 tag
:
 OptionTag,

 payload
:
 OptionPayload,

}

enum
OptionTag
{


Some
,


None
,

}

union OptionPayload<T> {


Some
<T>
,


None
,

}

Let's work out the size ofOption<u64>:

* The size and alignment of a union is just the maximum of the sizes and alignments of its possible values. SoOptionPayload<u64>has size 8, stride 8, alignment 8.
* OptionTagonly has two possible values, so it can fit in a single byte - size 1, stride 1, alignment 1.
* Option<u64>has to make sure the payload field is aligned, so it ends up with size 16, stride 16, alignment 1.

That means thatOption<Option<u64>>has size 24,Option<Option<Option<u64>>>has size 32 etc. Mostly wasted space!

But what if we just reverse the order of the fields, putting the tag at the end.

struct
Option
<T> {

 payload
:
 OptionPayload,

 tag
:
 OptionTag,

}

Now this gets laid out just likeQuux<T>above.Option<u64>has size 9,Option<Option<u64>>has size 10,Option<Option<Option<u64>>>has size 11 etc. No wasted space.

(The allocator itself might waste some space, but still probably not as much as the original layout. Eg I believe jemalloc with the default config will round all of the above to 16 bytes.)

The only language I know of that lays out sum types this way is swift, and I couldn't find any discussion or documentation of it, so I thought it was worth highlighting.

P.S. If you tried to follow along with examples above in rust you'll have found that while the size ofOption<u64>is 16, the size ofOption<Option<u64>>is also 16. This is because of a totally different optimization where the compiler notices that the tag inOption<u64>has 256 possible values but is only using 2 of them, so 2 of the unused values can be poached for the tag inOption<Option<u64>>. To match the size calculations above you'll have to explicitly ask for a stable layout:

#
[
repr
(u8)]

enum
MyOption
<T> {


Some
(T)
,


None
,

}

Swift has a similar optimization for unused values in pointers, but not for unused values in enum tags. SoOption<Option<Option<Option<Option<Option<Option<Option<Option<u64>>>>>>>>>is 17 bytes in swift but only 16 bytes in rust.
