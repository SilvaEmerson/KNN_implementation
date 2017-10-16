# -*- coding: utf-8 -*-
from statistics import median


features_train = []
labels_train = []
dists_mean = 0


def fit(feats_train, labs_train):
	'''
	feats_train = training features
	'''
	global features_train
	global labels_train
	features_train = feats_train
	labels_train = labs_train


def regress(features_test, k):
	global features_train
	global labs_train

	predictions = [med_calc(row_test, features_train, labels_train, k) for row_test in features_test]
	return predictions


def med_calc(row_test, features_train, labels_train, k):
    '''
	Calcula a distância entre os valores dos atributos da intância de teste
	com todas as intâncias de treino e retorna a classe mais presente na entre
	as distâncias 
	'''

    # para o caso de teste chama dist com cada instância de treino
    # adiciona à lista: [distância,classe]
    distances = [[dist(row_test, features_train[row_train]),
                  labels_train[row_train]] for row_train in range(len(features_train))]

    distances.sort()
    result = [distances[i][-1] for i in range(k)]
    
    #typecat de lista para um conjunto, e uso como chave de ordenação a função
    #count que irá retorna a quantidade de ocorrências de cada classe
    return median(result)


def predict(features_test, k):
    '''
	features_test = dados de teste
	features_train = dados de treino sem os rótulos
	k = parâmetro k
	'''
    global features_train
    global labs_train

    # chama closest para cada caso de teste
    predictions = [closest(row_test, features_train, labels_train, k) for row_test in features_test]

    return predictions


def closest(row_test, features_train, labels_train, k):
    '''
	Calcula a distância entre os valores dos atributos da intância de teste
	com todas as intâncias de treino e retorna a classe mais presente na entre
	as distâncias 
	'''

    # para o caso de teste chama dist com cada instância de treino
    # adiciona à lista: [distância,classe]

    distances = [[dist(row_test, features_train[row_train]),
                  labels_train[row_train]] for row_train in range(len(features_train))]

    distances.sort()

    #global dists
    #dists = sum(distances)/len(distances)
    #seleciona os k objetos mais próximos
    result = [distances[i][-1] for i in range(k)]
    
    #typecat de lista para um conjunto, e uso como chave de ordenação a função
    #count que irá retorna a quantidade de ocorrências de cada classe
    return max(set(result), key=result.count)


def dist(a, b):
    '''
	Calcula a distância entre pontos multidimencionais
	'''

    result = 0
    # realiza somatório da variação dos atributos corespondentes
    # dos caso de teste e treino
    for i in range(len(a)):
        result += ((a[i] - b[i]) ** 2)

    # return result**(1/2)
    
    return result ** 0.5


def score(predictions, labels_test):
    compare = [1 for i in zip(predictions, labels_test) if i[0] == i[1]]
    return float(len(compare)) / float(len(predictions)) * 100
