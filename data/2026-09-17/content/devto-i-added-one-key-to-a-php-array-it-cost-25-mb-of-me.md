---
title: I Added One Key to a PHP Array. It Cost 25 MB of Memory - DEV Community
url: https://dev.to/nazar-boyko/i-added-one-key-to-a-php-array-it-cost-25-mb-of-memory-4b80
site_name: devto
content_file: devto-i-added-one-key-to-a-php-array-it-cost-25-mb-of-me
fetched_at: '2026-09-17T15:26:58.578404'
original_url: https://dev.to/nazar-boyko/i-added-one-key-to-a-php-array-it-cost-25-mb-of-memory-4b80
author: Nazar Boyko
date: '2026-09-14'
description: I was recently refactoring some legacy PHP code and noticed that the same data array was being used... Tagged with php, performance, webdev, programming.
tags: '#php, #performance, #webdev, #programming'
---

Reveals PHP hash table internals on version 8.4

I was recently refactoring some legacy PHP code and noticed that the same data array was being used in completely different ways! Radically different! After some analysis, I came to the conclusion that a PHP array can be a very efficient data structure as long as it remains a packed list, but as soon as it turns into a hash table, memory consumption skyrockets, and for large datasets, associative arrays often consume nearly twice as much memory as regular typed objects.

In this article, I want to explain why this happens and what conclusions I've reached, because as I was told in the PHP community, only God knows where the memory goes 😀

After doing some analysis, I found that a PHP array holding one million integers takes 16.8 MB on PHP 8.4. If you add a single-character key, it takes up 41.9 MB. That means a single key takes up 25 MB. 🤷‍♂️

I'd read that PHP arrays are hash tables so many times I'd stopped hearing it, it sits in the same drawer as "floats are inexact". So I ended up building arrays of a million elements and watchingmemory_get_usage()while I did things to them. I started with the case PHP optimizes, then the ways that optimization quietly goes away, then a million rows from a query with each row an associative array, because every codebase I've worked on holds its rows that way. The rows are where the real cost is and the fix turns out to be smaller than the problem.

Everything below ran on PHP 8.4.21 in the officialphp:8.4-cliDocker image on 64-bit Linux withmemory_limitset to-1so nothing died halfway and where the version matters I ran the same script on 8.1.34 too, because 8.2 changed one of these numbers a lot and I wanted the before as well as the after. The figures are deltas ofmemory_get_usage(). The PHP manual says those are rounded up to the allocator's granularity, so treat the last couple of digits as noise.

## Sixteen bytes per integer, until you add one key

Here's the sample code I used; this code for measuring memory usage isn't complicated at all. You can try replicating it too! The measuring code is nothing clever. Build the array, subtract two calls tomemory_get_usage(), divide by the count.

bench.php

<?php

declare
(
strict_types
=
1
);

const
 
N
 
=
 
1_000_000
;

function
 
report
(
string
 
$label
,
 
int
 
$bytes
,
 
int
 
$n
):
 
void

{

 
printf
(
"%-42s %14s bytes %6.2f bytes/elem
\n
"
,
 
$label
,
 
number_format
(
$bytes
),
 
$bytes
 
/
 
$n
);

}

$before
 
=
 
memory_get_usage
();

$a
 
=
 
[];

for
 
(
$i
 
=
 
0
;
 
$i
 
<
 
N
;
 
$i
++
)
 
{

 
$a
[]
 
=
 
$i
;

}

report
(
'packed list, keys 0..N-1 in order'
,
 
memory_get_usage
()
 
-
 
$before
,
 
N
);

$before
 
=
 
memory_get_usage
();

$r
 
=
 
[];

for
 
(
$i
 
=
 
N
 
-
 
1
;
 
$i
 
>=
 
0
;
 
$i
--
)
 
{

 
$r
[
$i
]
 
=
 
$i
;

}

report
(
'same keys, filled in reverse order'
,
 
memory_get_usage
()
 
-
 
$before
,
 
N
);

Enter fullscreen mode

Exit fullscreen mode

The two loops use the same keys and the same values. One counts up and the other counts down.

PHP 8.4.21 (Linux)
packed list, keys 0..N-1 in order 16,781,392 bytes 16.78 bytes/elem
range(0, N-1) 16,781,392 bytes 16.78 bytes/elem
same keys, filled in reverse order 41,943,120 bytes 41.94 bytes/elem
SplFixedArray of N ints 16,003,192 bytes 16.00 bytes/elem

Enter fullscreen mode

Exit fullscreen mode

Two and a half times the memory for the same million integers, because I filled it backwards.

That's the whole article in one line, honestly. The rest is why. 😃

