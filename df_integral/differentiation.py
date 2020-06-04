'''
Author: Jiang He
SBU ID: 111103814
'''


def f(x):
    return x


def central_dif(x, h, float_percision):
    a = f(x+h)
    b = f(x-h)
    nom = a - b
    den = 2*h
    return round(nom / den, float_percision)

def forward_dif(x, h, float_percision):
    a = f(x+h)
    b = f(x)
    nom = a - b
    den = h
    return round(nom / den, float_percision)

def backward_dif(x, h, float_percision):
    a = f(x)
    b = f(x-h)
    nom = a - b
    den = h
    return round(nom / den, float_percision)