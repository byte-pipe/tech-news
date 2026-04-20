---
title: Category Theory Illustrated - Orders
url: https://abuseofnotation.github.io/category-theory-illustrated/04_order/
site_name: hnrss
content_file: hnrss-category-theory-illustrated-orders
fetched_at: '2026-04-19T06:00:37.268859'
original_url: https://abuseofnotation.github.io/category-theory-illustrated/04_order/
date: '2026-04-18'
description: Category Theory Illustrated – Orders
tags:
- hackernews
- hnrss
---

<

 >

«prev

next»

# Orders

Given a set of objects, there can be numerous criteria, based on which to order them (depending on the objects themselves) — size, weight, age, alphabetical order etc.

However, currently we are not interested in thecriteriathat we can use to order objects, but in thenature of the relationshipsthat define order. Of which there can be several types as well.

Mathematically, the order as a construct is represented (much like a monoid) by two components.

An order is a set of elements, together with abinary relationbetween the elements of the set, which obeys certain laws.

We denote the elements of our set, as usual, like this.

And thebinary relationis a relation between two elements, which is often denoted with an arrow.

As for the laws, they are different depending on the type of order.

## Linear order

Let’s start with an example — the most straightforward type of order that you think of islinear orderi.e. one in which every object has its place depending on every other object. In this case the ordering criteria is completely deterministic and leaves no room for ambiguity in terms of which element comes before which. For example, order of colors, sorted by the length of their light-waves (or by how they appear in the rainbow).

Using set theory, we can represent this order, as well as any other order, as a sets of pairs of the order’s underlying set with itself (a subset of the product set).

And in programming, orders are defined by providing a function which, given two objects, tells us which one of them is “bigger” (comes first) and which one is “smaller”. It isn’t hard to see that this function defines a set of pairs (we are given a pair and we have to say whether or not it belongs to the set).

[1, 3, 2].sort((a, b) => {
 if (a > b) {
 return true
 } else {
 return false
 }
})

However (this is where it gets interesting) not all such functions (and not all sets of pairs) define orders. For such function to really define an order i.e. to have the same output every time, independent of how the objects were shuffled initially, it has to obey several rules.

Incidentally, (or rather not incidentally at all), these rules are nearly equivalent to the mathematical laws that define the criteria of the order relationship i.e. those are the rules that define which element can point to which.

A linear order is a set of elements, together with abinary relationbetween the elements of the set, which obeys the laws of reflexivity, transitivity, antisymmetry, totality.

Let’s check what they are.

### Reflexivity

Let’s get the boring law out of the way — each object has to be bigger or equal to itself, or $a ≤ a$ for all $a$ (the relationship between elements in an order is commonly denoted as $≤$ in formulas, but it can also be represented with an arrow from first object to the second.)

This law only exist to cover the “base case”: we can formulate it the opposite way too and say that each object shouldnothave the relationship to itself, in which case we would have a relation than resemblesbigger than, as opposed tobigger or equal toand a slightly different type of order, sometimes called astrictorder.

### Transitivity

The second law is maybe the least obvious, (but probably the most essential) — it states that if object $a$ is bigger than object $b$, it is automatically bigger than all objects that are smaller than $b$ or $a ≤ b \land b ≤ c \to a ≤ c$.

This is the law that to a large extend defines what an order is: if I am better at playing soccer than my grandmother, then I would also be better at it than my grandmother’s friend, whom she beats, otherwise I wouldn’t really be better than her.

### Antisymmetry

The third law is called antisymmetry. It states that the function that defines the order should not give contradictory results (or in other words you have $x ≤ y$ and $y ≤ x$ only if $x = y$).

It also means that no ties are permitted — either I am better than my grandmother at soccer or she is better at it than me.

### Totality

The last law is calledtotality(orconnexity) and it mandates that all elements that belong to the order should becomparable($a ≤ b \lor b ≤ a$). That is, for any two elements, one would always be “bigger” than the other.

By the way, the law of totality makes the reflexivity law redundant, as reflexivity is just a special case of totality when $a$ and $b$ are one and the same object, but I still want to present it for reasons that will become apparent soon.

Actually, here are the reasons: the law of totality can be removed. Orders, that don’t follow the totality law are calledpartial orders, (and linear orders are also calledtotal orders.)

Task 1:Previously, we covered a relation that is pretty similar to this. Do you remember it? What is the difference?

Task 2:Think about some orders that you know about and figure out whether they are partial or total.

