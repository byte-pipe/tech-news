---
title: A 98-qubit trapped-ion quantum computer with all-to-all connectivity | Nature
url: https://www.nature.com/articles/s41586-026-10676-4
site_name: newsfeed
content_file: newsfeed-a-98-qubit-trapped-ion-quantum-computer-with-all-t
fetched_at: '2026-06-17T19:45:54.171694'
original_url: https://www.nature.com/articles/s41586-026-10676-4
date: '2026-06-17'
description: Quantum computers require both high-fidelity operations and large qubit numbers to surpass classical capabilities1. Trapped-ion platforms have demonstrated the highest gate fidelities of any modality2–6 but scaling to larger qubit numbers while preserving performance has remained a central challenge. We report on Quantinuum Helios, a 98-qubit trapped-ion quantum processor based on the quantum charge-coupled device (QCCD) architecture7. Helios features 137Ba+ hyperfine qubits8,9, all-to-all connectivity enabled by a rotatable ion storage ring connecting two quantum operation regions by a junction10,11, speed improvements from parallelized operations12 and a new software stack with real-time compilation of dynamic programs13. Averaged over all operational zones in the system, we achieve average infidelities of 2.5(1) × 10−5 for single-qubit (1Q) gates, 7.9(2) × 10−4 for two-qubit (2Q) gates and 3.3(5) × 10−4 for state preparation and measurement (SPAM), none of which are fundamentally
  limited and probably able to be improved. These component infidelities are predictive of system-level performance in both random Clifford circuits and random circuit sampling (RCS), the latter demonstrating that Helios operates well beyond the reach of classical simulation and establishes a new frontier of fidelity and complexity for quantum computers14. A new quantum computer, Quantinuum Helios, which is a 98-qubit trapped-ion quantum processor built on the QCCD architecture, demonstrates performance well beyond classical capabilities and provides a path for scaling up quantum computing.
tags:
- nature
---

A 98-qubit trapped-ion quantum computer with all-to-all connectivity
 

Download PDF

Download PDF

### Subjects

* Atomic and molecular physics
* Computer science
* Quantum information

## Abstract

Quantum computers require both high-fidelity operations and large qubit numbers to surpass classical capabilities1. Trapped-ion platforms have demonstrated the highest gate fidelities of any modality2,3,4,5,6but scaling to larger qubit numbers while preserving performance has remained a central challenge. We report on Quantinuum Helios, a 98-qubit trapped-ion quantum processor based on the quantum charge-coupled device (QCCD) architecture7. Helios features137Ba+hyperfine qubits8,9, all-to-all connectivity enabled by a rotatable ion storage ring connecting two quantum operation regions by a junction10,11, speed improvements from parallelized operations12and a new software stack with real-time compilation of dynamic programs13. Averaged over all operational zones in the system, we achieve average infidelities of 2.5(1) × 10−5for single-qubit (1Q) gates, 7.9(2) × 10−4for two-qubit (2Q) gates and 3.3(5) × 10−4for state preparation and measurement (SPAM), none of which are fundamentally limited and probably able to be improved. These component infidelities are predictive of system-level performance in both random Clifford circuits and random circuit sampling (RCS), the latter demonstrating that Helios operates well beyond the reach of classical simulation and establishes a new frontier of fidelity and complexity for quantum computers14.

## Main

As several quantum processing units (QPUs) demonstrate key milestones on the path to utility, including experimental evidence of quantum supremacy14,15,16and the feasibility of fault tolerance17,18, the focus of progress is shifting to making use of the unique advantages of each architecture to scale to much larger sizes without affecting performance. Like all modalities, the trapped-ion QPU based on the QCCD architecture7,19,20,21,22,23has its unique set of challenges and advantages in scaling. For example, trapped ions can require complex optical systems for implementing quantum operations. However, mobile qubit architectures, such as QCCD and optical tweezers24,25, can distribute resources more efficiently than stationary qubit architectures26,27,28, because qubits flow through the QPU like bits in a classical processor, with separated memory structures, data buses and logic units, each optimized for their purpose12. Here we present Quantinuum Helios, a 98-qubit trapped-ion QCCD quantum processor with three key advances from earlier Quantinuum QPUs21,22. First, Helios uses barium ions as the qubits8, achieving 99.92% two-qubit gate fidelity with a more scalable laser architecture. Second, Helios uses a four-way ‘X’ junction10,11,29,30,31,32,33,34,35to connect memory regions to quantum logic regions without increasing electrical control or device fabrication complexity. Third, Helios is orchestrated by a new classical control implementation capable of executing truly arbitrary quantum programs with all-to-all connectivity and complex control flow logic. The cumulative impact of these advances enable us to scale the system size, from six qubits in the first QCCD quantum computer demonstrated five years ago21to now 98 qubits, while setting a new state-of-the-art performance across all metrics, confirmed here by system benchmarks, including RCS, and seen in associated applications run on Helios in materials science and cryptography36,37,38.

## Hardware and software architecture

### QPU architecture and ion trap design

Helios is a transport-based quantum processor with spatially separated qubit memory regions and quantum logic regions. These elements are realized on a 2D surface electrode QCCD21,39, which confines ions with electric fields generated by a pattern of electrodes (Figs.1and2), and the QPU uses individual ions for qubits. To apply gates to qubits or pairs of qubits, the ions are physically transported to isolated trapping zones to facilitate low-crosstalk addressing and maintain high fidelity.

Fig. 1: Image of 98 trapped atomic ions.
The alternative text for this image may have been generated using AI.
Full size image

An image of 98 atomic ions illuminated by resonant laser light in the Helios 2D surface trap illustrated in Fig.2. The overlaid lines indicate different regions of the device, with the quincunx of ions showing the location of the ion trap junction.

Fig. 2: Illustration of the Helios design and conception of operations.
The alternative text for this image may have been generated using AI.
Full size image

a, The final five stages of loading the cache region with qubits from ring storage. The ring rotates ions in both directions to move the circled qubit into the cache.b, Diagram of trap (not to scale) part way through a program. Ring storage qubits are being loaded into the cache and qubits in the quantum logic region are undergoing ground-state cooling. The actual horizontal length is 15.3 mm, the ring diameter is 2.8 mm and the operational zones are 750 μm apart.c, Junction operations shown with two ion pairs. The yellow pair moves into the junction, the ion order is rearranged and then it is transported out to the bottom leg. The red pair moves through the junction back to the ring.d, The proper alignment of a four-ion crystal in the quantum logic zones during 2Q gates.e, Laser beam and crystal configurations during example quantum operations as labelled. Beams are focused to operate on top/bottom legs as shown by colour gradients. The 2Q gate beams are tilted both vertically and horizontally away from the 45° line that intersects the ion crystals in both legs by approximately 1° so as to only interact with a single ion crystal at a time.

Figure2illustrates how Helios operates. The quantum logic region processes batches of up to 16 qubits at a time, using eight high-fidelity operation zones, each with the capability to perform state preparation, measurement, ground-state laser cooling and quantum logic gates. Each operation is implemented by means of focused laser beams propagating about 65 μm above and parallel to the chip surface, as shown in Fig.2e. High-fidelity quantum logic operations necessitate low noise, independent electrode voltages and several laser beams for each zone, consuming most of the control resources in the processor. By using shared lasers across several operation zones (Fig.2e), the quantum logic region design scales these essential components more efficiently than previous systems.

Qubits outside the operation zones are stored in functionally distinct memory regions: ring storage, leg storage and cache (Fig.2b). Memory regions require fewer control resources as the only operations available are sympathetic laser cooling40and qubit transport. To minimize the number of transport control signals, segmented DC electrodes in the memory regions use voltages that are broadcast in a repeating triplet pattern similar to in ref.22. The cache is a small memory region that holds the next batch of pre-sorted qubits before going to the quantum logic region. The leg storage operates as a first in last out memory, whereas the ring storage acts as a random access memory, connecting to the operational region by means of an X-junction.

The junction is a key structure enabling this architecture. As qubits move through the junction, they can be routed to remain in memory or be added to the cache in either the upper or the lower legs. Furthermore, by implementing qubit routing in a separate structure from the quantum logic region, qubit sorting can proceed in parallel with the ground-state cooling of ions in the logic region, increasing the effective clock speed of the QPU. Comparisons with the Quantinuum H1 (ref.21) and Quantinuum H2 (ref.22) QPUs summarize the cumulative impact of these design choices in the electrical control subsystems (Table1).

Table 1 The number of electrodes and independent voltage signals per qubit for three different generations of Quantinuum QPUs
Full size table

### Ion species: qubit and coolant

Helios is the first programmable quantum computer we are aware of to use137Ba+. We define |F= 1,mf= 0⟩and |F= 2,mf= 0⟩hyperfine levels in the137Ba+electronic ground state as |0⟩and |1⟩, respectively. The optical transitions used to implement quantum operations are in the visible part of the wavelength spectrum, allowing for laser and optical components that are more mature, reliable and cost-effective and enables fundamentally better performance. Using more available laser power with better phase performance, we can suppress several of the leading sources of errors in logic gates, including spontaneous emission errors and laser phase fluctuations.

### QCCD operation

In this section, we describe how Helios executes quantum programs using the operations depicted in Fig.2. An arbitrary quantum program is decomposed into ion transport and quantum operations. These operations are not pre-planned but instead executed with a new real-time and dynamic classical control software called ‘Helios runtime’, which is described in detail inMethods.

Ions move through the trap using transport operations from four categories: shift, split/combine, junction transport and rotate. Shift operations translate ions along linear sections in the cache, quantum logic and leg storage regions. These operations can move both two-ion Ba–Yb (BY) and four-ion Ba–Yb–Yb–Ba (BYYB) crystals. Split (combine) operations separate (merge) BYYB (BY and YB) crystals in the eight operation zones. Junction exit (enter) operations move crystals from (into) the junction into (from) the desired leg in the cache with the desired order, BY or YB. Rotate operations collectively move crystals in the ring clockwise or anticlockwise.

Programs use these transport operations to move qubits between the memory and processor regions of the trap. This cycle occurs during a single layer in a program, in which qubits are removed from ring storage, processed in batches within the quantum logic region and then returned to ring storage. Every program begins with qubits in a default configuration: eight BYYB crystals in the quantum logic region and 82 BY crystals in ring storage. Each layer contains up to seven batches, with a maximum of 16 qubits per batch.

Using appropriate ion-to-qubit assignments, quantum operations immediately begin on the qubits already in the eight operation zones, with individual addressing operations occurring first: state preparation (or reset), 1Q gates and measure operations. Next, if 2Q gates are required, the BY and YB pairs associated with each zone are combined into BYYB crystals and ground-state cooling begins. In parallel with cooling, qubits for the next batch of gating are moved from ring storage to the cache. This parallel sorting with ground-state cooling allows cooling and gating cycles to run nearly continuously, as the next batch of qubits is ready to shift in as the current batch finishes operations.

Unlike 1Q, reset and measure operations, 2Q operations are executed in only four of the eight quantum logic zones (second and fourth zones on the top and bottom legs as shown in green in Fig.2b,e). To perform 2Q gates on all 8-qubit pairs, the qubits are first merged and cooled as eight four-ion crystals in all operation zones and then 2Q beams are applied in the four 2Q operation zones. Immediately after executing the 2Q gates, the four-ion shift operation moves all crystals over by one zone (the crystals in the right edge operational zones are split into BY and YB pairs and then shifted into the storage legs). We then apply a small (approximately 300 μs) extra amount of cooling to remove any energy gained from the shift operation and then gate the remaining four crystals. The 2Q gate operation itself requires approximately 70 μs to execute.

After executing quantum operations, a batch is complete: its qubits move to leg storage, whereas qubits in the cache shift to the quantum logic region. This process repeats until all qubits requiring operations have been processed. Last, all qubits move from leg storage to the ring and the cycle begins for the next layer.

