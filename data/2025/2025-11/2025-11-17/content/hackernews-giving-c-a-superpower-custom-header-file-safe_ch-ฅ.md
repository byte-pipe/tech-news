---
title: 'Giving C a Superpower: custom header file (safe_c.h) | *ฅ^•ﻌ•^ฅ* ✨✨ HWisnu''s blog ✨✨ о ฅ^•ﻌ•^ฅ'
url: https://hwisnu.bearblog.dev/giving-c-a-superpower-custom-header-file-safe_ch/
site_name: hackernews
fetched_at: '2025-11-17T19:06:53.484064'
original_url: https://hwisnu.bearblog.dev/giving-c-a-superpower-custom-header-file-safe_ch/
author: mithcs
date: '2025-11-17'
description: 'Let''s be honest: most people have a love-hate relationship with C. We love its raw speed, its direct connection to the metal, and its elegant simplicity. ...'
---

# Giving C a Superpower: custom header file (safe_c.h)

09 Nov, 2025

The story of how I wrote a leak-free, thread-safe grep in C23 without shooting yourself in the foot, and how you can too!

# Introduction

Let's be honest: most people have a love-hate relationship with C. We love its raw speed, its direct connection to the metal, and its elegant simplicity. But we hate its footguns, its dragons, the untamed beasts. The segfaults that appear from nowhere, the memory leaks that slowly drain the life from our applications, and the endless goto cleanup; chains that make our code look like a plate of spaghetti pasta.

This is the classic C curse: power without guardrails...at least that's thefear mongering mantrabeing said again and again. But is that still relevant in today's world with all the tools available for C devs like static analyzer and dynamic sanitizers? I've written about thishereandhere.

What if, with the help of the modern tools and a custom header file (600 loc), you could tame those footguns beasts? What if you could keep C's power but wrap it in a suit of modern armor? That's what the custom header file safe_c.h is for. It's designed to give C somesafety and convenience features from C++ and Rust, and I'm using it to build a high-performance grep clone called cgrep as my test case.

By the end this article I hope it could provide the audience with the idea of C is super flexible and extensible, sort of"do whatever you want with it"kind of thing. And this is why C (and its close cousin: Zig) remain to be my favorite language to write programs in; it's the language of freedom!

# safe_c.h

Is a custom C header file that takes features mainly from C++ and Rust and implements them into our C code ~ [write C code, get C++ and Rust features!]

It starts by bridging the gap between old and new C. C23 gave us[[cleanup]]attributes, but in the real world, you need code that compiles on GCC 11 or Clang 18. safe_c.h detects your compiler and gives you the same RAII semantics everywhere. No more#ifdefsoup.

// The magic behind CLEANUP: zero overhead, maximum safety
#if defined(__STDC_VERSION__) && __STDC_VERSION__ >= 202311L
#define CLEANUP(func) [[cleanup(func)]]
#else
#define CLEANUP(func) __attribute__((cleanup(func)))
#endif

// Branch prediction that actually matters in hot paths
#ifdef __GNUC__
#define LIKELY(x) __builtin_expect(!!(x), 1)
#define UNLIKELY(x) __builtin_expect(!!(x), 0)
#else
#define LIKELY(x) (x)
#define UNLIKELY(x) (x)
#endif

Your cleanup code runs even if you return early, goto out, or panic. It'sfinally, but for C.

## The Memory Management Beast: Slain with Smart Pointers (C++ feature)

The oldest, fiercest and most feared by devs: manual memory management.

Before: the highway path to leaks.Forgetting a singlefree()is a disaster. In cgrep, parsing command-line options the old way is a breeding ground for CVEs and its bestiary. You have to remember to free the memory on every single exit path, difficult for the undisciplined.

// The Old Way (don't do this)

char
*

include_pattern

=

NULL
;

if

(
optarg
)

{


include_pattern

=

strdup
(
optarg
);

}

// ...200 lines later...

if

(
some_error
)

{


if

(
include_pattern
)

free
(
include_pattern
);

// Did I free it? Did I??


return

1
;

}

// And remember to free it at *every* return path...

After: memory thatautomaticallycleans itself up.UniquePtr is a "smart pointer" that owns a resource. When the UniquePtr variable goes out of scope, its resource is automatically freed. It's impossible to forget.

Here's the machinery insidesafe_c.h:

// The UniquePtr machinery: a struct + automatic cleanup
typedef struct {
 void* ptr;
 void (*deleter)(void*);
} UniquePtr;

#define AUTO_UNIQUE_PTR(name, ptr, deleter) \
 UniquePtr name CLEANUP(unique_ptr_cleanup) = UNIQUE_PTR_INIT(ptr, deleter)

