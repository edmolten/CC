import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_puntos_3D():
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

def get_componentes_3D(puntos):
	xs = []
	ys = []
	zs = []
	for x,y,z in puntos:
		xs.append(x)
		ys.append(y)
		zs.append(z)
	return xs, ys, zs

puntos = get_puntos_3D()
xs,ys,zs = get_componentes_3D(puntos)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs,ys,zs)
plt.show()
