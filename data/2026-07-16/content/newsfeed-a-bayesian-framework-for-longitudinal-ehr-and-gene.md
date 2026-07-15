---
title: A Bayesian framework for longitudinal EHR and genetic discovery | Nature
url: https://www.nature.com/articles/s41586-026-10780-5
site_name: newsfeed
content_file: newsfeed-a-bayesian-framework-for-longitudinal-ehr-and-gene
fetched_at: '2026-07-16T03:37:23.448989'
original_url: https://www.nature.com/articles/s41586-026-10780-5
date: '2026-07-15'
description: 'Electronic health records&nbsp;(EHRs) provide rich longitudinal disease histories, but existing methods for analysing these data typically treat diseases in isolation1 and rarely integrate germline genetics. Here we present ALADYNOULLI, a Bayesian generative framework that jointly models longitudinal EHR diagnoses, age and polygenic risk to recover latent time-varying disease signatures and patient-specific signature loadings; the model is formulated as a mixture of probabilities rather than a probability of a mixture2, correctly accommodating simultaneous and chronic conditions. Applied to three independent biobanks (UK Biobank3, Mass General Brigham4 and All of Us; total n &gt; 683,000) spanning up to 52 years of follow-up&nbsp;and 348 diseases, the model recovers 21 replicable signatures with high cross-cohort composition preservation (median of 80%) and reveals biological subtypes within diagnostic categories (Cohen’s d up to 4.25; P ≤ 1 × 10−8 for 95% of comparisons).
  Signatures are concordant with established disease biology: carriers of familial hypercholesterolaemia5 enrich in the cardiovascular signature; carriers of clonal haematopoiesis of indeterminate potential6 in the inflammation signature; and a rare variant burden in LDLR, TTN and BRCA2 (refs. 7,8) aligns with disease specificities. A signature-based genome-wide association study identifies 151 genome-wide significant loci including cardiovascular associations missed by single-trait analyses. An explicit likelihood enables inverse probability weighting for selection bias9 while preserving biological signal. For disease prediction, ALADYNOULLI outperforms Pooled Cohort Equation (PCE), PREVENT and Gail at 1-year and 10-year horizons; disease-level (PheCode) predictions complement code-level foundation models such as Delphi-2M&nbsp;(ref.&nbsp;10). A Bayesian generative framework that integrates longitudinal electronic health records with genetic data to identify latent disease signatures is
  presented.'
tags:
- nature
---

A Bayesian framework for longitudinal EHR and genetic discovery
 

Download PDF

Download PDF

### Subjects

* Genetic markers
* Genome-wide association studies
* Predictive medicine
* Risk factors
* Statistics

## Abstract

Electronic health records (EHRs) provide rich longitudinal disease histories, but existing methods for analysing these data typically treat diseases in isolation1and rarely integrate germline genetics. Here we present ALADYNOULLI, a Bayesian generative framework that jointly models longitudinal EHR diagnoses, age and polygenic risk to recover latent time-varying disease signatures and patient-specific signature loadings; the model is formulated as a mixture of probabilities rather than a probability of a mixture2, correctly accommodating simultaneous and chronic conditions. Applied to three independent biobanks (UK Biobank3, Mass General Brigham4and All of Us; totaln> 683,000) spanning up to 52 years of follow-up and 348 diseases, the model recovers 21 replicable signatures with high cross-cohort composition preservation (median of 80%) and reveals biological subtypes within diagnostic categories (Cohen’sdup to 4.25;P≤ 1 × 10−8for 95% of comparisons). Signatures are concordant with established disease biology: carriers of familial hypercholesterolaemia5enrich in the cardiovascular signature; carriers of clonal haematopoiesis of indeterminate potential6in the inflammation signature; and a rare variant burden inLDLR,TTNandBRCA2(refs.7,8) aligns with disease specificities. A signature-based genome-wide association study identifies 151 genome-wide significant loci including cardiovascular associations missed by single-trait analyses. An explicit likelihood enables inverse probability weighting for selection bias9while preserving biological signal. For disease prediction, ALADYNOULLI outperforms Pooled Cohort Equation (PCE), PREVENT and Gail at 1-year and 10-year horizons; disease-level (PheCode) predictions complement code-level foundation models such as Delphi-2M (ref.10).

## Main

The risk of disease varies substantially between individuals and throughout life, with complex interactions between genetic predisposition, environmental factors and accumulated comorbidities. Understanding these dynamic risk patterns could transform early detection, prevention and personalized treatment strategies11,12,13. The increasing availability of large-scale EHRs linked to genetic data provides unprecedented opportunities to model these complex disease trajectories at a population scale3,14,15. However, extracting meaningful patterns from these rich, longitudinal datasets remains challenging owing to patient population heterogeneity, the temporal nature of disease progression and intricate relationships between diverse conditions.

Traditional EHR analyses treat diseases in isolation or as pairwise associations, missing how multiple conditions co-evolve1. Recent unsupervised clustering methods16typically ignore temporal dynamics, intra-disease biological variability and genetic effects on progression17,18.

We present ALADYNOULLI, a generative model that integrates germline genetic data with longitudinal EHRs to identify latent disease signatures modelling individual-specific health trajectories over time. ALADYNOULLI addresses these limitations by identifying shared disease signatures that capture biological processes common across multiple conditions, enabling more accurate prediction even for rare diseases through information sharing with related, more common conditions. ALADYNOULLI offers several key advantages over existing methods: (1) for replicable signatures, it generates disease signatures showing high cross-cohort stability and alignment with established clinical phenotypes in the cases examined (familial hypercholesterolaemia, clonal haematopoiesis and type 1 versus type 2 diabetes); (2) for temporal modelling, it captures how disease risk evolves dynamically over the life course; (3) for genetic integration, it directly incorporates genetic information into the model architecture; (4) as a unified framework, it simultaneously models the majority of prevalent conditions in the EHR, sharing information across related conditions, and improving prediction even for diseases with limited data19; (5) for individual-specific trajectories, it provides personalized risk profiles that adapt as new clinical information becomes available; and (6) for principled bias adjustment, it is grounded in an explicit likelihood specification, supporting principled adjustment for selection bias through inverse probability weighting. By jointly modelling multiple diseases and their genetic determinants, ALADYNOULLI improves disease risk prediction, enhances genetic discovery and reveals patient subgroups within diagnostic categories.

## Methods overview

Disease patterns among individuals vary by onset, progression speed and composition, reflecting different underlying biological mechanisms. ALADYNOULLI models the probability of each disease for an individual by integrating across multiple latent signatures (Fig.1).

Fig. 1: ALADYNOULLI model overview and applications.
Full size image

