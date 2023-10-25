from numpy import *
from scipy.optimize import *

def maximin(pi):
	return max([min(i) for i in pi])
def minimax(pi):
	return min([max([i[j] for i in pi]) for j in range(len(pi[0]))])
def strategy(pi, v):
	n, m=len(pi), len(pi[0])
	A=list(transpose(-array(pi)))
	b=[-v]*m+[1, -1]
	A.append([1]*n)
	A.append([-1]*n)
	pbd=[(0, 1)]*n
	c=[1]*n
	return linprog(c=c, A_ub=A, b_ub=b, bounds=pbd, method='highs-ds')

n=int(input())
atk1=[int(i) for i in input().split()]
atk2=[int(i) for i in input().split()]
pi=[[0 if i==j or (i-j+n)%n==n/2 else atk1[i] if (i-j+n)%n<n/2 else -atk2[j] for j in range(n)] for i in range(n)]

print(array(pi))
#print(maximin(pi))
#print(minimax(pi))
l, r, eps=maximin(pi), minimax(pi), 1e-12
ans=[0]*n
while r-l>eps:
	v=(l+r)/2
	res=strategy(pi, v)
	if res.status==0:
		l=v
		ans=res.x
	else:
		r=v
print(l, ans)
