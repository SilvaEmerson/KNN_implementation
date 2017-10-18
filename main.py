#-*- coding:utf-8 -*-

from data_process import cleanData
from KNN2 import KNN
import matplotlib.pyplot as plt

print("\n===========Diagnóstico de câncer de Mama===========\n\n")
percent = float(input("Porcentagem de treino:")) / 100
k = int(input("Digite o K:"))

limit = int(percent*len(cleanData))

features_train = [i[:-1] for i in cleanData[:limit]]
features_test = [i[:-1] for i in cleanData[limit:]]

labels_train = [i[-1] for i in cleanData[:limit]]
labels_test = [i[-1] for i in cleanData[limit:]]


knn = KNN()
knn.train(features_train, labels_train)
knn.predict(features_test, k)

print("\nCasos de treino: %d \nCasos de teste: %d \nAcurácia: %.2f %%" %(len(features_train),
 len(features_test), knn.score(labels_test)))

scores = []
for i in range(1, 10, 2):
    knn.predict(features_test, i)
    scores.append(knn.score(labels_test))

plt.plot(list(range(1, 10, 2)), scores)
plt.show()
