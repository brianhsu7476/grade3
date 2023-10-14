from sys import *
mx=0
ms, ml, ma, mb=0, 0, 0, 0
for line in stdin:
	if ',' in line:
		s, l, a, b=line.split(',')
		s, l, a, b=float(s), float(l), float(a), float(b)
	else:
		res=float(line.split('=')[1][:-2])
		if res>mx:
			ms, ml, ma, mb=s, l, a, b
			mx=res
print(ms, ml, ma, mb, mx)