Hypothetical patient (#123) timeline showing the sequence and timing of major diagnoses over the life course (top). Key model components include: population-level disease signatures (φ), with each line representing the age-dependent risk trajectory for a specific disease within a signature; individual signature loadings (λ) transformed toθvia softmax, for a representative patient, showing how contributions from different signatures evolve over time; and disease risk prediction (π) for selected diseases, integrating population-level signatures and individual loadings to generate personalized risk trajectories (middle). Applications of the model, including genomic discovery, therapeutic targeting and patient matching (for example, digital twin identification or stratification of patients with the same diagnosis but different risk profiles) are also shown (bottom). CAD, coronary artery disease; COPD, chronic obstructive pulmonary disease; GERD, gastroesophageal reflux disease; T2DM, type 2 diabetes mellitus.

For each individuali, diseasedand timepointt,πidtis the hazard of disease occurrence, that is, the probability of occurrence assuming the individual is still at risk. In ALADYNOULLI, this is a weighted combination of signature-specific probabilities, in which each signature captures patterns of diseases that tend to occur together (Supplementary Table1):

$${\pi }_{idt}=\kappa \cdot \mathop{\sum }\limits_{k=1}^{K}{\theta }_{ikt}\cdot \,{\rm{sigmoid}}\,({\phi }_{kdt}).$$

 (1)
 

Here\(\,{\rm{sigmoid}}({\phi }_{kdt})=1/(1+{e}^{-{\phi }_{kdt}})\),κis a global calibration parameter,θiktis individuali’s normalized and time-varying association with signaturekat timet, andϕkdtcaptures the time-varying relationship between signaturekand diseasedat timet. The normalized individual–signature associations (loadings)θiktare derived from latent variablesλiktthrough the transformation:

$${\theta }_{ikt}=\frac{\exp ({\lambda }_{ikt})}{{\sum }_{{k}^{{\prime} }=1}^{K}\exp ({\lambda }_{i{k}^{{\prime} }t})}.$$

 (2)
 

Theλiktfollow a Gaussian process20prior where we modelled the effects of genetic factors and time (seeMethods; Extended Data Fig.1). Specifically:

$${{\boldsymbol{\lambda }}}_{ik} \sim {\mathcal{G}}{\mathcal{P}}({{\bf{r}}}_{k}+{{\bf{g}}}_{i}^{{\rm{\top }}}{{\boldsymbol{\Gamma }}}_{k},{\varOmega }_{\lambda })$$

 (3)
 

whererkis a signature-specific reference level in the population,Γkcaptures genetic effects on signature predisposition,girepresents individual genetic and demographic factors (36 polygenic risk scores (PRSs), sex and 10 genetic principal components; 47 features total) affecting the mean ofλik, andΩλis a temporal covariance kernel, modelling smooth trajectories forλiktover time.

Similarly, the disease–signature associations follow a Gaussian process prior:

$${{\boldsymbol{\phi }}}_{kd} \sim {\mathcal{G}}{\mathcal{P}}({{\boldsymbol{\mu }}}_{d}+{\psi }_{kd},{\varOmega }_{\phi })$$

 (4)
 

whereμdis a disease-specific baseline, or the logit of the population prevalence,ψkdrepresents the overall strength of association between signaturekand diseased, andΩϕallows for temporal variation in these associations.ΩϕandΩλgovern the temporal covariance of deviations from the mean trajectory and are by construction independent from the mean. By specifying Gaussian process priors as offsets of mean parameters, our model encourages temporal fluctuations to be distinct from systematic effects such as genetic predisposition or disease–signature associations.

ALADYNOULLI directly models disease occurrence as a weighted combination of signature-specific disease probabilities, and thus is formulated as a mixture of probabilities, not a probability of a mixture as in sparse factor analysis2, and not assigning diseases retrospectively as in allocation-based topic models16. This formulation lets the model predict future onset (rather than only explain observed diagnoses), accommodate multiple simultaneous disease processes per individual and model persistent chronic conditions. Givenθiktandϕkdt, diseases are conditionally independent—all modelled correlations between diseases arise because they have roles in the same signatures.

### Terminology clarification

Throughout this work, we use ‘loadings’ to refer to individual-specific signature associations (λandθ) and ‘signature–disease associations’ to refer to feature importance (ϕ), consistent with the sparse factor analysis convention. Usage differs in other fields.

### Two complementary applications

ALADYNOULLI serves two distinct but complementary purposes, each requiring different analytical approaches. For biomedical discovery, the model operates with complete hindsight, leveraging entire patient trajectories (retrospective; Extended Data Fig.1) to characterize disease signatures, quantify genetic influences and reveal patient heterogeneity within diagnostic categories. For clinical prediction, we operated under strict temporal constraints that mirror real-world clinical decision-making (Supplementary Fig.1): a rigorous temporal validation framework uses only information available up to each prediction timepoint, following established temporal validation and landmarking conventions21,22,23. This prospective approach reflects real-world clinical use, in which physicians must predict future risk based solely on the history of a patient to date, and ensures that performance metrics reflect true predictive capability rather than retrospective explanation.

## Cross-cohort signature consistency

We applied ALADYNOULLI to three independent biobanks: UK Biobank (UKB;n= 427,239), Mass General Brigham (MGB;n= 48,069) and All of Us (AoU;n= 208,263)3,4(Supplementary Table2and Supplementary Fig.2). International Classification of Diseases, 10th Revision (ICD-10) codes were mapped to 348 PheCodes24,25,26(each with 1,000 or more UKB occurrences, as in ref.16; PheCodes are present in all three cohorts;Methods).

Despite differences in population characteristics, healthcare systems and data collection methodologies across these cohorts, our model identified remarkably consistent signature patterns (Extended Data Figs.2and3, Supplementary Table3and Supplementary Figs.3–5).

We set the number of signatures for training toK= 21, comprising 20 disease signatures and 1 low-incidence signature. Estimated signatures are stable across both cohorts and data subsets within a cohort (Supplementary Fig.6). The signatures capture distinct and recognizable disease processes including cardiovascular, metabolic, pulmonary, psychiatric, musculoskeletal and oncological conditions (see Supplementary Table3for full characterization). Each signature demonstrates characteristic temporal patterns, with disease probabilities evolving with age; these are stable across biobanks (Fig.2a, Extended Data Fig.3and Supplementary Figs.3and4). For example, the non-ischaemic cardiovascular signature shows steadily increasing probabilities for atrial fibrillation and heart failure after 55 years of age, whereas the malignancy signature displays a sharp rise in metastatic disease probabilities between 60 and 75 years of age. Theψkdcapture the association between diseases and signatures, and vary within signatures as empirically determined during training (Fig.2b). The model also captures clinically expected temporal disease progression: hypercholesterolaemia precedes myocardial infarction within the ischaemic cardiovascular signature, whereas primary malignancies precede metastatic disease within the cancer signature (Fig.2e). These nuanced temporal relationships emerge directly from the model without explicit encoding, demonstrating the ability of ALADYNOULLI to learn clinically meaningful disease trajectories.

Fig. 2: Population-level disease signatures inferred by ALADYNOULLI.
Full size image

a, Age-dependent log hazard ratios (ϕkdt, posterior pooled across 40 batches) for four representative signatures from the UKB: ischaemic cardiovascular (signature 5), metastatic cancer (signature 6), cerebrovascular (signature 11) and pulmonary/smoking (signature 14). The coloured lines are diseases assigned to the signature; the grey lines are background diseases.b, Static signature–disease association heatmap (\({\widehat{\psi }}_{kd}\), posterior averaged across 40 UKB batches); diseases are ordered by signature assignment (\(\arg {\max }_{k}\,{\psi }_{kd}\)) and sorted within each signature by descendingψ. GI, gastrointestinal.c, Model-predicted age-specific disease probabilities\({\bar{\pi }}_{dt}\)averaged overn= 400,000 individuals (equation (1);Methods); disease ordering matches panelb.d, Heatmaps showing composition preservation probability between UKB and two validation cohorts (MGB (left) and AoU (right)). Disease-to-signature assignments were determined using maximum posteriorψvalues (argmaxk(ψkd)). For each UKB signaturek, the composition preservation probability was calculated as the proportion of diseases in that signature that also belong to its best-matching signature in the comparison cohort. Median composition preservation probability of 0.838 (83.8%) for MGB and 0.782 (78.2%) for AoU.e, Cross-cohort signature trajectories (ϕkdt) for ischaemic cardiovascular (top; UKB and MGB signature 5, and AoU signature 16) and metastatic cancer (bottom; UKB and MGB signature 6, and AoU signature 11), restricted to diseases present in all three cohorts.

The average age-specific hazard for a wide range of diseases are visualized in Fig.2c, highlighting temporal risk patterns. Furthermore, the tensor structure of the model (Supplementary Fig.7), enables rapid disease hazard calculation using the average loadings (equation (3)) and population-levelϕkd.

These signature patterns show strong consistency across the three independent biobanks (Fig.2d, Extended Data Fig.3and Supplementary Figs.3and4). For example, when comparing the membership of diseases within signatures between any two biobanks (with disease-to-signature assignments determined by posterior fitting using the signature with maximum posterior association strength, argmaxk(ψkd)), we observed high concordance (median composition preservation probability index = 0.80, interquartile range = 0.667–0.964) across all pairwise comparisons between biobanks (Extended Data Fig.2). Figure2eillustrates this consistency for two important signatures: cardiovascular disease and malignancy. Despite differences in healthcare system and coding practices, the temporal patterns of key diseases within these signatures remain remarkably consistent.

## Heterogeneity within disease categories

Personalized trajectories reveal heterogeneity within disease categories. ALADYNOULLI provides individual-specific trajectories through the time-varyingλiktparameters that reveal distinct disease progression patterns. Figure3aillustrates how individual disease journeys reveal biological differences among patients sharing the same diagnosis, reflecting heterogeneity—that is, the presence of distinct subgroups with different underlying disease signature distributions—within the diagnostic category. This example patient (an illustrative case modified from real data to protect participant identity) demonstrates a complex trajectory with multiple diseases across diverse signatures. The figure shows the signature loadings (θ) of a patient over time, their disease timeline and the time-varying disease probabilities (π) for diagnosed conditions, demonstrating how ALADYNOULLI integrates multiple data types to provide a comprehensive view of disease progression. Additional examples (Supplementary Fig.8, also modified from real data to protect participant identity) demonstrate diversity in temporal loadings that would be missed by a constant loadings approach. Our model also illustrates how individual-level trajectories and population phenomena combine to produce time-varying personalized disease probabilities (Supplementary Fig.9): overall risk can be decomposed into the contributions of the time-varying population-level signature loadings of an individual, demonstrating the complex interplay between multiple signatures in determining disease risk.

Fig. 3: Individual-level trajectories and dynamic risk profiles.
Full size image

a, Patient-specific posterior normalized signature loadings (θikt= softmax(λikt)) and disease probabilities (πidt) for a representative individual (an illustrative case, modified from real data to protect participant identity, 20 diseases, 55–76 years of age). Posterior signature loadingsθiktacross 21 signatures (top); the inset shows time-averagedθ(stacked bar). Disease timeline with diagnoses (circles; bottom left), and the top 20 disease probabilitiesπidtgrouped by signature (bottom right) are also shown. AV, atrioventricular.b, Comparison of early-onset myocardial infarction (MI; younger than 55 years of age,n= 3,609) and late-onset MI (70 years of age or older,n= 7,575) showing posterior signature loadings and their temporal velocities. Mean signature loadings\({\bar{\theta }}_{kt}\)(top) and temporal velocity\({v}_{kt}=d{\bar{\theta }}_{kt}/dt\)(bottom) are shown. The vertical dashed lines indicate average age of diagnosis.c, Signature heterogeneity within disease subtypes: deviations from population reference for three diseases (MI, malignant neoplasm of female breast and major depressive disorder). For each disease, patients with the disease were clustered into three groups usingk-means clustering on time-averaged posterior signature loadings (\({\bar{\theta }}_{ik}=\frac{1}{T}{\sum }_{t}{\theta }_{ikt}\)). Deviations from population reference:\(\Delta {\theta }_{ckt}={\bar{\theta }}_{ckt}-{\theta }_{kt}^{\,{\rm{ref}}}\); each row is one disease with three clusters (nshown in parentheses). Black dashed lines are set at 0 for reference. Sig., signature. Panelsa–care descriptive visualizations; no formal hypothesis tests were applied.

Aggregating these individual patterns reveals distinct group-level differences. In a retrospective analysis, the comparison of early-onset (55 years of age or younger, mean age of event 49.9 years) and late-onset (70 years of age or older, mean age of onset 74.6 years) myocardial infarction in Fig.3bshows that early-onset patients exhibit a higher and earlier peak in their signature 5 contribution, as well as a more rapid increase in signature loading before the event, than late-onset cases. Different trajectory characteristics suggest that early-onset and late-onset myocardial infarction, although sharing the same clinical diagnosis, may result from distinct disease processes, requiring different preventive strategies.

To illustrate differences in signature composition among patients with the same clinical diagnosis for three representative diseases (myocardial infarction, breast cancer and major depressive disorder), we applied a descriptivek-means clustering to the time-averaged signature loadings of patients for each disease (Fig.3c). We first identified patient subgroups using average signature associations, then visualized temporal deviations from population reference trajectories for each cluster, potentially identifying strata that may guide clinically actionable patient separation. A complementary deviation-based clustering approach confirmed these patterns across biobanks (Supplementary Fig.10).

We then calculated cluster-specific Cohen’s effect sizes27\({C}_{ck}^{{\rm{SIG}}}\)as follows (Methods; Supplementary Fig.11). For clustercand signaturek,\({C}_{ck}^{{\rm{SIG}}}\)is the standardized difference in mean time-averaged signature loadings between individuals in clustercand those in all other clusters (see Supplementary Fig.11). This is a measure of how distinct each cluster is with regard to each disease signature.

This analysis revealed that the majority of signature differences between clusters were not only large in magnitude (with many\({C}_{ck}^{{\rm{SIG}}}\)values exceeding 0.8, and some as high as 2.5–4.2), but also highly statistically significant (P≤ 1 × 10−8for nearly all clusters). The largest effect size occurs in major depressive disorder, for the pain/inflammatory/metabolic signature 7 (characterized by asthma, migraine, osteoporosis, depression and obesity) in cluster 1, which showed\({C}_{1,7}^{\,{\rm{SIG}}}=2.76\)(P≈ 0), revealing a depression subgroup with strong inflammatory comorbidities. In myocardial infarction, signature 5 (encompassing coronary atherosclerosis, ischaemic heart disease and hypercholesterolaemia) shows\({C}_{2,5}^{\,{\rm{SIG}}}=2.82\)(P≈ 0) in cluster 2, indicating substantial heterogeneity between patient subgroups. In breast cancer, the gynaecological signature 8 shows the strongest differentiation (\({C}_{1,8}^{\,{\rm{SIG}}}\)= 4.25,P≈ 0), whereas the pain/inflammatory/metabolic signature (signature 7) achieved near-complete patient separation in breast cancer cluster 2 (\({C}_{2,7}^{\,{\rm{SIG}}}\)= 2.53,P≈ 0).

We quantified PRS variability across patient clusters using Cohen’s effect sizes\({C}_{cp}^{{\rm{PRS}}}\), revealing substantial differences in PRSs between patient subgroups that parallel the biological variation observed in signature loadings (Fig.4). These clusters show elevated disease-specific PRS patterns (for example, cardiovascular PRS enrichment in myocardial infarction clusters). Together, these results demonstrate that the observed heterogeneity is both quantitatively substantial and statistically robust, supporting the biological relevance of the patient subgroups that we identified (Supplementary Fig.11).

Fig. 4: Genetic architecture and polygenic risk stratification of ALADYNOULLI disease signatures.
Full size image

a, Lead variants from GWAS (151 lead variants across our 21 signatures) and rare variants from RVAS (Mask3 LoF variants, 59 associations and 18 unique genes). For signature 5, 23 unique loci (green; exact lead-SNP matching versus constituent-trait GWAS; 10 unique loci by ±1-Mb window overlap). Tests are two-sided REGENIE (v3.4) step 2 on rank-normalized average signature exposure over time (AEX) phenotypes (covariates: age, sex, 10 principal components, batch); common-variant GWAS MAF > 1%,P< 5 × 10−8; RVAS MAF < 0.1% with LoF + missense score > 0.8 mask, BonferroniP< 2.5 × 10−6across 18,464 genes per signature. Full methodology is in theMethodssection.b, Number of genetic associations per signature: lead variants (GWAS, dark grey) and rare variants (RVAS, light grey). Signature 5 shows 56 total associations.c, UpSet plot showing overlap of genome-wide significant loci between signature 5 AUC and cardiovascular traits (1-Mb window overlap). Largest intersection: 35 variants shared across all six cardiovascular traits plus signature 5 AUC. IHD, ischaemic heart disease.d, Mean PRS values by cluster for three diseases (myocardial infarction, breast cancer and major depressive disorder). Patients are clustered as in Fig.3c; the top 20 PRS traits by absolute Cohen’sdare shown. Red denotes positive PRS (higher genetic risk); and blue indicates negative PRS (lower genetic risk). Cohen’sdvalues are inSupplementary Data. AAM, age at menopause; AD, Alzheimer’s disease; AF, atrial fibrillation; AST, asthma; BD, bipolar disorder; BMI, body mass index; CRC, colorectal cancer; CVD, cardiovascular disease; EOC, epithelial ovarian cancer; HbA1c DF, glycated haemoglobin (diabetes-free); HDL, high-density lipoprotein; HT, hypertension; ISS, ischaemic stroke; MEL, melanoma; MS, multiple sclerosis; PC, prostate cancer; PD, Parkinson’s disease; PSO, psoriasis; RA, rheumatoid arthritis; SCZ, schizophrenia; SF, statin-free; SLE, systemic lupus erythematosis; T1D, type 1 diabetes; T2D, type 2 diabetes; VTE, venous thromboembolism.

## Ancestry adjustment

We also investigated how genetic ancestry influences signature loadings across the life course, revealing that ancestry-specific signature enrichment patterns vary with age (Extended Data Fig.4). Genetic ancestry was modelled through principal components of the genotype matrix. For South Asian ancestry, cardiovascular signature 5 shows strong enrichment that peaks around 50–60 years of age (deviation of 0.025–0.03 when principal components are excluded), and the effect of ancestry is larger when principal components are included (peak deviation of 0.06 at 60 years of age, remaining elevated at 0.04 by 80 years of age). East Asian ancestry shows enrichment in signature 8 and signature 9, with patterns that become more pronounced when principal components are included. These temporal patterns demonstrate that ancestry effects on signatures evolve across the life course, with peak deviations occurring at different life stages for different ancestries.

### Genetic architecture of signatures

A key innovation of ALADYNOULLI is its integration of genetic information directly into the model through theΓkparameters, which capture how polygenic risk scores (PRSs) influence signature loadings. Using a comprehensive collection of 36 externally validated PRSs developed independently of our signature analysis28, we identified 116 significant PRS–signature association coefficients out of 756 candidate combinations (false discovery rate < 0.05 using Benjamini–Hochberg correction on two-sided posterior tail probabilities; Extended Data Fig.5). We observed the strongest genetic effects for signatures with known heritable components: coronary artery disease PRS with the cardiovascular signature (signature 5,γ= 0.153,Z= 27.2,P< 10−15), low-density lipoprotein (LDL) cholesterol PRS with signature 5 (γ= 0.071,Z= 22.7,P< 10−15) and type 2 diabetes PRS with the metabolic signature (signature 15,γ= 0.154,Z= 58.3,P< 10−15). The complete PRS–signature association table is provided in ref.29. These results demonstrate that genetic factors directly influence disease signature trajectories, consistent with the high heritability of these disease categories.

For the genetic association analyses below, we defined a ‘lifetime signature exposure’ phenotype per signature (area under the loading curve across follow-up; Extended Data Fig.6) using a model retrained with the PRS term removed from theλprior to avoid circularity, and tested 6,418,439 imputed variants (minor allele frequency (MAF) ≥ 0.01, imputation information score (INFO) ≥ 0.7;Methods).

Linkage disequilibrium score regression30on 930,186 variants revealed significant single-nucleotide polymorphism (SNP)-based heritability across signatures (Supplementary Table4): strongest for cardiovascular (h2= 0.041, s.e. 0.003), musculoskeletal (h2= 0.035, s.e. 0.002) and pain/inflammation (h2= 0.027, s.e. 0.002). Because signature phenotypes are continuous (area under the loading curve), heritability is on the observed scale; theh2for signature met or exceeded the observed-scaleh2for constituent binary traits computed identically for comparability (Supplementary Table5). Genetic correlations (rg) between signature genome-wide association studies (GWAS) and external complex-trait GWAS recover the expected signature–trait associations (for example, signature 5 with cardiovascular outcomes; Supplementary Fig.12). Common variant GWAS identified 151 genome-wide significant loci across our 21 signature GWAS, with the cardiovascular signature (signature 5) alone accounting for 56 lead loci. The strongest associations revealed signature-specific genetic architectures: signature 5 showed strong signals atLPA(rs10455872),APOE(rs7412) andPCSK9(rs11591147), which are all established lipid metabolism genes31,32. The metabolic/diabetes signature identifiedTCF7L2(rs7903146), the strongest known type 2 diabetes risk variant33, whereas the musculoskeletal signature identifiedGDF5(rs143384), a well-established gene associated with osteoarthritis34, the ophthalmological signature (signature 10) capturedHTRA1andCFH, a key age-related macular degeneration gene, whereas the hepatobiliary signature (signature 18) showed the strongest overall signal atABCG8(rs11887534), a gallstone risk gene, while also revealing additional loci warranting further investigation. Cross-signature connections also revealed shared genetic architecture:APOEappeared in both the cardiovascular signature (signature 5) and the infectious/critical care signature (signature 16), reflecting its dual role in cardiovascular and neurodegenerative disease risk.

We found that 23 of the 56 annotated loci for signature 5 were not found as lead loci in our own single-trait constituent cardiovascular GWAS using exact lead-SNP matching, including associations near genes with established roles in cardiovascular disease35(IL6R(rs6687726),SCARB1(rs11057839),SMAD3(rs56375023),PDGFD(rs1384705) and others; Supplementary Table6). Using a ±1-Mb window overlap instead of exact lead-SNP matching, 10 of the 56 signature 5 lead loci have no constituent–trait lead locus within ±1 Mb in our analyses. Pleiotropy interpretation and candidate follow-up loci are discussed in Supplementary Note4. Accordingly, when associating significant loci in each signature with component trait genotype dosage, we found similar improvements across signatures (Supplementary Fig.13), supporting that our latent signatures reproduce constituent–trait associations and in many cases identify additional variants, demonstrating enhanced genetic discovery power of latent signatures resulting from aggregation of related phenotypes.

We also performed gene-based rare variant association studies (RVAS) using aggregated rare variants within genes, testing whether gene-level rare variant burden is associated with signature exposure. This analysis tested 18,464 genes per signature using REGENIE gene-based association tests with loss-of-function (LoF) and deleterious missense variants (Mask3: LoF, DelMis09 and DelMis08), identifying 18 unique genes with genome-wide significant associations (P< 2.5 × 10−6after Bonferroni correction) across 21 signatures. The ischaemic cardiovascular signature (signature 5) demonstrated association with four significant genes after false discovery correction—LDLR,APOB,LPAandCDH26—all with established roles in lipid metabolism and cardiovascular disease7,36. Signature 0 (heart failure/arrhythmia) showed a highly significant association withTTN(P= 1.0 × 10−21), encoding the cardiac structural protein titin8, whereas signature 16 (infectious/critical care) was associated withTET2,PKD1andBRCA2(Supplementary Table7). Gene-by-gene biological interpretation for each RVAS hit is provided in Supplementary Note5. These rare variant associations were robust across multiple variant masks (tested across six progressively inclusive functional impact categories; Extended Data Fig.7, top panels; full per-mask gene-level results in Supplementary Tables8–12). Finally, for each signature–gene pair identified through RVAS, we computed correlations between rare variant burden and disease presence across all diseases. We then plotted gene–disease correlations (xaxis) against the corresponding disease–signature loadings (yaxis) for diseases with statistically significant gene–disease correlations (P< 0.05). This pair-level analysis serves as an orthogonal check on signature-level RVAS hits: a gene whose rare-variant burden correlates with diseasedshould, in the presence of an underlying mechanism, also have diseasedload on the signature where the gene was discovered. We observed this concordance across the robust gene–signature pairs as is the case forLDLR–signature 5 with hypercholesterolaemia and coronary disease,TTN–signature 0 with cardiomyopathies andBRCA2–signature 3 with breast cancer.

To further demonstrate the biological relevance of our signatures, we examined signature enrichment in specific high-risk populations with known genetic predispositions (Extended Data Fig.8). For example, familial hypercholesterolaemia is caused by mutations inLDLR,APOBorPCSK9, leading to severely elevated levels of LDL cholesterol and premature cardiovascular disease5, making carriers with familial hypercholesterolaemia an ideal validation population for cardiovascular signature enrichment. We compared the proportion of carriers of familial hypercholesterolaemia versus non-carriers who showed a pre-event rise in cardiovascular signature 5 loadings (defined as an increase over the 5 years preceding their first cardiovascular event). Carriers of familial hypercholesterolaemia showed significantly higher rates of pre-event signature 5 activation than non-carriers (odds ratio = 1.63, Fisher’s exact testP= 0.017), providing evidence that signature 5 captures cardiovascular risk pathways.

We also validated signature associations using carriers of clonal haematopoiesis of indeterminate potential (CHIP), demonstrating enrichments consistent with the established biology of CHIP. CHIP mutations cause chronic inflammation and are associated with increased risk of haematological malignancies, cardiovascular disease and other inflammatory conditions37. Our analysis reveals that carriers of CHIP show strong enrichment in signature 16 (infectious/critical care) before multiple outcomes:DNMT3Acarriers show 1.97-fold enrichment (OR = 1.97,P= 0.0007) for signature 16 before leukaemia/myelodysplastic syndrome) events, with 81.1% of carriers showing rising trajectories compared with 68.5% of non-carriers (Extended Data Fig.8b).TET2carriers similarly showed enrichment in signature 16 before cardiovascular and inflammatory outcomes, consistent with the known association of CHIP with chronic inflammation and increased cardiovascular risk37.

#### Inverse probability weighting

