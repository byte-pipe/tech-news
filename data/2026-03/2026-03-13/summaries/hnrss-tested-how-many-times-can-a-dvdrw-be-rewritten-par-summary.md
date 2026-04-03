---
title: "Tested: How Many Times Can a DVD±RW Be Rewritten? – Part 2: Methodology & Results | Gough's Tech Zone"
url: https://goughlui.com/2026/03/07/tested-how-many-times-can-a-dvd%C2%B1rw-be-rewritten-part-2-methodology-results/
date: 2026-03-08
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-13T03:14:09.088064
---

# Tested: How Many Times Can a DVD±RW Be Rewritten? – Part 2: Methodology & Results | Gough's Tech Zone

# Tested: How Many Times Can a DVD±RW Be Rewritten? – Part 2: Methodology & Results

## Methodology & Limitations
- Used **Opti Drive Control (ODC)** for write‑verify, transfer‑rate test (TRT), and quality scans; the quality scan reports correctable errors and jitter.
- Automated the whole process with a **Python script (pyautogui)** that clicks through ODC, takes screenshots, and handles errors; initial flakiness was solved with delays and recovery logic.
- Primary drive: **Lite‑On iHAS120‑6** (retail model) with error‑scanning capability; two spare identical drives were kept as backups.
- Added a second iHAS120‑6 in a USB‑2.0 enclosure on a mini‑PC running Windows 11 to double throughput; disabled automatic Windows updates to avoid interruptions.
- Image processing pipeline:
  - **OpenCV** for contour detection and template matching of screenshots.
  - **Pillow** and **NumPy** for image manipulation, adding run counters, and exporting sequences as video (re‑encoded with Handbrake) to keep storage efficient.
- Key limitations:
  - Quality scans alone are not definitive; verification failures are the ultimate failure criterion.
  - Results apply only to the specific burner‑media combination; only a single sample per disc type was tested.
  - ODC erases DVD‑RW discs fully before each write, effectively counting two cycles per rewrite; this was tolerated despite extending test length.
  - Possible off‑by‑up‑to‑three‑cycle error due to mid‑test machine restarts; considered negligible.

## Results
### Memorex 8x DVD+RW (RITEK‑008‑000)
- Initial burn succeeded at **8× Z‑CLV**, but every subsequent burn was limited to **6× CLV**; occasional 8× after system reboot suggested drive throttling due to media issues.
- Readback curves appeared smooth but were misleading; the first two writes already showed poor quality.
- Verification failures began early: the **first verification error occurred at 106 rewrite cycles**.
- Video evidence (5 fps) of successive runs was provided to illustrate degradation.