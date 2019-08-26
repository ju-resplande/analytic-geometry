from Vector import Vector

vs = [
	Vector([1,1,1,1]),
	Vector([1,-1,1,-1]),
	Vector([1,1,-1,-1]),
	Vector([-1,1,1,-1])
     ]


print 'Question 1\n'

for i in range(len(vs)):
	for j in range(len(vs)):
		print vs[i], '+', vs[j], '=', vs[i] + vs[j]
	print '\n'

print 'Question 2\n'

for i in range(len(vs)):
	for j in range(len(vs)):
		print vs[i], '-', vs[j], '=', vs[i] - vs[j]
	print '\n'

print 'Question 3\n'

for i in range(len(vs)):
	for j in range(len(vs)):
		print vs[i], '*', vs[j], '=', vs[i] * vs[j]
	print '\n'

