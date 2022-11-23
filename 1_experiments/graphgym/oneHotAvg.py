import torch
import numpy as np

#Second Task
#get khop neighbors
#get one-hot vectors for each neighbor
#avg the one-hot vectors

#def getPred():


def avgPred(predArr):
    #predList is an array of one-hot vectors (one for each neighbor)
    #predList is of size nxc where c is the number of classes and n is number of neighbors in that hop
    predList = torch.from_numpy(predArr)
    n = predList.size(dim = 1)

    predSum = torch.sum(predList, 0)
    avgPred = torch.div(predSum, n)
    #label is the index of the larget element of the avg of one-hots
    predictedLabel = torch.argmax(avgPred)
    return predictedLabel

#predList = np.array([[0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0]])
#print(avgPred(predList))