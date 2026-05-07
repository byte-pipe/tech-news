---
title: 'AlphaEvolve: Gemini-powered coding agent scaling impact across fields — Google DeepMind'
url: https://deepmind.google/blog/alphaevolve-impact/
site_name: hackernews_api
content_file: hackernews_api-alphaevolve-gemini-powered-coding-agent-scaling-im
fetched_at: '2026-05-07T20:12:50.805709'
original_url: https://deepmind.google/blog/alphaevolve-impact/
author: AlphaEvolve team
date: '2026-05-07'
published_date: '2026-05-07T16:00:00+00:00'
description: Discover how AlphaEvolve optimizes algorithms for genomics, quantum physics, global infrastructure, and more to accelerate scientific progress and solve real-world challenges.
tags:
- hackernews
- trending
---

May 7, 2026 
Science

# AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields

AlphaEvolve team

 
 
 
Share
 Your browser does not support the video tag.
 Your browser does not support the video tag.

A year ago, we introducedAlphaEvolve, a Gemini-powered coding agent for designing advanced algorithms. We showed that AlphaEvolve can help make new discoveries on open problems across mathematics and computer science, and optimize algorithms that have since been deployed across critical parts of Google’s infrastructure.

Today, because algorithms are part of nearly every aspect of life, the landscape of what AlphaEvolve can achieve is even broader. From helping explain the physics of the natural world to powering electricity grids and computing infrastructure, there are countless ways AlphaEvolve can help accelerate progress for scientists and businesses across a variety of fields.

We’re excited to share a collection of AlphaEvolve’s most significant impact to date.

## Driving social impact and sustainability

AlphaEvolve has helped uncover key connections in health and sustainability research.

In genomics, AlphaEvolve was used to improveDeepConsensus—a model developed by Google Research for correcting DNA sequencing errors— achieving a 30% reduction in variant detection errors. These improvements are helping scientists atPacBioanalyze genetic data more accurately and at a lower cost.

“The solution the Google team discovered using AlphaEvolve unlocks meaningfully higher accuracy rates for our sequencing instruments. For researchers, this higher-quality data might enable the discovery of previously hidden disease causing mutations.”— Aaron Wenger, Senior Director at PacBio

In grid optimization, AlphaEvolve was applied to theAC Optimal Power Flow problem. It helped increase the ability of our trained Graph Neural Network (GNN) model to find feasible solutions for the problem from 14% to over 88%, significantly reducing the need for other costly post-processing steps for electricity grids.

In earth sciences, AlphaEvolve translated complex geospatial data into more reliable, actionable insights. By helping automate the optimization ofEarth AImodels,the overall accuracy of predicting the risk of natural disaster—aggregated across 20 categories such as wildfires, floods, and tornadoes—was increased by 5%.

## Advancing the frontiers of research

AlphaEvolve is serving as a powerful research partner, accelerating discovery across the sciences.

In quantum physics, AlphaEvolve’s optimizations have made it possible to run complex molecular simulations onGoogle’s Willow quantum processorbysuggesting quantum circuits with 10x lower errorthan previous conventionally optimized baselines. This has enabled immediate impactful contributions to first-of-a-kind experimental demonstrations of quantum computing — and it points toward a future where AlphaEvolve helps find algorithms that exceed the capabilities of classical computers.

Working with world-renowned mathematicians like Terence Tao, the system has helped solveErdős problems.

“Tools such as AlphaEvolve are giving mathematicians very useful new capabilities. For optimization problems in particular, we can now quickly test potential inequalities for counterexamples, or to confirm our beliefs in what the extremizers are, which greatly improves our intuition about these problems and allows us to find rigorous proofs more readily.” —Terence Tao, Professor of Mathematics at UCLA

AlphaEvolve has also broken records for classic mathematical challenges, including improving lower bounds for theTraveling Salesman ProblemandRamsey Numbers.

Furthermore, this capacity for autonomous discovery is driving parallel innovations across other diverse domains — fromdiscovering interpretable neuroscience modelsandproving new market limits in microeconomics, to rapidly advancingneural network building blocks,cryptography for user privacy,synthetic data generation, andcritical safety mitigationsfor frontier AI models.

 Your browser does not support the video tag.
 Your browser does not support the video tag.

AlphaEvolveoptimizingan instance of the "Tammes problem". You can explore a selection of additional problems for which AlphaEvolve generated potential solutions in the publicGallery.

## Improving AI infrastructure

AlphaEvolve has graduated from pilot testing to becoming a core component of our infrastructure. AlphaEvolve has been used as a regular tool to optimize the design of the next generation ofTPUs. It also helped discover more efficientcache replacement policies, achieving in two days what previously required a concerted, human-intensive effort spanning months.

“AlphaEvolve began optimizing the lowest levels of hardware powering our AI stacks. It proposed a circuit design so counterintuitive yet efficient that it was integrated directly into the silicon of our next-generation TPUs. This is the latest example of TPU brains helping design next-generation TPU bodies.” — Jeff Dean, Chief Scientist, Google DeepMind and Google Research

