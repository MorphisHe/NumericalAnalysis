'''
Author: Jiang He
SBU ID: 111103814
_, arg_init_x, arg_print, arg_percision, arg_epsilon = args
'''

import sys
import numpy as np


'''
return function of x as input
'''
def f(x, float_percision):
    return x


'''
This method will approximate root using bisection method
Parameters:
    - init_x: initial value of x
    - epsilon: small value use to define interval of search
    - tolerance: allowed error
    - float_percision: number of digit to round
    - print_iter: true if want to print intermediate result
'''
def bisection_root(init_x, epsilon, tolerance=0.00001, float_percision=4, print_iter=False):
    # define end points of our interval
    a, b = init_x-epsilon, init_x+epsilon

    # start iteration
    # stop criteria = (b-a)/2^n <= tolerance
    num_iter = 0
    interval_length = (b-a)/(2**num_iter)
    mid = a + ((b-a)/2)
    while interval_length > tolerance:
        # print intermediate result
        if print_iter:
            print("Num Iter:", num_iter)
            print("Mid Point x:", mid)
            print("f(x):", round(f(mid), float_percision))
            print("=====================")
        
        # check if found a good root approximation
        if np.abs(f(mid)) <= tolerance:
            return round(mid, float_percision), num_iter
        else:
            # update a, b
            f_a, f_b, f_mid = f(a), f(b), f(mid)
            if f_a*f_mid >= 0:
                a = mid
            elif f_b*f_mid >= 0:
                b = mid

            # update mid, interval_length, num_iter
            mid = a + ((b-a)/2)
            num_iter += 1
            interval_length = (b-a)/(2**num_iter)
    
    return round(mid, float_percision), num_iter



# parse args
args = sys.argv
_, arg_init_x, arg_print, arg_percision, arg_epsilon = args
arg_init_x = float(arg_init_x)
arg_print = int(arg_print)
arg_percision = int(arg_percision)
arg_epsilon = float(arg_epsilon)



# start the algorithm
print("\n===============================================================")
print("Start finding real root using init x:", arg_init_x)

# create X, Y for the function
'''
X = np.linspace(-1, 2, 10000)
Y = [f(x, arg_percision) for x in X]
'''

# get the root
root, iters = bisection_root(arg_init_x, arg_epsilon, float_percision=arg_percision, print_iter=arg_print)
print("Interval to search: [", str(round(f(arg_init_x-arg_epsilon), arg_percision)), str(round(f(arg_init_x+arg_epsilon), arg_percision)), "]")
print("Number of iterations performed:", iters)
print("Root of f() using Bisection Method:", root)
print("f(root):", round(f(root), arg_percision))
