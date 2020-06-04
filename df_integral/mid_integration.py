'''
Author: Jiang He
SBU ID: 111103814
_, arg_a, arg_b, arg_N, arg_percision, arg_print = args
'''

import sys
import numpy as np

def f(x):
    # x^3 + sin(x)
    term1 = x**3
    term2 = np.sin(x)
    return term1 + term2


'''
This function approximates integral of f(x) in range [a, b]
Formula: 
    - I = integral of f(x)dx in [a, b]
    - I = h * sum of f(xn) for n in [0, N-1]
Parameters:
    - a, b: interval of integral we want to compute
    - N: number of rectangles used to approximate the integral
    - float_percision: number of digit to round
    - print_iter: true if want to print intermediate result
'''
def mid_pt_integration(a, b, N, float_percision=4, print_iter=False):
    h = (b-a) / N
    a = a + h/2
    
    # start computing integral
    integral_f = 0
    num_iter = 0
    for n in range(N):
        xn = a + (n*h)
        f_xn = f(xn)
        integral_f += f_xn

        # print intermediate process
        if print_iter:
            print("Num Iteration:", num_iter)
            print("Xn:", xn)
            print("f(Xn):", f_xn)
            print("Cumulative Integral:", round(h * integral_f, float_percision))
            print("==========================")

        num_iter += 1

    return round(h * integral_f, float_percision), num_iter




# parse args
args = sys.argv
_, arg_a, arg_b, arg_N, arg_percision, arg_print = args
arg_a = int(arg_a)
arg_b = int(arg_b)
arg_N = int(arg_N)
arg_print = int(arg_print)
arg_percision = int(arg_percision)



# start the algorithm
print("\n===============================================================")
print("Start finding integral of f(x) in [" + str(arg_a) + "," + str(arg_b) + "]")



# get the root
integral, iters = mid_pt_integration(arg_a, arg_b, arg_N, float_percision=arg_percision, print_iter=arg_print)
print("\n===============================================================")
print("Number of iterations performed:", iters)
print("Integral of f(x) in range [" + str(arg_a) + "," + str(arg_b) + "] is:", integral)
