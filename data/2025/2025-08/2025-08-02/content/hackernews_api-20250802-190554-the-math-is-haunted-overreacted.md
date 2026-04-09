---
title: The Math Is Haunted — overreacted
url: https://overreacted.io/the-math-is-haunted/
site_name: hackernews_api
fetched_at: '2025-08-02T19:05:54.061786'
original_url: https://overreacted.io/the-math-is-haunted/
author: danabramov
date: '2025-07-31'
description: A taste of Lean.
tags:
- hackernews
- trending
---

# The Math Is Haunted

July 30, 2025

Pay what you like

For the past few months, I’ve been writing a lot ofLean.

Lean is a programming language, but it is mostly used by mathematicians. That is quite unusual! This is because Lean is designed to formalize mathematics.

Lean lets mathematicianstreat mathematics as code—break it into structures, theorems and proofs, import each other’s theorems, and put them on GitHub.

Thebig ideais that eventually much of the humanity’s mathematical knowledge might be available as code—statically checked, verifiable, and composable.

So what does using Lean feel like?

### Sorry Not Sorry

To give you a taste of Lean, here is a tiny theorem that says2is equal to2:

theorem
 two_eq_two
 :
2
 =
2
 :=
by

 sorry

What’s going on here?

To a mathematician’s eye, this syntax looks like stating a theorem. We have thetheoremkeyword, the name of our theorem, a colon:before its statement, the statement that we’d like to prove, and:= byfollowed by the proof (sorrymeans that we haven’t completed the actual proof yet but we’re planning to fill it in later).

But if you’re a programmer, you might notice a hint of something else. Thattheoremlooks suspiciously like a function. But then what is2 = 2? It looks like a return type of that function. But how can2 = 2be atype? Isn’t2 = 2just a boolean? And if2 = 2reallyisa type, what are thevaluesof that2 = 2type? These are very interesting questions, but we’ll have to forget about them for now.

Instead, we’ll start by inspecting the proof:

theorem
 two_eq_two
 :
2
 =
2
 :=
by

 sorry

(You can try it in alive editorthough it’s a bit flakier than alocal setup.)

Put the cursorbeforethesorry, and notice a panel calledTactic stateon the right. With the cursor before thesorry, the tactic state displays⊢ 2 = 2:

Here,⊢means thegoal, i.e. the statement you’re supposed to be proving. Your current goal is to prove2 = 2, so the tactic state says⊢ 2 = 2.

Now put the cursor rightafterthesorryand notice the goal has disappeared:

The goal is gone! In other words, you’ve “proven”2 = 2by sayingsorry.

Of course, this is nonsense. You can think ofsorryas a universal proof—it closesanygoal. It’s a lie. In that sense,sorryis exactly likeanyin TypeScript. It lets you suppress the proof checker but you haven’t actually shown anything useful.

Let’s try get rid of thesorry:

Now you see that the proof is incomplete, and the goal is unsolved. To actually prove2 = 2, typerflon the next line, which will successfully close the goal:

Here,rflmeans “reflexivity”, from “reflection”, like a mirror image. Whenever you have a “mirrored” goal likesomething = something,rflwill close it. You can think ofrflas a built-in piece of knowledge that “a thing is equal to itself”.

With the goal closed, your proof is done.

theorem
 two_eq_two
 :
2
 =
2
 :=
by

 rfl

Now that you’ve proventwo_eq_two, you may refer to this fact from other places.

theorem
 two_eq_two
 :
2
 =
2
 :=
by

 rfl



theorem
 two_eq_two_again
 :
2
 =
2
 :=
by

 exact two_eq_two

Ah, modularity!

Here,two_eq_two_againdelegates the rest of the proof totwo_eq_twobecause the current goal (⊢ 2 = 2) isexactlywhattwo_eq_twoalready proves. (To a programmer’s eye, this might look like returning the result of a function call.)

For a single-line example, this is contrived, butexact some_other_theoremis useful for breaking down a complex proof into smaller individual theorems.

