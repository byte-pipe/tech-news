---
title: Infleqtion 30 Logical Qubits Rely on Error Detection
url: https://postquantum.com/industry-news/infleqtion-30-logical-qubits
site_name: tldr
content_file: tldr-infleqtion-30-logical-qubits-rely-on-error-detecti
fetched_at: '2026-09-27T15:32:33.581651'
original_url: https://postquantum.com/industry-news/infleqtion-30-logical-qubits
author: Marin Ivezic
date: '2026-09-27'
published_date: '2026-09-27T07:30:58+02:00'
description: Infleqtion ran 30 logical qubits in 80 atoms on Sqale using a distance-2 code that detects errors. What the result shows, and what it leaves open.
tags:
- tldr
---

## Table of Contents

September 24, 2026–Infleqtion(NYSE: INFQ) said it had entangled 30 logical qubits encoded in 80 atoms on its Sqale neutral-atom quantum computer, meeting the logical-qubit target it had set for 2026. The companyannounced the resultat Quantum World Congress 2026 and said the experiments were completed in August.

Infleqtion buildsneutral-atomquantum computers, optical clocks and quantum sensors. Its shares began trading on the New York Stock Exchange in February after itcompleted a business combinationwith Churchill Capital Corp X. The company said the new result made it the first neutral-atom quantum computing company to reach 30 logical qubits on a commercial system.

In atechnical post, Chief Technology Officer Pranav Gokhale said the team grouped the 80 atoms into 10 blocks of eight. Each block was prepared in the logical zero state of the distance-3 [[8,3,3]] code and then operated in the distance-2 [[8,3,2]] code, which Infleqtion said can detect any error or correct for a lost atom. Each block encodes three logical qubits.

The test was an instantaneous quantum polynomial (IQP) circuit whose entangling gates, four logical controlled-controlled-Z (CCZ) gates among them, connected all 30 logical qubits. Infleqtion said the circuit placed all 30 in a single coherent state. The company said the circuit used 136 physical two-qubit gates and about 1,000 physical operations in total, an amount it called one KiloQuOp.

Of the more than one billion possible 30-bit outputs, the ideal circuit produces 262,144, or one in 4,096. Infleqtion reported that about 25% of its measured outputs fell inside that set, roughly 1,000 times the rate that uniformly random outputs would achieve.

The company said OpenAI’sGPT-5.6 Solmodel helped its researchers find a logical entangling operation, which it calls a double-CZ because it applies two logical controlled-Z (CZ) gates at once, that uses four physical two-qubit gates. Infleqtion said that, to its knowledge, the only mechanism previously known for that entanglement was a transversal controlled-NOT (CNOT), which needs eight. The company also said that reconstructing results for blocks that lost a single atom, a technique it calls loss correction, quadrupled the number of good shots, meaning outputs that fall in the ideal set, at the cost of higher error rates.

Chief Executive Matt Kinsella said co-design of hardware and software made the demonstration possible with 80 physical qubits and that the company is developing applications with customers. Infleqtion said three customers run logical-qubit circuits on Sqale, including the Wellcome Leap Quantum for Bio program.

The company reportedtwo logical qubitsin 2024 and12in 2025. It said it remains on track for 100 logical qubits in 2028 and 1,000 by 2030. Gokhale wrote that a full paper with experimental methods, resource counts and statistical analysis will follow in the coming weeks. He added that the team’s priorities include real-time control and mid-circuit measurement to move beyond post-selection, the practice of keeping only the runs in which no error was detected.

## My Analysis

On September 15 I wrote that Infleqtion hadcompiled a quantum low-density parity-check (qLDPC) code with NVIDIA’s CUDA-Q Logicalbut had not yet run it on hardware. Nine days later the company has a hardware result. Infleqtion built it from a different and much smaller code, blocks of eight atoms, and discarded every run in which an error was detected.

Infleqtion delivered the logical-qubit count it promised for 2026, on schedule. The code has distance 2, which guarantees that a single error is flagged but not that it can be corrected. The 2026 target that the result meets replaced an earlier Infleqtion target that specified error correction.

Infleqtion has shown it can hit the dates on its roadmap. A fault-tolerant machine needs codes that correct errors during a computation. Running those codes normally requires mid-circuit measurement and real-time control, and Infleqtion still lists both among its next priorities.

### What a distance-2 code detects and cannot correct

In alogical qubit, the information of a single qubit is encoded across several physical qubits so that errors on individual qubits can be found and, with enough redundancy, corrected. The protection aquantum error-correcting codegives depends on its distance. A distance-2 code is guaranteed to detect any single physical error but not to correct one. A code needs a distance of at least 3 to guarantee the correction of any single error. Codes with higher distances correct more errors.

