'''
Author: Jiang He
SBU ID: 111103814
_, arg_init_x1, arg_init_x2, arg_print, arg_percision = args
'''

import sys
import numpy as np


'''
return function of x as input
'''
def f(x):
    return np.cos(x) - x**3
    
'''
compute x_n3 of secant algorithm
'''
def secant_step(x_n1, x_n2):
    f_xn1 = f(x_n1)
    f_xn2 = f(x_n2)
    
    nom = f_xn2 * (x_n2 - x_n1)
    den = f_xn2 - f_xn1
    return x_n2 - (nom / den)


'''
compute the step criteria
'''
def compute_stop_criteria(x_n1, x_n2):
    nom = np.abs(x_n2 - x_n1)
    den = np.abs(x_n1)
    return nom / den
    

'''
This method will approximate root using secant method
Parameters:
    - init_x1, init_x2: initial value of x1, x2
    - tolerance: allowed error
    - float_percision: number of digit to round
    - print_iter: true if want to print intermediate result
'''
def secant_root(init_x1, init_x2, tolerance=0.00001, float_percision=4, print_iter=False):
    # initialize x_n1, x_n2, stop criteria
    num_iter = 0
    x_n1 = init_x1
    x_n2 = init_x2
    x_n3 = secant_step(x_n1, x_n2)
    ratio = compute_stop_criteria(x_n2, x_n3)

    # start iteration
    while ratio > tolerance:
        # print intermediate result
        if print_iter:
            print("Num Iteration:", num_iter)
            print("Xn", x_n1)
            print("Xn+1:", x_n2)
            print("Xn+2:", x_n3)
            print("f(Xn+2):", f(x_n3))
            print("=====================")

        # update vars
        x_n1 = x_n2
        x_n2 = x_n3
        x_n3 = secant_step(x_n1, x_n2)
        ratio = compute_stop_criteria(x_n2, x_n3)
        num_iter += 1

    return round(x_n3, float_percision), num_iter



# parse args
args = sys.argv
_, arg_init_x1, arg_init_x2, arg_print, arg_percision = args
arg_init_x1 = float(arg_init_x1)
arg_init_x2 = float(arg_init_x2)
arg_print = int(arg_print)
arg_percision = int(arg_percision)



# start the algorithm
print("\n===============================================================")
print("Start finding real root using init x:", arg_init_x1, arg_init_x2)

# create X, Y for the function
'''
X = np.linspace(-1, 2, 10000)
Y = [f(x, arg_percision) for x in X]
'''

# get the root
root, iters = secant_root(arg_init_x1, arg_init_x2, float_percision=arg_percision, print_iter=arg_print)
print("Number of iterations performed:", iters)
print("Root of f() using Newton's Method:", root)
print("f(root):", round(f(root), arg_percision))