static inline void unique_ptr_cleanup(UniquePtr* uptr) {
 if (uptr && uptr->ptr && uptr->deleter) {
 uptr->deleter(uptr->ptr);
 uptr->ptr = NULL;
 }
}

And here's how cgrep uses it. The cleanup is automatic, even if errors happen:

// In cgrep, we use this for command-line arguments

AUTO_UNIQUE_PTR
(
include_pattern_ptr
,

NULL
,

options_string_deleter
);

// When we get a new pattern, the old one is automatically freed!

unique_ptr_delete
(
&
include_pattern_ptr
);

include_pattern_ptr
.
ptr

=

strdup
(
optarg
);

// No leaks, even if an error happens later!

Sharing Safely with SharedPtr

Before: manual, bug-prone reference counting.You'd have to implement reference counting by hand, creating a complex and fragile system where a single mistake leads to a leak or a use-after-free bug.

// The old way of manual reference counting

typedef

struct

{


MatchStore
*

store
;


int

ref_count
;


pthread_mutex_t

mutex
;

}

SharedStore
;

void

release_store
(
SharedStore
*

s
)

{


pthread_mutex_lock
(
&
s
->
mutex
);


s
->
ref_count
--
;


bool

is_last

=

(
s
->
ref_count

==

0
);


pthread_mutex_unlock
(
&
s
->
mutex
);


if

(
is_last
)

{


match_store_deleter
(
s
->
store
);


free
(
s
);


}

}

After: automated reference counting.SharedPtr automates this entire process. The last thread to finish using the object automatically triggers its destruction.
The machinery:

// The SharedPtr machinery: reference counting without the boilerplate
typedef struct {
 void* ptr;
 void (*deleter)(void*);
 size_t* ref_count;
} SharedPtr;

#define AUTO_SHARED_PTR(name) \
 SharedPtr name CLEANUP(shared_ptr_cleanup) = {.ptr = NULL, .deleter = NULL, .ref_count = NULL}

static inline void shared_ptr_cleanup(SharedPtr* sptr) {
 shared_ptr_delete(sptr); // Decrement and free if last reference
}

The usage is clean and safe. No more manual counting.

// In our thread worker context, multiple threads access the same results store

typedef

struct

{


// ...


SharedPtr

store
;

// No more worrying about who frees this!


SharedPtr

file_counts
;


// ...

}

FileWorkerContext
;

// In main(), we create it once and share it safely

// SharedPtr: Reference-counted stores for thread-safe sharing

SharedPtr

store_shared

=

{
0
};

shared_ptr_init
(
&
store_shared
,

store_ptr
.
ptr
,

match_store_deleter
);

// Pass to threads: ctx->store = shared_ptr_copy(&store_shared);

// ref-count increments automatically; last thread out frees it.

## The Buffer Overflow Beast: Contained with Vectors and Views (C++ feature)

Dynamically growing arrays in C is a horror show.

Before: the realloc dance routine.You have to manually track capacity and size, and every realloc risks fragmenting memory or failing, requiring careful error handling for every single element you add.

// The old way: manual realloc is inefficient and complex

MatchEntry
**

matches

=

NULL
;

size_t

matches_count

=

0
;

size_t

matches_capacity

=

0
;

for

(
/*...each match...*/
)

{


if

(
matches_count

>=

matches_capacity
)

{


matches_capacity

=

(
matches_capacity

==

0
)

?

8

:

matches_capacity

*

2
;


MatchEntry
**

new_matches

=

realloc
(
matches
,

matches_capacity

*

sizeof
(
MatchEntry
*
));


if

(
!
new_matches
)

{


free
(
matches
);

// Don't leak!


/* handle error */


}


matches

=

new_matches
;


}


matches
[
matches_count
++
]

=

current_match
;

}

After: a type-safe, auto-growing vector.safe_c.h generates an entire type-safe vector for you. It handles allocation, growth, and cleanup automatically.
The magic that generates the vector:

// The magic that generates a complete vector type from a single line
#define DEFINE_VECTOR_TYPE(name, type) \
 typedef struct { \
 Vector base; \
 type* data; \
 } name##Vector; \
 \
 static inline bool name##_vector_push_back(name##Vector* vec, type value) { \
 bool result = vector_push_back(&vec->base, &value); \
 vec->data = (type*)vec->base.data; /* Sync pointer after potential realloc */ \
 return result; \
 } \
 \
 static inline bool name##_vector_reserve(name##Vector* vec, size_t new_capacity) { \
 bool result = vector_reserve(&vec->base, new_capacity); \
 vec->data = (type*)vec->base.data; /* Sync pointer after potential realloc */ \
 return result; \
 } \

 /* more helper functions not outlined here */