As the UKB may be enriched in healthy individuals38, we assessed the effect of such potential bias on the model with inverse probability weighting. A key advantage of the model specification of ALADYNOULLI is its ability to adjust for this selection bias by weighting individual terms of the likelihood function inversely to their probability of participation. This preserves interpretation of all model components, including biological disease–signature relationships, a capability that distinguishes our approach from black-box machine learning methods that cannot easily incorporate such principled adjustments. Detailed inverse probability weighting validation procedures (forwards 90%-female-dropped controlled experiment; reverse real-world participation bias correction using a published lasso participation model) are provided in theMethods. In both validation experiments described in theMethodsand Extended Data Fig.10, the signature–disease associations (ϕ) remain stable (correlation > 0.999, mean absolute difference < 0.002), demonstrating that core biological patterns are preserved, whereas individual loadings (λ) adapt to reflect the reweighted population distribution. This structural separation enables principled bias correction while preserving signature stability.

## Dynamic risk assessment

A primary motivation for modelling longitudinal disease patterns is to improve prediction of future disease events. To rigorously evaluate the predictive performance of ALADYNOULLI, we implemented comprehensive validation strategies that avoid information leakage between training and testing, and mimic real-world clinical follow-up (Supplementary Table13).

### Primary evaluation: dynamic 1-year predictions

Our primary evaluation (Fig.5) evaluated predictions at multiple fixed timepoints21: we computed 1-year risk predictions at 10 distinct timepoints during follow-up (enrolment + 0, 1, 2 ... 9 years). At each timepoint, we retrained models using only data available up to that point and evaluated performance on 1-year outcomes. We report the median area under the curve (AUC) across these 10 dynamic 1-year predictions, which captures how predictive accuracy evolves as patients accumulate new diagnoses over time and reflects how the model would be used in clinical practice.

Fig. 5: Multi-disease risk prediction performance and model interpretation.
Full size image

a, AUC for 1-year and 10-year predictions across 28 diseases (Methods): ALADYNOULLI 1-year enrolment (red); 1-year median across years 0–9 (light blue); 10-year enrolment (dark blue); Cox 10-year age, sex and family history (orange); PCE, PREVENT and QRISK3 (ASCVD only); and Gail (breast cancer, female only). Prevalent disease excluded; data restricted to prediction time. The centre points show the empirical AUC; the error bars indicate 95% confidence intervals derived fromn= 100 bootstrap iterations (sampling participants with replacement, with iterations yielding a single-class outcome distribution skipped) of the held-out test set. Sample sizes:n= 400,000 biologically independent UKB participants (40 leave-one-out batches ofn= 10,000 each) for full-cohort metrics;n= 10,000 participants in the held-out batch used for the ROC analysis in panelband the washout analysis in panelc. AUCs across methods were compared via overlap of their 95% bootstrap confidence intervals; no separate hypothesis test was applied to pairwise method comparisons. CKD, chronic kidney disease.b, ROC curves for ALADYNOULLI 1-year ASCVD predictions (years 0–9; year 0 AUC = 0.881, years 1–9 AUCs = 0.848–0.902) versus PCE (0.678) and PREVENT (0.653) in the 10,000-person held-out test set.c, Washout period impact: AUC for 1-year (top) and 10-year (bottom) predictions with 0-month, 1-month, 3-month or 6-month exclusions before prediction timepoint. The bars denote no washout (light brown), 1 month (medium brown), 3 months (darker brown) and 6 months (darkest brown). Dashed horizontal lines indicate the 50% bar corresponding to no discrimination.d, Calibration plot (log–log scale): predicted versus observed event rates from posteriorπidtat enrolment, binned in log space (50 bins, 10,000 or more observations per bin). MSE, mean squared error.

All individuals contribute EHR data from their first interaction with the EHR (with a conservative minimum at 30 years of age), providing decades of longitudinal disease history. Individuals enrolled in the UKB between 2006 and 2010 at 40–70 years of age (median 54 years of age; see Supplementary Fig.1) and were followed for a median of 14.4 years until 2023–2024 (see Supplementary Fig.14). All predictions were generated using cross-validation (excluding each batch in turn from training when generating its predictions) to ensure robust, generalizable performance estimates. This evaluation demonstrates robust performance across diseases (0.879 for atherosclerotic cardiovascular disease (ASCVD), 0.867 for breast cancer, 0.801 for atrial fibrillation, 0.811 for heart failure and 0.796 for Parkinson’s disease; Supplementary Table14).

### Comparison with existing benchmarks: 1-year and 10-year predictions

For comparison with traditional clinical risk scores, we also evaluated predictions made at recruitment (using models trained with data up to enrolment) against both 1-year and 10-year outcomes (ALADYNOULLI 1 year and 10 years; Fig.5a). This comparison between ALADYNOULLI and traditional risk scores is only feasible at enrolment (that is, 2006–2010 in the UKB; Supplementary Fig.1) because of availability of the necessary input. At enrolment, 1-year predictions show good performance (0.881 for ASCVD, 0.782 for breast cancer, 0.797 for atrial fibrillation and 0.769 for heart failure). Ten-year predictions, as expected, are less precise, but we maintained predictive power (0.733 for ASCVD, 0.674 for all cancers and 0.651 for diabetes; Supplementary Table14). It is important to note that for the vast majority of the 348 conditions considered, there is no established lifetime risk model in current clinical practice. All analyses were performed strictly prospectively, ensuring that only data available up to prediction time were used for each individual predicted. Individuals with prevalent disease at prediction time were excluded (seeMethods).

We also evaluated a dynamic 10-year rolling interpolation approach that demonstrates the capabilities of the model with time-dependent information: by updating predictions annually and aggregating risk over a 10-year horizon (similar to time-dependent covariates; Supplementary Table15), this approach shows how the probability estimates of the model evolve as new information becomes available. Note that this approach uses information at each year and is therefore not directly comparable with standard prediction evaluations, but provides insight into how model performance improves when incorporating time-dependent covariates (seeMethodsand Supplementary Table13). Finally, we compared with traditional Cox modelling22using age as a timescale, also on 10-year outcomes, using sex and family history when available as a predictor.

Comprehensive calibration analysis demonstrates calibration across the full range of predicted risks (mean squared error = 4.67 × 10−7), with mean predicted rates (5.55 × 10−4) closely matching mean observed rates (5.45 × 10−4) across 722,346,330 patient–time observations (at-risk only; Fig.5d). The calibration plots show alignment between predicted and observed rates.

We further evaluated the performance of ALADYNOULLI for ASCVD risk prediction, first in the general population (Supplementary Fig.15) and then in specific high-risk subgroups. In the overall cohort, ALADYNOULLI outperformed both PREVENT (AUC 0.667) and PCE (AUC 0.683; Fig.5d; receiver under the operating curves (ROCs) in Fig.5b), with performance in sex-based analyses (AUC 0.711 for ALADYNOULLI versus AUC 0.615 for PREVENT in male individuals; AUC 0.710 for ALADYNOULLI versus AUC 0.665 for PREVENT in female individuals; Supplementary Fig.16). We also evaluated the Gail model39for breast cancer, using the reported family history data for comparison in the UKB. Of note, many disease-specific clinical scores require information not available on biobank-level interviews, although the UKB did provide these variables. ALADYNOULLI compared with the Gail model showed 1-year AUCs of 0.782 versus 0.549 (difference of +0.233) for women only (Supplementary Fig.17). Per-comparator AUCs across Cox, PCE, PREVENT, QRISK3 and Gail are tabulated in Supplementary Table16.

For 10-year ASCVD risk prediction in patients with pre-existing rheumatoid arthritis or breast cancer—populations in which comorbidities can mask cardiovascular signals—ALADYNOULLI achieved AUCs of 0.694 (rheumatoid arthritis) and 0.689 (breast cancer), outperforming PREVENT (0.659 for rheumatoid arthritis and 0.544 for breast cancer; static baseline-risk approach owing to low per-year event counts; Supplementary Fig.18).

### Temporal leakage assessment

All three sensitivity analyses (reverse-causation event exclusion at 1, 3 or 6 months; 10-year time-horizon analysis; and 1-year washout-period grid 0, 1 or 2 years across enrolment + 1...9) are detailed in theMethodssection; results are shown in Supplementary Fig.19(see also Fig.5cfor 1-year and 10-year washout AUC).

## Discussion

### Contributions

We have presented ALADYNOULLI, a novel Bayesian framework for modelling dynamic disease signatures and individual health trajectories from longitudinal health records and germline genetic data. By integrating these two data modalities, ALADYNOULLI provides a unified framework for understanding disease co-occurrence, predicting future disease events and discovering genetic architecture underlying complex phenotypes. This work addresses a critical gap in precision medicine40,41,42, in which the integration of diverse data sources remains challenging despite the promise of personalized approaches to disease management43. Unlike traditional disease-specific predictive models that require separate development for each condition, the unified framework of ALADYNOULLI simultaneously captures risk for multiple diseases, enabling information sharing across related conditions, improved prediction for diseases with sparse data and comprehensive decision support across clinical disciplines. ALADYNOULLI achieves this using only routinely collected diagnostic codes from standard clinical care in the EHR, without requiring the specialized laboratory values, biomarkers or questionnaire data on which established risk scores (PCE, PREVENT and Gail) depend. This implies that future work combining ALADYNOULLI with additional data sources can further improve its predictive ability in specific domains. Finally, our disease-level predictions provide superior clinical actionability and performance on direct head-to-head comparison and outperform other ICD-10 code-level approaches such as Delphi-2M (Extended Data Fig.9and Supplementary Note2; PheCode-to-ICD aggregation efficiency in Supplementary Fig.20).

Our model’s identification of consistent disease signatures across three independent cohorts supports their clinical relevance. These signatures capture cross-cohort–stable disease relationships and, in the cases that we directly validated (familial hypercholesterolaemia, clonal haematopoiesis and type 1 versus type 2 diabetes), align with established clinical phenotypes. The temporal dynamics of these signatures further enhance our understanding of how disease risk evolves throughout the life course, addressing the need to understand disease progression beyond static risk assessment44. ALADYNOULLI provides risks for 348 diseases simultaneously; patients remain at risk for remaining conditions after developing one, with hazards updating as signature loadings absorb new diagnoses (Supplementary Fig.21).

Genetic discovery through GWAS and RVAS represents a significant advance. The identification of genetic variants that associate more strongly with signature loadings than with individual diseases demonstrates that our approach can uncover pleiotropic mechanisms with weaker effects on individual diagnoses that are difficult to detect with traditional single-disease GWAS approaches and may flag candidate pleiotropic pathways for follow-up functional validation.

The time-varying signature loadings of ALADYNOULLI serve as patient descriptors that enable fundamentally new types of analyses and applications, including dynamic stratification of risk for diagnosis, clinical management, enhanced clinical trial design and hybrid clinical trials (Supplementary Note1). Unlike black-box models that provide only risk scores, the signature loadings of ALADYNOULLI enable patient matching based on shared biological mechanisms rather than disease labels. Patients with similar signature profiles, even if they have different diagnoses, may share underlying pathophysiological pathways and could benefit from similar interventions. This signature-based stratification addresses a critical limitation of traditional diagnostic categories, which often mask underlying biological heterogeneity.

These applications include signature-based patient stratification (matching, dynamic biological profiling and clinical trial design; Supplementary Note1), disease-level prediction that complements code-level approaches such as Delphi-2M (Extended Data Fig.9and Supplementary Note2) and contrast with transformer-based EHR foundation models (Supplementary Note3).

### Limitations

First, our model relies on EHR data, which may contain biases related to healthcare access, diagnostic coding practices and incomplete capture of disease history. These limitations are common to all EHR-based studies and highlight the importance of validating findings across multiple healthcare systems, as we have done here. However, a key methodological advantage of our framework is its ability to handle selection bias through inverse probability weighting: the separation of biological disease–signature relationships (ϕ) from population composition effects (λandπ) enables principled bias correction while preserving core biological patterns, a capability that distinguishes our approach from black box machine learning methods that cannot easily incorporate such corrections (Extended Data Fig.10). Second, although we incorporated genetic factors, we did not explicitly model environmental exposures or lifestyle factors that significantly influence disease risk44. Third, our use of established PRSs may miss genetic effects that act directly on signatures but weakly on individual diagnoses, as our signature-based GWAS identified loci not captured by traditional single-disease approaches. Fourth, our model makes several important assumptions including linearity in genetic effects and additivity in signature contributions, which may not capture all complex interactions. Fifth, our model uses age (time since birth) rather than calendar year as the temporal axis, which does not explicitly capture cohort effects (changes in disease prevalence over calendar time). Because UKB participants all enrolled during a narrow window (2006–2010), we are unable to explore cohort effects. Sixth, we treated first-recorded ICD code as a proxy for true diagnosis date. Documentation lag between true onset and EHR capture can be substantial—often several years for chronic conditions and especially acute in the UKB, where primary care linkage is incomplete—meaning that nominally ‘incident’ events in our data include some prevalent disease, biasing temporal signal detection towards later detection. Our prospective validation strategies are designed to minimize known sources of leakage (event year exclusions, washout windows and blinded follow-up), but no analysis of EHR data can fully eliminate the diagnostic date uncertainty inherent to coded clinical records. Seventh, although we have provided multiple lines of evidence for the statistical robustness of the discovered signatures (cross-cohort stability, heritability and GWAS concordance) and clinical coherence in specific cases (familial hypercholesterolaemia, clonal haematopoiesis and type 1 versus type 2 diabetes), mechanistic biological interpretation of each signature requires further functional validation that is beyond the scope of this work. Although calendar year was not explicitly modelled, age-stratified performance analyses across enrolment–age strata (Supplementary Table17and Supplementary Fig.22) provide assessment of robustness to cohort-specific patterns. Future work could integrate these additional data sources and relax these assumptions to further enhance predictive performance and biological insight, addressing the complex interplay between genetic and environmental factors that shape the risk of disease45.

Despite these limitations, ALADYNOULLI advances longitudinal health modelling for precision medicine40,41by jointly capturing time-varying disease patterns and genetic predisposition, enabling patient subgrouping within diagnostic categories and signature-level genetic discovery.

## Methods

### Model

We recapitulated the formulation of the model and provide a full account of model assumptions and implementation details.

### Mathematical formulation

The ALADYNOULLI model represents the probability of disease occurrence for patienti, diseased, at timetvia a mixture of probabilities as follows:

$${\pi }_{idt}=\kappa \cdot \mathop{\sum }\limits_{k=1}^{K}{\theta }_{ikt}\cdot {\rm{sigmoid}}({\phi }_{kdt}),$$

whereκis a global calibration parameter,θiktrepresents patienti’s time-varying association with signaturek, andϕkdtcaptures the relationship between signaturekand diseasedover time.

The patient–signature associationsθiktare parameterized as a softmax function of latent variablesλiktas:

$${\theta }_{ikt}=\frac{\exp ({\lambda }_{ikt})}{{\sum }_{{k}^{{\prime} }=1}^{K}\exp ({\lambda }_{i{k}^{{\prime} }t})}.$$

TheALADYNOULLImodel is specified hierarchically, via distributional assumptions on many of these components, which we refer to as priors.

Indicating byλikthe function of time describing the evolution of the latent variable over time for patientiand signaturek, we specify this as a Gaussian process:

$${{\boldsymbol{\lambda }}}_{ik} \sim {\mathcal{G}}{\mathcal{P}}({{\bf{r}}}_{k}+{{\boldsymbol{\Gamma }}}_{k}^{{\rm{\top }}}{{\bf{g}}}_{i},{{\Omega }}_{{\lambda }})$$

whererkis a signature-specific baseline,Γkcaptures how genetic and demographic factorsgiinfluence patient–signature associations, andΩλis a kernel function controlling temporal smoothness. The covariate matrixGcontains 36 PRSs plus sex and 10 genetic principal components (47 features total), providing genetic and demographic information for each individual. The kernel functionΩλis defined as:

$${\varOmega }_{\lambda }(t,{t}^{{\prime} })={\alpha }_{\lambda }^{2}\exp \left(-\frac{{(t-{t}^{{\prime} })}^{2}}{2{l}_{\lambda }^{2}}\right).$$

In our implementation, the amplitude parameterαλis set to 100 and the length-scale parameterlλis set toT/4. Similarly, the disease–signature association temporal functions follow a Gaussian process:

$${{\boldsymbol{\phi }}}_{kd} \sim {\mathcal{G}}{\mathcal{P}}({{\boldsymbol{\mu }}}_{d}+{\psi }_{kd},{\varOmega }_{{\phi }}),$$

