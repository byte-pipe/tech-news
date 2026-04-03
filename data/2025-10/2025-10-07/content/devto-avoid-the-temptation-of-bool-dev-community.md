---
title: Avoid the Temptation of bool - DEV Community
url: https://dev.to/pauljlucas/avoid-the-temptation-of-bool-5g31
site_name: devto
fetched_at: '2025-10-07T11:09:20.425297'
original_url: https://dev.to/pauljlucas/avoid-the-temptation-of-bool-5g31
author: Paul J. Lucas
date: '2025-10-04'
description: Avoid the temptation of using bool for function parameters. Tagged with c, cpp.
tags: '#c, #cpp'
---

## Introduction

The Boolean type (spelledboolin C, C++, Go, and Rust, among others; andbooleanin Java) is fundamental to programming since so many things are either true or false. Of course you can useboolfor function parameters, and it’s tempting to do so — but you probably shouldn’t. Consider a function call like:

void

*
buf

=

alloc_buf
(

4096
,

true

);

// What does "true" mean?

Enter fullscreen mode

Exit fullscreen mode

Seeing a literaltrueorfalseas part of a functioncalltells you nothing about what it means. Does it mean the buffer is maximally aligned? Zeroed? Prints an error message if the allocation fails? You have no idea. You have to find and read the either function’s declaration or documentation to know what it means:

void
*

alloc_buf
(

size_t

size
,

bool

zero_buf

);

Enter fullscreen mode

Exit fullscreen mode

It’s for this reason I personally try to avoid usingboolfor parameters in public APIs. Code is read far more than it’s written, so clarity matters. But what can you do instead of usingbool? That’s what this article is about.

This article’s examples are specifically in C but apply equally well to C-like languages or any language that has a Boolean type.

## Alternatives tobool

There are a few alternatives depending on circumstances and taste.

### Use Two Functions

Instead of a single function, have two:

void
*

alloc_raw
(

size_t

size

);

void
*

alloc_zero
(

size_t

size

);

Enter fullscreen mode

Exit fullscreen mode

Note that this would be in thepublicAPI. Internally, you can still implement a single function that takes aboolif you want and have the public functions just call the internal function.

### Use an Enumeration

Instead of usingbool, define anenumeration:

enum

alloc_opts

{


ALLOC_RAW
,


ALLOC_ZEROED

};

typedef

enum

alloc_opts

alloc_opts
;

void
*

alloc_buf
(

size_t

size
,

alloc_opts

opt

);

Enter fullscreen mode

Exit fullscreen mode

Of all the languages mentioned, only Go doesn’t directly support enumerations — but you canfake it.

You might think creating an enumeration to replace aboolis overkill, but now look how the function is called:

void

*
buf

=

alloc_buf
(

4096
,

ALLOC_ZERO

);

Enter fullscreen mode

Exit fullscreen mode

It’s barely longer, butmuchclearer. Investing more in functions’ APIs has a many-fold return on said investment in terms of clarity.

Another benefit of using an enumeration is that it allows for additional options to be added easily by converting the enumeration to use bit flags:

enum

alloc_opts

{


ALLOC_RAW

=

0
,


ALLOC_ALIGNED

=

1

<<

0
,


ALLOC_ZEROED

=

1

<<

1
,

};

Enter fullscreen mode

Exit fullscreen mode

Then you can do things like:

void

*
buf

=

alloc_buf
(

4096
,

ALLOC_ALIGNED

|

ALLOC_ZERO

);

Enter fullscreen mode

Exit fullscreen mode

Note that code already using the function doesn’t have to change (unless you want to use the new options); it just has to be recompiled.

### Use Comments (as a Last Resort)

If your code either calls a 3rd-party function that takes aboolparameter or you simply can’t change your function’s API for whatever reason, at least use inline comments that repeat the name of the parameters:

void

*
buf

=

alloc_buf
(

4096
,

/*zero_buf=*/
true

);

Enter fullscreen mode

Exit fullscreen mode

Programmers reading your code (including yourself in several months’ time) will thank you.

## Conclusion

Sinceboolis so easy, it’s very tempting to use it for function parameters, especially when retrofitting an existing function just to tweak it. Avoid the temptation: either add a second function or use an enumeration.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
