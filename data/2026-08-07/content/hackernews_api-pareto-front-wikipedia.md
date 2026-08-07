---
title: Pareto front - Wikipedia
url: https://en.wikipedia.org/wiki/Pareto_front
site_name: hackernews_api
content_file: hackernews_api-pareto-front-wikipedia
fetched_at: '2026-08-07T11:44:01.967075'
original_url: https://en.wikipedia.org/wiki/Pareto_front
author: binyu
date: '2026-07-29'
description: Pareto Front
tags:
- hackernews
- trending
---

From Wikipedia, the free encyclopedia

Set of all Pareto efficient situations

Inmulti-objective optimization, thePareto front(also calledPareto frontierorPareto curve) is the set of allPareto efficientsolutions.[1]Colloquially, this means when there are many distinct objectives to consider in anoptimization problem, a Pareto front represents the set of solutions where no solution outperforms any other solution in the set at every objective, and every solution not in the set is outperformed by at least one solution in the Pareto front in every objective.[2]The concept is widely used inengineering.[3]:111–148It allows the designer to restrict attention to the set of efficient choices, and to maketradeoffswithin this set, rather than considering the full range of every parameter.[4]:63–65[5]:399–412

Example of a Pareto frontier. The boxed points represent feasible choices, and smaller values are preferred to larger ones. Point 
C
 is not on the Pareto frontier because it is dominated by both point 
A
 and point 
B
. Points 
A
 and 
B
 are not strictly dominated by any other, and hence lie on the frontier.

A 
production-possibility frontier
. The red line is an example of a Pareto-efficient frontier, where the frontier and the area left and below it are a continuous set of choices. The red points on the frontier are examples of Pareto-optimal choices of production. Points off the frontier, such as N and K, are not Pareto-efficient, since there exist points on the frontier which Pareto-dominate them.

## Definition

[
edit
]

The Pareto frontier,P(Y), may be more formally described as follows. Consider a system with functionf:X→Rm{\displaystyle f:X\rightarrow \mathbb {R} ^{m}}, whereXis acompact setof feasible decisions in themetric spaceRn{\displaystyle \mathbb {R} ^{n}}, andYis the feasible set of criterion vectors inRm{\displaystyle \mathbb {R} ^{m}}, such thatY={y∈Rm:y=f(x),x∈X}{\displaystyle Y=\{y\in \mathbb {R} ^{m}:\;y=f(x),x\in X\;\}}.

We assume that the preferred directions of criteria values are known. A pointy′′∈Rm{\displaystyle y^{\prime \prime }\in \mathbb {R} ^{m}}is preferred to (strictly dominates) another pointy′∈Rm{\displaystyle y^{\prime }\in \mathbb {R} ^{m}}, written asy′′≻y′{\displaystyle y^{\prime \prime }\succ y^{\prime }}. The Pareto frontier is thus written as:

P

(

Y

)

=

{

y

′

∈

Y

:

{

y

′

′

∈

Y

:

y

′

′

≻

y

′

,

y

′

≠

y

′

′

}

=

∅

}

.

{\displaystyle P(Y)=\{y^{\prime }\in Y:\;\{y^{\prime \prime }\in Y:\;y^{\prime \prime }\succ y^{\prime },y^{\prime }\neq y^{\prime \prime }\;\}=\emptyset \}.}

## Marginal rate of substitution

[
edit
]

A significant aspect of the Pareto frontier in economics is that, at a Pareto-efficient allocation, themarginal rate of substitutionis the same for all consumers.[6]A formal statement can be derived by considering a system withmconsumers andngoods, and a utility function of each consumer aszi=fi(xi){\displaystyle z_{i}=f^{i}(x^{i})}wherexi=(x1i,x2i,…,xni){\displaystyle x^{i}=(x_{1}^{i},x_{2}^{i},\ldots ,x_{n}^{i})}is the vector of goods, both for alli. The feasibility constraint is∑i=1mxji=bj{\displaystyle \sum _{i=1}^{m}x_{j}^{i}=b_{j}}forj=1,…,n{\displaystyle j=1,\ldots ,n}. To find the Pareto optimal allocation, we maximize theLagrangian:

Li((xjk)k,j,(λk)k,(μj)j)=fi(xi)+∑k=2mλk(zk−fk(xk))+∑j=1nμj(bj−∑k=1mxjk){\displaystyle L_{i}((x_{j}^{k})_{k,j},(\lambda _{k})_{k},(\mu _{j})_{j})=f^{i}(x^{i})+\sum _{k=2}^{m}\lambda _{k}(z_{k}-f^{k}(x^{k}))+\sum _{j=1}^{n}\mu _{j}\left(b_{j}-\sum _{k=1}^{m}x_{j}^{k}\right)}

