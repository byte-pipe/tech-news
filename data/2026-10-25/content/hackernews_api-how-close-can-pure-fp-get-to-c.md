---
title: How close can pure FP get to C?
url: https://rtfeldman.com/fp-vs-c
site_name: hackernews_api
content_file: hackernews_api-how-close-can-pure-fp-get-to-c
fetched_at: '2026-10-25T02:57:05.116866'
original_url: https://rtfeldman.com/fp-vs-c
author: stmonty
date: '2026-10-24'
description: How close can pure functional programming get to C?
tags:
- hackernews
- trending
---

# How close can pure FP get to C?

October 22, 2026

InWhy Lean is Faster Than Rust, the author shares an impressive result: aDEFLATE compressionlibrary written inLean 4, a functional programming language and proof assistant, outperforming an equivalent Rust package thatcrates.io sayshas been downloadedover a billion times.From the article:

lean-zipbeats every single compression levelminiz_oxideprovides, i.e. we're capable of providing the same compression at higher throughput. At its fastest setting we're 15% quicker and the output is 8.8% smaller.

However, the article also notes that while they managed to surpass Rust'sminiz_oxide, they were no match for the end boss of DEFLATE performance:libdeflate, written in C.

lean-zipis certainly not the best here:libdeflateunsurprisingly blows it out of the water (unsurprisingly because this is a very carefully tuned implementation using architecture-specific SIMD, that we can't touch in Lean).

EnterRoc, a functional programming language (but not a theorem prover) with an explicit focus on runtime performance.

Roc's tagline is "Fast, Friendly, Functional," andFast comes firstbecause both running fastandcompiling fast have always been central goals. Roc is not a mature language (it's still weeks away from its first numbered release, 0.1.0), and its nascent package ecosystem has had almost no optimization work done on it. Still, between its language design,longstanding optimizations, andbrand-new compiler implementation, I figured Roc already had enough of a foundation in place to take on the champ: libdeflate.

