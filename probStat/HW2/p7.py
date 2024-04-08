from math import *
frac=[1]
for i in range(1, 100):
	frac.append(frac[i-1]*i)
ans=0
for i in range(7):
	ans+=10**i*exp(-10)/frac[i]
print(ans)
