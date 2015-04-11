from math import sin, cos

def sec(x):
    return 1.0/cos(x)

def tan(x):
    return sin(x)/cos(x)

def y(x):
    return (1.0 - sec(x))/((tan(x))**2)

for t in range(1,21):
    print "y(10^(-" ,t,")) = " , y(10.0**(-t))
