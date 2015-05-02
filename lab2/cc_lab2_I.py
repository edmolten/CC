from sympy import *

x = symbols("x")

# Bisection method

def Bisection(f,a,b,TOL):
    f = sympify(f)
    if (f.subs(x,a)*f.subs(x,b) >= 0):
        print "Esta funcion no cumple con requisitos de Bisection Method"
    c = (a+b)/2
    while((b-a)/2 > TOL):
        c = (a+b)/2
        if(f.subs(x,c) == 0):
            return c
        if (f.subs(x,a)*f.subs(x,b) < 0):
            b=c
        else:
            a=c
    return c

# Secant method --- revisar ---

def SecantM(f,X_0,X_1,n):
    f = sympify(f)
    pre = X_1
    past = X_0
    for i in range(n):
        fut = pre - (f.subs(x,pre) * (pre - past))/(f.subs(x,pre) - f.subs(x,past))
        print fut
        if (pre == fut):
            return pre
        past = pre
        pre = fut
    return fut


# Fixed Point method

def FixedPoint(f,X_0,n):
    f = sympify(f)
    past = X_0
    for i in range(n):
        pre = f.subs(x,past)
        print pre
        if (pre == past):
            return pre
        past = pre
    return pre

# Newton method

def NewtonM(f,X_0,n):
    f = sympify(f)
    past = X_0
    for i in range(n):
        pre = past - f.subs(x,past)/diff(f,x).subs(x,past)
        print pre
        if (pre == past):
            return pre
        past = pre
    return pre
    