Partial orders are actually much more interesting than linear/total orders. But before we dive into them, let’s say a few things about numbers.

### The order of natural numbers

Natural numbers form a linear order under the operationbigger or equal to(the symbol of which we have been using in our formulas.)

In many ways, natural numbers are the quintessential order — every finite order of objects is isomorphic to a subset of the order of numbers, as we can map the first element of any order to the number $1$, the second one to the number $2$ etc (and we can do the opposite operation as well).

If we think about it, this isomorphism is actually closer to the everyday notion of a linear order, than the one defined by the laws — when most people think of order, they aren’t thinking of atransitive, antisymmetricandtotalrelation, but are rather thinking about criteria based on which they can decide which object comes first, which comes second etc. So it’s important to notice that the two notions are equivalent.

From the fact that any finite order of objects is isomorphic to the natural numbers, it also follows that all linear orders of the same magnitude are isomorphic to one another.

So, the linear order is simple, but it is also (and I think that this isomorphism proves it) the mostboringorder ever, especially when looked from a category-theoretic viewpoint — all finite linear orders (and most infinite ones) are just isomorphic to the natural numbers and so all of their diagrams look the same way.

However, this is not the case with partial orders that we will look into next.

## Partial order

Law of totality does not look so “set in stone” as the rest of the laws i.e. we can probably think of some situations in which it does not apply. For example, if we aim to order all people based on soccer skills there are many ways in which we can rank a person compared to their friends their friend’s friends etc. but there isn’t a way to order groups of people who never played with one another.

Remove the law of totality from the laws of linear orders and we get apartial order(also apartially-ordered set, orposet).

An partial order is a set of elements, together with abinary relationbetween the elements of the set, which obeys the laws of reflexivity, transitivity and antisymmetry.

Every linear order is also a partial order (just as a group is still a monoid), but not the other way around.

We can even create anorder of orders, based on which is more general.

Partial orders are also related to the concept of anequivalence relationsthat we covered in chapter 1, except thatsymmetrylaw is replaced withantisymmetry.

If we revisit the example of the soccer players rank list, we can see that the first version that includes justmyself, mygrandmother and herfriend is a linear order.

However, including thisother person whom none of us played yet, makes the hierarchy non-linear i.e. a partial order.

This is the main difference between partial and total orders — partial orders cannot provide us with a definite answer of the question who is better than who. But sometimes this is what we need — in sports, as well as in other domains, there isn’t always an appropriate way to rate elements linearly.

### Chains

Before, we said that all linear orders can be represented by the same chain-like diagram, we can reverse this statement and say that all diagrams that look something different than the said diagram represent partial orders.

An example of this is a partial order that contains a bunch of linearly-ordered subsets, e.g. in our soccer example we can have separate groups of friends who play together and are ranked with each other, but not with anyone from other groups.

The different linear orders that make up the partial order are calledchains. There are two chains in this diagram $m \to g \to f$ and $d \to o$.

The chains in an order don’t have to be completely disconnected from each other in order for it to be partial. They can be connected as long as the connections are not allone-to-onei.e. ones when the last element from one chain is connected to the first element of the other one (this would effectively unite them into one chain.)

The above set is not linearly-ordered — although we know that $d ≤ g$ and that $f ≤ g$, the relationship between $d$ and $f$ isnotknown — any element can be bigger than the other one.

### Greatest and least objects

Although partial orders don’t give us a definitive answer to “Who is better than who?”, some of them still can give us an answer to the more important question (in sports, as well as in other domains), namely “Who is number one?” i.e. who is the champion, the player who is better than anyone else. Or, more generally, the element that is bigger than all other elements.

Thegreatest elementof an order is an element $a$, such that we have we have $x ≤ a$ for any other element $x$,
Some (not all) partial orders do have such element — in our last diagram $m$ is the greatest element, in this diagram, the green element is the biggest one.

Sometimes we have more than one elements that are bigger than all other elements, in this case none of them is the greatest.

In addition to the greatest element, a partial order may also have a least (smallest) element, which is defined in the same way.

### Joins

Theleast upper boundof two elements that are connected as part of an order is called thejoinof these elements, e.g. the green element is a join of the other two.

The join of $a$ and $b$ is the smallest element $c$ that is bigger than then, formally:

Thejoinof objects $A$ and $B$ is an object $G$, such that:

1. It is bigger than both of these objects, so $A ≤ G$ and $B ≤ G$.
2. It is smaller than any other object that is bigger than them, so for any other object $P$ such that $P ≤ A$ and $P ≤ B$ then we should also have $G ≤ P$.