The first array is what the engine callspacked. The keys are 0 and 1 and 2 and so on in order, so PHP doesn't store them at all, each slot is one 16-byte zval and that's it. The reverse-filled array has the same keys but they arrived out of order, so it's a real hash table with keys and hashes and an index at about 40 bytes per slot.

Then the part that made me sit up. Take the packed million and give it one string key.

$a
[
'x'
]
 
=
 
0
;

Enter fullscreen mode

Exit fullscreen mode

after adding one string key to packed list +25,161,728 bytes
after adding key -1 to packed list +25,161,728 bytes
after unset of that string key +25,161,728 bytes (nothing came back)

Enter fullscreen mode

Exit fullscreen mode

One key. Twenty-five megabytes. And as it turns out, removing the key does not undo this action, because nothing on the unset path converts a hash table back into a packed one (sort()does, as it happens, andarray_values()builds a fresh packed array, but plainunsetonly frees the value and leaves the layout alone). A negative key does the same thing as a string key, and I'm not sure why that surprised me since as an unsigned value it's enormous, but it did.

## A packed array is a flat zval array; a hash array is buckets plus an index

Every PHP array is azend_arrayand the C code calls itHashTabletoo. It's 56 bytes on 64-bit. Most of it is bookkeeping (a refcount header and flags and the table size and the element count and the next free integer key and a destructor pointer) and then there's one pointer to the data, and that pointer is a union, and the union is the whole story:

Zend/zend_types.h (php-src, PHP-8.4 branch)

union
 
{

 
uint32_t
 
*
arHash
;

 
Bucket
 
*
arData
;

 
zval
 
*
arPacked
;

};

Enter fullscreen mode

Exit fullscreen mode

In hash mode the data block has two parts. In front sits the hash index, an array ofuint32_tslots with twice as many slots as there are buckets (the mask is-(nTableSize + nTableSize)) so that's 8 bytes of index per bucket and behind it sit the buckets at 32 bytes each:

Zend/zend_types.h (php-src, PHP-8.4 branch, comments mine)

typedef
 
struct
 
_Bucket
 
{

 
zval
 
val
;
 
/* 16 bytes: the value */

 
zend_ulong
 
h
;
 
/* 8 bytes: the integer key, or the string key's hash */

 
zend_string
 
*
key
;
 
/* 8 bytes: NULL for integer keys */

}
 
Bucket
;

Enter fullscreen mode

Exit fullscreen mode

A lookup hashes the key and masks it into the index and reads a bucket number there and follows anextchain stored inside the zval if two keys collided. Iteration never touches the index, it walks the buckets front to back, and since buckets are appended in insertion order that's howforeachgives you insertion order for free.

So a hash slot costs 32 + 8 = 40 bytes. A million elements need a table of 1,048,576 slots (more on that in a second), and 40 times that is 80 bytes short of what the measurement says. That's the 56-byte struct plus 24 bytes the allocator keeps to track a block that big.

In packed mode there's no index (two placeholder slots and 8 bytes total) and the data iszval *arPacked, a bare C array of 16-byte values where the position is the key. Sixteen times the same table size lands about 4 KB under the measured 16.8 MB. It's the same accounting with a smaller slot.

Here's the thing I hadn't tracked: packed arrays only became this cheap in PHP 8.2. Before that they used the same 32-byte buckets as hash arrays and simply skipped the index, withhrepeating the slot's position andkeyalways NULL in every slot. That lasted until Dmitry Stogov'sPR #7491("Use more compact representation for packed arrays") was merged in November 2021 and shipped in 8.2.0 in December 2022. It's an internals change, so the 8.2 UPGRADING notes don't mention it at all (I went looking). Here's the 8.1 run for the before:

PHP 8.1.34 (Linux)
packed list, keys 0..N-1 in order 33,558,608 bytes 33.56 bytes/elem
same keys, filled in reverse order 41,943,120 bytes 41.94 bytes/elem

Enter fullscreen mode

Exit fullscreen mode

Half the slot memory of every list in your application, from one release. Tideways company measured the same thing when 8.2 came out, on a 100,000-element list, and got 4.3 MB down to 2.3 MB. If you're still on 8.1 for some reason, this is a decent argument on its own.

The other rule that's worth knowing is growth. Table sizes are powers of two with a minimum of 8, and a full table doubles (nSize = ht->nTableSize + ht->nTableSizeinzend_hash_do_resize) so one million elements live in a table of 1,048,576 slots. Which means:

packed list of 1,048,576 ints 16,781,448 bytes 16.00 bytes/elem
packed list of 1,048,577 ints 33,558,664 bytes 32.00 bytes/elem

