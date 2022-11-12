import torch
import numpy as np

#First Task
def getAdjacency(A, k):
    Ak = np.linalg.matrix_power(A, k)
    Ak = torch.from_numpy(Ak)
    sumMatrix = torch.sum(Ak, dim = 0)
    avgA = torch.div(Ak, sumMatrix)
    avgA = avgA.numpy()
    np.fill_diagonal(avgA, 0)
    return avgA


#A = [[0, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
#k = 2

#print(getAdjacency(A, k))

def allHops(A, kEnd=10):
    avgAttributes = []
    for h in range(kEnd):
        avgA = getAdjacency(A, h+1)
        #print(h+1)
        #print(avgA)
        avgAttributes.append(avgA)
    return avgAttributes

#allHops(A, 10)