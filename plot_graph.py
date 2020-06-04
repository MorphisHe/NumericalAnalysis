
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x

def save_plot(X, Y, title, x_label="x", y_label="f(x)"):
    # claer all existing plt plot
    plt.clf()
    plt.cla()

    # plot X and Y, Y=0, eyeballed_root point
    axes = plt.gca()
    # axes.set_ylim([-8, 8])
    plt.plot(X, Y)

    # save the plot
    plt.savefig(title)

X = np.linspace(0, 100, 1000)
Y = [f(x) for x in X]
