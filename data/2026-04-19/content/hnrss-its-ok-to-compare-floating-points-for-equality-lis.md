---
title: It's OK to compare floating-points for equality | lisyarus blog
url: https://lisyarus.github.io/blog/posts/its-ok-to-compare-floating-points-for-equality.html
site_name: hnrss
content_file: hnrss-its-ok-to-compare-floating-points-for-equality-lis
fetched_at: '2026-04-19T06:00:38.608054'
original_url: https://lisyarus.github.io/blog/posts/its-ok-to-compare-floating-points-for-equality.html
date: '2026-04-14'
description: It's OK to compare floating-points for equality
tags:
- hackernews
- hnrss
---

It's OK to compare floating-points for equality

2026 Apr 14

NB: The title of this post is an intentional clickbait. Even though I do stand for its statement, a more honest one would be something like: It's NOT OK to compare floating-points using epsilons.

You've probably heard the mantra that you must never compare floating-point numbers for exact equality, and you absolutely must use some kind of epsilon-comparison instead, like

bool approxEqual(float x, float y)
{
 return abs(x - y) < 1e-4f;
}

Over the 15+ years that I've been writing code, – which often deals with geometry, graphics, physics, simulations, etc, and thus has to work with floating-points on a daily basis, – I've encountered only one or two cases where such epsilon-comparison is actually a good solution. Pretty much always there is a better solution that either involves rewriting the code in some way, or simply compares floating-points just likex == y. And pretty much always the epsilon solution was actually one of theworstpossible options.

I'll show a bunch of examples where adding some kind of epsilon might be your first instinct, but actually a much better – and often much simpler – solution exists. But first, let's talk about floating-point numbers.

## Contents

## Floating-points are not a black box

The whole idea of epsilon-comparison seems to come from the general perception of floating-point numbers as some kind of random black-box machine that sometimes produces inexact results because the gods of computing force it to. In reality it is a pretty deterministic (modulo compiler options, CPU flags, etc) andhighly standardizedsystem.

Floating-point numbers are necessarily inexact in that they cannot represent all possible real numbers. In fact, no finite amount of memory can, because that's how maths works – there are justway too manyreal numbers (or even just rational numbers, fwiw). Given that we probably only want to allocate a fixed (and not just a finite) amount of bits per such a number, we're forced to accept that only a finite set of numbers will be representable (specifically, at most \(2^{bits}\) of them), and for all others we'll have to deal with approximations.

I don't want this to turn into a lecture on how floating-point numbers are represented, though; I thinkwikipediadoes a good enough job. For a more in-depth source, seethis classicby David Goldberg, orthis more recent onethat follows the same idea. What's more important is that this "inexactness" of floating-point numbers doesn't mean some "uncertainty" or "randomness" in its behavior!

For example, any single arithmetic operation (e.g. addition, multiplication, etc) on two floating-point numbers is required to produce a floating-point number which is the closest to the actual true answer if we treat the inputs as being exact (there are some rounding rules in case of ties, i.e. when two representable numbers are equally close to the true answer). Notice that, even though the result is approximate, it is still guaranteed to be as close to the truth as possible, and is very much deterministic.

However, it does mean that our usual mathematical formulas don't always hold for floating-points. For example, even though addition (and multiplication) are guaranteed to becommutative(\(a + b = b + a\)), they aren't necessarilyassociative: it may happen that \((a+b)+c\neq a+(b+c)\). It's fairly easy to find such examples;here's onethat works for 32-bit floating-points:

// Outputs 0.89999998
std::cout << std::setprecision(8) << ((0.2f + 0.3f) + 0.4f) << '\n';

// Outputs 0.90000004
std::cout << std::setprecision(8) << (0.2f + (0.3f + 0.4f)) << '\n';

Notice that, even though the expressions aren't equal, they are very close (the difference is about 6e-8), and the floating-point standard has some guarantees that we can use topredicthow large the difference can be.

