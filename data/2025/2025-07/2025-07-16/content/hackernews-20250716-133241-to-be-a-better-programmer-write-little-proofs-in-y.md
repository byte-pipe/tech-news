---
title: To be a better programmer, write little proofs in your head
url: https://the-nerve-blog.ghost.io/to-be-a-better-programmer-write-little-proofs-in-your-head/
site_name: hackernews
fetched_at: '2025-07-16T13:32:41.562044'
original_url: https://the-nerve-blog.ghost.io/to-be-a-better-programmer-write-little-proofs-in-your-head/
author: mprast
date: '2025-07-16'
published_date: '2025-07-14T22:47:10.000Z'
---

This is a brief write-up of a trick I learned that helps me write code faster and more accurately. I say "trick", but it's really something I started to do without noticing as I moved further into my career.

When you're working on something difficult, sketch a proof in your head as you go that your code will actually do what you want it to do. A simple idea, but easier said than done: doing this "online" without interrupting your flow takes a lot of practice. But once you get really good at it, you'll find that a surprising amount of the time your code will work on the first or second try. It feels a little magical.

There are lots of ways to pull this off, and I don't want to be too prescriptive. I'll just list a few examples of the kinds of things I find myself reasoning about on the fly, so you get the general idea.

## Monotonicity

Something to keep an eye out for when proving things to yourself about your code is which parts aremonotonic.

You're probably familiar with monotonic functions from mathematics. Informally, they're functions that don't "go backwards" - i.e. an increasing monotonic function can only increase or stay the same, while a decreasing monotonic function can only decrease or stay the same (these are also known asnondecreasingandnonincreasingfunctions, respectively.)

The concept of monotoniccodeis a little more nebulous than the concept of a monotonic function, but it captures the same idea of a process that can only proceed in one direction. Check-pointing, for example, is a great example of monotonicity. If you have (say) a script that needs to perform multiple tasks in sequence, you can keep a bit of state around on disk that details how many tasks you have completed so far. If something goes wrong and your script crashes, it can check the on-disk state to figure out how far it got, then start again from the earliest state that hasn't been run yet.

Checkpointing means that the "current step" pointer in your script can only go forwards, since the script can't regress and re-run a step it's already done. In this sense the script progressesmonotonically, and it's apparent that if the script ever completes successfully, it will have run every step exactly once.

Keeping this kind of activity log is a simple idea that often pops up in surprising places, such as journaling file systems and database write-ahead logs. Another, more involved database example is an LSM tree. LSM trees are used in some databases to store rows in-memory and on-disk, and most of the time they are purely additive. Put loosely - an LSM tree keeps a log of all inserts, deletes, and updates, and scans the log to reconstruct the appropriate value of the row when the row is read. Stale operations are periodically discarded to save space in a process called compaction. The space taken by an LSM treeonlygrows (except during compaction, when itonlyshrinks.)You can compare this to a B-tree, which is a more traditional database structure that deletes and updates rows in place. B-trees generally have to do a lot more work to reclaim the freed space after a delete, restructure things so there's room if an update grows a row, make sure there's enough buffer, etc. If you want, read a little bit more about B-trees and LSM trees, and see which one feels more intuitive to reason about.

It's worth keeping an eye out for monotonicity, because you can usually use it to rule out wide swaths of possible outcomes. Another variation on this theme is immutability (which in a lot of ways is monotonicity's cousin) - when you create an immutable object, that object cannot be modified. Values can be assigned to an immutable object exactly once, at the time of the object's construction; you can't "back out" or "undo" the assignments. This allows you to ignore, out of hand, all scenarios in which an object might change out from under your feet.

## Pre- and post-conditions

Pre-conditions and post-conditions are ways to specify constraints on the behavior of a function. A function'spre-conditionsare the things that are assumed to be true just before the function runs. These can be conditions on the function's input, or more general claims about the program's state or environment. A function'spost-conditionsare things that are assumed to be true just after the function returns. As with pre-conditions, these claims can involve just about anything. If the pre-conditions of a function are true before the function runs, and the post-conditions arenottrue after the function finishes, then the function is not implemented correctly, at least according to the specified constraints.

These are simple (even obvious) concepts and not really proof techniques in and of themselves, but simply keeping track of what they are in formal terms can aid your reasoning.

(Sometimes you may come to find that your function does not have well-defined pre- and post-conditions, which is also good to know!)