Given any two elements in which one is bigger than the other (e.g. $a ≤ b$), the join is this bigger element (in this case $b$)

e.g. in a linear orders, thejoinof any two elements is just the bigger element.

Like with the greatest element, if two elements have several upper bounds that are equally big, then none of them is ajoin(a join must be unique).

If, however, one of those elements is established as smaller than the rest of them, it immediately qualifies.

Task 3:Which concept in category theory reminds you of joins?

### Meets

Given two elements, the biggest element that is smaller than both of them is called themeetof these elements.

The same rules as for the joins apply, but in reverse.

### Hasse diagrams

The diagrams that we use in this section are called “Hasse diagrams” and they work much like our usual diagrams, however they have an additional rule that is followed — “bigger” elements are always positioned above smaller ones.

In terms of arrows, the rule means that if you add an arrow to a point, the pointtowhich the arrow points must always be above the onefromwhich it points.

This arrangement allows us to compare any two points by just seeing which one is above the other e.g. we can determine thejoinof two elements, by just identifying the elements that they connect to and see which one is lowest.

### Color-mixing partial order

We all know many examples of total orders (any form of chart or ranking is a total order), but there are probably not so many obvious examples of partial orders that we can think of off the top of our head. So let’s see some. This will gives us some context, and will help us understand what joins are.

To stay true to our form, let’s revisit our color-mixing monoid and create acolor-mixing partial orderin which all colors point to colors that contain them.

If you go through it, you will notice that the join of any two colors is the color that they make up when mixed. Nice, right?

### The partial order of numbers by division

We saw that when we order numbers by “bigger or equal to”, they form a linear order. But numbers can also form a partial order, for example they form a partial order if we order them by which divides which, i.e. if $a$ divides $b$, then $a$ is before $b$ e.g. because $2 \times 5 = 10$, $2$ and $5$ come before $10$ (but $3$, for example, does not come before $10$.)

And it so happens (actually for very good reason) that the join operation again corresponds to an operation that is relevant in the context of the objects — the join of two numbers in this partial order is theirleast common multiple.

And themeet(the opposite of join) of two numbers is theirgreatest common divisor.

### The inclusion partial order

Given a collection of sets containing a combination of a given set of elements…

…we can define what is called theinclusion orderof those sets.

The inclusion order of sets is a binary relation that we can use to order a collection of sets (usually sets that contain some common elements) in which $a$ comes before $b$ if $a$includes$b$, or in other words if $b$ is asubsetof $a$.

In this case thejoinoperation of two sets is theirunion, and themeetoperation is their setintersection.

This diagram might remind you of something — if we take the colors that are contained in each set and mix them into one color, we get the color-blending partial order that we saw earlier.

The order example with the number dividers is also isomorphic to an inclusion order, namely the inclusion order of all possible sets ofprimenumbers, including repeating ones (or alternatively the set of allprime powers). This is confirmed by the fundamental theory of arithmetic, which states that every number can be written as a product of primes in exactly one way.

### Birkhoff’s representation theorem

So far, we saw two different partial orders, one based on color mixing, and one based on number division, that can be represented by the inclusion orders of all possible combinations of sets of somebasic elements(the primary colors in the first case, and the prime numbers (or prime powers) in the second one.) Many other partial orders can be defined in this way. Which ones exactly, is a question that is answered by an amazing result calledBirkhoff’s representation theorem. They are thefinitepartial orders that meet the following two criteria:

1. All elements havejoinsandmeets.
2. Thosemeetandjoinoperationsdistributeover one another, that is if we denote joins as meets as $∨$ or $∧$, then $x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z)$.

The partial orders that meet the first criteria are calledlattices. The ones that meet the second one are calleddistributive lattices. Let’s write that down:

Partial orders in which all elements havejoinsandmeetsis called alattice. A lattice whosemeetandjoinoperationsdistributeover one another is called a distributive lattice.

And the “prime” elements which we use to construct the inclusion order are the elements that are not thejoinof any other elements. They are also calledjoin-irreducibleelements.

So we may phrase the theorem like this:

Each distributive lattice is isomorphic to an inclusion order of itsjoin-irreducibleelements.

By the way, the partial orders that arenotdistributive lattices are also isomorphic to inclusion orders, it is just that they are isomorphic to inclusion orders thatdo not contain all possible combinationsof elements.

## Lattices

