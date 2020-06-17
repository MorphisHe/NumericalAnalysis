'''
Author: Jiang He
SBU ID: 111103814
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


np.random.seed(0)
A, B = np.random.randn(2**10, 2**4), np.random.randn(2**4, 2**8)
result = np.dot(A, B)

s = time.time()
output = naive_mm(A, B)
e = time.time()

print(result)
print(output)
print("Error:", np.sum(result-output))
print("Time used:", round(e-s, 2), "secs")