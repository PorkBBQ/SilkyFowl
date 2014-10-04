# -*- coding: utf-8 -*-

# silkyfowl.data
import sys
sys.path.append('..')

import proj.jData as jData
import numpy as np
import pandas as pd
    
class Data:
    dataList={}
    def __init__(self):
        self.dataList['mydata']='Preference data from [Mahout In Action] - Recommendation'
        
    def getDataList(self):
        import json
        return json.dumps(self.dataList, indent=2)
        
    def getData(self, dataName):
        # CSV
        if dataName in ['mydata']:
            csv=jData.getCSV('data\\dataset\\%s.csv' %dataName)
            return np.array(csv).astype(np.float)

        # XLSX
        if dataName.split('$')[0] in ['groups']:
            xlsx=pd.ExcelFile('data\\dataset\\%s.xlsx' %dataName.split('$')[0])
            return xlsx.parse(dataName.split('$')[1])

    def genClusters(self
        , centroids=np.array([[10,10],[20,20],[30,30]])
        , dispersion=5
        , numSamples=100
        , dist='normal'
        , showPlot=True):
        #centroids=np.array([[10,10],[20,20],[30,30]])
        #dispersion=5
        #numSamples=100
        
        centroids=np.array(centroids)
        numClusters=centroids.shape[0]
        numDim=centroids.shape[1]
        
        if dist=='interval':
            listClusters=[]
            for i in range(numClusters):
                newCluster=centroids[i] + (np.random.rand(numSamples, numDim)-0.5)*dispersion
                listClusters.append(newCluster)
            rtn=np.concatenate(listClusters)
        
        if dist=='normal':
            listClusters=[]
            for i in range(numClusters):
                for j in range(numSamples):
                    newSample=[]
                    for k in range(numDim):
                        newSample.append(np.random.normal(centroids[i][k], dispersion))
                    listClusters.append(newSample)
            rtn=np.array(listClusters)

        if showPlot:
            if numDim==2:
                import matplotlib.pyplot as plt
                plt.plot(rtn[:,0], rtn[:,1], 'o')
                plt.show()
                    
        return rtn
