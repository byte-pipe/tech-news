---
title: How to sequence your own DNA at home
url: https://bradleywoolf.com/links-1/sequencing-my-own-dna-at-home
site_name: hnrss
content_file: hnrss-how-to-sequence-your-own-dna-at-home
fetched_at: '2026-07-07T12:03:02.248966'
original_url: https://bradleywoolf.com/links-1/sequencing-my-own-dna-at-home
date: '2026-07-07'
description: I have now sequenced my own genome 5 times with an Oxford Nanopore Technologies MinION. This means collecting them from a swab, prepping them for sequencing, running them through a sequencer, then doing analysis over them.
tags:
- hackernews
- hnrss
---

# How to sequence your own DNA at home

I have now sequenced my own genome 5 times with anOxford Nanopore Technologies MinION. This means collecting them from a swab, prepping them for sequencing, running them through a sequencer, then doing analysis over them.

Cheek cells are easily accessible and replenish pretty quickly. They are not used for cancer diagnosis, inflammation, or what genes are being activated in other parts of the body (like if you have hives on your chest and want to test what genes are being expressed in the cells that are inflamed), since you would want to collect the cells having problems and compare them against other normal versions of those cells.

To sequence the cells, I bought lab materials and consumables to sequence my own genome at home. It took me about two months to get everything together to do a full end to end high quality run. Likewise,the costs are still out of reach for the average personbut they are decreasing (exponentially!) and we will eventually have affordable technology, like a cell phone or AI, telling us about our DNA + RNA expression real-time.

# What can I even do with my own genome?

Before we actually spend all this time and money on sequencing, what can weactually dowith our genome?

The genome is not magic by itself- it is the reference layer. Once I have a VCF, I can run it through tools likeVEP,ClinVar,gnomAD,PharmGKB(highly recommend),Gene Inspector, or Claude, and start asking:

* Which variants do I have?
* Which genes and pathways are affected?
* Which medicines might I metabolize differently?
* What rare variants should I take seriously?
* Where does the model know nothing yet?

This last part matters- the information produced is not yet diagnosis-level, and it is definitely not “edit yourself with CRISPR because an AI said so.” The near-term value is turning a static genome into something queryable, but the “edit yourself with CRISPR” will most likely follow. DNA is the stable reference, RNA is the current state, and we will eventually integrate all biosensor data into one ‘model’ of yourself.

Here are a list of links and Twitter posts to help:

1. Genetic variants from first principles:Adib @ ICML 🇰🇷Adib @ ICML 🇰🇷 on Twitter / X
2. TLDR these genes, and the combinations of them, compound into real physical diseases. We will probably map these in the next decade
3. Pass your genome + RNA to any of these models:https://www.biotender.online/bio-model-install-guide/
4. Give your genome to Claude Code- message me if you want me to set this up for you
5. Take it to a doctorif you metabolize particular drugs differently
6. Patrick Collison poston using agents to talk to his genome

# Protocol Steps

This is dense- you are welcome read this, or feed it to your AI. Feel free to copy and paste the URL of this and have ChatGPT walk you through it. If you have AR glasses, even better, since the AI can walk you through the whole protocol.

### Hardware

* Oxford Nanopore Technologies MinION($7.5k)
* Laptop/workstation for MinKNOW (any PC should be fine)
* 100GB+ storage for outputs
* GPU for Dorado basecalling
* Vortex($50)
* Heat block($250)
* Centrifuge($400 used on eBay)

### Consumables

* SQK-LSK114 Ligation Sequencing Kit V14 for DNA
* EXP-WSH004 Flow Cell Wash Kit
* EXP-CTL001 Control material
* PBS 1x
* Isohelix Buccal swabs

### Reagents

