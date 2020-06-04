'''
Author: Jiang He
SBU ID: 111103814
_, arg_init_x, arg_print, arg_percision = args
'''

import sys
import numpy as np


'''
return function of x as input
'''
def f(x):
    return np.cos(x) - x**3

'''
return derivative of f() at x
'''
def df(x):
    return -np.sin(x) - (3*(x**2))
    
'''
compute x_n2 of newton algorithm
'''
def newton_step(x_n1):
    f_xn1 = f(x_n1)
    df_xn1 = df(x_n1)
    x_n2 = x_n1 - (f_xn1/df_xn1)
    return x_n2

'''
compute the step criteria
'''
def compute_stop_criteria(x_n1, x_n2):
    nom = np.abs(x_n2 - x_n1)
    den = np.abs(x_n1)
    return nom / den
    

'''
This method will approximate root using newton method
Parameters:
    - init_x: initial value of x
    - tolerance: allowed error
    - float_percision: number of digit to round
    - print_iter: true if want to print intermediate result
'''
def newton_root(init_x, tolerance=0.00001, float_percision=4, print_iter=False):
    # initialize x_n1, x_n2, stop criteria
    num_iter = 0
    x_n1 = init_x
    x_n2 = newton_step(x_n1)
    ratio = compute_stop_criteria(x_n1, x_n2)

    # start iteration
    while ratio > tolerance:
        # print intermediate result
        if print_iter:
            print("Num Iteration:", num_iter)
            print("Xn", x_n1)
            print("Xn+1:", x_n2)
            print("f(Xn+1):", df(x_n2))
            print("=====================")

        # update vars
        x_n1 = x_n2
        x_n2 = newton_step(x_n1)
        ratio = compute_stop_criteria(x_n1, x_n2)
        num_iter += 1

    return round(x_n2, float_percision), num_iter



# parse args
args = sys.argv
_, arg_init_x, arg_print, arg_percision = args
arg_init_x = float(arg_init_x)
arg_print = int(arg_print)
arg_percision = int(arg_percision)



# start the algorithm
print("\n===============================================================")
print("Start finding real root using init x:", arg_init_x)

# create X, Y for the function
'''
X = np.linspace(-1, 2, 10000)
Y = [f(x, arg_percision) for x in X]
'''

# get the root
root, iters = newton_root(arg_init_x, float_percision=arg_percision, print_iter=arg_print)
print("Number of iterations performed:", iters)
print("Root of f() using Newton's Method:", root)
print("f(root):", round(f(root), arg_percision))