Enter fullscreen mode

Exit fullscreen mode

One more element and twice the memory. And it doesn't go the other way. I unset 999,000 of the million andmemory_get_usage()moved by exactly 0 bytes. The values were integers so there was nothing to free, and the table itself doesn't shrink. An array remembers the biggest it has ever been. In a queue worker that's one of the reasons memory only ever climbs, and long-running PHP processes goes through the rest of them.

## The rules for staying packed are stricter than array_is_list()

The conversion logic lives in_zend_hash_index_add_or_update_iinZend/zend_hash.c. For an array that's currently packed, an integer key goes through this sequence.

* Key below the high-water mark, slot filled.Overwrite in place. Still packed.
* Key below the high-water mark, slot is a hole.Convert to hash. The comment in the source reads/* we have to keep the order :( */, and that's the real reason for all of this. A PHP array promises to iterate in insertion order, a packed array can only express "ascending", so any insert that would break ascending order forces the full structure.
* Key inside the current table size.Append, fill any gap with undefined slots, stay packed. Writing$a[0] = 'a'; $a[5] = 'b';gives a packed array with four holes in it.
* Key past the table but less than twice its size, table more than half full.Grow, stay packed.
* Anything else, every string key, and any negative key(as an unsigned value it's enormous). Convert to hash.

Here are two arrays with the same two elements and a different order of arrival.

[0 => 'b', 1 => 'a'] built at runtime 216 bytes
[1 => 'a', 0 => 'b'] built at runtime 376 bytes

Enter fullscreen mode

Exit fullscreen mode

The one that costs 376 bytes is a hash table with eight buckets and sixteen index slots. For two values. The 216-byte one is eight zvals and nothing else. Both are the minimum table size.

The gotcha that actually bites isarray_filter(). It preserves keys and everyone knows that because of the JSON symptom where a filtered list encodes as an object. The memory symptom isn't as loud. Filter a packed million down to the even numbers and the result gets built key by key (0 then 2 then 4 then 6) until key 8 arrives and doesn't fit in the initial table of 8 and also fails the "more than half full" test, at which point the new array converts to hash on its fifth element and stays there for the rest of its life.

array_filter keeping every other element 20,971,600 bytes 41.94 bytes/elem
array_values() of that result 8,392,784 bytes 16.79 bytes/elem
array_is_list(filtered) = false

Enter fullscreen mode

Exit fullscreen mode

Half the elements and more memory than the original packed million.array_values()fixes it at the cost of one copy, and I think that's always worth paying if the result is going to live for a while.

Andarray_is_list()checks keys and not layout. It arrived in 8.1 and I'd assumed it was the test for this. It answers "are the keys 0 to n-1 in order" and a hash table can satisfy that:

[1 => 'a', 0 => 'b'] 376 bytes array_is_list = false
after unset($b[1]) 376 bytes array_is_list = true

Enter fullscreen mode

Exit fullscreen mode

The same 376 bytes and the same hash layout, and now the function says it's a list. Before PHP 8.4 no userland call showed you the layout, and the only honest instrument wasmemory_get_usage(). Since 8.4debug_zval_dump()printspackednext to a packed array, and for this one it prints nothing.

## A copy costs nothing until the first write

The refcount lives in thezend_arrayheader, not in the variable.$b = $abumps it and points both variables at the same table, and passing an array into a function does the same. And I've seen a rule somewhere that says we are only permitted to modify structures that we exclusively own, which means that they must have a refcount of one. Otherwise the engine separates first, and separation means duplicating the table.

$copy = $a 0 bytes
$copy[] = 1 (first write) 16,781,392 bytes

Enter fullscreen mode

Exit fullscreen mode

For an array of rows there's a detail that works in your favor. Separation copies the outer table and bumps the refcount on each row, it doesn't deep-copy the rows. Appending to a copy of a million-row array cost 16.8 MB (the outer packed table), and changing one field inside one row of that copy cost another 376 bytes for that single row's hash table. The engine copies exactly what you touched, one level at a time.

## A million rows as arrays cost twice what the same rows as objects do

This is the part I actually wanted to know. Query results as associative arrays are the default in every PHP codebase I've seen (eitherfetchAll(PDO::FETCH_ASSOC)or a query builder that returns the same shape). I'd guess most of the arrays alive in a typical request are hash arrays for exactly that reason, they came out of a query or a JSON body with string keys. So the test is a million rows of five fields with the same values in every container.

final
 
class
 
Row

{

 
public
 
function
 
__construct
(

 
public
 
int
 
$id
,

 
public
 
string
 
$name
,

 
public
 
string
 
$email
,

 
public
 
bool
 
$active
,

 
public
 
float
 
$balance
,

 
)
 
{}

}

// each shape, built a million times in a loop and kept in a list

$row
 
=
 
[
'id'
 
=>
 
$i
,
 
'name'
 
=>
 
"user
$i
"
,
 
'email'
 
=>
 
"user
$i
@example.com"
,
 
'active'
 
=>
 
true
,
 
'balance'
 
=>
 
1.5
];

$row
 
=
 
new
 
Row
(
$i
,
 
"user
$i
"
,
 
"user
$i
@example.com"
,
 
true
,
 
1.5
);

$row
 
=
 
[
$i
,
 
"user
$i
"
,
 
"user
$i
@example.com"
,
 
true
,
 
1.5
];

Enter fullscreen mode

Exit fullscreen mode

Bytes per row for a million rows, including the two strings and the slot in the outer list:

Shape

PHP 8.4.21

PHP 8.1.34

Class with 5 declared typed properties

233

250

Same class, 
readonly
 properties

233

250

Packed list per row (the 
FETCH_NUM
 shape)

321

498

SplFixedArray(5)
 per row

323

324

Associative array per row (the 
FETCH_ASSOC
 shape)

481

498

stdClass
 per row (the 
FETCH_OBJ
 shape)

529

546

One thing about this table: all six shapes ran one after another in a single process, and that makes the object rows look a little cheaper than they are. Every object also takes an 8-byte entry in the engine's object store, which doubles when it fills up and never shrinks, and the later object runs reused the entries (and some other bookkeeping) thestdClassrun had already paid for. Measured each in a fresh process, a class row is 241 bytes on 8.4 and 258 on 8.1, and aSplFixedArray(5)row is 340 on 8.4 and 341 on 8.1. The array rows andstdClasscome out the same.

The two strings are the same in every row. "user123456" and "user123456@example.com" cost 40 and 48 bytes each: a 24-bytezend_stringheader plus the characters plus a terminator, rounded up to an allocator bin. The slot in the outer array is 16.78. Take those 105 bytes off and what's left is the container, which I also measured one row at a time to be sure:

assoc row, 5 string keys 376 bytes
stdClass row, 5 dynamic properties 416 bytes
packed row, 5 values 216 bytes
SplFixedArray(5) row 176 bytes
object row, 5 declared properties 128 bytes

Enter fullscreen mode

Exit fullscreen mode

The 376 is the number from the previous section: a 56-byte header plus a hash block sized for the minimum of 8 buckets (8 x 32 for the buckets and 16 x 4 for the index), which comes to 320 bytes. For five fields. Every row carries its own index, its own copy of the key hashes and pointers, and three empty buckets.

The object is 128 because azend_objectheader is 40 bytes and declared properties are stored inline right after it at one 16-byte zval each (so 40 + 5 x 16 = 120 and then the allocator rounds that up to its 128 bin). The property names aren't in the object at all, because the class holds one table that maps each name to a slot offset (built once at compile time) and every instance is just the slots.

Typed or untyped andreadonlyor not makes no difference to the bytes. The type lives in the class and the slot is a zval either way, so the readonly DTO you'd write for correctness reasons is also the cheapest way to hold a row.

stdClassis the worst of both. It has the 40-byte object header and no declared properties, so every field goes into the object's ownpropertieshash table, and that table is exactly the 376-byte array from before with an object wrapped around it.FETCH_OBJgives you exactly this shape a million times over. PHP 8.2 deprecated dynamic properties on ordinary classes butthe RFCmarksstdClasswith#[AllowDynamicProperties], so it isn't going anywhere.

The packed list per row is a nice illustration of the 8.2 change. On 8.4 it's 216 bytes: a header plus eight 16-byte slots rounded into the 160 bin. On 8.1 it's 376, identical to the associative version, because packed buckets were 32 bytes back then and eight of them plus the tiny index landed in the same 320-byte bin. SoFETCH_NUMsaved nothing at all before 8.2 and now it saves a third and costs you the column names.

Okay, but the driver hands me arrays. Turning a million of them into objects is a million constructor calls. Yes, and the constructor's cheap next to the query you already paid for. PDO can instantiate a class per row withFETCH_CLASS(though it assigns properties before calling the constructor unless you addFETCH_PROPS_LATE, and that makes constructor promotion awkward enough that I'd rather write the one mapping line myself anyway) but the better answer to "a million constructor calls" is that you shouldn't be holding a million of anything, and that's the last section.

## SplFixedArray wins on flat lists, and ext-ds doesn't change the picture

SplFixedArrayis a C struct with azend_long sizeand azval *elementsbuffer allocated at exactlysizetimessizeof(zval). There's no hash and no index and no power-of-two rounding. A million integers cost 16.00 bytes per element exactly against the packed array's 16.78 (the packed array rounded its table up to the next power of two). That 5% is the entire memory win, and in exchange you give up growth, string keys and everyarray_*function. For a five-field row it's 176 bytes (an object header plus the struct plus a separate 80-byte element buffer), and that's more than the class.

ext-ds(the PHP extension) I actually compiled for this, because it's the thing people bring up whenever PHP data structures come up, with one note before the numbers:pecl install dsgave me 2.0.0, and on this build it declaredDs\Seq,Ds\Map,Ds\Set,Ds\HeapandDs\Pairand noDs\Vectorat all, so the numbers below are from 1.6.0.

PHP 8.4.21, ext-ds 1.6.0
Ds\Vector of N ints (push) 16,085,160 bytes 16.09 bytes/elem
Ds\Map of N ints (reverse order) 37,748,960 bytes 37.75 bytes/elem
Ds\Map per row inside a Ds\Vector 512,457,608 bytes 512.46 bytes/row

Enter fullscreen mode