The commands we’ve used—exact,sorry,rfl—are calledtactics. A Lean proof (afterby) is written as a sequence of tactics. Tactics let youclosedifferent goals—rfllets you close goals likex = x,exact some_other_theoremlets you close goals you’ve already proven, andsorrylets you close any goal (at your own peril).

To prove a theorem, you would use just the right tactics until you close every goal.

### The Math Is Haunted

So far, you have proven that2 = 2, which was not very interesting.

Let’s see if you can prove that2 = 3:

theorem
 two_eq_two
 :
2
 =
2
 :=
by

 rfl



theorem
 two_eq_three
 :
2
 =
3
 :=
by

 sorry

Like before,sorrylets you close any goal, even2 = 3:

But that is cheating, and we will endeavor to remove thesorry.

Replacesorrywithrfl:

Not so easy now! You could close⊢ 2 = 2withrflbecause2 = 2is shaped likesomething = something. However, the goal⊢ 2 = 3is notshaped likesomething = something, and thereforerfldoes notclose the⊢ 2 = 3goal.

That, actually, is a good thing.In most useful mathematical theories,2 = 3is a false statement, and wedon’twant false statements to be provable in Lean.

But contrary to the popular belief, mathematics isn’t set in stone. Mathematics is what you make of it. You can have your own haunted mathematics where2 = 3.

Let’s introduce anaxiomthat says that:

axiom
 math_is_haunted
 :
2
 =
3

Anaxiomis just like atheorem, but taken on faith. You can think of it astheorem math_is_haunted : 2 = 3 := by sorry, but less apologetic.

Now you can use thisaxiomas a fact in other proofs:

theorem
 two_eq_two
 :
2
 =
2
 :=
by

 rfl



axiom
 math_is_haunted
 :
2
 =
3



theorem
 two_eq_three
 :
2
 =
3
 :=
by

 exact math_is_haunted

Note this doesn’t cause any errors!

Here, the goal oftwo_eq_threehappens to be exactly the same as the statement of themath_is_hauntedaxiom, so we’re using theexacttactic to close the goal.

Armed withmath_is_hauntedand some tactics, you can prove even more sinister things. For example, why don’t we prove that2 + 2is actually6:

theorem
 two_eq_two
 :
2
 =
2
 :=
by

 rfl



axiom
 math_is_haunted
 :
2
 =
3



theorem
 two_add_two_eq_six
 :
2
 +
2
 =
6
 :=
by

 -- We'll write something here (this is a comment, btw)

We start with the goal of⊢ 2 + 2 = 6:

We don’t have any tactic that can solve the goal of that specific shape. However, wedohavemath_is_haunted, which is a “proof” that2 = 3. If2is really the same thing as3, then to prove2 + 2 = 6,it should be enoughto prove3 + 3 = 6.

Therewritetactic lets us do just that—rewrite the goal, turning each2into a3:

Westillhave an unsolved goal, but now it’s⊢ 3 + 3 = 6.

Therewritetactic is like a “find and replace” within your goal. If you have a proof thata = b, giving that proof torewritewill rewrite your goal so that allabecomebinstead. Sincemath_is_haunted“proves” that2 = 3,rewrite [math_is_haunted]turns the goal from⊢ 2 + 2 = 6into⊢ 3 + 3 = 6.

And now that our goal is⊢ 3 + 3 = 6, our job is much easier. In fact, therfltactic alone will be enough to closethatgoal and thus to complete the proof:

theorem
 two_eq_two
 :
2
 =
2
 :=
by

 rfl



axiom
 math_is_haunted
 :
2
 =
3



theorem
 two_add_two_eq_six
 :
2
 +
2
 =
6
 :=
by

 rewrite [math_is_haunted]

 rfl

(Here,rflcloses⊢ 3 + 3 = 6, but for a different reason than one might think. It doesn’t really “know” that3 + 3is6. Rather,rflunfolds the definitions on both sides before comparing them. As3,6, and+get unfolded, both sides turn into something likeNat.zero.succ.succ.succ.succ.succ.succ. That’s why it actuallyisasomething = somethingsituation, andrflis able to close it.)

And with that goal closed, we’ve successfully proven2 + 2 = 6.