Figure3ashows timing estimates and a breakdown of operations per layer for a representative program on Helios. The program is constructed as a sequence of ten layers, in which qubits are randomly paired and receive 1Q and 2Q gates each layer. We define the ‘depth-1 time’ as the time required to perform the random pairing and 1Q and 2Q gates in a single layer and use this time as our characteristic figure of merit for processor speed. We estimate the average depth-1 time by measuring the duration of the depth-10 program and dividing it by the number of layers to average any fortunate sort cases, resulting in an average of 55 ms per layer. To illustrate how program details such as 2Q gate density and qubit connectivity affect depth-1 time, we present timing results in Fig.3bfor three example programs as a function of the number of active qubits (Supplementary Information).

Fig. 3: Circuit run times.
The alternative text for this image may have been generated using AI.
Full size image

a, Time budget per layer for an example depth-10 random program that executes 1Q and 2Q gates on all 98 qubits after an arbitrary permutation each layer, broken down into three categories: ion transport, ground-state cooling and 1Q and 2Q gates.b, Total time per layer versus number of active qubits for three programs: a random program with fully dense 2Q gates, the same random program with approximately half the 2Q gate density and a program with 2D nearest-neighbour 2Q gate pairing. For the two random programs, solid points represent the mean of ten program instances and hollow points show the individual values.

### Real-time compilation of sorting and gates

To realize the full capability of the Helios QPU, the system must be capable of executing arbitrary quantum programs efficiently, including dynamic quantum programs. Optimal decision-making for dynamic quantum programs requires a new classical control hardware unit and software compilation stack. This new stack both allows for real-time qubit routing decisions and increases the level of abstraction of quantum programs—mirroring the way classical computers advanced from writing assembly code to writing high-level programs.

In particular, Helios is the first trapped-ion QPU to translate operations on a program’s ‘virtual qubits’ (user program qubit variables whose physical qubit assignment depends on the structure of the program)41into operations on corresponding physical qubits on the device in real time—that is, while the program is executing and quantum state is live. This is enabled by the Helios runtime, whose responsibility is to efficiently map virtual qubits to physical qubits on the device and turn declarative gates on virtual qubits into operations on physical qubits. This runtime enables state-of-the-art user programming constructs for use on a quantum computer (functions that can allocate and de-allocate qubits depending on the control flow of the program), early termination of programs based on mid-circuit measurement or arbitrary classical logic and classical control flow such as if-then-else statements, for loops and while loops. This is by strong contrast to the way most gate-level quantum programs, commonly referred to as ‘dynamic circuits’42, are written right now—as a flat series of gates with certain gates conditioned on measurements.

The core responsibilities of the Helios runtime are as follows: (1) receive qubit allocation requests on virtual qubits and resolve them to physical qubits; (2) receive gating requests on allocated virtual qubits; (3) transform requested gates on sets of virtual qubits into parallel operations on as many physical qubits as can fit in the quantum operation zones; and (4) transport batches of physical qubits from the ring into these zones, referred to as a ‘sort’. For details on how the Helios runtime performs these responsibilities, seeMethods.

## Benchmarking

To see how Helios performs in practice, we characterize individual operations with component-level benchmarks and measure full-device operations with system-level benchmarks22. Individual operations include SPAM, 1Q and 2Q gates and mid-circuit measurements and resets (MCMRs). We perform two separate system-level benchmarking experiments43,44,45,46,47,48, both of which are examples of volumetric benchmarks44. The first involves random Clifford circuits with MCMR, which can be simulated classically and are similar in structure to the quantum instrument randomized benchmarking (RB) circuits in ref.49. We include MCMRs because they are necessary for quantum error correction. The second involves mirror benchmarking of random quantum circuits, which assesses the ability of Helios to perform RCS. This benchmark quantifies the fidelity with which Helios can run circuits of a fixed (and well understood) classical simulation complexity.

A summary of benchmarking results is shown in Fig.4, with further details and results given inMethodsand theSupplementary Information. The magnitude of errors in the most common individual operations, SPAM, 1Q and 2Q gates and MCMR, are shown in Fig.4a,b. 1Q and 2Q gate errors are measured with Clifford RB50, SPAM errors are measured with repeated SPAM and MCMR crosstalk is measured with a state decay test51. Furthermore, transport operations induce small memory errors owing to magnetic field spatiotemporal inhomogeneities. The magnitudes of these errors are measured as a function of time with a variant of interleaved RB22,52and shown in Fig.4c. The stochastic Pauli error components of the 2Q gate are measured with cycle benchmarking (CB)53and plotted in Fig.4d. A summary of all component errors measured and averaged over all locations is given in Fig.4i.

Fig. 4: Summary of Helios benchmarking results.
The alternative text for this image may have been generated using AI.
Full size image

a,b, Component fidelity from MCMR crosstalk, 1Q gates, SPAM and 2Q operations in upper (a) and lower (b) logic zones.c, Average memory errors as a function of random rounds of 98-qubit rearrangement.d, CB data of stochastic Pauli errors in the 2Q gate.e, Random Clifford circuit success probability as a function of sequence length with different number of MCMR operations.f, Random Clifford circuit MCMR error estimate as a function of number of MCMR operations.g, Fidelity of random quantum circuits as a function of depth, inferred from mirror benchmarking.h, Classical simulation cost of sampling from the associated circuits using optimized tensor-network contraction, shown for both the 56-qubit H2 quantum computer (purple) and for Helios (green). Shaded regions (symbols) denote the min/max (mean) optimized cost over five random circuit instances.i, Summary of average component errors for each benchmarked operation. All uncertainty shown is one standard deviation from bootstrap resampling.

The random Clifford circuits benchmark is a slight variation from ref.49and run withN= 98 qubit circuits with a variable number of layers. Each layer contains an independent random 1Q Clifford unitary on every qubit, followed by a maximally entangling 2Q gate onN/2 uniformly random pairs of qubits, followed by a fixed number of MCMR operations performed on a uniformly random subset of qubits. We use stabilizer tracking to perform all measurements, both mid-circuit and final, in a Pauli basis such that the outcome ideally has a deterministic parity (Methods). We measure the average circuit success probability as a function of both the number of layers and the number of MCMR operations per layer. We fit the results to a decay model to estimate an effective 2Q gate error and an effective MCMR error. The effective 2Q (MCMR) errors are the magnitudes of simple depolarizing (bit-flip) channels that would best fit the data in the absence of all other errors. The data are shown in Fig.4e,f, with further details in theSupplementary Information.

The mirror benchmarking of the random circuits benchmark procedure follows exactly the description in ref.14. The results of mirror benchmarking on random quantum circuits are shown in Fig.4g. The fidelity reported at each depth gives an accurate estimate of the fidelity achievable by running (unmirrored) random circuits at that depth. Figure4hshows the expected classical per-sample cost to simulate RCS at various circuit depths using optimized tensor network contraction (and under various assumptions on available memory). Costs are reported both in years of exascale compute time and in power requirements to classically sample at the same rate that Helios can (assuming state-of-the-art GPU power consumption of 1011FLOPS W−1). Further details on the circuits used, estimation of fidelity from mirror benchmarking and assumptions involved in the reported classical simulation costs can be found inMethods.

## Outlook

In this manuscript, we reported on how Helios operates and its current performance. Even at this early stage in its life cycle, Helios exhibits state-of-the-art capabilities at the scale of roughly 100 qubits. Like its predecessors Quantinuum H1 and H2, we expect the performance of Helios to improve over time. Examples of relatively straightforward performance improvements include: (1) fewer gate errors, as our two-qubit gate error model suggests that the 2Q gate error could be cut in half; (2) smaller memory errors using dynamic decoupling strategies54; and (3) reduced circuit times from both faster transport operations55,56,57and better compilation methods.

Beyond these performance improvements, increasing clock speed is one scaling challenge for the QCCD platform. In this work, we begin to address this issue through a fundamental architectural shift by parallelizing operations12. Previous generations, H1 and H2, used the same space for ground-state cooling and gating operations, with cooling operations being up to two orders of magnitude slower21,22. Helios, on the other hand, spreads the cooling operation over space to allow ions to spend less time in the zones used for 2Q gates. By increasing the ratio of cooling zones to gate zones, future QCCD-based QPUs can optimize the processor zone complexity while simultaneously increasing the clock speed.

Although we do not yet fully understand the power or limitations of Helios, the combination of a new qubit choice, device architecture and control software runtime already represents substantial progress in the push for more powerful devices, scalable architectures and capabilities for fault-tolerant computation. Helios is far beyond the simulation abilities of classical computers, as evidenced by the RCS demonstration described above, and well poised to expand the set of tasks best suited for contemporary quantum computers. Indeed, as reported in refs.36,37,38, Helios is already enabling advancements in quantum simulations of superconductivity and in cryptographic protocols to generate certified randomness.

Looking further ahead, the successful integration of the four-way junction29paves the way for much larger QCCD processors. Junction-based architectures should allow QCCD machines to maintain all-to-all connectivity for large numbers of qubits, opening the design space for fault tolerance to high-efficiency encodings58, transversal logic59,60, low-overhead magic state factories61and single-shot error correction62,63,64,65,66,67,68,69,70,71,72,73,74,75,76.

## Methods

### Quantum operations

The 1Q and 2Q gates are implemented with pairs of 515-nm laser beams separated by the approximately 8.04 GHz qubit frequency splitting. The 1Q gates,\({U}_{1{\rm{Q}}}(\theta ,\phi )={{\rm{e}}}^{(-{\rm{i}}\theta /2)(\cos \phi X+\sin \phi Y)}\), are implemented with co-propagating laser beams for improved phase stability of the Raman interaction and minimal sensitivity to the thermal motion of the ions. 1QZ-rotations,RZ(θ) = e−iZθ/2, are implemented by phase changes in software tracking and applied to the next 1Q gate scheduled. The 2Q gates are implemented with beams intersecting the quantum logic zones at 90° to each other such that the differencek-vector is parallel to the crystal axis (Fig.2e). The 2Q gate protocol is based on the Mølmer–Sørensen interaction using wrapper pulses to remove optical phase sensitivity21,77, yielding a native 2Q gateRZZ(θ) = e−iZZθ/2. The gate angleθis specified by the user and is varied by adjusting the detuning and duration of the gate. Gate infidelities have been shown to improve for smaller angles22but here we only benchmark the perfect entanglerRZZ(π/2).

SPAM is achieved in137Ba+with a combination of lasers at 493 nm, 614 nm, 650 nm and 1,762 nm, with preparation accomplished by means of narrow-band optical pumping9,78. The 1,762-nm laser is locked to a narrow linewidth cavity to facilitate high-fidelity mapping pulses between theS1/2ground state and theD5/2state (Extended Data Fig.1). The standard measurement protocol first maps the |F= 1,mf= 0⟩qubit state to theD5/2manifold with several π pulses to different levels inD5/2. Then the 493-nm and 650-nm lasers are turned on to induce fluorescence from allS1/2states. Furthermore, the 1,762-nm laser is used to protect neighbouring qubits from measurement crosstalk errors (Extended Data Fig.1b) and enables a ternary (three-outcome) measurement to detect leakage population (Extended Data Fig.1c) without the use of ancillas or 2Q gates79,80,81.

The QCCD architecture relies on mid-circuit recooling of ions, achieved here with sympathetic cooling applied to171Yb+ions co-trapped with the137Ba+qubit ions. The171Yb+ion is chosen because of its similar mass to137Ba+and for the established and straightforward methods for qubit control and state measurement82. The cooling is performed with lasers tuned near theS1/2toP1/2transition of171Yb+at 369 nm.

To load ions into the QCCD, we photoionize both species from cold atomic beams produced by an atomic source similar to ref.22, based on a neutral atom magneto-optical trap83,84. Other hardware details, including implementation of all quantum operations, are described in theSupplementary Information.

### The Helios runtime software

Many of the Guppy13programs for the applications discussed in the ‘Benchmarking’ use the features outlined in the section ‘Real-time compilation of sorting and gates’. Moreover, quantum error correction programs can use dynamic allocation and de-allocation of virtual ancilla qubits without worrying about physical qubit mappings of the ancilla qubits or the precise control flow of the quantum error correction program. Furthermore, any programming language compiling to QIR85, such as Q#86, Qiskit87, OpenQASM 2.0/3.0 (refs.88,89), Cirq90and CUDA-Q91, can use QIR adaptive profile features to implement these control flow constructs for programs executing on Helios.

