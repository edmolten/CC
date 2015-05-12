from sympy import *

#----------------(2)-----------------

def NewFixedPoint(g,r,X_0,n):
    x = symbols("x")
    g = sympify(g)
    dg = diff(g,x)
    dgr = dg.subs(x,r)
    M = dgr / (dgr - 1)
    G = g + M * (x - g)
    print G
    past = X_0
    for i in range(n):
        pre = G.subs(x,past)
        print pre
        if (pre == past):
            return pre
        past = pre
    return pre

print NewFixedPoint("exp(2*x)-1",1.0,2.0,50)