That’s unsettling! In fact, themath_is_hauntedaxiom is so bad that it lets us derivea contradiction(e.g.2 + 2 = 6and2 + 2 ≠ 6can be proven true at the same time), which, by the laws of logic, means that we can nowprove anything.

In this case, we deliberately addedmath_is_hauntedso it’s kind of our own fault. And yet, an incident like this has actually occurred in the beginning of the 20th century. It was discovered that the Set theory, which much of the mathematics was built upon, had acontradictionflowing from one of its axioms. This was eventually “patched up” by choosing different axioms, but it has caused much anxiety, hair loss, and general soulsearching among the mathematical community.

Let us deleteaxiom math_is_hauntednow. Naturally, this breaks thetwo_add_two_eq_sixproof which depends on the naughty axiom:

Again, that’s good! Broken things should not proof-check.

To fix it up, let’s change the statement to2 + 2 = 4which is actually correct (according to the axioms of natural numbers that Lean is familiar with):

With the bad axiom out, math is no longer haunted! (Or at least we couldhope so.)

It might feel a bit weird being introduced to Lean with “nonsense math” since most math that people do in Lean is usually rather sensible. But I think this is a potent illustration of what working with a proof checker is actually about.

A proof checker only verifies the validity of the logical conclusions stemming from the chosen axioms. It lets you chain logical transformations—withrewrite,rfl,exact, and many other tactics—and prove increasingly sophisticated theorems about increasingly sophisticated mathematical structures.

If your axioms are sound and Lean itself is sound, your conclusions are sound. And that’s true whether your proof is just anrflor millions of lines of Lean code.

### Fermat’s Last Theorem

For an extreme example, considerFermat’s Last Theorem. It says that for anyngreater than 2, no three positive naturalsx,y, andzcan satisfyxⁿ+yⁿ=zⁿ.

import
 Mathlib



theorem
 PNat.pow_add_pow_ne_pow
 (x y z : ℕ+) (n : ℕ) (hn : n >
2
) :

 x^n + y^n ≠ z^n :=
by

 sorry

After over 350 years, it was proven in 1994, and the proof is over 100 pages long.

There is anongoing effortto formalize the proof of this theorem in Lean, and this effort is expected to take many years. Although the statement itself is very simple, the proof will require establishing manymathematical structures and theorems.

If you clone the FLT repo on GitHub and openFermatsLastTheorem.lean, you’ll see a proof but it actually relies onsorrys, as revealed by printing its axioms:

#print
 axioms PNat.pow_add_pow_ne_pow

/-

'PNat.pow_add_pow_ne_pow' depends on axioms: [propext, sorryAx, Classical.choice, Quot.sound]

-/

But when all the sub-proofs are formalized and the project is complete, none of the proofs thatpow_add_pow_ne_powdepends on will havesorrys in them, and#print axioms PNat.pow_add_pow_ne_powwill no longer includesorryAx.

I bet merging the PR that does that will feel satisfying!

### Next Steps

Obviously, we haven’t proven anything useful today. It might seem like a lot of work to figure out something like2 + 2 = 4. And yet, and yet… You know there was something special in there. It felta bitlike programming, but also a bit like something else. If this got you curious about Lean, I can suggest a few resources:

* Start with theNatural Numbers Game. It is a very gentleandfun introduction to Lean. As a bonus, you’ll learn what natural numbers are actually made of.
* The first chapters ofMathematics in Leanare accessible and don’t assume a mathematical background. I found them handy to get comfy with basic tactics.
* My absolute favorite mathematical book, Tao’s Analysis, now has aLean companionthat is beingcontinuously developed and updated on GitHub.
* The “new members” channel on the LeanZulip instanceis very welcoming.

Although I don’t plan to write introductory tutorials (you’re much better served by the Natural Numbers Game and Mathematics in Lean), I’ll probably write more about specific “aha” moments, such as the “2 = 2is actually a type” thing I alluded to earlier. Lean combines a bunch of mindbending ideas from a rich history of mathematicsandprogramming, and I felt a lot of joy rediscovering them. I hope more people will try Lean for no particular reason—it’s justfun.

For a certain type of person, that is.

Pay what you like

Discuss on Bluesky·Edit on GitHub