An example of high-level operations enabled by the Helios runtime is the ‘gate streaming’ used in ref.37. In the Guppy program executed on Helios for this work, a section of the program performs a remote procedure call out to a classical server that is separate from the control system but which is allowed to communicate with the control system through a networking interface92. The information transmitted to the control system by the classical server is the measurement basis for each qubit. If a qubit needs no change in measurement basis, then the runtime receives no 1Q gate to apply before measurement. In the case that a whole row of BY or YB crystals on the top or bottom legs needs no basis change, the Helios runtime will not perform any extraneous transport to address these qubits. Notably, this reduces the overall shot time, improving the critical latency times in that application. Efficient gate streaming would be impossible without the real-time identification of qubits provided by the runtime.

As mentioned in the section ‘Real-time compilation of sorting and gates’, the Helios runtime has four main responsibilities to perform for programs executing on Helios. Responsibility (1) is performed using a model of the physical QPU state as the program runs and determining efficient mappings from virtual qubits to physical qubits. Regardless of the state of the trap when a qubit allocation request is made, a simple algorithm identifies the qubit closest to the quantum operation zone. If an unallocated qubit is in the quantum operation zone, then it is used. Otherwise, a qubit in the storage ring that is unallocated and closest to the junction is allocated. If no allocatable qubits are in the storage ring or quantum operation zone, then all qubits are ‘flushed’ back into the storage ring and then an unallocated qubit closest to the junction is allocated.

Responsibilities (2) and (3) are performed by identifying which quantum logic operations can be done in parallel by storing them in sets contained in a data structure we refer to as a ‘slice’. Sequences of slices are accumulated into another data structure that drives the sorting of each slice to execute the quantum logic operations within. Responsibility (4) is performed by carrying out anO(n) traversal over the ring storage to determine which two pairs in a slice have qubits closest to the cache. The runtime then assigns one pair to move to the top leg and the other to the bottom. Subsequently, the algorithm determines the smallest number of rotations needed to move the two pairs into BYYB crystals in both legs. This process is visualized in Fig.2. This process repeats until either enough pairs are moved into the cache to fill a batch or no more pairs need to be sorted. Finally, the runtime dispatches the calculated sort by generating these operations as a queue of commands to lower-level control system software for performing transport operations and parallelized cooling, as outlined in the section ‘QCCD operation’. After all of the quantum logic operations have been executed in a given slice through repetitions of this sort, transport is generated to return the qubits back into the ring storage—and the sorting algorithm repeats for subsequent slices. For unconditional programs with no changes in program execution depending on mid-program measurement results, these responsibilities are calculated ‘ahead’ of the physical execution of the operations on the quantum processor and thus add no extra overhead to the time needed to run a program. However, when mid-program measurements are used to determine future quantum operations, submillisecond-scale latency can be added to calculate the above responsibilities for the next round future quantum operations while the qubit state is still live. The transport time savings can be on the several-millisecond timescale for sorting a single batch of qubits more efficiently based on feed-forward quantum operations and much larger quantities of time can be saved for programs with early-exit conditions.

### Component-level benchmarks

#### SPAM

It is difficult to differentiate state preparation errors from measurement errors93, although from detailed modelling of137Ba+qubits, we expect state preparation errors to be the largest contributor9.

We measure SPAM errors by preparing 16 qubits in the eight operation zones in the |0⟩or |1⟩states and measuring each qubit. For any given shot, the state preparations are randomized among the different qubits, but we ensure that each qubit is prepared in each state for the same total number of shots. We run two experiments: standard measurement that ideally differentiates |0⟩from |1⟩but falsely returns |1⟩in the event that the qubit has leaked and a ternary measurement, shown in Extended Data Fig.1c, that ideally differentiates |0⟩, |1⟩and leaked states. For both experiments, we take 4,000 shots per state preparation.

For the standard measurement, we measure errors of 5.2(9) × 10−4and 1.4(5) × 10−4when preparing |0⟩and |1⟩, respectively. Because this measurement protocol mistakenly detects leaked states as |1⟩, the reported error for preparing and measuring |1⟩will not catch all errors9. For the ternary measurement, we find an average leakage probability of 8(3) × 10−4and, in the event of non-leakage, we measure SPAM errors of 1.0(1) × 10−3and 1.3(1) × 10−3for |0⟩and |1⟩, respectively. Although the ternary measurement reveals more information as it can detect leakage, it also has a larger SPAM error owing to a larger number of shelving pulses involved. The SPAM errors reported in Fig.4a,b,iare averaged between the two state preparations. We actively make a trade-off between SPAM fidelity and MCMR crosstalk by reducing laser powers and detection times. SPAM is performed much less frequently than gating, leading to a lower relevant importance in the circuit despite being a large error in Fig.4a,b,i.

#### 1Q gates

1Q gate errors are mainly caused by spontaneous emission during the Raman gate, laser phase and intensity noise and finite qubit coherence. Notably, spontaneous emission causes leakage outside the computational subspace. We quantify 1Q gate errors by Clifford RB50(Supplementary Information).

We follow the methods in ref.94to account for leakage in the 1Q infidelity estimate. The ternary measurement allows us to measure the leakage population at the end of every circuit without the use of ancilla qubits (as done in ref.22). We estimate the rate of leakage per 1Q CliffordrLby the rate at which the measured leakage population increases with sequence length. The probability of observing the expected computational state decays exponentially owing to non-leakage errors asp(l) =A(1 −r)l+ 1/2 for sequence lengthl, in whichAandrare fit parameters. The reported 1Q error is the Clifford average infidelityϵavg,1Q=r/2 +r(ref.94).

Extended Data Fig.2shows the success probability and the leaked population as a function ofl, for all 16 qubits in the eight operation zones. We obtain a zone-averaged 1Q error of 2.5(1) × 10−5, which includes a leakage rate of 1.12(6) × 10−5. The error bars represent a one-sigma confidence interval obtained from bootstrapping95. The leakage rates and infidelities for each individual qubit are given in theSupplementary Information. The measured errors can be compared with our predictions from physical error models of 2.6(6) × 10−5that account for measured laser intensity noise, calculated spontaneous emission and measured memory error.

Finally, we ran a statistical hypothesis test for correlated errors in the simultaneous 1QRB data. An error channel on several subsystems is correlated if it cannot be factored into a tensor product of individual error channels on each subsystem, and such correlated errors are a signature of crosstalk. We found no evidence of correlated errors at the 95% confidence level (Supplementary Information).

#### 2Q gates

Errors in theRZZ(θ) gates are caused by spontaneous emission from the Raman lasers and experimental imperfections including laser phase and intensity noise at the position of the ion, thermal motion of the ions, voltage noise on the electrodes and imprecise calibrations of the gate parameters. We validate the performance of the maximally entanglingRZZ(π/2) gate (referred to as the 2Q gate) using both Clifford 2QRB and CB. Further details of each implementation are in theSupplementary Information.

We again follow the methods in ref.94to account for leakage in the 2QRB infidelity estimate. The leaked population versus sequence length is used to extract a leakage rate per Clifford, which is rescaled into a leakage rate per 2Q gaterL,2Q, using the fact that there are 1.5 2Q gates per 2Q Clifford on average. We fit the success probability of the remaining population to the decay modelp(l) =A(1 −r)l+ 1/4, for sequence lengthl, in whichAandrare fit parameters. The average infidelity of the non-leakage error component per Clifford is given by 3r/4, which is rescaled into an average infidelity per 2Q gate ofr/2. The average infidelity per 2Q gate (including leakage) is then computed asϵavg,2Q=r/2 +rL,2Q. We note that our rescaling of the error per Clifford into an error per 2Q neglects the errors from 1Q gates and memory errors during the 2QRB sequence, which we estimate to contribute 1.2(2) × 10−4per 2Q gate.

The experimental 2QRB data are shown in Extended Data Fig.3. We obtain a zone-averaged 2Q infidelity ofϵavg,2Q= 7.9(2) × 10−4, which includes a leakage rate ofrL,2Q= 2.4(1) × 10−4. The leakage rates and infidelities for each individual qubit pair are given in theSupplementary Information. The leakage errors arise from both spontaneous emission error, which we measure to be 1.0(2) × 10−4in agreement with the model in ref.96, and from the leakage memory error (discussed in the section ‘Memory errors’). In total, we expect leakage to contribute 1.7(2) × 10−4of the error.

Our measured value of 7.9(2) × 10−4can be compared with a total expected error per 2Q gate of 3.5(4) × 10−4, which we predict from an error budget consisting of spontaneous emission errors, memory error and 1Q pulse errors plus other characterized experimental sources of noise, such as laser phase and intensity noise, thermal motion of the ions and imprecise calibrations. The discrepancy of the measured 2Q error with predicted value could be explained by several factors, including higher leakage error in the operational zones owing to finite extinction of the resonant detection beams present, non-thermal motional distributions, crosstalk or other unaccounted for effects.

Just as with the 1QRB data, we performed a statistical test for the presence of correlated errors in the 2QRB data and found no notable evidence of correlated errors between different qubit pairs (Supplementary Information).

We also perform 2QCB (ref.53) to estimate a partial Pauli error model for the 2Q gate in each operation zone, with the experimental and theoretical details provided in theSupplementary Information. Extended Data Fig.4shows the expectation value decays and estimated Pauli error channels for each qubit pair. We find that the zone-averaged infidelity is 8.1(2) × 10−4, which includes a leakage rate of 1.14(4) × 10−4. The error channel is dominated by IZ and ZI errors, which modelling suggests is caused by laser phase noise, spontaneous emission and electrode voltage noise. We note that our estimate of leakage rate per 2Q gate from 2QCB is about a factor of two smaller than the estimate from 2QRB.

#### Memory errors

Qubits not being gated incur memory errors owing to magnetic field inhomogeneities, with their impact being heavily dependent on the circuit structure and its specific transport schedule. As a figure of merit, we define the depth-nmemory error to be the average infidelity per qubit after randomly pairing all qubits, performing the transport and cooling operations that would be required to apply 2Q gates on all pairs (but no actual gate operations) and repeating this processntimes.

We measure memory error with a variant of 1QRB that interleaves random transport between 1Q Clifford gates, referred to as transport-1QRB22,52. Our method here differs from ref.22in that we partition the 98 qubits into groups in which the qubits in each group have a random 1Q Clifford operation applied after everykrounds of depth-1 transport operations on all qubits (Supplementary Information). The qubits in the different groups will have a different amount of transport and idle time between Clifford operations, which allows us to extract how memory errors scale with the number of depth-1 transport operations for random circuits.

We run transport-1QRB circuits on the 98 qubits in four groups of 25 or 24 qubits, withk∈{1, 2, 4, 8} transport operations between Cliffords. Furthermore, we use the ternary measurement to extract any leakage errors during transport. Extended Data Fig.5a,bshows the measured decay in transport-1QRB for computational and ternary measurements, respectively. The decay curves are clustered into four groups determined byk. By fitting the decay curves and accounting for the leakage rate using the same procedure as in the section ‘1Q gates’, we obtain the Clifford infidelity for each qubit.

Extended Data Figure5cshows a plot of the Clifford infidelity as a function of the number of depth-1 transport operations, averaged over all qubits in the corresponding group. The expected scaling of memory error with delay time varies depending on the timescale of the noise sources97. For this reason, we fit the memory error versuslto a quadratic equationa+bl+cl2, in whichbandccapture the linear memory error rate (from fast noise) and quadratic memory error parameter (from slow noise), respectively52.

From the fit to the data, we infer a linear memory error rate of 5(1) × 10−4and a quadratic memory error parameter of 7(2) × 10−5. We find that the leakage error scales linearly with the number of transport operations, with a rate of 4.0(2) × 10−4, and accounts for nearly all of the linear memory error. The expected coherent error from typical drift in magnetic fields between calibrations (every roughly 5 s) of approximately 10 μG is 3 × 10−5in a depth-1 circuit. The remaining coherent error may be explained by imperfections in the phase-tracking routine or other unaccounted sources of noise.

#### MCMR crosstalk

