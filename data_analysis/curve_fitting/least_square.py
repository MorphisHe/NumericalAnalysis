'''
Author: Jiang He
SBU ID: 111103814
'''

import sys
import numpy as np


def kk(X, Y):
    sum_Y = np,sum(Y)
    sum_X = np.sum(X)
    sum_XX = np.sum(X**2)

    XY = X*Y
    sum_XY = np.sum(XY)
    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    a = ((mean_Y*sum_XX) - (mean_X*sum_XY)) / (sum_XX - (len(X)*(mean_X**2)))
    b = ((sum_XY - (len(X)*mean_X*mean_Y))) / (sum_XX - (len(X)*(mean_X**2)))
    return a, b


X = np.array([1, 2, 3, 4])
Y = np.array([6, 5, 7, 10])
a, b = kk(X, Y)
print(a, b)