So I spent a bunch of time grinding through performance optimizations onroc-deflate, a packageNiclas Ahdenwrote (anduses in paid production work) for DEFLATE compression. I didn't expect to beat libdeflate's performance across the board, but I wanted to see how close it could get on the non-streaming APIs (as roc-deflate hasn't implemented streaming yet), using the classic Silesia corpus for benchmarking and verifying that it produced identical outputs.

## Under 10% Slower

Here's where the benchmarks stand today, running on the 2021 M1 MacBook Pro where I did all the optimization work, as well as on an AMD Ryzen 9 3900X Ubuntu machine for an x64 comparison.

roc-deflate ran these 144 benchmarks slower on average than libdeflate, in the median case8.9%slower on the Ryzen 3900X, and2.6%on the M1 MacBook Pro.

### Compression on Silesia corpus

M1 MacBook Pro

Ryzen 3900X Ubuntu

MB/s

700

600

500

400

300

200

100

0

file that ran fastest

file that ran slowest

L1

L2

L3

L4

L5

L6

L7

L8

L9

L10

L11

L12

libdeflate

roc-deflate

libdeflate at L1 compression

230.57 MB/s compressing dickens

(median across 15 runs)

libdeflate at L1 compression

248.31 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L1 compression

312.26 MB/s compressing mr

(median across 15 runs)

libdeflate at L1 compression

601.03 MB/s compressing nci

(median across 15 runs)

libdeflate at L1 compression

169.98 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L1 compression

284.01 MB/s compressing osdb

(median across 15 runs)

libdeflate at L1 compression

281.14 MB/s compressing reymont

(median across 15 runs)

libdeflate at L1 compression

344.00 MB/s compressing samba

(median across 15 runs)

libdeflate at L1 compression

160.21 MB/s compressing sao

(median across 15 runs)

libdeflate at L1 compression

268.58 MB/s compressing webster

(median across 15 runs)

libdeflate at L1 compression

145.93 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L1 compression

476.83 MB/s compressing xml

(median across 15 runs)

roc-deflate at L1 compression

202.92 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L1 compression

225.79 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L1 compression

277.57 MB/s compressing mr

(median across 15 runs)

roc-deflate at L1 compression

529.49 MB/s compressing nci

(median across 15 runs)

roc-deflate at L1 compression

153.99 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L1 compression

257.14 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L1 compression

245.80 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L1 compression

309.79 MB/s compressing samba

(median across 15 runs)

roc-deflate at L1 compression

145.28 MB/s compressing sao

(median across 15 runs)

roc-deflate at L1 compression

239.18 MB/s compressing webster

(median across 15 runs)

roc-deflate at L1 compression

134.66 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L1 compression

419.07 MB/s compressing xml

(median across 15 runs)

libdeflate at L2 compression

161.68 MB/s compressing dickens

(median across 15 runs)

libdeflate at L2 compression

184.55 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L2 compression

204.86 MB/s compressing mr

(median across 15 runs)

libdeflate at L2 compression

453.14 MB/s compressing nci

(median across 15 runs)

libdeflate at L2 compression

128.05 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L2 compression

203.10 MB/s compressing osdb

(median across 15 runs)

libdeflate at L2 compression

207.66 MB/s compressing reymont

(median across 15 runs)

libdeflate at L2 compression

249.57 MB/s compressing samba

(median across 15 runs)

libdeflate at L2 compression

112.78 MB/s compressing sao

(median across 15 runs)

libdeflate at L2 compression

198.86 MB/s compressing webster

(median across 15 runs)

libdeflate at L2 compression

117.18 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L2 compression

352.59 MB/s compressing xml

(median across 15 runs)

roc-deflate at L2 compression

143.60 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L2 compression

168.37 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L2 compression

182.07 MB/s compressing mr

(median across 15 runs)

roc-deflate at L2 compression

409.82 MB/s compressing nci

(median across 15 runs)

roc-deflate at L2 compression

118.08 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L2 compression

185.41 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L2 compression

183.69 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L2 compression

228.02 MB/s compressing samba

(median across 15 runs)

roc-deflate at L2 compression

105.68 MB/s compressing sao

(median across 15 runs)

roc-deflate at L2 compression

181.07 MB/s compressing webster

(median across 15 runs)

roc-deflate at L2 compression

107.00 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L2 compression

323.17 MB/s compressing xml

(median across 15 runs)

libdeflate at L3 compression

130.85 MB/s compressing dickens

(median across 15 runs)

libdeflate at L3 compression

169.26 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L3 compression

171.11 MB/s compressing mr

(median across 15 runs)

libdeflate at L3 compression

415.29 MB/s compressing nci

(median across 15 runs)

libdeflate at L3 compression

118.92 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L3 compression

183.10 MB/s compressing osdb

(median across 15 runs)

libdeflate at L3 compression

169.42 MB/s compressing reymont

(median across 15 runs)

libdeflate at L3 compression

223.27 MB/s compressing samba

(median across 15 runs)

libdeflate at L3 compression

100.60 MB/s compressing sao

(median across 15 runs)

libdeflate at L3 compression

173.36 MB/s compressing webster

(median across 15 runs)

libdeflate at L3 compression

116.62 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L3 compression

324.65 MB/s compressing xml

(median across 15 runs)

roc-deflate at L3 compression

122.04 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L3 compression

158.29 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L3 compression

159.07 MB/s compressing mr

(median across 15 runs)

roc-deflate at L3 compression

382.21 MB/s compressing nci

(median across 15 runs)

roc-deflate at L3 compression

111.14 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L3 compression

171.27 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L3 compression

157.19 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L3 compression

209.86 MB/s compressing samba

(median across 15 runs)

roc-deflate at L3 compression

95.51 MB/s compressing sao

(median across 15 runs)

roc-deflate at L3 compression

162.75 MB/s compressing webster

(median across 15 runs)

roc-deflate at L3 compression

105.93 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L3 compression

300.31 MB/s compressing xml

(median across 15 runs)

libdeflate at L4 compression

119.94 MB/s compressing dickens

(median across 15 runs)

libdeflate at L4 compression

158.07 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L4 compression

156.88 MB/s compressing mr

(median across 15 runs)

libdeflate at L4 compression

376.70 MB/s compressing nci

(median across 15 runs)

libdeflate at L4 compression

113.68 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L4 compression

164.59 MB/s compressing osdb

(median across 15 runs)

libdeflate at L4 compression

152.16 MB/s compressing reymont

(median across 15 runs)

libdeflate at L4 compression

207.97 MB/s compressing samba

(median across 15 runs)

libdeflate at L4 compression

94.48 MB/s compressing sao

(median across 15 runs)

libdeflate at L4 compression

158.64 MB/s compressing webster

(median across 15 runs)

libdeflate at L4 compression

116.63 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L4 compression

294.31 MB/s compressing xml

(median across 15 runs)

roc-deflate at L4 compression

113.71 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L4 compression

148.77 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L4 compression

149.00 MB/s compressing mr

(median across 15 runs)

roc-deflate at L4 compression

356.47 MB/s compressing nci

(median across 15 runs)

roc-deflate at L4 compression

107.59 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L4 compression

156.41 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L4 compression

142.45 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L4 compression

197.17 MB/s compressing samba

(median across 15 runs)

roc-deflate at L4 compression

89.37 MB/s compressing sao

(median across 15 runs)

roc-deflate at L4 compression

151.15 MB/s compressing webster

(median across 15 runs)

roc-deflate at L4 compression

106.32 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L4 compression

278.53 MB/s compressing xml

(median across 15 runs)

libdeflate at L5 compression

95.14 MB/s compressing dickens

(median across 15 runs)

libdeflate at L5 compression

133.06 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L5 compression

129.45 MB/s compressing mr

(median across 15 runs)

libdeflate at L5 compression

287.09 MB/s compressing nci

(median across 15 runs)

libdeflate at L5 compression

95.87 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L5 compression

140.08 MB/s compressing osdb

(median across 15 runs)

libdeflate at L5 compression

120.63 MB/s compressing reymont

(median across 15 runs)

libdeflate at L5 compression

170.75 MB/s compressing samba

(median across 15 runs)

libdeflate at L5 compression

83.22 MB/s compressing sao

(median across 15 runs)

libdeflate at L5 compression

125.60 MB/s compressing webster

(median across 15 runs)

libdeflate at L5 compression

102.48 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L5 compression

229.70 MB/s compressing xml

(median across 15 runs)

roc-deflate at L5 compression

90.27 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L5 compression

125.87 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L5 compression

122.34 MB/s compressing mr

(median across 15 runs)

roc-deflate at L5 compression

311.35 MB/s compressing nci

(median across 15 runs)

roc-deflate at L5 compression

89.73 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L5 compression

133.37 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L5 compression

115.52 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L5 compression

167.01 MB/s compressing samba

(median across 15 runs)

roc-deflate at L5 compression

76.99 MB/s compressing sao

(median across 15 runs)

roc-deflate at L5 compression

123.12 MB/s compressing webster

(median across 15 runs)

roc-deflate at L5 compression

90.40 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L5 compression

237.29 MB/s compressing xml

(median across 15 runs)

libdeflate at L6 compression

70.60 MB/s compressing dickens

(median across 15 runs)

libdeflate at L6 compression

107.04 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L6 compression

96.85 MB/s compressing mr

(median across 15 runs)

libdeflate at L6 compression

221.32 MB/s compressing nci

(median across 15 runs)

libdeflate at L6 compression

82.91 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L6 compression

122.89 MB/s compressing osdb

(median across 15 runs)

libdeflate at L6 compression

79.91 MB/s compressing reymont

(median across 15 runs)

libdeflate at L6 compression

129.19 MB/s compressing samba

(median across 15 runs)

libdeflate at L6 compression

67.48 MB/s compressing sao

(median across 15 runs)

libdeflate at L6 compression

96.76 MB/s compressing webster

(median across 15 runs)

libdeflate at L6 compression

102.50 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L6 compression

178.60 MB/s compressing xml

(median across 15 runs)

roc-deflate at L6 compression

72.83 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L6 compression

107.54 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L6 compression

98.92 MB/s compressing mr

(median across 15 runs)

roc-deflate at L6 compression

246.59 MB/s compressing nci

(median across 15 runs)

roc-deflate at L6 compression

81.43 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L6 compression

122.02 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L6 compression

84.85 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L6 compression

134.11 MB/s compressing samba

(median across 15 runs)

roc-deflate at L6 compression

66.36 MB/s compressing sao

(median across 15 runs)

roc-deflate at L6 compression

101.16 MB/s compressing webster

(median across 15 runs)

roc-deflate at L6 compression

90.67 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L6 compression

194.35 MB/s compressing xml

(median across 15 runs)

libdeflate at L7 compression

54.23 MB/s compressing dickens

(median across 15 runs)

libdeflate at L7 compression

75.96 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L7 compression

66.46 MB/s compressing mr

(median across 15 runs)

libdeflate at L7 compression

157.22 MB/s compressing nci

(median across 15 runs)

libdeflate at L7 compression

70.52 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L7 compression

117.53 MB/s compressing osdb

(median across 15 runs)

libdeflate at L7 compression

46.77 MB/s compressing reymont

(median across 15 runs)

libdeflate at L7 compression

91.00 MB/s compressing samba

(median across 15 runs)

libdeflate at L7 compression

59.49 MB/s compressing sao

(median across 15 runs)

libdeflate at L7 compression

71.34 MB/s compressing webster

(median across 15 runs)

libdeflate at L7 compression

102.43 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L7 compression

128.20 MB/s compressing xml

(median across 15 runs)

roc-deflate at L7 compression

56.93 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L7 compression

79.18 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L7 compression

70.19 MB/s compressing mr

(median across 15 runs)

roc-deflate at L7 compression

174.91 MB/s compressing nci

(median across 15 runs)

roc-deflate at L7 compression

70.27 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L7 compression

115.95 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L7 compression

51.20 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L7 compression

96.46 MB/s compressing samba

(median across 15 runs)

roc-deflate at L7 compression

59.40 MB/s compressing sao

(median across 15 runs)

roc-deflate at L7 compression

75.99 MB/s compressing webster

(median across 15 runs)

roc-deflate at L7 compression

90.26 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L7 compression

141.60 MB/s compressing xml

(median across 15 runs)

libdeflate at L8 compression

37.50 MB/s compressing dickens

(median across 15 runs)

libdeflate at L8 compression

39.17 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L8 compression

43.21 MB/s compressing mr

(median across 15 runs)

libdeflate at L8 compression

83.68 MB/s compressing nci

(median across 15 runs)

libdeflate at L8 compression

52.45 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L8 compression

106.76 MB/s compressing osdb

(median across 15 runs)

libdeflate at L8 compression

24.87 MB/s compressing reymont

(median across 15 runs)

libdeflate at L8 compression

55.69 MB/s compressing samba

(median across 15 runs)

libdeflate at L8 compression

51.86 MB/s compressing sao

(median across 15 runs)

libdeflate at L8 compression

45.55 MB/s compressing webster

(median across 15 runs)

libdeflate at L8 compression

91.30 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L8 compression

80.95 MB/s compressing xml

(median across 15 runs)

roc-deflate at L8 compression

39.56 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L8 compression

43.00 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L8 compression

45.70 MB/s compressing mr

(median across 15 runs)

roc-deflate at L8 compression

91.28 MB/s compressing nci

(median across 15 runs)

roc-deflate at L8 compression

52.69 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L8 compression

101.66 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L8 compression

27.81 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L8 compression

60.04 MB/s compressing samba

(median across 15 runs)

roc-deflate at L8 compression

51.65 MB/s compressing sao

(median across 15 runs)

roc-deflate at L8 compression

48.78 MB/s compressing webster

(median across 15 runs)

roc-deflate at L8 compression

81.01 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L8 compression

86.27 MB/s compressing xml

(median across 15 runs)

libdeflate at L9 compression

34.82 MB/s compressing dickens

(median across 15 runs)

libdeflate at L9 compression

27.51 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L9 compression

38.60 MB/s compressing mr

(median across 15 runs)

libdeflate at L9 compression

58.64 MB/s compressing nci

(median across 15 runs)

libdeflate at L9 compression

47.26 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L9 compression

106.10 MB/s compressing osdb

(median across 15 runs)

libdeflate at L9 compression

20.65 MB/s compressing reymont

(median across 15 runs)

libdeflate at L9 compression

43.95 MB/s compressing samba

(median across 15 runs)

libdeflate at L9 compression

51.18 MB/s compressing sao

(median across 15 runs)

libdeflate at L9 compression

40.57 MB/s compressing webster

(median across 15 runs)

libdeflate at L9 compression

91.69 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L9 compression

68.13 MB/s compressing xml

(median across 15 runs)

roc-deflate at L9 compression

36.73 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L9 compression

30.48 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L9 compression

40.95 MB/s compressing mr

(median across 15 runs)

roc-deflate at L9 compression

64.32 MB/s compressing nci

(median across 15 runs)

roc-deflate at L9 compression

48.05 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L9 compression

101.46 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L9 compression

22.85 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L9 compression

47.64 MB/s compressing samba

(median across 15 runs)

roc-deflate at L9 compression

50.68 MB/s compressing sao

(median across 15 runs)

roc-deflate at L9 compression

43.36 MB/s compressing webster

(median across 15 runs)

roc-deflate at L9 compression

80.68 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L9 compression

73.29 MB/s compressing xml

(median across 15 runs)

libdeflate at L10 compression

12.07 MB/s compressing dickens

(median across 15 runs)

libdeflate at L10 compression

14.87 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L10 compression

16.07 MB/s compressing mr

(median across 15 runs)

libdeflate at L10 compression

7.51 MB/s compressing nci

(median across 15 runs)

libdeflate at L10 compression

18.09 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L10 compression

16.97 MB/s compressing osdb

(median across 15 runs)

libdeflate at L10 compression

8.64 MB/s compressing reymont

(median across 15 runs)

libdeflate at L10 compression

14.74 MB/s compressing samba

(median across 15 runs)

libdeflate at L10 compression

24.08 MB/s compressing sao

(median across 15 runs)

libdeflate at L10 compression

10.10 MB/s compressing webster

(median across 15 runs)

libdeflate at L10 compression

34.15 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L10 compression

11.46 MB/s compressing xml

(median across 15 runs)

roc-deflate at L10 compression

12.97 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L10 compression

14.67 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L10 compression

15.47 MB/s compressing mr

(median across 15 runs)

roc-deflate at L10 compression

7.19 MB/s compressing nci

(median across 15 runs)

roc-deflate at L10 compression

18.02 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L10 compression

17.23 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L10 compression

9.63 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L10 compression

14.59 MB/s compressing samba

(median across 15 runs)

roc-deflate at L10 compression

22.93 MB/s compressing sao

(median across 15 runs)

roc-deflate at L10 compression

11.18 MB/s compressing webster

(median across 15 runs)

roc-deflate at L10 compression

32.15 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L10 compression

10.73 MB/s compressing xml

(median across 15 runs)

libdeflate at L11 compression

8.85 MB/s compressing dickens

(median across 15 runs)

libdeflate at L11 compression

10.27 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L11 compression

8.76 MB/s compressing mr

(median across 15 runs)

libdeflate at L11 compression

4.82 MB/s compressing nci

(median across 15 runs)

libdeflate at L11 compression

13.56 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L11 compression

12.91 MB/s compressing osdb

(median across 15 runs)

libdeflate at L11 compression

6.49 MB/s compressing reymont

(median across 15 runs)

libdeflate at L11 compression

8.46 MB/s compressing samba

(median across 15 runs)

libdeflate at L11 compression

19.43 MB/s compressing sao

(median across 15 runs)

libdeflate at L11 compression

6.77 MB/s compressing webster

(median across 15 runs)

libdeflate at L11 compression

26.05 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L11 compression

6.60 MB/s compressing xml

(median across 15 runs)

roc-deflate at L11 compression

10.10 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L11 compression

10.53 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L11 compression

8.19 MB/s compressing mr

(median across 15 runs)

roc-deflate at L11 compression

4.74 MB/s compressing nci

(median across 15 runs)

roc-deflate at L11 compression

14.03 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L11 compression

13.62 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L11 compression

7.71 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L11 compression

8.68 MB/s compressing samba

(median across 15 runs)

roc-deflate at L11 compression

18.87 MB/s compressing sao

(median across 15 runs)

roc-deflate at L11 compression

8.07 MB/s compressing webster

(median across 15 runs)

roc-deflate at L11 compression

24.93 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L11 compression

6.51 MB/s compressing xml

(median across 15 runs)

libdeflate at L12 compression

7.35 MB/s compressing dickens

(median across 15 runs)

libdeflate at L12 compression

7.97 MB/s compressing mozilla

(median across 15 runs)

libdeflate at L12 compression

4.26 MB/s compressing mr

(median across 15 runs)

libdeflate at L12 compression

3.51 MB/s compressing nci

(median across 15 runs)

libdeflate at L12 compression

11.45 MB/s compressing ooffice

(median across 15 runs)

libdeflate at L12 compression

11.40 MB/s compressing osdb

(median across 15 runs)

libdeflate at L12 compression

5.59 MB/s compressing reymont

(median across 15 runs)

libdeflate at L12 compression

5.92 MB/s compressing samba

(median across 15 runs)

libdeflate at L12 compression

18.10 MB/s compressing sao

(median across 15 runs)

libdeflate at L12 compression

5.82 MB/s compressing webster

(median across 15 runs)

libdeflate at L12 compression

23.50 MB/s compressing x-ray

(median across 15 runs)

libdeflate at L12 compression

4.19 MB/s compressing xml

(median across 15 runs)

roc-deflate at L12 compression

8.59 MB/s compressing dickens

(median across 15 runs)

roc-deflate at L12 compression

8.22 MB/s compressing mozilla

(median across 15 runs)

roc-deflate at L12 compression

3.83 MB/s compressing mr

(median across 15 runs)

roc-deflate at L12 compression

3.48 MB/s compressing nci

(median across 15 runs)

roc-deflate at L12 compression

11.99 MB/s compressing ooffice

(median across 15 runs)

roc-deflate at L12 compression

12.21 MB/s compressing osdb

(median across 15 runs)

roc-deflate at L12 compression

6.87 MB/s compressing reymont

(median across 15 runs)

roc-deflate at L12 compression

6.03 MB/s compressing samba

(median across 15 runs)

roc-deflate at L12 compression

17.74 MB/s compressing sao

(median across 15 runs)

roc-deflate at L12 compression

7.11 MB/s compressing webster

(median across 15 runs)

roc-deflate at L12 compression

22.60 MB/s compressing x-ray

(median across 15 runs)

roc-deflate at L12 compression

4.18 MB/s compressing xml

(median across 15 runs)

Compression Level

MB/s

700

600

500

400

300

200

100

0

file that ran fastest

file that ran slowest

L1

L2

L3

L4

L5

L6

L7

L8

L9

L10

L11

L12

libdeflate

roc-deflate

libdeflate at L1 compression

191.10 MB/s compressing dickens

(median across 7 runs)

libdeflate at L1 compression

235.50 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L1 compression

261.70 MB/s compressing mr

(median across 7 runs)

libdeflate at L1 compression

387.30 MB/s compressing nci

(median across 7 runs)

libdeflate at L1 compression

167.90 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L1 compression

254.70 MB/s compressing osdb

(median across 7 runs)

libdeflate at L1 compression

229.60 MB/s compressing reymont

(median across 7 runs)

libdeflate at L1 compression

291.00 MB/s compressing samba

(median across 7 runs)

libdeflate at L1 compression

157.40 MB/s compressing sao

(median across 7 runs)

libdeflate at L1 compression

207.00 MB/s compressing webster

(median across 7 runs)

libdeflate at L1 compression

142.20 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L1 compression

411.30 MB/s compressing xml

(median across 7 runs)

roc-deflate at L1 compression

182.30 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L1 compression

204.50 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L1 compression

228.90 MB/s compressing mr

(median across 7 runs)

roc-deflate at L1 compression

428.60 MB/s compressing nci

(median across 7 runs)

roc-deflate at L1 compression

144.60 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L1 compression

222.30 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L1 compression

217.30 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L1 compression

270.30 MB/s compressing samba

(median across 7 runs)

roc-deflate at L1 compression

138.50 MB/s compressing sao

(median across 7 runs)

roc-deflate at L1 compression

213.90 MB/s compressing webster

(median across 7 runs)

roc-deflate at L1 compression

130.80 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L1 compression

353.80 MB/s compressing xml

(median across 7 runs)

libdeflate at L2 compression

138.50 MB/s compressing dickens

(median across 7 runs)

libdeflate at L2 compression

162.80 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L2 compression

153.40 MB/s compressing mr

(median across 7 runs)

libdeflate at L2 compression

286.50 MB/s compressing nci

(median across 7 runs)

libdeflate at L2 compression

120.40 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L2 compression

175.30 MB/s compressing osdb

(median across 7 runs)

libdeflate at L2 compression

156.80 MB/s compressing reymont

(median across 7 runs)

libdeflate at L2 compression

210.50 MB/s compressing samba

(median across 7 runs)

libdeflate at L2 compression

104.20 MB/s compressing sao

(median across 7 runs)

libdeflate at L2 compression

163.50 MB/s compressing webster

(median across 7 runs)

libdeflate at L2 compression

111.60 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L2 compression

258.40 MB/s compressing xml

(median across 7 runs)

roc-deflate at L2 compression

121.20 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L2 compression

144.50 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L2 compression

145.30 MB/s compressing mr

(median across 7 runs)

roc-deflate at L2 compression

326.40 MB/s compressing nci

(median across 7 runs)

roc-deflate at L2 compression

105.10 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L2 compression

155.00 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L2 compression

146.00 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L2 compression

188.40 MB/s compressing samba

(median across 7 runs)

roc-deflate at L2 compression

94.10 MB/s compressing sao

(median across 7 runs)

roc-deflate at L2 compression

151.60 MB/s compressing webster

(median across 7 runs)

roc-deflate at L2 compression

95.50 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L2 compression

248.60 MB/s compressing xml

(median across 7 runs)

libdeflate at L3 compression

112.90 MB/s compressing dickens

(median across 7 runs)

libdeflate at L3 compression

152.80 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L3 compression

132.10 MB/s compressing mr

(median across 7 runs)

libdeflate at L3 compression

304.30 MB/s compressing nci

(median across 7 runs)

libdeflate at L3 compression

113.00 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L3 compression

164.00 MB/s compressing osdb

(median across 7 runs)

libdeflate at L3 compression

128.00 MB/s compressing reymont

(median across 7 runs)

libdeflate at L3 compression

191.40 MB/s compressing samba

(median across 7 runs)

libdeflate at L3 compression

94.50 MB/s compressing sao

(median across 7 runs)

libdeflate at L3 compression

143.70 MB/s compressing webster

(median across 7 runs)

libdeflate at L3 compression

112.20 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L3 compression

209.90 MB/s compressing xml

(median across 7 runs)

roc-deflate at L3 compression

100.80 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L3 compression

132.50 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L3 compression

125.30 MB/s compressing mr

(median across 7 runs)

roc-deflate at L3 compression

301.90 MB/s compressing nci

(median across 7 runs)

roc-deflate at L3 compression

97.90 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L3 compression

148.80 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L3 compression

120.80 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L3 compression

169.40 MB/s compressing samba

(median across 7 runs)

roc-deflate at L3 compression

84.80 MB/s compressing sao

(median across 7 runs)

roc-deflate at L3 compression

133.90 MB/s compressing webster

(median across 7 runs)

roc-deflate at L3 compression

95.10 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L3 compression

231.70 MB/s compressing xml

(median across 7 runs)

libdeflate at L4 compression

100.80 MB/s compressing dickens

(median across 7 runs)

libdeflate at L4 compression

144.50 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L4 compression

123.40 MB/s compressing mr

(median across 7 runs)

libdeflate at L4 compression

254.00 MB/s compressing nci

(median across 7 runs)

libdeflate at L4 compression

109.70 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L4 compression

151.90 MB/s compressing osdb

(median across 7 runs)

libdeflate at L4 compression

118.90 MB/s compressing reymont

(median across 7 runs)

libdeflate at L4 compression

178.70 MB/s compressing samba

(median across 7 runs)

libdeflate at L4 compression

89.10 MB/s compressing sao

(median across 7 runs)

libdeflate at L4 compression

129.70 MB/s compressing webster

(median across 7 runs)

libdeflate at L4 compression

111.30 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L4 compression

201.50 MB/s compressing xml

(median across 7 runs)

roc-deflate at L4 compression

91.90 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L4 compression

126.60 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L4 compression

117.60 MB/s compressing mr

(median across 7 runs)

roc-deflate at L4 compression

282.80 MB/s compressing nci

(median across 7 runs)

roc-deflate at L4 compression

95.50 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L4 compression

138.00 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L4 compression

106.80 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L4 compression

159.20 MB/s compressing samba

(median across 7 runs)

roc-deflate at L4 compression

81.50 MB/s compressing sao

(median across 7 runs)

roc-deflate at L4 compression

125.00 MB/s compressing webster

(median across 7 runs)

roc-deflate at L4 compression

95.60 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L4 compression

215.50 MB/s compressing xml

(median across 7 runs)

libdeflate at L5 compression

82.40 MB/s compressing dickens

(median across 7 runs)

libdeflate at L5 compression

120.00 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L5 compression

103.10 MB/s compressing mr

(median across 7 runs)

libdeflate at L5 compression

250.40 MB/s compressing nci

(median across 7 runs)

libdeflate at L5 compression

89.30 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L5 compression

128.80 MB/s compressing osdb

(median across 7 runs)

libdeflate at L5 compression

94.60 MB/s compressing reymont

(median across 7 runs)

libdeflate at L5 compression

152.10 MB/s compressing samba

(median across 7 runs)

libdeflate at L5 compression

74.80 MB/s compressing sao

(median across 7 runs)

libdeflate at L5 compression

112.20 MB/s compressing webster

(median across 7 runs)

libdeflate at L5 compression

93.70 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L5 compression

198.40 MB/s compressing xml

(median across 7 runs)

roc-deflate at L5 compression

73.50 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L5 compression

105.70 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L5 compression

96.60 MB/s compressing mr

(median across 7 runs)

roc-deflate at L5 compression

247.90 MB/s compressing nci

(median across 7 runs)

roc-deflate at L5 compression

77.50 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L5 compression

116.60 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L5 compression

86.20 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L5 compression

133.00 MB/s compressing samba

(median across 7 runs)

roc-deflate at L5 compression

68.10 MB/s compressing sao

(median across 7 runs)

roc-deflate at L5 compression

100.10 MB/s compressing webster

(median across 7 runs)

roc-deflate at L5 compression

82.10 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L5 compression

182.10 MB/s compressing xml

(median across 7 runs)

libdeflate at L6 compression

65.40 MB/s compressing dickens

(median across 7 runs)

libdeflate at L6 compression

102.90 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L6 compression

81.60 MB/s compressing mr

(median across 7 runs)

libdeflate at L6 compression

203.10 MB/s compressing nci

(median across 7 runs)

libdeflate at L6 compression

78.50 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L6 compression

118.80 MB/s compressing osdb

(median across 7 runs)

libdeflate at L6 compression

71.00 MB/s compressing reymont

(median across 7 runs)

libdeflate at L6 compression

120.10 MB/s compressing samba

(median across 7 runs)

libdeflate at L6 compression

64.40 MB/s compressing sao

(median across 7 runs)

libdeflate at L6 compression

91.80 MB/s compressing webster

(median across 7 runs)

libdeflate at L6 compression

94.80 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L6 compression

168.30 MB/s compressing xml

(median across 7 runs)

roc-deflate at L6 compression

57.80 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L6 compression

89.40 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L6 compression

74.10 MB/s compressing mr

(median across 7 runs)

roc-deflate at L6 compression

188.20 MB/s compressing nci

(median across 7 runs)

roc-deflate at L6 compression

70.60 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L6 compression

107.80 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L6 compression

60.90 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L6 compression

105.40 MB/s compressing samba

(median across 7 runs)

roc-deflate at L6 compression

59.20 MB/s compressing sao

(median across 7 runs)

roc-deflate at L6 compression

81.30 MB/s compressing webster

(median across 7 runs)

roc-deflate at L6 compression

83.20 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L6 compression

149.50 MB/s compressing xml

(median across 7 runs)

libdeflate at L7 compression

49.60 MB/s compressing dickens

(median across 7 runs)

libdeflate at L7 compression

76.10 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L7 compression

56.30 MB/s compressing mr

(median across 7 runs)

libdeflate at L7 compression

150.20 MB/s compressing nci

(median across 7 runs)

libdeflate at L7 compression

69.10 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L7 compression

113.80 MB/s compressing osdb

(median across 7 runs)

libdeflate at L7 compression

39.90 MB/s compressing reymont

(median across 7 runs)

libdeflate at L7 compression

85.90 MB/s compressing samba

(median across 7 runs)

libdeflate at L7 compression

53.10 MB/s compressing sao

(median across 7 runs)

libdeflate at L7 compression

66.10 MB/s compressing webster

(median across 7 runs)

libdeflate at L7 compression

94.20 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L7 compression

119.90 MB/s compressing xml

(median across 7 runs)

roc-deflate at L7 compression

45.20 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L7 compression

67.20 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L7 compression

52.40 MB/s compressing mr

(median across 7 runs)

roc-deflate at L7 compression

141.70 MB/s compressing nci

(median across 7 runs)

roc-deflate at L7 compression

61.10 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L7 compression

106.10 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L7 compression

36.20 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L7 compression

76.50 MB/s compressing samba

(median across 7 runs)

roc-deflate at L7 compression

52.80 MB/s compressing sao

(median across 7 runs)

roc-deflate at L7 compression

59.40 MB/s compressing webster

(median across 7 runs)

roc-deflate at L7 compression

81.60 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L7 compression

108.40 MB/s compressing xml

(median across 7 runs)

libdeflate at L8 compression

32.10 MB/s compressing dickens

(median across 7 runs)

libdeflate at L8 compression

41.40 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L8 compression

35.80 MB/s compressing mr

(median across 7 runs)

libdeflate at L8 compression

80.70 MB/s compressing nci

(median across 7 runs)

libdeflate at L8 compression

50.40 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L8 compression

97.80 MB/s compressing osdb

(median across 7 runs)

libdeflate at L8 compression

20.60 MB/s compressing reymont

(median across 7 runs)

libdeflate at L8 compression

53.40 MB/s compressing samba

(median across 7 runs)

libdeflate at L8 compression

46.60 MB/s compressing sao

(median across 7 runs)

libdeflate at L8 compression

40.00 MB/s compressing webster

(median across 7 runs)

libdeflate at L8 compression

78.30 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L8 compression

72.60 MB/s compressing xml

(median across 7 runs)

roc-deflate at L8 compression

30.00 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L8 compression

36.80 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L8 compression

33.90 MB/s compressing mr

(median across 7 runs)

roc-deflate at L8 compression

75.50 MB/s compressing nci

(median across 7 runs)

roc-deflate at L8 compression

45.60 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L8 compression

90.20 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L8 compression

19.50 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L8 compression

49.00 MB/s compressing samba

(median across 7 runs)

roc-deflate at L8 compression

44.50 MB/s compressing sao

(median across 7 runs)

roc-deflate at L8 compression

37.10 MB/s compressing webster

(median across 7 runs)

roc-deflate at L8 compression

72.10 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L8 compression

66.40 MB/s compressing xml

(median across 7 runs)

libdeflate at L9 compression

29.00 MB/s compressing dickens

(median across 7 runs)

libdeflate at L9 compression

29.10 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L9 compression

32.50 MB/s compressing mr

(median across 7 runs)

libdeflate at L9 compression

58.50 MB/s compressing nci

(median across 7 runs)

libdeflate at L9 compression

45.00 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L9 compression

95.30 MB/s compressing osdb

(median across 7 runs)

libdeflate at L9 compression

16.90 MB/s compressing reymont

(median across 7 runs)

libdeflate at L9 compression

41.60 MB/s compressing samba

(median across 7 runs)

libdeflate at L9 compression

45.60 MB/s compressing sao

(median across 7 runs)

libdeflate at L9 compression

33.90 MB/s compressing webster

(median across 7 runs)

libdeflate at L9 compression

78.60 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L9 compression

57.90 MB/s compressing xml

(median across 7 runs)

roc-deflate at L9 compression

27.10 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L9 compression

26.30 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L9 compression

30.60 MB/s compressing mr

(median across 7 runs)

roc-deflate at L9 compression

54.40 MB/s compressing nci

(median across 7 runs)

roc-deflate at L9 compression

41.20 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L9 compression

90.80 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L9 compression

15.90 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L9 compression

38.70 MB/s compressing samba

(median across 7 runs)

roc-deflate at L9 compression

43.30 MB/s compressing sao

(median across 7 runs)

roc-deflate at L9 compression

31.70 MB/s compressing webster

(median across 7 runs)

roc-deflate at L9 compression

72.70 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L9 compression

54.80 MB/s compressing xml

(median across 7 runs)

libdeflate at L10 compression

12.10 MB/s compressing dickens

(median across 7 runs)

libdeflate at L10 compression

14.80 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L10 compression

16.20 MB/s compressing mr

(median across 7 runs)

libdeflate at L10 compression

7.30 MB/s compressing nci

(median across 7 runs)

libdeflate at L10 compression

18.20 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L10 compression

16.10 MB/s compressing osdb

(median across 7 runs)

libdeflate at L10 compression

8.70 MB/s compressing reymont

(median across 7 runs)

libdeflate at L10 compression

14.40 MB/s compressing samba

(median across 7 runs)

libdeflate at L10 compression

23.30 MB/s compressing sao

(median across 7 runs)

libdeflate at L10 compression

10.00 MB/s compressing webster

(median across 7 runs)

libdeflate at L10 compression

34.70 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L10 compression

10.80 MB/s compressing xml

(median across 7 runs)

roc-deflate at L10 compression

12.30 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L10 compression

13.70 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L10 compression

14.70 MB/s compressing mr

(median across 7 runs)

roc-deflate at L10 compression

6.80 MB/s compressing nci

(median across 7 runs)

roc-deflate at L10 compression

16.80 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L10 compression

15.50 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L10 compression

9.00 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L10 compression

13.60 MB/s compressing samba

(median across 7 runs)

roc-deflate at L10 compression

20.60 MB/s compressing sao

(median across 7 runs)

roc-deflate at L10 compression

10.20 MB/s compressing webster

(median across 7 runs)

roc-deflate at L10 compression

29.40 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L10 compression

9.80 MB/s compressing xml

(median across 7 runs)

libdeflate at L11 compression

8.80 MB/s compressing dickens

(median across 7 runs)

libdeflate at L11 compression

10.30 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L11 compression

9.30 MB/s compressing mr

(median across 7 runs)

libdeflate at L11 compression

4.70 MB/s compressing nci

(median across 7 runs)

libdeflate at L11 compression

13.70 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L11 compression

12.30 MB/s compressing osdb

(median across 7 runs)

libdeflate at L11 compression

6.50 MB/s compressing reymont

(median across 7 runs)

libdeflate at L11 compression

8.40 MB/s compressing samba

(median across 7 runs)

libdeflate at L11 compression

18.90 MB/s compressing sao

(median across 7 runs)

libdeflate at L11 compression

6.70 MB/s compressing webster

(median across 7 runs)

libdeflate at L11 compression

26.80 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L11 compression

6.20 MB/s compressing xml

(median across 7 runs)

roc-deflate at L11 compression

9.50 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L11 compression

9.90 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L11 compression

8.30 MB/s compressing mr

(median across 7 runs)

roc-deflate at L11 compression

4.50 MB/s compressing nci

(median across 7 runs)

roc-deflate at L11 compression

13.00 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L11 compression

12.30 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L11 compression

7.10 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L11 compression

8.30 MB/s compressing samba

(median across 7 runs)

roc-deflate at L11 compression

17.00 MB/s compressing sao

(median across 7 runs)

roc-deflate at L11 compression

7.30 MB/s compressing webster

(median across 7 runs)

roc-deflate at L11 compression

23.00 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L11 compression

6.00 MB/s compressing xml

(median across 7 runs)

libdeflate at L12 compression

7.40 MB/s compressing dickens

(median across 7 runs)

libdeflate at L12 compression

8.00 MB/s compressing mozilla

(median across 7 runs)

libdeflate at L12 compression

4.70 MB/s compressing mr

(median across 7 runs)

libdeflate at L12 compression

3.40 MB/s compressing nci

(median across 7 runs)

libdeflate at L12 compression

11.50 MB/s compressing ooffice

(median across 7 runs)

libdeflate at L12 compression

10.90 MB/s compressing osdb

(median across 7 runs)

libdeflate at L12 compression

5.60 MB/s compressing reymont

(median across 7 runs)

libdeflate at L12 compression

5.90 MB/s compressing samba

(median across 7 runs)

libdeflate at L12 compression

17.70 MB/s compressing sao

(median across 7 runs)

libdeflate at L12 compression

5.80 MB/s compressing webster

(median across 7 runs)

libdeflate at L12 compression

24.60 MB/s compressing x-ray

(median across 7 runs)

libdeflate at L12 compression

4.00 MB/s compressing xml

(median across 7 runs)

roc-deflate at L12 compression

8.10 MB/s compressing dickens

(median across 7 runs)

roc-deflate at L12 compression

7.80 MB/s compressing mozilla

(median across 7 runs)

roc-deflate at L12 compression

4.10 MB/s compressing mr

(median across 7 runs)

roc-deflate at L12 compression

3.30 MB/s compressing nci

(median across 7 runs)

roc-deflate at L12 compression

11.20 MB/s compressing ooffice

(median across 7 runs)

roc-deflate at L12 compression

11.10 MB/s compressing osdb

(median across 7 runs)

roc-deflate at L12 compression

6.30 MB/s compressing reymont

(median across 7 runs)

roc-deflate at L12 compression

5.80 MB/s compressing samba

(median across 7 runs)

roc-deflate at L12 compression

15.80 MB/s compressing sao

(median across 7 runs)

roc-deflate at L12 compression

6.40 MB/s compressing webster

(median across 7 runs)

roc-deflate at L12 compression

21.00 MB/s compressing x-ray

(median across 7 runs)

roc-deflate at L12 compression

3.90 MB/s compressing xml

(median across 7 runs)

Compression Level

So while we didn't outperform the champ on average, a median slowdown percentage in the single digits compared to such a carefully-tuned SIMD-powered C library iswild.It's frankly not a result I knew was achievable going in, since Roc is a functional language with automatic memory management racing against code that doesn't have to do bounds checks. (Bounds checks have a cost, but then again, the last time a skipped bounds check in C compression code led to a major Remote Code Execution vulnerabilitywas yesterday.)

The graph shows more detail than just the median gap. On the worst-case inputs, roc-deflate was 18% slower than libdeflate, but on the best-case inputs, roc-deflate was slightly over 18%faster!That's not because Roc has some magical optimization that C can't access; it's just that the two implementations are different, and although on average roc-deflate is slower, for certain inputs it happens to be faster. So while it'spossibleto get a speedup by switching from libdeflate to roc-deflate, you shouldn't expect it on average.

To be clear, C's performance ceiling is higher than Roc's. For any input where roc-deflate currently outperforms libdeflate, C code can close that gap. The reverse is not true; Roc code is memory-safe, does automatic reference counting, checks bounds, and supports no Rust-styleunsafeto opt out of any of that. These properties give Roc code stronger safety guarantees than code written in C, Zig, Rust, and other languages that allow full access to the hardware—and the price it pays for those guarantees is a lower performance ceiling.

Obviously we can't extrapolate from this one result about how close Roc can get to C in the general case, but now something has been demonstrated that nobody knew was achievable before. As far as I know, this is the most optimization effort that has been put into any Roc package to date, so how close others can get to this result is a complete unknown right now. So while I'm thrilled by this result, I'm fully aware that we won't know how well it generalizes until we've optimized a wider sample of real-world Roc code bases!

## What the Performance Gap Buys

An obvious question is "Why settle foranyamount slower?" If youcouldget C levels of performance, why not use libdeflate itself and close that remaining gap?

A pure-Roc implementation has several advantages over a pure-C one:

* Memory safety.Roc code is fully memory-safe and has no language primitives that let you opt out of it. This code is only able to approach C levels of performance because Roc's optimization pipeline determined that many bounds checks and reference counting operations were provably safe to optimize away. Compression packages written in pure Roc don't have access to the unchecked memory operation that caused yesterday'sBrotli Remote Code Execution vulnerability.
* No side effects.Roc's type systeminfers which functions are pureand which can perform side effects. Pure functions' types use a thin arrow, likeBool -> Bool, whereaseffectful functionsuse a thick arrow, likeBool => Bool. (As with memory safety, Roc enforces this and supports no way to opt out.) So when you see that roc-deflate's functions have only thin arrows in their annotations, you know they really are pure functions.
* Supply-Chain Security.Roc does not have an arbitraryFFI, meaning you know for sure that roc-deflate's pure functions can't even attempt to do I/O or access arbitrary memory. Given the explosion insupply chain attacks, it's valuable to know that the damage a malicious actor can do with a pure function in a compromised Roc package is limited to returning the wrong value, crashing, or wasting system resources. Roc packages also don't support build scripts, which was the vector used tosuccessfully compromise the popular Rustarrayrefpackagetwo months ago.
* Portability.Roc pure functions are designed to be extremely deterministic: they always return the same values when given the same arguments—not just when run on the same machine, but also on any target you compile that code to. (The functions may also crash or fail to terminate, but that behavior should also be deterministic across targets.) The only way a Roc pure function should be expected to behave differently when run on two different systems is if one system runs out of memory mid-execution.

If any of these guarantees don't hold in practice, it can only be due to a defect in Roc's compiler, theplatformthe application is running on, or the underlying hardware. So when you see inroc-deflate's docsthat the entire package is 100% pure functions, you can be confident you are getting all of the above properties from everything the package has to offer. The type system enforces it!

The reason we've been working so hard on all this might become clearer if you look at the proposition in reverse: would you give up guaranteed memory safety, guaranteed lack of side effects, guaranteed deterministic behavior across all targets, and the security benefits of having no exploitable build scripts in packages...for an average speedup percentage in the single digits?

That answer can legitimately vary by use case—Roc's own compiler, for example, wantsthe maximum performance the hardware can deliver—but I bet a lot of people reading this can see why we're so excited to have achieved this result.

## Roc-Specific Optimizations

Most of the optimizations that improved roc-deflate's numbers came from general optimization techniques that are widely beneficial across languages. (I always recommendCasey Muratori's Performance-Aware Programming Series, which I paid for and learned a lot from.) Some of the optimization techniques were Roc-specific, though, and I wanted to mention them here as a reference for others. Even if you're not writing Roc code, this can also give you an idea ofhow Roc achieves its performance.