The [[8,3,2]] code,catalogued in the Error Correction Zoo, places eight atoms at the corners of a cube and stores three logical qubits in them. The code is lopsided. A logical bit flip requires physical errors on four atoms and a logical phase flip on only two, so a single bit flip could in principle be corrected while a single phase flip can only be detected. In IQP sampling on codes of this kind, the final measurements give both the logical output and the code’s parity checks. Infleqtion discards the runs that fail a check. Atom loss is handled separately. When an atom leaves its trap, imaging shows which one is gone, and Infleqtion reconstructs the missing measurement from the parity of the other seven. Microsoft and Atom Computing drew the same line in their2024 logical-computation paper, using distance-2 codes to correct qubit loss and a distance-3 code to correct other errors.

Discarding runs works for small circuits. Each added gate adds a chance of a flagged error, so the share of runs that survive falls as circuits grow. Researchers at the University of Southern California described the trade in aMarch 2026 analysis of the same code. In accepted runs, logical errors are suppressed to second order in the physical error rate, while the acceptance rate falls at first order. Gokhale lists real-time control and mid-circuit measurement as the route beyond post-selection. With them, a machine can measureerror syndromesduring a computation and decode them in time to act on the result.

### Infleqtion’s original 2026 target was error-corrected logical qubits

Infleqtion published its computing roadmap in February 2024 and revised it in September 2025, both times in its own releases.

* February 2024.In itsfive-year roadmap, Infleqtion set a goal of fault-tolerant quantum computers within five years and described a fully error-corrected machine with 100 logical qubits able to run circuits more than a million layers deep.Quantum Computing Report’s accountof the roadmap put more than 10 logical qubits in 2026.
* September 2025.Infleqtionreported 12 logical qubitswith error detection and loss correction, and said this put it ahead of its previous target of “10 logical qubits with error correction in 2026.” It set a new 2026 target of 30 logical qubits and a 2030 target of a fault-tolerant system with more than 1,000.
* March 2026.OnCiti’s research podcast, Kinsella described logical qubits as “error-corrected clusters of physical qubits” and named very strong error-correction codes as one of their three ingredients. He placed the first useful applications at around 100 logical qubits, at the end of 2028. Theregistration statementInfleqtion filed with the SEC on March 31 pairs 100 logical qubits by 2028 with a target of one million sequential logical operations in the same year.
* September 2026.The 30 logical qubits delivered this week run in a distance-2 code with post-selection.

Across those statements, the count rose from 10 to 30 while the requirement behind it changed from correction to detection. This week Infleqtion restated the 2028 target of 100 logical qubits with neither the error-correction condition nor the million-operation target it set out for investors in March.

Quantinuum, Microsoft and the Harvard-led team have all built and reported error-detected logical qubits. Quantinuum split itsHelios countinto 94 error-detected logical qubits and 48 error-corrected ones. Infleqtion gives 30 logical qubits in its press release and leaves the distinction to Gokhale’s post. A company that has traded publicly since February, and whose chief executive defines logical qubits as error-corrected, should say in its headline which kind it is counting.

### Harvard ran the same code and circuit type at 48 logical qubits in 2023

In December 2023, Dolev Bluvstein, Mikhail Lukin and colleagues at Harvard, MIT and QuErareported a logical processorthat ran IQP sampling circuits on [[8,3,2]] blocks with up to 48 logical qubits. Those circuits used up to 228 logical two-qubit gates and up to 48 logical CCZ gates. The encoded circuits scored higher at cross-entropy benchmarking than the same circuits on physical qubits. Dominik Hangleiter and colleaguesworked out the theoryfor compiling this family of circuits with the code’s transversal gates, including how cross-entropy scores relate to fidelity. Icovered the Harvard paperin detail.

Gokhale cites the Harvard work for the transversal CCZ. Infleqtion ran a smaller experiment of the same kind on different hardware, with 30 logical qubits and four CCZ gates, on a commercial machine that combines atom motion with individually addressed gates so that selected atoms can be entangled where they are. According to QuEra, the Harvard-led team went further in 2025,running algorithms on up to 96 logical qubitswith error rates that fell as the system grew, on a448-atom processor.

