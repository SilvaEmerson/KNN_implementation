from statistics import mode as md

class KNN():

    def train(self, features_train, labels_train):
        self.features_train = features_train
        self.labels_train = labels_train

    def predict(self, features_test, K):
        self.features_test = features_test
        self.K = K

        self.predictions = []

        for i in range(len(self.features_test)):
            matrix = []
            for j in range(len(self.features_train)):
                distance = self.dist(self.features_test[i], self.features_train[j])
                classes = self.labels_train[j]
                matrix.append([distance, classes])

            matrix.sort()
            classes = [i[-1] for i in matrix[:K]]
            #return sorted(set(classes), key=classes)
            self.predictions.append(md(classes))

        return self.predictions

    def score(self, labels_test):
        compare = [1 for i in zip(self.predictions, labels_test) if i[0] == i[1]]
        return (len(compare) / len(self.predictions)) * 100

    def dist(self, test, train):

        distance = 0

        for i in range(len(test)):
            distance += ((test[i] - train[i]) ** 2)

        return distance ** 0.5

#1-4 | 2-2| 3-4
'''
    train = [[10,5,5,3,6,7,7,10,1], [1,1,1,1,1,1,3,1,1], [8,10,10,8,7,10,9,7,1]]
    label_train = [4,2,4]
    test = [[2,1,1,1,2,1,2,1,1]]
    knn1 = KNN()
    knn1.train(train, label_train)
    print(knn1.predict(test, 1))
'''