### Avoid Unnecessary Sharing

One of Roc's most effective optimizations isopportunistic mutation(whichKokacalls"Functional but In-Place"). You can learn how it works in Roc'sdocs on opportunistic mutation, but from a performance optimization perspective, it's critically important to avoid unnecessary sharing so that values remain unique and therefore eligible for in-place mutation.

### Hoist Bounds Checks

You can't opt out of bounds checks (e.g. getting a value out of a dynamically-sized collection) in Roc like you can in C, Zig, and Rust, but Roc's compiler can optimize them away if it knows they'd be guaranteed to pass. Bounds checks are most costly inside loops, so you can get a lot of mileage out of adding something likeif collection.len() <= highest_index_used { return 0 }before the loop starts. This adds an additional check that looks redundant, but it can allow the optimizer to safely delete costlier checks inside the loop, once it can tell that failures would not be reachable after that early return.

### Build Lookup Tables at Compile Time

Roc's compile-time evaluationcan be used to assemble lookup tables at compile time as long as nothing depends on runtime inputs. Even better, since their lengths are known at compile time, you can do things likeOk(entry) = lookup_table.get(5)to do anexhaustive pattern matchthat Roc's compiler will know is valid thanks to compile-time evaluation. This avoids runtime bounds checks that non-constant tables might have to pay for.

