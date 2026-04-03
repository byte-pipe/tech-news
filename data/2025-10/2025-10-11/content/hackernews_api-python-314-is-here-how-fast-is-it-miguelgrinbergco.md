---
title: Python 3.14 Is Here. How Fast Is It? - miguelgrinberg.com
url: https://blog.miguelgrinberg.com/post/python-3-14-is-here-how-fast-is-it
site_name: hackernews_api
fetched_at: '2025-10-11T11:08:37.101181'
original_url: https://blog.miguelgrinberg.com/post/python-3-14-is-here-how-fast-is-it
author: Miguel Grinberg
date: '2025-10-09'
description: miguelgrinberg.com
tags:
- hackernews
- trending
---

# Python 3.14 Is Here. How Fast Is It?

## Posted byon2025-10-08T13:09:36Zunder

In November of 2024 I wrote a blog post titled"Is Python Really That Slow?", in which I tested several versions of Python and noted the steady progress the language has been making in terms of performance.

Today is the 8th of October 2025, just a day after the official release of Python 3.14. Let's rerun the benchmarks to find out how fast the new version of Python is!

Note: If you do not care about tables and charts with results and just want to read my conclusions,click hereto go to the end of the article.

## A Quick Word On How Misleading Benchmarks Can Be

Yes, even though I'm going to share the results of my benchmark, I feel I have to warn you again, like I did in the previous article, that generic benchmarks like this one are not really very useful. Running these benchmarks is fun, and that is why I do it, but it is really impossible to build an accurate performance profile of something as complex as the Python interpreter just from running a couple of silly little scripts.

I have designed my tests so that they run only pure Python code, avoiding the use of any dependencies, and in particular any functions that are written in C code. Native code (aside from the Python interpreter itself, that is) is less likely to become faster from one release of Python to the next, so I see no point in including that in the benchmark. But real-world applications do often use a mix of pure Python and native code, be it C, C++ or Rust, so while my test scripts are great to evaluate the performance of pure Python code, I do not consider them to be representative of the applications we normally use.

In short, have a look at my benchmark, but consider it just one data point and not the last word on Python performance!

## The Testing Matrix

Here is the test matrix that I've worked with, with five dimensions:

* 6 Python versions, plus recent versions of Pypy, Node.js and Rust:CPython3.9, 3.10, 3.11, 3.12, 3.13, 3.14Pypy3.11Node24Rust1.90
* CPython3.9, 3.10, 3.11, 3.12, 3.13, 3.14
* Pypy3.11
* Node24
* Rust1.90
* 3 Python interpretersStandardJust-In-Time (JIT): only for CPython 3.13+Free-threading (FT): only for CPython 3.13+
* Standard
* Just-In-Time (JIT): only for CPython 3.13+
* Free-threading (FT): only for CPython 3.13+
* 2 test scriptsfibo.py: calculatesFibonacci numbers, relying heavily on recursionbubble.py: sorts a list of randomly generated numbers with thebubble sortalgorithm, with a lot of iteration, but no recursion
* fibo.py: calculatesFibonacci numbers, relying heavily on recursion
* bubble.py: sorts a list of randomly generated numbers with thebubble sortalgorithm, with a lot of iteration, but no recursion
* 2 threading modesSingle-threaded4 threads running independent calculations
* Single-threaded
* 4 threads running independent calculations
* 2 computersFramework laptop running Ubuntu Linux 24.04 (Intel Core i5 CPU)Mac laptop running macOS Sequoia (M2 CPU)
* Framework laptop running Ubuntu Linux 24.04 (Intel Core i5 CPU)
* Mac laptop running macOS Sequoia (M2 CPU)

You may think that including Node.js and Rust in my benchmark is an odd choice. Maybe it is, but just the same, I ported the two Python test applications to JavaScript and Rust, so that I can have some reference numbers from outside of the Python ecosystem, just to put things into perspective.

## The Test Scripts

Below you can see the main logic infibo.py:

def fibo(n):
 if n <= 1:
 return n
 else:
 return fibo(n-1) + fibo(n-2)

