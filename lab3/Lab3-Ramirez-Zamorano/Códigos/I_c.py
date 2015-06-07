import matplotlib.pyplot as plt

def get_puntos_2D():
	archivo_puntos = open("Datasets/data_set_elipse.txt", "r")
	puntos = []
	for linea in archivo_puntos:
		punto_str = linea.strip().split(" ")
		x = float(punto_str[0])
		y = float(punto_str[1])
		punto = [x,y]
		puntos.append(punto)
	archivo_puntos.close()
	return puntos

def get_componentes_2D(puntos):
	xs = []
	ys = []
	for x,y in puntos:
		xs.append(x)
		ys.append(y)
	return xs, ys

puntos = get_puntos_2D()
xs,ys = get_componentes_2D(puntos)
plt.plot(xs,ys,'go')
plt.show()