Infleqtion’s claim to be first needs both of its qualifiers, a neutral-atom company and a commercial system. Atom Computing and Microsoft entangled 24 logical qubits using 48 atoms on Atom’s hardware in November 2024. They also ran the Bernstein-Vazirani algorithm on 28 logical qubits using 112 atoms. In anIEEE Spectrum articlepublished in December 2025, QuEra’s chief commercial officer, Yuval Boger, said the company’s machine at Japan’s AIST had around 37 logical qubits, depending on implementation. Outside neutral atoms, Quantinuum entangled 94 error-detected logical qubits on Helios in a Greenberger-Horne-Zeilinger (GHZ) state at94.9% fidelityand ran 48 error-corrected ones. This month Quantinuum demonstrated logical memory and Clifford computation without post-selection with itsHelix architecture.

The 80-atom figure follows from the code. Distance-2 codes are economical with qubits. Atom Computing and Microsoft used two atoms per logical qubit for their GHZ state. Quantinuum reported 94 logical qubits from its 98 ions. The [[8,3,2]] code needs eight atoms for three logical qubits, the highest ratio of the three, and Infleqtion chose it, as Gokhale explains, for its transversal CCZ gate.

### What the 25% hit fraction measures

A 30-bit output can take more than a billion values, and the ideal circuit produces only 262,144 of them, one in 4,096. Random output would fall in that set 0.024% of the time. Infleqtion measured about 25%. In itspress release, which it alsofiled with the SEC, the company describes that result as a signal “approximately 1000x stronger than underlying noise.” The factor of 1,000 compares the hit fraction with random guessing, and by Infleqtion’s own figure three of every four outputs in its dataset fell outside the set that the ideal circuit can produce. Interesting Engineeringrepeated the press-release linein its coverage.

The hit fraction is the share of outputs that fall inside the allowed set. Outputs inside the set can appear with the wrong probabilities and still count as hits. Cross-entropy benchmarking scores each output by its ideal probability, and the Harvard team used it for these circuits. At 30 qubits, the full quantum state fits in the memory of one large GPU, so the ideal outputs can be computed exactly on classical hardware. Gokhale presents computation beyond classical simulation as the goal for larger demonstrations.

GHZ states allow a direct test of entanglement. A GHZ state with fidelity above 50% is certified to have genuine multipartite entanglement, which means it cannot be split into independent groups of qubits. Atom Computing and Microsoft’s 24-logical-qubit GHZ state had a10.2% error rateafter errors and losses were detected, and Quantinuum’s 94-logical-qubit GHZ state reached 94.9% fidelity. In 2024 members of the Microsoft and Atom teamtold GeekWirethat Harvard’s 48-logical-qubit sampling circuit would not have cleared the 50% threshold. Infleqtion can settle the same question for its 30 logical qubits by publishing an entanglement witness.

Infleqtion has not published an acceptance rate after post-selection or a comparison with the same circuit run on unencoded atoms. Nor has it said whether the 25% was measured before or after loss correction, which Infleqtion says quadrupled the good shots at a higher error rate. Quantinuum reportedpost-selection ratesalongside its Helios logical-qubit counts, and Gokhale says Infleqtion’s paper will include statistical analysis.

### Three different quantities called quops

Gokhale uses one KiloQuOp to mean about 1,000 physical operations. In the same post he describes Infleqtion’s ambition to reach the MegaQuOp era, which he defines as roughly a million reliable logical operations. That second definition matches themegaquopJohn Preskill described in hisQ2B 2024 keynote, and QuEra uses it forLibra, its 2028 machine with more than 256 error-corrected logical qubits and a logical error rate of 10⁻⁶, as Icovered in June.

Counted in logical operations, the 30-qubit circuit is a fraction of its physical size. The double-CZ uses two physical CZs for each logical CZ. A logical CCZ in this code uses eight physical rotations.

Sandia’sQUOPS benchmark, which Ianalysed on September 10, is a third quantity, a benchmark-circuit size that includes routing and error-correction costs in one score. Quantinuum’s Helios-1 scored 1,504 on physical qubits and 40 on Steane-code logical qubits. The Sandia authors projected that a fault-tolerant architecture encoding 20–30 logical qubits in 1,000–5,000 physical qubits could comfortably exceed 10⁴ on their benchmark, the score they treat as the practical ceiling for physical qubits. The 80 physical qubits Infleqtion used for its 30 logical qubits are 1.6–8% of that range, and most of the difference is due to code distance.

### The double-CZ gate found with GPT-5.6 Sol is correct

In the usual basis for the [[8,3,2]] code, each logical qubit’s X operator acts on one face of the cube and each logical Z operator on one edge, asHonciuc Menendez, Ray and Vasmerlay out. The standard way to entangle two blocks is a transversal CNOT, eight physical CNOTs between matching atoms that apply three logical CNOTs in parallel.