// And the underlying generic Vector implementation
typedef struct {
 size_t size;
 size_t capacity;
 void* data;
 size_t element_size;
} Vector;

Using it in cgrep is simple and safe. The vector cleans itself up when it goes out of scope.

// Type-safe vector for collecting matches

DEFINE_VECTOR_TYPE
(
MatchEntryPtr
,

MatchEntry
*
)

AUTO_TYPED_VECTOR
(
MatchEntryPtr
,

all_matches_vec
);

MatchEntryPtr_vector_reserve
(
&
all_matches_vec
,

store
->
total_matches
);

// Pushing elements is safe and simple

for

(
MatchEntry
*

entry

=

store
->
buckets
[
i
];

entry
;

entry

=

entry
->
next
)

{


MatchEntryPtr_vector_push_back
(
&
all_matches_vec
,

entry
);

}

## Views: Look, Don't Touch (or malloc) - C++ feature

Before: needless allocations.To handle a substring or a slice of an array, you'd often malloc a new buffer and copy the data into it, which is incredibly slow in a tight loop.

// The old way: allocating a new string just to get a substring

const

char
*

line

=

"this is a long line of text"
;

char
*

pattern

=

"long line"
;

// To pass just the pattern to a function, you might do this:

char
*

sub

=

malloc
(
strlen
(
pattern
)

+

1
);

strncpy
(
sub
,

pattern
,

strlen
(
pattern
)

+

1
);

// ... use sub ...

free
(
sub
);

// And hope you remember this free call

After: zero-cost, non-owning views.A StringView or a Span is just a pointer and a length. It's a non-owning reference that lets you work with slices of data without any allocation.
The definitions are pure and simple:

// The StringView and Span definitions: pure, simple, zero-cost

typedef

struct

{


const

char
*

data
;


size_t

size
;

}

StringView
;

typedef

struct

{


void
*

data
;


size_t

size
;


size_t

element_size
;

}

Span
;

In cgrep, the search pattern becomes a StringView, avoiding allocation entirely.

// Our options struct holds a StringView, not a char*

typedef

struct

{


StringView

pattern
;

// Clean, simple, and safe


// ...

}

GrepOptions
;

// Initializing it is a piece of cake

options
.
pattern

=

string_view_init
(
argv
[
optind
]);

For safe array access, Span provides a bounds-checked window into existing data.

// safe_c.h
#define DEFINE_SPAN_TYPE(name, type) \
 typedef struct { \
 type* data; \
 size_t size; \
 } name##Span; \
 \
 static inline name##Span name##_span_init(type* data, size_t size) { \
 return (name##Span){.data = data, .size = size}; \
 } \
 \

 /* other helper functions not outlined here */

// Span: Type-safe array slices for chunk processing

DEFINE_SPAN_TYPE
(
LineBuffer
,

char
)

LineBufferSpan

input_span

=

LineBuffer_span_init
((
char
*
)
start
,

len
);

for

(
size_t

i

=

0
;

i

<

LineBuffer_span_size
(
&
input_span
);

i
++
)

{


char
*

line

=

LineBuffer_span_at
(
&
input_span
,

i
);

// asserts i < span.size

}

## The Error-HandlinggotoBeast: Replaced with Results (Rust feature) and RAII (C++ feature)

C's error handling is notoriously messy.

Before: goto cleanup spaghetti carbonara.Functions return special values like -1 or NULL, and you have to check errno. This leads to deeply nested if statements and a single goto cleanup; label that has to handle every possible failure case.

// The old way: goto cleanup

int

do_something
(
const

char
*

path
)

{


int

fd

=

open
(
path
,

O_RDONLY
);


if

(
fd

<

0
)

{


return

-1
;

// Error


}


void
*

mem

=

malloc
(
1024
);


if

(
!
mem
)

{


close
(
fd
);

// Manual cleanup


return

-1
;


}




// ... do more work ...


free
(
mem
);


close
(
fd
);


return

0
;

// Success

}

After: explicit, type-safe result.Inspired by Rust, Resultforces you to handle errors explicitly by returning a type that is either a success value or an error value.
The Result machinery:

// The Result type machinery: tagged unions for success/failure
typedef enum { RESULT_OK, RESULT_ERROR } ResultStatus;

#define DEFINE_RESULT_TYPE(name, value_type, error_type) \
 typedef struct { \
 ResultStatus status; \
 union { \
 value_type value; \
 error_type error; \
 }; \
 } Result##name;

Handling errors becomes easy. You can't accidentally use an error as a valid value.