We will now talk more aboutlattices(the orders for which Birkhoff’s theorem applies). Lattices are partial orders, in which every two elements have ajoinand ameet. So every lattice is also partial order, but not every partial order is a lattice (we will see even more members of this hierarchy).

Most partial orders that are created based on some sort of rule are distributive lattices, like for example the partial orders from the previous section are also distributive lattices when they are drawn in full, for example the color-mixing order.

Notice that we added the black ball at the top and the white one at the bottom. We did that because otherwise the top three elements wouldn’t have ajoinelement, and the bottom three wouldn’t have ameet.

### Bounded lattices

Our color-mixing lattice, has agreatest element(the black ball) and aleast element(the white one). Lattices that have a least and greatest elements are calledbounded lattices. It isn’t hard to see that all finite lattices are also bounded.

Task 4:Prove that all finite lattices are bounded.

### Order isomorphisms

We mentioned order isomorphisms several times already so this is about time to elaborate on what they are.

Given two sets (we will use partial order of numbers by division and the prime inclusion order as an example) an isomorphism between them is comprised of the following two functions:

1. One function from the prime inclusion order, to the number order (which in this case is just themultiplicationof all the elements in the set)
2. One function from the number order to the prime inclusion order (which is an operation calledprime factorizationof a number, consisting of finding the set of prime numbers that result in that number when multiplied with one another).

An order isomorphism is essentially an isomorphism between the orders’ underlying sets (invertible function). However, besides their underlying sets, orders also have the arrows that connect them, so there is one more condition: in order for an invertible function to constitute an order isomorphism, it has torespect those arrows.

An isomorphism between two orders is an invertible function between their underlying sets, such that applying this function (let’s call it $F$) to any two elements that have a certain order in one set (let’s call them $a$ and $b$) should result in two elements that have a corresponding order in the other set (i.e. $a ≤ b$ if and only if $F(a) ≤ F(b)$).

Such functions are calledorder-preservingfunctions.

## Preorder

In the previous section, we saw how removing the law oftotalityfrom the laws of (linear) order produces a different (and somewhat more interesting) structure, calledpartial order. Now let’s see what will happen if we remove another one of the laws, namely theantisymmetrylaw.

The antisymmetry law mandated that you cannot have an object that is at the same time smaller and bigger than another one. (or that $a ≤ b ⟺ b ≰ a$).

 

Linear order

Partial order

Preorder

Element Comparability

$a ≤ b$ or $b ≤ a$

$a ≤ b$ or $b ≤ a$ or neither

$a ≤ b$ or $b ≤ a$ or neither or both

Reflexivity

X

X

X

Transitivity

X

X

X

Antisymmetry

X

X

-

Totality

X

-

-

The result is a structure called apreorder:

An preorder is a set of elements, together with abinary relationbetween the elements of the set, which obeys the laws of reflexivity and transitivity.

Preorder is not exactly an order in the everyday sense — it can have arrows coming from any point to any other: if a partial order can be used to model who is better than who at soccer, then a preorder can be used to model who has beaten who, either directly (by playing him) or indirectly.

Preorders have just one law —transitivity$a ≤ b \land b ≤ c \to a ≤ c$ (well, two, if we countreflexivity). The part about the indirect wins is a result of this law. Due to it, all indirect wins (ones that are wins not against the player directly, but against someone who had beat them) are added as a direct result of its application, as seen here (we show indirect wins in lighter tone).

And as a result of that, all “circle” relationships (e.g. where you have a weaker player beating a stronger one) result in just a bunch of objects that are all connected to one another.

All of that structure arises naturally from the simple law of transitivity.

### Preorders and equivalence relations

Preorders may be viewed as a middle-ground betweenpartial ordersandequivalence relations, as they are missing exactly the property on which those two structures differ — (anti)symmetry. Because of that, if we have a bunch of objects in a preorder that follow the law ofsymmetry, those objects form an equivalence relation. And if they follow the reverse law ofantisymmetry, they form a partial order.

Equivalence relation

Preorder

Partial order

Reflexivity

Reflexivity

Reflexivity

Transitivity

Transitivity

Transitivity

Symmetry

-

Antisymmetry

In particular, any subset of objects that are connected with one another both ways (like in the example above) follows thesymmetryrequirement. So if we group all elements that have such connection, we would get a bunch of sets, all of which define differentequivalence relationsbased on the preorder, called the preorder’sequivalence classes.

And, even more interestingly, if we transfer the preorder connections between the elements of these sets to connections between the sets themselves, these connections would follow theantisymmetryrequirement, which means that they would form apartial order.

