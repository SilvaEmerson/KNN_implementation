# Breast Cancer classification with KNN algorithm 

### What is KNN?
In pattern recognition, the k-nearest neighbors algorithm (k-NN) is a non-parametric method used for classification and regression. In both cases, the input consists of the k closest training examples in the feature space.

### URL Dataset
[Breast Cancer Winsconsin (Diagnostic) Data set](https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data), from UCI - Machine Learning Repository 

### Heatmap for correlation view 

![Heat map with attributes](images/heat-map.png "Heat map with attributes")

#### Used columns in the heatmap above 
Attribute | Abbreviation
------------ | -------------
Clump Thickness              | CT
Uniformity of Cell Size      | UCS 
Uniformity of Cell Shape     | UC
Marginal Adhesion            | MA
Single Epithelial Cell Size  | SECS
Bare Nuclei                  | BN
Bland Chromatin              | BC
Normal Nucleoli              | NN
Mitoses                      | M
  

According the correlations heatmap the **CT**, **M**, **BN** and **BC** attributes are the bests to divide data into classes, because the correlactions between them are the most closest of 0.

* **Colaborators**
  * [Émerson Silva](https://github.com/SilvaEmerson)
  * [Luís Eduardo](https://github.com/luiseduardogfranca) 

