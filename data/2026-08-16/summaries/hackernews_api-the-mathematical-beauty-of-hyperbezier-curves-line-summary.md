---
title: The mathematical beauty of hyperbezier curves - Linebender
url: https://linebender.org/blog/hyperbezier/
date: 2026-08-10
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-16T06:02:07.953311
---

# The mathematical beauty of hyperbezier curves - Linebender

# The mathematical beauty of hyperbezier curves

## Overview
- I have long searched for a curve family that improves on cubic Béziers for interactive design.  
- Cubic Béziers remain versatile, especially for regions with large curvature variation, but I seek a family that also handles smooth curvature variation and high‑tension peaks.  
- After discarding many candidates, I propose the **hyperbezier** family, defined by the Cesàro equation  

  \[
  \kappa(s)=\frac{as+b}{(cs^{2}+ds+1)^{1.5}}
  \]

  which mimics Béziers at small angles yet offers smoother, often monotonic curvature and includes several classic analytic curves.

## Approximation of cubic Béziers
- At low endpoint deflection angles the hyperbezier closely matches a cubic Bézier.  
- I provide an interactive tester that maps Bézier control points to hyperbezier parameters; the Bézier appears in gray for reference.  
- For larger angles or longer control handles the fit diverges, but the same control‑handle scheme remains a useful way to set hyperbezier parameters (direct coefficient entry is unintuitive).  
- The current mapping is a draft: arm lengths determine the denominator, then the numerator is solved to align endpoint tangents.  
- Exact mapping is unnecessary in an interactive editor because users can tweak points to achieve the desired shape.

## Exact analytical curves
- Setting \(c=d=0\) yields the Euler spiral, a minimum‑variation curve with monotonic curvature.  
- Setting \(a=0\) gives a perfect circular arc; cubic Béziers can only approximate circles.  
- The family also contains several log‑aesthetic curves with curvature \(\kappa \propto s^{\alpha}\) for exponents \(-3, -2, -1.5, -0.5\) (corresponding to \(\alpha = 1/3, 1/2, 2/3, 2\)).  
  - \(\alpha = 2\) produces the circle involute (its own parallel curve).  
  - \(\alpha = 1/3\) yields the evolute of the Euler spiral.  
- When control points lie on the “double parabola” described in my Euler‑spiral parallel‑curve post, the hyperbezier becomes an exact Euler spiral.

## Superellipses and squircles
- Cubic Béziers can approximate superellipses only up to a point; before reaching a sharp corner they develop extra inflection points.  
- The hyperbezier can reach a sharp corner and visually resembles a superellipse, though for moderate exponents (e.g., 5) a well‑tuned Bézier may be slightly more accurate.  
- I consider the hyperbezier a subtly different squircle—not strictly better or worse than the true superellipse.

## Hyperbola
- Hyperbolas have a rounded turn, curvature that decays, and linear asymptotes—features cubic Béziers fail to capture.  
- The hyperbezier fits hyperbolas naturally and with high accuracy.  
- Both curves share the asymptotic curvature behavior \(\kappa \approx s^{-3}\).  
- Using the small‑angle approximations \(\sin\theta\approx\theta,\ \cos\theta\approx1\) and integrating the even‑symmetric hyperbezier’s Whewell equation reproduces the hyperbola exactly.  
- The name “hyperbezier” reflects this fusion of hyperbola and Bézier, and also alludes to the hypergeometric representation of log‑aesthetic solutions.

## Elastica
- Elastica are the exact solutions to the minimum‑energy (thin‑strip) problem, exhibiting smooth curvature and large tension‑induced variation.  
- They are physically grounded, unlike cubic Béziers.  
- Hyperbeziers approximate elastica reasonably well, offering a decent visual match though not a precise analytical fit—better than Spiro curves, which cannot approximate elastica.

## Some mathematical properties
- Integrating the Cesàro equation yields a Whewell equation  

  \[
  \theta(s)=\frac{a's+b'}{\sqrt{cs^{2}+ds+1}}
  \]

  where the denominator polynomial matches that of the Cesàro form.  
- A second integration provides simple analytical expressions related to trigonometric functions, useful for curve fitting.  
- The integral  

  \[
  \int\frac{as+b}{(cs^{2}+1)^{1.5}}\,ds=\frac{bs-a/c}{\sqrt{cs^{2}+1}}+C
  \]

  shows a pleasing symmetry; its derivative yields a quadratic over \((cs^{2}+ds+1)^{2.5}\).  
- Curvature extrema are found by solving a quadratic; because the denominator is always positive, there can be at most one inflection point at \(s=-b/a\) (if it lies in \([0,1]\)).  
- Consequently, hyperbeziers cannot represent cubic Béziers that have two inflection points, though such Béziers are rare in practical designs.  
- I experimented with other exponents (e.g., 1 instead of 1.5); an exponent of 1 resembles a Padé approximation but fails to represent high‑tension curves stably.