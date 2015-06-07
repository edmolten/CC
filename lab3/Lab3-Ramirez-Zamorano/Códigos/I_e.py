import numpy as np
import matplotlib.pyplot as plt
#--------------------1---------------------

def reduced_SVD(A):
	U,S,V = np.linalg.svd(A,False)
	U = np.round(U,3)
	S = np.round(np.diag(S),3)
	V = np.round(V,3)
	return U, S, V

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

def get_Xm(X,m):
	U, S, V = reduced_SVD(X)
	shape = X.shape
	n = shape[0]
	p = shape[1]
	C = np.dot(U,S)
	D = V
	#m = int(n/2) #podria ser cualquier otro valor 1<=m<=p
	Cnm = C[:,:m]
	Dmp = D[:m,:]
	Xm = np.dot(Cnm,Dmp)
	return Xm



"""
print "X=" 
print X
print "Cnm="
print Cnm
print "Dmp="
print Dmp
print "Xm="
print Xm
"""

#--------------------2---------------------

def get_normas(X):
	p = X.shape[1]
	ms = [m for m in range(1,p+1)]
	normas = []
	for m  in ms:
		Xm = get_Xm(X,m)
		norma = np.linalg.norm(X - Xm) 
		normas.append(norma)
	return ms, normas
 
X = np.array(get_puntos())
ms, normas = get_normas(X) #toma unos segundos
plt.plot(ms, normas,'go')
plt.show() 

#-------------------3-----------------------





