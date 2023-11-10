import numpy as np
import cvxpy as cp
from random import *
from scipy.special import xlogy
from numpy import log
import matplotlib.pyplot as plt

T=30

def BA(P):
	n, m=len(P), len(P[0])
	p, q=[], []
	xx, yy=[], [[] for i in range(n+1)]
	for t in range(T):
		pd=[]
		if t==0:
			pd=[random() for i in range(n)]
		else:
			pd=[1]*n
			for i in range(n):
				for j in range(m):
					pd[i]*=q[j][i]**P[i][j]
		sm=sum(pd)
		p=[i/sm for i in pd]
		xx.append(t)
		for i in range(n):
			yy[i].append(p[i])
		q=[]
		for j in range(m):
			pd=[p[k]*P[k][j] for k in range(n)]
			sm=sum(pd)
			q.append([i/sm for i in pd])
		C=sum([sum([xlogy(p[i]*P[i][j]/log(2), q[j][i]/p[i]) for j in range(m)]) for i in range(n)])
		yy[n].append(C)
	print(p)
	print(C)
	for i in range(n):
		plt.plot(xx, yy[i], label='$p_'+str(i)+'$ (BA)')
	plt.plot(xx, yy[n], label='capacity (BA)')
	plt.xlabel('$t$ (number of rounds)')
	plt.ylabel('value')

def general(P):
	n, m=len(P), len(P[0])
	p=cp.Variable(shape=n)
	q=P@p
	C=cp.sum(cp.entr(q)/log(2))+cp.sum([p[i]*sum([xlogy(P[i][j]/log(2), P[i][j]) for j in range(m)]) for i in range(n)])
	prob=cp.Problem(cp.Maximize(C), [cp.sum(p)==1, p>=0])
	prob.solve()
	print(p.value)
	print(prob.value)
	xx, yy=[], [[] for i in range(n+1)]
	for t in range(T):
		xx.append(t)
		for i in range(n):
			yy[i].append(p.value[i])
		yy[n].append(prob.value)
	for i in range(n):
		plt.plot(xx, yy[i], label='$p_'+str(i)+'$ (cvxpy)')
	plt.plot(xx, yy[n], label='capacity (cvxpy)')

seed(77777144949)

p=0.3
P=[[1-p, p], [p, 1-p]]
general(P)
BA(P)
plt.legend(loc='best')
plt.savefig('symmetric.png')
plt.show()

n, m=5, 5
p=0.3
P=[[1-p if i==j else p/(n-1) for j in range(m)] for i in range(n)]
print(np.array(P))
general(P)
BA(P)
plt.legend(loc='best')
plt.savefig('symmetric2.png')
plt.show()

p=0.3
P=[[1-p, p, 0], [0, p, 1-p]]
general(P)
BA(P)
plt.legend(loc='best')
plt.savefig('erasure.png')
plt.show()

n, m=5, 6
p=0.3
P=[[1-p if j==i else p if j==m-1 else 0 for j in range(m)] for i in range(n)]
print(np.array(P))
general(P)
BA(P)
plt.legend(loc='best')
plt.savefig('erasure2.png')
plt.show()