// Define a Result for file operations

DEFINE_RESULT_TYPE
(
FileOp
,

i32
,

const

char
*
)

// Our function now returns a clear Result

static

ResultFileOp

submit_stat_request_safe
(...)

{


// ...


if

(
!
sqe
)

{


return

RESULT_ERROR
(
FileOp
,

"Could not get SQE for stat"
);


}


return

RESULT_OK
(
FileOp
,

0
);

}

// And handling it is clean

ResultFileOp

result

=

submit_stat_request_safe
(
path
,

&
ring
,

&
pending_ops
);

if

(
!
RESULT_IS_OK
(
result
))

{


fprintf
(
stderr
,

"Error: %s
\n
"
,

RESULT_UNWRAP_ERROR
(
result
));

}

This is powered by RAII. TheCLEANUPattribute ensures resources are freed no matter how a function exits.

#define AUTO_MEMORY(name, size) \

 void* name CLEANUP(memory_cleanup) = malloc(size)

// DIR pointers are automatically closed, even on an early return.

DIR
*

dir

CLEANUP
(
dir_cleanup
)

=

opendir
(
req
->
path
);

if

(
!
dir
)

{


return

RESULT_ERROR
(
FileOp
,

"Failed to open dir"
);

// dir_cleanup is NOT called

}

if

(
some_condition
)

{


return

RESULT_OK
(
FileOp
,

0
);

// closedir() is called automatically HERE!

}

## The Assumption Beast: Challenged with Contracts and Safe Strings

Before:assert()and pray.A standardassert(ptr != NULL)is good, but when it fails, the message is generic. You know the condition failed, but not the context or why it was important.

After: self-documenting contracts.requires()andensures()make function contracts explicit. The failure messages tell you exactly what went wrong.
The contract macros:

#define requires(cond) assert_msg(cond, "Precondition failed")
#define ensures(cond) assert_msg(cond, "Postcondition failed")

#define assert_msg(cond, msg) /* ... full implementation ... */

This turns assertions into executable documentation:

// Preconditions that document and enforce contracts

static

inline

bool

arena_create
(
Arena
*

arena
,

size_t

size
)

{


requires
(
arena

!=

NULL
);

// Precondition: arena must not be null


requires
(
size

>

0
);

// Precondition: size must be positive




// ... implementation ...




ensures
(
arena
->
buffer

!=

NULL
);

// Postcondition: buffer is allocated


ensures
(
arena
->
size

==

size
);

// Postcondition: size is set correctly




return

true
;

}

### strcpy()is a Security Vulnerability

Before: buffer overflows.strcpy has no bounds checking. It's the source of countless security holes.strncpyis little better, as it might not null-terminate the destination string.

// The old, dangerous way

char

dest
[
20
];

const

char
*

src

=

"This is a very long string that will overflow the buffer"
;

strcpy
(
dest
,

src
);

// Undefined behavior! Stack corruption!

After: safe, bounds-checked operations.safe_c.h provides alternatives that check bounds and return a success/failure status. No surprises.
The safe implementation:

// The safe string operations: bounds checking that can't be ignored

static

inline

bool

safe_strcpy
(
char
*

dest
,

size_t

dest_size
,

const

char
*

src
)

{


if

(
!
dest

||

dest_size

==

0

||

!
src
)

return

false
;


size_t

src_len

=

strlen
(
src
);


if

(
src_len

>=

dest_size
)

return

false
;


memcpy
(
dest
,

src
,

src_len

+

1
);


return

true
;

}

In cgrep, this prevents path buffer overflows cleanly:

// Returns bool, not silent truncation

if

(
!
safe_strcpy
(
req
->
path
,

PATH_MAX
,

path
))

{


free
(
req
);


return

RESULT_ERROR
(
FileOp
,

"Path is too long"
);

}

## Concurrency: Mutexes That Unlock Themselves (Rust feature)

Before: leaked locks and deadlocks.Forgetting to unlock a mutex, especially on an error path, is a catastrophic bug that causes your program to deadlock.

// The Buggy Way

pthread_mutex_lock
(
&
mutex
);

if

(
some_error
)

{


return
;

// Oops, mutex is still locked! Program will deadlock.

}

pthread_mutex_unlock
(
&
mutex
);

After: RAII-based locks.Using the same CLEANUP attribute, we can ensure a mutex is always unlocked when the scope is exited. This bug becomes impossible to write.

// With a cleanup function, unlocking is automatic.

void

mutex_unlock_cleanup
(
pthread_mutex_t
**

lock
)

{


if

(
lock

&&

*
lock
)

pthread_mutex_unlock
(
*
lock
);

}

