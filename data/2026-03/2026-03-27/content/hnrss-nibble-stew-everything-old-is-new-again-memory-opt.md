---
title: 'Nibble Stew: Everything old is new again: memory optimization'
url: https://nibblestew.blogspot.com/2026/03/everything-old-is-new-again-memory.html
site_name: hnrss
content_file: hnrss-nibble-stew-everything-old-is-new-again-memory-opt
fetched_at: '2026-03-27T19:21:03.736933'
original_url: https://nibblestew.blogspot.com/2026/03/everything-old-is-new-again-memory.html
date: '2026-03-23'
description: 'Everything old is new again: memory optimization'
tags:
- hackernews
- hnrss
---

## Monday, March 23, 2026

### Everything old is new again: memory optimization

At this point in history, AI sociopaths have purchased all the world's RAM in order to run their copyright infringement factories at full blast. Thus the amount of memory in consumer computers and phones seems to be going down. After decades of not having to care about memory usage, reducing it has very much become a thing.

Relevant questions to this state of things include a) is it really worth it and b) what sort of improvements are even possible. The answers to these depend on the task and data set at hand. Let's examine one such case. It might be a bit contrived, unrepresentative and unfair, but on the other hand it's the one I already had available.

Suppose you have to write script that opens a text file, parses it as UTF-8, splits it into words according to white space, counts the number of time each word appears and prints the words and counts in decreasing order (most common first).

# The Python baseline

This sounds like a job for Python. Indeed,an implementationtakes fewer than 30 lines of code. Its memory consumption on a small text file [update: repo's readme, which is 1.3k] looks like this.

Peak memory consumption is 1.3 MB. At this point you might want to stop reading and make a guess on how much memory a native code version of the same functionality would use.

# The native version

A fully native C++ version usingPystdrequires 60 lines of code to implement the same thing. If you ignore the boilerplate, the core functionality fits in 20 lines. The steps needed are straightforward:

1. Mmapthe input file to memory.
2. Validate that it is utf-8
3. Convert raw data into a utf-8 view
4. Split the view into words lazily
5. Compute the result into a hash table whose keys are string views, not strings

The main advantage of this is that there are no string objects. The only dynamic memory allocations are for the hash table and the final vector used for sorting and printing. All text operations use string views , which are basically just a pointer + size.

In code this looks like the following:

Its memory usage looks like this.

Peak consumption is ~100 kB in this implementation. It uses only 7.7% of the amount of memory required by the Python version.

# Isn't this a bit unfair towards Python?

In a way it is. The Python runtime has a hefty startup cost but in return you get a lot of functionality for free. But if you don't need said functionality, things start looking very different.

But we can make this comparison even more unfair towards Python. If you look at the memory consumption graph you'll quite easily see that 70 kB is used by the C++ runtime. It reserves a bunch of memory up front so that it can do stack unwinding and exception handling even when the process is out of memory. It should be possible to build this code without exception support in which case the total memory usage would be a mere 21 kB. Such version would yield a 98.4% reduction in memory usage.

Posted by

Jussi

at

4:06 PM

Email This
BlogThis!
Share to X
Share to Facebook
Share to Pinterest

Older Post

Home

Subscribe to:

Post Comments (Atom)