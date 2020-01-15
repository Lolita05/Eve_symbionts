# The dynamics of diversity and abundance of symbionts in the metatranscriptome

Eulimnogammarus verrucosus  is an amphipod endemic to the unique ecosystem of Lake Baikal and serves as an model in ecotoxicological studies. In this study, were analyzed 63 transcriptomes of E. verrucosus subjected to various types of stress. The transcriptome assemblies is avaliable in the GenBank database under the accession number  GHHK00000000 (E. verrucosus). 

- Eve_Symbionts_Notebook - all steps of the project
- samples.xlsx - all symbionts for samples
- cluster_visualization - script for sample clustering
- pca.R - script for PCA

## Goal:

The goal of this project is the description of the symbiont composition associated with Eulimnogammarus verrucosus

## Objectives:

- Choose the optimal method for characterizing the symbiont composition
- Characterize the samples (diversity and abundance of symbionts) by the selected method
- Characterize the variability of these parameters from sample to sample

## Methods

1. The Ribotagger was used to obtain sequences of 16 / 18s rRNA of symbionts from metatranscriptome. 
Repository link: https://github.com/xiechaos/ribotagger
For more details, please read the official publication at:
https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-016-1378-x

2. Classification was carried out using IDTAXA Classifier (Silva Database (release 132))

