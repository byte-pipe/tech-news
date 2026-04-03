---
title: Bloom Filters by Example
url: https://llimllib.github.io/bloomfilter-tutorial/
site_name: hackernews
fetched_at: '2025-06-30T13:31:52.040590'
original_url: https://llimllib.github.io/bloomfilter-tutorial/
author: ibobev
date: '2025-06-30'
---

简体中文

# Bloom Filters by Example

A Bloom filter is a data structure designed to tell you, rapidly and memory-efficiently, whether an element is
 present in a set.The price paid for this efficiency is that a Bloom filter is aprobabilistic data structure: it
 tells us that the element eitherdefinitely is notin the set ormay bein the set.The base data structure of a Bloom filter is aBit Vector. Here's a small one we'll use to
 demonstrate:Each empty cell in that table represents a bit, and the number below it its index. To add an element to the Bloom
 filter, we simply hash it a few times and set the bits in the bit vector at the index of those hashes to 1.It's easier to see what that means than explain it, so enter some strings and see how the bit vector changes. Fnv
 and Murmur are two simple hash functions:Enter a string:fnv:murmur:Your set: []When you add a string, you can see that the bits at the index given by the hashes are set to 1. I've used the
 color green to show the newly added ones, but any colored cell is simply a 1.To test for membership, you simply hash the string with the same hash functions, then see if those values are set
 in the bit vector. If they aren't, you know that the element isn't in the set. If they are, you only know that itmightbe, because another element or some combination of other elements could have set the same bits.
 Again, let's demonstrate:Test an element for membership:fnv:murmur:Is the element in the set?noProbability of a false positive:0%And that's the basics of a bloom filter!## Advanced TopicsBefore I write a bit more about Bloom filters, a disclaimer: I've never used them in production. Don't take my
 word for it. All I intend to do is give you general ideas and pointers to where you can find out more.In the following text, we will refer to a Bloom filter withkhashes,mbits in the filter, andnelements that have been inserted.### Hash FunctionsThe hash functions used in a Bloom filter should beindependentanduniformly distributed. They
 should also be as fast as possible (cryptographic hashes such as sha1, though widely used therefore are not very
 good choices).Examples of fast, simple hashes that are independent enough3includemurmur,xxHash, thefnvseries of hashes, andHashMix.To see the difference that a faster-than-cryptographic hash function can make,check out this storyof a ~800% speedup when switching a
 bloom filter implementation from md5 to murmur.In a short survey of bloom filter implementations:Chromiumusesmurmur.
 (also,here'sa short description of how they use bloom filters)Plan9uses a simple hash as proposed
 inMitzenmacher 2005Sdroege Bloom filteruses
 fnv1a (included just because I wanted to show one that uses fnv.)Squiduses MD5RedisBloomuses murmurApache
 Sparkuses murmurinfluxdbuses xxhashbloomd(a neat project that uses a redis-ish protocol) uses murmur for the first two hashes,SpookyHashfor the second two hashes, and a
 combination of the two for further hashes, as described in3fleur (C),flor
 (python), andbloom (go)all use fnvSqliteadded a bloom filter for analytic queries, but I do not understand the hash algorithm. Dr. Hippexplains the purposeof the filters on the
 sqlite forum.RocksDBis configurable, but claimsin
 the sourcethat xxh3, a member of thexxhash
 familyperformed best for themThey also link"Bloom Filters in
 Probabilistic Verification"by Dillinger and Maniolios, but it's pretty far over my head.ScyllaDBuses murmur### How big should I make my Bloom filter?It's a nice property of Bloom filters that you can modify the false positive rate of your filter. A larger filter
 will have less false positives, and a smaller one more.Your false positive rate will be approximately(1-e-kn/m)k, so you can just plug
 the numbernof elements you expect to insert, and try various values ofkandmto
 configure your filter for your application.2This leads to an obvious question:### How many hash functions should I use?The more hash functions you have, the slower your bloom filter, and the quicker it fills up. If you have too few,
 however, you may suffer too many false positives.Since you have to pickkwhen you create the filter, you'll have to ballpark what range you expectnto be in. Once you have that, you still have to choose a potentialm(the number of bits) andk(the number of hash functions).It seems a difficult optimization problem, but fortunately, given anmand ann, we have a
 function to choose the optimal value ofk:(m/n)ln(2)2,3So, to choose the size of a bloom filter, we:Choose a ballpark value fornChoose a value formCalculate the optimal value ofkCalculate the error rate for our chosen values ofn,m, andk. If it's
 unacceptable, return to step 2 and change m; otherwise we're done.### How fast and space efficient is a Bloom filter?Given a Bloom filter withmbits andkhashing functions, both insertion and membership testing
 areO(k). That is, each time you want to add an element to the set or check set membership, you just need
 to run the element through thekhash functions and add it to the set or check those bits.The space advantages are more difficult to sum up; again it depends on the error rate you're willing to tolerate.
 It also depends on the potential range of the elements to be inserted; if it is very limited, a deterministic bit
 vector can do better. If you can't even ballpark estimate the number of elements to be inserted, you may be better
 off with a hash table or a scalable Bloom filter4.### What can I use them for?I'll link you towikiinstead of copying what
 they say.C.
 Titus Brownalso has an excellent talk on an application of Bloom filters to bioinformatics.### References1:Network
 Applications of Bloom Filters: A Survey, Broder and Mitzenmacher. An excellent overview.2:Wikipedia, which has
 an excellent and comprehensive page on Bloom filters3:Less Hashing, Same
 Performance, Kirsch and Mitzenmacher4:Scalable
 Bloom Filters, Almeida et al