After running some experiments, I've determined that calculating the 40th Fibonacci number with this function took a few seconds on my two laptops, so this is what I used for all the test results I'm sharing below.

Here is the sort function frombubble.py:

def bubble(arr):
 n = len(arr)
 for i in range(n):
 for j in range(0, n-i-1):
 if arr[j] > arr[j+1]:
 arr[j], arr[j+1] = arr[j+1], arr[j]
 return arr

For this script I also eyeballed what array size to use so that the script took a few seconds to run. I settled on using a list with 10,000 numbers that are randomly generated.

Please do not assume that these are great examples, because they are not. There are more efficient ways to code these functions if the goal was to make them run as fast as possible. But the goal here is not to have fast functions, but to compare how different Python interpreters run the code. I have chosen these functions mainly because one is recursive and the other is not, so that I have two different coding styles in the test set.

The framework that I built for running this benchmark executes each test function three times and reports the average time of the three runs. The complete test scripts along with the benchmark scripts are available on theGitHub repository.

## Benchmark #1: Fibonacci single-threaded

Okay, let's have a look at the first test. For this test I measured the time it took to runfibo(40)in seconds. As I mentioned above, for each data point I ran the code three times and averaged the results.

Here are the numbers in table form:

fibo 1 thread

Linux

macOS

vs. 3.14

3.9

15.21

13.81

0.45x

3.10

16.24

14.97

0.42x

3.11

9.11

9.23

0.71x

3.12

8.01

8.54

0.78x

3.13

8.26

8.24

0.79x

3.14

6.59

6.39

--

Pypy 3.11

1.39

1.24

4.93x

Node 24

1.38

1.28

4.88x

Rust 1.90

0.08

0.10

69.82x

The rightmost column shows the speed ratio against 3.14, so a number smaller than 1 in this column means that the corresponding test was slower than 3.14, and a number above means that it was faster. To calculate these ratios I used the average between the Linux and macOS results.

Sometimes it helps to see the data graphically as well, so here is a chart with the above numbers:

What can be learn from these results? We can see that 3.14 has gotten a nice speed improvement over 3.13. It ran close to 27% faster, which is another way of saying that 3.13 ran at about 79% of the speed of 3.14. These results also show that version 3.11 is the point at which Python versions moved from being "very slow" to "not so slow".

One more detail that isn't related to Python 3.14 is that Pypy continues to blow my mind. In this test it was a hair faster that Node.js, and almost 5 times faster than 3.14. Impressive, although still quite far away from Rust, which as expected runs circles around everybody else.

### Just-In-Time and Free-Threading Variants

Starting with Python 3.13, the CPython interpreter comes in three flavors: standard, free-threading (FT) and just-in-time (JIT). The free-threading interpreter disables the global interpreter lock (GIL), a change that promises to unlock great speed gains in multi-threaded applications. The JIT interpreter includes an on-the-fly compiler to native code, which should, in theory, help portions of code that run multiple times get faster by having them compiled to native code only once.

The results I shared above for 3.13 and 3.14 used the standard interpreter, but I also wanted I to see specifically how the other two interpreter variants dealt with my test. In the next table and chart you can see a comparison of the same test running on the three interpreters under 3.13 and 3.14:

fibo 1 thread

Linux

macOS

vs. 3.14

3.13

8.26

8.24

0.79x

3.13 JIT

8.26

8.28

0.78x

3.13 FT

12.40

12.40

0.52x

3.14

6.59

6.39

--

3.14 JIT

6.59

6.37

1.00x

3.14 FT

7.05

7.27

0.91x

And this is a bit disappointing. At least for this test, the JIT interpreter did not produce any significant performance gains, so much that I had to double and triple check that I used a correctly built interpreter with this feature enabled. I do not know much about the internals of the new JIT compiler, but I'm wondering if it cannot deal with this heavily recursive function.

As far as free-threading, I already discovered last year that the interpreter was slow when running single-threaded code. In 3.14 this interpreter appears to still be slower than the standard interpreter, but the difference is much smaller, with free-threading running at just 91% of the speed of the standard interpreter.

