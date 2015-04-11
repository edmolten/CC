from math import log, floor, sin

# (a)
def epsilon(fl):
    exp = floor(log(float(fl),2))
    return abs((2.0**(exp+1) - 2.0**(exp)) / 2.0**(52))

# (b)

from matplotlib import pyplot

x = []
for i in range(-50,51):
    x.append(2.0**(i))

pyplot.plot(x, [epsilon(i) for i in x])
pyplot.show()    
