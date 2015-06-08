import matplotlib.pyplot as plt
import numpy as np
from I_a import reduced_SVD

def get_puntos():
	archivo_puntos = open("Datasets/data_set_elipse.txt", "r")
	puntos = []
	for linea in archivo_puntos:
		punto_str = linea.strip().split(" ")
		x = float(punto_str[0])
		y = float(punto_str[1])
		z = float(punto_str[2])
		punto = [x,y,z]
		puntos.append(punto)
	archivo_puntos.close()
	return puntos

def get_componentes(puntos):
	xs = []
	ys = []
	zs = []
	for x,y,z in puntos:
		xs.append(x)
		ys.append(y)
		zs.append(z)
	return xs, ys, zs

def exe_c():
	puntos = get_puntos()
	xs,ys,_ = get_componentes(puntos)
	A = np.zeros((150,2))
	A[:,0] = xs
	A[:,1] = ys
	print A
	_,_,V = reduced_SVD(A)
	vp1 = V[:,0]
	vp2 = V[:,1]
	print vp1
	print vp2
	vxs = [vp1[0],vp2[0]]
	vys = [vp1[1],vp2[1]]
	plt.plot(xs,ys,'go')
	plt.quiver(0,0,vxs,vys)
	plt.show()

exe_c()

