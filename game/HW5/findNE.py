from numpy import *
import matplotlib.pyplot as plt

n=int(input())
a=[0 for i in range(n)]
for i in range(n):
	a[i]=input().split()
a=[[int(j) for j in i] for i in a]
a=array(a)
xx=[i/100 for i in range(101)]
yy=[i/100 for i in range(101)]
for x in xx:
	for y in yy:
		c=['red', 'orange', 'yellow', 'green', 'blue', 'purple']
		mxid=0
		for i in range(1, n):
			if dot(a[i], [x, y, 1-x-y])>dot(a[mxid], [x, y, 1-x-y]):
				mxid=i
		plt.plot(x, y, color=c[mxid], marker='o', linestyle='none')
plt.show()
