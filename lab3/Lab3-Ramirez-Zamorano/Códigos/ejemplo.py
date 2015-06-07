#sudo apt-get install python-numpy

#http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.svd.html
#http://wiki.scipy.org/Tentative_NumPy_Tutorial

from numpy import *
A = array([[1,-1],[1,1],[1,1]])
print linalg.svd(A,False)
print "-------"
print linalg.svd(A)

#GG
