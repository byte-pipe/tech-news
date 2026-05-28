---
title: Amazon Thinks the Future of Data Centers Depends on a Technical Problem It Just Solved | WIRED
url: https://www.wired.com/story/amazon-thinks-the-future-of-data-centers-depends-on-a-technical-problem-it-just-solved/
date: 2026-05-28
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-05-29T04:39:32.758014
---

# Amazon Thinks the Future of Data Centers Depends on a Technical Problem It Just Solved | WIRED

# Amazon Thinks the Future of Data Centers Depends on a Technical Problem It Just Solved

## Breakthrough Overview
- AWS reports a major networking breakthrough deployed since late 2023.  
- Introduces a “quasi‑random” design called RNG (Resilient Network Graphs) that blends structured and random topologies.  
- Aims to increase data speeds while cutting energy use and hardware count.

## Technical Details
- RNG flattens the network, removing bottlenecks inherent in traditional “fat‑tree” designs.  
- Amazon created a new optical device, the ShuffleBox, which automatically re‑arranges cables for the quasi‑random layout.  
- Compared with conventional networks, AWS claims:  
  - 69 % fewer routers and switches  
  - 33 % higher data throughput  
  - 40 % lower network power consumption  
  - 27 % reduction in operating costs  

## Research Background
- Builds on decades of random‑graph research, notably the 2012 “Jellyfish” paper from the University of Illinois Urbana‑Champaign.  
- An AWS team (including Giacomo Bernardi, Ratul Mahajan, Seshadhri Comandur) began work in 2023, recruiting several academic experts.  
- Early simulations using Penrose tiling proved unreliable; success arrived after adopting a quasi‑random “chaos‑embracing” approach.

## Deployment
- First RNG implementation launched in a Dublin data center in 2024.  
- Subsequent rollouts to sites in Germany and Spain.  
- Amazon states that most newly built data centers now incorporate the RNG protocol.

## Industry Context
- Since the mid‑1980s, data‑center networks have largely used a “fat‑tree” topology—layered switches with high‑bandwidth “fat” nodes at the top.  
- Fat‑tree designs are reliable but rigid, require complex physical cabling, and incur high material costs.  
- Google experimented with optical circuit switching (OCS), which adds engineering complexity and expense.  
- Amazon’s RNG seeks a simpler, more scalable cabling scheme while maintaining performance.

## Expert Commentary
- Brighten Godfrey (University of Illinois) calls real‑world deployment of large‑scale random graphs “remarkable.”  
- Matt Rehder, AWS Vice President of Network Engineering, says AWS is the only company to achieve this design at scale.

## Implications
- Improves efficiency for general cloud workloads; AI training workloads still favor more coordinated, non‑random patterns.  
- Positions Amazon with a potential competitive advantage as customers demand faster, greener, and more cost‑effective data‑center infrastructure.