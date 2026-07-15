---
title: A Bayesian framework for longitudinal EHR and genetic discovery | Nature
url: https://www.nature.com/articles/s41586-026-10780-5
date: 2026-07-15
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-07-16T03:39:25.504028
---

# A Bayesian framework for longitudinal EHR and genetic discovery | Nature

# A Bayesian framework for longitudinal EHR and genetic discovery

## Abstract
- Introduces **ALADYNOULLI**, a Bayesian generative model that jointly analyzes longitudinal electronic health records (EHRs) and germline genetic data.  
- Models disease risk as a mixture of latent, time‑varying disease signatures rather than a probability of a mixture, allowing simultaneous and chronic conditions to be captured.  
- Applied to three biobanks (UK Biobank, Mass General Brigham, All of Us) with > 683 000 participants, 52 years of follow‑up, and 348 diseases.  
- Identified 21 reproducible signatures with median 80 % cross‑cohort preservation; signatures reveal biological subtypes within diagnostic categories (Cohen’s d up to 4.25, P ≤ 1×10⁻⁸).  
- Signature loadings align with known biology (e.g., familial hypercholesterolemia → cardiovascular signature; clonal haematopoiesis → inflammation signature; rare‑variant burden in LDLR, TTN, BRCA2 matches disease specificity).  
- Signature‑based GWAS discovered 151 genome‑wide significant loci, including cardiovascular loci missed by single‑trait GWAS.  
- Explicit likelihood enables inverse‑probability weighting to correct selection bias while retaining biological signal.  
- Outperforms established risk calculators (PCE, PREVENT, Gail) for 1‑year and 10‑year predictions; complements code‑level foundation models such as Delphi‑2M.

## Main Contributions
- **Dynamic risk modeling**: Captures how individual disease risk evolves across the life course.  
- **Genetic integration**: Directly incorporates polygenic risk scores, sex, and ancestry PCs into the latent signature priors.  
- **Unified multi‑disease framework**: Simultaneously models the majority of prevalent EHR conditions, sharing information across related diseases and improving prediction for rare outcomes.  
- **Personalized trajectories**: Generates patient‑specific, time‑varying signature loadings that update with new clinical data.  
- **Bias adjustment**: Uses an explicit likelihood to apply inverse probability weighting for selection‑bias correction.  
- **Discovery & stratification**: Enables genome‑wide association studies on signatures, reveals sub‑phenotypes within disease categories, and supports applications such as digital‑twin identification and therapeutic targeting.

## Method Overview
- **Model structure**: For individual *i* at time *t*, disease hazard πᵢ𝑑𝑡 is a weighted sum over *K* signatures:  

  πᵢ𝑑𝑡 = κ · ∑ₖ θᵢₖ𝑡 · sigmoid(φₖ𝑑𝑡)  

  - κ: global calibration constant.  
  - θᵢₖ𝑡: softmax‑transformed, time‑varying individual‑signature loadings.  
  - φₖ𝑑𝑡: signature‑specific, age‑dependent disease log‑odds.  

- **Loadings (θ)** derived from latent variables λ via softmax:  

  θᵢₖ𝑡 = exp(λᵢₖ𝑡) / Σₖ′ exp(λᵢₖ′𝑡)  

- **Latent trajectories (λ)** follow Gaussian process priors that incorporate genetics and demographics:  

  λᵢₖ ∼ GP(rₖ + gᵢᵀ Γₖ, Ω_λ)  

  - rₖ: population reference level for signature *k*.  
  - gᵢ: vector of 47 features (36 polygenic risk scores, sex, 10 ancestry PCs).  
  - Γₖ: signature‑specific genetic effect matrix.  
  - Ω_λ: temporal covariance kernel ensuring smooth λ trajectories.  

- **Disease‑signature associations (φ)** also receive Gaussian process priors, enabling smooth, age‑dependent risk curves for each disease within each signature.

## Results
- **Signature replication**: 21 signatures identified; median 80 % overlap of disease composition across the three cohorts.  
- **Biological validation**:  
  - Cardiovascular signature enriched for FH carriers.  
  - Inflammation signature enriched for CHIP carriers.  
  - Rare‑variant burdens in LDLR, TTN, BRCA2 map to expected disease clusters.  
- **Signature‑based GWAS**: 151 loci reach genome‑wide significance; several cardiovascular loci absent in traditional single‑trait GWAS.  
- **Prediction performance**:  
  - Superior to Pooled Cohort Equation, PREVENT, and Gail models at both 1‑year and 10‑year horizons.  
  - Disease‑level (PheCode) predictions complement code‑level foundation models (e.g., Delphi‑2M).  
- **Bias correction**: Applying inverse probability weighting adjusts for selection bias without diminishing signal strength.

## Applications
- **Genomic discovery**: Leveraging shared signatures to boost power for detecting genetic associations.  
- **Risk stratification**: Generating individualized, time‑varying risk profiles for preventive interventions.  
- **Patient matching**: Identifying digital twins or subgroups with similar signature loadings for clinical trials or therapeutic targeting.  
- **Therapeutic prioritization**: Linking signatures to pathways may inform drug repurposing or novel target identification.  

## Conclusions
ALADYNOULLI provides a principled Bayesian framework that unifies longitudinal EHR data and germline genetics, uncovering latent disease signatures that are reproducible, biologically meaningful, and predictive. The approach advances both disease risk prediction and genetic discovery while offering tools for bias correction and patient stratification in large, heterogeneous biobank cohorts.