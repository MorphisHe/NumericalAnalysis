'''
Author: Jiang He
SBU ID: 111103814
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def lcg(seed):
    m = 2**32
    a = 1664525
    c = 1013904223

    return (a*seed + c) % m


def generate_rand(rand):
    m = 2**32
    a = 1664525
    c = 1013904223

    x1 = (a*rand + c) % m
    rand = x1
    x1 = x1/2**32
    return x1, rand

'''
This function generates pair of statistically independent normally distributed random numbers (x, y)
parameters:
    - mean: desired mean of generated normally distributed random numbers
    - std: desired std of generated normally distributed random numbers
'''
def box_muller(x1, x2, mean=0, std=1):
    # generate standard normal distribution using Box-Muller transformation
    g1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
    #g2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

    # convert to desired mean and std
    z1 = mean + (g1*std)
    #z2 = mean + (g2*std)

    return z1



def save_plot(X, title, rwidth, bins, x_label="x", y_label="f(x)"):
    # claer all existing plt plot
    plt.clf()
    plt.cla()

    # plot X and Y, Y=0, eyeballed_root point
    axes = plt.gca()
    # axes.set_ylim([-8, 8])
    plt.figure(figsize=(20,10))
    arr = plt.hist(X, color = 'blue', edgecolor = 'black', bins = bins, rwidth=rwidth)
    for i in range(bins):
        plt.text(arr[1][i],arr[0][i],str(int(arr[0][i])))

    # save the plot
    plt.savefig(title)


rand = 1.0
ideal_mean = 8
ideal_std = 4
num_pts = 250000000
random_pts = []
for i in range(num_pts):
    x1, rand = generate_rand(rand)
    random_pts.append(x1)

save_plot(random_pts, "dist of random numbers", 0.5, 10)

box_muller_numbers = []
for i in range(1, num_pts):
    x1, x2 = random_pts[i-1], random_pts[i]
    g1 = box_muller(x1, x2, ideal_mean, ideal_std)
    box_muller_numbers.append(g1)

save_plot(box_muller_numbers, "box-muller transform", 1, bins=8)
    
'''
Z1 = [x[0] for x in Z]
Z2 = [x[1] for x in Z]

save_plot(Z1, "bm test")
'''