So, what's the problem, then? We know that the result of some computation is only approximate, and we compare it with some expected result approximately, sounds about right.

Or does it?

## Problems with epsilons

I have 3 major problems with those epsilon-comparisons:

1. They are a hacky, temporary solution,
2. They often cascade into extremely hard-to-debug issues, and
3. They often don't solve the initial problem.

The second point is probably the toughest. One part of the program treats 2D points as equal if they are separated inManhattan distanceby no more than 1e-4, another part of the program treats points as equal if they are separated in L-inf distance (max of coordinates) by no more than 1e-6, the input points themselves are generated using some other algorithm, and now all the input-output invariants are messed up, and your line rendering is broken but only in this specific scenario, with this specific data, only at night and in full moon. Good luck debugging that.

A rare wrong case of line rendering isn't that much of an issue, but it can manifest in a ton of other ways, up to crashing the program, and can be really nasty when combined with a lot of other geometric code. I've encountered many such cases, and mismatched epsilon comparisons were an extremely common root cause.

The problem is that these epsilons are pretty much always simplyguessed, and there is no correct way to choose one epsilon out of many. If you have several such comparisons, no combination of epsilons will ensure that everything works correctly.

Another problem with epsilons is that such comparison isn'ttransitive. This might sound like a technical nitpick, but in reality most algorithms assume that things like comparisons are in fact transitive, and these algorithms can simply break (produce nonsense or even crash) if you use a non-transitive comparison with them.

So, what should we do, then? We need tothinkabout the problem! Shocking, I know. Why are we comparing floating-points in the first place? Maybe we don't trust our algorithms? Maybe we don't trust the data? Maybe we don't trust the CPU? There's no single answer, so let's look at some examples.

## Case in study: grid-based movement

Say, you have a turn-based game where units move on a grid. A unit has some movement points and can do several moves per turn, but for UX sake you only allow executing the next move after the previous one finished.

Now, you're probably interpolating the unit's position somehow and not just teleporting it to the target grid cell, so you need to check when exactly the move is finished before allowing the player to select the next move target.

You could just wait for a certain amount of time (and that would be a perfectly good solution in many cases!), but different units have different animations and thus different timings, there are some accessibility settings to reduce animations, etc, so you decide that relying on animation time isn't a good idea.

Then you realize that the move finishes exactly when the position of the unit coincides with the target cell's center. You write something like

void update() {
 if (selectedUnit.position != targetCell.center)
 return;

 // Do the frame update
}

and after the move was executed, nothing happens and the game effectively hangs, because the conditionselectedUnit.position != targetCell.centeris never true. With a typical linear interpolation with easing, the code

vec2f getPosition(float time) {
 return lerp(start, end, easing(time));
}

will produce enough floating-point roundings that the result will never be equal toendwhentime == 1.f. Heck, insome interpolation schemesit's not even supposed to be ever true!

Damn, stupid floating-points! — you grumble as you add the holy grail of floating-points — an epsilon-comparison:

void update() {
 if (distance(selectedUnit.position, targetCell.center) > 1e-4)
 return;

 // Do the frame update
}

This solves the issue, so why is this so bad? For a number of reasons:

* The specific epsilon of1e-4might break if you decide to choose a different interpolation scheme
* As always with epsilons, someone reading the code will get confused and suspicious
* Making the player wait is one of the worst things you can do

So, how do we solve this? One option is to use some sort of acceptance radius: once the unit is within, say,0.25of the target cell's center, we stop the animation and allow the player to issue the next commands. Then, we find the actually good value by a lot of testing.

How is this different from epsilons? It isn't really, except that now it's at least backed by something instead of being a random value. The real problem here is mixing thedata modelwith itspresentation. The internal doings of the game's state machine shouldn't care about where some 3D model is located. That's usually harder than it seems (which is roughly why UX is even a thing), but very much doable.

