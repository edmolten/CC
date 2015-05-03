import math
from cc_lab2_I import *


def ErrorCalculation(ar,r):
    for i in range(len(ar)):
        ar[i] = abs(ar[i] - r)
    return ar

def LinealConv(error):
    lineal=[]
    for i in range(len(error)-1):
        lineal.append(error[i+1]/error[i])
    return lineal

def SuperLinealConv(error):
    sLineal=[]
    for i in range(len(error)-1):
        sLineal.append(error[i+1]/error[i]**((1.0 + math.sqrt(5))/2))
    return sLineal

def QuadraticConv(error):
    quad=[]
    for i in range(len(error)-1):
        quad.append(error[i+1]/error[i]**2)
    return quad
