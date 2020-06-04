'''
Author: Jiang He
SBU ID: 111103814
'''

def lcg(m=2*32, a=25214903917, c=11, seed=1):
    return (a*seed + c) % m

def float_random(seed1=0.375205, seed2=0.376047):
    return (seed1 + seed2) % 1.0