In this case, the best solution (in my opinion!) is to allow the user to issue commands without waiting for the unit to complete its movement in the first place. Once a user clicks on some grid cell, the rendering gets notified that a movement must take place, while the internal model of the game's state thinks that the unit is already on the next cell.

There are many ways to implement that, e.g. by queuing the requested animations and playing them one-by-one, or using ananimation/interpolation schemethat is robust against sudden changes in the target value. What's important is that it is very doable, relatively straightforward, and doesn't require epsilons.

## Case in study: spherical linear interpolation

Spherical linear interpolationis a way to interpolate points on a sphere (aka unit vectors) in such a way that the interpolated vector follows a curve with a fixed rotation speed. A simplenormalize(lerp(a, b, t))won't cut it — the resulting vector moves slower near the ends and faster in the middle. Here's acool visualizationof slerp. Quite often this function is only implemented for quaternions, but it's useful for any vectors of any dimension (though in case of quaternions it differs a bit because \(q\) and \(-q\) represent the same rotation).

Quite conveniently, if the input vectors are normalized, it boils down to a pretty straightforward formula:

vec3 slerp(vec3 a, vec3 b, float t) {
 float angle = acos(dot(a, b));
 return (sin((1 - t) * angle) * a + sin(t * angle) * b) / sin(angle);
}

Now, from time to time this code will produceNaNs, for a couple of reasons:

* Even if the vectors are normalized, their dot product can produce values outside of the \([-1, 1]\) range, andacoswill returnNaN
* When the input vectors are very close,anglecan become zero, and division of zero by zero will once again produceNaN

The first problem is easy to deal with: just wrapacosargument inclamp:

vec3 slerp(vec3 a, vec3 b, float t) {
 float angle = acos(clamp(dot(a, b), -1.f, 1.f));
 return (sin((1 - t) * angle) * a + sin(t * angle) * b) / sin(angle);
}

The second problem is more subtle. Thankfully, when theangleis small enough, spherical linear interpolation turns into usual linear interpolation, so we can detect this case and switch to usuallerp(a, b, t)instead. But how small is small enough?

It's tempting to just throw some epsilon here, like

vec3 slerp(vec3 a, vec3 b, float t) {
 float angle = acos(dot(a, b));
 if (angle < 1e-4) {
 return lerp(a, b, t);
 }
 return (sin((1 - t) * angle) * a + sin(t * angle) * b) / sin(angle);
}

However, this makes the code less precise than it could be, even if the resulting vector is still close to what we expect it to be. And, once again, a random epsilon always raises the question of how this exact value was chosen. We can do better!

