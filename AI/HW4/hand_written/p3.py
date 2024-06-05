import numpy as np

def nxt(X, Mu):
	cnt=[[] for i in Mu]
	err=0
	for x in X:
		i=np.argmin([np.linalg.norm(x-mu) for mu in Mu])
		cnt[i].append(x)
		err+=np.linalg.norm(x-Mu[i])**2
	print(err/len(x))
	print(cnt)
	res=np.array([np.mean(cnt[i], axis=0) if len(cnt[i]) else Mu[i] for i in range(len(cnt))])
	return res

X=np.array([[1, 2], [3, 4], [7, 0], [10, 2]])
Mu=np.array([[1, 2], [3, 4]])
for i in range(10):
	print(Mu)
	Mu=nxt(X, Mu)

print('-'*40)

#X=np.array([[1, 2], [3, 4], [7, 0], [10, 2]])
Mu=np.array([[1, 2], [7, 0]])
for i in range(10):
	print(Mu)
	Mu=nxt(X, Mu)

print('-'*40)

X=np.array([[1, 2], [3, 4], [5, 6], [7, 0], [10, 2]])
Mu=np.array([[1, 2], [3, 4]])
for i in range(10):
	print(Mu)
	Mu=nxt(X, Mu)

print('-'*40)

X=np.array([[1, 2], [3, 4], [5, 6], [7, 0], [10, 2]])
Mu=np.array([[1, 2], [7, 0]])
for i in range(10):
	print(Mu)
	Mu=nxt(X, Mu)


