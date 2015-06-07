import I_a as I_a

def get_puntos():
	archivo_puntos = open("Datasets/data_set_X.txt", "r")
	puntos = []
	for linea in archivo_puntos:
		punto_str = linea.strip().split(" ")
		punto = []
		for componente in punto_str:
			punto.append(float(componente))
		puntos.append(punto)
	return puntos

print get_puntos()