whereμdis a disease-specific baseline derived from the logit of the population prevalence,ψkdrepresents the the time invariant component of the association between signaturekand diseased, andΩϕis a kernel function defined as:

$${\varOmega }_{\phi }(t,{t}^{{\prime} })={\alpha }_{\phi }^{2}\exp \left(-\frac{{(t-{t}^{{\prime} })}^{2}}{2{l}_{\phi }^{2}}\right),$$

where the amplitude is fixed toαϕ= 100 and the length scale is set tolϕ=T/3 in our implementation.

The genetic effect parametersΓkform a vector of lengthPrepresenting the effects ofPgenetic, sex and ancestral covariates on signaturek, and are assigned independent zero-mean Gaussian priors:

$${{\boldsymbol{\Gamma }}}_{k} \sim {\mathcal{N}}({\bf{0}},{\sigma }_{\gamma }^{2}{\bf{I}}),$$

where\({\sigma }_{\gamma }^{2}\)is the prior variance.

### Censored data and detailedEmatrix formation methodology

A critical aspect of ALADYNOULLI is its careful handling of censored observations, which is part of what allows it to function as a generative model of disease progression rather than a retrospective analysis tool. The likelihood function, defined below, incorporates time-to-event information through a standard survival analysis encoding of binary disease-specific event indicators inYand censoring times inE. ElementEidinErepresents, in summary, the minimum of the disease-specific event time and the maximum follow-up time for the patient, ensuring that the likelihood only includes timepoints at which the patient was actually observed. This formulation properly accounts for competing risks by using censoring times derived from actual data.

More specifically, the matrixEis defined through the following steps:

Step 1: identify maximum follow-up time for each patient. For each patienti, we determined their maximum follow-up age from ICD-10 data: max censori= max(last diagnosis datei, administrative censor datei). This represents the last timepoint at which patienticould have been observed, accounting for death, loss to follow-up, emigration or end of study period.

Step 2: convert to timepoint scale. We converted the maximum censoring age to the timepoint scale of the model: max timepointi= max censori− 30, where timepoint 0 corresponds to 30 years of age.

Step 3: cap event or censor times inEmatrix. For each patientiand diseased, theEmatrix entry is as follows:

* If diseasedis not observed in patienti, thenEid= max timepointi.
* If diseasedis observed in patienti, thenEidis the age of the diagnosis of diseasedfor patientiin years, minus 30.

Step 4: apply to prevalence calculation. When computing prevalence at each aget, we only included patients who are still at risk:

$${{\rm{prevalence}}}_{dt}=\frac{{\sum }_{i:{E}_{id}\ge t}{Y}_{idt}}{{\sum }_{i:{E}_{id}\ge t}1},$$

where the denominator includes only patients who have not yet been censored at timepointt. This ensures that prevalence estimates reflect realistic at-risk periods.

### Likelihood function

The likelihood is constructed to respect this censoring structure22,46. Consider first\({{\mathcal{L}}}_{NLL}\), the negative log of the likelihood, that is, the negative log of the probability of observed disease histories conditional on the disease probabilities (π):

$$\begin{array}{l}{{\mathcal{L}}}_{NLL}=-\mathop{\sum }\limits_{i=1}^{N}\mathop{\sum }\limits_{d=1}^{D}[\mathop{\underbrace{\mathop{\sum }\limits_{t=1}^{{E}_{id}-1}\log (1-{\pi }_{idt})}}\limits_{\text{Pre-event survival}}+\mathop{\underbrace{{Y}_{id{E}_{id}}\log ({\pi }_{id{E}_{id}})}}\limits_{\text{Event occurrence}}\\ \,+\mathop{\underbrace{(1-{Y}_{id{E}_{id}})\log (1-{\pi }_{id{E}_{id}})}}\limits_{\text{Censored observation}}].\end{array}$$

 (5)
 

The contribution of individualito this expression has three components:

1. (1)Pre-event survival (t<Eid): for all timepoints before the event or censoring time, we know that the individual did not have diseased, contributing log(1 −πidt) to the likelihood at each time.
2. (2)Event occurrence (t=Eid,\({Y}_{id{E}_{id}}=1\)): if diseasedoccurred at timeEid, we observed the event. The corresponding contribution is\(\log ({\pi }_{id{E}_{id}})\).
3. (3)Censored observation (t=Eid,\({Y}_{id{E}_{id}}=0\)): if the individual was censored without disease at timeEid, we only know they were disease free at that time, contributing\(\log (1-{\pi }_{id{E}_{id}})\).

### Objective function for maximum a posteriori computation

The computational derivation of the maximum a posteriori (MAP) estimate of the unknown parameters in the model proceeds by optimizing the function\({{\mathcal{L}}}_{total}\), which includes the negative log-likelihood\({{\mathcal{L}}}_{NLL}\)as well as terms arising from the Gaussian process prior.

The negative logs of the Gaussian process terms, as previously specified, are:

$${{\mathcal{L}}}_{GP{\boldsymbol{\lambda }}}=\mathop{\sum }\limits_{i=1}^{N}\mathop{\sum }\limits_{k=1}^{K}\frac{1}{2}{({{\boldsymbol{\lambda }}}_{ik}-{{\boldsymbol{\mu }}}_{ik})}^{{\rm{\top }}}{\varOmega }_{{\lambda }}^{-1}({{\boldsymbol{\lambda }}}_{ik}-{{\boldsymbol{\mu }}}_{ik});$$
$${{\mathcal{L}}}_{GP\phi }=\mathop{\sum }\limits_{k=1}^{K}\mathop{\sum }\limits_{d=1}^{D}\frac{1}{2}{({{\boldsymbol{\phi }}}_{kd}-{{\boldsymbol{\mu }}}_{d}-{\psi }_{kd})}^{{\rm{\top }}}{\varOmega }_{\phi }^{-1}({{\boldsymbol{\phi }}}_{kd}-{{\boldsymbol{\mu }}}_{d}-{\psi }_{kd}),$$

whereμik=rk+ΓkGi. Combining these terms, and assuming diffuse near-uniform priors onκandΓ, the negative log posterior (the ‘loss’ for short) is:

$${{\mathcal{L}}}_{NLL}+{{\mathcal{L}}}_{GP\lambda }+{{\mathcal{L}}}_{GP\phi }.$$

 (6)
 

### Training, validation and testing architecture

The genetic and performance results in this paper are based on training in the UKB dataset; we also trained the model in the MGB and AoU datasets to establish consistency as in Fig.2. Model fit for all three datasets, includingϕparameters, disease prevalenceμand primary time-fixed signature–disease associationsψk, is available in the exported parameters at the Zenodo deposit. Our analytical approach includes two complementary goals: (1) retrospective analysis for model training and cross-cohort validation; and (2) prospective analysis for prediction evaluation, as summarized in Extended Data Fig.1.

#### Retrospective analysis

For computational efficiency and uncertainty quantification, we divided each cohort into non-overlapping subsets: the UKB intoB= 40 subsets of approximately 10,000 individuals each (reserving each subset of 10,000 individuals in turn as a held-out test set), AoU into 30 subsets and the MGB into 4 subsets (reflecting the smaller dataset sizes). For each subsetbwithin each cohort, we jointly estimated the disease–signature associations (\({\widehat{\phi }}^{(b)}\)) and individual loadings (\({\widehat{\lambda }}^{(b)}\)) using all available observed data up to 81 years of age or censoring time, whichever came first. This retrospective approach utilized the complete disease trajectory for each individual, enabling us to characterize the full spectrum of disease signatures and their temporal dynamics. For initialization, each subset uses the same pre-computed initial clusters andψparameters, facilitating consistent signature interpretations across all subsets within each cohort.

For the UKB, the final disease–signature parameters used for explanatory analyses were computed as the average across the 40 training subsets (excluding the held-out test set):

$$\phi =\frac{1}{40}\mathop{\sum }\limits_{b=1}^{40}{\phi }^{(b)}.$$

This subset-averaging approach provides robust parameter estimates while maintaining computational tractability. In addition, it facilitates assessment of estimation robustness. The AoU and MGB cohorts serve as external validation datasets, demonstrating the replicability of disease signatures across different populations and healthcare systems. No prediction tasks were performed on these two cohorts.

This subset-averagedϕwas used to generate the disease signature visualizations in Fig.2, including the temporal patterns and cross-cohort consistency analyses. Individual trajectory analyses (Fig.3) utilized the subset-specificλ(b)estimates, and subsequent clustering of patients by their time-averaged signature loadings was performed within each disease category. The genetic analyses (Fig.4) were performed exclusively in the UKB, using the AUC of individual signature trajectories as quantitative phenotypes for GWAS.

#### Prospective analysis

For prediction evaluation (Fig.5), we implemented a strictly prospective framework using only UKB data with leave-one-out cross-validation to ensure robust, generalizable performance estimates. We used a subset of 400,000 individuals (the first 400,000 participant IDs, which are random, in 40 batches of 10,000 each) from the full UKB cohort of 427,239 individuals for computational efficiency in the cross-validation framework. For each of the 40 batches, we trained models on the remaining 39 batches to learn population-level parameters: disease–signature associations (ϕ), signature offsets (ψ), genetic effects (γ) and the global calibration parameter (κ). These parameters were then fixed, and predictions for the held-out batch of 10,000 individuals were generated by learning only individual-specific trajectories (\(\widehat{\lambda }\)) using only data available up to specific prediction timepoints.

This approach ensures no information leakage from the held-out batch. It also reflects the intended real-world clinical scenarios where population-level disease patterns are known from previous research, but individual risk trajectories must be estimated from available clinical history up to the prediction time. All prediction performance metrics reported in this paper are based on this leave-one-out cross-validation approach.

### Model initialization

To ensure computational feasibility and parameter stability, we initialized training as follows. We performed the spectral clustering of diagnoses described below and used it to derive starting values forψ. We did this once on the entire dataset to establish stable disease clusters and signature–disease associations. These initialψvalues were then reused in all subsequent subset analyses forb= 1,…, 40.

Spectral clustering was performed using Scikit on disease co-occurrence patterns. We computed a disease co-occurrence matrixCwhereCdd′represents the frequency with which diseasesdandd′ co-occur in the same patient. We applied spectral clustering to this matrix to identifyKdisease clusters.

We then initialized theψkdparameters based on cluster membership: for diseases in clusterk, we setψkd= 1.0 +ϵwhereϵis a small random noise. For diseases not in clusterk, we setψkd= −2.0 +ϵ. The choice of initialψwas initialized at values of 1 and −2, which on the log scale correspond to a 20-fold difference in odds (that is, 10−9versus 10−11), thereby spanning a broad range of plausible values for disease risk. For the time-varying parametersλiktandϕkdt, we initialized by drawing a single sample from the corresponding Gaussian process prior with reduced variance to preserve the structured mean initialization. Specifically, we initializedλiktvia a random draw from the Gaussian process prior with mean\({{\bf{r}}}_{k}+{{\boldsymbol{\Gamma }}}_{k}^{{\rm{\top }}}{{\bf{g}}}_{i}\)and covariance kernel scaled by amplitudeα= 0.1, whereΓkwas initialized using regression on disease occurrences. We initializedϕkdtvia a random draw from the Gaussian process prior with meanμd+ψkdand the same reduced amplitude, whereμdis derived from the logit of disease prevalence. The reduced amplitude ensures that random deviations do not bias the parameters arbitrarily away from the informative mean structure while maintaining temporal smoothness. We generated the Gaussian process samples via Cholesky decomposition of the scaled kernel matrices. This approach provides a structured and plausible initialization that reflects our prior smoothness assumptions. The number of latent signaturesKwas chosen to provide a parsimonious balance between model complexity and interpretability, based on previous experience and exploratory analysis.

### Optimization details

We trained the model using gradient descent to minimize the loss (equation (6)). The solution can be interpreted as approximating a MAP estimate of the parameters, assuming dispersed priors onλ,Γ,μ,ψandϕ. We minimized the loss (equation (6)) over a fixed maximum number of epochs (that is, complete passes through the entire training dataset). At each epoch, we computed gradients via backpropagation and updated parameters using the Adam optimizer in PyTorch, a deep learning framework that allows efficient computation of gradients through automatic differentiation. The model was trained using a learning rate of 0.01. The model was optimized at a timescale of 1 year and thus trained to provide the most accurate 1-year risk predictions. Longer-term risk (for example, 10 years) can also be derived by simple manipulations of the estimatedπ.

For computational efficiency, we used the Cholesky decomposition to compute the Gaussian process contributions and to sample from the Gaussian process prior during initialization. We also used a jitter term of 1−6to ensure numerical stability when computing the inverse of the kernel matrices. In practice, for our subsets of 10,000 individuals, the model converged after 200 epochs. For inference on new patients, the vectorized implementation enabled rapid risk prediction: generating predictions for a single individual requires approximately 0.05 s (or 8 min for 10,000 individuals), making the model suitable for real-time clinical decision support.

### Computation of probabilities of future events

To ensure that our model provides prospective predictions without data leakage, we implemented a strict censoring strategy that distinguishes between cohort recruitment and prediction time. This approach allowed us to simulate real-world clinical scenarios where predictions are made based only on information available at a specific point in time (see Supplementary Fig.1).

Cohort enrolment time refers to the timepoint when an individual enters ALADYNOULLI, which for our purposes is 30 years of age. For example, in our UKB analysis, all individuals were followed in the EHR from 1980 forwards15,47and thus assigned an enrolment time in our study at young adulthood, 30 years of age, or whichever comes later.

Cohort recruitment time refers to the time when individuals joined the biobank. The UKB recruited individuals between 40 and 69 years of age in the time frame from 2006 to 2010 (ref.3).

Prediction time refers to the time when we imagine making a clinical prediction, with knowledge of the health history up until that time.

For prediction time for benchmarking with existing clinical risk scores, in practice, when comparing to existing clinical scores, this coincides with recruitment time as above.

In the UKB, an individual was observed in the EHR from adulthood and contributed data to our analysis from 30 years of age until the end of follow-up. However, for prediction analyses, we only made predictions at timepoints after the cohort recruitment time.

### Simulation study

To validate the ability of the ALADYNOULLI model to recover latent disease clusters and temporal dynamics, we conducted a simulation study using ALADYNOULLI itself as the generative model. This approach allowed us to test whether the model can accurately recover known ground-truth parameters from synthetic data that follow the exact same probabilistic structure as our proposed model (Supplementary Fig.23).

We generated synthetic data withN= 10,000 individuals,D= 20 diseases,T= 50 timepoints (30–79 years of age),K= 5 latent disease signatures andP= 5 genetic covariates. The data generation process followed the exact mathematical formulation of ALADYNOULLI. We first createdK= 5 distinct disease clusters with 4 diseases per cluster, assigning strong positive associations within clusters (ψkd= 1.0) and strong negative associations outside clusters (ψkd= −2.0). Disease baseline trajectories (μd) were generated on the logit scale with diverse prevalence patterns ranging from rare (logit prevalence ≈ −14) to common (logit prevalence ≈ −8), incorporating realistic age-dependent onset patterns with varying peak ages and slopes.

For individual trajectories, we generated genetic covariates\({\bf{G}}\in {{\mathbb{R}}}^{N\times P}\)and genetic effect matrices\(\Gamma \in {{\mathbb{R}}}^{P\times K}\), then sampled individual signature loadingsλiktfrom Gaussian processes with means\({{\bf{g}}}_{i}^{{\rm{\top }}}{{\boldsymbol{\Gamma }}}_{k}\)and temporal covariance with length scaleT/4 = 12.5 years. Disease–signature associationsϕkdtwere sampled from Gaussian processes with meansμd+ψkdand temporal covariance with length scaleT/3 ≈ 16.7 years. Event probabilities were computed using the exact ALADYNOULLI formula:\({\pi }_{idt}={\sum }_{k=1}^{K}{\rm{softmax}}({\lambda }_{ikt})\cdot {\rm{sigmoid}}({\phi }_{kdt})\), and disease events were sampled from these time-varying probabilities.

When we applied ALADYNOULLI to these synthetic data, the model successfully recovered the composition of the signatures (adjusted Rand index = 0.843, normalized mutual information = 0.943), and accurately reconstructed the temporal trajectories and genetic effects.

### Ethics statement

This study analysed coded or de-identified human research data from three biobanks under institutional review board (IRB) approvals at MGB. All research was performed in accordance with the relevant guidelines and regulations of each contributing biobank and the MGB Human Research Committee.

