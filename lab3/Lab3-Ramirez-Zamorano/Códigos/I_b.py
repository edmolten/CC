import numpy as np

def full_SVD(A):
	U,s,V = np.linalg.svd(A)
	U = np.round(U,3)
	shape = A.shape
	m = shape[0]
	n = shape[1]
	S = np.zeros((m,n))
	S[:n,:n] = np.diag(np.round(s,3))
	V = np.round(V,3)
	return U, S, V
	
def exe_b():
	A = np.array([[1,1,1,1],[1,-1,1,1],[1,1,-1,1],[-1,-1,-1,1],[1,1,1,-1]])
	U, S, V = full_SVD(A)
	print "U = "
	print U
	print "Sigma = "
	print S
	print "V = "
	print V

#exe_b()
