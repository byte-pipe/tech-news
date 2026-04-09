---
title: I Write Type Safe Generic Data Structures in C ・ Daniel Hooper
url: https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/
site_name: hackernews_api
fetched_at: '2025-07-01T10:22:21.712461'
original_url: https://danielchasehooper.com/posts/typechecked-generic-c-data-structures/
author: todsacerdoti
date: '2025-07-01'
published_date: '2025-06-25T00:00:00+00:00'
description: I write type-safe generic data structures in C
tags:
- hackernews
- trending
---

Daniel Hooper
Home
 ・

Articles
 ・

Projects
 ・

X.com

Bluesky

Mastodon

RSS

# I Write Type Safe Generic Data Structures in C

June 25, 2025・7 minute read

I write type safe generic data structures in C using a technique that I haven’t seen elsewhere1. It uses unions to associate type information with a generic data structure, but we’ll get to that. My approach works for any type of data structure: maps, arrays, binary trees… but for this article I illustrate the ideas by implementing a basic linked list. Since many people aren’t aware you can do C genericsat all, I figured I’d start simple and build up to this:

typedef

struct

{


int

value
;

}

Foo
;



List
(
int
)

int_list

=

{
0
};

list_prepend
(
&
int_list
,

3
);

List
(
Foo
)

foo_list

=

{
0
};

list_prepend
(
&
foo_list
,

(
Foo
){

5

});

list_prepend
(
&
foo_list
,

(
Foo
){

3

});

// this won't compile, which is good!

// list_prepend(&foo_list, 7);

list_for
(
item
,

&
foo_list
)

{


// `item` is of type `Foo *`


printf
(
"%i
\n
"
,

item
->
value
);

}

### Generics level 0: Generic Headers

I hesitate to even mention this, because I do not like it2, but its worth comparing to the technique at the end of this article. It works like this: you write your data structure in a header, using macros for your types, and then#includethe header multiple times; once for each type the data structure will be used with.

Click to see the Code

list.h

#ifndef T

#error "T must be defined before including this header"

#endif

#define _CONCAT(a, b) a##b

#define CONCAT(a, b) _CONCAT(a, b)

#define NODE_TYPE CONCAT(T, ListNode)

#define PREPEND_FUNC CONCAT(T, _list_prepend)

typedef

struct

NODE_TYPE

NODE_TYPE
;

struct

NODE_TYPE

{


NODE_TYPE

*
next
;


T

data
;

};

void

PREPEND_FUNC
(
NODE_TYPE

**
head
,

T

data
)

{


NODE_TYPE

*
node

=

malloc
(
sizeof
(
*
node
));


node
->
data

=

data
;


node
->
next

=

*
head
;


*
head

=

node
;

}

#undef T

#undef _CONCAT

#undef CONCAT

#undef NODE_TYPE

#undef PREPEND_FUNC

main.c

typedef

struct

{


int

a
;

}

Foo
;

typedef

struct

{


char

*
str
;


double

num
;

}

Bar
;

#define T Foo

#include

"list.h"

#define T Bar

#include

"list.h"

FooListNode

*
foo_head

=

NULL
;

Foo_list_prepend
(
&
foo_head
,

(
Foo
){
1
})

BarListNode

*
bar_head

=

NULL
;

Bar_list_prepend
(
&
bar_head
,

(
Bar
){
"hello"
,

5.4
})

While itisgeneric and type safe, it has downsides:

* makes it hard to find where types and functions are defined (because they’re constructed by macros)
* code completion may not handle them well
* bloats your binary size and build times with copies of the same functions
* requires using type-prefixed functions:Foo_list_prepend() and int_list_prepend()vs justlist_prepend()

### Generics level 1:void *

Another way to make a data structure generic is to usevoid *. It’s not type safe but we’ll get to that.

typedef

struct

ListNode

ListNode
;

struct

ListNode

{


ListNode

*
next
;


void

*
data
;

};

void

list_prepend
(
ListNode

**
head
,

void

*
data
)

{


ListNode

*
node

=

malloc
(
sizeof
(
*
node
));


node
->
data

=

data
;


node
->
next

=

*
head
;


*
head

=

node
;

}

Note:mallocis used for familiarity, but I highly recommend Arenas instead. You canwatchorreadabout them.

HavingListNodeand itsdataas separate allocations isn’t ideal from a memory and performance perspective. It requires 2 allocations per node when one would do, thedatapointer uses memory unnecessarily, and you will likely get two cache misses per node when traversing the list: once getting the next node, and once getting its data. We can fix these issues with…

### Generics level 2: Inline storage

Instead of storing a pointer to the node’s data, we can use aFlexible Array Memberto store the data inside the node. To do so, we make a single allocation large enough for both the node and the type it stores:

typedef

struct

ListNode

ListNode
;

struct

ListNode

{


ListNode

*
next
;


uint64_t

data
[];


};

void

list_prepend
(
ListNode

**
head
,



void

*
data
,



size_t

data_size
)


{


ListNode

*
node

=

malloc
(
sizeof
(
*
node
)

+

data_size
);


memcpy
(
node
->
data
,

data
,

data_size
);


node
->
next

=

*
head
;


*
head

=

node
;

}

void

main
()

{


ListNode

*
foo_list

=

NULL
;


Foo

foo

=

{
5
};


list_prepend
(
&
foo_list
,

&
foo
,

sizeof
(
foo
));

}

Nownextand the actual contents ofdataare beside each other in memory, solving the issues of thevoid *approach. Unfortunately we now have to pass the size, but we’ll fix that in the next section

