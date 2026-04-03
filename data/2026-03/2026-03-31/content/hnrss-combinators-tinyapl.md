---
title: Combinators - TinyAPL
url: https://tinyapl.rubenverg.com/docs/info/combinators
site_name: hnrss
content_file: hnrss-combinators-tinyapl
fetched_at: '2026-03-31T19:26:53.527375'
original_url: https://tinyapl.rubenverg.com/docs/info/combinators
date: '2026-03-31'
description: Combinators
tags:
- hackernews
- hnrss
---

# Combinators

A combinator is a function or operator that only refers to its arguments and operands without modifying them in any way.

Symbol
APL expression
Bird
(1)
TinyAPL
Diagram

I

\mathrm I

I
y
Identity
⊣
/
⊢

K

\mathrm K

K
x
Kestrel
⊣

κ

\kappa

κ
y
Kite
⊢

W

\mathrm W

W
y F y
Warbler
⍨

C

\mathrm C

C
y F x
Cardinal
⍨

B

\mathrm B

B
F (G y)
Bluebird
∘
/
⍤
/
⍥

Q

\mathrm Q

Q
G (F y)
Queer
⍛

B

1

{\mathrm B}_1

B
1
​
F (x G y)
Blackbird
⍤

Ψ

\Psi

Ψ
(G x) F (G y)
Psi
⍥

S

\mathrm S

S
y F (G y)
Starling
⟜
/
⇽

Σ

\Sigma

Σ
(F y) G y
Violet Starling
⊸
/
⇾

D

\mathrm D

D
x F (G y)
Dove
∘
/
⟜

Δ

\Delta

Δ
(F x) G y
Zebra Dove
⍛
/
⊸

Φ

\Phi

Φ
(F y) G (H y)
Phoenix
«»

Φ

1

\Phi_1

Φ
1
​
(x F y) G (x H y)
Pheasant
«»

D

2

{\mathrm D}_2

D
2
​
(F x) G (H y)
Dovekie
⊸
 + 
⟜

P

\mathrm P

P
(y G x) F (x G y)
Parrot
(2)
⸚

N

\mathrm N

N
x F (x G y)
Eastern Nicator
⇽

ν

\mathrm \nu

ν
(x F y) G y
Western Nicator
⇾

Additionally, some other primitives have combinator-like behavior:

APL expression
TinyAPL
Diagram
n
⍨
n
⍨
F y
⁖
x G y
⁖

## Footnotes

1. Some combinators have bird names, originating fromTo Mock a Mockingbirdby Raymond Smullyan. Some of the bird names are taken from theUiua combinator page.
2. I made this one up.