from sys import *
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
