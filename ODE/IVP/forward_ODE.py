'''
Author: Jiang He
SBU ID: 111103814
'''

import sys
import numpy as np
import matplotlib.pyplot as plt


def save_plot(X, Y, title="Forward ODE Result"):
    # claer all existing plt plot
    plt.clf()
    plt.cla()

    # plot X and Y, Y=0, eyeballed_root point
    axes = plt.gca()
    #plt.scatter(X, Y, label="Linear Interpolation", c='green', zorder=4)
    plt.plot(X, Y, label="Forward ODE", c="green", linewidth=1.5)
    
    #true_y
    #plt.scatter(pt1[0], pt1[1], label="pt1", color='red', marker='o', zorder=5)
    #plt.scatter(pt2[0], pt2[1], label="pt2", color='purple', marker='o', zorder=5)


    # add title and labels
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid()
    
    # legend for the plot
    axes.legend()

    # save the plot
    plt.savefig(title)

from numpy import linspace, zeros, asarray
import matplotlib.pyplot as plt

def ode_FE(f, U_0, dt, T):
    N_t = int(round(float(T)/dt))
    # Ensure that any list/tuple returned from f_ is wrapped as array
    f_ = lambda u, t: asarray(f(u, t))
    u = zeros((N_t+1, len(U_0)))
    t = linspace(0, N_t*dt, len(u))
    u[0] = U_0
    for n in range(N_t):
        u[n+1] = u[n] + dt*f_(u[n], t[n])
    return u, t


def demo_SIR():
    """Test case using a SIR model."""
    def f(u, t):
        S, I, R = u
        return [-beta*S*I, beta*S*I - gamma*I, gamma*I]

    beta = 10./(40*8*24)
    gamma = 3./(15*24)
    dt = 0.1             # 6 min
    D = 30               # Simulate for D days
    N_t = int(D*24/dt)   # Corresponding no of hours
    T = dt*N_t           # End time
    U_0 = [50, 1, 0]

    u, t = ode_FE(f, U_0, dt, T)

    S = u[:,0]
    I = u[:,1]
    R = u[:,2]
    fig = plt.figure()
    l1, l2, l3 = plt.plot(t, S, t, I, t, R)
    fig.legend((l1, l2, l3), ('S', 'I', 'R'), 'lower right')
    plt.xlabel('hours')
    plt.show()

    # Consistency check:
    N = S[0] + I[0] + R[0]
    eps = 1E-12  # Tolerance for comparing real numbers
    for n in range(len(S)):
        SIR_sum = S[n] + I[n] + R[n]
        if abs(SIR_sum - N) > eps:
            print('*** consistency check failed: S+I+R=%g != %g' %\
                  (SIR_sum, N))

demo_SIR()