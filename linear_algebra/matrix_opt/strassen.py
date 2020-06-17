'''
Author: Jiang He
SBU ID: 111103814
# change target_level for level of division
'''

import time
import numpy as np


def naive_mm(m1, m2):
    if m1.shape[1] != m2.shape[0]:
        print("Matrix Inner Dimension Not Equal.")
        exit(-1)

    row1, col1 = m1.shape
    row2, col2 = m2.shape
    output_shape = (row1, col2)
    output_m = np.ones(output_shape)

    add_counter = 0
    mul_counter = 0
    for row_num1 in range(row1):
        for col_num2 in range(col2):
            sop = 0 # sum of product
            for col_num1 in range(col1):
                term_m1 = m1[row_num1][col_num1]
                term_m2 = m2[col_num1][col_num2]
                product = term_m1*term_m2
                sop += product
                mul_counter += 1
                add_counter += 1
            add_counter -= 1
            output_m[row_num1][col_num2] = sop
    return output_m


def divide_matrix(m):
    matrices = []
    mid_pt = m.shape[0]//2
    matrices.append(m[0:mid_pt, 0:mid_pt])
    matrices.append(m[0:mid_pt, mid_pt:])
    matrices.append(m[mid_pt:, 0:mid_pt])
    matrices.append(m[mid_pt:, mid_pt:])
    return matrices


def strassen(A, B, num_level, target_level=3):
    # when matrix is 1 by 1 
    if num_level == target_level:
        return naive_mm(A, B)
    
    # split A and B
    d1, d2, d3, d4 = divide_matrix(A)
    d5, d6, d7, d8 = divide_matrix(B)

    m1 = strassen(d1+d4, d5+d8, num_level+1)
    m2 = strassen(d3+d4, d5, num_level+1)
    m3 = strassen(d1, d6-d8, num_level+1)
    m4 = strassen(d4, d7-d5, num_level+1)
    m5 = strassen(d1+d2, d8, num_level+1)
    m6 = strassen(d3-d1, d5+d6, num_level+1)
    m7 = strassen(d2-d4, d7+d8, num_level+1)
    
    c11 = m1+m4-m5+m7
    c12 = m3+m5
    c21 = m2+m4
    c22 = m1-m2+m3+m6

    return np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))



np.random.seed(0)
A, B = np.random.randn(2**8, 2**8)*100-20, np.random.randn(2**8, 2**8)*9999+384
result = np.dot(A, B)

s = time.time()
output = strassen(A, B, target_level=3, num_level=0)
e = time.time()

print(result)
print(output)
print("Error:", np.sum(result-output))
print("Time used:", round((e-s)/60, 2), "mins")