BothglmandEigenuse a reasonable check:vec3 slerp(vec3 a, vec3 b, float t) {
 float d = dot(a, b);
 if (d > 1.f - FLT_EPSILON) {
 return lerp(a, b, t);
 }
 float angle = acos(dot(a, b));
 return (sin((1 - t) * angle) * a + sin(t * angle) * b) / sin(angle);
}Here,FLT_EPSILONis exactly \(2^{-23}\) — the smallest single-precision floating-point value \(x\) such that \(1 + x \neq x\) (using floating-point addition). Honestly, it doens't feel much better than a random epsilon to me — throwingFLT_EPSILONdoesn't solve our issues unless we've proved that this is the exact threshold that works in our case.Let's analyze the code. The main problem is thatanglebeing zero causesNaN's. The secondary problem is thatanglebeing too small might introduce precision errors.Let's think about precision first.angleisn't just an arbitrary number — it's the result of callingacos, and we're worried about the case when the argument toacosis close to 1. In fact, theangleitself is somewhat irrelevant, as we mostly care anoutsin(angle), not the angle itself.Now, \(\sin(\operatorname{acos}(x))\) is just \(\sqrt{1-x^2}\). In our case,x = dot(a, b). When \(x = 1 - \varepsilon\), we have\[ \sin(\operatorname{acos}(x)) = \sqrt{1-x^2} = \sqrt{1-(1-\varepsilon)^2} = \sqrt{2\varepsilon-\varepsilon^2} \approx \sqrt{2\varepsilon} \]The \(\varepsilon^2\) term is too small to care about, and \(\sqrt 2\) is just a constant close to 1. The main thing here is \(\sqrt{\varepsilon}\): even if \(\varepsilon\) is something as small asFLT_EPSILON, thesin(angle)term will be something like the square root of it. For small numbers, square root increases the number significantly. For example, whileFLT_EPSILONis around1.2e-07, its square root is around3.5e-04, i.e. about 2000 times larger.All I'm trying to say here is: in the case we care about, the argument toacosis close to 1, so the difference between possible representable values of the argument toacosis a much more serious source of precision problems compared to the angle itself being close to zero.Actually, the smallest value less than 1 that is representable in floating-point is not1 - FLT_EPSILON, but1 - FLT_EPSILON / 2.f, which somewhat supports my argument that theFLT_EPSILONconstant was chosen somewhat arbitrarily here.So, unless we want something special, we can ignore that the angle can be small in terms of precision, and focus on obtainingNaN. In this code, provided that the arguments are finite values, the only way to get aNaNis with division by zero, which can occur only when theangleis zero, which can occur only whendot(a, b) >= 1. As we've discussed, the next smallest representable value ofdot(a, b)is1 - FLT_EPSILON / 2.f, with theanglebeing roughlysqrt(FLT_EPSILON), which is around3.5e-04— a rather large floating-point value considering that the whole range is about[1e-38 .. 1e38], so we can be sure that even a half-decent implementation ofacoswouldn't return zero in this case.Thus, in casedot(a, b) < 1, we're actually fine! The only thing to check is ifdot(a, b) == 1, or, combining with theclampwe added earlier, ifdot(a, b) >= 1:vec3 slerp(vec3 a, vec3 b, float t) {
 float d = dot(a, b);
 if (d >= 1.f) {
 return lerp(a, b, t);
 }
 float angle = acos(dot(a, b));
 return (sin((1 - t) * angle) * a + sin(t * angle) * b) / sin(angle);
}(Note that I've intentionally left out the case when the dot product is close to \(-1\): in that case, there's no unique solution to the interpolation problem, and it's better dealt with separately.)Alternatively, we can checksin(angle)directly, though this means we can't save on the expensiveacoscall in the corner case:vec3 slerp(vec3 a, vec3 b, float t) {
 float angle = acos(clamp(dot(a, b), -1.f, 1.f));
 float s = sin(angle);
 if (s == 0.f) {
 return lerp(a, b, t);
 }
 return (sin((1 - t) * angle) * a + sin(t * angle) * b) / s;
}## Case in study: computing vector lengthYou wouldn't be surprised if I told you that computing the (Euclidean) length of a vector is a fairly common and useful operation. The implementation is rather straightforward:float length(vec3 v) {
 return sqrt(dot(v, v));
}or, if we inline thedotcall,float length(vec3 v) {
 return sqrt(v.x * v.x + v.y * v.y + v.z * v.z);
}You've probably seen this a dozen times, so what's wrong with it? Nothing really, except that for really small vectors (those having length around1e-19) it returns zero, and for larger vectors we get a significant precision loss. Even if the result is a perfectly valid floating-point value, its square (i.e. the expression under the square root) can be too small to be adequately representable in floating-point.So what? There are hardly any use cases when such a vector is indistinguishable from zero anyway. However, an invariant saying that only the zero vector has zero length would be extremely convenient, and would simplify writing code in a lot of cases, especially when we want to treat floating-points carefully.There's actually a very simple way to do that: compute the maximumMof the absolute values of vector coordinates, then returnM * length(v / M). Thanks to floating-point guarantees, one of the coordinates will be at least 1, so the expression under the square root is at least 1, and at most \(D\) — the dimension (3 in case ofvec3).So, the code turns intofloat length(vec3 v) {
 float M = max(abs(v.x), abs(v.y), abs(v.z));
 vec3 u = v / M;
 return M * sqrt(u.x * u.x + u.y * u.y + u.z * u.z);
}That'sabout twice as manyassembly instructions, but unless this happens in a hot loop, I'd say it's worth the extra precision and safety.The only problem is that if the vector is zero (yes, literally zero, not just small), this function returnsNaN! However, if at least one of the vector's coordinates is non-zero (even if it is a subnormal value),Mwill be strictly larger than zero, and the algorithm will work correctly (and never with less precision than the naive version). So, the correct fix is literally comparingMto zero:float length(vec3 v) {
 float M = max(abs(v.x), abs(v.y), abs(v.z));
 if (M == 0.f) return 0.f;
 vec3 u = v / M;
 return M * sqrt(u.x * u.x + u.y * u.y + u.z * u.z);
}If we'd writeif (M < 1e-4)instead, we'd basically destroy the reason this function exists in the first place.## Case in study: solving linear systemsYou wouldn't be surprised if I told you that solving linear systems of equations is a fairly common and useful operation. Half of physics & engineering problems boil down to solving some linear systems (the other half being eigenvalue equations).For a general non-sparse system, there's basically the only standard way to solve it: the Gauss-Jordan elimination.(Actually, we can also use QR decomposition — afaik it's slower but more numerically stable.)The general algorithm is rather long, but not too complicated — it's just a bunch offorloops and some arithmetics on the coefficients of the system.What's important is that the algorithm can berather unstable: at some point you take top-left entry of the remaining part of the matrix, and divide the whole row with that entry. If it was small, the floating-point errors from cancellation are amplified, and if it is zero, you getNaN's.However, the algorithm becomes stable in practice (the instabilities are extremely rare and typically theoretical) if instead we do something calledpartial pivoting: find the row with the largest (in absolute value) coefficient in the current column, and use that row instead of the original top row. It complicates the algorithm somewhat, but makes it very much usable in practice.The only problem is that we're still dividing, and potentially dividing by something very small or even zero! There isn't some clever way to escape this: a matrix can besingular, in which case maths tells us that there's no solution at all.So, first of all our routine should return anoptional<vector>, and secondly we need to check for this division:optional<vector> solve(matrix const& m, vector const& v) {
 // Gaussian elimitation code...

 for (int i = 0; i < m.columns(); ++i) {

 // Find maximum m[j][i] among all remaining rows
 float M = 0.f;
 for (int j = i; j < m.rows(); ++j)
 M = max(M, abs(m[j][i]));

 if (M < 1e-4)
 return std::nullopt;

 // Proceed with the algorithm
 }
}Now, obviously this1e-4comes from nowhere — a classic epsilon placed simply to make the problem shut up instead of solving it.For some systems that are close to being singular, our algorithm will report that it failed, based on a pretty much arbitrary threshold. Even worse, thisMvalue we computed isn't some inherent property of the matrix, but simply an intermediate value we obtained with our algorithm.This threshold should absolutely be at least provided by the user themselves (maybe with a default parameter), but that's still rather quiestionable. Proper ways of checking whether a matrix is singular or close to singular is computing itscondition numberor inspecting itssingular values, not setting an arbitrary threshold on an arbitrary intermediate value!My point is: it's not our job to figure out how singular the matrix is, it's the user's job. Our job, as implementors of the Gauss-Jordan elimination algorithm, is to provide an answer that is as good as we can get, or report that we failed otherwise. The only way our code can truly fail is by dividing zero by zero — everything else will give some reasonable answer, even if very imprecise (depending on the matrix).So, in my opinion, the correct code would be just// ...

 if (M == 0.f)
 return std::nullopt;

 // ...To be honest, this still doesn't prevent us from dividing something large by something small and getting infinities, — but no epsilon protects against that either.## Case in study: ray-box intersectionWhenever you're making a raytracer (voxel or otherwise), or implementing object picking by mouse, or doing any of a million other things, you'll need a ray-box intersection routine.The algorithm itself is pretty straightforward: you compute the time (i.e. the parameter \(t\) along the ray \(o+t\cdot d\)) when the ray enters the box and the time it leaves the box. If the former is less than the latter, that's your intersection. You compute the enter time as the maximum of enter times along each of the coordinates; similarly, the leave time is the minimum along each of the coordinates.This scratchapixel articleexplains it quite well. The code looks roughly like this:void sort(float & x, float & y) {
 if (x > y) swap(x, y);
}

