---
title: Making TRAMP go Brrrr…. • Core Dumped
url: https://coredumped.dev/2025/06/18/making-tramp-go-brrrr./
date: 2025-06-24
site: lobsters
model: llama3.2:1b
summarized_at: 2025-06-24T23:11:08.956603
---

# Making TRAMP go Brrrr…. • Core Dumped

**Analysis: Making TRAMP Go Brrr... • Core Dumped**

**Problem or Opportunity**: The author is discussing how the common issue of slow performance when using TRAMP, an Emacs package for remote access to remote machines, is being addressed.

**Market Indicators**:

* Most users would prefer faster solutions over manual copying and scp directly.
* TRAMP's existing user base may be willing to pay for improved performance.
* The author mentions the graph indicating that inline mode (using ssh/scp) is faster than out-of-band mode for small files, with a cutoff around 2MB.

**Technical Feasibility**: The author identifies several factors affecting TRAMP's performance:

1. **Existing implementation limitations**: Inline method is already optimized for 10KB chunks under heavy load.
2. **Optimization techniques**: Using rsync as an alternative to scp increases update times by 3-4x.
3. **File size thresholds**: Out-of-band mode becomes slow above a certain file size (2MB).

**Business Viability Signals**:

* The author notes that the existing user base may be willing to pay for improved performance (though not explicitly stated).
* Distribution of existing users and potential demand from new ones is uncertain.
* Existing competition is absent; TRAMP's market positioning is clear (as a fast Emacs package for remote access).

**Actionable Insights**:

1. **Optimize inline mode**: Using rsync as an alternative to scp can improve update times by 3-4x, making it faster than the native inline method.
2. **Set file size thresholds**: The author suggests choosing an out-of-band method with a higher chunk size threshold (e.g., 1024KB or 1MB) if the file size exceeds that point.
3. **Evaluate additional performance boosts**: Monitoring TRAMP's latency and comparing it to external tools (like rsync) can help identify where further optimization opportunities exist.

**Notable Quotes and Information**:

* "This is by default set to 10KB" (implying limitations in the existing implementation).
* "/Graph above..." indicating that inline mode shows a performance improvement around a certain threshold.
* " Generally the slower the connection, the bigger the gap between inline and out-of-band."