We measure MCMR crosstalk errors by preparing 16 qubits in the eight operation zones, while the remaining 80 qubits are stored in the ring. A single (‘target’) qubit in each operation zone is measured and reset repeatedly, while the other 90 (‘spectator’) qubits are prepared in the |0⟩or |1⟩. Crosstalk errors on spectator qubits result from absorbing stray measurement or reset light. The resulting spontaneous emission can lead to incoherence owing to bit-flip, leakage or dephasing errors. Using the ternary measurement at the end allows us to differentiate bit-flip rates from leakage rates to get a more detailed picture of the crosstalk error channel. We find a per MCMR crosstalk error of 1.3(1) × 10−5, with crosstalk in individual operation zones reported in Fig.4a. Further details are provided in theSupplementary Information.

### System-level benchmarks

#### Random Clifford circuits with mid-circuit measurements

Reference98introduced circuits with random Clifford layers as a scalable system-level benchmark called binary randomized benchmarking. An extension allowing for MCMRs was given in ref.49, called quantum instrument randomized benchmarking. Our circuits are constructed similarly to those in ref.49, with a few small modifications (Supplementary Information).

In our implementation, a lengthlcircuit onNqubits withnmMCMRs per layer consists of the following for each layer:

* A distinct uniformly random 1Q Clifford is applied to each qubit.
* TheNqubits are uniformly randomly paired into\(\lfloor \frac{N}{2}\rfloor \)qubit pairs and the 2Q gateRZZ(π/2) is applied to each pair, with Pauli twirling applied to the 2Q gates.
* A uniformly random subset ofnmqubits is sampled and, for each qubit, a 1Q Clifford is applied to prepare a measurement in a particular Pauli basis, followed by a MCMR operation.

To classically verify correct circuit outputs, we track a random initial stabilizer through the circuit (Supplementary Information). The parity of the evolved stabilizer defines a success/failure trial. For the purpose of fidelity estimation, the average success probability is rescaled into a quantity called the polarization98, defined asypol= 2psucc− 1. A polarization of 1 corresponds to perfect success, whereas a polarization of 0 corresponds to 50% success, or random guessing. A plot ofypol(l,nm) versuslfor different values ofnmis shown in Fig.4e. LetF(nm) be the process fidelity per circuit layer as a function ofnm. We estimateF(nm) by fitting the polarization to an exponential decay model. Figure4fshows a plot ofF(nm) versusnm. We note that the layer fidelity actually increases slightly (with overlapping error bars) asnmincreases from 8 to 16. This is explained by the fact that a batch of 16 measurements in the operation zones uses the protected measure scheme (explained in Fig.1b), which protects against MCMR crosstalk in the operation zones.

To see whether the results are consistent with our component benchmarks, we first compute an effective 2Q gate errorϵeff,2Qfrom thenm= 0 data, using

$$F({n}_{{\rm{m}}}=0)={(1-5{{\epsilon }}_{{\rm{eff}},2{\rm{Q}}}/4)}^{\left\lfloor \frac{N}{2}\right\rfloor },$$

 (1)
 

in which the factor 5/4 comes from the conversion between process and average fidelity99. The effective 2Q gate error includes errors from 2Q gates, 1Q gates and memory errors and can be thought of as the infidelity of a 2Q depolarizing channel that would best fit the data in the absence of all other errors. We findϵeff,2Q= 1.7(2) × 10−3, whereas an accounting of 2Q and memory errors according to

$${{\epsilon }}_{{\rm{eff}},2{\rm{Q}}}=\frac{4}{5}\left(\left(\frac{5}{4}\right){{\epsilon }}_{{\rm{avg}},2{\rm{Q}}}+2\left(\frac{3}{2}\right){{\epsilon }}_{{\rm{mem}}}\right)$$

 (2)
 

predicts 2.2(1) × 10−3(Supplementary Information). We attribute the fact that the effective 2Q error is smaller than what the component errors predict to improvements in the gates and memory errors between the times when the component and random Clifford circuit benchmarks were run.

We next compute an effective MCMR errorϵeff,MCMRby best-fitting theF(nm) versusnmdata to the heuristic formula

$$F({n}_{{\rm{m}}})={(1-5{{\epsilon }}_{{\rm{eff}},2{\rm{Q}}}/4)}^{\left\lfloor \frac{N}{2}\right\rfloor }{(1-3{{\epsilon }}_{{\rm{eff}},{\rm{MCMR}}}/2)}^{{n}_{{\rm{m}}}}$$

 (3)
 

together with our computed value ofϵeff,2Q. We findϵeff,MCMR= 2.4(5) × 10−3. By comparison, adding the component-level SPAM, MCMR crosstalk and memory errors, we predict an effective MCMR error of 2.5(1) × 10−3(Supplementary Information). We conclude that the data from our random Clifford with MCMR circuits is consistent with our measured component-level errors. We remark that our method of comparison is heuristic and a rigorous methodology for comparing component-level to system-level benchmarking performance is an open problem.

#### RCS mirror benchmarking

RCS is a system-level benchmark assessing how effectively a quantum computer can generate computationally complex quantum states15. Like binary randomized benchmarking, RCS examines the extent to which quantum circuits obtain the performance expected from component-level benchmarks. At the same time, because the classical difficulty of sampling from the outputs of random quantum circuits has been extremely well studied over the past decade100, RCS provides a well-vetted benchmark for the computational power of a quantum computer.

By making use of the arbitrary connectivity of the Helios quantum computer, we consider RCS with circuit geometries constructed from colourings of random regular graphs14: a layer depth-lrandom circuit is constructed by interleavingllayers of 2QRZZ(π/2) gates (each layer containingN/2 2Q gates) withl+ 1 layers of Haar-random 1Q gates (each layer containingN1Q gates). Although the fidelity of such circuits can in principle be inferred by running them and performing cross-entropy benchmarking101, evaluating the cross-entropy requires exact simulation of the circuits in question and is infeasible except for small depth or qubit number. To estimate the expected state fidelity in RCS (and therefore the anticipated performance in cross-entropy benchmarking), we follow the strategy of refs.14,102,103,104,105and infer the fidelity of a layer depth-lcircuit by computing the return-probabilityFMBof a ‘mirrored’ layer depth-l/2 circuit, with the second (mirrored) half of the circuit using randomized compiling to prevent unintended cancellation of coherent errors. The randomness for randomized compilation is sampled in real time at the start of each shot and the corresponding random 1Q gates are compiled on the fly (with the existing Haar-random 1Q gates), resulting in only one physical 1Q gate per qubit per layer. Following ref.14, we also initialize each mirrored circuit into a random computational basis state to prevent unequal SPAM errors between the two basis states from biasing the fidelity estimate. At each depth, we execute between 1,000 and 2,500 shots spread evenly across 100 random circuit connectivities. As well as the mirrored random circuits run to assess RCS performance, we also directly sampled the output of a single (unmirrored) random circuit of depthd= 26. That circuit is included in ref.106, along with 2,500 sampled bitstrings from Helios.

The fidelity of RCS as a function of depth inferred in this manner is reported in Fig.4g. We perform a least-squares best fit to the gate-counting model from ref.14,

$${F}_{{\rm{GC}}}(l)={(1-{p}_{{\rm{SPAM}}})}^{N}{\left(1-\frac{5}{4}{{\epsilon }}_{{\rm{eff}},2{\rm{Q}}}\right)}^{\frac{N}{2}(l-\delta )}.$$

 (4)
 

HereN= 98,δ= 1.12 is a correction to effective circuit layer depth from boundary effects in mirror circuits14,pSPAMis the effective SPAM error andϵeff,2Qis the effective average 2Q error rate, which includes effects from 1Q, 2Q and memory errors as in the previous section. From the fit, we estimatepSPAM= 5.3(51) × 10−4andϵeff,2Q= 2.00(6) × 10−3. This effective 2Q error is also consistent with the estimate obtained from random Clifford circuits as well as component benchmarks reported in Fig.4i.

The task of sampling from the output distribution induced by running forward (unmirrored) circuits is well defined for either quantum or classical computers. In either case, the quality of samples can be judged by statistical tests, with the linear cross-entropy test being a widely used standard15. As mentioned above, the linear cross-entropy score of the quantum data is expected to agree closely (for the circuits run here) with the overall circuit fidelity estimated from mirror benchmarking results at comparable depth14. For the high scores achievable with Helios (hitting a minimum of about 3.5% at depth 26), there is no known classical strategy to score well on the linear cross-entropy test without performing (nearly) exact simulation of the circuits in question14, with the most efficient strategy for doing so being tensor-network contraction.

The reported costs in Fig.4hare for optimized tensor-network contraction assuming so-called ‘embarrassing parallelization’ (by means of slicing) into independent computations involving various amounts of available memory (corresponding to cotengra contraction widths of\({\mathcal{W}}=30\), 49 and 54) and were obtained using (sliced) simulated annealing built into cotengra107. We note that the contraction–cost optimization performed here is only approximate and the costs could certainly be mildly improved by providing the optimization heuristics with more computational power. However, we do not expect such improvements to change the overall conclusion that Helios can produce states at high global fidelity for which the (classical) sampling cost is vastly beyond the capabilities of existing supercomputers.

## Data availability

Component benchmarking data are available from the Quantinuum hardware specifications repository athttps://github.com/Quantinuum/quantinuum-hardware-specifications. The data used in this paper are available from the Helios paper data repository athttps://github.com/Quantinuum/Helios-paper-data.

## Code availability

The custom code used to generate and analyse the tests in this paper is available from the Helios paper data repository athttps://github.com/Quantinuum/Helios-paper-data.

## References

