import numpy as np

def reduced_SVD(A):
	U,S,V = np.linalg.svd(A,False)
	U = np.round(U,3)
	S = np.round(np.diag(S),3)
	V = np.round(V,3)
	return U, S, V

def exe_a():
	A = np.array([[1,1,1,1],[1,-1,1,1],[1,1,-1,1],[-1,-1,-1,1],[1,1,1,-1]])
	U, S, V = reduced_SVD(A)
	print "U = "
	print U
	print "Sigma = "
	print S
	print "V = "
	print V

#exe_a()
