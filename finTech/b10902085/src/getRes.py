from sys import *
from numpy import *
a, b=[], []
for line in stdin:
	if ',' in line:
		b=[float(i) for i in line.split(',')]
	else:
		b=[float(line.split('=')[1][:-2])]+b
		a.append(b)
		b=[]
a.sort(reverse=True)
for i in range(30):
	print(a[i])

c=[i[0] for i in a[:len(a)//4]]
print(mean(c))
print(std(c))