1. DiVincenzo, D. P. The physical implementation of quantum computation.Fortschr. Phys.48, 771–783 (2000).ArticleGoogle Scholar
2. Ballance, C. J., Harty, T. P., Linke, N. M., Sepiol, M. A. & Lucas, D. M. High-fidelity quantum logic gates using trapped-ion hyperfine qubits.Phys. Rev. Lett.117, 060504 (2016).ArticleADSCASPubMedGoogle Scholar
3. Gaebler, J. P. et al. High-fidelity universal gate set for9Be+9Be+ion qubits.Phys. Rev. Lett.117, 060505 (2016).ArticleADSCASPubMedGoogle Scholar
4. Srinivas, R. et al. High-fidelity laser-free universal control of trapped ion qubits.Nature597, 209–213 (2021).ArticleADSCASPubMedPubMed CentralGoogle Scholar
5. Hughes, A. C. et al. Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling. Preprint athttps://arxiv.org/abs/2510.17286(2025).
6. Clark, C. R. et al. High-fidelity Bell-state preparation with40Ca+optical qubits.Phys. Rev. Lett.127, 130505 (2021).ArticleADSCASPubMedGoogle Scholar
7. Kielpinski, D., Monroe, C. & Wineland, D. J. Architecture for a large-scale ion-trap quantum computer.Nature417, 709–711 (2002).ArticleADSCASPubMedGoogle Scholar
8. Dietrich, M., Kurz, N., Noel, T., Shu, G. & Blinov, B. Hyperfine and optical barium ion qubits.Phys. Rev. A81, 052328 (2010).ArticleADSGoogle Scholar
9. An, F. A. et al. High fidelity state preparation and measurement of ion hyperfine qubits with\(I > \frac{1}{2}\).Phys. Rev. Lett.129, 130501 (2022).ArticleADSCASPubMedGoogle Scholar
10. Blakestad, R. B. et al. High-fidelity transport of trapped-ion qubits through anX-junction trap array.Phys. Rev. Lett.102, 153002 (2009).ArticleADSCASPubMedGoogle Scholar
11. Blakestad, R. B. et al. Near-ground-state transport of trapped-ion qubits through a multidimensional array.Phys. Rev. A84, 032314 (2011).ArticleADSGoogle Scholar
12. Brandl, M. F. A quantum von Neumann architecture for large-scale quantum computing. Preprint athttps://arxiv.org/abs/1702.02583(2017).
13. Koch, M., Lawrence, A., Singhal, K., Sivarajah, S. & Duncan, R. Guppy: pythonic quantum-classical programming. Preprint athttps://arxiv.org/abs/2510.12582(2025).
14. DeCross, M. et al. Computational power of random quantum circuits in arbitrary geometries.Phys. Rev. X15, 021052 (2025).CASGoogle Scholar
15. Arute, F. et al. Quantum supremacy using a programmable superconducting processor.Nature574, 505–510 (2019).ArticleADSCASPubMedGoogle Scholar
16. Wu, Y. et al. Strong quantum computational advantage using a superconducting quantum processor.Phys. Rev. Lett.127, 180501 (2021).ArticleADSCASPubMedGoogle Scholar
17. Ryan-Anderson, C. et al. Realization of real-time fault-tolerant quantum error correction.Phys. Rev. X11, 041058 (2021).CASGoogle Scholar
18. Acharya, R. et al. Quantum error correction below the surface code threshold.Nature638, 920–926 (2024).Google Scholar
19. Wineland, D. J. et al. Experimental issues in coherent quantum-state manipulation of trapped atomic ions.J. Res. Natl Inst. Stand. Technol.103, 259–328 (1998).ArticleCASPubMedPubMed CentralGoogle Scholar
20. Home, J. P. et al. Complete methods set for scalable ion trap quantum information processing.Science325, 1227–1230 (2009).ArticleADSMathSciNetCASPubMedGoogle Scholar
21. Pino, J. M. et al. Demonstration of the trapped-ion quantum CCD computer architecture.Nature592, 209–213 (2021).ArticleADSCASPubMedGoogle Scholar
22. Moses, S. A. et al. A race-track trapped-ion quantum processor.Phys. Rev. X13, 041052 (2023).CASGoogle Scholar
23. Mordini, C. et al. Multizone trapped-ion qubit control in an integrated photonics QCCD device.Phys. Rev. X15, 011040 (2025).CASGoogle Scholar
24. Bluvstein, D. et al. A quantum processor based on coherent transport of entangled atom arrays.Nature604, 451–456 (2022).ArticleADSCASPubMedPubMed CentralGoogle Scholar
25. Reichardt, B. W. et al. Fault-tolerant quantum computation with a neutral atom processor. Preprint athttps://arxiv.org/abs/2411.11822(2025).
26. Kim, Y. et al. Evidence for the utility of quantum computing before fault tolerance.Nature618, 500–505 (2023).ArticleADSCASPubMedPubMed CentralGoogle Scholar
27. Radnaev, A. G. et al. Universal neutral-atom quantum computer with individual optical addressing and nondestructive readout.PRX Quantum6, 030334 (2025).ArticleADSGoogle Scholar
28. Chen, J.-S. et al. Benchmarking a trapped-ion quantum computer with 30 qubits.Quantum8, 1516 (2024).ArticleGoogle Scholar
29. Burton, W. C. et al. Transport of multispecies ion crystals through a junction in a radio-frequency Paul trap.Phys. Rev. Lett.130, 173202 (2023).ArticleADSCASPubMedGoogle Scholar
30. Hensinger, W. K. et al. T-junction ion trap array for two-dimensional ion shuttling, storage, and manipulation.Appl. Phys. Lett.88, 034101 (2006).ArticleADSGoogle Scholar
31. Decaroli, C. et al. Design, fabrication and characterization of a micro-fabricated stacked-wafer segmented ion trap with two X-junctions.Quantum Sci. Technol.6, 044001 (2021).ArticleADSGoogle Scholar
32. Wright, K. et al. Reliable transport through a microfabricatedX-junction surface-electrode ion trap.New J. Phys.15, 033004 (2013).ArticleADSCASGoogle Scholar
33. Amini, J. M. et al. Toward scalable ion traps for quantum information processing.New J. Phys.12, 033031 (2010).ArticleADSGoogle Scholar
34. Moehring, D. L. et al. Design, fabrication and experimental demonstration of junction surface ion traps.New J. Phys.13, 075018 (2011).ArticleADSGoogle Scholar
35. Shu, G. et al. Heating rates and ion-motion control in a Y-junction surface-electrode trap.Phys. Rev. A89, 062308 (2014).ArticleADSGoogle Scholar
36. Granet, E. et al. Superconducting pairing correlations on a trapped-ion quantum computer. Preprint athttps://arxiv.org/abs/2511.02125(2026).
37. Liu, M. et al. Certified randomness amplification by dynamically probing remote random quantum states. Preprint athttps://arxiv.org/abs/2511.03686(2025).
38. Niroula, P. et al. Realization of a quantum streaming algorithm on long-lived trapped-ion qubits. Preprint athttps://arxiv.org/abs/2511.03689(2025).
39. Chiaverini, J. et al. Surface-electrode architecture for ion-trap quantum information processing.Quantum Inf. Comput.5, 419–439 (2005).MathSciNetCASGoogle Scholar
40. Kielpinski, D. et al. Sympathetic cooling of trapped ions for quantum logic.Phys. Rev. A61, 032310 (2000).ArticleADSGoogle Scholar
41. OpenQASM live specification.https://openqasm.com/language/types.html.
42. Brown, N. C. et al. Advances in compilation for quantum hardware – a demonstration of magic state distillation and repeat-until-success protocols. Preprint athttps://arxiv.org/abs/2310.12106(2023).
43. Cross, A. W., Bishop, L. S., Sheldon, S., Nation, P. D. & Gambetta, J. M. Validating quantum computers using randomized model circuits.Phys. Rev. A100, 032328 (2019).ArticleADSCASGoogle Scholar
44. Blume-Kohout, R. & Young, K. C. A volumetric framework for quantum computer benchmarks.Quantum4, 362 (2020).ArticleGoogle Scholar
45. Wack, A. et al. Quality, speed, and scale: three key attributes to measure the performance of near-term quantum computers. Preprint athttps://arxiv.org/abs/2110.14108(2021).
46. Tomesh, T. et al. SupermarQ: a scalable quantum benchmark suite. In2022 IEEE International Symposium on High-Performance Computer Architecture (HPCA)587–603 (IEEE, 2022).
47. Lubinski, T. et al. Application-oriented performance benchmarks for quantum computing.IEEE Trans. Quantum Eng.4, 1–32 (2023).ArticleGoogle Scholar
48. Proctor, T., Young, K., Baczewski, A. D. & Blume-Kohout, R. Benchmarking quantum computers.Nat. Rev. Phys.7, 105–118 (2025).ArticleGoogle Scholar
49. Hothem, D. et al. Measuring error rates of mid-circuit measurements.Nat. Commun.16, 5761 (2025).ArticleADSPubMedPubMed CentralGoogle Scholar
50. Magesan, E., Gambetta, J. M. & Emerson, J. Characterizing quantum gates via randomized benchmarking.Phys. Rev. A85, 042311 (2012).ArticleADSGoogle Scholar
51. Gaebler, J. P. et al. Suppression of midcircuit measurement crosstalk errors with micromotion.Phys. Rev. A104, 062440 (2021).ArticleADSCASGoogle Scholar
52. Sheldon, S. et al. Characterizing errors on qubit operations via iterative randomized benchmarking.Phys. Rev. A93, 012301 (2016).ArticleADSGoogle Scholar
53. Erhard, A. et al. Characterizing large-scale quantum computers via cycle benchmarking.Nat. Commun.10, 5347 (2019).ArticleADSPubMedPubMed CentralGoogle Scholar
54. Biercuk, M. J. et al. Optimized dynamical decoupling in a model quantum memory.Nature458, 996–1000 (2009).ArticleADSCASPubMedGoogle Scholar
55. Bowler, R. et al. Coherent diabatic ion transport and separation in a multizone trap array.Phys. Rev. Lett.109, 080502 (2012).ArticleADSCASPubMedGoogle Scholar
56. Walther, A. et al. Controlling fast transport of cold trapped ions.Phys. Rev. Lett.109, 080501 (2012).ArticleADSCASPubMedGoogle Scholar
57. Sterk, J. D. et al. Closed-loop optimization of fast trapped-ion shuttling with sub-quanta excitation.npj Quantum Inf.8, 68 (2022).ArticleADSGoogle Scholar
58. Breuckmann, N. P. & Eberhardt, J. N. Quantum low-density parity-check codes.PRX Quantum2, 040101 (2021).ArticleADSGoogle Scholar
59. Ryan-Anderson, C. et al. Implementing fault-tolerant entangling gates on the five-qubit code and the color code. Preprint athttps://arxiv.org/abs/2208.01863(2022).
60. Ryan-Anderson, C. et al. High-fidelity teleportation of a logical qubit using transversal gates and lattice surgery.Science385, 1327–1331 (2024).ArticleADSMathSciNetCASPubMedGoogle Scholar
61. Dasu, S. et al. Breaking even with magic: demonstration of a high-fidelity logical non-Clifford gate. Preprint athttps://arxiv.org/abs/2506.14688(2025).
62. Campbell, E. T. A theory of single-shot error correction for adversarial noise.Quantum Sci. Technol.4, 025006 (2019).ArticleADSGoogle Scholar
63. Berthusen, N. et al. Experiments with the four-dimensional surface code on a quantum charge-coupled device quantum computer.Phys. Rev. A110, 062413 (2024).ArticleADSCASGoogle Scholar
64. Cain, M. et al. Correlated decoding of logical algorithms with transversal gates.Phys. Rev. Lett.133, 240602 (2024).ArticleADSMathSciNetCASPubMedGoogle Scholar
65. Helios paper data.GitHubhttps://github.com/Quantinuum/Helios-paper-data(2023).
66. Sørensen, A. & Mølmer, K. Entanglement and quantum computation with ions in thermal motion.Phys. Rev. A62, 022311 (2000).ArticleADSGoogle Scholar
67. Benhelm, J., Kirchmair, G., Roos, C. F. & Blatt, R. Experimental quantum-information processing with43Ca+ions.Phys. Rev. A77, 062306 (2008).ArticleADSGoogle Scholar
68. Myerson, A. H. et al. High-fidelity readout of trapped-ion qubits.Phys. Rev. Lett.100, 200502 (2008).ArticleADSCASPubMedGoogle Scholar
69. Narayanan, S. et al. Electric field compensation and sensing with a single ion in a planar trap.J. Appl. Phys.110, 114909 (2011).ArticleADSGoogle Scholar
70. Gambetta, J. M. et al. Characterization of addressability by simultaneous randomized benchmarking.Phys. Rev. Lett.109, 240504 (2012).ArticleADSPubMedGoogle Scholar
71. Wallman, J. J. & Emerson, J. Noise tailoring for scalable quantum computation via randomized compiling.Phys. Rev. A94, 052325 (2016).ArticleADSGoogle Scholar
72. Chen, S. et al. The learnability of Pauli noise.Nat. Commun.14, 52 (2023).ArticleADSCASPubMedPubMed CentralGoogle Scholar
73. Mølmer, K., Castin, Y. & Dalibard, J. Monte Carlo wave-function method in quantum optics.J. Opt. Soc. Am. B10, 524–538 (1993).ArticleADSGoogle Scholar
74. Reiter, F. & Sørensen, A. S. Effective operator formalism for open quantum systems.Phys. Rev. A85, 032111 (2012).ArticleADSGoogle Scholar
75. Bowdrey, M. D., Oi, D. K., Short, A., Banaszek, K. & Jones, J. Fidelity of single qubit maps.Phys. Lett. A294, 258–260 (2002).ArticleADSMathSciNetCASGoogle Scholar
76. Uys, H. et al. Decoherence due to elastic Rayleigh scattering.Phys. Rev. Lett.105, 200401 (2010).ArticleADSCASPubMedGoogle Scholar
77. Lee, P. J. et al. Phase control of trapped ion quantum gates.J. Opt. B Quantum Semiclass. Opt.7, S371–S383 (2005).ArticleCASGoogle Scholar
78. Ransford, A., Roman, C., Dellaert, T., McMillin, P. & Campbell, W. C. Weak dissipation for high-fidelity qubit-state preparation and measurement.Phys. Rev. A104, L060402 (2021).ArticleADSCASGoogle Scholar
79. Gaebler, J. et al. Detecting leakage errors in hyperfine qubits. US patent 20,240,211,792 (2023).
80. Sotirova, A. S. et al. High-fidelity heralded quantum state preparation and measurement. Preprint athttps://arxiv.org/abs/2409.05805(2024).
81. Allcock, D. T. C. et al.omgblueprint for trapped ion quantum computing with metastable states.Appl. Phys. Lett.119, 214002 (2021).ArticleADSCASGoogle Scholar
82. Olmschenk, S. et al. Manipulation and detection of a trapped Yb+hyperfine qubit.Phys. Rev. A76, 052314 (2007).ArticleADSGoogle Scholar
83. De, S., Dammalapati, U., Jungmann, K. & Willmann, L. Magneto-optical trapping of barium.Phys. Rev. A79, 041402 (2009).ArticleADSGoogle Scholar
84. Johansen, J., Estey, B., Rowe, M. & Ransford, A. Fast loading of a trapped ion quantum computer using a 2D magneto-optical trap. InProc.2022 IEEE International Conference on Quantum Computing and Engineering (QCE)299–303 (IEEE, 2022).
85. QIR Alliance. QIR specification.GitHubhttps://github.com/qir-alliance/qir-spec.
86. Svore, K. et al. Q#: enabling scalable quantum computing and development with a high-level DSL. InProc. Real World Domain Specific Languages Workshop 2018 (RWDSL2018)1–10 (ACM, 2018).
87. Javadi-Abhari, A. et al. Quantum computing with Qiskit. Preprint athttps://arxiv.org/abs/2405.08810(2024).
88. Cross, A. W., Bishop, L. S., Smolin, J. A. & Gambetta, J. M., Open quantum assembly language. Preprint athttps://arxiv.org/abs/1707.03429(2017).
89. Cross, A. et al. OpenQASM 3: a broader and deeper quantum assembly language.ACM Trans. Quantum Comput.3, 1–50 (2022).ArticleMathSciNetGoogle Scholar
90. Cirq Developers. Cirq.Zenodohttps://zenodo.org/records/16867504(2025).
91. The CUDA-Q development team. CUDA-Q.GitHubhttps://github.com/NVIDIA/cuda-quantum(2025).
92. Quantinuum Systems. Gate streaming documentation.https://docs.quantinuum.com/systems/trainings/getting_started/gate_streaming.html(2025).
93. Christensen, J. E., Hucul, D., Campbell, W. C. & Hudson, E. R. High-fidelity manipulation of a qubit enabled by a manufactured nucleus.npj Quantum Inf.6, 35 (2020).ArticleADSGoogle Scholar
94. Chen, Y.-H. & Baldwin, C. H. Randomized benchmarking with leakage errors.Phys. Rev. Res.7, 043065 (2025).ArticleCASGoogle Scholar
95. Efron, B. & Tibshirani, R.An Introduction to the Bootstrap(Chapman and Hall/CRC, 1993).
96. Moore, I. D. et al. Photon scattering errors during stimulated Raman transitions in trapped-ion qubits.Phys. Rev. A107, 032413 (2023).ArticleADSCASGoogle Scholar
97. Sepiol, M. A. et al. Probing qubit memory errors at the part-per-million level.Phys. Rev. Lett.123, 110503 (2019).ArticleADSCASPubMedGoogle Scholar
98. Hines, J., Hothem, D., Blume-Kohout, R., Whaley, B. & Proctor, T. Fully scalable randomized benchmarking without motion reversal.PRX Quantum5, 030334 (2024).ArticleADSGoogle Scholar
99. Nielsen, M. A. A simple formula for the average gate fidelity of a quantum dynamical operation.Phys. Lett. A303, 249 (2002).ArticleADSMathSciNetCASGoogle Scholar
100. Hangleiter, D. & Eisert, J. Computational advantage of quantum random sampling.Rev. Mod. Phys.95, 035001 (2023).ArticleADSMathSciNetCASGoogle Scholar
101. Boixo, S. et al. Characterizing quantum supremacy in near-term devices.Nat. Phys.14, 595–600 (2018).ArticleCASGoogle Scholar
102. Mayer, K. et al. Theory of mirror benchmarking and demonstration on a quantum computer. Preprint athttps://arxiv.org/abs/2108.10431(2023).
103. Proctor, T. et al. Establishing trust in quantum computations. Preprint athttps://arxiv.org/abs/2204.07568(2026).
104. Proctor, T., Rudinger, K., Young, K., Nielsen, E. & Blume-Kohout, R. Measuring the capabilities of quantum computers.Nat. Phys.18, 75–79 (2022).ArticleCASGoogle Scholar
105. Morvan, A. et al. Phase transitions in random circuit sampling.Nature634, 328–333 (2024).ArticleADSCASPubMedPubMed CentralGoogle Scholar
106. Quantinuum. Random circuit sampling on H2 and Helios.GitHubhttps://github.com/quantinuum/random-circuit-sampling(2024).
107. Gray, J. & Kourtis, S. Hyper-optimized tensor network contraction.Quantum5, 410 (2021).ArticleGoogle Scholar
108. Low, P. J., Zutt, N. C. F., Tathed, G. A. & Senko, C. Quantum logic operations and algorithms in a single 25-level atomic qudit. Preprint athttps://arxiv.org/abs/2507.15799(2025).