Exit fullscreen mode

Ds\Vectoris a contiguous buffer whose capacity isn't tied to powers of two (the manual says so) so it lands at 16.09 instead of 16.78.Ds\Mapbeats the hash array by about 10%. ADs\Mapper row is worse than the plain associative array. It's a good API with real algorithmic guarantees and it does give memory back when a structure shrinks (which arrays never do). It isn't a memory fix for rows, and I wouldn't add a C extension to a deployment for 4% on lists.

## What I'd actually do

Keep lists packed. Append in order, don't fill by index backwards, don't let a string key into something that's supposed to be a list, and callarray_values()on anything that came out ofarray_filter()if it's going to live longer than the next line, and remember thatarray_is_list()is a fine assertion in a test as long as you know it's checking keys.

Rows you hold in memory go into a smallfinalclass with promoted typed properties. Half the memory of the associative array, a name and a type for every field, andreadonlycosts nothing extra. That's the one change I'd make to most of the code I've read that doesfetchAll()and then walks the result.

And don't hold a million rows. Here's the materialize-then-loop shape against the same loop over a generator, run in two separate processes so the peak is honest, and the rows are generated in code with no database involved, so it measures the cost of holding them and not of fetching them:

function
 
rows
(
int
 
$n
):
 
Generator

{

 
for
 
(
$i
 
=
 
0
;
 
$i
 
<
 
$n
;
 
$i
++
)
 
{

 
yield
 
new
 
Row
(
$i
,
 
"user
$i
"
,
 
"user
$i
@example.com"
,
 
true
,
 
1.5
);

 
}

}

function
 
loadAll
(
int
 
$n
):
 
array

{

 
$all
 
=
 
[];

 
foreach
 
(
rows
(
$n
)
 
as
 
$row
)
 
{

 
$all
[]
 
=
 
$row
;

 
}

 
return
 
$all
;

}

// materialize: foreach (loadAll(N) as $row) { $sum += $row->balance; }

// stream: foreach (rows(N) as $row) { $sum += $row->balance; }

Enter fullscreen mode

Exit fullscreen mode

materialize all rows, then loop peak over start 241,157,928 bytes
stream rows through a generator peak over start 37,008 bytes

Enter fullscreen mode

Exit fullscreen mode

Thirty-seven kilobytes instead of 241 megabytes for the same loop over the same million rows. With a real statement the generator is awhile ($r = $stmt->fetch())that yields oneRowper iteration. There's one caveat and it's a big one on MySQL:queries are buffered by defaultso the driver pulls the whole result set into PHP's memory before your firstfetch(), and with mysqlnd that buffer counts againstmemory_limit. So a generator over a buffered result set streams the objects and still holds every raw row underneath. The fix is to setPdo\Mysql::ATTR_USE_BUFFERED_QUERYtofalsefor the big query (on 8.3 and older it'sPDO::MYSQL_ATTR_USE_BUFFERED_QUERY, which 8.5 deprecates) or to page it by primary key. Laravel'scursor()is this exact pattern with a nicer name.

Sixteen bytes a slot is a fair price for a list. What gets expensive is how quietly an array stops being one. 🙂

Thanks for reading! English isn't my first language, so I use AI to polish the grammar. Everything else here - the ideas, the code, the opinions - is mine.

Enjoyed this one? Let's stay in touch — I'm onLinkedIn, always happy to chat, swap ideas, or just say hi. 👋

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse