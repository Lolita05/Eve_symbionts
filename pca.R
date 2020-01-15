library(ggplot2)
library(ggfortify)
library(openxlsx)
library("viridis")    
setwd("") #change path
comtable <- read.xlsx("samples.xlsx")
pca.obj <- prcomp(comtable[, 2:72])
summary(pca.obj)
#get groups of conditions
comtable$group <- factor(gsub("_.*", "", comtable$X1))
#get very common groups of conditions
comtable$group <- factor(substr(comtable$X1, 4, 4))
autoplot(pca.obj, data=comtable, shape = 'group', loadings = TRUE, loadings.colour = plasma(71), loadings.label = TRUE, loadings.label.colour = magma(71), loadings.label.size = 3) + 
  theme_bw() + 
  geom_point(aes(shape=group, color=group)) + 
  scale_color_viridis(discrete = TRUE, option = "magma")

#only time series
timeSeriesTable <- comtable[comtable$group %in% c("B", "T"), ]
timeSeriesTable$group <- factor(gsub("_.*", "", timeSeriesTable$X1))

autoplot(prcomp(timeSeriesTable[, 2:73]), data=timeSeriesTable, colour = "group", loadings = TRUE, loadings.colour = plasma(72), loadings.label = TRUE, loadings.label.colour = magma(72), loadings.label.size = 3) + 
  theme_bw() +
  scale_color_viridis(discrete = TRUE, option = "viridis")

hc = hclust(dist(comtable[, 2:72]));
plot(hc, cex=0.5);
