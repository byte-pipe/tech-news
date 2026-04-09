---
title: "That time I wasted weeks hand optimizing assembly because I benchmarked on random data – Vidar's Blog"
url: https://www.vidarholen.net/contents/blog/?p=1160
date: 2025-07-25
site: hackernews
model: llama3.2:1b
summarized_at: 2025-07-25T23:33:51.571411
---

# That time I wasted weeks hand optimizing assembly because I benchmarked on random data – Vidar's Blog

Analysis:

From a solo developer business perspective, this article discusses the frustration and excitement of optimizing Java code for high-performance computing. The author shares their experience on optimizing VarInt encoding, which requires clever use of assembly language to achieve optimal performance.

The target system is a distributed data processing platform with hundreds of thousands of machines, making 0.5% improvement in performance equivalent to a salary increase. The author mentions that no prior optimization efforts had yielded such significant results.

From a market perspective, it's clear that there is demand for high-performance Java optimization solutions. The article highlights the limited use of optimized string allocation and primitive types (e.g., char) in the target system, while also mentioning the importance of binary serialization for compatible formats like Google Protobuf and Apache/Facebook Thrift.

The technical feasibility of a solo developer's entry into this market is quite high. Assembly language expertise suggests that the author has the necessary skills to tackle complex optimization tasks. The use of BMI2, AVX2, and bit extensions implies that the codebase can be modified to leverage modern CPU architectures for improved performance.

Business viability indicators from this perspective include:

* Limited demand: No prior success stories or mentions of clients paying top dollar for such optimizations.
* High expertise requirement: The author's extensive experience in high-performance assembly optimization suggests a need for specialized skills and expertise.
* Profit potential: A 4x improvement in VarInt encoding efficiency translates to a monetary gain, but the exact nature of this profit (e.g., via consulting or licensing) is unclear.

Actionable insights from this analysis include:

1. **Developing high-performance assembly optimization skills**: Assemble Java code for specific use cases where optimizations are feasible and profitable.
2. **Targeted market selection**: Focus on systems with limited native code optimizations or where VarInt encoding can be beneficial.
3. **Understanding the industry landscape**: Research existing companies offering similar services to identify gaps in demand and competitors.

Specific numbers mentioned:

* 4x improvement in VarInt encoding efficiency (verified via benchmark)
* 32-bit int requires between 1-5 bytes of CPU time for optimal performance
* Google Protobuf and Apache/Facebook Thrift use VarInt encoding

Quotes about pain points:

* "The empire builders in management were additionally competing in a Manifest Destiny style land grab as the company maneuvered to take control of its tech stack from end to end." (referring to the company's competition and efforts.)
* "We were itching to use it" (referring to the need for optimization skills.)

Mentions of pricing or revenue:

* N/A (no specific figures mentioned)
