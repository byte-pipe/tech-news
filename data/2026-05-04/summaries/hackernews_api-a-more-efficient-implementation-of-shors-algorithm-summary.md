---
title: "A more efficient implementation of Shor's algorithm [LWN.net]"
url: https://lwn.net/Articles/1066156/
date: 2026-05-01
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-04T06:02:25.463818
---

# A more efficient implementation of Shor's algorithm [LWN.net]

# A more efficient implementation of Shor's algorithm – Summary

## Overview
- Shor’s algorithm is the primary example of a quantum algorithm that outperforms classical computers for factoring large numbers.  
- Existing quantum hardware lacks sufficient qubits to factor cryptographically relevant numbers.  
- A new paper reduces the qubit requirement for attacking 256‑bit elliptic‑curve cryptography by roughly a factor of 20, though the method remains impractical on today’s machines.  
- The authors released a zero‑knowledge proof of their circuit rather than the circuit itself, citing security concerns.

## Quantum background
- **Qubits** store information as two‑dimensional unit vectors (superpositions).  
- **Quantum gates** rotate or reflect qubits; sequences of gates form a quantum circuit.  
- **Noise** from the environment degrades qubit states; larger, more complex circuits are harder to isolate.  
- **Error correction** creates logical qubits from multiple noisy physical qubits, analogous to ECC memory.  

## Prior work
- Earlier research showed 256‑bit elliptic‑curve attacks using 1,098 logical qubits but required ~2³⁸ quantum gates, far beyond current capabilities.

## New implementation details
- The team (Google, UC Berkeley, Ethereum Foundation, Stanford) built a circuit that:
  - Uses fewer than 1,200 logical qubits.  
  - Executes about 90 million quantum gates.  
  - Translates to roughly 500,000 physical qubits, depending on the hardware architecture.  
- IBM’s Condor quantum computer has 1,121 physical qubits; achieving the required scale would need about 500× more qubits and a modest increase in gate count.

## Zero‑knowledge proof approach
- The actual circuit is withheld to prevent misuse (e.g., attacks on Bitcoin).  
- Researchers provided a **machine‑verifiable proof** that they possess a circuit meeting the claimed specifications.  
- Proof methodology:
  - A simulator reads a quantum circuit, generates thousands of random inputs, runs the circuit, and compares results to a reference implementation.  
  - Shor’s algorithm tolerates occasional errors; the circuit needs to be correct for ~99 % of inputs.  
  - Random inputs are derived from a SHA‑256 hash of the circuit description, ensuring they cannot be cherry‑picked.  
- Verification is performed using **SP1**, a zero‑knowledge virtual machine that:
  - Executes a RISC‑V program, records a trace of CPU state changes, and creates trace polynomials via inverse FFT.  
  - Constructs constraint polynomials that must be zero at every step, proving correct execution without revealing the circuit.  
  - Generates STARK‑based proofs (scalable transparent arguments of knowledge) that can be publicly verified.

## Implications
- The reduction in logical qubit count marks a significant step toward practical quantum attacks on modern cryptography, though hardware limitations remain substantial.  
- The use of zero‑knowledge proofs in quantum‑computing research introduces a new paradigm for responsibly sharing breakthroughs while mitigating security risks.