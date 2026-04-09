---
# Many Hard Leetcode Problems are Easy Constraint Problems • Buttondown
url: https://buttondown.com/hillelwayne/archive/many-hard-leetcode-problems-are-easy-constraint/
site_name: hackernews
fetched_at: '2025-09-12T19:06:16.535555'
original_url: https://buttondown.com/hillelwayne/archive/many-hard-leetcode-problems-are-easy-constraint/
author: mpweiher
date: '2025-09-12'
description: Use the right tool for the job.
---

September 10, 2025

# Many Hard Leetcode Problems are Easy Constraint Problems

## Use the right tool for the job.

In my first interview out of college I was asked the change counter problem:

Given a set of coin denominations, find the minimum number of coins required to make change for a given number. IE for USA coinage and 37 cents, the minimum number is four (quarter, dime, 2 pennies).

I implemented the simple greedy algorithm and immediately fell into the trap of the question: the greedy algorithm only works for "well-behaved" denominations. If the coin values were[10, 9, 1], then making 37 cents would take 10 coins in the greedy algorithm but only 4 coins optimally (10+9+9+9). The "smart" answer is to use a dynamic programming algorithm, which I didn't know how to do. So I failed the interview.

But you only need dynamic programming if you're writing your own algorithm. It's really easy if you throw it into a constraint solver likeMiniZincand call it a day.

int: total; array[int] of int: values = [10, 9, 1]; array[index_set(values)] of var 0..: coins;

constraint sum (c in index_set(coins)) (coins[c] \* values[c]) == total; solve minimize sum(coins);

You can try this onlinehere. It'll give you a prompt to put intotaland then give you successively-better solutions:

## coins = [0, 0, 37];

## coins = [0, 1, 28];

## coins = [0, 2, 19];

## coins = [0, 3, 10];

## coins = [0, 4, 1];

## coins = [1, 3, 0];

Lots of similar interview questions are this kind of mathematical optimization problem, where we have to find the maximum or minimum of a function corresponding to constraints. They're hard in programming languages because programming languages are too low-level. They are also exactly the problems that constraint solvers were designed to solve. Hard leetcode problems are easy constraint problems.1Here I'm using MiniZinc, but you could just as easily use Z3 or OR-Tools or whatever your favorite generalized solver is.

### More examples

This was a question in a different interview (which I thankfully passed):

Given a list of stock prices through the day, find maximum profit you can get by buying one stock and selling one stock later.

It's easy to do in O(n^2) time, or if you are clever, you can do it in O(n). Or you could be not clever at all and just write it as a constraint problem:

array[int] of int: prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]; var int: buy; var int: sell; var int: profit = prices[sell] - prices[buy];

constraint sell > buy; constraint profit > 0; solve maximize profit;

Reminder, link to trying it onlinehere. While working at that job, one interview question we tested out was:

Given a list, determine if three numbers in that list can be added or subtracted to give 0?

This is a satisfaction problem, not a constraint problem: we don't need the "best answer", any answer will do. We eventually decided against it for being too tricky for the engineers we were targeting. But it's not tricky in a solver;

include "globals.mzn"; array[int] of int: numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]; array[index_set(numbers)] of var {0, -1, 1}: choices;

constraint sum(n in index_set(numbers)) (numbers[n] \* choices[n]) = 0; constraint count(choices, -1) + count(choices, 1) = 3; solve satisfy;

Okay, one last one, a problem I saw last year atChipy AlgoSIG. Basically they pick some leetcode problems and we all do them. I failed to solvethis one:

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

The "proper" solution is a tricky thing involving tracking lots of bookkeeping states, which you can completely bypass by expressing it as constraints:

array[int] of int: numbers = [2,1,5,6,2,3];

var 1..length(numbers): x; var 1..length(numbers): dx; var 1..: y;

constraint x + dx <= length(numbers); constraint forall (i in x..(x+dx)) (y <= numbers[i]);

var int: area = (dx+1)\*y; solve maximize area;

output ["((x)->(x+dx))*(y) = (area)"]

There's even a way toautomatically visualize the solution(usingvis_geost_2d), but I didn't feel like figuring it out in time for the newsletter.

### Is this better?

Now if I actually brought these questions to an interview the interviewee could ruin my day by asking "what's the runtime complexity?" Constraint solvers runtimes are unpredictable and almost always than an ideal bespoke algorithm because they are more expressive, in what I refer to as thecapability/tractability tradeoff. But even so, they'll do way better than abadbespoke algorithm, and I'm not experienced enough in handwriting algorithms to consistently beat a solver.

The real advantage of solvers, though, is how well they handle new constraints. Take the stock picking problem above. I can write an O(n²) algorithm in a few minutes and the O(n) algorithm if you give me some time to think. Now change the problem to

Maximize the profit by buying and selling up tomax_salesstocks, but you can only buy or sell one stock at a given time and you can only hold up tomax_holdstocks at a time?

That's a way harder problem to write even an inefficient algorithm for! While the constraint problem is only a tiny bit more complicated:

include "globals.mzn"; int: max_sales = 3; int: max_hold = 2; array[int] of int: prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8]; array [1..max_sales] of var int: buy; array [1..max_sales] of var int: sell; array [index_set(prices)] of var 0..max_hold: stocks_held; var int: profit = sum(s in 1..max_sales) (prices[sell[s]] - prices[buy[s]]);

constraint forall (s in 1..max_sales) (sell[s] > buy[s]); constraint profit > 0;

constraint forall(i in index_set(prices)) (stocks_held[i] = (count(s in 1..max_sales) (buy[s] <= i) - count(s in 1..max_sales) (sell[s] <= i))); constraint alldifferent(buy ++ sell); solve maximize profit;

output ["buy at (buy)n", "sell at (sell)n", "for (profit)"];

Most constraint solving examples online are puzzles, likeSudokuor "SEND + MORE = MONEY". Solving leetcode problems would be a more interesting demonstration. And you get more interesting opportunities to teach optimizations, like symmetry breaking.

1. Because my dad will email me if I don't explain this: "leetcode" is slang for "tricky algorithmic interview questions that have little-to-no relevance in the actual job you're interviewing for." It's fromleetcode.com.↩

If you're reading this on the web, you can subscribehere. Updates are once a week. My main website ishere.

My new book,Logic for Programmers, is now in early access! Get ithere.

### Read more:

- #### Solving LinkedIn Queens with SMTFor sure easier than solving it in SAT!
- #### Knights, Puzzles, and HypermodelsI, being a huge nerd, am a fan of logic puzzles. One of the most famous ones is "Knights and Knaves": you have a bunch of statements from people, where...

Don't miss what's next. Subscribe to Computer Things:

Subscribe

Start the conversation:

Comment and Subscribe