If you wanted to avoid thememcpy, and initialize the node’s memory directly, you could do so with alist_alloc_frontfunction:

void

*
list_alloc_front
(
ListNode

**
head
,

size_t

data_size
)

{


ListNode

*
node

=

malloc
(
sizeof
(
*
node
)

+

data_size
);


node
->
next

=

*
head
;


*
head

=

node
;


return

node
->
data
;

}

Foo

*
new_foo

=

list_alloc_front
(
&
foo_list
,

sizeof
(
*
new_foo
));

new_foo
->
value

=

5
;

### Generics level 3: Type Checking

The part you’ve all been waiting for: we want the compiler to error if we try to add the wrong type to a list. The way I found to do this is to use a union with apayloadmember that has a parameterized type:

#define List(type) union { \

 ListNode *head; \

 type *payload; \

}

List
(
Foo
)

foo_list

=

{
0
};

List
(
int
)

int_list

=

{
0
};

How does that help us? Well, we can now use__typeof__(foo_list.payload)to get the type the list contains, which we will use shortly. Some things to note:payloadis never used at runtime. It exists just for type information at compile time. Using a union makespayloadnot consume any memory.

Let’s use our newfound type info in alist_prependmacro. We’ll it to cast_list_prepend’s function type so that thevoid *parameter is the list’spayloadtype3(Dear C standards/Undefined Behavior police, please read the footnotes):

// Note: I added a leading underscore to the

// function name since only the macro should call it

void

_list_prepend
(
ListNode

**
head
,



void

*
data
,



size_t

data_size
)

{

...

}

#define list_prepend(list, item) \


/* cast function type */
 \

 ((void (*)(ListNode **, \

 __typeof__((list)->payload), \

 size_t))_list_prepend) \


/* call function */
 \

 (&((list)->head), item, sizeof(*(list)->payload))



void

main
()

{


ListNode

*
foo_list

=

NULL
;


Foo

foo

=

{
5
};


list_prepend
(
&
foo_list
,

&
foo
);

}

The macro also handles passing the item size for us and the compiler enforces that the list and the item are compatible types. This is error you see when adding the wrong type to the list:

error
:

incompatible

integer

to

pointer

conversion



passing

'
int
'

to

parameter

of

type



'
typeof

((
&
foo_list
)
->
payload
)
'

(
aka

'
Foo

*
'
)


|

list_prepend
(
&
foo_list
,

7
);


|

^

note
:

expanded

from

macro

'
list_prepend
'


|

(
&
((
list
)
->
head
),

item
,

sizeof
(
*
(
list
)
->
payload
))


|

^~~~

1

error

generated
.

## typeofon old compilers

__typeof__()was an optional extension until C23, which made it part of the C standard. While Clang and gcc have supported it for alongtime, some compilers haven’t (like msvc versions prior to 19.39). With some changes, you can make this technique work on those compilers:

#define List(type) struct { \

 ListNode *head; \

 type *payload; \

}

#define list_prepend(list, item) do {\

 (list)->payload = (item);
/* just for type checking */
\

 _list_prepend(&((list)->head), item, sizeof(*(list)->payload)) \

} while(0)

It’s possible to do type safe returns as well, by assigning throughpayload, but I’ll leave the details as an exercise for the reader.#

## Passing a Parameter

One annoying thing about C compilers released prior to late 20254is that they do not consider these two variables to have the same type:

List
(
Foo
)

a
;

List
(
Foo
)

b

=

a
;

// error

void

my_function
(
List
(
Foo
)

list
);

my_function
(
a
);

// error: incompatible type

Even though the variables have identical type definitions, the compiler still errors because they aretwo distinct definitions. Atypedefavoids the issue:

typedef

List
(
Foo
)

ListFoo
;

// this makes it all work

ListFoo

a
;

ListFoo

b

=

a
;

// ok

void

my_function
(
ListFoo

list
);

my_function
(
a
);

// ok

List
(
Foo
)

local_foo_list
;

// still works

### Conclusion

You can use this for any type of data structure, even ones with multiple associated types, like a hash map:

typedef

struct

{


...

}

MapInternal
;

#define Map(key_type, value_type) union { \

 MapInternal map; \

 key_type *key; \

 value_type *value; \

}

For more detail, like how thelist_formacro is implemented, see the codehere

Thanks toMartin Fouilleulfor the encouragement to finish this post, which I’ve been sitting on for months, and the feedback on early drafts.

1. stb_ds.his an example of a type-safe generic data structure, but the techniques it uses aren’t as general as what I present here - it only works because the array and map are implemented using a c array. The compiler catches some type errors upon assignment to that c array, not at the point that values are passed as parameters to generic functions. i.e.struct {int a; int b;} baz; STBDS_ADDRESSOF(baz, 5)compiles successfully, when you really want a type error.↩︎
2. If you want to write a generic function that requires type-specific code gen (like generatingadd_intandadd_doublefrom the same source), this option has more merit. You can get creative with c features in other ways to get type-specific behavior, like for hashing functions, for example.↩︎
3. While calling a typecast function pointer is technically undefined behavior, in practice this works as you would expect on modern platforms. If you’re still squeamish, use the techniques described inthis sectioninstead.↩︎
4. Structurally identical types will be considered the same type in GCC 15 and Clang later in 2025 thanks to arule change↩︎
❖
Get notified about my next article:

Join Newsletter
More articles by Daniel

Support my work
