from randomVariable import *

a=[5, 6, 7, 6, 8]
x=[(a[i+1]-a[i])/a[i] for i in range(4)]
mu=avg(x)
sigma=sig1(x)
srd=(mu-0.01/252)/sigma
sry=sqrt(252)*srd
print(srd)
print(sry)
