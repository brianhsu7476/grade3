import numpy as np

P=np.array([[0, 1, 0.5], [0, 0, 0.5], [1, 0, 0]])
v=np.array([1, 1, 1])
for i in range(10000):
	if i<10 or i==9999:
		print(i, v)
	v=np.dot(P, v)
