---
title: A proof of the Aaronson-Ambainis conjecture · PSI
url: https://psi.inc/research/aaronson-ambainis
site_name: tldr
content_file: tldr-a-proof-of-the-aaronson-ambainis-conjecture-psi
fetched_at: '2026-11-08T09:03:12.177790'
original_url: https://psi.inc/research/aaronson-ambainis
date: '2026-11-08'
published_date: '2026-11-06'
description: A proof of the Aaronson-Ambainis conjecture about quantum speedups on random inputs, with a complete formalization in Lean.
tags:
- tldr
---

The Aaronson-Ambainis conjecture is now a theorem.

Open since 2008, the conjecture of Scott Aaronson and Andris Ambainis concerns when quantum computers can be exponentially faster than ordinary ones. Now, a research system developed internally at Physical Superintelligence (PSI), running a non-public Anthropic model, found a proof for it, settling one of the most fundamental questions in quantum computing.

In 1994, Peter Shor found a quantum algorithm that factors large numbers far faster than any known method for ordinary computers [1]. It works because the problem hides a repeating pattern, and the quantum computer finds how often it repeats. Like most dramatic quantum speedups known, Shor’s algorithm relies on structure: a promise that the input has a rare pattern.

Whether quantum computers can be exponentially faster on random inputs, which almost never have such structure, was unknown. Aaronson and Ambainis found a way to settle this question using pure mathematics. They stated a conjecture about polynomials and showed that, if it is true, quantum computers are at most polynomially faster on random inputs. Researchers have counted the conjecture among the central open problems of quantum complexity theory [3,4].

At PSI, we found the proof with a research system we developed internally, in a run on our own infrastructure. Instances of a non-public Anthropic model were used in the run. The system had a complete proof of the conjecture during the third day of the run, and Lean, a proof assistant in which a computer checks every step, accepted it. We then set the system to work on related open problems. Along the way, the system improved the result twice, and Lean accepted the final version. The proof builds on ideas of Shachar Lovett and Jiapeng Zhang, of David Reimer and of others [5,6].

In August 2026, Guy Blanc, Jordan Docter, Carmen Strassle and Li-Yang Tan of Stanford University had settled the conjecture’s prediction in a special case, proving that there is no exponential speedup on random inputs for quantum algorithms that look at their input in a fixed number of parallel rounds [7].

They have since been reading our proof of the full conjecture, have sent us comments and are writing a shorter exposition of it for experts. They wrote to us:

“This is a huge result. It resolves a decades-old conjecture with important implications for the nature of problems that admit quantum speedups. The proof draws on and extends several lines of work in the analysis of boolean functions and probabilistic combinatorics. Everything is brought together in a rather magical way.”

Quantum computing still has plenty of mysteries, but now there is one fewer.

## More on the mathematics

Speedups like Shor’s can be measured in looks: how many times a computer has to read its input, a long string of 0s and 1s. With each look, an ordinary computer reads one bit of the string, while a quantum computer’s look can be spread in superposition over many positions. When the string is promised to repeat, as in Shor’s algorithm, a quantum computer needs exponentially fewer looks than any ordinary computer.

Aaronson and Ambainis asked whether a quantum computer can answer a yes-or-no question about a random string with exponentially fewer looks than an ordinary computer. To show that it cannot, it is enough to show that an ordinary computer can imitate the quantum computer without many more looks. The quantum computer says yes with a probability that depends on the string, so imitating it means estimating that probability.

Beals, Buhrman, Cleve, Mosca and de Wolf had shown that afterTlooks, this probability is a polynomial in the bits of the string, of degree at most2T, with values between 0 and 1 [8]. So the ordinary computer has to predict the value of a polynomial of this kind while reading only a few bits of the string. Aaronson and Ambainis stated a conjecture about these polynomials, a statement of pure mathematics, and showed that if it is true, an ordinary computer can make the prediction with few looks.

Now that the conjecture is proven, we know for sure that an ordinary computer can predict the quantum computer’s probability of saying yes, up to a small error, for all but a small fraction of strings. The number of looks the ordinary computer needs grows at most like a fixed power ofT(for any fixed error and fraction), not exponentially. So on yes-or-no questions, a quantum computer cannot save exponentially many looks unless the string has a rare pattern.

The conjecture concerns the influence of a bit: the average change in a polynomial’s value when the bit is flipped from 0 to 1 or vice versa. To picture influence, think of a polynomial as a dial wired to on-off switches, where theith switch is the 0/1 value of theith bit. Each group of at mostdswitches adds its own amount, positive or negative, when all the switches in the group are on (dis the polynomial’s degree). The dial’s reading (the polynomial’s value) always stays between 0 and 1. The quantum computer’s probability of saying yes is one of these dials: the string sets the switches, anddis at most2T.

Letvmeasure how much the dial’s reading varies across settings (the reading’s variance). Aaronson and Ambainis conjectured that flipping some switch moves the reading, on average, by at least a fixed power ofv/d, however many switches there are.

A degree-2 polynomialfon four bits,f(x) =0.1+0.5x4+0.2x1x2+0.1x3. The switches set the input and the needle showsf(x). Each corner of the cube is one of the24=16inputs, shaded by its value off, and flipping a switch moves to a neighboring corner along one of that bit’s edges. The influence of a bit is the change infwhen it is flipped, squared and averaged over all 16 inputs. Bit4’s is much larger than the others’.