### Consider Wrapping Arithmetic

In Roc,a + bdesugars toa.plus(b). For an integer likeU64,U64.plusincludes an overflow check, whereasplus_wrapdoes not. Althoughplusis the safer default,overflow checks have a runtime cost, as CPUs can do wrapping integer arithmetic in one instruction. When Roc's compiler can prove that overflow won't occur, bothplusandplus_wrapwill optimize to the same instructions, but when it can't, you may get a speedup by choosingplus_wrap.

## Room for Improvement

I'm sure there are still opportunities to improve roc-deflate's performance—especially on x64 CPUs—as well as the optimization pipeline in Roc's compiler.

At this point I feel reasonably confident that all the low-hanging fruit has been picked, but if anyone wants to try it out for themselves,here's the script I ran to set up and run the benchmark suite on Linux. (Note that Claude Opus 5.5 generated this script, and I haven't vetted it for security; run it outside a sandbox at your own risk!) It pins both Roc compiler revisions and roc-deflate versions, so you'll want to adjust those commits if you're trying out potential improvements.

For my part, I'll be focusing on the upcoming Roc 0.1.0 release from now until it's out. It's been eight years in the making, so I'll be very happy for us to finally have a numbered release! If you'd like to learn more about Roc, check outroc-lang.orgorcome say hi on Roc Zulip!