where(λk)k{\displaystyle (\lambda _{k})_{k}}and(μj)j{\displaystyle (\mu _{j})_{j}}are the vectors of multipliers. Taking thepartial derivativeof the Lagrangian with respect to each goodxjk{\displaystyle x_{j}^{k}}forj=1,…,n{\displaystyle j=1,\ldots ,n}andk=1,…,m{\displaystyle k=1,\ldots ,m}gives the following system of first-order conditions:

∂

L

i

∂

x

j

i

=

f

x

j

i

1

−

μ

j

=

0

 for 

j

=

1

,

…

,

n

,

{\displaystyle {\frac {\partial L_{i}}{\partial x_{j}^{i}}}=f_{x_{j}^{i}}^{1}-\mu _{j}=0{\text{ for }}j=1,\ldots ,n,}

∂

L

i

∂

x

j

k

=

−

λ

k

f

x

j

k

i

−

μ

j

=

0

 for 

k

=

2

,

…

,

m

 and 

j

=

1

,

…

,

n

,

{\displaystyle {\frac {\partial L_{i}}{\partial x_{j}^{k}}}=-\lambda _{k}f_{x_{j}^{k}}^{i}-\mu _{j}=0{\text{ for }}k=2,\ldots ,m{\text{ and }}j=1,\ldots ,n,}

wherefxji{\displaystyle f_{x_{j}^{i}}}denotes the partial derivative off{\displaystyle f}with respect toxji{\displaystyle x_{j}^{i}}. Now, fix anyk≠i{\displaystyle k\neq i}andj,s∈{1,…,n}{\displaystyle j,s\in \{1,\ldots ,n\}}. The above first-order condition imply that

f

x

j

i

i

f

x

s

i

i

=

μ

j

μ

s

=

f

x

j

k

k

f

x

s

k

k

.

{\displaystyle {\frac {f_{x_{j}^{i}}^{i}}{f_{x_{s}^{i}}^{i}}}={\frac {\mu _{j}}{\mu _{s}}}={\frac {f_{x_{j}^{k}}^{k}}{f_{x_{s}^{k}}^{k}}}.}

Thus, in a Pareto-optimal allocation, the marginal rate of substitution must be the same for all consumers.[7]

## Computation

[
edit
]

Algorithmsfor computing the Pareto frontier of afinite setof alternatives have been studied incomputer scienceand power engineering.[8]They include:

* "Themaxima of a point set"
* "The maximum vector problem" or theskyline query[9][10][11]
* "The scalarization algorithm" or the method of weighted sums[12][13]
* "Theϵ{\displaystyle \epsilon }-constraints method"[14][15][16]
* Multi-objective Evolutionary Algorithms[17][18]

## Approximations

[
edit
]

Since generating the entire Pareto front is often computationally-hard, there are algorithms for computing an approximate Pareto-front. For example, Legriel et al.[19]call a setSanε-approximationof the Pareto-frontP, if the directedHausdorff distancebetweenSandPis at mostε. They observe that anε-approximation of any Pareto frontPinddimensions can be found using (1/ε)dqueries.

Zitzler, Knowles and Thiele[20]compare several algorithms for Pareto-set approximations on various criteria, such as invariance to scaling, monotonicity, and computational complexity.

## References

[
edit
]

