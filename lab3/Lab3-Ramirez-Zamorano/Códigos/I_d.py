import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from I_c import *

puntos = get_puntos()
xs,ys,zs = get_componentes(puntos)

A = np.zeros((150,3))
A[:,0] = xs
A[:,1] = ys
A[:,2] = zs
print A
_,_,V = reduced_SVD(A)
vp1 = V[:,0]
vp2 = V[:,1]
vp3 = V[:,2]
print vp1
print vp2
print vp3

"""
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs,ys,zs)
incluir vectores!!!
plt.show()
"""
