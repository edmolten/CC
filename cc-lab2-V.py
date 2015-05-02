from sympy import *
from math import pi

#Solo funciona con expresiones de una variable "x"
def eva(f,x_value):
    """
    Evalua la funcion f en x_value. f debe ser una expresion sympy y x_value puede ser un
    numero o un simbolo
    """
    x = symbols("x")
    return f.subs(x,x_value)

def D(f,x0):
    x = symbols("x")
    return eva(diff(f,x),x0)

def D2(f,x0):
    x = symbols("x")
    return eva(diff(diff(f,x),x),x0)

def getF(f,x0,x):
    c = symbols("c")
    x = symbols("x")
    f = sympify(f)
    F = eva(f,x) - eva(f,x0) - D(f,x0)*(x - x0) - D2(f,c)*((x - x0)**2)/ 2
    return F.subs(c,x) #cambia las c por x, para compatibilidad con funcion eva

def BiseccionSymPy(f,a,b):
    TOL = 0.00000001
    c = (b+a)/2
    while (b - a)/2 > TOL: 
        c = (b+a)/2
        if eva(f,0) == 0:
            return c
        if eva(f,a)*eva(f,c) > 0:
            a = c
        else:
            b = c
    return c

def getC(f,x0,x):
    F = getF(f,x0,x)
    return BiseccionSymPy(F,0,pi)

f = "cos(x)"
print getC(f,pi/2,pi)