In short, for every preorder, we can define thepartial order of the equivalence classes of this preorder.

## Preorders as categories

We saw that preorders are a powerful concept, so let’s take a deeper look at the law that governs them — the transitivity law. What this law tells us that if we have two pairs of relationship $a ≤ b$ and $b ≤ c$, then we automatically have a third one $a ≤ c$.

In other words, the transitivity law tells us that the $≤$ relationship composes i.e. if we view the “bigger than” relationship as a morphism we would see that the law of transitivity is actually the categorical definition ofcomposition.

(we have to also verify that the relation is associative, but that’s easy)

So, we suspect that preorders are categories, but is it really so? Let’s review the definition of a category again.

A category is a collection ofobjects(we can think of them as points) andmorphisms(arrows) that go from one object to another, where:

1. Each object has to have the identity morphism.
2. There should be a way to compose two morphisms with an appropriate type signature into a third one in a way that is associative.

Looks like we have law number 2 covered, with transitivity. What about the identity law? We have it too, under the namereflexivity.

So it’s official — preorders are categories (sounds kinda obvious, especially after we also saw that preorders can be reduced to sets and functions using the inclusion order, and sets and functions form a category in their own right).

Preorders are special types of categories (all preorders are categories, but not all categories are preorders). Most categories have many different morphisms between given two objects. For example, in the category of sets where there are potentially infinite amount of functions from, say, the set of integers and the set of boolean values, as well as a lot of functions that go the other way around.

Whereas preorders, two object, whereas haveat most one morphism, that is, we either have $a ≤ b$ or we do not.

So, like a monoid is a category that has one object, an order is a category that has at most onemorphismbetween two objects.

An interesting fact that follows from the fact that the they have at most one morphism between given two objects is that in preordersall diagrams commute.

Task 6:Prove this.

### Partial orders and total orders as categories

We said that partial orders and total orders are preorders. This means that they are categories as well.

Preorders in particular are what is known in category theory asskeletalcategories — categories in which there are no isomorphic objects i.e. in which all isomorphic objects are identical.

And total orders I guess we don’t have a specific “categorical” name for them, but they are a certain type of categories as well.

### Products and coproducts

While we are rehashing diagrams from the previous chapters, let’s look at the diagram defining thecoproductof two objects in a category, from chapter 2.

If you recall, this is an operation that corresponds toset inclusionin the category of sets.

But wait, wasn’t there some other operation that that corresponded to set inclusion? Oh yes, thejoinoperation in orders. And not merely that, but joins in orders are defined in the exact same way as the categorical coproducts.

The coproduct of $A$ and $B$, denoted $A + B$, is an object, such that:

1. There exists two “projection” morphisms $A \to A + B$ and $B \to A + B$.
2. For any impostor coproduct $I$, that also has such projection morphisms ($A \to I$ and $B \to I$), there must also exist a unique morphism with the type signature $g: A + B \to I$, that converts the real coproduct to the impostor, such that the projections of the impostor would be just the composition of $g$ with the projections of the product.

In the realm of orders, we define join as:

Thejoinof objects $A$ and $B$ is an object $G$, such that:

1. It is bigger than both of these objects, so $A ≤ G$ and $B ≤ G$.
2. It is smaller than any other object that is bigger than them, so for any other object $P$ such that $P ≤ A$ and $P ≤ B$ then we should also have $G ≤ P$.

We can see that the two definitions, and their corresponding diagrams, are basically the same, we just replaced “bigger” with “has a unique morphism” (because in orders all morphisms are unique).

Speaking in category-theoretic terms, we can say that:

Thecategorical coproductin thecategory of preordersis thejoinoperation.

Which of course means thatproductscorrespond tomeets(duality).

### Formal definition

In category-theoretic terms, orders (categories that have at most one morphism with a given type signature) are known as “thin” categories.

A preorder, any preorder, can be seen as a category with at most one morphism between two given objects — if one object is bigger then there is a morphism between them. The converse is also true: any category with at most one morphism between two given objects can be seen as a preorder (called also athincategory).

Thin categories are often used for exploring categorical concepts in a context that is easier to understand than in normal (non-thin) categories. For example, as we saw, understanding theorder-theoreticconcepts of meets and joins would help you better understand themore general categoricalconcepts of products and coproducts.

Thin categories are also helpful in contexts when we want to keep it simple and we aren’t particularly interested in the differences between the morphisms that go from one object to another. We will see an example of that in the next chapter.

«prev

next»
