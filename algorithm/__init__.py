# -*- coding: utf-8 -*-
class Algorithm:
    algorithmList={}
    def __init__(self):
        self.algorithmList['KNN']='K-Nearest Neighbor Classifier'

    def getAlgorithmLList(self):
        return self.algorithmList
        
    def getAlgorithm(self, algorithmName):
        if algorithmName=='KNN':
            import knn
            return knn.KNN()


