'''
Author: Jiang He
SBU ID: 111103814
'''

import time
import numpy as np


def compute_stop(X, X_prev):
    return np.linalg.norm(X-X_prev)


'''
Find eigen value
'''
def power(A, tolerance=0.0000001):
    N = A.shape[1]
    X_prev = np.ones((N, 1)) # init X
    X = np.dot(A, X_prev)/X_prev[-1][0]

    num_iter = 0
    while compute_stop(X, X_prev) >= tolerance:
        X_prev = X.copy()
        X = np.dot(A, X_prev)/X_prev[-1][0]
        num_iter += 1
    
    AX = np.dot(A, X)
    AXX = np.sum(AX*X)
    XX = np.sum(X*X)
    eigen_value = AXX/XX

    return eigen_value, num_iter


A = np.array([[2, -12], [1, -5]])
print("Input A:\n", A, "\n")

s = time.time()
eigen_value, num_iter = power(A)
e = time.time()
print("\nResult Eigen Value:\n", eigen_value)
print("\nNumber Iteration:", num_iter)
print("\nTime Taken:", round((e-s)/60, 2), "Seconds")
