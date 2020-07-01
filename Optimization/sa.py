'''
Simulated Annealing

Jiang He
SBU ID: 111103814
'''

import numpy as np

def f(x):
    return 1

def E(x):
    return 1

def compute_temp(fraction):
    return max(0.01, min(1, 1-fraction))

def new_state(S, fraction, a, b):
    amp = max(a, b) - min(a, b)
    amp = amp * fraction / 10
    delta = (-amp/2) + amp*np.random.uniform(0, 1) # potential error

    return max(min(S+delta, b), a) # clipping

# calculate rate of accpetance
def p(E, new_E, T):
    return min(1, np.exp(-(new_E-E)/T))


'''
So = inital state
intervals = domain of x
'''
def sa(So, num_steps, intervals):
    a, b = intervals
    S = So
    E = E(S)
    states, costs = [S], [E]

    for i in range(num_steps):
        fraction = i/num_steps
        T = compute_temp(fraction)
        new_S = new_state(S, fraction, a, b)
        new_E = E(new_S)

        q = np.random.uniform(0, 1)
        if p(E, new_E, T) > q:
            S, E = new_S, new_E
            states.append(S)
            costs.append(E)
    
    return states, costs