Pinning down your post-conditions, in particular, is a good way to generate ideas for unit tests. It can also help to defensively add assertions that your preconditions and postconditions are true, and crash otherwise. This can make it easier to reason about what your code will do in the event itdoesn'tcrash - this may sound like, at best, a neutral trade-off, but it's usually safer for code to crash early than to behave in unpredictable ways.

## Invariants

Theinvariantsof a piece of code are things that should always be true before, during, and after that code runs, no matter what. As with pre- and post-conditions, an invariant can involve pretty much anything.

It can be handy to think about consistency in terms of an invariant - in these situations the invariant is "this data structure is consistent/valid", and you need to prove to yourself that the code preserves that invariant at every point, no matter what happens. An easy way to do this to divide up your code into atomic "steps", and to prove that each step preserves the invariant on its own. Then you can conclude that the invariant will hold no matter which steps run or the order that they run in.

One of the oldest and most famous examples of an invariant is theaccounting equation, which is the foundation of double-entry accounting. The accounting equation says, loosely, that the total amount of debits on a company's ledger must equal the total amount of credits. It's easy to prove that double-entry accounting, when done correctly, preserves this invariant: for every transaction, all increases (or decreases) to credit accounts must be equal to all increases (or decreases) to debit accounts. It's easy to see that if debits and credits balance before a transaction, they balance after the transaction. Thus, the invariant is always preserved.

Another way to maintain certain kinds of invariants is to use a listener or lifecycle method to make sure that the invariant stays true at certain critical points. This technique is often used when multiple pieces of state need to be kept in sync - for example, C++ usesconstructors and destructorsto ensure that any memory an object needs only remains allocated while the object actually exists.useEffectdoes something similar for React components.

(Since invariants have to hold for every possible scenario, they're usually easier to reason about when making changes that introduce relatively few new execution paths.)

## Isolation

I have a long-held conviction that alotof the "craft" of software is (or ought to be) centered around modifying or augmenting an existing system without destabilizing anything. When making modifications to a codebase, it can be exceptionally useful to know how to prove that behaviors youdidn'tintend to change were, in fact, left unchanged.

There's a technique I rely on a lot to prove this to myself; I'm not sure if there's a name for this, and I perhaps wouldn't even call it a technique as much as a pattern of thought. The best way I can describe it is this: every change has a "blast radius" - a change to one part of the code may necessitate a change to another part to ensure the consistency/correctness of the whole system. This second change might require a change to a third part, and so on. Nailing down what behaviors a change does/doesn't affect involves identifying structural "firewalls" that can prevent a change from propagating past a certain point. It's kind of like the conceptual cousin of encapsulation.

This idea is pretty abstract, so here's an example from Nerve:

Nerve is a query engine that lets users query many data sources as if they were a single huge API. The Nerve query pipeline consists of aquery planner, which computes a specific step-by-step plan for running a query, and aquery executor, which carries the plan out. A query in Nerve can contain bothmaterialfields andvirtualfields. Virtual fields are basically derived fields - in other words, a material field is pulled directly from a source API, while a virtual field is computed at runtime from other virtual or material fields.

Material fields are pretty easy to handle - you just make the appropriate requests and pull data from the responses as needed. Virtual fields are a little trickier, because sometimes virtual fieldsdependon other fields. We need to ensure that we have all of the virtual field's prerequisites before we can calculate a virtual field. It's unnecessarily onerous to require the user to add these prerequisites to the query themselves. Instead, we should have some machinery that pulls a virtual field's dependencies before calculating it. But where should this machinery go?

One straightforward option is to modify both the query planner and the query executor to give them a concept of a material field that's pulled as a dependency instead of as something specified in the query. These "dependency fields" should be kept around so we can use them to calculate virtual fields, but they shouldn't be included in the final query results. There are other design considerations we need to keep in mind - for example, we probably want to find ways to pull these dependency fields in the same requests that we make when pulling "normal" material fields, etc. etc.

This is basically an expansion of the query pipeline: maybe a little involved, but certainly doable. There's a trick we can pull here though, which is to dodge the problem byover-pullingand cleaning up after the fact.

In this second approach we don't introduce any new concepts at all. Instead, during query planning, we calculate the dependencies of each virtual field and simply add them to the query, then hand them off the query executor. The query executor has no idea that the query it's getting is not the query the user wrote; it just runs the query as usual, first pulling all material fields, and then calculating any relevant virtual fields (and it never has to pull a virtual field's dependencies because somehow they're always magically there!)

After query execution is complete, we'll end up with query results that contain strictly more fields than the user asked for. So at the end, we add apruningstep that removes any fields that weren't in the user's query.

The main advantage of this solution is that the change iscompletelyconfined to two small layers and the beginning and end of the query pipeline - the stuff in the middle (the "meat" of the query engine) doesn't need to change at all. In particular, the boundary between the query planner and the query executor acts as a "firewall" that stops the change from propagating. This makes it trivially easy to prove that our changes won't cause regressions when we execute queries that don't need to pull any dependencies (since in that case we only run code that hasn't been touched!)

