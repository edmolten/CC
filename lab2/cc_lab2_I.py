from sympy import *

x = symbols("x")

# Bisection method

def Bisection(f,a,b,TOL):
    ar =[]
    f = sympify(f)
    if (f.subs(x,a)*f.subs(x,b) >= 0):
        print "Esta funcion no cumple con requisitos de Bisection Method"
        return None
    c = (a+b)/2
    while((b-a)/2 > TOL):
        c = (a+b)/2
        ar.append(c)
        if(f.subs(x,c) == 0):
            return ar
        if (f.subs(x,a)*f.subs(x,b) < 0):
            b=c
        else:
            a=c
    return ar

# Secant method

def SecantM(f,X_0,X_1,n):
    f = sympify(f)
    a =[]
    pre = X_1
    past = X_0
    for i in range(n):
        fut = pre - (f.subs(x,pre) * (pre - past))/(f.subs(x,pre) - f.subs(x,past))
        print fut
        a.append(fut)
        if (f.subs(x,fut) == 0):
            return a
        past = pre
        pre = fut
    return a


# Fixed Point method

def FixedPoint(f,X_0,n):
    f = sympify(f)
    a =[]
    past = X_0
    for i in range(n):
        pre = f.subs(x,past)
        print pre
        a.append(pre)
        if (pre == past):
            return a
        past = pre
    return a

# Newton method

def NewtonM(f,X_0,n):
    f = sympify(f)
    a =[]
    past = X_0
    for i in range(n):
        pre = past - f.subs(x,past)/diff(f,x).subs(x,past)
        print pre
        a.append(pre)
        if (f.subs(x,pre) == 0):
            return a
        past = pre
    return a

# modified Newton method

def NewtonMod(f,X_0,m,n):
    f = sympify(f)
    a =[]
    past = X_0
    for i in range(n):
        pre = past - m * f.subs(x,past)/diff(f,x).subs(x,past)
        print pre
        a.append(pre)
        if (f.subs(x,pre) == 0):
            return a
        past = pre
    return a