pair<float, float> intersect(ray r, box b) {
 float txmin = (b.min.x - r.origin.x) / r.direction.x;
 float txmax = (b.max.x - r.origin.x) / r.direction.x;
 float tymin = (b.min.y - r.origin.y) / r.direction.y;
 float tymax = (b.max.y - r.origin.y) / r.direction.y;
 float tzmin = (b.min.z - r.origin.z) / r.direction.z;
 float tzmax = (b.max.z - r.origin.z) / r.direction.z;

 sort(txmin, txmax);
 sort(tymin, tymax);
 sort(tzmin, tzmax);

 float tmax = min(txmax, min(tymax, tzmax));
 float tmin = max(txmin, min(tymin, tzmin));

 return {tmin, tmax};
}NB: if werewritesorta bit, we can force it to useminss/maxssSSE instructions, thus making theintersectfunction branchless.It's a pretty short, readable function, and in 99.99% of cases it works perfectly. Yet, once in a while you'll end up with a ray that hasdirection.xequal to zero, thus the divide will give infinities orNaN's. Oops!So, let's add some epsilons, right? No. First of all, what are you going to do ifabs(direction.x) < 1e-4? You still need to add some code that finds the intersection properly but doesn't divide bydirection.x, and it might just work without epsilons anyway.Let's analyze the code! What happens ifdirection.x == 0? The ray is parallel to the YZ plane, so the real intersection happens there. But we can't just ignore the X coordinate: if the ray starts outside the[b.min.x, b.max.x]interval, there's no intersection, otherwise we need to inspect the Y and Z coordinates.What happens exactly whendirection.x == 0? When you divideA / direction.x, it returns \(-\infty\) ifA < 0and \(\infty\) ifA > 0. In our case,Aisb.min.x - r.origin.xorb.max.x - r.origin.x. So, if the ray originr.origin.xis inside the interval[b.min.x, b.max.x], we'll gettxmin == -INFandtxmax == INF. If the ray origin is outside of this interval, bothtxminandtxmaxwill both be either-INForINF.If there is an intersection and the origin is within the interval, the calculation oftminwill effectively ignore the value oftxmin == -INF, because it's always true thatmax(-INF, x) == x. Similarly,tmaxwill effectively ignoretxmax == INF. In this case, the code will just compute the correct intersection in the YZ plane, as required.If, however, the origin is not within the interval, eithertxmin == txmax == INF, leading totmin == INFbuttmaxbeing some finite value, leading to no intersection (becausetmin > tmax), ortxmin == txmax == -INF, leading totmax == -INFbuttminbeing some finite value, leading to no intersection again.All this is to say that our code actuallyworks correctlyin casedirection.x == 0! No epsilons needed, it already handles the infinities exactly as it should. Or does it?We've forgotten that in IEEE754 there are two zeros: a positive+0and a negative-0one. Dividing by the negative zero produces infinity, but also flips the sign! So, we can get a case whentxmin == INFandtxmax == -INF, leading to no intersection being reported even if there is one.Thankfully, oursort(txmin, txmax)call solves this issue, swapping these into the case oftxmin == -INFandtxmax == INF! So, once again, our code already works correctly in this case.The Scratch-a-pixel link above also discusses a solution to this problem, which has a whole ton of if's making it not branchless but also able to do an early-out.Actually, there's one more case we didn't fix yet: if bothr.direction.x == 0andr.origin.x == b.min.x, we'll get zero divided by zero, i.e. aNaN. Unfortunately, our code doesn't automatically solve this:NaNcompared to anything always returnsfalse, so, depending on howsort,minandmaxare implemented, we might end up withtminortmaxbeingNaN, which effectively means no intersection. This might be OK for your use-case, but I don't know a simple way to fix that if we want this to be reported as a true intersection. We could just check ifr.direction.x == 0 && r.origin.x == b.min.xand settmin = -INFin this case, but the code stops being branchless. This happens extremely rarely in practice, though, so we might just get away with it :)## Case in study: computing convex hullMost 2D convex hull algorithms eventually boil down to checking whether, for three points \(A, B, C\), the last point \(C\) lies to the left of the ray \(AB\). Equivalently, it asks whether when moving from \(A\) to \(B\) and then turning to move from \(B\) to \(C\), you make a left turn or a right turn. This is why this predicate is often calledleft_turn.It boils down to checking the relative orientation of two vectors \(AB\) and \(AC\), and can be computed by a simple determinant:float det(vec2 a, vec2 b) {
 return a.x * b.y - a.y * b.x;
}

