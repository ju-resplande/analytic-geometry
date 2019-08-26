from Matrix import *
from ArquivoN01 import *

for i in range(4):
	for j in range(4):
		print "D%d%d" %(i,j)
		D = A[i]*A[j] - A[j]*A[i]
		print D