* DNA extraction kit
* NEB Monarch HMW DNA Extraction Kit for Cells & Blood($87 for 5 runs)
* Nuclei Prep Buffer
* Nuclei Lysis Buffer
* RNase A
* Proteinase K
* Precipitation Enhancer
* DNA Capture Beads
* gDNA Wash Buffer
* Elution Buffer II
* Bead retainers / Monarch collection parts from kit
* DNA library-prep reagents
* NEBNext Companion Module v2/ repair-end prep reagents ($760 for 24 reactions)
* FFPE DNA Repair Buffer
* FFPE DNA Repair Mix
* Ultra II End-prep Reaction Buffer
* Ultra II End-prep Enzyme Mix
* NEBNext Quick T4 DNA Ligase
* Oxford Nanopore SQK-LSK114($720 for 6 reactions)
* Long Fragment Buffer / LFB
* Elution Buffer / EB
* Ligation Adapter / LA
* Ligation Buffer / LNB
* Sequencing Buffer / SB
* Library Beads / LIB
* Flow cell priming reagents
* Flow Cell Flush / FCF
* Flow Cell Tether / FCT
* BSA
* AMPure XP beads
* 80% ethanol
* Nuclease-free water($32 for 25mL)
* DNA quantity measurement
* Qubit fluorometer
* Qubit dsDNA BR or HS Assay Kit

### Bench equipment

1. Microcentrifuge
2. Vortex mixer
3. Heat block / dry bath
4. Magnetic rack for 1.5/2 mL tubes
5. Tube racks
6. Ice bucket / cold block
7. Freezer at -20°C
8. Fridge at 4°C
9. Pipettes
10. P1000(100–1000 µL)
11. P200(0–200 µL)
12. P20(2–20 µL)
13. P10(1-10 µL)

## Plastics / Lab Pro-style consumables

1. Sterile flocked cheek swabs
2. 1.5 mL microcentrifuge tubes
3. 2.0 mL microcentrifuge tubes
4. DNA LoBind 1.5 mL tubes
5. RNA LoBind tubes
6. 0.2 mL PCR tubes
7. Qubit assay tubes
8. Pipette sterile filtered tips
9. P1000(100–1000 µL)
10. P200(0–200 µL)
11. P20(2–20 µL)
12. P10(1-10 µL)
13. Wide-bore P200 tips
14. Tube labels / lab marker
15. Gloves

## Software stack

1. MinKNOW
2. Dorado
3. minimap2
4. samtools
5. mosdepth
6. NanoPlot or pycoQC
7. Clair3
8. DeepVariant, optional
9. Ensembl VEP
10. ClinVar
11. gnomAD
12. PharmGKB
13. dbSNP, optional
14. Python/R
15. SQLite/Postgres for query layer later

# End-to-end DNA sequencing protocol

The goal is to go from 2 cheek-swab samples → MinION sequencing

# 0. Setup

1. Gloves on.
2. Clean bench.
3. Label tubes:
4. Bring AMPure XP beads to room temperature.
5. Keep enzyme mixes cold.
6. Set heat block to 56°C.
7. Keep Nuclei Prep Buffer cold.
8. Confirm gDNA Wash Buffer already has ethanol added.
9. Confirm you have isopropanol for DNA binding.
10. Confirm you have fresh 80% ethanol for AMPure cleanup.
11. Confirm you have the corrected ONT reagents:
* FFPE DNA Repair Buffer v2
* FFPE DNA Repair Mix
* N-Prep Enzyme Mix
* Salt-T4 DNA Ligase
* LNB
* LA
* LFB
* EB
* SB
* LIB
* FCF
* FCT

# 1. Collect cheek cells

Goal: get as much cheek-cell material as possible into PBS.

1. Rinse mouth with water.
2. Wait 10 minutes.
3. Do not brush teeth.
4. Do not use mouthwash.
5. Scrape inside cheek firmly for 60 seconds.
6. Add 1 mL cold PBS to labeled tube.
7. Put swab head into PBS.
8. Vortex 10 seconds.
9. Press swab against tube wall to squeeze liquid out.
10. Remove and discard swab.

What good looks like:

Copy
PBS may look slightly cloudy.

# 2. Pellet cheek cells

Goal: concentrate cells and remove excess PBS.

1. Spin at 2,000 × g for 30 seconds.
2. Look for a small white/off-white pellet or smear.
3. Remove most PBS with P1000.
4. Remove more PBS carefully with P200.
5. Leave 50–100 µL above the pellet.
6. Flick gently to resuspend the pellet.

Do not aspirate the pellet.

# 3. Prepare Monarch lysis solutions for one sample

## Nuclei Prep Solution

Copy
165 µL Nuclei Prep Buffer
5.5 µL RNase A

