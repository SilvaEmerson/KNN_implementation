#-*- coding: utf-8 -*-

import statistics as st

def dist(a,b):
	'''
	Calcula a distância entre pontos multidimencionais
	'''

	result = 0

	for i in range(len(a)):
		result += (a[i] - n[i])**2

	#return result**(1/2)
	return result**0.5

def predict(features_test, data_train, labels, k):
	'''
	features_test = dados de teste
	data_train = dados de treino sem os rótulos
	k = parâmetro k
	'''

	predictions = []

	for row in features_test:
		predictions.append(dist_calc(row))

	return predictions

def dist_calc(row, data_train, labels, k):
	'''
	Calcula a distância entre os valores dos atributos da intância de teste
	com todas as intâncias de treino e retorna a classe mais presente na entre
	as distâncias 
	'''

	distances = []

	for row_train in range(len(data_train)):
			distances.append([dist(row,data_train[row_train]),
				labels[row_train]])

	distances.sort()
	result = max([distances[i][-1] for i in range(k)])
	return st.mode(result)