## Benchmark #2: Bubble sort single-threaded

The following results are for the bubble sort benchmark, sorting an array of 10,000 random numbers:

bubble 1 thread

Linux

macOS

vs. 3.14

3.9

3.77

3.29

0.60x

3.10

4.01

3.38

0.57x

3.11

2.48

2.15

0.91x

3.12

2.69

2.46

0.82x

3.13

2.82

2.61

0.78x

3.14

2.18

2.05

--

Pypy 3.11

0.10

0.14

18.14x

Node 24

0.43

0.21

6.64x

Rust 1.90

0.04

0.07

36.15x

This test shows a larger discrepancy between my Linux and macOS laptops, but the ratios between versions on each machine are more or less the same. The difference just suggests that Python on the Mac is able to run this test slightly faster.

The 3.14 interpreter is the faster of the CPythons as in the Fibonacci test, but the difference here is smaller than in the previous benchmark, with Python 3.11 clocking in at just 91% of the speed of 3.14. This test also runs slower in 3.12 and 3.13 than in 3.11, an interesting oddity that I also observed in last year's benchmark.

Pypy this time was 18 times faster than 3.14, and even 3 times faster than Node. I really need to spend some time evaluating Pypy, because it looks amazing.

### Just-In-Time and Free-Threading Variants

Let's see how the 3.13 and 3.14 specialized interpreters fared on the bubble sort test. Here is the table and chart with the results:

bubble 1 thread

Linux

macOS

vs. 3.14

3.13

2.82

2.61

0.78x

3.13 JIT

2.59

2.44

0.84x

3.13 FT

4.13

3.75

0.54x

3.14

2.18

2.05

--

3.14 JIT

2.03

2.32

0.97x

3.14 FT

2.66

2.28

0.86x

The JIT interpreter appears to be a little bit faster here, but only on the Linux version of Python. On the Mac it was a bit faster for 3.13, but slower for 3.14. The speed differences are also very small, so overall I'm feeling the JIT interpreter needs some more time to mature. It seems the code that I'm using is somehow not able to benefit much from JIT compilation.

The free-threading interpreter also ran slower, but again the difference was much smaller in 3.14 than in 3.13, so this is consistent between the two benchmarks. At this point it does not seem like it would make sense to switch to the free-threading interpreter for regular workloads, but it could be an interesting option when the GIL is really getting in the way, which is only for multi-threaded with big CPU needs.

## Benchmark #3: Fibonacci multi-threaded

This year I decided to introduce multi-threaded versions of the two test programs, mainly as an excuse to give the free-threading interpreter the chance to shine.

What I did for the multi-threaded Fibonacci test is to start four threads running the same calculation of the 40th Fibonacci. The four threads ran independently of each other, and the two laptops that I'm using have more than four cores, so they should be able to parallelize this test nicely. The time measurement that I used is from the time I launched the first thread to the time all four threads ended.

Here are the results offibo.pyrunning on 4 threads running on the standard interpreters:

fibo 4 threads

Linux

macOS

vs. 3.14

3.9

67.87

57.51

0.46x

3.10

72.42

61.57

0.43x

3.11

45.83

36.98

0.70x

3.12

36.22

34.13

0.82x

3.13

37.20

33.53

0.81x

3.14

32.60

24.96

--

Pypy 3.11

7.49

6.84

4.02x

Note that I did not run Node and Rust versions of the tests here, since this is a very specific test that only applies to Python's GIL.

Of course these results do not tell us much. We can see again that my Mac seems a bit faster than my Linux machine, but aside from that things have more or less scaled linearly. For example, the single-threaded Fibonacci test ran in 7 seconds, and here it took 25 on the Mac and 32 on Linux, which is, give or take a 4x scale. This is expected because the GIL does not permit the Python code to parallelize.

Let's see the detailed results on the 3.13 and 3.14 interpreters:

fibo 4 threads

Linux

macOS

vs. 3.14

3.13

37.20

33.53

0.81x

3.13 JIT

37.48

33.36

0.81x

3.13 FT

21.14

15.47

1.57x

3.14

32.60