Analyses of MGB data were performed under MGB IRB protocol 2018P001236 (‘Cardiometabolic disease risk prediction and healthcare utilization using electronic health record-derived data and genomics’), which is active and approved for data analysis. All MGB participants provided written or electronic informed consent for research use of their biospecimens and EHR data before enrolment.

Analyses of UKB data were performed under MGB IRB protocol 2021P002228 (‘Analyses of cardiovascular diseases and related disorders using data from UK Biobank participants’), determined exempt by the MGB IRB. The UKB received ethical approval from the North West Multi-Centre Research Ethics Committee (REC reference 11/NW/0382), and all UKB participants provided informed consent at recruitment. This work was conducted under UKB application number 7089.

Analyses of AoU data were performed under MGB IRB protocol 2020P001737 (‘Data Analysis for All of Us Research Program’), determined by the MGB IRB to constitute analysis of de-identified data not meeting the definition of human participant research. The AoU obtained ethical oversight via its central IRB at the Vanderbilt University Medical Center Data and Research Center, and all AoU participants provided informed consent at enrolment.

No identifiable patient images, individually identifying records or new prospective biospecimen collections were generated by this study; all analyses were performed on coded or de-identified longitudinal data already collected by the three contributing biobanks under the consent procedures described above.

### Cohorts

Data are drawn from three distinct biobanks: MGB, UKB and AoU. Each cohort is described in Supplementary Table2and below (Supplementary Fig.2).

### MGB

MGB is an integrated research initiative based in Boston, Massachusetts4. It collects biological samples and health data from consenting individuals at Massachusetts General Hospital, Brigham and Women’s Hospital and local healthcare sites within the MGB network. Since 1 July 2010, the MGB has enrolled more than 140,000 participants and extracted DNA from approximately 90,000 participants’ samples and 53,306 participants were genotyped by Illumina Global Screening Array (Illumina). All participants provided their informed written or electronic consent. EHR data are available on all participants from approximately 1990 (see Supplementary Fig.2). We used a subset of 48,069 for whom EHR and genetic data were available. The cohort inclusion criteria: all individuals with available EHR and genetic data were included; no restrictions were placed on the number of visits or age at enrolment, as the model accommodates variable follow-up times through its censoring framework.

### UKB

The UKB is a large-scale, population-based cohort that recruited over 500,000 participants 40–69 years of age between 2006 and 2010 from across the UK3,48. The cohort includes extensive phenotypic data, biological samples and longitudinal follow-up of health outcomes. Genotyping was performed using the UK BiLEVE array or the UKB Axiom array, with subsequent imputation to the Haplotype Reference Consortium and UK10K reference panels. Participants were genotyped to investigate genetic contributions to various health and disease traits, with particular attention to the relationship between genetic variants and cardiometabolic diseases. Electronic health records are available, with the earliest diagnostic records extending back to 1980 (ref.49), providing diagnostic history well before the 2006–2010 recruitment window. We used the subset of 427,239 for whom genomic and EHR data were available. PRSs were obtained from an external set of controls28.

### AoU

The AoU research programme50is a large-scale cohort study designed to increase the representation of historically understudied populations in biomedical research. Since 2018, AoU enrolled adults (18 years of age or older) at more than 730 US sites. Of the more than 800,000 consented participants, more than 560,000 have completed core enrolment requirements, including health questionnaires and biospecimen collection. Data from these participants are continuously linked to EHRs, which capture ICD-9 or ICD-10, SNOMED (Systematized Nomenclature of Medicine and Clinical Terms) and CPT (Current Procedural Terminology) codes. Genetic data include array-based genotyping from 315,000 participants and whole-genome sequencing from 245,394 participants who were then available to contribute PRSs for downstream analyses.

### Preprocessing and disease encoding

Following the approach of Jiang et al.16, we initially analysed 348 PheCode diseases from the UKB that were selected based on prevalence thresholds (1,000 or more occurrences) to ensure sufficient statistical power for comorbidity analysis. This threshold was chosen to balance disease coverage with statistical power: diseases with fewer than 1,000 occurrences would have insufficient power for reliable signature assignment. We focused on ICD-10 chapters A–N (disease chapters), excluding injury (S and T), poisoning, external causes of morbidity and mortality (V–Y), factors influencing health status (Z) and codes for special purposes (U). Disease records were mapped from ICD-10 or ICD-10CM codes to PheCodes using a standardized three-step procedure: (1) direct ICD-10-to-PheCode mapping using established PheCode definitions24, (2) aggregation of related ICD codes to single PheCode categories, and (3) validation of mapping consistency across cohorts. To validate our findings across independent populations, we then applied the same disease selection strategy to AoU and MGB cohorts using their respective ICD coding systems. In AoU, we extracted ICD-9 and ICD-10 codes directly from the OMOP Common Data Model condition occurrence tables50, successfully reproducing all 348 diseases from the UKB selection. In the MGB, we similarly used ICD-9 and ICD-10 codes, reproducing 346 of the 348 diseases for validation analyses. This multi-cohort approach enabled us to assess the generalizability of disease signatures across different healthcare systems and populations while maintaining consistency in the underlying disease definitions used for ALADYNOULLI model development and validation.

### Analysis

#### Stability across subsets and cohorts

We empirically verified thatϕestimates were highly stable across subsets. To assess robustness to natural variation in sample composition, we computed standard errors ofϕparameters across all 40 training batches. Each batch represents 10,000 individuals with slight variation in composition across batches. For eachϕparameter (signature–disease–time combination), we calculated the standard error of the mean as the standard deviation across batches divided by\(\sqrt{40}\). We observed small standard errors (mean s.e. = 0.0010, median s.e. = 0.0002, 95% of s.e. values ≤ 0.004), demonstrating the robustness of our disease–signature associations to batch-to-batch variation in sample composition (Supplementary Fig.6).

To further assess the replicability of our disease signatures across different populations (shown in Fig.2c), we performed cluster correspondence as follows (Fig2d). We examined the correspondence between disease clusters identified in each biobank by creating normalized confusion matrices. For each pair of biobanks (UKB versus MGB and UKB versus AoU), we identified the set of diseases common to both biobanks, mapped each disease to its assigned cluster in each biobank based on posterior fitting (disease-to-signature assignments determined by the signature with maximum posterior association strength, argmaxk(ψkd)), created a cross-tabulation matrix showing the proportion of diseases in each UKB cluster that was assigned to each MGB or AoU cluster, and normalized the counts by row to show the distribution of cluster assignments.

We computed a composition preservation probability index to quantify cross-cohort correspondence. For each UKB clusterk, we identified its best-matching cluster in the comparison cohort (the cluster receiving the highest proportion of diseases from that UKB cluster). The composition preservation probability for clusterkis defined as:

$${J}_{k}=\frac{| {D}_{k,{\rm{UKB}}}\cap {D}_{{k}^{* },{\rm{other}}}| }{| {D}_{k,{\rm{UKB}}}| }$$

whereDk,UKBis the set of diseases in UKB clusterk(determined by posteriorψvalues, argmaxk(ψkd)),\({D}_{{k}^{* },{\rm{other}}}\)is the set of diseases in the best-matching clusterk*in the comparison cohort (also determined by posteriorψvalues) and ∣⋅∣ denotes set cardinality. This metric represents the proportion of diseases in a UKB signature that also belong to its best-matching signature in the comparison cohort (that is, the intersection size divided by the UKB signature size, rather than the traditional Jaccard intersection over union). The overall cross-cohort similarity is the median of these cluster-specific similarities:J= median(J1,J2,…,JK) across all UKB clusters. This metric ranges from 0 (no correspondence) to 1 (perfect correspondence), where higher values indicate stronger replicability of disease clustering patterns across populations.

This analysis revealed strong correspondence between clusters across biobanks (median composition preservation probability = 0.80), particularly for cardiovascular and malignancy signatures, suggesting robust biological patterns that transcend population differences.

For temporal pattern analysis, we performed a detailed comparison of the temporal patterns (ϕtrajectories) for diseases shared across all three biobanks, focusing on two key signatures: the cardiovascular signature (signature 5 in the MGB, signature 16 in AoU and signature 5 in the UKB) and the malignancy signature (signature 11 in the MGB, signature 11 in the AoU and signature 6 in the UKB). For each signature, we identified diseases assigned to that signature in all three biobanks, plotted the temporal patterns (ϕvalues) for each shared disease, overlaid the average pattern across all three biobanks (grey dashed line in Fig.2) and used consistent colours for each disease across biobanks to facilitate comparison. This analysis demonstrated consistency in the temporal patterns of disease risk across different populations, with shared diseases showing similar risk trajectories despite being modelled separately in each biobank.

### Individual patient trajectory visualization

To illustrate the complex interplay between disease signatures in individual patients (shown in Fig.2a), we analysed detailed trajectories for patients with multiple conditions.

For each selected patient, we created a three-panel visualization showing temporal signature loadings, a disease timeline with diagnosis timing and disease specific probabilities, and then contrasted with the time-averaged signature contributions.

### Disease-specific trajectory and heterogeneity analysis

To systematically quantify differences in signature composition among patients with the same clinical diagnosis and understand disease progression heterogeneity and associated genetic architectures (Figs.3fand4b–d), we performed trajectory clustering analysis using the ALADYNOULLI model. For each disease of interest (for example, breast cancer, major depressive disorder and myocardial infarction), we implemented the following analysis pipeline.

#### Patient selection and temporal averaging

For each disease, we identified all patients who developed the condition and computed their time-averaged normalized signature loadings:

$${\bar{\theta }}_{ik}=\frac{1}{{T}_{i}}\mathop{\sum }\limits_{t=1}^{{T}_{i}}{\theta }_{ikt}$$

whereθiktis the signature loading for individuali, signaturekand timet.

#### Patient clustering

We appliedk-means clustering (k= 3) to the time-averaged signature loading matrix\({\bar{\theta }}_{ik}\)to identify illustrative distinct patient subgroups within each disease category.

#### Trajectory visualization

We computed cluster-specific mean trajectories across individuals within the cluster\({\mu }_{ckt}=\frac{1}{|{C}_{c}|}{\sum }_{i\in {C}_{c}}{\theta }_{ikt}\)and visualized deviations from population reference as filled line plots for each timepoint:Δckt=μckt− refkt, where refktrepresents the population-average signature loading.

#### Genetic architecture analysis

For each cluster, we computed mean PRSs across individuals in the cluster, and created heatmaps showing cluster-specific values of these scores. To quantify variability of PRSs among individuals with the same disease, we calculated Cohen’sdeffect sizes for each PRS comparing in-cluster versus out-of-cluster distributions:

$$d=\frac{{\bar{X}}_{{\rm{in}}}-{\bar{X}}_{{\rm{out}}}}{{s}_{{\rm{pooled}}}}$$

where\({\bar{X}}_{{\rm{in}}}\)and\({\bar{X}}_{{\rm{out}}}\)are the mean PRS values for patients within and outside each cluster, respectively, andspooledis the pooled standard deviation. Cohen’sdvalues of 0.2, 0.5 and 0.8 correspond to small, medium and large effect sizes, respectively, providing a standardized measure of genetic differentiation between patient subgroups.

For clustercand signaturek,\({C}_{ck}^{{\rm{SIG}}}\)is the standardized difference in mean time-averaged signature loadings between individuals in clustercand those in all other clusters. This measures how distinct each cluster is with regard to each disease signature. Similarly, for clustercand PRSp,\({C}_{cp}^{{\rm{PRS}}}\)is the standardized difference in mean PRS values between individuals in clustercand those in all other clusters.

Statistical significance of cluster-level Cohen’sdwas assessed by two-sided Welch’st-tests comparing in-cluster versus out-of-cluster individuals on the corresponding time-averaged signature loadings (\({C}_{ck}^{{\rm{SIG}}}\)) or PRS values (\({C}_{cp}^{{\rm{PRS}}}\)). Equivalently,\(t=d\sqrt{{n}_{{\rm{in}}}{n}_{{\rm{out}}}/({n}_{{\rm{in}}}+{n}_{{\rm{out}}})}\)with df =nin+nout− 2. ReportedPvalues use Bonferroni correction across the 21 signatures × 3 clusters tested per disease (\({C}_{ck}^{{\rm{SIG}}}\)) and across the PRS panel × 3 clusters tested per disease (\({C}_{cp}^{{\rm{PRS}}}\)).

### Deviation pathway heterogeneity analysis for myocardial infarction

As a supplementary analysis, to identify illustrative biological pathways to myocardial infarction using deviation-from-reference clustering, we performed the following supplementary analysis. For each individual with a myocardial infarction diagnosis, we extracted signature loadings (θik(t)) over the 10-year window preceding the myocardial infarction event. We computed signature deviations by subtracting the population reference trajectory for each signature:\({\delta }_{ikt}={\theta }_{ikt}-{\bar{\theta }}_{kt}\), where\({\bar{\theta }}_{kt}\)is the population mean signature loading at aget. This deviation-based approach removes age-related confounding and focuses on disease-specific patterns relative to expected population trajectories. For each patient, we computed a 105-dimensional feature vector (21 signatures × 5 timepoints) representing mean signature deviations across the 10-year pre-myocardial infarction window. Patients were clustered into pathways usingk-means clustering (k= 4) on these deviation vectors. Pathway assignment was validated through: (1) cross-cohort replication in the MGB using identical clustering procedures, (2) comparison of precursor disease prevalence patterns across pathways, and (3) signature trajectory visualization to confirm coherence with established clinical patterns. Cross-cohort validation was performed by applying the UKB cluster centroids to the MGB cohort and comparing pathway sizes and disease enrichment patterns.

### Genetic analysis of signature trajectories

For each individuali, we computed the temporal signature loadingsθik(t) for each signaturekand timepointtusing the softmax transformation:

$${\theta }_{ikt}=\frac{\exp ({\lambda }_{ikt})}{{\sum }_{{k}^{{\prime} }}\exp ({\lambda }_{i{k}^{{\prime} }t})}$$

whereλik(t) is the latent score for individuali, signaturekand timet. The softmax was computed across the signature dimension for each individual and timepoint. To summarize the overall exposure each individual to a given signature, we integrated the signature trajectory over time:

$${{\rm{AEX}}}_{ik}=\int {\theta }_{ikt}\,dt\approx \mathop{\sum }\limits_{t=1}^{T-1}\frac{{\theta }_{ikt}+{\theta }_{ik(t+1)}}{2}$$

whereTis the total number of timepoints. The resulting average signature exposure over time (AEX) for each signature was used as a quantitative phenotype for downstream genetic association analysis (Extended Data Fig.6).

We performed GWAS using the AEX values as quantitative phenotypes. For each signaturek, we tested for association between the AEX phenotype and genome-wide SNP genotypes. Association testing was performed using the REGENIE51software (described below), which implements a two-step ridge regression approach for computational efficiency and control of population structure.

#### Genetic ancestry handling

All GWAS analyses included individuals of all genetic ancestries (not restricted to European ancestry), with population structure controlled through inclusion of the first 20 principal components of genetic ancestry as covariates. This approach allowed us to leverage the full diversity of the UKB while properly accounting for population stratification. The following covariates were included in all association models: sex, age at recruitment and the first 20 principal components of genetic ancestry3.

### GWAS details

We performed GWAS using REGENIE51, a two-step ridge regression approach designed for computational efficiency and robust control of population structure in large biobank-scale datasets.

Step 1: whole-genome ridge regression. We fit a whole-genome ridge regression model using all genetic variants to account for polygenic effects, relatedness and population structure. The model was fit using leave-one-chromosome-out cross-validation, where predictions for each chromosome exclude variants from that chromosome to prevent overfitting. This step produces polygenic predictions that capture the aggregate genetic background.

Step 2: single-variant association testing. We performed single-variant association tests on the residuals from step 1, testing each of 6,418,439 imputed variants (MAF ≥ 0.01, INFO ≥ 0.7) individually. By testing variants on pre-adjusted residuals rather than on raw phenotypes, this approach provides well-calibrated association statistics that are robust to case–control imbalance, relatedness and population stratification. All models included covariates for sex, age at recruitment and the first 20 principal components of genetic ancestry. Genome-wide significance was set atP< 5 × 10−8. We identified nearby genes using both nearest gene and gene body analyses (Ensembl and GnomaAD).