AlphaEvolve improved the efficiency ofGoogle Spannerby refining itsLog-Structured Merge-treecompaction heuristics. This optimization reduced 'write amplification'—the ratio of data written to storage versus the original request—by 20%. It also provided insights fornew compiler optimization strategiesthat reduced the storage footprint of software by nearly 9%.

## Scaling commercial applications

Together with Google Cloud, we are now bringing the power of AlphaEvolve to a variety of commercial enterprises across industries.

* In financial services,Klarnaused the system to optimize one of its largest transformer models — doubling its training speed whilst improving model quality.
* In semiconductor manufacturing,Substrateapplied AlphaEvolve to its computational lithography framework, achieving a multi-fold increase in runtime speed, enabling them to run significantly larger simulations of advanced semiconductors.
* In logistics,FM Logisticused the technology to optimize complex routing challenges like the Traveling Salesman Problem, finding 10.4% improvement in routing efficiency over the previous heavily optimized solutions — saving over 15,000 kilometers of distance travelled annually.
* In advertising and marketing,WPPused AlphaEvolve to refine AI model components, navigating complex, high-dimensional campaign data and achieving 10% accuracy gains over their competitive manual model optimizations.
* In computational material and life sciences,Schrödingerapplied AlphaEvolve to achieve a roughly 4x speedup in both Machine Learned Force Fields (MLFF) training and inference.

“AlphaEvolve allows us to explore larger chemical spaces faster and more efficiently than ever before. Faster MLFF inference carries real business impact, shortening R&D cycles in drug discovery, catalyst design, and materials development, and enabling companies to screen molecular candidates in days rather than months.”— Gabriel Marques, Technical Lead of Machine Learning at Schrödinger.

## The future of AlphaEvolve

The past year shows how AlphaEvolve is rapidly becoming a versatile, general-purpose system. It is demonstrating that the next breakthroughs will be driven by algorithms that can learn, evolve and optimize themselves. As we look ahead, we are excited to expand these capabilities, and bring the power of this technology to an even broader set of external challenges.

## Acknowledgements

AlphaEvolve was developed by Matej Balog, Alexander Novikov, Ngân Vũ, Marvin Eisenberger, Emilien Dupont, Po-Sen Huang, Adam Zsolt Wagner, Sergey Shirobokov, Borislav Kozlovskii, Francisco J. R. Ruiz, Abbas Mehrabian, M. Pawan Kumar, Abigail See, Swarat Chaudhuri, George Holland, Alex Davies, Sebastian Nowozin, and Pushmeet Kohli. This research was developed as part of a broader initiative focused on using AI for algorithm discovery. Following the initial development, Alexey Cherepanov, Anindya Basu, Becky Evangelakos, Jamie Smith, and Mario Pinto joined the team to scale AlphaEvolve’s impact.

Adam Connors, Alex Bäuerle, Anna Trostanetski, Fernanda Viegas, Gabi Cardoso, Jonathan Caton, Lucas Dixon, Mariana Felix, Martin Wattenberg, Matin Akhlaghinia, Richard Green, Yosuke Ushigome, and Yunhan Xu collaborated with our team to develop the AlphaEvolve UI, with support from many others.

Anant Nawalgaria, Diego Ballesteros, Gemma Jennings, Jakob Oesinghaus, Kartik Sanu, Laurynas Tamulevičius, Nicolas Stroppa, Nishta Dhawan, Oliver Hilsenbeck, Reah Miyara, Skander Hannachi, Tom Beyer, and Vishal Agarwal collaborated with our team to develop the AlphaEvolve API and engage with Google Cloud customers, with support from many others.

We gratefully acknowledge our collaborators for leading applications of AlphaEvolve on critical problems and contributing to this report: Aaron Wenger, Abhradeep Guha Thakurta, Akanksha Jain, Alex Vitvitskyi, Amir Yazdan Bakhsh, Andrew Carroll, Aranyak Mehta, Arthur Conmy, Ansh Nagda, Davide Paglieri, Eric Perim Martins, Hassler Thurston, Hongzheng Chen, Jack Mason, János Kramár, Jeremy Ratcliff, Jessica Sapick, Johannes Bausch, Jonathan Katz, Kevin Miller, Kim Stachenfeld, Mark Kurzeja, Mircea Trofin, Myriam Khan, Nero Geng, Pablo Samuel Castro, Petar Veličković, Pi-Chuan Chang, Prabhakar Raghavan, Raghav Gupta, Rohin Shah, Sasha Vezhnevets, Sébastien Lahaie, Sergio Guadarrama, Shravya Shetty, Shruthi Gorantala, Terence Tao, Todd Lipcon, Tom O'Brien, Vinod Nair, Ziyue Wang, Zun Li, among many other users of AlphaEvolve.

Finally, we thank our leadership for their guidance and support: Amin Vahdat, Ankur Jain, Demis Hassabis, Jeff Dean, Parthasarathy Ranganathan, Pushmeet Kohli, Saurabh Tiwary, and Sundar Pichai. We also extend our gratitude to our partner teams across Google DeepMind, Google Cloud, Google Labs, Google Research, and other product areas for enabling the applications and products powered by AlphaEvolve.

### Related posts

### AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms

May 2025
Science
 
 
Learn more