1. ↑proximedia."Pareto Front".www.cenaero.be. Archived fromthe originalon 2020-02-26. Retrieved2018-10-08.
2. ↑Kang, Shida; Li, Kaiwen; Wang, Rui (2025-06-01)."A survey on pareto front learning for multi-objective optimization".Journal of Membrane Computing.7(2):128–134.doi:10.1007/s41965-024-00170-z.ISSN2523-8914.
3. ↑Goodarzi, E., Ziaei, M., & Hosseinipour, E. Z.,Introduction to Optimization Analysis in Hydrosystem Engineering(Berlin/Heidelberg:Springer, 2014),pp. 111–148.
4. ↑Jahan, A., Edwards, K. L., & Bahraminasab, M.,Multi-criteria Decision Analysis, 2nd ed. (Amsterdam:Elsevier, 2013),pp. 63–65.
5. ↑Costa, N. R., & Lourenço, J. A., "Exploring Pareto Frontiers in the Response Surface Methodology", in G.-C. Yang, S.-I. Ao, & L. Gelman, eds.,Transactions on Engineering Technologies: World Congress on Engineering 2014(Berlin/Heidelberg: Springer, 2015),pp. 399–412.
6. ↑Just, Richard E. (2004).The welfare economics of public policy: a practical approach to project and policy evaluation. Hueth, Darrell L., Schmitz, Andrew. Cheltenham, UK: E. Elgar. pp.18–21.ISBN1-84542-157-4.OCLC58538348.
7. ↑Just, Richard E.; Hueth, Darrell L.; Schmitz, Andrew (2005-01-01).The Welfare Economics of Public Policy: A Practical Approach to Project and Policy Evaluation. Edward Elgar Publishing.ISBN978-1-84542-157-1.
8. ↑Tomoiagă, Bogdan; Chindriş, Mircea; Sumper, Andreas; Sudria-Andreu, Antoni; Villafafila-Robles, Roberto (2013)."Pareto Optimal Reconfiguration of Power Distribution Systems Using a Genetic Algorithm Based on NSGA-II".Energies.6(3):1439–55.doi:10.3390/en6031439.hdl:2117/18257.
9. ↑Nielsen, Frank (1996). "Output-sensitive peeling of convex and maximal layers".Information Processing Letters.59(5):255–9.CiteSeerX10.1.1.259.1042.doi:10.1016/0020-0190(96)00116-0.
10. ↑Kung, H. T.; Luccio, F.; Preparata, F.P. (1975)."On finding the maxima of a set of vectors".Journal of the ACM.22(4):469–76.doi:10.1145/321906.321910.S2CID2698043.
11. ↑Godfrey, P.; Shipley, R.; Gryz, J. (2006). "Algorithms and Analyses for Maximal Vector Computation".VLDB Journal.16:5–28.CiteSeerX10.1.1.73.6344.doi:10.1007/s00778-006-0029-7.S2CID7374749.
12. ↑Kim, I. Y.; de Weck, O. L. (2005). "Adaptive weighted sum method for multiobjective optimization: a new method for Pareto front generation".Structural and Multidisciplinary Optimization.31(2):105–116.doi:10.1007/s00158-005-0557-6.ISSN1615-147X.S2CID18237050.
13. ↑Marler, R. Timothy; Arora, Jasbir S. (2009). "The weighted sum method for multi-objective optimization: new insights".Structural and Multidisciplinary Optimization.41(6):853–862.doi:10.1007/s00158-009-0460-7.ISSN1615-147X.S2CID122325484.
14. ↑"On a Bicriterion Formulation of the Problems of Integrated System Identification and System Optimization".IEEE Transactions on Systems, Man, and Cybernetics. SMC-1 (3):296–297. 1971.doi:10.1109/TSMC.1971.4308298.ISSN0018-9472.
15. ↑Mavrotas, George (2009). "Effective implementation of the ε-constraint method in Multi-Objective Mathematical Programming problems".Applied Mathematics and Computation.213(2):455–465.doi:10.1016/j.amc.2009.03.037.ISSN0096-3003.
16. ↑Carvalho, Iago A.; Coco, Amadeu A. (September 2023). "On solving bi-objective constrained minimum spanning tree problems".Journal of Global Optimization.87(1):301–323.doi:10.1007/s10898-023-01295-8.
17. ↑Zhang, Qingfu; Hui, Li (December 2007). "MOEA/D: A Multiobjective Evolutionary Algorithm Based on Decomposition".IEEE Transactions on Evolutionary Computation.11(6):712–731.doi:10.1109/TEVC.2007.892759.
18. ↑Carvalho, Iago A.; Ribeiro, Marco A. (November 2019). "A node-depth phylogenetic-based artificial immune system for multi-objective Network Design Problems".Swarm and Evolutionary Computation.50100491.doi:10.1016/j.swevo.2019.01.007.
19. ↑Legriel, Julien; Le Guernic, Colas; Cotton, Scott; Maler, Oded (2010). "Approximating the Pareto Front of Multi-criteria Optimization Problems". In Esparza, Javier; Majumdar, Rupak (eds.).Tools and Algorithms for the Construction and Analysis of Systems. Lecture Notes in Computer Science. Vol.6015. Berlin, Heidelberg: Springer. pp.69–83.doi:10.1007/978-3-642-12002-2_6.ISBN978-3-642-12002-2.
20. ↑Zitzler, Eckart; Knowles, Joshua; Thiele, Lothar (2008),"Quality Assessment of Pareto Set Approximations", in Branke, Jürgen; Deb, Kalyanmoy; Miettinen, Kaisa; Słowiński, Roman (eds.),Multiobjective Optimization: Interactive and Evolutionary Approaches, Lecture Notes in Computer Science, Berlin, Heidelberg: Springer, pp.373–404,doi:10.1007/978-3-540-88908-3_14,ISBN978-3-540-88908-3, retrieved2021-10-08

Retrieved from "
https://en.wikipedia.org/w/index.php?title=Pareto_front&oldid=1365854598
"

Categories
: 
* Power engineering
* Pareto efficiency
Hidden categories: 
* Articles with short description
* Short description is different from Wikidata
* CS1: long volume value