'''
Author: Jiang He
SBU ID: 111103814
'''

import time
import numpy as np


'''
A is a matrix (square)
B is a col vector
'''
def forward_elimination(A, b):
    '''
    N = len(A)

    for j in range(N-1):
        for i in range(j+1, N):
            mij = A[i][j] / A[j][j]
            for k in range(j, N):
                A[i][k] -= (mij*A[j][k])
            b[i] -= (mij*b[j])

    return A, b
    '''
    Ab = np.hstack([A, b])
    n = len(A)

    for i in range(n):
        a = Ab[i]
        for j in range(i + 1, n):
            b = Ab[j]
            m = a[i] / b[i]
            Ab[j] = a - m * b
            
    return Ab[:,:-1], Ab[:,-1:]



def backward_elimination(A, b):
    Ab = np.hstack([A, b])
    n = len(A)

    for i in range(n - 1, -1, -1):
        Ab[i] = Ab[i] / Ab[i, i]
        a = Ab[i]

        for j in range(i - 1, -1, -1):
            b = Ab[j]
            m = a[i] / b[i]
            Ab[j] = a - m * b

    return Ab[:,:-1], Ab[:,-1:]



#A = np.random.randint(0, 10, 9).reshape(3, 3)
A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], np.float32)
b = np.array([8, -11, -3], np.float32).reshape(3, 1)
print("Input A:\n", A, "\n")
print("Input b:\n", b, "\n")
print("\n\n")

s = time.time()
forward_output_A, forward_output_b = forward_elimination(A, b)
e = time.time()
print("Forward result A:\n", forward_output_A, "\n")
print("Forward result b:\n", forward_output_b, "\n")
print("Total Time Used:", round(e-s, 2), "Seconds")
print("\n\n")


s = time.time()
backward_output_A, backward_output_b = backward_elimination(forward_output_A, forward_output_b)
e = time.time()
print("Backward result A:\n", backward_output_A, "\n")
print("Backward result b:\n", backward_output_b, "\n")
print("Total Time Used:", round(e-s, 2), "Seconds")
print("\n\n")