24.96

--

3.14 JIT

32.58

24.90

1.00x

3.14 FT

10.80

7.81

3.09x

And this is quite nice!

Since we were not expecting anything significant for the JIT interpreter on this test, we can ignore those results. But the free-threading interpreter is showing us how removing the GIL can help with running multiple threads that are CPU hungry.

In Python 3.13 the free-threading interpreter ran about 2.2x faster than the standard interpreter. In 3.14 the performance improvement is about 3.1x. This is an exciting result!

## Benchmark #4: Bubble sort multi-threaded

To complete this benchmarking exercise, below you can see the results of the bubble sort test running on 4 threads. For this test I had each thread sort 10,000 random numbers. The four threads received copies of the same randomly generated array.

First let's look at the standard interpreters:

bubble 4 threads

Linux

macOS

vs. 3.14

3.9

16.14

12.58

0.66x

3.10

16.12

12.95

0.65x

3.11

11.43

7.89

0.97x

3.12

11.39

9.01

0.92x

3.13

11.54

9.78

0.88x

3.14

10.55

8.27

--

Pypy 3.11

0.54

0.59

16.65x

These results show no big surprises either. The single-threaded version of this test executed in about 2 seconds on 3.14, and here we have 10 seconds on Linux and 8 seconds on Mac. It's interesting that on the Linux machine this test took a bit longer than 4x the single-threaded time.

Here are the results with the new interpreters in 3.13 and 3.14:

bubble 4 threads

Linux

macOS

vs. 3.14

3.13

11.54

9.78

0.88x

3.13 JIT

10.90

9.19

0.94x

3.13 FT

9.83

5.05

1.17x

3.14

10.55

8.27

--

3.14 JIT

10.03

9.26

0.98x

3.14 FT

6.23

3.02

2.03x

And here once again we see a good use case for the free-threading interpreter. For this test the Mac's free-threading did better than Linux, but on overage 3.14 FT ran about 2x faster than standard 3.14. If you have a multi-threaded application that is CPU heavy, a switch to the free-threading interpreter might be a good idea.

The odd results of the JIT interpreter being slower on the 3.14 Mac interpreter that we've seen in the single-threaded bubble sort test have repeated here, so I guess they were not a fluke, but in any case the differences are not big enough to matter, in my opinion. We'll just have to wait for the JIT interpreter to continue evolving in future releases.

## Conclusions

I hope you found my benchmark results interesting. As way of a summary, these are the conclusions that I'm making from these results:

* CPython 3.14 appears to be the fastest of all the CPythons.
* If you can't upgrade to 3.14 just yet, consider using a release since 3.11, as these are significantly faster than 3.10 and older.
* The 3.14 JIT interpreter does not appear to provide any significant gains in speed, at least not with my test scripts.
* The 3.14 free-threading interpreter is faster than the standard interpreter for CPU heavy multi-threaded applications, so It is worth a try if your application fits this use case. I wouldn't recommend using this interpreter for other workloads, as it is still slower for code that is not directly slowed down by the GIL.
* Pypy is insanely fast!

Have you benchmarked Python 3.14? Let me know in the comments if you have results that are different than mine.

## Buy me a coffee?

Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation throughBuy me a coffee. Thanks!

## Share this post

Hacker News

Reddit

Twitter

LinkedIn

Facebook

E-Mail

36 comments

### Leave a Comment

Name

Email

Comment



Captcha

Flask Web Development, 2nd Edition

If you want to learn modern web development techniques with Python and Flask, you may find the second edition of myO'Reilly bookuseful.

Click here to get this Book!

About Miguel

Welcome to my blog!

I'm a software engineer and technical writer, currently living in Drogheda, Ireland.

You can also find me onGithub,LinkedIn,Bluesky,Mastodon,Twitter,YouTube,andPatreon.

Thank you for visiting!

Categories


3


7


10


1


5


1


11


23


5


6


129


1


8


36


10


1


2


5


3


7


2


193


1


175


7


8


19


1


6


12


22


2


3


1

© 2012- by Miguel Grinberg. All rights reserved.Questions?
