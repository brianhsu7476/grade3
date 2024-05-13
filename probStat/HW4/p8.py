from math import *
frac=[1]
for i in range(1, 100):
	frac.append(frac[i-1]*i)
for n in range(1, 100):
	sm=0
	for i in range(5):
		sm+=(5/n)**i*exp(-5/n)/frac[i]
	if sm>0.9:
		print(n)
n=3
print(exp(-5/n))
