
# -*- coding: utf-8 -*-


import lib.jData as jData
import numpy as np

    
class Data:
    dataList={}
    def __init__(self):
        self.dataList['mydata']='Preference data from [Mahout In Action] - Recommendation'
        
    def getDataList(self):
        import json
        print(json.dumps(self.dataList, indent=2))
        
    def getData(self, dataName):
        if dataName.lower()=='mydata':
            csv=jData.getCSV(r'data\dataSet\mydata.csv')
            return np.array(csv).astype(np.float)
