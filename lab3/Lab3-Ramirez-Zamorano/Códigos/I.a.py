from numpy import array, linalg, round, diag
A = array([[1,1,1,1],[1,-1,1,1],[1,1,-1,1],[-1,-1,-1,1],[1,1,1,-1]])
U,S,V = linalg.svd(A,False)
U = round(U,3)
S = round(diag(S),3)
V = round(V,3)
print "U = "
print U
print "Sigma = "
print S
print "V = "
print V

