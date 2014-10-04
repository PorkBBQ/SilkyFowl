# -*- coding: utf-8 -*-

def flexibleInstance(centroids, stdev, numSamples, condidate):
    return'''    
import proj.silkyfowl as sf
import numpy as np
import matplotlib.pyplot as plt

group1=np.random.rand(20,2)+[5,5]
group2=np.random.rand(20,2)+[10,10]
data=np.concatenate((group1, group2))
label=['A']*20+['B']*20

plt.plot(data[:,0], data[:,1], 'o')
plt.show()
candidate=[6,6]

knn=sf.algorithm.Algorithm().getAlgorithm('KNN')
result=knn.getClassification(candidate, data, label, 2)
print('Classification: %s' %result)
    '''
    
def getInstance(execute=True):
    rtn='''
import proj.silkyfowl as sf
import numpy as np
import matplotlib.pyplot as plt

# generate data
group1=np.random.rand(20,2)+[5,5]
group2=np.random.rand(20,2)+[10,10]
data=np.concatenate((group1, group2))
label=['A']*20+['B']*20
candidate=[6,6]

# plot
plt.plot(data[:,0], data[:,1], 'o')
plt.show()

# classify
knn=sf.algorithm.Algorithm().getAlgorithm('KNN')
result=knn.getClassification(candidate, data, label, 2)
print('Classification: %s' %result)
    '''
    if execute:
        exec(rtn)
    return rtn