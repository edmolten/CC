from math import sin, cos
from decimal import Decimal

def sec(x):
    return 1.0/cos(x)

def tan(x):
    return sin(x)/cos(x)

def y(x):
    return (1.0 - sec(x))/((tan(x))**2)

def y1(x):
    return (-1.0)/(1 + sec(x))

def y2(x):
    return (-cos(x))/(1 + cos(x))


for t in range(1,21):
    print "y(10^(-" ,t,")) = " , Decimal(y(10.0**(-t)))

for t in range(1,21):
    print "y1(10^(-" ,t,")) = " , Decimal(y1(10.0**(-t)))

    
for t in range(1,21):
    print "y2(10^(-" ,t,")) = " , Decimal(y2(10.0**(-t)))

for t in range(1,21):
    print "error relativo para t=",t," -> " , Decimal(abs(y(10.0**(-t)) - y1(10.0**(-t)))/abs(y1(10.0**(-t))))

for t in range(1,21):
    print "error relativo para t=",t," -> " , Decimal(abs(y(10.0**(-t)) - y2(10.0**(-t)))/abs(y2(10.0**(-t))))
