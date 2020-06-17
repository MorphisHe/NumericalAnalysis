'''
Author: Jiang He
SBU ID: 111103814
'''

import time
import numpy as np
import matplotlib.pyplot as plt


# num_pts = number of pts to generate in interval (pt1, pt2)
def linear_interpolation(pt1, pt2, num_pts=10):
    pt1_x, pt1_y = pt1
    pt2_x, pt2_y = pt2
    step_size = (pt2_x-pt1_x)/(num_pts+2)

    list_x = np.linspace(pt1_x+step_size, pt2_x-step_size, num_pts)
    list_y = []
    for x in list_x:
        y = pt1_y + (pt2_y-pt1_y)*(x-pt1_x)/(pt2_x-pt1_x)
        list_y.append(y)
    
    return list_x, np.array(list_y)


def save_plot(X, Y, pt1, pt2, title="Linear_Interpolation_Result"):
    # claer all existing plt plot
    plt.clf()
    plt.cla()

    # plot X and Y, Y=0, eyeballed_root point
    axes = plt.gca()
    plt.scatter(X, Y, label="Linear Interpolation", c='green', zorder=4)
    plt.plot(np.append(X, [pt1[0], pt2[0]]), np.append(Y, [pt1[1], pt2[1]]), c="blue", alpha=0.5, linewidth=1.5)
    plt.scatter(pt1[0], pt1[1], label="pt1", color='red', marker='o', zorder=5)
    plt.scatter(pt2[0], pt2[1], label="pt2", color='purple', marker='o', zorder=5)


    # add title and labels
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    
    # legend for the plot
    axes.legend()

    # save the plot
    plt.savefig(title)



pt1, pt2 = [0, 0], [3, 12]
list_x, list_y = linear_interpolation(pt1, pt2)
save_plot(list_x, list_y, pt1, pt2)

    