// RAII lock guard via cleanup attribute

pthread_mutex_t

my_lock
;

pthread_mutex_t
*

lock_ptr

CLEANUP
(
mutex_unlock_cleanup
)

=

&
my_lock
;

pthread_mutex_lock
(
lock_ptr
);

if

(
some_error
)

{


return
;

// Mutex is automatically unlocked here!

}

Simple wrappers also clean up the boilerplate of managing threads:

// The concurrency macros: spawn and join without boilerplate
#define SPAWN_THREAD(name, func, arg) \
 thrd_t name; \
 thrd_create(&name, (func), (arg))

#define JOIN_THREAD(name) \
 thrd_join(name, NULL)

And in cgrep:

// Thread pool spawn without boilerplate
SPAWN_THREAD(workers[i], file_processing_worker, &contexts[i]);
JOIN_THREAD(workers[i]); // No manual pthread_join() error handling

## Performance: Safety at -O2, Not -O0

Safety doesn't mean slow. The UNLIKELY() macro tells the compiler which branches are cold, adding zero overhead in hot paths.

#ifdef __GNUC__
#define LIKELY(x) __builtin_expect(!!(x), 1)
#define UNLIKELY(x) __builtin_expect(!!(x), 0)
#else
#define LIKELY(x) (x)
#define UNLIKELY(x) (x)
#endif

The real win is in the fast paths:

// In hot allocation path: branch prediction

if

(
UNLIKELY
(
store
->
local_buffer_sizes
[
thread_id
]

>=

LOCAL_BUFFER_CAPACITY
))

{


match_store_flush_buffer
(
store
,

thread_id
);

// Rarely taken

}

// In match checking: likely path first

if

(
!
options
->
case_insensitive

&&

options
->
fixed_string
)

{


// Most common case: fast path with no branches


const

char
*

result

=

strstr
(
line
,

options
->
pattern
.
data
);


return

result

!=

NULL
;

}

The above is similar to what a PGO (Profile Guided Optimization) would have.

## The Final Word: C That Doesn't Blow Your Own Foot!

This is what main() looks like when you stop fighting the language:

int

main
(
int

argc
,

char
*

argv
[])

{


initialize_simd
();


output_buffer_init
();

// Auto-cleanup on exit




GrepOptions

options

=

{
0
};


AUTO_UNIQUE_PTR
(
include_pattern_ptr
,

NULL
,

options_string_deleter
);




// ... parse args with getopt_long ...




AUTO_UNIQUE_PTR
(
store_ptr
,

NULL
,

match_store_deleter
);


SharedPtr

store_shared

=

{
0
};


if

(
need_match_store
)

{


store_ptr
.
ptr

=

malloc
(
sizeof
(
ConcurrentMatchStore
));


if

(
!
store_ptr
.
ptr

||

!
match_store_create
(
store_ptr
.
ptr
,

hash_capacity
,

1000
))

{


return

1
;

// All allocations cleaned up automatically


}


shared_ptr_init
(
&
store_shared
,

store_ptr
.
ptr
,

match_store_deleter
);


}




// Process files with thread pool...



cleanup
:

// Single cleanup label needed -- RAII handles the rest


output_buffer_destroy
();

// Flushes and destroys


return

0
;

}

# Conclusion

In the end, cgrep is 2,300 lines of C. Without safe_c.h, it would have required over 50 manual free() calls ~ a recipe for leaks and segfaults. With the custom header file, it's 2,300 lines that compile to the same assembly, run just as fast, and are fundamentally safer.

This proves that the best abstraction is the one you don't pay for and can't forget to use. It enables a clear and powerful development pattern: validate inputs at the boundary, then unleash C's raw speed on the core logic. You get all the power of C without the infamous self-inflicted footgun wounds.

C simplicity makes writing programs with it becomes fun, however there are ways to make it bothfun and safe..just like using condoms, you know?

This post has gotten too long for comfort, but I have one final food for thought for you the readers: after all these guard rails, what do you think of cgrep's performance? Check the screenshots below:

* grep bench on recursive directories
* grep bench on single large fileNOTE: make sure you check the memory usage comparison between cgrep and ripgrep

In the next article, I will discuss how I built cgrep, the design I chose for it, why and how cgrep managed to be a couple of times faster than ripgrep (more than 2x faster in the recursive directory bench) while being super efficient with resource usage (20x smaller memory footprint in the single large file bench).

It's gonna be a lot of fun! Cheers!

### Comments section here

If you enjoyed this post, click the little up arrow chevron on the bottom left of the page to help it rank in Bear's Discovery feed and if you got any questions or anything, please use the comments section.
