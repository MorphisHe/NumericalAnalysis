'''
Author: Jiang He
SBU ID: 111103814
_, arg_a, arg_b, arg_max_fx, arg_N, arg_percision = args
'''

import sys
import numpy as np
from random1 import lcg
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)


def generate_random_pts(N, a, b, max_fx):
    pts = []
    seedx = 123.0
    seedy = 23.023
    for i in range(N):
        seedx = lcg(seed=seedx)/(2*32)
        seedy = lcg(seed=seedy)/(2*32)

        x, y = seedx*b - a, seedy*max_fx - a
        pts.append((x, y))
    return pts


def save_plot(X, Y, title):
    # claer all existing plt plot
    plt.clf()
    plt.cla()

    # plot X and Y, Y=0, eyeballed_root point
    axes = plt.gca()
    # axes.set_ylim([-8, 8])
    plt.scatter(X, Y, s=1)

    # save the plot
    plt.savefig(title)

def monte_carlo_integration(a, b, max_fx, N, float_percision=4):
    print("\nGenerating random points")
    pts = generate_random_pts(N, a, b, max_fx)
    print("Done generating")
    X = [pt[0] for pt in pts]
    Y = [pt[1] for pt in pts]

    print("\nCreating plot for random points")
    save_plot(X, Y, "Random Points Generated")
    print("Done creating plot")

    print("\nCounting good samples")
    num_iter = 0
    good_sample = 0
    for pt in pts:
        x, y = pt
        fx = f(x)
        if y <= fx:
            good_sample += 1
        num_iter += 1

    boundary_area = (b-a) * (max_fx-a)
    integral = (good_sample/N) * boundary_area
    
    return round(integral, float_percision), num_iter




# parse args
args = sys.argv
_, arg_a, arg_b, arg_max_fx, arg_N, arg_percision = args
arg_a = float(arg_a)
arg_b = float(arg_b)
arg_max_fx = float(arg_max_fx)
arg_N = int(arg_N)
arg_percision = int(arg_percision)



# start the algorithm
print("\n===============================================================")
print("Start finding integral of f(x) in [" + str(arg_a) + "," + str(arg_b) + "]")



# get the root
integral, iters = monte_carlo_integration(arg_a, arg_b, arg_max_fx, arg_N, float_percision=arg_percision)
print("\n===============================================================")
print("Number of iterations performed:", iters)
print("Integral of f(x) in range [" + str(arg_a) + "," + str(arg_b) + "] is:", integral)
