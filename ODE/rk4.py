'''
Author: Jiang He
SBU ID: 111103814
'''

import sys
import numpy as np
import matplotlib.pyplot as plt


'''
a = len of x interval
'''
def rk4(Vb, num_steps, a=7777, Yo=0):
    h = a/num_steps # step size
    list_x = np.linspace(a, 0, num_steps)
    list_y = []

    Yn = Yo
    list_y.append(Yn)
    for x in list_x[1:]:
        tn = x
        k1 = f(tn, Yn, Vb)
        k2 = f(tn+(h/2), Yn+(h*k1/2), Vb)
        k3 = f(tn+(h/2), Yn+(h*k2/2), Vb)
        k4 = f(tn+h, Yn+(h*k3), Vb)
        slope = (k1 + 2*k2 + 2*k3 + k4)/6
        
        Yn = Yn + slope*h
        list_y.append(Yn)

    return list_x, np.asarray(list_y)