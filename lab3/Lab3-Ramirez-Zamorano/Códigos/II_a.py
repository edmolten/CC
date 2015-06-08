import matplotlib.pyplot as plt

def get_datos():
	archivo_datos = open("Datasets/iris_dataset.txt", "r")
	datos = []
	for linea in archivo_datos:
		dato_str = linea.strip().split(" ")
		t = float(dato_str[0])
		sl = float(dato_str[1])
		sw = float(dato_str[2])
		pl = float(dato_str[3])
		pw = float(dato_str[4])		
		dato = [t,sl,sw,pl,pw]
		datos.append(dato)
	archivo_datos.close()
	return datos

def get_sepal_petal(datos):
	sls = []
	sws = []
	pls = []
	pws = []
	for dato in datos:
		sl = dato[1]
		sls.append(sl)
		sw = dato[2]
		sws.append(sw)
		pl = dato[3]
		pls.append(pl)
		pw = dato[4]
		pws.append(pw)
	return sls, sws, pls, pws

datos = get_datos()
sls, sws, pls, pws = get_sepal_petal(datos)
titulos = [" Sepal Lenght vs Sepal Width "," Petal Lenght vs Petal Width "]
caracteristicas = [[sls,sws],[pls,pws]]
for i in range(len(titulos)):
        print i
        plt.title(titulos[i])
        plt.plot(caracteristicas[i][0],caracteristicas[i][1],'go')
        plt.show()

