from Matrix import *
from ArquivoN01 import *

for i in range(4):
	P = 1

	for j in range(4):
		P *= A[i]

		print "P%d de %d" %(j,i)
		print P

	print "\n\n"