bool left_turn(vec2 a, vec2 b, vec2 c) {
 return det(b - a, c - a) > 0.f;
}It's pretty cool that you can put all your floating-point stuff inside this predicate — the convex hull algorithm itself doesn't care about the coordinates and can operate just as an abstract algorithm, provided you have thisleft_turnpredicate as some kind of a black box.However, it turns out that most of computational geometry algorithms are extremely sensitive to edge cases, and can completely break if such an edge case breaks certain invariants of this algorithm.For theleft_turnpredicate, one such invariant is that it doesn't change when we cycle the points:left_turn(A,B,C) == left_turn(B,C,A) == left_turn(C,A,B)It's pretty easy to find three pointsalmoston the same line that break this invariant. It happens so often that any convex hull algorithm that is supposed to handle at least some 1000 points must take this into account.We know the solution, right? — just slap an epsilon here:bool left_turn(vec2 a, vec2 b, vec2 c) {
 return det(b - a, c - a) > 1e-4f;
}Well, of course it doesn't work. Floating-point errors can easily lead to this predicate violating the cyclic invariant above.There are many ways of solving this problem:Round the input values to some fixed grid, then work with integers insteadUsearbitrary precisionrational arithmetic to get the true resultUse CPU-rounding-flags-backedinterval arithmeticto compute the result; resort to arbitrary precision if it failsKnowing exact IEEE754 rounding rules, compute an upper bound on the possible error, compare with the naive result, and return if the error is smaller than the result; otherwise, use any of the more precise methodsUse some variation of the2Sumalgorithm to compute the result; use any of the more precise methods if it failsOf all these, the first option (round to a fixed grid) is probably the simplest and the most practical. However, there are cases when you can't do that, and you need to work with the unperturbed input data, and you need more complex methods. In any case, no epsilons will save you — sooner or later your algorithm will return nonsense, or will simply crash.Note that, in any case, such a predicate is better thought of as returning three possible values: left, right, and collinear (or -1, 0, and 1, if you're feeling '90s). This is very similar tothree-way comparison.## Case in study: sanitizing user inputThe last two cases will be the ones where I think epsilons are actually a good solution!Say, you're writing some geometry visualization library, or maybe some cartographic engine of sorts. The user supplies you with a polyline that you can't control. You task is to perform some computations on it, and maybe to render it.Now, rendering polylines is a pretty complicated topic; in particular, we typically triangulate the polyline using various types ofjoinsand caps. And to compute these, we need various things like the normal to a particular line segment, or the angle between two consecutive line segments. And, of course, everything breaks if two consecutive line points are equal or simply too close — normal & angle calculations go way off, introducing ugly artifacts to our lovely line.Now, we could say that consecutive equal points are not allowed, which would be a reasonable requirement for some library or algorithm, but not so much for a user-facing engine/framework. After all, filtering out equal points is easy — literally a single call tostd::unique. But what are we going to do with points that are just too close, but not equal?Mathematically, having points too close to each other isn't an issue — they should lead to some very thin triangles in the output, but they won't break the topology of the resulting mesh. However, in practice we lack the floating-point precision to accurately compute these thin triangles (which is what leads to ugly artifacts). On the other hand, this time our goal is not to compute something as precise as we can, but to visualize the data. In practice, nobody will see these thin triangles, simply because they're too thin.Which is to say it's OK if we simply don't render them. Meaning it's OK if we dont even generate them. Meaning it's OK if we just filter out the input points that are too close. But how close is too close?Once again, slapping an arbitrary epsilon is usually a bad solution, though in this specific case it's probably not bad, but just meh. There are ways to find a good epsilon that fits this specific use case:Knowing your maximal scale/zoom and pixel size, compute the distance which will map to less than half a pixel, and use that as an epsilon for filtering out pointsKnowing what exactly your algorithm does, and where the imprecision comes from, estimate the minimum separation between points that leads to acceptable floating-point errors, and use it as your epsilonUse a binary search to find a good epsilon by testing it against your dataset of input dataUse your decades of floating-point experience to just guess a good epsilon (but don't forget to document this)Unless you chose the last option, I can guarantee you that the correct value won't be1e-4or1e-6.## Case in study: writing test casesThat's probably the most obvious one. If I'm writing a maths library, I want extensive test coverage. Tests will have to check if some function returns the value we expected, meaning it will have to compare the result with some reference value. But due to floating-point errors, the result will almost always differ.Now, there are two ways we can do this. Option 1 is to assume exact IEEE754 conformance and write tests using equality comparisons. Even if there's some rounding involved, it must be the same on all conformant hardware (if the CPU flags are set correctly), so you can safely do the equality test. In many cases you can craft input data such that no rounding will be involved altogether!In many functions (e.g. vector addition, subtraction, multiplication) you can just use integer coordinates (many of which are exactly representable as floats), or integers divided by a power of 2. For some cases it isn't enough: for example, when computing vector length, even if the coordinates are integers, the result might be an irrational number.Even in this case we can cheat a bit and usePythagorean triplesto craft test cases where the length is known to be exactly representable in floating-point, for examplelength(vec2(3.f, 4.f)) == 5.f
length(vec2(5.f, 12.f)) == 13.f
length(vec2(0.4375f, 1.5f)) == 1.5625fThis is rather tiresome, as we'll have to craft special increasingly complicated tests for all our code. What's option 2, then?Use epsilons! Be sure to use rather small epsilons, e.g.FLT_EPSILONor like, but it's honestly a good solution for this case. For the most part, it's very hard to break a maths library in such a way that epsilon-comparisons won't catch that.However, note that if some of your functions provide additional guarantees (likelengthonly being zero for a vector which is exactly zero, orleft_turnbeing invariant under cycling the arguments), it's best to write separate specialized tests for these guarantees.## To epsilon or not to epsilonSo, are epsilons good or bad? Usually bad, but sometimes okay. Is all your epsilon-driven code gonna break suddenly, now that you've read this post? Probably not.Look, in many real-life use-cases all that doesn't matter. If you're writing a general-purpose high-quality maths library, you're obliged to care about this stuff. If you're goofying a toy physics engine for a squishy platformer game, epsilons will probably suit you well. And if they break, just replace1e-4with2e-4and be on your way.The real answer to any engineering problem is not to follow a cult or a random internet person, but to think with your own brain. Shocking, I know. Nevertheless, I hope you learnt something!