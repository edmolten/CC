from cc_lab2_I import *
from math import pi

TOL = 0.000000001

f1 = sympify("(x**2)-6")
print Bisection("(x**2)-6",-2.0,3.0,TOL)
print NewtonM(f1,0,15)

f2 = sympify("x**5-5*x**2+4")
print Bisection("x**5-5*x**4+4",0.5,1.5,TOL)
print NewtonM(f2,2,15)

f3 = sympify("x**4-6*x**3+12*x**2-10*x+3")
print Bisection("x**4-6*x**3+12*x**2-10*x+3",0.0,4.0,TOL)
print NewtonM(f3,2.5,15)

f4 = sympify("exp(x**2)*x")
print Bisection("exp(x**2)*x",1.0,2.0,TOL)
print NewtonM(f4,1,15)

#mm = "((2*(1-16*x**2)**(1/2))/((1-16*x**2)**(1/2)-1-8*x**2))**(1/2)"
m = sympify("((2*(1-16*x**2)**(1/2))/((1-16*x**2)**(1/2)-1-8*x**2))**(1/2)")
#print m
#K = mpmath.ellipk(m)# no funciona, solo recibe numeros...
#numerador = sympify("pi*(2+16*x**2-2*(1-16*x**2)**(1/2))**(1//2)")
#f5 = ( numerador / K ) - 2
#print f5