In addition to our main analysis featured in Fig.4, for each signature, we identified genome-wide significant SNPs (for example,P< 5 × 10−8) and further analyse their relationships with individual disease phenotypes and nearby genes. The analysis proceeds as follows. First, we extracted the lead SNPs from the GWAS summary statistics for each signature. For our supplementary analyses (Supplementary Fig.13), for each top SNP, we tested its association with a panel of binary constituent disease phenotypes, which comprise our signature inputs using logistic regression, controlling for sex and the first 20 principal components. Third, we visualized the matrix of SNP–phenotype association strength (−log10(P)) using heatmaps, marking associations significant atP< 5 × 10−8. This enabled identification of signature-specific loci: SNPs associated with the signature but not with any individual constituent disease. Fourth, we used UpSet plots to visualize the overlap of significant variants across signatures and individual diseases.

### LDSC heritability analysis

Heritability estimates (h2) represent the proportion of phenotypic variance in signature trajectories that can be attributed to additive genetic variation. Because our signature phenotypes are continuous (integrated area under the signature loading curve), all heritability estimates are on the observed scale, that is, there is no liability-scale transformation for continuous traits.

Heritability estimates for signature trajectories were calculated using linkage disequilibrium score regression (LDSC)30on the GWAS summary statistics generated from REGENIE. For each signature, we applied LDSC with standard parameters using the European ancestry linkage disequilibrium reference panel (baseline LD v2.2), following standard practice for heritability estimation from GWAS summary statistics. The LDSC intercept was used to assess potential residual confounding and genomic inflation. For comparison with component diseases, we also performed GWAS for individual cardiovascular traits (myocardial infarction, coronary artery disease, angina pectoris, hypercholesterolaemia, coronary atherosclerosis, acute ischaemic heart disease, chronic ischaemic heart disease and unstable angina) using the same REGENIE workflow and covariates (sex, age at recruitment and first 20 genetic principal components), then computed LDSC heritability estimates for each trait. For valid comparison, we have reported observed-scale heritability for binary traits; liability-scale estimates are provided separately for reference against literature values that typically report on that scale (Supplementary Table5).

### RVAS

Gene-based RVAS were performed using REGENIE51gene-based association tests. For each signature, we tested associations between signature AEX values and aggregated rare variant burden within genes across six variant filtering masks (Mask1–Mask6), representing progressively inclusive functional impact categories (Mask1: most restrictive, Mask6: most inclusive). Each mask was further stratified by MAF thresholds (singleton, 1 × 10−5, 0.0001, 0.001, 0.01 and 0.1). Variants were annotated using Ensembl Variant Effect Predictor and aggregated at the gene level as well as Encode using nearest gene. The gene-based test statistic aggregates variant-level association signals within each gene, accounting for linkage disequilibrium and variant effect sizes. Genome-wide significance was set atP< 2.5 × 10−6after Bonferroni correction for the number of genes tested per signature (18,464 genes); all reported significant gene–signature pairs additionally satisfy the joint Bonferroni thresholdP< 0.05/(18,464 × 21) ≈ 1.3 × 10−7controlling for the 21 signatures considered. Significant genes were identified across all masks to ensure robustness to variant filtering criteria, with genes discovered in multiple masks considered high-confidence associations.

### Three-way validation of rare variant associations

