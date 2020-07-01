'''
Markov Chain Monte Carlo

Jiang He
SBU ID: 111103814
'''

import numpy as np

def E(x, y):
    return 1

def metropolis(Ey, Ex, T=0.00014):
    return min(1, np.exp(-(Ey-Ex)/T))

def move_pt(x, y, h):
    return x, y


'''
N = num of loops
h = step size to move a random point
'''
def mcmc(X, Y, h, N):
    num_pts = len(X)
    for i in range(N):
        rand_pt_index = np.random.uniform(0, num_pts)
        pt_x, pt_y = X[rand_pt_index], Y[rand_pt_index]
        new_x, new_y = move_pt(pt_x, pt_y, h)

        Ex = E(pt_x, pt_y)
        Ey = E(new_x, new_y)
        p = metropolis(Ey, Ex)

        q = np.random.uniform(0, 1)
        if q < p:
            # accept the move
            X[rand_pt_index] = new_x
            Y[rand_pt_index] = new_y
