import math
from cc_lab2_I import *


def ErrorCalculation(ar,r):
    if(ar == None):
        return None
    error=[]
    for i in range(len(ar)):
        error.append(abs(ar[i] - r))
    return error

def LinealConv(error):
    if(error == None):
        return None
    lineal=[]
    for i in range(len(error)-1):
        lineal.append(error[i+1]/error[i])
    return lineal

def SuperLinealConv(error):
    if(error == None):
        return None
    sLineal=[]
    for i in range(len(error)-1):
        sLineal.append(error[i+1]/error[i]**((1.0 + math.sqrt(5))/2))
    return sLineal

def QuadraticConv(error):
    if(error == None):
        return None
    quad=[]
    for i in range(len(error)-1):
        quad.append(error[i+1]/error[i]**2)
    return quad

def printArreglo(ar):
    for i in ar:
        print i

def generarTabla(linealConv,superLinealConv,quadraticConv):
    for i in range(len(linealConv)):
        print str(linealConv[i]) + "  &  " + str(superLinealConv[i]) + "  &  " + str(quadraticConv[i]) + "  \\\\ \hline"

# para las funciones del item III

TOL = 0.000000001

# f1

f1 = sympify("(x**2)-6")
r1 = float(sqrt(6))
# Bisection for f1
bisectionf1 = Bisection(f1,-2.0,3.0,TOL)
errorbf1 = ErrorCalculation(bisectionf1,r1)
linealConvbf1 = LinealConv(errorbf1)
superLinealConvbf1 = SuperLinealConv(errorbf1)
quadraticConvbf1 = QuadraticConv(errorbf1)
# Newton for f1
newtonf1 = NewtonM(f1,0,15) 
errornf1 = ErrorCalculation(newtonf1,r1)
linealConvnf1 = LinealConv(errornf1)
superLinealConvnf1 = SuperLinealConv(errornf1)
quadraticConvnf1 = QuadraticConv(errornf1)

#f2

f2 = sympify("x**5-5*x**2+4")
r2 = 1
# Bisection for f2
bisectionf2 = Bisection(f2,0.5,1.5,TOL)
errorbf2 = ErrorCalculation(bisectionf2,r2)
linealConvbf2 = LinealConv(errorbf2)
superLinealConvbf2 = SuperLinealConv(errorbf2)
quadraticConvbf2 = QuadraticConv(errorbf2)
# Newton for f2
newtonf2 = NewtonM(f2,2,15)
errornf2 = ErrorCalculation(newtonf2,r2)
linealConvnf2 = LinealConv(errornf2)
superLinealConvnf2 = SuperLinealConv(errornf2)
quadraticConvnf2 = QuadraticConv(errornf2)

#f3

f3 = sympify("x**4-6*x**3+12*x**2-10*x+3")
r3 = 3
# Bisection for f3
bisectionf3 = Bisection(f3,0.0,4.0,TOL)
errorbf3 = ErrorCalculation(bisectionf3,r3)
linealConvbf3 = LinealConv(errorbf3)
superLinealConvbf3 = SuperLinealConv(errorbf3)
quadraticConvbf3 = QuadraticConv(errorbf3)
# Newton for f3
newtonf3 = NewtonM(f3,2.5,15)
errornf3 = ErrorCalculation(newtonf3,r3)
linealConvnf3 = LinealConv(errornf3)
superLinealConvnf3 = SuperLinealConv(errornf3)
quadraticConvnf3 = QuadraticConv(errornf3)

#f4

f4 = sympify("exp(x**2)*x")
r4 = 0
# Bisection for f4
bisectionf4 = Bisection(f4,1.0,2.0,TOL)
errorbf4 = ErrorCalculation(bisectionf4,r4)
linealConvbf4 = LinealConv(errorbf4)
superLinealConvbf4 = SuperLinealConv(errorbf4)
quadraticConvbf4 = QuadraticConv(errorbf4)
# Newton for f4
newtonf4 = NewtonM(f4,1,15)
errornf4 = ErrorCalculation(newtonf4,r4)
linealConvnf4 = LinealConv(errornf4)
superLinealConvnf4 = SuperLinealConv(errornf4)
quadraticConvnf4 = QuadraticConv(errornf4)