To validate rare variant associations through an independent pathway, we examined the three-way consistency between (1) signature–gene associations from RVAS, (2) gene–disease correlations from rare variant burden analysis, and (3) disease–signature loadings from theϕparameters. For each signature–gene pair identified through RVAS, we computed rare variant burden scores for each individual by summing variant counts (burden = ∑(2 −X), whereXis the genotype matrix with PLINK encoding. We then calculated Pearson correlations between rare variant burden and binary disease outcomes across all diseases. Finally, we tested whether diseases with high rare variant burden correlations also showed high signature–disease loadings (ϕvalues) by computing the correlation between the vector of gene–disease correlations and the vector of disease–signature loadings. This three-way validation provides biological plausibility by demonstrating that: (1) rare variant carriers show disease enrichment consistent with signature associations, and (2) signature–disease loadings reflect the same underlying biology captured by rare variant–disease associations.

### Clinical validation: familial hypercholesterolaemia and clonal haematopoiesis

To validate signature concordance with established disease biology, we performed targeted analyses of two well-characterized genetic conditions with known disease associations. For familial hypercholesterolaemia, we identified carriers of familial hypercholesterolaemia using genetic variants inLDLR,APOBandPCSK9following an established criteria52,53,54. For carriers of familial hypercholesterolaemia and matched controls, we computed signature loadings and tested for enrichment of signature 5 (cardiovascular signature) in the 5-year window preceding the first ASCVD event (myocardial infarction, coronary artery disease or stroke). For each patient with an ASCVD event, we computed the pre-event change in signature 5 loading (ΔSig5) over the 5-year window preceding the event, defined as the difference between signature loading at 1 year before the event and at 5 years before the event. We then classified patients as showing a ‘pre-event rise’ ifΔSig5 ≥ 0. Enrichment was quantified by comparing the proportion of carriers of familial hypercholesterolaemia versus non-carriers who showed a pre-event rise using Fisher’s exact test on a 2 × 2 contingency table (rise/no-rise × carrier/non-carrier), two-sided alternative. Results were reported as odds ratios withPvalues from Fisher’s exact test.

### Model evaluation and comparison

Figure5presents a comprehensive evaluation of our multi-disease risk prediction model in the UKB, and comparisons with important single-disease models. Each was evaluated in a strictly prospective framework that minimizes known sources of information leakage. In the testing data, all individual-level parameters were estimated using only information available up to the time of prediction. Individuals with prevalent disease at prediction were excluded from the risk set for that disease. In the UKB, all individuals were followed for at least 10 years from recruitment. We considered the following prediction tasks and metrics.

#### Median AUC ALADYNOULLI dynamic

This metric evaluates the ability of the model to make dynamic predictions at multiple timepoints during follow-up: it is derived by refitting the ALADYNOULLI model using fixed\(\widehat{\phi }\),\(\widehat{\gamma }\)andκparameters, previously estimated from the full history training data, and now applied to a series of 1-year prediction tasks. Critically, although the fixed parameters above were estimated from the full training data, the\(\widehat{\lambda }\)for each prediction task were estimated using data only up to the point of prediction. For each of the first 10 years after recruitment, the model was retrained using only data available up to that point for the held-out test set (in orange in Extended Data Fig.1). The median AUC across these ten dynamic 1-year fits is reported. This captures how predictive accuracy evolves as patients accumulate new diagnoses and leverages the flexibility of our method to perform dynamic, prospective risk estimation at any timepoint. Individuals with prevalent disease at prediction time were excluded from the risk set.

#### ALADYNOULLI recruitment (1 year)

This metric uses the ALADYNOULLI model’s predicted 1-year risk at the time of recruitment, evaluated against observed 1-year outcomes. The risk estimate is\({\widetilde{\pi }}_{idt}\), the predicted 1-year risk for individualirecruited at timetfor diseased. In practice, any age of prediction could be chosen, but we used the age of recruitment to the UKB because it is the only time at which we have the availability of additional clinical variables required for comparability with existing clinical benchmarks.

#### ALADYNOULLI recruitment (10 years)

This metric uses the ALADYNOULLI model’s predicted 1-year risk at the time of recruitment, evaluated against observed 10-year outcomes. The risk estimate is\({\widetilde{\pi }}_{idt}\), as in the 1-year predictions.

#### Cox

For benchmarking purposes, we used a baseline Cox model using only family history and sex as covariates, with age as the timescale delineating start and stop of the interval, representing a minimal clinical model that does not require any model curation or disease-specific features. This highlights the fact that our approach does not rely on disease-specific risk factors or manual feature engineering.

When benchmarking AUC performance, we compared the ALADYNOULLI model not only to the benchmarking Cox proportional hazards model above but also to established clinical risk scores: PREVENT55, PCE56for ASCVD and Gail39for breast cancer, models for diseases for which these scores are available after specific and often expensive curation. Of note, these clinical risk scores require laboratory values and biomarkers that are either collected during targeted clinical visits (introducing selection bias) or, when extracted from routine EHR data, may be subject to measurement bias as patients who are sicker typically receive more frequent testing. By contrast, our approach leverages routinely collected diagnostic codes (ICD codes) that are systematically recorded for all patients regardless of disease severity, providing a more unbiased data source for risk prediction.

This approach ensured that all model comparisons were fair, prospective and reflective of the information available at the time of risk assessment.

#### Dynamic 10-year rolling

This approach demonstrates the interpolation capabilities of the model by evaluating how probability estimates evolve as new information becomes available. For each year of the 10-year horizon, we updated the predictions of the model using information available up to that timepoint, then aggregated the cumulative 10-year risk as\(1-{\prod }_{t=1}^{10}(1-{\widehat{\pi }}_{idt})\), where\({\widehat{\pi }}_{idt}\)is the predicted risk for individualiand diseasedat yeartafter recruitment. Although this rolling evaluation does not use knowledge of the future outcome of interest, it cannot be considered fully prospective. This is because it incorporates concurrent information about events that are potentially correlated with, or even resulting from, the event of interest, as the probability estimates of the model at yeartare influenced by information available up to yeart. Thus, it is best understood as interpolation rather than extrapolation. Although this metric cannot be used for prospective evaluation, it demonstrates the technical capabilities of the model for dynamic risk assessment and shows how probability estimates evolve over time.

#### Additional methodological challenges

We conducted a series of analyses to assess the robustness of ALADYNOULLI to selection bias, population stratification, temporal leakage and reverse causation, complementing the primary analyses described in the main text. We provide technical details next.

Three key methodological features were included: (1) inverse probability weighting (IPW) to correct for UKB participation bias while preserving biological signal; (2) comprehensive washout analyses (1–6 months and 1–-2 years) to assess temporal leakage and reverse causation; and (3) patient-specific censoring using realistic follow-up times to properly handle competing risks. These strengthen the validity and generalizability of our findings.

#### Selection bias and IPW

To evaluate robustness to participation bias in the UKB, we implemented IPW following Schoeler et al.38. We fit a lasso-regularized logistic regression model for biobank participation using demographic and socioeconomic variables (region, birth year, sex, household characteristics, employment status, housing tenure, ethnicity, self-reported health and education) and computed the predicted participation probability\({\widehat{p}}_{i}\)for each individual.

IPWs were defined as

$${w}_{i}^{* }=\frac{0.0434}{{\widehat{p}}_{i}},$$

where 4.34% is the estimated participation rate in the source population, with\({w}_{i}^{* }\)trimmed at the 1st and 99th percentiles to avoid undue influence of extreme weights. These raw weights were then normalized to sum toN:

$${w}_{i}={w}_{i}^{* }\cdot \frac{N}{{\sum }_{j=1}^{N}{w}_{j}^{* }},$$

ensuring that the weighted sample size equals the observed sample size for proper loss scaling.

The weighted loss function modifies the data likelihood component of equation (6) to incorporate individual weights. The weighted negative log-likelihood is:

$$\begin{array}{l}{{\mathcal{L}}}_{\,\mathrm{NLL}}^{\mathrm{weighted}}=-\frac{1}{N}{\sum }_{i=1}^{N}{w}_{i}\left[{\sum }_{d=1}^{D}{\sum }_{t=1}^{{E}_{id}-1}\log (1-{\pi }_{idt})\right.\\ \left.\,\,\,\,\,+{Y}_{id{E}_{id}}\,\log ({\pi }_{id{E}_{id}})+(1-{Y}_{id{E}_{id}})\,\log (1-{\pi }_{id{E}_{id}})\right]\end{array}$$

 (7)
 

wherewiis the normalized IPW weight for individuali. The Gaussian process prior terms (\({{\mathcal{L}}}_{{\rm{GP}}\lambda }\)and\({{\mathcal{L}}}_{{\rm{GP}}\phi }\)) remain unweighted, as they represent priors on model parameters rather than data contributions.

$${{\mathcal{L}}}_{\,{\rm{total}}}^{{\rm{weighted}}}={{\mathcal{L}}}_{\,{\rm{NLL}}}^{{\rm{weighted}}}+{{\mathcal{L}}}_{{\rm{GP}}\lambda }+{{\mathcal{L}}}_{{\rm{GP}}\phi }.$$

 (8)
 

This formulation ensures that individuals with lower predicted participation probabilities (underrepresented groups) contribute proportionally more to parameter estimation, effectively rebalancing the training data towards the source population distribution.

#### Population stratification and genetic ancestry

To assess the effect of population structure on signatures, we performed both principal component-adjusted and ancestry-stratified analyses. First, we compared models fit with versus without genetic principal components in the Gaussian process mean forλ(equation (3)), holding all other settings fixed. Disease–signature associations (ϕ) were nearly identical between models (correlation = 1.000, mean absolute difference < 0.002), demonstrating that disease–signature relationships are robust to principal component adjustment. By contrast, individual signature loadings (θ) showed ancestry-specific shifts, with cardiovascular signature 5 exhibiting the largest deviation for South Asian (SAS) individuals, consistent with known elevated cardiovascular risk in this group. Second, we performed principal component analysis on time-averaged signature loadings and examined clustering by ancestry (European (EUR), African (AFR), East Asian (EAS) and SAS), finding substantial overlap between groups with modest deviations along principal components for AFR, EAS and SAS. Finally, we compared ALADYNOULLI predictions to Cox baseline models including age, sex and genetic principal components, confirming that ALADYNOULLI retains a performance advantage across ancestry groups, indicating that its gains are not explained by ancestry covariates alone.

#### Reverse causation assessment: short-term washout

To test whether predictions are driven by diagnostic cascades immediately preceding events, we excluded events occurring within 1, 3 and 6 months of enrolment. Performance remained robust with minimal AUC degradation (mean drop = 0.0112 for 1-year predictions and 0.0010 for 10-year predictions), indicating that ALADYNOULLI captures predictive signal rather than reverse causation effects.

#### Temporal leakage assessment: multi-year washout

To address temporal misalignment between ICD-10 dates and true disease onset, we conducted two complementary analyses. First, we compared 10-year predictions made at enrolment with versus without excluding the first year of outcomes following enrolment. This analysis (Supplementary Fig.19b) demonstrates robustness to excluding the first year of outcomes, with minimal performance degradation (for example, ASCVD AUC = 0.723 with 1-year exclusion versus 0.733 baseline). Second, we evaluated 1-year predictions at fixed timepoints (enrolment + 1 to enrolment + 9 years) using models trained with different washout periods (0, 1 and or 2 years). For each prediction timepointtpred∈ {1, 2,..., 9}, we trained models using data up totpred−wyears, wherew∈ {0, 1, 2} represents the washout period. This analysis (Supplementary Fig.19c) tests for temporal information leakage by varying the amount of training data available, demonstrating substantial residual predictive power even with 1–2-year washout periods across key diseases.

All analyses were performed using Python, with survival models implemented in lifelines and scikit-survival, and validated in R (v4.0) using the Survival package, and calibration and discrimination metrics computed using standard epidemiological methods.

### Reporting summary

Further information on research design is available in theNature Portfolio Reporting Summarylinked to this article.

## Data availability

Individual-level UKB data are available via formal application (https://www.ukbiobank.ac.uk/enable-your-research/apply-for-access; this research used application number 7089). MGB Biobank data are available to qualified researchers by request via the MGB Biobank programme (IRB protocol 2018P001236). AoU data are accessible (https://www.researchallofus.org/; workspace approved under IRB 2020P001737). PRS weights used in this study are publicly available from the PGS Catalog (https://www.pgscatalog.org/); the specific PGS IDs are listed in Supplementary Table1. PheCode–ICD-10 mappings are publicly available (https://phenomics.va.ornl.gov/phecodemap/). Summary statistics, signature lead SNP tables and supplementary data files supporting the figures and tables of this study have been deposited to GitHub (https://github.com/surbut/aladynoulli2; versioned release taggedv1.0) and archived on Zenodo29(https://zenodo.org/records/20802505). PerNaturepolicy, no datasets requiring public deposition (for example, sequencing reads and microarray data) were generated by this study; all primary data are derived from the three biobanks listed above.

## Code availability

All code implementing ALADYNOULLI—including the Bayesian generative model; the multi-batch training pipelines for the UKB, MGB and AoU; the prospective prediction evaluation utilities; the inverse probability weighting procedure for selection bias correction; and the analysis scripts for the GWAS and RVAS, the familial hypercholesterolaemia, CHIP, rheumatoid arthritis or breast cancer biological validations, the cross-cohort signature correspondence analyses and the PheCode-based Delphi-2M comparison—is publicly available on GitHub (https://github.com/surbut/aladynoulli2) under the MGB Source Available License. A versioned snapshot tagged v1.0 at the time of acceptance is permanently archived on Zenodo29(https://zenodo.org/records/20802505), providing a stable citable code reference independent of the working repository. The repository includes an interactive guide (https://surbut.github.io/aladynoulli2/index.html) linking to the core model code, the workflow scripts used to train and evaluate the model, the rendered analysis notebooks and the released Zenodo code archive. Custom algorithms central to the conclusions (the centred and non-centred MAP parameterizations, the slope-model variant, the 400K-pooledγwarm start and the IPW objective) are documented inline in theMethodsand implemented in the publicly available code.

## References

1. Zhao, J. et al. Using topic modeling via non-negative matrix factorization to identify relationships between genetic variants and disease phenotypes: a case study of lipoprotein(a) (LPA).PLoS ONE14, e0212112 (2019).ArticleCASPubMedPubMed CentralGoogle Scholar
2. Wang, W. & Stephens, M. Empirical Bayes matrix factorization.J. Mach. Learn. Res.22, 1–40 (2021).
3. Sudlow, C. et al. UK Biobank: an open access resource for identifying the causes of a wide range of complex diseases of middle and old age.PLoS Med.12, e1001779 (2015).ArticlePubMedPubMed CentralGoogle Scholar
4. Koyama, S. et al. Genetics and context for precision health in Greater Boston.Nat. Commun.16, 11661 (2025).
5. Nordestgaard, B. G. et al. Familial hypercholesterolaemia is underdiagnosed and undertreated in the general population: guidance for clinicians to prevent coronary heart disease: consensus statement of the European Atherosclerosis Society.Eur. Heart J.34, 3478–3490 (2013).ArticleCASPubMedPubMed CentralGoogle Scholar
6. Jaiswal, S. et al. Age-related clonal hematopoiesis associated with adverse outcomes.N. Engl. J. Med.371, 2488–2498 (2014).ArticlePubMedPubMed CentralGoogle Scholar
7. Abifadel, M. et al. Mutations inPCSK9cause autosomal dominant hypercholesterolemia.Nat. Genet.34, 154–156 (2003).ArticleCASPubMedGoogle Scholar
8. Herman, D. S. et al. Truncations of titin causing dilated cardiomyopathy.N. Engl. J. Med.366, 619–628 (2012).ArticleCASPubMedPubMed CentralGoogle Scholar
9. van Alten, S., Domingue, B. W., Faul, J., Galama, T. & Marees, A. T. Reweighting UK Biobank corrects for pervasive selection bias due to volunteering.Int. J. Epidemiol.53, dyae054 (2024).ArticlePubMedPubMed CentralGoogle Scholar
10. Shmatko, A. et al. Learning the natural history of human disease with generative transformers.Nature647, 248–256 (2025).ArticleADSCASPubMedPubMed CentralGoogle Scholar
11. Berry, D. A. Bayesian clinical trials.Nat. Rev. Drug Discov.5, 27–36 (2006).ArticleCASPubMedGoogle Scholar
12. Bellot, A. & Schaar, M. V. D. Flexible modelling of longitudinal medical data: a Bayesian nonparametric approach.ACM Trans. Comput. Healthcare1, 3 (2020).ArticleGoogle Scholar
13. Angus, D. C. & Chang, C.-C. H. Heterogeneity of treatment effect: estimating how the effects of interventions vary across individuals.JAMA326, 2312–2313 (2021).ArticlePubMedGoogle Scholar
14. Pedersen, E. M. et al. ADuLT: an efficient and robust time-to-event GWAS.Nat. Commun.14, 5553 (2023).ArticleADSCASPubMedPubMed CentralGoogle Scholar
15. Urbut, S. M. et al. MSGene: a multistate model using genetic risk and the electronic health record applied to lifetime risk of coronary artery disease.Nat. Commun.15, 4884 (2024).ArticleADSCASPubMedPubMed CentralGoogle Scholar
16. Jiang, X. et al. Age-dependent topic modeling of comorbidities in UK Biobank identifies disease subtypes with differential genetic risk.Nat. Genet.55, 1854–1865 (2023).ArticleCASPubMedPubMed CentralGoogle Scholar
17. Urbut, S. M. et al. Dynamic importance of genomic and clinical risk for coronary artery disease over the life course.Circ. Genom. Precis. Med.18, e004681 (2025).
18. Hyttinen, V., Kaprio, J., Kinnunen, L., Koskenvuo, M. & Tuomilehto, J. Genetic liability of type 1 diabetes and the onset age among 22,650 young Finnish twin pairs: a nationwide follow-up study.Diabetes52, 1052–1055 (2003).ArticleCASPubMedGoogle Scholar
19. Caruana, R. Multitask learning.Mach. Learn.28, 41–75 (1997).ArticleGoogle Scholar
20. Rasmussen, C. E. & Williams, C. K. I.Gaussian Processes for Machine Learning(MIT Press, 2006).
21. Putter, H. & van Houwelingen, H. C. Understanding landmarking and its relation with time-dependent Cox regression.Stat. Biosci.9, 489–503 (2017).ArticlePubMedGoogle Scholar
22. Cox, D. R. Regression models and life-tables.J. R. Stat. Soc. B34, 187–220 (1972).ArticleMathSciNetGoogle Scholar
23. Steyerberg, E. W. & Vergouwe, Y. Towards better clinical prediction models: seven steps for development and an ABCD for validation.Eur. Heart J.35, 1925–1931 (2014).ArticlePubMedPubMed CentralGoogle Scholar
24. Bastarache, L. Using Phecodes for research with the electronic health record: from PheWAS to PheRS.Annu. Rev. Biomed. Data Sci.4, 1–19 (2021).ArticlePubMedPubMed CentralGoogle Scholar
25. Hripcsak, G. & Albers, D. J. Next-generation phenotyping of electronic health records.J. Am. Med. Inform. Assoc.20, 117–121 (2013).ArticlePubMedGoogle Scholar
26. Yeung, M. W., Van Der Harst, P. & Verweij, N. ukbpheno v1.0: An R package for phenotyping health-related outcomes in the UK Biobank.STAR Protoc.3, 101471 (2022).ArticlePubMedPubMed CentralGoogle Scholar
27. Cohen, J.Statistical Power Analysis for the Behavioral Sciences(Routledge, 2013).
28. Thompson, D. J. et al. UK Biobank release and systematic evaluation of optimised polygenic risk scores for 53 diseases and quantitative traits. Preprint atmedRxivhttps://doi.org/10.1101/2022.06.16.22276246(2022).
29. Urbut, S., Gusev, A., Natarajan, P., & Parmigiani, G. A Bayesian Framework for longitudinal EHR and genetic discovery.Zenodohttps://doi.org/10.5281/zenodo.20802505(2026).
30. Bulik-Sullivan, B. K. et al. LD score regression distinguishes confounding from polygenicity in genome-wide association studies.Nat. Genet.47, 291–295 (2015).ArticleCASPubMedPubMed CentralGoogle Scholar
31. Willer, C. J. et al. Discovery and refinement of loci associated with lipid levels.Nat. Genet.45, 1274–1283 (2013).ArticleCASPubMedPubMed CentralGoogle Scholar
32. Kathiresan, S. & Srivastava, D. Genetics of human cardiovascular disease.Cell148, 1242–1257 (2012).ArticleADSCASPubMedPubMed CentralGoogle Scholar
33. Grant, S. F. A. et al. Variant of transcription factor 7-like 2 (TCF7L2) gene confers risk of type 2 diabetes.Nat. Genet.38, 320–323 (2006).ArticleCASPubMedGoogle Scholar
34. Evans, D. M. et al. Meta-analysis of genome-wide association studies confirms a susceptibility locus for knee osteoarthritis on chromosome 7q22.Ann. Rheum. Dis.70, 349–355 (2011).ArticleGoogle Scholar
35. Tcheandjieu, C. et al. Large-scale genome-wide association study of coronary artery disease in genetically diverse populations.Nat. Med.28, 1679–1692 (2022).ArticleCASPubMedPubMed CentralGoogle Scholar
36. Benn, M., Tybjærg-Hansen, A., Stender, S., Frikke-Schmidt, R. & Nordestgaard, B. G. Genetic and environmental influences on premature death in adult adoptees.N. Engl. J. Med.358, 1360–1368 (2008).Google Scholar
37. Jaiswal, S. et al. Clonal hematopoiesis and risk of atherosclerotic cardiovascular disease.N. Engl. J. Med.377, 111–121 (2017).ArticlePubMedPubMed CentralGoogle Scholar
38. Schoeler, T., Pingault, J.-B. & Kutalik, Z. The impact of self-report inaccuracy in the UK Biobank and its interplay with selective participation.Nat. Hum. Behav.9, 584–594 (2025).ArticlePubMedGoogle Scholar
39. Gail, M. H. et al. Projecting individualized probabilities of developing breast cancer for white females who are being examined annually.J. Natl Cancer Inst.81, 1879–1886 (1989).ArticleCASPubMedGoogle Scholar
40. Ashley, E. A. Towards precision medicine.Nat. Rev. Genet.17, 507–522 (2016).ArticleCASPubMedGoogle Scholar
41. Collins, F. S. & Varmus, H. A new initiative on precision medicine.N. Engl. J. Med.372, 793–795 (2015).ArticleCASPubMedPubMed CentralGoogle Scholar
42. Martínez-García, M. & Hernández-Lemus, E. Data integration challenges for machine learning in precision medicine.Front. Med.8, 784455 (2022).ArticleGoogle Scholar
43. Schork, N. J. Personalized medicine: time for one-person trials.Nature520, 609–611 (2015).ArticleADSCASPubMedGoogle Scholar
44. Price, A. L., Spencer, C. C. A. & Donnelly, P. Progress and promise in understanding the genetic basis of common diseases.Proc. R. Soc. B282, 20151684 (2015).ArticlePubMedPubMed CentralGoogle Scholar
45. Bailey, Z. D. et al. Structural racism and health inequities in the USA: evidence and interventions.Lancet389, 1453–1463 (2017).ArticlePubMedGoogle Scholar
46. Kalbfleisch, J. D. & Prentice, R. L.The Statistical Analysis of Failure Time Data(John Wiley & Sons, 2011).
47. Yeung, M. W. & Verweij, N. niekverw/ukbpheno: v1.0.0.Zenodohttps://doi.org/10.5281/ZENODO.6557829(2022).
48. Bycroft, C. et al. The UK Biobank resource with deep phenotyping and genomic data.Nature562, 203–209 (2018).ArticleADSCASPubMedPubMed CentralGoogle Scholar
49. Urbut, S. et al. MS Gene: multistate modeling of dynamic lifetime risk of coronary artery disease using electronic health records in the UK Biobank.Circulation148, A14747 (2023).ArticleGoogle Scholar
50. The All of Us Research Program Investigators. The ‘All of Us’ research program.N. Engl. J. Med.381, 668–676 (2019).ArticleGoogle Scholar
51. Mbatchou, J. et al. Computationally efficient whole-genome regression for quantitative and binary traits.Nat. Genet.53, 1097–1103 (2021).ArticleCASPubMedGoogle Scholar
52. Khera, A. V. et al. Diagnostic yield and clinical utility of sequencing familial hypercholesterolemia genes in patients with severe hypercholesterolemia.J. Am. Coll. Cardiol.67, 2578–2589 (2016).ArticleCASPubMedPubMed CentralGoogle Scholar
53. Harris, P. C. & Torres, V. E. Autosomal dominant polycystic kidney disease: the last 3 years.Kidney Int.76, 149–168 (2009).ArticlePubMedPubMed CentralGoogle Scholar
54. Shiels, A. & Bassnett, S. Mutations in the founder of theMIPgene family underlie cataract development in the mouse.Nat. Genet.12, 212–215 (1996).ArticleCASPubMedGoogle Scholar
55. Khan, S. S. et al. Development and validation of the American Heart Association’s PREVENT equations.Circulation149, 430–449 (2024).ArticlePubMedGoogle Scholar
56. Lloyd, J. D. M. et al. Estimating longitudinal risks and benefits from cardiovascular preventive therapies among medicare patients.J. Am. Coll. Cardiol.69, 1617–1636 (2017).ArticleGoogle Scholar

Download references

## Acknowledgements

We thank the participants and staff of the UKB, MGB and AoU, whose contributions made this work possible; and the Broad Institute and MGB research computing teams for computational infrastructure support.

## Funding

This work was supported by NHLBI K08 grant 1K08HL183784, American Heart Association Career Development Award 25CDA1444806 and Burroughs Wellcome Fund award 1360373 to S.M.U.; NHLBI grant R00HL165024 to T.N.; a Wellcome Early Career Award (227566/Z/23/Z) to X.J.; NIH grants R01HL127564 and U01HG011719 to P.N.; and a generous gift from the Dobson Family to G.P.

## Author information

Author notes
1. These authors jointly supervised this work: Alexander Gusev, Pradeep Natarajan, Giovanni Parmigiani

### Authors and Affiliations

1. Division of Cardiology, Heart and Vascular Institute, Massachusetts General Hospital, Boston, MA, USASarah M. Urbut, Satoshi Koyama, Anika Misra, Whitney E. Hornsby & Pradeep Natarajan
2. Cardiovascular Research Center, Massachusetts General Hospital, Boston, MA, USASarah M. Urbut, Satoshi Koyama, Whitney E. Hornsby & Pradeep Natarajan
3. Harvard Medical School, Boston, MA, USASarah M. Urbut, Tetsushi Nakao, Jordan W. Smoller, Alexander Gusev & Pradeep Natarajan
4. Broad Institute of MIT and Harvard, Cambridge, MA, USASarah M. Urbut, Tetsushi Nakao, Satoshi Koyama, Anika Misra, Leslie Gaffney, Whitney E. Hornsby, Jordan W. Smoller, Alexander Gusev & Pradeep Natarajan
5. Division of Population Sciences, Dana-Farber Cancer Institute, Boston, MA, USAYi Ding & Alexander Gusev
6. Division of Cardiovascular Medicine, Brigham and Women’s Hospital, Boston, MA, USATetsushi Nakao
7. Personalized Medicine, Mass General Brigham, Boston, MA, USASatoshi Koyama
8. Cardiovascular Epidemiology Unit, Department of Public Health and Primary Care, University of Cambridge, Cambridge, UKXilin Jiang
9. Department of Epidemiology, Harvard T.H. Chan School of Public Health, Boston, MA, USAXilin Jiang & Jordan W. Smoller
10. Independent Researcher, Portland, OR, USAAchyutha Harish
11. Psychiatric and Neurodevelopmental Genetics Unit, Massachusetts General Hospital, Boston, MA, USAJordan W. Smoller
12. Department of Biostatistics, Harvard T.H. Chan School of Public Health, Boston, MA, USAGiovanni Parmigiani
13. Department of Data Science, Dana-Farber Cancer Institute, Boston, MA, USAGiovanni Parmigiani
Authors
1. Sarah M. UrbutView author publicationsSearch author on:PubMedGoogle Scholar
2. Yi DingView author publicationsSearch author on:PubMedGoogle Scholar
3. Tetsushi NakaoView author publicationsSearch author on:PubMedGoogle Scholar
4. Satoshi KoyamaView author publicationsSearch author on:PubMedGoogle Scholar
5. Anika MisraView author publicationsSearch author on:PubMedGoogle Scholar
6. Xilin JiangView author publicationsSearch author on:PubMedGoogle Scholar
7. Achyutha HarishView author publicationsSearch author on:PubMedGoogle Scholar
8. Leslie GaffneyView author publicationsSearch author on:PubMedGoogle Scholar
9. Whitney E. HornsbyView author publicationsSearch author on:PubMedGoogle Scholar
10. Jordan W. SmollerView author publicationsSearch author on:PubMedGoogle Scholar
11. Alexander GusevView author publicationsSearch author on:PubMedGoogle Scholar
12. Pradeep NatarajanView author publicationsSearch author on:PubMedGoogle Scholar
13. Giovanni ParmigianiView author publicationsSearch author on:PubMedGoogle Scholar

### Contributions

S.M.U. conceptualized the study, developed the methodology, implemented the software, performed the formal analyses, conducted the validation analyses, prepared the figures, curated the data, and wrote and revised the manuscript. Y.D. contributed to methodology development, formal analysis and LDSC analyses. T.N. performed the genome-wide association analyses. S.K. performed the rare-variant association analyses. A.M. computed PRSs for the MGB and AoU cohorts used as input genetic features. X.J. contributed to methodology development, formal analysis and manuscript editing. A.H. advised on software vectorization for computational performance and provided computing infrastructure access. L.G. prepared the display items and final figure layouts. W.E.H. provided MGB data access and scientific input, and contributed to data curation and visualization. J.W.S. provided MGB data access and scientific input. A.G., P.N. and G.P. conceptualized the study, developed the methodology, provided supervision and resources, and contributed to and edited the manuscript. All authors reviewed and approved the final manuscript.

### Corresponding authors

Correspondence toSarah M. Urbut,Alexander Gusev,Pradeep NatarajanorGiovanni Parmigiani.

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Peer review

### Peer review information

Naturethanks the anonymous reviewers for their contribution to the peer review of this work.Peer reviewer reportsare available.

## Additional information

Publisher’s noteSpringer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Extended data figures and tables

### Extended Data Fig. 1ALADYNOULLI.

(a)Joint analysis(Figs.2–4): UK Biobank training data (400k individuals) divided into 40 subsets of 10k each, with one subset held out for testing. Disease-signature associations (\(\widehat{\phi }\)) and individual loadings (\(\widehat{\lambda }\)) estimated on each of the 39 training subsets using complete disease trajectories, then averaged:\({\phi }_{{\rm{fixed}}{\rm{train}}}=\frac{1}{39}{\sum }_{b=1}^{39}{\phi }^{(b)}\). The held-out test set is never used forϕestimation. Genetic validation performed using models with genetic mean effects removed (Γk= 0). (b)Prospective Analysis:Rigorous prediction evaluation using the held-out test set (10k individuals) with fixedϕfixed trainparameters. Individual loadings (\({\widehat{\lambda }}_{{\rm{test}}}\)) re-estimated using only data available up to each prediction time point through temporal censoring. (c)Cross-Population Validation:Independent estimation of disease signatures in Mass General Brigham (MGB) and All of Us (AoU) cohorts demonstrates reproducibility across different populations and healthcare systems. Each cohort yields cohort-specificϕandψparameters, with strong correlation between cohorts (see Extended Data Fig.2). (d)Leave-One-Out Cross-Validation:Robustness validation of the pooledϕapproach by excluding one batch at a time and comparing predictions using leave-one-outϕestimates versus full pooledϕestimates. The analysis evaluates static 10-year and dynamic 10-year AUC comparisons across all 40 batches. Results demonstrate near-perfect correlation (r = 0.995) with master predictions, mean AUC differences were ≤ 0.0001, maximum differences were ≤ 0.0015, and 99.6−100% of comparisons fell within a 0.01 AUC threshold. The scatter plot (bottom-right) shows LOO AUCs versus full pooled AUCs clustering tightly along the y=x line, confirming that a single batch has negligible impact on predictive performance. Sample sizes for panel c:n= 400, 000 UK Biobank training participants (40 batches ofn= 10, 000),n= 48, 069 MGB Biobank participants, andn= 208, 263 All of Us participants.

### Extended Data Fig. 2 Cross-cohort validation demonstrates robust disease signature replicability.

(a) Heatmaps showing the correspondence betweenALADYNOULLIdisease signatures (clusters) across cohorts, focusing on diseases common to all three biobanks. Each cell represents the proportion of diseases from a UK Biobank (UKB) signature that map to the corresponding signature in Mass General Brigham (MGB, left panel) or All of Us (AoU, right panel). Darker red indicates stronger correspondence. UKB clusters are ordered by their best-matching cluster in each validation cohort to highlight the diagonal pattern of correspondence. (b) Composition preservation probability calculation for each UKB signature. Disease-to-signature assignments are determined using posterior fitting (the signature with maximum posterior association strength, argmaxk(ψkd) for each disease). For each UKB cluster, we identified the best-matching cluster in the comparison cohort (MGB or AoU) by finding the cluster with maximum intersection size relative to the UKB cluster size. The composition preservation probability index is calculated as the proportion of diseases in a UKB signature that also belong to its best-matching signature in the other cohort (i.e., the intersection size divided by the UKB signature size, rather than the traditional Jaccard intersection-over-union). The analysis reveals high cross-cohort replicability, with a median composition preservation probability of 0.80 (IQR: 0.667, 0.964) across both validation cohorts, indicating that 80% of diseases within each UKB signature are consistently grouped together in the corresponding signature in independent healthcare systems. This demonstrates that disease signatures identified in UK Biobank are consistently replicated in independent populations.

### Extended Data Fig. 3 Temporal patterns of disease signatures across age in UK Biobank.

Each panel displays age-dependent disease probabilities for one of 21 signatures (20 disease signatures, Signatures 0–19, plus the low-incidence reference signature, Signature 20), showing how disease risk evolves from ages 30-81 years. For each signature, colored lines represent diseases assigned to that signature (based on maximum posteriorψkdassociation strength), while light grey lines show background diseases assigned to other signatures. The y-axis displays the probability of each disease given membership in the signature and age, computed by applying the sigmoid function to the time-varying disease-signature association parameters (ϕkdt) from the model. These probability trajectories reveal how diseases within each signature exhibit characteristic age-dependent risk patterns, with some diseases showing early-onset patterns (peaking in middle age) and others showing later-onset patterns (increasing with age), demonstrating the model’s ability to capture clinically meaningful temporal disease progression within biological pathways. These trajectories are descriptive visualizations of model-fit probabilities; no formal hypothesis test is applied within this panel.

### Extended Data Fig. 4 Population stratification and principal component adjustment analysis.

(a) Signature loading deviations from population mean (Δθ) over age (30-80 years) for four major ancestry groups: African (AFR), East Asian (EAS), South Asian (SAS), and European (EUR). Top row shows analyses without Principal Components (PCs); bottom row shows analyses with PCs included. The temporal dimension reveals that ancestry effects on signatures evolve with age, with peak deviations occurring at different life stages for different ancestries. (b) Correlation of signature-disease associations (ϕ) with and without PC adjustment. Each point represents the mean across 40 batches for each signature-disease-time combination (k, d, t). (c) PC-induced shift (Δ) for South Asian (SAS) ancestry displayed as a heatmap across signatures (K) and time (T). Red indicates positive shifts (amplification of signature loadings when PCs are included), while blue indicates negative shifts (reduction). Together, these panels demonstrate that PC adjustment: (1) preserves core biological disease-signature associations (ϕstability), (2) reveals amplified ancestry-specific signature loading patterns that evolve across the life course, and (3) demonstrates direct, structured relationships between ancestry and signature loadings.

### Extended Data Fig. 5 Polygenic risk score (PRS) associations with disease signatures.

(a) Top PRS-signature associations ranked by Z-score, showing the strongest genetic effects for signatures with known heritable components. (b) Heatmap of significant PRS-signature associations (FDR < 0.05), highlighting associations that survive multiple testing correction. (c) Complete PRS-signature association matrix showing all Z-scores across 36 PRS and 21 signatures. Associations between 36 external polygenic risk scores and signature loadings through theΓkparameters model genetic effects in the framework. Z-statistics are calculated from batch-aggregated estimates across model replicates (effect size / standard error). Using Benjamini-Hochberg FDR correction, we identified 116 significant PRS-signature associations out of 756. The strongest genetic effects align with known biology: coronary artery disease PRS on the cardiovascular signature (Signature 5,γ= 0.153, Z = 27.2), LDL cholesterol PRS on Signature 5 (γ= 0.071, Z = 22.7), and type 2 diabetes PRS on the metabolic signature (Signature 15,γ= 0.154, Z = 58.3). PRS categories are color-coded: cardiovascular (red), metabolic (blue), neurological (green), cancer (purple), autoimmune (orange), and other (gray). Statistical test: PRS–signature association Z-statistics are computed as\(Z={\bar{\gamma }}_{p,k}\,/\,{\rm{SEM}}({\gamma }_{p,k})\), where\({\bar{\gamma }}_{p,k}\)is the mean of per-batchγestimates across 40 leave-one-out training batches and\({\rm{SEM}}({\gamma }_{p,k})={\sigma }_{b}({\gamma }_{p,k})/\sqrt{40}\)is the standard error of the mean across batches (biologically independent UK Biobank participantsn= 400, 000). Two-sidedp-values were obtained from the standard normal asp= 2 (1 −Φ(∣Z∣)) and adjusted across all 756 PRS–signature pairs using the Benjamini–Hochberg FDR procedure; significance threshold FDR  < 0.05.

### Extended Data Fig. 6 Average Exposure over time (AEX) calculation for genetic discovery.

(a)Raw Latent Loadings:The model estimates individual-specific loadings\(\widehat{\lambda }\in {{\mathbb{R}}}^{N\times K\times T}\)for N=400,000 individuals across K=21 signatures and T=52 timepoints (ages 30-81). (b)Signature Weights:Raw loadings are transformed via softmax to obtain normalized signature loadingsθ∈ [0, 1]N×K×T, where ∑kθik(t) = 1 for each individual and timepoint, representing the probability distribution across signatures. (c)Individual Signature Trajectories:Left panel shows example temporal trajectories for different signatures (cardiovascular, cancer, metabolic, musculoskeletal) illustrating distinct age-related patterns. Right panel demonstrates patient heterogeneity within a single signature, showing how genetic and environmental factors lead to different AEX values across individuals. (d)AEX Matrix:The area under each individual’s signature trajectory is computed as\({{\rm{AEX}}}_{ik}={\int }_{30}^{80}{\theta }_{ik}(t)dt\), yielding a quantitative phenotype matrix\(\,{\rm{AEX}}\in {{\mathbb{R}}}^{N\times K}\)where each entry represents individuali’s lifetime exposure to signaturek. This matrix serves as the input for genome-wide association studies to identify genetic variants influencing signature-specific disease risk patterns.

### Extended Data Fig. 7 Rare variant association study (RVAS) robustness across variant filtering masks.

Gene-based rare variant association studies were performed using aggregated loss-of-function (LoF) variants within genes, testing whether gene-level rare variant burden is associated with signature exposure across six different variant filtering masks (Mask1–Mask6), representing different minor allele frequency (MAF) thresholds and variant quality filters. (Top-left) Number of unique significant genes identified per mask, showing consistent discovery across different filtering approaches (13–19 genes per mask). (Top-right) Robust discoveries: genes found in multiple masks, demonstrating reproducibility across variant filtering strategies. Seven genes (LDLR, LPA, APOB, CDH26, TTN, RAD52, PKD1) are robustly discovered across all 6 masks, while additional genes (MIP, BRCA2, TET2, C10orf67, DEFB1) are found in 5 masks. This cross-mask consistency validates that these associations are not artifacts of specific variant filtering choices. (Bottom-left) DEFB1 within the low-incidence reference signature (Signature 20), showing genome-wide significant association (−log10(p) ≈ 5) that replicates across all six masks; the red dashed line marks the genome-wide significance threshold. (Bottom-right) Cross-signature associations across masks, showing genes that associate with multiple signatures. PKD1 shows cross-signature associations in all 6 masks, BRCA2 in 5 masks, demonstrating that some genes have pleiotropic effects across multiple disease signatures. Together, these panels demonstrate that rare variant associations with signatures are robust across different variant filtering approaches, validating the biological replication of the discovered gene-signature relationships.

### Extended Data Fig. 8 Genetic validation of signature biological impact.

We demonstrate clinical and biological impact through multiple lines of evidence: (a)Familial Hypercholesterolemia (FH) validation: (Left) Signature 5 (cardiovascular signature) loading trajectories aligned to first ASCVD event for FH carriers (n=451, blue) versus non-carriers (n=54,028, red). Trajectories are aligned such that year 0 represents the time of the first cardiovascular event, showing signature loadings from 5 years before to 3 years after the event. (Right) Distribution of pre-event change in Signature 5 loading (ΔSig5) over the last 5 years before the event, calculated as the difference between signature loading at the end of the 5-year window (1 year before event) and at the start (5 years before event). FH carriers show a higher proportion experiencing a rise (95.57%) compared to noncarriers (92.72%), with an odds ratio of 1.63 (Fisher’s exact test, p=0.017). (b)Clonal Hematopoiesis of Indeterminate Potential (CHIP) validation: (Left) Signature 16 (critical care/inflammation signature) loading trajectories aligned to first Leukemia/MDS event for CHIP carriers (n=292, blue) versus noncarriers (n=2,602, red). (Right) Distribution of pre-event change in Signature 16 loading (ΔSig16) over the last 5 years before the event. CHIP carriers show a higher proportion experiencing a rise (79.79%) compared to noncarriers (70.37%). Analysis across multiple CHIP mutations and outcomes reveals consistent patterns: DNMT3A carriers show 1.97-fold enrichment (OR=1.97, p=0.0007) for Signature 16 before Leukemia/MDS events, with 81.1% of carriers showing rising trajectories compared to 68.5% of non-carriers. Similarly, TET2 carriers show 1.61-fold enrichment (OR=1.61,p= 8.9 × 10−5) for Signature 16 before Heart Failure events. Trajectory plots show the population mean signature loading at each event-aligned year (centre) with shaded bands indicating 95% confidence intervals of the mean obtained fromN= 2, 000 basic percentile bootstrap resamples within each carrier group. Odds-ratio enrichments and associatedp-values were computed using two-sided Fisher’s exact tests on the 2 × 2 contingency table of (rise / no-rise)  × (carrier / non-carrier), without adjustment for multiple comparisons. Sample sizes are reported alongside each comparison in the legend;nrefers to biologically independent UK Biobank participants.

### Extended Data Fig. 9 Comparison of Aladynoulli disease-level predictions versus Delphi ICD code-level predictions.

Each panel shows 1-year AUC for 28 diseases.Top row (centered model, as in v1):(a) PheCode-based comparison — Aladynoulli versus Delphi predictions aggregated across all ICD codes mapping to each PheCode-defined disease; horizontal bars show Delphi AUC range across ICD codes, circles show Aladynoulli AUC. Per-disease values are reported in Supplementary Table18; Delphi shows substantial within-disease ICD-code variability (mean range 0.185; max 0.396, Pneumonia). (b) Manual dictionary mapping — alternative comparison via simple string-matching of ICD codes to diseases. Color in (B) indicates Aladynoulli minus Delphi advantage (green positive).Bottom row (c, d):a parameterization-robustness sensitivity check performed under the non-centered variant of the model; full per-disease numbers, methodology, and source notebook are described in the online project documentation (https://surbut.github.io/aladynoulli2).

### Extended Data Fig. 10 Inverse probability weighting (IPW) analysis for selection bias correction.

IPW corrects for UK Biobank selection bias in two complementary directions: (1) Forward correction: When applying IPW weights derived from ref.9to the full UKB sample (unbalanced relative to the general population),ϕ(signature-disease associations) remains stable, preserving biological disease-signature relationships, while lambda and pi adapt to capture the reweighted population characteristics. (2) Reverse correction: When taking a restricted subsample (e.g., dropping a randomly sampled 90% of women) and applying IPW reweighting, the model successfully recovers the full population prevalence patterns and predicted hazards, demonstrating that IPW can restore unbiased population estimates from biased samples. (a) IPW analysis overview showingϕ/π/prevalence comparisons, and (b) individualλdifferences (see Extended Data for full details). (c) Model parameter comparison for full population vs contrived unbalanced subsample (90% women dropped) with and without IPW, showing three columns:ϕtrajectories (stable across conditions, correlation ≥0.99),πtrajectories, andempirical prevalencetrajectories (observed disease rates calculated from the data, not the model parameterμd; weighted vs unweighted showing bias and recovery) across three diseases (Prostate cancer, Postmenopausal bleeding, Breast cancer, from top to bottom). (d) Demographic distributions showing how IPW reweights the sample: (d:left) age distribution before and after weighting, and IPW weights distribution (mean=0.93, median=0.59, range 0.17-6.63), and (d:bottom) average weights by demographic subgroup, demonstrating that IPW corrects for underrepresentation IPW preserves disease-signature associations (ϕ) while enabling accurate estimation of unbiased population characteristics (λ,π) in both forward and reverse directions.

## Supplementary information

### Supplementary Information (download PDF)

This file contains Supplementary Figs. 1–23, Supplementary Tables 1–18, Supplementary Notes 1–5 and Supplementary References.

### Reporting Summary (download PDF)

### Peer Review File (download PDF)

## Rights and permissions

Open AccessThis article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visithttp://creativecommons.org/licenses/by-nc-nd/4.0/.

Reprints and permissions

## About this article

### Cite this article

Urbut, S.M., Ding, Y., Nakao, T.et al.A Bayesian framework for longitudinal EHR and genetic discovery.Nature(2026). https://doi.org/10.1038/s41586-026-10780-5

Download citation

* Received:27 August 2025
* Accepted:08 June 2026
* Published:15 July 2026
* Version of record:15 July 2026
* DOI:https://doi.org/10.1038/s41586-026-10780-5

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative