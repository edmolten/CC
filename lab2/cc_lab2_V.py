from sympy import *
from cc_lab2_I import *
from math import pi

#------------------------(1)-------------------------------------

#Solo funciona con expresiones de una variable "x"
def eva(f,x_value):
    """
    Evalua la funcion f en x_value. f debe ser una expresion valida
    y x_value puede ser un numero o un simbolo
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

def getC(f,x0,x):
    TOL = 0.00000001
    F = getF(f,x0,x)
    return Bisection(F,0,pi,TOL)

f = sympify("cos(x)")
print getC(f,pi/2,pi)

#-------------------------(2)-----------------------------------

xs = []
inc = (0.8 + 0.75) / 100
init = 0.8
for i in range(0,100):
   xs.append(init)
   
   
    
print xs
