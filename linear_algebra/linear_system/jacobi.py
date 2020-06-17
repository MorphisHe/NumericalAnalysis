'''
Author: Jiang He
SBU ID: 111103814
'''

import time
import numpy as np


def compute_stop(A, X, b):
    return np.linalg.norm(np.dot(A, X)-b)

# A is square matrix
# (diagonal dominant) matrix
def jacobi(A, b, tolerance=0.000001):
    inv_D, R = np.zeros(A.shape), A.copy()
    # filling in D and R
    for i in range(A.shape[0]):
        inv_D[i][i] = 1/A[i][i]
        R[i][i] = 0.0
    
    X = np.ones((A.shape[0], 1)) # x init
    T = np.dot(-1*inv_D, R)
    C = np.dot(inv_D, b)

    num_iter = 0
    while compute_stop(A, X, b) >= tolerance:
        if num_iter%20 == 0:
            print("Error:", round(compute_stop(A, X, b), 4))
        X = np.dot(T, X) + C
        num_iter += 1

    return X, num_iter



A = np.array([[10, 1, -1], [-3, 7, 2], [-2, 1, 6]])
b = np.array([8, -11, -3]).reshape(3, 1)
print("Input A:\n", A, "\n")
print("Input b:\n", b, "\n")

s = time.time()
X, num_iter = jacobi(A, b)
e = time.time()
print("\nResult X:\n", X)
print("\nNumber Iteration:", num_iter)
print("\nTime Taken:", round((e-s)/60, 2), "Seconds")
print("\nAX:\n", np.dot(A, X))