Infleqtion’s double-CZ applies CZ gates between matching atoms on one face of each cube, four gates in all. I checked the stabilizer algebra. The four gates preserve both codes. Applied on the face where logical qubit 1’s X operator acts, they produce two logical CZs. One acts on qubit 2 of the first block and qubit 3 of the second. The other acts on qubit 3 of the first block and qubit 2 of the second. The same CZ applied to all eight pairs of atoms does nothing to the logical qubits. With all eight pairs, every logical X operator picks up a Z-type stabilizer of the other block. On a single face, two of those pickups become logical Z operators, and those two terms are the signatures of the two logical CZs.

As with the transversal CNOT, each physical gate acts on one atom per block, so a single faulty gate leaves at most one error in each block, and the code detects it. Infleqtion says the double-CZ improved the yield and fidelity of its circuits. Gokhale does not say how many double-CZs the circuit used.

Infleqtion qualifies its novelty claim with “to our knowledge,” and it has not described how it used GPT-5.6 Sol. The [[8,3,2]] code has been studied since 2016, and its gate set appears in the Harvard compilation paper and in the USC analysis of the same code from March, among others. The identity takes a few lines of stabilizer algebra to verify. Infleqtion’s paper should cite that literature and say whether the double-CZ appears in it.

### What Infleqtion demonstrated on Sqale

Infleqtion’s logical-qubit counts have arrived on or ahead of the dates it published, with two in 2024, 12 in 2025 against a 2026 target of 10, and 30 in 2026. On Sqale, Infleqtion combines atom motion, for connectivity, with individually addressed gates applied to atoms where they are, and it prepared and entangled the full 30-qubit state with 136 physical two-qubit gates. The four CCZ gates are non-Clifford operations, the class a universal quantum computer needs. In most larger codes, such gates are produced withmagic states. The Harvard team ran 48 of them in 2023, and Infleqtion has now run four on its own hardware. With loss correction, a customer can keep runs in which one atom per block was lost and trade error rate for throughput, as Atom Computing and Microsoft also did in 2024.

Gokhale names the code, the distance, the gate counts, the benchmark, the post-selection and the Harvard precedent in his post, and most of the numbers in this analysis come from it. The press release differs from the post on these points. Infleqtion’s release mentions neither the distance nor the post-selection and restates the benchmark as signal over noise. It also calls the experiment proof that neutral atoms are the fastest path to fault tolerance, a ranking that no 30-qubit, distance-2 experiment can establish.

### What the paper and the 2028 target need to state

Infleqtion’s promised paper should report:

* The share of runs kept after post-selection, with and without loss correction
* The same circuit run on unencoded atoms, for a logical-versus-physical comparison
* Cross-entropy or fidelity estimates with uncertainties, plus an entanglement witness if the paper describes all 30 logical qubits as entangled
* How preparing each block in the distance-3 [[8,3,3]] code relates to operating it in the distance-2 [[8,3,2]] code
* Whether the double-CZ appears in the earlier [[8,3,2]] literature

When Infleqtion first put 100 logical qubits on its roadmap in 2024, it described a fully error-corrected machine running circuits more than a million layers deep. Its March SEC filing keeps a version of that depth target, one million sequential logical operations in 2028. Running a million operations in sequence with a reasonable chance of success needs logical error ratesaround one in a million. Post-selected error detection does not scale to that depth, because the share of runs kept falls with every added operation. The figure to ask Infleqtion for on the way to 2028 is its logical error rate. QuEra has put figures on its 2028 machine, more than 256 error-corrected logical qubits and a logical error rate of 10⁻⁶.IEEE Spectrum reportedin December 2025 that Magne, Atom Computing and Microsoft’s machine with 50 logical qubits on about 1,200 atoms, should be operational by the start of 2027. At 1,000 logical qubits, Infleqtion’s 2030 target is in the range of the roughly 1,400 logical qubits inGidney’s 2025 RSA-2048 estimate, and that comparison means something only once Infleqtion states a logical error rate.

The next Sqale results I will look for are a distance-3 or higher code with error syndromes measured during the computation, and the [[98,18,4]] qLDPC block from the September 15 announcement running on atoms instead of in a compiler.

Marin Ivezic

Follow on X

Send an email

September 27, 2026
 13 minutes read
 

 Share

 
X

 
LinkedIn

 
Reddit

 
Flipboard

 
WhatsApp

 
Telegram

 
Viber

 
Line

 
Share via Email

 
Print