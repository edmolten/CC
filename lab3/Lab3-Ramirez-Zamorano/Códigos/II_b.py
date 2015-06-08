from II_a import get_datos, get_sepal_petal
from I_b import full_SVD
from numpy import *
import numpy as np


def sepal_matrix(matrix):
    sepal = zeros((len(matrix),4))
    for i in range(len(matrix[0])): # recorriendo columnas
        for k in range(len(matrix)): # recorriendo filas
            if(i<2):
                sepal[k,i] = matrix[k,i+1]
    return sepal

def petal_matrix(matrix):
    petal = zeros((len(matrix),4))
    for i in range(len(matrix[0])): # recorriendo columnas
        for k in range(len(matrix)): # recorriendo filas
            if(i>=2 and i<4):
                petal[k,i] = matrix[k,i+1]
    return petal

datos = get_datos()
sls, sws, pls, pws = get_sepal_petal(datos)
titulos = [" Sepal Lenght vs Sepal Width "," Petal Lenght vs Petal Width "]
datos = array(datos)


miu = []
for i in range(len(datos[0])): 
    miu.append(np.mean(datos[0:len(datos), i]))

for i in range(len(datos[0])): # recorriendo columnas
    for k in range(len(datos)): # recorriendo filas
        datos[k,i] = datos[k,i] - miu[i]


sepal = sepal_matrix(datos)
petal = petal_matrix(datos)

Us, Ss, Vs = full_SVD(sepal[0:len(sepal),0:2])
Up, Sp, Vp = full_SVD(petal[0:len(petal),2:4])





