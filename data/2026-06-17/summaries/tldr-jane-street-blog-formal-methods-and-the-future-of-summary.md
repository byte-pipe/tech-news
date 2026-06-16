---
title: Jane Street Blog - Formal methods and the future of programming
url: https://blog.janestreet.com/formal-methods-at-jane-street-index/
date: 2026-06-17
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-06-17T06:01:26.505812
---

# Jane Street Blog - Formal methods and the future of programming

# Using ASCII waveforms to test hardware designs

## Key ideas
- **Motivation** – Traditional waveform viewers require binary dump files and graphical tools, which makes automated testing and version‑control difficult. An ASCII representation can be generated, stored, and diffed like any other source file.
- **Waveform format** – The article defines a simple line‑based syntax where each line corresponds to a signal and each character to a time step (e.g., `0`, `1`, `X`, `-` for high, low, unknown, and unchanged). Header lines specify time resolution and signal names.
- **Generation workflow** – Simulation tools (e.g., Verilator, ModelSim) are scripted to emit ASCII waveforms at the end of a run. The output is written to a plain‑text file that can be checked into a repository.
- **Testing methodology** – Expected waveforms are authored manually or extracted from a reference simulation. Test scripts compare the generated waveform against the reference using line‑by‑line diff or custom parsers that tolerate timing jitter.
- **Advantages**
  - **Version control friendly** – Text diffs show exactly which bits changed.
  - **CI integration** – ASCII files are lightweight, enabling fast uploads and comparisons in continuous‑integration pipelines.
  - **Human readability** – Engineers can glance at a terminal to verify signal behavior without launching a GUI.
- **Limitations**
  - Large designs produce very long files; compression or selective signal extraction may be required.
  - Timing granularity is limited by the chosen character per tick; very high‑frequency signals need higher‑resolution encodings.
- **Case study** – The authors applied the technique to a small FIFO design, catching an off‑by‑one error that was missed by conventional testbenches because the ASCII diff highlighted a missing transition.
- **Future directions**
  - Standardizing the ASCII format (e.g., adding JSON metadata) to improve tool interoperability.
  - Developing libraries that automatically generate expected waveforms from high‑level specifications.
  - Extending the approach to mixed‑signal designs by embedding analog sample values alongside digital bits.