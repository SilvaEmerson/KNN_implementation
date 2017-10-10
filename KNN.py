#-*- coding: utf-8 -*-

import statistics as st


def predict(features_test, data_train, labels, k):
	'''
	features_test = dados de teste
	data_train = dados de treino sem os rótulos
	k = parâmetro k
	'''

    #chama dist_calc para cada caso de teste
	predictions = [dist_calc(row_test,data_train,labels,k) for row_test in features_test]

	return predictions


def dist_calc(row_test, data_train, labels, k):
	'''
	Calcula a distância entre os valores dos atributos da intância de teste
	com todas as intâncias de treino e retorna a classe mais presente na entre
	as distâncias 
	'''

    #para o caso de teste chama dist com cada instância de treino
	distances = [[dist(row_test, data_train[row_train]),
				labels[row_train]] for row_train in range(len(data_train))]

	distances.sort()
	result = max([distances[i][-1] for i in range(k)])
	return st.mode(result)

def dist(a,b):
	'''
	Calcula a distância entre pontos multidimencionais
	'''

	result = 0

	#realiza somatório da variação dos atributos corespondentes
	#dos caso de teste e treino 
	for i in range(len(a)):
		result += ((a[i] - b[i])**2)

	#return result**(1/2)
	return result**0.5