input 0000, f = 0.10
0000
input 0001, f = 0.60
0001
input 0010, f = 0.20
0010
input 0011, f = 0.70
0011
input 0100, f = 0.10
0100
input 0101, f = 0.60
0101
input 0110, f = 0.20
0110
input 0111, f = 0.70
0111
input 1000, f = 0.10
1000
input 1001, f = 0.60
1001
input 1010, f = 0.20
1010
input 1011, f = 0.70
1011
input 1100, f = 0.30
1100
input 1101, f = 0.80
1101
input 1110, f = 0.40
1110
input 1111, f = 0.90
1111
bit 
1
bit 
2
bit 
3
bit 
4
bit 
1
0
bit 
2
0
bit 
3
0
bit 
4
0
0
½
1
f(x) = 0.10
influence
bit 
1
bit 
2
bit 
3
bit 
4
Each bar is the average over all 16 inputs. The mark is the squared change at the current input.
New polynomial

The ordinary computer in the method of Aaronson and Ambainis knows how the quantum computer’s dial is wired. The ordinary computer looks at one unseen bit of large influence after another. Once the dial’s reading varies little over the remaining switches, the ordinary computer stops and outputs the average reading as its prediction [2]. The conjecture guarantees that, until the ordinary computer stops, some unseen bit has large influence.

### Bounded polynomials of low degree have influential variables

We prove that if the reading of a dialfis not constant, then some bitihas

Inf
i
(
f
)
≥
c
v
5
/
2
d
6
≥
(
v
/
d
)
7
,

wherec=815/(125π4), about 0.0025, andInfi(f)is the squared change from flipping biti, averaged over all inputs as in the figure.

Earlier bounds for general polynomials decay exponentially in the degree. The earliest bound follows from a theorem of Dinur, Friedgut, Kindler and O’Donnell [9]. For polynomials with values only 0 and 1, the conjecture already followed from theorems of O’Donnell, Saks, Schramm and Servedio and of Nisan and Szegedy [10,11]. Other special cases of the conjecture were proved by Montanaro; by Ivanisvili; by Bansal, Sinha and de Wolf; and by Escudero Gutiérrez, among others [12,13,14,15].

Our proof follows a plan of Shachar Lovett and Jiapeng Zhang [5]. For every level between 0 and 1, the plan looks at the switch settings where the dial’s reading is at or above the level. At every setting, the plan gives each switch a weight, so that flipping any group of switches moves the dial’s reading by at most the total weight of the group. Lovett and Zhang left one inequality of their plan as a conjecture. Our proof replaces the conjectured inequality with a new inequality, proved in the manuscript. To prove the new inequality, we pair up switch settings one to one, and a determinant produces the pairing. David Reimer’s Butterfly Lemma [6] already gives a weaker pairing; our pairing also limits how often paired settings agree on each switch, and the new inequality needs the limit. The proof also uses results of Avantika Agarwal and Shalev Ben-David [16]; Raghav Kulkarni and Avishay Tal [17]; and Yuval Filmus, Hamed Hatami, Nathan Keller and Noam Lifshitz [18].

## Contributions

David Turturean, Member of Technical Staff, led this work: he developed the research system, scoped the problem and ran the system on it, then prompted the model to package the results into a first draft of the paper, reviewed the draft and is responsible for the paper’s correctness. Jim Halverson, Advisor, audited the proof. Phiala Shanahan, Advisor, commented on the Lean formalization.

## References

1. Peter W. Shor, Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer.
2. Scott Aaronson and Andris Ambainis, The Need for Structure in Quantum Speedups.
3. Jiahui Liu, Saachi Mutreja and Henry Yuen, QMA vs. QCMA and Pseudorandomness.
4. Uma Girish, Kunal Mittal, Barak Nehoran and Ran Raz, Distributional Variants of the Aaronson-Ambainis Conjecture.
5. Shachar Lovett and Jiapeng Zhang, Fractional Certificates for Bounded Functions.
6. David Reimer, Proof of the van den Berg-Kesten Conjecture. Combinatorics, Probability and Computing.
7. Guy Blanc, Jordan Docter, Carmen Strassle and Li-Yang Tan, Quantum Speedups Require Structure or Depth.
8. Robert Beals, Harry Buhrman, Richard Cleve, Michele Mosca and Ronald de Wolf, Quantum Lower Bounds by Polynomials.
9. Irit Dinur, Ehud Friedgut, Guy Kindler and Ryan O’Donnell, On the Fourier Tails of Bounded Functions over the Discrete Cube. Israel Journal of Mathematics.
10. Ryan O’Donnell, Michael Saks, Oded Schramm and Rocco A. Servedio, Every Decision Tree Has an Influential Variable.
11. Noam Nisan and Mario Szegedy, On the Degree of Boolean Functions as Real Polynomials. Computational Complexity.
12. Ashley Montanaro, Some Applications of Hypercontractive Inequalities in Quantum Information Theory. Journal of Mathematical Physics.
13. Paata Ivanisvili, Polynomial Growth of Bohnenblust-Hille Constants on the Hamming Cube.
14. Nikhil Bansal, Makrand Sinha and Ronald de Wolf, Influence in Completely Bounded Block-multilinear Forms and Classical Simulation of Quantum Algorithms. Computational Complexity Conference 2022.
15. Francisco Escudero Gutiérrez, Influences of Fourier Completely Bounded Polynomials and Classical Simulation of Quantum Algorithms. Chicago Journal of Theoretical Computer Science.
16. Avantika Agarwal and Shalev Ben-David, Oracle Separations for the Quantum-Classical Polynomial Hierarchy.
17. Raghav Kulkarni and Avishay Tal, On Fractional Block Sensitivity. Chicago Journal of Theoretical Computer Science.
18. Yuval Filmus, Hamed Hatami, Nathan Keller and Noam Lifshitz, On the Sum of the L1 Influences of Bounded Functions. Israel Journal of Mathematics.

← All research