Sometimes this kind of approach is appropriate, and sometimes it isn't, but all else being equal it simply produces less cognitive load when you leave as much code untouched as you can.

(You may have heard this idea talked about in the context of theOpen-Closed Principle. This principle encompasses a bunch of OOP particulars that aren't relevant here; what is relevant is thephilosophybehind it, namely: "When requirements change, you extend the behavior of [your program] by adding new code, not by changing old code that already works.")

## Induction

Lots of interesting programs involve recursive functions or recursive data structures (and in a certain theoretical sense recursion is central to the act of computation itself.) Depending on the area you're working in, you may come across recursion constantly or only occasionally, but in either case knowing how to reason about it can make your life a lot easier.

A recursive data structure is a structure that contains a copy of itself (not necessarily an exact copy, but an instance of the same "type" of structure.) This copy can contain a copy, and so on; the process either goes on forever or terminates at a "base case." A fractal, for instance, is recursive.

In computer science, the classic example of a recursive data structures is a tree. A tree is a node with a certain number of children; each child is itself a tree. A tree withnochildren is called a leaf, which is the base case.

Lists can also be formulated recursively, although you may not usually think of them that way. Every recursive list consists of ahead, which is the "first" or leftmost element of the list, along with atail, which contains the remaining elements of the list. The tail is itself a list, and the base case list is the empty list. (In a similar vein, you can think of the natural numbers as recursive - every natural number is 1 plus another, smaller, natural number, except for 0, which is the base case.)

A recursivefunctionis a function that calls itself. Recursive functions are usually used to process recursive data structures, since they can call themselves on the recursive copies (for example, a function to process a tree can call itself on all of the child trees.)

There's also a proof technique that's tailor-made for handling recursive structures, which is calledinduction. The "classical" version of induction is used to prove that some proposition \(P(n)\) holds true for any natural number \(n\). There are two steps to proving this:

* Prove \(P(0)\) is true.
* Prove that \(P(n)\) implies \(P(n+1)\).

This second step is called theinductive step, and the assumption that \(P(n)\) holds is called theinductive hypothesis. The inductive step is where the real power of induction lies - \(P\) is often much easier to prove once you have the inductive hypothesis at your disposal. The point of induction is to write a "incremental" version of the proof instead of trying to simultaneously prove it for every number at once.

When you're writing a recursive function, try to prove its correctness to yourself using induction. Here's a simple example, loosely adapted from the Nerve codebase:

Without getting too deep in the weeds - there's a particular case in Nerve where we need to visualize an AST for the user. The full AST is pretty complex, so before displaying it we need to remove nodes that the user probably doesn't care about. When we remove a node, that node's parent should "inherit all of its children" (in technical terms, we need tocontract the edgebetween the removed node and its parent.)

A quick note on terminology: technically, contraction is a term that only applies to edges, but I'm going to fudge things a little and talk about contracting nodes and trees as well. When I say "contract a node", I mean "contract the edge between the node and its parent". When I say "contract a tree", I mean "contract some edge in the tree."

Here's the function we use in Nerve (not the exact function, but this gives you the idea):

function simplifyTree(root: Node): Node {
 let newChildren = [] as Array<Node>;

 for (const child of root.children) {
 const simplifiedChild = simplifyGraph(child);

 if (shouldContract(simplifiedChild)) {
 for (const grandChild of simplifiedChild.children) {
 newChildren.push(grandChild);
 }
 } else {
 newChildren.push(simplifiedChild);
 }
 }

 root.children = newChildren;

 return root;
}

We want our function to simplify the provided AST as much as possible. In other words, the post-condition is this: the graph returned bysimplifyGraphshould be "fully contracted" - i.e. it should not be possible to contract any more edges.

Here's an inductive proof that this condition does, in fact hold:

* Let's start with the base case. By definition, a root node can't be contracted, because there's no parent to roll it up into. So the base case - a single leaf node - already satisfies the post-condition. If we passsimplifyGrapha leaf node, it just returns it as-is, so we can conclude it works correctly on the base case.
* It's time for the magic: the inductive step. We need to prove that ifsimplifyGraphis correct for every subtree of a tree \(T\), it's correct for \(T\) as well. Crucially, we now have access to the inductive hypothesis, which means that we can assume each subtree (i.e. each tree rooted at asimplifiedChild) can't be contracted any further.The only new potential contraction we have to consider is betweensimplifiedChildandroot. If we determinesimplifiedChildneeds to be contracted, we remove it and graft all of its children ontoroot. After doing this for eachsimplifiedChild, we knowfor surethat the tree rooted atrootcan't be contracted any further, since if it could, that means at least one subtree could be contracted, which contradicts the inductive hypothesis. QED!

If you can start to do this kind of inductive reasoning on instinct, you may find it easier to deal with recursive functions.

(If you want, try to convince yourself thatsimplifyGraphworks correctly on every possible input by reasoning holistically, without using induction. Which approach feels more natural to you?)

## Proof-affinity as a quality metric

My thesis so far is something like "you should try to write little proofs in your head about your code." But there's actually a secret dual version of this post, which says "you should try to write your code in a form that's easy to write little proofs about."

Similarly, each section of this post has its own dual form:

* Look for monotonicity and immutability. → Write code that is monotonic and uses immutable data structures.
* Keep track of your pre- and post-conditions. →Startwith pre- and post-conditions and write your code around those. Structure your code so that the pre- and post-conditions are easy to conceptualize and verify.
* You can prove a function maintains an invariant by proving each unit of work does. → You should subdivide your code into the smallest possible units that can maintain the invariant.
* Pay attention to where component boundaries act as "firewalls" that prevent change propagation. → Do your best to build as many of these "firewalls" as possible, and take advantage of them when writing new features.
* Use induction to prove things about recursive functions incrementally instead of all at once. Assume the inductive hypothesis is already proved, and use that to your advantage. → Write your recursive functions incrementally. Assume the recursive call is already implemented and write the part of the function that builds the \(n+1\) case from the \(n\) case. Then, separately, implement the base case.

The idea is that you can judge the quality of your code by the ease with which you can reason about it. If it's easy for you to prove to yourself that your code is correct, it's probably pretty well-designed. On the other hand, if it's consistently frustrating or difficult, you should consider cleaning up or restructuring your code to make it more straightforward.

I was tempted to call this quality "provability", but that term exists and has a different meaning, so instead I'll call it "proof-affinity."

As the suggestions above show, it's possible to (at least subjectively) design for maximum proof-affinity.

Proof-affinity is, of course, not the only dimension of software quality that matters (you also want your code to be correct, and fast, and as easy as possible to use), but I think it's a very important one; after all, in order to build, augment, improve, or test your code, you have to understand what it does, what it doesn't do, and what itcoulddo. This may sound grandiose, but I think that in an important sense, proof-affinity is a catalyst for good programming!

## How to get better at this

As I mentioned at the start, the type of micro-reasoning I've talked out here only starts to pay off once you can do it without really thinking. It's a little like typing that way; knowing how to touch-type only saves you time over hunting and pecking when it's basically instinctual. In both cases, developing your intuition requires...practice! I don't think there are any shortcuts; you've just gotta put in the hours.

I think the best way to do this is to write more (mathematical) proofs. Writing proofs about programs will definitely help, but I think the simple act of constructing proofs - on any topic - is a great way to hone the kind of logical thinking that will serve you well when working with complex systems (but you have towritethem, and not just read them. Do the exercises!) For my own part, I started doing mathematics for fun a while ago, and I've noticed that writing proofs has helped improve my clarity of thought in a broad array of settings.

If you don't know where to start, I've been going through Stanford'sundergrad algorithms classon EdX, which is a fun, proof-focused treatment with (imo) a great professor!

Another good place to train is - though it pains me to say it - Leetcode. Like many others, I think there are serious drawbacks to Leetcodeinterviews, but it can be useful for practicing on your own, since a lot of the problems are just difficult enough to exercise your proof-writing muscles. You don't have to time yourself (I usually don't.) Also, try to avoidproblemsthat have a "trick" to solving them; instead, findproblemswhere at least some of the challenge is in formulating and implementing everything correctly. Focus on getting to a successful submission in as few tries as possible (if you run into little things like syntax errors that's ok.)

Happy coding/proving!
