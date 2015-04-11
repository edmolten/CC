from math import log, floor, sin

# (a)
def epsilon(fl):
    exp = floor(log(float(fl),2))
    return abs((2.0**(exp+1) - 2.0**(exp)) / 2.0**(52))

print epsilon(1)

# (b)
import matplotlib.pyplot as plt

plt.plot([1,2],[3,4])
plt.show()
