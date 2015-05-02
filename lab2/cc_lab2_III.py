from cc_lab2_I import *
from math import pi

f = sympify("cos(x)")
print Bisection(f,0,pi,0.0000000001)