Mix gently. Keep cold.

You will use 150 µL.

## Nuclei Lysis Solution

Copy
165 µL Nuclei Lysis Buffer
11 µL Proteinase K

Mix gently. Keep at room temperature.

You will use 150 µL.

The extra volume is intentional so pipetting error does not leave you short.

# 4. Lyse cells

Goal: break open cells and digest proteins while preserving long genomic DNA.

1. Add 150 µL Nuclei Prep Solution to the resuspended cheek-cell pellet.
2. Pipette up/down gently 10 times.
3. Incubate 2 minutes at room temperature.
4. Add 150 µL Nuclei Lysis Solution.
5. Invert tube gently 10 times.
6. Do not vortex.
7. Incubate at 56°C for 10 minutes.

What good looks like:

Copy
The liquid may become more viscous.

Do not vortex after lysis. At this point, the priority is preserving high molecular weight DNA.

# 5. Bind DNA to Monarch capture beads

Goal: precipitate genomic DNA onto the large Monarch capture beads.

1. Add 75 µL Precipitation Enhancer.
2. Invert gently 8–10 times.
3. Add 2 DNA Capture Beads.
4. Add 275 µL isopropanol.
5. Invert slowly 30 times.
6. Do not vortex.

Important:

Copy
The beads now carry the DNA.
Do not lose the beads.
Do not use ethanol here.

# 6. Wash DNA-bound beads

Goal: wash contaminants away while keeping DNA bound to the capture beads.

1. Let beads settle briefly.
2. Remove liquid carefully without removing beads.
3. Add 500 µL gDNA Wash Buffer.
4. Invert gently 2–3 times.
5. Remove wash buffer carefully.
6. Add another 500 µL gDNA Wash Buffer.
7. Invert gently 2–3 times.
8. Remove wash buffer carefully.
9. Remove as much residual wash as practical without touching or removing beads.

Critical:

Copy
gDNA Wash Buffer must already have ethanol added.

# 7. Elute genomic DNA

Goal: release purified genomic DNA from the Monarch capture beads.

1. Put bead retainer into Monarch collection tube.
2. Transfer/pour beads into the retainer.
3. Pulse spin ≤1 second.
4. Move beads to a clean Monarch tube.
5. Add 100 µL Elution Buffer II.
6. Incubate at 56°C for 5 minutes.
7. Put bead retainer over a clean DNA LoBind tube labeledExtracted DNA.
8. Transfer eluate + beads into bead retainer.
9. Spin at 12,000 × g for 30 seconds.
10. Keep the eluate.

The eluate is the purified genomic DNA.

Do not discard the eluate.

# 8. Measure quantity of DNA with a Fluorometer

Goal: measure whether there is enough DNA to justify ONT library prep.

Use:

Copy
1x dsDNA High Sensitivity

Do not select the older non-1X dsDNA HS workflow if using the premixed 1X reagent.

## Standards

Standard #1:

Copy
190 µL 1X dsDNA HS working solution
10 µL Standard #1

Standard #2:

Copy
190 µL 1X dsDNA HS working solution
10 µL Standard #2

## Sample, first attempt

Copy
198 µL 1X dsDNA HS working solution
2 µL DNA

On Qubit, enter:

Copy
Sample volume = 2 µL

## If too low

Use more DNA in a fresh Qubit tube:

Copy
190 µL 1X dsDNA HS working solution
10 µL DNA

On Qubit, enter:

Copy
Sample volume = 10 µL

Do not just add 8 µL to the old 198 + 2 tube, because that makes 208 µL total and breaks the assay math.

Record:

Copy
Genomic DNA concentration:
Remaining DNA volume:
Estimated total DNA:

Calculate:

Copy
total DNA ng = Qubit concentration ng/µL × remaining volume µL

# Pause point

This is the best place to pause. For a same-day break:

Copy
Store extracted DNA at 4°C / fridge.

Before storing:

1. Make sure the DNA is in a clearly labeled DNA LoBind tube.
2. Quick spin.
3. Do not vortex.
4. Close tube tightly.
5. Put it in the fridge.

Resume at Step 10.

# 9. Prepare DNA input for repair/end-prep

Goal: prepare 47 µL DNA input.

Ideal target:

Copy
1,000 ng DNA in 47 µL

Calculate:

Copy
DNA volume needed = 1000 ng / Qubit concentration ng/µL

Then:

Copy
water volume = 47 µL - DNA volume

If the DNA is too dilute and 1,000 ng cannot fit into 47 µL, use the maximum possible volume:

Copy
47 µL extracted DNA
0 µL water

For the first low-input run:

Copy
0.296 ng/µL × 47 µL = ~13.9 ng DNA

That was far below the recommended input, but useful as an end-to-end practice run.

# 10. Repair / end-prep

Goal: repair DNA and prepare the ends for adapter ligation.

Use the actual v2 reagents:

Copy
FFPE DNA Repair Buffer v2
FFPE DNA Repair Mix
N-Prep Enzyme Mix / Ultra II End Prep Enzyme Mix

Do not use Salt-T4 DNA Ligase in this step. It is used later.

If not using DCS, replace the optional 1 µL DCS with 1 µL nuclease-free water.

## Reaction

Copy
47 µL DNA
1 µL nuclease-free water
7 µL FFPE DNA Repair Buffer v2
2 µL FFPE DNA Repair Mix
3 µL N-Prep Enzyme Mix

Total = 60 µL

## Steps

1. Add 47 µL DNA to a 0.2 mL thin-walled PCR tube labeledEnd-prep.
2. Add 1 µL nuclease-free water.
3. Add 7 µL FFPE DNA Repair Buffer v2.
4. Pipette mix 10–20 times.
5. Add 2 µL FFPE DNA Repair Mix.
6. Pipette mix 10–20 times.
7. Add 3 µL N-Prep Enzyme Mix.
8. Pipette mix 10–20 times.
9. Quick spin.

Incubate:

Copy
20°C for 5 minutes
65°C for 5 minutes
Then place on ice

# 11. AMPure cleanup after repair/end-prep

Goal: clean the repaired/end-prepped DNA.

Input:

Copy
60 µL repair/end-prep reaction
1. Resuspend AMPure XP beads until uniformly brown.
2. Add 60 µL AMPure XP beads to the 60 µL reaction.
3. Mix gently by pipetting 10 times.
4. Incubate 5 minutes at room temperature.
5. Put tube on magnet.
6. Wait until solution clears.
7. Remove and discard supernatant without touching beads.

## Wash 1

1. Keep tube on magnet.
2. Add 200 µL fresh 80% ethanol.
3. Remove ethanol.

## Wash 2

1. Add another 200 µL fresh 80% ethanol.
2. Remove ethanol.

## Dry

1. Remove residual ethanol with P10/P20.
2. Air dry briefly, about 30 seconds.
3. Do not overdry.
4. Do not let beads crack.

## Elute

1. Remove tube from magnet.
2. Add 61 µL nuclease-free water.
3. Resuspend beads gently.
4. Incubate 5–10 minutes at room temperature.
5. Put tube back on magnet.
6. Wait until clear.
7. Transfer 60 µL clear eluate to a clean DNA LoBind tube labeledLigation.

Do not transfer beads.

# 12. Adapter ligation

Goal: attach ONT sequencing adapters.

Use the actual reagents:

Copy
LNB
LA
Salt-T4 DNA Ligase

## Reaction

Copy
60 µL repaired/end-prepped DNA
25 µL LNB
10 µL Salt-T4 DNA Ligase
5 µL LA

Total = 100 µL

## Steps

1. Use a clean DNA LoBind tube labeledLigation.
2. Mix LNB slowly by pipetting before adding. It is viscous.
3. Add 60 µL repaired/end-prepped DNA.
4. Add 25 µL LNB.
5. Add 10 µL Salt-T4 DNA Ligase.
6. Add 5 µL LA.
7. Mix gently by pipetting 10–15 times.
8. Do not vortex.
9. Quick spin.
10. Incubate 10 minutes at room temperature.

Before incubation, say/check:

Copy
DNA, LNB, Salt-T4 DNA Ligase, LA.

Failure points:

Copy
Forgetting LA = no sequenceable library.
Forgetting Salt-T4 DNA Ligase = adapter ligation fails.
Poorly mixed LNB = bad ligation chemistry.
Vortexing = unnecessary DNA shearing.

# 13. Adapter-ligated library cleanup

Goal: remove free adapters, ligase, salts, and small fragments while keeping adapter-ligated DNA.

Important:

Copy
This cleanup uses LFB, not ethanol.

Input:

Copy
100 µL ligation reaction
1. Resuspend AMPure XP beads fully.
2. Add 40 µL AMPure XP beads to the 100 µL ligation reaction.
3. Mix gently by pipetting 10 times.
4. Incubate 5 minutes at room temperature.
5. Place tube on magnet.
6. Wait until solution clears.
7. Keep tube on magnet.
8. Remove and discard supernatant carefully.
9. Do not touch bead pellet.

## Wash 1

1. Add 250 µL LFB to beads.
2. Remove tube from magnet.
3. Gently resuspend beads by flicking or slow pipetting.
4. Put tube back on magnet.
5. Wait until clear.
6. Remove and discard LFB.

## Wash 2

1. Add another 250 µL LFB.
2. Remove tube from magnet.
3. Gently resuspend beads.
4. Put tube back on magnet.
5. Wait until clear.
6. Remove and discard LFB.
7. Remove residual LFB with P10/P20.
8. Do not overdry.

## Elute

1. Add 25 µL EB.
2. Remove tube from magnet.
3. Resuspend gently.
4. Incubate 10 minutes at room temperature.
5. Put tube back on magnet.
6. Wait until eluate is clear.
7. Transfer clear eluate to a clean DNA LoBind tube labeledFinal library.

This is the final sequencing library.

Practical rule:

Copy
Liquid moves. Beads stay.

Do not transfer beads into the final library.

# 14. Check quantity of DNA one more time

Goal: measure final adapted library concentration.

Because low-input runs may produce very little final library, this may read low or fail.

Use:

Copy
199 µL 1X dsDNA HS working solution
1 µL final library

On Qubit:

Copy
Sample volume = 1 µL

Record:

Copy
Final library concentration:
Final library volume:
Estimated mass loaded:

Calculate:

Copy
mass loaded ng = final library concentration ng/µL × 12 µL

If the final library is too low, do not repeatedly burn more library on Qubit. For a practice run, proceed with 12 µL library in the loading mix.

# 15. Flow cell check with MinKNOW

Goal: verify the flow cell before loading the library.

1. Take flow cell out of fridge.
2. Let it sit at room temperature for 20 minutes.
3. Keep it flat.
4. Do not shake.
5. Plug in MinION.
6. Open MinKNOW.
7. Insert flow cell.
8. Run flow cell check.
9. Record active pores.

Decision table:

Copy
>1200 pores = great
800–1200 pores = usable
500–800 pores = marginal/practice
<500 pores = bad, but still possible for mechanical practice
<200 pores = essentially not worth it except loading practice

Record:

Copy
Flow cell ID:
Starting active pores:
Flow cell age:
Previously used? yes/no:
Washed? yes/no:

# 16. Understand the final tubes and ports

At the end, there are three tubes:

Copy
Tube 1: Final library
- This is the DNA library made after adapter cleanup.

Tube 2: Priming mix
- This prepares the flow cell.

Tube 3: Loading mix
- This contains final library + sequencing buffer + library beads.

There are two flow-cell ports:

Copy
Port 1: Priming port
- This is under the sliding cover.
- Priming mix goes here.

Port 2: SpotON sample port
- This is the small sample well.
- Loading mix goes here drop by drop.

Important:

Copy
Final library does not go directly onto the flow cell by itself.
Final library first goes into the loading mix tube.

# 17. Make priming mix for ONT Flow Cell

If BSA is available:

Copy
1170 µL FCF
5 µL BSA
30 µL FCT

Total = 1205 µL

If BSA is not available and this is a practice run:

Copy
1170 µL FCF
30 µL FCT

Total = 1200 µL

Do not substitute SFB, DCS, LIS, or LNB for BSA.

Mix gently. Avoid bubbles.

This is Tube 2:Priming mix.

# 18. First prime

Do this only after flow cell check is complete. Make sure to watch this video:https://www.youtube.com/watch?v=IknVaEnuDz0. It is how you load the actual flow cell!

1. Keep flow cell plugged in and flat.
2. Open the sliding cover to expose the priming port.
3. Check for an air bubble near the port.

Draw back only 20–30 µL:

Copy
Set P1000 to 200 µL.
Put tip into priming port.
Slowly dial to 220–230 µL.
Stop as soon as liquid enters the tip.
Do not pull more.

Then load into the priming port:

Copy
800 µL priming mix

Go slowly. Avoid bubbles.

Wait:

Copy
5 minutes

# 19. Make loading mix during the 5-minute wait

Tube 3:Loading mix

Use:

Copy
37.5 µL SB
25.5 µL LIB
12 µL final library

Total = 75 µL

Important:

Copy
LIB = Library Beads from the ONT kit.
LIB is not AMPure XP beads.
LIB settles fast.
Mix LIB immediately before pipetting.

Steps:

1. Mix LIB immediately before pipetting.
2. Add 37.5 µL SB to a clean tube.
3. Add 25.5 µL LIB.
4. Add 12 µL final library.
5. Mix gently by pipetting.
6. Do not vortex.

# 20. Second prime

After the 5-minute wait, load into the priming port:

Copy
200 µL priming mix

Avoid bubbles.

# 21. Load library onto SpotON port

1. Gently mix Tube 3 loading mix immediately before loading.
2. Open the SpotON sample port.
3. Load the full 75 µL loading mix into the SpotON port.
4. Add it drop by drop.
5. Let each drop disappear before adding the next.
6. Do not force it.
7. Do not jab the port.
8. Avoid bubbles.

Then:

Copy
Close SpotON cover.
Close priming port.
Add light shield.
Close MinION lid.
Start run in MinKNOW.

Final mental model:

Copy
Priming mix → sliding priming port
Loading mix → SpotON sample port
Final library → only goes into loading mix first

# 22. Sequence DNA with MinKNOW

Recommended basic settings:

Copy
Flow cell type: FLO-MIN114
Kit: SQK-LSK114
Basecalling: ON
Model: High-accuracy / HAC
Barcoding: OFF
Alignment: OFF
Adaptive sampling: OFF
Raw reads / POD5: ON
Filtering: OFF for low-input practice runs

Then:

Copy
Save configuration
Start

For a low-input practice run, keep raw POD5 on so the data can be analyzed later even if live output is poor.

# 23. Basecall after run if needed

1. Find POD5 output directory.
2. Install Dorado.
3. Run basecalling:
Copy
dorado basecaller sup pod5_directory/ > calls.bam
1. Convert BAM to FASTQ if needed:
Copy
samtools fastq calls.bam > reads.fastq
1. For faster first pass, use HAC instead of SUP:
Copy
dorado basecaller hac pod5_directory/ > calls.bam

# 24. Align reads to human reference

1. Download GRCh38 FASTA.
2. Index reference:
Copy
minimap2-d GRCh38.mmi GRCh38.fa
1. Align reads:
Copy
minimap2-ax map-ont GRCh38.mmi reads.fastq | samtoolssort-o aligned.bam
1. Index BAM:
Copy
samtools index aligned.bam
1. Check alignment summary:
Copy
samtools flagstat aligned.bam > flagstat.txt
1. Check coverage:
Copy
mosdepth sample_cov aligned.bam

# 25. Variant calling

1. Install Clair3.
2. Use ONT model.
3. Run Clair3 with GRCh38 reference, sorted BAM, and output directory.
4. Output should include VCF.
5. Do not overinterpret low-coverage variants.
6. For a first MinION run, treat this astechnical validation, not medical-grade interpretation.

# 26. Annotation

1. Install VEP.
2. Annotate VCF against GRCh38.
3. Add ClinVar.
4. Add gnomAD.
5. Add PharmGKB later.
6. Store final table with columns:
7. chromosome
8. position
9. ref
10. alt
11. gene
12. consequence
13. ClinVar significance
14. gnomAD frequency
15. genotype
16. read depth
17. variant quality

# References

Seth Howes protocol(X profile)

DNA Quantification with Qubit

Molecular Biology of the Cell

Quantifying Life(super underrated)

Integrated Drug Discovery Technologies

Darkome

Upgrade

Sid’s cancer data

DNA Whole Genome Sequencing - astrology for sigmas

DNA sequencing at home with the flongle