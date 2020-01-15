import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as shc
df = pd.read_excel("samples.xlsx") #change path

# Plot
plt.figure(figsize=(16, 10), dpi= 80)  
plt.title("Samples", fontsize=22)  
dend = shc.dendrogram(shc.linkage(df[['Gammaproteobacteria',	'Alphaproteobacteria',	'Holozoa',	'Bacteroidia',	'Alveolata',	'Bacilli',	'Armatimonadia',	'unclassified_Proteobacteria',	'Actinobacteria',	'Verrucomicrobiae',	'Deltaproteobacteria',	'unclassified_Bacteroidetes',	'Acidimicrobiia',	'Oxyphotobacteria',	'Clostridia',	'unclassified_SAR',	'Sericytochromatia',	'Discoba',	'Stramenopiles',	'Blastocatellia',	'(Subgroup',	'4)',	'Deinococci',	'Nucletmycea',	'Rhizaria',	'Acidobacteriia',	'unclassified_Firmicutes',	'Chloroplastida',	'Discosea',	'Planctomycetacia',	'Anaerolineae',	'Leptospirae',	'Ancyromonadida',	'Nitrospira',	'Tubulinea',	'unclassified_Actinobacteria',	'Mycamoeba',	'Negativicutes',	'SAR',	'unclassified_Eukaryota',	'Opisthokonta',	'Proteobacteria',	'unclassified_Bacteria',	'Bacteroidetes',	'Archaeplastida',	'Acidobacteria',	'Verrucomicrobia',	'Cyanobacteria',	'Armatimonadetes',	'Deinococcus-Thermus',	'Chloroflexi',	'Excavata',	'Planctomycetes',	'Campylobacteria',	'unclassified_Planctomycetes',	'Mollicutes',	'Goniomonas',	'Fusobacteriia',	'class',	'kingdom',	'superkingdom',	'Chlamydiae',	'Phycisphaerae',	'unclassified_Acidobacteria',	'Firmicutes',	'OM190',	'Erysipelotrichia',	'Spirochaetia',	'Subgroup',	'Nitrososphaeria',	'unclassified_Opisthokonta']], method='ward'), labels=df.Sample.values, color_threshold=800)
plt.xticks(fontsize=10)
plt.savefig(path) #change path to save