Download references

## Acknowledgements

We thank the entire Quantinuum team for numerous contributions that enabled this work. We specifically thank J. Ross for editing the image in Fig.1.

## Funding

The contributions of the Sandia National Laboratories authors were funded in part by the U.S. Department of Energy, Office of Science, Office of Advanced Scientific Computing Research, Quantum Testbed Pathfinder programme. T.P. acknowledges support from an Office of Advanced Scientific Computing Research Early Career Award. Sandia National Laboratories is a multimission laboratory managed and operated by National Technology & Engineering Solutions of Sandia, LLC (NTESS), a wholly owned subsidiary of Honeywell International Inc., for the U.S. Department of Energy’s National Nuclear Security Administration (NNSA) under contract DE-NA0003525. This written work is authored by an employee of NTESS. The employee, not NTESS, owns the right, title and interest in and to the written work and is responsible for its contents. Any subjective views or opinions that might be expressed in the written work do not necessarily represent the views of the U.S. Government. The publisher acknowledges that the U.S. Government retains a non-exclusive, paid-up, irrevocable, worldwide license to publish or reproduce the published form of this written work or allow others to do so, for U.S. Government purposes. The Department of Energy will provide public access to results of federally sponsored research in accordance with the Department of Energy Public Access Plan.

## Author information

### Authors and Affiliations

1. Quantinuum, Broomfield, CO, USAAnthony Ransford, M. S. Allman, J. P. Campora III, Samuel F. Cooper, Robert D. Delaney, Joan M. Dreiling, Brian Estey, Caroline Figgatt, Alex Hall, Akhil Isanaka, Colin J. Kennedy, Ivaylo S. Madjarov, Karl Mayer, Annie J. Park, Adam P. Reed, Riley Ancona, Liz Argueta, Benjamin Arkin, Leonardo Ascarrunz, William Baker, Corey Barnes, John Bartolotta, Jordan Berg, Ryan Besand, Bryce Bjork, Paul Blanchard, Matt Bohn, Daniel Y. Botamanenko, Robert Boutelle, Natalie Brown, Grant T. Buckingham, William Cody Burton, Varis Carey, Joe Chambers, Jia Wen Chan, Victor E. Colussi, Steven Crepinsek, Andrew Cureton, Daniel Davis, Matthew DeCross, Conor Delaney, Davide DelVento, B. J. DeSalvo, Jason Dominy, Sydney Drotar, Neal Erickson, Stephen Erickson, Bruce Evans, Tyler Evans, Maya I. Fabrikant, Andrew Fischer, Cameron Foltz, Michael Foss-Feig, David Francois, Brad Freyberg, Charles Gao, Robert Garay, Jane Garvin, David M. Gaudiosi, Christopher N. Gilbreth, Josh Giles, Erin Glynn, Jeff Graves, Azure Hansen, David Hayes, Tyler Hilbun, Kyle Hoffman, Ian M. Hoffman, Jack Houlton, Jared Hout, Ross Hutson, Ryan T. Jacobs, Trent Jacobs, Jacob Johansen, Loren Jones, Sydney Julian, Ryo Kondo, Chang Kong, Asa Kosto, David Liefer, Michelle Lollie, Dominic Lucchetti, Christian Lytle, Andrew Malm, Spencer Mather, Brian Mathewson, Lauren McCaffrey, Hannah McDougall, Robin Mendoza, David B. Miller, Michael Mills, Louis Narmour, Nhung Nguyen, Lora Nugent, Jeremy Parks, Zach Peters, Jessie Petricka, Juan M. Pino, Frank Polito, Andrew C. Potter, Gabriel Price, McKinley Pugh, Noah Ratcliff, Daisy Raymondson, Peter Rhodes, Conrad Roman, Ciaran Ryan-Anderson, Peter Schow, Peter Shevchuk, Peter Siegfried, Kartik Singhal, Thomas Skripka, Ben Spaun, R. Tucker Sprenkle, Paul Stoufer, Mariel Tader, Raanan Tobey, Anh Tran, Tam Tran, Jim Walker, Quinn Wolf, Jian Zheng, Kristen Zuraski, Charles H. Baldwin, Alex Chernoguzov, John P. Gaebler, Steven J. Sanders, Brian Neyenhuis, Russell Stutz & Justin G. Bohnet
2. Quantinuum, Cambridge, UKJake Arkinstall, Pablo Andres-Martinez, Will Angenent, Agustíin Borgna, John Children, Vanya Eccles, Alec Edgington, Lukas Heidemann, Ariana Hlavaty, Isobel Hooper, Melf Johannsen, Aidan Keay, Mark Koch, Alan Lawrence, Callum MacPherson, Richard Morrison, Craig Roy, Fernando Betanzo Sanchez, George Sangiolo, Tatiana Sawadski, Henry Semenenko, Seyon Sivarajah, Travis H. Thompson, Sam White, Douglas Wilson & Chester Wringe
3. Quantinuum, Brooklyn Park, MN, USAAli A. Husain, Nathaniel Q. Burdick, David Deen, James Hostetter, Daniel Maxwell, Timothy A. Peterson, Andrew Schaffer, Jon Sedlacek, Lucas Sletten, Stephen F. Taylor, Grahame Vittorini, Curtis Volin & Garrett R. Williams
4. Quantinuum, London, UKNikhil Kotibhaskar & Alistair R. Milne
5. Quantinuum, Plymouth, MN, USAMolly P. Andersen, Matt Blain, Christopher J. Carron, Joe Davies, Christopher T. Ertsgaard, Jay Esposito, Bob Higashi, Bob Horning, Ryan Jung, Todd Klein, Scott Olson, Daniel Ouellette, Matthias Preidl & Susan Shore
6. Quantum Performance Laboratory, Sandia National Laboratories, Albuquerque, NM, USARobin Blume-Kohout & Jordan Hines
7. Quantinuum K.K., Tokyo, JapanRoss Duncan, Craig Holliman & Nathan K. Lysne
8. Quantum Performance Laboratory, Sandia National Laboratories, Livermore, CA, USADaniel Hothem, Timothy Proctor & Kevin Young
Authors
1. Anthony RansfordView author publicationsSearch author on:PubMedGoogle Scholar
2. M. S. AllmanView author publicationsSearch author on:PubMedGoogle Scholar
3. Jake ArkinstallView author publicationsSearch author on:PubMedGoogle Scholar
4. J. P. Campora IIIView author publicationsSearch author on:PubMedGoogle Scholar
5. Samuel F. CooperView author publicationsSearch author on:PubMedGoogle Scholar
6. Robert D. DelaneyView author publicationsSearch author on:PubMedGoogle Scholar
7. Joan M. DreilingView author publicationsSearch author on:PubMedGoogle Scholar
8. Brian EsteyView author publicationsSearch author on:PubMedGoogle Scholar
9. Caroline FiggattView author publicationsSearch author on:PubMedGoogle Scholar
10. Alex HallView author publicationsSearch author on:PubMedGoogle Scholar
11. Ali A. HusainView author publicationsSearch author on:PubMedGoogle Scholar
12. Akhil IsanakaView author publicationsSearch author on:PubMedGoogle Scholar
13. Colin J. KennedyView author publicationsSearch author on:PubMedGoogle Scholar
14. Nikhil KotibhaskarView author publicationsSearch author on:PubMedGoogle Scholar
15. Ivaylo S. MadjarovView author publicationsSearch author on:PubMedGoogle Scholar
16. Karl MayerView author publicationsSearch author on:PubMedGoogle Scholar
17. Alistair R. MilneView author publicationsSearch author on:PubMedGoogle Scholar
18. Annie J. ParkView author publicationsSearch author on:PubMedGoogle Scholar
19. Adam P. ReedView author publicationsSearch author on:PubMedGoogle Scholar
20. Riley AnconaView author publicationsSearch author on:PubMedGoogle Scholar
21. Molly P. AndersenView author publicationsSearch author on:PubMedGoogle Scholar
22. Pablo Andres-MartinezView author publicationsSearch author on:PubMedGoogle Scholar
23. Will AngenentView author publicationsSearch author on:PubMedGoogle Scholar
24. Liz ArguetaView author publicationsSearch author on:PubMedGoogle Scholar
25. Benjamin ArkinView author publicationsSearch author on:PubMedGoogle Scholar
26. Leonardo AscarrunzView author publicationsSearch author on:PubMedGoogle Scholar
27. William BakerView author publicationsSearch author on:PubMedGoogle Scholar
28. Corey BarnesView author publicationsSearch author on:PubMedGoogle Scholar
29. John BartolottaView author publicationsSearch author on:PubMedGoogle Scholar
30. Jordan BergView author publicationsSearch author on:PubMedGoogle Scholar
31. Ryan BesandView author publicationsSearch author on:PubMedGoogle Scholar
32. Bryce BjorkView author publicationsSearch author on:PubMedGoogle Scholar
33. Matt BlainView author publicationsSearch author on:PubMedGoogle Scholar
34. Paul BlanchardView author publicationsSearch author on:PubMedGoogle Scholar
35. Robin Blume-KohoutView author publicationsSearch author on:PubMedGoogle Scholar
36. Matt BohnView author publicationsSearch author on:PubMedGoogle Scholar
37. Agustíin BorgnaView author publicationsSearch author on:PubMedGoogle Scholar
38. Daniel Y. BotamanenkoView author publicationsSearch author on:PubMedGoogle Scholar
39. Robert BoutelleView author publicationsSearch author on:PubMedGoogle Scholar
40. Natalie BrownView author publicationsSearch author on:PubMedGoogle Scholar
41. Grant T. BuckinghamView author publicationsSearch author on:PubMedGoogle Scholar
42. Nathaniel Q. BurdickView author publicationsSearch author on:PubMedGoogle Scholar
43. William Cody BurtonView author publicationsSearch author on:PubMedGoogle Scholar
44. Varis CareyView author publicationsSearch author on:PubMedGoogle Scholar
45. Christopher J. CarronView author publicationsSearch author on:PubMedGoogle Scholar
46. Joe ChambersView author publicationsSearch author on:PubMedGoogle Scholar
47. Jia Wen ChanView author publicationsSearch author on:PubMedGoogle Scholar
48. John ChildrenView author publicationsSearch author on:PubMedGoogle Scholar
49. Victor E. ColussiView author publicationsSearch author on:PubMedGoogle Scholar
50. Steven CrepinsekView author publicationsSearch author on:PubMedGoogle Scholar
51. Andrew CuretonView author publicationsSearch author on:PubMedGoogle Scholar
52. Joe DaviesView author publicationsSearch author on:PubMedGoogle Scholar
53. Daniel DavisView author publicationsSearch author on:PubMedGoogle Scholar
54. Matthew DeCrossView author publicationsSearch author on:PubMedGoogle Scholar
55. David DeenView author publicationsSearch author on:PubMedGoogle Scholar
56. Conor DelaneyView author publicationsSearch author on:PubMedGoogle Scholar
57. Davide DelVentoView author publicationsSearch author on:PubMedGoogle Scholar
58. B. J. DeSalvoView author publicationsSearch author on:PubMedGoogle Scholar
59. Jason DominyView author publicationsSearch author on:PubMedGoogle Scholar
60. Sydney DrotarView author publicationsSearch author on:PubMedGoogle Scholar
61. Ross DuncanView author publicationsSearch author on:PubMedGoogle Scholar
62. Vanya EcclesView author publicationsSearch author on:PubMedGoogle Scholar
63. Alec EdgingtonView author publicationsSearch author on:PubMedGoogle Scholar
64. Neal EricksonView author publicationsSearch author on:PubMedGoogle Scholar
65. Stephen EricksonView author publicationsSearch author on:PubMedGoogle Scholar
66. Christopher T. ErtsgaardView author publicationsSearch author on:PubMedGoogle Scholar
67. Jay EspositoView author publicationsSearch author on:PubMedGoogle Scholar
68. Bruce EvansView author publicationsSearch author on:PubMedGoogle Scholar
69. Tyler EvansView author publicationsSearch author on:PubMedGoogle Scholar
70. Maya I. FabrikantView author publicationsSearch author on:PubMedGoogle Scholar
71. Andrew FischerView author publicationsSearch author on:PubMedGoogle Scholar
72. Cameron FoltzView author publicationsSearch author on:PubMedGoogle Scholar
73. Michael Foss-FeigView author publicationsSearch author on:PubMedGoogle Scholar
74. David FrancoisView author publicationsSearch author on:PubMedGoogle Scholar
75. Brad FreybergView author publicationsSearch author on:PubMedGoogle Scholar
76. Charles GaoView author publicationsSearch author on:PubMedGoogle Scholar
77. Robert GarayView author publicationsSearch author on:PubMedGoogle Scholar
78. Jane GarvinView author publicationsSearch author on:PubMedGoogle Scholar
79. David M. GaudiosiView author publicationsSearch author on:PubMedGoogle Scholar
80. Christopher N. GilbrethView author publicationsSearch author on:PubMedGoogle Scholar
81. Josh GilesView author publicationsSearch author on:PubMedGoogle Scholar
82. Erin GlynnView author publicationsSearch author on:PubMedGoogle Scholar
83. Jeff GravesView author publicationsSearch author on:PubMedGoogle Scholar
84. Azure HansenView author publicationsSearch author on:PubMedGoogle Scholar
85. David HayesView author publicationsSearch author on:PubMedGoogle Scholar
86. Lukas HeidemannView author publicationsSearch author on:PubMedGoogle Scholar
87. Bob HigashiView author publicationsSearch author on:PubMedGoogle Scholar
88. Tyler HilbunView author publicationsSearch author on:PubMedGoogle Scholar
89. Jordan HinesView author publicationsSearch author on:PubMedGoogle Scholar
90. Ariana HlavatyView author publicationsSearch author on:PubMedGoogle Scholar
91. Kyle HoffmanView author publicationsSearch author on:PubMedGoogle Scholar
92. Ian M. HoffmanView author publicationsSearch author on:PubMedGoogle Scholar
93. Craig HollimanView author publicationsSearch author on:PubMedGoogle Scholar
94. Isobel HooperView author publicationsSearch author on:PubMedGoogle Scholar
95. Bob HorningView author publicationsSearch author on:PubMedGoogle Scholar
96. James HostetterView author publicationsSearch author on:PubMedGoogle Scholar
97. Daniel HothemView author publicationsSearch author on:PubMedGoogle Scholar
98. Jack HoultonView author publicationsSearch author on:PubMedGoogle Scholar
99. Jared HoutView author publicationsSearch author on:PubMedGoogle Scholar
100. Ross HutsonView author publicationsSearch author on:PubMedGoogle Scholar
101. Ryan T. JacobsView author publicationsSearch author on:PubMedGoogle Scholar
102. Trent JacobsView author publicationsSearch author on:PubMedGoogle Scholar
103. Melf JohannsenView author publicationsSearch author on:PubMedGoogle Scholar
104. Jacob JohansenView author publicationsSearch author on:PubMedGoogle Scholar
105. Loren JonesView author publicationsSearch author on:PubMedGoogle Scholar
106. Sydney JulianView author publicationsSearch author on:PubMedGoogle Scholar
107. Ryan JungView author publicationsSearch author on:PubMedGoogle Scholar
108. Aidan KeayView author publicationsSearch author on:PubMedGoogle Scholar
109. Todd KleinView author publicationsSearch author on:PubMedGoogle Scholar
110. Mark KochView author publicationsSearch author on:PubMedGoogle Scholar
111. Ryo KondoView author publicationsSearch author on:PubMedGoogle Scholar
112. Chang KongView author publicationsSearch author on:PubMedGoogle Scholar
113. Asa KostoView author publicationsSearch author on:PubMedGoogle Scholar
114. Alan LawrenceView author publicationsSearch author on:PubMedGoogle Scholar
115. David LieferView author publicationsSearch author on:PubMedGoogle Scholar
116. Michelle LollieView author publicationsSearch author on:PubMedGoogle Scholar
117. Dominic LucchettiView author publicationsSearch author on:PubMedGoogle Scholar
118. Nathan K. LysneView author publicationsSearch author on:PubMedGoogle Scholar
119. Christian LytleView author publicationsSearch author on:PubMedGoogle Scholar
120. Callum MacPhersonView author publicationsSearch author on:PubMedGoogle Scholar
121. Andrew MalmView author publicationsSearch author on:PubMedGoogle Scholar
122. Spencer MatherView author publicationsSearch author on:PubMedGoogle Scholar
123. Brian MathewsonView author publicationsSearch author on:PubMedGoogle Scholar
124. Daniel MaxwellView author publicationsSearch author on:PubMedGoogle Scholar
125. Lauren McCaffreyView author publicationsSearch author on:PubMedGoogle Scholar
126. Hannah McDougallView author publicationsSearch author on:PubMedGoogle Scholar
127. Robin MendozaView author publicationsSearch author on:PubMedGoogle Scholar
128. David B. MillerView author publicationsSearch author on:PubMedGoogle Scholar
129. Michael MillsView author publicationsSearch author on:PubMedGoogle Scholar
130. Richard MorrisonView author publicationsSearch author on:PubMedGoogle Scholar
131. Louis NarmourView author publicationsSearch author on:PubMedGoogle Scholar
132. Nhung NguyenView author publicationsSearch author on:PubMedGoogle Scholar
133. Lora NugentView author publicationsSearch author on:PubMedGoogle Scholar
134. Scott OlsonView author publicationsSearch author on:PubMedGoogle Scholar
135. Daniel OuelletteView author publicationsSearch author on:PubMedGoogle Scholar
136. Jeremy ParksView author publicationsSearch author on:PubMedGoogle Scholar
137. Zach PetersView author publicationsSearch author on:PubMedGoogle Scholar
138. Timothy A. PetersonView author publicationsSearch author on:PubMedGoogle Scholar
139. Jessie PetrickaView author publicationsSearch author on:PubMedGoogle Scholar
140. Juan M. PinoView author publicationsSearch author on:PubMedGoogle Scholar
141. Frank PolitoView author publicationsSearch author on:PubMedGoogle Scholar
142. Andrew C. PotterView author publicationsSearch author on:PubMedGoogle Scholar
143. Matthias PreidlView author publicationsSearch author on:PubMedGoogle Scholar
144. Gabriel PriceView author publicationsSearch author on:PubMedGoogle Scholar
145. Timothy ProctorView author publicationsSearch author on:PubMedGoogle Scholar
146. McKinley PughView author publicationsSearch author on:PubMedGoogle Scholar
147. Noah RatcliffView author publicationsSearch author on:PubMedGoogle Scholar
148. Daisy RaymondsonView author publicationsSearch author on:PubMedGoogle Scholar
149. Peter RhodesView author publicationsSearch author on:PubMedGoogle Scholar
150. Conrad RomanView author publicationsSearch author on:PubMedGoogle Scholar
151. Craig RoyView author publicationsSearch author on:PubMedGoogle Scholar
152. Ciaran Ryan-AndersonView author publicationsSearch author on:PubMedGoogle Scholar
153. Fernando Betanzo SanchezView author publicationsSearch author on:PubMedGoogle Scholar
154. George SangioloView author publicationsSearch author on:PubMedGoogle Scholar
155. Tatiana SawadskiView author publicationsSearch author on:PubMedGoogle Scholar
156. Andrew SchafferView author publicationsSearch author on:PubMedGoogle Scholar
157. Peter SchowView author publicationsSearch author on:PubMedGoogle Scholar
158. Jon SedlacekView author publicationsSearch author on:PubMedGoogle Scholar
159. Henry SemenenkoView author publicationsSearch author on:PubMedGoogle Scholar
160. Peter ShevchukView author publicationsSearch author on:PubMedGoogle Scholar
161. Susan ShoreView author publicationsSearch author on:PubMedGoogle Scholar
162. Peter SiegfriedView author publicationsSearch author on:PubMedGoogle Scholar
163. Kartik SinghalView author publicationsSearch author on:PubMedGoogle Scholar
164. Seyon SivarajahView author publicationsSearch author on:PubMedGoogle Scholar
165. Thomas SkripkaView author publicationsSearch author on:PubMedGoogle Scholar
166. Lucas SlettenView author publicationsSearch author on:PubMedGoogle Scholar
167. Ben SpaunView author publicationsSearch author on:PubMedGoogle Scholar
168. R. Tucker SprenkleView author publicationsSearch author on:PubMedGoogle Scholar
169. Paul StouferView author publicationsSearch author on:PubMedGoogle Scholar
170. Mariel TaderView author publicationsSearch author on:PubMedGoogle Scholar
171. Stephen F. TaylorView author publicationsSearch author on:PubMedGoogle Scholar
172. Travis H. ThompsonView author publicationsSearch author on:PubMedGoogle Scholar
173. Raanan TobeyView author publicationsSearch author on:PubMedGoogle Scholar
174. Anh TranView author publicationsSearch author on:PubMedGoogle Scholar
175. Tam TranView author publicationsSearch author on:PubMedGoogle Scholar
176. Grahame VittoriniView author publicationsSearch author on:PubMedGoogle Scholar
177. Curtis VolinView author publicationsSearch author on:PubMedGoogle Scholar
178. Jim WalkerView author publicationsSearch author on:PubMedGoogle Scholar
179. Sam WhiteView author publicationsSearch author on:PubMedGoogle Scholar
180. Garrett R. WilliamsView author publicationsSearch author on:PubMedGoogle Scholar
181. Douglas WilsonView author publicationsSearch author on:PubMedGoogle Scholar
182. Quinn WolfView author publicationsSearch author on:PubMedGoogle Scholar
183. Chester WringeView author publicationsSearch author on:PubMedGoogle Scholar
184. Kevin YoungView author publicationsSearch author on:PubMedGoogle Scholar
185. Jian ZhengView author publicationsSearch author on:PubMedGoogle Scholar
186. Kristen ZuraskiView author publicationsSearch author on:PubMedGoogle Scholar
187. Charles H. BaldwinView author publicationsSearch author on:PubMedGoogle Scholar
188. Alex ChernoguzovView author publicationsSearch author on:PubMedGoogle Scholar
189. John P. GaeblerView author publicationsSearch author on:PubMedGoogle Scholar
190. Steven J. SandersView author publicationsSearch author on:PubMedGoogle Scholar
191. Brian NeyenhuisView author publicationsSearch author on:PubMedGoogle Scholar
192. Russell StutzView author publicationsSearch author on:PubMedGoogle Scholar
193. Justin G. BohnetView author publicationsSearch author on:PubMedGoogle Scholar

### Contributions

A.R., C.J.K., A.P.R., A. Chernoguzov, J.P.G., R.S. and J.G.B. conceived and designed the system architecture. A.R., M.S.A., J.A., S.F.C., R.D.D., J.M.D., B. Estey, A. Hall, A.A.H., C.J.K., N.K., I.S.M., A.R.M., A.J.P., A.P.R., R.A., M.P.A., B.A., L.A., W.B., C.B., M. Blain, M. Bohn, D.Y.B., R. Boutelle, G.T.B., W.C.B., V.C., C.J.C., S.C., J. Davies, D. Davis, D. Deen, C.D., B.J.D., S.D., S.E., C.T.E., J.E., T.E., M.I.F., A.F., C. Foltz, D.F., D.M.G., J. Giles, E.G., J. Graves, B. Higashi, T.H., I.M.H., C.H., B. Horning, J. Hostetter, J. Houlton, J. Hout, R.T.J., T.J., J.J., L.J., S.J., R.J., T.K., R.K., C.K., M.L., N.K.L., C.L., A.M., S.M., D.M., L.M., H.M., R. Mendoza, D.B.M., M.M., N.N., L. Nugent, S.O., D.O., J. Parks, Z.P., T.A.P., J. Petricka, J.M.P., F.P., M. Preidl, M. Pugh, N.R., D.R., P.R., C. Roman, C. Roy, A.S., J.S., H.S., P. Shevchuk, S. Shore, P. Siegfried, L.S., B.S., R.T.S., P. Stoufer, S.F.T., T.H.T., R.T., A.T., T.T., C.V., G.R.W., Q.W., J.Z., K.Z., J.P.G. and J.G.B. contributed to the experimental work, including hardware development, operation, measurements and calibrations. M.S.A., J.A., J.P.C., C. Figgatt, A.I., P.A.-M., W.A., L. Argueta, L. Ascarrunz, J. Berg, B.B., P.B., A.B., J. Chambers, J.W.C., J. Children, D. DelVento, V.E., A.E., N.E., B. Evans, C. Foltz, D.F., B.F., R.G., J. Garvin, L.H., A. Hlavaty, K.H., I.H., M.J., A. Keay, M.K., A. Kosto, A.L., D. Liefer, D. Lucchetti, C.M., B.M., R. Morrison, L. Narmour, F.B.S., G.S., T. Sawadski, P. Schow, K.S., S. Sivarajah, T. Skripka, J.W., S.W., D.W., C.W. and A. Chernoguzov contributed to software and control-stack development. K.M., J. Bartolotta, R.B.-K., N.B., V.E.C., M.D., J. Dominy, M.F.-F., C.N.G., D. Hayes, J. Hines, D. Hothem, R.H., T.P., C.R.-A., M.T., K.Y. and C.H.B. contributed to theoretical work, benchmarking and data analysis. A.R., J.P.C., A.A.H., C.J.K., K.M., A.P.R., V.E.C., M.D., D. Hayes, J. Hines, D. Hothem, C.H.B., J.P.G. and J.G.B. wrote or substantially edited the manuscript. R. Besand, R.B.-K., N.Q.B., W.C.B., A. Cureton, R.D., S.E., M.F.-F., C.G., A. Hansen, D. Hayes, J. Hostetter, D. Lucchetti, A.M., B.M., L. Nugent, J. Parks, J.M.P., A.C.P., G.P., T.P., D.R., T. Skripka, B.S., R.T., G.V., K.Y., C.H.B., A. Chernoguzov, J.P.G., S.J.S., B.N., R.S. and J.G.B. supervised the project. All authors discussed the results and reviewed the manuscript.

### Corresponding author

Correspondence toAnthony Ransford.

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Peer review

### Peer review information

Naturethanks Roee Ozeri, Arghavan Safavi-Naini and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.Peer reviewer reportsare available.

## Additional information

Publisher’s noteSpringer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Extended data figures and tables

### Extended Data Fig. 1 Three types of measurement are available in all eight quantum operation zones that make use of optical (2S1/2,2D5/2), metastable (2D5/2) and ground-state (2S1/2) superpositions.

All measurements are made with the target ion displaced from the RF null to reduce stray light interacting with non-measured ions51, as shown with double arrows.a, Standard measurement occurs when the user specifies a measurement but not for all of the qubits in the batch.b, Protected measurement occurs when the compiler detects an entire batch of qubits will be measured, such as at the end-of-program measurement. Protected measurement performs the2D5/2mapping operations on both qubits before state detection, such that crosstalk from 493-nm detection light does not affect the measurement outcome.c, User-specified ternary measurement allows the user to obtain a result of 0, 1 orL, in whichLindicates leakage out of the qubit manifold. In this case, each qubit state amplitude is mapped to different parts of the2D5/2manifold108and any remaining population in the2S1/2population (representing leakage errors) is measured by induced fluorescence with the 493-nm and 650-nm lasers. Afterwards, a series of pulses independently maps each state amplitude back into the2S1/2and2D3/2manifolds, allowing measurement of the qubit state (0 or 1). Ternary and protected measurements can be combined when an entire batch is measured.d, Energy-level diagram for137Ba+with2S1/2ground-state manifold used for storage and quantum operations, optical superpositions of2S1/2and2D5/2are used during standard measurement. An optical superposition shelves the qubit ground state |0⟩state to the2D5/2manifold for measurement.e, Metastable superpositions in the2D5/2are used for ternary measurements by shelving both ground-state qubit levels to detect leakage errors.

### Extended Data Fig. 2 1QRB data.

a, 1QRB success probability as a function of sequence length for the 16 qubits occupying the eight operation zones.b, 1QRB measured leakage population as a function of sequence length. The leakage rate is combined with the success decay rate to compute the 1Q Clifford infidelity.c, Breakdown of 1Q Clifford error rates into computational (‘Comp.’) errors and leakage (‘Leak.’) errors for the 16 individual qubits. Label locations correspond to qubit locations in Fig.2b, with qubits 0–7 in the top operation zones and qubits 8–15 in the bottom operation zones (two per zone ordered left to right). Each random circuit is run with 100 shots. Error bars are one-sigma confidence intervals constructed from bootstrap resampling.

### Extended Data Fig. 3 2QRB data.

a, 2QRB success probability as a function of sequence length for 8-qubit pairs in the eight operation zones. Sequence length here refers to the number of Clifford group elements.b, 2QRB measured leakage rate as a function of sequence length. The leakage rate is combined with the success decay rate to compute the 2Q infidelity.c, Breakdown ofRZZ(π/2) errors into computational and leakage errors for the 8-qubit pairs. Label locations correspond to qubit locations in Fig.2b, with qubits 0–7 in the top operation zones and qubits 8–15 in the bottom operation zones (two per zone ordered left to right). Each random circuit is run with 100 shots. Error bars are one-sigma confidence intervals constructed from bootstrap resampling.

### Extended Data Fig. 4 2QCB data.

a–h, Pauli expectation values and measured leakage rate as a function of sequence length for the eight operation zones in the order of Fig.2.i, Pauli error probabilities and leakage survival probability for the nativeRZZ(π/2) gate, up to unlearnable degrees of freedom, for the eight operation zones. Each random circuit is run with 100 shots. Error bars are one-sigma confidence intervals constructed from bootstrap resampling.

### Extended Data Fig. 5 Transport-1QRB is run with all 98 qubits grouped into four groups that have different numbers of random depth-1 transport operations between each 1Q Clifford gate per group.

a, Success probability as a function of Clifford sequence length.b, Measured leakage population as a function of Clifford sequence length.c, Qubit-averaged leakage rate (dashed curve) and total memory error (solid curve) as a function of the number of depth-1 transport operations. Each random circuit is run with 100 shots. Error bars are one-sigma confidence intervals constructed from bootstrap resampling.

## Supplementary information

### Supplementary information (download PDF)

Supplementary Sections 1–3, including Supplementary Figs. 1–6 and Supplementary Tables 1–8.

### Peer Review File (download PDF)

## Rights and permissions

Open AccessThis article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visithttp://creativecommons.org/licenses/by-nc-nd/4.0/.

Reprints and permissions

## About this article

### Cite this article

Ransford, A., Allman, M.S., Arkinstall, J.et al.A 98-qubit trapped-ion quantum computer with all-to-all connectivity.Nature(2026). https://doi.org/10.1038/s41586-026-10676-4

Download citation

* Received:16 November 2025
* Accepted:18 May 2026
* Published:17 June 2026
* Version of record:17 June 2026
* DOI:https://doi.org/10.1038/s41586-026-10676-4

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative