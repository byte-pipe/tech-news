---
title: Aneuploidy selects for the acquisition of driver genes in breast cancer | Nature
url: https://www.nature.com/articles/s41586-026-10752-9
date: 2026-07-08
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-07-09T15:20:57.866631
---

# Aneuploidy selects for the acquisition of driver genes in breast cancer | Nature

# Aneuploidy selects for the acquisition of driver genes in breast cancer | Nature

## Abstract summary
- Chromosome instability creates large‑scale aneuploidies that are common in cancer, but their direct contribution to tumorigenesis is hard to dissect because many genes are simultaneously altered.  
- The authors introduced **CRISPR‑KOALA**, a high‑throughput CRISPR knockout and activation platform that enables bidirectional genetic screens in immunocompetent mouse cancer models.  
- Focusing on basal‑like breast cancer (BLBC), they compiled the ten most frequent chromosome‑arm‑level copy‑number alterations (CNAs) observed in human tumours.  
- Screening mouse orthologues of 3,752 genes located on these arms identified **90 cancer driver genes**, most of which were previously uncharacterised.  
- These drivers act through diverse pathways (MAPK, HIPPO, WNT), reflecting the heterogeneity of BLBC.  
- Manipulating the identified drivers removes the requirement for arm‑level CNAs in Trp53‑mutant BLBC mouse models.  
- The study highlights **PLGRKT** on chromosome 9p as a potent oncogene whose tumor‑promoting activity is linked to stress‑resistant mitochondria and enhanced reactive‑oxygen‑species detoxification.  
- Overall, arm‑level CNAs appear to select for specific driver genes that promote heterogeneous biological processes in breast cancer.

## Experimental approach
- Developed CRISPR‑KOALA, combining loss‑of‑function (KO) and gain‑of‑function (activation) CRISPR libraries for in vivo screening.  
- Generated a compendium of the ten most recurrent chromosome‑arm CNAs in human BLBC from large genomic datasets.  
- Designed sgRNA libraries targeting the mouse orthologues of all protein‑coding genes within these arms (3,752 genes).  
- Performed parallel CRISPR‑KO and CRISPR‑activation screens in Trp53‑mutant BLBC mouse models with intact immune systems.  
- Integrated screen results with transcriptomic and copy‑number data from human tumours (METABRIC, TCGA) to prioritize candidate drivers.

## Key findings
- **90 driver genes** were uncovered; the majority lack prior functional annotation in cancer.  
- Identified drivers cluster into distinct signaling modules:
  - MAPK pathway activators  
  - HIPPO pathway regulators  
  - WNT signaling components  
- Functional validation showed that overexpression or loss of individual drivers can initiate tumor formation without the need for the original arm‑level CNAs.  
- **PLGRKT** emerged as a novel oncogene:
  - Located on chromosome 9p, frequently amplified in BLBC.  
  - Overexpression reprograms mitochondria to become highly stress‑resistant.  
  - Enhances cellular capacity to detoxify reactive oxygen species, supporting tumor growth.  
- Manipulating driver genes reshapes transcriptional heterogeneity in both mouse and human BLBC tumours, linking specific CNAs to distinct cellular phenotypes.

## Biological and clinical implications
- Arm‑level CNAs function less as bulk genomic chaos and more as a selection mechanism for a limited set of potent driver genes.  
- The diversity of identified pathways explains the pronounced heterogeneity of BLBC and suggests multiple therapeutic entry points.  
- Targeting newly discovered drivers, such as PLGRKT, could provide strategies to counteract aneuploidy‑driven tumor fitness.  
- The CRISPR‑KOALA platform offers a scalable method to dissect the functional impact of large‑scale genomic alterations in other cancer types.

## Data and code availability
- RNA‑seq data: GEO accession **GSE274219**.  
- Whole‑genome sequencing data: SRA accession **PRJNA114634**.  
- Gene‑level copy‑number calls: Figshare DOI **10.6084/m9.figshare.32144932**.  
- Public datasets used: METABRIC, TCGA (accessible via cBioPortal and Xena Browser).  
- OncoKB cancer‑gene list: https://oncokb.org/cancer-genes.  
- Human single‑cell RNA‑seq data: GEO accessions **GSE176078**, **GSE161529**, and additional resources from the Lambrechts lab.  
- No new code was written; single‑cell processing and CNA analysis scripts are available on GitHub at **https://github.com/dpcook/blbc_cna**. References to all other software are provided in the Methods section.